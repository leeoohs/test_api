import time

from playwright.sync_api import sync_playwright

from pw.util.locator_util import Locator

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://mail.163.com')
    page.wait_for_load_state("load")  # 等待所有资源加载完成
    time.sleep(2)  # 额外等待动态渲染

    # --------------------------------V1-----------------------------------------
    # # 登录操作
    # # frame
    # frame = page.frame_locator('//html//body//div[3]//div[3]//div[1]//div//div[3]//div[1]//div[2]//iframe')
    # frame.get_by_placeholder('邮箱账号或手机号码').fill('leeoohs')
    # frame.locator('#pwdtext').fill('Ad112211..')
    # frame.locator('#dologin').click()
    # time.sleep(3)
    #
    # # 写信
    # write_btn = page.get_by_role('button',  name='写 信')
    # write_btn.wait_for(state="visible", timeout=10000)  # 等待按钮可见
    # write_btn.click()
    # time.sleep(3)  # 等待写信页面加载完成
    #
    # # 切换到写信浮层的iframe（收件人 / 主题都在这个iframe内）
    # # letter_frame = page.frame_locator(".nui-iframe")  # 写信浮层固定iframe class
    # # 等待iframe内的收件人输入框可见，确认iframe加载完成
    # # letter_frame.locator(".nui-editableAddr-ipt").wait_for(state="visible", timeout=15000)
    #
    # # 收件人
    # recipient_input = page.locator(".nui-editableAddr-ipt")
    # # 滚动到元素（避免被侧边栏遮挡）
    # recipient_input.scroll_into_view_if_needed()
    # # 等待元素可见+可编辑
    # recipient_input.wait_for(state="visible", timeout=10000)
    # recipient_input.fill('leeoohs@sina.com')
    # time.sleep(1)
    #
    # # 主题
    # subject_input = page.locator('//html//body//div[2]//div[1]//div[2]//div[1]//section//header//div[2]//div[1]//div//div//input')
    # subject_input.wait_for(state="visible")
    # subject_input.fill('测试邮件')
    # time.sleep(1)
    #
    # # 输入正文内容
    # edit_frame = page.frame_locator('.APP-editor-iframe')
    # edit_frame.locator('.nui-scroll').fill('测试邮件内容')
    # time.sleep(1)
    #
    # # 点击发送
    # page.locator('//html//body//div[2]//div[1]//div[2]//header//div//div[1]//div//span[2]').click()
    # # send_btn = page.get_by_role('button', name='发送')  # 用角色+文字定位，比XPath稳定
    # # send_btn.wait_for(state="visible", timeout=10000)
    # # send_btn.click()
    # time.sleep(3)
    #
    # input("邮件发送完成，按回车键关闭浏览器...")
    # browser.close()

    # --------------------------------V2-----------------------------------------
    # locator = Locator(page)
    # frame_obj = locator.find_frame('//html//body//div[3]//div[3]//div[1]//div//div[3]//div[1]//div[2]//iframe')
    # locator.within_frame_by_locator(frame_obj, '[placeholder=邮箱账号或手机号码]').fill('leeoohs')
    # locator.within_frame_by_locator(frame_obj, '#pwdtext').fill('Ad112211..')
    # locator.within_frame_by_locator(frame_obj, '#dologin').click()
    # time.sleep(3)

    # --------------------------------V3-----------------------------------------
    locator = Locator(page)
    frame_obj = locator.locator_element(selector='//html//body//div[3]//div[3]//div[1]//div//div[3]//div[1]//div[2]//iframe', is_frame= True)
    locator.locator_element(selector='[placeholder=邮箱账号或手机号码]',frame=frame_obj, within_frame= True).fill('leeoohs')
    locator.locator_element(selector='#pwdtext',frame=frame_obj, within_frame= True).fill('Ad112211..')
    locator.locator_element(selector='#dologin',frame=frame_obj, within_frame= True).click()
    time.sleep(3)
