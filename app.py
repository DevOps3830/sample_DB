from flask import Flask, render_template_string
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    db_host = os.environ['DB_HOST']
    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']
    db_password = os.environ['DB_PASSWORD']

    try:
        cnx = mysql.connector.connect(
            user=db_user, 
            password=db_password,
            host=db_host,
            database=db_name
        )
        cursor = cnx.cursor()
        cursor.execute("SELECT message FROM test_table")
        messages = cursor.fetchall()
        cnx.close()
    except mysql.connector.Error as err:
        return f"Failed to connect or retrieve data: {err}"

    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Data</title>
    </head>
    <body>
        <h1>Fetched Data</h1>
        {% for message in messages %}
            <p>{{ message[0] }}</p>
        {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(html, messages=messages)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
