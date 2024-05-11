import streamlit as st
from google.cloud import firestore
from  google.oauth2 import service_account
import json

key_dict = json.loads(st.secrets['textkey'])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)

doc_ref = db.collection('books').document('Hyperion')
doc = doc_ref.get()

st.write(f'Book id: {doc.id}')
st.write(f'Book information: {doc.to_dict()}')