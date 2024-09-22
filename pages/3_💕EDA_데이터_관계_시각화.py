import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(
    page_title="EDA 데이터 관계 시각화 EDA",
    page_icon="💕",
    layout="wide")

@st.cache_data
def get_train_data():
    return pd.read_csv("./data/train.csv")

train = get_train_data()
train = train.drop(['PassengerId','Name'],axis=1)

with st.sidebar: 
    st.header("🎯타켓변수와의 관계")
    st.subheader('1️⃣ 범주형/이산형 변수')
    options = st.multiselect('변수를 선택하세요. (최대 2개 선택 가능)', ['Pclass', 'Sex', 'SibSp','Parch', 'Embarked'] ,max_selections=2)

    st.subheader('2️⃣ 연속형 변수')
    options2 = st.multiselect('변수를 선택하세요. (최대 2개 선택 가능)', ['Age', 'Fare'], max_selections=2 )

    st.header('🔎 변수들간의 관계')
    options3 = st.multiselect('연속형 변수를 1개 선택하세요.', ['Age', 'Fare'], max_selections=1 )
    options4 = st.multiselect('범주형 변수를 1개 선택하세요.', ['Pclass', 'Sex', 'SibSp','Parch', 'Embarked'], max_selections=1 )    

st.header('💕 EDA2. 데이터 관계 시각화 해보기')

