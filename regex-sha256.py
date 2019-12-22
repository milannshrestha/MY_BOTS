#regex for extracting all sha256 hash from given url

import re
import requests
from time import sleep

#regex = (r"[A-Fa-f0-9]{64}")
url = requests.get('https://paste.cryptolaemus.com/emotet/2019/12/19/emotet-malware-IoCs_12-19-19.html')
intxt = url.text
string = str(intxt)
put_list = string.split()

r = re.compile("[A-Fa-f0-9]{64}")

newlist = list(filter(r.match, put_list)) # Read Note
for i in newlist:
        print ("SHA256: ",i)
        sleep(1)



