from numpy import ModuleDeprecationWarning
import pyautogui,time
 
print("Starting in 5 sec .....")
time.sleep(5)
ty="Pavan Bhai Party Chaheye "
  
for i in range (25):
    pyautogui.typewrite(ty)
    pyautogui.press("Enter")
