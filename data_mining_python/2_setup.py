# -*- coding: UTF-8 -*-
from selenium import webdriver

driver1 = webdriver.Chrome()   # if the path of the chromedriver is not set at your local $PATH, one need to fill the path
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()
driver4 = webdriver.Chrome()
#driver.set_page_load_timeout(20)

driver1.implicitly_wait(5)

driver1.get("https://www.weibo.com/u/5607461482?refer_flag=1001030103_&is_hot=1")
driver2.get("https://www.weibo.com/andyisme?refer_flag=1001030103_&is_hot=1")
driver3.get("https://www.weibo.com/northwales?refer_flag=1001030103_&is_hot=1")
driver4.get("https://www.weibo.com/u/2136305097?refer_flag=1001030103_&is_hot=1")

#driver1.implicitly_wait(15)    # we need this, just in case of slow internet connection
#driver2.implicitly_wait(15)
#driver.set_page_load_timeout(15)

tt1 = driver1.find_elements_by_css_selector('.item_text.W_fl')
tt2 = driver2.find_elements_by_css_selector('.item_text.W_fl')
tt3 = driver3.find_elements_by_css_selector('.item_text.W_fl')
tt4 = driver4.find_elements_by_css_selector('.item_text.W_fl')

jjj = 0

for iii in range(len(tt1)):
    s1 = (tt1[iii].text).encode('unicode-escape').decode('string_escape')
    if(s1.find('\\u5317\\u4eac') != -1):						# "\\u5317\\u4eac"  is  北京
        print(tt1[iii].text)
        jjj = jjj+1
        break

for iii in range(len(tt2)):
    s1 = (tt2[iii].text).encode('unicode-escape').decode('string_escape')
    if(s1.find('\\u5317\\u4eac') != -1):                        # "\\u5317\\u4eac"  is  北京
        print(tt2[iii].text)
        jjj = jjj+1
        break

for iii in range(len(tt3)):
    s1 = (tt3[iii].text).encode('unicode-escape').decode('string_escape')
    if(s1.find('\\u5317\\u4eac') != -1):                        # "\\u5317\\u4eac"  is  北京
        print(tt3[iii].text)
        jjj = jjj + 1
        break

for iii in range(len(tt4)):
    s1 = (tt4[iii].text).encode('unicode-escape').decode('string_escape')
    if(s1.find('\\u5317\\u4eac') != -1):                        # "\\u5317\\u4eac"  is  北京
        print(tt4[iii].text)
        jjj = jjj + 1
        break

print "位于北京的人数：",jjj
'''
s1 = (tt1.text).encode('unicode-escape').decode('string_escape')
if(s1.find('\\u5e7f\\u4e1c') != -1):    # '\\u5e7f\\u4e1c' is 广东
    print("!!found!!")
else:
    print("!!not found!!")
u1 = s1.decode('unicode-escape') 
print(s1)
print(type(s1))
print(u1)
print(type(u1))
'''
'''
tt1 = driver1.find_elements_by_css_selector('.item_text.W_fl')
tt2 = driver2.find_elements_by_css_selector('.item_text.W_fl')
tt3 = driver3.find_elements_by_css_selector('.item_text.W_fl')
print(len(tt1))
for iii in range(len(tt1)):
    print(tt1[iii].text)
    if(iii > 0) : break

print(len(tt2))
for iii in range(len(tt2)):
    print(tt2[iii].text)

print(len(tt3))
for iii in range(len(tt3)):
    print(tt3[iii].text)
'''

'''
tt = driver.find_elements_by_partial_link_text("北京")
print(len(tt2))
for iii in range(len(tt2)):
    print(tt2[iii].text)
'''
'''
tt = driver.find_elements_by_class_name("B_unlog")
print(len(tt))
for iii in range(len(tt)):
    print(tt[iii].text)
'''

'''
tt = driver.find_elements_by_partial_link_text("한글")
print(len(tt))
for iii in range(len(tt)):
    print(tt[iii].text)
'''

driver1.quit()
driver2.quit()
driver3.quit()
driver4.quit()
