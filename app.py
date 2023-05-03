from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    # connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE if not exists mytable (id SERIAL PRIMARY KEY, name TEXT, message TEXT);")
    cursor.execute("INSERT INTO mytable(name, message) VALUES ('Joeaas', 'This app is working just fine!!');")
    cursor.execute("SELECT * FROM mytable;")
    results = cursor.fetchall()
    connection.close()
    final_res = []
    for r in results:
        final_res.append(dict(id=r[0], name=r[1], message=[2]))
    return {'payload': final_res}, 200

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
