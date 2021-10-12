#!/usr/bin/python3

from scapy.all import *
import sys

conf.verb = 0

portas = [21,22,23,25,80,110,443]

pIP = IP(dst = sys.argv[1])
pTCP = TCP(dport = portas,flags = "S")
pacote = pIP/pTCP
resp, noresp = sr(pacote)
print (resp)


for resposta in resp:
    porta = respota[1][TCP].sport
    flag = respota[1][TCP].flags
    if (flag == "SA"):
        print ("Porta %d ABERTA" %(porta))
