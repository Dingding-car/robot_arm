import serial
import time
import struct
from uservo import UartServoManager

# 串口参数配置
# 报错请重新插拔串口
SERVO_PORT = "COM8"
SERVO_BAUDRATE = 115200
SERVO_ID = [i for i in range(6)] # 舵机ID号，底座为0，依次递增

# 选择要控制的舵机ID
id = 2

# 初始化串口
uart = serial.Serial(
  port= SERVO_PORT,
  baudrate= SERVO_BAUDRATE,
  parity= serial.PARITY_NONE,
  stopbits= 1,
  bytesize= 8,
  timeout= 0.05
)

# 初始化舵机管理器
print("设备扫描中……")
servo_manager = UartServoManager(
  uart,
  is_scan_servo= True,
  srv_num= 254
  )

# 检测在线舵机
online_servo_ids = list(servo_manager.servos.keys())
if not online_servo_ids:
    print(f"{SERVO_PORT}上未检测到任何舵机！")
else:
    print(f"{SERVO_PORT}上在线的舵机ID：{online_servo_ids}")

is_online = servo_manager.ping(SERVO_ID[id])
print(f"舵机ID= {SERVO_ID[id]} 在线状态: {is_online}")

# 等待时间
print("等待2秒钟……")
time.sleep(2)
print("等待结束")

# 舵机角度控制
set_angle = 0
print(f"[单圈模式] 将舵机ID= {SERVO_ID[id]} 旋转到 {set_angle} 度")
servo_manager.set_servo_angle(SERVO_ID[id], set_angle, interval= 0)
servo_manager.wait()

# 关闭串口
uart.close()
print("串口已关闭")