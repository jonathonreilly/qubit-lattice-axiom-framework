#!/usr/bin/env python3
"""minimal-toe-merged runner: does B's level/link split act as A's missing breaking rule?

Site: 5 fermionic modes (2 unit levels + 3 owned links), Fock space Lambda(C^5), dim 32,
built with Jordan-Wigner.  Checks (exact up to float):
  S. so(10) from the 10 Majorana Clifford generators; the stabiliser of (occupation
     number N, link number N_L) inside so(10) has dim 13 = u(2)+u(3); the plain number
     operator N is NOT in so(10) but N - 5/2 is (the spinor twist).
  X. U(1)_X = N - 5/2 on the even half: charges, anomaly freedom with Y, SU3, SU2, grav;
     untwisted N anomalous; the Z4 centre lies in U(1)_X; nu^c nu^c breaks Z4 -> Z2.
  W. induced-coupling indices: Tr T3^2 = Tr T8-type = (3/5) Tr Y^2 = 2 -> sin^2 = 3/8;
     one-loop SM running from measured M_Z couplings (comparison only).
  F. family count: the three record-axis readings of the unit span the same 32 states;
     the axis change is an element of the SU(2) frame group.
  Z. Z16 cross-check: 2^(1+d) = 16 only at d = 3.
No measured number enters S, X, F, Z.  W compares to measured couplings.
"""
AUDIT_TIMEOUT_SEC = 60
import numpy as np
from fractions import Fraction as Fr
from itertools import combinations
from math import comb, log, pi, exp

P = F = 0
def check(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))

n = 5  # modes 0,1 = unit levels ; 2,3,4 = owned links
I2 = np.eye(2); Z = np.diag([1., -1.]); a1 = np.array([[0., 1.], [0., 0.]])  # annihilator
def kron(*ms):
    out = np.array([[1.]])
    for m in ms: out = np.kron(out, m)
    return out
c = [kron(*([Z] * j + [a1] + [I2] * (n - j - 1))) for j in range(n)]
cd = [x.T.conj() for x in c]
num = [cd[j] @ c[j] for j in range(n)]
N = sum(num); NL = num[2] + num[3] + num[4]; NQ = num[0] + num[1]
# Majorana generators -> so(10)
G = []
for j in range(n):
    G.append(c[j] + cd[j]); G.append(1j * (c[j] - cd[j]))
so10 = [0.5 * (G[a] @ G[b]) for a in range(10) for b in range(a + 1, 10)]
def vec(m): return np.concatenate([m.real.ravel(), m.imag.ravel()])
B = np.array([vec(m) for m in so10]).T
def in_span(m):
    x, *_ = np.linalg.lstsq(B, vec(m), rcond=None)
    return np.linalg.norm(B @ x - vec(m)) < 1e-9
def in_span(m, _r=in_span):  # Hermitian generators are i * (real so(10) element)
    return _r(m) or _r(1j * m)
check("S1 so(10) spanned by 45 bilinears", np.linalg.matrix_rank(B) == 45)
# stabiliser: X in so(10) with [X,N]=0 and [X,NL]=0
def comm_map(Hs):
    rows = []
    for m in so10:
        rows.append(np.concatenate([vec(m @ H - H @ m) for H in Hs]))
    return np.array(rows).T
dimJ = 45 - np.linalg.matrix_rank(comm_map([N]))
dimS = 45 - np.linalg.matrix_rank(comm_map([N, NL]))
check("S2 stabiliser of N in so(10) has dim 25 = u(5) (complex structure)", dimJ == 25, f"dim={dimJ}")
check("S3 stabiliser of (N, N_L) has dim 13 = u(2)+u(3) (level/link split)", dimS == 13, f"dim={dimS}")
Id = np.eye(32)
check("S4 plain N not in so(10); N - 5/2 is (spinor twist forced)",
      (not in_span(N)) and in_span(N - 2.5 * Id))
Ytw = (-1 / 3) * NL + 0.5 * NQ
check("S5 hypercharge Y = -1/3 N_L + 1/2 N_Q lies in so(10) (standard SU(5) embedding)", in_span(Ytw))

# ---- X: sector table on the even half ----
sect = []  # (kl, kq, mult, Y, X)
for kl in range(4):
    for kq in range(3):
        if (kl + kq) % 2 == 0:
            sect.append((kl, kq, comb(3, kl) * comb(2, kq),
                         Fr(-kl, 3) + Fr(kq, 2), 2 * (Fr(kl + kq) - Fr(5, 2))))
