import os

numpdfs = 100
for x in range(1, numpdfs):
    os.remove('windowsticker (%d).pdf' % x)
