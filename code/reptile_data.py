import xlwt
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import time
import xlrd
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import csv

def get_document_name(elements_name1,i):#篇名
    i=1+i*50
    j=1
    # 获得窗口句柄
    sreach_windows = browser.current_window_handle
    for t in elements_name1:
        #print(t.text)
        p = t.text
        if p=='大学生问题性短视频媒体使用量表的初步编制':
            i=i+1
            continue
        excel_table.write(i, 0, i)#序号
        excel_table.write(i, j, p)#篇名
        element = browser.find_element_by_partial_link_text(p)
        #爬取作者来源
        #webdriver.ActionChains(browser).move_to_element(element).click(element).perform()
        # element.click()
        browser.execute_script("arguments[0].click();", element)
        all_handles = browser.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                browser.switch_to.window(handle)
                #关键词
                keywords=browser.find_elements_by_xpath("//p[@class='keywords']")
                for keyword in keywords:
                    m=keyword.text
                    excel_table.write(i,8,m)
                #摘要
                content1 = browser.find_element_by_xpath("//span[@id='ChDivSummary']")
                content=content1.text
                excel_table.write(i, 10, content)
                # 页数
                content1 = browser.find_element_by_xpath("//p[@class='total-inform']/span[3]")
                if content1 == None:
                    continue
                else:
                    content = content1.text
                excel_table.write(i, 9, content)
                # 刊名
                content1 = browser.find_element_by_xpath("//div[@class='top-tip']/span[1]/a[1]")
                if content1 == None:
                    continue
                else:
                    content = content1.text
                excel_table.write(i, 3, content)

                #作者
                authers=browser.find_elements_by_xpath("//div[@class='wx-tit']/h3[1]/span[1]")
                for auther in authers:
                    n=auther.text
                    excel_table.write(i,2,n)
                # 第一作者所在地
                f=browser.find_elements_by_xpath("//div[@class='wx-tit']/h3[2]/span[1]")
                if f==[]:
                    f=browser.find_elements_by_xpath("//div[@class='wx-tit']/h3[2]/a[1]")
                for q in f:
                    k=q.text
                    excel_table.write(i, 7, k)
                #time.sleep(2)
                browser.close()
                browser.switch_to.window(sreach_windows)
        #
        i += 1
    excel.save(r"E:\暑期实践.xls")

# def get_document_source(elements_name2,i): # 刊名
#     i=1+i*50
#     j = 3
#     # soup_all = BeautifulSoup(str(document), 'html.parser')
#     # source = soup_all.find_all('td', class_='source')
#     # soup_source = BeautifulSoup(str(source), 'html.parser')
#     # for line in soup_source.stripped_strings:
#     #     p = line
#     #     if p=='[' or p==',' or p==']':
#     #         continue
#     #
#     for t in elements_name2:
#         #print(t.text)
#         p = t.text
#         excel_table.write(i, j, p)#刊名
#     excel_table.write(i, j, p)
#     i += 1
#     excel.save('AI_teach1.xls')

def get_document_time(document,i):  # 时间
    i=1+i*50
    j = 4
    soup_all = BeautifulSoup(str(document), 'html.parser')
    date = soup_all.find_all('td', class_='date')
    soup_date = BeautifulSoup(str(date), 'html.parser')
    for line in soup_date.stripped_strings:
        p = line
        if p=='[' or p==',' or p==']':
            continue
        excel_table.write(i, j, p)
        i += 1
    excel.save(r"E:\暑期实践.xls")


def get_document_use(document,i):  # 被引次数
    i=1+i*50
    j = 5
    soup_all = BeautifulSoup(str(document), 'html.parser')
    date = soup_all.find_all('td', class_='quote')
    soup_date = BeautifulSoup(str(date), 'html.parser')
    for line in soup_date.stripped_strings:
        p = line
        if p=='[' or p==']':
            continue
        elif p==',':
            i=i+1
            continue
        else:
            excel_table.write(i, j, p)
    excel.save(r"E:\暑期实践.xls")

def get_document_download(document,i):  # 下载次数
    i=1+i*50
    j = 6
    soup_all = BeautifulSoup(str(document), 'html.parser')
    date = soup_all.find_all('td', class_='download')
    soup_date = BeautifulSoup(str(date), 'html.parser')
    for line in soup_date.stripped_strings:
        p = line
        if p=='[' or p==']':
            continue
        elif p==',':
            i=i+1
            continue
        else:
            excel_table.write(i, j, p)
    excel.save(r"E:\暑期实践.xls")


