# Bookwhen-API

**Bookwhen-API** is a Python application designed to extract booking data from the [Bookwhen](https://bookwhen.com/) website and automate the creation of social media messages and captions in both English and Chinese. (I built this for a dance studio in London to help with make social media management more automated)

This project leverages bookwhen's API to pull event data from Bookwhen, the Data is then organised to generate messages in English and Chinese (simplified) for messaging via Whatsapp or Wechat.
There is the additional API interaction with chatGPT that generates captions for social media platforms like Instagram, Twitter, and Facebook. 

## Features
- Scrapes event data from Bookwhen using API and generates structured message in English and Chinese that could be sent on WeChat and WhatsApp. Message Generation App.
- Generates social media captions in both English and Chinese, by interacting with ChatGPT via API.


## Usage
Please fill out your API tokens for Bookwhen and ChatGPT inside the code then run the application.
Message generation and Social media caption generation are located in two seperate .py files.
