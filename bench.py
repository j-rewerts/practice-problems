#!/usr/bin/env python3

import yaml
import time

FILE = './benchmarks.yml'

with open(FILE, 'r') as stream:
  try:
    config = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

for test in config['tests']:
  print(test['name'])
  for run in test['work']:
    start = time.time()
    print('Running ' + run['name'])
    exec(open(run['source']).read())
    print("--- %s seconds ---" % (time.time() - start))

