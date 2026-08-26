
from fastapi import FastAPI
import joblib
import pandas as pd
import mysql.connector

app = FastAPI()
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ml_prediction_db"
    )

model = joblib.load("mymodel.pkl")


@app.get("/")
def testing():
    return {"test": "all ok"}


@app.post("/predication")
def myprediction(hours: float):
    newdata = pd.DataFrame({
        "StudyHours": [hours]
    })

    mynewdata = model.predict(newdata)

    prediction = float(mynewdata[0])

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO predictions (study_hours, prediction)
    VALUES (%s, %s)
    """

    cursor.execute(query, (hours, prediction))

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "prediction": prediction
    }