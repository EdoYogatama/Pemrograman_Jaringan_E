from library import UDP
import datetime
import threading
import time

def main():
    isDone = False
    udp = UDP('192.168.0.1',5005)
    while not isDone:
        try:
            texec = dict()
            paths = udp.get_file_list()

            catat_awal = datetime.datetime.now()
            for k in paths:
                print(f"Sending file {paths[k]}")
                waktu = time.time()
                texec[k] = threading.Thread(target=udp.send_file, args=(paths[k],))
                texec[k].start()

            for k in paths:
                texec[k].join()

            catat_akhir = datetime.datetime.now()
            selesai = catat_akhir - catat_awal
            print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
        finally:
            isDone = True
            print("Done")

if __name__=='__main__':
    main()
