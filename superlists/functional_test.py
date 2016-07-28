from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    """Test story for new visitor"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # 听说有个待办事项应用，访问主页
    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://localhost:8000')

        # 网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 应用邀请用户添加待办事项

        # 用户在输入框中输入“购买刮胡刀片”

        # 按下回车键后，页面更新
        # 待办事项表格中显示“1、购买刮胡刀片”

        # 页面又显示了一个输入框，用户又输入了“回到家买馒头”

        # 页面再次更新，显示了这两个待办事项

        # 用户想知道这个网站是否会记住他记录的清单

        # 用户可以看到网站为他生成了一个唯一的URL
        # 并且页面中有一些文字说明了这个功能

        # 用户访问那个URL，发现所有待办事项列表都在

        # 用户很满意

if __name__ == '__main__':
    unittest.main(warnings='ignore')

