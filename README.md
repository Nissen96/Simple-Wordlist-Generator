# Simple Wordlist Generator

This script is used to generate a wordlist from one or more input wordlists.
The output is the cartesian product of the provided wordlists, i.e. for two wordlists, the result is all combinations of a word from the first followed by one from the second.

Optionally, a prefix, suffix and delimiter (or list of delimiters) can be provided.


## Examples

Assume the following three wordlists:

`w1.txt`:
```
123
456
789
```

`w2.txt`:
```
abc
def
```

`w3.txt`:
```
UVW
XYZ
```

Combine two wordlists:
```
$ python wordgen.py -w w1.txt w2.txt
123abc
123def
456abc
456def
789abc
789def
```

Combine a wordlist with itself `n=3` times, delimiting the first two by `+` and last two by `=`:
```
$ python wordgen.py -w w2.txt -n 3 -d '+' '='
abc+abc=abc
abc+abc=def
abc+def=abc
abc+def=def
def+abc=abc
def+abc=def
def+def=abc
def+def=def
```

Combine all three wordlists, adding a prefix and suffix to each and joining with `/`:
```
$ python3 wordgen.py -w w1.txt w2.txt w3.txt -p "<" -s ">" -d "/"
<123/abc/UVW>
<123/abc/XYZ>
<123/def/UVW>
<123/def/XYZ>
<456/abc/UVW>
<456/abc/XYZ>
<456/def/UVW>
<456/def/XYZ>
<789/abc/UVW>
<789/abc/XYZ>
<789/def/UVW>
<789/def/XYZ>
```
