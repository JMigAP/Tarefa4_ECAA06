import rospy
from std_msgs.msg import String

rospy.init_node('no1')

def timerCallBack(event):
    msg = String()
    msg.data = '2017005688'
    pub.publish(msg)
    
def topCallBack(msg):
    global mat
    mat = msg.data
    print(msg.data)
    
pub = rospy.Publisher('/topic1', String, queue_size=1)
sub = rospy.Subscriber('/topic2', String, topCallBack)

timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()
