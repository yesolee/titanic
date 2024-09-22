import streamlit as st
import pandas as pd
import numpy as np
import io

st.set_page_config(
    page_title="데이터 불러오기",
    page_icon="👀",
    layout="wide")

@st.cache_data
def get_train_data():
    return pd.read_csv("./data/train.csv")

train = get_train_data()


st.header('👀 데이터 둘러보기')

with st.container():
    col1, col2 = st.columns([1,2])
    
    # col1

    col1.subheader('1️⃣ 분석 목적 확인')
    col1.write('**🗂️ 데이터셋 설명보기/다운로드 [Kaggle](https://www.kaggle.com/c/titanic/data)**')
    col1.code(
        '''
    # 데이터셋 불러오기
    
    import pandas as pd

    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    sub = pd.read_csv('gender_submission.csv') 
    
    # 제출해야 하는 데이터 확인
    sub.columns # ['PassengerId', 'Survived']
        '''
    , language="python")
    col1.success('**목표: 탑승객 생존 여부 예측**', icon="🎯")

    # col2

    col2.subheader('2️⃣ 변수 설명 확인')
    data_info = pd.DataFrame({
        '변수':['Survived', 'Pclass', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
        '설명': ['생존 여부','티켓 등급(사회적지위 가늠)', '성별', '나이', '함께 탑승한 형제/배우자 수', '함께 탑승한 부모/자녀 수','티켓 번호','승객 요금', '객실 번호', '탑승 항구'],
        'Key': ['0: 사망, 1: 생존', '1: 상위, 2: 중간, 3: 하위','-','-','-','-','-','-','-','C: Cherbourg,  Q: Queenstown, S: Southampton' ]
    })

    col2.dataframe(data_info, width=1000)



with st.container():
    col1, col2 = st.columns([1,2])

    # col1

    col1.subheader('3️⃣ 데이터 타입/결측치 확인')
    col1.code(
        '''
    train.info()    
        '''
    , language="python")
    buffer = io.StringIO()
    train.info(buf=buffer)
    s = buffer.getvalue()

    col1.text(s)
    col1.error('**Age, Cabin, Embarked에 결측치 존재**', icon="🚨")
    
    # col2

    col2.subheader('4️⃣ 데이터 확인')
    col2.code(
        '''
    train.head(10)
        '''
    , language="python")
    
    col2.dataframe(train.head(10))

    col2.warning('- **PassengerId, Name은 생존 여부와 상관 없어 보이니 제외하자!** \n - **Name으로 가족 여부를 확인할 수도 있지만 Ticket, Cabin, SibSp, Parch로도 추정할 수 있을 것이다**', icon="🤔")
    
with st.container():
    st.subheader('5️⃣ 데이터 요약 정보 확인')
    st.code(
        '''
    train = train.drop(['PassengerId', 'Name'], axis=1)
    train.describe(include="all")
        '''
    , language="python")    
    train = train.drop(['PassengerId', 'Name'],axis=1)
    st.dataframe(train.describe(include="all"),width=1200)
    st.info('- **Ticket, Cabin에 중복 값이 있는 것으로 보아 가족일 가능성이 있다.** \n - **Cabin과 Embarked의 결측치를 Ticket이 같으면 같은 값을 가지도록 대체하면 어떨까?** \n - **SibSp와 Parch모두 동승한 가족 수이니 합쳐도 되지 않을까?**', icon="🤓")
    