from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

class qi_dian():
    #启动浏览器
    def open_chrome(self):
        chromedriver = "../qidian_web_auto\\chromedriver\\chromedriver.exe"  # Chrome浏览器驱动
        self.driver = webdriver.Chrome(chromedriver)  # 打开chrome浏览器
        self.driver.maximize_window()  # 窗口最大化

    # 完成企点账户登录
    def login_qi_dian(self):
        self.open_chrome() #调用open_chrome的代码
        self.driver.get("https://oaadmin.qidian.qq.com/ac/login")  # 打开账户中心登录页
        sleep(1)
        iframe = self.driver.find_element_by_xpath("//iframe[@id='login_div']")  # 定位"快速安全登录"iframe
        self.driver.switch_to_frame(iframe)  # 进入"快速安全登录"iframe
        self.driver.find_element_by_xpath("//div/a[@class='link' and @id='switcher_plogin' and @tabindex='8']").click()  # 定位并点击账号密码登录
        sleep(1)
        admin_qq = self.driver.find_element_by_xpath("//div/input[@type='text']")  # 定位账户输入框
        admin_qq.send_keys("3007048422")  # 输入企点管理QQ
        qq_password = self.driver.find_element_by_xpath("//div/input[@type='password']")  # 定位密码输入框
        qq_password.send_keys("WOcao0748")  # 输入管理QQ密码
        login_btn = self.driver.find_element_by_xpath("//div/a/input[@type='submit']").click()  # 定位登录按钮并点击
        sleep(5)
        #frist_handle=self.driver.window_handles#获取当前窗口句柄

        # 新开窗口打开分支切换工具
    def  selbranch(self):
        self.login_qi_dian()  # 调用login_qi_dian的代码
        selbranch= 'window.open("https://oaadmin.qidian.qq.com/ea/site/selbranch");'# 新开一个窗口(打开分支切换工具页)
        self.driver.execute_script(selbranch)
        #self.driver.find_element_by_xpath('//select[@name="version"]').click()#定位切换分支下拉框并点击
        sleep(2)
        self.second_handle = self.driver.window_handles  # 获取当前窗口句柄

        # 再次切换企点首页窗口
    def switch_qidian(self):
        self.selbranch()#调用self.selbranch()的代码
        sleep(2)
        get_handles = self.driver.window_handles  # 获取当前页面的所有窗口句柄
        print(get_handles)#返回的是个list
        for handle in get_handles:#通过遍历切换到企点首页的句柄
             if handle != self.second_handle:
                self. driver.switch_to_window(handle)
                break#这里要加个终止不然会一直遍历窗口句柄
        sleep(2)

        self.driver.find_element_by_xpath("//h1/div[@class='btnSwitch']").click()#点击切换模块下拉框
        sleep(1)

        self.a=self.driver.find_element_by_xpath("//div[@class='xbtn marketing'][3]")#选择企点营销模块

        ActionChains(self.driver).move_to_element(self.a).perform()#这里有个悬停的操作

        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[8]/div/span").click()#点击“企点营销”模块
        sleep(2)

        #切换到客户管理子站
    def ea_customer_manage(self):
        self.switch_qidian()#调用switch_qidian()的代码
        self.driver.find_element_by_xpath("//a[text()='客户管理']").click()#点击"客户管理"
        sleep(3)
        self.driver.find_element_by_xpath('//a[@env="test" and @data-title="线索库"]').click()#点击线索库
        sleep(5)
        #self.driver.refresh()#刷新页面
        self.b =self.driver.find_element_by_xpath("(//span[@class='menu-content'])[1]")#点击导入旁边的下拉框
        ActionChains(self.driver).move_to_element(self.b).perform()
        self.driver.find_element_by_xpath("(//button[@type='button'])[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath("(//div[@class='v-popmenu__item'])[2]").click()#点击新建





qi_dian = qi_dian()  # 实例化方法class qi_dian()

if __name__ == '__main__':
    # qi_dian.login_qi_dian()# 调用方法qi_dian的login_qi_dian函数
    #qi_dian.selbranch()
    #qi_dian.switch_qidian()#调用方法qi_dian的switch_qidiant函数
    qi_dian.ea_customer_manage()

