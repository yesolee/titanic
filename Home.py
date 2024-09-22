import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon="🛳️",
    layout="wide"
)

with st.sidebar:
    st.markdown(
        """  
        ### 참고 가이드
        - 데이터 분석 어떻게 시작해야 할까요? [캐글 가이드](https://www.kaggle.com/code/daehungwak/guide-kor-dg)
        - 데이터 분석 입문자를 위한 데이터 살펴보기 [데이콘 가이드](https://dacon.io/en/competitions/official/236056/codeshare/7417)
        - 전처리 무엇부터 해야할까? [티스토리 블로그](https://find-in-data.tistory.com/92)
        - 통계를 더 공부해 보고 싶다면? [슬기로운 통계생활](https://statisticsplaybook.com/)
        - 나만의 웹페이지를 쉽게 만들고 싶다면? [streamlit](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app)
    """
    )

st.write("# 타이타닉 생존자 예측 모델링 🛳️")

st.markdown(
        """
    데이터 분석이 처음이시라구요? 저와 함께 단계별로 분석해봐요!
    
    ### 데이터셋 주소
    - 캐글 타이타닉 [다운로드](https://www.kaggle.com/c/titanic/data)
    
    ### 데이터 설명
"""            
)

data_info = pd.DataFrame({
    '변수':['Survived', 'Pclass', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
    '설명': ['생존여부','티켓 등급(사회적지위 가늠)', '성별', '나이', '함께 탑승한 형제/배우자 수', '함께 탑승한 부모/자녀 수','티켓 번호','승객 요금', '객실 번호', '탑승 항구'],
    'Key': ['0: 생존하지 못함, 1: 생존', '1: 상위, 2: 중간, 3: 하위','-','-','-','-','-','-','-','C: Cherbourg,  Q: Queenstown, S: Southampton' ]
})

st.dataframe(data_info, width=1200)

