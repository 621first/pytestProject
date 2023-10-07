from selenium.webdriver.common.by import By
from base_page.base_page import BasePage
from time import sleep

class IndexPage(BasePage):
    '''
        分业务：封装各个页面的元素，以及页面的操作和断言
    '''
    # 页面url
    url = 'http://www.taobao.com'

    # 页面元素
    search_input = (By.NAME,'q')
    search_click = (By.XPATH,'//*[@id="J_TSearchForm"]/div[1]/button')
    cart_button = (By.XPATH,'//*[@id="J_MiniCart"]/div[1]/a/span[2]')

    # 页面动作：查询
    def search(self,q):
        self.visit()
        # self.send_keys(self.search_input,q)
        # self.click(self.search_click)
        # sleep(3)
        self.click(self.cart_button)

    # 断言:获取预期值
    def get_except_result(self):
        return self.get_value(LoginPage.search_input)