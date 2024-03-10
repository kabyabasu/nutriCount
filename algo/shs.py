import streamlit as st

#new_weigh = st.session_state.weight * 100

def bm(D7,D9):
        # Assuming D7, D8, and D9 are variables in Python that have been previously defined
    D7 = 10  # Example value
    D9 = 20  # Example value


    result = D7 / ((D9 / 100) ** 2)

    print(result)
    return result
if ["bm"] in st.session_state:
    current_bm = st.session_state["bm"]
else:
    current_bm = bm(st.session_state["height"],st.session_state["weight"])
    st.session_state["bm"] = current_bm

# (st.session_state["height"]/ (st.session_state["weight"]/100) ** 2)

