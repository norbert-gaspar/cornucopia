#!/usr/bin/env python3

import argparse
import json
import logging
import os
import sys
import yaml
import fnmatch
from typing import List, TextIO


def main() -> None:
    logging.basicConfig(
        format="%(asctime)s %(filename)s | %(levelname)s | %(funcName)s | %(message)s",
        level=logging.INFO,
    )
    args = parse_arguments(sys.argv[1:])
    
    yaml_files = []
    for root, dirnames, filenames in os.walk('../source'):
        if args.debug:
            print("--- root = " + str(root))
            for name in filenames:
                print("--- files = " + str(os.path.join(root,name)))
        for filename in fnmatch.filter(filenames, '*.yaml'):
            yaml_files.append(os.path.join(root, filename))
    if args.debug: print("--- yaml_files = " + str(yaml_files))
    
    if args.output != None and len(yaml_files) > 0:
        for file in yaml_files:
            yaml.load(file)
            if args.debug: print('--- file = ' + str(file))


def parse_arguments(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Tool to convert.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-o",
        "--output",
        type=str,
        choices=["json", "pdf", "indd"],
        default=None,
        help="Output format to produce.",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Output additional information to debug script",
        )
    return parser.parse_args(args)


if __name__ == "__main__":
    main()
