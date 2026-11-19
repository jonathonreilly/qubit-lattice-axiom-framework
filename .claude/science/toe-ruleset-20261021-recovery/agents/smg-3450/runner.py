"""smg-3450: the 1+1D analogue of the register's light/far setup.

Four-flavour Wilson-Dirac two-leg ladder: leg A (light) carries the 3-4-5-0
chiral content (3,4 left-moving, 5,0 right-moving) at k = 0, leg B (far)
carries its mirror; the Wilson rung (1 - cos k) gaps both legs together at
the zone corner k = pi.  U(1)_A = (3,4,5,0), U(1)_B = (2,1,2,-1) act on-site
(vector-like on the lattice).  The Tong/Wang-Wen gapping terms act on leg B.

Sections: A exact algebra; B free ladder, spectral flow; C quadratic
completions (1D corner index); D filtered far-end operators (also 3+1D);
E interacting ED, L = 3 antiperiodic ring (k = pi/3, pi, -pi/3), sector
dim 64444, sparse.  Self-contained (numpy/scipy/stdlib)."""
import itertools, math, time
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = [0, 0]


def check(name, ok, detail=""):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))


QA = np.array([3, 4, 5, 0]); QB = np.array([2, 1, 2, -1]); S = np.array([-1, -1, 1, 1])
K = np.diag([1, 1, -1, -1])                       # left-movers +, right-movers -
L1 = np.array([1, -2, 1, 2]); L2 = np.array([2, 1, -2, 1])

# ---------------------------------------------------------------- A algebra
print("== A. exact algebra of the 3450 gapping data")
an = lambda x, y: int(x @ K @ y)
check("A1 3450 anomaly-free: A^2, B^2, AB = 0; 3451 has A^2 = 9+16-25-1 = -1",
      (an(QA, QA), an(QB, QB), an(QA, QB)) == (0, 0, 0) and an(np.array([3, 4, 5, 1]), np.array([3, 4, 5, 1])) == -1,
      f"(A2,B2,AB) = {(an(QA, QA), an(QB, QB), an(QA, QB))}")
minors = [L1[i] * L2[j] - L1[j] * L2[i] for i in range(4) for j in range(i + 1, 4)]
g = 0
for m in minors: g = math.gcd(g, abs(m))
# charges preserved by both terms: q.l1 = q.l2 = 0  <=>  q in K span(l1,l2)
M = np.array([K @ L1, K @ L2]).T
sol = np.linalg.lstsq(M, np.array([QA, QB]).T, rcond=None)[0]
check("A2 Tong vectors l1 = (1,-2,1,2), l2 = (2,1,-2,1): null, mutually null, neutral; "
      "the preserved charges are exactly K span(l1,l2) = span(q_A, q_B); minors gcd 1 (no leftover discrete breaking)",
      an(L1, L1) == an(L2, L2) == an(L1, L2) == 0 and all(int(q @ l) == 0 for q in (QA, QB) for l in (L1, L2))
      and np.allclose(M @ sol, np.array([QA, QB]).T) and g == 1,
      f"q_A = {sol[:,0].round(3)} , q_B = {sol[:,1].round(3)} in (Kl1,Kl2); gcd {g}")
# theorem: q kept by a Lagrangian L means Kq in L, so q^T K q = 0.  brute force for 3451
q51 = np.array([3, 4, 5, 1]); vecs = []
for v in itertools.product(range(-4, 5), repeat=4):
    v = np.array(v)
    if v.any() and an(v, v) == 0 and int(q51 @ v) == 0: vecs.append(v)
pairs = sum(1 for a, b in itertools.combinations(vecs, 2)
            if an(a, b) == 0 and np.linalg.matrix_rank(np.array([a, b])) == 2)
check("A3 THEOREM a charge kept by a Lagrangian gapping set has q^T K q = 0, so 3451's U(1) (anomaly -1) can never be kept; "
      "brute force |l_i| <= 4: no independent mutually-null neutral pair", pairs == 0,
      f"{len(vecs)} single neutral null vectors, 0 Lagrangian pairs")
ent = [(a, b) for a in range(-6, 7) for b in range(-6, 7) if (a, b) != (0, 0)
       and np.abs(a * L1 + b * L2).max() <= 1]
