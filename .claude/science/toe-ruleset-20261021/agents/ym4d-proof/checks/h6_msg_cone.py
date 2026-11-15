#!/usr/bin/env python3
"""Check h6 (lane D session 3): non-abelian cone ratio at depth 2 (d = 4) and the multi-scale small-field gauge (MSG).
Pre-registered criteria: checks/h6_criteria.md (written before this script). SU(2), L = 3, kappa = 1, S4' with order pairing,
W_0(M) = M/sqrt(det M). Open cone boxes W_P^{(i)}. Finite instances only; no claim beyond the sampled chains.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import time, itertools as it, numpy as np
AUDIT_TIMEOUT_SEC = 1800
T0 = time.time(); NP = NF = 0
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
L = 3; HF = (L - 1) // 2; KAP = 1.0; NC = 2
SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex)
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))
I2 = np.eye(2, dtype=complex)
def su2_exp(a):  # exp(i a.sigma/2)
    th = np.linalg.norm(a, axis=-1) / 2; c = np.cos(th); sn = np.where(th > 0, np.sin(th) / np.where(th > 0, th, 1), 1.0) / 2
    return c[..., None, None] * I2 + 1j * np.einsum("...j,jab->...ab", sn[..., None] * a, SIG)
def su2_log(U):  # components a with U = exp(i a.sigma/2); principal branch theta in [0, pi]
    v = np.imag(np.einsum("...ab,jba->...j", U, SIG)) / 2; c = np.real(np.trace(U, axis1=-2, axis2=-1)) / 2
    nv = np.linalg.norm(v, axis=-1); th = np.arctan2(nv, c)
    return 2 * (th / np.where(nv > 0, nv, 1))[..., None] * v
theta = lambda U: np.arctan2(np.linalg.norm(np.imag(np.einsum("...ab,jba->...j", U, SIG)) / 2, axis=-1),
                             np.real(np.trace(U, axis1=-2, axis2=-1)) / 2)  # op norm of log U
sfun = lambda U: 1 - np.real(np.trace(U, axis1=-2, axis2=-1)) / 2
smax = lambda x: float(np.max(x)) if np.size(x) else 0.0
def W0(M): return M / np.sqrt(np.real(np.linalg.det(M)))[..., None, None]

class Geo:
    """Level-i box of shape S (open); links (mu, x) with x, x + e_mu in the box."""
    def __init__(s, S):
        s.S = tuple(S); s.d = len(S); s.NL = s.d * int(np.prod(S)); s.E = np.eye(s.d, dtype=int)
    def lid(s, m, x): return np.ravel_multi_index((np.full(len(x), m),) + tuple(np.asarray(x).T), (s.d,) + s.S)
    def inside(s, m):  # slice of base sites whose mu-link stays in the box
        return tuple(slice(0, n - 1) if a == m else slice(0, n) for a, n in enumerate(s.S))
def axial_rel(o, order, start):  # links of the complete-axial path from start to start + o (relative), order = axis order
    cur = np.array(start); out = []
    for m in order:
        for _ in range(abs(o[m])):
            if o[m] > 0: out.append((cur.copy(), m, 1)); cur[m] += 1
            else: cur[m] -= 1; out.append((cur.copy(), m, -1))
    return out
def s4_patterns(d):
    pats = {}
    E = np.eye(d, dtype=int)
    for mu in range(d):
        F = []; B = []
        for o in it.permutations(range(d)):
            for off in it.product(range(L), repeat=d):
                rel = np.array(off) - HF
                f = axial_rel(rel, o, np.zeros(d, int)) + [(rel + j * E[mu], mu, 1) for j in range(L)]
                b = axial_rel(rel, o, L * E[mu])
                F.append(f); B.append(b)
        pats[mu] = (F, B)
    return pats
PATS = {}
def coarse_index(gf, gc, mu):  # index arrays for all coarse mu-links of box gc, contours on fine box gf
    d = gf.d
    if d not in PATS: PATS[d] = s4_patterns(d)
    F, B = PATS[d][mu]
    Xs = np.array(list(it.product(*[range(n - (1 if a == mu else 0)) for a, n in enumerate(gc.S)])))
    base = L * Xs + HF
    def enc(lst, pad):
        cols = []
        for (rel, m, sg) in lst:
            ids = gf.lid(m, base + rel) + (0 if sg > 0 else gf.NL); cols.append(ids)
        while len(cols) < pad: cols.append(np.full(len(Xs), 2 * gf.NL))
        return np.stack(cols, axis=1)
    PF = max(len(f) for f in F); PB = max(len(b) for b in B)
    IF = np.stack([enc(f, PF) for f in F], axis=1); IB = np.stack([enc(b, PB) for b in B], axis=1)
    IS = np.stack([gf.lid(mu, base + j * gf.E[mu]) for j in range(L)], axis=1)
    return Xs, IF, IB, IS
def bank_of(U, g): f = U.reshape(g.NL, 2, 2); return np.concatenate([f, dag(f), I2[None]], 0)
def bprod(bank, I):
    P = np.broadcast_to(I2, I.shape[:-1] + (2, 2)).copy()
    for j in range(I.shape[-1]): P = P @ bank[I[..., j]]
    return P
def mbar(U, g, idx):
    _, IF, IB, _ = idx; bk = bank_of(U, g); return (bprod(bk, IF) @ dag(bprod(bk, IB))).mean(axis=1)
def qroot(a, g, idx):
    _, IF, IB, _ = idx; f = a.reshape(g.NL, 3); bk = np.concatenate([f, -f, np.zeros((1, 3))], 0)
    return (bk[IF].sum(axis=2) - bk[IB].sum(axis=2)).mean(axis=1)
def plaqs(U, g):
    out = []
    for mu in range(g.d):
        for nu in range(mu + 1, g.d):
            sl = tuple(slice(0, n - 1) if a in (mu, nu) else slice(0, n) for a, n in enumerate(g.S))
            sh = lambda A, m: A[tuple(slice(1, n) if a == m else s for a, (n, s) in enumerate(zip(g.S, sl)))]
            out.append((U[mu][sl] @ sh(U[nu], mu) @ dag(sh(U[mu], nu)) @ dag(U[nu][sl])).reshape(-1, 2, 2))
    return np.concatenate(out, 0)
def dflux(A, g):
    out = []
    for mu in range(g.d):
        for nu in range(mu + 1, g.d):
            sl = tuple(slice(0, n - 1) if a in (mu, nu) else slice(0, n) for a, n in enumerate(g.S))
            sh = lambda X, m: X[tuple(slice(1, n) if a == m else s for a, (n, s) in enumerate(zip(g.S, sl)))]
            out.append((A[mu][sl] + sh(A[nu], mu) - sh(A[mu], nu) - A[nu][sl]).reshape(-1, 3))
    return np.concatenate(out, 0)
def shapes(d, k): return [tuple([2 * L ** (k - i)] * 2 + [L ** (k - i)] * (d - 2)) for i in range(k + 1)]

def build_chain(d, k, a0, res, t, IDX, G):
    """Bottom-up chain. res[i] (i = 1..k): residual comps array (d,)+S_i+(3,). Returns per-level U, W0, Mbar, phi lists."""
    Us = [su2_exp(a0)]; Ws = [None]; Ms = [None]; As = [a0.copy()]
    for i in range(k):
        gf, gc = G[i], G[i + 1]; U1 = np.broadcast_to(I2, (d,) + gc.S + (2, 2)).copy()
        Wl = U1.copy(); Ml = U1.copy(); A1 = np.zeros((d,) + gc.S + (3,))
        for mu in range(d):
            if (i, mu) not in IDX: continue
            idx = IDX[(i, mu)]; Xs = idx[0]; M = mbar(Us[i], gf, idx); W = W0(M); key = (mu,) + tuple(Xs.T)
            r = res[i + 1][key]; U1[key] = W @ su2_exp(t * r); Wl[key] = W; Ml[key] = M
            A1[key] = qroot(As[i], gf, idx) + t * r
        Us.append(U1); Ws.append(Wl); Ms.append(Ml); As.append(A1)
    return Us, Ws, Ms, As
def link_mask(g, mu): m = np.zeros(g.S, bool); m[g.inside(mu)] = True; return m
def energy_terms(Us, Ws, Ms, G, k, res, t):
    d = G[0].d; E0 = sfun(plaqs(Us[0], G[0])).sum(); Ek = 0.0; rmax = 0.0
    for i in range(1, k + 1):
        for mu in range(d):
            m = link_mask(G[i], mu); U = Us[i][mu][m]; W = Ws[i][mu][m]; M = Ms[i][mu][m]
            Ek += 0.5 * np.sum(np.real(np.trace(dag(W) @ M, axis1=-2, axis2=-1)) - np.real(np.trace(dag(U) @ M, axis1=-2, axis2=-1)))
            rmax = max(rmax, smax(2 * np.sin(theta(dag(W) @ U) / 2)))
    return E0 + KAP * Ek, rmax
def topP(Uk):
    d = Uk.shape[0]; o = (0,) * d; e0 = (1,) + (0,) * (d - 1); e1 = (0, 1) + (0,) * (d - 2)
    return Uk[(0,) + o] @ Uk[(1,) + e0] @ dag(Uk[(0,) + e1]) @ dag(Uk[(1,) + o])
def topdB(Ak):
    d = Ak.shape[0]; o = (0,) * d; e0 = (1,) + (0,) * (d - 1); e1 = (0, 1) + (0,) * (d - 2)
    return Ak[(0,) + o] + Ak[(1,) + e0] - Ak[(0,) + e1] - Ak[(1,) + o]
def eps_hyp(Us, G, k, rmax):
    e = rmax
    for i in range(k): e = max(e, float((2 * np.sin(theta(plaqs(Us[i], G[i])) / 2)).max()))
    return e

# ---------------- MSG gauge ----------------
def axial_gauge(U, g):  # H(x) = hol along complete axial path (order 0..d-1) from the origin; returns G = H^dagger
    H = np.broadcast_to(I2, g.S + (2, 2)).copy()
    for m in range(g.d):
        for j in range(1, g.S[m]):
            sl = tuple(slice(None) if a < m else (j if a == m else 0) for a in range(g.d))
            slp = tuple(slice(None) if a < m else (j - 1 if a == m else 0) for a in range(g.d))
            H[sl] = H[slp] @ U[m][slp]
    return dag(H)
def apply_gauge(U, Gs, g):
    out = U.copy()
    for mu in range(g.d):
        sl = g.inside(mu); slp = tuple(slice(1, n) if a == mu else slice(0, n) for a, n in enumerate(g.S))
        out[mu][sl] = dag(Gs[sl]) @ U[mu][sl] @ Gs[slp]
    return out
def whitney(ac, gc, gf):  # clamped lowest-order cubical Whitney interpolation; ac: (d,)+Sc+(3,) coarse comps
    d = gf.d; out = np.zeros((d,) + gf.S + (3,)); X = np.indices(gf.S)
    for mu in range(d):
        jm = np.floor((X[mu] - HF) / L).astype(int); valid = (jm >= 0) & (jm <= gc.S[mu] - 2) & (X[mu] <= gf.S[mu] - 2)
        jmc = np.clip(jm, 0, max(gc.S[mu] - 2, 0)); acc = np.zeros(gf.S + (3,))
        js, ws = [], []
        for nu in range(d):
            if nu == mu: js.append(None); ws.append(None); continue
            xi = np.clip((X[nu] - HF) / L, 0, gc.S[nu] - 1)
            j = np.minimum(np.floor(xi).astype(int), max(gc.S[nu] - 2, 0)); js.append(j); ws.append(xi - j)
        for epsv in it.product((0, 1), repeat=d - 1):
            w = np.ones(gf.S); ix = [None] * d; q = 0
            for nu in range(d):
                if nu == mu: ix[nu] = jmc; continue
                e = epsv[q]; q += 1; w = w * (ws[nu] if e else 1 - ws[nu]); ix[nu] = np.minimum(js[nu] + e, gc.S[nu] - 1)
            acc += w[..., None] * ac[mu][tuple(ix)]
        out[mu] = np.where(valid[..., None], acc / L, 0.0)
    return out
def block_paths(g_f, g_c):  # for every offset o in {-HF..HF}^d: axial links (order 0..d-1) from centre to centre + o
    return {o: axial_rel(np.array(o), range(g_f.d), np.zeros(g_f.d, int)) for o in it.product(range(-HF, HF + 1), repeat=g_f.d)}
def hol_paths(U, gf, centres, lst):
    P = np.broadcast_to(I2, (len(centres), 2, 2)).copy()
    for (rel, m, sg) in lst:
        pos = centres + rel; M = U[(m,) + tuple(pos.T)]; P = P @ (M if sg > 0 else dag(M))
    return P
def msg_gauge(Us, G, k):
    d = G[0].d; Gs = [None] * (k + 1); Ug = [None] * (k + 1); stats = {}
    Gs[k - 1] = axial_gauge(Us[k - 1], G[k - 1]); Ug[k - 1] = apply_gauge(Us[k - 1], Gs[k - 1], G[k - 1])
    b2h = b2i = 0.0
    for i in range(k - 2, -1, -1):
        gf, gc = G[i], G[i + 1]; ac = su2_log(Ug[i + 1]); V = su2_exp(whitney(ac, gc, gf))
        amax = max(float((np.linalg.norm(ac[mu][gc.inside(mu)], axis=-1) / 2).max()) for mu in range(d))
        vmax = max(float((np.linalg.norm(whitney(ac, gc, gf)[mu][gf.inside(mu)], axis=-1) / 2).max()) for mu in range(d))
        b2i = max(b2i, vmax / max(amax / L, 1e-300) - 1)
        for mu in range(d):  # hol_V(S_c) = exp(a_c)
            if gc.S[mu] < 2: continue
            Xs = np.array(list(it.product(*[range(n - (1 if a == mu else 0)) for a, n in enumerate(gc.S)]))); c = L * Xs + HF
            P = np.broadcast_to(I2, (len(c), 2, 2)).copy()
            for j in range(L): P = P @ V[(mu,) + tuple((c + j * gf.E[mu]).T)]
            b2h = max(b2h, float(np.abs(P - su2_exp(ac[(mu,) + tuple(Xs.T)])).max()))
        Xc = np.array(list(it.product(*[range(n) for n in gc.S]))); cen = L * Xc + HF; Gf = np.empty(gf.S + (2, 2), complex)
        Gc = Gs[i + 1][tuple(Xc.T)]
        for o, lst in block_paths(gf, gc).items():
            HU = hol_paths(Us[i], gf, cen, lst); HVv = hol_paths(V, gf, cen, lst)
            Gf[tuple((cen + np.array(o)).T)] = dag(HU) @ Gc @ HVv
        Gs[i] = Gf; Ug[i] = apply_gauge(Us[i], Gs[i], gf)
    Gs[k] = Gs[k - 1][tuple(slice(HF, None, L) for _ in range(d))][tuple(slice(0, n) for n in G[k].S)]
    Ug[k] = apply_gauge(Us[k], Gs[k], G[k])
    sizes = [max(smax(theta(Ug[i][mu][G[i].inside(mu)])) for mu in range(d)) for i in range(k + 1)]
    return Gs, Ug, sizes, b2h, b2i
def gauge_invariance(Us, Ug, G, k, IDX):
    d = G[0].d; err = 0.0
    for i in range(k + 1):
        if min(G[i].S[:2]) >= 2: err = max(err, float(np.abs(sfun(plaqs(Us[i], G[i])) - sfun(plaqs(Ug[i], G[i]))).max()))
    for i in range(k):
        for mu in range(d):
            if (i, mu) not in IDX: continue
            idx = IDX[(i, mu)]; key = (mu,) + tuple(idx[0].T)
            def phi(UU):
                M = mbar(UU[i], G[i], idx); Wv = W0(M); V1 = UU[i + 1][key]
                return 0.5 * (np.real(np.trace(dag(Wv) @ M, axis1=-2, axis2=-1)) - np.real(np.trace(dag(V1) @ M, axis1=-2, axis2=-1)))
            err = max(err, float(np.abs(phi(Us) - phi(Ug)).max()))
    return err

def smooth_field(S, rng, d):
    X = np.indices(S); H = np.zeros((d,) + S + (3,))
    for mu in range(d):
        for nu in range(d):
            if nu == mu: continue
            c = rng.normal(size=3); ph = rng.uniform(0, 2 * np.pi)
            for j in range(3): H[mu][..., j] += c[j] * np.cos(np.pi * X[nu] / S[nu] + ph + j)
    return H
def setup(d, k):
    G = [Geo(S) for S in shapes(d, k)]
    IDX = {(i, mu): coarse_index(G[i], G[i + 1], mu) for i in range(k) for mu in range(d) if G[i + 1].S[mu] >= 2}
    return G, IDX

# ================= Part A + B: d = 4, depth 2 =================
d, k = 4, 2; G, IDX = setup(d, k); TS = (0.0025, 0.005, 0.01, 0.02, 0.04)
print(f"A/B setup d=4 k=2 shapes {[g.S for g in G]}  ({time.time() - T0:.1f} s)")
samples = []
for sd in (1, 2, 3): samples.append(("smooth", sd))
for sd in (4, 5, 6): samples.append(("noise", sd))
for sd in (7, 8, 9): samples.append(("res", sd))
samples.append(("coh", 0))
okA1 = okA2 = okA3 = okB1 = okB2 = okB3 = True; fam_max = {}; Cmax = 0.0; worst = {}
for fam, sd in samples:
    rng = np.random.default_rng(sd); S0 = G[0].S
    if fam == "smooth": H = smooth_field(S0, rng, d); res = {i: np.zeros((d,) + G[i].S + (3,)) for i in range(1, k + 1)}
    elif fam == "noise": H = rng.normal(size=(d,) + S0 + (3,)); res = {i: rng.normal(size=(d,) + G[i].S + (3,)) for i in range(1, k + 1)}
    elif fam == "res": H = np.zeros((d,) + S0 + (3,)); res = {i: rng.normal(size=(d,) + G[i].S + (3,)) for i in range(1, k + 1)}
    else:
        H = np.zeros((d,) + S0 + (3,)); res = {i: np.zeros((d,) + G[i].S + (3,)) for i in range(1, k + 1)}
        v = np.array([1.0, 0, 0]); o = (0,) * d; e0 = (1,) + (0,) * (d - 1); e1 = (0, 1) + (0,) * (d - 2)
        res[k][(0,) + o] = v; res[k][(1,) + e0] = v; res[k][(0,) + e1] = -v; res[k][(1,) + o] = -v
    Ds = []
    for t in TS:
        a0 = t * H; Us, Ws, Ms, As = build_chain(d, k, a0, res, t, IDX, G)
        E, rmax = energy_terms(Us, Ws, Ms, G, k, res, t)
        Rna = 0.5 * np.sum(su2_log(topP(Us[k])) ** 2) / E
        dB = topdB(As[k]); Elin = np.sum(dflux(As[0], G[0]) ** 2) * 0.5 / (2 * NC)
        for i in range(1, k + 1):
            for mu in range(d): Elin += KAP * 0.5 * np.sum((t * res[i][mu][G[i].inside(mu)]) ** 2) / (2 * NC)
        Rlin = 0.5 * np.sum(dB ** 2) / Elin; D = abs(Rna / Rlin - 1); Ds.append(D)
        okA1 &= Rna <= 80; fam_max[fam] = max(fam_max.get(fam, (0, 0))[0], Rna), max(fam_max.get(fam, (0, 0))[1], Rlin)
        eps = eps_hyp(Us, G, k, rmax); Gs, Ug, sizes, b2h, b2i = msg_gauge(Us, G, k)
        gi = gauge_invariance(Us, Ug, G, k, IDX); okB1 &= gi <= 1e-11; okB2 &= (b2h <= 1e-12) and (b2i <= 1e-12)
        C = max(sizes) / eps; okB3 &= C <= 450; Cmax = max(Cmax, C)
        if t == 0.01: worst[(fam, sd)] = (Rna, Rlin, eps, [x / eps for x in sizes], sizes[0] - sizes[1] / L, gi, b2h)
    okA2 &= Ds[0] <= 0.05
    if Ds[0] < 1e-7: sl = None
    else: sl = np.polyfit(np.log(TS[1:]), np.log(np.maximum(Ds[1:], 1e-300)), 1)[0]; okA3 &= 0.7 <= sl <= 2.3
    print(f"{fam:6s} seed {sd}: D(t)= " + " ".join(f"{x:.2e}" for x in Ds) + (f" slope {sl:.2f}" if sl is not None else " below floor"))
print("t=0.01 rows: fam seed | R_NA R_lin | eps | max|log U_i^g|/eps (i=0,1,2) | max|a0|-max|a1|/L | gauge-inv err | holV err")
for (f, sd), (a, b, e, cs, cd, gi, hb) in worst.items():
    print(f"  {f:6s} {sd}: {a:.4f} {b:.4f} | {e:.3e} | " + " ".join(f"{c:.3f}" for c in cs) + f" | {cd / e:+.3f}eps | {gi:.1e} | {hb:.1e}")
for f, (a, b) in fam_max.items(): print(f"A4 (info) {f}: max R_NA {a:.4f}  max R_lin {b:.4f}")
check("A1 R_NA <= N*C_loc = 80 (all samples, all t)", okA1)
check("A2 |R_NA/R_lin - 1| <= 0.05 at t = 0.0025", okA2)
check("A3 deviation slope in [0.7, 2.3] (or below floor)", okA3)
check("B1 MSG gauge leaves every s and phi invariant (<= 1e-11)", okB1)
check("B2 hol_V(S_c) = exp(a_c) and |Ia| <= max|a|/L", okB2)
check("B3 C_meas <= 450", okB3, f"max C_meas = {Cmax:.3f}")
print(f"A/B done ({time.time() - T0:.1f} s)")

# ================= Part C: d = 2, depths 1..5 =================
d = 2; tab = {}
for k in range(1, 6):
    G, IDX = setup(d, k)
    for fam, sd in (("noise", 11), ("noise", 12), ("smooth", 13), ("smooth", 14)):
        rng = np.random.default_rng(sd); S0 = G[0].S
        if fam == "noise":
            t = 0.01; a0 = t * rng.normal(size=(d,) + S0 + (3,)); res = {i: rng.normal(size=(d,) + G[i].S + (3,)) for i in range(1, k + 1)}
        else:
            t = 0.0; a0 = (0.3 / S0[0]) * smooth_field(S0, rng, d); res = {i: np.zeros((d,) + G[i].S + (3,)) for i in range(1, k + 1)}
        Us, Ws, Ms, As = build_chain(d, k, a0, res, t, IDX, G); E, rmax = energy_terms(Us, Ws, Ms, G, k, res, t)
        eps = eps_hyp(Us, G, k, rmax); Gs, Ug, sizes, _, _ = msg_gauge(Us, G, k)
        Gax = axial_gauge(Us[0], G[0]); Uax = apply_gauge(Us[0], Gax, G[0])
        cax = max(float(theta(Uax[mu][G[0].inside(mu)]).max()) for mu in range(d)) / eps
        tab[(k, fam, sd)] = (max(sizes) / eps, cax, eps)
print("C table: k | fam seed | C_meas | C_ax(level-0 axial) | eps")
for (k, f, sd), (c, ca, e) in tab.items(): print(f"  k={k} {f:6s} {sd}: {c:.3f} | {ca:.3f} | {e:.3e}")
c1 = all(v[0] <= 450 for v in tab.values())
m5 = max(v[0] for (k, f, s), v in tab.items() if k == 5); m2 = max(v[0] for (k, f, s), v in tab.items() if k == 2)
c3 = all(tab[(5, "noise", s)][1] / tab[(5, "noise", s)][0] >= 2 for s in (11, 12))
check("C1 C_meas(k) <= 450, k = 1..5", c1)
check("C2 depth-uniformity max C(5) <= 1.5 max C(2) + 0.5", m5 <= 1.5 * m2 + 0.5, f"max C(5) = {m5:.3f}, max C(2) = {m2:.3f}")
check("C3 contrast C_ax(5)/C_meas(5) >= 2 (noise)", c3, " ".join(f"{tab[(5, 'noise', s)][1] / tab[(5, 'noise', s)][0]:.2f}" for s in (11, 12)))
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}  OVERALL {'PASS' if NF == 0 else 'FAIL'}")
