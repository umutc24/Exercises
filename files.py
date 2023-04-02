# files.py

import sys

f = open(sys.arvg[1], mode='rt', encoding='utf-8')
for line in f:
    #print(line)
    sys.stdout.write(line)
f.close()
