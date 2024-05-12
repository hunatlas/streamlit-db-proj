import streamlit as st
from utilities.firebase_doc import get_collection

st.title('Registered Books')

COLS_NUM = 3
cols = []
for col in st.columns([1] * COLS_NUM):
    cols.append(col)

col_idx = 0
for doc in get_collection():
    cols[col_idx].markdown(f'## {doc.id}')
    info = doc.to_dict()
    cols[col_idx].markdown(f'Author: {info['author_first_name']} {info['author_last_name']}')
    cols[col_idx].markdown(f'Genre: {info['genre']}')
    cols[col_idx].markdown(f'Year {info['year']}')
    if col_idx + 1 == COLS_NUM:
        col_idx = 0
    else:
        col_idx += 1