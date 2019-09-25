# referenced https://leithsuheimat.wordpress.com/2017/11/22/simple-python-script-to-check-website-response-time/
# referenced https://stackabuse.com/read-a-file-line-by-line-in-python/
import datetime
import requests

with open('ips.txt') as fp:
    url = fp.readline()
    while url:
        try:
            r = requests.get(url, timeout=4)
            r.raise_for_status()
            respTime = str(round(r.elapsed.total_seconds(),4))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            print(url + " " + currDate + " " + respTime + "s " + r.text)
            url = fp.readline()
        except requests.exceptions.HTTPError as err01:
            print("HTTP error: ", err01)
        except requests.exceptions.ConnectionError as err02:
            print("Error connecting: ", err02)
        except requests.exceptions.Timeout as err03:
            print ("Timeout error:", err03)
        except requests.exceptions.RequestException as err04:
            print("Error: ", err04)
