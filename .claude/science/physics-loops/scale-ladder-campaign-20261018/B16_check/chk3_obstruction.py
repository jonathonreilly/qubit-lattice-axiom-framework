"""B16 check, item 3: the uniform-shift obstruction identity and its order in a.

C3a  EXACT (Fractions, L=3 and 4, generic g^2, cB): {G_A[e0], H_EM(1)} equals
       (g^2/2) sum_l (E_l - E_(l-e0))^2 - (cB/(2g^2)) sum_p (F_p - F_(p-e0))^2 + g^2 sum_w E_(w-e0,0) Gauss_w
     (G_A = B16's forward generator; computed from my own bracket code, compared as quadratic forms).
C3b  the identity is coupling independent at order (matter^2, h^0): the only coupling contribution there is
     {G_g[xi], N h.T} = -N (delta_xi h).T, and delta_xi h = 0 at uniform xi (checked: my G_g[e0] = 0).
C3c  float scaling on smooth fields (transverse E, so the Gauss term is 0), box units a = 1/L:
       D(L)  = {G'[e0], H(1)}                          (pure lattice defect; continuum value 0)
       B(L)  = {G'[e0], H(N)}  with smooth N            (continuum value H(d_0 N) != 0)
       R(L)  = B(L) - H(N'),  N' = best of {backward, forward, central} difference of N (no fitting)
     for FWD and STAG Maxwell and for the B14 scalar (central G_m, mean bond timing).  Exponents fitted on
     L = 8..32.  The B16 claim to test: Maxwell defect is O(a) relative to B, scalar O(a^2).
"""
from fractions import Fraction as Fr
import sys

import numpy as np
import scipy.sparse as spm

from chk_lat import Lat, uniform_timing
from chk1_timing import staggered
from chk1b_induced_generator import induced_generator, fwd_GA

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def qadd(Q, i, j, v):
    key = (min(i, j), max(i, j))
    Q[key] = Q.get(key, 0) + v
    if Q[key] == 0:
        del Q[key]


def c3a(L):
    lat = Lat(L)
    g2, cb = Fr(9, 4), Fr(35, 132)
    X = fwd_GA(lat)
    xi = {b: Fr(1) if b[1] == 0 else Fr(0) for b in X}
    G = {}
    for b, d in X.items():
        if xi[b]:
            for ka, v in d.items():
                G[ka] = G.get(ka, 0) + xi[b] * v
    # {G,H} = sum_a dG/dA_a dH/dE_a - sum_k dG/dE_k dH/dA_k ; G = sum G[k,a] E_k A_a
    QE, QA = {}, {}  # E-E and A-A quadratic forms (keys sorted pairs, value = coefficient of monomial)
    for (k, a), v in G.items():
        qadd(QE, k, a, g2 * v)  # dG/dA_a = G[k,a] E_k ; dH/dE_a = g2 E_a
    # dH/dA_k = (cb/g2) sum_p sigma_pk F_p ;  dG/dE_k = sum_a G[k,a] A_a
    for (k, a), v in G.items():
        for (p, s) in lat.inc[k]:
            for a2, f in lat.Fp[p].items():
                qadd(QA, a, a2, -(cb / g2) * v * s * f)
    # claimed identity
    CE, CA = {}, {}
    for k, (x, j) in enumerate(lat.links):
        km = lat.lidx[(lat.sh(x, 0, -1), j)]
        for (i1, s1) in ((k, 1), (km, -1)):
            for (i2, s2) in ((k, 1), (km, -1)):
                if i1 <= i2:
                    qadd(CE, i1, i2, (g2 / 2) * s1 * s2 * (1 if i1 == i2 else 2))
    for p, (y, ij) in enumerate(lat.plaqs):
        pm = lat.pidx[(lat.sh(y, 0, -1), ij)]
        diff = dict(lat.Fp[p])
        for a, f in lat.Fp[pm].items():
            diff[a] = diff.get(a, 0) - f
        items = [(a, f) for a, f in diff.items() if f]
        for x1, (a1, f1) in enumerate(items):
            for x2, (a2, f2) in enumerate(items):
                if x1 <= x2:
                    qadd(CA, a1, a2, -(cb / (2 * g2)) * f1 * f2 * (1 if a1 == a2 else 2))
    for w in lat.sites:
        kq = lat.lidx[(lat.sh(w, 0, -1), 0)]
        for j in range(3):
            qadd(CE, kq, lat.lidx[(w, j)], g2)
            qadd(CE, kq, lat.lidx[(lat.sh(w, j, -1), j)], -g2)
    okE = QE == CE
    okA = QA == CA
    check(f"C3a(L={L})", okE and okA, f"exact identity {{G_A[e0],H_EM(1)}} = (g^2/2)sum(dE)^2 - (cB/2g^2)sum(dF)^2 + g^2 sum E_(w-e0,0) Gauss_w (EE part {okE}, AA part {okA}; #EE monomials {len(QE)}, #AA {len(QA)})")


