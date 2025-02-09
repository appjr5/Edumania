from flask import Flask, render_template

# Initialize the app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    # Serve your home page 
    return render_template('main.html')

@app.route('/about')
def about():
    # Serve the about page
    return render_template('about.html')

@app.route('/courses')
def courses():
    # Dynamically pass course data to main.html
    courses = [
        {
            "title": "Algebra",
            "description": "Learn Pythagoras Theorem...",
            "price": "TZS 500.00",
            "duration": "1hr",
            "link": "#"
        },
        {
            "title": "Calculus",
            "description": "Master differentiation and integration.",
            "price": "TZS 700.00",
            "duration": "5hrs",
            "link": "#"
        }
    ]
    return render_template('main.html', courses=courses)

@app.route('/registration/page')
def registration():
    return render_template('registration.html')

@app.route('/registration')
def regist():
    return 0
# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=8888)
