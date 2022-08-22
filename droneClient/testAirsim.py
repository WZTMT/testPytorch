"""
 test python environment
 """
import airsim
import time

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

# get control
client.enableApiControl(True)

# unlock
client.armDisarm(True)

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()

client.moveToZAsync(-10, 1).join()
client.hoverAsync().join()          # 悬浮600秒钟
time.sleep(600)

client.landAsync().join()

# lock
client.armDisarm(False)

# release control
client.enableApiControl(False)
