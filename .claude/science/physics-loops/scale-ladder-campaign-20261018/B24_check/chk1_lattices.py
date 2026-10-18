#!/usr/bin/env python3
"""B24_check part 1: independent lattice classification (claims 1 and 2 of the B24 check request).
Independent of b24base/b24lib/b23lib/chklib/chk_model: the PSG affine action is taken from B7_check/chk_core.py
(own GF(2) gauge, brute-force PSG), and is itself re-verified on a symmetric Bloch Hamiltonian built from that gauge.
Lattice enumeration: Hermite normal forms (not the orbit-closure BFS of B24), exact integer arithmetic.

 (a) chk_core affine action k -> R k + pi R lam_R is a symmetry of H(k) (onsite + link hopping, random t1, t2).
 (b) k* (fixed by all 24 rotations mod 2pi Z^3) exists in chk_core coordinates.
 (c) HNF enumeration of all lattices 2pi Z^3 <= Lam <= (pi/4) Z^3 invariant under O: count, types (sc/fcc/bcc), scales.
 (d) Per lattice, with the full AFFINE action: number of commuting-C2-pair-fixed classes, T-fixed classes, bad classes.
 (e) For every N = 1..16: all O-invariant lattices 2pi Z^3 <= Lam <= (2pi/N) Z^3 (this is every invariant lattice with
     |Lam/2piZ^3| | N^3, hence covers non-dyadic scales) are sc/fcc/bcc, and none has all C2-pair classes T-fixed
     (linear action around k*).
 (f) scale-free witnesses: exact Fractions, little group identified (D4 / D2), contains no C3.
"""
import sys, os, itertools, time
from fractions import Fraction as Fr
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B7_check'))
import chk_core as cc
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

ROT = [cc.OH[g] for g in cc.PROPER]
LAMR = [cc.OH[g] @ cc.LAM[g] for g in cc.PROPER]           # c_R = pi * R lam (mod 2pi)

# ---- (a) verify the affine action on a symmetric Hamiltonian built from chk_core's gauge
rng = np.random.default_rng(5)
t1, t2 = rng.normal(), rng.normal()
h = {}
for (i1, i2, s), e in cc.ETYPES.items():
    amp = (-1.0) ** int(cc.u[e]) * (t1 if s == (0, 0, 0) else t2)
    # edge corner i1 at 0 -- corner i2 at s ; H = sum |v+d><v| h_d
    h.setdefault(tuple(s), np.zeros((12, 12)))[i2, i1] += amp
    h.setdefault(tuple(-x for x in s), np.zeros((12, 12)))[i1, i2] += amp
ks = rng.uniform(-np.pi, np.pi, (5, 3))
ok = True
for g in cc.PROPER:
    for k in ks:
        H1 = cc.Hk(h, k)[0]; k2 = cc.fibre_image(g, k); H2 = cc.Hk(h, k2)[0]
        U = cc.UF[g]
        # G Bloch(k) = Bloch(k') U up to the H(k) convention: check spectral + operator covariance either way
        ok &= np.allclose(U @ H1 @ U.T, H2) or np.allclose(U @ H1 @ U.T, cc.Hk(h, cc.OH[g] @ k - np.pi * (cc.OH[g] @ cc.LAM[g]))[0])
check("(a) chk_core PSG: U_g H(k) U_g^T = H(R k + pi R lam_g) for all 24 rotations (random t1,t2,k)", ok)

