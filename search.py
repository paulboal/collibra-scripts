################################################################################
# search.py
#
# Sample Python script that will log you into Collibra,
# Search for a specified term,
# Print out the matching terms and URL to that term
#
# Author: Paul Boal
# Date: 2015-09-29
# Company: Amitech Solutions
################################################################################


import requests
import json

HOST = '54.210.185.88'
PORT = '8080'
BASE = 'dgc'
REST = 'http://'+HOST+':'+PORT+'/'+BASE+'/rest/1.0/'

values = { 'username' : 'paul.boal', 'password' : '***'}

loggedin = requests.post(REST+'user/login', data=values)
if (loggedin.status_code == 401 ):
    print 'Unable to login ('+loggedin.text+')'
    exit(1)

cookies = loggedin.cookies
search = 'term/find?searchSignifier='+'pecos'
results = requests.get(REST+search, cookies=cookies)

terms = json.loads(results.text)

print "%-64s | %s" % ('TERM', 'URL')
for term in terms.get('simpleTerm'):
    print "%-64s | %s" % (term.get('signifier'), term.get('vocabularyReference').get('uri'))
