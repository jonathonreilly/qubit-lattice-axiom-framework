AUDIT_INPUT_PATHS = ('docs/D4_EVENT_ONE_MODE_PER_EVENT_ORDER96_NONSYMMORPHIC_DIRAC_BLOCK_OVERLAP_AND_GAUGE_KINETIC_ANISOTROPY_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-order96-dirac-overlap: one fermion mode per D4 event, order-96 rotations-only protected G, nonsymmorphic flux realisation:
explicit Dirac-block kernel, overlap on it, smooth-background index, invariant counts.  Group/realisation code reused from
d4-chiral-rotations-only.  Seeded, numpy/scipy-free (numpy only), no external files."""
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
SH = np.array([v for v in itertools.product(range(-2, 3), repeat=4) if sum(v) % 2 == 0 and np.dot(v, v) <= 6], float)
SHk = {tuple(np.rint(s).astype(int)): i for i, s in enumerate(SH)}; TGT = cls(XC[:, None, :] + SH[None, :, :]); RNG = np.random.default_rng(1)
INVW = np.array([np.where(MT[i] == E)[0][0] for i in range(N)])
def mat(Kc, w):
    D = np.zeros((16, 16), complex); np.add.at(D, (np.repeat(np.arange(16), len(SH)), TGT.ravel()), (Kc * w[None, :]).ravel()); return D
dims = set(); nzero = 0; w1max = 0.; isomin = 1e9; ncase = 0; inverr = 0.
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
kq = lambda v: tuple(np.rint(v * 1000).astype(int)); mul = lambda a, b: np.concatenate([qm(a[:4], b[:4]), qm(a[4:], b[4:])])
inv = lambda a: np.concatenate([cj(a[:4]), cj(a[4:])]); Z8 = np.array([-1., 0, 0, 0, -1, 0, 0, 0]); E8 = np.array([1., 0, 0, 0, 1, 0, 0, 0])
# ======================= d4-order96-dirac-overlap (new code; group/realisation code above reused from d4-chiral-rotations-only)
print(f"protected rotations-only sample: orders {sorted(len(h) for h in PR)}  [t={time.time()-T0:.1f}s]")
def module_census(H):   # for one order-96 group: realisations without fixed class; orbit sizes holding S+alpha / S-alpha
    Hl = list(H); gens = list(GOT[H]); Bm_, Zs_, _ = cocycles(gens); el_, img_, MTh_, Kd_ = hat(Hl); n_ = len(el_)
    zi_ = Kd_[kq(Z8)]; ei_ = Kd_[kq(E8)]; INV_ = np.array([np.where(MTh_[a] == ei_)[0][0] for a in range(n_)])
    al_ = subchars(range(n_), MTh_, zi_, ei_, 1); Sp_ = np.array([2 * e[0] for e in el_]); Sm_ = np.array([2 * e[4] for e in el_]); pats = set()
    for k in range(1, 2 ** len(Zs_)):
        zv_ = sum(Zs_[i] for i in range(len(Zs_)) if (k >> i) & 1) % 2
        cm_ = {h: cls(XC @ WA[h].T + (TB @ ((Bm_[h] @ zv_) % 2)).astype(float)) for h in Hl}
        if any(all(cm_[h][c] == c for h in Hl) for c in range(16)): continue
        cmh_ = [cm_[img_[a]] for a in range(n_)]; seen = set(); orbs = []
        for c in range(16):
            if c in seen: continue
            orb = {cmh_[a][c] for a in range(n_)}; seen |= orb; st = [a for a in range(n_) if cmh_[a][c] == c]; tr = {}
            for a in range(n_): tr.setdefault(cmh_[a][c], a)
            chs = []
            for lam in subchars(st, MTh_, zi_, ei_, -1):
                chv = np.zeros(n_, complex)
                for g in range(n_):
                    for t in tr.values():
                        y = MTh_[MTh_[INV_[t], g], t]
                        if y in lam: chv[g] += lam[y]
                chs.append(chv)
            orbs.append((len(orb), chs))
        for a_ in al_:
            av = np.array([a_[g] for g in range(n_)]); hp = {o[0] for o in orbs if any(abs(np.conj(Sp_ * av) @ ch) > n_ / 2 for ch in o[1])}
            hm = {o[0] for o in orbs if any(abs(np.conj(Sm_ * av) @ ch) > n_ / 2 for ch in o[1])}
            if hp and hm: pats.add((tuple(sorted(o[0] for o in orbs)), tuple(sorted(hp)), tuple(sorted(hm))))
    return pats
G96 = [h for h in PR if len(h) == 96]; CEN = [module_census(h) for h in G96]; host = [i for i, p in enumerate(CEN) if p]
allp = set().union(*CEN)
check("C1 [F] census of the sampled order-96 protected groups: Dirac-hosting realisations exist for exactly 2 of them; in EVERY one the 16 events split into orbits 4 + 12 with S+alpha and S-alpha on DIFFERENT orbits",
      len(host) == 2 and all(p[0] == (4, 12) and set(p[1]) | set(p[2]) == {4, 12} and not set(p[1]) & set(p[2]) for p in allp), f"{len(host)}/{len(G96)} groups; patterns (orbits, S+ orbit, S- orbit) {sorted(allp)}")
H = G96[host[0]]; Hl = list(H); gens = list(GOT[H]); Bm, Zs, _ = cocycles(gens); el, img, MTh, Kd = hat(Hl); n = len(el)
zi = Kd[kq(Z8)]; ei = Kd[kq(E8)]; INVh = np.array([np.where(MTh[a] == ei)[0][0] for a in range(n)])
al = subchars(range(n), MTh, zi, ei, 1); Sp = np.array([2 * e[0] for e in el]); Sm = np.array([2 * e[4] for e in el])
for kk in range(1, 2 ** len(Zs)):
    zv = sum(Zs[i] for i in range(len(Zs)) if (kk >> i) & 1) % 2; TAU = {h: (TB @ ((Bm[h] @ zv) % 2)).astype(float) for h in Hl}
    cm = {h: cls(XC @ WA[h].T + TAU[h]) for h in Hl}
    if not any(all(cm[h][c] == c for h in Hl) for c in range(16)): break
cmh = [cm[img[a]] for a in range(n)]; ORB = []; seen = set()
for c in range(16):
    if c in seen: continue
    orb = sorted({cmh[a][c] for a in range(n)}); seen |= set(orb); st = [a for a in range(n) if cmh[a][c] == c]; tr = {}
    for a in range(n): tr.setdefault(cmh[a][c], a)
    ORB.append((c, orb, st, tr, subchars(st, MTh, zi, ei, -1)))
def build_U(lch):
    U = np.zeros((n, 16, 16), complex)
    for (c0, orb, st, tr, lams), li in zip(ORB, lch):
        for a in range(n):
            for c in orb: c2 = cmh[a][c]; U[a, c2, c] = lams[li][MTh[MTh[INVh[tr[c2]], a], tr[c]]]
    return U
def light_proj(U, ai):
    av = np.array([al[ai][g] for g in range(n)])
    return 2 / n * np.einsum('a,aij->ij', np.conj(Sp * av), U), 2 / n * np.einsum('a,aij->ij', np.conj(Sm * av), U)
found = None
for lch in itertools.product(*[range(len(o[4])) for o in ORB]):
    U = build_U(lch); chM = np.trace(U, axis1=1, axis2=2)
    for ai in range(len(al)):
        PIp, PIm = light_proj(U, ai)
        if abs(np.trace(PIp) - 2) < 1e-8 and abs(np.trace(PIm) - 2) < 1e-8 and abs(np.mean(np.abs(chM) ** 2) - 6) < 1e-8: found = (lch, ai); break
    if found: break
herr = max(np.abs(U[MTh[a, b]] - U[a] @ U[b]).max() for a in range(n) for b in range(0, n, 11))
OC = np.zeros(16, int)
for oi, o in enumerate(ORB): OC[o[1]] = oi
osz = [len(o[1]) for o in ORB]; i4 = osz.index(4); EPS = np.where(OC == i4, -1.0, 1.0)
inP = [np.trace(PIp[np.ix_(o[1], o[1])]).real for o in ORB]; inM = [np.trace(PIm[np.ix_(o[1], o[1])]).real for o in ORB]
rr = np.random.default_rng(0); Xr = rr.normal(size=(16, 16)) + 1j * rr.normal(size=(16, 16)); Xr += Xr.conj().T
evc, Vc = np.linalg.eigh(np.mean([U[a] @ Xr @ U[a].conj().T for a in range(n)], 0)); grp = []
for i, e in enumerate(evc):
    if grp and abs(e - evc[grp[-1][0]]) < 1e-6: grp[-1].append(i)
    else: grp.append([i])
IRP = [Vc[:, g] @ Vc[:, g].conj().T for g in grp]; dims = sorted(len(g) for g in grp)
check("C2 [T] explicit realisation: 16x16 monomial matrices of Ghat (order 192, nonsymmorphic tau, no fixed class, U(1) phases from stabiliser characters) form a representation with U(z) = -1; module multiplicity-free (<M,M> = 6), irreps 2,2,2,2,2,6; S+alpha (irreducible) lies on the 12-orbit, S-alpha on the 4-orbit; S+ and S- inequivalent",
      herr < 1e-12 and np.abs(U[zi] + np.eye(16)).max() < 1e-12 and dims == [2, 2, 2, 2, 2, 6] and abs(np.mean(np.abs(Sp) ** 2) - 1) < 1e-9 and abs(np.mean(np.conj(Sp) * Sm)) < 1e-9 and inP[i4] < 1e-8 and inM[i4] > 2 - 1e-8,
      f"G gens {gens}, cocycle #{kk}, lambda {found[0]}, alpha #{found[1]}; hom err {herr:.0e}; orbits {osz}")
# ---- light-block and tensor counts (characters over Ghat)
hkG = lambda k: np.array([hk(WA[img[a]], k) for a in range(n)])
cnt = {k: (np.mean(hkG(k) * np.abs(Sp) ** 2).real, np.mean(hkG(k) * np.abs(Sm) ** 2).real, np.mean(hkG(k) * np.conj(Sp) * Sm).real) for k in range(7)}
tot = {k: round(v[0] + v[1] + 2 * v[2]) for k, v in cnt.items()}
check("C3 [T] light Dirac block counts Hom_G(Sym^k V x S_D, S_D) vs SO(4) (= 2 for every k): equal for k <= 3 (isotropic velocity, isotropic p^2 and p^2 g.p: no dim-5/6 LIV); first excess at k = 4, only in the S- chirality block (quartic not (p^2)^2 there); off-diagonal excess at k = 5",
      all(tot[k] == 2 for k in range(4)) and tot[4] > 2 and abs(cnt[4][0] - 1) < 1e-9 and cnt[4][1] > 1.5,
      "k:(++,--,+-) " + " ".join(f"{k}:({cnt[k][0]:.0f},{cnt[k][1]:.0f},{cnt[k][2]:.0f})" for k in range(7)))
# ---- kernels on the fine lattice
SHB = np.array([v for v in itertools.product(range(-2, 3), repeat=4) if sum(v) % 2 == 0 and np.dot(v, v) <= 8], float)
SBk = {tuple(np.rint(s).astype(int)): i for i, s in enumerate(SHB)}; NB = len(SHB); TG = cls(XC[:, None, :] + SHB[None, :, :])
PERM = np.zeros((n, 16 * NB), int); PH = np.zeros((n, 16 * NB), complex)
for a in range(n):
    nd = np.array([SBk[tuple(v)] for v in np.rint(SHB @ WA[img[a]].T).astype(int)]); pc = cmh[a]; PERM[a] = (pc[:, None] * NB + nd[None, :]).ravel()
    ua = U[a][pc, np.arange(16)]; PH[a] = (ua[:, None] * np.conj(ua[TG])).ravel()
avg = lambda K: (np.conj(PH) * K.ravel()[PERM]).mean(0).reshape(16, NB)
MINUS = np.array([SBk[tuple(-np.rint(s).astype(int))] for s in SHB])
def herm(K):
    Kh = np.zeros_like(K); np.add.at(Kh, (TG.ravel(), np.tile(MINUS, 16)), np.conj(K).ravel()); return Kh
def Dmat(K, P):
    D = np.zeros((16, 16), complex); np.add.at(D, (np.repeat(np.arange(16), NB), TG.ravel()), (K * np.exp(1j * SHB @ P)[None, :]).ravel()); return D
def inv_basis(R2):
    B = []; seen_ = np.zeros(16 * NB, bool)
    for i in range(16 * NB):
        c, s = divmod(i, NB)
        if seen_[i] or SHB[s] @ SHB[s] > R2 + 1e-9: continue
        seen_[PERM[:, i]] = True
        for ph in (1, 1j):
            K = np.zeros((16, NB), complex); K[c, s] = ph; T = avg(K)
            if np.abs(T).max() > 1e-9: B.append(T)
    return B
same = (OC[:, None] == OC[TG]).astype(float); rg = np.random.default_rng(20261026)
Akr = sum(rg.normal() * b for b in inv_basis(4)) * (1 - same); Akr = 2.5 * (Akr - herm(Akr))       # Gamma-odd, anti-Hermitian
Rb = [b * same for b in inv_basis(4)]; Rb = [b for b in Rb if np.abs(b).max() > 1e-9]                  # Gamma-even
Cn = np.array([[f(np.trace(Pr @ Dmat(b, np.zeros(4)))) for b in Rb] for Pr in (PIp, PIm) for f in (np.real, np.imag)])
Ns = np.linalg.svd(Cn)[2][np.linalg.matrix_rank(Cn):]
RLs = np.pi * np.array(list(itertools.product(range(-2, 3), repeat=4))) @ BD.T
def farset(Ps): return Ps[np.min(np.linalg.norm(Ps[:, None, :] - RLs[None], axis=2), axis=1) > 0.8]
FS = farset(np.pi * rg.uniform(0, 1, (600, 4)) @ BD.T); PL = PIp + PIm; PHv = np.linalg.svd(np.eye(16) - PL)[0][:, :12]
Wof = lambda Rk, p: sum(Dmat(R, p).conj().T @ Dmat(R, p) for R in Rk)
def normR(Rk):
    lh = np.linalg.eigvalsh(PHv.conj().T @ Wof(Rk, np.zeros(4)) @ PHv).min(); return [R / np.sqrt(lh) for R in Rk]
cands = [normR([sum(c * b for c, b in zip(rg.normal(size=len(Ns)) @ Ns, Rb)) for _ in range(2)]) for _ in range(6)]
wfar = [min(np.linalg.eigvalsh(Wof(Rk, p)).min() for p in FS) for Rk in cands]; Rt = cands[int(np.argmax(wfar))]
M0 = 0.5 * max(wfar)                                                                                     # m0 below the far Wilson floor
dl = 0.05
while True:
    Ru = [R + dl * sum(rg.normal() * b for b in Rb) for R in Rt]
    if np.linalg.svd(np.linalg.svd(PL)[0][:, :4].conj().T @ Wof(Ru, np.zeros(4)) @ np.linalg.svd(PL)[0][:, :4], compute_uv=False).max() < 0.5 * M0: break
    dl /= 2
vA = np.linalg.norm(PIm @ (Dmat(Akr, 1e-5 * I4[0]) - Dmat(Akr, -1e-5 * I4[0])) @ PIp / 2e-5, 2); Akr = Akr * 0.5 / vA  # light speed ~ 0.5
def DWb(P, Rk):
    D = Dmat(Akr, P)
    for R in Rk: RP = Dmat(R, P); D = D + RP.conj().T @ RP
    return D
ierr = max(np.abs(avg(K) - K).max() for K in [Akr] + Rt + Ru)
eqv = max(np.abs(DWb(WA[img[a]] @ P, Rt) - U[a] @ DWb(P, Rt) @ U[a].conj().T).max() for a in range(0, n, 7) for P in rg.normal(size=(2, 4)))
D0 = DWb(np.zeros(4), Rt); u0, s0, v0 = np.linalg.svd(D0); nul = v0[-4:].conj().T; PL = PIp + PIm
cover = np.abs(nul.conj().T @ PL @ nul - np.eye(4)).max()
PGr = np.pi * (np.array(list(itertools.product(range(6), repeat=4)))[1:] / 6) @ BD.T; PGr = np.concatenate([PGr, np.pi * rg.uniform(0, 1, (1500, 4)) @ BD.T])
RL = np.pi * np.array([v for v in itertools.product(range(-2, 3), repeat=4) if True]) @ BD.T
far = PGr[np.min(np.linalg.norm(PGr[:, None, :] - RL[None], axis=2), axis=1) > 0.8]
mins = min(np.linalg.svd(DWb(p, Rt), compute_uv=False).min() for p in far)
epsh = max(np.abs(EPS[:, None] * DWb(p, Rt) * EPS[None, :] - DWb(p, Rt).conj().T).max() for p in far[:20])
QL = nul; QH = np.linalg.svd(np.eye(16) - PL)[0][:, :12]
def aniso(Df, epss=(0.2, 0.1, 0.05)):
    ns = np.random.default_rng(3).normal(size=(12, 4)); ns /= np.linalg.norm(ns, axis=1)[:, None]; out = []
    for e in epss:
        f = []
        for v in ns:
            D = Df(e * v); Dl = QL.conj().T @ D @ QL - QL.conj().T @ D @ QH @ np.linalg.solve(QH.conj().T @ D @ QH, QH.conj().T @ D @ QL)
            f.append(abs(np.linalg.det(Dl)) ** 0.25 / e)
        f = np.array(f); out.append((f.max() - f.min()) / f.mean())
    return np.array(out), np.log(out[0] / out[-1]) / np.log(epss[0] / epss[-1]), f.mean()
an, sl, vel = aniso(lambda p: DWb(p, Rt))
check("C4 [F] finite-range one-mode-per-event kernel D_W = A + sum R^dag R (hops |d|^2 <= 4 per factor): G-invariant, eps-hermitian (eps = orbit sign); D_W(0) has exactly 4 null vectors = the Dirac block; D_W(P) invertible elsewhere (Re<v,Dv> = <v,Wv> > 0)",
      ierr < 1e-12 and eqv < 1e-11 and epsh < 1e-12 and s0[-5] > 0.1 and s0[-4] < 1e-12 and cover < 1e-10 and mins > 1e-2,
      f"invariance {ierr:.0e}, equivariance {eqv:.0e}, eps-herm {epsh:.0e}; sv(D_W(0)) 4 x {s0[-1]:.0e}, next {s0[-5]:.3f}; null = S_D to {cover:.0e}; min sv at distance > 0.8 from P = 0 images: {mins:.3f} (|D_W| {s0[0]:.2f})")
check("C5 [F] light branch of D_W: |det D_eff(p)|^(1/4)/|p| isotropic; anisotropy over 12 directions falls like eps^4 (first LIV at dim 8, none at dim 6)",
      sl > 3.5 and an[-1] < 1e-5, f"velocity {vel:.4f}; anisotropy at eps 0.2/0.1/0.05: {an[0]:.1e}/{an[1]:.1e}/{an[2]:.1e}, slope {sl:.2f}")
# ---- overlap on the UNTUNED kernel
Du0 = DWb(np.zeros(4), Ru); wl = np.linalg.svd(QL.conj().T @ Du0 @ QL, compute_uv=False); wh = np.linalg.eigvalsh(0.5 * (Du0 + Du0.conj().T) + 10 * PL)
def sgn(Hm):
    e, V = np.linalg.eigh(Hm); return (V * np.sign(e)) @ V.conj().T
def Dov(P):
    Hm = EPS[:, None] * (DWb(P, Ru) - M0 * np.eye(16)); Hm = 0.5 * (Hm + Hm.conj().T); return M0 * (np.eye(16) + EPS[:, None] * sgn(Hm))
Do0 = Dov(np.zeros(4)); farP = far; so0 = np.linalg.svd(Do0, compute_uv=False); E_ = np.diag(EPS)
gw = max(np.abs(E_ @ D + D @ E_ - D @ E_ @ D / M0).max() for D in [Do0] + [Dov(p) for p in far[:30]])
minov = min(np.linalg.svd(Dov(p), compute_uv=False).min() for p in far[::3])
eqo = max(np.abs(Dov(WA[img[a]] @ P) - U[a] @ Dov(P) @ U[a].conj().T).max() for a in range(0, n, 13) for P in rg.normal(size=(2, 4)))
ano, slo, velo = aniso(Dov, (0.02, 0.01, 0.005))
check("C6 [F] overlap D_ov = m0 (1 + eps sign(eps (D_W - m0))) on the UNTUNED kernel (light masses nonzero, below m0): GW exact, exactly 4 zero modes at P = 0 with no tuning, no zero modes elsewhere, G-equivariant (the protection survives)",
      wl.min() > 1e-5 and wl.max() < M0 and gw < 1e-12 and so0[-4] < 1e-12 and so0[-5] > 0.5 * M0 and minov > 0.5 * M0 and eqo < 1e-12,
      f"D_W(0) light sv {wl.min():.1e}-{wl.max():.1e}, m0 {M0:.3f}; GW {gw:.0e}; sv(D_ov(0)) 4 x {so0[-1]:.0e}, next {so0[-5]:.3f}; min sv far {minov:.3f}; equivariance {eqo:.0e}")
check("C7 [F] overlap light branch: isotropic, anisotropy falls like eps^4 (dim 6 = 0)", slo > 3.5 and ano[-1] < 1e-6,
      f"velocity {velo:.4f}; anisotropy at eps 0.02/0.01/0.005: {ano[0]:.1e}/{ano[1]:.1e}/{ano[2]:.1e}, slope {slo:.2f}")
print(f"  [t = {time.time() - T0:.1f} s]")
# ---- smooth U(1) backgrounds on the Z^4 box of side 8 (8 Z^4 inside 2D4): index = (Tr eps - Tr sign H)/2
LT = 8; SITES = np.array([x for x in itertools.product(range(LT), repeat=4) if sum(x) % 2 == 0], float)
SID = {tuple(map(int, x)): i for i, x in enumerate(SITES)}; NS = len(SITES); CS = cls(SITES); EPSL = EPS[CS]
def gauged(K, n12, n34):
    f12 = 2 * np.pi * n12 / LT ** 2; f34 = 2 * np.pi * n34 / LT ** 2; M = np.zeros((NS, NS), complex)
    for s in np.nonzero(np.abs(K).max(0) > 1e-14)[0]:
        d = SHB[s]; Y = SITES + d; nn = np.floor(Y / LT); XJ = Y - LT * nn; j = np.array([SID[tuple(map(int, y))] for y in XJ])
        ph = f12 * d[1] * (SITES[:, 0] + d[0] / 2) + f34 * d[3] * (SITES[:, 2] + d[2] / 2) - LT * (f12 * nn[:, 0] * XJ[:, 1] + f34 * nn[:, 2] * XJ[:, 3])
        np.add.at(M, (np.arange(NS), j), K[CS, s] * np.exp(1j * ph))
    return M
def Hbg(n12, n34):
    D = gauged(Akr, n12, n34)
    for R in Ru: Rg = gauged(R, n12, n34); D += Rg.conj().T @ Rg
    D[np.arange(NS), np.arange(NS)] -= M0; return EPSL[:, None] * D
IDX = {}; herm_e = 0; adm = {}
for bg in ((0, 0), (1, 1), (1, -1), (2, 1)):
    Hm = Hbg(*bg); herm_e = max(herm_e, np.abs(Hm - Hm.conj().T).max()); Hm = 0.5 * (Hm + Hm.conj().T)
    if bg == (1, 1): ev, V = np.linalg.eigh(Hm); ev1 = ev
    else: ev = np.linalg.eigvalsh(Hm)
    IDX[bg] = 0.5 * (EPSL.sum() - np.sign(ev).sum()); adm[bg] = np.abs(ev).min() / M0
Qs = {(0, 0): 0, (1, 1): 1, (1, -1): -1, (2, 1): 2}; sg_ = np.sign(IDX[(1, 1)]) if IDX[(1, 1)] else 1
okQ = all(abs(IDX[b] - Q) < 1e-9 for b, Q in Qs.items())
check("C8 [F] gauged overlap on the 2048-event Z^4 box (constant fluxes, Q = n12 n34), index = (Tr eps - Tr sign H)/2: H Hermitian; RECORDED RESULT: index = +Q for Q = 0, 1, 2 but NOT for Q = -1 (index theorem not established at this m0/box)",
      herm_e < 1e-10 and all(abs(IDX[b] - Qs[b]) < 1e-9 for b in ((0, 0), (1, 1), (2, 1))) and not okQ,
      " ".join(f"Q={Q}:{IDX[b]:+.0f}" for b, Q in Qs.items()) + f"; herm {herm_e:.0e}; min|eig H|/m0 " + " ".join(f"{adm[b]:.3f}" for b in Qs))
Eps_ = (V * np.sign(ev1)) @ V.conj().T; del V
Gh = -Eps_; Ph = 0.5 * (np.eye(NS) - Gh); prj = np.abs(Ph @ Ph - Ph).max()
dx = SITES[None] - SITES[:, None]; dx = dx - LT * np.round(dx / LT); dist = np.sqrt((dx ** 2).sum(-1)); Em = np.abs(Gh)
ds = np.unique(np.round(dist, 6)); mx = np.array([Em[np.abs(dist - d) < 1e-6].max() for d in ds]); fs = (ds > 1) & (ds < 4.5)
rate = -np.polyfit(ds[fs], np.log(mx[fs]), 1)[0]; del Em, dist, dx
check("C9 [F] Q = 1: Luscher P_hat = (1 - Gamma_hat)/2 (Gamma_hat = -sign H) is a projector; Tr Gamma_hat = 2 index - Tr eps; Gamma_hat decays exponentially",
      prj < 1e-10 and abs(np.trace(Gh).real - (2 * IDX[(1, 1)] - EPSL.sum())) < 1e-8 and rate > 0.2,
      f"P^2-P {prj:.0e}; Tr Gamma_hat {np.trace(Gh).real:.1f} vs {2 * IDX[(1, 1)] - EPSL.sum():.1f}; decay rate {rate:.2f}/unit (max |Gamma_hat| at |x-y|=2: {mx[np.argmin(abs(ds - 2))]:.1e}, 4: {mx[np.argmin(abs(ds - 4))]:.1e})")
# ---- invariant tensor counts (full V^k, symmetric, gauge kinetic Lambda^2 x Lambda^2, Sym^2 x Sym^2) vs O(4), SO(4)
TRg = np.array([np.trace(WA[h]) for h in Hl]); TR2 = np.array([np.trace(WA[h] @ WA[h]) for h in Hl])
full = [round(np.mean(TRg ** k)) for k in (2, 4, 6)]; symc = [round(np.mean([hk(WA[h], k) for h in Hl])) for k in (2, 4, 6)]
lam2 = round(np.mean(((TRg ** 2 - TR2) / 2) ** 2)); sym2 = round(np.mean(((TRg ** 2 + TR2) / 2) ** 2))
check("C10 [T] tensor counts of G (order 96): full rank 2/4/6 vs O(4) 1/3/15 and SO(4) 1/4/25; symmetric rank 2/4/6 vs SO(4) 1/1/1; <L2,L2> (gauge kinetic) vs SO(4) 2; <S2,S2> vs SO(4) 2",
      full[0] == 1 and symc[:2] == [1, 1], f"full {full}; symmetric {symc}; <L2,L2> {lam2}; <S2,S2> {sym2}")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
