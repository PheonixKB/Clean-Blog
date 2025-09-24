---
# Flask Blog & Contact App

A lightweight blog + contact web app built with Flask and MySQL.  
Allows listing blog posts, viewing about page, submitting contact messages, and basic post management.

---

## Features

- Home page listing blog posts with pagination  
- About page with static content  
- Contact page with a form, storing messages to the database  
- Flash messages for user feedback  
- Post page (currently a static template, can be extended to show post content dynamically)  

---

## Technologies Used

- Python 3.x  
- Flask microframework  
- MySQL (via `mysql-connector-python`)  
- HTML / Jinja2 templates  
- Bootstrap or custom CSS  
- `datetime` for timestamping  

---

## Database Schema

### `contact` table

| Column         | Type         | Notes                                     |
|----------------|-------------|--------------------------------------------|
| sno            | INT (PK, AI) | Primary key, auto-increment               |
| name           | VARCHAR(20) | Sender’s name                             |
| email_address  | VARCHAR(30) | Sender’s email                            |
| phone_number   | VARCHAR(15) | Sender’s phone number                     |
| message        | TEXT        | The message content                       |
| created_at     | DATETIME    | Timestamp (defaults to CURRENT_TIMESTAMP) |

### `posts` table

| Column   | Type           | Notes                                     |
|----------|----------------|-------------------------------------------|
| id       | INT (PK, AI)   | Primary key, auto-increment               |
| title    | VARCHAR(255)   | Title of the post                         |
| subtitle | VARCHAR(255)   | Subtitle of the post (optional)           |
| content  | TEXT           | Main content of the post                  |
| author   | VARCHAR(100)   | Author name                               |
| date     | DATETIME       | Timestamp (defaults to CURRENT_TIMESTAMP) |

---

## Installation & Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/flask-blog-app.git
   cd flask-blog-app
   ```

2. **Set up virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS / Linux
   # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL connection**

   In `app.py`, check:

   ```python
   con = mysql.connector.connect(
       host="localhost",
       user="root",
       password="YOUR_PASSWORD",
       database="flask"
   )
   ```

5. **Run SQL to create tables (if not already done)**

   ```sql
   CREATE DATABASE IF NOT EXISTS flask;

   USE flask;

   CREATE TABLE IF NOT EXISTS contact (
     sno INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(20),
     email_address VARCHAR(30),
     phone_number VARCHAR(15),
     message TEXT,
     created_at DATETIME DEFAULT CURRENT_TIMESTAMP
   );

   CREATE TABLE IF NOT EXISTS posts (
     id INT AUTO_INCREMENT PRIMARY KEY,
     title VARCHAR(255) NOT NULL,
     subtitle VARCHAR(255),
     content TEXT,
     author VARCHAR(100),
     date DATETIME DEFAULT CURRENT_TIMESTAMP
   );
   ```

---

## Running the App

```bash
python app.py
```

* Runs at `http://127.0.0.1:5000/`
* Debug mode is enabled by default in `app.py`

---

## Usage

* `/` → Blog home with list of posts (paginated)
* `/about` → About page
* `/contact` → Contact form (saves to `contact` table)
* `/post` → Static post template (you can extend it to show posts dynamically with `/post/<id>`)

---

## Project Structure

```
flask-blog-app/
├── app.py
├── requirements.txt
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── post.html
├── static/
│   ├── assets/
│   │   ├── img/
│   │   ├── css/
│   │   └── js/
└── README.md
```

---

## To Do / Improvements

* Dynamic post view (`/post/<id>`)
* Add CRUD functionality for posts
* Add form validation for contact page
* Add authentication (admin login to manage posts)
* Improve styling with Bootstrap components
* Use environment variables for secrets and DB credentials

---

## License

MIT License — free to use and modify.

---

**Author**: Kavya Bhatiya

---
