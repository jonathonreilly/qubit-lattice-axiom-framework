"""c31: Lemma E-low (symbol + chain level), NA-lev smallness arithmetic, and the analytic F-representative of the
f_0 map (Lemma F-df_0's factorisation identity).

Criteria: checks/c31_criteria.md (written first).
Usage: python3 -I c31_linear.py E | F
"""
import itertools
import math
import os
import resource
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c26_led as C  # noqa: E402

T0 = time.time()
L = 3
d = 4
PLANES = list(itertools.combinations(range(d), 2))


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20


def cE(kap):
    k = len(kap); kk = kap[k - 1]
    kh = max(kk / x for x in kap)
    Rb = 1 + kh / (L * L - 1) + kk / 9
    return 2 * kk / (math.pi ** 2 * (kk + 4 * math.pi ** 2 * Rb))


def per_mode(T, k, kap):
    """e(p) = (kappa/2) lambda_2(A)/psi on the T-grid, with eigenvectors."""
    P = C.P_symbol(d, T, k, kap)
    nu = C.nu_sym(d, T)
    w = np.stack([1.0 / x for x in P], -1)              # (T,)*d + (d,)
    v = np.stack(nu, -1)
    Wv = w * v
    den = np.einsum("...m,...m->...", np.conj(v), Wv).real
    psi = np.einsum("...m,...m->...", np.conj(v), v).real
    zero = (0,) * d
    den[zero] = 1.0; psi[zero] = 1.0
    A = np.einsum("...m,mn->...mn", w, np.eye(d)) - np.einsum("...m,...n->...mn", Wv, np.conj(Wv)) / den[..., None, None]
    A[zero] = np.eye(d)
    lam, vec = np.linalg.eigh(A)
    e = (kap[k - 1] / 2) * lam[..., 1] / psi
    e[zero] = np.inf
    return e, A, vec, P


def part_E():
    print("Part E: Lemma E-low")
    ok = dict(E1=True, V=True, E2a=True, E2b=True, E3=True)
    for (T, k, kap) in ((16, 1, (1.0,)), (16, 2, (1.0, 1.0)), (12, 3, (1.0, 1.0, 1.0)), (16, 2, (0.5, 2.0))):
        e, A, vec, P = per_mode(T, k, kap)
        c = cE(kap)
        i = np.unravel_index(np.argmin(e), e.shape)
        mn = float(e[i])
        ok["E1"] &= mn >= c
        print(f" E1 T={T} k={k} kap={kap}: min e = {mn:.6f}, c_E = {c:.6f}, ratio {mn / c:.2f} at p-index {i}  "
              f"rss {rss():.0f} MB  t {time.time() - T0:.1f}s", flush=True)
        del e, A, vec, P
    rng = np.random.default_rng(20261027)
    for (T, k, kap) in ((3, 1, (1.0,)), (2, 2, (1.0, 1.0)), (2, 2, (0.5, 2.0))):
        c = cE(kap)
        ch = C.Chain(d, T, k, kap); top = ch.levels[k]; Dk = top.dmat()
        e, A, vec, P = per_mode(T, k, kap)
        i = np.unravel_index(np.argmin(e), e.shape)
        p = 2 * np.pi * np.array(i) / T
        selfconj = all(((2 * ii) % T) == 0 for ii in i)
        if selfconj:
            lam, vv = np.linalg.eigh(A[i].real)
            b = vv[:, 1].astype(complex)
        else:
            b = vec[i][:, 1]
        X = top.coords()
        phase = np.exp(1j * (X @ p))
        Bmode = np.concatenate([np.real(b[m] * phase) for m in range(d)])
        data = [("rand%d" % j, rng.normal(size=top.NL)) for j in range(3)] + [("mode", Bmode)]
        for (name, Bk) in data:
            sol = ch.solve(Bk)
            F = Dk @ Bk
            ratio = sol["E"] / float(F @ F)
            ok["V"] &= sol["ne"] <= 1e-8
            ok["E2a"] &= ratio >= c
            line = f" E2 T={T} k={k} kap={kap} {name}: E_k/||dB_k||^2 = {ratio:.8f} (c_E {c:.6f}, x{ratio / c:.1f}), ne {sol['ne']:.1e}"
            if name == "mode":
                rel = abs(ratio - float(e[i])) / float(e[i])
                ok["E2b"] &= rel <= 1e-6
                line += f"; symbol e(p_min) = {float(e[i]):.8f}, rel {rel:.1e}, p_index {i}, self-conj {selfconj}"
            print(line + f"  rss {rss():.0f} MB  t {time.time() - T0:.1f}s", flush=True)
        del ch, e, A, vec, P
    c1 = cE((1.0,))
    pL = 5 * L - 4; c_1 = 1 / 3.5e6; kk = 1.0
    rhs = 0.5 * min(c1, kk / 4) * c_1
    lhs_coef = (kk / 2) * L * L * 81 * pL
    eta = 0.5 * math.log1p(math.sqrt(rhs / lhs_coef))
    ang = eta / (2 * L * (L - 1))
    ok["E3"] = abs(c1 - 0.004069) <= 5e-7 and 1.85e-7 <= eta <= 1.95e-7 and 1.5e-8 <= ang <= 1.65e-8
    print(f" E3: c_E(kappa=1, L=3) = {c1:.7f}; NA-lev eta_bar_max = {eta:.4e}; plaquette angle {ang:.4e}")
    print(" " + " ".join(f"{kk2}:{'PASS' if v else 'FAIL'}" for kk2, v in ok.items()))
    print(f"Part E: {'PASS' if all(ok.values()) else 'FAIL'}  t {time.time() - T0:.1f}s  rss {rss():.0f} MB")


