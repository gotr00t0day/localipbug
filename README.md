# localipbug
In some cases the Miscorosoft HTTP Server API leaks internal ip addresses while sending a GET / HTTP/1.0 request to the server. This bug exposes the IP addresses that are usually hidden and protected by a WAF.

Tested on Microsoft HTTPAPI httpd 2.0.


# USAGE

python3 localipbug.py HOST PORT
