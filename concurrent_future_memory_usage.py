import argparse
from concurrent.futures import ThreadPoolExecutor, Future, wait, FIRST_COMPLETED
import gc
import sys
import time

unsafe_submitted = 0

def concurrently(fn, elems, max_workers=None, max_active=None, init_pause=2):
    ''' Naively submit all jobs and provide finished results as a generator'''

    global unsafe_submitted

    submitted = 0
    active = 0

    with ThreadPoolExecutor(max_workers=max_workers) as tpe:
        fs = {}

        time.sleep(init_pause)

        for e in elems:
            if max_active and active >= max_active:
                break

            # just the Future is about 1KB per instance?

            f = Future()
            #f = tpe.submit(fn, e)

            active += 1
            submitted += 1

            unsafe_submitted += 1

            fs[f] = None
            f.set_result(None)

        if submitted == 0:
            raise Exception('0 submitted')

        while fs:
            done, _ = wait(fs, return_when=FIRST_COMPLETED)

            for f in done:
                e = fs.pop(f)
                yield e, f
                active -= 1

            if max_active:
                for e in elems:
                    fs[f] = e

if __name__ == '__main__':
    ap = argparse.ArgumentParser()

    ap.add_argument('-a', '--max-active')
    ap.add_argument('-w', '--max-workers')

    ap.add_argument('-f', '--work-factor', type=int, default=2)
    ap.add_argument('-s', '--work-sleep', type=float, default=0.5)
    ap.add_argument('-j', '--total-jobs', type=int, default=100000)

    pa, _ = ap.parse_known_args()

    stop = False

    unsafe_started = 0
    unsafe_finished = 0
    unsafe_consumed = 0

    with ThreadPoolExecutor(1) as tpe:
        def print_python_memory_usage():
            total_memory = 0

            # TODO use resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            for obj in gc.get_objects():
                try:
                    total_memory += sys.getsizeof(obj)
                except:
                    pass

            print(f'memory:{total_memory / (1024):.2f}KB submitted:{unsafe_submitted} started:{unsafe_started} finished:{unsafe_finished} consumed:{unsafe_consumed}')

        def forever_ppmu():
            while not stop:
                print_python_memory_usage()
                time.sleep(0.5)

            print_python_memory_usage()

        print_python_memory_usage()
        tpe.submit(forever_ppmu)

        def work(i):
            global unsafe_started, unsafe_finished
            unsafe_started += 1
            time.sleep(pa.work_wait)
            e = [ii + i for ii in range(pa.work_factor)]
            unsafe_finished += 1
            return e

        print(pa)

        try:
            itera = range(pa.total_jobs)
            for r, f in concurrently(work, itera, max_workers=pa.max_workers, max_active=pa.max_active):
                unsafe_consumed += 1

            print('stopping...')

        finally:
            stop = True
            tpe.shutdown(True)

