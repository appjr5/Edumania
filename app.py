from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Secret key for session and CSRF protection
app.secret_key = os.urandom(24)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_user'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'edumania'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('Name')
        gender = request.form.get('Gender')
        phone_number = request.form.get('Phone Number')
        password = request.form.get('Password')
        role = request.form.get('Role')
        levels = request.form.getlist('Level of Education')  # Checkbox values
        level_of_education = ', '.join(levels)  # Combine selected levels into a single string

        # Save data to MySQL database
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                """
                INSERT INTO users (name, gender, phone_number, password, role, level_of_education)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (name, gender, phone_number, password, role, level_of_education)
            )
            mysql.connection.commit()
            cur.close()
            flash('Signup successful!', 'success')
            return redirect(url_for('signup'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
