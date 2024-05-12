import streamlit as st

st.set_page_config(
    page_title='Book Webshop'
)

st.title('Main Page')
st.text('Welcome to the database project created by Ildikó Boros and Gábor Kiss!')
st.text('Select Book Registration to register a new book. \nThe books are stored in a Firestore database.')
st.text('Select Registered Books to display the already registered books.')