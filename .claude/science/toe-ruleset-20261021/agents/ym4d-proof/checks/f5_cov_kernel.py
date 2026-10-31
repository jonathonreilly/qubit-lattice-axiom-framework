#!/usr/bin/env python3
"""f5 (FLOW.md §14, T1 (R4); criteria in checks/f5_criteria.md, written before this script).

Complex unit-charge lattice scalar in a U(1) background A, massless, IR-regulated by a gauge-COVARIANT soft block kernel
K_A = kappa Q_A^dag Q_A, (Q_A phi)(c) = l^-4 sum_{x in B(c)} (1/24) sum_sigma exp(i int_{sigma: x->c} A) phi(x).
Gamma(A) = log det(M_A + K_A). beta = sum_z z1 z2 Pi_12(z) of the l-translation-averaged Hessian at A = 0; c_Gamma = beta/2.
Per coarse momentum class P (aliases P_K = P + 2 pi K / l): G(P) = (diag w + c d d^T)^{-1} (c = kappa l^-4), first- and
second-order vertices as diagonal + low-rank operators between classes P and P + k; T(k) = l^-4 avg_P {tr G d12 - tr G d2 G' d1}.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import sys, time, itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 3600
T0 = time.time()
PERMS = list(itertools.permutations(range(4)))
NPASS = NFAIL = 0


def report(name, ok, msg):
    global NPASS, NFAIL
    NPASS += bool(ok); NFAIL += (not ok)
    print(f"[{name}] {'PASS' if ok else 'FAIL'} :: {msg}", flush=True)


# ---------------------------------------------------------------- 1D path factors
def factor_1d(beta, mode, sigma, ell):
    """1D function over w in -h..h for coordinate beta of lambda_sigma for a mode (mu, kvec)."""
    mu, kv = mode
    h = (ell - 1) // 2
    ws = np.arange(-h, h + 1)
    if beta == mu:
        out = np.zeros(ell, complex)
        for i, w in enumerate(ws):
            if w > 0:
                r = np.arange(0, w); out[i] = -np.exp(1j * kv[mu] * r).sum()
            elif w < 0:
                r = np.arange(w, 0); out[i] = np.exp(1j * kv[mu] * r).sum()
        return out
    if sigma.index(beta) < sigma.index(mu):
        return np.ones(ell, complex)
    return np.exp(1j * kv[beta] * ws)


class Classes:
    """Alias structure for a batch of class representatives P (B x 4), shifted by s (4-vector)."""

    def __init__(self, P, s, ell):
        self.ell = ell
        h = (ell - 1) // 2
        ws = np.arange(-h, h + 1)
        K = np.arange(ell)
        q = P[:, :, None] + s[None, :, None] + 2 * np.pi * K[None, None, :] / ell  # (B,4,l)
        self.q = q
        self.ph = np.exp(1j * q[..., None] * ws[None, None, None, :])  # (B,4,l,w)
        cosq = np.cos(q)
        B = P.shape[0]
        om = np.zeros((B,) + (ell,) * 4)
        for b in range(4):
            shp = [B, 1, 1, 1, 1]; shp[b + 1] = ell
            om = om + (2 - 2 * cosq[:, b, :]).reshape(shp)
        self.om = om.reshape(B, -1)
        Dl = (self.ph.sum(-1) / ell).real  # (B,4,l)
        self.d = self.tensor([Dl[:, b, :] for b in range(4)]).real
        self.cosq = cosq

    @staticmethod
    def tensor(vs):
        B = vs[0].shape[0]
        return np.einsum('bi,bj,bk,bl->bijkl', *vs).reshape(B, -1)

    def transform(self, f, beta, sign):
        """sum_w f(w) exp(sign*i q_beta w) over aliases: (B,l)."""
        ph = self.ph[:, beta] if sign > 0 else np.conj(self.ph[:, beta])
        return ph @ f

    def cp_vector(self, terms, sign):
        """sum over terms (weight, [f_beta]) of the tensor product of transforms."""
        out = 0
        for wgt, fs in terms:
            out = out + wgt * self.tensor([self.transform(fs[b], b, sign) for b in range(4)])
        return out


def mode_terms(mode, ell):
    acc = {}
    for sg in PERMS:
        fs = [factor_1d(b, mode, sg, ell) for b in range(4)]
        key = tuple(np.round(np.concatenate(fs), 14).tobytes() for _ in [0])
        if key in acc:
            acc[key][0] += 1 / 24
        else:
            acc[key] = [1 / 24, fs]
    return list(acc.values())


def pair_terms(m1, m2, ell):
    acc = {}
    for sg in PERMS:
        fs = [factor_1d(b, m1, sg, ell) * factor_1d(b, m2, sg, ell) for b in range(4)]
        key = np.round(np.concatenate(fs), 14).tobytes()
        if key in acc:
            acc[key][0] += 1 / 24
        else:
            acc[key] = [1 / 24, fs]
    return list(acc.values())


# ---------------------------------------------------------------- diag + low-rank algebra (X = diag(x) + A B^T)
def lr_mul(X, Y):
    dx, Ax, Bx = X; dy, Ay, By = Y
    d = dx * dy
    if Ay.shape[-1] == 0 and Ax.shape[-1] == 0:
        e = np.zeros(d.shape + (0,), complex); return (d, e, e)
    A = np.concatenate([dx[..., None] * Ay, Ax], axis=-1)
    if Ax.shape[-1] > 0 and Ay.shape[-1] > 0:
        Mx = np.einsum('bnr,bns->brs', Ay, Bx)
        B2 = dy[..., None] * Bx + np.einsum('bnr,brs->bns', By, Mx)
    else:
        B2 = dy[..., None] * Bx
    B = np.concatenate([By, B2], axis=-1)
    return (d, A, B)


def lr_tr(X):
    d, A, B = X
    return d.sum(-1) + np.einsum('bnr,bnr->b', A, B)


def stackc(vs):
    return np.stack(vs, axis=-1)


# ---------------------------------------------------------------- class integrand
def class_integrand(P, k1, mu, nu, ell, kappas, dense=False):
    """Returns dict kappa -> (total, Monly) arrays over the batch P, of
    tr G d12 - tr G d2 G' d1  (per class; T = l^-4 * avg over classes)."""
    k1 = np.asarray(k1, float); k2 = -k1
    m1 = (mu, k1); m2 = (nu, k2)
    C0 = Classes(P, np.zeros(4), ell)      # class P
    C1 = Classes(P, k1, ell)               # class P + k1
    t1 = mode_terms(m1, ell); t2 = mode_terms(m2, ell); t12 = pair_terms(m1, m2, ell)
    L4 = float(ell) ** -4
    e1 = 1j * L4 * C0.cp_vector(t1, +1)        # E_1(P_K)
    f1p = -1j * L4 * C1.cp_vector(t1, -1)      # F_1((P+k1)_K)
    f1 = -1j * L4 * C0.cp_vector(t1, -1)       # F_1(P_K)
    e2p = 1j * L4 * C1.cp_vector(t2, +1)       # E_2((P+k1)_K)
    e2 = 1j * L4 * C0.cp_vector(t2, +1)        # E_2(P_K)
    f2 = -1j * L4 * C0.cp_vector(t2, -1)       # F_2(P_K)
    e12 = -L4 * C0.cp_vector(t12, +1)
    f12 = -L4 * C0.cp_vector(t12, -1)
    d, dp = C0.d.astype(complex), C1.d.astype(complex)
    q0 = C0.q; q1 = C1.q
    # M vertices, diagonal in K
    def rs(a):  # (B,4,l) component -> (B, l^4) broadcast for coordinate b
        return a
    B = P.shape[0]
    def coord(qarr, b):
        shp = [B, 1, 1, 1, 1]; shp[b + 1] = ell
        return np.broadcast_to(qarr[:, b, :].reshape(shp), (B,) + (ell,) * 4).reshape(B, -1)
    qm0 = coord(q0, mu); qn1 = coord(q1, nu)
    md1 = 1j * (np.exp(1j * qm0) - np.exp(-1j * (qm0 + k1[mu])))          # input P_K
    md2 = 1j * (np.exp(1j * qn1) - np.exp(-1j * (qn1 + k2[nu])))          # input (P+k1)_K
    d12 = (2 * np.cos(qm0)) if mu == nu else np.zeros_like(qm0)
    d12 = d12.astype(complex)
    out = {}
    Z = np.zeros((B, ell ** 4, 0), complex)
    for kap in kappas:
        c = kap * L4
        if not dense:
            g, gp = 1 / C0.om, 1 / C1.om
            u, up = g * d, gp * dp
            s = c / (1 + c * (d * u).sum(-1)); sp = c / (1 + c * (dp * up).sum(-1))
            G = (g.astype(complex), (-s[:, None] * u)[..., None], u[..., None])
            Gp = (gp.astype(complex), (-sp[:, None] * up)[..., None], up[..., None])
            D1 = (md1, stackc([c * dp, c * f1p]), stackc([e1, d]))
            D2 = (md2, stackc([c * d, c * f2]), stackc([e2p, dp]))
            D12 = (d12, stackc([c * f12, c * d, c * f1, c * f2]), stackc([d, e12, e2, e1]))
            tot = lr_tr(lr_mul(G, D12)) - lr_tr(lr_mul(lr_mul(lr_mul(G, D2), Gp), D1))
            D1m, D2m, D12m = (md1, Z, Z), (md2, Z, Z), (d12, Z, Z)
            mon = lr_tr(lr_mul(G, D12m)) - lr_tr(lr_mul(lr_mul(lr_mul(G, D2m), Gp), D1m))
        else:
            tot = np.zeros(B, complex); mon = np.zeros(B, complex)
            for b in range(B):
                G = np.linalg.inv(np.diag(C0.om[b]) + c * np.outer(d[b], d[b]))
                Gp = np.linalg.inv(np.diag(C1.om[b]) + c * np.outer(dp[b], dp[b]))
                D1 = np.diag(md1[b]) + c * (np.outer(dp[b], e1[b]) + np.outer(f1p[b], d[b]))
                D2 = np.diag(md2[b]) + c * (np.outer(d[b], e2p[b]) + np.outer(f2[b], dp[b]))
                D12 = np.diag(d12[b]) + c * (np.outer(f12[b], d[b]) + np.outer(d[b], e12[b])
                                             + np.outer(f1[b], e2[b]) + np.outer(f2[b], e1[b]))
                tot[b] = np.trace(G @ D12) - np.trace(G @ D2 @ Gp @ D1)
                mon[b] = np.trace(G @ np.diag(d12[b])) - np.trace(G @ np.diag(md2[b]) @ Gp @ np.diag(md1[b]))
        out[kap] = (tot, mon)
    return out


