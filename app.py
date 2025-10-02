import streamlit as st

st.set_page_config(
    page_title = "FootySight",
    page_icon = "⚽",
)

if "page" not in st.session_state:
    st.session_state.page = "Home"
    
pages = ['Home', 'Explore', 'About']

for p in pages:
    if st.sidebar.button(p, use_container_width=True):
        st.session_state.page = p
    
if st.session_state.page == "Home":
    st.title("FootySight")
    st.subheader("Coming Soon")

elif st.session_state.page == "Explore":
    st.title("Explore")
    st.subheader("Coming Soon")
    
elif st.session_state.page == "About":
    st.title("About")
    st.subheader("Coming Soon")