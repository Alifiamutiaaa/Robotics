# wall_follower controller.

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

def run_robot(robot):
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28
    
    # Enable motors   
    left_motor = robot.getMotor('left wheel motor')
    right_motor = robot.getMotor('right wheel motor')
    
    if left_motor and right_motor:
        left_motor.setPosition(float('inf'))
        left_motor.setVelocity(0.0)
    
        right_motor.setPosition(float('inf'))
        right_motor.setVelocity(0.0)
    
        # Enable proximity sensors
        prox_sensors = []
        for ind in range(8):
            sensor_name = 'ps' + str(ind)
            prox_sensors.append(robot.getDistanceSensor(sensor_name))
            prox_sensors[ind].enable(timestep)
    
        # Main loop:
        # - perform simulation steps until Webots is stopping the controller
        while robot.step(timestep) != -1:
            # Read the sensors:
            sensor_values = [prox_sensors[ind].getValue() for ind in range(8)]
            print("Sensor values:", sensor_values)
        
            # Process sensor data here.
            left_wall = sensor_values[5] > 80
            left_corner = sensor_values[6] > 80
            right_wall = sensor_values[7] > 80
            
            # Initialize speeds
            left_speed = max_speed
            right_speed = max_speed
            
            # Adjust speeds based on sensor readings
            if left_wall:
                print("Turn right in place")
                left_speed = max_speed
                right_speed = -max_speed
            elif left_corner:
                print("Came too close, drive right")
                left_speed = max_speed
                right_speed = max_speed/2
            elif right_wall:
                print("Turn left")
                left_speed = max_speed/2
                right_speed = max_speed
            
            # Enter here functions to send actuator commands
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)
    
if __name__ == '__main__':
    # Create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)
