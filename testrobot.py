import streamlit as st
import SparkApi

appid = "ca1c76c1"     #填写控制台中获取的 APPID 信息
api_secret = "YTdmZTY5YmRkMTIxYThlMDBmZGJjMTNj"   #填写控制台中获取的 APISecret 信息
api_key ="fecf8bef78cba57c974c9d33051a91fb"    #填写控制台中获取的 APIKey 信息
domain = "4.0Ultra"          #我使用的是4.0版本
Spark_url = "wss://spark-api.xf-yun.com/v4.0/chat"    #4.0服务地址 
text =[]


def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text

# Streamlit 应用程序界面

if __name__ == "__main__":
     st.title('testrobot build on lightAPI')
     st.caption("by 刘士铭")
     if 'generated' not in st.session_state:
        st.session_state['generated'] = []
     if 'past' not in st.session_state:
        st.session_state['past'] = []
    
     with st.form('my_form'): 
      user_input = st.text_area('Enter text:', '请输入您的问题') 
      submitted = st.form_submit_button('Submit') 
      if submitted :
          if user_input:
        
           question = checklen(getText("user",user_input))
           SparkApi.answer = ""
           SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
           getText("assistant", SparkApi.answer)
      st.info(SparkApi.answer)    
      