#!/usr/bin/env python3
"""The Spin(10) pair square on one mirror 16 with two spin components (32 modes, 2^32 states): exact spectrum.

Supplied model: one site (cell) carrying c_{A,s}, A in the Spin(10) Weyl 16, s = up/down, and H = g(Omega + Omega^dag),
Omega = sum_a B_a B_a, B_a = sum M_a[A,B] c_{A,up} c_{B,dn}, M_a = (C gamma_a)|16 (main-branch convention).
 A  Fock-level identities: vector pairs, charge 4, one-body stabiliser, so(12) closure, Fock norms.
 B  exact so(12) x SU(2) content of the 2^32 Fock space (characters: Newton identities + Klimyk, integer arithmetic).
 C  Gelfand-Tsetlin formulas (checked on o_3..o_8) and their so(12) consistency checks.
 D  H = g[J,[J,C_so(11)]], J = (16-N)/2, on every block: ground state, gap, symmetry, exact characteristic polynomials.
 E  estimates: single-site Green function, second-order bond energy, hopping threshold, Floquet ceiling.
 F  against measurement.
Labels: [T] theorem / exact finite computation, [E] estimate, [M] comparison with measurement.  Finite diagnostic of a
supplied model; no physical identification."""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/SPIN10_PAIR_SQUARE_GIVES_UNIQUE_GAPPED_SYMMETRIC_MIRROR_CELL_GROUND_STATE_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from fractions import Fraction as Fr
from math import comb
import numpy as np
import scipy.sparse as sps
import sympy as sp

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

# ================================================================ A. Fock level
print('== A. Fock-level identities (32 modes, bit-level states)')
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1]).astype(complex); I2 = np.eye(2)
def kron(*a):
    out = np.array([[1.0 + 0j]])
    for m in a: out = np.kron(out, m)
    return out
gam = []
for k in range(5):
    gam.append(kron(*([I2] * k + [X] + [Z] * (4 - k)))); gam.append(kron(*([I2] * k + [Y] + [Z] * (4 - k))))
plus = [i for i in range(32) if kron(*([Z] * 5))[i, i].real > 0]
M = [(kron(Y, X, Y, X, Y) @ g)[np.ix_(plus, plus)] for g in gam]
tg = {(a, b): 0.5j * (gam[a] @ gam[b])[np.ix_(plus, plus)] for a in range(10) for b in range(a + 1, 10)}
vec_ok = all(np.allclose(tg[(a, b)].T @ M[c] + M[c] @ tg[(a, b)], 1j * ((a == c) * M[b] - (b == c) * M[a])) for (a, b) in tg for c in range(10))
gram = np.array([[np.trace(M[a] @ M[b].conj().T) for b in range(10)] for a in range(10)])
def cre(k, st):
    if (st >> k) & 1: return None, 0
    return st | (1 << k), (-1) ** bin(st & ((1 << k) - 1)).count('1')
def ann(k, st):
    if not (st >> k) & 1: return None, 0
    return st ^ (1 << k), (-1) ** bin(st & ((1 << k) - 1)).count('1')
NZ = [[(al, be, np.conj(M[a][al, be])) for al in range(16) for be in range(16) if abs(M[a][al, be]) > 1e-12] for a in range(10)]
def Bdag(a, vec):
    out = {}
    for st, amp in vec.items():
        for al, be, c in NZ[a]:
            s1, g1 = cre(al, st)
            if s1 is None: continue
            s2, g2 = cre(16 + be, s1)
            if s2 is None: continue
            out[s2] = out.get(s2, 0) + amp * c * g1 * g2
    return out
def Omdag(vec):
    out = {}
    for a in range(10):
        for k, v in Bdag(a, Bdag(a, vec)).items(): out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if abs(v) > 1e-12}
nrm2 = lambda v: float(sum(abs(x) ** 2 for x in v.values()))
v1 = Omdag({0: 1.0}); v2 = Omdag(v1); f1 = Omdag({1 << 3: 1.0}); f2 = Omdag(f1)
fock = (nrm2(v1), nrm2(v2), nrm2(f1), nrm2(f2))
check('A1 [T] M_a symmetric and unitary, t^T M_c + M_c t = i(d_ac M_b - d_bc M_a): B_a is a Spin(10) vector and SU(2) singlet; '
      'Tr M_a M_b^dag = 16 d_ab gives [B_a, B_a^dag] = 16 - N; Omega lowers N by 4, so its phase is removable and only Z4 of N survives',
      all(np.allclose(m, m.T) and np.allclose(m @ m.conj().T, np.eye(16)) for m in M) and vec_ok and np.allclose(gram, 16 * np.eye(10)),
      f'|Omega^dag|0>| has {len(v1)} terms')
