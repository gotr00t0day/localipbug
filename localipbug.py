import socket
import sys
import threading
import re

domain = sys.argv[1]
port = int(sys.argv[2])

def connect(domain: str, port: int):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((domain, port))
        s.sendall(b"GET / HTTP/1.0\r\n\r\n")
        buffer = s.recv(4096)
        pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        buffer_list = []
        ip = []
        no_dup = []
        buffer_list.append(buffer) 
        for get_ip in buffer_list:
            get_ip = str(get_ip)
            ip.append(pattern.search(get_ip)[0])
        [no_dup.append(x) for x in ip if x not in no_dup]
        print(no_dup)
            
    except socket.error:
        pass
    except socket.gaierror:
        pass
    except TypeError:
        pass


if __name__ == "__main__":
    threads = []
    for _ in range(1, 256):
        thread = threading.Thread(target=connect, args=(domain,port))
        threads.append(thread)
        thread.start()

    # wait for all threads to complete
    for thread in threads:
        thread.join()