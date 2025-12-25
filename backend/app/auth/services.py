from datetime import datetime
from pymongo.collection import Collection
from app.core.security import hash_password, verify_password


def create_user(users_collection: Collection, user_data: dict):
    user_data["password"] = hash_password(user_data["password"])
    user_data["created_at"] = datetime.utcnow()

    result = users_collection.insert_one(user_data)
    return str(result.inserted_id)


def authenticate_user(users_collection: Collection, email: str, password: str):
    user = users_collection.find_one({"email": email})
    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    return user
