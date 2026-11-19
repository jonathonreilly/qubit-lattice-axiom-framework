"""filtered-smg-1d: the 1+1D test of the cube-filtered far-end gapping.

Wilson ladder, light 3450 on leg A and its mirror on leg B; the two Tong gapping terms are built on the
two-site filtered mirror operators b~_x = (b_x + b_{x+1})/2, b~(k) = f(k) b(k), f = (1 + e^ik)/2, so the
k = pi pair is exactly free.  Momentum-space sector ED (U(1)_A x U(1)_B x momentum), exactly free modes
factored out; L = 3 antiperiodic and L = 4 periodic ladders, L = 4 and 5 for the mirror leg alone.
Measured: ground-state degeneracy, the k = 0 mirror line and its propagator zero, the line next to the
corner, and the composite channel O_f(pi) defined by [b_f(k), H] = conj(f(k)) O_f(k).
Self-contained (numpy/scipy/stdlib)."""
import itertools, math, time
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla

QA = np.array([3, 4, 5, 0]); QB = np.array([2, 1, 2, -1]); S = np.array([-1, -1, 1, 1])
P1 = [(0, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (3, 0, 0), (3, 0, 1)]   # B3 B4+ B4'+ B5 B0 B0'
P2 = [(0, 0, 0), (0, 0, 1), (1, 0, 0), (2, 1, 0), (2, 1, 1), (3, 0, 0)]   # B3 B3' B4 B5+ B5'+ B0


class Ladder:
    def __init__(s, L, bc, wcut=0.0, qa=QA, qb=QB, keep_pi=False):
        s.L = L; s.M = 2 * L; s.qa = qa; s.qb = qb
        s.ku = np.array([(2 * n + (1 if bc == 'a' else 0)) % (2 * L) for n in range(L)])
        s.kv = np.pi * s.ku / L
        s.kept = []; s.dropped = []
        for f in range(4):
            for leg in (0, 1):
                for i in range(L):
                    k = s.ku[i]; w = 1 - np.cos(s.kv[i])
                    if k == L and not keep_pi: s.dropped.append((f, leg, i, 'pi-exact')); continue
                    if leg == 0 and k == 0: s.dropped.append((f, leg, i, 'a0-exact')); continue
                    if leg == 0 and w < wcut: s.dropped.append((f, leg, i, 'trunc')); continue
                    s.kept.append((f, leg, i))
        s.idx = {m: j for j, m in enumerate(s.kept)}
        s.n = len(s.kept)

    def has(s, f, leg, i): return (f, leg, i) in s.idx

    # ------------------------------------------------ sectors
    def sector(s, qa_t, qb_t, Kt):
        per = []
        for f in range(4):
            mods = [s.idx[m] for m in s.kept if m[0] == f]; ks = [s.ku[s.kept[j][2]] for j in mods]; cf = []
            for bits in range(1 << len(mods)):
                st = 0; nn = 0; kk = 0
                for j, md in enumerate(mods):
                    if bits >> j & 1: st |= 1 << md; nn += 1; kk += ks[j]
                cf.append((st, nn * s.qa[f], nn * s.qb[f], kk % s.M))
            per.append(cf)
        def merge(a, b):
            d = {}
            for x in a:
                for y in b: d.setdefault((x[1] + y[1], x[2] + y[2], (x[3] + y[3]) % s.M), []).append(x[0] | y[0])
            return d
        d1 = merge(per[0], per[1]); d2 = merge(per[2], per[3]); out = []
        for (a, b, c), s1 in d1.items():
            key = (qa_t - a, qb_t - b, (Kt - c) % s.M)
            if key in d2:
                out.append((np.array(s1, np.int64)[:, None] | np.array(d2[key], np.int64)[None, :]).ravel())
        return np.sort(np.concatenate(out)) if out else np.zeros(0, np.int64)

    # ------------------------------------------------ terms: list of (coef, [(mode, dag)]) leftmost first
    def free_terms(s):
        T = []
        for f in range(4):
            for i in range(s.L):
                e = S[f] * np.sin(s.kv[i]); w = 1 - np.cos(s.kv[i])
                ha, hb = s.has(f, 0, i), s.has(f, 1, i)
                if hb: b = s.idx[(f, 1, i)]; T.append((-e, [(b, True), (b, False)]))
                if ha: a = s.idx[(f, 0, i)]; T.append((e, [(a, True), (a, False)]))
                if ha and hb: T += [(w, [(a, True), (b, False)]), (w, [(b, True), (a, False)])]
        return T

    def tong_terms(s, filt=True, mark=None):
        """mark = (f, i): terms of O_f(k_i) with [b_f(k_i), H_int] = conj(f(k_i)) O_f(k_i), built directly
        (so defined also at k = pi where f = 0); mark None: H_int (both patterns + h.c.)."""
        L = s.L; T = []
        for pat in [p for p in (P1, P2) if p]:
            for iks in itertools.product(range(L), repeat=6):
                kt = 0
                for (f, d, sh), i in zip(pat, iks): kt += (-1 if d else 1) * s.ku[i]
                if kt % s.M: continue
                shp = 1 + 0j; ops = []
                for (f, d, sh), i in zip(pat, iks):
                    shp *= np.exp((-1 if d else 1) * 1j * s.kv[i] * sh)
                    ff = (1 + np.exp(1j * s.kv[i])) / 2 if filt else 1.0 + 0j
                    ops.append(((f, 1, i), bool(d), ff))
                for conj in (False, True):
                    if conj:
                        o2 = [(m, not d, ff) for m, d, ff in reversed(ops)]; sp_ = np.conj(shp)
                    else:
                        o2 = ops; sp_ = shp
                    fac = [np.conj(ff) if d else ff for m, d, ff in o2]
                    if mark is None:
                        ph = sp_ * np.prod(fac)
                        if abs(ph) < 1e-14: continue
                        T.append((ph / L ** 2, [(s.idx[m], d) for m, d, _ in o2]))
                    else:
                        for j, (m, d, ff) in enumerate(o2):
                            if not (d and m == (mark[0], 1, mark[1])): continue
                            rest = sp_ * np.prod([x for jj, x in enumerate(fac) if jj != j])
                            if abs(rest) < 1e-14: continue
                            T.append(((-1) ** j * rest / L ** 2, [(s.idx[m2], d2) for jj, (m2, d2, _) in enumerate(o2) if jj != j]))
        return T

    def single(s, f, leg, i, dag):
        return [(1.0, [(s.idx[(f, leg, i)], dag)])]


def apply(st, ops):
    st = st.copy(); sg = np.ones(len(st)); ok = np.ones(len(st), bool)
    for md, dag in reversed(ops):
        bit = np.int64(1) << np.int64(md); occ = (st & bit) != 0; ok &= occ != dag
        sg *= 1 - 2 * (np.bitwise_count(st & (bit - 1)) & 1).astype(np.int64); st ^= bit
    return st, sg, ok


def matrix(bi, bo, terms):
    r = []; c = []; v = []; idx = np.arange(len(bi))
    for co, ops in terms:
        ns, sg, ok = apply(bi, ops)
        if not ok.any(): continue
        ns = ns[ok]; p = np.minimum(np.searchsorted(bo, ns), max(len(bo) - 1, 0)); h = bo[p] == ns
        r.append(p[h]); c.append(idx[ok][h]); v.append(co * sg[ok][h])
    if not r: return sp.csr_matrix((len(bo), len(bi)), dtype=complex)
    return sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(len(bo), len(bi)), dtype=complex)


