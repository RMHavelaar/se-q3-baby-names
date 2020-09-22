#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

__author__ = "Robert Havelaar"

import sys
import re
import argparse


def extract_names(filename):
    names = list()
    arg = dict()

    with open(filename, 'r') as f:
        output = f.read()
        pattern = re.search(r'Popularity\sin\s(\d\d\d\d)', output)
        if pattern is None:
            return None
        year = pattern.group(1)
        names.append(year)
        name_tuple = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',
                                output)
    for r, m, f in name_tuple:
        if m not in arg:
            arg[m] = r
        if f not in arg:
            arg[f] = r
    for n in sorted(arg):
        names.append(f'{n} {arg[n]}')
    return names


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    create_summary = ns.summaryfile

    for file in file_list:
        if create_summary:
            with open(file + '.summary', 'w') as f:
                f.write('\n'.join(extract_names(file)))
        else:
            print('\n'.join(extract_names(file)))


if __name__ == '__main__':
    main(sys.argv[1:])
