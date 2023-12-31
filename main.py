import os
import struct
import sys

from LoliconFlash import Flash

record_max = 20  # 最大记录数


# 选择键盘设备
def choose_device():
    f = open("/proc/bus/input/handlers", "r")
    print(f.read())
    dev = str(input("Which is your keyboard(a number): "))
    return '/dev/input/event' + dev


# 终端模式
def terminal():
    userinput = str(input("0:退出 1:启动 2:测试键码: "))
    if userinput == '0':
        exit(0)
    elif userinput == '1':
        start()
    elif userinput == '2':
        f = open(choose_device(), "rb")  # 读取键盘设备
        while 1:
            data = f.read(24)
            out = struct.unpack('4IHHI', data)
            input_key = out[5]
            if out[4] == 1 and out[6] != 0:  # 按下
                print('\n')
                print(hex(input_key))


def start():
    key = [  # 关键词, 可通过
        [0x26, 0x16, 0x18, 0x26, 0x17],  # luoli
        [0x26, 0x26, 0x15]  # lly
    ]
    record = []
    f = open(choose_device(), "rb")  # 读取键盘设备
    while 1:
        data = f.read(24)
        out = struct.unpack('4IHHI', data)  # 4 unsigned int, 2 unsigned short, 1 unsigned int
        input_key = out[5]  # 按键值
        # print(out)
        if out[4] == 1 and out[6] != 0:  # 按下
            print(hex(input_key))
            if len(record) >= record_max:
                record.pop(0)  # 超过最大记录长度个按键则删除第一个
            record.append(input_key)
            # 如果按键值等于预设值
            for k in key:
                if record[-len(k):] == k:
                    Flash()


if __name__ == '__main__':
    print(os.getcwd())
    if len(sys.argv) != 1:
        print("Lolicon lolicon lolicon !")
        if sys.argv[1] == ('-t' or '-h'):
            terminal()
        elif sys.argv[1] == '-g':
            Flash()
    else:
        start()