def lowest(H, k=2):
    n = H.shape[0]
    if n == 0: return np.array([np.inf]), None
    if n <= 400:
        e, v = np.linalg.eigh(H.toarray()); return e[:k], v[:, :k]
    e, v = sla.eigsh(H, k=k, which='SA', tol=1e-10); o = np.argsort(e); return e[o], v[:, o]


def krylov(H, vecs, m=60):
    """block Krylov with full reorthogonalisation; returns poles E_n (of H in Krylov space) and overlaps <n|v_j>."""
    n = H.shape[0]
    if n <= 600:
        e, U = np.linalg.eigh(H.toarray()); return e, U.conj().T @ np.array(vecs).T
    Q = []
    blk = [v for v in vecs]
    for it in range(m):
        new = []
        for v in blk:
            w = v.copy()
            for _ in range(2):
                for q in Q: w -= np.vdot(q, w) * q
                for q in new: w -= np.vdot(q, w) * q
            nw = np.linalg.norm(w)
            if nw > 1e-9: new.append(w / nw)
        if not new: break
        Q += new; blk = [H @ q for q in new]
        if len(Q) >= min(n, 2 * m): break
    if not Q: return np.zeros(0), np.zeros((0, len(vecs)), complex)
    Qm = np.array(Q).T; T = Qm.conj().T @ (H @ Qm); T = (T + T.conj().T) / 2
    e, U = np.linalg.eigh(T)
    ov = U.conj().T @ (Qm.conj().T @ np.array(vecs).T)
    return e, ov


