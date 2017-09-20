'''
Created on Sep 19, 2017

@author: louie
'''

import humansize

if __name__ == '__main__':
    print(humansize.approximate_size(1000000000000, False))
    print(humansize.approximate_size(1000000000000))