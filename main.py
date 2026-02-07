import time
# 从初始化文件导入函数和默认参数
from servo_init import init_servo_system, SERVO_ID

# 主文件中自定义COM口（可按需修改，或通过命令行/配置文件读取）
SERVO_PORT = "COM8"  # 这里可以自由修改COM口

def main():
    uart = None  # 初始化串口变量，确保finally能访问
    try:
        # 调用外部初始化函数，传入自定义COM口和舵机ID列表
        uart, servo_manager = init_servo_system(
            servo_port=SERVO_PORT,  # 传入COM口参数
            servo_ids=SERVO_ID     # 可选：自定义舵机ID列表，如[0,1,2]
        )

        # -------------------------- 核心业务逻辑 --------------------------
        # print("\n⏳ 等待2秒钟……")
        # time.sleep(2)
        # print("✅ 等待结束")

        # 舵机角度控制
        set_angle = 0 # 目标角度
        for servo_id in SERVO_ID:
            if servo_id == 5 and set_angle == 0:
                set_angle = 5 # 夹爪设置5度，防止电机堵转
            print(f"\n[单圈模式] 控制舵机ID={servo_id} 旋转到 {set_angle} 度")
            servo_manager.set_servo_angle(servo_id, set_angle, velocity= 150, t_acc= 100, t_dec= 100)
            # time.sleep(0.2)
        servo_manager.wait()


        # # 舵机阻尼模式
        # power = 100 # 阻尼功率，单位mW
        # for servo_id in SERVO_ID:
        #   print(f"\n[阻尼模式] 设置舵机ID={servo_id} 阻尼功率 {power} mW")
        #   servo_manager.set_damping(servo_id, power)
        #   time.sleep(0.2)
        # ----------------------------------------------------------------

    except Exception as e:
        print(f"\n❌ 程序执行出错：{e}")
    finally:
        # 确保串口最终关闭（无论是否异常）
        if uart and uart.is_open:
            uart.close()
            print("\n🔌 串口已关闭")

# 程序入口
if __name__ == "__main__":
    main()