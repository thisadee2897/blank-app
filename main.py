import streamlit as st

def main():
    st.set_page_config(page_title="Main Page", layout="centered")
    
    query_params = st.query_params
    page = query_params.get("page", ["login"])[0]

    if page == "home":
        import home
    else:
        import login

if __name__ == "__main__":
    main()
