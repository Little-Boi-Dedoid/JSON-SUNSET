# JSON-SUNSET
#This will get the sunrise and sunset

import urlib2
import json
request = Request('http://api.sunrise-sunset.org/json?lat=51.458747&lng=-0.288259')
response_from_website = urlopen(request)
###sunrise###
sunrise = response_from_website.read()
sunrisedict = json.loads(sunrise)]
###sunset###
sunset = response_from_web_site.read()
sunsetdict = json.loads(sunset)

print(sunrisedict['sunrise'])
print(sunsetdict['sunset'])

