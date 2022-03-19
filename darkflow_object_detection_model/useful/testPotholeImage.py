import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# give respective local path locations of the trained model.
options = {
	"model": "/var/www/html/onspot/onspot_backend/backend/darkflow/cfg/yolov2-tiny-voc-1c.cfg",
    "pbLoad": "/var/www/html/onspot/onspot_backend/backend/darkflow/built_graph/yolov2-tiny-voc-1c.pb",
    "metaLoad": "/var/www/html/onspot/onspot_backend/backend/darkflow/built_graph/yolov2-tiny-voc-1c.meta",
    "load": 5500,
	"threshold": 0.1
}

tfnet = TFNet(options)

# input image
img = cv2.imread('<INPUT-IMAGE-PATH>', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

result = tfnet.return_predict(img)
print ("Result length: "+str(len(result)))

# counter for iterating over result
counter=0

while counter<len(result):
	tl = (result[counter]['topleft']['x'], result[counter]['topleft']['y'])
	br = (result[counter]['bottomright']['x'], result[counter]['bottomright']['y'])

	label = result[counter]['label']
	confidence = result[counter]['confidence']

	print (tl, br, label, confidence)

	img = cv2.rectangle(img, tl, br, (0,255,0), 2)
	percentageConfidence = round(confidence*100,2)
	img = cv2.putText(img, label+": "+str(percentageConfidence)+"%", tl,cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 4)
	#img = cv2.putText(img, label, tl,cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 4)
	counter=counter+1

plt.imsave("<OUTPUT-IMAGE-PATH>", img) # dave output image
