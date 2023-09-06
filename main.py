import selenium
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
from csv import reader
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def duration_split(duration):
    hour = 0
    min = 0
    sec = 0
    list = duration.split(":")
    hour = int(list[0])
    min = int(list[1])
    sec = int(list[2])
    return hour*3600 + min*60 + sec

def Connecting_To_Browser(id_str, pass_str, TimeLine1, LinkView1):
    if id_str != "" and pass_str != "":

        dur1 = TimeLine1
        dur1 = duration_split(dur1)

        loop = 999999999


        while loop:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
            chrome_options.add_argument("--mute-audio")
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-web-security')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            browser = webdriver.Chrome(options=chrome_options)

            browser.get('https://accounts.google.com/')

            email_field = browser.find_element(By.ID, "identifierId")
            email_field.clear()
            email_field.send_keys(id_str)
            email_next_button = browser.find_element(By.ID, "identifierNext")
            email_next_button.click()

            time.sleep(5)

            password_field = browser.find_element(By.NAME, "Passwd")
            password_field.send_keys(pass_str)
            password_next_button = browser.find_element(By.ID, "passwordNext")
            password_next_button.click()

            time.sleep(5)
            browser.get(LinkView1)
            time.sleep(dur1)
            browser.close()
            loop -= 1

    else:
        print("Either ID or PASSWORD is null")

    


with open('id_google.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

#print("Total Ids and Passwords: ", len(list_of_rows))
total_Len = len(list_of_rows)

ids_pass_list = list_of_rows

for i in range(len(ids_pass_list)):
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    TimeLine1 = ids_pass_list[i][2]
    LinkView1 = ids_pass_list[i][3]
    print(i)
    print("Login Id: ", id_str)
    print("Starting Crome Browser")

    Connecting_To_Browser(id_str, id_pass, TimeLine1, LinkView1)
