#!/usr/bin/env python3
# Ethical Telco Tracking Simulator for ROS

import rospy
import random
from std_msgs.msg import String

class EthicalTrackingSimulator:
    def __init__(self):
        rospy.init_node('ethical_tracking_sim')
        
        # Dummy data - အမှန်တကယ် ဖုန်းနံပါတ်များ မသုံးပါ
        self.dummy_phones = ["SIM_001", "SIM_002", "SIM_003"]
        
        # Simulated cell towers
        self.towers = [
            {"id": "T1", "location": "Yangon Tower 1"},
            {"id": "T2", "location": "Yangon Tower 2"},
            {"id": "T3", "location": "Yangon Tower 3"}
        ]
        
        # Publisher for simulation data
        self.tracking_pub = rospy.Publisher('/ethical_tracking/data', String, queue_size=10)
        
        rospy.loginfo("✅ Ethical Tracking Simulator Started")
        rospy.loginfo("⚠️  Using simulated data only")
        rospy.loginfo("⚠️  No real phone numbers used")
        rospy.loginfo("📡 Educational Purpose Only")
    
    def simulate_tracking(self):
        """ကျင့်ဝတ်နဲ့ညီတဲ့ tracking simulation"""
        rate = rospy.Rate(1)  # 1 second တစ်ကြိမ်
        
        while not rospy.is_shutdown():
            # Random dummy data ရွေးချယ်ခြင်း
            dummy_phone = random.choice(self.dummy_phones)
            tower = random.choice(self.towers)
            
            # Simulation message
            message = f"📱 SIMULATED: {dummy_phone} at {tower['id']} ({tower['location']})"
            rospy.loginfo(message)
            
            # Publish to ROS topic
            msg = String()
            msg.data = message
            self.tracking_pub.publish(msg)
            
            # Educational messages (30% chance)
            if random.random() < 0.3:
                edu_msg = "💡 Remember: Real phone tracking requires legal permission!"
                rospy.loginfo(edu_msg)
                
                edu_msg_obj = String()
                edu_msg_obj.data = edu_msg
                self.tracking_pub.publish(edu_msg_obj)
            
            rate.sleep()

if __name__ == '__main__':
    try:
        simulator = EthicalTrackingSimulator()
        simulator.simulate_tracking()
    except rospy.ROSInterruptException:
        rospy.loginfo("Ethical Tracking Simulator ရပ်လိုက်ပါပြီ")
