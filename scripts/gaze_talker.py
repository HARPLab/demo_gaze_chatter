#!/usr/bin/env python
import rospy
from gaze_chatter.msg import Gaze


def talker(x=1, y=1):
    pub = rospy.Publisher('gaze_chatter', Gaze)
    rospy.init_node('gaze_talker', anonymous=True)
    r = rospy.Rate(10)

    msg = Gaze()
    msg.x = float(x)
    msg.y = float(y)
    msg.label = get_label(x, y)
    msg.timestamp = rospy.get_rostime()

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

    return

def get_label(x=1, y=1):
    return 0

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
