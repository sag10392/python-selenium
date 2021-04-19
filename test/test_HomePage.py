from selenium import webdriver
from selenium.webdriver.support.select import Select
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):
    def test_form_submission(self,getData):
         log = self.getLogger()
         homepage = HomePage(self.driver)
         log.info("firstname is " + getData["firstname"])
         homepage.get_name().send_keys(getData["firstname"])
         homepage.get_email().send_keys(getData["email"])
         homepage.select_checkbox().click()
         self.select_option_by_text(homepage.get_gender(),getData["gender"])
         homepage.submission().click()
         alertText = homepage.get_alert_text().text
         log.info(alertText)
         assert ("Success" in alertText)

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    #@pytest.fixture(params=HomePageData.getTestData("test-case-2"))
    def getData(self, request):
         return request.param


