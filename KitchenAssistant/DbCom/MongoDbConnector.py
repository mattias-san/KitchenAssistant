from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@kitchendata.0l2p1ib.mongodb.net/"

def LoadUserData():
    client = MongoClient(uri)
    db = client["KitchenData"]
    collection = db["UserData"]
    print(collection)


# Example: Insert a document
#result = collection.find_one({"name": "Alice"})

