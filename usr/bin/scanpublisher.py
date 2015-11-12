#!/usr/bin/env python


#Pipe parser-- made to accept pipe from gmapping
#publishes the average scan matching score to the fuzzy logic RFID decider




import roslib; roslib.load_manifest('aticuss')
import rospy, sys
from std_msgs.msg import Float32 as Float
def scanner():
    pub = rospy.Publisher('scan_score', Float)
    rospy.init_node('scan_publisher')
    print "Scan_Plublisher starting"
    
    while not rospy.is_shutdown():
        line = (sys.stdin.readline()).rstrip("\r\n")
        if line:
            print 'Got data:', line
            
            if 'Average' in line:
                str = line.split('=')
                scan = str[1]
                print 'SCAN IS:::::::::::::::::::::', str
                print 'Scan is:', scan
                rospy.loginfo(line)
                pub.publish(float(scan))

if __name__ == '__main__':
    try:
        scanner()
    except rospy.ROSInterruptException: pass
