import streamlit as st

st.title("Input your information", anchor = False) 
st.divider()

name = st.text_input ( "Enter your Name ")
print ( type (name))
st.write ("Your name is : ", name)

st.divider()
age = st.number_input ( "Enter your Age ", value = None, placeholder="Type your age", step = 1)
print ( type (age))
st.write ("Your age is : ", age)

password = st.text_input ( "Enter your Password ", type = "password")  
#st.write ("Your password is : ", password)  

pressed = st.button("Enter to confirm",type="primary")
if pressed: 
    st.write(f"Your name is {name} and your age is {age}")

selected = st.selectbox("Choose your profession",
             ("Student","Employee","Businessman", "Teacher"),
             index=None,
             accept_new_options = True
             )
st.write ("Your profession is : ", selected)