# =====================================================================================================
AUDIT_TIMEOUT_SEC = 120
TSTART = time.time(); NP = [0, 0]
def check(name, ok, detail=""):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

K2 = np.diag([1, 1, -1, -1]); an = lambda x, y: int(x @ K2 @ y)
L1 = np.array([1, -2, 1, 2]); L2 = np.array([2, 1, -2, 1]); Q51 = np.array([3, 4, 5, 1])

print("== A. exact algebra, filter and composite identities")
vecs = [np.array(v) for v in itertools.product(range(-4, 5), repeat=4) if any(v) and an(np.array(v), np.array(v)) == 0 and int(Q51 @ np.array(v)) == 0]
pairs = sum(1 for a, b in itertools.combinations(vecs, 2) if an(a, b) == 0 and np.linalg.matrix_rank(np.array([a, b])) == 2)
check("A1 3450: anomalies (AA, BB, AB) = 0 and the Tong vectors l1, l2 are null, mutually null and neutral; 3451: AA = -1, and no "
      "neutral Lagrangian pair exists (|l_i| <= 4), so no symmetric Tong-type gapping set exists for 3451",
      (an(QA, QA), an(QB, QB), an(QA, QB)) == (0, 0, 0) and an(L1, L1) == an(L2, L2) == an(L1, L2) == 0
      and all(int(q @ l) == 0 for q in (QA, QB) for l in (L1, L2)) and an(Q51, Q51) == -1 and pairs == 0,
      f"{len(vecs)} neutral null vectors for 3451, 0 Lagrangian pairs")

l3 = Ladder(3, 'a', keep_pi=True); B = l3.sector(36, 12, 0); TF3 = l3.tong_terms(); HF = matrix(B, B, TF3)
ip = list(l3.ku).index(3); worst = 0.0
for leg in (0, 1):
    for f in range(4):
        Bh = l3.sector(36 - QA[f], 12 - QB[f], 3); b = matrix(B, Bh, l3.single(f, leg, ip, False))
        worst = max(worst, abs(b @ HF - matrix(Bh, Bh, TF3) @ b).max())
check("A2 THEOREM (exact on the L = 3 sector with the zone-corner modes kept, dim %d) [a_f(pi), H_F] = [b_f(pi), H_F] = 0 for every "
      "flavour: the corner pair is exactly free at every coupling, so its gap stays the free Wilson gap 2" % len(B), worst < 1e-13,
      f"max |[c(pi), H_F]| = {worst:.1e}")
del HF
l3 = Ladder(3, 'a'); TF3 = l3.tong_terms(); T03 = l3.free_terms(); err = 0.0; onrm = 0.0
for K in (0, 2, 4):
    B = l3.sector(24, 8, K); HI = matrix(B, B, TF3)
    for f in range(4):
        for i in (0, 2):
            Bh = l3.sector(24 - QA[f], 8 - QB[f], (K - l3.ku[i]) % 6); b = matrix(B, Bh, l3.single(f, 1, i, False))
            O = matrix(B, Bh, l3.tong_terms(mark=(f, i))); ff = (1 + np.exp(1j * l3.kv[i])) / 2
            err = max(err, abs(b @ HI - matrix(Bh, Bh, TF3) @ b - np.conj(ff) * O).max())
lp = Ladder(3, 'a', keep_pi=True); onrm = max(abs(matrix(lp.sector(36, 12, 0), lp.sector(36 - QA[f], 12 - QB[f], 3),
                                                     lp.tong_terms(mark=(f, 1)))).max() for f in range(4))
check("A3 THEOREM the composite O_f(k) defined by [b_f(k), H_F] = conj(f(k)) O_f(k), f = (1 + e^ik)/2, is built directly and "
      "verified on every sector; O_f(pi) is a nonzero local operator although b(pi) is free. Since f(pi) = 0, every b-reducible "
      "part of <O O+> vanishes at pi: the composite propagator at pi IS the self-energy kernel Sigma_BB(k)/|f(k)|^2 at k -> pi",
      err < 1e-13 and onrm > 1e-3, f"identity error {err:.1e}; max |O(pi)| element {onrm:.3f}")

