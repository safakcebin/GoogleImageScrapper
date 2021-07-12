from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import time
import csv

class getImgUrl:
    def main(self,link):
        options = Options()
        options.headless = True # keeps selenium browser private
        browser = webdriver.Firefox(options=options)
        browser.get(link) #opens the google image in the given link
        time.sleep(3) #delay to wait for page to load

        selectImg = browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
        selectImg.click() #selects 0 indexed images from google images 
        time.sleep(2) #delay to wait for page to load

        imagelink = browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img')
        src = imagelink.get_attribute("src") #Gets the source of the clicked image with index 0
        self.save(src)
        browser.close()

    def save(self,source):        
        file_exists = os.path.isfile("out.csv")
        url_dict = {"url":source}

        with open('out.csv', 'a+', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=url_dict.keys())
            if not file_exists:
                w.writeheader()
            w.writerow(url_dict)

def getData():
    # # # this is where you need to edit by data type # # #
    with open('imglink.csv', 'r') as file:
        reader = csv.reader(file)
        array = []
        for row in reader:
            array.append(row)
    return array

def main(data):
    for item in data:
        getImgUrl().main(item[1])

data = getData()
main(data)
