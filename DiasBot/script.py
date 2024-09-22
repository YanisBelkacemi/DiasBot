#script.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
import colorama
from colorama import Fore , init
#clear terminal
import os

try:
    os.system("cls")
except:
    os.system('clear')


#logo
init(autoreset=True)
print (Fore.GREEN + """
██████╗ ██╗ █████╗ ███████╗██████╗  ██████╗ ████████╗
██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██║  ██║██║███████║███████╗██████╔╝██║   ██║   ██║   
██║  ██║██║██╔══██║╚════██║██╔══██╗██║   ██║   ██║   
██████╔╝██║██║  ██║███████║██████╔╝╚██████╔╝   ██║   
╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝    ╚═╝ 
""" + "\n")


# warning output

init(autoreset=True)
print(Fore.RED + 'Be carefull Using this script many times in row may harm you account !!!\n"Ctrl+c" to quit ')


#Your input
username = input('Enter your Username : ')
password = input('Enter your Password : ')
#victim name and number
victimeUsername = input('Enter your victime username : ')
number = input('Number of spam messages : ')
message = input('Message You want send : ')

class InstaScript:
    def __init__(self, username, password, victim_username, number):
        self.username = username
        self.password = password
        self.victim_username = victim_username
        self.number = number
        self.browser = webdriver.Firefox()

    def login(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #opening instagram.com
        browser.get('http://instagram.com/')
        #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
        browser.find_element(By.XPATH,"//input[@name='username']").send_keys(self.username)
        browser.find_element(By.XPATH,"//input[@name='password']").send_keys(self.password)
        #findind login button and clicking it
        browser.find_element(By.XPATH,"//button[@type='submit']").click()
        #-------login process ends
        browser.implicitly_wait(15)
        browser.find_element(By.XPATH, '//button[@type="button"]').click()
        browser.implicitly_wait(15)
    def victim_profile(self):
        browser = self.browser
        browser.implicitly_wait(5)
        #Clicking "Not Now" in pop up just after login
        sleep(2.5)
        
        #sleep(2)



        #not_now_notif = browser.find_element(By.XPATH,"//button[text()='Plus tard']")
        #not_now_notif.click()

            #click search bar
        browser.find_element(By.PARTIAL_LINK_TEXT,"Recherche").click()
            #enter victim's username and clicking Search
        browser.find_element(By.XPATH,"//input[@placeholder='Rechercher']").send_keys(self.victim_username)
        sleep(1)
        #open victim's profile
        browser.find_element(By.XPATH,"//a[@href='/"+self.victim_username+"/']").click()
        sleep(2)

        #-------search for username stops

    def spamming(self):
        browser = self.browser
        browser.implicitly_wait(5)
        sleep(5)
        #-------spamming begins
        #click message buttom
        browser.find_element(By.XPATH,"//div[text()='Contacter']").click()
        #input random messages 100 times
        sleep(5)
        not_now_button = browser.find_element(By.XPATH,"//button[text()='Plus tard']")
        not_now_button.click()
        sleep(5)
        div_element = browser.find_element(By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1i64zmx xw3qccf x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
        browser.execute_script("arguments[0].scrollIntoView(true);", div_element)
        div_element.click()
        sleep(5)
        div_element.send_keys(message, Keys.ENTER)
        number_of_messages = 0
        for _ in range(0, self.number):
            number_of_messages += 1
            message_area = browser.find_element(By.XPATH,"//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1i64zmx xw3qccf x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
            message_area.click()
            message_area.send_keys(message, Keys.ENTER)
            print(Fore.LIGHTGREEN_EX+'sended messages ----------->  '+str(number_of_messages))
        browser.close()



if __name__ == '__main__':
        Instagram_Spam_Bot = InstaScript(username, password, victimeUsername, int(number))
        Instagram_Spam_Bot.login()
        Instagram_Spam_Bot.victim_profile()
        Instagram_Spam_Bot.spamming()
