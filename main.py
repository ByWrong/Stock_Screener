from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ctypes
from tkinter import *


def pop_up(title, text):
    """
    Create a pop up window function.
    """
    return ctypes.windll.user32.MessageBoxW(0, text, title, 0x1000)


def first_batch():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::0,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
    driver.implicitly_wait(1)  # wait for 1 sec
    urls = driver.find_elements_by_xpath("//a[@target='_blank']") # pass all clickable links to array

    for element in urls[:10]:
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #click escape key
        element.click() # click element in array
    pop_up('Message', 'Finished loading first 10 stocks')


def second_batch():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::0,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
    driver.implicitly_wait(1)  # wait for 1 sec
    urls = driver.find_elements_by_xpath("//a[@target='_blank']")

    for element in urls[10:20]:
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        element.click()
    pop_up('Message', 'Finished loading 11-20th stocks.')


def third_batch():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::0,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
    driver.implicitly_wait(1)  # wait for 1 sec
    urls = driver.find_elements_by_xpath("//a[@target='_blank']")

    for element in urls[20:30]:
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        element.click()
    pop_up('Message', 'Finished loading 20-30th stocks.')


def fouth_batch():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::0,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
    driver.implicitly_wait(1)  # wait for 1 sec
    urls = driver.find_elements_by_xpath("//a[@target='_blank']")

    for element in urls[30:40]:
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        element.click()

    pop_up('Message', 'Finished loading 30-40th stocks.')


def fifth_batch():
    driver = webdriver.Chrome()
    driver.get(
        'https://www.investing.com/stock-screener/?sp=country::6|sector::a|industry::a|equityType::a|RSI::0,45|yield_us::2.5,2569.1%3Ceq_market_cap;1')
    driver.implicitly_wait(1)  # wait for 1 sec
    urls = driver.find_elements_by_xpath("//a[@target='_blank']")

    for element in urls[40:50]:
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        element.click()

    pop_up('Message', 'Finished loading 40-50th stocks.')


# Code below are for UI generation.
root = Tk()

# title
root.title('Stocks Screener V.1.0.0')
# create a container
frame = LabelFrame(root, text='Good luck on your trades.', padx=10, pady=10, bg='pale green')
frame.grid(padx=5,pady=5)
# label
theLabel = Label(frame,
                 text='The stocks are ranked based on market caps.\nThe current screening parameters are: country = Canada | dividend yield > 2.5% | RSI < 45.',
                 padx=5, pady=5)
theLabel.grid(row=0, padx=5, pady=5)
# submit button
submit_button = Button(frame, text='Fetch First 10 Stocks',
                       command=lambda: first_batch())
submit_button.grid(row=1, padx=5, pady=5)
# submit button
submit_button2 = Button(frame, text='Fetch 11-20th Stocks',
                        command=lambda: second_batch())
submit_button2.grid(row=2, padx=5, pady=5)
# submit button
submit_button3 = Button(frame, text='Fetch 21-30th Stocks',
                        command=lambda: third_batch())
submit_button3.grid(row=3, padx=5, pady=5)
# submit button
submit_button4 = Button(frame, text='Fetch 31-40th Stocks',
                        command=lambda: fouth_batch())
submit_button4.grid(row=4, padx=5, pady=5)
# submit button
submit_button5 = Button(frame, text='Fetch 41-50th Stocks',
                        command=lambda: fifth_batch())
submit_button5.grid(row=5, padx=5, pady=5)

# label
theLable2 = Label(frame,
                 text='Copyright © 2020 by Byron Liu',
                 padx=5, pady=5)
theLable2.grid(row=8, padx=5, pady=5)

root.mainloop()