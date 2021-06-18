from library import UDP
import concurrent.futures
import datetime
import time

def main():
    udp = UDP('192.168.0.1',5005)
    isDone = False
    while not isDone:
        try:
            texec = dict()
            status_task = dict()
            paths = udp.get_file_list()
            task = concurrent.futures.ThreadPoolExecutor(max_workers=3)

            catat_awal = datetime.datetime.now()
            for k in paths:
                print(f"Sending file {paths[k]}")
                waktu = time.time()
                
                #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi broadcast gambar secara multithread
                texec[k] = task.submit(udp.send_file, paths[k])
            
            for k in paths:
                status_task[k]=texec[k].result()

            catat_akhir = datetime.datetime.now()
            selesai = catat_akhir - catat_awal
            print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
            print("hasil task yang dijalankan")
            print(status_task)
        finally:
            isDone = True
            print("Done")

if __name__=='__main__':
    main()