FROM python:3

RUN apt-get update && apt-get install -y \
    xvfb \
    x11-utils \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY main.py .
COPY two_joint_robot_custom.urdf .


RUN pip install pybullet
RUN pip install numpy

CMD command python3 main.py

