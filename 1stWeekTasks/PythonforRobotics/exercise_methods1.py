import time
from robot_control_class import RobotControl

robotcontrol = RobotControl(robot_name="summit")

def move_time_seconds(secs):
    robotcontrol.move_straight()
    time.sleep(secs)
    robotcontrol.stop_robot()


move_time_seconds(5)