check("A4 THEOREM (Pauli) every nonzero 3450 gapping vector a l1 + b l2 has an entry |l_i| >= 2 "
      "(entries a+2b and a-2b differ by 4b): no 3450 gapping term exists on a cell with one mode per flavour; "
      "the terms are multi-site (point-split)", len(ent) == 0)

# ---------------------------------------------------------------- B free ladder
print("== B. free ladder: chirality on the legs and anomaly inflow")
def hk(s, k, m=0.0):
    return np.array([[s * np.sin(k), 1 - np.cos(k) + m], [1 - np.cos(k) + m, -s * np.sin(k)]])
ks = np.linspace(-np.pi, np.pi, 2001)
gapo = min(abs(np.linalg.eigvalsh(hk(1, k))).min() for k in ks if abs(k) > 0.05)
e, U = np.linalg.eigh(hk(1, 1e-3)); legA = abs(U[0, 1]) ** 2
e2, U2 = np.linalg.eigh(hk(1, np.pi))
check("B1 per flavour h(k) = s sin k sz + (1-cos k) sx: gapless only at k = 0 where leg A moves with velocity s and leg B with -s; "
      "at the corner k = pi both legs mix fully, gap 2", gapo > 0.04 and legA > 0.999 and np.allclose(abs(e2), 2)
      and abs(abs(U2[0, 0]) ** 2 - 0.5) < 1e-12, f"min |E| off k=0 window {gapo:.3f}; leg-A weight at k=0+ {legA:.6f}")

def pump(qx, Lr=240, steps=12):
    """adiabatic flux 2 pi through U(1)_X: change of leg-A occupation per flavour"""
    out = []
    for f in range(4):
        q = qx[f]; tot = 0.0
        for n in range(Lr):
            k0 = (2 * n + 1) * np.pi / Lr
            e, U = np.linalg.eigh(hk(S[f], k0)); v = U[:, 0]; wa0 = abs(v[0]) ** 2
            nst = max(1, abs(q)) * steps
            for j in range(1, nst + 1):
                k = k0 + 2 * np.pi * q * j / (nst * Lr)
                e, U = np.linalg.eigh(hk(S[f], k)); v = U[:, np.argmax(abs(U.conj().T @ v))]
            tot += abs(v[0]) ** 2 - wa0
        out.append(tot)
    return np.array(out)
pa = pump(QA); pb = pump(QB)
inflow = {'AA': QA @ pa, 'BA': QB @ pa, 'AB': QA @ pb, 'BB': QB @ pb}
check("B2 flux 2 pi of U(1)_A pumps s_f q_A,f particles of flavour f onto the light leg (integers to 1/L^2); "
      "net light-leg charge pumped = sum s q_X q_Y = 0 for all X,Y in {A,B}: no inflow, the far end can be gapped",
      np.allclose(pa, S * QA, atol=0.01) and all(abs(v) < 0.05 for v in inflow.values()),
      f"per flavour {pa.round(3)}; inflow {[(k, round(v, 3)) for k, v in inflow.items()]}")
p51 = pump(q51)
check("B3 3451: flux of its U(1) pumps net charge sum s q^2 = +1 onto the light leg per flux quantum; a gapped symmetric far end "
      "has no low states to supply it, so no symmetric interaction gaps the 3451 far end (anomaly matching)",
      abs(q51 @ p51 - 1) < 0.05, f"pumped {q51 @ p51:.3f}")

# ---------------------------------------------------------------- C quadratic completions
print("== C. zeros of the far leg and the zone corner (exact, 1D index)")
def crossings(hfun, n=4000):
    kk = np.linspace(-np.pi, np.pi, n, endpoint=False) + 1e-4
    neg = np.array([(np.linalg.eigvalsh(hfun(k)) < 0).sum() for k in kk])
    d = np.diff(np.append(neg, neg[0]))
    return kk[np.nonzero(d)[0]], d[np.nonzero(d)]
def h3(s, Vf, ef):
    return lambda k: np.array([[s * np.sin(k), 1 - np.cos(k), 0], [1 - np.cos(k), -s * np.sin(k), Vf(k)],
                               [0, np.conj(Vf(k)), ef(k)]], dtype=complex)
