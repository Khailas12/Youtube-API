import user_auth
import time


start_time = time.time()

if __name__ == "__main__": 
    user_auth.auth_user()

    
end_time = time.time()
total_time = end_time - start_time
print(f'\nFetched Playlist info in {total_time} Seconds')