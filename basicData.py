# coding=UTF-8

import requests
import json
import time
import pandas as pd

# 基金代码
code = []
for line in open("data.txt","r"): #设置文件对象并读取每一行文件
    test = line.strip('\n')
    code.append(test)

# 设置网页
htmls = []
url = "https://www.lionfund.com.cn/api/quoter/fundInfoBasic?fundCode={index}"

# 爬取资源
for index in code:
    time.sleep(1)
    print("爬取基金代码为", index)
    r = requests.get(url.format(index = index))
    html = r.json()
    data = html['data']
    del data['investField']
    del data['investOrientation']
    del data['investRatiosDesc']
    del data['performanceBenchmark']
    del data['riskProfitCharacter']
    del data['investTarget']

    L_temp = [data['fundCode'],data['fundFullName'],data['fundType'],data['establishDate'],data['trusteeCompany']]
    htmls.append(L_temp)

# 写入excel
output = open('basicData.xls','w',encoding='gbk')
output.write('基金代码\t基金名称\t基金种类\t基金成立时间\t托管银行名称\n')
for i in range(len(htmls)):
    for j in range(len(htmls[i])):
        output.write(str(htmls[i][j]))  #write函数不能写int类型的参数，所以使用str()转化
        output.write('\t')  #相当于Tab一下，换一个单元格
    output.write('\n')    #写完一行立马换行
output.close()

