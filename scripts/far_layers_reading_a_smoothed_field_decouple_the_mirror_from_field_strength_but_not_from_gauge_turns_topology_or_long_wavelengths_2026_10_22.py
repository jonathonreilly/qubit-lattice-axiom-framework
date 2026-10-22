AUDIT_INPUT_PATHS = ('docs/FAR_LAYERS_READING_A_SMOOTHED_FIELD_DECOUPLE_THE_MIRROR_FROM_FIELD_STRENGTH_BUT_NOT_FROM_GAUGE_TURNS_TOPOLOGY_OR_LONG_WAVELENGTHS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Grabowska-Kaplan route in framework terms: a full-density layer coordinate
whose layer s reads a smoothed (gradient-flowed, or rung-s block-averaged)
copy of the links. 2D euclidean U(1) toy (1+1D world) x Ls layers, Shamir
domain-wall slab with Pauli-Villars subtraction, 3-4-5-0 content.
Self-contained (numpy/scipy). Seeded. Dense matrices <= 1024^2 complex."""
import time
import numpy as np
import scipy.sparse as sps

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = [0, 0]


def check(tag, kind, ok, msg, detail):
    NP[0 if ok else 1] += 1
    print("[%s] %s %s %s | %s" % ("PASS" if ok else "FAIL", tag, kind, msg, detail))


def note(tag, kind, msg):
    print("   %s %s %s" % (tag, kind, msg))


S1 = np.array([[0, 1], [1, 0]], complex)
S2 = np.array([[0, -1j], [1j, 0]])
S3 = np.diag([1.0, -1.0]).astype(complex)
GAM = [S1, S2]
PP, PM = (np.eye(2) + S3) / 2, (np.eye(2) - S3) / 2

# ---------------- gauge fields: th[mu, x, y], link (x,y)->(x,y)+mu ----------
def plaq(th):
    return th[0] + np.roll(th[1], -1, 0) - np.roll(th[0], -1, 1) - th[1]


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def force(F):
    """dS/dth for S = sum(1 - cos F) (compact) given s = sin F."""
    return np.array([F - np.roll(F, 1, 1), np.roll(F, 1, 0) - F])


def flow(th, n, eps=0.125, compact=True):
    """n explicit gradient-flow (Wilson-flow) steps; each step reads one
    link's two plaquettes (nearest-neighbour, staple)."""
    th = th.copy()
    for _ in range(n):
        F = plaq(th)
        th -= eps * force(np.sin(F) if compact else F)
    return th


def gauge(th, lam):
    """U(p, p+mu) -> g(p) U g(p+mu)^*, th -> th + lam(p) - lam(p+mu)."""
    return np.array([th[0] + lam - np.roll(lam, -1, 0), th[1] + lam - np.roll(lam, -1, 1)])


def dmat(L):
    """exterior derivative links -> plaquettes on the L x L torus (dense)."""
    nl = 2 * L * L
    D = np.zeros((L * L, nl))
    for i in range(nl):
        e = np.zeros(nl)
        e[i] = 1
        D[:, i] = plaq(e.reshape(2, L, L)).ravel()
    return D


def block_avg(th, b, Dm):
    """rung reading: replace the flux inside each b x b plaquette block by the
    block mean, adding a = d_B^+ (mean - F) on the block's interior links
    (a depends only on F, so it is gauge invariant: covariance per site)."""
    L = th.shape[1]
    F = wrap(plaq(th))
    tgt = F.copy()
    for X in range(0, L, b):
        for Y in range(0, L, b):
            tgt[X:X + b, Y:Y + b] = F[X:X + b, Y:Y + b].mean()
    rhs = (tgt - F).ravel()
    if b >= L:
        cols = np.arange(2 * L * L)
    else:
        cols = []
        for mu in range(2):
            for x in range(L):
                for y in range(L):
                    # interior link: both adjacent plaquettes in the same block
                    if mu == 0:
                        p1, p2 = (x, y), (x, (y - 1) % L)
                    else:
                        p1, p2 = (x, y), ((x - 1) % L, y)
                    if (p1[0] // b, p1[1] // b) == (p2[0] // b, p2[1] // b):
                        cols.append(mu * L * L + x * L + y)
        cols = np.array(cols)
    a = np.zeros(2 * L * L)
    a[cols] = np.linalg.lstsq(Dm[:, cols], rhs, rcond=None)[0]
    return th + a.reshape(2, L, L)


def anchor_read(th, b):
    """naive zoom reading with transports: fine links replaced by
    -phi(p) + Abar(c_p, c_q) + phi(q), phi = Wilson line anchor -> p
    (first along y, then x), Abar = straight coarse Wilson line."""
    L = th.shape[1]
    phi = np.zeros((L, L))
    for x in range(L):
        for y in range(L):
            cx, cy = (x // b) * b, (y // b) * b
            phi[x, y] = sum(th[1, cx, yy % L] for yy in range(cy, y)) + \
                sum(th[0, xx % L, y] for xx in range(cx, x))
    out = np.zeros_like(th)
    for mu in range(2):
        for x in range(L):
            for y in range(L):
                q = ((x + 1) % L, y) if mu == 0 else (x, (y + 1) % L)
                cp = ((x // b) * b, (y // b) * b)
                cq = ((q[0] // b) * b, (q[1] // b) * b)
                ab = 0.0
                if cp != cq:
                    for t in range(b):
                        if mu == 0:
                            ab += th[0, (cp[0] + t) % L, cp[1]]
                        else:
                            ab += th[1, cp[0], (cp[1] + t) % L]
                out[mu, x, y] = -phi[x, y] + ab + phi[q]
    return out


# ---------------- fermions: Wilson-Dirac (2D) and Shamir slab --------------
def hop_blocks(L, Uf, Ub):
    """hop part of D_W, antiperiodic both ways: -(1/2)[(1-g)Uf psi(p+mu) +
    (1+g)Ub(p-mu) psi(p-mu)]; Uf, Ub arrays [mu, x, y]. Returns dense."""
    n = L * L
    H = np.zeros((2 * n, 2 * n), complex)
    for mu in range(2):
        Pm, Pp = (np.eye(2) - GAM[mu]) / 2, (np.eye(2) + GAM[mu]) / 2
        for x in range(L):
            for y in range(L):
                q = (x + 1, y) if mu == 0 else (x, y + 1)
                bc = -1.0 if (q[0] == L or q[1] == L) else 1.0
                i, j = x * L + y, (q[0] % L) * L + q[1] % L
                H[2 * i:2 * i + 2, 2 * j:2 * j + 2] -= bc * Pm * Uf[mu, x, y]
                H[2 * j:2 * j + 2, 2 * i:2 * i + 2] -= bc * Pp * Ub[mu, x, y]
    return H


def dw2(th, q, M=1.0):
    L = th.shape[1]
    U = np.exp(1j * q * th)
    return (2 - M) * np.eye(2 * L * L) + hop_blocks(L, U, U.conj())


def slab(ths, q, mf, M=1.0):
    """Shamir: (D psi)_s = (D_W(th_s) + 1) psi_s - P_- psi_{s+1} - P_+ psi_{s-1},
    psi_Ls = -mf psi_0, psi_-1 = -mf psi_{Ls-1}; light P_- at s=0, P_+ at Ls-1.
    Sparse (csc)."""
    Ls = len(ths)
    n = 2 * ths[0].shape[1] ** 2
    Im = sps.identity(n // 2)
    KM, KP = sps.kron(Im, PM), sps.kron(Im, PP)
    rows = [[None] * Ls for _ in range(Ls)]
    for s in range(Ls):
        rows[s][s] = sps.csr_matrix(dw2(ths[s], q, M) + np.eye(n))
        rows[s][(s + 1) % Ls] = -KM if s + 1 < Ls else mf * KM
        rows[s][(s - 1) % Ls] = -KP if s > 0 else mf * KP
    return sps.bmat(rows, format="csc")


def lowest_sv(D, k):
    """k smallest singular triplets of sparse D via shift-invert on D^H D."""
    import scipy.sparse.linalg as spl
    lu = spl.splu(D.tocsc())
    luh = spl.splu(D.conj().T.tocsc())
    op = spl.LinearOperator(D.shape, matvec=lambda x: lu.solve(luh.solve(x)), dtype=complex)
    ev, V = spl.eigsh(op, k=k, which="LM", tol=1e-12, v0=np.ones(D.shape[0], complex))
    sv = 1 / np.sqrt(ev)
    o = np.argsort(sv)
    sv, V = sv[o], V[:, o]
    U = (D @ V) / sv
    return sv, U, V


def dslab(L, phis, q, order, phis2=None):
    """derivative of the slab wrt probe amplitudes at zero background:
    order 1: dU = i q phi; order 2: d^2U = -(q phi)(q phi2)."""
    blocks = []
    for s in range(len(phis)):
        if order == 1:
            uf, ub = 1j * q * phis[s], -1j * q * phis[s]
        else:
            p2 = phis[s] if phis2 is None else phis2[s]
            uf = ub = -(q * phis[s]) * (q * p2)
        blocks.append(sps.csr_matrix(hop_blocks(L, uf, ub)))
    return sps.block_diag(blocks, format="csr")


GCACHE = {}


def greens(L, Ls):
    key = (L, Ls)
    if key not in GCACHE:
        zero = [np.zeros((2, L, L))] * Ls
        GCACHE[key] = (np.linalg.inv(slab(zero, 1.0, 0.0).toarray()), np.linalg.inv(slab(zero, 1.0, 1.0).toarray()))
    return GCACHE[key]


def response(L, Ls, phA, phB):
    """d^2/da db [log det D_DW(mf=0) - log det D_PV(mf=1)] at zero field, unit
    charge (charge q multiplies it by q^2 exactly at this order)."""
    Gdw, Gpv = greens(L, Ls)
    DA, DB = dslab(L, phA, 1.0, 1), dslab(L, phB, 1.0, 1)
    DAB = dslab(L, phA, 1.0, 2, phB)
    out = 0
    for G, sg in ((Gdw, 1), (Gpv, -1)):
        GA, GB = (DA.T @ G.T).T, (DB.T @ G.T).T
        out += sg * (DAB.T.multiply(G).sum() - np.sum(GA * GB.T))
    return out


def index_hw(th, q, M=1.0):
    """overlap index from the spectral asymmetry of H_W = g5 D_W(-M)."""
    L = th.shape[1]
    H = np.kron(np.eye(L * L), S3) @ dw2(th, q, M)
    ev = np.linalg.eigvalsh((H + H.conj().T) / 2)
    return 0.5 * np.sum(np.sign(ev))


def ipr(v, L, nsp=2):
    w = np.sum(np.abs(v.reshape(-1, nsp)) ** 2, axis=1)
    w = w / w.sum()
    return len(w) * np.sum(w ** 2)


def lump(L, Qt, rho, Dm, x0=(2, 3)):
    """flux 2 pi Qt as a gaussian lump of radius rho on the uniform bundle."""
    th = np.zeros((2, L, L))
    xs = np.arange(L)
    th[1] = (2 * np.pi * Qt * xs / L ** 2)[:, None]
    th[0, L - 1, :] = -2 * np.pi * Qt * xs / L
    dx = np.minimum(np.abs(xs - x0[0]), L - np.abs(xs - x0[0]))
    dy = np.minimum(np.abs(xs - x0[1]), L - np.abs(xs - x0[1]))
    w = np.exp(-(dx[:, None] ** 2 + dy[None, :] ** 2) / (2 * rho ** 2))
    tgt = 2 * np.pi * Qt * w / w.sum()
    a = np.linalg.lstsq(Dm, (tgt - wrap(plaq(th))).ravel(), rcond=None)[0]
    return th + a.reshape(2, L, L)


hol = lambda t: np.mean(np.sum(t[0], axis=0))   # mean x-holonomy (harmonic part)

# ============================ A. the smoothing rules =======================
print("== A. layer smoothing rules: covariance, topology, holonomy, reach (2D U(1), L = 8)")
L, Ls = 8, 8
Dm = dmat(L)
th0 = 0.6 * RNG.standard_normal((2, L, L))
lam = 3.0 * RNG.standard_normal((L, L))
thg = gauge(th0, lam)
naive = lambda t: 0.5 * (t + np.roll(t, 1, 1))   # average parallel links, no transport
rules = {"flow": lambda t: flow(t, 40), "block": lambda t: block_avg(t, 4, Dm),
         "anchor": lambda t: anchor_read(t, 4), "naive": naive}
res = {k: np.max(np.abs(wrap(f(thg) - gauge(f(th0), lam)))) for k, f in rules.items()}
check("A1", "THEOREM", max(res["flow"], res["block"], res["anchor"]) < 1e-9 and res["naive"] > 0.1,
      "per-site covariance th_s[g.th] = g.th_s[th], so the slab is gauge invariant (all layers at p turn with g(p)): yes for flow (force sin F), block-flux averaging (added a[F] is gauge invariant), anchor transports; no for link averaging without transports",
      "rough field, 40 steps, b = 4: residuals flow %.0e, block %.0e, anchor %.0e, naive %.2f" % (res["flow"], res["block"], res["anchor"], res["naive"]))
thl = lump(L, 1, 1.2, Dm) + 0.15 * RNG.standard_normal((2, L, L))
outs = {"field": thl, "flow200": flow(thl, 200), "block4": block_avg(thl, 4, Dm),
        "block8": block_avg(thl, 8, Dm), "anchor4": anchor_read(thl, 4)}
st = {}
for k, t in outs.items():
    F = wrap(plaq(t))
    st[k] = (np.sum(F) / (2 * np.pi), hol(t), np.max(np.abs(F)), np.max(np.abs(F - 2 * np.pi / L ** 2)))
ok = (abs(st["flow200"][0] - 1) < 1e-9 and abs(st["block4"][0] - 1) < 1e-9 and abs(st["block8"][0] - 1) < 1e-9
      and abs(st["flow200"][1] - st["field"][1]) < 1e-12 and st["flow200"][3] < 1e-6 and st["block8"][3] < 1e-9
      and abs(st["anchor4"][0]) < 0.5 and st["anchor4"][2] > 2 * st["field"][2])
check("A2", "THEOREM", ok,
      "flow keeps Q and the mean holonomy exactly and relaxes to the uniform flux 2 pi Q/L^2; block averaging keeps Q (whole-torus block: uniform at once); coarse Wilson lines with anchor transports (naive zoom reading) pile block flux onto corner plaquettes and lose Q mod 2 pi",
      "Q=1 lump+noise (Q, hol, max|F|, max|F-F_unif|): field (%.0f, %.3f, %.2f, %.2f); flow200 (%.0f, %.3f, %.3f, %.0e); block4 (%.0f, -, %.2f, %.2f); block8 (%.0f, -, %.3f, %.0e); anchor4 (%.0f, -, %.2f, -)"
      % (st["field"][0], st["field"][1], st["field"][2], st["field"][3], st["flow200"][0], st["flow200"][1],
         st["flow200"][2], st["flow200"][3], st["block4"][0], st["block4"][2], st["block4"][3], st["block8"][0],
         st["block8"][2], st["block8"][3], st["anchor4"][0], st["anchor4"][2]))
# reach: flux of one plaquette under n nearest-neighbour flow steps (F -> F - eps Lap F)
rr = {}
for eps in (0.125, 0.25, 0.26):
    N2 = 40
    F = np.zeros((N2, N2))
    F[N2 // 2, N2 // 2] = 1.0
    stag = (-1.0) ** np.add.outer(np.arange(N2), np.arange(N2))
    for n in range(60):
        F = F - eps * (4 * F - np.roll(F, 1, 0) - np.roll(F, -1, 0) - np.roll(F, 1, 1) - np.roll(F, -1, 1))
    xs = np.arange(N2) - N2 // 2
    G2 = stag / N2 ** 2
    for n in range(200):   # staggered (largest-level) mode alone
        G2 = G2 - eps * (4 * G2 - np.roll(G2, 1, 0) - np.roll(G2, -1, 0) - np.roll(G2, 1, 1) - np.roll(G2, -1, 1))
    rr[eps] = (np.sum(F * (xs[:, None] ** 2 + xs[None, :] ** 2)) / np.sum(F) / 60, np.abs(np.sum(G2 * stag)))
check("A3", "THEOREM", rr[0.125][0] <= 1.0 + 1e-9 and rr[0.25][0] <= 1.0 + 1e-9 and rr[0.26][1] > 1,
      "reach: a nearest-neighbour step is stable iff eps <= 1/(2d), and flux variance grows 2 d eps <= 1 per step, so n layer-local steps smooth over r <= sqrt(n) cells; the zoom reading (layer s reads rung-s blocks) reaches 2^s",
      "r^2/step: eps 1/8 %.3f, 1/4 %.3f; eps 0.26: staggered mode x %.0e in 200 steps" % (rr[0.125][0], rr[0.25][0], rr[0.26][1]))

# ============================ B. the free slab =============================
print("== B. free slab (Shamir, M = 1, Ls = 8, antiperiodic 8 x 8, mf = 0)")
zero = [np.zeros((2, L, L))] * Ls
D0 = slab(zero, 1.0, 0.0)
sv, _, Vl = lowest_sv(D0, 9)
n = 2 * L * L
KMf, KPf = np.kron(np.eye(L * L), PM), np.kron(np.eye(L * L), PP)
wts = []
for i in range(8):
    v = Vl[:, i]
    wts.append(np.linalg.norm(KMf @ v[:n]) ** 2 + np.linalg.norm(KPf @ v[-n:]) ** 2)
check("B1", "DIAGNOSTIC", min(wts) > 0.95 and sv[8] > 1.5 * sv[0],
      "the eight lowest modes (a light pair at each momentum (+-pi/8, +-pi/8)) sit on the end layers, P_- on layer 0, P_+ on layer Ls-1; the rest is gapped",
      "min end-layer chiral weight %s; lowest singular value %s (x8), next %.2f" % (np.round(min(wts), 4), np.round(sv[0], 3), sv[8]))

# ============================ C. far-end decoupling ========================
print("== C. GK layers: light end keeps the charge, far end decouples from smooth fields")
NF = [0, 0, 0, 0, 10, 30, 80, 200]   # flow steps per layer (eps = 1/8): flow time grows with s
BB = [1, 1, 1, 1, 2, 4, 8, 8]          # zoom reading: layer s reads rung-(s-3) blocks


def probe(n, kind):
    xs = np.arange(L)
    k = 2 * np.pi * n / L
    t = np.zeros((2, L, L))
    if kind == "T":           # transverse (a photon): A_y(x) = cos kx
        t[1] = np.cos(k * xs)[:, None]
        return t
    return gauge(t, np.sin(k * xs)[:, None] * np.ones((1, L)))   # pure gauge


def layers(t, rule):
    if rule == "none":
        return [t] * Ls
    if rule == "flow":
        return [flow(t, m, compact=False) for m in NF]
    if rule == "block":
        return [t if b == 1 else block_avg(t, b, Dm) for b in BB]
    if rule == "cut":        # far layers see no field at all (not covariant)
        return [t if b == 1 else 0 * t for b in BB]
    if rule == "cutR":       # mirror image: light right-hander on layer Ls-1
        return [t if b == 1 else 0 * t for b in BB][::-1]


# layer profile of the light modes (B1): near = P_- weight, far = P_+ weight
wn = np.zeros(Ls)
wf = np.zeros(Ls)
for i in range(8):
    v = Vl[:, i].reshape(Ls, L * L, 2)
    wn += np.sum(np.abs(v[:, :, 1]) ** 2, axis=1)
    wf += np.sum(np.abs(v[:, :, 0]) ** 2, axis=1)
wn, wf = wn / wn.sum(), wf / wf.sum()
del Vl, D0
gv = {}
for nk in (1, 2):
    for kind in ("T", "L"):
        p = probe(nk, kind)
        for rule in ("flow", "block"):
            fs = np.array([np.sum(t * p) / np.sum(p * p) for t in layers(p, rule)])
            gv[(nk, kind, rule)] = (wn @ fs, wf @ fs, fs[-1])
lT = [gv[(nk, "T", r)][0] for nk in (1, 2) for r in ("flow", "block")]
fT = [gv[(nk, "T", r)][1] for nk in (1, 2) for r in ("flow", "block")]
fL = [gv[(nk, "L", r)][1] for nk in (1, 2) for r in ("flow", "block")]
check("C1", "DIAGNOSTIC", min(lT) > 0.99 and max(np.abs(fT)) < 0.02 and min(fL) > 1 - 1e-9,
      "field seen by each end (B1 layer weights x field per layer): light end sees a photon mode in full, the far mirror ~0; both see a pure-gauge mode in full: the mirror is blind to field strength but turns under gauge transformations (GK 'fluff')",
      "weight on layers >= 4: near %.0e, far %.4f; (flow, block) x k = 2pi/8, 4pi/8: photon near %s, far %s; pure-gauge far %s"
      % (wn[4:].sum(), wf[4:].sum(), np.round(lT, 4), np.round(fT, 4), np.round(fL, 6)))
rsp = {}
for nk in (1, 2):
    pT, pL = probe(nk, "T"), probe(nk, "L")
    base = response(L, Ls, layers(pT, "none"), layers(pT, "none"))
    for rule in ("none", "flow", "block", "cut", "cutR"):
        lt = layers(pT, rule)
        ll = layers(pL, rule)
        rsp[(nk, rule)] = (response(L, Ls, lt, lt) / base, response(L, Ls, ll, lt) / abs(base),
                           response(L, Ls, ll, ll) / abs(base))
gi = max(abs(rsp[(nk, r)][i]) for nk in (1, 2) for r in ("none", "flow", "block") for i in (1, 2))
dtt = max(abs(rsp[(nk, r)][0] - rsp[(nk, "cut")][0]) / abs(rsp[(nk, "cut")][0]) for nk in (1, 2) for r in ("flow", "block"))
an = [rsp[(nk, "cut")][1] for nk in (1, 2)]
anR = [rsp[(nk, "cutR")][1] for nk in (1, 2)]
check("C2", "DIAGNOSTIC", gi < 1e-10 and dtt < 0.03 and min(abs(a.imag) for a in an) > 0.05,
      "effective action (DW - PV): smoothed slabs are exactly gauge invariant and their photon response equals the light end's alone (far layers cut) to < 3%; the cut slab has an imaginary pure-gauge x photon term, the light Weyl's anomaly, which the far end's fluff cancels",
      "photon TT/unsmoothed k1,k2: flow %s, block %s, cut %s; smoothed pure-gauge rows <= %.0e; cut LxT %s, mirror cut %s"
      % (np.round([rsp[(nk, 'flow')][0].real for nk in (1, 2)], 4), np.round([rsp[(nk, 'block')][0].real for nk in (1, 2)], 4),
         np.round([rsp[(nk, 'cut')][0].real for nk in (1, 2)], 4), gi, np.round(an, 4), np.round(anR, 4)))
QS = [(3, 1), (4, 1), (5, -1), (0, -1)]   # 3-4-5-0: (charge, light handedness)
tot = []
for nk in (1, 2):
    s_lt = sum(q * q * (rsp[(nk, "cut")][1] if c > 0 else rsp[(nk, "cutR")][1]) for q, c in QS)
    s_ll = sum(q * q * (rsp[(nk, "cut")][2] if c > 0 else rsp[(nk, "cutR")][2]) for q, c in QS)
    tot.append((s_lt, s_ll))
check("C3", "THEOREM", all(abs(t[0]) < 1e-12 for t in tot) and all(t[1].real > 1 for t in tot),
      "3-4-5-0, quadratic order: responses scale as q^2 and the mirror-image slab's is the complex conjugate (g5-R5 hermiticity), so the cut slab's anomalous terms sum to sum chi q^2 = 9+16-25 = 0, but its real pure-gauge term sums to sum q^2 > 0 (needs a counterterm); the smoothed slab needs none",
      "cut sums k1, k2: anomalous %s, real pure-gauge %s" % (["%.0e" % abs(t[0]) for t in tot], np.round([t[1].real for t in tot], 2)))

GCACHE.clear()
# ============================ D. topology: the mirror's 't Hooft vertex =====
print("== D. topology: Q = 1 lump; the far layers read its flow-time-200 field")
thq = lump(L, 1, 1.6, Dm)
thf = flow(thq, 200)
idx = [(q, index_hw(thq, q), index_hw(thf, q)) for q in (1, 3, 4, 5)]
check("D1", "DIAGNOSTIC", all(abs(a - q) < 1e-9 and abs(b - q) < 1e-9 for q, a, b in idx),
      "index (spectral asymmetry of g5 D_W(-1)) of the near-layer field and the flowed far-layer field: both q Q for each 3-4-5-0 charge, so the far mirror keeps q Q zero modes",
      "(q, near, far): %s" % ", ".join("(%d, %.0f, %.0f)" % t for t in idx))
thq = lump(L, 1, 0.9, Dm)
lay = [thq if m == 0 else flow(thq, m) for m in NF]
res_q = {}
for name, ths in (("unsmoothed", [thq] * Ls), ("GK", lay)):
    sq, Uq, Vq = lowest_sv(slab(ths, 1.0, 0.0), 2)
    vr = Vq[:, 0].reshape(Ls, L * L, 2)
    ul = Uq[:, 0].reshape(Ls, L * L, 2)
    res_q[name] = (sq[0], sq[1], np.sum(np.abs(vr[0, :, 1]) ** 2), np.sum(np.abs(ul[-1, :, 1]) ** 2),
                   ipr(vr[0, :, 1], L, 1), ipr(ul[-1, :, 1], L, 1))
u, g = res_q["unsmoothed"], res_q["GK"]
check("D2", "DIAGNOSTIC", g[0] < 1e-3 * g[1] and g[2] > 0.9 and g[3] > 0.9 and g[5] < u[5],
      "Q = 1 slab: one near-zero mode with or without smoothing, right vector the near-end left-handed zero mode at the lump, left vector the far mirror's (psi-bar P_-) zero mode, only spread by smoothing: every topological event moves chi q Q light units and the opposite in the mirror; the 't Hooft vertex includes the mirror, unsuppressed",
      "(sig0, sig1, near wt, far wt, IPR near, IPR far): unsmoothed (%.0e, %.2f, %.3f, %.3f, %.2f, %.2f); GK (%.0e, %.2f, %.3f, %.3f, %.2f, %.2f)"
      % (u + g))
note("D3", "THEOREM", "holonomy: smoothing keeps the harmonic part (A2), so under a 2 pi winding the mirror's levels still cross q times (rung-dimension-chirality B2/E2); in 1+1D a winding in time is the topological charge (D1-D2)")

# ============================ E. estimates against measurement =============
print("== E. estimates (a = sqrt(8 pi) l_P = 8.10e-35 m; r = the far layer's smoothing radius)")
a_m = np.sqrt(8 * np.pi) * 1.616255e-35
hbarc = 1.97327e-16   # GeV m
scales = {"1/M_Z": hbarc / 91.1876, "1/m_e": hbarc / 0.000511, "R_Earth": 6.371e6, "c/H0": 2.99792458e8 / (67.4e3 / 3.0857e22)}
lr = {k: np.log10(v / a_m) for k, v in scales.items()}
zl = {k: np.log2(v / a_m) for k, v in scales.items()}
neff = 48 * (10.75 / 106.75) ** (4 / 3)
check("E1", "ESTIMATE", zl["c/H0"] < 201 and 2 * lr["1/M_Z"] > 30,
      "layers to smooth over r: layer-local flow n >= (r/a)^2 (A3); zoom reading log2(r/a)",
      "(r: local, zoom) " + ", ".join("%s: 1e%.0f, %.1f" % (k, 2 * lr[k], zl[k]) for k in scales))
note("E2", "ESTIMATE", "Gamma_Z, alpha: the mirror couples at momentum k through the filter f(k) (flow exp(-k^2 t); block ~1/(k b) per direction): for r >> 1/m_e nothing added to Gamma_Z (unsmoothed e^c' alone: +35.5 MeV per family) or to alpha running m_e..M_Z; equal layer gaps, no tower")
Tc = 2.35e-4   # eV
gh = (1 / 137.036) ** 2 * 1.22e28 * (1.97327e-7 / 6.371e6) ** 3 / Tc ** 4
note("E3", "ESTIMATE", "left over: a massless conjugate copy, fully charged for wavelengths > r, holonomy and topology, plus gravity; if ever thermal with the SM above the EW scale, Delta N_eff = 48 (10.75/106.75)^(4/3) = %.2f vs Planck 2.99 +- 0.17 (excluded): it must never thermalise; soft production at r = R_Earth: Gamma/H ~ alpha^2 M_P r^-3 T^-4 = %.0e at T_CMB (larger T: smaller); topology makes k ~ 1/r quanta only: Delta N_eff ~ 0" % (neff, gh))
note("E4", "SPECULATION", "dark sector: as is, dark radiation of zero abundance, not dark matter; a far-layer Yukawa reading the smoothed Higgs (vev = k=0 mode, survives) would make it a stable, nearly inert massive copy; untested")
print("supplied: 2D U(1) toy, L = 8, Ls = 8, M = 1, mf, PV subtraction, antiperiodic BC, flow profile NF and eps, block profile BB, probes, lump, measured inputs | %.1f s" % (time.time() - T0))
print("cited: rung-dimension-chirality, ladder-wall E3, toy-qmc, Grabowska-Kaplan 2016, Shamir, Neuberger, Jackiw-Rajaraman, Planck 2018")
print("TOTAL: PASS=%d FAIL=%d" % tuple(NP))
