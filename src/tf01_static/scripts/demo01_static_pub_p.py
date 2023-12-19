#! /usr/bin/env python

import rospy
import tf2_ros
import tf
import tf.transformations
from geometry_msgs.msg import TransformStamped
""" 
    发布两个坐标系的相对关系  车辆底盘 base_link   and  雷达 laser  
    流程
        1 导包
        2 初始化节点
        3 创建发布对象
        4 组织被发布者的数据
        5 发布数据
        6 spin()
 """

if __name__ == "__main__":
    rospy.init_node("static_pub_p")
    pub = tf2_ros.StaticTransformBroadcaster()
    ts = TransformStamped()
    #header
    ts.header.stamp = rospy.Time.now()
    ts.header.frame_id = "base_link"
    #child frame
    ts.child_frame_id = "laser"
    #相对关系（便宜与四元数）
    ts.transform.translation.x = 2.0
    ts.transform.translation.y = 0
    ts.transform.translation.z = 0.5
    #先从欧拉角转换为四元数
    qtm = tf.transformations.quaternion_from_euler(0,0,0)

    #然后再设置 四元数
    ts.transform.rotation.x = qtm[0]
    ts.transform.rotation.y = qtm[1]
    ts.transform.rotation.z = qtm[2]
    ts.transform.rotation.w = qtm[3]

    #发布数据
    pub.sendTransform(ts)
    #spin
    rospy.spin()
