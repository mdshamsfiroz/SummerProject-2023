#!/usr/bin/env python

import cgi
from geopy.geocoders import Nominatim

# Create an instance of FieldStorage
form = cgi.FieldStorage()

# Get the location name from the form data
location_name = form.getvalue("location")

# Initialize Nominatim
geolocator = Nominatim(user_agent="GetLoc")

# Get location information
location = geolocator.geocode(location_name)

# HTML header
print("Content-type: text/html\n")

# HTML content
print("<html>")
print("<head>")
print("<title>Location Information</title>")
print("</head>")
print("<body>")

# Print location details if available
if location:
    print("<h1>Location Details:</h1>")
    print("<p><strong>Location Name:</strong> {}</p>".format(location_name))
    print("<p><strong>Address:</strong> {}</p>".format(location.address))
    print("<p><strong>Latitude:</strong> {}</p>".format(location.latitude))
    print("<p><strong>Longitude:</strong> {}</p>".format(location.longitude))
else:
    print("<h1>Location not found.</h1>")

print("</body>")
print("</html>")