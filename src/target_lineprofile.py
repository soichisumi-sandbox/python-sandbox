# pprofile --include target_lineprofile.py target_lineprofile.py

import time
from concurrent.futures import ThreadPoolExecutor

# avoding not defined error of decorator for profiling
try:
    profile
except NameError:
    import builtins
    import line_profiler
    builtins.__dict__['profile'] = line_profiler.LineProfiler()


@profile
def longtask():
    print("  start longtask")
    for i in range(10):
        time.sleep(100 / 1000)
    print("  longtask done")


@profile
def shorttask():
    print("  start short task")
    time.sleep(10 / 1000)
    print("  short task done")


def run():
    tasks = [longtask]
    for i in range(1000):
        tasks.append(shorttask)
    # runInParallel(*tasks)

    # default worker count:
    # Python 3.7 or below ... os.cpu_count() x 5
    # Python 3.8 or above ... min(32, os.cpu_count() + 4)
    with ThreadPoolExecutor() as executor:
        res = []
        for t in tasks:
            f = executor.submit(t)
            res.append(f)

    # retrieve results


if __name__ == '__main__':
    print("start tasks")
    run()
    print("all tasks done")
