import serial
from uservo import UartServoManager

# -------------------------- 可配置默认参数（非COM口） --------------------------
# DEFAULT_BAUDRATE = 115200  # 波特率默认值
SERVO_ID = [i for i in range(6)]  # 舵机ID默认列表
# -----------------------------------------------------------------------------

def init_servo_serial(servo_port, servo_baudrate= 115200):
    """
    初始化舵机串口
    :param servo_port: 串口端口（如"COM8"、"/dev/ttyUSB0"）
    :return: 初始化后的串口对象
    """
    try:
        uart = serial.Serial(
            port=servo_port,
            baudrate=servo_baudrate,
            parity=serial.PARITY_NONE,
            stopbits=1,
            bytesize=8,
            timeout=0.05
        )
        print(f"✅ 串口 [{servo_port}] 初始化成功")
        return uart
    except Exception as e:
        raise RuntimeError(f"❌ 串口 [{servo_port}] 初始化失败：{e}")

def init_servo_manager(uart, servo_port):
    """
    初始化舵机管理器，并扫描在线舵机
    :param uart: 已初始化的串口对象
    :param servo_port: 串口端口
    :return: 舵机管理器对象
    """
    print("🔍 设备扫描中……")
    servo_manager = UartServoManager(
        uart,
        is_scan_servo=True,
        srv_num=10
    )
    # 检测全局在线舵机
    online_servo_ids = list(servo_manager.servos.keys())
    if not online_servo_ids:
        print(f"⚠️ {servo_port} 上未检测到任何舵机！")
    else:
        print(f"✅ {servo_port} 在线舵机ID：{online_servo_ids}")
    return servo_manager

def check_servo_online(servo_manager, servo_ids):
    """
    检测指定ID的舵机在线状态
    :param servo_manager: 舵机管理器对象
    :param servo_ids: 需检测的舵机ID列表
    """
    for servo_id in servo_ids:
        is_online = servo_manager.ping(servo_id)
        print(f"📌 舵机ID={servo_id} 在线状态: {is_online}")

def init_servo_system(servo_port, servo_baudrate=115200, servo_ids=SERVO_ID):
    """
    一站式初始化：串口 + 舵机管理器 + 在线检测
    :param servo_port: 串口端口（外部传入）
    :param servo_ids: 需检测的舵机ID列表（可选，默认0-5）
    :return: (uart, servo_manager) 串口对象、舵机管理器对象
    """
    uart = init_servo_serial(servo_port, servo_baudrate)  # 初始化串口
    servo_manager = init_servo_manager(uart, servo_port)  # 初始化管理器
    check_servo_online(servo_manager, servo_ids)          # 检测指定舵机在线状态
    return uart, servo_manager