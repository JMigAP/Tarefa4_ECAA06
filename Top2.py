import rospy
from std_msgs.msg import String

rospy.init_node('no2')
ni = 0

def timerCallBack(event):
    msg = String()
    x = ni
    soma = 0
    
    while (x != 0):
        resto = x % 10
        x = (x - resto)//10
        soma = soma + resto
    
    msg.data = str(soma)
    pub.publish(msg)
    
def topCallBack(msg):
    global mat, ni
    mat = msg.data
    ni = int(msg.data)
    
pub = rospy.Publisher('/topic2', String, queue_size=1)
sub = rospy.Subscriber('/topic1', String, topCallBack)

timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()