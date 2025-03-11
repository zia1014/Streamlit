%matplotlib inline

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(layout="wide", page_title="관리자 페이지")

# 사이드바 - 기업 문서 관리
st.sidebar.header("기업 문서 관리")
search_query = st.sidebar.text_input("Search")

# 문서 리스트 (임시 데이터)
documents = [
    {"name": "문서 1", "status": "green"},
    {"name": "문서 2", "status": "red"},
    {"name": "문서 3", "status": "orange"},
    {"name": "문서 4", "status": "green"},
]

for doc in documents:
    st.sidebar.markdown(f"⭐ **{doc['name']}** 🟢" if doc['status']=='green' else 
                         f"⭐ **{doc['name']}** 🔴" if doc['status']=='red' else 
                         f"⭐ **{doc['name']}** 🟠")

# 메인 컨텐츠
st.title("관리자 페이지")

# 일자별 탐지 통계
dates = ["5월", "6월", "7월", "8월", "9월", "10월", "11월"]
values = [40, 8, 60, 55, 70, 30, 19]

fig, ax = plt.subplots()
ax.plot(dates, values, marker='o', linestyle='-', color='b')
ax.set_ylim(0, 80)
ax.set_title("일자별 탐지 통계")
st.pyplot(fig)

# 오늘 탐지된 횟수
st.subheader("오늘 탐지된 횟수")
st.markdown("**5회 검색 탐지**")
st.markdown("1. 문서1  ")
st.markdown("2. 문서2  ")
st.markdown("3. 문서5  ")
st.markdown("4. 문서6  ")
st.markdown("5. 문서9  ")

# 문서 상세 사항
st.subheader("문서 상세 사항")
st.markdown("### 문서 1 (문서 제목)")
st.markdown("**등록 일자:** 2025년 5월 3일")
st.markdown("**탐지 횟수:** 3 회")
st.markdown("**최대유사도:** 60%")
st.markdown("**업로드 상태:** 업로드 중")

# 탐지 세부 사항 테이블
data = {
    "날짜": ["2025년 6월 20일", "2025년 6월 25일", "2025년 7월 2일", "2025년 7월 10일"],
    "탐지 내용": ["탐지 세부 내용 (요약)"] * 4
}
df = pd.DataFrame(data)
st.table(df)

# 버튼 UI
col1, col2, col3 = st.columns(3)
with col1:
    st.button("업로드")
with col2:
    st.button("삭제")
with col3:
    st.button("다운로드")
