# Uploads data from csv to datawrapper api

import requests
import os
import json
import sys

DW_TOKEN=os.getenv("DW_TOKEN")

if DW_TOKEN is None:
    print("DW_TOKEN env variable is missing")
    sys.exit(1)

CHART_ID="1TwrU"
#print(DW_TOKEN)
#import sys

#sys.exit(0)
# Check
print("-- 01 Check")
URL=f"""https://api.datawrapper.de/v3/charts/{CHART_ID}"""

dw_response = requests.get(URL, headers={
    'Authorization': f"""Bearer {DW_TOKEN}"""
})

#print(dw_response)
#print(dw_response.text)

csv_file = "./nuts-merged-count.csv"

from functools import reduce

data = reduce(lambda a, b: a + b, open(csv_file, 'rb').readlines())


# Upload
print("-- 02 Upload")
URL=f"""https://api.datawrapper.de/v3/charts/{CHART_ID}/data"""

dw_response = requests.put(URL, data, headers={
    'Authorization': f"""Bearer {DW_TOKEN}""",
    'Content-Type': 'text/csv',
    "Accept": "*/*"
})

#print(dw_response)
#print(dw_response.text)

# Update timestamp
print("-- 03 Update timestamp")
url = f"""https://api.datawrapper.de/v3/charts/{CHART_ID}"""


headers = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    'Authorization': f"""Bearer {DW_TOKEN}"""
}

from datetime import datetime
actual_time = datetime.now().strftime("%H:%M:%S %d.%m.%Y")
payload = {"metadata": {"language": "de-DE", "annotate": {"notes": f"""Zuletzt aktualisiert: {actual_time}"""}}}
response = requests.request("PATCH", url, json=payload, headers=headers)

#print(response)
#print(response.text)

# publish
print("-- 04 Publish chart")
URL=f"""https://api.datawrapper.de/v3/charts/{CHART_ID}/publish"""

headers = {
    "Accept": "*/*",
    'Authorization': f"""Bearer {DW_TOKEN}"""
}
response = requests.request("POST", URL, headers=headers)
###print(response)
#print(response.text)

print(json.loads(response.text)['url'])
print("Published")
