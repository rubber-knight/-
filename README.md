# -
import pyautogui
import keyboard
import time
import pyperclip

def auto_typing():
    print("Enter what you want to repeat:")
    stuff_repeat = input()

    print("Switch to the interface you want to type in")
    print("Press space to start typing")

    while True:
        if keyboard.is_pressed('space'):
            break
    
    while True:
        pyperclip.copy(stuff_repeat)  # Copy the text to the clipboard
        pyautogui.hotkey('command', 'v')  # Simulate paste action

        pyautogui.press('enter')

        expected_continue_time = time.time() + 3  # replace 1 with your delay time
        while time.time() < expected_continue_time:
            if keyboard.is_pressed('space'):
                return  # if space is pressed during the delay, exit the function
                

auto_typing()


首先介绍写这个script的初心
被骗钱了，想微信轰炸，不论能不能要回钱来，先爽完再说

下面是使用教程，不会编程也能看得懂
1.检查python环境，pip装了没，把最上面import的library都装一遍，格式是 pip install library名称， 比如说装pyautogui就是 pip install pyautogui
2.打开电脑terminal/cmd
3.输入“sudo python3 ”把script文件拖进去，回车运行
4.可能要你输入密码，输入按回车就可以了
5.按照提示走，输入你想轰炸的内容
6.切换到软件，微信，qq，word随你
7.空格键开始轰炸
8.再按空格键停止
