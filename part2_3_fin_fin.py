import cv2
import part1_fin as info
from collections import Counter

check=0
leng=len(info.new_var)
cnt = 1
printed=0
sum_data=[]

for i in range(leng):
    w=info.new_var[i][1]
    h=info.new_var[i][2] #horizontal and vertical lengths in the i-th picture
    totalArea = w*h
    if totalArea >= info.width*info.height*70/100: # if one object is more than 70% of the total image size
        print('This picture is an image that focuses on', info.new_var[i][0]) 
        check=1
        break
    else:
        for j in range(len(sum_data)):
            
            if info.new_var[i][0] in sum_data[j]:
                index=j
                sum=sum_data[index][1]
                sum=sum+totalArea
                sum_data[index][1]=sum
                break
        else:

            thing_list=[info.new_var[i][0], totalArea]
            sum_data.append(thing_list)
        
            
for i in range(len(sum_data)):
    if check==0 and sum_data[i][1] >= info.width*info.height*70/100:

        # To determine the image based on the context
        # if the sum of the image size of either 'car' or 'bus' or 'truck' or 'traffic light' is more than 70% of the total size, the image is printed as a 'driveway picture'. etc...
        if sum_data[i][0] in ( 'car' , 'bus', 'truck', 'traffic light'):
            print('driveway picture')
        elif sum_data[i][0] in 'book':
            print('bookstore picture')
        elif sum_data[i][0] in ('person', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'zebra', 'giraffe', 'mouse'):
            print('flock picture')
        else:
            print(sum_data[i][0], 'picture')

        printed=1
        break


if printed==0 and check==0:
    print('There are ', end=' ')
    for i in range(len(sum_data)):
        if i!=0:
            print(',', end=' ')
        print(sum_data[i][0],'(s)', end=' ')
    print(' in this picture.')

cv2.imshow('Objects', info.img)
cv2.waitKey()
cv2.destroyAllWindows()
