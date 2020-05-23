from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# from pyvirtualdisplay import Display

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--kiosk")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get('https://votedev.iottalk.tw/video')

    pygame.mixer.init()
    pygame.mixer.music.load("./audio/Background.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)