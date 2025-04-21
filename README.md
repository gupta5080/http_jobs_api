# http_jobs_api
This project will create api for post and get methods, where post and get methods will create and get data from mysql database

---

## 🛠 Features
- **POST /job**: Submit a job (raw string) to the queue
- **GET /job?amount=&checkpoint=**: Retrieve up to N jobs in FIFO order, optionally after a given checkpoint ID
- MySQL used as persistent backing store

---

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd your-project
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
   curl -d '{"foo": "bar"}' http://localhost:8080/job
   curl -d 'ajkashdkja' http://localhost:8080/job 
   curl http://localhost:8080/job?amount=5
   curl http://localhost:8080/job?amount=5&checkpoint=1
   ```

---

## 📄 API Endpoints

### `POST /job`
- Body: Raw string
- Adds a job to the queue

### `GET /job?amount=&checkpoint=`
- `amount`: Max number of jobs to fetch (default: 10)
- `checkpoint`: Optional job ID after which to fetch jobs
- Returns a list of jobs with `jobId` and payload

---

## 📁 Project Structure
```
.
├── app/
│   ├── api.py         # FastAPI routes
│   ├── database.py     # DB connection
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

---

## ✅ Todo (Future Enhancements)
- Move secrets to secret mount for using password


---