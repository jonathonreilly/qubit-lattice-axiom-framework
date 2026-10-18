#!/usr/bin/env python3
"""C8 part 1b: mixed words of range-0 doubled-cell letters (G0, from c8_qletters' orbit pieces) with old letters.
Exact sublattice-block algebra on the infinite lattice (no L=4 aliasing): an operator commuting with 2Z^3 is
{d: X[s] (8,12,12)}, X[s] = block from sublattice s to s+d.
(e) a R_L b with a, b in G0 (all perm-part pairs, all Z4 orbit phases): translation-invariant cases and what they are
    (the perm-part lemma: both perm parts must be 1 or the A0-permutation; checked here exhaustively).
(f) bounded random search of words M1 g1 M2 g2 M3 (g in G0 random, M in {R_L, S, S^-1, on-site}) for translation-invariant
    words whose G0 letters are not themselves translation invariant; their k* doublet speeds vs the L1 value |n_S| sqrt2/3."""
import sys, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
t0 = time.time()
from c8lib import *
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
SI = {s: i for i, s in enumerate(SUBL)}
def smod(s, d): return SI[tuple((a + b) % 2 for a, b in zip(SUBL[s], d))]
def mul(X, Y):
    Z = {}
    for d2, Yb in Y.items():
        for d1, Xb in X.items():
            d = tuple(a + b for a, b in zip(d1, d2)); perm = [smod(s, d2) for s in range(8)]
            Z[d] = Z.get(d, 0) + np.einsum('sij,sjk->sik', Xb[perm], Yb)
    return {d: B for d, B in Z.items() if np.abs(B).max() > 1e-12}
def const(blocks): return {d: np.broadcast_to(M, (8, 12, 12)).copy() for d, M in blocks.items()}
def is_ti(X): return all(np.allclose(B, B[:1]) for B in X.values())
def inv(X):          # unitary inverse: (X^-1)_s(-d) = X_{s-d}(d)^dagger
    Z = {}
    for d, B in X.items():
        nd = tuple(-x for x in d); perm = [smod(s, nd) for s in range(8)]
        Z[nd] = np.conj(np.transpose(B[perm], (0, 2, 1)))
    return Z

# ---- G0 pieces (recomputed exactly as in c8_qletters)
G = G2_elements()
seen = -np.ones(nV, int); orbits = []
for a in range(nV):
    if seen[a] >= 0: continue
    o = sorted(set(int(P[a]) for P, _, _ in G)); orbits.append(o)
    for b in o: seen[b] = len(orbits) - 1
ORB = np.zeros((8, 12), int)
for si, s in enumerate(SUBL):
    for c in CORN: ORB[si, CI[c]] = seen[vid(s, c)]
pieces = {}
for oi, o in enumerate(orbits):
    m0 = o[0]; v0, c0 = VERTS[m0]
    for cc in CORN:
        t = vid(v0, cc)
        for twist in (False, True):
            X = gavg(m0, t, twist, G)
            if X and is_partial_phased_perm(X) and len({k[0] for k in X}) == len(o):
                p = np.zeros((8, 12, 12), complex)
                for (a, b), val in X.items():
                    va, ca = VERTS[a]; vb, cb = VERTS[b]
                    if any(x >= 2 for x in vb): continue
                    p[SI[tuple(vb)], CI[ca], CI[cb]] += val
                pieces.setdefault((oi, twist), []).append(p / np.abs(p).max())
