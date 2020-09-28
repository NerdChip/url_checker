# url_checker
This is a tool the will identify if a url is active or not, additionally you can check web server IP using DNS(DNS server used on the network you are connected to) and check if the server accepts connections made on port 80(http) or port 443(https))
This only Works for Windows OS only

```
usage: URL Checker [-h] [-p] URL

URL checker used to check if a url can be reached and additionally if the port
is open

positional arguments:
  URL         input a url or domain name that you want checked

optional arguments:
  -h, --help  show this help message and exit
  -p, --port  port - use this conduct a name server lookup the domian and
              check if the port is open
              
```

using the program with the required positional argument which can be a URL or domain name\n

`python URL_checker.py google.com`

# output 

`This Domain/URL is Active received a status 200`


Can check if the web server(s) are listening on port 80 or 443

`python URL_checker.py google.com -p`

# ouput 
```
This Domain/URL is Active received a status 200
Found 1 IP addresses associated with google.com:: The Following Domain Has Been Mapped to These Web Severs IP's:
216.58.213.110

[*]Port 443 Is Open On: 216.58.213.110
[*]Timeout Reached, could not established connection to 216.58.213.110 on port 80
``` 
  
