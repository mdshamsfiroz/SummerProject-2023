#!/usr/bin/python3

import cgi
import json
import openai
import time
import cgitb

cgitb.enable()
# Set the appropriate headers for a CGI script
print("Content-Type: text/html")
print()

# Get the user's message from the request
form = cgi.FieldStorage()
user_message = form.getvalue('msg')
openai.api_key = "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"


 # Generate response using OpenAI GPT-3
response =  openai_instance.Completion.create(
        engine='text-davinci-003',
        prompt=user_message,
        max_tokens=50,
        temperature=1.2,
        n=1,
        stop=None
        )
print(response.choices[0].text.strip())