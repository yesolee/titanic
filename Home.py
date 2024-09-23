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
   
"""            
)


