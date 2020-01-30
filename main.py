from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from win32gui import MessageBox





driver = webdriver.Chrome()
driver.get(
    'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::13.5,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
urls = driver.find_elements_by_xpath("//a[@target='_blank']")

for element in urls[:10]:
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    element.click()


# ask if want to load next 10
MessageBox(None, 'Finished loading first 10 stocks, hit "OK" to continue loading next 10.', 'Message', 0x40000)
driver.quit()
driver = webdriver.Chrome()
driver.get(
    'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::13.5,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
urls = driver.find_elements_by_xpath("//a[@target='_blank']")

for element in urls[10:20]:
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    element.click()

# ask if want to load next 10
MessageBox(None, 'Finished loading first 10 stocks, hit "OK" to continue loading next 10.', 'Message', 0x40000)
driver.quit()
driver = webdriver.Chrome()
driver.get(
    'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::13.5,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
urls = driver.find_elements_by_xpath("//a[@target='_blank']")

for element in urls[20:30]:
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    element.click()

# ask if want to load next 10
MessageBox(None, 'Finished loading first 10 stocks, hit "OK" to continue loading next 10.', 'Message', 0x40000)
driver.quit()
driver = webdriver.Chrome()
driver.get(
    'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::13.5,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
urls = driver.find_elements_by_xpath("//a[@target='_blank']")

for element in urls[30:40]:
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    element.click()

# ask if want to load next 10
MessageBox(None, 'Finished loading first 10 stocks, hit "OK" to continue loading next 10.', 'Message', 0x40000)
driver.quit()
driver = webdriver.Chrome()
driver.get(
    'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::13.5,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
urls = driver.find_elements_by_xpath("//a[@target='_blank']")

for element in urls[40:50]:
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    element.click()

MessageBox(None, 'Finished loading all 50 stocks, good luck on your trade.', 'Message', 0x40000)