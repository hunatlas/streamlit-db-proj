import streamlit as st
from google.cloud import firestore
from  google.oauth2 import service_account
import json
from utilities.firebase_doc import document_exists
from utilities.firebase_doc import insert_document

#key_dict = json.loads(st.secrets['textkey'])
#creds = service_account.Credentials.from_service_account_info(key_dict)
#db = firestore.Client(credentials=creds, project='database-24-415313')

#db = firestore.Client.from_service_account_json('firestore-key.json')

st.title('Book Registration')

with st.form(key='book_form'):
    title = st.text_input('Book title*')
    author_first_name = st.text_input('First name of author*')
    author_last_name = st.text_input('Last name of author*')
    genre = st.text_input('Genre*')
    year = st.text_input('Year*')

    st.markdown('**required*')
    
    submit = st.form_submit_button('Add book to collection')

    if submit:
        if title and author_first_name and author_last_name and genre and year:
            if document_exists(title):
                st.error('Book is already registered.')
            else:
                insert_document(title=title,
                                author_first_name=author_first_name,
                                author_last_name=author_last_name,
                                genre=genre,
                                year=year)
                st.success('Book registered.')
        else:
            st.warning('Fill all required fields.')