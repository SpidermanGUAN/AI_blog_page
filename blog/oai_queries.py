# import settings
from django.conf import settings
import os
import openai

# OpenAI API Key
'''
if settings.OPENAI_API_KEY:
    openai.api_key = settings.OPENAI_API_KEY
else:
    raise Exception('OpenAI API Key not found')
'''

# OpenAI API Key
if settings.OPENAI_API_KEY:
    openai.api_key = settings.OPENAI_API_KEY
else:
    raise Exception('OpenAI API Key not found')


def get_completion(prompt):
    system_prompt = "You are a blog writer. User will give you some key words, you rephrase them and write a blog post.Give a title and a content seperatedly."
    query = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "system", "content": system_prompt},{"role": "user", "content": prompt }]
    )
    print("pass message")
    response = query.get('choices')[0]['message']['content']
    print("get response")
    return response
