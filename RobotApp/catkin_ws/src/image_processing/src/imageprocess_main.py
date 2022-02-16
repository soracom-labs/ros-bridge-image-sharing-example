#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import rospy
from sensor_msgs.msg import CompressedImage
import base64
import cv2
from util.application_exception import *
import traceback
from cv_bridge import CvBridge
import numpy as np

import time
import copy
import logging
import threading

logger = logging.getLogger('rosout')

class ImageUtil:
    def __init__(self):
        self.captured_img = None


        cameraid=int(os.getenv('APP_CAMERA_ID', 0))
        self.latency=float(os.getenv('APP_CAMERA_LATENCY', 0.0))
        logging.info("cameraid is "+str(cameraid))
        logging.info('camera latency is '+str(self.latency)+' second')
        #self.cap = cv2.VideoCapture(cameraid)
        rospy.sleep(3)
        trycount=0
        while(trycount<10):
            logging.info("try to read camera,attempt:"+str(trycount))
            self.cap = cv2.VideoCapture(cameraid)

            logging.info("fps:"+str(self.cap.get(5)))
            logging.info("codec:"+str(self.cap.get(6)))
            logging.info("CV_CAP_PROP_FORMAT:"+str(self.cap.get(8)))
            logging.info("CV_CAP_PROP_MODE:"+str(self.cap.get(9)))
            time.sleep(1)
            ret, captured_img = self.cap.read()
            if ret:
                break
            trycount+=1
            time.sleep(1)
        else:
            raise ApplicationException("e_99999999")
        self.inputwidth=captured_img.shape[1]
        self.inputheight=captured_img.shape[0]
        logging.info(captured_img.shape)
        self.firstimagegetted=True

        #a thread to comsume buffer to get less latency
        self.getimagethread=threading.Thread(target=self.getimagefromcamera)
        self.getimagethread.setDaemon(True)
        self.getimagethread.start()


    @warp_with_try()
    def getimagefromcamera(self):
        while(self.cap.isOpened()):
            ret, captured_img = self.cap.read()
            if(ret):
                self.captured_img=copy.deepcopy(captured_img)
                self.firstimagegetted=True
            else:
                raise ApplicationException("e_99999999")
            time.sleep(0.1)
        raise ApplicationException("e_99999999")

    def getimage(self):
        self.timestamp = rospy.Time.now()-rospy.Duration(self.latency)
        return self.captured_img

class ImageProcess:
    def __init__(self):
        self.pub = None
        self.bridge = None

    @classmethod
    @warp_with_try()
    def main(self):
        image_util=ImageUtil()
        image_fps=int(os.getenv('APP_IMAGE_FPS', 3))
        rate = rospy.Rate(image_fps) # 3hz

        logging.info("starting main loop")

        while(not image_util.firstimagegetted):
            time.sleep(1)

        logging.info("start main has started")

        self.pub = rospy.Publisher('camera1_compressed', CompressedImage, queue_size=10)
        self.bridge = CvBridge()

        while not rospy.is_shutdown():
            logging.info("start main loop")

            image=image_util.getimage()
            if image is not None:
                image_quality=int(os.getenv('APP_IMAGE_QUALITY', 10))

                msg = CompressedImage()
                msg.header.stamp = rospy.Time.now()
                msg.format = "jpeg"
                msg.data = np.array(cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), image_quality])[1]).tostring()

                self.pub.publish(msg)

            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('image_processing')
    ImageProcess().main()
