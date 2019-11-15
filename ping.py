#This script pings a list of IP addresses specified in a text file and uploads the results of those pings to a Google Sheets spreadsheet
#On the Google Sheets side of things, you can automate the change of color of the cells to green or red from the results of this script

import os

import gspread

import time

from oauth2client.service_account import ServiceAccountCredentials





# use creds to create a client to interact with the Google Drive API
# need to create a custom keyfile to authenticate with google sheets

scope = ['https://spreadsheets.google.com/feeds']

creds = ServiceAccountCredentials.from_json_keyfile_name('<PATH_TO_CUSTOM_JSON_KEYFILE_HERE>', scope)

client = gspread.authorize(creds)



# Find a workbook by name and open the first sheet

# Make sure you use the right name here.

sheet = client.open("<NAME_OF_WORKBOOK>").sheet1



row=3 

col=1

col1=1 

col2=2



addresses = []



contents = ""





with open('<PATH_TO_TEXT_FILE_CONTAINING_ALL_IPS>') as f:

	

	for line in f.readlines():

		contents=line

		hostname = contents

		response = os.system("ping -n 1 " + hostname)

			

		if response == 0:

			addresses.append(hostname + 'up!')

			

		else:

			addresses.append(hostname + 'down!')

			



for address in addresses:

	

	if row == 20:

		col1 = col1 + 1

		row = 3

	

	sheet.update_cell(row, col1, address)

	

	row = row + 1
