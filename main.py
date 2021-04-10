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

def month_generator(date):
    month = {'Jan': '01',
                 'Feb': '02',
                 'Mar': '03',
                 'Apr': '04',
                 'May': '05',
                 'Jun': '06',
                 'Jul': '07',
                 'Aug': '08',
                 'Sep': '09',
                 'Oct': '10',
                 'Nov': '11',
                 'Dec': '12'
                 }
    return month[date]
  
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
                
    #Code For HackerEarth scrapping( Contributed By : Dev Pandya)    
    URL = requests.get('https://www.hackerearth.com/challenges/').text

    soup = BeautifulSoup(URL, 'html.parser')

    Upcoming_events = soup.find('div', class_='upcoming')
    Event_names = []  # newly added

    for card in Upcoming_events.find_all('div', class_='challenge-card-modern'):
        event_temp = card.find('div', class_='challenge-name').text
        event = event_temp.split('\n')

        date_temp1 = card.find('div', class_='date').text
        date_temp2 = date_temp1.split(' ')
        date_temp3 = date_temp2[1].split(',')

        month = month_generator(date_temp2[0])
        date_passed = f"2021-{month}-{date_temp3[0]}"
        time = f"{date_temp2[2]} {date_temp2[3]}"
        image = card.find('div', class_='event-image').get('style').split('url(\'')
        Link_front = "https://www.hackerearth.com"
        Link_tail = card.a.get('href')
        Link = Link_front + Link_tail
        img = image[1].split('\');')
        if event[1] == "Java Developer Hiring Challenge - May21":
            continue
        else:
            temp = [event[1], date_passed, Link, img[0], "No Data","HackerEarth"]
            Events.append(temp)
            Event_names.append(event[1])
   

    req = requests.get('https://codeforces.com/api/contest.list')
    received = req.text
    data = json.loads(received)
    data_result = data['result']

    for x in data_result:
        if (x['relativeTimeSeconds'] < 0):
            name = x['name']  # Name Var
            start_date = datetime.datetime.today() + datetime.timedelta(seconds=-1 * x['relativeTimeSeconds'])
            s_date = f"{start_date.year}-{start_date.month}-{start_date.day}"  # Start Date Var
            end_date = datetime.datetime.today() + datetime.timedelta(
                seconds=x['durationSeconds'] + (-1 * x['relativeTimeSeconds']))
            e_date = f"{end_date.year}-{end_date.month}-{end_date.day}"  # End Date Var
            website = "https://codeforces.com/contests/page/1"  # Website URL Var
            temp_event_1 = [name, s_date, website, "static\images\\3-01.jpg", e_date, "CodeForces"]
            Events.append(temp_event_1)
    
    return render_template('index.html', events=Events, length=len(Events))
    
 app.run(debug = True)
    
    
    
