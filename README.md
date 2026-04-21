# 🚀 FastAPI Blog API with MongoDB

A fully functional **Blog REST API** built using **FastAPI** and **MongoDB (Motor - Async Driver)**.
This project demonstrates CRUD operations, clean structure, async programming, and modern backend practices.

---

# 📌 Features

* ✅ Create Blog
* ✅ Read All Blogs
* ✅ Read Single Blog
* ✅ Update Blog (PUT)
* ✅ Partial Update (PATCH)
* ✅ Delete Blog
* ✅ Async MongoDB Integration
* ✅ Environment Variable Support
* ✅ Clean Project Structure

---

# 🛠️ Tech Stack

* **Backend Framework:** FastAPI
* **Database:** MongoDB
* **Driver:** Motor (Async MongoDB)
* **Validation:** Pydantic
* **Server:** Uvicorn
* **Environment Config:** python-dotenv

---

# 📂 Project Structure

```
BlogApp MongoDB/
│
├── routers/
│   └── blog.py          # API Routes
│
├── crud.py              # Database logic
├── database.py          # MongoDB connection
├── schemas.py           # Pydantic models
├── main.py              # Entry point
│
├── .env                 # Environment variables
├── .gitignore           # Ignored files
├── requirements.txt     # Dependencies
│
└── myvenv/              # Virtual environment
```

---

# ⚙️ Installation & Setup

## 🔹 1. Clone Repository

```
git clone <your-repo-link>
cd BlogApp MongoDB
```

---

## 🔹 2. Create Virtual Environment

```
python -m venv myvenv
myvenv\Scripts\activate
```

---

## 🔹 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔹 4. Setup Environment Variables

Create `.env` file:

```
MONGO_URL=mongodb://localhost:27017
DB_NAME=blog_db
```

---

## 🔹 5. Start MongoDB Server

```
mongod
```

---

## 🔹 6. Run FastAPI Server

```
uvicorn main:app --reload
```

---

# 🌐 API Documentation

Once server is running:

* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc

---

# 📌 API Endpoints

| Method | Endpoint      | Description     |
| ------ | ------------- | --------------- |
| GET    | `/blogs/`     | Get all blogs   |
| POST   | `/blogs/`     | Create new blog |
| GET    | `/blogs/{id}` | Get single blog |
| PUT    | `/blogs/{id}` | Update blog     |
| PATCH  | `/blogs/{id}` | Partial update  |
| DELETE | `/blogs/{id}` | Delete blog     |

---

# 📥 Sample Request (POST)

```
{
  "title": "Exploring Goa",
  "content": "Beautiful beaches and nightlife",
  "author": "Karan"
}
```

---

# 📤 Sample Response

```
{
  "_id": "662f8c9d8f1a4e3a9c123456",
  "title": "Exploring Goa",
  "content": "Beautiful beaches and nightlife",
  "author": "Karan",
  "created_at": "2026-04-21T10:00:00"
}
```

---

# 🧠 Key Concepts Used

### 🔹 FastAPI

Modern Python framework for building APIs with high performance.

### 🔹 MongoDB

NoSQL database storing data as JSON-like documents.

### 🔹 Motor

Async MongoDB driver for FastAPI.

### 🔹 Pydantic

Used for data validation and serialization.

### 🔹 ObjectId

MongoDB uses `_id` instead of traditional integer IDs.

---

# ⚠️ Important Notes

* MongoDB automatically creates database and collection
* `_id` is converted to string for API responses
* Async (`async/await`) is required when using Motor
* `.env` file should not be pushed to GitHub

---

# 🚫 .gitignore Includes

```
myvenv/
__pycache__/
.env
.vscode/
*.pyc
```

# 👨‍💻 Author

**Karan**
Backend Web Developer (Python)

---

**Happy Coding 🚀**
