import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import constant as cnst
import time
class Scrapper (webdriver.Chrome):

    def __init__(self,driver_path=cnst.path, teardown = False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH'] +=self.driver_path
        super(Scrapper,self).__init__()
        self.implicitly_wait(60)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown :
            self.quit()

    def land_page(self,x):
        self.get(x)
    def find(self):
        lst = []
        rows = self.find_element(by=By.XPATH,value='//*[@id="post_185973"]/div/div[2]/div[1]/div[5]/div')
        row = rows.text
        row = row.split('\n')
        for i in range(len(row)):
            if i % 2 ==0:
                lst.append(row[i])
        print(lst)
        return lst