# local (k-independent) zero: Sigma_BB = V^2/omega  <=> hidden level at 0 coupled by const V
kc, dc = crossings(h3(1, lambda k: 0.8, lambda k: 0.0))
check("C1 THEOREM a local far-leg zero (Sigma_BB = V^2/w at every k) leaves zero-energy poles at k = 0 (light) and k = pi "
      "(the doubler, light-leg chirality reversed): the 1D form of the seven top-rung doublers",
      len(kc) == 2 and min(abs(abs(kc) - np.pi)) < 2e-3 and min(abs(kc)) < 2e-3 and dc.sum() == 0,
      f"crossings at {np.round(kc, 3)}")
rng = np.random.default_rng(7); ok = True; nmin = 9
for t in range(40):
    c = rng.normal(size=4); d = rng.normal(size=4) + 1j * rng.normal(size=4)
    ef = lambda k, c=c: sum(c[j] * np.cos(j * k) + 0.5 * c[j] * np.sin((j + 1) * k) for j in range(4))
    Vf = lambda k, d=d: sum(d[j] * np.exp(1j * j * k) for j in range(4))
    kc, dc = crossings(h3(1, Vf, ef), 1500)
    other = [k for k in kc if abs(k) > 0.02]
    ok &= dc.sum() == 0 and (abs(Vf(0)) < 1e-9 or len(other) >= 1); nmin = min(nmin, len(other))
check("C2 THEOREM any local quadratic completion (far leg plus any local hidden band, i.e. a zero with a local dispersion) "
      "obeys Nielsen-Ninomiya: signed crossings sum to 0, so once the mirror at k = 0 is gapped another gapless point exists",
      ok, f"40 random completions; min extra crossings {nmin}")
fV = lambda k: 0.8 * (1 + np.exp(1j * k)) / 2
kc, dc = crossings(h3(1, fV, lambda k: 0.0))
wts = []
for dl in (0.02, 0.04, 0.08):
    e, U = np.linalg.eigh(h3(1, fV, lambda k: 0.0)(np.pi - dl)); j = np.argmin(abs(e))
    wts.append((abs(e[j]), 1 - abs(U[2, j]) ** 2))
sl = np.polyfit(np.log([0.02, 0.04, 0.08]), np.log([w for _, w in wts]), 1)[0]
sle = np.polyfit(np.log([0.02, 0.04, 0.08]), np.log([x for x, _ in wts]), 1)[0]
check("C3 filtering the residue (Sigma_BB = |f(k)|^2 V^2/w, f = (1+e^ik)/2, zero residue at pi) does NOT help: "
      "a soft branch E ~ (k-pi)^3 with physical weight ~ (k-pi)^2 still reaches zero at the corner",
      len(kc) == 2 and min(abs(abs(kc) - np.pi)) < 2e-3 and abs(sle - 3) < 0.15 and abs(sl - 2) < 0.15,
      f"energy slope {sle:.2f}, weight slope {sl:.2f}")

# ---------------------------------------------------------------- D filter algebra (3+1D)
print("== D. filtered far-end operators")
Lc = 4; xs = list(itertools.product(range(Lc), repeat=3)); worst = 0.0
for Q in itertools.product((0, np.pi / 2, np.pi), repeat=3):
    if np.pi not in Q: continue
    bq = np.array([np.exp(-1j * np.dot(Q, x)) for x in xs]) / Lc ** 1.5
    for x in xs[:8]:
        bt = np.zeros(len(xs), complex)
        for dv in itertools.product((0, 1), repeat=3):
            bt[xs.index(tuple((np.array(x) + dv) % Lc))] += 1 / 8
        worst = max(worst, abs(np.vdot(bt, bq)))
check("D1 THEOREM the cube-average slot mode b~_x = (1/8) sum over the 2^3 cube at x anticommutes with b(Q) for every Q with a "
      "component pi (all seven corners and the three faces): any interaction built from b~ leaves those slot modes exactly free",
      worst < 1e-14, f"max |{{b(Q), b~_x^+}}| = {worst:.1e} on 4^3")

# ---------------------------------------------------------------- E interacting ED
print("== E. interacting ED, L = 3 antiperiodic, sector (Q_A,Q_B,K) = (36,12,0)")
Lr = 3; ku = np.array([1, 3, 5]); kv = np.pi * ku / Lr
mode = lambda f, leg, ik: (f * 2 + leg) * Lr + ik

