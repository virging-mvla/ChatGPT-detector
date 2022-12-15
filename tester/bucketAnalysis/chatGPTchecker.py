from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import json
import time
from os.path import exists

PATH = "/home/garv/chromeDriver/chromedriver" #add path to  your chromedriver.
driver = webdriver.Chrome(PATH)

def readFile():
    with open("GPTtexts.json", encoding="utf8") as GPTFiles:
        data = GPTFiles.read()
    gptData = json.loads(data)
    arrayOfData = {}
    for i in gptData:
        try:
            text = i["Text"]
            arrayOfData[text] = {}
            arrayOfData[text]["Green%"] = i["Green%"]
            arrayOfData[text]["Yellow%"] = i["Yellow%"]
            arrayOfData[text]["Red%"] = i["Red%"]
            arrayOfData[text]["frac"] = i["frac"]
            arrayOfData[text]["entropy"] = i["entropy"]
            arrayOfData[text]["totalVal"] = i["totalVal"]
        except:
            continue
    return(arrayOfData)

sampleDict = readFile()

for j in sampleDict :
    time.sleep(4)
    driver.get("http://gltr.io/dist/index.html")
    elem = driver.find_element(By.ID, "test_text")
    elem.clear()
    elem.send_keys(j)
    elem.send_keys(Keys.RETURN)

    button = driver.find_element(By.ID, "submit_text_btn")
    button.click()
    time.sleep(5)

    buttons = driver.find_elements(By.CLASS_NAME, "bar")
    green = buttons[0]
    yellow = buttons[1]
    red = buttons[2]
    purple = buttons[3]

    action = ActionChains(driver)
    action.move_to_element(green).perform()
    time.sleep(1)
    greenText = driver.find_element(By.CSS_SELECTOR, "#stats_top_k > g > g.fg > text")
    try : 
        numGreen = int(greenText.text)
    except :
        numGreen = 0

    action.move_to_element(yellow).perform()
    time.sleep(1)
    yellowText = driver.find_element(By.CSS_SELECTOR, "#stats_top_k > g > g.fg > text")
    try : 
        numYellow = int(yellowText.text)
    except :
        numYellow = 0

    action.move_to_element(red).perform()
    time.sleep(1)
    redText = driver.find_element(By.CSS_SELECTOR, "#stats_top_k > g > g.fg > text")
    try : 
        numRed = int(redText.text)
    except :
        numRed = 0

    action.move_to_element(purple).perform()
    time.sleep(1)
    purpleText = driver.find_element(By.CSS_SELECTOR, "#stats_top_k > g > g.fg > text")
    try :
        numPurple = int(purpleText.text)
    except :
        numPurple = 0

    finalVal = 0
    percentPredicted = numGreen / (numGreen + numYellow + numRed + numPurple)
    if percentPredicted > 0.75:
        if percentPredicted <= 0.82:
            finalVal += (75 * 0.5)
        else :
            finalVal += 75
    medians = driver.find_elements(By.CLASS_NAME, "median")
    frac = float(medians[0].text)
    entropy = float(medians[1].text)
    print(frac)
    if frac > 0.63:
        if frac <= 0.666 :
            finalVal += (25 * 0.5)
        elif frac < 0.9 :
            finalVal + 25
        else :
            finalVal += 100

    print (finalVal)
    if finalVal < 50 :
        print ("Probably Human")
    elif finalVal >= 50:
        if finalVal <= 62.5:
            print ("Possibly Human")
        elif finalVal <= 75:
            print ("Possibly AI")
        else:
            print ("AI")
    	
    sampleDict[j]["Green%"] = percentPredicted
    sampleDict[j]["Yellow%"] = numYellow
    sampleDict[j]["Red%"] = numRed
    sampleDict[j]["Purple%"] = numPurple
    sampleDict[j]["frac"] = frac
    sampleDict[j]["entropy"] = entropy
    sampleDict[j]["totalVal"] = finalVal

with open("test.json", "w") as output:
            json.dump(sampleDict, output, indent=3)


