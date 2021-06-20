from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import json
import random
from flask import Flask
OPTIONS = Options()
#OPTIONS.add_argument("--headless")
DRIVER = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=OPTIONS)
DELAY = 1.5

def checkLiquidity(coin):
    #DRIVER.get('https://v2.info.uniswap.org/pair/'+coin)
    DRIVER.get('https://v2.info.uniswap.org/home')
    action = ActionChains(DRIVER)
    time.sleep(2)
    text = "0x63607de7ae773638d012561a01383ab8ac321371"
    search = DRIVER.find_element_by_xpath("//input[contains(@class,'sc-kafWEX dlporq')]")
    
    action.move_to_element(search)
    action.click()
    for character in text:
        #action.click()
        action.send_keys(character)
        print(character)
        time.sleep(0.01)
    action.perform()
    search.send_keys(Keys.BACK_SPACE)
    time.sleep(1)
    search.send_keys('1')
    time.sleep(2)
    pair_link = DRIVER.find_element_by_xpath("//a[contains(@class,'sc-kAzzGY gNzgwd')]")
    print(pair_link.get_attribute("href"))
    #action.move_to_element(pair_link)
    #action.click()
    DRIVER.close()
    
    #results = DRIVER.find_elements_by_xpath("//div[contains(@class,'sc-bdVaJa KpMoH css-9on69b')]")
    #pair = DRIVER.find_elements_by_xpath("//div[contains(@class,'sc-hEsumM erpGeW')]")
    #return results

#app = Flask(__name__)
#@app.route('/v2/<coin>', methods=['GET'])
#def index(coin):
    
    #results = checkLiquidity(coin)
    #return json.dumps({'Pair': results[1].text,
                       #'Total': results[0].text,
                       #'Volume': results[1].text,
                       #'Fees': results[2].text,})
#app.run()

def main():
    checkLiquidity("0x63607de7ae773638d012561a01383ab8ac321371")

if __name__ == "__main__":
    main()