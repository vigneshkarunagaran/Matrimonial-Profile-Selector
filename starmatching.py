from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep, strftime
import pandas as pd

#Preface
validStars = ('ரோகிணி','ஹஸ்தம்','சதயம்','சுவாதி','உத்திரட்டாதி','பூசம்','அனுஷம்','அஸ்வினி','மகம்','மூலம்','பரணி','பூரம்','பூராடம்')
prev_star_matching_list = []
#prev_star_matching_list = pd.read_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\starMatching\hrefCSV\{}_starMatching.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log
#prev_star_matching_list = list(prev_star_matching_list['0'])

#web driver
chromedriver_path = r'C:\Users\Vignesh Karunagaran\AppData\Local\Programs\Python\Python37-32\Chrome Driver\newDriver\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('http://bhuvaneshwarimatrimony.com/')
sleep(3)

#User name password
webdriver.find_element_by_xpath('//*[@id="MainContent_UserLogin_UserName"]').send_keys('username')
webdriver.find_element_by_xpath('//*[@id="MainContent_UserLogin_Password"]').send_keys('password')
sleep(2)

#click on login
webdriver.find_element_by_xpath('//*[@id="MainContent_UserLogin_LoginButton"]').click()
sleep(5)

#filter
webdriver.find_element_by_xpath('//*[@id="rblLookSex_1"]').click()
cast = Select(webdriver.find_element_by_xpath('//*[@id="ddCaste"]'))
cast.select_by_visible_text('அகமுடையார்')
fromAge = webdriver.find_element_by_xpath('//*[@id="txtFromAge"]')
fromAge.clear()
fromAge.send_keys('29')
toAge = webdriver.find_element_by_xpath('//*[@id="txtToAge"]')
toAge.clear()
toAge.send_keys('32')
sleep(1)

#search
webdriver.find_element_by_xpath('//*[@id="MainContent_btnSearch"]').click()
sleep(5)

def validate(xPath):
    href = str(webdriver.find_element_by_xpath(xPath+'tr[1]/td[2]/a').get_attribute("href")).strip()
    if href not in prev_star_matching_list:
        age = int(str(webdriver.find_element_by_xpath(xPath+'tr[2]/td[2]').text).strip())
        height = int(str(webdriver.find_element_by_xpath(xPath+'tr[2]/td[4]').text).strip())
        star = str(webdriver.find_element_by_xpath(xPath+'tr[3]/td[4]').text).strip()
        if age >= 28:
            if age <= 32:
                if height > 163:
                    if star in validStars:
                        prev_star_matching_list.append(href)



status = input('Enter "y" to continue :').lower()

try:
    loop = 0
    while status == 'y':
        loop += 1
        if (loop == 1):
            a, b = 2, 12
        else:
            a, b = 4, 14

        for page in range(a, b):
            pageElement = '//*[@id="MainContent_gridBasicSearch"]/tbody/tr[7]/td/table/tbody/tr/td[' + str(page) + ']'
            for i in range(2, 7):
                xPath = '//*[@id="MainContent_gridBasicSearch"]/tbody/tr[' + str(i) + ']/td/table/tbody/'
                validate(xPath)
            sleep(2)
            webdriver.find_element_by_xpath(pageElement).click()
            sleep(3)
        status = input('Enter "y" to continue :').lower()
finally:
    updated_user_df = pd.DataFrame(prev_star_matching_list)
    updated_user_df.to_csv(
        r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\starMatching\hrefCSV\{}_starMatching.csv'.format(strftime("%Y%m%d-%H%M%S")))

