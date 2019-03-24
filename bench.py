#!/usr/bin/env python3

import yaml
import time
import math

FILE = './benchmarks.yml'

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

print(R+"hello how are you"+W)

class BenchWriter:
  lineBreakTmpl = '{:*^80}'
  lineBreakAltTmpl = '{:-^80}'
  spacerTmpl = '{:^80}'
  headerTmpl = '|{:^8}|{:^12}|{:^56}|'
  headers = ['test #', 'runner', 'results']

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

      # We try to print the test name in the middle
      if row == middle:
        runRow = testName
      else:
        runRow = ''
      print(self.headerTmpl.format(runRow, key, value['time']))

      row += 1
      if row == middle:
        spaceRow = testName
      else:
        spaceRow = ''
      print(self.headerTmpl.format(spaceRow, '', ''))
    print(self.lineBreakAltTmpl.format(''))

with open(FILE, 'r') as stream:
  try:
    config = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

testResults = {}
for test in config['tests']:
  testResults[test['name']] = {}
  for run in test['work']:
    start = time.time()
    exec(open(run['source']).read())
    testResults[test['name']][run['name']] = {
      'time': time.time() - start,
      'source': run['source']
    }

# Print results
bench = BenchWriter()
bench.writeHeader()

test = 1
for name, value in testResults.items():
  bench.writeBench(value, '#' + str(test))
  test += 1