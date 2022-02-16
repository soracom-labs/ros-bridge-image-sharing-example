# Robot

## Prerequisite

- OS: Raspbian GNU/Linux(armv7l) or Ubuntu 18.04(x86_64). (These are tested os.)
- Docker environment
- Web Camera: It needs to be connected to your pc.

## Build

```
docker build -t ros_bridge_dev:1.0 .
```

## Run

### Container

In your host pc. You can start container.

```
docker run --name=ros_bridge_dev -it \
    --volume="$PWD/:/workspace/share:rw" \
    --device=/dev/video0:/dev/video0 \
    --net=host\
    ros_bridge_dev:1.0
```

### ROS

In your container, please build ros packages.

```
cd $WORKSPACE/catkin_ws
catkin build
source $WORKSPACE/catkin_ws/devel/setup.bash
```

Launch ros application to publish camera images.

```
export APP_IMAGE_FPS=5
export APP_IMAGE_QUALITY=30
export APP_CAMERA_ID=0
sudo chmod 666 /dev/video0
roslaunch app.launch
```
