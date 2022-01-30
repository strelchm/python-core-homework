from timeit import default_timer
from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    def wrapper(func):
        def ret_fun(*args, **kwargs):
            time_stat_list = []
            for _ in range(num):
                start_time = default_timer()
                func(*args, **kwargs)
                end_time = default_timer()
                print(end_time - start_time)
                time_stat_list.append(end_time - start_time)
            print(sum(time_stat_list) / num)
        return ret_fun
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
