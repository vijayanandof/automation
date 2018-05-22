# -*- coding: utf-8 -*-
"""
Created on Mon May  7 13:41:57 2018

@author: vijayana
"""

import os
import stat
import datetime as dt
from pprint import pprint


def print_files(directory):
    """
    gets a list of files sorted by modified time

    keyword args:
    num_files -- the n number of files you want to print
    directory -- the starting root directory of the search

    """
    modified = []
#    accessed = []
    rootdir = os.path.join(os.getcwd(), directory)

    for root, sub_folders, files in os.walk(rootdir):
        for file in files:
            try:
                unix_modified_time = os.stat(os.path.join(root, file))[stat.ST_MTIME]
                #unix_accessed_time = os.stat(os.path.join(root, file))[stat.ST_ATIME]
                human_modified_time = dt.datetime.fromtimestamp(unix_modified_time).strftime('%Y-%m-%d %H:%M:%S')
                #human_accessed_time = dt.datetime.fromtimestamp(unix_accessed_time).strftime('%Y-%m-%d %H:%M:%S')
                filename = os.path.join(root, file)
                modified.append((human_modified_time, filename))
                #accessed.append((human_accessed_time, filename))
            except:
                pass

    modified.sort(key=lambda a: a[0], reverse=True)
#    accessed.sort(key=lambda a: a[0], reverse=True)
    print('Modified')
    for itm in modified:
        if ".xml" or ".png" in itm[1]:
            print(itm)
#    pprint(modified)
#    print('Accessed')
#    pprint(accessed[:num_files])


def main():
#    parser = argparse.ArgumentParser()
#    parser.add_argument('-n',
#                        '--number',
#                        help='number of items to return',
#                        type=int,
#                        default=1)
#    parser.add_argument('-d',
#                        '--directory',
#                        help='specify a directory to search in',
#                        default='./')
#
#    args = parser.parse_args()

    print_files("C:\Cudo_WORK")

if __name__ == '__main__':
    main()