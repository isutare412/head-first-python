from threading import Thread
import time


def very_long_routine(*args):
    for arg in args:
        time.sleep(5)
        print('Done processing "{}"'.format(arg))


th = Thread(
    target=very_long_routine,
    args=('Suhyuk', 'Jungwon', 'Sungwon'),
    daemon=True,  # daemonic thread auto-exits when main thread terminates
)

th.start()

while True:
    if not th.is_alive():
        break
    time.sleep(1)
    print('Busy main thread')

print('All done!')
