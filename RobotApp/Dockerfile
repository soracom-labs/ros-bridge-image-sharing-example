##
# ROS1 Dockerfile
##
FROM ros:melodic

ARG USERNAME=user
ARG GROUPNAME=user
ARG UID=1000
ARG GID=1000
ARG PASSWORD=user
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME && \
    echo $USERNAME:$PASSWORD | chpasswd && \
    echo "$USERNAME   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# bootstrap rosdep
RUN sudo rosdep update

# For raspberrypi following versions are compatible. But to build for ubuntu we removed specifying the versions.
#ros-melodic-catkin=0.7.29-1bionic.20201014.192528 \
#ros-melodic-rosbridge-suite=0.11.13-1bionic.20210922.045638 \
#ros-melodic-cv-bridge=1.13.0-0bionic.20210922.005012

RUN apt update && \
  apt install -y ros-melodic-catkin \
  python-catkin-tools=0.6.1-1 \
  python-pip=9.0.1-2.3~ubuntu1.18.04.5 \
  ros-melodic-rosbridge-suite \
  python-opencv=3.2.0+dfsg-4ubuntu0.1 \
  ros-melodic-cv-bridge

RUN apt install -y vim=2:8.0.1453-1ubuntu1.8 \
  curl=7.58.0-2ubuntu3.16

ENV ROS_DISTRO melodic
ENV WORKSPACE /workspace/share/
WORKDIR $WORKSPACE

USER $USERNAME