def T_value(Plist, k1, mu, nu, ell, kappas, dense=False, batch=8):
    acc = {kap: [0j, 0j] for kap in kappas}
    for i in range(0, len(Plist), batch):
        r = class_integrand(Plist[i:i + batch], k1, mu, nu, ell, kappas, dense)
        for kap in kappas:
            acc[kap][0] += r[kap][0].sum(); acc[kap][1] += r[kap][1].sum()
    n = len(Plist)
    return {kap: (acc[kap][0] / n * ell ** -4, acc[kap][1] / n * ell ** -4) for kap in kappas}


def midpoint_grid(ell, nP):
    a = (np.arange(nP) + 0.5) * (2 * np.pi / ell) / nP - np.pi / ell
    return np.array(list(itertools.product(a, a, a, a)))


def cgamma(ell, kc_list, nP, h=1e-3):
    """c_Gamma = beta/2 for each kappa_c; also the M-only part. beta = -d1 d2 T_12."""
    P = midpoint_grid(ell, nP)
    kappas = [kc * ell ** 2 for kc in kc_list]
    vals = {}
    for s1, s2 in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        vals[(s1, s2)] = T_value(P, [s1 * h, s2 * h, 0, 0], 0, 1, ell, kappas)
    res = {}
    for kc, kap in zip(kc_list, kappas):
        tot = (vals[(1, 1)][kap][0] - vals[(1, -1)][kap][0] - vals[(-1, 1)][kap][0] + vals[(-1, -1)][kap][0]) / (4 * h * h)
        mon = (vals[(1, 1)][kap][1] - vals[(1, -1)][kap][1] - vals[(-1, 1)][kap][1] + vals[(-1, -1)][kap][1]) / (4 * h * h)
        imag = max(abs(tot.imag), abs(mon.imag))
        res[kc] = (-tot.real / 2, -mon.real / 2, imag)
    return res


