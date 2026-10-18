"""X1 arithmetic checks on one SM generation (16, all left-handed Weyl). Exact rationals.
(a) kappa_H = sum of charges (F3-B flux index / FX U(1) case) for U(1)_Y, B-L, X, F.
(b) Z4^X charges mod 4 and Z16 index.
(c) which psi psi pairings are G_SM singlets (only these can enter a G_SM-symmetric Gaussian unitary
    that does not conserve U(1)_F); with Z4^X imposed, which survive.
(d) Fidkowski-Xu condition 2N | N_f for uniform chiral Z_2N, N_f = 16 (and 15).
"""
from fractions import Fraction as Fr
from itertools import combinations_with_replacement as cwr
# name, SU3 irrep ('1','3','3b'), SU2 irrep (1 or 2), Y, B-L, X, multiplicity = dim
fields = [
 ("Q",   '3', 2, Fr(1,6),  Fr(1,3),  1),
 ("u^c", '3b',1, Fr(-2,3), Fr(-1,3), 1),
 ("d^c", '3b',1, Fr(1,3),  Fr(-1,3), -3),
 ("L",   '1', 2, Fr(-1,2), Fr(-1),   -3),
 ("e^c", '1', 1, Fr(1),    Fr(1),    1),
 ("nu^c",'1', 1, Fr(0),    Fr(1),    5),
]
dim = lambda f: {'1':1,'3':3,'3b':3}[f[1]]*f[2]
N = sum(dim(f) for f in fields); print("N_f =", N)
for lab, k in (("Y",3),("B-L",4),("X",5)):
    s1 = sum(dim(f)*f[k] for f in fields); s3 = sum(dim(f)*f[k]**3 for f in fields)
    print(f"kappa_{lab} = sum q = {s1};  sum q^3 = {s3}")
print("kappa_F = sum 1 =", N)
# X = 5(B-L) - 4Y check
print("X == 5(B-L)-4Y for all:", all(f[5] == 5*f[4]-4*f[3] for f in fields))
print("X mod 4:", {f[0]: f[5] % 4 for f in fields}, "-> Z16 index (all charge 1 mod 4) =", N % 16, "mod 16")
def su3_singlet(a,b): return {a,b}=={'3','3b'} or (a=='1' and b=='1')
print("\nG_SM-singlet psi psi pairings (Lorentz scalar, one generation):")
for f,g in cwr(fields,2):
    if not su3_singlet(f[1],g[1]): continue
    if f[3]+g[3]!=0: continue
    su2 = (f[2]==1 and g[2]==1) or (f[2]==2 and g[2]==2)
    if not su2: continue
    # same field with SU(2) doublet: eps_ij antisym x Lorentz eps x Grassmann -> vanishes for one generation
    if f is g and f[2]==2: note="vanishes (one generation)"
    else: note="allowed"
    z4 = (f[5]+g[5]) % 4
    print(f"  {f[0]} {g[0]}: {note}; X-charge {f[5]+g[5]} = {z4} mod 4 -> {'Z4^X-allowed' if z4==0 else 'Z4^X-forbidden'}")
print("\nFidkowski-Xu: uniform chiral Z_2N shallow-circuit possible only if 2N | N_f:")
for Nf in (16,15):
    print(f"  N_f={Nf}: allowed 2N in", [n for n in (2,4,6,8,10,12,16,32) if Nf % n == 0], "; U(1)_F (N->inf): forbidden")
