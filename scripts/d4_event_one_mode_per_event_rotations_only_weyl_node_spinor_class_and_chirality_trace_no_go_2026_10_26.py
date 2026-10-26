AUDIT_INPUT_PATHS = ('docs/D4_EVENT_ONE_MODE_PER_EVENT_ROTATIONS_ONLY_WEYL_NODE_SPINOR_CLASS_AND_CHIRALITY_TRACE_NO_GO_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-chiral-rotations-only: can one fermion mode per D4 event host a single Weyl node protected by a rotations-only
subgroup G of W(F4)?  Exact group/representation facts + finite kernel diagnostics.  Seeded, numpy only."""
import itertools, time
import numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok); print(("PASS " if ok else "FAIL ") + name + (": " + info if info else ""))
def refl(n):
    n = np.array(n, float); return np.eye(4) - 2 * np.outer(n, n) / n.dot(n)
key = lambda A: tuple(np.rint(2 * A).astype(int).ravel())
FV = [np.array(v, float) for v in ([0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 0, 1], [.5, -.5, -.5, -.5])]
els = {key(np.eye(4)): np.eye(4)}; fr = [np.eye(4)]; GEN = [refl(v) for v in FV]
while fr:
    nf = []
    for A in fr:
        for g in GEN:
            B = g @ A
            if key(B) not in els: els[key(B)] = B; nf.append(B)
    fr = nf
WA = np.array(list(els.values())); N = len(WA)
enc = lambda K: (np.rint(2 * K).astype(int) + 2).reshape(K.shape[0], 16) @ (5 ** np.arange(16))
cod = enc(WA); od = np.argsort(cod); sc = cod[od]; idx = lambda K: od[np.searchsorted(sc, enc(K))]
MT = np.array([idx(np.einsum('ab,nbc->nac', WA[i], WA)) for i in range(N)]); E = idx(np.eye(4)[None])[0]
DET = np.array([round(np.linalg.det(A)) for A in WA]); TR = np.trace(WA, axis1=1, axis2=2); MONE = idx(-np.eye(4)[None])[0]
def qm(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0])
cj = lambda q: q * np.array([1, -1, -1, -1]); I4 = np.eye(4)
BQ = {(a, b): np.array([qm(qm(I4[a], I4[j]), cj(I4[b])) for j in range(4)]).T for a in range(4) for b in range(4)}
def lift(A):  # A x = l x conj(r)
    T = np.array([[np.sum(BQ[(a, b)] * A) / 4 for b in range(4)] for a in range(4)])
    i = np.argmax(np.linalg.norm(T, axis=1)); r = T[i] / np.linalg.norm(T[i]); return T @ r, r
ROT = [i for i in range(N) if DET[i] > 0]; LR = {i: lift(WA[i]) for i in ROT}
lerr = max(np.abs(np.array([qm(qm(LR[i][0], I4[j]), cj(LR[i][1])) for j in range(4)]).T - WA[i]).max() for i in ROT)
check("C1 [T] W(F4) = 1152, rotations W(F4)+ = 576 contain -1; every rotation lifts to Spin(4): A x = l x rbar", N == 1152 and len(ROT) == 576 and MONE in ROT and lerr < 1e-12, f"lift err {lerr:.0e}")
def hk(A, k):
    c = np.zeros(k + 1, complex); c[0] = 1
    for l in np.linalg.eigvals(A): c = np.array([sum(c[i] * l ** (j - i) for i in range(j + 1)) for j in range(k + 1)])
    return c[k].real
HK3 = np.array([hk(A, 3) for A in WA]); HK4 = np.array([hk(A, 4) for A in WA])
TRS2 = {i: (2 * LR[i][0][0] + 2 * LR[i][1][0]) ** 2 for i in ROT}
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
rng = np.random.default_rng(7); GOT = {}
for t in range(3000):
    g2 = [int(x) for x in rng.integers(N, size=2)]; H = close(g2)
    if len(H) >= 48 and H not in GOT and all(DET[h] > 0 for h in H) and abs(HK4[list(H)].mean() - 1) < 1e-9: GOT[H] = g2
GI = [idx(refl(v)[None])[0] for v in FV]; gp = [int(MT[GI[0], GI[i]]) for i in (1, 2, 3)] + [int(MT[GI[1], GI[2]]), int(MT[GI[2], GI[3]])]
GOT[close(gp)] = gp
prot = lambda H: abs(np.mean([HK3[h] * TRS2[h] for h in H]) - 2) < 1e-9  # parent criterion: quartic 1 + cubic spinor covariant 2
PR = sorted([H for H in GOT if prot(H)], key=len); UP = [H for H in GOT if not prot(H)]
# ---- spinor class: z = (-1,-1) in [Ghat, Ghat] ?
kq = lambda v: tuple(np.rint(v * 1000).astype(int)); mul = lambda a, b: np.concatenate([qm(a[:4], b[:4]), qm(a[4:], b[4:])])
inv = lambda a: np.concatenate([cj(a[:4]), cj(a[4:])]); Z8 = np.array([-1., 0, 0, 0, -1, 0, 0, 0]); E8 = np.array([1., 0, 0, 0, 1, 0, 0, 0])
def gclose(gs):
    S = {kq(E8): E8}; fr = [E8]
    while fr:
        nf = []
        for h in fr:
            for g in gs:
                x = mul(g, h)
                if kq(x) not in S: S[kq(x)] = x; nf.append(x)
        fr = nf
    return S
def spin_nontrivial(gens):
    L = [np.concatenate(LR[g]) for g in gens]; D = gclose([mul(mul(a, b), mul(inv(a), inv(b))) for a in L for b in L])
    while True:
        new = [mul(mul(g, x), inv(g)) for g in L for x in D.values()]
        if all(kq(x) in D for x in new): return kq(Z8) in D
        D = gclose(list(D.values()) + new)
orders = sorted({len(H) for H in PR}); allm1 = all(MONE in H for H in PR)
spn = [spin_nontrivial(GOT[H]) for H in PR]; spu = [spin_nontrivial(GOT[H]) for H in UP]
check("C2 [F] seeded sample: protected rotations-only groups (quartic 1, cubic spinor covariant 2) have orders 96-576, all contain -1",
      orders == [96, 192, 288, 576] and allm1, f"{len(PR)} groups, orders {orders}")
check("C3 [T] spinor class NONTRIVIAL for every protected group (z in [Ghat,Ghat]: no 1-dim lambda with lambda(z) = -1, so S+ is not a genuine G-rep up to phase); contrast: trivial for some unprotected ones",
      all(spn) and not all(spu), f"protected nontrivial {sum(spn)}/{len(spn)}; unprotected nontrivial {sum(spu)}/{len(spu)}")
# ---- H^1(G, D4/2D4) and cocycles
TB = np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]]).T; TBi = np.linalg.inv(TB)
M2 = [np.rint(TBi @ A @ TB).astype(int) % 2 for A in WA]
def rref2(R):
    R = R.copy() % 2; piv = []; r = 0
    for c in range(R.shape[1]):
        p = [i for i in range(r, R.shape[0]) if R[i, c]]
        if not p: continue
        R[[r, p[0]]] = R[[p[0], r]]
        for i in range(R.shape[0]):
            if i != r and R[i, c]: R[i] ^= R[r]
        piv.append(c); r += 1
    return R, piv
def cocycles(gens):
    d = 4; nv = d * len(gens); Bm = {E: np.zeros((d, nv), int)}; fr = [E]; rows = []
    while fr:
        nf = []
        for h in fr:
            for t, gi in enumerate(gens):
                j = MT[gi, h]; bg = np.zeros((d, nv), int); bg[:, t * d:(t + 1) * d] = np.eye(d, dtype=int); new = (bg + M2[gi] @ Bm[h]) % 2
                if j in Bm: rows.append((new - Bm[j]) % 2)
                else: Bm[j] = new; nf.append(j)
        fr = nf
    R, piv = rref2(np.vstack(rows)); Zs = []
    for f in [c for c in range(nv) if c not in piv]:
        v = np.zeros(nv, int); v[f] = 1
        for i, c in enumerate(piv): v[c] = R[i, f]
        Zs.append(v)
    fix = d - len(rref2(np.vstack([(M2[g] - np.eye(d, dtype=int)) % 2 for g in gens]))[1])
    return Bm, Zs, len(Zs) - (d - fix)
VEC = np.array(list(itertools.product([0, 1], repeat=4))); XC = (TB @ VEC.T).T.astype(float)
cls = lambda X: (np.rint(X @ TBi.T).astype(int) % 2) @ np.array([8, 4, 2, 1])
BD = np.array([[1, 0, 0, .5], [0, 1, 0, .5], [0, 0, 1, .5], [0, 0, 0, .5]]); BDi = np.linalg.inv(BD)
PS = [BD @ np.array(m) / 4 for m in itertools.product([0, 1], repeat=4)]  # -1 in G => G-fixed momenta lie in (1/4)D4* mod (1/2)D4*
fixedP = lambda H: [P for P in PS if all(np.abs(2 * BDi @ (WA[h] @ P - P) - np.rint(2 * BDi @ (WA[h] @ P - P))).max() < 1e-9 for h in H)]
h1 = {H: cocycles(list(GOT[H]))[2] for H in PR}; nPf = {len(fixedP(H)) for H in PR}
check("C4 [T] H^1(G, D4/2D4) = 0 for orders 288, 576 (every realisation, any phases, fixes an event class: genuine Bloch module); 1-2 for orders 96, 192 (nonsymmorphic realisations exist); every protected G fixes ONLY P = 0 of the cell zone",
      all(h1[H] == 0 for H in PR if len(H) >= 288) and all(h1[H] > 0 for H in PR if len(H) < 288) and nPf == {1},
      f"H^1 by order {sorted({(len(H), h1[H]) for H in PR})}")
# ---- C5 finite: most general invariant kernel (shells |d|^2 <= 6), psibar twisted by any 1-dim character, every realisation
SH = np.array([v for v in itertools.product(range(-2, 3), repeat=4) if sum(v) % 2 == 0 and np.dot(v, v) <= 6], float)
SHk = {tuple(np.rint(s).astype(int)): i for i, s in enumerate(SH)}; TGT = cls(XC[:, None, :] + SH[None, :, :]); RNG = np.random.default_rng(1)
INVW = np.array([np.where(MT[i] == E)[0][0] for i in range(N)])
def chars(H, gens):
    C = {MT[MT[a, b], MT[INVW[a], INVW[b]]] for a in gens for b in gens}; D = set(close(list(C)))
    while True:
        new = {MT[MT[g, x], INVW[g]] for g in gens for x in D}
        if new <= D: break
        D = set(close(list(D | new)))
    n = len(H) // len(D); w = np.exp(2j * np.pi * np.arange(n) / n); out = []
    for vals in itertools.product(range(n), repeat=len(gens)):
        ch = {E: 1 + 0j}; fr = [E]; ok = True
        while fr and ok:
            nf = []
            for h in fr:
                for t, g in enumerate(gens):
                    j = MT[g, h]; v = w[vals[t]] * ch[h]
                    if j in ch: ok = ok and abs(ch[j] - v) < 1e-9
                    else: ch[j] = v; nf.append(j)
            fr = nf
        if ok: out.append(ch)
    return out
def mat(Kc, w):
    D = np.zeros((16, 16), complex); np.add.at(D, (np.repeat(np.arange(16), len(SH)), TGT.ravel()), (Kc * w[None, :]).ravel()); return D
dims = set(); nzero = 0; w1max = 0.; isomin = 1e9; ncase = 0; inverr = 0.
for H in [PR[0], PR[1], next(h for h in PR if len(h) == 192), PR[-2], PR[-1]]:
    Hl = list(H); gens = list(GOT[H]); Bm, Zs, _ = cocycles(gens); chs = chars(Hl, gens)
    for k in [0] + [1 << i for i in range(len(Zs))]:
        zv = (sum(Zs[i] for i in range(len(Zs)) if (k >> i) & 1) % 2) if k else np.zeros(4 * len(gens), int)
        perms = []
        for h in Hl:
            nc = cls(XC @ WA[h].T + (TB @ ((Bm[h] @ zv) % 2)).astype(float)); nd = np.rint(SH @ WA[h].T).astype(int)
            perms.append((nc[:, None] * len(SH) + np.array([SHk[tuple(v)] for v in nd])[None, :]).ravel())
        perms = np.array(perms)
        for chi in chs:
            cv = np.array([chi[h] for h in Hl]); K = RNG.normal(size=16 * len(SH)) + 1j * RNG.normal(size=16 * len(SH))
            KR = (np.conj(cv)[:, None] * K[perms]).mean(0); inverr = max(inverr, np.abs(KR[perms] - cv[:, None] * KR[None, :]).max())
            Kc = KR.reshape(16, len(SH)); D0 = mat(Kc, np.ones(len(SH))); U, s, Vh = np.linalg.svd(D0); nz = int((s < 1e-9 * s.max()).sum())
            dims.add(nz); ncase += 1
            if nz:
                Q = Vh.conj().T[:, -nz:]; Qp = U[:, -nz:]; Dm = [mat(Kc, 1j * SH[:, m]) for m in range(4)]; Lm = [Qp.conj().T @ X @ Q for X in Dm]
                ps = RNG.normal(size=(40, 4)); ps /= np.linalg.norm(ps, axis=1)[:, None]
                sv = np.array([np.linalg.svd(sum(p[m] * Lm[m] for m in range(4)), compute_uv=False) for p in ps]) / np.linalg.norm(D0, 2)
                if nz == 1 or sv.max() < 1e-9: w1max = max(w1max, sv.max()) if nz == 1 else w1max; nzero += (nz > 1)
                else: isomin = min(isomin, (sv.max(1) / np.maximum(sv.min(1), 1e-300)).max())
check("C5 [F] most general invariant kernel (shells |d|^2<=6, 145 hops), every sampled realisation (tau) and psibar character twist: forced light blocks at P = 0 are never 2-dim; 1-dim blocks have zero linear term; larger blocks have L = 0 or are anisotropic",
      2 not in dims and w1max < 1e-9 and isomin > 1.5 and inverr < 1e-12, f"{ncase} cases, forced dims {sorted(dims)}, 1-dim |L|/|D0| {w1max:.0e}; larger: {nzero} with L = 0, others min anisotropy {isomin:.1f}")
# ---- C6/C7: spin-class (nonsymmorphic + phase) realisations: modules = induced from stabiliser characters with z -> -1
def hat(Hl):
    el = []; img = []
    for h in Hl:
        for s in (1, -1): el.append(np.concatenate([s * LR[h][0], s * LR[h][1]])); img.append(h)
    Kd = {kq(e): i for i, e in enumerate(el)}; return el, img, np.array([[Kd[kq(mul(a, b))] for b in el] for a in el]), Kd
def subchars(sub, MTh, zi, ei, sgn):
    sub = list(sub); INVh = {a: [b for b in sub if MTh[a, b] == ei][0] for a in sub}
    C = {MTh[MTh[a, b], MTh[INVh[a], INVh[b]]] for a in sub for b in sub}; D = set(C) | {ei}; fr = list(D)
    while fr:
        nf = []
        for a in fr:
            for b in C:
                c = MTh[a, b]
                if c not in D: D.add(c); nf.append(c)
        fr = nf
    cos = {}; reps = []
    for a in sub:
        if a in cos: continue
        reps.append(a)
        for d in D: cos[MTh[a, d]] = len(reps) - 1
    m = len(reps); R = np.zeros((m, m, m))
    for i, a in enumerate(reps):
        for j, b in enumerate(reps): R[i, cos[MTh[a, b]], j] = 1
    _, v = np.linalg.eig(sum(np.random.default_rng(3).normal(size=m)[i] * R[i] for i in range(m))); out = []
    for k in range(m):
        x = v[:, k]; j = np.argmax(abs(x)); vals = np.array([(R[i] @ x)[j] / x[j] for i in range(m)]); ch = {a: vals[cos[a]] for a in sub}
        if abs(ch[zi] - sgn) < 1e-8: out.append(ch)
    return out
nreal = 0; badtr = 0; trs = set(); dirac = 0; weylpair = 0
for H in PR:
    if len(H) >= 288: continue
    Hl = list(H); gens = list(GOT[H]); Bm, Zs, _ = cocycles(gens); el, img, MTh, Kd = hat(Hl); n = len(el)
    zi = Kd[kq(Z8)]; ei = Kd[kq(E8)]; mi = Kd[kq(np.array([1., 0, 0, 0, -1, 0, 0, 0]))]; INVh = np.array([np.where(MTh[a] == ei)[0][0] for a in range(n)])
    al = subchars(range(n), MTh, zi, ei, 1); Sp = np.array([2 * e[0] for e in el]); Sm = np.array([2 * e[4] for e in el])
    for k in range(1, 2 ** len(Zs)):
        zv = sum(Zs[i] for i in range(len(Zs)) if (k >> i) & 1) % 2
        cm = {h: cls(XC @ WA[h].T + (TB @ ((Bm[h] @ zv) % 2)).astype(float)) for h in Hl}
        if any(all(cm[h][c] == c for h in Hl) for c in range(16)): continue
        nreal += 1; cmh = [cm[img[a]] for a in range(n)]; seen = set(); mods = [np.zeros(n, complex)]
        for c in range(16):
            if c in seen: continue
            orb = {cmh[a][c] for a in range(n)}; seen |= orb; st = [a for a in range(n) if cmh[a][c] == c]; tr = {}
            for a in range(n): tr.setdefault(cmh[a][c], a)
            Ich = []
            for lam in subchars(st, MTh, zi, ei, -1):
                chv = np.zeros(n, complex)
                for g in range(n):
                    for t in tr.values():
                        y = MTh[MTh[INVh[t], g], t]
                        if y in lam: chv[g] += lam[y]
                Ich.append(chv)
            mods = [m + c_ for m in mods for c_ in Ich]
        mods = np.array(mods); trs |= set(np.round(np.abs(mods[:, mi]), 6)); badtr += int(np.ptp(mods[:, mi].real) > 1e-8)
        for a_ in al:
            av = np.array([a_[g] for g in range(n)]); mp = np.rint((np.conj(Sp * av) @ mods.T).real / n); mm = np.rint((np.conj(Sm * av) @ mods.T).real / n)
            dirac += int(((mp >= 1) & (mm >= 1)).any()); weylpair += int(((mp >= 1)[:, None] & (mm >= 1)[None, :] & (mp[None, :] == mp[:, None])).any())
check("C6 [T] spin-class realisations (96, 192; nonsymmorphic tau with no fixed class, U(1) phases): the lifted -1 has the SAME trace on every 16-mode module, so [M_psi] - [M_psibar] = (S+ - S-)alpha (needs trace difference 4) is impossible: no Weyl node, tuned or forced",
      nreal > 0 and badtr == 0 and trs == {8.0}, f"{nreal} realisations, |tr(-1 lift)| = {sorted(trs)}")
check("C7 [T] the same realisations can contain S+alpha and S-alpha together (order 96 only): a Dirac light block at P = 0 is rep-allowed (mass not forbidden; lead for GW)", dirac > 0, f"(realisation, alpha) pairs with a Dirac block: {dirac}")
# ---- C8 Nielsen-Ninomiya bookkeeping on the 2-component control D = sum sigma_mu sin p_mu (sigma = (1, i s))
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1]).astype(complex)
SG = [np.eye(2, dtype=complex), 1j * s1, 1j * s2, 1j * s3]
def chir(Ms):
    A = [np.linalg.inv(Ms[0]) @ M for M in Ms[1:]]; return np.trace(A[0] @ A[1] @ A[2]).real / 2
nodes = list(itertools.product([0, np.pi], repeat=4)); ch = [chir([np.cos(p[m]) * SG[m] for m in range(4)]) for p in nodes]
Rt = refl([1, 1, 0, 0]); Ro = WA[ROT[5]]
cr = chir([sum(Ro[m, n_] * SG[m] for m in range(4)) for n_ in range(4)]); cf = chir([sum(Rt[m, n_] * SG[m] for m in range(4)) for n_ in range(4)])
ct = chir([sum(Rt[m, n_] * SG[m] for m in range(4)).conj().T for n_ in range(4)])
check("C8 [T] NN control: 16 nodes, chiralities +-1, sum 0; a rotation PRESERVES chirality, a plain reflection FLIPS it, the OS map Theta (reflection + dagger) PRESERVES it",
      sorted(ch) == [-1] * 8 + [1] * 8 and abs(sum(ch)) < 1e-12 and cr == 1 and cf == -1 and ct == 1, f"sum {sum(ch):.0f}; rot {cr:+.0f}, refl {cf:+.0f}, Theta {ct:+.0f}")
# ---- C9 real time on a root slice
rt = np.array([1., 1, 0, 0]) / np.sqrt(2); st = [i for i in ROT if np.allclose(WA[i] @ rt, rt)]; st2 = [i for i in ROT if np.allclose(np.abs(WA[i] @ rt), np.abs(rt)) and abs(abs(WA[i] @ rt @ rt) - 1) < 1e-9]
Bp = np.linalg.qr(np.column_stack([rt, np.eye(4)[:, 2], np.eye(4)[:, 3], [1, -1, 0, 0]]))[0][:, 1:]
q3 = np.mean([hk(Bp.T @ WA[i] @ Bp, 4) for i in st]); q3b = np.mean([hk(Bp.T @ WA[i] @ Bp, 4) for i in st2]); impr = sum(DET[i] < 0 for i in st)
check("C9 [T] real-time step on a root slice: rotations fixing the time root = 24 (proper cube group), 48 with time reversal; quartic invariants on transverse R^3 = 2 (no dim-6 protection from the slice symmetry alone); no improper element in G",
      len(st) == 24 and len(st2) == 48 and abs(q3 - 2) < 1e-9 and abs(q3b - 2) < 1e-9 and impr == 0, f"|stab| {len(st)}, {len(st2)}; quartic {q3:.0f}, {q3b:.0f}")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
