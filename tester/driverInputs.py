from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json
import time
from os.path import exists

class driverInputs(object) :
    #, numGreen, numYellow, numRed, numPurple, frac

    def __init__(self, input_text) :
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        #self.driver = webdriver.Chrome()
        self.driver.get("http://gltr.io/dist/index.html")
        self.numGreen = 0
        self.numYellow = 0
        self.numRed = 0
        self.numPurple = 0
        self.frac = 0
        self.input_text = input_text

    def loadPage(self) :
        elem = self.driver.find_element(By.ID, "test_text")
        elem.clear()
        elem.send_keys(self.input_text)

        button = self.driver.find_element(By.ID, "submit_text_btn")
        button.click()
        time.sleep(2)

    def findButton(self, action, ele) :
        #time.sleep(1)
        action.move_to_element(ele).perform()
        time.sleep(1)
        currText = self.driver.find_element(By.CSS_SELECTOR, "#stats_top_k > g > g.fg > text")
        try :
            return int(currText.text)
        except :
            return 0

    def getButtons(self) :
        buttons = self.driver.find_elements(By.CLASS_NAME, "bar")
        green = buttons[0]
        yellow = buttons[1]
        red = buttons[2]
        purple = buttons[3]

        action = ActionChains(self.driver)
        self.numGreen = self.findButton(action, green)
        self.numYellow = self.findButton(action, yellow)
        self.numRed = self.findButton(action, red)
       #time.sleep(3)
        self.numPurple = self.findButton(action, purple)
        print (self.numGreen)
        print (self.numYellow)
        print (self.numRed)
        print (self.numPurple)

        medians = self.driver.find_elements(By.CLASS_NAME, "median")
        self.frac = float(medians[0].text)
        print (self.frac)
