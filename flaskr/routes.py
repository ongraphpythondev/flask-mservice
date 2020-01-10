from flaskr import app
import datetime
import pytz

@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/ctime')
def utc_time():
    current_time = datetime.datetime.now(tz=pytz.utc)
    date_time = current_time.strftime("%m/%d/%Y %H:%M:%S")
    return "The UTC time with format 'mm/dd/YYYY HH:MM:SS' is {}".format(date_time)

@app.route('/ctime/<path:timeZone>')
def utc_time_zone(timeZone):
    try:
        tz = pytz.timezone(timeZone)
        current_time = datetime.datetime.now(tz=tz).strftime("%m/%d/%Y %H:%M:%S")
        response = current_time
    except pytz.exceptions.UnknownTimeZoneError:
        response = "Unknown time zone please provide valid timezone"
    return response
