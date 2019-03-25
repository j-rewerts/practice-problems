#!/usr/bin/env python3

import yaml
import time
import math
import importlib
from string import Formatter

FILE = './benchmarks.yml'

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

print(R+"hello how are you"+W)

# This string formatter allows you to define a default dictionary to look
# for values in. These can be overridden by using the kwargs from the regular
# string formatter.
# @param defaults A dict of default kwargs to use.
class DefaultFormatter(Formatter):
  def __init__(self, defaults={}):
    Formatter.__init__(self)
    self.defaults = defaults
  
  def get_value(self, key, args, kwds):
    if isinstance(key, str):
      try:
        return kwds[key]
      except KeyError:
        return self.defaults[key]
    else:
      fmt = Formatter()
      return fmt.get_value(key, args, kwds)

# Helps with writing well formatted test runs.
class BenchWriter:
  LINE_LENGTH = 80
  lineBreakTmpl = '{:*^{length!s}}'
  lineBreakAltTmpl = '{:-^{length!s}}'
  spacerTmpl = '{:^{length!s}}'
  headerTmpl = '|{:^{testLength}}|{:^{runnerLength}}|{:^{detailsLength}}|'
  headers = ['test #', 'runner', 'results']
  fmt = DefaultFormatter({
    'length': 80,
    'testLength': 8,
    'runnerLength': 12,
    'detailsLength': 56
  })

  # Writes out a header
  def writeHeader(self):
    print(self.fmt.format(self.lineBreakTmpl, ''))
    print(self.fmt.format(self.headerTmpl, P+'TEST #'+W, P+'RUNNER'+W, P+'RESULTS'+W, 
      testLength=17, runnerLength=21, detailsLength=65))
    print(self.fmt.format(self.lineBreakTmpl, ''))

  # Writes out a benchmark in the form:
  # |        |            |                                                        |
  # |        |   Jared    |                     170.645ms                          |
  # |   #1   |            |                                                        |
  # |        |   Cody     |       7000000000ms    (this took FOREVER to run)       |
  # |        |            |                                                        |
  # --------------------------------------------------------------------------------
  def writeBench(self, obj, testName):
    numRunners = len(obj.items())
    numLines = 2 * numRunners + 1
    middle = math.floor(numLines/2)+1

    print(self.fmt.format(self.headerTmpl, '', '', ''))
    row = 1
    for key, value in obj.items():
      row += 1

      # We try to print the test name in the middle.
      if row == middle:
        runRow = testName
      else:
        runRow = ''
      print(self.fmt.format(self.headerTmpl, runRow, key, value['time']))
      # Again, we're trying to identify when to write the test name.
      row += 1
      if row == middle:
        spaceRow = testName
      else:
        spaceRow = ''
      print(self.fmt.format(self.headerTmpl, spaceRow, '', ''))
    print(self.fmt.format(self.lineBreakAltTmpl, ''))

# Parses a YAML file into a Bench config object.
def getConfig(file):
  with open(file, 'r') as stream:
    try:
      config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)
  return config

# Runs the tests defined in config.
def runBench(config):
  results = {}
  for test in config['tests']:
    results[test['name']] = {}
    for run in test['work']:
      start = time.time()
      exec(open(run['source']).read(), globals())
      results[test['name']][run['name']] = {
        'time': str((time.time() - start) * 1000) + ' ms',
        'source': run['source']
      }
  return results

# Prints the output of the runs.
def printBench(results):
  bench = BenchWriter()
  bench.writeHeader()

  test = 1
  for _, value in results.items():
    bench.writeBench(value, '#' + str(test))
    test += 1

config = getConfig(FILE)
results = runBench(config)
printBench(results)