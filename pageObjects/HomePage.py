from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver
    #driver.find_element_by_css_selector("a[href*='shop']")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
    # form_submission Test case
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    mark = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    confirm_text = (By.CSS_SELECTOR, "[class*='alert-success']")
    def get_name(self):
        return self.driver.find_element(*HomePage.name)
    def get_email(self):
        return self.driver.find_element(*HomePage.email)
    def select_checkbox(self):
        return self.driver.find_element(*HomePage.mark)
    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)
    def submission(self):
        return self.driver.find_element(*HomePage.submit)
    def get_alert_text(self):
        return self.driver.find_element(*HomePage.confirm_text)




