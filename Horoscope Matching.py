from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep, strftime
import pandas as pd
from random import randint
import ppp
kattamPos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
kattam = {}
fileName = ''

star_matching_list = pd.read_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\starMatching\20200104-042502_starMatching.csv', delimiter=',').iloc[:,1:2]
star_matching_list = list(star_matching_list['0'])
sleep(2)
starMatchCount = len(star_matching_list)

noHoroCount = 0

prev_horo_matching_list = []
# prev_horo_matching_list = pd.read_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\horoMatching\20200104-045249_horoMatching.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log
# prev_horo_matching_list = list(prev_horo_matching_list['0'])
horoMatchCount = len(prev_horo_matching_list)

prev_horo_not_matching_list =[]
# prev_horo_not_matching_list = pd.read_csv(r'F:\PyCharm\ToPlay\bhuvaneshwarimatrimony\csvFolder\horoNotMatching\20200104-045249_horoNotMatching.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log
# prev_horo_not_matching_list = list(prev_horo_not_matching_list['0'])
horoNotMatchCount = len(prev_horo_not_matching_list)

previousList = prev_horo_matching_list + prev_horo_not_matching_list
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

#status = input('Enter "y" to continue :').lower()
print('Proceeding for horo scope match')


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
