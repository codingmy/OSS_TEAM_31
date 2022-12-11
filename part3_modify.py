import cv2

import getinfo_print_name_not_print_photo as info

check=0
leng=len(info.new_var)
print(leng)
for i in range(leng):
    w=info.new_var[i][1]
    h=info.new_var[i][2]
    if w*h >= info.width*info.height*70/100:
        print('이 사진은', info.new_var[i][0], '중점으로 찍은 사진이다.')
        check=1
        break

cv2.imshow('Objects', info.img)
cv2.waitKey()
cv2.destroyAllWindows()