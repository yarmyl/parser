#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import argparse
import json
import yaml


"""request to url"""
def req(url, data={}, req_method=0):
    if not req_method:
        r = requests.get(url, data=data)
    elif req_method == 1:
        r = requests.post(url, data=data)
    else:
        print("Wrong method!")
    return r.json()


"""Arg Parser"""
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', nargs='?')
    parser.add_argument('--format', nargs='?')
    parser.add_argument('--local', nargs='?')
    return parser


"""Format Config"""
def formatCfg(dict):
    ret = ""
    while dict:
        key, value = dict.popitem()
        ret = ret + str(key) + '=' + str(value) + '\n'
    return ret


"""read yaml file"""
def readYaml(filename):
    stream = open(filename, 'r')
    return yaml.load(stream)


def main():
    parser = createParser()
    namespace = parser.parse_args()
    if namespace.url:
        dict = req(namespace.url)['propertySources'][1]['source']
    if namespace.local:
        dict = readYaml(namespace.local)
    if namespace.format:
        if namespace.format == "json":
            print(json.dumps(dict))
        elif namespace.format == "conf":
            print(formatCfg(dict))
        elif namespace.format == "dict":
            print(dict)
        elif namespace.format == "yaml":
            print(yaml.dump(dict, default_flow_style=False))
        else:
            print("Wrong format!")
    else:
        print(formatCfg(dict))


if __name__ == "__main__":
    main()
