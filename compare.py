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

	filename_A = sys.argv[1]
	filename_B = sys.argv[2]
	outfile = sys.argv[3]

	workbook_A = openpyxl.load_workbook(filename_A)
	workbook_B = openpyxl.load_workbook(filename_B)

	sheet_names_A = workbook_A.get_sheet_names()
	sheet_names_B = workbook_B.get_sheet_names()


	compare_A = workbook_A.get_sheet_by_name(sheet_names_A[0])
	compare_B = workbook_B.get_sheet_by_name(sheet_names_B[0])

	print(compare_A['A1'].value)
	print(compare_B['A1'].value)

	# sort by ucsc emails
	# compare ucsc emails
	# if match, write row into outfile
	
	# compare_A: from cell F1 to end of F column
	#	sort emails

	#compare_B: from cell C2 to end of C column
	#	sort emails

if __name__ == '__main__':
	main()