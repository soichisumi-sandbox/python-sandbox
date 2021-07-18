import time
from multiprocessing import Process


def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()


def longtask():
    print("start longtask")
    for i in range(10):
        time.sleep(100/1000)
    print("longtask done")

def shorttask():
    print("start short task")
    time.sleep(10/1000)
    print("short task done")

def run():
    tasks = []
    tasks.append(longtask)
    for i in range(20):
        tasks.append(shorttask)
    runInParallel(*tasks)


if __name__ == '__main__':
    print("start tasks")
    run()
    print("all tasks done")
