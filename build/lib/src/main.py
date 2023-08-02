import sqlite3 as sql
from app.src.website import create_app
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app=create_app('sqlite:///' + os.path.join(basedir, 'database.db'))


#only if we run this file, will the app run
if __name__=='__main__':
    app.run(debug=True)
