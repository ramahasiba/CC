from fastapi import FastAPI
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List  

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class News(BaseModel):
    id: int
    title: str
    content: str

def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql_container',
        user='user',
        password='password',
        database='newsdb'
    )
    return connection

@app.get("/getUrgentNews")
def get_urgent_news():
    print("stage 1")
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    print("stage 3")
    cursor.execute("SELECT * FROM News")
    news = cursor.fetchall()
    cursor.close()
    print("stage 3")
    connection.close()
    return news