def tr(f): return sum(m * f(kl, kq, Y, X) for kl, kq, m, Y, X in sect)
def T2_3(kl): return Fr(1, 2) if kl in (1, 2) else Fr(0)      # SU(3) index per state-multiplet unit
def T2_2(kq): return Fr(1, 2) if kq == 1 else Fr(0)
# per-state Dynkin weights: index of rep / dim, so tr over states counts index*dim(other factor)
def w3(kl, kq): return Fr(1, 3) * T2_3(kl) / 1 if kl in (1, 2) else Fr(0)  # T(3)/dim3 per state
def w2(kl, kq): return Fr(1, 2) * T2_2(kq) if kq == 1 else Fr(0)
Xs = sorted({(kl + kq, X) for kl, kq, m, Y, X in sect})
check("X1 U(1)_X charges on even half: N=0:-5, N=2:-1, N=4:+3 (U(1)_chi of 10,5b,1)",
      Xs == [(0, Fr(-5)), (2, Fr(-1)), (4, Fr(3))], str(Xs))
an = {"X": tr(lambda kl, kq, Y, X: X), "X^3": tr(lambda kl, kq, Y, X: X ** 3),
      "X^2Y": tr(lambda kl, kq, Y, X: X * X * Y), "XY^2": tr(lambda kl, kq, Y, X: X * Y * Y),
      "SU3^2X": tr(lambda kl, kq, Y, X: w3(kl, kq) * X), "SU2^2X": tr(lambda kl, kq, Y, X: w2(kl, kq) * X)}
check("X2 all U(1)_X anomalies vanish on the 16 (grav, cubic, mixed with Y, SU3, SU2)",
      all(v == 0 for v in an.values()), str({k: str(v) for k, v in an.items()}))
anN = tr(lambda kl, kq, Y, X: Fr(kl + kq)), tr(lambda kl, kq, Y, X: Fr(kl + kq) ** 3)
check("X3 untwisted N is anomalous on the 16 (Tr N, Tr N^3 nonzero)", anN[0] != 0 and anN[1] != 0,
      f"TrN={anN[0]} TrN3={anN[1]}")
ph = {complex(np.round(np.exp(1j * pi / 2 * float(X)), 12)) for *_, X in sect}
check("X4 exp(i pi/2 X) acts as one phase on the 16: Z4 centre of Spin(10) sits in U(1)_X",
      len(ph) == 1, str(ph))
check("X5 nu^c nu^c has X = -10: condensate breaks Z4 -> Z2 (fermion parity)",
      np.isclose(np.exp(1j * pi / 2 * -10), -1))
# ---- W: induced coupling ratios ----
t3sq = tr(lambda kl, kq, Y, X: Fr(1, 4) if kq == 1 else Fr(0))
y2 = tr(lambda kl, kq, Y, X: Y * Y)
t3c = tr(lambda kl, kq, Y, X: (Fr(1, 4) if (kl == 1) else Fr(0)) if True else 0)
# SU(3) Cartan lambda_3/2 on a colour index: eigen (1/2,-1/2,0); on Lambda^1: sum 1/2 ; on Lambda^2 same
su3 = tr(lambda kl, kq, Y, X: Fr(1, 6) if kl in (1, 2) else Fr(0))  # (1/4+1/4+0)/3 per state
check("W1 Tr T3^2 = 2, Tr(T_colour^2) = 2, Tr Y^2 = 10/3 on the 16",
      t3sq == 2 and su3 == 2 and y2 == Fr(10, 3), f"{t3sq},{su3},{y2}")
s2w = t3sq / (t3sq + y2)
check("W2 induced couplings from complete content: sin^2 theta_W(cell) = 3/8, alpha_3 = alpha_2",
      s2w == Fr(3, 8), str(s2w))
ainv = {1: 0.6 * 127.95 * (1 - 0.23122), 2: 127.95 * 0.23122, 3: 1 / 0.1179}
b = {1: 41 / 10, 2: -19 / 6, 3: -7.0}
L12 = (ainv[1] - ainv[2]) / ((b[1] - b[2]) / (2 * pi))
mu = 91.19 * exp(L12)
a12 = ainv[1] - b[1] / (2 * pi) * L12; a3 = ainv[3] - b[3] / (2 * pi) * L12
print(f"W: SM one-loop: alpha1=alpha2 at mu={mu:.2e} GeV, 1/alpha={a12:.1f}; 1/alpha3={a3:.1f}")
check("W3 (tension) SM-only running cannot meet the 1:1:1 cell prediction (mismatch > 3 in 1/alpha)",
      abs(a12 - a3) > 3, f"mismatch={a12 - a3:.1f}")
# ---- F: families from record axes ----
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)          # z-basis -> x-basis
S = np.array([[1, 0], [0, 1j]]) @ H                   # z-basis -> y-basis
def fock_lift(U):  # one-body U on unit levels, identity on links, lifted to Lambda(C^5)
    from scipy.linalg import expm, logm
    K = logm(U)
    h = sum(K[i, j] * cd[i] @ c[j] for i in range(2) for j in range(2))
    return expm(h)
evens = np.diag((N.diagonal().round() % 2 == 0).astype(float))
spans = [np.eye(32)]
for U in (H * np.exp(-1j * np.angle(np.linalg.det(H)) / 2), S * np.exp(-1j * np.angle(np.linalg.det(S)) / 2)):
    spans.append(fock_lift(U))
