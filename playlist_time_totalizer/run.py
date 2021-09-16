import total_duration as dt
import time


start_time = time.time()

if __name__ == "__main__":
    dt.main()

end_time = time.time()
total_time = end_time - start_time
print(f"\nFetched Result in {total_time} Seconds\n")