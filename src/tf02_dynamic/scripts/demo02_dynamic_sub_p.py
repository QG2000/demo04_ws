#! /usr/bin/env python

import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs
""" 
    订阅方   订阅坐标变化信息  传入被转化的坐标点  调用转换算法api
    流程：
        1 导包
        2 初始 ros节点
        3 创建订阅对象
        4 组织被转换的坐标点
        5 转换逻辑实现
        6 输出最后的转换结果
        7 spin()   |  spinOnce();

"""

if __name__ == "__main__":
    # 2 初始 ros节点
    rospy.init_node("static_sub_p")
    # 3 创建订阅对象
        #创建缓存对象
    buffer = tf2_ros.Buffer()
        #创建订阅对象 将缓存传入
    sub = tf2_ros.TransformListener(buffer)
    # 4 组织被转换的坐标点
    ps = tf2_geometry_msgs.PointStamped()
    #时间cuo为0
    ps.header.stamp = rospy.Time()
    ps.header.frame_id = "turtle1"
    ps.point.x = 2.0
    ps.point.y = 3.0
    ps.point.z = 5.0
    # 5 转换逻辑实现
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
                    # 6 输出最后的转换结果
            ps_out = buffer.transform(ps, "world")
            rospy.loginfo("转换后的坐标：(%.2f,%.2f,%.2f),参考坐标系：%s",
                        ps_out.point.x,
                        ps_out.point.y,
                        ps_out.point.z,
                        ps_out.header.frame_id
                        )
        except Exception as e:
            rospy.logwarn("错误提示 %s", e)
        
        rate.sleep()
    #有循环 就 不用  spin

