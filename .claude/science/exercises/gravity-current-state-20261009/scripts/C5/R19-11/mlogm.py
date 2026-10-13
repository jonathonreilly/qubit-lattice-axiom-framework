"""R19-11 (a): test for m ln m terms. Fit row(m) = c0 + c1 m + e m ln m + c2 m^2 + c3 m^3 on the Dirac scan (m <= mmax)
and report e against the m-ln-m-free fit; scalars: c0 + c1 m + e m ln m + c2 m^2 + c4 m^4."""
import sys, re, numpy as np
def parse(fn):
    D = {}
    for line in open(fn):
        mm = re.match(r'm=(\S+)', line)
        if not mm: continue
        D[float(mm.group(1))] = {k: float(v) for k, v in re.findall(r'(\w+) ([+-]\d\.\d+e[+-]\d+)', line.split('|')[0])}
        if '| off:' in line:
            for k, v in re.findall(r'(\w+) ([+-]\d\.\d+e[+-]\d+)', line.split('| off:')[1]): D[float(mm.group(1))]['off_' + k] = float(v)
    return D
lnm = lambda m: m*np.log(m) if m > 0 else 0.0
for fn, mmax, hi in ((sys.argv[1], 2.6e-3, lambda m: m**3), (sys.argv[2], 2.6e-2, lambda m: m**4)):
    D = parse(fn); ms = sorted(m for m in D if m <= mmax); print('== %s, %d points m in [%g, %g]' % (fn, len(ms), ms[0], ms[-1]))
    for k in D[ms[0]]:
        if k.startswith('off_T2g') or k.startswith('off_Eg'): continue
        y = np.array([D[m][k] for m in ms])
        A0 = np.array([[1, m, m*m, hi(m)] for m in ms]); A1 = np.array([[1, m, lnm(m), m*m, hi(m)] for m in ms])
        c0, *_ = np.linalg.lstsq(A0, y, rcond=None); c1, *_ = np.linalg.lstsq(A1, y, rcond=None)
        print('  %-9s no-log: c1 %+.6e res %.1e | with m ln m: e %+.3e c1 %+.6e res %.1e' % (k, c0[1], np.abs(A0@c0 - y).max(), c1[2], c1[1], np.abs(A1@c1 - y).max()))
