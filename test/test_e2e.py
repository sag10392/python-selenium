import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmationPage import ConfirmPage
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card details ")
        #checkOutPage = CheckOutPage(self.driver)
        #confirmPage = ConfirmPage(self.driver)
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "iphone X":
                checkoutpage.getCardFooter()[i].click()
        checkoutpage.checkOutButton().click()
        confirmpage = checkoutpage.checkOutItem()
        log.info("Entering country name as ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        #explicit wait
        self.link_presence("India")
        confirmpage.country_name().click()
        confirmpage.check_box().click()
        confirmpage.get_purchase().click()
        success_text = confirmpage.successText().text
        log.info("Text received from application")
        log.info(success_text)
        assert "Success! Thank you!" in success_text

        self.driver.save_screenshot("success.png")
