import google.generativeai as genai
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import os
import json  # To parse AI response properly

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'edumania'

mysql = MySQL(app)

# Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def generate_courses():
    """Fetch AI-generated course suggestions from Gemini."""
    model = genai.GenerativeModel("gemini-pro")
    
    # **Updated Prompt** - Asking for structured JSON output
    prompt = (
        "Suggest 5 online courses from trusted platforms like Khan Academy. "
        "Return the data in JSON format with the following keys: title, category, "
        "price, duration, description, level, and link."
    )
    
    response = model.generate_content(prompt)
    
    try:
        return json.loads(response.text)  # Convert AI response to Python dictionary
    except json.JSONDecodeError:
        return None  # Handle invalid AI response

@app.route('/fetch_ai_courses', methods=['POST'])
def fetch_ai_courses():
    """Fetch AI-generated courses and store them in the MySQL database."""
    try:
        # Generate AI courses
        prompt = "Suggest online courses with title, category, price, duration, description, level, and link from trusted platforms like Khan Academy."
        ai_response = generate_courses(prompt)

        # Ensure the AI response is valid
        if not ai_response:
            return jsonify({"error": "AI did not return a response"}), 500

        # Convert AI response to a structured format
        courses = ai_response.split("\n")  # Adjust parsing as needed

        if not isinstance(courses, list) or len(courses) == 0:
            return jsonify({"error": "Invalid AI response format"}), 500

        # **Batch Insert for Optimization**
        cur = mysql.connection.cursor()
        query = "INSERT INTO courses (title, category, price, duration, description, level, link) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = [(course["title"], course["category"], course["price"], course["duration"], 
                   course["description"], course["level"], course["link"]) for course in ai_courses]
        
        cur.executemany(query, values)  # Insert all rows in one query
        mysql.connection.commit()
        cur.close()
        
        return jsonify({"message": "AI-generated courses added successfully", "courses_added": len(ai_courses)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
