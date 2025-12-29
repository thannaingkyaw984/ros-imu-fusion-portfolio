#!/usr/bin/env python3
import rospy
from imu_camera_fusion.msg import ImuData
from std_msgs.msg import Header
import random

def main():
    rospy.init_node('imu_publisher_node')
    
    # IMU data ပို့မယ့် publisher ဖန်တီးပါ
    pub = rospy.Publisher('imu/data', ImuData, queue_size=10)
    
    # 10Hz နှုန်းနဲ့ data ပို့မယ်
    rate = rospy.Rate(10)
    
    rospy.loginfo("📡 IMU Publisher Node စတင်ပါပြီ!")
    
    counter = 0
    while not rospy.is_shutdown():
        # IMU data message ဖန်တီးပါ
        msg = ImuData()
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "imu_frame"
        
        # နမူနာ IMU data တွေ
        # Linear acceleration (m/s²)
        msg.linear_acceleration = [
            random.uniform(-0.1, 0.1),    # x-axis
            random.uniform(-0.1, 0.1),    # y-axis  
            9.8 + random.uniform(-0.1, 0.1)  # z-axis (gravity + noise)
        ]
        
        # Angular velocity (rad/s)
        msg.angular_velocity = [
            random.uniform(-0.05, 0.05),  # x-axis
            random.uniform(-0.05, 0.05),  # y-axis
            random.uniform(-0.05, 0.05)   # z-axis
        ]
        
        # Data ပို့ပါ
        pub.publish(msg)
        
        # 10 ကြိမ်မှာ 1 ကြိမ် log ပြပါ
        if counter % 10 == 0:
            rospy.loginfo(f"📤 IMU Data Published - Count: {counter}")
        
        counter += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo("IMU Publisher ရပ်လိုက်ပါပြီ")
