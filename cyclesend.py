"""
该程序模拟手动敲击键盘发送消息的流程
当前qq聊天框需要是想要发送的对象（谨慎点，小心发群里）
如果想要发送中文，运行时输入法需要是中文
运行指令: python cyclesend.py
"""

import pyautogui as gui
import time
import random


def send(txt="woaini"):
    gui.typewrite(message=txt)    # 在当前对话框键入文字
    gui.hotkey("space")    # 选中中文输入法的内容
    gui.hotkey("enter")    # 发送


if __name__ == "__main__":
    gui.hotkey("ctrl","alt","z")    # 模拟组合键，打开qq

    while(True):
        time.sleep(random.randint(10, 30))    # 间隔10到30秒
        send("woaini")    # 发送消息