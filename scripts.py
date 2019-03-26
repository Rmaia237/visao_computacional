import cv2

image = cv2.imread("/home/ime/Imagens/stitch.png",10)
print(type(image))
cv2.imshow("img",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------

import numpy as np
import cv2
img = np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(511,511),(255,255,255),5) # \
cv2.line(img,(0,255),(511,255),(255,255,255),5) # horizontal
cv2.line(img,(0,511),(511,0),(255,255,255),5) # /
cv2.line(img,(255,0),(255,511),(255,255,255),5) # vertical
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------

import numpy as np
import cv2
img = np.zeros((512,512,3),np.uint8)
cv2.line(img,(73,73),(436,436),(255,255,255),5) # \
cv2.line(img,(0,255),(511,255),(255,255,255),5) # horizontal principal
cv2.line(img,(73,436),(436,73),(255,255,255),5) # /
cv2.line(img,(255,0),(255,511),(255,255,255),5) # vertical principal

cv2.line(img,(255,0),(73,436),(255,255,255),5)
cv2.line(img,(255,0),(436,436),(255,255,255),5)

cv2.line(img,(255,511),(73,73),(255,255,255),5)
cv2.line(img,(255,511),(436,73),(255,255,255),5)

cv2.line(img,(0,255),(436,73),(255,255,255),5)
cv2.line(img,(0,255),(436,436),(255,255,255),5)

cv2.line(img,(511,255),(73,73),(255,255,255),5)
cv2.line(img,(511,255),(73,436),(255,255,255),5)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#--------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,5,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()

#----------------------

import numpy as np
import matplotlib.pyplot as plt

w=10
h=10
fig=plt.figure(figsize=(8,8))
columns=4
rows=5
for i in range(1,columns*rows +1):
    img = np.random.randint(10,size=(h,w))
    fig.add_subplot(rows,columns,i)
    plt.imshow(img)
plt.show()

#------------------

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/home/ime/Imagens/stitch.png",10)
plt.imshow(img,cmap="gray",interpolation="bicubic")
plt.xticks([]),plt.yticks([])
plt.show()

#-----------------

