import uvicorn
from fastapi import FastAPI
from db import get_db_connection
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/jobs")
def get_jobs():
    """
    Fetches all job records from the database.
    
    returns:
        list: A list of dictionaries representing job records.
    """
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    db.close()
    return jobs

@app.post("/jobs")
def create_job(job: dict):
    """
    Creates a new job record in the database.
    
    args:
        job (dict): A dictionary representing the job record to be created.
        
    returns:
        dict: The created job record.
    """
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("INSERT INTO jobs (title, description) VALUES (%s, %s)", (job.title, job.description))
    db.commit()
    job['id'] = cursor.lastrowid
    cursor.close()
    db.close()
    return job
#to start the server
if __name__ == "__main__":
    db=get_db_connection()
    cursor = db.cursor(dictionary=True) 
    create_table_query = """
    CREATE TABLE IF NOT EXISTS jobs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT NOT NULL
    )
    """
    cursor.execute(create_table_query)
    db.commit()
    cursor.close()
    db.close()
    print("Table created successfully.")
    uvicorn.run(app, host="0.0.0.0", port=8080)
