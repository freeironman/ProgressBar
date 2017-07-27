import time
from ProgressBar import *

total_work = get_total_work()

work_done_so_far = 0

for val in range(0,61): 	#<main processing loop>:
	time.sleep(0.1)
	work_done_so_far = val
	print_progress(work_done_so_far, total_work)
# End For