def part_F():
    print("Part F: analytic F-representative of the f_0 map")
    ok = dict(F0=True, F1=True)
    for (T, k, u) in ((8, 1, (0, 0, 0, 0)), (8, 1, (1, 0, 0, 0)), (8, 2, (0, 0, 0, 0)), (8, 2, (2, 1, 0, 0))):
        kap = (1.0,) * k; n = L ** k
        P = C.P_symbol(d, T, k, kap); nu = C.nu_sym(d, T)
        Phi = {(a, b): C.Phi_f(d, T, n, a, b, u) for a in range(d) for b in range(d) if a != b}
        B = np.zeros((d, len(PLANES)) + (T,) * d, dtype=complex)   # B[v, plane](p)
        for v in range(d):
            bh = [np.full((T,) * d, 1.0 + 0j) if s == v else np.zeros((T,) * d, complex) for s in range(d)]
            r = C.r_from_b(P, bh, nu)
            for j, (a, b) in enumerate(PLANES):
                B[v, j] = n ** (5.0 - d) * (-kap[k - 1]) * (Phi[(a, b)] * r[b] - Phi[(b, a)] * r[a])
        Bmax = np.abs(B).max()
        g0 = sum(nu[v] * B[v] for v in range(d))
        g0[(slice(None),) + (0,) * d] = 0.0
        e0 = np.abs(g0).max() / Bmax
        ok["F0"] &= e0 <= 1e-12

        def E_lt(g, a):
            """evaluate at p_1..p_{a-1} = 0 (array axes a' < a of the momentum part), keep shape by broadcasting."""
            idx = [slice(None)] * g.ndim
            off = g.ndim - d
            for aa in range(a):
                idx[off + aa] = slice(0, 1)
            return g[tuple(idx)]

        def T_op(g, a):
            idx = [slice(None)] * g.ndim
            off = g.ndim - d
            idx[off + a] = slice(0, 1)
            with np.errstate(divide="ignore", invalid="ignore"):
                return (g - g[tuple(idx)]) / nu[a]

        h = {}
        for (a, b) in PLANES:
            h[(a, b)] = T_op(E_lt(B[b], a), a)          # 6-vector of output planes, shape (6,)+(T,)*d
        mask = np.ones((T,) * d, dtype=bool)
        for a in range(d):
            sl = [slice(None)] * d; sl[a] = 0; mask[tuple(sl)] = False
        e1 = 0.0
        for v in range(d):
            lhs = np.zeros((len(PLANES),) + (T,) * d, dtype=complex)
            for (a, b) in PLANES:
                coef = (nu[a] if b == v else 0.0) - (nu[b] if a == v else 0.0)
                if np.isscalar(coef) and coef == 0.0:
                    continue
                lhs = lhs + h[(a, b)] * coef
            e1 = max(e1, float(np.abs((lhs - B[v])[:, mask]).max()) / Bmax)
        ok["F1"] &= e1 <= 1e-10
        hmax = max(float(np.abs(h[kk][:, mask]).max()) for kk in h) / Bmax
        print(f" T={T} k={k} u={u}: max|B| {Bmax:.3e}; F0 gauge err {e0:.1e}; F1 factorisation err {e1:.1e}; "
              f"F2 max|h|/max|B| {hmax:.2f}; tested points {int(mask.sum())}  rss {rss():.0f} MB  t {time.time() - T0:.1f}s",
              flush=True)
        del P, Phi, B, h
    print(" " + " ".join(f"{kk}:{'PASS' if v else 'FAIL'}" for kk, v in ok.items()))
    print(f"Part F: {'PASS' if all(ok.values()) else 'FAIL'}  t {time.time() - T0:.1f}s  rss {rss():.0f} MB")


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "E"
    {"E": part_E, "F": part_F}[part]()
