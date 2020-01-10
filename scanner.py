from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep, strftime
import pandas as pd
from random import randint
import ppp

validStars = ('ரோகிணி','ஹஸ்தம்','சதயம்','சுவாதி','உத்திரட்டாதி','பூசம்','அனுஷம்','அஸ்வினி','மகம்','மூலம்','பரணி','பூரம்','பூராடம்')
kattamPos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
kattam = {}
fileName = ''

prev_star_matching_list = []
#prev_star_matching_list = pd.read_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\starMatching\{}_starMatching.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log
#prev_star_matching_list = list(prev_star_matching_list['0'])
starMatchCount = len(prev_star_matching_list)

noHoroCount = 0

prev_horo_matching_list = []
#prev_horo_matching_list = pd.read_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\horoMatching\{}_horoMatching.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log
#prev_horo_matching_list = list(prev_horo_matching_list['0'])
horoMatchCount = len(prev_horo_matching_list)

prev_horo_not_matching_list =[]
# prev_horo_not_matching_list = pd.read_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\horoNotMatching\20200104-045249_horoNotMatching.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log
# prev_horo_not_matching_list = list(prev_horo_not_matching_list['0'])
horoNotMatchCount = len(prev_horo_not_matching_list)

previousList = prev_horo_matching_list + prev_horo_not_matching_list

chromedriver_path = r'C:\Users\Vignesh Karunagaran\AppData\Local\Programs\Python\Python37-32\Chrome Driver\newDriver\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('http://bhuvaneshwarimatrimony.com/')
sleep(3)

webdriver.find_element_by_xpath('//*[@id="MainContent_UserLogin_UserName"]').send_keys('username')
webdriver.find_element_by_xpath('//*[@id="MainContent_UserLogin_Password"]').send_keys('password')
sleep(2)
webdriver.find_element_by_xpath('//*[@id="MainContent_UserLogin_LoginButton"]').click()
sleep(5)

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
webdriver.find_element_by_xpath('//*[@id="MainContent_btnSearch"]').click()
sleep(3)

#Checks for age, height, star
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

#check for horoscope
def validateKattam(dic):
    for key, value in dic.items():
        if 'லக்னம்' in dic[key]:
            if ('ராகு' not in dic[(key + 6) % 12]) and ('கேது' not in dic[(key + 6) % 12]):
                if ('ராகு' not in dic[(key + 7) % 12]) and ('கேது' not in dic[(key + 7) % 12]):
                    return True
    return False

#screeenshot
def printScreen():
    try:
        picturName = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/strong/big').text).strip()
    except:
        picturName = 'unknown'+randint(1, 100)

    print(picturName,'> Valid')
    #prev_horo_matching_list.append(picturName)
    ppp.fullpage_screenshot(webdriver, r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\Profiles\HoroMatching\{}.png'.format(picturName))
    sleep(2)


status = input('Enter "y" to Scan Star Matching :').lower()

try:
    loop = 0
    if status == 'y':
        while True:
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
except:
    fileName = '{}_starMatching.csv'.format(strftime("%Y%m%d-%H%M%S"))
    starMatchCount = len(prev_star_matching_list)
    updated_user_df = pd.DataFrame(prev_star_matching_list)
    updated_user_df.to_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\starMatching\{}'.format(fileName))
    sleep(2)

print('Proceeding for horoscope matching')

star_matching_list = prev_star_matching_list
sleep(2)

try:
    for profile in star_matching_list:
        if profile not in previousList:
            print('verify >',profile)
            webdriver.get(profile)
            sleep(2)
            ra1 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[1]/td[1]').text).split('\n')
            ra2 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[1]/td[2]').text).split('\n')
            ra3 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[1]/td[3]').text).split('\n')
            ra4 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[1]/td[4]').text).split('\n')
            ra5 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[2]/td[3]').text).split('\n')
            ra6 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[3]/td[2]').text).split('\n')
            ra7 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[4]/td[4]').text).split('\n')
            ra8 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[4]/td[3]').text).split('\n')
            ra9 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[4]/td[2]').text).split('\n')
            ra10 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[4]/td[1]').text).split('\n')
            ra11 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[3]/td[1]').text).split('\n')
            ra12 = str(webdriver.find_element_by_xpath('//*[@id="MainContent_VPTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td/table[1]/tbody/tr[2]/td[1]').text).split('\n')
            li = [ra1, ra2, ra3, ra4, ra5, ra6, ra7, ra8, ra9, ra10, ra11, ra12]
            for key, value in zip(kattamPos,li): kattam[key] = value

            if ra1 == ra2 == ra3 == ra4 == ra5 == ra6 == ra7 == ra8 == ra9 == ra10 == ra11 == ra12:
                printScreen()
                prev_horo_matching_list.append(profile)
                noHoroCount += 1
            elif validateKattam(kattam):
                printScreen()
                prev_horo_matching_list.append(profile)
                horoMatchCount += 1
            else:
                prev_horo_not_matching_list.append(profile)
                horoNotMatchCount += 1
finally:
    fileName = '{}_horoMatching.csv'.format(strftime("%Y%m%d-%H%M%S"))
    updated_user_df = pd.DataFrame(prev_horo_matching_list)
    updated_user_df.to_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\horoMatching\{}'.format(fileName))
    sleep(2)
    fileName = '{}_horoNotMatching.csv'.format(strftime("%Y%m%d-%H%M%S"))
    updated_user_df = pd.DataFrame(prev_horo_not_matching_list)
    updated_user_df.to_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\horoNotMatching\{}'.format(fileName))
    sleep(2)
    webdriver.close()

    print('Star Match count :',starMatchCount)
    print('NoHoro Count :',noHoroCount)
    print('Horo Match Count :',horoMatchCount+noHoroCount)
    print('Horo Not Match Count :', horoNotMatchCount)
