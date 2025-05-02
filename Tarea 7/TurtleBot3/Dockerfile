FROM osrf/ros:noetic-desktop-full

#Instalar turtleBot3 y SLAM

RUN apt-get update && apt-get install -y \
	ros-noetic-turtlebot3 \
	ros-noetic-turtlebot3-simulations \
	ros-noetic-slam-gmapping

#Configurar entorno
#ENV TURTLEBOT3_MODEL=burger
ENV TURTLEBOT3_MODEL=waffle_pi
#Agregado
#RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
RUN echo "export TURTLEBOT3_MODEL=w" >> ~/.bashrc
RUN apt-get update && apt-get install -y bash

#Script de inicio
#Modificado
#CMD bash -c "source /opt/ros/noetic/setup.bash && roslaunch turtlebot3_gazebo turtlebot3_world.launch"
CMD bash -c "source /opt/ros/noetic/setup.bash && roslaunch turtlebot3_gazebo turtlebot3_house.launch"


