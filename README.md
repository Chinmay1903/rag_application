# 📌 Project Documentation (README.md)
This README provides step-by-step instructions to set up, run, and test the **Django + Vue.js** project using **Docker**.

---

## 📌 Project Overview
This project is a **Django API + Vue.js frontend** with user authentication, file upload, and OpenAI-based Q&A functionality. The backend uses **Django REST Framework (DRF) & PostgreSQL**, while the frontend is built using **Vue 3**.

---

## 📌 Prerequisites
Ensure you have the following installed:

- **Docker** & **Docker Compose** → [Download Here](https://www.docker.com/get-started)
- **Git** (for cloning the repository)
- **Make sure ports 8000, 8080, and 5432 are free** (Django, Vue, and PostgreSQL)

---

## 📌 Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Chinmay1903/rag_application.git
cd your-repo
```
### 2️⃣ Configure Environment Variables
Rename .env.example to .env in the backend:

```bash
cd backend
cp .env.example .env
```
Update the `.env` file with the correct values:
```ini
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
```
### 3️⃣ Build and Run Docker Containers
Navigate to the project root directory and run:
```bash
docker-compose up --build
```
This will:
- Build and start PostgreSQL, Django backend, and Vue frontend.
- Run migrations automatically.
- Start the Django development server on `http://localhost:8000`.
- Start the Vue frontend on `http://localhost:8080`.

✅ Check Running Containers:
```bash
docker ps
```

## 📌 Running the Backend (Django API)
The backend runs on `http://localhost:8000/api/`.

### 1️⃣ Manually Apply Migrations (If Needed)
```bash
docker exec -it django_backend python manage.py migrate
```
### 2️⃣ Create a Superuser (For Admin Access)
```bash
docker exec -it django_backend python manage.py createsuperuser
```
### 3️⃣ Run Django Shell
```bash
docker exec -it django_backend python manage.py shell
```
### 4️⃣ API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/register/` | User registration |
| `POST` | `/api/login/` | User login (JWT token) |
| `POST` | `/api/upload/` | Upload document |
| `POST` | `/api/ask/<doc_id>/` | Ask a question about the document |
| `GET`  | `/api/admin/` | Django Admin Panel |

## 📌 Running the Frontend (Vue.js)
The Vue frontend runs on `http://localhost:8080/`.

### 1️⃣ Access Vue Frontend
Visit:

```arduino
http://localhost:8080
```
### 2️⃣ Manually Run Vue (If Needed)
```bash
docker exec -it vue_frontend npm run serve
```
## 📌 Running Tests
### 1️⃣ Run Backend Tests (Django)
```bash
docker exec -it django_backend pytest
```
<!-- ### 2️⃣3️⃣ Run Frontend Tests (Vue.js)
```bash
docker exec -it vue_frontend npm run test
``` -->
### 2️⃣ Run Tests in Docker Compose
```bash
docker-compose run test
```

## 📌 Stopping the Project
To stop all containers:
```bash
docker-compose down
```
To restart:
```bash
docker-compose up -d
```

## 📌 Troubleshooting
| **Issue**               | **Solution** |
|-------------------------|-------------|
| **Port Already in Use** | Change ports in `docker-compose.yml`. |
| **Database Errors**     | Reset migrations: `docker exec -it django_backend python manage.py migrate --fake-initial` |
| **Docker Build Fails**  | Run: `docker-compose down && docker-compose up --build` |
| **Login Not Working**   | Ensure JWT tokens are included in API requests. |


## 📌 Project Structure
```bash
your-repo/
│── backend/            # Django API (Backend)
│   ├── api/            # App folder (models, views, serializers)
│   ├── backend/        # Django settings
│   ├── manage.py       # Django CLI
│   ├── Dockerfile      # Backend Dockerfile
│   ├── pytest.ini      # Test configuration
│── frontend/           # Vue.js Frontend
│   ├── src/            # Vue components
│   ├── package.json    # Vue dependencies
│   ├── Dockerfile      # Frontend Dockerfile
│── docker-compose.yml  # Docker Compose config
│── README.md           # Documentation
```

### ✅ Conclusion
This guide helps you set up, run, and test the Django + Vue project with Docker. 🚀

If you have any issues, feel free to open an issue on GitHub. 🛠
Happy Coding! 😊🎉


