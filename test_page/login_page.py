from selenium.webdriver.common.by import By
from base_page.base_page import BasePage

class LoginPage(BasePage):
    '''
        分业务：封装各个页面的元素，以及页面的操作和断言
    '''
    # 页面url
    url = 'https://login.taobao.com/member/login.jhtml'

    # 页面元素
    username_input = (By.ID,'fm-login-id')
    password_input = (By.ID,'fm-login-password')
    login_submit = (By.XPATH,'//*[@id="login-form"]/div[4]/button')

    # 页面动作：登录
    def login(self,username,password):
        self.visit()
        self.send_keys(self.username_input,username)
        self.send_keys(self.password_input,password)
        self.click(self.login_submit)

    # 断言:获取预期值
    def get_except_result(self):
        return self.get_value(LoginPage.search_input)