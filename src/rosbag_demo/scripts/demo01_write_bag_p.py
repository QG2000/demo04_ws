#! /usr/bin/env python

import rospy
import rosbag
from std_msgs.msg import String
""" 
    需求  写出数据到磁盘上的bag文件
    流程：
        1 导包
        2 初始化
        3 创建 rosbag 对象 并且打开文件流
        4 写数据
        5 关闭流
"""

if __name__ == "__main__":
    rospy.init_node("write_bag_p")
    bag = rosbag.Bag("hello_p.bag", 'w')
    msg = String()
    msg.data = "hello_bag!"
    bag.write("/liaoTian", msg)
    

    bag.close()





    pass