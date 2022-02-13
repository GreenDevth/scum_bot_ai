import time
import pyautogui as ai
import pygetwindow as gw


def start_game():
    time.sleep(1)
    icon = "./img/icon.PNG"
    scum = ai.locateOnScreen(icon, grayscale=True, confidence=0.9)
    ai.moveTo(scum)
    ai.doubleClick(scum)
    msg = "กำลังเริ่มเกมส์ โปรดรอสักครู่"
    return msg.strip()


def login_game():
    time.sleep(1)
    login = "./img/login.PNG"
    scum = ai.locateOnScreen(login, grayscale=True, confidence=0.9)
    ai.moveTo(scum)
    ai.click(scum)
    ai.mouseDown(button='left')
    ai.moveTo(30, 15)
    win = gw.getWindowsWithTitle('SCUM')[0]
    win.resize(640, 400)
    time.sleep(1)
    ai.keyDown('ctrl')
    ai.press('d')
    ai.keyUp('ctrl')
    ai.moveTo(80, 207)
    ai.click()
    msg = "กำลัง Login เข้าสู่เซิร์ฟเวอร์"
    return msg.strip()


def goto_home():
    time.sleep(1)
    ai.moveTo(76, 210)
    time.sleep(1)

    ai.press('x')
    time.sleep(1)
    ai.press('t')
    time.sleep(1)
    ai.press('tab')
    time.sleep(1)
    ai.write('#teleport 240715.578 81483.711 26945.559')
    time.sleep(1)
    ai.press('enter')
    time.sleep(1)
    ai.write('#announce The Bot Shop is Open.')
    time.sleep(1)
    ai.press('enter')
    msg = 'กำลังส่งบอทไปยังร้านค้า'
    return msg.strip()
