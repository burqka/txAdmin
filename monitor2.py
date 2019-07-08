import urllib.request
import urllib.parse
import signal
import sys
from time import sleep, gmtime, strftime

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


if len(sys.argv) != 2:
    print('start it as "python3 monitor2.py 30120" or your server port')
    exit()
timeout = 1
port = '32072'
port = sys.argv[1]
print('Starting with port: ' + port)

def writeLog(tstamp, msgType, message):
    msg = tstamp + "\t" + msgType + "\t" + message
    print(msg)
    try:
        with open("data/debug_python.log", "a") as myfile:
            myfile.write(msg + "\n")
    except Exception as e:
        print(tstamp + '\terror saving file')
    finally:
        myfile.close()


def tryRequest():
    url = 'http://localhost:40120'
    tstamp = strftime("%H:%M:%S", gmtime())
    try:
        f = urllib.request.urlopen(url, timeout=timeout)
        # print(f.read().decode('utf-8'))
        print(tstamp + '\tOkay')
    except urllib.error.URLError as e: 
        writeLog(tstamp, 'txadmin', 'timed out')

def tryRequest2():
    url = 'http://localhost:'+port+'/players.json'
    tstamp = strftime("%H:%M:%S", gmtime())
    try:
        f = urllib.request.urlopen(url, timeout=timeout)
        # print(f.read().decode('utf-8'))
        print(tstamp + '\tOkay')
    except urllib.error.URLError as e: 
        writeLog(tstamp, 'players', 'timed out')


tstamp = strftime("%H:%M:%S", gmtime())
writeLog(tstamp, 'LOGSTART', '')

while True:
    tryRequest()
    tryRequest2()
    sleep(1)
