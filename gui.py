import csv
import sys
import tkinter as tk
import tkinter.filedialog

class MyApp():
	def __init__(self, root):
		self.root = root
		self.input_path = ''
		self.output_path = ''

		self.open_file_button = tk.Button(text="Select CSV File", command=self.open_file)
		self.open_file_button.pack()

		self.path_label = tk.Label(self.root, text="No file selected")
		self.path_label.pack()

		self.output_entry = tk.Entry(self.root, textvariable=self.output_path)
		self.output_entry.pack()

		self.output_submit_button = tk.Button(text="Save", command=self.set_output_path)
		self.output_submit_button.pack()

		self.output_label = tk.Label(self.root, text='Output name: ')
		self.output_label.pack()

		self.go_button = tk.Button(text="Anonymize Data!", command=self.anonymize_data)
		self.go_button.pack()

	def set_output_path(self):
		self.output_path = self.output_entry.get()
		self.output_label.config(text="Output name: " + self.output_path)

	def open_file(self):
		self.input_path = tk.filedialog.askopenfilename()
		self.path_label.config(text="File path: " + self.input_path)

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
		with open(self.input_path) as csv_input:
			csv_reader = csv.DictReader(csv_input)

			# Grab the header
			header = csv_reader.fieldnames

			with open(self.output_path, 'w+') as csv_output:
				csv_writer = csv.DictWriter(csv_output, fieldnames=header)

				# Write the header to a new file
				csv_writer.writeheader()

				# For each row in the original file, anonymize the data and write to a new file
				for i, row in enumerate(csv_reader):
					self.write_anonymized_row(csv_writer, row)




def main():
	# output_path = 'output.csv'
	root = tk.Tk()
	root.title("Data Anonymizer")
	root.minsize(500,250)
	app = MyApp(root)
	root.mainloop()


main()
