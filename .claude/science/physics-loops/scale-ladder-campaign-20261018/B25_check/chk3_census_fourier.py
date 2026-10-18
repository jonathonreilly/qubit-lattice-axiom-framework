#!/usr/bin/env python3
"""B25_check part 3: census spot-check by an independent Fourier route + the ALIGN2 k-dependent mechanism on one word.
Independent build (corelib, chk_core gauge).  For each sampled census word:
  Lambda_sp from the EXACT characterisation  spec W(k+t) = spec W(k) for all k  <=>  e^{i t.K} = 1 for every Fourier frequency
  K of tr W^p, p = 1..12 (all twelve power sums -> characteristic polynomial).  Frequencies are read mod N from an N^3 sample
  of tr W^p on a randomly offset grid (alias classes; the offset makes accidental cancellation inside a class non-generic),
  so  Lambda_sp cap (2pi/N)Z^3 = {2pi m/N : m.K = 0 mod N for every K class present}.  N = 48 and N = 64 (covers (pi/8)Z^3,
  (pi/32)Z^3 and (pi/24)Z^3, so finer-dyadic and 3-adic tastes are also seen).
  Lambda_u: largest O-invariant lattice inside Lambda_sp whose generators have a k-independent invertible U intertwiner
  (own solver: null space at 5 random k, generic element invertible, validated at 4 fresh k); coset kinds U/T.
  good: own good table (C2pair mod Lambda_u within Tfix mod Lambda_sp, linear action, (pi/32) grid).
Compares with census.pkl (B25's detector).  Prints PASS/FAIL, TOTAL."""
import sys, os, itertools, collections, pickle, random, time
import numpy as np
import corelib as cl
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
W1 = lambda w, k: cl.Wc(w, np.asarray(k)[None])[0]
# ---------------- lattices in units pi/32, mod 64 (own formulas, cross-checked against chk1's from-scratch enumeration)
U = 64
def lat(kind, a):            # a in units pi/32
    S = set()
    for v in itertools.product(range(0, U, 2), repeat=3):          # all candidates lie on (pi/16)Z^3 for a >= 4 (bcc(pi/4) half = pi/8)
        if kind == 'sc': ok = all(c % a == 0 for c in v)
        elif kind == 'fcc': ok = all(c % a == 0 for c in v) and sum(c // a for c in v) % 2 == 0
        else: ok = all(c % a == 0 for c in v) or all((c - a // 2) % a == 0 for c in v)
        if ok: S.add(v)
    return frozenset(S)
LATS = {f"sc({a})": lat('sc', a) for a in (64, 32, 16, 8, 4)}
LATS.update({f"fcc({b})": lat('fcc', b) for b in (32, 16, 8, 4)})
LATS.update({f"bcc({a})": lat('bcc', a) for a in (64, 32, 16, 8)})
B25NAME = {f"sc({a})": f"sc({a // 2})" for a in (64, 32, 16, 8, 4)}
B25NAME.update({f"fcc({b})": f"fcc({b // 2})" for b in (32, 16, 8, 4)}); B25NAME.update({f"bcc({a})": f"bcc({a // 2})" for a in (64, 32, 16, 8)})
def lname(L):
    for n, S in LATS.items():
        if S == L: return n
    return f"?{len(L)}"
def gens(n):
    kind, a = n.split('(')[0], int(n[n.index('(') + 1:-1])
    if kind == 'sc': return [(a % U, 0, 0)]
    if kind == 'fcc': return [(a % U, a % U, 0)]
    return [(a % U, 0, 0), (a // 2, a // 2, a // 2)]
ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROT.append(M)
tr = [int(np.trace(R)) for R in ROT]
isT = [t in (3, 0) or (t == -1 and np.all(np.abs(np.diag(R)) == 1)) for R, t in zip(ROT, tr)]
C2 = [i for i, t in enumerate(tr) if t == -1]
C2P = [(i, j) for i in C2 for j in C2 if i < j and np.array_equal(ROT[i] @ ROT[j], ROT[j] @ ROT[i])]
grid = np.array(list(itertools.product(range(U), repeat=3)))
def fixsets(L):
    memb = np.zeros((U,) * 3, bool)
    for v in L: memb[v] = True
    F = [memb[tuple(((grid @ R.T - grid) % U).T)] for R in ROT]
    c = np.zeros(len(grid), bool)
    for i, j in C2P: c |= F[i] & F[j]
    return c, np.all([F[i] for i in range(24) if isT[i]], axis=0)
FS = {n: fixsets(L) for n, L in LATS.items()}
GOOD = {(a, b): not (FS[a][0] & ~FS[b][1]).any() for a in LATS for b in LATS if LATS[a] <= LATS[b]}
check("own good table: 56 good of 74 strict nested pairs, none among (L,L), (sc,bcc)_a, (fcc,sc)_b",
      sum(v for (a, b), v in GOOD.items() if a != b) == 56 and sum(1 for a, b in GOOD if a != b) == 74 and
      not any(GOOD[(n, n)] for n in LATS) and not any(GOOD[(f"sc({a})", f"bcc({a})")] for a in (64, 32, 16, 8)) and not any(GOOD[(f"fcc({b})", f"sc({b})")] for b in (32, 16, 8, 4)))
# ---------------- Fourier route
def lam_sp_fourier(w, N, seed=0):
    r = np.random.default_rng(seed); classes = np.zeros((N,) * 3, bool)
    g = 2 * np.pi * np.arange(N) / N; K = np.array(list(itertools.product(g, repeat=3)))
    for rep in range(2):
        k0 = r.uniform(-np.pi, np.pi, 3); P = np.zeros((12, len(K)), complex)
        for s in range(0, len(K), 16384):
            ev = np.linalg.eigvals(cl.Wc(w, K[s:s + 16384] + k0))
            z = np.ones_like(ev)
            for p in range(12):
                z = z * ev; P[p, s:s + 16384] = z.sum(1)
        for p in range(12):
            F = np.fft.fftn(P[p].reshape(N, N, N)) / N ** 3
            classes |= np.abs(F) > 1e-9
    Ks = np.argwhere(classes)          # residues d mod N present (sign convention irrelevant for the annihilator)
    M = np.array(list(itertools.product(range(N), repeat=3)))
    H = np.zeros((N,) * 3, bool); H[0, 0, 0] = True; gl = []          # subgroup of Z_N^3 generated by the residues; keep generators
    for Kv in Ks:
        if H[tuple(Kv)]: continue
        gl.append(Kv); cur = np.argwhere(H)
        for n in range(1, N): H[tuple(((cur + n * Kv) % N).T)] = True
    assert H[tuple(Ks.T)].all()
    ok = np.all((M @ np.array(gl).T) % N == 0, axis=1) if gl else np.ones(len(M), bool)
    return {tuple(v) for v in M[ok]}
FK = {'U': lambda M: M, 'T': lambda M: M.T}
_cache = {}
def has_inter(w, wid, t32, kind):
    key = (wid, tuple(int(x) % U for x in t32), kind)
    if key in _cache: return _cache[key]
    t = np.pi / 32 * np.asarray(t32, float); r = np.random.default_rng(7); ks = r.uniform(-np.pi, np.pi, (5, 3)); rows = []
    for k in ks: rows.append(np.kron(W1(w, k + t), np.eye(12)) - np.kron(np.eye(12), FK[kind](W1(w, k)).T))
    _, s, vh = np.linalg.svd(np.vstack(rows)); null = vh[np.sum(s > 1e-9 * s[0]):].conj(); res = False
    if len(null):
        V = ((r.normal(size=len(null)) + 1j * r.normal(size=len(null))) @ null).reshape(12, 12)
        if np.linalg.svd(V, compute_uv=False)[-1] > 1e-6 * np.linalg.norm(V, 2):
            res = all(np.allclose(W1(w, k + t) @ V, V @ FK[kind](W1(w, k)), atol=1e-8) for k in r.uniform(-np.pi, np.pi, (4, 3)))
    _cache[key] = res; return res
def analyse(w, wid):
    S64 = lam_sp_fourier(w, 64); S48 = lam_sp_fourier(w, 48, seed=1)
    Lsp = frozenset(S64 & set(itertools.product(range(0, U, 2), repeat=3)))      # on (pi/16)Z^3 (contains every LATS member)
    ns = lname(Lsp)
    finer = len(S64) != len({v for v in S64 if all(c % 2 == 0 for c in v)})          # tastes on (pi/32)Z^3 not on (pi/16)Z^3
    tri = len(S48) != len({v for v in S48 if all(c % 3 == 0 for c in v)})            # tastes on (pi/24)Z^3 not on (pi/8)Z^3
    out = dict(Lsp=ns, finer=finer, triadic=tri, n48=len(S48), n64=len(S64))
    if ns.startswith('?'): return out
    nu = None
    for n, L in sorted(LATS.items(), key=lambda x: -len(x[1])):
        if L <= Lsp and all(has_inter(w, wid, g, 'U') for g in gens(n) if any(g)): nu = n; break
    out['Lu'] = nu; out['index'] = len(Lsp) // len(LATS[nu])
    reps = []
    for t in sorted(Lsp, key=lambda v: sum(min(c, U - c) for c in v)):
        if any(tuple((a - b) % U for a, b in zip(t, r)) in LATS[nu] for r in reps): continue
        reps.append(t)
    out['kinds'] = collections.Counter(''.join(k for k in 'UT' if has_inter(w, wid, t, k)) for t in reps[1:])
    out['good'] = GOOD[(nu, ns)]
    return out
# ---------------- sample ~20 census words, stratified
R = pickle.load(open(os.path.join(cl.HERE, '..', 'B25_spectral_tastes', 'census.pkl'), 'rb'))['R']
named = [(j, r) for j, r in R if r and r.get('Lu')]
strata = collections.defaultdict(list)
for j, r in named:
    kd = r['kdep'] > 0; strata[(r['index'], kd, j[0] if r['index'] == 1 else 'any', 'T' if r['kinds'].get('T') else '')].append((j, r))
rnd = random.Random(2511); sample = []
for key in sorted(strata, key=str):
    lst = strata[key]; take = 3 if key[0] > 1 else 2
    sample += rnd.sample(lst, min(take, len(lst)))
sample = sample[:22]
extra = [(('B24', ('S2', 'p', 'S4', 'o'), ('P7', 'H00')), None)]                   # B25's FAIL word (non-dyadic tastes)
print(f"   {len(sample)} census words sampled from {len(strata)} strata (+ B25's Fourier-FAIL word)")
agree = 0; rows = []
for wid, (j, r) in enumerate(sample + extra):
    w = cl.build(j[1], j[2]); A = analyse(w, wid)
    if r is None:
        print(f"   FAIL-word {j[1]} {j[2]}: Lsp cap (pi/16) = {A['Lsp']}, |cap (pi/32)| = {A['n64']}, |cap (pi/24)| = {A['n48']}, triadic tastes {A['triadic']}, Lu {A.get('Lu')}, kinds {dict(A.get('kinds', {}))}")
        fail_word = A; continue
    mine = (B25NAME.get(A['Lsp'], A['Lsp']), B25NAME.get(A.get('Lu'), A.get('Lu')), A.get('index'))
    theirs = (r['Lsp'], r['Lu'], r['index'])
    kd_mine = A.get('kinds', {}).get('', 0); kd_their = r['kdep']; T_mine = A.get('kinds', {}).get('T', 0); T_their = r['kinds'].get('T', 0)
    same = mine == theirs and kd_mine == kd_their and T_mine == T_their and A.get('good') == r['good'] == False
    agree += same; rows.append(same)
    print(f"   {j[0]:6s} {'.'.join(x for x in j[1])} {j[2]}: mine Lsp={mine[0]} Lu={mine[1]} idx={mine[2]} T={T_mine} kdep={kd_mine} good={A.get('good')} "
          f"finer={A['finer']} triadic={A['triadic']} | B25 Lsp={theirs[0]} Lu={theirs[1]} idx={theirs[2]} T={T_their} kdep={kd_their} good={r['good']}  {'OK' if same else 'DIFF'}", flush=True)
check(f"Fourier-route Lambda_sp, own Lambda_u and coset kinds agree with B25's census on every sampled word; none is a good pair", all(rows), f"{agree}/{len(rows)}")
check("B25's FAIL word S2.P7.S4.H00 (= S^6 P up to conjugation) has tastes off the dyadic grid, all with U intertwiners (Lambda_sp cap (pi/16) = Lambda_u)",
      fail_word['triadic'] and fail_word.get('Lu') is not None and fail_word['index'] == 1)
# ---------------- ALIGN2 mechanism on one word (own derivation)
a, pw = 2, 'S2'; P, Pp, G = cl.letter_const('P7'), cl.letter_const('P5'), cl.letter_const('H11')
w = [pw, P, pw, G, pw, Pp, pw, G]; wr = [pw, Pp, pw, G, pw, P, pw, G]; X = [pw, P, pw, G]
tY = np.pi / (2 * a) * np.ones(3); ks = np.random.default_rng(9).uniform(-np.pi, np.pi, (5, 3))
cyc = all(np.allclose(np.linalg.inv(W1(X, k)) @ W1(w, k) @ W1(X, k), W1(wr, k)) for k in ks)
# k-independent V with W(k+tY) V = V W_rot(k)
rows = [np.kron(W1(w, k + tY), np.eye(12)) - np.kron(np.eye(12), W1(wr, k).T) for k in ks]
_, s, vh = np.linalg.svd(np.vstack(rows)); null = vh[np.sum(s > 1e-9 * s[0]):].conj()
V = null[0].reshape(12, 12) if len(null) else None
Vok = V is not None and np.linalg.svd(V, compute_uv=False)[-1] > 1e-6 and all(np.allclose(W1(w, k + tY) @ V, V @ W1(wr, k)) for k in np.random.default_rng(10).uniform(-3, 3, (4, 3)))
diagV = V is not None and np.allclose(V, np.diag(np.diag(V)))
kdep_ok = Vok and all(np.allclose(W1(w, k + tY) @ (V @ np.linalg.inv(W1(X, k))), (V @ np.linalg.inv(W1(X, k))) @ W1(w, k)) for k in np.random.default_rng(11).uniform(-3, 3, (4, 3)))
noU = not has_inter(w, 999, tY / (np.pi / 32), 'U') and not has_inter(w, 999, tY / (np.pi / 32), 'T')
Sf = lam_sp_fourier(w, 64); inLsp = tuple(int(round(x)) % 64 for x in tY / (np.pi / 32)) in Sf
print(f"   ALIGN2 word S2.P7.S2.H11.S2.P5.S2.H11, t_Y = (pi/4)(1,1,1): cyclic {cyc}, constant V {Vok} (diagonal {diagV}), "
      f"k-dependent intertwiner V X(k)^-1 works {kdep_ok}, no constant U/T {noU}, t_Y in Fourier Lambda_sp {inLsp}")
check("ALIGN2 mechanism: W_rot = X^-1 W X; W(k+t_Y) = V W_rot(k) V^-1 with constant (diagonal) V; so V X(k)^-1 is a k-dependent intertwiner; no k-independent U/T one; t_Y in Lambda_sp (Fourier)",
      cyc and Vok and kdep_ok and noU and inLsp)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