def c3b():
    from chk2_cone import Grav
    lat = Lat(3)
    gr = Grav(lat)
    xi = {(x, j): (1.0 if j == 0 else 0.0) for x in lat.sites for j in range(3)}
    check("C3b", np.abs(gr.gg(xi)).max() == 0,
          "my G_g[e0 uniform] = 0 identically, so at order (matter^2, h^0) no h- or P-coupling enters {G[e0], C(N)}: the uniform-shift identity is coupling independent")


# ------------------------------------------------------------------ smooth-field scaling
def sparse_gen(lat, X, xi):
    rows, cols, vals = [], [], []
    for b, d in X.items():
        if xi.get(b, 0) == 0:
            continue
        for (k, a), v in d.items():
            rows.append(k); cols.append(a); vals.append(float(xi[b] * v))
    nL = len(lat.links)
    return spm.csr_matrix((vals, (rows, cols)), shape=(nL, nL))


def fmat(lat):
    r, c, v = [], [], []
    for p, d in enumerate(lat.Fp):
        for a, s in d.items():
            r.append(p); c.append(a); v.append(s)
    return spm.csr_matrix((v, (r, c)), shape=(len(lat.plaqs), len(lat.links)))


def smear(lat, u, w, N):
    nl = np.array([sum(float(v) * N[lat.sidx[s]] for s, v in u[k].items()) for k in range(len(lat.links))])
    mp = np.array([sum(float(v) * N[lat.sidx[s]] for s, v in w[p].items()) for p in range(len(lat.plaqs))])
    return nl, mp


def em_fields(lat):
    L = lat.L
    a = 1.0 / L
    tp = 2 * np.pi
    def Ac(j, r):
        x, y, z = r
        return [np.sin(tp * y) + 0.5 * np.cos(tp * z + 0.3), np.cos(tp * (x + 0.2)) * np.sin(tp * z), 0.7 * np.sin(tp * (x - y))][j]
    def Wc(q, r):
        x, y, z = r
        return [np.cos(tp * (x + z)) + 0.4 * np.sin(tp * y), 0.8 * np.sin(tp * (y - 0.1)) * np.cos(tp * x), np.cos(tp * z + 0.7)][q]
    A = np.zeros(len(lat.links))
    for k, (x, j) in enumerate(lat.links):
        r = np.array(x, float); r[j] += 0.5
        A[k] = a * Ac(j, r * a)
    b = np.zeros(len(lat.plaqs))
    for p, (y, (i, j)) in enumerate(lat.plaqs):
        r = np.array(y, float); r[i] += 0.5; r[j] += 0.5
        b[p] = a * Wc(lat.pairs.index((i, j)), r * a)
    Fm = fmat(lat)
    E = Fm.T @ b  # curl^T b : exactly divergence free
    return A, E, Fm


def lapse_smooth(lat):
    a = 1.0 / lat.L
    # generic (all Fourier modes present) so that H(d_0 N) is not suppressed by orthogonality
    tp = 2 * np.pi
    return np.array([np.exp(0.35 * np.sin(tp * x[0] * a + 0.4) + 0.3 * np.cos(tp * (x[0] - x[1]) * a) + 0.25 * np.sin(tp * (x[2] + x[1]) * a + 0.2)) for x in lat.sites])


def dlapse(lat, N, kind):
    out = np.zeros_like(N)
    for x in lat.sites:
        i = lat.sidx[x]
        f, bk = N[lat.sidx[lat.sh(x, 0)]], N[lat.sidx[lat.sh(x, 0, -1)]]
        out[i] = {"backward": N[i] - bk, "forward": f - N[i], "central": (f - bk) / 2}[kind]
    return out


def em_scaling(name, Ls):
    g2, cb = 0.9, 1.7
    out = []
    for L in Ls:
        lat = Lat(L)
        if name == "FWD":
            u, w = uniform_timing(lat, {j: (Fr(1), Fr(0)) for j in range(3)}, {ij: {"00": Fr(1)} for ij in lat.pairs})
            X = fwd_GA(lat)
        else:
            u, w = staggered(lat, 0)
            X = induced_generator(lat, u, w, Fr(1))
        xi = {b: (1 if b[1] == 0 else 0) for b in X}
        G = sparse_gen(lat, X, xi)
        A, E, Fm = em_fields(lat)
        F = Fm @ A

        def bracket_GH(N):
            nl, mp = smear(lat, u, w, N)
            dGdA = G.T @ E
            dGdE = G @ A
            dHdE = g2 * nl * E
            dHdA = (cb / g2) * (Fm.T @ (mp * F))
            return dGdA @ dHdE - dGdE @ dHdA

        def H(N):
            nl, mp = smear(lat, u, w, N)
            return (g2 / 2) * np.sum(nl * E * E) + (cb / (2 * g2)) * np.sum(mp * F * F)
        one = np.ones(len(lat.sites))
        D = bracket_GH(one)
        N = lapse_smooth(lat)
        B = bracket_GH(N)
        R = min(abs(B - H(dlapse(lat, N, k))) for k in ("backward", "forward", "central"))
        out.append((L, D, B, R, H(one)))
    return out


