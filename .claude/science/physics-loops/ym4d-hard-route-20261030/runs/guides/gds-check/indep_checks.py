# Independent checks of row 1081's GUIDE code (run from a copy; reads only).
import sys, math, random
import numpy as np
sys.path.insert(0, sys.argv[1])            # folder with the COPY of su2box.py
import su2box as S
from sympy import Rational as Q
from sympy.physics.wigner import wigner_6j as _w6
def wigner_6j(*a):
    try: return _w6(*a)
    except ValueError: return 0
# (a) Racah 6j against sympy (exact), doubled arguments
maxerr = 0.0; cnt = 0
for a in range(0, 13):
  for b in range(0, 13):
    for c in range(0, 13):
      if not S.ok(a, b, c): continue
      for da in (-1, 1):
        for db in (-1, 1):
          args = (a, b, c, b+db, a+da, 1)
          if min(args) < 0: continue
          v = S.sixj(*args); w = float(wigner_6j(*[Q(x, 2) for x in args]))
          maxerr = max(maxerr, abs(v - w)); cnt += 1
random.seed(1)
for _ in range(400):
  args = tuple(random.randint(0, 16) for _ in range(6))
  v = S.sixj(*args); w = float(wigner_6j(*[Q(x, 2) for x in args]))
  maxerr = max(maxerr, abs(v - w)); cnt += 1
print(f"(a) sixj vs sympy wigner_6j: {cnt} cases, max abs error {maxerr:.2e}")
# (b) hand-check entries of X12, X23
B = S.basis(6, 'n3'); idx = {s: i for i, s in enumerate(B)}; X12, X23 = S.xmats(B)
print("(b) X12[(1,1,0)<-(0,0,0)] =", X12[idx[(1,1,0)], idx[(0,0,0)]], "(expect 0.5)")
print("    2*X23[(1,0,1)<-(1,1,0)] =", 2*X23[idx[(1,0,1)], idx[(1,1,0)]], "(expect 1/2, the integral <tr AB, tr A tr B>)")
print("    min entry X12, X23:", X12.min(), X23.min())
# (c) two-sheet face gap at beta_L = infinity against an independent n = 2 code (power series Bessel)
def I(nu, x, K=300):
    t = math.exp(nu*math.log(x/2) - math.lgamma(nu+1)); s = 0.0
    for k in range(K):
        s += t; t *= (x/2)**2/((k+1)*(k+1+nu))
    return s
def m_n2(beta, t=0.0, nmax=50):
    ns = np.arange(1, nmax+1); a = np.array([I(n, beta)/I(1, beta) for n in ns])
    k = np.array([[I(abs(n-m), beta) - I(n+m, beta) for m in ns] for n in ns])
    d = a*np.exp(-t*(ns**2-1)/4.)
    w = np.linalg.eigvalsh(d[:,None]*k*d[None,:]); return math.log(w[-1]/w[-2])
for bM, logged in ((2.4, 2.2829867354), (4.0, 2.4210796688), (0.5, 4.2118995134)):
    print(f"(c) beta_M {bM}: independent n=2 face gap {m_n2(bM):.10f}; logged two-sheet face gap {logged}")
