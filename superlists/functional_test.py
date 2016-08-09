from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    """Test story for new visitor"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # 听说有个待办事项应用，访问主页
    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://localhost:8108')

        # 网页的标题和头部都包含“To-Do”这个词
        self.assertIn('待办', self.browser.title)
        header_txt = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('待办', header_txt)

        # 应用邀请用户添加待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '添加待办事项'
        )

        # 用户在输入框中输入“购买刮胡刀片”
        inputbox.send_keys('购买刮胡刀片')

        # 按下回车键后，页面更新
        # 待办事项表格中显示“1、购买刮胡刀片”
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. 购买刮胡刀片' for row in rows),
            "新建的待办事项没有出现在列表中"
        )

        # 页面又显示了一个输入框，用户又输入了“回到家买馒头”

        # 页面再次更新，显示了这两个待办事项

        # 用户想知道这个网站是否会记住他记录的清单

        # 用户可以看到网站为他生成了一个唯一的URL
        # 并且页面中有一些文字说明了这个功能

        # 用户访问那个URL，发现所有待办事项列表都在

        # 用户很满意
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
