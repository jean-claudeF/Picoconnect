# Picoconnect
Python library for connecting to a defined Raspi Pico (even if there is more than one connected and you don't know on which port it is connected)
(Find  a defined Pico, execute commands on it etc.)

# Working principle
Each Pico has a file info.txt in the root folder. The first line of this file contains a keyword under which the Pico can be found. The picoconnector_xx.py lib has functions to find this and connect.


