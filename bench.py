#!/usr/bin/env python3

import yaml
import time
import math
import importlib

FILE = './benchmarks.yml'

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

print(R+"hello how are you"+W)

# Helps with writing well formatted test runs.
class BenchWriter:
  lineBreakTmpl = '{:*^80}'
  lineBreakAltTmpl = '{:-^80}'
  spacerTmpl = '{:^80}'
  headerTmpl = '|{:^8}|{:^12}|{:^56}|'
  headers = ['test #', 'runner', 'results']

  # Writes out a header
  def writeHeader(self):
    print(self.lineBreakTmpl.format(''))
    print(self.headerTmpl.format('TEST #', 'RUNNER', 'RESULTS'))
    print(self.lineBreakTmpl.format(''))

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

    print(self.headerTmpl.format('', '', ''))
    row = 1
    for key, value in obj.items():
      row += 1

      # We try to print the test name in the middle.
      if row == middle:
        runRow = testName
      else:
        runRow = ''
      print(self.headerTmpl.format(runRow, key, value['time']))
      # Again, we're trying to identify when to write the test name.
      row += 1
      if row == middle:
        spaceRow = testName
      else:
        spaceRow = ''
      print(self.headerTmpl.format(spaceRow, '', ''))
    print(self.lineBreakAltTmpl.format(''))

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
        'time': time.time() - start,
        'source': run['source']
      }
  return results

# Prints the output of the runs.
def printBench(results):
  bench = BenchWriter()
  bench.writeHeader()

  test = 1
  for name, value in results.items():
    bench.writeBench(value, '#' + str(test))
    test += 1

config = getConfig(FILE)
results = runBench(config)
printBench(results)