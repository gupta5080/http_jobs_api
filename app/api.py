import uvicorn
from fastapi import FastAPI,Body, Query
from typing import Optional
from .db import get_db_connection
app = FastAPI()

@app.get("/")
def read_root():
    return {"root URL": "Welcome to the Job API"}
    
@app.get("/job")
def get_jobs(
    amount: Optional[int] = Query(None, gt=0, description="Maximum number of jobs to retrieve"),
    checkpoint: Optional[int] = Query(None, gt=0, description="The ID to start fetching jobs after")
):
    """
    Fetches job records from the database based on the provided query parameters.

    Args:
        amount (Optional[int]): The maximum number of job records to retrieve. Must be greater than 0.
        checkpoint (Optional[int]): The ID of the last job retrieved. Fetches jobs with IDs greater than this value.

    Returns:
        dict: A dictionary containing a list of job records. Each record includes the job ID and title.
    """
    print("INFO: value of amount and checkpoint", amount, checkpoint)
    if checkpoint is None:
        print("INFO: checkpoint is None")
        checkpoint = 0
    if amount is None:
        print("INFO: amount is None")
        query = "SELECT * FROM jobs HAVING id > %s"
        params = (checkpoint,)
    else:
        print("INFO: Inside else condition where checkpoint and amount is not null")
        query = "SELECT * FROM jobs HAVING id > %s LIMIT %s"
        params = (checkpoint, amount)

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(query, params)
    jobs = cursor.fetchall()
    cursor.close()
    db.close()
    return {
        "jobs": [{"jobId": job['id'], "job": job['title']} for job in jobs]
    }

@app.post("/job")
def create_job(request_body: str = Body(..., media_type="text/plain")):
    """
    Creates a new job record in the database.
    
    Args:
        request_body (str): The title of the job to be created, provided as plain text.
        
    Returns:
        str: The title of the created job record.
    """
    db = get_db_connection()
    cursor = db.cursor()
    print(request_body)
    cursor.execute("INSERT INTO jobs (title) VALUES (%s)", (request_body,))
    db.commit()
    cursor.close()
    db.close()
    return request_body
#to start the server
if __name__ == "__main__":
    print("INFO: Starting server")
    # Uncomment the line below to run the server with uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8080)
