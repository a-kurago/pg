# Simple password generator
```
Usage: pg.py [OPTIONS]

Options:
  -n, --length INTEGER          Password length
  -c, --count INTEGER           Number of passwords to generate
  -d, --use-digits
  -l, --use-letters
  -L, --use-upper-letters
  -s, --use-special-chars
  -S, --special-chars-set TEXT  Set of special characters to use in password.
                                Example: @#$%

  -e, --exclude-similar         Exclude similar characters like 0,o,O,1,l,I
  -p, --pattern TEXT            Example: "llddLL". d, l, L, s stands for
                                digit, letter, upper letter, special character

  -h, --help                    Show this message and exit.
```
