#!/usr/bin/env python3
import cgi
import boto3

# Initialize Boto3 Polly client
polly_client = boto3.client('polly')

# HTML header
print("Content-type: text/html\n\n")
print("<html><body>")

# Get user input from the HTML form
form = cgi.FieldStorage()
text_input = form.getvalue("text_input")

# Check if input is provided
if text_input:
    try:
        # Convert text to speech using Amazon Polly
        response = polly_client.synthesize_speech(
            Text=text_input,
            OutputFormat="mp3",
            VoiceId="Joanna"
        )

        # Save the audio stream to an mp3 file
        audio_stream = response['AudioStream'].read()
        audio_filename = "/path/to/output/audio.mp3"  # Replace with actual path
        with open(audio_filename, "wb") as audio_file:
            audio_file.write(audio_stream)

        # Display success message and provide a link to the generated audio file
        print("<h2>Text to Speech Conversion Successful!</h2>")
        print(f"<p>Download the audio: <a href='{audio_filename}'>audio.mp3</a></p>")
    except Exception as e:
        print(f"<h2>Error: {str(e)}</h2>")
else:
    # Display the input form
    print("<h2>Text to Speech Conversion</h2>")
    print("<form method='post'>")
    print("<textarea name='text_input' rows='4' cols='50'></textarea><br><br>")
    print("<input type='submit' value='Convert to Speech'>")
    print("</form>")

# Close HTML body and document
print("</body></html>")
