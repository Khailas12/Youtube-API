import total_duration as dt
import concurrent.futures
import time

start_time = time.perf_counter()

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(dt.main())


end_time = time.perf_counter()
total_time = end_time - start_time

print(f"\nFetched Result in {total_time} Seconds\n")