# ---------------------------------------------------------------- dense torus (validation)
def dense_gamma(nf, ell, A, kappa, kernel_A=True):
    """log det(M_A + K_{A or 0}) on the torus Z_nf^4, A complex array (4, nf^4)."""
    N = nf ** 4
    idx = lambda x: np.ravel_multi_index(tuple(np.mod(x, nf)), (nf,) * 4)
    M = np.zeros((N, N), complex)
    sites = list(itertools.product(range(nf), repeat=4))
    for x in sites:
        ix = idx(np.array(x))
        for m in range(4):
            y = np.array(x); y[m] += 1; iy = idx(y)
            a = A[m, ix]
            M[iy, iy] += 1; M[ix, ix] += 1; M[iy, ix] -= np.exp(1j * a); M[ix, iy] -= np.exp(-1j * a)
    Ak = A if kernel_A else np.zeros_like(A)
    h = (ell - 1) // 2
    centres = [c for c in sites if all((ci % ell) == h for ci in c)]
    nc = len(centres)
    Q = np.zeros((nc, N), complex); Qd = np.zeros((N, nc), complex)
    for ci, c in enumerate(centres):
        c = np.array(c)
        for w in itertools.product(range(-h, h + 1), repeat=4):
            x = c + np.array(w); ix = idx(x)
            for sg in PERMS:
                y = x.copy(); Lsum = 0j
                for b in sg:
                    while y[b] != c[b]:
                        if y[b] > c[b]:
                            y2 = y.copy(); y2[b] -= 1; Lsum -= Ak[b, idx(y2)]; y = y2
                        else:
                            Lsum += Ak[b, idx(y)]; y = y.copy(); y[b] += 1
                Q[ci, ix] += np.exp(1j * Lsum) / (24 * ell ** 4)
                Qd[ix, ci] += np.exp(-1j * Lsum) / (24 * ell ** 4)
    Mt = M + kappa * Qd @ Q
    sgn, la = np.linalg.slogdet(Mt)
    return la + np.log(sgn)