def g0_perm(twist, choice): return sum(pieces[(oi, twist)][ci] for oi, ci in enumerate(choice))
CHOICES = [(tw, ch) for tw in (False, True) for ch in itertools.product(*[range(len(pieces[(oi, False)])) for oi in range(6)])]
check("G0 perm parts rebuilt: 2 x 64", len(CHOICES) == 128)
PH4 = np.array([1, 1j, -1, -1j])
def g0(tw, ch, alpha): return {(0, 0, 0): PH4[np.asarray(alpha)][ORB][:, :, None] * g0_perm(tw, ch)}
A0perm = [(tw, ch) for tw, ch in CHOICES if tw and all(np.allclose(np.abs(p), np.abs(A0)) for p in g0_perm(tw, ch))]
ID = [(tw, ch) for tw, ch in CHOICES if (not tw) and all(np.allclose(np.abs(p), np.eye(12)) for p in g0_perm(tw, ch))]
check("exactly one G0 perm part has |entries| = identity (chi=1) and one = |A0| (chi=A2) on every sublattice", len(ID) == 1 and len(A0perm) == 1)

# ---- (e) a R_L b, all perm-part pairs: pattern test first (phase-free), then Z4 phase solve
RB = const(blL)
pat_ok = []
for (ta, ca) in CHOICES:
    pa = {(0, 0, 0): g0_perm(ta, ca)}
    for (tb, cb) in CHOICES:
        pb = {(0, 0, 0): g0_perm(tb, cb)}
        X = mul(pa, mul(RB, pb))
        if all(np.all((np.abs(B) > 1e-9) == (np.abs(B[:1]) > 1e-9)) for B in X.values()): pat_ok.append(((ta, ca), (tb, cb)))
okpat = all(a in ID + A0perm and b in ID + A0perm for a, b in pat_ok)
check("lemma: a R_L b (a, b in G0) has an s-independent support pattern only if both perm parts are 1 or the A0 permutation (all 128^2 pairs)",
      okpat, f"{len(pat_ok)} pattern-admissible pairs")
# phases: a = Z_alpha a0, b = b0 Z_beta;  entry (s,d,i,j) of a0 R b0 gets phase alpha[ORB[s+d,i]] + beta[ORB[s,j]]
AL = np.array(list(itertools.product(range(4), repeat=6)))
found = {}
for (A, B) in pat_ok:
    X0 = mul({(0, 0, 0): g0_perm(*A)}, mul(RB, {(0, 0, 0): g0_perm(*B)}))
    eqA = []; eqB = []; base = []
    for d, Bk in X0.items():
        ii, jj = np.nonzero(np.abs(Bk[0]) > 1e-9)
        for i, j in zip(ii, jj):
            for s in range(1, 8):      # compare sublattice s with sublattice 0
                ph = np.angle(Bk[s, i, j] / Bk[0, i, j]) / (np.pi / 2)
                eqA.append((ORB[smod(s, d), i], ORB[smod(0, d), i])); eqB.append((ORB[s, j], ORB[0, j])); base.append(int(round(ph)) % 4)
    eqA = np.array(eqA); eqB = np.array(eqB); base = np.array(base)
    ka = (AL[:, eqA[:, 0]] - AL[:, eqA[:, 1]] + base[None]) % 4         # alpha part + base
    kb = (-(AL[:, eqB[:, 0]] - AL[:, eqB[:, 1]])) % 4                  # need beta part == -(alpha part + base)
    dict_b = {}
    for ib, row in enumerate(kb): dict_b.setdefault(row.tobytes(), []).append(ib)
    for ia, row in enumerate(ka):
        for ib in dict_b.get(row.tobytes(), []):
            X = mul(g0(*A, AL[ia]), mul(RB, {(0, 0, 0): g0_perm(*B) * PH4[AL[ib]][ORB][:, None, :]}))
            assert is_ti(X)
            key = tuple(np.round(np.concatenate([X[d][0].ravel() for d in sorted(X)]), 6))
            found.setdefault(key, (A, B, X))
