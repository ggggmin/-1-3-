import streamlit as st

# 제목
st.title("📝 투두리스트")

# 할 일 저장 공간 만들기
if "todos" not in st.session_state:
    st.session_state.todos = []

# 입력창
todo = st.text_input("할 일을 입력하세요")

# 추가 버튼
if st.button("추가"):
    if todo != "":
        st.session_state.todos.append(todo)

# 목록 출력
st.subheader("📌 할 일 목록")

for i, item in enumerate(st.session_state.todos):
    col1, col2 = st.columns([5, 1])

    with col1:
        st.write(f"{i + 1}. {item}")

    with col2:
        if st.button("삭제", key=i):
            st.session_state.todos.pop(i)
            st.rerun()
