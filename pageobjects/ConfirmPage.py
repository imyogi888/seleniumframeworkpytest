from selenium.webdriver.common.by import By


class Confirmpage:

    def __init__(self,driver):
        self.driver= driver

    confirmpagebox= (By.ID, "country")
    confirmboxclick= (By.LINK_TEXT, "India")
    checkboxclick= (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    Purchaseclick= (By.CSS_SELECTOR, "input[type='submit']")
    Alertmsg= (By.CLASS_NAME, "alert-success")

    def confirmbox(self):
        return self.driver.find_element(*Confirmpage.confirmpagebox)

    def confirmclick(self):
        return self.driver.find_element(*Confirmpage.confirmboxclick)

    def checkclick(self):
        return self.driver.find_element(*Confirmpage.checkboxclick)

    def purchasebox(self):
        return self.driver.find_element(*Confirmpage.Purchaseclick)

    def alertpop(self):
        return self.driver.find_element(*Confirmpage.Alertmsg)



