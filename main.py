from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import date

politician_names = []
political_party = []
congressional_house = []
Representative_state = []
stock_name = []
stock_ticker = []
traded_date = []
stock_traded_owner = []
trade_type = []
trade_amount = []
#Created the lists to house the data pulled and store

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Firefox()
website_html = driver.get("https://www.capitoltrades.com/trades")
#Selenium Pathing to website

driver.find_element(By.XPATH, "/html/body/div/main/main/article/section/div[1]/div[8]/div").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/ul/li[1]/label/input").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/ul/li[2]/label/input").click()
#Selecting Transaction Types Buy and Sell

driver.find_element(By.XPATH, "/html/body/div/main/main/article/section/div[1]/div[7]/div").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/ul/li[4]/label/input").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/ul/li[9]/label/input").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/ul/li[17]/label").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/ul/li[18]/label/input").click()
#Clicking ETF, Mutual Fund, REIT, and Stock

driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/button[2]").click()
#Clicking the Only Analytics Button to remove the banner

driver.find_element(By.XPATH, "/html/body/div/main/main/article/section/div[3]/div[2]/div[2]/div/div/div").click()
#Clicking dropdown for number of entries visible

#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/article/div/article/header/div[2]/a/span"))).click()
#Waiting for the popup to appear so to click the X on it

#driver.find_element(By.XPATH, "/html/body/div/div/main/div/article/section/div[2]/div[2]/div/div/div/div/span").click()
#Clicking dropdown for number of entries visible again

driver.find_element(By.XPATH, "/html/body/div/div/ul/li[4]/label/input").click()
#Clicking the 96 entries selection

time.sleep(2)
#Letting the webpage load correctly

current_page_number = 1
end_page_number = int(driver.find_element(By.XPATH, "/html/body/div/main/main/article/section/div[3]/div[2]/div[1]/p[1]/b[2]").text)
while current_page_number <= end_page_number - 1:
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    trades = soup.find('tbody')
    for trade in trades:
        politician_name = trade.find('a', class_='text-txt-interactive').text
        politician_names.append(politician_name)
        politician_other_info = trade.find('div', class_='q-fieldset politician-info').text
        if len(politician_other_info) == 15:
            politician_party = politician_other_info[:8]
            congress = politician_other_info[8:13]
            State = politician_other_info[13:15]
        elif len(politician_other_info) == 16:
            politician_party = politician_other_info[:8]
            congress = politician_other_info[8:14]
            State = politician_other_info[14:16]
        elif len(politician_other_info) == 17:
            politician_party = politician_other_info[:10]
            congress = politician_other_info[10:15]
            State = politician_other_info[15:17]
        else:
            politician_party = politician_other_info[:10]
            congress = politician_other_info[10:16]
            State = politician_other_info[16:18]

        political_party.append(politician_party)
        congressional_house.append(congress)
        Representative_state.append(State)
        traded_stock_name = trade.find('h3', class_='q-fieldset issuer-name').text
        stock_name.append(traded_stock_name)
        traded_stock_ticker = trade.find('span', class_='q-field issuer-ticker').text[:-3]
        stock_ticker.append(traded_stock_ticker)
        traded_date_info = trade.find('div', class_='q-cell cell--tx-date')
        stock_traded_date = traded_date_info.find('div', class_='text-size-3 font-medium').text.strip() + ', ' + traded_date_info.find(
            'div', class_='text-size-2 text-txt-dimmer').text
        traded_date.append(stock_traded_date)
        stock_owner = trade.find('div', class_='q-cell cell--owner').text.strip()
        stock_traded_owner.append(stock_owner)
        stock_trade_type = trade.find('div', 'q-cell cell--tx-type').text.strip()
        trade_type.append(stock_trade_type)
        stock_trade_amount = trade.find('div', class_='q-cell cell--trade-size').text.strip()
        trade_amount.append(stock_trade_amount)
    driver.find_element(By.XPATH, "/html/body/div/main/main/article/section/div[3]/div[2]/div[1]/button[3]/a").click()
    current_page_number = current_page_number + 1
    time.sleep(1)
# For loop to iterate through the webpage and pull the data from each entry in the webpage list until it reaches the last page

time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'lxml')
trades = soup.find('tbody')
for trade in trades:
    politician_name = trade.find('a', class_='text-txt-interactive').text
    politician_names.append(politician_name)
    politician_other_info = trade.find('div', class_='q-fieldset politician-info').text
    if len(politician_other_info) == 15:
        politician_party = politician_other_info[:8]
        congress = politician_other_info[8:13]
        State = politician_other_info[13:15]
    elif len(politician_other_info) == 16:
        politician_party = politician_other_info[:8]
        congress = politician_other_info[8:14]
        State = politician_other_info[14:16]
    elif len(politician_other_info) == 17:
        politician_party = politician_other_info[:10]
        congress = politician_other_info[10:15]
        State = politician_other_info[15:17]
    else:
        politician_party = politician_other_info[:10]
        congress = politician_other_info[10:16]
        State = politician_other_info[16:18]

    political_party.append(politician_party)
    congressional_house.append(congress)
    Representative_state.append(State)
    traded_stock_name = trade.find('h3', class_='q-fieldset issuer-name').text
    stock_name.append(traded_stock_name)
    traded_stock_ticker = trade.find('span', class_='q-field issuer-ticker').text[:-3]
    stock_ticker.append(traded_stock_ticker)
    traded_date_info = trade.find('div', class_='q-cell cell--tx-date')
    stock_traded_date = traded_date_info.find('div', class_='q-value').text.strip() + ', ' + traded_date_info.find(
        'div', class_='q-label').text
    traded_date.append(stock_traded_date)
    stock_owner = trade.find('div', class_='q-cell cell--owner').text.strip()
    stock_traded_owner.append(stock_owner)
    stock_trade_type = trade.find('div', 'q-cell cell--tx-type').text.strip()
    trade_type.append(stock_trade_type)
    stock_trade_amount = trade.find('div', class_='q-cell cell--trade-size').text.strip()
    trade_amount.append(stock_trade_amount)
# For loop to pull the last page of information

compiled_lists = {'Names': politician_names, 'Political_Party': political_party,
                  'Congressional_House': congressional_house, "Representative_State": Representative_state,
                  'Stock_name': stock_name,
                  'Stock_Ticker': stock_ticker, 'Traded_Date': traded_date, 'Stock_Owner': stock_traded_owner,
                  'Trade_Type': trade_type, 'Trade_Amount': trade_amount}
df = pd.DataFrame(compiled_lists)
# Turned the various lists into a combined dataframe

df.to_excel('C:/Users/nicka/PycharmProjects/Webscraping_script_v2/Congressional_Trades_Capital_Trades_' + str(
    date.today()) + '.xlsx')
# Exported as a csv file


# NOTE: USE soup var to get data, contained the entire script, compared to finding select elements that dont load all of the scripts

# To see the html text correctly, use the prettify function, if printing, use only on final html code u want to see