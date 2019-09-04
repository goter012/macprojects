import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0'

mykey = "api_key=TYurgUWrgbIB6jzopeuzp8LIG3sntrGKXejH6euu"

apodurlobj = urllib.request.urlopen(apodurl+mykey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread.decode("utf-8"))

print("\n\nConverted python data")
print(decodeapod)

