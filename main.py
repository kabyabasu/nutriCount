from src.input.input import basicInfo
import streamlit as st
if __name__ == "__main__":
    st.image("/workspaces/nutriCount/image/eae413ab-fe80-4cad-862c-584aeed0b894.webp")
    app = basicInfo
    name = app.intro()
    print(name)
