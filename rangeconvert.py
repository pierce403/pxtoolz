import socket, ssl
import OpenSSL # pip install pyopenssl
import sys

if len(sys.argv) != 2:
  print("usage: "+sys.argv[0]+" <list_of_ips.txt> "+str(len(sys.argv)) )
  sys.exit()

ips = open(sys.argv[1], 'r')

for ipline in ips:

  # check range
  if '-' in ipline:
    ip_start, ip_stop = ipline.split('-')
    ip_range = iter_iprange(ip_start.strip(),ip_stop.strip())

  # check cidr
  if '/' in ipline:
    ip_range = IPNetwork(ipline.strip())

  for ip in ip_range:
    print(ip)
