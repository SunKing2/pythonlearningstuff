# THESE STARTED WITH KB IN THE EXAMPLE
BYTES_STRINGS = {
    1024: ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1000: ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
}

# THIS IS SUPPOSED TO RETURN A STRING
def show_size(size, kb_1024=True):
    # WHERE IS THE DOCSTRING?
    divisor = 1024 if kb_1024 else 1000
    if (size < 0):
        raise ValueError('Negative value invalid')
    
    i = 1   # TODO REMOVE ME!
    for k in BYTES_STRINGS[divisor]:
        if (size < divisor):
            print('{:.1f}{}'.format(size, k))
            return
        size = size / divisor
        i += 1  #TODO REMOVE ME
    raise ValueError('Too frickin big')

def main():
    isRealKB = True;
    show_size(20, isRealKB)
    show_size(200, isRealKB)
    show_size(999, isRealKB)
    show_size(1000, isRealKB)
    show_size(1001, isRealKB)
    show_size(1023, isRealKB)
    show_size(1024, isRealKB)
    show_size(1025, isRealKB)
    show_size(2000, isRealKB)
    show_size(2047, isRealKB)
    show_size(2048, isRealKB)
    show_size(2049, isRealKB)
    show_size(20000, isRealKB)
    show_size(200000, isRealKB)
    show_size(2000000, isRealKB)  # 2MB
    show_size(20000000, isRealKB)  # 20MB
    show_size(200000000, isRealKB)  # 200MG
    show_size(2000000000, isRealKB)  # 2GB
    show_size(1000000000000, False)
    show_size(1000000000000, True)
    
if __name__ == '__main__':
    main()
