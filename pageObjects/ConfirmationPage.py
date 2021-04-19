from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver
    #self.driver.find_element_by_link_text("India").click()

    country = (By.LINK_TEXT, "India")

    def country_name(self):
        return self.driver.find_element(*ConfirmPage.country)

    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

    term_condition = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def check_box(self):
        return self.driver.find_element(*ConfirmPage.term_condition)

#       self.driver.find_element_by_class_name("btn-success").click()
    purchase = (By.CLASS_NAME, "btn-success")

    def get_purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    #success_text = self.driver.find_element_by_css_selector(".alert-success").text
    text = (By.CSS_SELECTOR,".alert-success")
    def successText(self):
        return self.driver.find_element(*ConfirmPage.text)
