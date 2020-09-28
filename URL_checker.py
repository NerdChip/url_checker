#python site checker 
#author: Gamu Manungo

#imported libraries
import subprocess
import re
import sys
import time 
import socket
import requests
import argparse


#Function to check if port 443 is open using the sockets module
def CheckPort443(public_ip):
	port = 443

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.settimeout(4)

		try:
			res = s.connect((public_ip, port))
			s.sendall(b"Hello World")
			data = s.recv(1024)

			print(" ")
			if res != 0:
				print(f'[*]Port 443 Is Open On: {public_ip}')

			s.close()
		except socket.timeout:
			print(f"[*]Timeout Reached, could not established connection to {public_ip} on port 443")

#Function to check if port 80 is open using the sockets module
def CheckPort80(public_ip):
	port = 80

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.settimeout(4)

		try:
			res = s.connect((public_ip, port))
			s.sendall(b"Hello World")
			data = s.recv(1024)

			print(" ")
			if res != 0:
				print(f'[*]Port 80 Is Open On: {public_ip}')

			s.close()
		except socket.timeout:
			print(f"[*]Timeout Reached, could not established connection to {public_ip} on port 80")

#Function used to check if url is active, looking for a status 200 response  
def httpcheck(dn):
	url_checker = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

	user_choice = "http://www." + dn


	check = bool(url_checker.match(user_choice))
	
	if check == True:
		pass
	else:
		print("YOU HAVE ENTERED A VAILD DOAMIN PLEASE CHECK AND TRY AGAIN")
		sys.exit()

	res = requests.get(user_choice).status_code

	if res == 200:
		print("This Domain/URL is Active received a status 200")
	else:
		print("""Could not sucessfully reach the Domain/url please see summary of web server status code error



			3XX =  Redirection codes returned when a new resource has been substituted for the requested resource.
			4XX = Client error codes indicating that there was a problem with the request
			5XX =  Server error codes indicating that the request was accepted, but that an error on the server prevented the fulfillment of the request.


			""")

#main function argparser object defined, this is where the function calls are made based on the postitional and optional argument. 
def main():
	parser = argparse.ArgumentParser(prog='URL Checker', description='URL checker used to check if a url can be reached and additionally if the port is open')

	parser.add_argument('URL' ,help='input a url or domain name that you want checked')
	parser.add_argument('-p','--port' , help='port - use this conduct a name server lookup the domian and check if the port is open',action="store_true")
	args = parser.parse_args()


	try:
		httpcheck(args.URL)
	except:
		print(f"OOPS I SEEM TO HAVE ENCOUNTRED AN ERROR PLEASE CHECK INPUT IS CORRECT: {args.URL}")


	if args.port:
		windows_domain_lookup = "nslookup " + args.URL 

		p1 = subprocess.run(windows_domain_lookup, shell=True, capture_output=True, text=True)

		ip_addresses_checker = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}')

		ip_check = ip_addresses_checker.findall(p1.stdout)

		ip_check.pop(0) 

		print(f'Found {len(ip_check)} IP addresses associated with {args.URL}:: The Following Domain Has Been Mapped to These Web Severs IP\'s: ')
		for number in ip_check:
			print(number)


		for ip in ip_check:
			CheckPort443(ip)
			time.sleep(2)
			CheckPort80(ip)
			time.sleep(5)

			
if __name__ == '__main__':
	main()