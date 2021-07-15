from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    icecreamcheck = (By.ID, "exampleCheck1")
    submitbtn = (By.XPATH, "//input[@value = 'Submit']")
    sucessMessage = (By.CSS_SELECTOR, "div[class *='alert-success']")

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)

    def uName(self):
        return self.driver.find_element(*HomePage.name)

    def uemail(self):
        return self.driver.find_element(*HomePage.email)

    def upassword(self):
        return self.driver.find_element(*HomePage.password)

    #def udropdown(self):
       # return self.driver.find_element(*HomePage.dropdown)

    def Icecreamcheck(self):
        return self.driver.find_element(*HomePage.icecreamcheck)

    def Submitbtn(self):
        return self.driver.find_element(*HomePage.submitbtn)

    def SucessMessage(self):
        return self.driver.find_element(*HomePage.sucessMessage)

    def Gender(self):
        return self.driver.find_element(*HomePage.gender)



