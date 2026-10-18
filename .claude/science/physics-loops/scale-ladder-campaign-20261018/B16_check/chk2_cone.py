"""B16 check, item 2: photon cone and generator normalisation (own code, float64 with tolerances).

Gravity sector re-implemented from the B14 conventions (09-24 clauses), not imported:
  kin(N) = sum_x N_x/(4a) [sum_j Pd_j^2 - (1/2)(sum_j Pd_j)^2] + sum_f Nbar4_f/(8a) Pf^2
  R1(N)  = sum_x sum_j (-sum_i lap_i N + lap_j N)_x hd_j(x) + sum_f 2 mixed(N)_f hf
  G_g[xi]= sum_x,j 2(xi_(x,j) - xi_(x-j,j)) Pd_j(x) + sum_f (D_i xi_j + D_j xi_i) Pf,   C_g = kin + s K R1.
C2e  {C_g(N),C_g(M)} = G_g[sigma xi~] with sigma fitted; expect sigma = s K/(4 alpha).
C2f  total (gravity + Maxwell, FWD and STAG timings): closes into one G_g[xi] + G'[xi] iff cB = -sigma.
C2g  rescaled generator 2G' moves the closing value to 2 kappa (normalisation dependence, as B16 T3c).
C2h  normalisation is NOT a lattice choice: G' is computed from the bracket; on smooth fields with smooth,
     NON-uniform xi, delta_xi F = {F, G'[xi]} -> (L_xi F) with unit coefficient (relative error -> 0 as L grows),
     for both FWD and STAG.  L_xi F_ij = xi^k d_k F_ij + F_kj d_i xi^k + F_ik d_j xi^k.
"""
from fractions import Fraction as Fr
import random

import numpy as np

from chk_lat import Lat, uniform_timing
from chk1_timing import staggered
from chk1b_induced_generator import induced_generator

RES = {"pass": 0, "fail": 0}
ALPHA, KK = 3 / 7, 5 / 11
KAPPA = KK / (4 * ALPHA)


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


class Grav:
    def __init__(self, lat):
        self.lat = lat
        S = len(lat.sites)
        self.nPd, self.nPf = 3 * S, 3 * S  # Pd index (x,j) ; Pf index (y, pair)

    def pd(self, x, j):
        return 3 * self.lat.sidx[x] + j

    def pf(self, y, q):
        return self.nPd + 3 * self.lat.sidx[y] + q

    def kin_grad(self, N):
        """d kin(N) / dP as a linear map P -> vector (matrix)."""
        lat = self.lat
        n = self.nPd + self.nPf
        Km = np.zeros((n, n))
        for x in lat.sites:
            idx = [self.pd(x, j) for j in range(3)]
            blk = np.eye(3) - 0.5 * np.ones((3, 3))
            Km[np.ix_(idx, idx)] += 2 * N[lat.sidx[x]] / (4 * ALPHA) * blk
        for y in lat.sites:
            for q, (i, j) in enumerate(lat.pairs):
                cs = [y, lat.sh(y, i), lat.sh(y, j), lat.sh(lat.sh(y, i), j)]
                nb = sum(N[lat.sidx[z]] for z in cs) / 4
                Km[self.pf(y, q), self.pf(y, q)] += 2 * nb / (8 * ALPHA)
        return Km

    def r1_coef(self, N):
        lat = self.lat
        r = np.zeros(self.nPd + self.nPf)
        n = lambda z: N[lat.sidx[z]]
        for x in lat.sites:
            lap = [n(lat.sh(x, i)) - 2 * n(x) + n(lat.sh(x, i, -1)) for i in range(3)]
            for j in range(3):
                r[self.pd(x, j)] = -sum(lap) + lap[j]
        for y in lat.sites:
            for q, (i, j) in enumerate(lat.pairs):
                r[self.pf(y, q)] = 2 * (n(y) - n(lat.sh(y, i)) - n(lat.sh(y, j)) + n(lat.sh(lat.sh(y, i), j)))
        return r

    def gg(self, xi):
        lat = self.lat
        v = np.zeros(self.nPd + self.nPf)
        for x in lat.sites:
            for j in range(3):
                v[self.pd(x, j)] = 2 * (xi[(x, j)] - xi[(lat.sh(x, j, -1), j)])
        for y in lat.sites:
            for q, (i, j) in enumerate(lat.pairs):
                v[self.pf(y, q)] = xi[(lat.sh(y, i), j)] - xi[(y, j)] + xi[(lat.sh(y, j), i)] - xi[(y, i)]
        return v

    def bracket_CC(self, N, M, s):
        """{C_g(N),C_g(M)} as coefficient vector of P (linear).  {kin(N), sK R1(M)} = - dkin(N)/dP . sK r(M); P-linear."""
        # kin(N) = 1/2 P^T Km(N) P ; d kin/dP = Km P ; {kin(N), R1(M)} = -(Km(N) P).r(M) -> coefficient -Km(N) r(M)
        return s * KK * (-self.kin_grad(N) @ self.r1_coef(M) + self.kin_grad(M) @ self.r1_coef(N))