def scalar_scaling(Ls):
    c, mu = 1.3, 0.0
    out = []
    for L in Ls:
        lat = Lat(L)
        a = 1.0 / L
        tp = 2 * np.pi
        X = np.array(lat.sites, float) * a
        phi = np.sin(tp * X[:, 0] + 0.3) * np.cos(tp * X[:, 1]) + 0.5 * np.cos(tp * (X[:, 2] - X[:, 0]))
        pi = a * (np.cos(tp * X[:, 1] - 0.2) + 0.7 * np.sin(tp * (X[:, 0] + X[:, 2])))
        idx = np.arange(len(lat.sites))
        fwd = [np.array([lat.sidx[lat.sh(x, j)] for x in lat.sites]) for j in range(3)]

        def H(N):
            v = np.sum(N * (pi ** 2 / 2 + mu * phi ** 2 / 2))
            for j in range(3):
                v += np.sum((N + N[fwd[j]]) / 2 * c / 2 * (phi[fwd[j]] - phi) ** 2)
            return v

        def bracket_GH(N):
            # G_m[e0] = sum_x (phi_{x+0}-phi_x)(pi_x+pi_{x+0})/2 ; {G,H} = dG/dphi dH/dpi - dG/dpi dH/dphi
            f0 = fwd[0]
            b0 = np.empty_like(f0); b0[f0] = idx
            dGdpi = (phi[f0] - phi[b0]) / 2
            dGdphi = (pi[b0] - pi[f0]) / 2
            dHdpi = N * pi
            dHdphi = N * mu * phi
            for j in range(3):
                fj = fwd[j]
                bj = np.empty_like(fj); bj[fj] = idx
                wf = (N + N[fj]) / 2
                wb = (N[bj] + N) / 2
                dHdphi = dHdphi + c * (wb * (phi - phi[bj]) - wf * (phi[fj] - phi))
            return dGdphi @ dHdpi - dGdpi @ dHdphi
        one = np.ones(len(lat.sites))
        D = bracket_GH(one)
        N = lapse_smooth(lat)
        B = bracket_GH(N)
        R = min(abs(B - H(dlapse(lat, N, k))) for k in ("backward", "forward", "central"))
        out.append((L, D, B, R, H(one)))
    return out


def slope(Ls, vals):
    return np.polyfit(np.log(Ls), np.log(np.abs(vals)), 1)[0]


def c3c():
    Ls = [8, 12, 16, 24, 32]
    res = {"FWD": em_scaling("FWD", Ls), "STAG": em_scaling("STAG", Ls), "scalar": scalar_scaling(Ls)}
    print("  (L, D={G[e0],H(1)}, B={G[e0],H(N)}, R=B-H(N'_best), H(1)); ratios D/B, R/B:")
    sl = {}
    for k, rows in res.items():
        for (L, D, B, R, H1) in rows:
            print(f"    {k:6s} L={L:3d}  D={D: .4e}  B={B: .4e}  R={R: .4e}  H1={H1: .4e}  D/B={D / B: .3e}  R/B={R / B: .3e}  D/H1={D / H1: .3e}")
        Lv = [r[0] for r in rows]
        sl[k] = (slope(Lv, [r[2] for r in rows]), slope(Lv, [max(abs(r[1] / r[2]), 1e-300) for r in rows]),
                 slope(Lv, [max(abs(r[3] / r[2]), 1e-300) for r in rows]))
        print(f"    {k}: log-log slopes vs L: B {sl[k][0]:.2f}, D/B {sl[k][1]:.2f}, R/B {sl[k][2]:.2f}")
    fwd_D = sl["FWD"][1]
    check("C3c-FWD", abs(fwd_D + 1) < 0.15 and abs(sl["FWD"][2] + 1) < 0.15,
          f"forward Maxwell: uniform-shift defect D/B ~ L^{fwd_D:.2f} and full residual R/B ~ L^{sl['FWD'][2]:.2f}: O(a) confirmed on smooth fields")
    sc_D = max(abs(r[1]) for r in res["scalar"])
    check("C3c-scalar", sc_D < 1e-10 and abs(sl["scalar"][2] + 2) < 0.2,
          f"scalar: D = 0 (max |D| {sc_D:.1e}); residual R/B ~ L^{sl['scalar'][2]:.2f}: O(a^2)")
    print(f"  STAG (measured, no prior expectation): D/B slope {sl['STAG'][1]:.2f}, R/B slope {sl['STAG'][2]:.2f}; max |D| = {max(abs(r[1]) for r in res['STAG']):.2e}")
    return res, sl


if __name__ == "__main__":
    c3a(3)
    c3a(4)
    c3b()
    c3c()
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
