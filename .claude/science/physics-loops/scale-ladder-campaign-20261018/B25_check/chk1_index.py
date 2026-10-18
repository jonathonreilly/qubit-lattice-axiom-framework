#!/usr/bin/env python3
"""B25_check part 1: the lattice side of the index lemma, independently.
 (a) enumerate ALL O-invariant subgroups of (pi/8)Z^3 / 2piZ^3 = Z_16^3 from scratch (orbit-generated subgroups closed
     under joins; no sc/fcc/bcc formula assumed), then name them;
 (b) all nested pairs: strict count, index, exponent of the quotient, whether O acts trivially ((R-1)L' in L);
 (c) goodness  C2pair(mod L_u) within Tfix(mod L_sp)  for the linear action around k*, on the FINER (pi/64)Z^3 grid
     (B25 used (pi/32)); own membership tables;
 (d) scale-free version: for L' in {sc, fcc, bcc} at unit scale, M(L') = span{(R-1)v} and every O-invariant L with
     M(L') <= L <= L' (exactly the lattices with trivial O action on L'/L), via exact integer Hermite reduction;
 (e) exact rational witnesses that (sc(a), bcc(a)) and (fcc(b), sc(b)) are bad at every scale a, b;
 (f) k* is fixed (mod 2pi) by all 24 affine PSG rotations of the independent chk_core build (justifies the linear action).
Prints PASS/FAIL, TOTAL."""
import sys, os, itertools, collections, time
from fractions import Fraction as Fr
import numpy as np
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROT.append(M)
assert len(ROT) == 24
# ---------------- (a) subgroups of Z_16^3 (unit pi/8; 2pi = 16)
Nn = 16
ALLV = np.array(list(itertools.product(range(Nn), repeat=3)))
def idx(v): v = np.asarray(v) % Nn; return (v[..., 0] * Nn + v[..., 1]) * Nn + v[..., 2]
def gen_subgroup(gens):
    S = np.zeros(Nn ** 3, bool); S[0] = True
    for g in gens:
        g = np.asarray(g) % Nn
        if S[idx(g)]: continue
        cur = ALLV[S]
        for n in range(1, Nn):
            S[idx(cur + n * g)] = True
    return S
orbit_gen = {}
for v in ALLV:
    key = tuple(sorted({tuple((R @ v) % Nn) for R in ROT}))
    if key not in orbit_gen: orbit_gen[key] = gen_subgroup(list(key))
subs = {}
for S in orbit_gen.values(): subs[S.tobytes()] = S
def join(A, B):
    S = A.copy()
    for g in ALLV[B & ~A]:
        if S[idx(g)]: continue
        cur = ALLV[S]
        for n in range(1, Nn): S[idx(cur + n * g)] = True
    return S
changed = True
while changed:
    changed = False; items = list(subs.values())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            Jn = join(items[i], items[j]); kb = Jn.tobytes()
            if kb not in subs: subs[kb] = Jn; changed = True
