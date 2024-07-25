from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World from Tyler Hopkins in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab10_postgressql_tylerhopkins_user:FrS8NBHDF7zzcjwub4Q0gSgOA1mfHrjU@dpg-cqh5fliju9rs73egr270-a/lab10_postgressql_tylerhopkins")
    conn.close()
    return "Database connection Successful"