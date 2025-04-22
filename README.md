# http_jobs_api
This project creates api for post and get methods using python, where post and get methods will create and get data from mysql database

---

## 🛠 Features
- **POST /job**: Submit a job (raw string) to the queue
- **GET /job?amount=&checkpoint=**: Retrieve up to N jobs in FIFO order, optionally after a given checkpoint ID
- MySQL used as persistent backing store

---

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gupta5080/http_jobs_api.git
   cd https_jobs_api
   ```

2. **Create an `.env` file** (already included):
   ```env
    MYSQL_ROOT_PASSWORD=root
    MYSQL_DATABASE=message_queue
    MYSQL_USER=admin
    MYSQL_PASSWORD=admin 
   ```

3. **Start the service with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

4. **Test with curl**:
   ```bash
   curl -d '{"foo": "bar"}' http://localhost:8080/job # Add/POST to the job
   curl -d 'ajkashdkja' http://localhost:8080/job # Another example of adding in the queue
   curl http://localhost:8080/job?amount=5 # Example of retrieving data with a limit of 5 aka amount
   curl 'http://localhost:8080/job?amount=5&checkpoint=1' # Example of retrieving data with a limit of 5 and a checkpoint of 1
   curl 'http://localhost:8080/job?checkpoint=2' # Example of retrieving data with a checkpoint of 2
   ```

---

## 📄 API Endpoints

### `POST /job`
- Body: Raw string
- Adds a job with a auto increment id to the the database

### `GET /job?amount=&checkpoint=`
- `amount`: Max number of jobs to fetch (default: all jobs)
- `checkpoint`: Optional job ID after which to fetch jobs (default: all jobs)
- Returns a dictionary containing a list of job records. Each record includes the job ID and job.

---

## 📁 Project Structure
```
.
├── app/
│   ├── api.py         # FastAPI routes and logic   
│   ├── database.py
│   ├── requirements.txt
├── init.sql            # Auto-create table on DB startup
├── docker-compose.yml
├── .env
|── Dockerfile
```

---

## 🤔 Assumptions & Decisions
- MySQL is used with native SQL instead of ORM for simplicity
- Table is initialized via MySQL's `docker-entrypoint-initdb.d` hook
- Jobs are stored as `TEXT` for flexibility
- Used MySql for persistent storage
- Used FastAPI for creating the API as its ease of usage

---

## ✅ Todo (Future Enhancements)
- Move secrets to secret mount for using password so that we are not exposing them in the environment variables
- Using Liquibase or a similar tool for initializing the database schema and loading any pre required data
- Usage of authentication and authorization for the API endpoints.
- Adding a health check endpoint to monitor the status of the API and database connection.
- if the job id is non-integer, logic can be updated to have the primary column as text/string and the checpoint can be managed using another timestamp column which can be used to fetch the data in a sorted manner.

---