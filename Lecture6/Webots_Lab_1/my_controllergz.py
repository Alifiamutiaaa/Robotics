from controller import Robot
import time

# Function to calculate velocity
def calculate_velocity(distance, time):
    return distance / time

# Constants
X = 30  # Distance in inches
Y = 5   # Time in seconds
MAX_VELOCITY = 6.28

# Initialize the Webots robot
robot = Robot()

# Time step
timestep = int(robot.getBasicTimeStep())

# Convert distance to meters (1 inch = 0.0254 meters)
distance_in_meters = X * 0.0254

# Calculate velocity
velocity = calculate_velocity(distance_in_meters, Y)

# Initialize motors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))  # Set to infinity for velocity control
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0)
right_motor.setVelocity(0)

# Test case: Velocity is positive
if velocity > 0:
    print("Test Case: Velocity is positive")
    # Move the robot
    start_time = robot.getTime()
    total_distance = 0.0

    while robot.step(timestep) != -1:
        current_time = robot.getTime()
        elapsed_time = current_time - start_time

        if elapsed_time < Y:
            left_motor.setVelocity(velocity)
            right_motor.setVelocity(velocity)
            # Calculate and print the distance for each timestep
            distance_this_step = velocity * timestep
            total_distance += distance_this_step
            print(f"Timestamp: {current_time:.2f}, Distance: {total_distance:.2f} meters")

        else:
            left_motor.setVelocity(0)
            right_motor.setVelocity(0)
            break
        print(f"Timestamp: {current_time:.2f}, Distance: {total_distance:.2f} meters")


    # Check if the robot could not complete the movement
    if elapsed_time >= Y:
        print("The robot could not complete the movement in the given time.")
else:
    print("Error: Velocity is not positive.")
