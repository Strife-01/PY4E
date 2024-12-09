import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False :
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True :
    address = input("Enter a location: ")
    if len(address) < 1 : break

    params = dict()
    params['address'] = address
    if api_key is not False : params['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(params)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieving', len(data), 'characters')

    try :
        js = json.loads(data)
    except :
        js = None

    if not js or 'status' not in js or js['status'] != 'OK' :
        print('======== Failure To Retrieve ========')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

    add_comp = js['results'][0]['address_components']
    country_code = None
    for li in add_comp :
        found = False
        if 'types' in li :
            for t_li in li['types'] :
                if t_li == 'country' :
                    country_code = li['short_name']
                    found = True
                    break
        if found == True : break

    print(country_code)

