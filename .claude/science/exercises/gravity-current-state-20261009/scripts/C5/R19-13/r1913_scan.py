"""Scan the best radius-R isometric insertion cost c(M,R) on the infinite chain (upper bound, explicit Gaussian
isometry), M descending with warm starts.  Usage: python r1913_scan.py R1 R2 ...  -> r1913_scan_R{R}.out"""
import sys, time, os, numpy as np
from r1913_lib import window, symp_opt, dE_of_S
Mg = np.logspace(np.log10(3.0), -3, 31)
suf = ''
if os.environ.get('MGRID'):
    lo, hi, num = os.environ['MGRID'].split(','); Mg = np.linspace(float(hi), float(lo), int(num)); suf = '_gap'
for R in map(int, sys.argv[1:]):
    t0 = time.time(); S = None
    with open('r1913_scan%s_R%d.out' % (suf, R), 'w') as fo:
        fo.write('# R=%d  columns: M  dE_upper(best Gaussian isometry on slab radius R)  dE_product(R=0 check uses S=1)  seconds\n' % R)
        for M in Mg:
            W = window(M, R); t = time.time()
            d, S = symp_opt(W, S_init=S)
            fo.write('%.8e %.12e %.1f\n' % (M, d, time.time() - t)); fo.flush()
    print('R=%d done in %.0f s' % (R, time.time() - t0), flush=True)
