from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def go_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group: Group):
        wd = self.app.wd
        self.go_to_group_page()
        wd.find_element_by_name("new").click()
        self.__fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.go_to_group_page()

    def edit(self, group: Group):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()
        self.__fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.go_to_group_page()

    def __fill_group_form(self, group: Group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@type='checkbox'][1]").click()

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()
        self.go_to_group_page()
