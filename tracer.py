import re
import sys
from subprocess import Popen, PIPE, STDOUT
import requests
from collections import defaultdict


def trace():
    p = Popen('tracert ' + sys.argv[1], stdout=PIPE, stderr=STDOUT, shell=True)
    tmp = 4
    pattern = re.compile('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
    for line in p.stdout:
        if tmp > 0:
            tmp -= 1
            continue
        try:
            line = line.decode()
        except:
            continue
        print(line[0:3], end='\t')
        ips = pattern.findall(line)
        if not ips:
            continue
        ip = ips[-1]
        print(ip, end='\t\t')
        response = requests.get('http://ip-api.com/json/' + ip)
        headers = defaultdict(int, response.json())
        print(headers['as'], end='\t\t')
        print(headers['country'], end='\t\t')
        print(headers['isp'])
