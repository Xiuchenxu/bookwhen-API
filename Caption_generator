
from openai import OpenAI

import requests
from requests.auth import HTTPBasicAuth
# Initialize the OpenAI client with your API key

client = OpenAI(api_key="ENTER API KEY HERE",  # Replace with ChatGPT API key
)

url = "https://api.bookwhen.com/v2/events"
api_key = "ENTER API KEY HERE" # Replace with bookwhen API key

bwresponse = requests.get(url, auth=HTTPBasicAuth(api_key, ''))
data = bwresponse.json()

event_details = ""

for event in data['data']:
    title = event['attributes'].get('title', 'No Title')
    tags = ", ".join(event['attributes'].get('tags', []))  # Join tags into a comma-separated string
    event_details += f"Title: {title} | Tags: {tags}\n"

print(event_details)

airesponse = client.chat.completions.create(
  model="gpt-3.5-turbo", #Feel free to change. We use gpt 3.5 because it is cheaper.
  messages=[
    {
      "role": "system",
      "content": "You will be given structured data, each row represents a dance class. Please convert each class information into a paragraph of instagram caption, and print out those separate paragraphs. Be creative with advertising the class, you can praise the teacher, the song, the routine, the studio space or the students. Then also generate those captions in chinese, for posting on XHS"
    },
    {
      "role": "user",
      "content": event_details
    }
  ],
  temperature=0.7,
  max_tokens=200, #Increase this number if there are a lot of classes
  top_p=1
)

print(airesponse)
reply = airesponse.choices[0].message.content
print(reply)
with open("messages.txt", "w") as file:
        file.write(reply)
