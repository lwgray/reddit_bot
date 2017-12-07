# coding: utf-8
import os
import csv
import sys


def score():
    results = {'positive': 0, 'negative':0}
    neg = 0
    pos = 0
    with open('data.csv', 'r') as infile:
        reader = csv.reader(infile, delimiter=',')
        for index,line in enumerate(reader):
            if line[-1] == 'negative':
                results['negative'] += float(line[-2])
                neg += 1
            else:
                results['positive'] += float(line[-2])
                pos += 1
    return results pos neg


def main():
    results, pos, neg = score()
    print results, pos, neg
    return


if __name__ == '__main__':
    sys.exit(main())
