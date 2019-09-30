# referenced https://leithsuheimat.wordpress.com/2017/11/22/simple-python-script-to-check-website-response-time/                                                                                      
# referenced https://stackabuse.com/read-a-file-line-by-line-in-python/                                                                                                                               
import datetime
import requests
import json

with open('working-ips.txt') as fp:
    line = fp.readline()
    while line:
        try:
            url = line.rpartition('@')[2].rstrip()
            r = requests.get(url, timeout=4)
            r.raise_for_status()
            respTime = str(round(r.elapsed.total_seconds(),4))
            if r.headers['content-type'] == "application/json":
                data = json.loads(r.text)
                retNum = str(data["returnNum"])
            else:
                retNum = r.text
            print(line.rstrip() + " " + respTime + " " + retNum)
            line = fp.readline()
        except requests.exceptions.HTTPError as err01:
            print("HTTP error: ", err01)
        except requests.exceptions.ConnectionError as err02:
            print("Error connecting: ", err02)
        except requests.exceptions.Timeout as err03:
            print ("Timeout error:", err03)
        except requests.exceptions.RequestException as err04:
            print("Error: ", err04)