# ---- units: pi/8 for points (mod 16), lattice in units pi/4 (mod 8) -> point grid is half-lattice-unit
def fixed_by(Rm, cvec, kvec, member, N):
    """kvec, cvec in half-lattice units (mod 2N); fixed iff (R k + c - k) even and /2 in lattice."""
    d = (Rm @ kvec + cvec - kvec) % (2 * N)
    return bool(np.all(d % 2 == 0)) and member(tuple(int(x) // 2 for x in d))

# ---- (b) k*: fixed by all 24 rotations mod 2pi Z^3, on (pi/2) Z^3
kst_list = []
for m in itertools.product(range(4), repeat=3):
    k = np.array(m) * np.pi / 2
    if all(cc.same_k(cc.fibre_image(g, k), k) for g in cc.PROPER): kst_list.append(m)
check("(b) points fixed by all 24 rotations mod 2piZ^3 exist (chk_core coords, units pi/2)", len(kst_list) > 0, f"{kst_list}")
KST = np.array(kst_list[0])

# ---- group bookkeeping
def typ(R): return {3: 'E', -1: 'C2', 0: 'C3', 1: 'C4'}[int(round(np.trace(R)))]
isT = [typ(R) in ('E', 'C3') or (typ(R) == 'C2' and np.all(np.abs(np.diag(R)) == 1)) for R in ROT]
C2 = [i for i, R in enumerate(ROT) if typ(R) == 'C2']
C2P = [(i, j) for i in C2 for j in C2 if i < j and np.array_equal(ROT[i] @ ROT[j], ROT[j] @ ROT[i])]
C3 = [i for i, R in enumerate(ROT) if typ(R) == 'C3']
check("group: |T| = 12, 9 C2, 12 commuting C2 pairs, 8 C3", sum(isT) == 12 and len(C2) == 9 and len(C2P) == 12 and len(C3) == 8)

# ---- HNF enumeration
def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]
def make_member(B):
    d1, a12, a13 = B[0]; _, d2, a23 = B[1]; _, _, d3 = B[2]
    def mem(x):
        x1, x2, x3 = x
        if x1 % d1: return False
        c1 = x1 // d1; y2 = x2 - c1 * a12
        if y2 % d2: return False
        c2 = y2 // d2; y3 = x3 - c1 * a13 - c2 * a23
        return y3 % d3 == 0
    return mem
GENS = [np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]), np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])]   # C4z, C3(111): generate O
def inv_lattices(N):
    out = []
    for d1, d2, d3 in itertools.product(divisors(N), repeat=3):
        for a12 in range(d2):
            for a13 in range(d3):
                for a23 in range(d3):
                    B = [(d1, a12, a13), (0, d2, a23), (0, 0, d3)]; mem = make_member(B)
                    if not all(mem(tuple(N * np.eye(3, dtype=int)[i])) for i in range(3)): continue
                    if all(mem(tuple(int(x) for x in G @ np.array(b))) for G in GENS for b in B): out.append((B, mem))
    return out
