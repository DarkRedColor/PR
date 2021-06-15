import urllib.request
import requests
import urllib.parse
import re

def listToString(list): 
    string = "" 
    for element in list: 
        string += element  
    return string

PROXY_ADDRESS = "192.168.0.101:9097"
url = 'https://ro.wikipedia.org/wiki/Python'
resp = requests.get(url, proxies = {"http" : PROXY_ADDRESS})
print("Proxy server returns response headers: %s " %resp.headers)

values =''


data = urllib.parse.urlencode(values)
#print(data)
data = data.encode('utf-8')
#print(data)
req = urllib.request.Request(url, data)
#print(req)
resp = urllib.request.urlopen(req)
#print(resp)
respData = resp.read()
#print(respData)
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
#print(paragraphs)
for eachP in paragraphs:
	print(eachP)

# defining the api-endpoint 
API_ENDPOINT = "https://pastebin.com/api/api_post.php"
  
# your API key here
API_KEY = "3EyLsDeerYFf6prdqAzJfcPR2cRREQDN"
  
# your source code here
source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''

  
# data to be sent to api
data = {'api_dev_key':API_KEY,
        'api_option':'paste',
        'api_paste_code':source_code,
        'api_paste_format':'python'}
  
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
  
# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)

# Making a HEAD request
r = requests.head('https://httpbin.org/', data ={'key':'value'})

# check status code for response recieved
# success code - 200
print(r)

# print headers of request
print(r.headers)

# checking if request contains any content

print(r.content)

url='https://requestbin.com/r/enyasw7ymmvf8'
response = requests.options(url)
methods = re.findall(r"Methods': '.*\w+',", str(response.headers))
methods = listToString(methods)
print(methods.replace('[', '').replace(']', '').replace("',", '').replace("'", ''))
