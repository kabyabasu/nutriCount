from src.input.input import basicInfo
import streamlit as st
if __name__ == "__main__":
    st.image("./image/eae413ab-fe80-4cad-862c-584aeed0b894.webp",width=100)
    app = basicInfo
    name = app.intro()
    print(name)
