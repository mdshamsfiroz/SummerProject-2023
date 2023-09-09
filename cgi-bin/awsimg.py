#!/usr/bin/env python3
import cgi
import boto3

# Initialize AWS Rekognition client
session = boto3.Session(
    aws_access_key_id='AKIA4H6T3K6QKULMW5HV',
    aws_secret_access_key='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',
    region_name='ap-south-1'
)
rekognition_client = session.client('rekognition')

# Read uploaded image
form = cgi.FieldStorage()
uploaded_image = form['image']

# Perform image recognition
response = rekognition_client.detect_labels(
    Image={'Bytes': uploaded_image.file.read()}
)
print("Content-Type: text/html\n")
print("<h2>Recognition Results:</h2>")
print("<ul>")
for label in response['Labels']:
    print(f"<li>{label['Name']} - {label['Confidence']:.2f}%</li>")
print("</ul>")
