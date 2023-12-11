"""distance controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, DistanceSensor, Motor
import matplotlib.pyplot as plt

# Inisialisasi robot dan perangkat keras
robot = Robot()
time_step = int(robot.getBasicTimeStep())

# Inisialisasi sensor jarak
ds = robot.getDistanceSensor("ds")
ds.enable(time_step)

# Inisialisasi motor
left_motor = robot.getMotor("left wheel motor")
right_motor = robot.getMotor("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0)
right_motor.setVelocity(0)

# Fungsi untuk menggerakkan robot
def move_robot(forward, duration):
    left_motor.setVelocity(forward)
    right_motor.setVelocity(forward)
    robot.step(duration)
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

# Fungsi untuk merekam data perpindahan dan waktu
def record_data(filename, data):
    with open(filename, 'w') as file:
        file.write("Time\tDistance\n")
        for entry in data:
            file.write(f"{entry[0]}\t{entry[1]}\n")

# Fungsi untuk melakukan tugas jarak
def distance_task(speed, duration, direction, plot_filename):
    data = []
    move_robot(speed * direction, duration)
    data.append([0, 0])  # Initial position at time = 0
    time = 0
    while robot.step(time_step) != -1:
        distance = ds.getValue()
        time += time_step / 1000.0  # Convert time_step to seconds
        data.append([time, distance])
        if time >= duration:
            break
    record_data(plot_filename, data)
    plt.plot(*zip(*data))
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.title('Distance vs Time')
    plt.savefig(f"{plot_filename}.png")
    plt.show()

# Example 1
distance_task(6.28, 5, 1, "plot1.txt")

# Example 2
distance_task(-0.1, 10, -1, "plot2.txt")

# Example 3
distance_task(0.2, 5, 1, "plot3.txt")
