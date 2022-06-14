#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        Buf = bytes()
        while True:
            data = conn.recv(100)
            if not data:
                break
            if len(data) > 0:
                Buf += data
                if Buf[-1] == 10 or Buf[-1] == 13:
                    print('Received', len(Buf), repr(Buf))
                    conn.sendall(Buf)
                    Buf = bytes() 