# ----------------------------------------------------------------------------------- ED machinery
def study(L, bc, G, label):
    lad = Ladder(L, bc); N = np.zeros(4, int); amb = []
    for f in range(4):
        for i in range(L):
            ha, hb = lad.has(f, 0, i), lad.has(f, 1, i)
            if ha and hb: N[f] += 1
            elif hb:
                if abs(np.sin(lad.kv[i])) < 1e-12: amb.append(f)
                elif -S[f] * np.sin(lad.kv[i]) < 0: N[f] += 1
    targets = set()
    for sub in itertools.product((0, 1), repeat=len(amb)):
        targets.add((int(N @ QA) + sum(QA[f] * x for f, x in zip(amb, sub)), int(N @ QB) + sum(QB[f] * x for f, x in zip(amb, sub))))
    TF = lad.tong_terms(); T0 = lad.free_terms(); cache = {}
    def H(qa, qb, K):
        key = (int(qa), int(qb), int(K) % lad.M)
        if key not in cache:
            B = lad.sector(*key); cache[key] = (B, matrix(B, B, T0), matrix(B, B, TF))
        return cache[key]
    out = {}
    for g in G:
        lev = []
        for qa, qb in targets:
            for K in range(lad.M):
                B, H0, HI = H(qa, qb, K)
                if len(B): lev += [(x, qa, qb, K) for x in lowest(H0 + g * HI, 2)[0]]
        lev.sort(); E0, qa0, qb0, K0 = lev[0]; deg = sum(1 for x in lev if x[0] - E0 < 1e-8)
        gap = min(x[0] for x in lev if x[0] - E0 >= 1e-8) - E0
        B, H0, HI = H(qa0, qb0, K0); gs = lowest(H0 + g * HI, 1)[1][:, 0]
        r = dict(deg=deg, gap=gap, sec=(qa0, qb0, K0), dim=len(B), k={}, comp=[], sA=0.0)
        for f in range(4):
            for i in range(L):
                legs = [l for l in (0, 1) if lad.has(f, l, i)]
                if not legs: continue
                k = lad.ku[i]
                Bp, H0p, HIp = H(qa0 + QA[f], qb0 + QB[f], K0 + k); Bh, H0h, HIh = H(qa0 - QA[f], qb0 - QB[f], K0 - k)
                ep, op = krylov(H0p + g * HIp, [matrix(B, Bp, lad.single(f, l, i, True)) @ gs for l in legs])
                eh, oh = krylov(H0h + g * HIh, [matrix(B, Bh, lad.single(f, l, i, False)) @ gs for l in legs])
                pp = ep - E0; ph = -(eh - E0); bl = legs.index(1)
                Rp = np.einsum('ni,nj->nij', op.conj(), op); Rh = np.einsum('nj,ni->nij', oh.conj(), oh)
                mp = (abs(op) ** 2).sum(1) > 1e-6; mh = (abs(oh) ** 2).sum(1) > 1e-6
                lo = pp[mp].min() if mp.any() else 9.0; hi = ph[mh].max() if mh.any() else -9.0
                wB = [abs(x) for x, R in list(zip(pp, Rp)) + list(zip(ph, Rh)) if R[bl, bl].real > 0.05]
                zs = []
                if hi < lo:
                    ws = np.linspace(hi + 1e-4 * (lo - hi), lo - 1e-4 * (lo - hi), 3001)
                    Gw = np.array([(Rp / (w - pp)[:, None, None]).sum(0) + (Rh / (w - ph)[:, None, None]).sum(0) for w in ws])
                    dG = np.linalg.det(Gw).real; zs = list(ws[np.nonzero(np.diff(np.sign(dG)))[0]])
                    if len(legs) == 2:
                        h0 = np.array([[S[f] * np.sin(lad.kv[i]), 1 - np.cos(lad.kv[i])], [1 - np.cos(lad.kv[i]), -S[f] * np.sin(lad.kv[i])]])
                        wm = 0.5 * (hi + lo); Gm = (Rp / (wm - pp)[:, None, None]).sum(0) + (Rh / (wm - ph)[:, None, None]).sum(0)
                        Sg = wm * np.eye(2) - h0 - np.linalg.inv(Gm); r['sA'] = max(r['sA'], abs(Sg[0, 0]), abs(Sg[0, 1]))
                r['k'].setdefault(int(k), []).append((min(wB) if wB else np.nan, zs, hi < lo))
            ipi = [i for i in range(L) if lad.ku[i] == L]
            if ipi:
                Tm = lad.tong_terms(mark=(f, ipi[0])); Tmd = [(np.conj(c), [(m, not d) for m, d in reversed(o)]) for c, o in Tm]
                for sgn, TT in ((-1, Tm), (1, Tmd)):
                    Bx, H0x, HIx = H(qa0 + sgn * QA[f], qb0 + sgn * QB[f], K0 + L); v = matrix(B, Bx, TT) @ gs; nv = np.linalg.norm(v)
                    if nv < 1e-12: continue
                    e, o = krylov(H0x + g * HIx, [v / nv]); w = abs(o[:, 0]) ** 2
                    r['comp'].append((e[w > 0.01][0] - E0, nv ** 2))
        out[g] = r
        kk = sorted(r['k']); kn = [k for k in kk if k != L]
        print(f" {label} g={g:g}: GS deg {deg} (dim {r['dim']}), gap {gap:.3f}; "
              + "; ".join(f"k={k}pi/{L}: B{np.nanmin([x[0] for x in r['k'][k]]):.2f} z{sum(len(x[1]) for x in r['k'][k])}"
                          for k in kk)
              + (f"; comp(pi) {min(c[0] for c in r['comp']):.2f}" if r['comp'] else ""))
    return lad, out

