from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import json
import pandas as pd

from selenium import webdriver
browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.get('http://www.courstack.com/square/sysu')

count = 0
while count>=5:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    count += 1

data_res = {
    "coursename":[],
    "time":[],
    "body":[],
    "approval":[],
    "oppose":[],
    "comment_num":[],
    }
results= browser.find_elements_by_class_name("newsfeedItem")
for result in results:
    try:
        coursename = result.find_element_by_tag_name("a")
        print(coursename.text)
        data_res['coursename'].append(coursename.text)
        time = result.find_element_by_tag_name("div.time")
        print(time.text)
        data_res['time'].append(time.text)
        body = result.find_element_by_tag_name("pre")
        print(body.text)
        data_res['body'].append(body.text)
        approval=result.find_element_by_tag_name("div.approvalBox")
        print(approval.text)
        data_res['approval'].append(approval.text)
        oppose=result.find_element_by_tag_name("div.opposeBox")
        print(oppose.text)
        data_res['oppose'].append(oppose.text)
        comment_num=result.find_element_by_tag_name("div.commentBox.reviewBox")
        print(comment_num.text)
        data_res['comment_num'].append(comment_num.text)
        print("--------------------------------------------------------")
    except:
        continue

pdres = pd.DataFrame(data_res)
print(pdres)
pdres.to_csv("out.csv")
browser.close()