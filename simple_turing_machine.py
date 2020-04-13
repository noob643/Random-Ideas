#! python3
# simple_turing_machine.py Simple Turing Machine
"""
There are n number of rooms
A robot goes into a random room and turns the light on/off based on the state of the robot.
When the robot is scared:
    if the light is off, the robot turns it on and remains scared
    if the light is on, the robot does nothing and changes state to normal
When robot state is normal:
    if the light is off, the robot turns it on and becomes scared
    if the light is on, the robot does nothing and remains normal
"""

import random
import time

number_of_rooms = 30
state = "normal"

# Create rooms initial condition
rooms = []
for z in range(number_of_rooms):
    r = random.choice(["*", " "])
    rooms.append(r)

# Main Loop
while True:
    selected_room = random.randint(0, number_of_rooms - 1)

    # Display the light status in each room
    print("|", end="")
    for z in range(number_of_rooms):
        print(rooms[z], end="|")
    print()

    if state == "normal":
        if rooms[selected_room] == "*":
            rooms[selected_room] = " "
            s = state
        if rooms[selected_room] == " ":
            s = "scared"
            rooms[selected_room] = "*"
    else:
        if rooms[selected_room] == " ":
            rooms[selected_room] = "*"
            s = state
        if rooms[selected_room] == "*":
            s = "normal"
            rooms[selected_room] = " "
    state = s
    time.sleep(0.01)
