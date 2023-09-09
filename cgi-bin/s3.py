#!/usr/bin/env python3

import cgi
import os
import boto3


AWS_ACCESS_KEY_ID = 'AKIA4H6T3K6QKULMW5HV'
AWS_SECRET_ACCESS_KEY = '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'
BUCKET_NAME = 'newtask10'


s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def upload_to_s3(file_path, bucket_name, object_name):
    s3.upload_file(file_path, bucket_name, object_name)

def main():
    form = cgi.FieldStorage()

    if "document" in form:
        document = form["document"]
        
        if document.filename:
            
            uploaded_file_path = os.path.join('/tmp', os.path.basename(document.filename))
            with open(uploaded_file_path, 'wb') as f:
                f.write(document.file.read())
            
        
            s3_object_name = f"uploaded_documents/{document.filename}"
            upload_to_s3(uploaded_file_path, BUCKET_NAME, s3_object_name)
            print("Document uploaded successfully!")
        else:
            print("No file selected.")
    else:
        print("No document field found in the form.")

if __name__== "__main__":
    print("Content-type: text/html\n")
    print("<html><body>")
    main()
    print("</body></html>")