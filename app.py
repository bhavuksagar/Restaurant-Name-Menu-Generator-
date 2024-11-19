import streamlit as st
import langchain_helper


st.title("Welcome To the Restaurant Name And Menu Generator!🍔")
st.write("A Gen-AI based tool for generating the restaurant names and menu on the basis of the cuisine.")
st.write("")

st.subheader("Restaurant Name:")


#cuisine=st.sidebar.selectbox("Pick the cuisine:",("Indian","American","Arabic","Maxican"))
st.sidebar.title("Enter Cuisine:")
cuisine=st.sidebar.text_input("Cuisine:")


result=langchain_helper.main_model(cuisine)



#st.write(result)


st.write(result["restaurant name"])

st.subheader("Menu Items 🍲:")

st.write(result["menu items"])


