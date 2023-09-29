from robot_control_class import RobotControl

robotcontrol = RobotControl(robot_name="summit")

robotcontrol.turn("counter-clockwise", 0.3, 2)
robotcontrol.move_straight_time("forward", 0.3, 2)
robotcontrol.turn("counter-clockwise", 0.3, 1)
robotcontrol.move_straight_time("forward", 0.3, 1)
robotcontrol.turn("counter-clockwise", 0.3, 3)
robotcontrol.move_straight_time("forward", 0.3, 2)
robotcontrol.turn("counter-clockwise", 0.3, 6)
robotcontrol.move_straight_time("forward", 0.3, 8)