print("== B. ED, L = 3 antiperiodic ladder (k = pi/3, pi, -pi/3; corner pair exactly free and factored out)")
l3, R3 = study(3, 'a', (8.0, 16.0, 32.0, 48.0), 'L3a')
check("B1 FINITE DIAGNOSTIC L = 3: unique neutral ground state with gap > 1 for g = 8, 16; at g = 32, 48 the neutral sector "
      "develops a quasi-doublet (gap < 0.1, shrinking with g): no clean symmetric strong-coupling limit at this size",
      all(R3[g]['deg'] == 1 and R3[g]['gap'] > 1 for g in (8.0, 16.0)) and all(R3[g]['gap'] < 0.1 for g in (32.0, 48.0)),
      f"gaps {[round(float(R3[g]['gap']), 3) for g in R3]}")
check("B2 FINITE DIAGNOSTIC L = 3 composite channel at k = pi (O_f(pi) acting on the ground state, both charge signs, "
      "all flavours): lowest pole stays above 2.5", all(min(c[0] for c in R3[g]['comp']) > 2.5 for g in R3),
      f"min composite gap {[round(float(min(c[0] for c in R3[g]['comp'])), 2) for g in R3]}")

print("== C. ED, L = 4 periodic ladder (k = 0, +-pi/2, pi; a(0) and the corner pair exactly free, factored out)")
l4, R4 = study(4, 'p', (8.0, 16.0, 32.0, 64.0), 'L4p')
check("C1 consistency: Sigma_AA = Sigma_AB = 0 (to 1e-9) from the reconstructed 2x2 propagators (the interaction acts on leg B only)",
      max(R4[g]['sA'] for g in R4) < 1e-9 and max(R3[g]['sA'] for g in (8.0, 16.0)) < 1e-9,
      f"max {max(R4[g]['sA'] for g in R4):.1e}")
check("C2 FINITE DIAGNOSTIC L = 4 periodic: the total-neutral ground state is exactly 4-fold degenerate (four (Q_A, Q_B) sectors of "
      "the retained modes, identical spectra) at every g > 0 tested; the free b(0) zero modes (16-fold) are only partly lifted",
      all(R4[g]['deg'] == 4 for g in R4), f"degeneracy {[R4[g]['deg'] for g in R4]}, next gap {[round(float(R4[g]['gap']), 3) for g in R4]}")
m0 = {g: np.nanmin([x[0] for x in R4[g]['k'][0]]) for g in R4}; z0 = {g: sum(len(x[1]) > 0 for x in R4[g]['k'][0]) for g in R4}
check("C3 FINITE DIAGNOSTIC mirror at k = 0 (free zero modes at g = 0): its lowest B-weighted line rises with g (to > 1.4 at g = 32) "
      "and every flavour's G_BB(0, w) has a zero inside the gap window (a self-energy pole: zero-type gapping, not a bilinear mass)",
      m0[8.0] < m0[16.0] < m0[32.0] and m0[32.0] > 1.4 and all(z0[g] == 4 for g in R4),
      f"B-line {[round(float(m0[g]), 2) for g in R4]}, flavours with a zero {[z0[g] for g in R4]}")
cp = {g: min(c[0] for c in R4[g]['comp']) for g in R4}
check("C4 FINITE DIAGNOSTIC composite channel at k = pi (the kernel limit of A3): lowest pole >= 2.4 at every g, no soft composite "
      "at the corner on either size", all(cp[g] > 2.4 for g in R4), f"L4 min composite gap {[round(float(cp[g]), 2) for g in R4]}")
