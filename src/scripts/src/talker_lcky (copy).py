#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states_',JointState, queue_size=10)
    rospy.init_node('talker_azaza', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.header.frame_id = 'kek'   
    hello_str.name = ['base_to_first_link', 'base_to_second', 'first_link_to_third_link']
#    hello_str.velocity = []
#    hello_str.effort = []
    a = 0.0
    b = 0.0
    c = 0.0
    flag_1 = True
    flag_2 = True
    while not rospy.is_shutdown():
	    
	    hello_str.header.stamp = rospy.Time.now()
	    hello_str.position = [0.3, 0.3, 0.3]
	        
	    pub.publish(hello_str)
	    rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
