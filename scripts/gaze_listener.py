#!/usr/bin/env python
import rospy
from gaze_chatter.msg import Gaze

def callback(data):
    rospy.loginfo("%d at %d seconds" % (data.label, data.timestamp))

def listener():
    rospy.init_node('gaze_listener', anonymous=True)
    rospy.Subscriber("gaze_chatter", Gaze, callback)

    rospy.spin()
    return


if __name__ == '__main__':
    listener()

