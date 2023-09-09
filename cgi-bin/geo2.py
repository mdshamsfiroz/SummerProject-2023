#!/usr/bin/python3

import cgi
import geocoder

print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<title>IP Geolocation</title>")
print("</head>")
print("<body>")

g = geocoder.ip('me')

print("<h2>IP Geolocation</h2>")
print("<p>Your IP address latitude and longitude:</p>")
print("<p>Latitude: {}</p>".format(g.latlng[0]))
print("<p>Longitude: {}</p>".format(g.latlng[1]))

print("</body>")
print("</html>")