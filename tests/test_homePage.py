import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Testdata.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utlities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getlogger()

        homepage = HomePage(self.driver)
        homepage.uName().send_keys(getData["Fname"])
        log.info("First Name is "+ getData["Fname"])
        homepage.uemail().send_keys(getData["Email"])
        homepage.upassword().send_keys(getData["Lname"])

        self.selectDropdown(homepage.Gender(), getData["gender"])

        homepage.Icecreamcheck().click()
        homepage.Submitbtn().click()
        message = homepage.SucessMessage().text

        assert "Success! The Form has been submitted successfully!." in message

        self.driver.refresh()

        #assert 'Success! The Form has been submitted successfully!.' == message

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self, request):
        return request.param
