import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

filename = "Sermon_Count_for_Email-06302021.csv"
csv_file_name = 'test_csv.csv' #template csv file we will save our counts to

page = requests.get('https://www.sermonaudio.com/source_detail.asp?sourceid=faithbaptistavon')
soup = BeautifulSoup(page.content, 'html.parser')

#Variable for Date and Time
current_day_of_the_week = datetime.now().strftime('%a')
current_hour_in_24hr = datetime.now().strftime('%H')
print(current_day_of_the_week)
print(current_hour_in_24hr)
#Check for date and see if it's Sunday and earlier 10:00AM
#If it is then wipe the template csv file
if current_day_of_the_week == "SUN" and current_hour_in_24hr < 10:
        #opening the file with w+ mode truncates the file
    f = open(csv_file_name, "w+")
    f.close()
#if it's not just update the existing CSV file
else:
    with open(csv_file_name, 'a') as f:
        wr = csv.writer(f)
        page_numbers = soup.find_all('font', color='880000', class_='ve4') #HTML and Inline CSS we are targeting to pull counts Right Click on page and Inspect Element <font color="880000" class="ve4">16</font>    
        for numbers in page_numbers:
            wr.writerow([numbers.get_text()])
            wr = csv.writer(f)
            print(numbers.get_text())

