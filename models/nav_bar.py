class NavBar:
    def __init__(self, page):
        self.page = page


    def navigate_to_contact_us_page(self):
        self.page.get_by_role("link", name="Contact ").click()
        self.page.get_by_label("Menu", exact=True).get_by_role("link", name="Contact Us").click()