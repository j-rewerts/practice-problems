#!/usr/bin/env python3

import yaml

FILE = './benchmarks.yml'

with open(FILE, 'r') as stream:
  try:
    config = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

for test in config['tests']:
  print(test['name'])
  for run in test['work']:
    print('Running ' + run['name'])
    exec(open(run['source']).read())
