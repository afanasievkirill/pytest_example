from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def go_to_group_page(self):
        wd = self.app.wd
        if not (
            wd.current_url.endswith("/group.php")
            and len(wd.find_elements_by_name("new")) > 0
        ):
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
        self.go_to_group_page()
        self.select_first()
        wd.find_element_by_name("edit").click()
        self.__fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.go_to_group_page()

    def __fill_group_form(self, group: Group):
        self.app.page.set_field_value_by_name("group_name", group.name)
        self.app.page.set_field_value_by_name("group_header", group.header)
        self.app.page.set_field_value_by_name("group_footer", group.footer)

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@type='checkbox'][1]").click()

    def delete(self):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_first()
        wd.find_element_by_name("delete").click()
        self.go_to_group_page()

    def count(self):
        wd = self.app.wd
        self.go_to_group_page()
        return len(wd.find_elements_by_xpath("//input[@type='checkbox']"))

    def get_group_list(self):
        """
            Функция пербирает записи на странице
            http://localhost/addressbook/group.php и возвращает их список.
        Returns:
            group[]: лист объектов GROUP
        """
        wd = self.app.wd
        self.go_to_group_page()
        group_list = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            group_list.append(Group(name=text, id=id))
        return group_list
