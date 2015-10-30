#!/bin/bash
iptables -A INPUT -s 43.229.53.67 -j DROP
iptables -A INPUT -s 43.229.53.68 -j DROP
iptables -A INPUT -s 198.23.65.244-st -j DROP
iptables -A INPUT -s 222.186.21.31 -j DROP
iptables -A INPUT -s 222.186.21.208 -j DROP
iptables -A INPUT -s ec2-52-18-232-83 -j DROP
iptables -A INPUT -s 2-226-65-19.ip17 -j DROP
iptables -A INPUT -s 45.35.52.182 -j DROP
iptables -A INPUT -s ip-104-238-95-14 -j DROP
iptables -A INPUT -s static-201-243.i -j DROP
iptables -A INPUT -s 218.236.113.44 -j DROP
iptables -A INPUT -s 149-210-244-213. -j DROP
iptables -A INPUT -s 175.126.123.228 -j DROP
iptables -A INPUT -s 50.118.255.147 -j DROP
iptables -A INPUT -s 202.114.72.243 -j DROP
iptables -A INPUT -s 27.221.10.43 -j DROP
iptables -A INPUT -s 106.243.125.195 -j DROP
iptables -A INPUT -s 112.220.63.83 -j DROP
iptables -A INPUT -s rs000068.fastroo -j DROP
iptables -A INPUT -s 110.45.132.212 -j DROP
iptables -A INPUT -s 218.28.152.162 -j DROP
iptables -A INPUT -s 36.84.248.8 -j DROP
iptables -A INPUT -s 193.107.16.206 -j DROP
iptables -A INPUT -s 202.100.99.7 -j DROP
iptables -A INPUT -s 46.151.53.43 -j DROP
iptables -A INPUT -s ip-45-40-135-180 -j DROP
service iptables save