def main():
    print("f5: covariant soft block kernel, scalar U(1) background; criteria checks/f5_criteria.md", flush=True)
    # ---------------- (A) dense torus validation
    nf, ell, kc = 6, 3, 1.0
    kappa = kc * ell ** 2
    kv = 2 * np.pi / nf * np.array([1., 1., 0., 0.])
    sites = np.array(list(itertools.product(range(nf), repeat=4)))
    ph = np.exp(1j * sites @ kv)
    a1 = np.zeros((4, nf ** 4), complex); a1[0] = ph
    a2 = np.zeros((4, nf ** 4), complex); a2[1] = np.conj(ph)
    hs = 1e-4
    def fd(kernel_A):
        v = {}
        for s1, s2 in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            v[(s1, s2)] = dense_gamma(nf, ell, s1 * hs * a1 + s2 * hs * a2, kappa, kernel_A)
        return (v[(1, 1)] - v[(1, -1)] - v[(-1, 1)] + v[(-1, -1)]) / (4 * hs * hs) / nf ** 4
    Td = fd(True); Tdm = fd(False)
    Ptor = np.array(list(itertools.product(2 * np.pi / nf * np.arange(nf // ell), repeat=4)))
    rT = T_value(Ptor, kv, 0, 1, ell, [kappa], dense=True)[kappa]
    relA = abs(rT[0] - Td) / abs(Td); relAm = abs(rT[1] - Tdm) / abs(Tdm)
    report("A", relA <= 1e-6 and relAm <= 1e-6,
           f"T12 class {rT[0]:.10e} vs dense FD {Td:.10e} (rel {relA:.1e}); M-only {rT[1]:.10e} vs {Tdm:.10e} (rel {relAm:.1e})")
    # POST-HOC, labelled (not a pre-registered criterion): a development smoke test showed that step 1e-4 is
    # roundoff-limited for a 1296-dimensional log det; the same comparison with step 1e-3.
    hs = 1e-3
    Td3 = fd(True); Tdm3 = fd(False)
    rel3 = abs(rT[0] - Td3) / abs(Td3); rel3m = abs(rT[1] - Tdm3) / abs(Tdm3)
    print(f"   [A' POST-HOC] step 1e-3: total rel {rel3:.1e}, M-only rel {rel3m:.1e} "
          f"({'within' if max(rel3, rel3m) <= 1e-6 else 'outside'} 1e-6)", flush=True)
    print(f"   (t={time.time()-T0:.0f}s)", flush=True)
    # implementation cross-check (informational): low-rank vs dense per-class on a midpoint grid
    Pm = midpoint_grid(3, 2)
    r_lr = T_value(Pm, [0.01, 0.02, 0, 0], 0, 1, 3, [9.0])[9.0]
    r_dn = T_value(Pm, [0.01, 0.02, 0, 0], 0, 1, 3, [9.0], dense=True)[9.0]
    print(f"   [info] low-rank vs dense per-class: {abs(r_lr[0]-r_dn[0]):.1e}, {abs(r_lr[1]-r_dn[1]):.1e}", flush=True)
    # ---------------- (A2) dense gauge invariance
    rng = np.random.default_rng(5)
    Ar = 0.3 * rng.standard_normal((4, nf ** 4)); lam = 0.3 * rng.standard_normal(nf ** 4)
    Ag = Ar.copy()
    for m in range(4):
        sh = sites.copy(); sh[:, m] = (sh[:, m] + 1) % nf
        Ag[m] += lam[np.ravel_multi_index(tuple(sh.T), (nf,) * 4)] - lam
    g1 = dense_gamma(nf, ell, Ar.astype(complex), kappa); g2 = dense_gamma(nf, ell, Ag.astype(complex), kappa)
    report("A2", abs(g1 - g2) <= 1e-9, f"|Gamma(A+d lambda) - Gamma(A)| = {abs(g1-g2):.1e} (Gamma = {g1.real:.6f})")
    print(f"   (t={time.time()-T0:.0f}s)", flush=True)
    # ---------------- (B) Ward identity on the torus momenta
    okB = True; msgB = []
    for kvB in [2 * np.pi / nf * np.array([1., 1., 0., 0.]), 2 * np.pi / nf * np.array([1., 2., 1., 0.])]:
        Ts = [T_value(Ptor, kvB, nu1, 1, ell, [kappa], dense=True)[kappa] for nu1 in range(4)]
        w = sum((np.exp(1j * kvB[n]) - 1) * Ts[n][0] for n in range(4)); sc = sum(abs(Ts[n][0]) for n in range(4))
        wm = sum((np.exp(1j * kvB[n]) - 1) * Ts[n][1] for n in range(4)); scm = sum(abs(Ts[n][1]) for n in range(4))
        okB &= abs(w) <= 1e-10 * sc
        msgB.append(f"k={np.round(kvB/(2*np.pi/nf)).astype(int).tolist()}: |Ward| {abs(w):.1e} (scale {sc:.2e}); M-only {abs(wm):.1e} (scale {scm:.2e})")
    report("B", okB, "; ".join(msgB))
    print(f"   (t={time.time()-T0:.0f}s)", flush=True)
    # ---------------- (C) quadrature, (D) k-step
    c6 = cgamma(5, [1.0], 6)[1.0]; c10 = cgamma(5, [1.0], 10)[1.0]
    report("C", abs(c6[0] - c10[0]) <= 1e-5 * abs(c10[0]), f"c_Gamma(5,1): nP=6 {c6[0]:.9f}, nP=10 {c10[0]:.9f}, diff {abs(c6[0]-c10[0]):.1e}")
    c8a = cgamma(5, [1.0], 8, h=1e-3)[1.0]; c8b = cgamma(5, [1.0], 8, h=2e-3)[1.0]
    report("D", abs(c8a[0] - c8b[0]) <= 1e-6 * abs(c8a[0]), f"h=1e-3 {c8a[0]:.10f}, h=2e-3 {c8b[0]:.10f}, diff {abs(c8a[0]-c8b[0]):.1e}; max imag {max(c8a[2],c8b[2]):.1e}")
    print(f"   (t={time.time()-T0:.0f}s)", flush=True)
    # ---------------- (E), (F), (G) scan
    kcs = [0.25, 1.0, 4.0]
    ells = [3, 5, 7, 9, 11, 13]
    tab = {}
    for el in ells:
        tab[el] = cgamma(el, kcs, 8)
        print(f"   l={el}: " + ", ".join(f"kc={kc}: c={tab[el][kc][0]:.7f} cM={tab[el][kc][1]:.7f} cK={tab[el][kc][0]-tab[el][kc][1]:.7f}" for kc in kcs)
              + f"  [t={time.time()-T0:.0f}s]", flush=True)
    t = 48 * np.pi ** 2
    slope = lambda f, a, b: (f(b) - f(a)) / np.log(b / a)
    okE = True; okG = True; last = {}
    for kc in kcs:
        cT = lambda el: tab[el][kc][0]; cM = lambda el: tab[el][kc][1]; cK = lambda el: tab[el][kc][0] - tab[el][kc][1]
        sT = [slope(cT, a, b) * t for a, b in zip(ells[:-1], ells[1:])]
        sM = [slope(cM, a, b) * t for a, b in zip(ells[:-1], ells[1:])]
        sK = [slope(cK, a, b) * t for a, b in zip(ells[:-1], ells[1:])]
        print(f"   kc={kc}: slope x 48pi^2 total {', '.join(f'{x:.4f}' for x in sT)}; M-only {', '.join(f'{x:.4f}' for x in sM)}; kernel-vertex {', '.join(f'{x:.4f}' for x in sK)}", flush=True)
        okE &= abs(sT[-1] - 1) <= 0.03
        okG &= abs(sK[-1]) <= 0.05 and abs(sK[-1]) <= abs(sK[2])
        last[kc] = sT[-1]
    report("E", okE, "slope at (11,13) x 48pi^2: " + ", ".join(f"kc={kc}: {last[kc]:.4f}" for kc in kcs))
    spread = max(last.values()) - min(last.values())
    report("F", spread <= 0.03, f"kappa spread at (11,13) = {spread:.4f} x 1/(48pi^2)")
    report("G", okG, "kernel-vertex slopes at (11,13) and (7,9) printed above")
    print("   [info] constants c(13) - log(13)/(48pi^2): " + ", ".join(f"kc={kc}: {tab[13][kc][0]-np.log(13)/t:.6f}" for kc in kcs))
    print(f"f5 done: PASS={NPASS} FAIL={NFAIL}; wall {time.time()-T0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
