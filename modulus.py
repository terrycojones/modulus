#!/usr/bin/env python

from __future__ import print_function, division

import argparse
from math import log10


def mods(base, places=None):
    """
    Generate 10^x mod C{base} for increasing values of x.

    @param n: An C{int} base for the modulus operation.
    @param places: The C{int} number of places (1, 10, 100, etc.) to generate
        the modulus for. If C{None} there is no limit.
    @return: A generator yielding 10^x mod C{base} for increasing values of x.
    """
    place = 0
    x = 1
    while places is None or place < places:
        place += 1
        if base > x:
            yield x
        else:
            yield x % base
        x *= 10


def remainder(n, base):
    """
    Calculate C{n} mod C{base} using the 10^x remainders.

    @param n: The C{str} of an C{int}.
    @param base: The C{int} base for the modulo operation.
    """
    return sum(int(digit) * mod
               for digit, mod in zip(n[::-1], mods(base, len(n))))


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description=(
        'Either print a list of remainders for 10^X mod BASE, for '
        'increasing values of X and BASE. Or compute a specific '
        'modulus using the remainders for a given base.'))

group = parser.add_argument_group(
    'list', 'print a list of remainders for a list of bases')

group.add_argument(
    '--from', type=int, default=2, dest='_from', metavar='N',
    help='The first base to display if producing an output list.')

group.add_argument(
    '--to', type=int, default=100, metavar='N',
    help='The final base to display if producing an output list.')

group.add_argument(
    '--places', type=int, default=20, metavar='N',
    help=('The number of places to show remainders for if producing an '
          'output list.'))

group.add_argument(
    '--negatives', action='store_true', default=False,
    help=('If specified, print negative multipliers when the multiplier for '
          'a place is greater than half the base.'))

group = parser.add_argument_group(
    'remainder', 'compute a specific remainder')

group.add_argument(
    '--n', type=int, metavar='N',
    help='The number whose remainder should be computed.')

group.add_argument(
    '--base', type=int, metavar='N',
    help='The int base of the remainder to compute.')

group.add_argument(
    '--verbose', action='store_true', default=False,
    help='If specified, show intermediat information.')

args = parser.parse_args()


if args.n is not None and args.base is not None:
    # Calculate a specific remainder.
    n = args.n
    base = args.base

    if args.verbose:
        modList = list(map(str, mods(base, len(str(n)))))
        print('mods for base %d: %s' % (base, ', '.join(modList[::-1])))

    if base > n:
        print(n)
    else:
        last = -1

        while True:
            rem = remainder(str(n), base)
            if rem == last:
                break
            else:
                if args.verbose:
                    print('intermediate', rem)
                n = rem
                last = rem
        result = rem % base
        assert result == (args.n % args.base)
        print(result)
else:
    # Produce a list of remainders for a list of bases.
    assert args._from <= args.to, '--from must be <= --to'
    width = int(log10(args.to)) + 1 + args.negatives
    places = args.places

    # Print header line.
    print('%*s  ' % (width, ''), end='')
    for place in range(places, 0, -1):
        print('%*d  ' % (width, place - 1), end='')
    print()

    negatives = args.negatives
    for base in range(args._from, args.to + 1):
        if negatives:
            half = int(base / 2.0)
        print('%*d: ' % (width, base), end='')
        remainders = list(mods(base, places))
        for place, x in enumerate(remainders[::-1], start=1):
            if x:
                if negatives and x > half:
                    x = -(base - x)
                print('%*d%s' %
                      (width, x, '' if place == places else ', '), end='')
            else:
                print('%*s%s' %
                      (width, '', '' if place == places else '  '), end='')
        print()
