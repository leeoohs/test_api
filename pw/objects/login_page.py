import time

from playwright.sync_api import sync_playwright

from pw.util.locator_util import Locator


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.locator = Locator(self.page)

    def find_login_frame(self):
        """查找frame"""
        return self.locator.find_frame('//html//body//div[3]//div[3]//div[1]//div//div[3]//div[1]//div[2]//iframe')

    def input_username(self, frame, username):
        """输入用户名"""
        self.locator.locator_element('[placeholder=邮箱账号或手机号码]', frame=frame).fill(username)

    def input_password(self, frame, password):
        """输入密码"""
        self.locator.locator_element('#pwdtext', frame=frame).fill(password)

    def click_login_btn(self, frame):
        """点击登录按钮"""
        self.locator.locator_element('#dologin', frame=frame).click()


if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://mail.163.com')
        login_page = LoginPage(page)

        frame_obj = login_page.find_login_frame()
        login_page.input_username(frame_obj, 'leeoohs')
        login_page.input_password(frame_obj, 'Ad112211..')
        login_page.click_login_btn(frame_obj)
        time.sleep(3)
        input("登录完成，按回车键关闭浏览器...")
        browser.close()
