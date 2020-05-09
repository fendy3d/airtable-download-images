import pandas as pd
import os
# Import requests, shutil python module.
import requests
import shutil

filename = "airtable.csv"
df = pd.read_csv(filename)

folder_list = list(df["Folder"])
filename_list = list(df["FileName"])
link_list = list(df["Link"])

cwd = os.getcwd() #get current working directory

if len(folder_list) == len(filename_list) == len(link_list):
	for index in range(len(link_list)):

		####### CHECKING IF FOLDER EXIST. IF NOT, CREATE ONE. #######
		folder_path = cwd + "/" + folder_list[index]
		if os.path.exists(folder_path) == False: # If folder does not exist
			print("No folder. Making a directory")
			os.mkdir(folder_list[index])

		####### DOWNLOADING IMAGE #######
		image_url = link_list[index] # Get image URL		
		resp = requests.get(image_url, stream=True) # Open the url image, set stream to True, this will return the stream content.
		local_file = open(folder_path + "/" + filename_list[index]+'.jpg', 'wb') # Open a local file with wb ( write binary ) permission.
		resp.raw.decode_content = True # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
		shutil.copyfileobj(resp.raw, local_file) # Syntax is shutil.copyfileobj(file_source, file_destination). # Copy the response stream raw data to local image file.
		del resp # Remove the image url response object.
		print(filename_list[index] + " image has been downloaded.")
		
else:
	print("The number of rows are not the same across all 3 fields. Please check.")
	print("Number of folder rows: {}".format(len(folder_list)))
	print("Number of FileName rows: {}".format(len(filename_list)))
	print("Number of link rows: {}".format(len(link_list)))