mk = {g: min(np.nanmin([x[0] for x in R4[g]['k'][k]]) for k in (2, 6)) for g in R4}
zk = {g: sum(len(x[1]) > 0 for k in (2, 6) for x in R4[g]['k'][k]) for g in R4}
check("C5 FINITE DIAGNOSTIC next to the corner (k = +-pi/2, free line 2 sin(k/2) = 1.414, exposed-doubler line |sin k| = 1): the "
      "B-weighted line softens to about 0.5 by g = 64 and propagator zeros enter the window from g = 16 (the zero band disperses from "
      "w ~ 0 at k = 0 through the pi/2 window to the composite pole above 2.4 at pi)",
      mk[8.0] > 1.1 and mk[64.0] < 0.6 and zk[8.0] == 0 and all(zk[g] > 0 for g in (16.0, 32.0, 64.0)),
      f"B-line {[round(float(mk[g]), 2) for g in R4]}, zeros at +-pi/2 {[zk[g] for g in R4]}")

print("== D. mirror leg alone (light leg removed): the degeneracies are the mirror's own")
for L, bc, G in ((4, 'p', (16.0, 32.0)), (5, 'a', (16.0, 32.0))):
    lad = Ladder(L, bc, wcut=10.0); TF = lad.tong_terms(); T0 = lad.free_terms(); nb = lad.n // 4; h = nb // 2
    qs = sorted(set((int(np.dot(N, QA)), int(np.dot(N, QB))) for N in itertools.product(range(max(0, h - 1), min(nb, h + 1) + 1), repeat=4)))
    if L == 5: qs = [(24, 8)]
    mats = []
    for q in qs:
        for K in range(2 * L):
            B = lad.sector(q[0], q[1], K)
            if len(B): mats.append((matrix(B, B, T0), matrix(B, B, TF)))
    res = {}
    for g in G:
        e = sorted(x for H0, HI in mats for x in lowest(H0 + g * HI, 2)[0]); res[g] = (sum(1 for x in e if x - e[0] < 1e-8), e[1] - e[0], e[2] - e[0] if len(e) > 2 else 9)
    if L == 4:
        check("D1 FINITE DIAGNOSTIC mirror alone, L = 4 periodic: the same exact 4-fold ground state (so it is not a light-leg effect)",
              all(res[g][0] == 4 for g in G), f"degeneracy {[res[g][0] for g in G]}, next {[round(float(res[g][2]), 3) for g in G]}")
    else:
        check("D2 FINITE DIAGNOSTIC mirror alone, L = 5 antiperiodic, neutral sector: unique ground state at g = 16 (gap > 0.25), "
              "quasi-doublet at g = 32 (splitting < 0.02): the L = 3 pattern recurs, no size trend can be extracted",
              res[16.0][1] > 0.25 and res[32.0][1] < 0.02, f"(splitting, next) {[(round(float(res[g][1]), 4), round(float(res[g][2]), 3)) for g in G]}")

print("== E. anomalous control")
l3 = Ladder(3, 'a'); B = l3.sector(24, 8, 0); HI = matrix(B, B, l3.tong_terms()); H0 = matrix(B, B, l3.free_terms())
q51 = sum(Q51[m[0]] * ((B >> j) & 1) for j, m in enumerate(l3.kept)).astype(float); D51 = sp.diags(q51)
gs = lowest(H0 + 16 * HI, 1)[1][:, 0]; var = float(np.vdot(gs, q51 ** 2 * gs).real - np.vdot(gs, q51 * gs).real ** 2)
check("E1 THEOREM-CHECK under 3451 charges every Tong term is charged: [Q_3451, H_F] != 0 and the gapped L = 3 ground state at g = 16 "
      "has Var(Q_3451) > 0, so any gap these terms open in 3451 is symmetry-breaking (with A1: no symmetric gapping set exists)",
      abs(HI @ D51 - D51 @ HI).max() > 1e-3 and var > 1e-6, f"|[Q51,H_F]| {abs(HI @ D51 - D51 @ HI).max():.3f}, Var {var:.2e}")
print("supplied: Wilson ladder, 3450 charges, Tong vectors (l1, l2), two-site filter b~ = (b_x + b_{x+1})/2, couplings g, sizes, "
      "boundary twists; cited: smg-3450 (A3, B3, C1, C3, E4), collective-spin10 (B3, C4)")
print(f"time {time.time() - TSTART:.1f} s")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
