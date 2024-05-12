from utilities.db_connection import connect_to_firebase

def _get_firebase_db():
    return connect_to_firebase()

def document_exists(title):
    db = _get_firebase_db()
    doc_ref = db.collection('books').document(title)
    if doc_ref.get().to_dict():
        return True
    return False

def insert_document(title, author_first_name, author_last_name, genre, year):
    db = _get_firebase_db()
    doc_ref = db.collection('books').document(title)
    doc_ref.set({
                'title' : title,
                'author_first_name' : author_first_name,
                'author_last_name' : author_last_name,
                'genre' : genre,
                'year' : int(year)
                })
    
def get_collection():
    db = _get_firebase_db()
    return db.collection('books').stream()