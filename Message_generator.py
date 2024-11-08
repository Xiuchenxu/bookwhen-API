import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

url = "https://api.bookwhen.com/v2/events"
api_key = "" #Enter API token here

response = requests.get(url, auth=HTTPBasicAuth(api_key, ''))

if response.status_code == 200:
    data = response.json()
    formatted_events = "@所有人  本周课程预告～🔥💃\n\n"
    
    for event in data['data']:
        title = event['attributes']['title']
        start_at = datetime.fromisoformat(event['attributes']['start_at'][:-6])  # Removing timezone for formatting
        end_at = datetime.fromisoformat(event['attributes']['end_at'][:-6])
        
        day_of_week = "周四" if start_at.weekday() == 3 else "周五" if start_at.weekday() == 4 else "周六" if start_at.weekday() == 5 else "周日"
        
        date_str = f"{start_at.day}th {start_at:%I:%M%p}-{end_at:%I:%M%p}"
        date_str = date_str.replace("th", "号")
        instructor = "@" + ("Holly" if "Holly" in event['attributes']['tags'] else
                            "Flora" if "Flora" in event['attributes']['tags'] else
                            "Yan" if "Yan" in event['attributes']['tags'] else "Nicholas")

        link = event['links']['self']
        location = event['relationships']['location']['data']['id']
        location = "Base: James Brown Studio" if "b4owg0oy6kbu" in location else "Manor Studio 4" if "oofym055zbp1" in location else "The Place Studio 1" if "1qy2wnol1e8b" in location else print(location)
        
        formatted_events += f"🩵{day_of_week} {date_str} ｜<{title}> {title.split('-')[0].strip()}\n{instructor}\n🔗 \n📍{location}\n\n"

    formatted_events += "宝宝们可以提前查看链接里的视频做好准备。如果有任何问题，欢迎随时在群里沟通！期待大家的精彩表现！💃🕺"
    print(formatted_events)


    formatted_events +=  "\n\nThis week's timetable 👀\n\n"
    
    for event in data['data']:
        title = event['attributes']['title']
        start_at = datetime.fromisoformat(event['attributes']['start_at'][:-6])  # Removing timezone for formatting
        end_at = datetime.fromisoformat(event['attributes']['end_at'][:-6])
        
        day_of_week = "Thursday" if start_at.weekday() == 3 else "Friday" if start_at.weekday() == 4 else "Saturday" if start_at.weekday() == 5 else "Sunday"
        
        date_str = f"{start_at.day}th {start_at:%I:%M%p}-{end_at:%I:%M%p}"
        instructor = "@" + ("Holly" if "Holly" in event['attributes']['tags'] else
                            "Flora" if "Flora" in event['attributes']['tags'] else
                            "Yan" if "Yan" in event['attributes']['tags'] else "")
        location = event['relationships']['location']['data']['id']
        location = "Base: James Brown Studio" if "b4owg0oy6kbu" in location else "Manor Studio 4" if "oofym055zbp1" in location else "The Place Studio 1" if "1qy2wnol1e8b" in location else print(location)
        
        formatted_events += f"🩵{day_of_week} {date_str} ｜ <{title}> {title.split('-')[0].strip()}\n{instructor}\n📍{location}\n\n"

    formatted_events += "Look forward to seeing you all come slay "
else:
    print(f"Failed to retrieve events: {response.status_code}")
    print(response.text)

with open("messages.txt", "w") as file:
        file.write(formatted_events)
