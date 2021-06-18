from library import UDP
from multiprocessing import Process, Pool
import datetime
import time

def main():
    udp = UDP('192.168.0.1', 5005)
    isDone = False
    while not isDone:
        try:
            texec = dict()
            status_task = dict()
            paths = udp.get_file_list()
            task_pool = Pool(processes=20)

            catat_awal = datetime.datetime.now()
            for k in paths:
                print(f"mengirim gambar {paths[k]}")
                waktu = time.time()
                texec[k] = task_pool.apply_async(func=udp.send_file, args=(paths[k],))

            for k in paths:
                status_task[k]=texec[k].get(timeout=10)

            catat_akhir = datetime.datetime.now()
            selesai = catat_akhir - catat_awal
            print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
            print("hasil task yang dijalankan")
            print(status_task)
        finally:
            isDone = True
            print('Done')

if __name__ == '__main__':
    main()