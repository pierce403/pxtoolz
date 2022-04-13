import socket, ssl
import OpenSSL # pip install pyopenssl
import sys

# https://stackoverflow.com/questions/7689941/how-can-i-retrieve-the-tls-ssl-peer-certificate-of-a-remote-host-using-python
# https://www.pyopenssl.org/en/stable/api/crypto.html

if len(sys.argv) != 2:
  print("usage: "+sys.argv[0]+" <list_of_ips.txt> "+str(len(sys.argv)) )
  sys.exit()

ips = open(sys.argv[1], 'r')

for ipline in ips:

  # check range
  if ipline.contains('-'):
    ip_start, ip_stop = ipline.split('-')
    ip_range = iter_iprange(ip_start.strip(),ip_stop.strip())

  # check cidr
  if ipline.contains('/'):
    ip_range = IPNetwork(ipline.strip())

  for ip in ip_range:
    cert = ssl.get_server_certificate((ip.strip(), 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    comps = x509.get_subject().get_components()
    for comp in comps:
      if comp[0].decode() == "CN":
        print(comp[1].decode())
