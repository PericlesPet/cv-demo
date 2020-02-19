import rospy
from sensor_msgs.msg import Image
from darknet_ros_msgs.msg import BoundingBoxes
from std_msgs.msg import Header
from std_msgs.msg import String
from rosIPMap import IPMap

# INPUT
DARKNET_ROS_BOUNDING_BOXES = '/darknet_ros/bounding_boxes'

# OUTPUT
DARKNET_ROS_CONE_POINTS = '/turtle/BirdsEyeView'


bev_pub = rospy.Publisher(DARKNET_ROS_CONE_POINTS, Float64[][], queue_size=10)

def callback(data):

#   bboxes = data.bounding_boxes
#   cxy_points = IPMap(width, height, bboxes)
#   publish(DARKNET_ROS_CONE_POINTS, cxy_points)
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    # bev_points = IPM_helper.ros_bbox2points(IM_WIDTH, IM_HEIGHT, --missing-- )

def main():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber(DARKNET_ROS_BOUNDING_BOXES, BoundingBoxes , callback)
    rospy.spin()


if __name__ == '__main__':
    try :
        main()
    except rospy.ROSInterruptException:
        pass