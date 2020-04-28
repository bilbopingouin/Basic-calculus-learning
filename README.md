# Basic-calculus-learning

This helps to generate simple calculus exercises for a kid, learning to sum

## Objective

A kid learning to count and to calculate needs to do many operations or the type: "4+5=?". It requires some effort to write them oneself. And tends not to be very random. This program offers an alternative.

## Installation

Simply requires a running `python3` installation.

## Run

Run using the default as

``` bash
python3 generate.py
```

See the details as

``` bash
python3 generate.py --help
```

## Examples

```bash
$ python3 generate.py
  4 +   1 =   5
  5 +   5 =  10
  4 +   4 =   8
  3 +   5 =   8
  3 +   1 =   4

$ python3 generate.py --min 1 --max 5 --operation sub
  5 -   3 =   2
  3 -   2 =   1
  5 -   2 =   3
  2 -   1 =   1
  2 -   1 =   1

$ python3 generate.py --help

usage: generate.py [-h] [-n NUMBER] [-p OPERATION] [-m MIN] [-M MAX]
                   [-u UNKNOWN]

Generate simple operations

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Number of operations [default: 5]
  -p OPERATION, --operation OPERATION
                        Operation to be done. [default: add; available: add
                        sub div times max]
  -m MIN, --min MIN     Minimum value for the operations [default: 0]
  -M MAX, --max MAX     Maximum value for the operations [default: 10]
  -u UNKNOWN, --unknown UNKNOWN
                        Missing value for the operation a+b=c [default: 0;
                        available: 0 (None missing), a, b, c]

$ python3 generate.py --min 1 --max 10 --number 9 -u b
  2 + ___ =  10
  3 + ___ =   9
  5 + ___ =  10
  9 + ___ =  10
  6 + ___ =   8
  1 + ___ =   3
  1 + ___ =  10
  3 + ___ =   7
  1 + ___ =   4
1 2 2 3 4 5 6 8 9
```
