from selenium.webdriver.common.by import By

from pageobjects.CheckOutPage import CheckOutPage




class HomePage:

    def __init__(self,driver):
        self.driver= driver

    shop= (By.CSS_SELECTOR, "a[href*='shop']")
    name= (By.CSS_SELECTOR, "input[name='name']")
    email= (By.NAME,"email")
    password= (By.ID, "exampleInputPassword1")
    check= (By.ID, "exampleCheck1")
    radio= (By.CSS_SELECTOR, "#inlineRadio1")
    submit= (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")
    gender= (By.ID, "exampleFormControlSelect1")

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckOutPage(self.driver)
        return checkout

    def namebox(self):
        return self.driver.find_element(*HomePage.name)

    def emailbox(self):
        return self.driver.find_element(*HomePage.email)

    def passwordbox(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.check)

    def radiobutton(self):
        return self.driver.find_element(*HomePage.radio)

    def submitbutton(self):
        return self.driver.find_element(*HomePage.submit)

    def alertmsg(self):
        return self.driver.find_element(*HomePage.alert)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

