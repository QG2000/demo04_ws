#! /usr/bin/env python

import rospy
from turtlesim.msg import Pose
import tf2_ros 
from geometry_msgs.msg import TransformStamped
import tf
import tf.transformations
""" 
    发布方：订阅乌龟的位置信息 转换成坐标系的相对关系 在发布
    准备：
        话题 /turtle1/pose
        类型 /turtlesim/pose
    流程：
        导包
        初始化ros节点
        创建订阅对象
        回调函数处理订阅到的消息（位姿信息转换成坐标系的相对关系）
        spin
 """

def doPose(pose):
    pub = tf2_ros.TransformBroadcaster()
    ts = TransformStamped()
    ts.header.frame_id = "world"
    ts.header.stamp = rospy.Time.now()
    ts.child_frame_id = "turtle1"
    ts.transform.translation.x = pose.x
    ts.transform.translation.y = pose.y
    ts.transform.translation.z = 0
    #四元数
    qtn = tf.transformations.quaternion_from_euler(0, 0, pose.theta)
    ts.transform.rotation.x = qtn[0]
    ts.transform.rotation.y = qtn[1]
    ts.transform.rotation.z = qtn[2]
    ts.transform.rotation.w = qtn[3]
    pub.sendTransform(ts)
    pass


if __name__ == "__main__":
    rospy.init_node("dynamic_pub_p")
    sub = rospy.Subscriber("/turtle1/pose", Pose, doPose, queue_size=100)
    rospy.spin()

    pass