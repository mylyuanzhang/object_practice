# -*- coding: utf-8 -*-
import difflib

a = 'a.txt'
b = 'b.txt'
d = difflib.ndiff(a, b)

if __filename__ == '__main__'