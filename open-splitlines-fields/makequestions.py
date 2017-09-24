'''
Created on Sep 20, 2017

@author: louie
'''


def do_it():
    with open('twolines.qz', 'r') as fin:
        lines_list = fin.read().splitlines()

    questions = {}
    for line in lines_list:
        fields_lis = line.split('\t')
        print('alphagram=' + fields_lis[0])


if __name__ == '__main__':
    do_it()
