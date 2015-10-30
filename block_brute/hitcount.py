#!/usr/bin/python -tt

import sys
"""
here is what the lines of the lastb.txt file look like:

administ ssh:notty    27.221.10.43     Fri Oct 30 11:16 - 11:16  (00:00)    
administ ssh:notty    27.221.10.43     Fri Oct 30 11:15 - 11:15  (00:00)    
administ ssh:notty    27.221.10.43     Fri Oct 30 11:15 - 11:15  (00:00)    
user2    ssh:notty    27.221.10.43     Fri Oct 30 11:15 - 11:15  (00:00)    
"""

from operator import itemgetter, attrgetter


def make_dict(filename):
  dict = {}
  counter1 = 0
  file = open(filename, 'rU')
  for line in file:
    counter1 += 1
    # print(line, line.split())
    cols = line.split()
    # print('len(cols) = ', len(cols))
    # print('counter1 = ', counter1)
    if len(cols) > 9:
      if cols[2] in dict:
        dict[cols[2]] = dict[cols[2]] + 1
      else:
        dict[cols[2]] = 1
  file.close()

  counter2 = 0
  iplist = []
  for key in dict.keys():
    counter2 += 1    
    iptuple = dict[key], key
    iplist.append(iptuple)



  """
  generate an iptables command to drop the bastards
  iptables -A INPUT -s 65.55.44.100 -j DROP
  """

  ipfile = open('ipfile.txt', 'w')
  block_iptables_file = open('block_iptables.sh', 'w')
  block_iptables_file.write('#!/bin/bash\n')

  counter3 = 0
  print('len(iplist) = ', len(iplist))
  iplist = sorted(iplist, key=itemgetter(0), reverse=True)
  for iptuple in sorted(iplist, key=itemgetter(0), reverse=True):
    counter3 += 1
    ipstring = str(iptuple[0]) + ', ' + iptuple[1] + '\n'
    if iptuple[0] > 20:
      block_command = 'iptables -A INPUT -s ' + iptuple[1] + ' -j DROP' + '\n'
      block_iptables_file.write(block_command)

    ipfile.write(ipstring)
    # print('iptuple[0] =', iptuple[0], 'iptuple[1] =', iptuple[1])
  
  ipfile.close()

  block_iptables_file.write('service iptables save\n')
  block_iptables_file.close()
  return iplist

"""
the ipfile.txt looks likel this:
# of failed logins, ip address
117444, 43.229.53.67
10583, 43.229.53.68
2872, 198.23.65.244-st
2768, 222.186.21.31
2482, 222.186.21.208
1620, ec2-52-18-232-83
1453, 2-226-65-19.ip17
1091, 45.35.52.182
1000, ip-104-238-95-14
713, static-201-243.i

generate an iptables command to drop the bastards
iptables -A INPUT -s 65.55.44.100 -j DROP


How Do I Unblock An IP Address?

Use the following syntax (the -d options deletes the rule from table):
	# iptables -D INPUT -s xx.xxx.xx.xx -j DROP
	# iptables -D INPUT -s 65.55.44.100 -j DROP
	# service iptables save



"""

make_dict('lastb.txt')


