from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import json
from flask import Flask

app = Flask(__name__)
@app.route('/v2/<coin>', methods=['GET'])
def index(coin):
    
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=options)
    driver.get('https://v2.info.uniswap.org/pair/'+coin)
    time.sleep(2)
    results = driver.find_elements_by_xpath("//div[contains(@class,'sc-bdVaJa KpMoH css-9on69b')]")
    pair = driver.find_elements_by_xpath("//div[contains(@class,'sc-hEsumM erpGeW')]")

    return json.dumps({'Pair': pair[1].text,
                       'Total': results[0].text,
                       'Volume': results[1].text,
                       'Fees': results[2].text,})
app.run()
