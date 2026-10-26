AUDIT_INPUT_PATHS = ('docs/D4_EVENT_ONE_MODE_PER_EVENT_SPIN_TASTE_SIXTEEN_CELL_FROBENIUS_ORBIT_NO_GO_AND_CHIRAL_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-spin-taste-16: can one fermion mode per D4 event carry protected spin x taste on the 16-event cell D4/2D4?
Exact group / F2 facts plus finite diagnostics. Seeded, self-contained (numpy only)."""
import itertools, time
import numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (": " + info if info else ""))
def refl(n):
    n = np.array(n, float); return np.eye(4) - 2 * np.outer(n, n) / n.dot(n)
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1]).astype(complex); I2 = np.eye(2)
GM = [np.kron(s1, s1), np.kron(s1, s2), np.kron(s1, s3), np.kron(s2, I2)]; G5 = GM[0] @ GM[1] @ GM[2] @ GM[3]
def lift(n):  # Pin lift with Ad = +reflection on gamma.p
    n = np.array(n, float); n /= np.linalg.norm(n); return G5 @ sum(n[i] * GM[i] for i in range(4))
def key(A): return tuple(np.rint(2 * A).astype(int).ravel())
def group(gvecs):
    gens = [(refl(v), lift(v)) for v in gvecs]; els = {key(np.eye(4)): (np.eye(4), np.eye(4, dtype=complex), (0, 0))}; fr = list(els.values())
    while fr:
        nf = []
        for A, L, c in fr:
            for k, (g, l) in enumerate(gens):
                B = g @ A; kk = key(B)
                if kk not in els:
                    cc = list(c); cc[0 if abs(gvecs[k] @ np.array(gvecs[k], float) - 2) < 1e-9 else 1] ^= 1
                    els[kk] = (B, l @ L, tuple(cc)); nf.append(els[kk])
        fr = nf
    v = list(els.values()); return np.array([a for a, _, _ in v]), [l for _, l, _ in v], [c for _, _, c in v]
FV = [np.array(v, float) for v in ([0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 0, 1], [.5, -.5, -.5, -.5])]
WA, LF, CH = group(FV); N = len(WA)
check("C1 W(F4) generated, Pin lift Ad = +A on gamma", N == 1152 and max(np.abs(LF[i] @ GM[a] @ np.linalg.inv(LF[i]) - sum(WA[i][b, a] * GM[b] for b in range(4))).max()
      for i in range(0, N, 37) for a in range(4)) < 1e-12, f"|W| = {N}")
enc = lambda K: (np.rint(2 * K).astype(int) + 2).reshape(K.shape[0], 16) @ (5 ** np.arange(16))
cod = enc(WA); od = np.argsort(cod); sc = cod[od]
def idx(K): return od[np.searchsorted(sc, enc(K))]
MT = np.array([idx(np.einsum('ab,nbc->nac', WA[i], WA)) for i in range(N)]); E = idx(np.eye(4)[None])[0]
GI = [idx(refl(v)[None])[0] for v in FV]
TB = np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]]).T; TBi = np.linalg.inv(TB)
M2 = [np.rint(TBi @ A @ TB).astype(int) % 2 for A in WA]
VEC = np.array(list(itertools.product([0, 1], repeat=4)))
def rk2(A):
    A = A.copy() % 2; r = 0
    for c in range(A.shape[1]):
        p = [i for i in range(r, A.shape[0]) if A[i, c]]
        if not p: continue
        A[[r, p[0]]] = A[[p[0], r]]
        for i in range(A.shape[0]):
            if i != r and A[i, c]: A[i] ^= A[r]
        r += 1
    return r
def subspaces():
    S = set()
    for r in range(5):
        for B in itertools.combinations(range(1, 16), r):
            sp = {0}
            for b in B: sp |= {s ^ b for s in sp}
            S.add(frozenset(sp))
    return S
SUBS = subspaces(); b2i = lambda v: int(''.join(map(str, v)), 2); i2b = lambda i: np.array(list(map(int, format(i, '04b'))))
def inv_subs(Ms): return [sp for sp in SUBS if all(b2i((M @ i2b(v)) % 2) in sp for M in Ms for v in sp)]
def altforms(Ms):
    out = []
    for bits in itertools.product([0, 1], repeat=6):
        F = np.zeros((4, 4), int); k = 0
        for i in range(4):
            for j in range(i + 1, 4): F[i, j] = F[j, i] = bits[k]; k += 1
        if all(((M.T @ F @ M) % 2 == F).all() for M in Ms): out.append(F)
    return out
# ---- C2: forms and invariant subspaces (taste Clifford impossible) ----
MG = [M2[i] for i in GI]; Sp = inv_subs(MG); Spd = inv_subs([M.T for M in MG]); AF = altforms(MG)
B2 = (TB.T @ TB) % 2; R = [v for v in range(16) if not ((B2 @ i2b(v)) % 2).any()]
Rd = [s for s in Spd if len(s) == 4][0]; ann = all(int(i2b(l) @ i2b(a)) % 2 == 0 for l in Rd for a in R)
check("C2 [T] D4/2D4: invariant subspaces 0,R,all (dual 0,R^0,all); invariant alternating forms {0, b}, rank b = 2",
      sorted(map(len, Sp)) == [1, 4, 16] and sorted(map(len, Spd)) == [1, 4, 16] and len(AF) == 2 and sorted(rk2(f) for f in AF) == [0, 2]
      and any((f == B2).all() for f in AF) and len(R) == 4 and ann,
      "graph-type Sigma needs a nondegenerate invariant form (none); (2,2)-type pairs R with R^0 = annihilator (degenerate); so no 4-dim taste Clifford")
# ---- C3: H^1 ----
def H1(gens, Mod):
    d = Mod(E).shape[0]; nv = d * len(gens); Bm = {E: np.zeros((d, nv), int)}; fr = [E]; rows = []
    while fr:
        nf = []
        for h in fr:
            for t, gi in enumerate(gens):
                j = MT[gi, h]; bg = np.zeros((d, nv), int); bg[:, t * d:(t + 1) * d] = np.eye(d, dtype=int)
                new = (bg + Mod(gi) @ Bm[h]) % 2
                if j in Bm: rows.append((new - Bm[j]) % 2)
                else: Bm[j] = new; nf.append(j)
        fr = nf
    z = nv - rk2(np.vstack(rows)); fix = d - rk2(np.vstack([(Mod(g) - np.eye(d, dtype=int)) % 2 for g in gens]))
    return z - (d - fix)
Rb = [i2b(v) for v in R if v][:2]
CB = next(np.array([Rb[0], Rb[1], a, b]).T for a in VEC for b in VEC if rk2(np.array([Rb[0], Rb[1], a, b]).T) == 4)
CBi = np.rint(np.linalg.inv(CB) * round(abs(np.linalg.det(CB)))).astype(int) % 2 if False else None
def inv2(A):
    n = 4; Aug = np.hstack([A % 2, np.eye(n, dtype=int)])
    for c in range(n):
        p = [i for i in range(c, n) if Aug[i, c]][0]; Aug[[c, p]] = Aug[[p, c]]
        for i in range(n):
            if i != c and Aug[i, c]: Aug[i] ^= Aug[c]
    return Aug[:, n:]
CBi = inv2(CB)
h1a = H1(GI, lambda i: M2[i]); h1b = H1(GI, lambda i: ((CBi @ M2[i] @ CB) % 2)[2:, 2:])
check("C3 [T] H^1(W(F4), F2^4) = 0 and H^1(W(F4), F2^4/R) = 0", h1a == 0 and h1b == 0,
      "so any symmetry group mapping onto W(F4) (any shifts, phases) has an event class x whose stabiliser G_x maps onto W(F4)")
# ---- helpers for counts ----
TR2 = np.array([abs(np.trace(L)) ** 2 for L in LF]); DET = np.array([round(np.linalg.det(A)) for A in WA])
def hk(A, k):
    c = np.zeros(k + 1, complex); c[0] = 1
    for l in np.linalg.eigvals(A):
        c = np.array([sum(c[i] * l ** (j - i) for i in range(j + 1)) for j in range(k + 1)])
    return c[k].real
HK3 = np.array([hk(A, 3) for A in WA]); HK4 = np.array([hk(A, 4) for A in WA])
RNG = np.random.default_rng(20261026)
def enddims(Ls):
    X = RNG.normal(size=(16, 16)) + 1j * RNG.normal(size=(16, 16)); X = X + X.conj().T; C = 0
    for L in Ls: U = np.kron(L, L.conj()); C = C + U @ X @ U.conj().T
    ev = np.sort(np.linalg.eigvalsh(C / len(Ls))); d = [1]
    for a, b in zip(ev[:-1], ev[1:]):
        if b - a < 1e-8 * max(1, abs(b)): d[-1] += 1
        else: d.append(1)
    return sorted(d)
def orbits(Ms):
    seen = set(); out = []
    for v in VEC:
        if tuple(v) in seen: continue
        o = {tuple((M @ v) % 2) for M in Ms}; seen |= o; out.append(len(o))
    return sorted(out)
def part(items, bins):
    items = sorted(items, reverse=True)
    def rec(i, b):
        if i == len(items): return all(x == 0 for x in b)
        for k in range(len(b)):
            if b[k] >= items[i]:
                b[k] -= items[i]
                if rec(i + 1, b): return True
                b[k] += items[i]
        return False
    return rec(0, list(bins))
def stats(H):
    H = np.array(H); imp = bool((DET[H] < 0).any())
    return dict(n=len(H), q=HK4[H].mean(), c=(HK3[H] * TR2[H]).mean(), irr=TR2[H].mean(), imp=imp, orb=orbits([M2[h] for h in H]),
                end=enddims([LF[h] for h in H]))
def prot(s): return abs(s['q'] - 1) < 1e-9 and abs(s['c'] - (1 if s['imp'] else 2)) < 1e-9
# ---- C4: Frobenius partition on the stabiliser ----
sW = stats(range(N))
sub = {'kerlong': [i for i in range(N) if CH[i][0] == 0], 'kershort': [i for i in range(N) if CH[i][1] == 0], 'det+': [i for i in range(N) if DET[i] > 0]}
sS = {k: stats(v) for k, v in sub.items()}
check("C4 [T] W(F4): S irreducible, End(S) = 1+1+4+4+6, classes 1+3+12: partition IMPOSSIBLE (no spin x taste, any range/phases/shifts)",
      abs(sW['irr'] - 1) < 1e-9 and sW['end'] == [1, 1, 4, 4, 6] and sW['orb'] == [1, 3, 12] and not part(sW['end'], sW['orb']) and prot(sW),
      f"q={sW['q']:.0f} c={sW['c']:.0f}")
check("C4b [T] index-2 subgroups: both improper ones fail the same way; rotations-only (det+, 576) pass but S = two Weyl halves",
      all(not part(sS[k]['end'], sS[k]['orb']) and prot(sS[k]) and abs(sS[k]['irr'] - 1) < 1e-9 for k in ('kerlong', 'kershort'))
      and part(sS['det+']['end'], sS['det+']['orb']) and prot(sS['det+']) and abs(sS['det+']['irr'] - 2) < 1e-9,
      f"det+ End(S) = {sS['det+']['end']}")
# ---- C5: KS control on Z^4 ----
BA, BL, _ = group([np.array(v, float) for v in ([1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 0, 1])])
BM = [np.rint(A).astype(int) % 2 for A in BA]; bo = orbits(BM); be = enddims(BL)
bq = np.mean([hk(A, 4) for A in BA]); bc = np.mean([hk(A, 3) * abs(np.trace(L)) ** 2 for A, L in zip(BA, BL)])
ksw = altforms(BM); ksF = np.ones((4, 4), int) - np.eye(4, dtype=int)
check("C5 [T] KS control (Z^4, B4 = 384): classes 1+4+6+4+1 = End(S) dims, partition PASSES, KS form invariant; quartic 2, cubic 2: unprotected",
      len(BA) == 384 and bo == [1, 1, 4, 4, 6] and be == [1, 1, 4, 4, 6] and part(be, bo) and any((f == ksF).all() for f in ksw) and abs(bq - 2) < 1e-9 and abs(bc - 2) < 1e-9)
# ---- C6: subgroup sample ----
def close(gs):
    S = {E}; fr = [E]
    while fr:
        nf = []
        for h in fr:
            for g in gs:
                j = MT[g, h]
                if j not in S: S.add(j); nf.append(j)
        fr = nf
    return tuple(sorted(S))
rng = np.random.default_rng(7); got = {}
for t in range(3000):
    H = close(list(rng.integers(N, size=2)))
    if len(H) >= 48 and H not in got:
        s = stats(H)
        if prot(s): got[H] = s
got[tuple(sub['det+'])] = sS['det+']
imp_fail = all(not part(s['end'], s['orb']) for s in got.values() if s['imp'])
prop_pass = all(part(s['end'], s['orb']) and abs(s['irr'] - 2) < 1e-9 for s in got.values() if not s['imp'])
summ = sorted({(s['n'], s['imp']) for s in got.values()})
check("C6 [F] seeded sample of 2-generated subgroups: every protected group with an improper element fails the partition; every protected rotations-only group passes with S reducible",
      imp_fail and prop_pass and len(got) >= 10, f"{len(got)} protected groups (order, improper): {summ}")
# ---- C7: Pauli (KS-type) taste Clifford needs |tr S(A)|^2 <= #fixed classes ----
FIX = np.array([sum(1 for v in VEC if ((M2[i] @ v - v) % 2 == 0).all()) for i in range(N)])
def viol(H): return int(sum(1 for h in H if TR2[h] > FIX[h] + 1e-9 or (round(TR2[h]) - FIX[h]) % 2))
cands = [(H, f) for H in got for f in altforms([M2[h] for h in H]) if rk2(f) == 4]
vs = [viol(H) for H, _ in cands]
check("C7 [T] a KS-type taste Clifford (graph Sigma) makes every symmetry Clifford, so Ad S(A) is a signed Pauli permutation: |tr S|^2 <= Fix(A). Violated by W(F4) and by every sampled protected group with a nondegenerate invariant form",
      viol(range(N)) > 0 and len(cands) > 0 and min(vs) > 0, f"W(F4) violations {viol(range(N))}; {len(cands)} (group, form) candidates, violations min {min(vs)}")
# ---- C8: NN root hops with the candidate dressing: no Clifford sign pattern ----
X16 = [i2b(i) for i in range(16)]; XI = {tuple(x): i for i, x in enumerate(X16)}
def pauli(a, l):
    U = np.zeros((16, 16), complex)
    for i, x in enumerate(X16): U[XI[tuple((x + a) % 2)], i] = (-1) ** (int(l @ x) % 2)
    return 1j * U if int(l @ a) % 2 else U
RP = [np.array(r) for r in sorted({tuple(s * np.array(v)) for v in set(itertools.permutations([1, 1, 0, 0])) for s in itertools.product([1, -1], repeat=4)}) if r[np.nonzero(r)[0][0]] > 0]
RR = np.array(RP, float); found = 0; seen_f = set()
for H, om in cands:
    if key(om) in seen_f: continue
    seen_f.add(key(om)); ph = np.triu(om, 1); GR = np.array([pauli(np.rint(TBi @ r).astype(int) % 2, (ph.T @ (np.rint(TBi @ r).astype(int) % 2)) % 2) for r in RP])
    sh = pauli(np.array([1, 0, 0, 0]), (ph @ np.array([1, 0, 0, 0])) % 2)
    assert all(np.abs(sh @ g - g @ sh).max() < 1e-12 for g in GR)
    for bits in range(2 ** 11):
        s = np.array([1] + [1 - 2 * ((bits >> k) & 1) for k in range(11)], float); G = np.einsum('c,ca,cij->aij', s, RR, GR)
        if max(np.abs(G[a] @ G[b] + G[b] @ G[a] - (12 if a == b else 0) * np.eye(16)).max() for a in range(4) for b in range(a, 4)) < 1e-9: found += 1
check("C8 [F] NN root hops dressed by each candidate form: shifts commute, but none of the 2^11 sign patterns gives a Clifford linear term", found == 0, f"{len(seen_f)} distinct forms")
# ---- C9: KS + Adams control in exact spin-taste form ----
I4 = np.eye(4); Gs = [np.kron(g, I4) for g in GM]; Xi5 = np.kron(I4, G5)  # Adams flavoured mass 1 (x) xi5 (= eps Gamma5 in spin-taste form)
def DKS(p): return 1j * sum(np.sin(p[m]) * Gs[m] for m in range(4))
def DA(p, r=1.): return DKS(p) + r * (np.eye(16) - np.prod(np.cos(p)) * Xi5)
light0 = int(np.sum(np.linalg.svd(DA(np.zeros(4)), compute_uv=False) < 1e-12))
def aniso(Df, nl):
    out = []
    for n in (np.array([1., 0, 0, 0]), np.array([.5, .5, .5, .5])):
        a = []
        for t in (0.02, 0.04):
            sv = np.sort(np.linalg.svd(Df(t * n), compute_uv=False))[:nl]; a.append((sv[-1] ** 2 / t ** 2 - 1) / t ** 2)
        out.append((4 * a[0] - a[1]) / 3)
    return out
ks = aniso(DKS, 16); ad = aniso(DA, 8)
check("C9 [F] KS + Adams flavoured mass r(1 - prod cos 1(x)xi5) (supplied): 8 light modes = 2 tastes x 4 spin; light-mode p^4 coefficient anisotropic for KS (-1/3 axis, -1/12 body) and for Adams",
      light0 == 8 and abs(ks[0] + 1 / 3) < 1e-3 and abs(ks[1] + 1 / 12) < 1e-3 and abs(ad[0] - ad[1]) > 1e-2,
      f"KS axis {ks[0]:.4f} body {ks[1]:.4f}; Adams axis {ad[0]:.4f} body {ad[1]:.4f}")
# ---- C10: taste is not internal ----
check("C10 [T] taste transforms as a spinor under the event stabiliser (T|G_x = S* lambda by Frobenius); KS: 16 = End(S) as B4-module",
      be == bo and abs(sW['irr'] - 1) < 1e-9 and abs(np.mean([abs(np.trace(L)) ** 2 for L in BL]) - 1) < 1e-9)
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
