
import cv2
import numpy as np
from obect_tracker import *
import objtracking as oj
import contour_detect as cd

COLORS = None
classes = None

trackObject = oj.ObjTracking()


def get_output_layers(net):
    layer_names = net.getLayerNames()

    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    if (label == 'car'):
        color = COLORS[class_id]

        cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)

        cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        box = [x, y, x_plus_w, y_plus_h]
        o_id = trackObject.calc_centroid(box)
        if (o_id > -1):
            idObject = str(o_id)
            # print(idObject + " ", (x - 10, y - 20))
            cv2.putText(img, idObject, (x - 10, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imm = imgray[y:y_plus_h, x:x_plus_w]
            obj_Dict[o_id].frame = imm



def getObject(image, net, scale):
    super
    trackObject
    Width = image.shape[1]
    Height = image.shape[0]

    blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(get_output_layers(net))
    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    # at this point all the objects for this frame are detected. Convert the orignal tracker back into the form were it will take all teh frames at once and assign ID
    # and then I will iterate through that object list and assign values like confidence etc
    for i in indices:
        i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]

        draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x + w), round(y + h))

    cv2.imshow("object detection", image)


def main():
    global COLORS,frame_rate
    location = '../BDDA/training/camera_videos/567.mp4'
    args_config = './yolov3.cfg'
    args_weights = '../yolov3.weights'
    args_classes = './yolov3.txt'

    scale = 0.00392
    global classes

    with open(args_classes, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

    net = cv2.dnn.readNet(args_weights, args_config)

    cap = cv2.VideoCapture(location)
    # cap = cv2.VideoCapture(0)
    if cap.isOpened() == False:
        print("Error opening video stream or file")

    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            getObject(frame, net, scale)
            cd.getCountours()
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__": main()