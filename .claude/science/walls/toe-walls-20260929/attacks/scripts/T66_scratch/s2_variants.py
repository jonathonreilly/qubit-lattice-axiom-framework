from solve import *
import sys
for R in (1,2):
    for use in (('V2','T3'), ('V2','T3','G2'), ('V2','T3','G2','xi1'), ('V2','T3','G2','xi1','chi'), ('V2','T3','xi1','chi'), ('V2','T3','G2','chi')):
        for mode in ('full','uniformM'):
            r,_ = analyse(R, mode, use, exact=True, verbose=False)
            print(R, mode, use, 'rows',r['rows'],'cols',r['cols'],'rank',r['float_rank'],'resid %.2e'%r['float_resid'], 'modOK', r['mod'][0][2], 'rk', r['mod'][0][1], r['secs'])
