# GUIDE only. Free massive lattice scalar, mode sums (formulas READ from row 903, L33-37).
# Compares the thermal log-sum g of the free-wall slab (Neumann = bonds across the cut removed;
# also a Dirichlet variant) with the ring g_P in the doubled direction, and the doubling ratio.
import numpy as np, itertools, sys
def F(a, w): return -np.log1p(-np.exp(-a*w))
def omega(m, th1, th2, th3):
    s = m*m + (2-2*np.cos(th1))[:,None,None] + (2-2*np.cos(th2))[None,:,None] + (2-2*np.cos(th3))[None,None,:]
    return np.arccosh(1 + s/2)
def grid(kind, n):
    if kind == 'N': return np.pi*np.arange(n)/n
    if kind == 'P': return 2*np.pi*np.arange(n)/n
    if kind == 'D': return np.pi*np.arange(1, n+1)/(n+1)
def g(a, m, kind1, b, c, d):
    return F(a, omega(m, grid(kind1, b), grid('N', c), grid('N', d))).sum()
rows = []
for m in (0.01, 0.1, 0.3, 1.0):
    for b in (6, 8, 12, 16, 24, 32):
        for cd in (b, 2*b):
            for a in sorted(set([3, max(3, b//4), b//2])):
                if a > b//2: continue
                gN, gP, gD = (g(a, m, k, b, cd, cd) for k in 'NPD')
                gN2, gP2, gD2 = (g(a, m, k, 2*b, cd, cd) for k in 'NPD')
                rows.append((m, b, cd, a, gN/gP-1, gN2/gP2-1, gD/gP-1, gD2/gP2-1, gN2/gN, gD2/gD, gP2/gP, gP))
print("m b c=d a | (gN-gP)/gP at b, at 2b | (gD-gP)/gP at b, at 2b | dbl N, D, P | gP")
for r in rows:
    print("%.2f %2d %2d %2d | %+.3f %+.3f | %+.3f %+.3f | %.3f %.3f %.3f | %.3e" % r)
A = np.array(rows)
print("range (gN-gP)/gP:", A[:,4:6].min(), A[:,4:6].max())
print("range (gD-gP)/gP:", A[:,6:8].min(), A[:,6:8].max())
print("max doubling N, D, P:", A[:,8].max(), A[:,9].max(), A[:,10].max())
