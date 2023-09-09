#!/usr/bin/python3

print("Content-type: text/html")
print()

import cgi
import boto3



translate = boto3.client('translate', aws_access_key_id="AKIA4H6T3K6QKULMW5HV",
    aws_secret_access_key="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", region_name="ap-south-1")

print(translate)


form = cgi.FieldStorage()

source_lang = form.getvalue('source_lang', 'en')
target_lang = form.getvalue('target_lang', 'hi')    
text_to_translate = form.getvalue('text_to_translate', '')

if text_to_translate:
    response = translate.translate_text(
        Text=text_to_translate,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )
    translated_text = response['TranslatedText']