from library import copy_file, get_file_list
import time
import datetime

def copy_semua():
    urls = get_file_list()

    catat = datetime.datetime.now()
    for k in urls:
        print(f"copying {urls[k]}")
        waktu_proses = copy_file(urls[k], 'CopyDir')
        print(f"completed {waktu_proses} detik")
    selesai = datetime.datetime.now() - catat
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik")

#fungsi download_gambar akan dijalankan secara berurutan

if __name__=='__main__':
    copy_semua()