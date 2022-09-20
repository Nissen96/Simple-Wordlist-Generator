import argparse
from itertools import product
from pathlib import Path
import sys


def generate_wordlist(wordlists, delimiters, prefix, suffix):
    for words in product(*wordlists):
        word = prefix
        for w, d in zip(words, delimiters):
            word += f'{w.strip()}{d}'
        yield f'{word}{words[-1].strip()}{suffix}\n'


def parse_args():
    parser = argparse.ArgumentParser(description='Wordlist generator')
    parser.add_argument('-w', '--wordlist', type=argparse.FileType('r'), nargs='+', required=True, help='wordlist(s)')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('x'), metavar='OUTFILE', default=sys.stdout, help='output file (default: stdout)')
    parser.add_argument('-n', type=int, default=1, help='number of wordlist repetitions (for single wordlist only)')
    parser.add_argument('-d', '--delim', type=str, nargs='*', action='extend', default=[], help='optional delimiter or list of #wordlists-1 delimiters')
    parser.add_argument('-p', '--prefix', type=str, default='', help='optional prefix to prepend to each entry')
    parser.add_argument('-s', '--suffix', type=str, default='', help='optional suffix to append to each entry')

    args = parser.parse_args()

    # Validate and expand wordlists
    if len(args.wordlist) > 1 and args.n > 1:
        parser.error('repetition cannot be used for multiple wordlists')
    args.wordlist.extend([open(args.wordlist[0].name) for _ in range(args.n - 1)])

    # Validate and expand delimiters
    if len(args.delim) == 0:
        args.delim.append('')
    elif len(args.delim) not in (1, len(args.wordlist) - 1):
        parser.error('invalid number of delimiters, must be 1 or #wordlists-1')
    if len(args.delim) == 1:
        args.delim.extend([args.delim[0]] * (len(args.wordlist) - 2))

    return args


def main():
    args = parse_args()
    for word in generate_wordlist(args.wordlist, args.delim, args.prefix, args.suffix):
        args.outfile.write(word)
    for f in args.wordlist:
        f.close()


if __name__ == "__main__":
    main()
