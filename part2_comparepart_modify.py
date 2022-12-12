import cv2
import getinfo_print_name_not_print_photo as info
from collections import Counter

check=0
leng=len(info.new_var)
cnt = 1
printed=0
sum_data=[]

for i in range(leng):
    w=info.new_var[i][1]
    h=info.new_var[i][2] #i번째 사진의 가로, 세로
    totalArea = w*h
    if totalArea >= info.width*info.height*70/100: # 하나의 객체가 전체 이미지 크기의 70% 이상일 때
        print('이 사진은', info.new_var[i][0], ' 을(를) 중점으로 찍은 사진이다.') 
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

        # car 또는 bus 또는 truck 또는 traffic light 중 한 종류의 이미지 크기 총합이
        # 전체 크기의 70% 이상이면, 해당 이미지가 driveway 사진이라고 출력.
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


cv2.imshow('Objects', info.img)
cv2.waitKey()
cv2.destroyAllWindows()