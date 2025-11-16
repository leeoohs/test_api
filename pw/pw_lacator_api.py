# 定位器 locator
# page.locator(选择器) --> locator 对象
# page.get_by_xxx(xxx) --> locator 对象

"""
按 id：#id_name
按class：.class_name
按属性： [type="button"]
组合使用：
"""
import time
from playwright.sync_api import Playwright, sync_playwright, expect


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.baidu.com")
#     time.sleep(3)
#     locator_obj = page.locator("#chat-textarea")
#     locator_obj.fill("hello")
#     page.fill('#chat-textarea', '米兰')
#     time.sleep(3)
#     page.locator('//*[@id="chat-submit-button"]').click()
#     page.click('//*[@id="chat-submit-button"]')
#     time.sleep(3)
#     模糊查找：page.locator('test=米兰')
#     page.locator('text=米兰 - 百度百科').click()
#     精确查找：page.locator('text=米兰 - 百度百科')
#     page.locator(text='米兰 - 百度百科').click()
#     time.sleep(3)
#     page.get_by_text('换一换').click()
#     模糊匹配 div span p 等非交互元素，用文本定位器，交互元素，按钮，a，input用角色定位器 get_by_role()
#     page.get_by_text('换一').click()
#     定位到超链接文本
#     page.get_by_text('hao123').click()
#     time.sleep(3)
#
#     角色定位器：page.get_by_role() button link textbox checkbox and so on
#     page.get_by_role('button', name='换一换', id='chat-submit-button').click()
#     page.locator('role=button[name="百度一下"]').click()
#     time.sleep(3)
#
#     page.goto("https://mail.163.com")
#     frame = page.frame_locator("#x-URS-iframe")
#     frame.get_by_placeholder("邮箱账号或手机号码").fill('你好')
#     frame.get_by_label('30天内免登录').click()
#     page.get_by_alt_text('公安').click()
#     time.sleep(3)
#     # locator.filter()
#
#     page.locator('.classname').filter({'has-text': '30天内免登录'})
#
#     元素操作 - 网页
#     page.goto("https://www.baidu.com")
#     time.sleep(3)
#     page.goto("https://zhibo8.com")
#     time.sleep(3)
#     page.go_back()  # 返回
#     time.sleep(3)
#     page.go_forward()  #前进
#     time.sleep(3)
#     page.reload()  # 刷新
#     print(page.title())
#     print(page.content())
#
#     元素类
#     click() 单击
#     fill() 文本框输入内容
#     clear() 清空操作
#     page.goto("https://www.baidu.com")
#     locator_obj = page.locator("#chat-textarea")
#     locator_obj.fill('hello')
#     time.sleep(3)
#     locator_obj.clear()
#     time.sleep(3)
#     print(locator_obj.is_visible())  # 是否可见
#     print(locator_obj.is_enabled())  # 是否可用
#     print(locator_obj.get_attribute())  # 获取属性
#
#     Frame
#     frame = page.frame_locator()
#     frame.get_by_label()
#     frame.get_by_text()
#
#     窗口切换
#     完全隔离的独立对话

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # 创建第一个浏览器上下文
    # context1 = browser.new_context()
    # page1 = context1.new_page()
    # page1.goto("https://www.baidu.com")

    # 创建第2个浏览器上下文
    # context2 = browser.new_context()
    # page2 = context2.new_page()
    # page2.goto("https://www.zhibo8.com")

    # 同一会话下的新的标签页
    # context = browser.new_context()
    # page1 = context.new_page()
    # page1.goto("https://www.baidu.com")
    #
    # # 同一会话下的新的标签页
    # page2 = context.new_page()
    # page2.goto("https://www.zhibo8.com")

    # 点击连接产生新窗口或弹出窗口
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://www.baidu.com")
    #
    # 设置了一个监听器，当点击连接时，会返回一个页面对象
    # with context.expect_page() as new_page_info:
    #     page.click('text=贴吧')
    # new_page = new_page_info.value
    # time.sleep(3)

    # 鼠标移动
    conttext = browser.new_context()
    page = conttext.new_page()
    # page.goto("https://sahitest.com/demo/dragDropMooTools.htm")
    page.goto("https://www.baidu.com")
    time.sleep(3)
    # 拖拽
    # page.locator("#dragger").drag_to(page.locator("text=Item 3"))
    # page.drag_and_drop("#dragger", "text=Item 2")
    # time.sleep(3)
    element = page.locator('//*[@id="s-usersetting-top"]')
    # 悬浮
    element.hover()
    time.sleep(3)