R_, C_, V_, rows = [], [], [], {}
for i in range(32):
    for j in range(32):
        for st, amp in v1.items():
            s1, g1 = ann(j, st)
            if s1 is None: continue
            s2, g2 = cre(i, s1)
            if s2 is None: continue
            R_.append(rows.setdefault(s2, len(rows))); C_.append(32 * i + j); V_.append(amp * g1 * g2)
Am = sps.csr_matrix((V_, (R_, C_)), shape=(len(rows), 1024)); evs = np.linalg.eigvalsh((Am.conj().T @ Am).toarray())
stab = int(np.sum(evs < 1e-8 * evs.max()))
# Nambu form of ad on span{c, c^dag}: pairs Q = c^T A c / 2 -> [[0, A], [0, 0]], Q^dag -> [[0, 0], [-A*, 0]]
def nambu(Mm):
    A = np.zeros((32, 32), complex); A[:16, 16:] = Mm; A[16:, :16] = -Mm.T
    P = np.zeros((64, 64), complex); P[:32, 32:] = A
    Pd = np.zeros((64, 64), complex); Pd[32:, :32] = -A.conj(); return P, Pd
gens = [x for Mm in M for x in nambu(Mm)]
basis = []
def add(Xm):
    v = Xm.ravel().copy()
    for b in basis: v -= np.vdot(b, v) * b
    nv = np.linalg.norm(v)
    if nv > 1e-8: basis.append(v / nv); return True
    return False
for g_ in gens: add(g_)
front = list(gens)
while front:
    new = []
    for Xm in front:
        for Ym in gens:
            Zm = Xm @ Ym - Ym @ Xm
            if add(Zm): new.append(Zm)
    front = new
P0, P0d = nambu(M[0]); comm = P0 @ P0d - P0d @ P0
adJ = np.diag([0.5] * 32 + [-0.5] * 32)                       # ad of J = (16 - N)/2 on (c, c^dag)
check('A2 [T] the one-body (number-conserving) stabiliser of Omega in gl(32) has dimension 48 = so(10) + sl(2): no flavour '
      'symmetry beyond Spin(10) x SU(2)_spin and no U(1)_N; the pairs '
      'B_a, B_a^dag close on a 66-dim algebra (so(12)) in which [B_a, B_a^dag] = 2J has J-spectrum +-1/2 on (c, c^dag)',
      stab == 48 and len(basis) == 66 and np.allclose(comm, 2 * adJ), f'stabiliser {stab}, closure {len(basis)}')

# ================================================================ B. so(12) x SU(2) content
print('== B. exact so(12) x SU(2)_spin content of the Fock space')
n6 = 6; RHO2 = tuple(2 * (n6 - 1 - i) for i in range(n6))
W32 = [v for v in itertools.product((1, -1), repeat=n6) if sum(1 for x in v if x < 0) % 2 == 0]
def dom(nu):
    a = [abs(x) for x in nu]
    if len(set(a)) < n6: return 0, None
    order = sorted(range(n6), key=lambda i: -a[i]); sgn = 1; seen = [False] * n6
    for i in range(n6):
        if seen[i]: continue
        j = i; L = 0
        while not seen[j]: seen[j] = True; j = order[j]; L += 1
        if L % 2 == 0: sgn = -sgn
    mu = [a[i] for i in order]
    if sum(1 for x in nu if x < 0) % 2 == 1 and mu[-1] != 0: mu[-1] = -mu[-1]
    return sgn, tuple(mu)
def times_adams(rep, i):
    out = {}
    for lam, m in rep.items():
        base = tuple(l + r for l, r in zip(lam, RHO2))
        for v in W32:
            s, mu = dom(tuple(b + i * x for b, x in zip(base, v)))
            if s: hw = tuple(x - r for x, r in zip(mu, RHO2)); out[hw] = out.get(hw, 0) + s * m
    return {k: v for k, v in out.items() if v}
def dimD(hw, n):
    rho = [Fr(n - 1 - i) for i in range(n)]; l = [h + r for h, r in zip(hw, rho)]; num = den = Fr(1)
    for i in range(n):
        for j in range(i + 1, n): num *= (l[i] - l[j]) * (l[i] + l[j]); den *= (rho[i] - rho[j]) * (rho[i] + rho[j])
    return int(num / den)
