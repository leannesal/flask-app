import sqlite3 as sql
from website import create_app

app=create_app()


#db = SQLAlchemy(app)



#only if we run this file, will the app run
if __name__=='__main__':
    app.run(debug=True)
