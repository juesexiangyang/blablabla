import requests
from bs4 import BeautifulSoup as bs

def get_new_ip(ip_pool_file):
    ip_pool = open('ip_agent','rw+')
    ip_dict = []
    ips = ip_pool.readlines()
    for ip in ips:
        ip_dict.append(ip.strip())
        
    url = 'http://www.kuaidaili.com/free/'
    headers = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
	       'referer':'http://www.baidu.com'	}
    proxies = {'http':'http://222.221.47.138',
               'https':'http://222.221.47.138'}
    response = requests.get(url,headers = headers)#,proxies = proxies)    
    soup = bs(response.content,'lxml')
    for ip in soup.find_all('td',attrs={"data-title": "IP"}):
        if ip.string not in ip_dict:
            print 'new'
            ip_pool.write(ip.string+'\n')

        else:
            print 'got'
        
get_new_ip('ip_agent')
