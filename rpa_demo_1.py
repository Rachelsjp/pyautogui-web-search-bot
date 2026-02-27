import pyautogui
import time
#mouse operation

#pyautogui.click(100,100)

#time.sleep(2)
#pyautogui.rightClick(100,100)
#pyautogui.click(572,288)
#pyautogui.rightClick(100,100)

#pyautogui.drag(100,100, 200,200)
#pyautogui.scrolldown(500)
#time.sleep(3)
#pyautogui.click(100,100)
#time.sleep(3)
#pyautogui.typewrite("socialeagle.ai")
#pyautogui.write("python rpa_demo_1.py")
#pyautogui.press('enter')
#pyautogui.hotkey('ctrl','a')

location=pyautogui.locateOnScreen('chrome_icon.png',confidence=0.8)
print(location)
time.sleep(10)
pyautogui.click(pyautogui.center(location))

print(pyautogui.size())

ss=pyautogui.screenshot()
ss.save('demo.png')











