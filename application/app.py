from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def products_name() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'abcd',
        'host': 'database',
        'port': '3306',
        'database': 'products'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products_name')
    results = [{id: name} for (id, name) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'products_name': products_name()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

