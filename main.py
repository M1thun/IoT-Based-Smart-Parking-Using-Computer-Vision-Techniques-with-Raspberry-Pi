# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:47:22 2020

@author: mithun
"""

import argparse
import cv2
import numpy as np
import click_coordinate,coordinates
import urllib.request
#import car_classifier

parser = argparse.ArgumentParser()
parser.add_argument("-setup_park", help="To plot parking slots in new parking area",type=bool,default=False)
parser.add_argument("-slots", help="Number of parking slots",type=int,default=6)
args = parser.parse_args()


def saveData(coord_list):
    f1 = open('coordinates.py', 'w+')
    f1.write("boxes=")
    f1.write(str(coord_list))
    f1.close()


def capture_img():
    camera = cv2.VideoCapture('video input final cmprsd.mp4')
    print("Taking image...")
    retval, camera_capture = camera.read()
    file = "process_img.png"
    cv2.imwrite(file, camera_capture)


def auto_canny(image, sigma=0.33):
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged


def cal_count(edges,x1,y1,x2,y2):

    count=0
    for y in range(y1,y2):
        for x in range(x1,x2):
            if edges[y][x] != 0:
                count+=1
    return count


def solt_info(args,coord_list):
    camera = cv2.VideoCapture('video input final cmprsd.mp4')
    while (camera.isOpened()):
      retval, img = camera.read()
      if retval==True:
        scale_percent = 30
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        imge=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges=auto_canny(imge)
        i=edges.copy()
        for j in range(len(coord_list)):
            cv2.rectangle(img, (coord_list[j][0][0], coord_list[j][0][1]), (coord_list[j][1][0], coord_list[j][1][1]), (0, 255, 0), 2)          
        for j in range(len(coord_list)):
            cv2.rectangle(i, (coord_list[j][0][0], coord_list[j][0][1]), (coord_list[j][1][0], coord_list[j][1][1]), (255, 0, 0), 2)        
        # cv2.imshow("parking slots",i)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        white_area=[]
        for j in range(args.slots):
            white_area.append(cal_count(edges, coord_list[j][0][0], coord_list[j][0][1], coord_list[j][1][0], coord_list[j][1][1]))





        print(white_area)
        for s in white_area:
            if s > 1000:
                print("Slot "+str(white_area.index(s)+1)+": Not available")
                cv2.rectangle(img, (coord_list[white_area.index(s)][0][0], coord_list[white_area.index(s)][0][1]), (coord_list[white_area.index(s)][1][0], coord_list[white_area.index(s)][1][1]), (0, 0, 255), 2)        
                cv2.imshow("Real Timee",img)                
                white_area[white_area.index(s)] = "1"          

            else:
                print("Slot "+str(white_area.index(s)+1)+": Available")
                white_area[white_area.index(s)] = "0"

        display(white_area)
      else:
       camera.set(cv2.CAP_PROP_POS_AVI_RATIO , 0);
       continue;
    camera.release()
    cv2.destroyAllWindows()



def display(white_area):
    info=""
    for i in range(len(white_area)):
        #print("slot-"+str(i+1)+"="+white_area[i]+"\n")
        info=info+white_area[i]
    print("\nString:",info)
    print(urllib.request.urlopen("http://localhost/connect.php?temp="+info).read())
    print("added to database\n")
    


if __name__=="__main__":
    if args.setup_park:
        print("true")
        capture_img()
        image = cv2.imread('process_img.png')
        scale_percent = 30
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        coord_list=click_coordinate.find_coord(args,image)
        saveData(coord_list)
        solt_info(args,coord_list)
        
    else:
        print("False")
        coord_list=coordinates.boxes
        solt_info(args,coord_list)
