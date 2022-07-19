import pyautogui

pyautogui.alert("Hello world!")

password = pyautogui.prompt("What is the password??")

if password == 'lalu':
    pyautogui.alert("good")
else:
    pyautogui.alert("NO WRONG")