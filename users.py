#!/usr/bin/env python3

import os
import csv
from tkinter import messagebox


def main():

	path_win = "C:\prathamdata\Csvfiles\output.csv"

	path_pi = "/home/pi/output.csv"

	try:

		if os.path.isfile(path_win):

			csvfile = open(path_win, 'r+')

			data = csv.reader(csvfile, delimiter=',')

			for line in data:
				cms = 'kolibri manage shell -c "from kolibri.auth.models import FacilityUser; ' \
					  'FacilityUser.objects.create_superuser(\'' + \
					  line[0] + '\',\'' + line[1] + '\')"'
				os.system(cms)

			csvfile.close()

		elif os.path.isfile(path_pi):
			csvfile1 = open(path_pi, 'r+')

			data = csv.reader(csvfile1, delimiter=',')

			for line in data:
				cms = 'kolibri manage shell -c "from kolibri.auth.models import FacilityUser; ' \
					  'FacilityUser.objects.create_superuser(\'' + \
					  line[0] + '\',\'' + line[1] + '\')"'
				os.system(cms)

			csvfile1.close()
		else:
			messagebox.showinfo("Pratham", "File Not Found")

	except Exception as e:
		messagebox.showinfo("Pratham", e)


main()
