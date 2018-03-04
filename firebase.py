#%%


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

cred = credentials.Certificate("servicekey.json")
firebase_admin.initialize_app(cred)
a=3
data = {
    u'name' : u'abdul',
    u'slotno' : a

}

db = firestore.client()

db.collection(u'slotp').add(data)