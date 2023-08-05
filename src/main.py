import sqlite3 as sql
from website import create_app
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app=create_app('sqlite:///' + os.path.join(basedir, 'database.db'))


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
