import urllib
import urllib.request
data={}
data['word']='alan'
url_value=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_value
data=urllib.request.urlopen(full_url).read()

print(data)
input()