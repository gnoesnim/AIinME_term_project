import serial
import time

ARDUINO_PORT = 'COM10'
BAUD_RATE = 115200

num = 0
FILE_NAME = f"IMU_data_{num}.csv"

try:
    ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    print(f"{ARDUINO_PORT} successfully connected")

    header_written = False

    input("start")
    ser.write(b's')

    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        while True:
            try:
                line = ser.readline()
                data_str = line.decode('utf-8').strip()
                if data_str:
                    is_data = len(data_str) > 00 and data_str[0].isnumeric()
                    if is_data:
                        if not header_written:
                            f.write("y,p,r\n")
                            header_written = True
                        f.write(data_str + "\n")
                        print(data_str)
            except Exception as e:
                print(f"error: {e}")
except Exception as e:
    print(f"error: {e}")