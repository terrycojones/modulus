This repo has some simple code for playing around looking for remainder
patterns that give tricks for rapid calculation of divisibility.  When I
was a kid we were told rules for divisibility. Some were very simple:

* If the final digit of a number is 0, the number is divisible by 10.
* If the final digit of a number is 0 or 5, the number is divisible by 5.
* If the final digit of a number is even, the number is divisible by 2.

Some were a little more involved:

* If all the digits of a number add to something divisible by 3, then the
  number is also divisible by 3.
* If the two outside digits of a 3-digit number sum to the middle digit,
  then the number is divisible by 11.

Later, as a teen, I came across a more general rule for 11:

* Alternately add and subtract the digits in the number. If the result is
  divisible by 11, then the number is also divisible by 11.

It's not hard to prove that the general rules for 3 and 11 work. Hint:
consider 10^0 mod 3, 10^1 mod 3, 10^2 mod 3, etc., and do the same for 11.

Fast forward nearly 40 years... The other day I saw a tweet from
[Josh Reich](https://twitter.com/i2pi) giving an example of the rule of 3:

> 345 is divisible by 3. 3+4+5=12, 12/3=4. 345 = 3*100 + 4*10 + 5 =
> 3*(99+1) + 4*(9+1) + 5*(0+1) = (3*99 + 4*9 + 5*0) + (3+4+5). The first part
> is divisible by three (9, 99, 999, etc). The number will be divisible by
> three if its sum of digits are. Happy 3pm!
> 
> Josh Reich (@i2pi)
> [March 21, 2018]("https://twitter.com/i2pi/status/976579575030231040")

I decided to write a quick bit of code to print out a table of remainders
for different powers of ten and different bases to see if there were any
other nice patterns.

## modulus.py

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

There are so many interesting things here it's hard to know where to start.

First of all, if you count the number of entries in a row (i.e., for a
base), it tells you how many digits (from the right) that you need to
consider in a number to determine if it's divisible by the number for the
row (i.e., to determine if the number modulo the base is zero). So you can
see that for 2, 5, and 10 you only need to look at the last digit, as in
the very simple rules above.  For divisibility by 8 you only need consider
the last 3 digits. And you can see that for 3 and 11 (also mentioned above)
it looks like you need to consider every digit.

To use a row of the table to a number to test for divisibility, you multiply
each of the digits in the number by the corresponding entry in the row for
that base.  Add all those products and if the sum is divisible by the base,
then so is the original number. If the sum is too large for you to know
this, you can just apply the rule again to get a smaller (equivalent,
modulo the base) sum.

For example, let's see if 659721 is divisible by 16. The 16 row of the
table shows us we only have to consider the last 4 digits of 659721. To
find the remainder we compute the sum

```
(9 * 8) + (7 * 4) + (2 * -6) + (1 * 1) = 72 + 28 - 12 + 1 = 89
```

At this point you'll need to work out yourself that `89 = (5 * 16) + 9`,
and therefore `659721 mod 16 = 9`.

### 3 (and 11)

Given this explanation, you can see why the rule of 3 works. Each column in
the table for the base 3 row has a 1. Put another way, `10^x mod 3 = 1` for
all `x >= 0`. That means that each digit in a number contributes 1 times
that digit to the remainder when the number is divided by 3. So if you
simply add up the digits in the number (which of course the same as
multiplying each digit by 1 and adding up the products), you get the
overall remainder. If that remainder is 0 or otherwise divisible by 3, then
the overall remainder is 0.

And you can see why the alternating add/subtract rule of 11 works because
its table values alternate between 1 and -1. The underpinnings of the rule
for 11 and the rule for 3 are almost identical.

### 4

You can see there's a simple rule for 4: double the second last (tens)
digit and add it to the last digit. If the result is divisible by 4, so was
the original number. E.g., with `735` we'd compute `(2 * 3) + 5 = 11` and
conclude that `735` is not divisible by 4. You probably already know this
test, at least implicitly, because 100 is 0 mod 4 and so are all higher
powers of 10. I think I learned that when I was about 9, so I'm probably
not telling you anything new.

You can easily show that if `10^X mod BASE = 0` then `10^(X+i) mod BASE` is
also 0, for all `i >= 0`. In other words, once a remainder is 0 for some
power of ten, it's 0 for all higher powers. You can prove this by
induction, since moving from `X` to `X+1` just adds 10 more of something
that is `0 mod B`, which is also 0.

### 6

There's a simple rule for 6: compute the sum of the double of each
digit. You probably wouldn't use that though as you can trivially use the
rule for 2 (look at the last digit) and then the simpler rule for 3.

### 7

7 gets interesting. You can see the row ends `-2, -3, -1, 2, 3, 1` and
looking further left on the row it looks like that pattern continues. This
is cool because the remainders match each other in sets of 3, with opposite
signs. This means that all numbers of the form `abcabc` (where `a`, `b`,
and `c` are digits) are divisible by 7, as are all numbers of the form
`defdefabcabc` and so on. This is not surprising if you happen to know that
`1001` is divisible by 7, because `abcabc = abc * 1001`. So it doesn't
matter at all what `a`, `b`, and `c` are because `abcabc` is divisible by
`1001` (and hence also by 7 (and 11 and 13, since 1001 = 7 * 11 * 13). The
`defdefabcabc` (and so on) patterns are then also not surprising because
they are just of the form `(1000000 * X + Y)` where X and Y are both of the
6-digit form just shown to be divisible by 7, and adding two numbers that
are both `0 mod 7` gives another.

This example shows the advantage of using the `--negatives` option. Without
it the rule for 7 looks more complicated:

```sh
$ modulus.py --places 15 --from 7 --to 7
    14  13  12  11  10   9   8   7   6   5   4   3   2   1   0
 7:  2,  3,  1,  5,  4,  6,  2,  3,  1,  5,  4,  6,  2,  3,  1
```

the above looks like we'd have to remember the remainders 1, 3, 2, 6, 4, 5
to apply (right to left) repeatedly, whereas the `-2, -3, -1, 2, 3, 1` is
easier to remember and makes the `abcabc` pattern immediately clear.

Note that the `abcabc` pattern is not the *only* thing that will be
divisible by 7, it's just a pattern that always will be. E.g., 301021 isn't
in the `abcabc` pattern but is divisible by 7 `(3 * -2 + 1 * -1 + 2 * 3 +
1 * 1) = 0`. So the `abcabc` pattern is sufficient, but not necessary.

This leads to another simple thing you can prove.

Assume `10^x mod a = b` and `10^(x+1) mod a = c`. Then if `10^y mod a = b`
for some `y > x`, then `10^(y+1) mod a = c`. In words this means that if
you read the values right-to-left in a row in the above table, as soon as
you come to a repeated value, an infinite loop of values has begun. So
e.g., in the row for 3 as soon as you see the second 1 you know all
subsequent numbers will be 1. In the row for 7 (above), as soon as you see
the second 1, you know the sequence `5, 4, 6, 2, 3, 1` is going to repeat
indefinitely.

Anyway, the rule for divisibility by 7 is complicated enough that you
wanted a quick way to test for it you could just do the division in your
head :-) But at least our table shows us that there cannot be any quick way
to do it, in the sense that you definitely have to consider all the digits
in the number. You can prove that with an adversary argument: if you
claimed to have an algorithm for divisibility by 7 that didn't consider one
(or more) digits in the number, an adversary could trivially break your
algorithm on every input.

### Composite bases

When I first wrote the code I made it only print lines for bases that were
prime, partly from habit, partly from knowing that in many interesting
(small) cases you would simply apply the rules for the prime factors of a
composite. E.g., to test for divisibility by 6, do the 2 test and if that
passes also do the 3 test.  But then I decided to print the rows for
composite numbers too, and I'm glad I did. There's nothing deep to see, but
it's interesting to look at some composite values, such as 22 or 33, and to
see how they relate to the rows for their factors.

### Powers of 2

If you look at increasing powers of 2 in the table, it looks like you need
to consider one more digit each time the divisor doubles. So for
divisibility by 32 (2^5) you need to look at the final 5 digits.  You could
probably prove this with a little thought, but you can intuitively see that
it makes sense. For a number to be divisible by `2^x` you need it to be
divisible by 2 and (if so) you need half the number to be divisible by
`2^(x-1)`. To determine the first requirement you need to look at just one
digit (the last) of the number. Then you need to consider just the last
digit of half the number, and so on.  As for all the digits to the left of
the last `x`, they all represent something times `10^y` (where `y > x`) and
so are zero mod `2^x` (because 10 = 2 x 5), so that's why you get to ignore
them. Neat.

### 37

Finally, I have to mention 37, at least for sentimental reasons. When I was
16 or so I wondered why people only memorized their times tables out to
12x12 and not more. I knew the table out to 20x20 but decided that wasn't
enough. So with the help of my first programmable calculator (my beloved
[Casio FX-502P](https://en.wikipedia.org/wiki/Casio_FX-502P_series), before
the [HP41](https://en.wikipedia.org/wiki/HP-41C) series stole my heart
forever) I wrote out (yes, by hand, with a pen) the tables to 100x100. It
covered something like 16 sheets of paper, which I taped together. I
started trying to memorize the whole thing (all 4950 values) but didn't get
too far.

I noticed that 37 had a nice property. Here are the first multiples of 37:

    037, 074, 111, 148, 185, 222, 259, 296, 333, 370, 407, 444, 481, 518, 555

111, 222, 333 stand out, obviously. But if you look at the other digits you
can see that to get from 037 to 074 you flip the last two digits and add
one. To get from 148 to 185 or from 259 to 296, do the same thing. From 370
to 407 and from 481 to 518 you flip the last two digits but add one in the
hundreds column.

Here again is the row for 37:

    37: -11, 10, 1, -11, 10, 1, -11, 10, 1, -11, 10, 1, -11, 10, 1

The last three remainders are `-11, 10, 1`. You can see that if all digits
are the same you're going to get a 0 total (since -11 + 10 + 1 = 0). 

037:   0*-11 + 3*10 + 7*1
074:   0*-11 + 7*10 + 4*1

A*10 + B
B*10 + (A+1)


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
