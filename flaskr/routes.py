from flaskr import app
from datetime import datetime


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/ctime')
def utc_time():
    date_time = datetime.strftime(datetime.utcnow(), "%m/%d/%Y %H:%M:%S")
    return "The UTC time with format 'mm/dd/YYYY HH:MM:SS' is {}".format(date_time)

