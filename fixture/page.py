from cgitb import text


class PageHelper:
    def __init__(self, app):
        self.app = app

    def set_field_value_by_name(self, locator, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(locator).click()
            wd.find_element_by_name(locator).clear()
            wd.find_element_by_name(locator).send_keys(value)
