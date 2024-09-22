import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  
import time

st.set_page_config(
    page_title="EDA 각 데이터 분포 시각화",
    page_icon="🎨",
    layout="wide")


@st.cache_data
def get_train_data():
    return pd.read_csv("./data/train.csv")

train = get_train_data()
train = train.drop(['PassengerId','Name'],axis=1)

st.header('🎨 EDA 1. 각 데이터 분포 시각화 해보기')

with st.container():
    st.subheader('1️⃣ 각 변수의 분포 그려보기')
    with st.expander("코드보기"):
        st.code(
            '''
        columns_to_plot = train.columns
 
        fig, axs = plt.subplots(2, 5, figsize=(20, 8))  # 2x5 그리드로 10개의 서브플롯 생성
        axs = axs.flatten()  # 2D 배열을 1D로 변환
        
        # 각 컬럼에 대해 반복문을 통해 그래프 생성
        for i, col in enumerate(columns_to_plot):
            if train[col].dtype in ['float', 'int']:
                # 수치형 변수인 경우 히스토그램
                train[col].plot(kind='hist', bins=30, ax=axs[i], title=col)
                
            else:
                # 범주형 변수인 경우 막대그래프
                train[col].value_counts().plot(kind='bar', ax=axs[i], title=col)
                axs[i].set_xticklabels(axs[i].get_xticklabels(), rotation=45)
            
            # x축 이름(축 제목) 제거
            axs[i].set_xlabel('')        
        plt.subplots_adjust(hspace=0.3) 
            '''
        , language="python")

    columns_to_plot = train.columns

    # 서브플롯 설정 (2행 5열 그리드)
    fig, axs = plt.subplots(2, 5, figsize=(20, 8))  # 2x5 그리드로 10개의 서브플롯 생성
    axs = axs.flatten()  # 2D 배열을 1D로 변환

    # 각 컬럼에 대해 반복문을 통해 그래프 생성
    for i, col in enumerate(columns_to_plot):
        if train[col].dtype in ['float', 'int']:
            # 수치형 변수인 경우 히스토그램
            train[col].plot(kind='hist', bins=30, ax=axs[i], title=col)
            
        else:
            # 범주형 변수인 경우 막대그래프
            train[col].value_counts().plot(kind='bar', ax=axs[i], title=col)
            axs[i].set_xticklabels(axs[i].get_xticklabels(), rotation=45)
        
        # x축 이름(축 제목) 제거
        axs[i].set_xlabel('')    
    
    plt.subplots_adjust(hspace=0.3)        
    st.pyplot(fig)
    
    st.info('- **타켓변수의 분포가 극단적이지 않다.** \n - **연속형 변수인 Age와 Fare의 경우 한쪽으로 치우쳐져 있으므로(positive skewed) 정규분포에 근사시키기 위해 log변환 등이 필요해보인다**', icon="🤓")
    
with st.container():
    st.subheader('2️⃣ 결측치 시각화 하기')
    with st.expander("코드보기"):
        st.code('''
        # 결측치 시각화        
        sns.heatmap(train.isnull())  
        
        # 결측치 비율 확인
        missing = train.isnull().mean().to_frame()
        missing = missing.rename(columns={0:'ratio'})      
                ''')
    
    col1, col2 = st.columns([2,1])
    
    # col1 결측치 시각화
    fig, ax = plt.subplots()
    sns.heatmap(train.isnull(), cmap='viridis', cbar=False, ax=ax)
    col1.pyplot(fig)
    
    # col2 결측치 비율 데이터 프레임 출력 
    with col2.container():
        missing = train.isnull().mean().to_frame().reset_index()
        missing = missing.rename(columns={0:'ratio'})
    
        col3, col4, col5 = st.columns(3)
        col3.metric(label="Age", value=f"{float(missing.query('index=="Age"')['ratio'])*100:.2f}%")
        col4.metric(label="Cabin", value=f"{float(missing.query('index=="Cabin"')['ratio'])*100:.2f}%")
        col5.metric(label="Embarked", value=f"{float(missing.query('index=="Embarked"')['ratio'])*100:.2f}%")

        col2.dataframe(missing, width=800)
        col2.warning('**Cabin의 결측치가 약 77%로 너무 많다. drop할지, 어떻게 채울지 고민해보자!**', icon="🤔")
        
    