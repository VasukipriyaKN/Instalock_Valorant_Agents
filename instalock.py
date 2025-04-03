# My screen resolution is 1920x1080

import pyautogui as pg
import time

screen_width, screen_height = pg.size()

agent_coordinates = {
    "1": (0.0416 * screen_width, 0.7917 * screen_height),        # Sova
    "2": (0.0989 * screen_width, 0.7917 * screen_height),        # Tejo
    "3": (0.1406 * screen_width, 0.7917 * screen_height),        # Viper
    "4": (0.1927 * screen_width, 0.7917 * screen_height),        # Vyse
    "5": (0.0416 * screen_width, 0.6944 * screen_height),                        # Raze == 5
    "6": (0.0989 * screen_width, 0.6944 * screen_height),                        # Reyna == 6
    "7": (0.1406 * screen_width, 0.6944 * screen_height),        # Sage
    "8": (0.1927 * screen_width, 0.6944 * screen_height),        # Skye
    "9": (0.0416 * screen_width, 0.5972 * screen_height),        # Killjoy
    "10": (0.0989 * screen_width, 0.5972 * screen_height),       # Neon
    "11": (0.1406 * screen_width, 0.5972 * screen_height),       # Omen
    "12": (0.1927 * screen_width, 0.5972 * screen_height),       # Phoenix
    "13": (0.0416 * screen_width, 0.5 * screen_height),          # Harbor
    "14": (0.0989 * screen_width, 0.5 * screen_height),          # Isolde
    "15": (0.1406 * screen_width, 0.5 * screen_height),          # Jett
    "16": (0.1927 * screen_width, 0.5 * screen_height),          # Kayo
    "17": (0.0416 * screen_width, 0.4028 * screen_height),       # Cypher
    "18": (0.0989 * screen_width, 0.4028 * screen_height),       # Deadlock
    "19": (0.1406 * screen_width, 0.4028 * screen_height),       # Fade
    "20": (0.1927 * screen_width, 0.4028 * screen_height),       # Gekko
    "21": (0.0416 * screen_width, 0.3056 * screen_height),       # Astra
    "22": (0.0989 * screen_width, 0.3056 * screen_height),       # Breach
    "23": (0.1406 * screen_width, 0.3056 * screen_height),       # Brimstone
    "24": (0.1927 * screen_width, 0.3056 * screen_height),       # Chamber
}

def instalock(agent):
    pg.click(*(agent_coordinates.get(agent)))
    pg.PAUSE = 0  # Remove delay between PyAutoGUI actions. You can remove if your system doesn't handles it well.

time.sleep(1)  # When you start the script, it will wait for 1 second before executing the code. This helps you to switch to the game window.
for i in range(250):  # This loop will run 250 times. You can change the number of iterations as per your requirement.
    instalock("5")
    pg.click(950, 750)  # Click on the "Lock In" button
    pg.PAUSE = 0  # Remove delay between PyAutoGUI actions. You can remove if your system doesn't handles it well.

