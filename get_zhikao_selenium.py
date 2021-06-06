from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

# opt.add_argument('--headless')
#更换头部
#opt.add_argument('user-agent="%s"' % 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36')
opt = webdriver.ChromeOptions()
opt.add_argument('user-agent="%s"' % 'Chrome/83.0.4103.97')
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', chrome_options=opt)
regnum = 0

class zhikao:

    def __init__(self, login_name, real_name, id_num, phonenum, detail_address, ismail, passwd = "Xx056600", email = "xiyanggao7991200@163.com"):
        self.name   = login_name
        self.passwd = passwd
        self.email = email
        self.real_name = real_name
        self.id_num = id_num
        self.phonenum = phonenum
        self.detail_address = detail_address
        self.ismail   = ismail
        self.num = 0
    def check_is_already_reg(self, driver):
        lname = driver.find_element_by_xpath ("//input[@id='login_name']")
        lname.send_keys (self.name)
        lname.send_keys (Keys.TAB)
        try:
            nameused = driver.find_element_by_xpath ('//span[contains(./text(),"用户名已被他人使用，建议更换")]')
            print('Name already registered.')
            return True
        except Exception as e:
            #print (e)
            #print('register failed.')
            #return False
            pass
        idcard = driver.find_element_by_xpath ("//input[@id='vol_cert_number']")
        idcard.send_keys (self.id_num)
        idcard.send_keys (Keys.TAB)
        try:
            used = driver.find_element_by_xpath ('//span[contains(./text(),"该证件号码已被其他志愿者注册！请不要注册，建议 ")]')
            print('IDCard already registered.')
            return True
        except Exception as e:
            #print (e)
            #print('register failed.')
            return False
        return False
        
    def hbzyz(self):
        global regnum
        try:
            driver.get ("https://he.zhiyuanyun.com/app/user/register.php")
            driver.implicitly_wait(4)
            if True == self.check_is_already_reg(driver):
                return
            lname = driver.find_element_by_xpath ("//input[@id='login_name']")
            lname.clear()
            lname.send_keys (self.name)
            
            lname_r = driver.find_element_by_xpath ("//input[@id='login_name_repeat']")
            lname_r.send_keys (self.name)
            
            lpasswd = driver.find_element_by_xpath ("//input[@id='login_pass']")
            lpasswd.send_keys (self.passwd)
            
            lpasswd_r = driver.find_element_by_xpath ("//input[@id='login_pass_repeat']")
            lpasswd_r.send_keys (self.passwd)
            
            lemail = driver.find_element_by_xpath ("//input[@id='login_email']")
            lemail.send_keys (self.email)
            
            lemail_r = driver.find_element_by_xpath ("//input[@id='login_email_repeat']")
            lemail_r.send_keys (self.email)
            
            
            real_name = driver.find_element_by_xpath ("//input[@id='vol_true_name']")
            real_name.send_keys (self.real_name)
            
            idcard = driver.find_element_by_xpath ("//input[@id='vol_cert_number']")
            idcard.clear()
            idcard.send_keys (self.id_num)
            
            #gender femail
            if 0 == self.ismail:
                driver.find_element_by_xpath ("//input[@value='0']").click()
            #gender mail
            else:
                driver.find_element_by_xpath ("//input[@value='1']").click()
            '''
            ye = self.id_num[6:10]
            mo = self.id_num[10:12]
            da = self.id_num[12:14]
            year = driver.find_element_by_xpath ("//select[@id='vol_reg_year']")
            year.send_keys (ye)
            month = driver.find_element_by_xpath ("//select[@id='vol_reg_month']")
            month.send_keys (mo)
            day = driver.find_element_by_xpath ("//select[@id='vol_reg_day']")
            day.send_keys (da)
            '''
            time.sleep(2)
            
            political = driver.find_element_by_xpath ("//select[@id='vol_political']")
            political.send_keys ('群众')
            
            
            callphone = driver.find_element_by_xpath ("//input[@id='login_mobile']")
            callphone.send_keys (self.phonenum)
            
            
            area_address = driver.find_element_by_xpath ("//select[@id='house_district1']")
            area_address.send_keys ('邯郸市')
            time.sleep(3)
            area_address1 = driver.find_element_by_xpath ("//select[@id='house_district2']")
            area_address1.send_keys ('临漳县')
            time.sleep(3)
            area_address2 = driver.find_element_by_xpath ("//select[@id='house_district3']")
            area_address2.send_keys ('西羊羔乡')
            
            
            detail_address = driver.find_element_by_xpath ("//input[@id='vol_address']")
            detail_address.send_keys (self.detail_address)
            
            edu_degree = driver.find_element_by_xpath ("//select[@id='vol_edu_degree']")
            edu_degree.send_keys ('初中')
            
            job = driver.find_element_by_xpath ("//select[@id='vol_job_title']")
            job.send_keys ('农民')
            
            
            service_area = driver.find_element_by_xpath ("//select[@id='district1']")
            service_area.send_keys ('邯郸市')
            time.sleep(3)
            service_area = driver.find_element_by_xpath ("//select[@id='district2']")
            service_area.send_keys ('临漳县')
            time.sleep(3)
            service_area = driver.find_element_by_xpath ("//select[@id='district3']")
            service_area.send_keys ('西羊羔乡')
            
            service_type = driver.find_element_by_xpath ("//input[@value='社区服务']")
            service_type.send_keys (' ')
            service_type = driver.find_element_by_xpath ("//input[@value='敬老助残']")
            service_type.send_keys (' ')
            service_type = driver.find_element_by_xpath ("//input[@value='环境保护']")
            service_type.send_keys (' ')
            
            button = driver.find_element_by_xpath('//a[@class="but1 but_reg"]')
            button.click()
            time.sleep(5)
            try:
                success = driver.find_element_by_xpath('//div[@class="reg_success"]')
                #self.num+=1
                regnum+=1
                print("{}: {} {} {} 注册成功".format(regnum, self.name, self.real_name, self.phonenum))
                time.sleep(3)
                filename = 'reg_success.txt'
                with open(filename, 'a+', encoding='utf-8') as fobject:
                    fobject.write("{}: {} {} {} 注册成功\n".format(regnum, self.name, self.real_name, self.phonenum))
                    fobject.close()
            #self.send_yzm(button,name)
            except Exception as e:
                #print (e)
                print('register failed.')
            
        except Exception as e:
            print (e)
            print('register failed.')


    # 循环执行
    def main(self):           
        self.hbzyz()
           
        #time.sleep(10)

if __name__ == '__main__':
    fp=open("reg_success.txt", "r", encoding='utf-8')
    lastl=fp.readlines()[-1]#取最后一行的计数
    lastnum=int(lastl.split(":", 1)[0])
    regnum = lastnum
    fp.close()
    
    data = xlrd.open_workbook("C:\\Users\ZhangJi\Desktop\志愿者注册.xlsx")
    table = data.sheet_by_name('Sheet1')
    for rowNum in range(1, table.nrows):
        rowVale = table.row_values(rowNum)
        loginname = 'x'+str(int(rowVale[9]))
        realname = rowVale[3]
        id_num = rowVale[6]
        callphone = int(rowVale[9])
        address = rowVale[7]+rowVale[8]
        gender = rowVale[4]
        if gender == '男':
            mail = 1
        else:
            mail = 0
        
        print(loginname, realname, id_num, callphone, address, mail)
        
        #(self, login_name, passwd, email, real_name, id_num, phonenum, detail_address, ismail):
        OneReg = VolReg(login_name=loginname, real_name=realname, id_num=id_num, phonenum=callphone, detail_address=address, ismail=mail)
        OneReg.main()
        
    #driver.quit()
