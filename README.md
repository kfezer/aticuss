To run turtlebot autonomous mapping:

Make sure the aticuss package is installed.


Open 6 terminal windows. in 4 ssh to turtlebot. I prefer to use tabs.
1. 
Make sure the laptop is on, plugged into the base, and the base is on. Then make sure you can ssh into the turtlebot (sshtb)

2.
In the first terminal:
run:

roslaunch aticuss turtlebot_bringup.launch

if this doesn't work, or runs into errors, ctrl-c. 
run:
sudo service turtlebot stop 

now run turtlebot_bringup again

3. 
In terminal 2:

roslaunch turtlebot_navigation gmapping_demo.launch | rosrun aticuss scan_publisher

This should work. IF not, try scan_publisher.py. Always use tab when typing in the terminal. It will fill out as much as possible, until there is a choice for two options. In most cases, aticuss has few conflicts between similiarly starting programs. 

That is one command. The "|" opens a pipe so the output of gmapping runs into scan_publisher and creates a node that publishes the data. 

4.
In the two not ssh'd to turtlebot, run:

dashboard

rosrun rviz rviz

If there are problems running rivz, see the SLAM Gmapping tutorial on ROS.

5. 

In the last two ssh'd terminals:

rosrun aticuss rfid_mapper

This is optional. If it's not on, then rfid tags will not be read. 

and finally:

choose a autonomous navigation node, either:

rosrun aticuss random_explorer
rosrun aticuss greedy_exlorer
rosrun aticuss bb_evolver 
or 
rosrun aticuss bb_exploration

if there is an evolved method. THere is one in the code that can be used.

