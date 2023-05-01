import csv
import sys

csv_input_file = sys.argv[1]
csv_output_file = sys.argv[2]

def anonymize_name(name):
	return name[0] + '.'

def write_anonymized_row(csv_writer, row):
	# Get the data from the row
	id = row['id']
	first_name = row['first_name']
	last_name = row['last_name']
	phone = row['phone']

	last_name = anonymize_name(last_name)

	# Write the row
	csv_writer.writerow({'id': id, 'first_name': first_name, 'last_name': last_name, 'phone': phone})

def main():
	with open(csv_input_file) as csv_input:
		csv_reader = csv.DictReader(csv_input)

		# Grab the header
		header = csv_reader.fieldnames

		with open(csv_output_file, 'w') as csv_output:
			csv_writer = csv.DictWriter(csv_output, fieldnames=header)

			# Write the header to a new file
			csv_writer.writeheader()

			# For each row in the original file, anonymize the data and write to a new file
			for i, row in enumerate(csv_reader):
				write_anonymized_row(csv_writer, row)

main()
