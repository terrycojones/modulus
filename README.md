The short script in this repo (`modulus.py`) can do two things:

1. Print a table of 10^`x` modulo `base` for increasing values of `x` and
   `base`.
1. Print a specific value of `n` module `base`, calculated by using values
   from the just-mentioned table.

## Printing a table

```sh
$ modulus.py --negatives --places 15 --to 40
  2:                                                                         1,
  3:   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
  4:                                                                    2,   1,
  5:                                                                         1,
  6:  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,   1,
  7:   2,   3,   1,  -2,  -3,  -1,   2,   3,   1,  -2,  -3,  -1,   2,   3,   1,
  8:                                                               4,   2,   1,
  9:   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
 10:                                                                         1,
 11:   1,  -1,   1,  -1,   1,  -1,   1,  -1,   1,  -1,   1,  -1,   1,  -1,   1,
 12:   4,   4,   4,   4,   4,   4,   4,   4,   4,   4,   4,   4,   4,  -2,   1,
 13:  -4,  -3,   1,   4,   3,  -1,  -4,  -3,   1,   4,   3,  -1,  -4,  -3,   1,
 14:   2,  -4,  -6,  -2,   4,   6,   2,  -4,  -6,  -2,   4,   6,   2,  -4,   1,
 15:  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,   1,
 16:                                                          8,   4,  -6,   1,
 17:   8,  -6,  -4,   3,   2,   7,  -1,   5,  -8,   6,   4,  -3,  -2,  -7,   1,
 18:  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,   1,
 19:  -3,  -6,   7,  -5,   9,  -1,  -2,  -4,  -8,   3,   6,  -7,   5,  -9,   1,
 20:                                                                   10,   1,
 21:  -5,  10,   1,  -2,   4,  -8,  -5,  10,   1,  -2,   4,  -8,  -5,  10,   1,
 22: -10,  10, -10,  10, -10,  10, -10,  10, -10,  10, -10,  10, -10,  10,   1,
 23: -11,  -8, -10,  -1,  -7,  -3,   2,  -9,   6,  -4,  -5,  11,   8,  10,   1,
 24:  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,   4,  10,   1,
 25:                                                                   10,   1,
 26:  -4,  10, -12,   4, -10,  12,  -4,  10, -12,   4, -10,  12,  -4,  10,   1,
 27:  -8,  10,   1,  -8,  10,   1,  -8,  10,   1,  -8,  10,   1,  -8,  10,   1,
 28: -12,  -4,   8,  12,   4,  -8, -12,  -4,   8,  12,   4,  -8, -12,  10,   1,
 29:  -1,  -3,  -9,   2,   6, -11,  -4, -12,  -7,   8,  -5,  14,  13,  10,   1,
 30:  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,   1,
 31:  -3,   9,   4, -12,   5, -15,  14, -11,   2,  -6, -13,   8,   7,  10,   1,
 32:                                                    16,   8,   4,  10,   1,
 33:   1,  10,   1,  10,   1,  10,   1,  10,   1,  10,   1,  10,   1,  10,   1,
 34:   8,  -6,  -4, -14,   2, -10,  16, -12,  -8,   6,   4,  14,  -2,  10,   1,
 35:  -5,  10,  15,   5, -10, -15,  -5,  10,  15,   5, -10, -15,  -5,  10,   1,
 36:  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  10,   1,
 37: -11,  10,   1, -11,  10,   1, -11,  10,   1, -11,  10,   1, -11,  10,   1,
 38:  16,  -6, -12,  14, -10,  18,  -2,  -4,  -8, -16,   6,  12, -14,  10,   1,
 39: -17,  10,   1,   4,  16, -14, -17,  10,   1,   4,  16, -14, -17,  10,   1,
 40:                                                              20,  10,   1,
```

## Printing a specific value

This just calculates a regular modulus, but does so using values from the
above table.

```sh
$ modulus.py --n 1003 --base 13
2
```

## Usage options

Run with `--help` to see all options:

```sh
$ modulus.py --help
usage: modulus.py [-h] [--n N] [--base N] [--verbose] [--from N] [--to N]
                  [--places N] [--negatives]

Either print a list of remainders for 10^X mod BASE, for increasing values of
X and BASE. Or compute a specific modulus using the remainders for a given
base.

optional arguments:
  -h, --help   show this help message and exit

remainder:
  compute a specific remainder

  --n N        The number whose remainder should be computed. (default: None)
  --base N     The int base of the remainder to compute. (default: None)
  --verbose    If specified, show intermediat information. (default: False)

list:
  print a list of remainders for a list of bases

  --from N     The first base to display if producing an output list.
               (default: 2)
  --to N       The final base to display if producing an output list.
               (default: 100)
  --places N   The number of places to show remainders for if producing an
               output list. (default: 20)
  --negatives  If specified, print negative multipliers when the multiplier
               for a place is greater than half the base. (default: False)
```