print(f"  distinct translation-invariant a R_L b: {len(found)}  [{time.time() - t0:.0f}s]")
KS = np.random.default_rng(5).uniform(-np.pi, np.pi, (4, 3))
def blochX(X, k): return sum(B[0] * np.exp(1j * np.dot(k, d)) for d, B in X.items())
def ident(X):
    for nm, f in (('R_L', RLk), ('Rt', RLt), ('A0 R_L', lambda k: A0 @ RLk(k)), ('R_L A0', lambda k: RLk(k) @ A0)):
        for z in PH4:
            if all(np.allclose(blochX(X, k), z * f(k)) for k in KS): return f"{z:.0f}*{nm}".replace('(', '').replace(')', '')
    return None
ids = [ident(X) for (_, _, X) in found.values()]
print("  identified:", collections.Counter(ids))
check("every translation-invariant a R_L b (a, b in G0, all phases) is z*{R_L, Rt, A0 R_L, R_L A0}: an old word up to a phase", all(i is not None for i in ids))

# ---- (f) bounded random search of 3-letter mixed words with NON-invariant G0 letters
rng = np.random.default_rng(2026)
OLDL = {'R': RB, 'S': const(blS), 'Si': inv(const(blS)), 'Lx': {(0, 0, 0): np.broadcast_to(PC['L132'], (8, 12, 12)).copy()},
        'Hx': {(0, 0, 0): np.broadcast_to(PC['H21'], (8, 12, 12)).copy()}}
names = list(OLDL); NTRY = 20000; nti = 0; nontriv = []; t1 = time.time()
for it in range(NTRY):
    m = [names[i] for i in rng.integers(0, len(names), 3)]
    gs = [CHOICES[i] for i in rng.integers(0, 128, 2)]; al = rng.integers(0, 4, (2, 6))
    if rng.random() < 0.5: gs[1] = gs[0]; al[1] = al[0]; inverse_second = True
    else: inverse_second = False
    g1 = g0(*gs[0], al[0]); g2 = inv(g0(*gs[1], al[1])) if inverse_second else g0(*gs[1], al[1])
    W = mul(OLDL[m[0]], mul(g1, mul(OLDL[m[1]], mul(g2, OLDL[m[2]]))))
    if is_ti(W):
        nti += 1
        if not (is_ti(g1) and is_ti(g2)): nontriv.append((m, gs, al.tolist(), inverse_second, W))
print(f"  random 3-letter mixed words: {NTRY} tried, translation-invariant {nti}, of which with non-invariant G0 letters {len(nontriv)}  [{time.time() - t1:.0f}s]")
# speeds at k* for those: compressed derivative of the 12x12 Bloch matrix on D+, D-
def kstar_speeds(W):
    out = []
    for D in (Dp, Dm):
        fg = lambda k: (blochX(W, k), [sum(1j * d[j] * B[0] * np.exp(1j * np.dot(k, d)) for d, B in W.items()) for j in range(3)])
        isc, sc, h = compressed_velocity(fg, kst, D); iso, v = iso_speed(h); out.append((isc, iso, v))
    return out
bad = 0; spd = collections.Counter()
for m, gs, al, invs, W in nontriv:
    ns = sum({'S': 1, 'Si': -1}.get(x, 0) for x in m)
    for isc, iso, v in kstar_speeds(W):
        spd[(isc, iso, round(v, 6))] += 1
        if isc and abs(v - abs(ns) * np.sqrt(2) / 3) > 1e-8: bad += 1
print("  k* (scalar on D, isotropic, speed) counts:", dict(spd))
for m, gs, al, invs, W in nontriv:
    print("   word", m, "G0 letters", gs, "phases", al, "second = inverse of first" if invs else "", "| W =", ident(W) or ('on-site' if list(W) == [(0, 0, 0)] else 'other'),
          "| G0 letters are pure phases:", [bool(all(np.allclose(np.abs(p), np.eye(12)) for p in g0_perm(*g))) for g in gs])
check("in the random mixed-word sample, every translation-invariant word with non-invariant G0 letters has k* D+/D- speed = |n_S| sqrt2/3 (no new velocity source found)", bad == 0, f"{len(nontriv)} words")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