def xi_tilde(lat, N, M):
    return {(x, j): N[lat.sidx[lat.sh(x, j)]] * M[lat.sidx[x]] - N[lat.sidx[x]] * M[lat.sidx[lat.sh(x, j)]] for x in lat.sites for j in range(3)}


def gp_vec(lat, X, xi):
    nL = len(lat.links)
    G = np.zeros((nL, nL))
    for b, d in X.items():
        if xi[b] == 0:
            continue
        for (k, a), v in d.items():
            G[k, a] += xi[b] * float(v)
    return G.ravel()


def em_bracket_vec(lat, u, w, N, M, c):
    from chk_lat import em_pair_coeffs
    co = em_pair_coeffs(lat, u, w, Fr(1))
    nL = len(lat.links)
    G = np.zeros((nL, nL))
    for (s, t), d in co.items():
        f = N[lat.sidx[s]] * M[lat.sidx[t]]
        if f == 0:
            continue
        for (k, a), v in d.items():
            G[k, a] += c * f * float(v)
    return G.ravel()


def span_residual(cols, target):
    A = np.array(cols).T
    sol, *_ = np.linalg.lstsq(A, target, rcond=None)
    return np.linalg.norm(A @ sol - target) / max(np.linalg.norm(target), 1e-300)


def main():
    lat = Lat(3)
    gr = Grav(lat)
    rng = np.random.default_rng(5)
    N = rng.integers(-3, 4, len(lat.sites)).astype(float)
    M = rng.integers(-3, 4, len(lat.sites)).astype(float)
    xt = xi_tilde(lat, N, M)
    sig = {}
    for s in (-1, 1):
        br = gr.bracket_CC(N, M, s)
        g = gr.gg(xt)
        sg = float(br @ g / (g @ g))
        sig[s] = (sg, np.linalg.norm(br - sg * g) / np.linalg.norm(br))
    check("C2e", all(abs(sig[s][0] - s * KAPPA) < 1e-12 and sig[s][1] < 1e-12 for s in sig),
          f"gravity alone: {{C_g(N),C_g(M)}} = G_g[sigma xi~] exactly with sigma = s K/(4 alpha): {{s: (sigma, sigma/kappa, rel.resid)}} = "
          + str({s: (round(v[0], 12), round(v[0] / KAPPA, 12), f"{v[1]:.1e}") for s, v in sig.items()}))
    timings = {"FWD": uniform_timing(lat, {j: (Fr(1), Fr(0)) for j in range(3)}, {ij: {"00": Fr(1)} for ij in lat.pairs}),
               "STAG": None}
    lat4 = Lat(4)  # staggering needs even L
    timings_l = {"FWD": (lat, timings["FWD"]), "STAG": (lat4, staggered(lat4, 0))}
    allok = True
    rows = []
    for name, (lt, (u, w)) in timings_l.items():
        g_ = Grav(lt)
        X = induced_generator(lt, u, w, Fr(1))
        bonds = [(x, j) for x in lt.sites for j in range(3)]
        cols = []
        cols2 = []
        for b in bonds:
            e = {bb: (1.0 if bb == b else 0.0) for bb in bonds}
            cols.append(np.concatenate([g_.gg(e), gp_vec(lt, X, e)]))
            cols2.append(np.concatenate([g_.gg(e), 2 * gp_vec(lt, X, e)]))
        Nn = rng.integers(-3, 4, len(lt.sites)).astype(float)
        Mn = rng.integers(-3, 4, len(lt.sites)).astype(float)
        for s in (-1, 1):
            for cb_over in (1.0, -1.0, 2.0, 0.5):
                cb = cb_over * KAPPA
                tgt = np.concatenate([g_.bracket_CC(Nn, Mn, s), em_bracket_vec(lt, u, w, Nn, Mn, cb)])
                r1 = span_residual(cols, tgt)
                r2 = span_residual(cols2, tgt)
                closes = r1 < 1e-9
                expect = abs(cb_over + s) < 1e-12  # cB = -s kappa
                allok &= closes == expect
                rows.append((name, s, cb_over, closes, r2 < 1e-9))
    print("  (timing, s, cB/kappa, closes with G', closes with 2G'):")
    for r in rows:
        print("   ", r)
    check("C2f", allok, "gravity + Maxwell closes into ONE total relabelling G_g[xi] + G'[xi] iff cB = -s K/(4 alpha), for the FWD timing (L=3) and the STAG timing (L=4)")
    ok2 = all((r[4] == (abs(r[2] + 2 * r[1]) < 1e-12)) for r in rows)
    check("C2g", ok2, "with 2G' the closing value moves to cB = -2 s kappa (the cone is tied to the generator's normalisation)")
    # ---- C2h smooth-field normalisation
    print("  C2h: delta_xi F vs L_xi F on smooth fields (relative L2 error):")
    errs = {}
    for name in ("FWD", "STAG"):
        errs[name] = []
        for L in (8, 12, 16, 20):
            lt = Lat(L)
            u, w = uniform_timing(lt, {j: (Fr(1), Fr(0)) for j in range(3)}, {ij: {"00": Fr(1)} for ij in lt.pairs}) if name == "FWD" else staggered(lt, 0)
            X = induced_generator(lt, u, w, Fr(1))
            errs[name].append((L, lie_test(lt, X)))
        print(f"    {name}: " + ", ".join(f"L={L}: {e:.4e}" for L, e in errs[name]))
    ok = True
    for name in errs:
        e = [v for _, v in errs[name]]
        ok &= e[-1] < e[0] and e[-1] < 0.1
        slope = np.polyfit(np.log([L for L, _ in errs[name]]), np.log(e), 1)[0]
        print(f"    {name}: fitted log-log slope {slope:.2f}")
    check("C2h", ok, "induced generator acts on F as the Lie derivative L_xi F with UNIT coefficient in the continuum limit (smooth non-uniform xi), both timings: the normalisation is computed, not chosen")


