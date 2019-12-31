#!/usr/bin/env python3

import os
import csv
from tkinter import messagebox


def coach():

	path_win = 'C:\prathamdata\Csvfiles\learners.csv'
	path_pi = '/home/pratham/output.csv'

	try:
		if os.path.exists(path_win):
			os.system('kolibri manage importusers C:\prathamdata\Csvfiles\learners.csv')
		elif os.path.exists(path_pi):
			try:
				os.system('kolibri manage import users /home/pratham/output.csv')
			except StopIteration:
				messagebox.showinfo("Pratham", "No value in file please check")

	except FileExistsError as e:
		print(e)
		messagebox.showinfo("pratham", e)


coach()
