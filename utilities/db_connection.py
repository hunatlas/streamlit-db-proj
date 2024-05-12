import streamlit as st
from google.cloud import firestore

def connect_to_firebase():
    if 'firestore_db' not in st.session_state:
        firestore_db = firestore.Client.from_service_account_json('firestore-key.json')
        st.session_state['firestore_db'] = firestore_db
    return st.session_state['firestore_db']