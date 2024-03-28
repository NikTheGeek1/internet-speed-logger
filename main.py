import csv
import time
from datetime import datetime
import speedtest

def get_internet_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    return st.results.download / 1000000, st.results.upload / 1000000

def write_to_csv(download_speed, upload_speed):
    with open('internet_speed.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), download_speed, upload_speed])

def main():
    while True:
        try:
            download_speed, upload_speed = get_internet_speed()
            write_to_csv(download_speed, upload_speed)
            print(f"Download Speed: {download_speed} Mbps")
            print(f"Upload Speed: {upload_speed} Mbps")
            print(f"=====================")
            time.sleep(1800)  # 30 minutes
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
