# -*- coding:utf-8 -*-
import os
import openai
import json
import requests

from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
from django.urls import reverse

from research.models import *

TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')
TELEGRAM_CHANNEL_ID = os.environ.get('TELEGRAM_CHANNEL_ID')
ARXIV_HOST_URL = os.environ.get('ARXIV_HOST_URL', 'https://arxiv.org')

def generate_msg_for_telegram_channel(paper_object):
    P_SUBJECT = paper_object.subject.name
    P_TITLE = paper_object.title
    P_SUMMARY = paper_object.summary
    
    P_AUTHORS = paper_object.authors
    P_PUBLISHED = paper_object.published_date.strftime('%Y-%m-%d %H:%M:%S')
    P_UPDATED = paper_object.updated_date.strftime('%Y-%m-%d %H:%M:%S')
    
    MESSAGE_TEMPLATE = f"""
<b>[{P_SUBJECT}]</b> | <b>{P_TITLE}</b>
<b>Published</b>: {P_PUBLISHED}
<b>Updated</b>: {P_UPDATED}
<b>By</b>: <i>{P_AUTHORS}</i>
<b>Summary</b>: {P_SUMMARY}
    """
    
    KEYBOARD_TEMPLATE = {
        "inline_keyboard" : [
            [
                {
                    "text" : "arXiv",
                    "url" : ARXIV_HOST_URL + "/abs/" + paper_object.short_id
                },
                {
                    "text" : "PDF",
                    "url" : ARXIV_HOST_URL + "/pdf/" + paper_object.short_id
                }
            ]
        ]
    }
    
    msg_text = MESSAGE_TEMPLATE
    keyboard_markup = json.dumps(KEYBOARD_TEMPLATE)
    
    return msg_text, keyboard_markup

def telegram_send_to_channel(paper_object):
    
    msg_text, keyboard_markup = generate_msg_for_telegram_channel(paper_object)
    
    print(msg_text)

    apiURL = apiURL = f'https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL_ID}&text={msg_text}&reply_markup={keyboard_markup}&parse_mode=HTML&disable_web_page_preview=true'
    
    try:
        response = requests.get(apiURL)
    except Exception as e:
        print(e)