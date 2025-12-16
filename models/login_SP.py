from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.homepage=self.page.goto("https://secure.simplepractice.com")

        self.username=self.page.locator("input#user_email")
        self.password=self.page.get_by_role("textbox", name="Password")
        self.login_btn=self.page.locator("input#submitBtn")

    def login(self, username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()