import cv2
import numpy as np

img=cv2.imread('C://for_anaconda/horse.jpg')
height, width, channel=img.shape
print('original image shape:', height, width, channel)

blob=cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
print('blob shape::', blob.shape)

with open ("C://for_anaconda/coco.names", "r") as f:
    classes=[line.strip() for line in f.readline()]

net=cv2.dnn.readNetFromDarknet('C://for_anaconda/yolov3.cfg', 'C://for_anaconda/yolov3.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

layer_names=net.getLayerNames()
output_layers=[layer_names[i-1] for i in net.getUnconnectedOutLayers()]
print(output_layers)

net.setInput(blob)
outs=net.forward(output_layers)
print('shape of the first output:', outs[0].shape)
print(outs[0][0,:5])

class_ids=[]
confidence_scores=[]
boxes=[]
new_var=[]

for out in outs:
    for detection in out:
        scores=detection[5:]
        class_id=np.argmax(scores)
        confidence=scores[class_id]
        if confidence>0.5:
            center_x=int(detection[0]*width)
            center_y=int(detection[0]*height)
            w=int(detection[2]*width)
            h=int(detection[3]*height)
            x=int(center_x-w/2)
            y=int(center_y-h/2)
            
            boxes.append([x, y, w, h])
            confidence_scores.append(float(confidence))

            class_ids.append(class_id)


            

print('number of dectected objects=', len(boxes))

indices=cv2.dnn.NMSBoxes(boxes, confidence_scores, 0.5, 0.4)
print('number of final objects=', len(indices))

colors=np.random.uniform(0, 255, size=(len(classes),3))
font=cv2.FONT_HERSHEY_PLAIN
j=0
for i in range(len(boxes)):
    if i in indices:
        x, y, w, h= boxes[i]
        label=str(classes[class_ids[i]])
        print(f'class{label} detected at {x}, {y}, {w}, {h}')
        color=colors[i]
        cv2.rectangle(img, (x+30, y+30), (x+w+100, y+h+100), color, 20)
        cv2.putText(img, label, (x, y-10), font, 2, color, 2)



        a=[label, w,h]
        new_var.append(a)
        j=j+1


print(new_var)
cv2.imshow('Objects', img)
cv2.waitKey()
cv2.destroyAllWindows()








