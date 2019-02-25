import httplib, urlparse, sys, urllib
from pymd5 import md5, padding

url = sys.argv[1]

# Your code to modify url goes here
start = url.find("token=")
end = url.find("&user=")
token = url[start+6:end]
length = 8+len(url[end+1:])
bits = (length+len(padding(length*8)))*8
h = md5(state=token.decode("hex"), count=bits)
append = "&command3=UnlockAllSafes"
h.update(append)
newtoken = h.hexdigest()
url = url[:start+6] + newtoken + url[end:] + urllib.quote(padding(length*8)) + append

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
