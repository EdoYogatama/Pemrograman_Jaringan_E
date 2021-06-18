import logging
import time
import datetime
import socket

class UDP:
    def __init__(self, target_ip, target_port):
        self.TARGET_IP = target_ip
        self.TARGET_PORT = target_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

    def get_file_list(self):
        paths = dict()
        paths['file1']='Data/file1.txt'
        paths['file2']='Data/file2.txt'
        paths['file3']='Data/file3.txt'
        paths['file4']='Data/file4.txt'
        paths['file5']='Data/file5.txt'

        return paths

    def send_file(self, path=None):
        waktu_awal = datetime.datetime.now()
        if (path is None):
            return False

        f = open(path,"rb")
        sendfile = f.read(1024)
        while (sendfile):
            if(self.socket.sendto(sendfile, (self.TARGET_IP, self.TARGET_PORT))):
                # print(f"sending...")
                sendfile = f.read(1024)
        f.close()
        time.sleep(2) #untuk simulasi, diberi tambahan delay 2 detik

        waktu_process = datetime.datetime.now() - waktu_awal
        waktu_akhir =datetime.datetime.now()
        logging.warning(f"writing {path} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")
        return waktu_process

if __name__=='__main__':
    udp = UDP('127.0.0.1', 5005)
    print(udp.send_file('Data/file1.txt'))