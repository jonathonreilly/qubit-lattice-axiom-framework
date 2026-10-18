#!/usr/bin/env python3
"""B26 part 2: tastes of the new (A2 half-) letters and of the enlarged-palette words.
(a) Letter-level tastes V X(k) V^-1 = w X(k + pi e) (constant V, |w| = 1, e in {0,1}^3 minus 0) for X = A_a = A0 S^a, a = 1, 2:
    solved as a linear null space over 6 random k for each w in the 8th roots of unity (the B18 S-theorem form).
(b) Joint tastes with S, with H_on, with R_L (needed for any word containing them letter-wise).
(c) Word level: spectral taste lattice Lambda_sp cap (pi/4)Z^3 (spectrum of W(k) = spectrum of W(k+t) up to a global
    phase shift e^{i theta}, theta in pi/4 Z, at 4 random k) for one-slot new skeleton classes x a seeded sample of fills;
    compared with the B24 lattice classification (no rotation-invariant lattice makes all C2-pair points T-fixed)."""
import sys, os, time, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
t0 = time.time()
from b26lib import *
from skeletons import generate
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(21); KS = rng.uniform(-np.pi, np.pi, size=(6, 3))
def Aa(k, a): return A0 @ Sk(k, a) if a else A0
def intertwiners(Xfs, e, w):
    """dim of {V : V X(k) = w X(k+pi e) V for all X in Xfs, k in KS}"""
    rows = []
    for Xf in Xfs:
        for k in KS:
            X1, X2 = Xf(k), Xf(k + np.pi * np.asarray(e))
            # V X1 - w X2 V = 0  ->  (X1^T (x) 1 - w 1 (x) X2) vec(V) = 0   (column-major vec)
            rows.append(np.kron(X1.T, np.eye(12)) - w * np.kron(np.eye(12), X2))
    A = np.vstack(rows); _, sv, Vh = np.linalg.svd(A); null = Vh[np.sum(sv > 1e-8):].conj()
    if len(null) == 0: return 0, False
    # a taste needs an INVERTIBLE V (second run counted singular intertwiners; log kept): test a random element of the
    # null space (det is a polynomial on it, so a random element is invertible iff some element is)
    c = np.random.default_rng(0).normal(size=len(null)) + 1j * np.random.default_rng(1).normal(size=len(null))
    V = (c @ null).reshape(12, 12, order='F'); sv2 = np.linalg.svd(V, compute_uv=False)
    return len(null), bool(sv2.min() > 1e-8 * sv2.max())
ES = [e for e in itertools.product((0, 1), repeat=3) if any(e)]
WS = [np.exp(1j * np.pi * j / 4) for j in range(8)]
def taste_table(Xfs):
    tab = {}
    for e in ES:
        tab[e] = [(j,) + intertwiners(Xfs, e, w) for j, w in enumerate(WS)]
        tab[e] = [(j, d, inv) for j, d, inv in tab[e] if d > 0]
    return tab
print("(a) letter-level intertwiners (e: [(w = e^{i pi j/4}, dim of solution space, contains invertible V)])")
tA1 = taste_table([lambda k: Aa(k, 1)]); tA2 = taste_table([lambda k: Aa(k, 2)])
for e in ES: print(f"   A_1 e={e}: {tA1[e]}    A_2 e={e}: {tA2[e]}")
check("A_1 has a nonzero intertwiner for every e (constant-spectrum letter: tastes exist; as B18 found for H_link, R_L)", all(any(x[2] for x in tA1[e]) for e in ES))
tS = taste_table([lambda k: Sk(k, 1)])
for e in ES: print(f"   S e={e}: {tS[e]}")
# expectation corrected after the first run (log kept): S(k + pi(1,1,1)) = S(k) since e.f_c is even for e = (1,1,1); that
# taste maps k* -> -k* (B18: all allowed maps send k* to +-k*).  The S-theorem is the absence of every other e.
check("S has a constant-V taste only for e = (1,1,1) (k* -> -k*, trivial V = 1, w = 1); none maps k* to a doubler (B18 S-theorem)",
      all(not any(x[2] for x in tS[e]) for e in ES if e != (1, 1, 1)) and tS[(1, 1, 1)] == [(0, 12, True)])
