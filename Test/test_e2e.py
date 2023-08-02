import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.CheckOutPage import CheckOutPage
from pageobjects.ConfirmPage import Confirmpage
from pageobjects.HomePage import HomePage
from utilities.baseclass import Baseclass


class Testone(Baseclass):

    def test_e2e(self):
        log= self.getLogger()
        homepage= HomePage(self.driver)
        # homepage.shopitems().click() (old code brfore modification)
        checkout= homepage.shopitems()


        # checkout= CheckOutPage(self.driver)  (old code brfore modification)
        products = checkout.checkoutitems()
        log.info("getting all the card titles")

        for product in products:
            productsname = product.find_element(By.XPATH, "div/h4/a").text
            if productsname == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        cartclick= CheckOutPage(self.driver)
        cartclick.cartclick().click()

        finalcheckpage= CheckOutPage(self.driver)
        finalcheckpage.finalcartclick().click()
        conformbox= Confirmpage(self.driver)
        conformbox.confirmbox().send_keys("Ind")
        self.verifylinkpresence("India")
        conformclick= Confirmpage(self.driver)
        conformclick.confirmclick().click()
        checkboxclick= Confirmpage(self.driver)
        checkboxclick.checkclick().click()
        purchaseclick= Confirmpage(self.driver)
        purchaseclick.purchasebox().click()
        alertmsg= Confirmpage(self.driver)
        successmesssage = alertmsg.alertpop().text
        log.info("Text received from the application is"+successmesssage)
        assert "Success! Thank you!" in successmesssage
        self.driver.close()






























