AUDIT_INPUT_PATHS = ('docs/D4_EVENT_ONE_MODE_PER_EVENT_SPIN_CELL_NO_GO_ROOT_HOP_PHASES_AND_CELL_SPINOR_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-spin-cell: can spin-1/2 emerge from ONE fermion mode per D4 event on a superlattice cell (staggered-style phases)
while keeping the W(F4) protection?  Exact F2 linear algebra, group/representation checks and finite node diagnostics
on supplied free nearest-neighbour root-hop kernels.  Self-contained (numpy/scipy), seeded.  Run time ~40-55 s."""
import itertools, time
import numpy as np
from scipy.optimize import minimize

AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); RNG = np.random.default_rng(20261026)
PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" | {info}" if info else ""), flush=True)

# ---------------- D4 roots, W(F4), W(B4), W(D4)
ROOTS = np.array(sorted({tuple(s * np.array(v)) for v in set(itertools.permutations([1, 1, 0, 0]))
                          for s in itertools.product([1, -1], repeat=4)}), int)
RP = np.array([r for r in ROOTS if r[np.nonzero(r)[0][0]] > 0]); RPi = {tuple(r): i for i, r in enumerate(RP)}
def refl(v):
    v = np.array(v, float); return np.eye(4) - 2 * np.outer(v, v) / (v @ v)
GENS = {'F4': [(refl([0, 1, -1, 0]), 0), (refl([0, 0, 1, -1]), 0), (refl([1, -1, 0, 0]), 0), (refl([1, 0, 0, 0]), 1), (refl([1, 1, 1, 1]), 1)],
        'B4': [(refl([1, -1, 0, 0]), 0), (refl([0, 1, -1, 0]), 0), (refl([0, 0, 1, -1]), 0), (refl([0, 0, 0, 1]), 1)],
        'D4': [(refl([1, -1, 0, 0]), 0), (refl([0, 1, -1, 0]), 0), (refl([0, 0, 1, -1]), 0), (refl([0, 0, 1, 1]), 0)]}
def closure(gs):
    key = lambda A: tuple(np.round(2 * A).astype(int).ravel()); E = np.eye(4); G = {key(E): E}; fr = [E]
    while fr:
        nf = []
        for A in fr:
            for g in gs:
                B = g @ A
                if key(B) not in G: G[key(B)] = B; nf.append(B)
        fr = nf
    return list(G.values())
GRP = {k: closure([g for g, _ in v]) for k, v in GENS.items()}
print(f"setup: |W(F4)|, |W(B4)|, |W(D4)| = {len(GRP['F4'])}, {len(GRP['B4'])}, {len(GRP['D4'])}; 24 roots, 12 positive")
TRI = [(a, b, -(a + b)) for a in ROOTS for b in ROOTS if a @ b == -1]
TB = np.array([(1, 1, 0, 0), (1, -1, 0, 0), (0, 1, -1, 0), (0, 0, 1, -1)]).T   # D4 basis (columns)

# ---------------- C1 W(F4)-invariant cells between 4D4 and D4
Ginv = [np.round(np.linalg.inv(TB) @ g @ TB).astype(int) for g in GRP['F4']]
els = list(itertools.product(range(4), repeat=4))
def span(gens):
    S = {(0, 0, 0, 0)}; fr = list(S)
    while fr:
        nf = []
        for s in fr:
            for g in gens:
                t = tuple((np.array(s) + np.array(g)) % 4)
                if t not in S: S.add(t); nf.append(t)
        fr = nf
    return frozenset(S)
orbs = {}
for e in els:
    o = frozenset(tuple(M @ np.array(e) % 4) for M in Ginv); orbs[o] = 1
base = [span(list(o)) for o in orbs]
subs = set(base)
while True:
    new = {span(list(a | b)) for a in subs for b in subs} - subs
    if not new: break
    subs |= new
idxs = sorted(256 // len(s) for s in subs)
check("C1 cells: the W(F4)-invariant sublattices L with 4D4 <= L <= D4 have indices " + str(idxs) + "; there is none of index 2 or 8, so the small cells are 2D4* (index 4, the sqrt2 cell), 2D4 (16), 4D4* (64)",
      2 not in idxs and 8 not in idxs and 4 in idxs and 16 in idxs and 64 in idxs, f"{len(subs)} invariant subgroups of D4/4D4")

# ---------------- cell machinery (Z2 phases eta on the 12 positive root hops, periodic mod L)
BASES = {'2D4*': np.array([[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [1, 1, 1, 1]]).T, '2Z4': 2 * np.eye(4, dtype=int),
         '2D4': 2 * TB, '4D4*': 2 * np.array([[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [1, 1, 1, 1]]).T}
def make_cell(B):
    d = int(round(abs(np.linalg.det(B)))); adj = np.round(np.linalg.inv(B) * d).astype(int)
    red = lambda x: tuple(np.asarray(x, int) - B @ np.floor_divide(adj @ np.asarray(x, int), d))
    idx = {}
    for x in itertools.product(range(-4, 5), repeat=4):
        if sum(x) % 2 == 0 and red(x) not in idx: idx[red(x)] = len(idx)
    return red, idx, {v: np.array(k) for k, v in idx.items()}
CELLS = {k: make_cell(B) for k, B in BASES.items()}
def edge(cell, x, r, anti):
    red, idx, _ = CELLS[cell]; t = tuple(r)
    if t in RPi: return idx[red(x)] * 12 + RPi[t], 0
    return idx[red(np.asarray(x) + r)] * 12 + RPi[tuple(-np.asarray(r))], (1 if anti else 0)
def tri_form(cell, x, a, b, c, anti):
    x = np.asarray(x); es = [edge(cell, x, a, anti), edge(cell, x + a, b, anti), edge(cell, x + a + b, c, anti)]
    return [e[0] for e in es], sum(e[1] for e in es) % 2
def gf2_solve(rows, rhs):
    M = np.unique(np.concatenate([rows, rhs[:, None]], 1).astype(np.uint8), axis=0); n = M.shape[1] - 1
    piv = []; r = 0
    for c in range(n):
        nz = np.nonzero(M[r:, c])[0]
        if not len(nz): continue
        p = r + nz[0]; M[[r, p]] = M[[p, r]]; mk = M[:, c].astype(bool); mk[r] = False; M[mk] ^= M[r]; piv.append(c); r += 1
        if r == len(M): break
    if np.any(M[r:, n]): return None, None
    x = np.zeros(n, np.uint8); x[piv] = M[:len(piv), n]
    free = sorted(set(range(n)) - set(piv)); N = np.zeros((len(free), n), np.uint8)
    for i, f in enumerate(free): N[i, f] = 1; N[i, piv] = M[:len(piv), f]
    return x, N
def gf2_rank(A):
    return 0 if A.size == 0 else A.shape[1] - len(gf2_solve(A, np.zeros(len(A), np.uint8))[1])
def cov_system(cell, grp, anti, chi):
    _, idx, reps = CELLS[cell]; n = len(idx); R = []; b = []
    for g, typ in GENS[grp]:
        for c in range(n):
            x = reps[c]; gx = np.round(g @ x).astype(int)
            for a, bb, cc in TRI:
                v1, k1 = tri_form(cell, x, a, bb, cc, anti)
                ga, gb = np.round(g @ a).astype(int), np.round(g @ bb).astype(int)
                v2, k2 = tri_form(cell, gx, ga, gb, -(ga + gb), anti)
                row = np.zeros(12 * n, np.uint8)
                for v in v1 + v2: row[v] ^= 1
                R.append(row); b.append((k1 + k2 + (chi[typ] == -1)) % 2)
    return np.array(R), np.array(b, np.uint8)
def flux_rows(cell, anti):
    _, idx, reps = CELLS[cell]; n = len(idx); F = np.zeros((n * len(TRI), 12 * n), np.uint8); K = np.zeros(n * len(TRI), np.uint8)
    for c in range(n):
        for j, (a, b, cc) in enumerate(TRI):
            v, k = tri_form(cell, reps[c], a, b, cc, anti); K[c * len(TRI) + j] = k
            for q in v: F[c * len(TRI) + j, q] ^= 1
    return F, K
def flux_dirs(F, N):
    FN = (F.astype(np.int64) @ N.T.astype(np.int64)) % 2; sel = []; cur = np.zeros((len(F), 0), np.uint8)
    for j in range(FN.shape[1]):
        tr = np.concatenate([cur, FN[:, j:j + 1].astype(np.uint8)], 1)
        if gf2_rank(tr.T) > cur.shape[1]: cur = tr; sel.append(j)
    return sel
STRUCT = {}
def Dk(cell, eta, anti, k, mu=None):
    key = (cell, eta.tobytes(), anti)
    if key not in STRUCT:
        red, idx, reps = CELLS[cell]; C, Cp, S, Rv = [], [], [], []
        for c in range(len(idx)):
            for r in ROOTS:
                vi, k0 = edge(cell, reps[c], r, anti)
                C.append(c); Cp.append(idx[red(reps[c] + r)]); S.append((-1.0) ** ((int(eta[vi]) + k0) % 2)); Rv.append(r)
        STRUCT[key] = (len(idx), np.array(C), np.array(Cp), np.array(S), np.array(Rv, float))
    n, C, Cp, S, Rv = STRUCT[key]; w = S * np.exp(1j * (Rv @ k))
    if mu is not None: w = w * 1j * Rv[:, mu]
    M = np.zeros((n, n), complex); np.add.at(M, (C, Cp), w); return M
def classify(cell, eta, anti, m=4, nref=4):
    """find zeros of D(k); at each, Dirac iff z = 0 mod 4 and the linearised map is a NONDEGENERATE Clifford map"""
    Ls = 2 * np.pi * np.linalg.inv(BASES[cell]).T
    f = lambda t: np.linalg.svd(Dk(cell, eta, anti, Ls @ t), compute_uv=False)[-1]
    grid = sorted(((f(np.array(t)), t) for t in itertools.product(np.arange(m) / m + 0.013, repeat=4)), key=lambda z: z[0])
    out = []
    for _, t in grid[:nref]:
        r = minimize(f, np.array(t), method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13, 'maxiter': 3000})
        if r.fun > 1e-6: out.append('gap'); continue
        k0 = Ls @ r.x; U, s, Vh = np.linalg.svd(Dk(cell, eta, anti, k0)); z = int((s < 1e-6).sum())
        Ms = [U[:, -z:].conj().T @ Dk(cell, eta, anti, k0, mu) @ Vh[-z:].conj().T for mu in range(4)]
        g = np.array([[np.trace(Ms[a].conj().T @ Ms[b] + Ms[b].conj().T @ Ms[a]).real / (2 * z) for b in range(4)] for a in range(4)])
        err = max(np.abs(Ms[a].conj().T @ Ms[b] + Ms[b].conj().T @ Ms[a] - 2 * g[a, b] * np.eye(z)).max() for a in range(4) for b in range(4))
        ev = np.linalg.eigvalsh(g); rk = int((ev > 1e-4 * max(ev.max(), 1e-12)).sum())
        out.append('DIRAC' if (err < 1e-6 and rk == 4 and z % 4 == 0) else f'deg(z={z},rank{rk})')
    return out
def is_bad(o): return any(t.startswith('deg') for t in o)

# ---------------- C2 no KS eta phases on D4
u, v, w, z = (1, 1, 0, 0), (1, -1, 0, 0), (1, 0, 1, 0), (1, 0, -1, 0)
neg = {u, v, w, z} | {tuple(-np.array(q)) for q in (u, v, w, z)}
s = {tuple(r): (-1 if tuple(r) in neg else 1) for r in ROOTS}
viol = [(a, b) for a in ROOTS for b in ROOTS if tuple(a + b) in s and s[tuple(a + b)] != s[tuple(a)] * s[tuple(b)]]
_, idx2, reps2 = CELLS['2D4']; red2 = CELLS['2D4'][0]; dix = {tuple(r): i for i, r in enumerate(ROOTS)}
rows = []; rhs = []
for c in range(16):
    x = reps2[c]
    for a in ROOTS:
        for b in ROOTS:
            if np.all(a == b) or np.all(a == -b): continue
            vs = [idx2[red2(x)] * 24 + dix[tuple(a)], idx2[red2(x + a)] * 24 + dix[tuple(b)], idx2[red2(x)] * 24 + dix[tuple(b)], idx2[red2(x + b)] * 24 + dix[tuple(a)]]
            row = np.zeros(16 * 24, np.uint8)
            for q in vs: row[q] ^= 1
            rows.append(row); rhs.append(1)
sol, _ = gf2_solve(np.array(rows), np.array(rhs, np.uint8))
sx, sy, sz, I2 = np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]]), np.eye(2)
gam = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, I2)]
Gm = lambda r: sum(r[i] * gam[i] for i in range(4)) / np.sqrt(2)
a, b = np.array([1, 1, 0, 0]), np.array([0, -1, 1, 0]); P = Gm(a) @ Gm(b) @ Gm(-(a + b))
check("C2 no D4 eta phases: (i) if all 24 root hops A_r pairwise anticommuted (KS property, ANY U(1) phases, any period), Delta = (A_u A_v)(A_w A_z)^-1 is diagonal with Delta(x+r) = s_r Delta(x), s = -1 exactly on +-u,+-v,+-w,+-z (u,v,w,z = e1+-e2, e1+-e3); s must be a character of D4 but is not; (ii) F2 system on the 2D4 cell inconsistent; (iii) the naive spinor kernel sum (r.gamma) T_r cannot be spin-diagonalised: a triangle product of r.gamma/sqrt2 is not a multiple of 1",
      len(viol) > 0 and sol is None and np.abs(P - np.trace(P) / 4 * np.eye(4)).max() > 0.5,
      f"character violations {len(viol)} (e.g. (e2+e4)+(e1-e4) = e1+e2); F2 consistent: {sol is not None}; triangle product = {np.round(np.diag(P.conj().T @ P).real, 3)} x unit, |P - tr/4| = {np.abs(P - np.trace(P) / 4 * np.eye(4)).max():.2f} (P is (gamma3-gamma2)/sqrt2-type)")

# ---------------- C3 no onsite chirality; translation characters vs W(F4)
lamorb = {}
for lam in itertools.product([0, 1], repeat=4):
    o = frozenset(tuple(int(np.dot(lam, np.round(np.linalg.inv(TB) @ np.linalg.inv(g) @ TB[:, j]).astype(int)) % 2) for j in range(4)) for g in GRP['F4'])
    lamorb[o] = 1
sizes = sorted(len(o) for o in lamorb)
check("C3 chirality: the D4 root graph has triangles (r1+r2+r3 = 0), so no onsite sign eps(x) can anticommute with ANY kernel whose hops include a triangle: no remnant U(1)_eps at nearest neighbour (KS's eps is constant on D4). The sign characters of D4/2D4 fall into W(F4) orbits " + str(sizes) + ": a character eps is W(F4)-invariant only if trivial; the best keeps 384 (one triality frame)",
      sizes == [1, 3, 12] and len(TRI) == 192, f"ordered 120-degree root pairs {len(TRI)}")

# ---------------- C4/C5 projective covariance search
res = {}; tab = []
for cell, grp in [('2D4*', 'F4'), ('2D4', 'F4'), ('2D4*', 'B4'), ('2Z4', 'B4'), ('2D4', 'B4'), ('2D4*', 'D4'), ('2Z4', 'D4')]:
    F_a, K_a = flux_rows(cell, True); F_s, K_s = flux_rows(cell, False)
    for anti in (True, False):
        for chi in ([(1, 1), (1, -1), (-1, 1), (-1, -1)] if grp != 'D4' else [(1, 1), (-1, 1)]):
            x, N = gf2_solve(*cov_system(cell, grp, anti, chi))
            if x is None: continue
            sel = flux_dirs(F_a if anti else F_s, N); pats = []
            for cb in itertools.product([0, 1], repeat=len(sel)):
                eta = x.copy()
                for bit, j in zip(cb, sel):
                    if bit: eta ^= N[j]
                pats.append(eta)
            res[(cell, grp, anti, chi)] = pats; tab.append(f"{cell}/{grp}/{'A' if anti else 'S'}{chi}:{len(pats)}")
okc = all(k[2] == (k[3] == (-1, 1)) and (k[3] in [(-1, 1), (1, 1)]) for k in res) and len(res) == 14
print("   consistent (cell/group/class chi_long,chi_short : flux patterns): " + ", ".join(tab))
worst = []; allbad = True
for k, pats in res.items():
    for eta in pats:
        o = classify(k[0], eta, k[2]); allbad &= is_bad(o); worst.append(o[0])
check("C4 full W(F4) and the subgroups W(B4), W(D4), realised projectively on the cells 2D4*, 2Z4, 2D4: the covariance systems are consistent ONLY for (antisymmetric, chi = -1 on long reflections) and (symmetric, trivial chi), each with exactly 2 flux patterns (D and -D): the uniform flux is forced. Every pattern has degenerate zeros (no isolated Dirac node)",
      okc and allbad, f"{len(res)} consistent systems; zero types seen {sorted(set(worst))}")
# exact structure of the uniform antisymmetric pattern
eta = res[('2D4*', 'F4', True, (-1, 1))][0]
Ks = RNG.uniform(-np.pi, np.pi, (300, 4)); dev = 0; Fv = []
for k in Ks:
    M = Dk('2D4*', eta, True, k); H = M.conj().T @ M; fk = np.trace(H).real / 4; dev = max(dev, np.abs(H - fk * np.eye(4)).max()); Fv.append(fk)
n4 = [r for r in itertools.product(range(-2, 3), repeat=4) if sum(np.array(r) ** 2) == 4 and (sum(r) % 2 == 0)]
n8 = [tuple(2 * r) for r in ROOTS]
fpred = lambda k: 24 + 6 * sum(np.cos(np.array(q) @ k) for q in n4) + sum(np.cos(np.array(q) @ k) for q in n8)
fit = max(abs(fv - fpred(k)) for fv, k in zip(Fv, Ks))
line = max(np.linalg.svd(Dk('2D4*', eta, True, np.array([0, 0, 0, np.pi]) + t * np.ones(4)), compute_uv=False).max() for t in np.linspace(0.1, 1.4, 7))
check("C4b the forced (uniform) antisymmetric pattern is a WEAK D4 eta: D^dag D = f(k) 1 exactly (the 60/120-degree cross terms cancel), f = 24 + 6 sum_{24 norm-4 v} cos(v.k) + sum_{r} cos(2r.k), a scalar coarse operator on 2D4*. But f = 0 on whole lines, e.g. k = (0,0,0,pi) + t(1,1,1,1): a line of zero modes, not a Dirac point",
      dev < 1e-12 and fit < 1e-10 and line < 1e-12 and len(n4) == 24, f"|D^dag D - f| {dev:.0e}, fit {fit:.0e}, max singular value on the line {line:.0e}")
# 4D4* (index 64): W(F4) admits 16 non-uniform patterns; all degenerate
bad64 = True; n64 = 0
for anti, chi in [(True, (-1, 1)), (False, (1, 1))]:
    x, N = gf2_solve(*cov_system('4D4*', 'F4', anti, chi)); F, K = flux_rows('4D4*', anti); sel = flux_dirs(F, N)
    for cb in itertools.product([0, 1], repeat=len(sel)):
        e = x.copy()
        for bit, j in zip(cb, sel):
            if bit: e ^= N[j]
        bad64 &= is_bad(classify('4D4*', e, anti, m=3, nref=2)); n64 += 1
check("C4c the 64-event cell 4D4*: W(F4)-covariant patterns (both classes) number " + str(n64) + " (non-uniform ones appear); every one has degenerate zeros", bad64 and n64 == 32, f"{time.time() - t0:.0f}s so far")

# ---------------- C6 all translation-uniform Z2 fluxes, any point symmetry
rows = []; rhs = []; nunif = {}
for anti in (True, False):
    R = []; bb = []
    for t in TB.T:
        for c in range(16):
            for a, b_, cc in TRI:
                v1, k1 = tri_form('2D4', reps2[c], a, b_, cc, anti); v2, k2 = tri_form('2D4', reps2[c] + t, a, b_, cc, anti)
                row = np.zeros(192, np.uint8)
                for q in v1 + v2: row[q] ^= 1
                R.append(row); bb.append((k1 + k2) % 2)
    x, N = gf2_solve(np.array(R), np.array(bb, np.uint8)); F, K = flux_rows('2D4', anti); sel = flux_dirs(F, N)
    combos = np.array(list(itertools.product([0, 1], repeat=len(sel))), np.int64)
    ETA = (x[None].astype(np.int64) + combos @ N[sel].astype(np.int64)) % 2
    FL = (ETA @ F[:192].T.astype(np.int64) + K[:192]) % 2
    cls = sorted({min((tuple(a), tuple(b), tuple(c)), (tuple(b), tuple(c), tuple(a)), (tuple(c), tuple(a), tuple(b))) for a, b, c in TRI})
    pos = {}
    for j, (a, b, c) in enumerate(TRI): pos.setdefault(min((tuple(a), tuple(b), tuple(c)), (tuple(b), tuple(c), tuple(a)), (tuple(c), tuple(a), tuple(b))), j)
    cols = [pos[c] for c in cls]; ci = {c: i for i, c in enumerate(cls)}
    can = lambda T: min(T, T[1:] + T[:1], T[2:] + T[:2])
    PERM = np.array([[ci[can(tuple(tuple(np.round(g @ np.array(q)).astype(int)) for q in T))] for T in cls] for g in GRP['F4']])
    F64 = FL[:, cols]; wv = (np.uint64(1) << np.arange(64, dtype=np.uint64)); best = np.full(len(F64), np.iinfo(np.uint64).max, np.uint64)
    for flip in (0, 1):
        for p in PERM: best = np.minimum(best, ((F64 ^ flip)[:, p].astype(np.uint64) * wv).sum(1))
    reps_o = {}
    for i, bv in enumerate(best): reps_o.setdefault(int(bv), i)
    ndeg = ngap = 0; gapinfo = []
    Ls2 = 2 * np.pi * np.linalg.inv(BASES['2D4']).T
    for bv, i in reps_o.items():
        o = classify('2D4', ETA[i].astype(np.uint8), anti, m=4, nref=3)
        if is_bad(o): ndeg += 1; continue
        if all(t == 'gap' for t in o):
            smin = min(np.linalg.svd(Dk('2D4', ETA[i].astype(np.uint8), anti, Ls2 @ RNG.uniform(0, 1, 4)), compute_uv=False)[-1] for _ in range(1500))
            if smin > 0.5: ngap += 1; gapinfo.append((int((best == bv).sum()), round(float(smin), 2)))
    nunif[anti] = (len(sel), len(ETA), len(reps_o), ndeg, ngap, gapinfo)
check("C6 EVERY translation-uniform Z2 flux on the 24 unit root hops (any point symmetry or none; 2^14 per class, all W(F4)(+sign) orbits): each orbit either has degenerate zeros or is GAPPED; none has only isolated Dirac nodes",
      all(v[0] == 14 and v[3] + v[4] == v[2] for v in nunif.values()), "anti: dim %d, %d patterns, %d orbits, %d degenerate, %d gapped %s; sym: dim %d, %d patterns, %d orbits, %d degenerate, %d gapped (orbit size, min singular value) %s" % (nunif[True] + nunif[False]))
lam_bad = True
for anti in (True, False):
    for _ in range(8):
        lam = RNG.integers(0, 2, 4); R = []; bb = []
        for ti, t in enumerate(TB.T):
            for c in range(16):
                for a, b_, cc in TRI:
                    v1, k1 = tri_form('2D4', reps2[c], a, b_, cc, anti); v2, k2 = tri_form('2D4', reps2[c] + t, a, b_, cc, anti)
                    row = np.zeros(192, np.uint8)
                    for q in v1 + v2: row[q] ^= 1
                    R.append(row); bb.append((k1 + k2 + lam[ti]) % 2)
        x, N = gf2_solve(np.array(R), np.array(bb, np.uint8))
        e = (x.astype(np.int64) + RNG.integers(0, 2, len(N)) @ N.astype(np.int64)) % 2
        lam_bad &= is_bad(classify('2D4', e.astype(np.uint8), anti, m=3, nref=2))
check("C6b translations acting with a sign character (D -> -D, staggered flux): seeded sample of 16 patterns, all degenerate (the full sweep of all orbits is a scratch diagnostic)", lam_bad)

# ---------------- C7 representation theory: spinor in the cell mode space at an invariant node
# lift generators: reflection in unit n -> n.gamma ; build the lifted group by closure modulo phase
Lg = []
for g, _ in GENS['F4']:
    M = g; n_ = np.linalg.eigh(M)[1][:, 0]; Lg.append((M, sum(n_[i] * gam[i] for i in range(4))))
def close_lift(gens):
    key = lambda A: tuple(np.round(2 * A).astype(int).ravel()); E = np.eye(4); G = {key(E): (E, np.eye(4, dtype=complex))}; fr = [key(E)]
    while fr:
        nf = []
        for kk in fr:
            A, SA = G[kk]
            for g, Sg in gens:
                B = g @ A
                if key(B) not in G: G[key(B)] = (B, Sg @ SA); nf.append(key(B))
        fr = nf
    return list(G.values())
LIFT = close_lift(Lg)
cov = max(np.abs(S @ gam[0] @ np.linalg.inv(S) - sum((A @ np.eye(4)[:, 0])[j] * gam[j] for j in range(4)) * np.sign(np.linalg.det(A))).max() for A, S in LIFT)
def span_dim(mats):
    return np.linalg.matrix_rank(np.array([m.ravel() for m in mats]), tol=1e-8)
stabdims = {}
for cell in ['2D4*', '2D4']:
    red, idx, reps = CELLS[cell]; dims = set()
    for c, x in reps.items():
        H = [S for A, S in LIFT if red(np.round(A @ x).astype(int)) == red(x)]
        dims.add((len(H), span_dim(H)))
    stabdims[cell] = sorted(dims)
check("C7 rep theory (ANY kernel range, ANY U(1) phases): at a W(F4)-invariant node the cell's mode space is a sum of monomial modules induced from coset stabilisers H; every H lifts to a set spanning all of M_4(C) (S|H irreducible), so by Frobenius the 4-dim spinor S never occurs: the 4-event sqrt2 cell (dim 4) cannot hold one Dirac spinor, and the 16-event cell cannot hold an untasted one. Only spin x taste (S x T, dim 16) is left open there",
      len(LIFT) == 1152 and cov < 1e-9 and all(d == 16 for cell in stabdims for _, d in stabdims[cell]), f"lift covariance S gamma S^-1 = det(g) g.gamma: {cov:.0e}; (|H|, span dim): {stabdims}")

# ---------------- C8 quartic invariants (protection count) and C9 supply
mon = [m for m in itertools.product(range(5), repeat=4) if sum(m) == 4]; Pt = RNG.normal(size=(60, 4))
def nquart(G):
    Q = np.einsum('tj,gij->tgi', Pt, np.array(G)); V = np.prod(Q[:, :, None, :] ** np.array(mon, float)[None, None], -1).mean(1)
    return np.linalg.matrix_rank(V, tol=1e-8)
stab96 = [g for g in GRP['F4'] if np.allclose(g @ np.array([1, 1, 0, 0.]), np.array([1, 1, 0, 0.])) or np.allclose(g @ np.array([1, 1, 0, 0.]), -np.array([1, 1, 0, 0.]))]
q = {k: nquart(GRP[k]) for k in GRP}; q96 = nquart(stab96)
check("C8 protection count: quartic invariants W(F4) 1 (only (p^2)^2), W(B4) 2, W(D4) 3, stabiliser of a root class (96) " + str(q96) + ": any staggered escape that breaks W(F4) to a frame or root stabiliser re-admits dim-6 LIV",
      q['F4'] == 1 and q['B4'] == 2 and q['D4'] == 3 and len(stab96) == 96 and q96 >= 2, f"{q}, 96: {q96}")
check("C9 supply: one Dirac spinor per event = 4 complex fermion modes per event = Fock dim 2^4 = 16 = four qubits (M_2(C)^(x)4), not two; the Qubit axiom gives M_2(C) (one mode). The 4-event sqrt2 cell holds exactly 4 modes, which C7 rules out as a spinor; spreading one spinor over 16 events (2D4 cell) needs spin x taste",
      2 ** 4 == 16 and len(CELLS['2D4*'][1]) == 4 and len(CELLS['2D4'][1]) == 16)
print(f"runtime {time.time() - t0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
