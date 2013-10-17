from datetime import datetime, timedelta

def get_today():
	return datetime.utcnow()

def get_next_day(date):
	one_day = one_day_diff()
	return date + one_day
	
def get_prev_day(date):
	one_day = one_day_diff()
	return date - one_day

def construct_datetime_obj(year, month, day):
	return datetime(year, month, day)

def get_formatted_date(date):
	return to_string(date.year, date.month, date.day)

def one_day_diff():
	return timedelta(days=1)

def to_string(year, month, day):
	return str(year) + '-' + str(month) + '-' + str(day)
