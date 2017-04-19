import openpyxl
import sys

# verifies that a given filename has .xlsx extension
# if it does not, an error is thrown
def check_extension(filename):
	extension_flag = 0
	extension = ""
	good_extension = "xlsx"

	for char in filename:
		if extension_flag==0:
			if char==".":
				extension_flag = 1
		else:
			extension+=char

	if extension!=good_extension:
		sys.exit("must pass in .xlsx files")

def main():
	print("checking command line arguments")
	if len(sys.argv)!=4:
		sys.exit("usage: python compare.py filename_A.xlsx filename_B.xlsx output_file.xlsx")
	else:
		print("verifying file extensions")
		for i in range(1, len(sys.argv)):
			check_extension(sys.argv[i])


if __name__ == '__main__':
	main()