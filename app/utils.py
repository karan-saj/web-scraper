import time
import random

def retry_request(func, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            return func()
        except Exception as e:
            retries += 1
            time.sleep(random.uniform(1, 3))
            if retries == max_retries:
                raise e
