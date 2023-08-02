from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self,driver):
        self.driver= driver


    checkout= (By.XPATH, "//div[@class='card h-100']")
    checkoutclick= (By.CSS_SELECTOR, "a[class*='btn-primary']")
    finalcheckpage= (By.XPATH, "//button[@class='btn btn-success']")


    def checkoutitems(self):
        return self.driver.find_elements(*CheckOutPage.checkout)

    def cartclick(self):
        return self.driver.find_element(*CheckOutPage.checkoutclick)

    def finalcartclick(self):
        return self.driver.find_element(*CheckOutPage.finalcheckpage)
