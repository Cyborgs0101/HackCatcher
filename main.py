from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests
import json
import datetime

app = Flask(__name__)

def today_date() :
    t_date = datetime.datetime.today()
    month = t_date.month
    year = t_date.year
    day = t_date.day
    date = f"{year}-{month}-{day}"
    return date
  
@app.route('/')
def hackerEarth():

    Events = []

    #Code For MLH scrapping( Contributed By : Dhairya Patel)
    URL1 = requests.get("https://mlh.io/seasons/2021/events")
    if URL1.status_code != 200:
        print("Sorry an error occured. Please try Again Later:)")
    else:
        soup = BeautifulSoup(URL1.text, 'html.parser')

        final_details = []

        for card in soup.find_all('div', class_='event'):
            event_name = card.find('h3', class_='event-name').text
            t_date = card.find('p', class_='event-date').text
            parent = card.find('div', class_='image-wrap')
            image_wrap = parent.find('img').get('src')
            link = card.find('a', class_='event-link').get('href')
            registration_date = card.find_all('meta')
            new_date_format = date_converter(t_date)
            if new_date_format[0] != " " and new_date_format[1] != " ":
                current_date = today_date()
                date = new_date_format[0].split("-")
                date_curr_list = current_date.split("-")
                d1 = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
                d2 = datetime.datetime(int(date_curr_list[0]), int(date_curr_list[1]), int(date_curr_list[2]))
                if d1 >= d2:
                    temp_details = [event_name, new_date_format[0], link, image_wrap, new_date_format[1], "MLH(Multi League Hacking)"]
                    Events.append(temp_details)
                else:
                    break
            else:
                continue
                
       return render_template('index.html', events=Events, length=len(Events))
    
    app.run(debug = True)
