# Traffic-management-system-
This traffic management control system consists of a hall effect sensor, LED lights (red and green), and Raspberry Pi. The Raspberry Pi microcontroller contains the python programming code, which controls the time delay of led lights.
The Hall effect sensors are placed on the road surface at regular intervals of distance to detect vehicles' presence on the road. The emergency vehicles are requested to place radio wave transmitters, allowing the radio wave detector to identify emergency vehicles. The radio waves detector is placed at every junction to detect the presence of a radio wave emitter placed inside the emergency vehicle. Raspberry Pi microcontroller is placed at every intersection that collects the information from the various sensors placed at different locations, and the resultant time is calculated. The microcontroller turns on the LED lights for the stipulated time estimated.

Phase-1:-
We are assuming four different breadboards to imitate a four-direction intersection junction and have placed three hall effect sensors on three sides along with one green light and red light on each side. All the terminals from the hall effect sensor and the led lights are connected to the raspberry pi's gpio pins. The instantaneous data of a particular moment is collected from all the sensors from every direction, and the program compares and identifies the side having maximum traffic volume. The green light is given to the particular side with maximum volume, and the other three sides will remain red. As the vehicles move out, the last active sensor detects the absence of a vehicle, and the program goes on to check which other side has maximum traffic. Considering there are four directions in an intersection junction, once the green light is given to one, the preference is given to the next maximum congestion side.
