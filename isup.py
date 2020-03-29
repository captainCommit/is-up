import os
import argparse
import math
import time
import requests
import subprocess

status = {}
def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return
def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return True

def read_from_txt(path):
    f = open(path)
    links = [x.strip() for x in f.readlines()]
    return links

def check_up(url):
    try:
        t = requests.get(url)
        if t.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def get_load_time(url):
    try:
        t = requests.get(url).elapsed
        mu = t.microseconds/10**6
        #print("Load Time : {0:.2f} seconds".format(mu))
        return "{0:.2f}".format(mu)
    except:
        return None
      
def ui():
    print()
    links = []
    n = 1
    parser = argparse.ArgumentParser()
    parser.add_argument("--f",required=True,type = str)
    args = parser.parse_args()
    f = args.f
    if "http://" not in f and "https://" not in f:
        f = "http://"+f
    st = check_up(f)
    if st:
        sta= "up"
    else:
        sta= "down"
    sendmessage('{l} is {st}'.format(l = f.replace('http://','').replace('https://',''),st = sta))
    status[f] = st
    load = get_load_time(f)
    if load == None:
        load = "infinite"
    print('Webiste : {l} || Status : {st} || Load Time : {load} seconds'.format(l = f.replace('http://','').replace('https://',''),st = sta,load=load))
ui()