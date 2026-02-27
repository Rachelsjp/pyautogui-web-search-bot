
#pyautogui learning
import pyautogui
import time
import webbrowser

print("Starting automation in 2 seconds...")
time.sleep(2)

# Step 1: Open Google
webbrowser.open("https://www.google.com")
time.sleep(2)  # wait for browser to open

# Step 2: Click on Google search bar
#  You MUST adjust these coordinates
pyautogui.click(573, 414)  
time.sleep(2)

# Step 3: Type search query
pyautogui.write("today 1 gram gold rate in india", interval=0.05)
pyautogui.press("enter")

time.sleep(2)

# Step 4: Click first result (adjust coordinates)
pyautogui.click(463, 866)

print("Finished.")
