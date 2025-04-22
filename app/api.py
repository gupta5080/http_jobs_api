import uvicorn
from fastapi import FastAPI, Body, Query, HTTPException
from typing import Optional
from .db import get_db_connection
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
        dict: A dictionary containing a list of job records. Each record includes the job ID and job.
    """
    logger.info("value of amount and checkpoint: %s, %s", amount, checkpoint)
    try:
        if checkpoint is None:
            logger.info("checkpoint is None")
            checkpoint = 0
        if amount is None:
            logger.info("amount is None")
            query = "SELECT * FROM jobs HAVING id > %s"
            params = (checkpoint,)
        else:
            logger.info("Inside else condition where checkpoint and amount is not null")
            query = "SELECT * FROM jobs HAVING id > %s LIMIT %s"
            params = (checkpoint, amount)

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(query, params)
        jobs = cursor.fetchall()
        cursor.close()
        db.close()
        return {
            "jobs": [{"jobId": job[0], "job": job[1]} for job in jobs]
        }
    except Exception as e:
        logger.error("Unexpected error: %s", e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.post("/job")
def create_job(request_body: str = Body(..., media_type="text/plain")):
    """
    Creates a new job record in the database.
    
    Args:
        request_body (str): The title of the job to be created, provided as plain text.
        
    Returns:
        str: The title of the created job record.
    """
    logger.info("Received request to create job with title: %s", request_body)
    try:
        db = get_db_connection()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO jobs (title) VALUES (%s)", (request_body,))
        except Exception as e:
            logger.error("Error while inserting job into database: %s", e)
            raise HTTPException(status_code=500, detail="Failed to create job")
        db.commit()
        cursor.close()
        db.close()
        logger.info("Job created successfully with title: %s", request_body)
        job_id = cursor.lastrowid
        return {"jobId": job_id, "message": "Job created successfully"}, 201
    except Exception as e:
        logger.error("Unexpected error: %s", e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

# to start the server
if __name__ == "__main__":
    logger.info("Starting server")
    # Uncomment the line below to run the server with uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8080)
