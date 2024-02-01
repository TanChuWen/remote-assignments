# Today, we want to finish some jobs in multi-thread and you can see the sample code below.
# The main function executes the do_job function 5 times and in each time it takes 3 seconds
# to finish the job. So it will take 15 seconds to finish all the jobs and that is very inefficient. We
# want to finish all the jobs in around 3 seconds in total, try to rewrite the main function to
# achieve the goal and keep other functions untouched.

import threading
from time import sleep

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")

# rewrite everything inside this main function and keep others untouched
def main():
    threads =[] # build a list to store thread

    # execute the thread
    for i in range(5):
        thread = threading.Thread(target=do_job, args=(i,))
        threads.append(thread) #put the execution into threads[]
        thread.start() #start
    
    # wait for the thread to end
    for thread in threads:
        thread.join()

main()