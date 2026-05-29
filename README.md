# 🚀 PyAutoGUI Google Search Automation Demo

---

## **Description**

This is a beginner-level automation project created to learn and demonstrate the capabilities of the Python **PyAutoGUI** library.

The script automates a simple web browsing task by:

- Opening Google in the default browser
- Entering a search query automatically
- Executing the search
- Clicking on a search result

The project was developed as a hands-on study exercise to understand GUI automation concepts such as mouse control, keyboard input simulation, screen coordinate interaction, and browser automation.

---

## **Author**

**Rachel Purnima Johnpeter**

This project was created as a learning and study exercise for Python automation using PyAutoGUI.

---

## **Tech Stack**

- Python 3.x
- PyAutoGUI
- Webbrowser Module
- Time Module

---

## **Features**

- Opens Google automatically in the default browser
- Clicks on the Google search box using screen coordinates
- Types a search query automatically
- Presses Enter to execute the search
- Clicks on a search result automatically
- Demonstrates mouse and keyboard automation

---

## **How It Works**

### **Step 1**
The script waits for 2 seconds before starting.

### **Step 2**
Google is opened in the default web browser.

### **Step 3**
PyAutoGUI clicks on the Google search box using predefined screen coordinates.

### **Step 4**
The script types the following query:

```text
today 1 gram gold rate in india
```

### **Step 5**
The Enter key is pressed to perform the search.

### **Step 6**
The script clicks on a search result using predefined screen coordinates.

---

## **Learning Objectives**

This project helped in understanding:

- GUI Automation using PyAutoGUI
- Mouse Click Automation
- Keyboard Input Automation
- Browser Interaction through Python
- Screen Coordinate-Based Automation
- Timing and Synchronization using Python

---

## **Project Structure**

```python
import pyautogui
import time
import webbrowser
```

Main modules used:

- pyautogui
- time
- webbrowser

---

## **Installation**

Install PyAutoGUI:

```bash
pip install pyautogui
```

Run the script:

```bash
python pyautogui_web_search_bot.py
```

---

## **Important Note**

This script uses fixed screen coordinates:

```python
pyautogui.click(573, 414)
pyautogui.click(463, 866)
```

These coordinates may vary depending on:

- Screen resolution
- Browser size
- Display scaling settings
- Operating system

You may need to adjust the coordinates for your system before running the script.

---

## **Future Improvements**

- Dynamic image recognition instead of fixed coordinates
- Voice-controlled automation
- Multi-browser support
- Selenium integration
- AI-powered task automation
- Automated data extraction and reporting

---

## **Disclaimer**

This project is intended for educational and learning purposes only.

It was created to study GUI automation concepts using Python and PyAutoGUI.
