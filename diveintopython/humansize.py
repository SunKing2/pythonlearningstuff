'''
Created on Sep 19, 2017

@author: louie
'''

SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'],
    }

def approximate_size(nbytes, real_1024=True):
    '''Returns string showing approximate bytes converted to KiB, KB, MiB, or MB.

    nbytes(int)      : number of bytes to be converted
    real_1024(bool)  : if units are to be expressed as divisible by 1024.
        if true, shows units as KiB, Mib, GiB, etc.
        if false, shows units as KB, MB, GB, etc
        defaults to true if not specified
    '''
    if nbytes < 0:
        raise ValueError('too small')

    multiplier = 1024 if real_1024 else 1000

    for suffix in SUFFIXES[multiplier]:
        nbytes /= multiplier
        if nbytes < multiplier:
            return '{:.1f} {}'.format(nbytes, suffix)

    raise ValueError('too big')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
    
