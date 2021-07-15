from selenium.webdriver.common.by import By


class ConfirmPage:
    # create driver constructor
    def __init__(self, driver):
        self.driver = driver

    chkoutBBtn = (By.XPATH, "//*[contains(@class, 'btn-success')]")
    countrycode = (By.ID, "country")
    Country = "ind"
    selectCountryUI = "//a[contains(text(),'India')]"
    selectCountry = (By.XPATH, "//a[contains(text(),'India')]")
    agreeCHKbox = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    purchaseBTN = (By.XPATH, "//input[@type = 'submit']")
    validTxt = (By.CSS_SELECTOR, "div[class = 'alert alert-success alert-dismissible']")



    def CheckOutBBTN(self):
        return self.driver.find_element(*ConfirmPage.chkoutBBtn)

    def CountryCode(self):
        return self.driver.find_element(*ConfirmPage.countrycode)

    def SelectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def AgreeCHKBox(self):
        return self.driver.find_element(*ConfirmPage.agreeCHKbox)

    def PurchaseBTN(self):
        return self.driver.find_element(*ConfirmPage.purchaseBTN)

    def ValidationTxt(self):
        return self.driver.find_element(*ConfirmPage.validTxt)

