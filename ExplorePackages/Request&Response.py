import urllib.request
import os
import urllib.parse

# Construct Request
values = {}
values['username'] = os.environ.get('DailyKosUserName')
values['password'] = os.environ.get('DailyKosPassword')
data = urllib.parse.urlencode(values)
url = "https://www.dailykos.com/"
geturl = url+'?'+data
request = urllib.request.Request(geturl)
response = urllib.request.urlopen(request)
print(response.read())