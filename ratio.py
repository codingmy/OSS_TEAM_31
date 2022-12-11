import cv2
import numpy as np
import getinfo_print_name as info

 
info.img = cv2.imread('C://for_anaconda/horse.jpg')
#이미지의 가로, 세로, 채널 수 가져오기
info.height, info.width, info.channel = info.img.shape 

info.net = cv2.dnn.readNetFromDarknet('C://for_anaconda/yolov3.cfg', 'C://for_anaconda/yolov3.weights')
info.new_var = []

with open("C://for_anaconda/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
print('number of classes =', len(classes))

info.blob = cv2.dnn.blobFromImage(info.img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
info.net.setInput(info.blob)
info.outs = info.net.forward(info.output_layers)

print('original image shape: ', info.height, info.width, info.channel)



for i in range(info.new_var):
    info.img_width[i] = info.new_var[i][1]
    info.img_height[i] = info.new_var[i][2]

presentArea = []
ratio=[]
info.class_ids=[]

totalArea = info.height * info.width
for i in range(info.new_var):
    presentArea[i] = info.height[i] * info.width[i]
    ratio[i] = presentArea[i]/totalArea*100
    if(ratio[i]>=70):
        print('이 사진은', info.class_ids[i], '중점으로 찍은 사진이다.')
        break


cv2.imshow("Image", info.img)
cv2.waitKey()
