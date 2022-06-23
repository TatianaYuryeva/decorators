from functools import wraps
import datetime


def log_decorator(old_func):

	@wraps(old_func)
	def new_func(*args, **kwargs):
		start = datetime.datetime.now()
		result = old_func(*args, **kwargs)
		with open("func.log", "a", encoding="utf-8") as f:
			f.write(f"Start: {start}\n")
			f.write(f"Function name: {old_func.__name__}\n")
			f.write(f"Arguments: {args}, {kwargs}\n")
			f.write(f"Returned: {result}\n\n")
		return result
	return new_func
