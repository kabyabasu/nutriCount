import streamlit as st
from pathlib import Path

# import basic
# import lifestyleInformation

# PAGES = {"Basic Information": basic, 
#          "Life Style Information": lifestyleInformation}

# st.sidebar.title("Navigation")
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
# selection
# page = PAGES[selection]

# page.app()



"Contents of `pages_sections.toml`"

st.code(Path("pages_section.toml").read_text(), language="toml")

"Streamlit script:"

with st.echo("below"):
    from st_pages import show_pages_from_config

    show_pages_from_config("pages_section.toml")


with st.expander("Show documentation"):
    from st_pages import add_indentation

    st.help(show_pages)

    st.help(Page)

    st.help(add_page_title)

    st.help(Section)

    st.help(add_indentation)
