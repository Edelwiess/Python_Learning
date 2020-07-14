import  urllib.request
from w3lib.html import remove_tags
from w3lib.html import remove_tags_with_content
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.3"}

hacgurl = 'https://www.liuli.se/wp/79053.html'



req = urllib.request.Request(hacgurl, headers=headers)
response = urllib.request.urlopen(req)
response = response.read().decode('utf8')
title = re.search(r'<title>(.*?)</title>', response)
if title:
    title = title[1]
response = remove_tags_with_content(response, which_ones=('script','style'))
response = remove_tags(response)
#print(response)
hash_result = re.search(r'[a-fA-F0-9]{40,40}', response, re.M)
magnet_result = ''
if hash_result:
    magnet_result='magnet:?xt=urn:btih:'+hash_result[0]
print(title)
print(magnet_result)