E = [{(0,) * n6: 1}]; dims_ok = True
for r in range(1, 17):
    acc = {}
    for i in range(1, r + 1):
        for k, v in times_adams(E[r - i], i).items(): acc[k] = acc.get(k, 0) + (-1) ** (i - 1) * v
    assert all(v % r == 0 for v in acc.values()); E.append({k: v // r for k, v in acc.items() if v})
    dims_ok &= sum(m * dimD(tuple(Fr(x, 2) for x in k), 6) for k, m in E[r].items()) == comb(32, r)
irr = {}; mult1 = True
for r in range(17):
    om = dict(E[r])
    if r >= 2:
        for k, v in E[r - 2].items(): om[k] = om.get(k, 0) - v
    for k, m in om.items():
        if m == 0: continue
        mult1 &= (m == 1) and k not in irr; irr[k] = Fr(16 - r, 2)        # irrep (doubled hw) -> spin j
tot = sum(int(2 * j + 1) * dimD(tuple(Fr(x, 2) for x in k), 6) for k, j in irr.items())
STAR = (16, 0, 0, 0, 0, 0)
check('B1 [T] under so(12) x SU(2)_spin the 2^32 Fock space is a sum of 63 irreducibles, each so(12) irrep occurring once and '
      'with one spin: H, a polynomial in so(12), can only be degenerate inside one so(12) irrep (times 2j+1)',
      dims_ok and mult1 and tot == 2 ** 32 and len(irr) == 63, f'{len(irr)} irreps, sum (2j+1) dim = 2^32')
check('B2 [T] |0> and |F> lie in L* = (8,0,0,0,0,0) (dim 63206, spin 0, once); the so(12) singlets are the 17 fully '
      'spin-polarised states (spin 8), so the ground state need not and does not lie in an so(12) singlet',
      irr.get(STAR) == 0 and dimD(tuple(Fr(x, 2) for x in STAR), 6) == 63206 and irr.get((0,) * 6) == 8)

# ================================================================ C. Gelfand-Tsetlin
print('== C. Gelfand-Tsetlin coefficients for o_N > o_{N-1}')
def lval(row, r):
    if r % 2 == 1: k = (r - 1) // 2; return [row[i] + k - i for i in range(k)]
    k = r // 2; return [row[i] + k - (i + 1) for i in range(k)]
def coefA2(l_lo, l_mid, l_hi, j):
    lj = l_mid[j]; num = Fr(1)
    for x in l_lo + l_hi: num *= (x - lj - 1) * (x + lj)
    den = Fr(1)
    for i, x in enumerate(l_mid):
        if i != j: den *= (x * x - lj * lj) * (x * x - (lj + 1) ** 2)
    return num / den / 4
def coefB2(l_lo, l_mid, l_hi, j):
    lj = l_mid[j]; num = Fr(1)
    for x in l_lo + l_hi: num *= (x * x - lj * lj)
    den = lj * lj * (4 * lj * lj - 1)
    for i, x in enumerate(l_mid):
        if i != j: den *= (x * x - lj * lj) * ((x - 1) ** 2 - lj * lj)
    return num / den
def coefC(l_lo, l_mid, l_hi):
    num = Fr(1)
    for x in l_lo + l_hi: num *= x
    if num == 0: return Fr(0)
    den = Fr(1)
    for x in l_mid: den *= x * (x - 1)
    return num / den
def rng(lo, hi): return [lo + t for t in range(int(hi - lo) + 1)] if hi >= lo else []
def below(row, r):
    if r % 2 == 0: k = r // 2; return list(itertools.product(*[rng(row[i + 1] if i < k - 2 else abs(row[k - 1]), row[i]) for i in range(k - 1)]))
    k = (r - 1) // 2; return list(itertools.product(*[rng(row[i + 1] if i < k - 1 else -row[k - 1], row[i]) for i in range(k)]))
def gt_rep(top, N):
    pats = [[tuple(top)]]
    for r in range(N, 2, -1): pats = [p + [b] for p in pats for b in below(p[-1], r)]
    pats = [tuple(p) for p in pats]; idx = {p: i for i, p in enumerate(pats)}; D = len(pats); F = {}
    for r in range(2, N + 1):
        Mx = np.zeros((D, D), complex)
        for p in pats:
            rows_ = {N - t: p[t] for t in range(len(p))}; a = idx[p]
            if r % 2 == 1:
                k = (r - 1) // 2; t = N - 2 * k
                for j in range(k):
                    q = list(p); rw = list(q[t]); rw[j] += 1; q[t] = tuple(rw); q = tuple(q)
                    if q in idx:
                        c = float(coefA2(lval(rows_[2 * k - 1], 2 * k - 1) if k > 1 else [], lval(rows_[2 * k], 2 * k), lval(rows_[2 * k + 1], 2 * k + 1), j)) ** 0.5
                        Mx[idx[q], a] += c; Mx[a, idx[q]] -= c
            else:
                k = (r - 2) // 2; t = N - (2 * k + 1); llo = lval(rows_[2 * k], 2 * k) if k >= 1 else []
                lhi = lval(rows_[2 * k + 2], 2 * k + 2)
                if k >= 1:
                    for j in range(k):
                        q = list(p); rw = list(q[t]); rw[j] += 1; q[t] = tuple(rw); q = tuple(q)
                        if q in idx:
                            c = float(coefB2(llo, lval(rows_[2 * k + 1], 2 * k + 1), lhi, j)) ** 0.5
                            Mx[idx[q], a] += c; Mx[a, idx[q]] -= c
                Mx[a, a] += 1j * float(coefC(llo, lval(rows_[2 * k + 1], 2 * k + 1) if k >= 1 else [], lhi))
        F[r] = Mx
    return F, D
cm = lambda A_, B_: A_ @ B_ - B_ @ A_
gt_err = 0.0
for N, top in [(3, (1,)), (4, (2, -1)), (4, (Fr(3, 2), Fr(1, 2))), (5, (2, 1)), (5, (Fr(3, 2), Fr(1, 2))), (6, (2, 1, -1)),
               (6, (Fr(3, 2), Fr(1, 2), Fr(-1, 2))), (7, (1, 1, 0)), (7, (Fr(3, 2), Fr(1, 2), Fr(1, 2))), (8, (2, 1, 1, 0)),
               (8, (Fr(3, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2)))]:
    top = tuple(Fr(x) for x in top); F, D = gt_rep(top, N); Fij = {(r, r - 1): F[r] for r in range(2, N + 1)}
    for r in range(2, N + 1):
        for s_ in range(r + 2, N + 1): gt_err = max(gt_err, np.abs(cm(F[r], F[s_])).max())
        if r < N: gt_err = max(gt_err, np.abs(cm(F[r], cm(F[r], F[r + 1])) + F[r + 1]).max(), np.abs(cm(F[r + 1], cm(F[r + 1], F[r])) + F[r]).max())
    for gp in range(2, N):
        for a in range(gp + 1, N + 1): Fij[(a, a - gp)] = cm(Fij[(a, a - 1)], Fij[(a - 1, a - gp)])
    n_ = N // 2; rho = [n_ - i - 1 for i in range(n_)] if N % 2 == 0 else [n_ - i - 0.5 for i in range(n_)]
    cexp = sum(float(l) * (float(l) + 2 * r_) for l, r_ in zip(top, rho))
    gt_err = max(gt_err, np.abs(sum(Fij[k] @ Fij[k] for k in Fij) + cexp * np.eye(D)).max())

def block(L, la):
    """GT multiplicity space of the so(10) irrep la in the so(12) irrep L: J = L_{11,12} and C_so(11) (diagonal)."""
    ms = [m for m in itertools.product(*[rng(L[i + 1] if i < 4 else abs(L[5]), L[i]) for i in range(5)])
          if all(m[i] >= la[i] >= (m[i + 1] if i < 4 else -m[4]) for i in range(5))]
    idx = {m: i for i, m in enumerate(ms)}; d = len(ms); J = np.zeros((d, d), complex); l12 = lval(L, 12); l10 = lval(la, 10)
    for m in ms:
        a = idx[m]; l11 = lval(m, 11)
        for j in range(5):
            mp = list(m); mp[j] += 1; mp = tuple(mp)
            if mp in idx: c = float(coefB2(l10, l11, l12, j)) ** 0.5; J[idx[mp], a] += -1j * c; J[a, idx[mp]] += 1j * c
        J[a, a] += float(coefC(l10, l11, l12))
    return ms, J, np.array([float(sum(x * (x + Fr(11 - 2 * (i + 1))) for i, x in enumerate(m))) for m in ms])
def blocks(L):
    groups = {}
    for m in itertools.product(*[rng(L[i + 1] if i < 4 else abs(L[5]), L[i]) for i in range(5)]):
        for la in itertools.product(*[rng(m[i + 1] if i < 4 else -m[4], m[i]) for i in range(5)]): groups[la] = 1
    return list(groups)
levels = []; chk = [0.0, 0.0, 0.0]; maxblk = 0; dim_ok = True; bnds = []
for k2, j in irr.items():
    L = tuple(Fr(x, 2) for x in k2); trJ2 = 0.0; dsum = 0
    for la in blocks(L):
        ms, J, Dg = block(L, la); maxblk = max(maxblk, len(ms)); qe, qv = np.linalg.eigh(J)
        chk[0] = max(chk[0], np.abs(2 * qe - np.round(2 * qe)).max())
        R2 = qv @ np.diag(np.exp(1j * np.pi * qe)) @ qv.conj().T; chk[1] = max(chk[1], np.abs(R2 * Dg[None, :] - Dg[:, None] * R2).max())
        dl = dimD(la, 5); trJ2 += dl * np.trace(J @ J).real; dsum += dl * len(ms)
        if not (k2 == STAR and all(v == 0 for v in la)):         # block-wise Casimir lower bound on h = H/2g
            bnds.append((-(max(sum(x * (x + 11 - 2 * (i + 1)) for i, x in enumerate(m)) for m in ms)
                           - sum(x * (x + 10 - 2 * (i + 1)) for i, x in enumerate(la))), j.denominator == 2))
        hq = qv.conj().T @ (0.5 * (J @ J * Dg[None, :] - 2 * (J * Dg[None, :]) @ J + Dg[:, None] * (J @ J))) @ qv
        cls = [int(round(2 * q)) % 4 for q in qe]                 # e^{i pi J} classes: N = 16 - 2J mod 4
        for c_ in set(cls):
            sel = [i for i in range(len(qe)) if cls[i] == c_]
            for e in np.linalg.eigvalsh(hq[np.ix_(sel, sel)]):
                levels.append((2 * e, k2, la, dl * int(2 * j + 1), (16 - c_) % 4, j))
    c12 = float(sum(x * (x + 2 * (5 - i)) for i, x in enumerate(L)))
    chk[2] = max(chk[2], abs(trJ2 - dimD(L, 6) * c12 / 66) / (dimD(L, 6) * c12 / 66 + 1))
    dim_ok &= dsum == dimD(L, 6)
check('C1 [T] Gelfand-Tsetlin coefficients: o_3..o_8 (11 irreps, spinorial and both signs) satisfy the consecutive-generator '
      'relations and give Casimir <L, L+2 rho>; on all 63 so(12) irreps 2J is integral, e^{i pi J} commutes with C_so(11), and '
      'Tr J^2 = dim C_so(12)/66; the blocks exhaust each irrep', dim_ok and gt_err < 1e-9 and chk[0] < 1e-9 and chk[1] < 1e-9 and chk[2] < 1e-9,
      f'errors {gt_err:.0e}, {chk[0]:.0e}, {chk[1]:.0e}, {chk[2]:.0e}; largest block {maxblk}')

# ================================================================ D. spectrum
print('== D. H = g(Omega + Omega^dag) = 2g sum_p (L_{p,11}^2 - L_{p,12}^2) = g [J,[J,C_so(11)]]')
levels.sort(key=lambda t: t[0]); E0 = levels[0][0]
agg = []
for e, k2, la, d, nm4, j in levels:
    if agg and abs(e - agg[-1][0]) < 1e-7: agg[-1][1] += d; agg[-1][2].add((tuple(float(x) / 2 for x in k2), tuple(str(x) for x in la), nm4, str(j)))
    else: agg.append([e, d, {(tuple(float(x) / 2 for x in k2), tuple(str(x) for x in la), nm4, str(j))}])
gs = agg[0]; (gL, gla, gnm, gj), = gs[2]
Delta = agg[1][0] - E0; Dfer = min(e for e, k2, la, d, nm4, j in levels if j.denominator == 2) - E0
lam = sp.symbols('lambda')
def exact_block(L, la):
    ms = [m for m in itertools.product(*[rng(L[i + 1] if i < 4 else abs(L[5]), L[i]) for i in range(5)])
          if all(m[i] >= la[i] >= (m[i + 1] if i < 4 else -m[4]) for i in range(5))]
    idx = {m: i for i, m in enumerate(ms)}; d = len(ms); J = sp.zeros(d, d); l12 = lval(L, 12); l10 = lval(la, 10)
    for m in ms:
        a = idx[m]; l11 = lval(m, 11)
        for j in range(5):
            mp = list(m); mp[j] += 1; mp = tuple(mp)
            if mp in idx:
                b2 = coefB2(l10, l11, l12, j); c = sp.sqrt(sp.Rational(b2.numerator, b2.denominator))
                J[idx[mp], a] += -sp.I * c; J[a, idx[mp]] += sp.I * c
        cc = coefC(l10, l11, l12); J[a, a] += sp.Rational(cc.numerator, cc.denominator)
    Dm = sp.diag(*[sp.Rational(*(lambda q: (q.numerator, q.denominator))(sum(x * (x + Fr(11 - 2 * (i + 1))) for i, x in enumerate(m)))) for m in ms])
    Hg = J * J * Dm - 2 * J * Dm * J + Dm * J * J                # = H/g
    return sp.Poly(sp.expand((lam * sp.eye(d) - Hg).det(method='berkowitz')), lam)
def chain_poly(beta2):
    p_prev, p = sp.Poly(1, lam), sp.Poly(lam, lam)
    for b2 in beta2: p_prev, p = p, sp.Poly(lam, lam) * p - b2 * p_prev
    return p
Ls = (Fr(8), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)); Lf = (Fr(15, 2),) + (Fr(1, 2),) * 4 + (Fr(-1, 2),)
P0 = exact_block(Ls, (Fr(0),) * 5); P1 = exact_block(Ls, (Fr(1),) + (Fr(0),) * 4); Pf = exact_block(Lf, (Fr(1, 2),) * 4 + (Fr(-1, 2),))
Q0 = chain_poly([16 * k * (9 - k) * (k + 4) * (13 - k) for k in range(1, 9)])
Q1 = chain_poly([16 * k * (8 - k) * (k + 5) * (13 - k) for k in range(1, 8)])
Qf = chain_poly([16 * k * (8 - k) * (k + 4) * (13 - k) for k in range(1, 8)])
# polynomial model: so(10)-invariant harmonic polynomials of degree 8 on R^12, F(s = |x_1..10|^2, x = x11, y = x12)
s_, x_, y_ = sp.symbols('s x y')
mons = [s_ ** a * x_ ** b * y_ ** (8 - 2 * a - b) for a in range(5) for b in range(8 - 2 * a + 1)]
cs = sp.symbols('c0:%d' % len(mons)); Fp = sum(c * m for c, m in zip(cs, mons))
lap = sp.Poly(sp.expand(4 * s_ * sp.diff(Fp, s_, 2) + 20 * sp.diff(Fp, s_) + sp.diff(Fp, x_, 2) + sp.diff(Fp, y_, 2)), s_, x_, y_).coeffs()
sol = list(sp.linsolve(lap, cs))[0]; free = sorted(set().union(*[sp.sympify(e).free_symbols for e in sol]), key=lambda c: cs.index(c))
hb = [sp.expand(sum(sp.sympify(v).subs({f: int(f == fs) for f in free}) * m for v, m in zip(sol, mons))) for fs in free]
def Aop(F_, xa):
    G_ = sp.diff(F_, xa) - 2 * xa * sp.diff(F_, s_); return sp.expand(s_ * sp.diff(G_, xa) - 10 * xa * G_ - 2 * s_ * xa * sp.diff(G_, s_))
cvec = lambda P_: sp.Matrix([sp.Poly(P_, s_, x_, y_).coeff_monomial(m) for m in mons])
Bm = sp.Matrix.hstack(*[cvec(b) for b in hb]); Hp = sp.zeros(len(hb), len(hb))
poly_res = 0
for i, b in enumerate(hb):
    hv = cvec(sp.expand(-2 * (Aop(b, x_) - Aop(b, y_)))); Hp[:, i] = (Bm.T * Bm).inv() * Bm.T * hv
    poly_res += sum(abs(v) for v in (Bm * Hp[:, i] - hv))       # H maps the harmonic singlet space into itself
Ppoly = sp.Poly((lam * sp.eye(len(hb)) - Hp).det(method='berkowitz'), lam)
e0_exact = -2 * sp.sqrt(11088 + 48 * sp.sqrt(21081))
def lanczos(L, la):
    ms, J, Dg = block(L, la); qe, qv = np.linalg.eigh(J); o = np.argsort(-qe); qv = qv[:, o]
    hq = qv.conj().T @ (J @ J * Dg[None, :] - 2 * (J * Dg[None, :]) @ J + Dg[:, None] * (J @ J)) @ qv
    return np.array([abs(hq[k, k + 1]) for k in range(len(qe) - 1)]) ** 2, np.abs(np.diag(hq)).max()
chains = [(Ls, (Fr(0),) * 5, [16 * k * (9 - k) * (k + 4) * (13 - k) for k in range(1, 9)]),
          (Ls, (Fr(1),) + (Fr(0),) * 4, [16 * k * (8 - k) * (k + 5) * (13 - k) for k in range(1, 8)]),
          (Ls, (Fr(2),) + (Fr(0),) * 4, [16 * k * (7 - k) * (k + 6) * (13 - k) for k in range(1, 7)]),
          (Lf, (Fr(1, 2),) * 4 + (Fr(-1, 2),), [16 * k * (8 - k) * (k + 4) * (13 - k) for k in range(1, 8)])]
chain_err = max(max(np.abs(lanczos(L, la)[0] - np.array(b, float)).max() / max(b), lanczos(L, la)[1]) for L, la, b in chains)
same = lambda Pa, Pb: sp.expand(Pa.as_expr() - Pb.as_expr()) == 0
h0 = float(e0_exact) / 2; bmin = min(b for b, f in bnds); bfer = min(b for b, f in bnds if f)
check('D0 [T] Casimir localisation: on the so(10) block la of irrep L, H/2g >= -(C_so(11)\' - C_so(10)) >= -(max c11(mu) - c10(la)); '
      'over every block except the Spin(10) singlet of L* this bound is >= %s (the 10 of L*), above E0/2g = %.3f: the ground state '
      'lies in that 9-dim block (solved exactly in D1), and from Casimirs alone Delta >= %.2f g, Delta_f >= %.2f g'
      % (bmin, h0, 2 * (float(bmin) - h0), 2 * (float(bfer) - h0)), float(bmin) > h0)
check('D1 [T] ground state unique: the minimum over all 63 irreps is a simple level of L* in its Spin(10)-singlet block, '
      'E0 = -2g sqrt(11088 + 48 sqrt 21081); that block is the 9-state Jacobi chain beta_k^2 = 16k(9-k)(k+4)(13-k), and the '
      'exact Gelfand-Tsetlin, harmonic-polynomial and chain characteristic polynomials agree',
      gs[1] == 1 and gL == (8.0, 0.0, 0.0, 0.0, 0.0, 0.0) and gla == ('0',) * 5 and gj == '0' and same(P0, Q0) and same(Q0, Ppoly) and poly_res == 0
      and abs(float(e0_exact) - E0) < 1e-9 and sp.expand(P0.as_expr().subs(lam, e0_exact)) == 0 and chain_err < 1e-9,
      f'E0/g = {E0:.6f}; Lanczos-vs-formula err {chain_err:.0e}; P0 = {sp.factor(P0.as_expr())}')
gap_chain = sorted(np.real(np.roots([float(c) for c in Q1.all_coeffs()])))[0] - E0
ferm_chain = sorted(np.real(np.roots([float(c) for c in Qf.all_coeffs()])))[0] - E0
check('D2 [T] gap Delta = %.4f g to the Spin(10) 10 (spin 0, N = 2 mod 4, 10 states; chain 16k(8-k)(k+5)(13-k)); fermion gap '
      '%.4f g (64 states: 16 + 16bar, spin 1/2, chain 16k(8-k)(k+4)(13-k)); 54: chain 16k(7-k)(k+6)(13-k)' % (Delta, Dfer),
      agg[1][1] == 10 and same(P1, Q1) and same(Pf, Qf) and abs(gap_chain - Delta) < 1e-7 and abs(ferm_chain - Dfer) < 1e-7
      and agg[2][1] == 64 and abs(agg[2][0] - E0 - Dfer) < 1e-9,
      'next: ' + '; '.join('%.3f g x%d' % (a[0] - E0, a[1]) for a in agg[3:6]))
pred = (7680, 7680 * 14784, 6720, 6720 * 12672)
check('D3 [T] the so(12) chains are the Fock chains: ||Om^dag|0>||^2, ||Om^dag^2|0>||^2, ||Om^dag c^dag|0>||^2, '
      '||Om^dag^2 c^dag|0>||^2 = beta_1^2, beta_1^2 beta_2^2 of the two chains (normalisation fixed, |beta| = 1)',
      all(abs(a - b) < 1e-6 * b for a, b in zip(fock, pred)), 'Fock ' + ', '.join('%.0f' % x for x in fock))
b0 = np.sqrt([16 * k * (9 - k) * (k + 4) * (13 - k) for k in range(1, 9)]); T0m = np.diag(b0, 1) + np.diag(b0, -1)
ew, ev = np.linalg.eigh(T0m); gsv = ev[:, 0]; PN = gsv ** 2
check('D4 [T] symmetric: Spin(10) singlet, spin singlet, N in {0,4,...,32} so Z4 = +1 and fermion parity even; <N> = 16, '
      '<c^dag_a c_b> = d_ab/2 (Spin(10) x SU(2) irreducible on the 32 modes), all pair and vector expectations zero',
      gnm == 0 and abs(sum(4 * k * PN[k] for k in range(9)) - 16) < 1e-9 and np.allclose(PN, PN[::-1]),
      'P(N=0,4,..,16) = ' + ', '.join('%.4f' % p for p in PN[:5]))
c10 = lambda la: float(sum(x * (x + 2 * (4 - i)) for i, x in enumerate(la)))
lv1 = sorted(e + c10(la) for e, k2, la, d, nm4, j in levels); gapC = min(e for e in lv1 if e > lv1[0] + 1e-7) - lv1[0]
check('D5 [T] main-branch atom: its singlet (|0> + e^{i phi}|F>)/sqrt2 lies in L* with overlap <= 2 P(N=0) = %.1e with this '
      'ground state; both carry trivial Spin(10) x SU(2) x Z4 charges (one 0D class); its Casimir term lam C_Spin(10) leaves E0 '
      'and raises the 10 by 9 lam; Q, C_2 and number projections are not needed' % (2 * PN[0]),
      2 * PN[0] < 1e-2 and abs(lv1[0] - E0) < 1e-9 and abs(gapC - Delta - 9) < 1e-9, 'gap with lam = g: %.4f g' % gapC)
print('   lowest (E-E0)/g x deg (so(12); so(10)): ' + '; '.join(
    '%.3f x%d (%s; %s)' % (a[0] - E0, a[1], ','.join('%g' % v for v in sorted(a[2])[0][0]), ','.join(sorted(a[2])[0][1])) for a in agg[:4]))

# ================================================================ E. estimates
print('== E. one site with hopping t: strong-coupling estimates')
nf = np.concatenate([[1.0], np.cumprod(np.array([16 * k * (8 - k) * (k + 4) * (13 - k) for k in range(1, 8)], float))])
n0 = np.concatenate([[1.0], np.cumprod(b0 ** 2)])
bf = np.sqrt([16 * k * (8 - k) * (k + 4) * (13 - k) for k in range(1, 8)]); Tf = np.diag(bf, 1) + np.diag(bf, -1)
ef, vf = np.linalg.eigh(Tf); amp = vf.T @ (gsv[:8] * np.sqrt(nf / n0[:8])); Aw = amp ** 2; epf = ef - E0
kappa = 64 * sum(Aw[i] * Aw[j] / (epf[i] + epf[j]) for i in range(8) for j in range(8))
check('E1 [T/E] c^dag|GS> lies %.4f%% in the lowest fermion level (weights sum to 1/2; alpha_k^2 = 1 - k/8 exactly), so the site '
      'Green function is z/(z^2 - Delta_f^2) up to %.0e: a zero at z = 0, as in the main-branch atom; second-order bond energy '
      '%.4f t^2/g (bound 8/Delta_f = %.4f)' % (200 * Aw[0], 1 - 2 * Aw[0], kappa, 8 / Dfer),
      abs(Aw.sum() - 0.5) < 1e-9 and np.allclose(nf / n0[:8], 1 - np.arange(8) / 8) and kappa <= 8 / Dfer + 1e-12)
tc2 = np.sqrt(Delta / (6 * kappa)); tc1 = Dfer / (6 * 2 * Aw[0]); width = -2 * E0; ceil_ = 2 * np.pi / width
check('E2 [E] cubic lattice (z = 6), hopping t c^dag_i c_j on all 32 modes: the gapped symmetric phase persists for t < t_* > 0 '
      '(stability of a unique gapped product state, cited); second-order estimate z kappa t_c^2 = Delta gives t_c = %.2f g, '
      'the first-order fermion band Delta_f = z t gives %.2f g; as a per-tick term the site spectrum (width %.1f g) needs '
      'g tau < %.4f' % (tc2, tc1, width, ceil_), 3 < tc2 < tc1 < 6 and ceil_ < 0.012)

# ================================================================ F. measurement
print('== F. against measurement')
eps_hi = ceil_ * tc2 * np.sqrt(3)
check('F1 [E/M] with the tick hop t = eps/(sqrt3 tau) (= 1/(2a) at c = 1, block 2a), the window eps/(%.2f sqrt3) < g tau < %.4f is open for eps < '
      '%.3f, containing the register bound eps < 0.04; the mirror fermion mass Delta_f = %.1f g > %.1f/a, ~1e19 GeV for a of a '
      'few Planck lengths, vs LHC limits near 1.5 TeV on extra quarks and leptons; the singlet ground state breaks no gauge '
      'symmetry' % (tc2, ceil_, eps_hi, Dfer, Dfer / (2 * tc2)), eps_hi > 0.04 and Dfer / (2 * tc2) > 1)
print('theorems: A1-A2, B1-B2, C1, D0-D5 (exact finite; uniqueness needs only D0 + the exact singlet block).')
print('estimates: E1-E2, F1.  cited: gap stability for weak hopping, 0D classification by symmetry charges, anomaly reason for')
print('  breaking U(1)_N to Z4, LHC limits.  supplied: the mirror content (16 x 2 per cell), the pair-square term alone, g,')
print('  the hopping model (z = 6, mode-diagonal), t = eps/(sqrt3 tau), the lattice spacing.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
