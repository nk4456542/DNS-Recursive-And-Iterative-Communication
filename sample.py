# # import csv

# # fileName = 'map.csv'

# # with open(fileName) as f:
# #     reader = csv.DictReader(f)
# #     for row in reader:
# #         # print(row)
# #         # if row.get('hostname') == 'stackoverflow.com':
# #         hostname = row.get('hostname')
# #         ipaddress = row.get('ipaddress')
# #         if hostname.endswith('com'):
# #             print(str(hostname) + ' ----------> ' + str(ipaddress))
            
# import dns
# import dns.name
# import dns.resolver

# print("enter the domain name")
# user = input()
# default = dns.resolver.get_default_resolver()
# nameserver = default.nameservers[0]
# user = dns.name.from_text(user)
# userInput = user.split(2)
# tld = userInput[1]
# query = dns.message.make_query(tld, dns.rdatatype.NS)
# response = dns.query.udp(query,nameserver)
# print(response)
# answers = dns.resolver.resolve(user,"SOA")
# for rdata in answers:
#     print(rdata)
    
# # print(type(rdata))
# # default = dns.resolver.get_default_resolver()
# # nameserver = default.nameservers[0]
# # print(nameserver)
# print(userInput[0].to_unicode())
# print(u'@')
# last = userInput[0].to_unicode() == u'@'
# print(last)

import socket
import dns
import dns.query
import dns.name
import dns.resolver

default = dns.resolver.get_default_resolver()
nameserver = default.nameservers[0]
userInput = input("Enter the domain: ")
query = dns.message.make_query(userInput,dns.rdatatype.A)
print(query)
response = dns.query.udp(query,nameserver)
print(response)
result = dns.resolver.resolve(userInput)
print(result)
for rdata in result:
    print(rdata)

# import socket
# import ssl
# import requests
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect((userInput, 80))

# cmd = f'GET {userInput} HTTP/1.0\r\n\r\n'.encode()
# requests.get("https://" + str(userInput))

# mysocket.send(cmd)

# while True:
# 	data = mysocket.recv(512)
# 	if(len(data) < 1):
# 		break
# 	print(data.decode(), end=' ')

# mysocket.close()