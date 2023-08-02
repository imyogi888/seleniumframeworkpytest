import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Testdata.HomePageData import HomePageData
from pageobjects.HomePage import HomePage
from utilities.baseclass import Baseclass


class TestHomePage(Baseclass):

    def test_formsubmisssion(self,getdata):
        log= self.getLogger()
        home= HomePage(self.driver)
        log.info("first name is"+getdata["firstname"])
        home.namebox().send_keys(getdata["firstname"])
        home.emailbox().send_keys(getdata["gmail"])
        home.passwordbox().send_keys(getdata["password"])
        home.getcheckbox().click()
        self.selectoption(home.getgender(),getdata["Gender"])
        home.radiobutton().click()


        home.submitbutton().click()
        message = home.alertmsg().text
        print(message)
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getdata(self,request):
        return request.param