from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

ids = ["buyTime machine", "buyPortal","buyAlchemy lab","buyShipment","buyMine","buyFactory","buyGrandma","buyCursor","cookie"]
elements = [driver.find_element(By.ID, value=id) for id in ids]

cookie = driver.find_element(By.ID, value="cookie")

# buy_cursor = driver.find_element(By.ID, value="buyCursor")
# buy_grandma = driver.find_element(By.ID, value="buyGrandma")
# buy_factory = driver.find_element(By.ID, value="buyFactory")
# buy_mine = driver.find_element(By.ID, value="buyMine")
# buy_shipment = driver.find_element(By.ID, value="buyShipment")
# buy_alchemylab = driver.find_element(By.ID, value="buyAlchemy lab")
# buy_portal = driver.find_element(By.ID, value="buyPortal")
# buy_timemachine = driver.find_element(By.ID, value="buyTime machine")


game_is_on = True
count = 0
while game_is_on:
    count+=1
    time.sleep(0.1)
    cookie.click()
    if count%50 == 0:           #every 5 seconds
        # buy_timemachine.click()
        # buy_portal.click()
        # buy_alchemylab.click()
        # buy_shipment.click()
        # buy_mine.click()
        # buy_factory.click()
        # buy_grandma.click()
        # buy_cursor.click()
        for element in elements:
            element.click()

    if count == 50*60:        #five minutes
        game_is_on = False

cookies_per_sec = driver.find_element(By.ID, value="cps")
print(cookies_per_sec.text)
