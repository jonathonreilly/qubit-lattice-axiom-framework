#!/usr/bin/env python3
"""Can a NON-ABELIAN gauge group come from composite registers of one-qubit sites without being named?
Supplied models; exact finite checks plus finite enumerations; no physical identification.

A. Census of composite cubic clusters (site blocks of side b = 2..7): orbit irreps under the 24 rotations O,
   bond-end mode counts and their C4v content; largest Schur-forced multiplet dimensions.
B. The generic cubic-covariant cluster rule at b = 5 (inner 6-orbit as composite matter, 3x3 face ends as
   link-end registers): per-cluster gauge algebra = commutant of every cluster-local, cluster-number-conserving
   piece. Cases: on-cluster only; + matter-end pieces; + end-end (plaquette) pieces; proper-O complex pieces;
   and a control with an internal 2-copy label per site (atomic, bends the Qubit axiom).
C. Fock registers Lambda(+ C^d_i) of Schur multiplets d_i in {1,2,3} (single-valued) or {1,2,3,4} (spinor lift):
   even sector (arrow-selected chiral half), group prod SU(d_i) x U(1)_X (X = 2N - n, number conservation).
   Anomalies, mass protection (invariants in Sym^2), non-abelian charge; smallest passing n; least-information
   split (fewest distinct one-body frequencies = largest one-body commutant).
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/COMPOSITE_CUBIC_CLUSTERS_ALLOW_ONLY_SU2_SU3_SCHUR_FACTORS_GENERIC_COVARIANT_UPDATE_LEAVES_ABELIAN_GAUGE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import os, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np

T0 = time.time()
RNG = np.random.default_rng(20261022)
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------------------------------------------------------- groups
OH = []
for perm in itertools.permutations(range(3)):
    for s in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = s[i]
        OH.append(M)
O = [g for g in OH if round(np.linalg.det(g)) == 1]

def oclass(g):
    t = int(np.trace(g))
    if (g == np.eye(3, dtype=int)).all(): return 0
    if (g == np.diag(np.diag(g))).all(): return 1      # C2 about a face axis
    return {1: 2, 0: 3, -1: 4}[t]                       # C4, C3, C2'
CHI_O = {'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, -1, 1, -1], 'E': [2, 2, 0, -1, 0],
         'T1': [3, -1, 1, 0, -1], 'T2': [3, -1, -1, 0, 1]}
STAB_X = [g for g in OH if (g[:, 0] == [1, 0, 0]).all()]
def c4vclass(g):
    R = g[1:, 1:]
    if (R == np.eye(2, dtype=int)).all(): return 0
    if (R == -np.eye(2, dtype=int)).all(): return 1
    if round(np.linalg.det(R)) == 1: return 2
    return 3 if (R == np.diag(np.diag(R))).all() else 4
CHI_C4V = {'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, 1, -1, -1], 'B1': [1, 1, -1, 1, -1],
           'B2': [1, 1, -1, -1, 1], 'E': [2, -2, 0, 0, 0]}

def decompose(points, group, cls, table):
    pts = [tuple(p) for p in points]; idx = {p: i for i, p in enumerate(pts)}
    mult = {}
    for name, ch in table.items():
        s = 0
        for g in group:
            fixed = sum(1 for p in pts if tuple(g @ np.array(p)) == p)
            s += fixed * ch[cls(g)]
        mult[name] = s // len(group)
        assert s % len(group) == 0
    return {k: v for k, v in mult.items() if v}

print("A. composite cubic clusters: orbits, bond ends, Schur dimensions")
cs = [sum(1 for g in O if oclass(g) == k) for k in range(5)]
orth = all(sum(cs[k] * CHI_O[a][k] * CHI_O[b][k] for k in range(5)) == 24 * (a == b) for a in CHI_O for b in CHI_O)
check("A1 |O_h| = 48, |O| = 24, O character table orthonormal; |Stab(+x)| = 8 (C4v)",
      len(OH) == 48 and len(O) == 24 and orth and len(STAB_X) == 8, f"class sizes {cs}")
dims_O = sorted(CHI_O[k][0] for k in CHI_O); dims_C4v = sorted(CHI_C4V[k][0] for k in CHI_C4V)
spin_extra = [2, 2, 4]
check("A2 largest irreps: O {1,1,2,3,3} (max 3), C4v max 2; binary octahedral adds {2,2,4}: 48 = sum d^2",
      max(dims_O) == 3 and max(dims_C4v) == 2 and sum(d * d for d in dims_O + spin_extra) == 48,
      "Schur-forced simple factors: SU(2), SU(3); SU(4) only with a spinor lift")
half = [np.array(v) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
d6 = decompose(half, O, oclass, CHI_O)
check("A3 six half-links of a site = A1 + E + T1 (reproduces time-complex-structure S1)", d6 == {'A1': 1, 'E': 1, 'T1': 1}, str(d6))

census = []; allA1once = True; firstE = None; first2 = None
for b in range(2, 8):
    vals = list(range(-(b - 1), b, 2))                  # doubled coordinates
    pts = [np.array(p) for p in itertools.product(vals, repeat=3)]
    seen = set(); orbits = []
    for p in pts:
        if tuple(p) in seen: continue
        orb = {tuple(g @ p) for g in O}; seen |= orb; orbits.append(sorted(orb))
    for orb in orbits:
        dec = decompose([np.array(q) for q in orb], O, oclass, CHI_O)
        allA1once &= dec.get('A1', 0) == 1
    end = [p for p in pts if p[0] > abs(p[1]) and p[0] > abs(p[2])]
    dec_end = decompose(end, STAB_X, c4vclass, CHI_C4V) if end else {}
    nE = dec_end.get('E', 0)
    census.append((b, len(orbits), len(end), nE))
    if nE and firstE is None: firstE = b
    if len(end) >= 2 and first2 is None: first2 = b
print("   b: orbits, sites per bond end (Voronoi), E copies per end = " +
      "; ".join(f"b{b}:{o},{n},{e}" for b, o, n, e in census))
check("A4 every O-orbit of sites carries A1 exactly once (transitive permutation rep), b = 2..7",
      allA1once, "so no cubic cell carries E+T1 alone; the A1 must be removed (gapped) by the rule")
check("A5 first block with >= 2 sites per bond end is b = 4; first with a C4v doublet E at an end is b = 4",
      first2 == 4 and firstE == 4, f"b=3 has 1 site per end (abelian link only); b=5 has 10 sites, 2 E's")
check("A6 state count never binds: 2N-state SU(2)/SU(3) links need 4/6 states, b>=4 ends give 2^8 >= 256",
      2 ** (2 * census[2][2]) >= 6, "the binding requirement is a Schur-protected degeneracy, not a count")

# ---------------------------------------------------------------- B. cluster commutant
print("B. per-cluster gauge algebra of the generic covariant rule at b = 5")
M_sites = [tuple(v) for v in half]
ends = {}
for e in M_sites:
    ax = int(np.nonzero(e)[0][0]); sg = e[ax]; oth = [i for i in range(3) if i != ax]
    L = []
    for u, v in itertools.product([-1, 0, 1], repeat=2):
        p = [0, 0, 0]; p[ax] = 2 * sg; p[oth[0]] = u; p[oth[1]] = v; L.append(tuple(p))
    ends[e] = L
SITES = M_sites + [p for e in M_sites for p in ends[e]]
IDX = {p: i for i, p in enumerate(SITES)}; NS = len(SITES)
def rho(g):
    P = np.zeros((NS, NS))
    for p, i in IDX.items(): P[IDX[tuple(g @ np.array(p))], i] = 1
    return P
RHO = {id(g): rho(g) for g in OH}
def avg(R, group):
    return sum(RHO[id(g)] @ R @ RHO[id(g)].T for g in group) / len(group)
def rand_on(support, cplx=False):
    R = np.zeros((NS, NS), complex if cplx else float); ii = [IDX[p] for p in support]
    A = RNG.normal(size=(len(ii), len(ii)))
    if cplx: A = A + 1j * RNG.normal(size=A.shape)
    A = A + A.conj().T; R[np.ix_(ii, ii)] = A; return R
def pieces(group, cplx, with_P1=True, with_P2=True, copies=2, no_mm=False):
    out = []
    for _ in range(copies):
        out.append(avg(rand_on(M_sites, cplx), group))
        if with_P1:
            st = [g for g in group if tuple(g @ np.array((1, 0, 0))) == (1, 0, 0)]
            P = avg(rand_on(M_sites + ends[(1, 0, 0)], cplx), st)
            if no_mm: P[:6, :6] = 0                    # pairing + end-local only, no direction-dependent matter term
            for e in M_sites:
                g = next(g for g in group if tuple(g @ np.array((1, 0, 0))) == e)
                out.append(RHO[id(g)] @ P @ RHO[id(g)].T)
        if with_P2:
            pair = {(1, 0, 0), (0, 1, 0)}
            st = [g for g in group if {tuple(g @ np.array(q)) for q in pair} == pair]
            P = avg(rand_on(ends[(1, 0, 0)] + ends[(0, 1, 0)], cplx), st)
            done = set()
            for g in group:
                im = frozenset(tuple(g @ np.array(q)) for q in pair)
                if im in done: continue
                done.add(im); out.append(RHO[id(g)] @ P @ RHO[id(g)].T)
    return out

def commutant(pcs, n):
    pcs = [p[:n, :n] for p in pcs]
    A = sum(RNG.normal() * p for p in pcs)
    w, V = np.linalg.eigh(A)
    blocks = []; cur = [0]
    for k in range(1, n):
        if abs(w[k] - w[k - 1]) < 1e-7 * (1 + abs(w).max()): cur.append(k)
        else: blocks.append(cur); cur = [k]
    blocks.append(cur)
    tests = [V.conj().T @ (sum(RNG.normal() * p for p in pcs)) @ V for _ in range(2)]
    basis = [(a, c) for Bk in blocks for a in Bk for c in Bk]
    m = len(basis); G = np.zeros((m, m), complex)
    for T in tests:                                   # Gram of the linear map X -> [X, T], in column chunks
        for s0 in range(0, m, 64):
            ch = basis[s0:s0 + 64]; Mc = np.zeros((n * n, len(ch)), complex)
            for k, (a, c) in enumerate(ch):
                Z = np.zeros((n, n), complex); Z[a, :] += T[c, :]; Z[:, c] -= T[:, a]; Mc[:, k] = Z.ravel()
            for t0 in range(0, m, 64):
                ch2 = basis[t0:t0 + 64]; Mc2 = np.zeros((n * n, len(ch2)), complex)
                for k, (a, c) in enumerate(ch2):
                    Z = np.zeros((n, n), complex); Z[a, :] += T[c, :]; Z[:, c] -= T[:, a]; Mc2[:, k] = Z.ravel()
                G[s0:s0 + len(ch), t0:t0 + len(ch2)] += Mc.conj().T @ Mc2
    ev, U = np.linalg.eigh(G)
    null = U[:, ev < 1e-10 * max(1.0, ev.max())].T
    Xs = []
    for v in null:
        X = np.zeros((n, n), complex)
        for coef, (a, c) in zip(v, basis): X[a, c] = coef
        Xs.append(V @ X @ V.conj().T)
    res = max((np.abs(X @ p - p @ X).max() for X in Xs for p in pcs), default=0.0)
    Dd = len(Xs); Gc = np.zeros((Dd, Dd), complex)   # centre = span elements commuting with every X_j
    for Xj in Xs:
        Mj = np.array([(Xi @ Xj - Xj @ Xi).ravel() for Xi in Xs]).T
        Gc += Mj.conj().T @ Mj
    evc = np.linalg.eigvalsh(Gc) if Dd else np.array([])
    centre = int(np.sum(evc < 1e-10 * max(1.0, evc.max() if Dd else 1.0)))
    return Dd, Dd - centre, res
def _unit(n, a, c):
    E = np.zeros((n, n), complex); E[a, c] = 1; return E

D, der, res = commutant(pieces(OH, False, False, False), 6)
check("B1 on-cluster only (matter 6-orbit): commutant u(1)+u(2)+u(3), dim 14, derived 11 (Schur A1,E,T1)",
      D == 14 and der == 11 and res < 1e-9, f"dim {D}, derived {der}, residual {res:.1e}")
D2, der2, res2 = commutant(pieces(OH, False, True, False), NS)
check("B2 + C4v-covariant matter-end pieces: per-cluster gauge algebra is ABELIAN",
      der2 == 0 and res2 < 1e-9, f"dim {D2} (all u(1)), derived {der2}, residual {res2:.1e}")
D2b, der2b, res2b = commutant(pieces(OH, False, True, False, no_mm=True), NS)
check("B2b same with the matter-matter part of each end piece removed (only pairings + end-local): abelian",
      der2b == 0 and res2b < 1e-9, f"dim {D2b}, derived {der2b}; T1 and E of the matter are split by the six end pairings")
D3, der3, res3 = commutant(pieces(OH, False, True, True), NS)
check("B3 + end-end (plaquette) pieces: still abelian, and no larger",
      der3 == 0 and D3 <= D2 and res3 < 1e-9, f"dim {D3}, derived {der3}")
D4, der4, res4 = commutant(pieces(O, True, True, True), NS)
check("B4 proper rotations only, complex Hermitian pieces: abelian (C4 has no 2-dim irrep)",
      der4 == 0 and res4 < 1e-9, f"dim {D4}, derived {der4}")
# control: two indistinguishable modes per site (internal copy label = atomic structure)
pc = pieces(OH, False, True, True)
pc2 = [np.kron(p, np.eye(2)) for p in pc]
NS_save = NS
D5, der5, res5 = commutant(pc2, 2 * NS)
check("B5 control: an internal 2-copy label on every site turns each u(1) into u(2) (non-abelian)",
      D5 == 4 * D3 and der5 == 3 * D3 and res5 < 1e-9,
      f"dim {D5}, derived {der5}: non-abelian needs a label no covariant rule can see")

# ---------------------------------------------------------------- C. Fock registers of Schur multiplets
print("C. Fock registers of Schur multiplets: anomalies, mass protection, least information")
def fock_ops(n):
    I2 = np.eye(2); Z = np.diag([1., -1.]); a = np.array([[0., 1.], [0., 0.]])
    cs_ = []
    for i in range(n):
        op = np.array([[1.]])
        for j in range(n): op = np.kron(op, Z if j < i else (a if j == i else I2))
        cs_.append(op)
    return cs_
FOCK = {n: fock_ops(n) for n in range(1, 7)}
def lift(h, n):
    c = FOCK[n]; return sum(h[i, j] * c[i].T @ c[j] for i in range(n) for j in range(n) if h[i, j] != 0)

def analyse(dims):
    n = sum(dims); c = FOCK[n]
    occ = np.array([[(s >> (n - 1 - i)) & 1 for i in range(n)] for s in range(2 ** n)])
    Nn = occ.sum(1); ev = np.nonzero(Nn % 2 == 0)[0]
    off = np.cumsum([0] + list(dims))
    cart, offd, an = [], [], {}
    for b, d in enumerate(dims):
        if d < 2: continue
        o = off[b]
        for k in range(d - 1):
            h = np.zeros((n, n)); h[o + k, o + k] = 1; h[o + k + 1, o + k + 1] = -1; cart.append(np.diag(h))
        for i in range(d):
            for j in range(i + 1, d):
                h = np.zeros((n, n), complex); h[o + i, o + j] = 1; h[o + j, o + i] = 1; offd.append(lift(h, n)[np.ix_(ev, ev)])
                h = np.zeros((n, n), complex); h[o + i, o + j] = -1j; h[o + j, o + i] = 1j; offd.append(lift(h, n)[np.ix_(ev, ev)])
        Hc = np.zeros(n); Hc[o:o + d] = 1; Hc[o + d - 1] = 1 - d          # traceless Cartan
        hw = (occ @ Hc)[ev]
        an[f"SU{d}^3#{b}"] = float(np.sum(hw ** 3)) if d >= 3 else 0.0
        J = np.zeros(n); J[o] = .5; J[o + 1] = -.5
        jw = (occ @ J)[ev]
        if d == 2: an[f"Witten#{b}"] = int(round(2 * np.sum(jw ** 2))) % 2
        an[f"SU{d}^2X#{b}"] = float(np.sum(jw ** 2 * (2 * Nn[ev] - n)))
    X = (2 * Nn - n)[ev].astype(float)
    an["X"] = float(X.sum()); an["X^3"] = float((X ** 3).sum())
    anomaly_free = all(abs(v) < 1e-9 for v in an.values())
    W = np.array([occ[ev] @ cv for cv in cart] + [X]).T if cart else X[:, None]
    charged = any(np.abs(T).max() > 1e-12 for T in offd) or (np.abs(W[:, :-1]).max() > 0 if cart else False)
    R = len(ev); cand = [(a, b) for a in range(R) for b in range(a, R) if np.all(np.abs(W[a] + W[b]) < 1e-9)]
    if not cand: masses = 0
    elif not offd: masses = len(cand)
    else:
        cols = []
        for a, b in cand:
            S = np.zeros((R, R), complex); S[a, b] = S[b, a] = 1
            cols.append(np.concatenate([(T.T @ S + S @ T).ravel() for T in offd]))
        Mx = np.array(cols).T
        sv = np.linalg.svd(Mx, compute_uv=False)
        masses = len(cand) - int(np.sum(sv > 1e-9))
    return anomaly_free, masses, charged, an

def partitions(n, maxpart):
    if n == 0: yield (); return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p): yield (p,) + rest

results = {}
for n in range(1, 7):
    for part in partitions(n, 4):
        if max(part) < 2: continue
        results[part] = analyse(part)
passing = {p: r for p, r in results.items() if r[0] and r[1] == 0 and r[2]}
line = "; ".join(f"{''.join(map(str, p))}:{'A' if r[0] else 'a'}{r[1]}{'c' if r[2] else '-'}" for p, r in results.items())
print("   partition: A=anomaly-free/a=anomalous, #Sym^2 mass invariants, c=non-abelian charged")
print("   " + line)
single = {p: r for p, r in passing.items() if max(p) <= 3}
nmin = min(sum(p) for p in single)
check("C1 even n never protected: empty and filled states (X = -n, +n) pair into an invariant mass",
      all(results[p][1] > 0 for p in results if sum(p) % 2 == 0))
check("C2 n = 3 fails: (3) has SU(3)^3 anomaly (1 + 3bar), (2,1) has one doublet (Witten)",
      not results[(3,)][0] and abs(results[(3,)][3]['SU3^3#0']) > 0 and results[(2, 1)][3]['Witten#0'] == 1)
check("C3 smallest single-valued Schur register passing anomaly-free + protected + non-abelian charged: n = 5",
      nmin == 5, f"passing: {sorted(''.join(map(str, p)) for p in single)}")
n5 = [p for p in partitions(5, 3) if max(p) >= 2]
check("C4 at n = 5 EVERY split with parts <= 3 passes (all sit in U(5) acting on the 16): not selected by anomalies",
      all(p in single for p in n5), f"{len(n5)} splits")
info = {p: sum(d * d for d in p) for p in n5}
best = max(info.values()); win = [p for p in n5 if info[p] == best]
check("C5 least information (fewest distinct one-body frequencies, largest commutant): unique winner 3+2",
      win == [(3, 2)] and best == 13, f"commutant dims {dict((''.join(map(str, p)), v) for p, v in info.items())}")
an32 = results[(3, 2)][3]
check("C6 the 3+2 even sector: SU(3)^3, Witten, SU(d)^2 X, X, X^3 all zero; 0 mass invariants",
      results[(3, 2)][0] and results[(3, 2)][1] == 0, f"anomalies {sorted(an32.items())}")
w4 = [p for p in partitions(5, 4) if max(p) >= 2]
info4 = {p: sum(d * d for d in p) for p in w4}; b4 = max(info4, key=info4.get)
check("C7 with the spinor lift (d = 4 allowed) least information picks 4+1, not 3+2: the selection needs",
      b4 == (4, 1) and (4, 1) in passing, "single-valued (site-permutation) multiplets, which have d <= 3")

print(f"elapsed_seconds {time.time() - T0:.1f}")
print("supplied: cluster = b=5 site block, inner 6-orbit as matter, 3x3 face ends as link-end registers, piece")
print("supports, real (O_h) or complex (O) pieces; Fock register, even sector, U(1)_X, mass protection criterion,")
print("least-information = largest one-body commutant. Forced: A1-A6, B1-B5 (+B2b), C1-C7. Not derived: a gauge group.")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
