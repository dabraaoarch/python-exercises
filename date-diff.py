days = {
	1 : 31,
	2 : 28,
	3 : 31,
	4 : 30,
	5 : 31,
	6 : 30,
	7 : 31,
	8 : 31,
	9 : 30,
	10: 31,
	11: 30,
	12: 31
}

def validate_date_format(read_date):
	if len(read_date) != 10:
		raise ValueError("The date must be in the informed format [yyyy-mm-dd].")
		
	array_date = read_date.split("-")
	
	if len(array_date) != 3:
		raise ValueError("The date must be in the informed format [yyyy-mm-dd].")		
	
	if len(array_date[0]) != 4 or len(array_date[1]) != 2 or len(array_date[2]) != 2:
		raise ValueError("Year must have 4 digits, month and day must have 2 digits.")
	
	return array_date


def get_date_from_user(message):
	read_date = input(message)
	array_read_date = validate_date_format(read_date)
	return convert_to_int(array_read_date)
		
def convert_to_int(string_array):
	if len(string_array) != 3:
		raise ValueError("The date must be in the informed format.")
		
	output_array = []
	for index in range(0, len(string_array)):
		output_array += [int(string_array[index])]
		
	return output_array
	
def is_leap_year(year):
	int_type = 0
	if type(year) != type(int_type):
		raise ValueError("The year is not a valid integer")
	
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
		
	return False
	
def literal_date(int_date_array):
	literal = ""
	for i in range(0, len(int_date_array)):
		literal += "-" + str(int_date_array[i])
	return literal[1:]
	
def valid_date_value(date_value_array):
	year, month, day = date_value_array
	if not (month in days.keys()):
		return False
	if day > days[month]:
		if month != 2 or not is_leap_year(year):
			return False
		elif day > days[month] + 1:
			return False			
	return True
	
def calculate_date_diff(start_date, end_date):
	start_year, start_month, start_day = start_date
	end_year, end_month, end_day = end_date
	if start_year > end_year:
		raise ValueError("Initial date is ahead of final date, cant calculate the differente") 

	if not valid_date_value(start_date) or not valid_date_value(end_date):
		raise ValueError("Ivalid date values")
	
	days_of_year_start_date = days_to_end_of_year(start_date)
	days_of_year_end_date = days_to_end_of_year(end_date)
	if start_year==end_year:
		return days_of_year_start_date - days_of_year_end_date
	
	return days_of_year_start_date + days_to_begin_of_year(end_date) + years_in_betwen(start_year, end_year)
		
def years_in_betwen(start, end):
	if end == start+1:
		return 0
	total_days = 0
	for year in range(start, end):
		if	is_leap_year(year):
			total_days += 1
		total_days += 365
	return total_days
	 
def days_to_end_of_year(date):
	year, month, day = date
	total_days = 0
	for i in range(month, 13):
		total_days += days[i]
	total_days -= day
	if month <= 2 and is_leap_year(year):
		total_days += 1
	return total_days
	 
def days_to_begin_of_year(date):
	year, month, day = date
	total_days = 365 - days_to_end_of_year(date)
	if month > 2 and is_leap_year(year):
		total_days += 1
	return total_days 
	

def start():
	try:
		start_date = get_date_from_user("Enter the initial date [yyyy-mm-dd]:")
		end_date = get_date_from_user("Enter the final date [yyyy-mm-dd]:")
		if not valid_date_value(start_date) or not valid_date_value(end_date):
			raise ValueError("Please enter a valid date: {} and {}".format(start_date, end_date))
		days = calculate_date_diff(start_date, end_date)
		if days >= 0:
			print("There are {} days betwen {} and {}".format(days, literal_date(start_date), literal_date(end_date)))
		else:
			print("Initial date is after the final date.")
	except ValueError as error:
		print("You must give a date in the format yyyy-mm-dd e.g. 2021-08-03 \n " + repr(error))
		return False
		
if __name__ == "__main__":
	start()
	