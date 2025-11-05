import pyvesc


from pyvesc import VESC

with VESC(serial_port='/dev/ttyUSB0',has_sensor=False,start_heartbeat=True,baudrate=115200,timeout=0.01) as drv:
    print(motor.get_rpm())


