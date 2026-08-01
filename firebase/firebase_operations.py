from firebase.firebase_config import db


def save_user_to_firebase(full_name, email, phone):

    try:

        db.collection("users").add({

            "full_name": full_name,
            "email": email,
            "phone": phone

        })

        print("✅ User saved to Firebase")

        return True

    except Exception as e:

        print(f"❌ Firebase Error: {e}")

        return False