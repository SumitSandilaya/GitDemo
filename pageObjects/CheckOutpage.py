from selenium.webdriver.common.by import By


class CheckOutpage:
    # create driver constructor
    def __init__(self, driver):
        self.driver = driver

    productTitle = (By.XPATH, "//div/h4")
    #itemName = (By.XPATH, "div/h4")
    addProduct = (By.XPATH, "//*[contains(@class, 'btn-info')]")
    chkoutABtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")



    def getProductTitles(self):
        return self.driver.find_elements(*CheckOutpage.productTitle)

    def AddProductBTN(self):
        return self.driver.find_elements(*CheckOutpage.addProduct)

    def CheckOutABTN(self):
        return self.driver.find_element(*CheckOutpage.chkoutABtn)
