"""
moveByVelocityBodyFrameAsync基于无人机自身的坐标系，每次施加新的速度都会在新的和速度上有一个位移
z轴上的加速度需要有一个缩放
加速度的范围需要与duration相匹配，初步结论，加速度越大，duration应该越小
在设置传感器时，先设置yaw，在设置pitch，都是顺时针方向，仅在无人机正面设置，共37根
"""

import airsim
import time
import pprint
import keyboard
from multirotor import *
import torch

# pip install --upgrade msgpack-rpc-python

from airsim import YawMode

client = airsim.MultirotorClient()  # connect to the AirSim simulator
# mr = Multirotor(client=client)
# my_yaw_mode = YawMode()
# my_yaw_mode.is_rate = False
# my_yaw_mode.yaw_or_rate = 0
# client.moveToPositionAsync(x=-250, y=400, z=-60, velocity=10, drivetrain=airsim.DrivetrainType.ForwardOnly, yaw_mode=my_yaw_mode).join()
# client.hoverAsync().join()          # 第四阶段：悬停5秒钟
# time.sleep(60)

for i in range(3):
    mr = Multirotor(client=client)
    # client.hoverAsync().join()          # 悬浮5秒钟
    # time.sleep(5)

    print("-------------------初始位置-------------------")
    # print("位置: %s" % position)
    # print("速度: %s" % kinematic_state.linear_velocity.to_numpy_array())
    # print("加速度: %s" % kinematic_state.linear_acceleration)
    # print("偏航角: {}°".format(np.array([mr.get_deflection_angle()])))
    # print("距离传感器数据：{}".format(np.array(mr.get_distance_sensors_data())))
    print(mr.ux, mr.uy, mr.uz)
    print(torch.FloatTensor(mr.get_state()))
    print("距离：{}".format(mr.get_distance()))
    print("是否发生碰撞：{}".format(client.simGetCollisionInfo().has_collided))
    # 效果测试
    # 角度的转动速率为弧度制
    my_yaw_mode = YawMode()
    my_yaw_mode.is_rate = False
    my_yaw_mode.yaw_or_rate = 0
    for i in range(50):
        a = 1
        client.moveByVelocityAsync(vx=client.simGetGroundTruthKinematics().linear_velocity.x_val + a,
                                   vy=client.simGetGroundTruthKinematics().linear_velocity.y_val + a,
                                   vz=client.simGetGroundTruthKinematics().linear_velocity.z_val-a,
                                   duration=0.5,
                                   drivetrain=airsim.DrivetrainType.ForwardOnly,
                                   yaw_mode=my_yaw_mode).join()
        kinematic_state = client.simGetGroundTruthKinematics()
        print("-------------------episode {} -------------------".format(i))
        position = kinematic_state.position.to_numpy_array()
        print("位置: %s" % position)
        print("速度: %s" % kinematic_state.linear_velocity.to_numpy_array())
        print("加速度: %s" % kinematic_state.linear_acceleration)
        # mr.current_set(client)
        # print("偏航角: {}°".format(np.array([mr.get_deflection_angle()])))
        # print("距离传感器数据：{}".format(np.array(mr.get_distance_sensors_data())))
        # print("距离：{}".format(mr.get_distance()))
        # print("是否发生碰撞：{}".format(client.simGetCollisionInfo().has_collided))

    print("***********************************************************************************************************")

    for i in range(50):
        a = 1
        client.moveByVelocityAsync(vx=client.simGetGroundTruthKinematics().linear_velocity.x_val - a,
                                   vy=client.simGetGroundTruthKinematics().linear_velocity.y_val - a,
                                   vz=0,
                                   duration=0.1,
                                   drivetrain=airsim.DrivetrainType.ForwardOnly,
                                   yaw_mode=my_yaw_mode).join()
        kinematic_state = client.simGetGroundTruthKinematics()
        print("-------------------episode {} -------------------".format(i))
        position = kinematic_state.position
        print("位置: %s" % position)
        print("速度: %s" % kinematic_state.linear_velocity)
        print("加速度: %s" % kinematic_state.linear_acceleration)
        # mr.current_set(client)
        # print("偏航角: {}°".format(mr.get_deflection_angle()))
        # print("距离传感器数据：{}".format(mr.get_distance_sensors_data()))
        # print("距离：{}".format(mr.get_distance()))
        # print("是否发生碰撞：{}".format(client.simGetCollisionInfo().has_collided))

    print("***********************************************************************************************************")

    for i in range(25):
        a = 1
        client.moveByVelocityAsync(vx=client.simGetGroundTruthKinematics().linear_velocity.x_val - a,
                                   vy=client.simGetGroundTruthKinematics().linear_velocity.y_val - a,
                                   vz=client.simGetGroundTruthKinematics().linear_velocity.z_val-a*0.5,
                                   duration=0.1,
                                   drivetrain=airsim.DrivetrainType.ForwardOnly,
                                   yaw_mode=my_yaw_mode).join()
        kinematic_state = client.simGetGroundTruthKinematics()
        print("-------------------episode {} -------------------".format(i))
        position = kinematic_state.position
        print("位置: %s" % position)
        print("速度: %s" % kinematic_state.linear_velocity)
        print("加速度: %s" % kinematic_state.linear_acceleration)
        # mr.current_set(client)
        # print("偏航角: {}°".format(mr.get_deflection_angle()))
        # print("距离传感器数据：{}".format(mr.get_distance_sensors_data()))
        # print("距离：{}".format(mr.get_distance()))
        # print("是否发生碰撞：{}".format(client.simGetCollisionInfo().has_collided))

    print("***********************************************************************************************************")

    for i in range(25):
        a = 1
        client.moveByVelocityAsync(vx=client.simGetGroundTruthKinematics().linear_velocity.x_val + a,
                                   vy=client.simGetGroundTruthKinematics().linear_velocity.y_val + a,
                                   vz=client.simGetGroundTruthKinematics().linear_velocity.z_val + a*0.5,
                                   duration=0.1,
                                   drivetrain=airsim.DrivetrainType.ForwardOnly,
                                   yaw_mode=my_yaw_mode).join()
        kinematic_state = client.simGetGroundTruthKinematics()
        print("-------------------episode {} -------------------".format(i))
        position = kinematic_state.position
        print("位置: %s" % position)
        print("速度: %s" % kinematic_state.linear_velocity)
        print("加速度: %s" % kinematic_state.linear_acceleration)
        # mr.current_set(client)
        # print("偏航角: {}°".format(mr.get_deflection_angle()))
        # print("距离传感器数据：{}".format(mr.get_distance_sensors_data()))
        # print("距离：{}".format(mr.get_distance()))
        # print("是否发生碰撞：{}".format(client.simGetCollisionInfo().has_collided))

    # keyboard.press_and_release("backspace")  # 使无人机返回初始位置
    # time.sleep(1)

# 悬停 5 秒钟
client.hoverAsync().join()          # 第四阶段：悬停5秒钟
time.sleep(5)

# state = client.getMultirotorState()
# s = pprint.pformat(state)
# print("state: %s" % s)

# print("-------------------seperate-------------------")
# # 获取无人机位置，速度，加速度，角速率，角加速度，姿态角的真值
# kinematics_state = client.simGetGroundTruthKinematics()
# ks = pprint.pformat(kinematics_state)
# print("kinematics_state: %s" % ks)

client.landAsync(timeout_sec=0).join()           # 第五阶段：降落
client.armDisarm(False)             # 上锁
client.enableApiControl(False)      # 释放控制权