def sector(qa_t, qb_t, Kt, legs=(0, 1)):
    per = []
    for f in range(4):
        mods = [mode(f, l, i) for l in legs for i in range(Lr)]; cf = []
        for bits in range(1 << len(mods)):
            st = 0; n = 0; kk = 0
            for j, md in enumerate(mods):
                if bits >> j & 1: st |= 1 << md; n += 1; kk += ku[md % Lr]
            cf.append((st, n * QA[f], n * QB[f], kk % 6))
        per.append(cf)
    def merge(a, b):
        d = {}
        for x in a:
            for y in b: d.setdefault((x[1] + y[1], x[2] + y[2], (x[3] + y[3]) % 6), []).append(x[0] | y[0])
        return d
    d1 = merge(per[0], per[1]); d2 = merge(per[2], per[3]); out = []
    for (a, b, c), s1 in d1.items():
        key = (qa_t - a, qb_t - b, (Kt - c) % 6)
        if key in d2:
            out.append((np.array(s1, np.int64)[:, None] | np.array(d2[key], np.int64)[None, :]).ravel())
    return np.sort(np.concatenate(out))

def apply(st, ops):
    st = st.copy(); sg = np.ones(len(st)); ok = np.ones(len(st), bool)
    for md, dag in reversed(ops):
        bit = np.int64(1) << np.int64(md); occ = (st & bit) != 0; ok &= occ != dag
        sg *= 1 - 2 * (np.bitwise_count(st & (bit - 1)) & 1).astype(np.int64); st ^= bit
    return st, sg, ok

def matrix(bi, bo, terms):
    Mt = None; r = []; c = []; v = []; idx = np.arange(len(bi))
    def flush(Mt):
        if not r: return Mt
        A = sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(len(bo), len(bi)), dtype=complex)
        return A if Mt is None else Mt + A
    for co, ops in terms:
        ns, sg, ok = apply(bi, ops)
        if not ok.any(): continue
        ns = ns[ok]; p = np.minimum(np.searchsorted(bo, ns), len(bo) - 1); h = bo[p] == ns
        r.append(p[h]); c.append(idx[ok][h]); v.append(co * sg[ok][h])
        if len(r) > 60: Mt = flush(Mt); r.clear(); c.clear(); v.clear()
    Mt = flush(Mt)
    return Mt if Mt is not None else sp.csr_matrix((len(bo), len(bi)), dtype=complex)

def free_terms():
    T = []
    for f in range(4):
        for i in range(Lr):
            a, b = mode(f, 0, i), mode(f, 1, i); e = S[f] * np.sin(kv[i]); w = 1 - np.cos(kv[i])
            T += [(e, [(a, 1), (a, 0)]), (-e, [(b, 1), (b, 0)]), (w, [(a, 1), (b, 0)]), (w, [(b, 1), (a, 0)])]
    return [(c, [(m, bool(d)) for m, d in o]) for c, o in T]

