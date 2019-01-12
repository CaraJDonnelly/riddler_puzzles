"""Brute force solution to Riddler Express puzzle:
https://fivethirtyeight.com/features/in-space-no-one-can-hear-your-3d-printer-die/

$ time python main.py
6

real	0m0.037s
user	0m0.025s
sys	0m0.012s
"""

# Input number, known to be made up of only factors in [1,..,99]. Goal of this
# module is to work out the valid value of 'digit'.
NUMBER_TEMPLATE = ('53013180176278773980288979275410970{digit}1393585477100662'
                   '5765205034629448443332397474796029780329298923618304000000'
                   '0000')
# All primes up to 99.
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                61, 67, 71, 73, 79, 83, 89, 97]
# Digits to try out in the template.
DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# For each trial digit, use the small primes to factorize it.  If we run out of
# small primes and we've not successfully factorized the number i.e. we are not
# left with 1, there is a prime factor bigger than 97, so this trial digit was
# not the right answer.
for digit in DIGITS:
    num_to_divide = long(NUMBER_TEMPLATE.format(digit=digit))
    for p in SMALL_PRIMES:
        while num_to_divide % p == 0:
            num_to_divide = num_to_divide / p
    if num_to_divide == 1:
	# We could break here, but it would be nice to check we don't
	# accidentally find two 'correct' answers.
        print digit

