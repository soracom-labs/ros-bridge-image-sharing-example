#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
import configparser
import rospy
import traceback
from util.application_exception import *

default_code="e_99999999"

def warp_with_try():
    def real_decorator(func):
        def wrapper(*args, **kargs):
            try:
                return func(*args, **kargs)
            except ApplicationException as e:
                rospy.logerr("ApplicationException: " + e.error_code + " " + e.error_msg)
                rospy.loginfo(e)
                rospy.loginfo(traceback.format_exc())
            except Exception as e:
                app_exception = ApplicationException(default_code)
                rospy.logerr("ApplicationException: " + app_exception.error_code + " " + app_exception.error_msg)
                rospy.loginfo(e)
                rospy.loginfo(traceback.format_exc())
        return wrapper
    return real_decorator



class ApplicationException(Exception):

    def __init__(self, error_code):
        self.error_code = error_code
        error_info = self.get_error_info(error_code).split(",")
        self.error_level = error_info[0]
        self.error_msg = error_info[1]

    def __str__(self):
        return repr(self.error_code + " " + self.error_msg)

    def get_error_info(self, key):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'error.ini'))
        env = "default"
        return config.get(env, key)
