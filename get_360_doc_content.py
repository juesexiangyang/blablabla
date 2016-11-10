#encoding:utf-8
#一个小脚本，可以把360的文章下载下来然后提取出文章正文，去掉html标签，对付360文章不登陆不能复制的设置
url = 'http://www.360doc.com/content/12/1012/21/7662927_241124973.shtml'
import requests

response = requests.get(url)

#print response.content
from bs4 import BeautifulSoup as bs
import re
soup = bs(response.content)

article = soup.find('div',class_ = 'entry-content')
regex = re.compile('\<.*?\>')
art = regex.split(str(article))
for i in art:
    print str(i).strip()