with st.container():
    with st.expander("코드보기"):
        st.code('''
    mypalette = {0: '#A9A9A9', 1: '#4A90E2'} 

    if len(options) == 1:
        plt.rcParams['font.family'] ='Malgun Gothic'
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))

        sns.barplot(data=train, x=options[0], y='Survived', hue=options[0], palette=sns.cubehelix_palette(), ci=None, ax=axs[0])
        axs[0].set_title(f'{options[0]} 내 Survived비율')
        for p in axs[0].patches:
            height = p.get_height()
            if height > 0:  # 높이가 0보다 클 때만 텍스트 표시
                axs[0].text(p.get_x() + p.get_width() / 2., height + 0.01, f'{height:.2f}', ha='center', size=9)

        sns.countplot(data=train, x=options[0], hue='Survived', palette=mypalette, ax=axs[1])
        axs[1].set_title(f'{options[0]} 내 Survived 수')
        for p in axs[1].patches:
            height = p.get_height()
            if height > 0:  # 높이가 0보다 클 때만 텍스트 표시
                axs[1].text(p.get_x() + p.get_width() / 2., height + 0.01, f'{int(height)}', ha='center', size=9)
        st.pyplot(fig)

    elif len(options) == 2:
        plt.rcParams['font.family'] ='Malgun Gothic'  
        fig, ax = plt.subplots(figsize=(12,4))
        sns.lineplot(ax=ax, data=train, x=options[0], y="Survived", hue=options[1], marker='o', ci=None)
        ax.set_title(f'{options[0]} 내 {options[1]} 별 Survived 비율')
        for line in ax.lines:
            for x, y in zip(line.get_xdata(), line.get_ydata()):
                ax.text(x, y + 0.01, f'{y:.2f}', ha='center', size=9)
        st.pyplot(fig)
        
    elif len(options2) == 1:
        col1, col2 = st.columns(2)
        value = col1.slider(f"{options2[0]}의 범위를 선택하세요", 0, int(max(train[options2[0]]))+1, int(max(train[options2[0]])*0.25))
        survived_ratio = train.query(f'{options2[0]} < {value} ')['Survived'].mean()
        col2.success(f"**{options2[0]}가 0 ~ {value} 일 때 생존률: {round(survived_ratio*100,2)}%**",icon="🦺")
        
        fig, axs = plt.subplots(1,2, figsize=(12, 4))
        sns.kdeplot(x=options2[0],data=train,color='gray', ax=axs[0])
        sns.kdeplot(x=options2[0], data=train, hue='Survived', ax=axs[0])
        
        axs[0].axvline(value, c="k", lw=2, alpha=0.5)
        axs[0].set_title(f'Survived별 {options2[0]} 분포')
        
        cummulate_survival_ratio = []
        for i in range(1, int(max(train[options2[0]]))+1):
            cummulate_survival_ratio.append(train[train[options2[0]] < i]['Survived'].mean())
            
        axs[1].plot(cummulate_survival_ratio)
        axs[1].axvline(value, c="k", lw=2, alpha=0.5)
        axs[1].set_title(f'{options2[0]}에 따른 누적 생존 비율')
        plt.ylabel('Survival rate')
        plt.xlabel('Range of Age(0~x)')
        plt.legend([f'{options2[0]} 누적 확률'])
        st.pyplot(fig)  
        
    elif len(options2) == 2:
        fig, ax = plt.subplots(figsize=(12,4))
        sns.scatterplot(ax=ax, data=train, x=options2[0], y=options2[1], hue="Survived")
        ax.set_title(f'{options2[0]} 와 {options2[1]} 의 Survived 별 분포')
        st.pyplot(fig)

    elif len(options3)*len(options4) == 1:
        fig, ax = plt.subplots(figsize=(12, 4))
        sns.kdeplot(x=options3[0], data=train, hue=options4[0])
        plt.xlim(0, train[options3[0]].max())
        st.pyplot(fig)  

    else:
        st.success('**왼쪽의 사이드바에서 변수를 선택해 주시면 그래프가 나타납니다!**', icon="😄")
    ''')

    mypalette = {0: '#A9A9A9', 1: '#4A90E2'} 

    if len(options) == 1:
        plt.rcParams['font.family'] ='Malgun Gothic'
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))

        sns.barplot(data=train, x=options[0], y='Survived', hue=options[0], palette=sns.cubehelix_palette(), ci=None, ax=axs[0])
        axs[0].set_title(f'{options[0]} 내 Survived비율')
        for p in axs[0].patches:
            height = p.get_height()
            if height > 0:  # 높이가 0보다 클 때만 텍스트 표시
                axs[0].text(p.get_x() + p.get_width() / 2., height + 0.01, f'{height:.2f}', ha='center', size=9)

        sns.countplot(data=train, x=options[0], hue='Survived', palette=mypalette, ax=axs[1])
        axs[1].set_title(f'{options[0]} 내 Survived 수')
        for p in axs[1].patches:
            height = p.get_height()
            if height > 0:  # 높이가 0보다 클 때만 텍스트 표시
                axs[1].text(p.get_x() + p.get_width() / 2., height + 0.01, f'{int(height)}', ha='center', size=9)
        st.pyplot(fig)

    elif len(options) == 2:
        plt.rcParams['font.family'] ='Malgun Gothic'  
        fig, ax = plt.subplots(figsize=(12,4))
        sns.lineplot(ax=ax, data=train, x=options[0], y="Survived", hue=options[1], marker='o', ci=None)
        ax.set_title(f'{options[0]} 내 {options[1]} 별 Survived 비율')
        for line in ax.lines:
            for x, y in zip(line.get_xdata(), line.get_ydata()):
                ax.text(x, y + 0.01, f'{y:.2f}', ha='center', size=9)
        st.pyplot(fig)
        
    elif len(options2) == 1:
        col1, col2 = st.columns(2)
        value = col1.slider(f"{options2[0]}의 범위를 선택하세요", 0, int(max(train[options2[0]]))+1, int(max(train[options2[0]])*0.25))
        survived_ratio = train.query(f'{options2[0]} < {value} ')['Survived'].mean()
        col2.success(f"**{options2[0]}가 0 ~ {value} 일 때 생존률: {round(survived_ratio*100,2)}%**",icon="🦺")
        
        fig, axs = plt.subplots(1,2, figsize=(12, 4))
        sns.kdeplot(x=options2[0],data=train,color='gray', ax=axs[0])
        sns.kdeplot(x=options2[0], data=train, hue='Survived', ax=axs[0])
        
        axs[0].axvline(value, c="k", lw=2, alpha=0.5)
        axs[0].set_title(f'Survived별 {options2[0]} 분포')
        
        cummulate_survival_ratio = []
        for i in range(1, int(max(train[options2[0]]))+1):
            cummulate_survival_ratio.append(train[train[options2[0]] < i]['Survived'].mean())
            
        axs[1].plot(cummulate_survival_ratio)
        axs[1].axvline(value, c="k", lw=2, alpha=0.5)
        axs[1].set_title(f'{options2[0]}에 따른 누적 생존 비율')
        plt.ylabel('Survival rate')
        plt.xlabel('Range of Age(0~x)')
        plt.legend([f'{options2[0]} 누적 확률'])
        st.pyplot(fig)  
        
    elif len(options2) == 2:
        fig, ax = plt.subplots(figsize=(12,4))
        sns.scatterplot(ax=ax, data=train, x=options2[0], y=options2[1], hue="Survived")
        ax.set_title(f'{options2[0]} 와 {options2[1]} 의 Survived 별 분포')
        st.pyplot(fig)

    elif len(options3)*len(options4) == 1:
        fig, ax = plt.subplots(figsize=(12, 4))
        sns.kdeplot(x=options3[0], data=train, hue=options4[0])
        plt.xlim(0, train[options3[0]].max())
        st.pyplot(fig)

    else:
        st.success('**왼쪽의 사이드바에서 변수를 선택해 주시면 그래프가 나타납니다!**', icon="😄")
        col1, col2 = st.columns(2)      
        
        with col1:
            col1.subheader('📊 범주형/이산형 변수')
            with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 2px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 5px)
                }
                """,
        ):
                st.write('**🎯 타켓변수: Survived** (범주형,명목형)')
                st.write('**✅ Pclass** (범주형,순서형)')
                st.write('**✅ Sex** (범주형,명목형)')
                st.write('**✅ SibSp** (수치형,이산형)')
                st.write('**✅ Parch** (수치형,이산형)')
                st.write('**✅ Embarked** (범주형,명목형)')
                st.write('**✖️ PassengerId** - 의미없는 변수')
                st.write('**✖️ Name** 직접적인 관계 없음')
                st.write('**✖️ Ticket** 전처리 필요')
                st.write('**✖️ Cabin** 전처리 필요')
                
                
        with col2:
            col2.subheader('📈 연속형 변수')
            with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 2px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 5px)
                }
                """,
        ):
                st.write('**✅ Age** (수치형,연속형)')
                st.write('**✅ Fare** (수치형,연속형)')