def lat_type(B, mem, N):
    idx = B[0][0] * B[1][1] * B[2][2]
    m = min(s for s in range(1, N + 1) if mem((s, 0, 0)))
    if idx == m ** 3: return ('sc', Fr(m, N))                 # scale a in units of 2pi
    if m % 2 == 0 and idx * 4 == m ** 3 and mem((m // 2, m // 2, 0)): return ('fcc', Fr(m, 2 * N))
    if m % 2 == 0 and idx * 2 == m ** 3 and mem((m // 2, m // 2, m // 2)): return ('bcc', Fr(m, N))
    return ('OTHER', Fr(m, N))

def counts(B, mem, N, affine):
    """classes mod Lam of C2-pair-fixed and T-fixed points; points on (pi/N)Z^3 (half lattice unit); affine uses chk_core c_R."""
    if affine:
        assert (2 * N) % 2 == 0
        cs = [(N * lr) % (2 * N) for lr in LAMR]            # pi R lam in units pi/N
    else:
        cs = [np.zeros(3, int)] * 24
    pts = np.array(list(itertools.product(range(2 * N), repeat=3)))
    # vectorised: for each R, which points fixed
    def memv(D):        # D: (n,3) ints (lattice units) -> bool array
        return np.array([mem(tuple(int(x) for x in d)) for d in D])
    FIX = np.zeros((24, len(pts)), bool)
    for i, (R, c) in enumerate(zip(ROT, cs)):
        D = (pts @ R.T + c - pts) % (2 * N); ev = np.all(D % 2 == 0, axis=1)
        sub = np.where(ev)[0]; FIX[i, sub] = memv(D[sub] // 2)
    pair = np.zeros(len(pts), bool)
    for i, j in C2P: pair |= FIX[i] & FIX[j]
    Tf = np.all(FIX[np.array(isT)], axis=0)
    c3f = np.zeros(len(pts), bool)
    for i in C3: c3f |= FIX[i]
    size = N ** 3 // (B[0][0] * B[1][1] * B[2][2])           # |Lam / 2pi Z^3|
    npair, nT = int(pair.sum()), int(Tf.sum()); nbad = int((pair & ~Tf).sum())
    assert npair % size == 0 and nT % size == 0 and nbad % size == 0
    # check: is T-fixed implied by C2-pair-fixed + some C3?  (consistency)
    return npair // size, nT // size, nbad // size, size, int((pair & ~Tf & c3f).sum())

# ---- (c), (d) dyadic case N = 8 (units pi/4)
N = 8
L8 = inv_lattices(N)
typs = [lat_type(B, mem, N) for B, mem in L8]
names = sorted([f"{t}({str(2 * a)}pi)" for t, a in typs])
check("(c) exactly 10 O-invariant lattices with 2piZ^3 <= Lam <= (pi/4)Z^3 (HNF enumeration)", len(L8) == 10, f"{len(L8)}: {names}")
exp_types = {('sc', Fr(1)), ('sc', Fr(1, 2)), ('sc', Fr(1, 4)), ('sc', Fr(1, 8)), ('fcc', Fr(1, 2)), ('fcc', Fr(1, 4)), ('fcc', Fr(1, 8)),
             ('bcc', Fr(1)), ('bcc', Fr(1, 2)), ('bcc', Fr(1, 4))}
check("(c) they are sc at 2pi, pi, pi/2, pi/4; fcc at pi, pi/2, pi/4; bcc at 2pi, pi, pi/2 (NOT bcc at pi/4: needs (pi/8)(1,1,1))",
      set(typs) == exp_types and ('bcc', Fr(1, 8)) not in set(typs))
res = {}
for (B, mem), tp in zip(L8, typs):
    a = counts(B, mem, N, affine=True); b = counts(B, mem, N, affine=False)
    res[tp] = (a, b)
    print(f"   {tp[0]}(a={str(2 * tp[1])}pi) |Lam/2piZ3|={a[3]:3d}  affine: C2pair={a[0]:2d} T={a[1]:2d} bad={a[2]:2d}   linear-around-k*: C2pair={b[0]:2d} T={b[1]:2d} bad={b[2]:2d}  bad-with-a-C3={a[4]}")
check("(d) affine (chk_core c_R) and linear-around-k* counts agree for every lattice (k* fixed => counts are pure lattice data)",
      all(a[:4] == b[:4] for a, b in res.values()))
bad = {t: {(v[0][0], v[0][2]) for k_, v in res.items() if k_[0] == t} for t in ('sc', 'fcc', 'bcc')}
print("   (C2-pair classes, bad classes) by type:", bad)
check("(d) no lattice has all C2-pair classes T-fixed", all(v[0][2] > 0 for v in res.values()))
check("(d) bad/C2-pair counts: sc 6/8, fcc 6/10, bcc 9/10 at every scale in the range", bad == {'sc': {(8, 6)}, 'fcc': {(10, 6)}, 'bcc': {(10, 9)}})
check("(d) no bad point is fixed by any C3 (bad points have little group without C3)", all(v[0][4] == 0 for v in res.values()))

# ---- (e) all N = 1..16 (non-dyadic scales included), linear action around k*
allok = True; summary = {}
for N in range(1, 17):
    LN = inv_lattices(N)
    for B, mem in LN:
        tp = lat_type(B, mem, N)
        if tp[0] == 'OTHER': allok = False
        c = counts(B, mem, N, affine=False)
        if c[2] == 0: allok = False
        summary.setdefault(tp[0], set()).add((c[0], c[2]))
    print(f"   N={N:2d}: {len(LN)} invariant lattices: {sorted(set(lat_type(B, m, N)[0] + '(' + str(2 * lat_type(B, m, N)[1]) + 'pi)' for B, m in LN))}", flush=True)
check("(e) N = 1..16: every O-invariant lattice between 2piZ^3 and (2pi/N)Z^3 is sc, fcc or bcc and has >= 1 bad class",
      allok, f"(C2-pair, bad) by type over all scales: {summary}")

# ---- (f) scale-free witnesses with exact Fractions, little groups
def member_a(kind, x):
    if kind == 'sc': return all(v.denominator == 1 for v in x)
    if kind == 'fcc': return all(v.denominator == 1 for v in x) and sum(x) % 2 == 0
    if kind == 'bcc': return all(v.denominator == 1 for v in x) or all((v - Fr(1, 2)).denominator == 1 for v in x)
W = {'sc': (Fr(1, 2), Fr(0), Fr(0)), 'fcc': (Fr(0), Fr(1, 2), Fr(1, 2)), 'bcc': (Fr(0), Fr(0), Fr(1, 2))}
lg = {}
for kind, q in W.items():
    fix = [i for i, R in enumerate(ROT) if member_a(kind, [sum(int(R[r, s]) * q[s] for s in range(3)) - q[r] for r in range(3)])]
    ty = sorted(typ(ROT[i]) for i in fix)
    lg[kind] = (len(fix), ty.count('C4'), ty.count('C3'), ty.count('C2'), [p for p in C2P if p[0] in fix and p[1] in fix] != [])
print("   witness little groups (order, #C4, #C3, #C2, has commuting C2 pair):", lg)
check("(f) witnesses: sc (a/2)e_x -> D4 (order 8, 2 C4), fcc (a/2)(0,1,1) -> D2 (order 4, 3 C2), bcc (a/2)e_z -> D4; no C3; commuting C2 pair present",
      lg['sc'][:3] == (8, 2, 0) and lg['bcc'][:3] == (8, 2, 0) and lg['fcc'][:4] == (4, 0, 0, 3) and all(v[4] for v in lg.values()))
# fcc type check: (a/2)(0,1,1) is in the lattice?  (should not be a lattice vector, else it is Gamma-equivalent)
check("(f) witnesses are not lattice vectors (not equivalent to k* itself)", all(not member_a(kd, list(q)) for kd, q in W.items()))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
