from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver
    #self.driver.find_elements_by_css_selector(".card-title a")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)
    #self.driver.find_elements_by_css_selector(".card-footer button")[i].click()
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

     #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    def checkOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

     # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    checkout_item = (By.XPATH, "//button[@class='btn btn-success']")
    def checkOutItem(self):
        self.driver.find_element(*CheckOutPage.checkout_item).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page