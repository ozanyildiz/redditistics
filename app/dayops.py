from datetime import datetime, timedelta

def get_today():
	return datetime.utcnow()

def get_tomorrow(date):
	one_day = one_day_diff()
	return get_formatted_date(date + one_day)
	
def get_yesterday(date):
	one_day = one_day_diff()
	return get_formatted_date(date - one_day)

def get_formatted_date(date):
	return to_string(date.year, date.month, date.day)

def one_day_diff():
	return timedelta(days=1)

def to_string(year, month, day):
	return str(year) + '-' + str(month) + '-' + str(day)
