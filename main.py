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
