import serial
import time
import struct
from uservo import UartServoManager

SERVO_PORT = "COM10"
SERVO_BAUDRATE = 115200
SERVO_ID = 0

uart = serial.Serial(
  port= SERVO_PORT,
  baudrate= SERVO_BAUDRATE,
  parity= serial.PARITY_NONE,
  stopbits= 1,
  bytesize= 8,
  timeout= 0.05
)

print("设备扫描中……")
servo_manager = UartServoManager(
  uart,
  is_scan_servo= True,
  srv_num= 254
  )

online_servo_ids = list(servo_manager.servos.keys())
if not online_servo_ids:
    print(f"{SERVO_PORT}上未检测到任何舵机！")
else:
    print(f"{SERVO_PORT}上在线的舵机ID：{online_servo_ids}")

is_online = servo_manager.ping(SERVO_ID)
print(f"舵机ID={SERVO_ID} 在线状态: {is_online}")

uart.close()
print("串口已关闭")