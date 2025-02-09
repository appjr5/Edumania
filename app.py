from flask import Flask, render_template, request, redirect, url_for, flash
import os
import mysql.connector as sql  # Ensure you have mysql-connector-python installed

app = Flask(__name__)

# Secret key for session and CSRF protection
app.secret_key = os.urandom(24)

# MySQL Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "",  # Replace with your MySQL password
    "database": "edumania"
}

@app.route('/register', methods=['POST'])
def signup():
    if request.method == 'POST':
        try:
            # Retrieve form data
            UserID = request.form.get('UserID')
            Name = request.form.get('Name')
            Gender = request.form.get('Gender')
            Phone_No = request.form.get('Phone_No')
            Password = request.form.get('Password')
            Role = request.form.get('Role')
            levels = request.form.getlist('LoEd')  # Checkbox values
            LoEd = ', '.join(levels)  # Combine selected levels into a single string

            # Connect to MySQL
            mydb = sql.connect(**DB_CONFIG)
            cur = mydb.cursor()

            # Execute Insert Query
            cur.execute("""
                INSERT INTO users (UserID, Name, Gender, Phone_No, `Password`, Role, LoEd)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (UserID, Name, Gender, Phone_No, Password, Role, LoEd))

            # Commit and Close
            mydb.commit()
            cur.close()
            mydb.close()

            flash('Signup successful!', 'success')
            return redirect(url_for('registred'))
        
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')
            return f"An error has occurred: {str(e)}"

@app.route('/', methods=['GET'])
def registred():
    return render_template('registration.html') 

if __name__ == '__main__':
    app.run(debug=True)
