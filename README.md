🍽️ AI - Powered Smart Recipe Generator

An AI-powered web application that generates customized cooking recipes based on user-provided ingredients, cooking time, servings, and cuisine style.
The system uses an open-source Large Language Model (LLM) via Ollama and is built with Flask for a clean, scalable web experience.

🚀 Features
🔐 User Login System (Session-based)
🧾 Recipe generation using Gemma:2B (Open-source LLM)
🧠 AI-driven cooking instructions
🎨 Modern UI with HTML & CSS
📄 Separate pages for Login, Recipe Input, and Recipe Output
🖥️ Fully local — No paid APIs, no rate limits
🔒 Secure session handling with Flask secret key

🧠 Why This Project?
Most AI recipe generators depend on paid APIs and face:
API quota limits
Cost issues
Network dependency
This project solves those problems by:
Using open-source LLMs
Running fully offline
Giving complete control over the AI model

🛠️ Tech Stack
Layer	Technology
Backend:Flask (Python)
AI Model:	Gemma:2B (via Ollama)
Frontend : HTML, CSS
Session Management : Flask Sessions
Environment Variables	python-dotenv
Model Runtime	Ollama

📂 Project Structure
new_cooking/
│
├── app.py
│
├── templates/
│   ├── login.html
│   ├── index.html
│   └── recipe.html
│
├── static/
│   └── style.css
│
├── .env
├── README.md
└── venv/

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate  

3️⃣ Install Dependencies
pip install flask python-dotenv ollama

4️⃣ Install & Run Ollama

Download Ollama from:
👉 https://ollama.com

Pull the model:
ollama pull gemma:2b
Ensure Ollama is running:
ollama run gemma:2b

5️⃣ Environment Variables
Create a .env file:
FLASK_SECRET_KEY=your_secret_key_here

You can generate one using:
import secrets
print(secrets.token_hex(32))

6️⃣ Run the Application
python app.py

Open browser:

http://127.0.0.1:5000

🔄 Application Flow
Login Page
User enters username & password
Session is created
Main Page
User inputs:
Ingredients
Cooking time
Servings
Cuisine
Recipe Page
AI generates a full recipe
Output is structured and readable
Recipe fills full page width

Session cleared securely

🧪 Example Prompt Used
Create a clear cooking recipe.
Ingredients: eggs, onion, tomato
Cooking Time: 20 minutes
Servings: 2
Cuisine: Indian

🧠 Why Flask?

Lightweight & beginner-friendly
Easy routing and session management
Perfect for AI-based web prototypes
Scales well with WSGI servers (Waitress/Gunicorn)

🧠 Why Gemma:2B?
Open-source
Lightweight and fast
No API keys or costs
Runs fully offline using Ollama

🚀 Future Enhancements
User-specific recipe history
Save favorite recipes
Image-based recipe suggestions
Mobile-responsive UI
Database integration (SQLite / PostgreSQL)
Deployment using Docker

👨‍💻 Author
Prakash
Aspiring AI Engineer
Focused on practical AI systems using open-source tools
