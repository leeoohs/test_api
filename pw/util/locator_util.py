class Locator:
    def __init__(self, page):
        self.page = page

    def by_css(self, selector):
        """通过 css 选择器定位元素"""
        return self.page.locator(selector)

    def by_xpath(self, xpath):
        """通过 xpath 选择器定位元素"""
        return self.page.locator(f"xpath={xpath}")

    def by_text(self, text):
        """通过文本内容定位元素"""
        return self.page.locator(f"text={text}")

    def by_role(self, role, **kwargs):
        """通过角色和属性定位元素"""
        return self.page.locator(f"role={role}", **kwargs)

    # def by_tag_name(self, tag_name):
    #     """通过标签名定位元素"""
    #     return self.page.locator(tag_name)

    def by_placeholder(self, placeholder):
        """通过占位符定位元素"""
        return self.page.get_by_placeholder(placeholder)
        # return self.page.locator(f"placeholder={placeholder}")

    def find_frame(self, selector):
        """定位 frame"""
        return self.page.frame_locator(selector)

    def within_frame_by_locator(self, frame_obj, selector):
        """在特定的 frame 中通过 selector 来定位frame"""
        return frame_obj.locator(selector)

    def locator_element(self, selector=None, frame=None, role=None, name=None, is_frame=False):
        """

        :param selector:
        :param frame:
        :param role:
        :param name:
        :param if_frame:
        :param within_frame:
        :return:
        """
        try:
            # 用来定位的主题是 page 还是 frame
            target = self.page
            # 判断是否在frame
            # if within_frame:
            #     target = frame
            if frame:
                target = frame

            # 判断控件是否是frame
            if is_frame:
                return target.frame_locator(selector)

            # 通过角色和名称定位
            if role:
                return target.get_by_role(role, name=name)

            return target.locator(selector)

        except Exception as e:
            raise Exception(f"元素定位失败：{e}")

