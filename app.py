
import streamlit as st
import requests

def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res
	# 將 response 轉換成 json 格式
	# 回傳值

def getCountyOption(items):
    # 創建一個空的 List 並命名為 optionList
    optionList = []
    for item in items:
        # 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
        name = ['cityname'][0,3]
        # hint: 想辦法處理 item['cityName'] 的內容
        for item in items:
        # 如果 name 不在 optionList 之中，便把它放入 optionList
        if name not in optionList:
            optionList.append(name)
        # hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList

	return optionList

def app():
	# 呼叫 getAllBookstore 函式並將其賦值給變數 bookstoreList
    bookstoreList = getAllBookstore()
    countyOption = getCountyOption(bookstoreList)
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList)) # 將 118 替換成書店的數量
    county = st.selectbox('請選擇縣市', countyOption)
    district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])
    st.snow()




def app():
	bookstoreList = getAllBookstore()
	# 呼叫 getCountyOption 並將回傳值賦值給變數 countyOption
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C']) # 將['A', 'B', 'C']替換成縣市選項 
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])


def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
		name = item['cityName']
		# 如果 name 不是我們選取的 county 則跳過
        if county in name:
        specificBookstoreList.append(item)
		# hint: 用 if-else 判斷並用 continue 跳過
	
    return specificBookstoreList

def app():
	bookstoreList = getAllBookstore()

	countyOption = getCountyOption(bookstoreList)
	
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	specificBookstore = getSpecificBookstore(bookstoreList)
	# 呼叫 getSpecificBookstore 並將回傳值賦值給變數 specificBookstore
	num = len(specificBookstore)
	# 用 st.write 將目標書店的總數量計算出來，格式：總共有3項結果


def getBookstoreInfo(items):
	expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        # 用 expander.write 呈現書店的 Introduction
        expander.subheader('Address')
        # 用 expander.write 呈現書店的 Address
        expender.write
        expander.subheader('Open Time')
        # 用 expander.write 呈現書店的 Open Time
	expander.subheader('Email')
	# 用 expander.write 呈現書店的 Email
        # 將該 expander 放到 expanderList 中
    return expanderList

def app():
	bookstoreList = getAllBookstore()

	countyOption = getCountyOption(bookstoreList)
	
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 

	
	specificBookstore = getSpecificBookstore(bookstoreList, county, district)
	num = len(specificBookstore)
	st.write(f'總共有{num}項結果', num)
	
	# 呼叫 getBookstoreInfo 並將回傳值賦值給變數 bookstoreInfo

if __name__ == '__main__':
    app()