print("(b) joint tastes")
tSA = taste_table([lambda k: Sk(k, 1), lambda k: Aa(k, 1)])
tAH = taste_table([lambda k: Aa(k, 1), lambda k: Hon0.astype(complex)])
tAR = taste_table([lambda k: Aa(k, 1), RLk])
for e in ES: print(f"   e={e}:  (A_1,H_on): {tAH[e]}   (A_1,R_L): {tAR[e]}")
for e in ES: print(f"   (S,A_1) e={e}: {tSA[e]}")
check("joint (S, A_1) tastes exist only for e = (1,1,1) (k* -> -k*) -- any word containing S letter-wise inherits the S-theorem",
      all(not any(x[2] for x in tSA[e]) for e in ES if e != (1, 1, 1)))
print("   note: A_a appear in symmetric words only in pairs, and every even-A word is +-(old-palette word); its tastes are those of that word.")

# (c) word-level spectral taste lattice on (pi/4)Z^3
G = generate(); ONE = sorted([v for (no, c), v in G.items() if no == 1], key=lambda s: (len(s), s))
names = list(PC); TS = [np.array(t) * np.pi / 4 for t in itertools.product(range(8), repeat=3)]
KS4 = rng.uniform(-np.pi, np.pi, size=(3, 3))
def spec_eq(e1, e2):
    # equal up to a global phase in (pi/4)Z
    for j in range(8):
        a = np.sort(np.mod(np.angle(e1 * np.exp(1j * np.pi * j / 4)), 2 * np.pi)); b = np.sort(np.mod(np.angle(e2), 2 * np.pi))
        d = np.abs(np.exp(1j * a)[:, None] - np.exp(1j * b)[None, :]).min(axis=1)
        if d.max() < 1e-7 and len(a) == len(b):
            # multiset check
            if np.allclose(np.sort_complex(np.round(np.exp(1j * a), 8)), np.sort_complex(np.round(np.exp(1j * b), 8)), atol=1e-7): return True
    return False
def lattice_of(w):
    base = [np.linalg.eigvals(Wb(w, k[None])[0]) for k in KS4]
    L = []
    for t in TS:
        if all(spec_eq(b, np.linalg.eigvals(Wb(w, (k + t)[None])[0])) for b, k in zip(base, KS4)): L.append(tuple(int(round(x / (np.pi / 4))) % 8 for x in t))
    return frozenset(L)
LATS = {}
for m, an in ((8, '2pi'), (4, 'pi'), (2, 'pi/2'), (1, 'pi/4')):
    sc = {tuple((m * x) % 8 for x in t) for t in itertools.product(range(8), repeat=3)}
    LATS[f'sc({an})'] = frozenset(sc)
    if m % 2 == 0:
        h = m // 2
        LATS[f'bcc({an})'] = frozenset(sc | {tuple((x + h) % 8 for x in t) for t in sc})
        LATS[f'fcc({an})'] = frozenset(sc | {tuple((x + y) % 8 for x, y in zip(t, sh)) for t in sc for sh in ((h, h, 0), (h, 0, h), (0, h, h))})
def lat_name(L):
    for nm, X in LATS.items():
        if L == X: return nm
    return 'other(|L|=%d)' % len(L)
cnt = collections.Counter(); ex = {}
rs = np.random.default_rng(99)
for sk in ONE:
    for t in rs.choice(len(names), size=3, replace=False):
        w = [PC[names[t]] if L == 'o' else L for L in sk]
        L = lattice_of(w); nm = lat_name(L); cnt[nm] += 1; ex.setdefault(nm, (sk, names[t], sorted(L)[:8]))
print("(c) spectral taste lattice census (one-slot new classes x 3 seeded fills each):", dict(cnt))
for nm, e in ex.items(): print(f"   {nm}: e.g. {e[0]} {e[1]} {e[2]}")
print("   (census only; B24's lattice theorem is exact for every rotation-invariant lattice, so it covers any outcome here)")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