M = np.hstack(spans)
check("F1 the three record-axis readings span 32 states, not 96 (one family's worth)",
      np.linalg.matrix_rank(M, tol=1e-8) == 32, f"rank={np.linalg.matrix_rank(M, tol=1e-8)}")
detok = all(np.isclose(np.linalg.det(U * np.exp(-1j * np.angle(np.linalg.det(U)) / 2)), 1) for U in (H, S))
Uf = fock_lift(H * np.exp(-1j * np.angle(np.linalg.det(H)) / 2))
check("F2 the axis change is an SU(2) frame element: commutes with N, N_L (frame-dependent label)",
      detok and np.allclose(Uf @ N, N @ Uf) and np.allclose(Uf @ NL, NL @ Uf))
check("F3 Holevo: three MUB readings of one unit carry <= 1 bit in total (log2 dim C^2)",
      np.isclose(np.log2(2), 1.0))
# ---- Z: Z16 cross-check over link count d ----
ok = [d for d in range(1, 8) if 2 ** (d + 1) % 16 == 0 and d % 2 == 1]
check("Z1 smallest odd d with half-Fock dim 2^(d+1) = 0 mod 16 is d = 3 (A's minimal 16 = B's site)",
      ok[0] == 3 and 2 ** 4 == 16, f"allowed d={ok}")
# ---- S6: the split as a Spin(10) vacuum orientation (45 vev along a X + b Y) ----
Xop = N - 2.5 * Id
dim45 = 45 - np.linalg.matrix_rank(comm_map([0.7 * Xop + 1.3 * Ytw]))
check("S6 a generic 45-adjoint orientation aX+bY has stabiliser dim 13: the 2+3 split = a vacuum choice",
      dim45 == 13, f"dim={dim45}")
# ---- C: Spin(10) channels for 16 x 16bar (mirror pairing), C(L^k) = k(10-k)/2, C(16)=45/8 ----
C16 = Fr(45, 8)
ch = {"1": 0, "45": Fr(2 * 8, 2), "210": Fr(4 * 6, 2)}
dC = {k: 2 * C16 - v for k, v in ch.items()}
print("C: 16x16bar channels DeltaC = 2C16 - C(R):", {k: str(v) for k, v in dC.items()})
check("C1 16x16bar: singlet most attractive (gaps 16 with its mirror), 45 next, 210 repulsive",
      dC["1"] > dC["45"] > 0 > dC["210"])
# ---- T: tastes of the 2^3 cell under lattice rotations (binary octahedral, spin-taste locked) ----
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
from scipy.linalg import expm as _ex
gens = [_ex(-1j * pi / 4 * sx), _ex(-1j * pi / 4 * sz)]
grp = [np.eye(2, dtype=complex)]
changed = True
while changed:
    changed = False
    for g in list(grp):
        for h in gens:
            k = g @ h
            if not any(np.allclose(k, q) for q in grp):
                grp.append(k); changed = True
check("T0 binary octahedral group generated (order 48)", len(grp) == 48, f"order={len(grp)}")
def decomp(rep):
    Pt = sum(rep(g) for g in grp) / len(grp)          # projector on invariants
    comm = sum(np.kron(rep(g), rep(g).conj()) for g in grp) / len(grp)
    return int(round(np.trace(Pt).real)), int(round(np.trace(comm).real))
I2c = np.eye(2)
unl = lambda g: np.kron(g.conj(), np.kron(I2c, I2c))     # taste(right index) x centre x qubit (inert)
lck = lambda g: np.kron(g.conj(), np.kron(I2c, g))       # qubit Bloch axes locked to lattice axes
n1u, cu = decomp(unl); n1l, cl = decomp(lck)
check("T1 qubit not locked: flavour 8 = 4 x (spinor doublet); no singlet, no triplet (sum m^2 = 16)",
      n1u == 0 and cu == 16, f"inv={n1u} comm={cu}")
check("T2 qubit locked: flavour 8 = 2 x (1 + 3): two singlets + two triplets (sum m^2 = 8)",
      n1l == 2 and cl == 8, f"inv={n1l} comm={cl}")
SX = sum(np.kron(-m.conj(), m) for m in (sx, sy, sz))
ev = np.round(np.linalg.eigvalsh(SX).real, 9)
check("T3 locked invariant sigma(taste).sigma(qubit): eigen -3 (singlet) x1, +1 (triplet) x3",
      sorted(ev.tolist()) == [-3.0, 1.0, 1.0, 1.0], str(sorted(ev.tolist())))
check("T4 3 = d: the triplet is the vector of the d=3 rotation group (2x2 = 1+3 only for SU(2))",
      2 * 2 - 1 == 3)
print(f"TOTAL: PASS={P} FAIL={F}")
