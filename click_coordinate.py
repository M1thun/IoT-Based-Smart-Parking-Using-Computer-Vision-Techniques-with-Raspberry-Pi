import cv2
import numpy as np

disp = False
slots=0
coordinate=[]
x_start, y_start, x_end, y_end = 0, 0, 0, 0

 
def mouse_crop(event, x, y, flags, param):
    global x_start, y_start, x_end, y_end, disp,slots,coordinate


    if event == cv2.EVENT_RBUTTONDOWN:
        if len(coordinate)>=1:
            coordinate.pop()


    elif event == cv2.EVENT_MOUSEMOVE:
        if disp == True:
            x_end, y_end = x, y


    elif event == cv2.EVENT_LBUTTONDOWN:
        disp=True
        x_start, y_start, x_end, y_end = x, y, x, y
 

    elif event == cv2.EVENT_LBUTTONUP:
        disp=False
        x_end, y_end = x, y
        refPoint = [(x_start, y_start), (x_end, y_end)]
 
        if len(refPoint) == 2:
            coordinate.append(refPoint)
            refPoint=[None,None]        


def find_coord(args,image):
    global x_start, y_start, x_end, y_end, disp,slots,coordinate
    slots=args.slots
    oriImage = image.copy()        
 
    cv2.namedWindow("parking area",0)
    cv2.resizeWindow("parking area",image.shape[1],image.shape[0])
    cv2.setMouseCallback("parking area", mouse_crop)
 
    while True:
        i=image.copy()
        ii=image.copy()
        if not disp:            
            for j in range(len(coordinate)):
                cv2.rectangle(ii, (coordinate[j][0][0], coordinate[j][0][1]), (coordinate[j][1][0], coordinate[j][1][1]), (255, 0, 0), 2)
            cv2.imshow("parking area", ii)

        if disp:
            for j in range(len(coordinate)):
                cv2.rectangle(i, (coordinate[j][0][0], coordinate[j][0][1]), (coordinate[j][1][0], coordinate[j][1][1]), (255, 0, 0), 2)
            cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
            cv2.imshow("parking area", i)

    
        if len(coordinate)==slots:
            cv2.destroyAllWindows()
            break
                
        cv2.waitKey(1)
    return coordinate