if __name__=='__main__':
    # 设置谷歌驱动器的环境
    options = webdriver.ChromeOptions()
    # 设置chrome不加载图片，提高速度
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # 创建一个谷歌驱动器
    browser = webdriver.Chrome(options=options,executable_path=r"E:\chromedriver.exe")  # executable_path是驱动器chromedriver的路径
    url = 'https://kns.cnki.net/kns8/AdvSearch?dbprefix='
    browser.get(url)
    browser.set_window_size(1400, 800)
    WebDriverWait(browser, 1000).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-tipid='gradetxt-1']")))

    # 选择学术期刊
    browser.find_element(By.XPATH, "//*[@data-id='xsqk']").click()
    time.sleep(5)


    #点击专业检索
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[4]').click()
    #browser.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/ul/li[4]')
    time.sleep(1)
    #输入主题
    browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/textarea").send_keys(''' SU=‘大学生’*‘短视频’ OR  SU='高校'*‘短视频平台’ ''')
    #browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/textarea').send_keys('''  SU=‘高校’*‘思政’*‘课程’ OR SU=‘大学生’*‘思想政治’*‘教育’ OR SU=‘思政课’*‘改革’ OR SU=‘思想政治’*‘建设''')
    time.sleep(1)
    # 选择主题
    # browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/dl/dd[2]/div[2]/div[1]/div[1]/span").click()
    # time.sleep(2)
    # browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/dl/dd[2]/div[2]/div[1]/div[2]/ul[1]/li[2]/a").click()
    # time.sleep(1)
    # print("\n请稍等片刻！")
    #主题：教育
    # browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/dl/dd[2]/div[2]/input").send_keys('教育')
    # time.sleep(1)
    # browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    # time.sleep(2)
    #取消英文检索
    # browser.find_element_by_xpath("//*[@data-id='EN']").click()
    #browser.find_element(By.XPATH, "//*[@data-id='EN']")
    time.sleep(3)
    #取消CSCD检索
    # browser.find_element_by_xpath("//*[@key='SI']").click()
    # browser.find_element_by_xpath("//*[@key='EI']").click()
    # browser.find_element_by_xpath("//*[@key='HX']").click()
    # browser.find_element_by_xpath("//*[@key='CSI']").click()
    # browser.find_element_by_xpath("//*[@key='CSD']").click()
    # time.sleep(3)

    #选择时间
    # browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/input").send_keys('2006')
    # browser.find_element_by_xpath(
    #     "/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/input").send_keys(
    #     '2021')

    # 点击检索
    browser.find_element_by_class_name('btn-search').click()
    #browser.find_element(By.XPATH, "btn-search")
    time.sleep(3)

    #选择每页显示数量
    browser.find_element_by_xpath("//*[@class='icon icon-sort']").click()
    #browser.find_element(By.XPATH, "//*[@class='icon icon-sort']")
    time.sleep(2)
    browser.find_element_by_xpath("//*[@data-val='50']").click()
    time.sleep(2)
    # print('hello')
    # time.sleep(30)


    book = xlwt.Workbook()  # 新建工作簿
    sheet = book.add_sheet('DATA', cell_overwrite_ok=True)  # 如果对同一单元格重复操作会发生overwrite Exception，cell_overwrite_ok为可覆盖
    sheet.write(0, 0, '序号')  # 行，列，属性值
    sheet.write(0, 1, '名字')  # 行，列，属性值
    sheet.write(0, 2, '作者')  # 行，列，属性值
    sheet.write(0, 3, '刊名')  # 行，列，属性值
    sheet.write(0, 4, '发表时间')  # 行，列，属性值
    sheet.write(0, 5, '引用次数')  # 行，列，属性值
    sheet.write(0, 6, '下载次数')  # 行，列，属性值
    sheet.write(0, 7, '第一作者所在地')  # 行，列，属性值
    sheet.write(0, 8, '关键词')  # 行，列，属性值
    sheet.write(0, 10, '摘要')  # 行，列，属性值
    sheet.write(0, 9, '页数')  # 行，列，属性值
    style = xlwt.XFStyle()  # 新建样式
    font = xlwt.Font()  # 新建字体
    font.name = 'Times New Roman'
    font.bold = True
    style.font = font  # 将style的字体设置为font
    # table.write(0, 0, 'Test', style)
    book.save(filename_or_stream=r"E:\暑期实践.xls")  # 一定要保存
    data = xlrd.open_workbook(r"E:\暑期实践.xls", formatting_info=True)  # 读取各种格式信息
    excel = copy(wb=data)  # 完成xlrd对象向xlwt对象转换，进行编辑操作
    excel_table = excel.get_sheet(0)  # 获得要操作的页


    for i in range(0,119):
        elements_name1 = browser.find_elements_by_xpath("//*[@class='fz14']")
        flag0=get_document_name(elements_name1,i)#篇名

        elements_name2 = browser.find_elements_by_xpath("//*[@class='source']")
        # get_document_source(elements_name2,i)#刊名

        url=browser.page_source
        soup = BeautifulSoup(url, "lxml")
        document_list = soup.find_all('tbody')
        get_document_time(document_list,i)#时间
        get_document_use(document_list, i)#引用次数
        get_document_download(document_list, i)#下载次数

        excel.save(r"E:\暑期实践.xls")


        browser.find_element_by_id("PageNext").click()

        time.sleep(30)

        #WebDriverWait(browser, 1000).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-tipid='gradetxt-1']")))




