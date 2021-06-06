from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar
from bs4 import BeautifulSoup
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

login_url = "http://bdy.zhikao666.com/login"
list_url = "http://bdy.zhikao666.com/tags"
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
'Connection': 'keep-alive',
'DNT': '1',
'Referer': 'http://bdy.zhikao666.com/login',
'Origin': 'http://bdy.zhikao666.com',
}


data = {}
data['username'] = "郑洋"
data['password'] = "123456"
logingData = parse.urlencode(data).encode('utf-8')
cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
login_request = request.Request(url=login_url, data=logingData, headers=headers)
list_request = request.Request(list_url, headers = headers)
login_rsp = opener.open(login_request)
response = opener.open(list_request)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')

li=soup.find_all('tr')
section_url=li[1].find_all('a', {'class': 'uk-button uk-button-primary'})[1]['href']

result_url = 'http://bdy.zhikao666.com/%s' % (section_url)
item_request = request.Request(result_url, headers = headers)
response = opener.open(item_request)
html1 = response.read().decode('utf-8')


soup1 = BeautifulSoup(html1, 'lxml')

li = soup1.find("div", {"class": "questions"})
questions_list = li.find_all("a", href=True)
for qitem in questions_list:
    result_url = 'http://bdy.zhikao666.com%s' % (qitem['href'])
    item_request = request.Request(result_url, headers = headers)
    response = opener.open(item_request)
    html2 = response.read().decode('utf-8')
    soup2 = BeautifulSoup(html2, 'lxml')
    title_num = soup2.find('div', {'class':'head'}).h2.text.strip()
    question_title = soup2.find('div', {'class':'question html-container'}).text.strip()
    #ans_list_num = soup2.find_all('div', {'class':'choice'}).text.strip()
    ans_list = soup2.find_all('div', {'class':'item'})
    for item in ans_list:
        item.div.text
        item.text.strip()
        
