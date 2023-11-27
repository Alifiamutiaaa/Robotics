from robot_control_class import RobotControl
rc = RobotControl()


rc.move_straight()

depan = rc.get_laser(360)

if depan < 1:
    rc.stop_robot()
    rc.turn(90)