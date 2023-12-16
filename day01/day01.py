import re

def read_calibration_value(line):
	numbers = re.findall(r'\d', line)
	return int((numbers[0]+numbers[-1]),10)
	
with open("input.txt", "r") as infile:
	calibration_sum = 0
	calibration_entry = infile.readline()
	while calibration_entry:
		calibration_sum += read_calibration_value(calibration_entry)
		calibration_entry = infile.readline()
		
print(calibration_sum)