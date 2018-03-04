#%%

# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

#Firebase Libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
 

imageA = cv2.imread('0.jpg')
imageB = cv2.imread('5.jpg')
 
# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))



#Firebase srevice Authentication
cred = credentials.Certificate("servicekey.json")
firebase_admin.initialize_app(cred)

#Applying thresholds
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# print("Number of cars in parking: %d" % len(cnts))
# f=18
# b= len(cnts)
# c= f-b
# print("Number of Vacant spce: %d" %c)


for c in cnts:
    	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
    
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    

# print("Number of cars in parking: %d" % len(cnts))
f =18
b = len(cnts)
c = f-b
print("Number of Vacant space: %d" %c)
print("Number of cars in slot: %d" %b)

#Firebase Data Save
data = {
    u'freespace' : c,
  	u'No. of cars in slot' : b

}

db = firestore.client()

db.collection(u'slots').document(u'available space').set(data)

# show the output images
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

