"""Referee X2: (i) SU(N) lemma margin for all N (monotone); g^2 needed for 15 one-loop decades,
pure SU(3) and SU(3) b1>0 contents. (ii) R3 closure with Wilson hop: mass dependence is (m+3r)*X."""
import math, sys, numpy as np
b0c = 8*math.pi**2/(15*math.log(10))
marg = lambda N: (11*N-3*b0c)/2 - 34*N**3/(13*N**2-3)
print("margin N=2,3,10,100,1e4:", [round(marg(N),3) for N in (2,3,10,100,10**4)])
print("margin increasing on N>=2 (dm/dN>0 at 2..1e4 sample):", all(marg(N+1)>marg(N) for N in range(2,10000)))
for Nf in (0, 8):
    b0 = 11 - 2*Nf/3
    print(f"SU(3) Nf={Nf}: g^2 for 15 one-loop decades = {8*math.pi**2/(15*math.log(10)*b0):.3f}")
sys.path.insert(0, '../H1')
import importlib.util
spec = importlib.util.spec_from_file_location("r3", "../H1/r3_closure_mass.py")
src = open("../H1/r3_closure_mass.py").read().split("for trial in range(3):")[0]
ns = {}; exec(src, ns)
rng = np.random.default_rng(5); V = ns['V']
N = 1 + 0.3*rng.standard_normal(V); M = 1 + 0.3*rng.standard_normal(V)
br = lambda m, r: ns['comm'](ns['dirac_h'](N, m, r=r), ns['dirac_h'](M, m, r=r))
r = 1.0
B0 = br(-3*r, r)
for m in (-1.0, 0.0, 0.9, 2.0):
    X = (br(m, r) - B0)/(m + 3*r)
    print(f"m={m}: (bracket(m)-bracket(-3r))/(m+3r) max {np.abs(X).max():.4f}")
Xa = (br(0.0, r)-B0)/3; Xb = (br(2.0, r)-B0)/5
print("mass dependence exactly linear in (m+3r):", np.allclose(Xa, Xb))
print("bracket at m=-3r equals the on-site-free (hop-only) bracket by construction of dirac_h line 74")
