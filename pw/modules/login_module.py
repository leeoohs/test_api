import time

from playwright.sync_api import sync_playwright

from pw.objects.login_page import LoginPage


class LoginAction:

    def __init__(self):
         print('---------------开始登录了---------------')

    def login(self, page, username, password):
        try:
            login_page = LoginPage(page)

            frame_obj = login_page.find_login_frame()
            login_page.input_username(frame_obj, username)
            login_page.input_password(frame_obj, password)
            login_page.click_login_btn(frame_obj)
        except Exception as e:
            raise e


if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://mail.163.com')
        login_page = LoginPage(page)

        login_action = LoginAction()
        login_action.login(page, 'leeoohs', 'Ad112211..')
        time.sleep(3)
        input("登录完成，按回车键关闭浏览器...")
        browser.close()