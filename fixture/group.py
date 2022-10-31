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
        self.group_cache = None

    def edit(self, group: Group, index: int):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_by_index(index)
        wd.find_element_by_name("edit").click()
        self.__fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.go_to_group_page()
        self.group_cache = None

    def __fill_group_form(self, group: Group):
        self.app.page.set_field_value_by_name("group_name", group.name)
        self.app.page.set_field_value_by_name("group_header", group.header)
        self.app.page.set_field_value_by_name("group_footer", group.footer)

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//input[@type='checkbox']")[index].click()

    def select_first(self):
        self.select_by_index(0)

    def delete_first(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_by_index(index)
        wd.find_element_by_name("delete").click()
        self.go_to_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.go_to_group_page()
        return len(wd.find_elements_by_xpath("//input[@type='checkbox']"))

    group_cache = None

    def get_group_list(self):
        """
            Функция проверяет состояние кэша,
            в случае его отсутсвия анализирует записи о группах на странице:
            http://localhost/addressbook/group.php и возвращает их список.
        Returns:
            group_cache[]: лист объектов GROUP
        """
        if self.group_cache is None:
            wd = self.app.wd
            self.go_to_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
