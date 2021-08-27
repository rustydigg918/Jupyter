!apt install tesseract-ocr
!apt install libtesseract-dev
!apt install ghostscript
!pip install pytesseract --quiet
!pip install ocrmypdf --quiet
!pip install anvil-uplink --quiet
!pip install camelot-py
!pip install ghostscript
!mkdir input_papers
!mkdir output_papers


# To upload the files from your local system to the drive >>>>>
from google.colab import files
files.upload()

#@title
import os
import ghostscript
import pandas as pd
import camelot as cm

# Extract data from the zip file
input_folder = "/content/input_papers"
for i in os.listdir():
  if i[-4:] == '.zip':
    !unzip "{i}" -d "{input_folder}"

# Getting path from the list
paths = []
for a,b,c in os.walk(input_folder):
  paths.append(a)
input_folder_path = paths[1]   #input folder path
output_folder_path = "/content/output_papers" #output folder path

file_list = []
for filename in os.listdir(input_folder_path):
    if filename.endswith("pdf"): 
      file_list.append(filename)

for filename in file_list:
  print("Converting : " + filename)
  input_filename = input_folder_path+'/'+filename
  output_filename = output_folder_path+'/'+filename
  !ocrmypdf --force-ocr "{input_filename}" "{output_filename}"

  # Extraction of data from searchable pdf
df = pd.DataFrame()
os.chdir(output_folder_path)
for i in os.listdir():
  if i.endswith(".pdf"):
    pdf_data = cm.read_pdf(i, flavor='lattice', pages='1')
    pdf_data_iter = pdf_data[0].df.T
    pdf_data_iter[19] = i
    df = df.append(pdf_data_iter).drop_duplicates(keep='first', subset = [0,1])
    df.iloc[0,19] = "Filename"
  else:
    pass
df.to_csv("test.csv",header=None,index=False)
