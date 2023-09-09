#!/usr/bin/env python3

import cgi
import os
import boto3

# AWS credentials
AWS_ACCESS_KEY_ID = 'AKIA4H6T3K6QOPMZV6DQ'
AWS_SECRET_ACCESS_KEY = 'UX3BQ3m0BOHxMEJKeg0suqh4U65ReI12rXDodWK8'
BUCKET_NAME = 'newtask10'  # Change this to your bucket name

# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def upload_to_s3(file_path, bucket_name, object_name):
    s3.upload_file(file_path, bucket_name, object_name)

def main():
    form = cgi.FieldStorage()

    if "document" in form:
        document = form["document"]
        
        if document.filename:
            # Save the uploaded file locally
            uploaded_file_path = os.path.join('/tmp', os.path.basename(document.filename))
            with open(uploaded_file_path, 'wb') as f:
                f.write(document.file.read())
            
            # Upload the file to S3
            s3_object_name = f"uploaded_documents/{document.filename}"
            upload_to_s3(uploaded_file_path, BUCKET_NAME, s3_object_name)
            print("Document uploaded successfully!")
        else:
            print("No file selected.")
    else:
        print("No document field found in the form.")

if __name__ == "__main__":
    print("Content-type: text/html\n")
    print("<html><body>")
    main()
    print("</body></html>")