def smooth(L, fn):
    return fn


def lie_test(lat, X):
    """Compare delta F_p = sum_l sigma_pl {A_l, G'[xi]} with a^2 (L_xi F)_ij at the plaquette centre.
    Lattice units: a = 1, box length L; fields are smooth functions of x/L."""
    L = lat.L
    tp = 2 * np.pi / L
    # smooth A_i(x) (continuum), sampled at link midpoints * a (a=1): A_l = int_link A . dl ~ A_j(x + e_j/2)
    def Acont(j, r):
        x, y, z = r
        return [np.sin(tp * y) + 0.5 * np.cos(tp * z + 0.3), np.cos(tp * (x + 0.2)) * np.sin(tp * z), 0.7 * np.sin(tp * (x - y))][j]
    def xic(i, r):
        x, y, z = r
        return [1.0 + 0.5 * np.sin(tp * z), 0.3 * np.cos(tp * x), 0.4 * np.sin(tp * y + 0.1)][i]
    A = np.zeros(len(lat.links))
    for k, (x, j) in enumerate(lat.links):
        r = np.array(x, float)
        r[j] += 0.5
        A[k] = Acont(j, r)
    xi = {}
    for (x, i) in [(x, i) for x in lat.sites for i in range(3)]:
        r = np.array(x, float)
        r[i] += 0.5  # bond midpoint
        xi[(x, i)] = xic(i, r)
    nL = len(lat.links)
    dA = np.zeros(nL)  # {A_k, G'} = dG'/dE_k = sum_b xi_b sum_a X_b[k,a] A_a  (sparse)
    for b, d in X.items():
        for (k, a), v in d.items():
            dA[k] += xi[b] * float(v) * A[a]
    dF = np.array([sum(s * dA[a] for a, s in fp.items()) for fp in lat.Fp])
    # continuum L_xi F at plaquette centre, numerical derivatives of the continuum functions
    h = 1e-4
    def Fc(i, j, r):
        def dA_(jj, kk):
            e = np.zeros(3); e[kk] = h
            return (Acont(jj, r + e) - Acont(jj, r - e)) / (2 * h)
        return dA_(j, i) - dA_(i, j)
    exact = np.zeros(len(lat.plaqs))
    for p, (y, (i, j)) in enumerate(lat.plaqs):
        r = np.array(y, float)
        r[i] += 0.5
        r[j] += 0.5
        def dF_(ii, jj, kk):
            e = np.zeros(3); e[kk] = h
            return (Fc(ii, jj, r + e) - Fc(ii, jj, r - e)) / (2 * h)
        def dxi(m, kk):
            e = np.zeros(3); e[kk] = h
            return (xic(m, r + e) - xic(m, r - e)) / (2 * h)
        val = sum(xic(k, r) * dF_(i, j, k) for k in range(3))
        val += sum(Fc(k, j, r) * dxi(k, i) + Fc(i, k, r) * dxi(k, j) for k in range(3))
        exact[p] = val
    return np.linalg.norm(dF - exact) / np.linalg.norm(exact)


if __name__ == "__main__":
    main()
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
