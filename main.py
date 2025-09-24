from flask import Flask, render_template, request, redirect, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flashing messages

# Database connection
try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kavya1022",
        database="flask"
    )
    print("Database connected successfully!")
except mysql.connector.Error as e:
    print("Database connection failed:", e)
    con = None

# Home Page
@app.route("/")
def home():
    cur = con.cursor()
    # Get current page number (default = 1)
    page = request.args.get("page", 1, type=int)
    per_page = 4   # Show 4 posts per page
    offset = (page - 1) * per_page
    cur.execute("""
        SELECT id, title, subtitle, author, date 
        FROM posts 
        ORDER BY id DESC 
        LIMIT %s OFFSET %s
    """, (per_page, offset))
    posts = cur.fetchall()

    # Count total posts for pagination
    cur.execute("SELECT COUNT(*) FROM posts")
    total_posts = cur.fetchone()[0]
    cur.close()

    # Pagination logic
    has_next = (page * per_page) < total_posts
    has_prev = page > 1

    return render_template(
        "index.html",
        posts=posts,
        page=page,
        has_next=has_next,
        has_prev=has_prev
    )



# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Contact Page (GET + POST)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    cur = con.cursor()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        # Insert into DB
        sql = "INSERT INTO contact (name, email_address, phone_number, message, created_at) VALUES (%s, %s, %s, %s, %s)"
        values = (name, email, phone, message, datetime.now())
        cur.execute(sql, values)
        con.commit()

        flash("Your message has been sent successfully!", "success")
        return redirect("/contact")

    return render_template("contact.html")

# Post Page
@app.route("/post")
def post():
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)
