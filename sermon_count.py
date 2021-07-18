import requests
from bs4 import BeautifulSoup
import csv

filename = "Sermon_Count_for_Email-06302021.csv"

page = requests.get('https://www.sermonaudio.com/source_detail.asp?sourceid=faithbaptistavon')
soup = BeautifulSoup(page.content, 'html.parser')

#Variable for Date and Time
#Check for date and see if it's Sunday and earlier 10:00AM


#Create Template CSV File if we are on Sunday and it's earlier than 10:00AM AND Delete the old CSV file
header_fields=['Type','Total','Concurrent']
first_row_fields=["Sun_School","Sun_AM","Sun_PM","Wed"]
csv_file_name = 'test_csv.csv'
with open(csv_file_name, 'a') as f:
    wr = csv.writer(f)
    page_numbers = soup.find_all('font', color='880000', class_='ve4') #HTML and Inline CSS we are targeting to pull counts Right Click on page and Inspect Element <font color="880000" class="ve4">16</font>    
    for numbers in page_numbers:
        wr.writerow([numbers.get_text()])
        wr = csv.writer(f)
        print(numbers.get_text())

#if it's not just update the existing CSV file
