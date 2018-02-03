# -*- coding: UTF-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()   # if the path of the chromedriver is not set at your local $PATH, one need to fill the path

#driver.get("https://nid.naver.com/nidlogin.login")
#driver.get("https://www.naver.com")
#driver.get("https://www.google.ch/search?source=hp&ei=1zl2WoWGKcHVwALE1Zgw&q=test&oq=test&gs_l=psy-ab.3..0j0i131k1j0l8.23.227.0.368.4.3.0.0.0.0.159.436.0j3.3.0....0...1c.1.64.psy-ab..1.3.436....0.Zyar46qbEyA")
#driver.get("http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=test&rsv_pq=cdb5406000024622&rsv_t=9525gMe8iVNGTjn05T6Q9%2FnAgaz8IM5JHXgigb%2FdfkU%2FwdPcRXbaqx06Xpk&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug2=0&inputT=515&rsv_sug4=698")
#driver.get("https://www.weibo.com")

driver.get("https://www.weibo.com/u/5607461482?refer_flag=1001030103_&is_hot=1")
driver.get("https://www.weibo.com/andyisme?refer_flag=1001030103_&is_hot=1")

driver.implicitly_wait(15)    # we need this, just in case of slow internet connection


tt = driver.find_elements_by_css_selector('.item_text.W_fl')
print(len(tt))
for iii in range(len(tt)):
    print(tt[iii].text)


#tt = driver.find_elements_by_css_selector('.item_text W_fl')  # not working, dont't know why
#print(len(tt))

#tt = driver.find_elements_by_class_name("item_text.W_fl")
#tt = driver.find_elements_by_class_name("gb_qb")
'''
tt = driver.find_elements_by_class_name("B_unlog")
print(len(tt))
for iii in range(len(tt)):
    print(tt[iii].text)
'''
'''
#for "naver.com"
tt = driver.find_elements_by_class_name("blind")
for iii in range(len(tt)):
    print(tt[iii].text)
'''

'''
#tt = driver.find_elements_by_link_text("쥬니어네이버")
tt = driver.find_elements_by_partial_link_text("한글")
print(len(tt))
for iii in range(len(tt)):
    print(tt[iii].text)
'''

driver.quit()
