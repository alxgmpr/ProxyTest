from worker import Worker

from os import listdir


def main():
    # pls no remove credit
    print '**********'
    print 'Proxy Test'
    print ' by Alex'
    print ' @edzart  '
    print '**********'

    if 'proxies.txt' not in listdir('.'):
        raise Exception('[error] couldnt find proxy file in dir')

    try:
        with open('proxies.txt') as proxy_file:
            proxy_list = proxy_file.read().splitlines()
    except IOError:
        raise Exception('[error] couldnt read proxy file')

    if len(proxy_list) <= 0:
        raise Exception('[error] no proxies in file')

    workers = []
    for i in range(0, len(proxy_list)):
        worker = Worker(i, proxy_list[i])
        workers.append(worker)
        workers[i].start()

if __name__ == '__main__':
    main()
