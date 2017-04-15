# FHMPRobotArm
####################Initial Setup####################
If you are reading this, you have already downloaded the code folder and should have all of the files you need. Only a few more steps:

1. Make sure that the Pi is connected to the same wireless network as the device that will be sending the X,Y,Z coordinates
 	so that the UDP receiver can function properly.
2. Ensure that all hardware is connected properly. Follow the setup instructions in the report.
3. To run the program, open up the file "GrabFromVicon.py" and then press F5 and then the ENTER key. Or, to run it in command line,
	open the terminal, navigate to the directory of the program (by typing "cd pathOfDirectory") and then type "python
	GrabFromVicon.py".
	Note that the program will not move the arm unless it receives the UDP coordinates, so the companion device (Vicon computer) 
	must be also running.
	#####################################################
	
####################File Descriptions####################
AngleFinder.py
	This calculates the joint angles using inverse kinematics. This shouldn't need to be changed.
ArmMovement.py
	This is a helper program that uses the maestro library to move the joints. This also should not require modification.
Constants.py
	This contains constants that we created to store the PWM value ranges and offsets for each joint. We modified the offsets 
	to calibrate the arm. Unless the arm is not calibrated, these don't need to be modified.
Maestro.py
	This is the Pololu maestro library that we use to move the arm. This was downloaded from https://github.com/frc4564/maestro.
GrabFromVicon.py
	This is the main program that is run to move the arm to the given position. It calls the other helper files to combine several 
	functions. This can be modified to fit different applications (ex: repeated movement or specific tasks after grabbing an object).
	
	
Note: .pyc files are not important and can be ignored (but they are necessary for the program to function). Don't delete them.
	
