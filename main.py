import time
# 从初始化文件导入函数和默认参数
from servo_init import init_servo_system, SERVO_ID
import sys

# 添加运动学模块路径
sys.path.append("./kinematic")
from kinematic.arm5dof_uservo import Arm5DoFUServo
# 从配置文件导入参数
# from kinematic.config import *


SERVO_PORT = 'COM8'  # 使用配置文件中的默认COM口

def main():
  # 初始化舵机系统
  servo_manager = Arm5DoFUServo(device= SERVO_PORT, is_init_pose= False)
  servo_manager.home() # 回零

  # -------------------------- 核心业务逻辑 --------------------------

  # servo_manager.set_damping(1000)
  # print(servo_manager.get_tool_pose())

  # ----------------------------------------------------------------


# 程序入口
if __name__ == "__main__":
    main()