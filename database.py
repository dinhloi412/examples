from fastapi import FastAPI
import uvicorn

from pymongo import MongoClient

app = FastAPI()

# Define global variable for database connection
connect = None

# Connect to database
def connect_database(info: str):
    global connect
    try:
        client = MongoClient(info)
        connect = client["testdb"]
        print("Connected to database")
    except Exception as e:
        print("Something went wrong:", e)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.post("/database")
async def read_database():
    # verify the password 
    url = "mongodb://localhost:27017"
    connect_database(url)
    return {"message": "Connected to database"}

@app.get("/create")
async def create_data():
    if connect is None:
        return {"message": "Database connection not established"}
    
    d = connect["customers"]
    mydict = {"name": "John", "address": "Highway 37"}
    x = d.insert_one(mydict)
    return {"message": "Data inserted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# https://github.com/mongodb-developer/pymongo-fastapi-crud/tree/main