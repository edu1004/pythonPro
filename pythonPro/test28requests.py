#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#comment 한글
import requests

print("requests")
req = requests.get("http://192.168.0.106")

print(req.status_code)
print(req.headers)
print(req.content)





