import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutpage import CheckOutpage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utlities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getlogger()

        homePage = HomePage(self.driver)
        homePage.shopItem().click()

        checkoutPage = CheckOutpage(self.driver)
        products = checkoutPage.getProductTitles()
        log.info("Getting all cards Title")

        confirmpage = ConfirmPage(self.driver)

        i = -1
        for product in products:
            i = i+1
            productName = product.text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.AddProductBTN()[i].click()

        checkoutPage.CheckOutABTN().click()

        assert productName == "Blackberry"
        confirmpage.CheckOutBBTN().click()
        confirmpage.CountryCode().send_keys(confirmpage.Country)

        self.expicitWait("//a[contains(text(),'India')]")

        confirmpage.SelectCountry().click()
        confirmpage.AgreeCHKBox().click()
        confirmpage.PurchaseBTN().click()

        successtxt = confirmpage.ValidationTxt().text
        log.info("this is the text" +successtxt)

        assert "Success! Thank you! " in successtxt

        #self.driver.get_screenshot_as_file("screen.png")
