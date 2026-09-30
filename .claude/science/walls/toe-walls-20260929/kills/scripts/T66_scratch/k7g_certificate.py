"""Exact left-null certificate for E2 (+weak ell conditions) at planar R=1, no Z: find w with w^T A = 0 and w^T b != 0, and print its support."""
import sys
import sympy as sp
sys.argv = ['x', '1', '1', '1', 'noZ']
src = open('k7f_E2_firstclass.py').read().split("tag = f")[0]
exec(src)
c, r, e, bb = sub(lambda k: isPP(k) or ellrow(k))
nr, nc = len(r), len(c)
inv_r = {v: k for k, v in r.items()}
M = sp.zeros(nr, nc)
for i, j, cf in e:
    M[i, j] += sp.Rational(cf.numerator, cf.denominator)
bvec = sp.zeros(nr, 1)
for i, cf in bb.items():
    bvec[i] = sp.Rational(cf.numerator, cf.denominator)
ns = M.T.nullspace()
print("rows", nr, "cols", nc, "left-null dim", len(ns))
cert = None
for w in ns:
    val = (w.T * bvec)[0]
    if val != 0:
        cert = w / val; break
print("certificate found:", cert is not None)
supp = [(inv_r[i], cert[i]) for i in range(nr) if cert[i] != 0]
print("support size", len(supp))
for key, v in supp[:60]:
    print(key, v)
