from time import sleep


def log_time(func):
    def wrapper():
        import time
        t = time.time()
        t = time.ctime(t)
        func()
        print(f"Function executed at: {t}")
    return wrapper


@log_time
def first():
    print('first')
    sleep(2)


@log_time
def second():
    print('second')


if __name__ == '__main__':
    first()
    second()
