
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="lab44444",
                        user="postgres",
                        password="RCX1337FUW",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route("/", methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == '' or password == '':
        return render_template('account.html', no_data=True)
    else:
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        if len(records) == 0:
            return render_template('account.html', nepravilno=True)

    return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
