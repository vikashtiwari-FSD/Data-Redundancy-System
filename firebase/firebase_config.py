import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

firebase_app = None
db = None

try:

    if not firebase_admin._apps:

        cred = credentials.Certificate(
            "firebase/serviceAccountKey.json"
        )

        firebase_app = firebase_admin.initialize_app(cred)

    db = firestore.client()

    print("✅ Firebase connected successfully!")

except Exception as e:

    print(f"❌ Firebase Connection Error: {e}")