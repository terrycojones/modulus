The short script in this repo (`modulus.py`) can do two things:

1. Print a table of 10^`x` modulo `base` for increasing values of `x` and
   `base`.
1. Print a specific value of `n` module `base`, calculated by using values
   from the just-mentioned table.

## Printing a table

Here's a tiny example:

```sh
$ modulus.py --places 6 --to 11
     5   4   3   2   1   0
 2:                      1
 3:  1,  1,  1,  1,  1,  1
 4:                  2,  1
 5:                      1
 6:  4,  4,  4,  4,  4,  1
 7:  5,  4,  6,  2,  3,  1
 8:              4,  2,  1
 9:  1,  1,  1,  1,  1,  1
10:                      1
11: 10,  1, 10,  1, 10,  1
```

The first line of output shows column headers for values of `x` (in the
`10^x` above). So the rightmost column is the ones, the second to the right
is the tens, etc.

Subsequent lines start with a `base`, then a colon, then show the value of
`10^x mod base` (if not zero). E.g., with `x=3` and `base=7`, you can see
`10^3 mod 7 = 6`.

If you pass `--negatives`, values that are greater than half the modulo
base will be shown as a smaller (but negative) number that's equivalent
under modulo.  Here's the same table as above, but with the large values
replaced in that way:


```sh
$ modulus.py --places 6 --to 11 --negatives
       5    4    3    2    1    0
  2:                            1
  3:   1,   1,   1,   1,   1,   1
  4:                       2,   1
  5:                            1
  6:  -2,  -2,  -2,  -2,  -2,   1
  7:  -2,  -3,  -1,   2,   3,   1
  8:                  4,   2,   1
  9:   1,   1,   1,   1,   1,   1
 10:                            1
 11:  -1,   1,  -1,   1,  -1,   1
```

## OK, already, what's the point?

I wrote this so I could look at the patterns of remainders to think about
tricks for rapid calculation of divisibility.

When I was a kid we were told rules for divisibility. Some were very
simple. E.g.,

* If the final digit of a number is 0, the number is divisible by 10.
* If the final digit of a number is 0 or 5, the number is divisible by 5.
* If the final digit of a number is even, the number is divisible by 2.

and some were a little more involved:

* If all the digits of a number add to something divisible by 3, then the
  number is also divisible by 3.
* If the two outside digits of a 3-digit number sum to the middle digit,
  then the number is divisible by 11.

When I was a teen I came across a more general rule for 11:

* Alternately add and subtract the digits in the number. If the result is
  divisible by 11, then the number is also divisible by 11.

At some point I worked out (i.e., proved) why the rules for 3 and 11 work.

