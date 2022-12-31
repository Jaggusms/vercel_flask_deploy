import streamlit as st
def main():
    st.title("simple login form")
    menu=["Home","login","Signup"]
    choice=st.sidebar.selectbox("menu",menu)
    if choice=="Home":
        st.subheader("Home")
    elif choice=="login":
        st.subheader("Login")
        username=st.sidebar.text_input("User Name")
        password=st.sidebar.text_input("password",type="password")
        if st.sidebar.button("login"):
            st.success(f" login in as {username}")
        
        
    else:
        st.subheader("SignUp")
        
if __name__=="__main__":
    main()