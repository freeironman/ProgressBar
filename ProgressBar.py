#import sys
import os
def get_total_work():
	total_work = 60
	
	# for <loop that counts total work>:
		# total_work = xxx
	# End For
	
	return total_work

#End Function
######################################################################

def print_progress(work_done_so_far, total_work):
	
	total_print_length = 80
	current_print_length = int((float(work_done_so_far) / float(total_work)) * float(total_print_length))
	
	display_string = "\r||"
	count = 0
	
	for count in range(0, current_print_length - 1):
		display_string = display_string + "="
	# End For
	
	display_string = display_string + ">"
	
	for count in range(current_print_length, total_print_length):
		display_string = display_string + " "
	# End For
	
	print display_string + "||",
	#sys.stdout.flush()
	os.system('clear')# cls for windows
	
#End Function
######################################################################
