from flask import Flask, render_template, request, redirect, session, flash
import ollama
import os
from dotenv import load_dotenv

# ---------------- ENV SETUP ----------------
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev_secret_key")

# ---------------- MODEL CONFIG ----------------
MODEL_NAME = "gemma:2b"   # fast & lightweight

# ---------------- STATIC UI LABELS ----------------
UI_LABELS = {
    "title": "Smart Recipe Generator",
    "ingredients": "Ingredients",
    "cooking_time": "Cooking Time (minutes)",
    "servings": "Servings",
    "cuisine": "Cuisine",
    "generate": "Generate Recipe",
    "recipe": "Generated Recipe",
    "logout": "Logout"
}
# LLM
def generate_text(prompt):
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error generating recipe: {str(e)}"


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            session.clear()
            session["user"] = username
            flash("Login Successfully", "success")
            return redirect("/")
        else:
            flash("Invalid login details", "error")

    return render_template("login.html")


# Main page
@app.route("/", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        session["ingredients"] = request.form.get("ingredients")
        session["time"] = request.form.get("time")
        session["servings"] = request.form.get("servings")
        session["cuisine"] = request.form.get("cuisine")
        return redirect("/recipe")

    return render_template("index.html", labels=UI_LABELS)


# Recipe page
@app.route("/recipe")
def recipe():
    if "user" not in session:
        return redirect("/login")

    prompt = f"""
You are a professional chef.

Create a clear and detailed cooking recipe in ENGLISH.

STRICT FORMAT:

Recipe Title:
Ingredients:
- item 1
- item 2

Cooking Time:
{session.get('time')} minutes

Servings:
{session.get('servings')}

Steps:
1. Step one
2. Step two
3. Step three

Cuisine: {session.get('cuisine')}
Ingredients: {session.get('ingredients')}
"""

    recipe_text = generate_text(prompt)

    return render_template(
        "recipe.html",
        labels=UI_LABELS,
        recipe=recipe_text
    )

if __name__ == "__main__":
    app.run(debug=True)
