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



#"Contents of `pages_sections.toml`"

#st.code(Path("pages_section.toml").read_text(), language="toml")

# "Streamlit script:"

with st.echo("below"):
    from st_pages import show_pages_from_config

    show_pages_from_config("pages_section.toml")


# with st.expander("Show documentation"):
#     from st_pages import add_indentation

#     st.help(show_pages)

#     st.help(Page)

#     st.help(add_page_title)

#     st.help(Section)

#     st.help(add_indentation)

# from st_pages import Page, Section, show_pages,add_page_title

# add_page_title() # By default this also adds indentation

# # Specify what pages should be shown in the sidebar, and what their titles and icons
# # should be
# show_pages(
#     [
#         Page("basic.py", "Basic Information", "🏠"),
#         Page("lifestyleInformation.py", "life Style Information", ":books:"),
#         #Section("My section", icon="🎈️"),
#         # # Pages after a section will be indented
#         # Page("Another page", icon="💪"),
#         # # Unless you explicitly say in_section=False
#         # Page("Not in a section", in_section=False)
#     ]
# )