P1 = [(0, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (3, 0, 0), (3, 0, 1)]   # B3 B4+ B4'+ B5 B0 B0'
P2 = [(0, 0, 0), (0, 0, 1), (1, 0, 0), (2, 1, 0), (2, 1, 1), (3, 0, 0)]   # B3 B3' B4 B5+ B5'+ B0
def tong_terms(filt, qa=QA, qb=QB):
    T = []; charged = 0
    for pat in (P1, P2):
        dq = sum((1 if d else -1) * qa[f] for f, d, _ in pat); dqb = sum((1 if d else -1) * qb[f] for f, d, _ in pat)
        charged += (dq != 0) or (dqb != 0)
        for iks in itertools.product(range(Lr), repeat=6):
            kt = 0; ph = 1 + 0j; ops = []
            for (f, d, sh), i in zip(pat, iks):
                sgn = -1 if d else 1; kt += sgn * ku[i]
                ff = (1 + np.exp(1j * kv[i])) / 2 if filt else 1.0
                ph *= np.exp(sgn * 1j * kv[i] * sh) * (np.conj(ff) if d else ff); ops.append((mode(f, 1, i), bool(d)))
            if kt % 6 or abs(ph) < 1e-14: continue
            T.append((ph / Lr ** 2, ops)); T.append((np.conj(ph) / Lr ** 2, [(m, not d) for m, d in reversed(ops)]))
    return T, charged
TL, c50 = tong_terms(False); TF, _ = tong_terms(True)
_, c51 = tong_terms(False, qa=q51)
check("E1 both point-split Tong terms are neutral under U(1)_A x U(1)_B (exact symmetry of H); with 3451 charges both are charged",
      c50 == 0 and c51 == 2, f"terms (local, filtered) {len(TL)}, {len(TF)}")

B0 = sector(36, 12, 0); TFr = free_terms()
H0 = matrix(B0, B0, TFr); HL = matrix(B0, B0, TL); HF = matrix(B0, B0, TF)
f = 1; ikp = 1                                   # flavour 4, k = pi
secp = sector(36 + QA[f], 12 + QB[f], 3); sech = sector(36 - QA[f], 12 - QB[f], 3)
mb = mode(f, 1, ikp); ma = mode(f, 0, ikp)
Bm = matrix(B0, sech, [(1.0, [(mb, False)])])
HFh = matrix(sech, sech, TF); HLh = matrix(sech, sech, TL)
cF = abs(HFh @ Bm - Bm @ HF).max(); cL = abs(HLh @ Bm - Bm @ HL).max()
check("E2 THEOREM check [b(pi), H_filtered] = 0 exactly on the sector; the local Tong terms do not commute with b(pi)",
      cF < 1e-12 and cL > 1e-3, f"|[b,H_F]| {cF:.1e}, |[b,H_L]| {cL:.2f}; dim {len(B0)}")

def lanc(H, v, n=40):
    nv = np.linalg.norm(v); q = v / nv; Q = [q]; a = []; b = []; qp = 0 * q; bb = 0.0
    for _ in range(n):
        w = H @ q - bb * qp; al = np.vdot(q, w).real; w -= al * q
        for qq in Q: w -= np.vdot(qq, w) * qq
        a.append(al); bb = np.linalg.norm(w)
        if bb < 1e-10: break
        b.append(bb); qp = q; q = w / bb; Q.append(q)
    T = np.diag(a) + np.diag(b[:len(a) - 1], 1) + np.diag(b[:len(a) - 1], -1)
    e, Uv = np.linalg.eigh(T); return e, nv ** 2 * abs(Uv[0]) ** 2
H0p = matrix(secp, secp, TFr); HLp = matrix(secp, secp, TL); HFp = matrix(secp, secp, TF); H0h = matrix(sech, sech, TFr)
Ap = matrix(B0, secp, [(1.0, [(ma, True)])]); Ah = matrix(B0, sech, [(1.0, [(ma, False)])])
res = {}
for name, HI, HIp, HIh in (("loc", HL, HLp, HLh), ("fil", HF, HFp, HFh)):
    for gg in (0.0, 8.0, 32.0):
        e0, v0 = sla.eigsh(H0 + gg * HI, k=3, which='SA'); o = np.argsort(e0); gs = v0[:, o[0]]
        lo = []
        for Op, Hs in ((Ap, H0p + gg * HIp), (Ah, H0h + gg * HIh)):
            e, w = lanc(Hs, Op @ gs); m = w > 1e-3; lo.append((e[m][0] - e0[o[0]], w[m][0]))
        res[(name, gg)] = (np.sort(e0) - e0[o[0]], lo)
fe = [res[("fil", gg)][1] for gg in (0.0, 8.0, 32.0)]
check("E3 corner channel a(pi), filtered: lowest excitation exactly 2 with weight 1/2 at g = 0, 8, 32 (the free corner pair)",
      all(abs(x - 2) < 1e-8 and abs(w - 0.5) < 1e-6 for lo in fe for x, w in lo))
le = res[("loc", 32.0)][1]
check("E4 corner channel a(pi), local Tong terms: at g = 32 a low (|E| < 0.3) weight >= 0.2 line appears in the light leg at "
      "the corner (doubler softening; a negative value means the half-filled sector is no longer the ground sector)",
      all(abs(x) < 0.3 and w > 0.2 for x, w in le), f"g=8 {[(round(x,3), round(w,3)) for x, w in res[('loc', 8.0)][1]]}; "
      f"g=32 {[(round(x,3), round(w,3)) for x, w in le]}")
gaps = {k: round(float(v[0][1]), 3) for k, v in res.items()}
check("E5 FINITE DIAGNOSTIC at L = 3 neither interaction gives a unique gapped symmetric ground state at strong coupling "
      "(first gap in the sector collapses): no SMG claim at this size; the BKT-type SMG of the literature needs L >> 3",
      gaps[("loc", 32.0)] < 0.05 and gaps[("fil", 32.0)] < 0.2, f"first sector gap {gaps}")
print(f"time {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
