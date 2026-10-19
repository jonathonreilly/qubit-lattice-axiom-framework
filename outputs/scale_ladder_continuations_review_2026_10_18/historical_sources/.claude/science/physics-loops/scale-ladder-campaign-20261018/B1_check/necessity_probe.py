#!/usr/bin/env python3
"""Independent check of item 6 (B1).  Own Bloch construction from a cell gauge;
imports only the PSG module's combinatorial definitions (corners, rotations,
gf2_solve, psg_sign) for the torus symmetry check."""
import itertools, os, sys
import numpy as np
import sympy as sp
from scipy.linalg import expm
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), *[os.pardir] * 5))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as M
C = M._run_reviewed_program(definitions_only=True)
rng = np.random.default_rng(12345)
s3 = np.sqrt(3)

# ======================= (b) corner step, own cell gauge and Bloch matrices
print("== (b) corner step")
DIRS = C['DIRS']; CORN = C['CORNERS']; CI = {c: i for i, c in enumerate(CORN)}
neg = lambda d: tuple(-x for x in d); perp = lambda d, e: sum(a*b for a, b in zip(d, e)) == 0 and d != e
Z = (0, 0, 0)
# edge types in the one-site cell: (c1, c2, shift); on-site and link
ET = {}; ETL = []
def addt(c1, c2, sh, kind):
    if (c1, c2, sh) in ET: return
    ET[(c1, c2, sh)] = ET[(c2, c1, neg(sh))] = len(ETL); ETL.append((c1, c2, sh, kind))
for c in CORN:
    d, e = tuple(c)
    for a, b in ((d, e), (e, d)):
        for f in DIRS:
            if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a): addt(c, frozenset((a, f)), Z, 'on')
        addt(c, frozenset((neg(a), b)), a, 'link')
print(" cell edge types:", len(ETL), {k: sum(t[3] == k for t in ETL) for k in ('on', 'link')})
add3 = lambda a, b: tuple(x+y for x, y in zip(a, b))
def cyc(seq): return [ET[(c1, c2, tuple(y-x for x, y in zip(p1, p2)))] for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1])]
cyc_all = []
for d in DIRS:   # squares and tubes
    ring = [f for f in DIRS if perp(f, d)]; r0 = ring[0]; r1 = [f for f in ring if perp(f, r0) and f != neg(r0)][0]
    ring = [r0, r1, neg(r0), neg(r1)]
    cyc_all.append((cyc([(frozenset((d, r)), Z) for r in ring]), 1))
    for i in range(4):
        p, q = ring[i], ring[(i+1) % 4]
        cyc_all.append((cyc([(frozenset((d, p)), Z), (frozenset((neg(d), p)), d), (frozenset((neg(d), q)), d), (frozenset((d, q)), Z)]), 1))
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
    cyc_all.append((cyc([(frozenset((x, y)), Z), (frozenset((y, z)), Z), (frozenset((z, x)), Z)]), 0))
plaq = []
for d in DIRS:
    for e in DIRS:
        if perp(d, e):
            cy = cyc([(frozenset((d, e)), Z), (frozenset((neg(d), e)), d), (frozenset((neg(d), neg(e))), add3(d, e)), (frozenset((d, neg(e))), e)])
            cyc_all.append((cy, 1)); plaq.append(cy)
ug = C['gf2_solve']([c for c, _ in cyc_all], [f for _, f in cyc_all], len(ETL))
assert ug is not None
sgn = (-1.0) ** np.array(ug, float)
print(" all 24 link 4-cycles (plaquettes) have flux pi:", all(sum(ug[j] for j in c) % 2 == 1 for c in plaq))
def bloch(kind, t, k):
    H = np.zeros((12, 12), complex)
    for i, (c1, c2, sh, kd) in enumerate(ETL):
        if kd != kind: continue
        a = -t * sgn[i]; ph = np.exp(1j * np.dot(k, sh))
        H[CI[c2], CI[c1]] += a * ph; H[CI[c1], CI[c2]] += a * np.conj(ph)
    return H
HL = lambda k: bloch('link', 1.0, k)
print(" max |H_link(k)^2 - 2| over 500 random k:", max(np.abs(HL(k) @ HL(k) - 2*np.eye(12)).max() for k in rng.uniform(-9, 9, (500, 3))))
print(" diag of H_link(k) zero (trace 0):", np.allclose(np.diag(HL(np.array([.3, .7, -1.1]))), 0))
Hon = bloch('on', 1.0, np.zeros(3)).real
w, V = np.linalg.eigh(Hon); print(" on-site hopping eigenvalues:", np.round(w, 4))
P2 = V[:, np.abs(w - 2) < 1e-8]; Uc = np.eye(12) - 2 * P2 @ P2.T
Wk = lambda k: HL(k) / np.sqrt(2) @ Uc
kst = np.pi / 2 * np.array([1, -1, 1])

from scipy.linalg import expm
def eig_doublet_speeds(Hf):
    e0=np.linalg.eigvalsh(Hf(kst)); out=[]
    i=0
    while i<12:
        j=i
        while j+1<12 and e0[j+1]-e0[i]<1e-8: j+=1
        if j-i+1==2:
            sp_=0
            for d in rng.normal(size=(6,3)):
                d/=np.linalg.norm(d); e=np.linalg.eigvalsh(Hf(kst+1e-4*d)); sp_=max(sp_,(e[j]-e[i])/2e-4)
            out.append(round(sp_,5))
        i=j+1
    return out
Hl=HL; Ho=Hon
cands={'i[HL,Ho]':lambda k:1j*(Hl(k)@Ho-Ho@Hl(k)), 'i[HL,Ho^2]':lambda k:1j*(Hl(k)@Ho@Ho-Ho@Ho@Hl(k)),
 'i(HL Ho HL Ho^2 - hc)':lambda k:(lambda A:1j*(A-A.conj().T))(Hl(k)@Ho@Hl(k)@Ho@Ho),
 'i(HL Ho Ho2? HL Ho - hc)':lambda k:(lambda A:1j*(A-A.conj().T))(Hl(k)@Ho@Ho@Hl(k)@Ho),
 'i(HL Ho HL Ho Ho HL - hc)':lambda k:(lambda A:1j*(A-A.conj().T))(Hl(k)@Ho@Hl(k)@Ho@Ho@Hl(k))}
for nm,K in cands.items():
    Hf=lambda k,K=K: bloch('on',-1.0,k)+bloch('link',0.2,k)+0.1*K(k)
    print(nm, 'isolated Hamiltonian doublet speeds at k*:', eig_doublet_speeds(Hf))
