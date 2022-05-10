import time
def zähler(num_of_secs):
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end= ',')
        time.sleep(1)
        num_of_secs -= 1
    return