The other day I saw a tweet from [Josh Reich](https://twitter.com/i2pi)
giving an example of the rule of 3:

<blockquote class="twitter-tweet" data-lang="en"><p> 345 is divisible
by 3. 3+4+5=12, 12/3=4. 345 = 3*100 + 4*10 + 5 = 3*(99+1) + 4*(9+1) +
5*(0+1) = (3*99 + 4*9 + 5*0) + (3+4+5). The first part is divisible by
three (9, 99, 999, etc). The number will be divisible by three if its sum
of digits are. Happy 3pm!</p>&mdash; Josh Reich (@i2pi) <a
href="https://twitter.com/i2pi/status/976579575030231040">March 21,
2018</a></blockquote>

Later I decided to write a quick bit of code to print out a table of
remainders for different powers of ten and different bases to see if there
were any other nice patterns.

Here's a larger chunk of output:

```sh
$ modulus.py --negatives --places 15 --to 40
      14   13   12   11   10    9    8    7    6    5    4    3    2    1    0
  2:                                                                         1
  3:   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1
  4:                                                                    2,   1
  5:                                                                         1
  6:  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,   1
  7:   2,   3,   1,  -2,  -3,  -1,   2,   3,   1,  -2,  -3,  -1,   2,   3,   1
  8:                                                               4,   2,   1
  9:   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1
 10:                                                                         1
 11:   1,  -1,   1,  -1,   1,  -1,   1,  -1,   1,  -1,   1,  -1,   1,  -1,   1
 12:   4,   4,   4,   4,   4,   4,   4,   4,   4,   4,   4,   4,   4,  -2,   1
 13:  -4,  -3,   1,   4,   3,  -1,  -4,  -3,   1,   4,   3,  -1,  -4,  -3,   1
 14:   2,  -4,  -6,  -2,   4,   6,   2,  -4,  -6,  -2,   4,   6,   2,  -4,   1
 15:  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,  -5,   1
 16:                                                          8,   4,  -6,   1
 17:   8,  -6,  -4,   3,   2,   7,  -1,   5,  -8,   6,   4,  -3,  -2,  -7,   1
 18:  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,   1
 19:  -3,  -6,   7,  -5,   9,  -1,  -2,  -4,  -8,   3,   6,  -7,   5,  -9,   1
 20:                                                                   10,   1
 21:  -5,  10,   1,  -2,   4,  -8,  -5,  10,   1,  -2,   4,  -8,  -5,  10,   1
 22: -10,  10, -10,  10, -10,  10, -10,  10, -10,  10, -10,  10, -10,  10,   1
 23: -11,  -8, -10,  -1,  -7,  -3,   2,  -9,   6,  -4,  -5,  11,   8,  10,   1
 24:  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,   4,  10,   1
 25:                                                                   10,   1
 26:  -4,  10, -12,   4, -10,  12,  -4,  10, -12,   4, -10,  12,  -4,  10,   1
 27:  -8,  10,   1,  -8,  10,   1,  -8,  10,   1,  -8,  10,   1,  -8,  10,   1
 28: -12,  -4,   8,  12,   4,  -8, -12,  -4,   8,  12,   4,  -8, -12,  10,   1
 29:  -1,  -3,  -9,   2,   6, -11,  -4, -12,  -7,   8,  -5,  14,  13,  10,   1
 30:  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,  10,   1
 31:  -3,   9,   4, -12,   5, -15,  14, -11,   2,  -6, -13,   8,   7,  10,   1
 32:                                                    16,   8,   4,  10,   1
 33:   1,  10,   1,  10,   1,  10,   1,  10,   1,  10,   1,  10,   1,  10,   1
 34:   8,  -6,  -4, -14,   2, -10,  16, -12,  -8,   6,   4,  14,  -2,  10,   1
 35:  -5,  10,  15,   5, -10, -15,  -5,  10,  15,   5, -10, -15,  -5,  10,   1
 36:  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  -8,  10,   1
 37: -11,  10,   1, -11,  10,   1, -11,  10,   1, -11,  10,   1, -11,  10,   1
 38:  16,  -6, -12,  14, -10,  18,  -2,  -4,  -8, -16,   6,  12, -14,  10,   1
 39: -17,  10,   1,   4,  16, -14, -17,  10,   1,   4,  16, -14, -17,  10,   1
 40:                                                              20,  10,   1
```

There are so many interesting things here it's hard to know where to start!

First of all, if you count the number of entries in a row (i.e., for a
base), it tells you how many digits (from the right) that you need to
consider in a number to determine if it's divisible by the number for the
row (i.e., to determine if the number modulo the base is zero). So you can
see that for 2, 5, and 10 you only need to look at the last digit, as
mentioned above.  For divisibility by 8 you only need consider the last 3
digits. And you can see that for 3 and 11 (mentioned above) it looks like
you need to consider every digit.

To apply a row of the table to a number to test for divisibilty by a given
base, you multiply each of the digits in the number by its corresponding
entry in the row for that base.  You add all those products and if the sum
is divisble by the base, then so is the original number. If the sum is too
large for you to know this, you can just apply the rule again to get a
smaller (equivalent, modulo the base) sum.

For example, let's see if 659721 is divisible by 16. The table shows us we
only have to consider the last 4 digits of 659721.  We compute the sum

```
(9 * 8) + (7 * 4) + (2 * -6) + (1 * 1) = 72 + 28 - 12 + 1 = 89
```

At this point you'll need to work out yourself that `89 = (5 * 16) + 9`,
and therefore `659721 mod 16 = 9`.

So now you can see pretty much why the rule of 3 works. Each column in the
table for the 3 row has a 1. Put another way, `10^x mod 3 = 1` for all `x
>= 0`. That means that each digit in a number contributes 1 times that
digit to the remainder when the number is divided by 3. So if you simply
add up the digits in the number (which of course the same as multiply each
digit by 1 and adding up the products), you get the overall remainder.

And you can see why the rule of 11 works.




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
usage: modulus.py [-h] [--from N] [--to N] [--places N] [--negatives] [--n N]
                  [--base N] [--verbose]

Either print a list of remainders for 10^X mod BASE, for increasing values of
X and BASE. Or compute a specific modulus using the remainders for a given
base.

optional arguments:
  -h, --help   show this help message and exit

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

remainder:
  compute a specific remainder

  --n N        The number whose remainder should be computed. (default: None)
  --base N     The int base of the remainder to compute. (default: None)
  --verbose    If specified, show intermediat information. (default: False)
```
