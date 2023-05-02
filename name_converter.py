import csv
import sys
import tkinter as tk
import tkinter.filedialog

class DataAnonymizer:
	def __init__(self, csv_input_file='', output_name='', output_path=''):
		self.csv_input_file = csv_input_file
		self.output_name = output_name
		self.output_path = output_path

	def anonymize_name(self, name):
		return name[0] + '.'

	def write_anonymized_row(self, csv_writer, row):
		# Get the data from the row
		id = row['id']
		first_name = row['first_name']
		last_name = row['last_name']
		phone = row['phone']

		last_name = self.anonymize_name(last_name)

		# Write the row
		csv_writer.writerow({'id': id, 'first_name': first_name, 'last_name': last_name, 'phone': phone})

	def anonymize_data(self):
		with open(self.csv_input_file) as csv_input:
			csv_reader = csv.DictReader(csv_input)

			# Grab the header
			header = csv_reader.fieldnames

			# Combine the desired file name with the desired output path
			file_output = self.output_path + '/' + self.output_name

			with open(file_output, 'w') as csv_output:
				csv_writer = csv.DictWriter(csv_output, fieldnames=header)

				# Write the header to a new file
				csv_writer.writeheader()

				# For each row in the original file, anonymize the data and write to a new file
				for i, row in enumerate(csv_reader):
					self.write_anonymized_row(csv_writer, row)

class MyGUI:
	def __init__(self, root, anonymizer):
		self.root = root
		self.anonymizer = anonymizer
		self.build_ui()

	def build_ui(self):
		self.open_file_button = tk.Button(text="Select CSV File", command=self.open_file)
		self.open_file_button.pack()

		self.input_label = tk.Label(self.root, text="No file selected")
		self.input_label.pack()

		self.destination_button = tk.Button(text="Select Destination", command=self.select_destination)
		self.destination_button.pack()

		self.destination_label = tk.Label(self.root, text="No destination selected")
		self.destination_label.pack()

		self.output_entry = tk.Entry(self.root, textvariable=self.anonymizer.output_name)
		self.output_entry.pack()

		self.output_submit_button = tk.Button(text="Save", command=self.set_output_path)
		self.output_submit_button.pack()

		self.output_label = tk.Label(self.root, text='Output name: ')
		self.output_label.pack()

		self.go_button = tk.Button(text="Anonymize Data!", command=self.anonymizer.anonymize_data)
		self.go_button.pack()

	def set_output_path(self):
		self.anonymizer.output_name = self.output_entry.get()
		self.output_label.config(text="Output name: " + self.anonymizer.output_name)

	def open_file(self):
		self.anonymizer.csv_input_file = tk.filedialog.askopenfilename()
		self.input_label.config(text="Input File path: " + self.anonymizer.csv_input_file)

	def select_destination(self):
		self.anonymizer.output_path = tk.filedialog.askdirectory()
		self.destination_label.config(text="Output File path: " + self.anonymizer.output_path)

def main():
	root = tk.Tk()
	root.title("Data Anonymizer")
	root.minsize(500,250)

	data_anonymizer = DataAnonymizer()

	app = MyGUI(root, data_anonymizer)
	root.mainloop()

main()