LATT = list(subs.values())
# every one is O-invariant by construction (joins of orbit-generated groups); verify
assert all(all(S[idx(ALLV[S] @ R.T)].all() for R in ROT) for S in LATT)
def name(S):
    def has(v): return bool(S[idx(v)])
    for a in (1, 2, 4, 8, 16):                    # unit pi/8: a=16 is 2pi
        sc = {tuple(v) for v in ALLV if all(c % a == 0 for c in v)}
        fcc = {tuple(v) for v in ALLV if all(c % a == 0 for c in v) and (sum(c // a for c in v)) % 2 == 0} if a < 16 else None
        bcc = (sc | {tuple(v) for v in ALLV if all((c - a // 2) % a == 0 for c in v)}) if a % 2 == 0 else None
        Sset = {tuple(v) for v in ALLV[S]}
        if Sset == sc: return f"sc({a})"
        if fcc is not None and Sset == fcc: return f"fcc({a})"
        if bcc is not None and Sset == bcc: return f"bcc({a})"
    return f"?{S.sum()}"
NAMES = {name(S): S for S in LATT}
print("   O-invariant subgroups of (pi/8)Z^3/2piZ^3 (unit pi/8):", sorted(NAMES, key=lambda n: -NAMES[n].sum()))
# lattices containing 2piZ^3 = subgroups here; but 'fcc(16)' (= fcc at 2pi) does not contain 2piZ^3 and cannot appear.
check("(a) exactly 13 O-invariant lattices 2piZ^3 <= L <= (pi/8)Z^3: sc(2pi..pi/8), fcc(pi..pi/8), bcc(2pi..pi/4)",
      len(LATT) == 13 and not any(n.startswith('?') for n in NAMES), f"{len(LATT)}")
# ---------------- (b) nested pairs
def triv(Lu, Ls):
    V = ALLV[Ls]; return all(Lu[idx(V @ R.T - V)].all() for R in ROT)
def exp2(Lu, Ls): return Lu[idx(2 * ALLV[Ls])].all()
rows = []
for nu, Lu in NAMES.items():
    for ns, Ls in NAMES.items():
        if (Lu & ~Ls).any(): continue
        rows.append((nu, ns, int(Ls.sum() // Lu.sum()), exp2(Lu, Ls), triv(Lu, Ls)))
strict = [r for r in rows if r[0] != r[1]]
adm = [r for r in strict if r[4]]
print("   strictly nested:", len(strict), "; O-trivial strict:", [(r[0], r[1], r[2]) for r in adm])
check("(b) 74 strictly nested pairs; the O-trivial ones are exactly (sc(a),bcc(a)) a=2pi..pi/4 and (fcc(b),sc(b)) b=pi..pi/8 (8 pairs, index 2)",
      len(strict) == 74 and {(r[0], r[1]) for r in adm} == {(f"sc({a})", f"bcc({a})") for a in (16, 8, 4, 2)} | {(f"fcc({b})", f"sc({b})") for b in (8, 4, 2, 1)}
      and all(r[2] == 2 for r in adm))
check("(b) every O-trivial pair has elementary-abelian quotient of order <= 4 (so the Klein-group bound is never the binding constraint)",
      all(r[3] and r[2] <= 4 for r in adm))
others = [r for r in strict if not r[4] and r[2] <= 4]
print("   index <= 4 but NON-trivial O action:", [(r[0], r[1], r[2], 'exp2' if r[3] else 'Z4') for r in others])
# ---------------- (c) goodness on the (pi/64) grid: unit pi/64, 2pi = 128; lattice unit pi/8 = 8 grid units
G = 128
grid = np.array(list(itertools.product(range(G), repeat=3)), dtype=np.int32)
tr = [int(np.trace(R)) for R in ROT]
isT = [t in (3, 0) or (t == -1 and np.all(np.abs(np.diag(R)) == 1)) for R, t in zip(ROT, tr)]
C2 = [i for i, t in enumerate(tr) if t == -1]
C2P = [(i, j) for i in C2 for j in C2 if i < j and np.array_equal(ROT[i] @ ROT[j], ROT[j] @ ROT[i])]
check("(c) 12 commuting C2 pairs in O; T = {E, 8 C3, 3 coordinate C2}", len(C2P) == 12 and sum(isT) == 12)
def fixed(S, R):
    d = (grid @ R.T - grid) % G
    ok = np.all(d % 8 == 0, axis=1)
    out = np.zeros(len(grid), bool); out[ok] = S[idx(d[ok] // 8)]
    return out
C2SET, TSET = {}, {}
for n, S in NAMES.items():
    F = [fixed(S, R) for R in ROT]
    c = np.zeros(len(grid), bool)
    for i, j in C2P: c |= F[i] & F[j]
    C2SET[n] = c; TSET[n] = np.all([F[i] for i in range(24) if isT[i]], axis=0)
good = {(r[0], r[1]): int((C2SET[r[0]] & ~TSET[r[1]]).sum()) == 0 for r in rows}
ng = sum(good[(r[0], r[1])] for r in strict)
sub10 = [r for r in strict if all(x not in ('sc(1)', 'fcc(1)', 'bcc(2)') for x in r[:2])]
check("(c) good pairs on the (pi/64) grid: 56 of 74 strict pairs (29 of the 42 pairs of the 10 lattices down to pi/4); no (L, L) pair is good",
      ng == 56 and sum(good[(r[0], r[1])] for r in sub10) == 29 and len(sub10) == 42 and not any(good[(n, n)] for n in NAMES), f"{ng}, {sum(good[(r[0], r[1])] for r in sub10)}/{len(sub10)}")
check("(c) all 8 O-trivial strict pairs (and all 13 (L,L)) are bad: the index lemma's pair list contains no good pair", not any(good[(r[0], r[1])] for r in adm))
check("(c) every good pair has a non-trivial O action on L_sp/L_u (so it needs a taste outside Lambda_ind)", all(not r[4] for r in strict if good[(r[0], r[1])]))
# ---------------- (d) scale-free O-trivial extensions (integer coordinates, unit = half the scale)
def hnf_rows(vs):
    """integer echelon row-basis of the Z-span of integer 3-vectors vs (own Euclid reduction, exact)"""
    A = [list(map(int, v)) for v in vs if any(v)]; B = []
    for col in range(3):
        while True:
            nz = [r for r in A if r[col] != 0]
            if len(nz) <= 1: break
            nz.sort(key=lambda r: abs(r[col])); p = nz[0]
            A = [r for r in A if r[col] == 0] + [p] + [[x - (r[col] // p[col]) * y for x, y in zip(r, p)] for r in nz[1:]]
            A = [r for r in A if any(r)]
        nz = [r for r in A if r[col] != 0]
        if nz: B.append(nz[0]); A = [r for r in A if r is not nz[0]]
    return B
def in_span(B, v):
    v = list(v)
    for r in B:
        col = next(i for i in range(3) if r[i] != 0)
        if v[col] % r[col] != 0: return False
        q = v[col] // r[col]; v = [x - q * y for x, y in zip(v, r)]
    return not any(v)
BASE = {'sc': [(2, 0, 0), (0, 2, 0), (0, 0, 2)], 'fcc': [(2, 2, 0), (2, 0, 2), (0, 2, 2)], 'bcc': [(2, 0, 0), (0, 2, 0), (1, 1, 1)]}
def lat_of(kind): return hnf_rows(BASE[kind])
def lat_eq(A, B): return all(in_span(A, v) for v in B) and all(in_span(B, v) for v in A)
res_d = {}
for kind, gens in BASE.items():
    Mv = [tuple(int(x) for x in (R - np.eye(3, dtype=int)) @ np.array(g)) for R in ROT for g in gens]
    Mb = hnf_rows(Mv)
    # O-invariant lattices between M and L': enumerate cosets of L'/M (finite) and test all subgroups generated by unions of O-orbits
    Lp = hnf_rows(gens)
    box = [tuple(v) for v in itertools.product(range(-2, 3), repeat=3) if in_span(Lp, v)]
    reps = []
    for v in box:
        if not any(in_span(Mb, tuple(a - b for a, b in zip(v, r))) for r in reps): reps.append(v)
    found = []
    for mask in range(1 << len(reps)):
        L = hnf_rows([r for i, r in enumerate(reps) if mask >> i & 1] + [tuple(r) for r in Mb])
        if all(in_span(L, tuple(int(x) for x in R @ np.array(r))) for R in ROT for r in L) and not any(lat_eq(L, F) for F in found): found.append(L)
    names_ = [nk for F in found for nk in BASE if lat_eq(F, lat_of(nk))]
    res_d[kind] = (len(reps), sorted(names_), len(found))
print("   scale-free O-trivial sublattices L <= L' (unit scale):", res_d)
check("(d) scale-free: [L' : M(L')] and the O-invariant L with trivial action on L'/L are sc' -> {fcc, sc}, bcc -> {sc, bcc}, fcc -> {fcc}",
      res_d['sc'][1] == ['fcc', 'sc'] and res_d['bcc'][1] == ['bcc', 'sc'] and res_d['fcc'][1] == ['fcc'] and all(r[1].__len__() == r[2] for r in res_d.values()))
# ---------------- (e) exact witnesses at unit scale (exact rationals; the condition is invariant under q -> s q, L -> s L)
def member(kind, a, v):
    x = [Fr(c) / a for c in v]
    integ = all(t.denominator == 1 for t in x)
    if kind == 'sc': return integ
    if kind == 'fcc': return integ and sum(x) % 2 == 0
    return integ or all((t - Fr(1, 2)).denominator == 1 for t in x)
def Rv(R, v): return [sum(int(R[i, j]) * v[j] for j in range(3)) for i in range(3)]
def c2pair(kind, a, q): return any(all(member(kind, a, [x - y for x, y in zip(Rv(ROT[i], q), q)]) for i in (i_, j_)) for i_, j_ in C2P)
def tfix(kind, a, q): return all(member(kind, a, [x - y for x, y in zip(Rv(ROT[i], q), q)]) for i in range(24) if isT[i])
a = Fr(1)
w1 = [Fr(0), Fr(0), a / 2]; w2 = [Fr(0), a / 2, a / 2]
check("(e) exact witnesses at every scale: q = (a/2)e_z is C2-pair-fixed mod sc(a) and not T-fixed mod bcc(a); q = (b/2)(0,1,1) is C2-pair-fixed mod fcc(b), not T-fixed mod sc(b)",
      c2pair('sc', a, w1) and not tfix('bcc', a, w1) and c2pair('fcc', a, w2) and not tfix('sc', a, w2))
# ---------------- (f) k* fixed by the affine PSG action of the independent build
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'B7_check'))
import chk_core as cc
ksts = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)]
fixed_by_all = [k for k in ksts if all(cc.same_k(cc.fibre_image(g, k), k) for g in cc.PROPER)]
check("(f) chk_core build: some cube point (+-pi/2)^3 is fixed mod 2pi by all 24 affine rotations k -> Rk + pi R lam (linear action around k*)",
      len(fixed_by_all) > 0, f"{len(fixed_by_all)} of 8: {[tuple(np.round(k/np.pi, 2)) for k in fixed_by_all]}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
