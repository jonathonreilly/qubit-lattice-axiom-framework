#!/usr/bin/env python3
"""f6 (FLOW.md §22 target S3-3; criteria in checks/f6_criteria.md, written and stat-logged before this script).

Iterated two-level covariant chain for a complex lattice scalar in a U(1) background A:
  Gamma_it(A) = log det of  phi0^* M_A phi0 + k1 sum_y |phi1(y) - (Q0_A phi0)(y)|^2 + k2 sum_c |(Q1_A phi1)(c)|^2,
Q0: covariant average over level-1 blocks of side 3 (24 axial orders, fine links); Q1: covariant average of level-1 values
over level-2 blocks of side L2 (level-1 units), axial paths on FINE links from the level-1 site to the level-2 centre.
Per coarse class: joint space = (fine aliases) + (level-1 aliases), organised in blocks g = level-1 alias (its m = 81 fine
aliases + 1 level-1 coordinate). Operators: diagonal + per-block low rank + global low rank, exact.
The single block (f5's class integrand) is imported unchanged from checks/f5_cov_kernel.py.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import sys, time, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f5_cov_kernel as F

AUDIT_TIMEOUT_SEC = 7200
T0 = time.time()
ALPHA = 0.65
L1 = 3
PERMS = F.PERMS
NP_ = NF_ = 0
T48 = 48 * np.pi ** 2
TWIST = np.array([0.17, 0.29, 0.41, 0.13])  # constant twist (units of the torus momentum quantum), post-hoc V2'/V3'


def report(name, ok, msg):
    global NP_, NF_
    if ok is None:
        print(f"[{name}] NOT EVALUATED :: {msg}", flush=True); return
    NP_ += bool(ok); NF_ += (not ok)
    print(f"[{name}] {'PASS' if ok else 'FAIL'} :: {msg}", flush=True)


# ------------------------------------------------------------------ path factors with a spacing
def factor_1d_s(beta, mode, sigma, nside, spacing):
    """1D path function over positions w = spacing*j, |j| <= (nside-1)/2, for coordinate beta (f5's factor_1d at spacing 1)."""
    mu, kv = mode
    h = (nside - 1) // 2
    ws = spacing * np.arange(-h, h + 1)
    if beta == mu:
        out = np.zeros(len(ws), complex)
        for i, w in enumerate(ws):
            if w > 0:
                r = np.arange(0, w); out[i] = -np.exp(1j * kv[mu] * r).sum()
            elif w < 0:
                r = np.arange(w, 0); out[i] = np.exp(1j * kv[mu] * r).sum()
        return out
    if sigma.index(beta) < sigma.index(mu):
        return np.ones(len(ws), complex)
    return np.exp(1j * kv[beta] * ws)


def mode_terms_s(mode, nside, spacing):
    acc = {}
    for sg in PERMS:
        fs = [factor_1d_s(b, mode, sg, nside, spacing) for b in range(4)]
        key = np.round(np.concatenate(fs), 14).tobytes()
        if key in acc:
            acc[key][0] += 1 / 24
        else:
            acc[key] = [1 / 24, fs]
    return list(acc.values())


def pair_terms_s(m1, m2, nside, spacing):
    acc = {}
    for sg in PERMS:
        fs = [factor_1d_s(b, m1, sg, nside, spacing) * factor_1d_s(b, m2, sg, nside, spacing) for b in range(4)]
        key = np.round(np.concatenate(fs), 14).tobytes()
        if key in acc:
            acc[key][0] += 1 / 24
        else:
            acc[key] = [1 / 24, fs]
    return list(acc.values())


# ------------------------------------------------------------------ alias sets
class Aliases:
    """Alias momenta per coordinate qc (B,4,na) and positions ws (nw,) for the transforms."""

    def __init__(self, qc, ws):
        self.qc = qc
        self.ph = np.exp(1j * qc[..., None] * ws[None, None, None, :])  # (B,4,na,nw)

    def transform(self, f, beta, sign):
        ph = self.ph[:, beta] if sign > 0 else np.conj(self.ph[:, beta])
        return ph @ f  # (B, na)

    def cp_vector(self, terms, sign):
        out = 0
        for wgt, fs in terms:
            out = out + wgt * tensor4([self.transform(fs[b], b, sign) for b in range(4)])
        return out

    def avg(self):
        return (self.ph.sum(-1) / self.ph.shape[-1]).real  # (B,4,na)


def tensor4(vs):
    B = vs[0].shape[0]
    return np.einsum('bi,bj,bk,bl->bijkl', *vs).reshape(B, -1)


class Level:
    """Per-class geometry of the two-level chain at shift s: fine aliases in block order (J..., I...), level-1 aliases J."""

    def __init__(self, P, s, L2):
        self.L2 = L2
        ell = L1 * L2
        self.ell, self.n1, self.m = ell, L2 ** 4, L1 ** 4
        B = P.shape[0]
        J = np.arange(L2); I = np.arange(L1)
        Kord = (J[:, None] + L2 * I[None, :]).reshape(-1)  # K = J + L2*I, ordered (J, I)
        base = P[:, :, None] + s[None, :, None]
        qf = base + 2 * np.pi * Kord[None, None, :] / ell          # (B,4,ell) fine aliases
        q1 = base + 2 * np.pi * J[None, None, :] / ell             # (B,4,L2) level-1 aliases
        self.qf, self.q1 = qf, q1
        h1 = (L1 - 1) // 2
        self.Af = Aliases(qf, np.arange(-h1, h1 + 1).astype(float))
        h2 = (L2 - 1) // 2
        self.A1 = Aliases(q1, (L1 * np.arange(-h2, h2 + 1)).astype(float))
        cosq = np.cos(qf)
        om = 0
        for b in range(4):
            shp = [B, 1, 1, 1, 1]; shp[b + 1] = ell
            om = om + (2 - 2 * cosq[:, b, :]).reshape(shp)
        self.om = self.blocks(np.broadcast_to(om, (B,) + (ell,) * 4).reshape(B, -1))
        self.u = self.blocks(tensor4([self.Af.avg()[:, b, :] for b in range(4)]))     # Q0 symbol (real)
        self.v = tensor4([self.A1.avg()[:, b, :] for b in range(4)])                   # Q1 symbol (real), (B,n1)
        self.B = B

    def blocks(self, x):
        """fine vector (B, ell^4) in (J1,I1,...,J4,I4) order -> (B, n1, m)."""
        B = x.shape[0]; L2 = self.L2
        y = x.reshape((B,) + (L2, L1) * 4)
        y = y.transpose(0, 1, 3, 5, 7, 2, 4, 6, 8)
        return y.reshape(B, self.n1, self.m)

    def coord(self, b):
        """fine coordinate b of the aliases, in block shape."""
        B = self.B; ell = self.ell
        shp = [B, 1, 1, 1, 1]; shp[b + 1] = ell
        x = np.broadcast_to(self.qf[:, b, :].reshape(shp), (B,) + (ell,) * 4).reshape(B, -1)
        return self.blocks(x)


# ------------------------------------------------------------------ structured operators on the joint space
# Op = (d, Ab, Bb, Ag, Bg): d (B,n1,M1); Ab,Bb (B,n1,M1,rb) per-block low rank A B^T; Ag,Bg (B,n1,M1,rg) global A B^T.
def op_apply(X, V):
    d, Ab, Bb, Ag, Bg = X
    out = d[..., None] * V
    if Ab.shape[-1]:
        t = np.einsum('bgis,bgir->bgsr', Bb, V); out = out + np.einsum('bgis,bgsr->bgir', Ab, t)
    if Ag.shape[-1]:
        t = np.einsum('bgis,bgir->bsr', Bg, V); out = out + np.einsum('bgis,bsr->bgir', Ag, t)
    return out


def op_applyT_local(X, V):
    d, Ab, Bb, Ag, Bg = X
    out = d[..., None] * V
    if Ab.shape[-1]:
        t = np.einsum('bgis,bgir->bgsr', Ab, V); out = out + np.einsum('bgis,bgsr->bgir', Bb, t)
    return out


def op_mul(X, Y):
    dx, Axb, Bxb, Axg, Bxg = X; dy, Ayb, Byb, Ayg, Byg = Y
    d = dx * dy
    Ab = np.concatenate([dx[..., None] * Ayb, Axb], -1)
    M = np.einsum('bgjs,bgjr->bgsr', Ayb, Bxb)
    Bb = np.concatenate([Byb, dy[..., None] * Bxb + np.einsum('bgis,bgsr->bgir', Byb, M)], -1)
    Ag = np.concatenate([op_apply(X, Ayg), Axg], -1)
    Bg = np.concatenate([Byg, op_applyT_local(Y, Bxg)], -1)
    return (d, Ab, Bb, Ag, Bg)


def op_tr(X):
    d, Ab, Bb, Ag, Bg = X
    return d.sum((1, 2)) + np.einsum('bgir,bgir->b', Ab, Bb) + np.einsum('bgir,bgir->b', Ag, Bg)


def jv(fine, lev):
    """joint vector (B,n1,M1) from a fine part (B,n1,m) (or 0) and a level-1 part (B,n1) (or 0)."""
    return np.concatenate([fine, lev[..., None]], -1)


def stack(vs):
    return np.stack(vs, -1)


# ------------------------------------------------------------------ the iterated class integrand
def iter_class_integrand(P, k1, mu, nu, L2, kpairs, want_cov=True):
    """kpairs: list of (kt1, kt2) = (k1 L1^-4, k2 l^-4) per kappa. Returns dict -> (total, M-only, cov) per class."""
    k1 = np.asarray(k1, float); k2 = -k1
    m1 = (mu, k1); m2 = (nu, k2)
    C0 = Level(P, np.zeros(4), L2); C1 = Level(P, k1, L2)
    B, n1, m = C0.B, C0.n1, C0.m
    Z1 = np.zeros((B, n1)); Zf = np.zeros((B, n1, m))
    one = np.ones((B, n1))
    # Q0 vertex vectors (fine aliases, block shape); f5's conventions with L4 -> 3^-4
    l4 = float(L1) ** -4
    t1 = mode_terms_s(m1, L1, 1); t2 = mode_terms_s(m2, L1, 1); t12 = pair_terms_s(m1, m2, L1, 1)
    e0_1 = C0.blocks(1j * l4 * C0.Af.cp_vector(t1, +1)); f0_1p = C1.blocks(-1j * l4 * C1.Af.cp_vector(t1, -1))
    f0_1 = C0.blocks(-1j * l4 * C0.Af.cp_vector(t1, -1)); e0_2p = C1.blocks(1j * l4 * C1.Af.cp_vector(t2, +1))
    e0_2 = C0.blocks(1j * l4 * C0.Af.cp_vector(t2, +1)); f0_2 = C0.blocks(-1j * l4 * C0.Af.cp_vector(t2, -1))
    e0_12 = C0.blocks(-l4 * C0.Af.cp_vector(t12, +1)); f0_12 = C0.blocks(-l4 * C0.Af.cp_vector(t12, -1))
    # Q1 vertex vectors (level-1 aliases), positions 3j, weight L2^-4
    l24 = float(L2) ** -4
    s1 = mode_terms_s(m1, L2, L1); s2 = mode_terms_s(m2, L2, L1); s12 = pair_terms_s(m1, m2, L2, L1)
    e1_1 = 1j * l24 * C0.A1.cp_vector(s1, +1); f1_1p = -1j * l24 * C1.A1.cp_vector(s1, -1)
    f1_1 = -1j * l24 * C0.A1.cp_vector(s1, -1); e1_2p = 1j * l24 * C1.A1.cp_vector(s2, +1)
    e1_2 = 1j * l24 * C0.A1.cp_vector(s2, +1); f1_2 = -1j * l24 * C0.A1.cp_vector(s2, -1)
    e1_12 = -l24 * C0.A1.cp_vector(s12, +1); f1_12 = -l24 * C0.A1.cp_vector(s12, -1)
    # M vertices (f5's formulas), fine diagonal
    qm0 = C0.coord(mu); qn1 = C1.coord(nu)
    md1 = 1j * (np.exp(1j * qm0) - np.exp(-1j * (qm0 + k1[mu])))
    md2 = 1j * (np.exp(1j * qn1) - np.exp(-1j * (qn1 + k2[nu])))
    d12 = (2 * np.cos(qm0)).astype(complex) if mu == nu else np.zeros_like(qm0, dtype=complex)
    u, up, v, vp = C0.u, C1.u, C0.v, C1.v
    E0 = np.zeros((B, n1, m + 1, 0), complex)
    out = {}
    for (kt1, kt2) in kpairs:
        def G_of(C):
            om, uu, vv = C.om, C.u, C.v
            a = (uu ** 2 / om).sum(-1)
            sig = a + 1 / kt1
            w = jv(uu / om, Z1); e = jv(Zf, one)
            d = jv(1 / om, sig).astype(complex)
            xi = jv(uu / om * vv[..., None], sig * vv)
            tau = 1 / ((sig * vv ** 2).sum(-1) + 1 / kt2)
            return (d, stack([w, e]).astype(complex), stack([e, w]).astype(complex),
                    (-tau[:, None, None] * xi)[..., None].astype(complex), xi[..., None].astype(complex))
        G = G_of(C0); Gp = G_of(C1)
        mu_ = -u; mup = -up
        D1 = (jv(md1, Z1),
              kt1 * stack([jv(mup, one), jv(-f0_1p, Z1)]), stack([jv(-e0_1, Z1), jv(mu_, one)]),
              kt2 * stack([jv(Zf, vp), jv(Zf, f1_1p)]), stack([jv(Zf, e1_1), jv(Zf, v)]))
        D2 = (jv(md2, Z1),
              kt1 * stack([jv(mu_, one), jv(-f0_2, Z1)]), stack([jv(-e0_2p, Z1), jv(mup, one)]),
              kt2 * stack([jv(Zf, v), jv(Zf, f1_2)]), stack([jv(Zf, e1_2p), jv(Zf, vp)]))
        D12 = (jv(d12, Z1),
               kt1 * stack([jv(mu_, one), jv(-f0_12, Z1), jv(-f0_1, Z1), jv(-f0_2, Z1)]),
               stack([jv(-e0_12, Z1), jv(mu_, one), jv(-e0_2, Z1), jv(-e0_1, Z1)]),
               kt2 * stack([jv(Zf, v), jv(Zf, f1_12), jv(Zf, f1_1), jv(Zf, f1_2)]),
               stack([jv(Zf, e1_12), jv(Zf, v), jv(Zf, e1_2), jv(Zf, e1_1)]))
        tot = op_tr(op_mul(G, D12)) - op_tr(op_mul(op_mul(op_mul(G, D2), Gp), D1))
        D1m = (D1[0], E0, E0, E0, E0); D2m = (D2[0], E0, E0, E0, E0); D12m = (D12[0], E0, E0, E0, E0)
        mon = op_tr(op_mul(G, D12m)) - op_tr(op_mul(op_mul(op_mul(G, D2m), Gp), D1m))
        cov = np.zeros(B, complex)
        if want_cov:
            # log det J11, J11 = kt1 + kt2 N^dag N on level-1 (f5's diag + low-rank algebra)
            def g11(vv):
                sc = (kt2 / kt1 ** 2) / (1 + (kt2 / kt1) * (vv ** 2).sum(-1))
                return (np.full(vv.shape, 1 / kt1, complex), (-sc[:, None] * vv)[..., None].astype(complex),
                        vv[..., None].astype(complex))
            H, Hp = g11(v), g11(vp)
            Zr = np.zeros((B, n1), complex)
            c1 = (Zr, F.stackc([kt2 * vp, kt2 * f1_1p]), F.stackc([e1_1, v]))
            c2 = (Zr, F.stackc([kt2 * v, kt2 * f1_2]), F.stackc([e1_2p, vp]))
            c12 = (Zr, F.stackc([kt2 * v, kt2 * f1_12, kt2 * f1_1, kt2 * f1_2]), F.stackc([e1_12, v, e1_2, e1_1]))
            cov = F.lr_tr(F.lr_mul(H, c12)) - F.lr_tr(F.lr_mul(F.lr_mul(F.lr_mul(H, c2), Hp), c1))
        out[(kt1, kt2)] = (tot, mon, cov)
    return out


def kpair(kc, L2):
    ell = L1 * L2
    s = kc * (1 + L2 ** -2.0)
    return (s * L1 ** 2 * float(L1) ** -4, s * ell ** 2 * float(ell) ** -4)


# ------------------------------------------------------------------ quadrature (f5b's)
def nodes(ell, n):
    t = (np.arange(n) + 0.5) * (2 * np.pi / ell) / n - np.pi / ell
    P = t - ALPHA * np.sin(ell * t) / ell
    w = 1 - ALPHA * np.cos(ell * t)
    return P, w / w.sum()


def grid(ell, n):
    P, w = nodes(ell, n)
    pos = np.where(P > 0)[0]
    pts, wts = [], []
    for i in range(n):
        for j in range(n):
            for a in pos:
                for b in pos:
                    if P[a] > P[b]:
                        continue
                    mult = 4 * (1 if a == b else 2)
                    pts.append((P[i], P[j], P[a], P[b])); wts.append(w[i] * w[j] * w[a] * w[b] * mult)
    wts = np.array(wts)
    return np.array(pts), wts / wts.sum()


def batch_for(L2):
    return max(1, int(4.0e4 // (L2 ** 4 * (L1 ** 4 + 1))))


def c_iter(L2, kcs, n, h=3e-4):
    ell = L1 * L2
    pts, wts = grid(ell, n)
    kps = [kpair(kc, L2) for kc in kcs]
    acc = {s: {kp: np.zeros(3, complex) for kp in kps} for s in [(1, 1), (1, -1), (-1, 1), (-1, -1)]}
    bt = batch_for(L2)
    for s in acc:
        kv = [s[0] * h, s[1] * h, 0, 0]
        for i in range(0, len(pts), bt):
            r = iter_class_integrand(pts[i:i + bt], kv, 0, 1, L2, kps)
            ww = wts[i:i + bt]
            for kp in kps:
                acc[s][kp] += np.array([(ww * r[kp][j]).sum() for j in range(3)])
    res = {}
    for kc, kp in zip(kcs, kps):
        d = (acc[(1, 1)][kp] - acc[(1, -1)][kp] - acc[(-1, 1)][kp] + acc[(-1, -1)][kp]) / (4 * h * h) * ell ** -4
        res[kc] = (-d.real / 2, np.max(np.abs(d.imag / 2)))  # (c_tot, c_M, c_cov), max imag
    return res


def c_single(ell, kcs, n, h=3e-4):
    pts, wts = grid(ell, n)
    kappas = [kc * ell ** 2 for kc in kcs]
    acc = {s: {kap: np.zeros(2, complex) for kap in kappas} for s in [(1, 1), (1, -1), (-1, 1), (-1, -1)]}
    bt = max(1, int(2.0e5 // ell ** 4))
    for s in acc:
        kv = [s[0] * h, s[1] * h, 0, 0]
        for i in range(0, len(pts), bt):
            r = F.class_integrand(pts[i:i + bt], kv, 0, 1, ell, kappas)
            ww = wts[i:i + bt]
            for kap in kappas:
                acc[s][kap] += np.array([(ww * r[kap][0]).sum(), (ww * r[kap][1]).sum()])
    res = {}
    for kc, kap in zip(kcs, kappas):
        d = (acc[(1, 1)][kap] - acc[(1, -1)][kap] - acc[(-1, 1)][kap] + acc[(-1, -1)][kap]) / (4 * h * h) * ell ** -4
        res[kc] = (-d.real / 2, np.max(np.abs(d.imag / 2)))
    return res


def loadavg():
    return os.getloadavg()[0]


# ------------------------------------------------------------------ main
def main():
    print("f6: iterated two-level covariant chain vs single block; criteria checks/f6_criteria.md", flush=True)
    rng = np.random.default_rng(6)
    # (V1) A = 0 propagator identity at ell = 9
    L2 = 3; ell = 9; kc = 1.0
    Ps = rng.uniform(-np.pi / ell, np.pi / ell, (4, 4))
    C = Level(Ps, np.zeros(4), L2)
    kt1, kt2 = kpair(kc, L2)
    a = (C.u ** 2 / C.om).sum(-1); sig = a + 1 / kt1
    tau = 1 / ((sig * C.v ** 2).sum(-1) + 1 / kt2)
    xi_f = (C.u / C.om * C.v[..., None]).reshape(4, -1)        # fine part of G0 nu
    Cs = F.Classes(Ps, np.zeros(4), ell)
    cs = kc * ell ** 2 * float(ell) ** -4
    gs = 1 / Cs.om; us = gs * Cs.d
    s5 = cs / (1 + cs * (Cs.d * us).sum(-1))
    # compare tau*xi xi^T with s5*us us^T via sorted entries of the rank-1 vectors and the scalars
    xs = np.sort(np.abs(xi_f), -1); ys = np.sort(np.abs(us), -1)
    relv = np.max(np.abs(xs - ys)) / np.max(np.abs(ys)); rels = np.max(np.abs(tau - s5) / np.abs(s5))
    omi = np.sort(C.om.reshape(4, -1), -1); oms = np.sort(Cs.om, -1)
    relo = np.max(np.abs(omi - oms)) / np.max(oms)
    report("V1", max(relv, rels, relo) <= 1e-12, f"rank-1 vector {relv:.1e}, coefficient {rels:.1e}, diagonal {relo:.1e}")
    # (V2) reduction L2 = 1 vs f5 at ell = 3
    Ps = rng.uniform(-np.pi / 3, np.pi / 3, (5, 4)); kv = [1e-3, 2e-3, 0, 0]
    kp = kpair(1.0, 1)
    ce = 1 / (1 / kp[0] + 1 / kp[1])
    ri = iter_class_integrand(Ps, kv, 0, 1, 1, [kp])[kp]
    rf = F.class_integrand(Ps, kv, 0, 1, 3, [ce * 81.0])[ce * 81.0]
    rT = np.max(np.abs(ri[0] - rf[0]) / np.abs(rf[0])); rM = np.max(np.abs(ri[1] - rf[1]) / np.abs(rf[1]))
    report("V2", max(rT, rM) <= 1e-10, f"L2=1 vs f5 ell=3: total {rT:.1e}, M-only {rM:.1e}; cov integrand max {np.max(np.abs(ri[2])):.1e}")
    # POST-HOC, labelled (not a pre-registered criterion; added after a smoke test, before the official run, logged in
    # FLOW_LOG): the joint and the integrated-out (f5) forms assign the second-order kernel terms that pass through the
    # level-1 coordinate of the class P - k1 to different classes, so per-class integrands differ by a class-shift term;
    # the class SUM over a shift-closed set (all classes of a torus, k a torus momentum) must agree exactly.
    nfV = 6
    PtV = np.array(list(itertools.product(2 * np.pi / nfV * np.arange(nfV // 3), repeat=4))) + TWIST * (2 * np.pi / nfV)
    worstV = 0
    for kvV in [2 * np.pi / nfV * np.array([1., 1., 0., 0.]), 2 * np.pi / nfV * np.array([1., 2., 1., 0.])]:
        si = iter_class_integrand(PtV, kvV, 0, 1, 1, [kp])[kp][0].sum()
        sf = F.class_integrand(PtV, kvV, 0, 1, 3, [ce * 81.0])[ce * 81.0][0].sum()
        worstV = max(worstV, abs(si - sf) / abs(sf))
    print(f"   [V2' POST-HOC] torus (fine side 6) class sums, L2=1 vs f5: max rel {worstV:.1e} "
          f"({'within' if worstV <= 1e-10 else 'outside'} 1e-10)", flush=True)
    print(f"   (t={time.time()-T0:.0f}s)", flush=True)
    # (V3) Ward identity on the torus of fine side 18 (ell = 9)
    nf = 18; L2 = 3; kp = kpair(1.0, 3)
    Ptor = np.array(list(itertools.product(2 * np.pi / nf * np.arange(nf // 9), repeat=4)))
    # The untwisted torus contains the fine alias q = 0 (omega = 0) in the class P = 0, where the class formula (built on
    # 1/omega) is singular: (V3) as pre-registered is NOT EVALUATED. POST-HOC, labelled (logged before the official run):
    # (V3') the same Ward identity on the torus with a constant twist (a flat background, under which Gamma stays gauge
    # invariant); the twisted class set is still closed under the torus momenta k.
    report("V3", None, "untwisted torus has q = 0 in class P = 0, where the class formula is singular; see V3'")
    Ptor = Ptor + TWIST * (2 * np.pi / nf)
    okW = True; msg = []
    for kvB in [2 * np.pi / nf * np.array([1., 1., 0., 0.]), 2 * np.pi / nf * np.array([1., 2., 1., 0.])]:
        Ts = []
        for n1_ in range(4):
            r = iter_class_integrand(Ptor, kvB, n1_, 1, L2, [kp])[kp]
            Ts.append((r[0].sum(), r[1].sum()))
        w = sum((np.exp(1j * kvB[n]) - 1) * Ts[n][0] for n in range(4)); sc = sum(abs(Ts[n][0]) for n in range(4))
        wm = sum((np.exp(1j * kvB[n]) - 1) * Ts[n][1] for n in range(4)); scm = sum(abs(Ts[n][1]) for n in range(4))
        okW &= abs(w) <= 1e-10 * sc
        msg.append(f"k={np.round(kvB/(2*np.pi/nf)).astype(int).tolist()}: |Ward| {abs(w):.1e} (scale {sc:.2e}); M-only {abs(wm):.1e} (scale {scm:.2e})")
    print(f"   [V3' POST-HOC, twisted torus] {'within' if okW else 'outside'} 1e-10 :: " + "; ".join(msg), flush=True)
    print(f"   (t={time.time()-T0:.0f}s)", flush=True)
    # (V4) symmetry
    Ps = rng.uniform(-np.pi / 9, np.pi / 9, (5, 4)); kv = [1e-3, 2e-3, 0, 0]; kp = kpair(1.0, 3)
    base = iter_class_integrand(Ps, kv, 0, 1, 3, [kp])[kp][0]
    worst = 0
    for R in (lambda P: P * np.array([1, 1, -1, 1]), lambda P: P * np.array([1, 1, 1, -1]), lambda P: P[:, [0, 1, 3, 2]]):
        fr = iter_class_integrand(R(Ps), kv, 0, 1, 3, [kp])[kp][0]
        worst = max(worst, np.max(np.abs(fr - base) / np.abs(base)))
    report("V4", worst <= 1e-10, f"max relative symmetry defect {worst:.1e}")
    print(f"   (t={time.time()-T0:.0f}s)", flush=True)
    # (Q6) quadrature
    tq = time.time()
    q10 = c_iter(3, [1.0], 10)[1.0][0][0]; q14 = c_iter(3, [1.0], 14)[1.0][0][0]
    report("Q6", abs(q10 - q14) <= 1e-4 * abs(q14), f"c_it(9,1): n=10 {q10:.9f}, n=14 {q14:.9f}, rel {abs(q10-q14)/abs(q14):.1e}  [{time.time()-tq:.0f}s]")
    # ---------------- scan
    kcs = [0.25, 1.0, 4.0]
    tabI, tabS, wall, imags = {}, {}, {}, []
    for L2 in (3, 5):
        ell = 3 * L2
        t1_ = time.time(); tabI[ell] = c_iter(L2, kcs, 10); wI = time.time() - t1_
        t2_ = time.time(); tabS[ell] = c_single(ell, kcs, 10); wS = time.time() - t2_
        wall[ell] = (wI, wS)
        imags += [tabI[ell][kc][1] for kc in kcs] + [tabS[ell][kc][1] for kc in kcs]
        print(f"   l={ell}: " + "; ".join(
            f"kc={kc}: it c={tabI[ell][kc][0][0]:.8f} cM={tabI[ell][kc][0][1]:.8f} cK={tabI[ell][kc][0][0]-tabI[ell][kc][0][1]:.8f} "
            f"ccov={tabI[ell][kc][0][2]:.8f} | single c={tabS[ell][kc][0][0]:.8f} cM={tabS[ell][kc][0][1]:.8f} cK={tabS[ell][kc][0][0]-tabS[ell][kc][0][1]:.8f}"
            for kc in kcs) + f"  [iter {wI:.0f}s, single {wS:.0f}s, t={time.time()-T0:.0f}s, load {loadavg():.1f}]", flush=True)
    proj = 4.2 * (wall[15][0] + wall[15][1])
    run21 = proj <= 3000 and loadavg() < 8
    print(f"   [rule] projected l=21 time {proj:.0f}s, load {loadavg():.1f}: {'RUN' if run21 else 'SKIP'}", flush=True)
    if run21:
        t1_ = time.time(); tabI[21] = c_iter(7, kcs, 10); wI = time.time() - t1_
        t2_ = time.time(); tabS[21] = c_single(21, kcs, 10); wS = time.time() - t2_
        imags += [tabI[21][kc][1] for kc in kcs] + [tabS[21][kc][1] for kc in kcs]
        print(f"   l=21: " + "; ".join(
            f"kc={kc}: it c={tabI[21][kc][0][0]:.8f} cM={tabI[21][kc][0][1]:.8f} cK={tabI[21][kc][0][0]-tabI[21][kc][0][1]:.8f} "
            f"ccov={tabI[21][kc][0][2]:.8f} | single c={tabS[21][kc][0][0]:.8f} cM={tabS[21][kc][0][1]:.8f} cK={tabS[21][kc][0][0]-tabS[21][kc][0][1]:.8f}"
            for kc in kcs) + f"  [iter {wI:.0f}s, single {wS:.0f}s, t={time.time()-T0:.0f}s]", flush=True)
    # ---------------- criteria
    ells = sorted(tabI)
    cmax = max(abs(tabI[e][kc][0][j]) for e in ells for kc in kcs for j in range(3))
    okM = all(abs(tabI[e][kc][0][1] - tabS[e][kc][0][1]) <= 1e-9 * abs(tabS[e][kc][0][1]) for e in ells for kc in kcs)
    worstM = max(abs(tabI[e][kc][0][1] - tabS[e][kc][0][1]) / abs(tabS[e][kc][0][1]) for e in ells for kc in kcs)
    report("V1b", okM, f"max |c_it^M - c_s^M|/|c_s^M| = {worstM:.1e}")
    report("V5", max(imags) <= 1e-8 * cmax, f"max |Im| = {max(imags):.1e} (max |c| = {cmax:.2e})")
    sl = lambda f, a, b: (f(b) - f(a)) / np.log(b / a) * T48
    okG = okH = okC = True; okG2 = True; lines = []
    for kc in kcs:
        cKi = lambda e: tabI[e][kc][0][0] - tabI[e][kc][0][1]
        cKs = lambda e: tabS[e][kc][0][0] - tabS[e][kc][0][1]
        cDel = lambda e: cKi(e) - cKs(e)
        cCov = lambda e: tabI[e][kc][0][2]
        sG = sl(cKi, 9, 15); sH = sl(cDel, 9, 15); sC = sl(cCov, 9, 15)
        sTi = sl(lambda e: tabI[e][kc][0][0], 9, 15); sTs = sl(lambda e: tabS[e][kc][0][0], 9, 15)
        okG &= abs(sG) <= 0.005; okH &= abs(sH) <= 0.005; okC &= abs(sC) <= 0.005
        line = f"kc={kc}: s_it^K(9,15) {sG:+.5f}, s^Delta(9,15) {sH:+.5f}, s^cov(9,15) {sC:+.5f}; total s_it {sTi:.4f}, s_s {sTs:.4f}"
        if 21 in tabI:
            sG2 = sl(cKi, 15, 21)
            okG2 &= abs(sG2) <= 0.005 and abs(sG2) <= abs(sG)
            line += (f"; s_it^K(15,21) {sG2:+.5f}, s^Delta(15,21) {sl(cDel, 15, 21):+.5f}, s^cov(15,21) {sl(cCov, 15, 21):+.5f}, "
                     f"total s_it(15,21) {sl(lambda e: tabI[e][kc][0][0], 15, 21):.4f}")
        lines.append(line)
    for line in lines:
        print("   " + line, flush=True)
    report("G6", okG, "|s_it^K(9,15)| x 48pi^2 <= 0.005 for each kc (values above)")
    report("H6", okH, "|s^Delta(9,15)| x 48pi^2 <= 0.005 for each kc (values above)")
    report("C6", okC, "|s^cov(9,15)| x 48pi^2 <= 0.005 for each kc (values above)")
    report("G6'", okG2 if 21 in tabI else None, "l = 21 " + ("run" if 21 in tabI else "not run (rule)"))
    print(f"f6 done: PASS={NP_} FAIL={NF_}; wall {time.time()-T0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
