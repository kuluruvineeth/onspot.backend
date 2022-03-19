from darkflow.net.build import TFNet
import cv2

# model, pbLoad, metaLoad : give your local paths.
options = {"model": "/var/www/html/onspot/onspot_backend/backend/darkflow/cfg/yolov2-tiny-voc-1c.cfg",
               "pbLoad": "/var/www/html/onspot/onspot_backend/backend/darkflow/built_graph/yolov2-tiny-voc-1c.pb",
               "metaLoad": "/var/www/html/onspot/onspot_backend/backend/darkflow/built_graph/yolov2-tiny-voc-1c.meta",
               "threshold": 0.2}

tfnet = TFNet(options)

# test image
imgcv = cv2.imread("<INPUT-IMAGE-PATH>")
print(imgcv)
result = tfnet.return_predict(imgcv)
print(result)

for item in result:
    imgcv = cv2.rectangle(imgcv, (item["topleft"]["x"], item["topleft"]["y"]), (item["bottomright"]["x"], item["bottomright"]["y"]), (0, 255, 0), 4)
    text_x, text_y = item["topleft"]["x"] - 10, item["topleft"]["y"] - 10
    imgcv = cv2.putText(imgcv, item["label"], (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imwrite("<OUTPUT-IMAGE-PATH>", imgcv) # location to save output image.
