"""c28: N2-exp (analytic symbols, strip bounds, decay rates) and IT' (composite slice functional).

Criteria: checks/c28_criteria.md (written first, with a pre-script addendum).
Usage: python3 -I c28_exp.py A | B | C | D
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
RNG = np.random.default_rng(20261027)


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20


# ------------------------------------------------------------- bound chain (Lemma EXP-strip, verbatim arithmetic)
def consts(eta, r0, kap, kh, L=3):
    ch = math.cosh(eta); eps = math.exp(eta) - 1
    Rb = 1 + kh / (L * L - 1) + kap / 9
    bstar = min(kap, 24 / math.pi ** 2)
    Gam = max(math.pi ** 2 / 4, Rb)
    epsp = (math.pi ** 2 / 4) * eps
    e5 = (1 + epsp) ** 5 - 1
    lam = 1 - 4 * eta ** 2 * ch ** 2 / 9
    eZ = (4 * eta ** 2 / 9 + 4 * eta / 3) * ch
    epsS = eps * (1 + math.exp(eta))
    dN = eps * math.exp(4 * eta) + 4 * math.exp(3 * eta) * epsS
    cZ = dN / (9 * lam) + eZ / (9 * lam)
    eR = kh / (L * L - 1) * eps + kap * cZ
    rho = e5 + (4 * eta ** 2 / bstar + 4 * eta / math.sqrt(bstar)) * ch * (Rb + eR) + eR
    PsiU = kap * (1 - r0 ** 2 / 6) / (kap + r0 ** 2 * Rb)
    ePsi = ((4 * eta ** 2 + 4 * eta * r0) * ch * (Rb + eR) + r0 ** 2 * eR) / ((1 - rho) * bstar) + rho / (1 - rho)
    psi0 = 4 * r0 ** 2 / math.pi ** 2
    brV = 1 / ((1 + rho) * Gam) - (4 * eta ** 2 / psi0 + 4 * eta / math.sqrt(psi0)) * ch / (1 - rho)
    ok = rho <= 0.5 and ePsi <= PsiU / 2 and brV >= 0.5 / ((1 + rho) * Gam)
    return ok, dict(rho=rho, PsiU=PsiU, ePsi=ePsi, brV=brV, cZ=cZ, eR=eR, Gam=Gam, bstar=bstar, Rb=Rb)


def eta_star(kap, kh, L=3):
    best = (0.0, None)
    for i in range(40):
        r0 = 0.3 + 0.05 * i
        if r0 ** 2 >= 6:
            break
        lo, hi = 0.0, 0.5
        for _ in range(60):
            mid = (lo + hi) / 2
            if consts(mid, r0, kap, kh, L)[0]:
                lo = mid
            else:
                hi = mid
        if lo > best[0]:
            best = (lo, r0)
    return best


# ------------------------------------------------------------- analytic building blocks (complex arguments)
def delta_c(w, n):
    """entire continuation of |D_n|^2: sum_{|l|<n} (n-|l|)/n^2 e^{-iwl/n}."""
    w = np.asarray(w, dtype=complex)
    l = np.arange(-(n - 1), n)
    wl = (n - np.abs(l)) / n ** 2
    return (wl * np.exp(-1j * w[..., None] * l / n)).sum(-1)


def Dn_c(w, n):
    w = np.asarray(w, dtype=complex)
    j = np.arange(n)
    return np.exp(-1j * w[..., None] * j / n).sum(-1) / n


def phi1(w, n):
    return 2.0 * n * n * (1 - np.cos(np.asarray(w, dtype=complex) / n))


def Delta1(w):
    return 2.0 * (1 - np.cos(np.asarray(w, dtype=complex)))


def tvec(s):
    j = np.arange(2 * s)
    t = np.minimum(j + 1, 2 * s - 1 - j) / s ** 2
    t[2 * s - 1] = 0.0
    return t


def S_c(w, s):
    if s == 1:
        return np.ones_like(np.asarray(w, dtype=complex))
    t = tvec(s); a = t[:s]; b = t[s:2 * s]
    return (np.sum(a * a + b * b) + 2 * np.sum(a * b) * np.cos(np.asarray(w, dtype=complex))) / s


def A_c(z, mu, k, kap):
    out = 0.0
    for m in range(k):
        out = out + (kap[k - 1] / kap[k - 1 - m]) * S_c(z[mu], L ** m)
    return out


def Z_direct(z, n):
    """exact finite K != 0 alias sums Z_mu(z), mu = 0..3, for one complex point z (K_alpha in -(n-1)/2..(n-1)/2)."""
    Ks = np.arange(-(n - 1) // 2, (n - 1) // 2 + 1)
    dl = [delta_c(z[a] + 2 * np.pi * Ks, n) for a in range(d)]
    ph = [phi1(z[a] + 2 * np.pi * Ks, n) for a in range(d)]
    N = C.outer(dl)
    P = ph[0][:, None, None, None] + ph[1][None, :, None, None] + ph[2][None, None, :, None] + ph[3][None, None, None, :]
    i0 = (n - 1) // 2
    P[i0, i0, i0, i0] = 1.0
    out = []
    for mu in range(d):
        sh = [1] * d; sh[mu] = n
        term = N * dl[mu].reshape(sh) / P
        term[i0, i0, i0, i0] = 0.0
        out.append(term.sum())
    return np.array(out)


def blocks(z, n, k, kap, Z=None):
    """a, delta_mu, phi_mu, Delta_mu, R_mu, beta_mu, Psi, Sigma at one complex point z."""
    z = np.asarray(z, dtype=complex)
    dl = np.array([delta_c(z[a], n) for a in range(d)])
    ph = np.array([phi1(z[a], n) for a in range(d)])
    De = np.array([Delta1(z[a]) for a in range(d)])
    kp = kap[k - 1]
    a = kp * np.prod(dl)
    if Z is None:
        Z = Z_direct(z, n)
    R = np.array([A_c(z, mu, k, kap) for mu in range(d)]) + kp * Z
    phi = ph.sum()
    beta = a * dl + phi * R
    Psi = 1 - np.sum(ph * R / beta)
    Sig = np.sum(De / beta)
    return dict(a=a, dl=dl, ph=ph, De=De, R=R, Z=Z, phi=phi, beta=beta, Psi=Psi, Sig=Sig)


# ------------------------------------------------------------- real-grid versions (Part A, C)
def pc_grid(T):
    p = C.pgrid(T)
    return (p + np.pi) % (2 * np.pi) - np.pi


def Z_laplace(T, n):
    """K != 0 alias sums on the real grid, factorised Laplace quadrature (independent of c26's G)."""
    p = pc_grid(T)
    Ks = np.arange(-(n - 1) // 2, (n - 1) // 2 + 1)
    th = p[:, None] + 2 * np.pi * Ks[None, :]
    dl = delta_c(th, n).real
    ph = phi1(th, n).real
    i0 = (n - 1) // 2
    taus = np.arange(-34.0, math.log(6.0) + 0.1, 0.1)
    h = taus[1] - taus[0]
    Z = [np.zeros((T,) * d) for _ in range(d)]
    for tau in taus:
        t = math.exp(tau); e = np.exp(-t * ph)
        for mu in range(d):
            full = [(dl * e).sum(1) if a != mu else (dl * dl * e).sum(1) for a in range(d)]
            zero = [dl[:, i0] * e[:, i0] if a != mu else dl[:, i0] ** 2 * e[:, i0] for a in range(d)]
            Z[mu] += h * t * (C.outer(full) - C.outer(zero))
    return Z


def grid_blocks(T, k, kap, Z):
    n = L ** k
    p = pc_grid(T)
    g = np.meshgrid(*([p] * d), indexing="ij")
    dl = [delta_c(x, n).real for x in g]
    ph = [phi1(x, n).real for x in g]
    De = [Delta1(x).real for x in g]
    kp = kap[k - 1]
    a = kp * dl[0] * dl[1] * dl[2] * dl[3]
    R = [sum((kap[k - 1] / kap[k - 1 - m]) * S_c(g[mu], L ** m).real for m in range(k)) + kp * Z[mu] for mu in range(d)]
    phi = sum(ph)
    beta = [a * dl[mu] + phi * R[mu] for mu in range(d)]
    Psi = 1 - sum(ph[mu] * R[mu] / beta[mu] for mu in range(d))
    Sig = sum(De[mu] / beta[mu] for mu in range(d))
    nub = [np.exp(-1j * x) - 1 for x in g]
    return dict(g=g, dl=dl, ph=ph, De=De, a=a, R=R, phi=phi, beta=beta, Psi=Psi, Sig=Sig, nub=nub)


def R_formula(B, form):
    out = [[None] * len(PLANES) for _ in range(d)]
    for mu in range(d):
        for j, (aa, bb) in enumerate(PLANES):
            if mu == bb:
                nu, sgn = aa, 1.0
            elif mu == aa:
                nu, sgn = bb, -1.0
            else:
                out[mu][j] = 0.0 * B["a"]
                continue
            if form == "Psi":
                out[mu][j] = -sgn * B["a"] * B["nub"][nu] / (B["beta"][mu] * B["beta"][nu] * B["Psi"])
            else:
                out[mu][j] = -sgn * B["phi"] * B["nub"][nu] / (B["beta"][mu] * B["beta"][nu] * B["Sig"])
    return out


def part_A():
    print("Part A: exact identities (d = 4)")
    ok = True
    for T in (8, 12):
        for k in (1, 2, 3):
            for kap in ((1.0,) * k, (0.5, 1.0, 2.0)[:k]):
                n = L ** k
                P = C.P_symbol(d, T, k, kap)
                nu = C.nu_sym(d, T)
                Rc = C.R_symbol(P, nu, PLANES)
                Z = Z_laplace(T, n)
                B = grid_blocks(T, k, kap, Z)
                m0 = np.ones((T,) * d, bool); m0[(0,) * d] = False
                # informational: c26 P vs PROOF decomposition beta/phi
                dP = max(np.max(np.abs(P[mu][m0] - B["beta"][mu][m0] / B["phi"][m0]) / np.abs(P[mu][m0])) for mu in range(d))
                scale = max(np.max(np.abs(Rc[mu][j][m0])) for mu in range(d) for j in range(6))
                e1 = e2 = 0.0
                for form in ("Psi", "Sig"):
                    Rf = R_formula(B, form)
                    e = max(np.max(np.abs(Rc[mu][j][m0] - Rf[mu][j][m0])) for mu in range(d) for j in range(6)) / scale
                    if form == "Psi":
                        e1 = e
                    else:
                        e2 = e
                e3 = np.max(np.abs(B["a"] * B["Sig"] - B["phi"] * B["Psi"])) / np.max(np.abs(B["phi"]))
                # A4: b-form of r, with beta := phi * P (c26) so that r_from_b is the reference
                beta = [B["phi"] * P[mu] for mu in range(d)]
                Rr = [(beta[mu] - B["a"] * B["dl"][mu]) / B["phi"] for mu in range(d)]
                Psi = 1 - sum(B["ph"][mu] * Rr[mu] / beta[mu] for mu in range(d))
                nuc = [np.exp(1j * x) - 1 for x in B["g"]]
                e4 = 0.0; e5 = 0.0
                for trial in range(3):
                    bh = [RNG.normal(size=(T,) * d) + 1j * RNG.normal(size=(T,) * d) for _ in range(d)]
                    rc = C.r_from_b(P, bh, nu)
                    S1 = sum(B["nub"][v] * bh[v] / beta[v] for v in range(d))
                    rf = [-B["phi"] * bh[s] / beta[s] + nuc[s] * B["a"] * S1 / (beta[s] * Psi) for s in range(d)]
                    sc = max(np.max(np.abs(rc[s][m0])) for s in range(d))
                    e4 = max(e4, max(np.max(np.abs(rc[s][m0] - rf[s][m0])) for s in range(d)) / sc)
                    # A5: K = 0 term of f_0 as a map of b
                    D = [Dn_c(x, n) for x in B["g"]]
                    PD = D[0] * D[1] * D[2] * D[3]
                    nun = [n * (np.exp(1j * x / n) - 1) for x in B["g"]]
                    for u in ((0, 0, 0, 0), tuple(np.array((1, 2, 0, 1)) % n)):
                        ph_u = np.exp(1j * sum(B["g"][a] * u[a] for a in range(d)) / n)
                        for (ro, si) in PLANES:
                            W_s = PD * D[si]; W_r = PD * D[ro]
                            ref = np.zeros((T,) * d, complex)
                            ref[m0] = (-kap[k - 1] * ph_u * (nun[ro] * W_s * rc[si] - nun[si] * W_r * rc[ro]))[m0] / B["phi"][m0]
                            fm = kap[k - 1] * ph_u * (PD * (nun[ro] * D[si] * bh[si] / beta[si] - nun[si] * D[ro] * bh[ro] / beta[ro])
                                                      + (PD / Psi) * nun[ro] * nun[si] * (Rr[si] / beta[si] - Rr[ro] / beta[ro]) * S1)
                            sc5 = np.max(np.abs(ref[m0]))
                            e5 = max(e5, np.max(np.abs(ref[m0] - fm[m0])) / sc5)
                okc = e1 <= 1e-9 and e2 <= 1e-9 and e3 <= 1e-12 and e4 <= 1e-9 and e5 <= 1e-9
                ok &= okc
                p1 = (1,) + (0,) * (d - 1)
                print(f" T={T} k={k} kap={kap}: A1 {e1:.1e} A2 {e2:.1e} A3 {e3:.1e} A4 {e4:.1e} A5 {e5:.1e} "
                      f"{'PASS' if okc else 'FAIL'} | info: |P_c26 - beta/phi|rel {dP:.1e}, Psi(2pi/T e1)={B['Psi'][p1]:.6f}", flush=True)
    # informational: Laplace vs exact Z at real points (n = 9)
    em = 0.0
    for _ in range(20):
        x = RNG.uniform(-np.pi, np.pi, d)
        Zd = Z_direct(x.astype(complex), 9).real
        # single-point Laplace via the same quadrature
        Ks = np.arange(-4, 5); th = x[:, None] + 2 * np.pi * Ks[None, :]
        dl = delta_c(th, 9).real; ph = phi1(th, 9).real
        taus = np.arange(-34.0, math.log(6.0) + 0.1, 0.1); h = taus[1] - taus[0]
        Zl = np.zeros(d)
        for tau in taus:
            t = math.exp(tau); e = np.exp(-t * ph)
            for mu in range(d):
                full = np.prod([(dl[a] * e[a]).sum() if a != mu else (dl[a] ** 2 * e[a]).sum() for a in range(d)])
                zero = np.prod([dl[a, 4] * e[a, 4] if a != mu else dl[a, 4] ** 2 * e[a, 4] for a in range(d)])
                Zl[mu] += h * t * (full - zero)
        em = max(em, np.max(np.abs(Zl - Zd)))
    # A6 informational: values at p = 0
    B0 = blocks(np.zeros(d, complex), 9, 2, (1.0, 1.0))
    print(f" info: max|Z_laplace - Z_exact| at 20 real points (n = 9) = {em:.1e}; at p = 0 (n = 9, k = 2): "
          f"Psi = {B0['Psi'].real:.12f}, beta = {np.round(B0['beta'].real, 6)}")
    print("Part A:", "VALID (all PASS)" if ok else "FAIL")


# ------------------------------------------------------------- Part B
def part_B():
    print("Part B: strip inequalities at complex points (exact alias sums)")
    allok = True
    for kapv in (1.0, 0.25, 4.0):
        eta, r0 = eta_star(kapv, 1.0)
        _, K = consts(eta, r0, kapv, 1.0)
        for k in (1, 2, 3):
            n = L ** k; kap = (kapv,) * k
            nx = 150 if k < 3 else 40
            xs = [RNG.uniform(-np.pi, np.pi, d) for _ in range(nx)]
            xs += [np.zeros(d), np.full(d, np.pi), np.array([np.pi, 0, 0, 0]), np.array([r0, 0, 0, 0]),
                   np.array([r0, r0, 0, 0]) / math.sqrt(2)]
            worst = dict(B1=0.0, B1r=0.0, B2=0.0, B2r=np.inf, B3r=np.inf, B3=0.0, B4=np.inf, B5=0.0)
            for x in xs:
                Bx = blocks(x.astype(complex), n, k, kap)
                beta_x = Bx["beta"].real
                worst["B1r"] = max(worst["B1r"], np.max(Bx["Z"].real) * 9)
                worst["B2r"] = min(worst["B2r"], np.min(beta_x) / K["bstar"])
                worst["B5"] = max(worst["B5"], np.max(beta_x) / np.min(beta_x) / K["Gam"])
                rx = np.linalg.norm(x)
                if rx <= r0 + 1e-12:
                    worst["B3r"] = min(worst["B3r"], Bx["Psi"].real / K["PsiU"])
                ys = [RNG.uniform(-eta, eta, d) for _ in range(2)] + [eta * RNG.choice([-1, 1], d) for _ in range(2)]
                for y in ys:
                    Bz = blocks(x + 1j * y, n, k, kap)
                    worst["B1"] = max(worst["B1"], np.max(np.abs(Bz["Z"] - Bx["Z"])) / K["cZ"])
                    worst["B2"] = max(worst["B2"], np.max(np.abs(Bz["beta"] - Bx["beta"]) / beta_x) / K["rho"])
                    if rx <= r0 + 1e-12:
                        worst["B3"] = max(worst["B3"], abs(Bz["Psi"] - Bx["Psi"]) / K["ePsi"])
                    if rx >= r0 - 1e-12:
                        psi = Bx["De"].real.sum()
                        lb = psi / np.min(beta_x) * K["brV"]
                        worst["B4"] = min(worst["B4"], Bz["Sig"].real / lb)
            ok = (worst["B1"] <= 1 and worst["B1r"] <= 1 and worst["B2"] <= 1 and worst["B2r"] >= 1
                  and worst["B3"] <= 1 and worst["B3r"] >= 1 and worst["B4"] >= 1 and worst["B5"] <= 1)
            allok &= ok
            print(f" kap={kapv} eta*={eta:.4f} r0={r0:.2f} n={n}: |dZ|/cZ {worst['B1']:.3f}, 9Z {worst['B1r']:.3f}, "
                  f"|dbeta|/(rho beta) {worst['B2']:.3f}, beta/b* {worst['B2r']:.3f}, |dPsi|/ePsi {worst['B3']:.3f}, "
                  f"Psi/PsiU {worst['B3r']:.3f}, ReSig/lb {worst['B4']:.3f}, ratio/Gam {worst['B5']:.3f} "
                  f"{'PASS' if ok else 'FAIL'}", flush=True)
    print("Part B:", "PASS" if allok else "FAIL")


# ------------------------------------------------------------- Part C
def axis_profile(entries_fn, T):
    prof = np.zeros(T // 2 + 1)
    for sym in entries_fn():
        Kx = np.fft.ifftn(sym)
        line = np.abs(Kx[(slice(0, T // 2 + 1),) + (0,) * (d - 1)])
        prof = np.maximum(prof, line)
        del Kx
    return prof


def fit_rate(prof, T):
    xs = np.arange(3, T // 2 - 2 + 1)
    vals = prof[xs]
    m = vals > 1e-12 * prof.max()
    if m.sum() < 2:
        return float("nan")
    s = np.polyfit(xs[m], np.log(vals[m]), 1)[0]
    return -s


def part_C():
    print("Part C: decay rates along the axis (kappa = 1)")
    eta1, _ = eta_star(1.0, 1.0)
    rates = {}
    for T in (16, 24, 32):
        for k in (1, 2, 3):
            kap = (1.0,) * k
            P = C.P_symbol(d, T, k, kap); nu = C.nu_sym(d, T)
            R = C.R_symbol(P, nu, PLANES)
            prof = axis_profile(lambda: (R[mu][j] for mu in range(d) for j in range(6) if np.any(R[mu][j] != 0)), T)
            rates[("R", T, k)] = fit_rate(prof, T)
            print(f" R  T={T} k={k}: rate {rates[('R', T, k)]:.4f}  ratio/unit {math.exp(-rates[('R', T, k)]):.3f}  "
                  f"profile x=1..8: {' '.join(f'{v:.2e}' for v in prof[1:9])}  rss {rss():.0f} MB", flush=True)
            if T <= 24 and k <= 2:
                cols = []
                for v in range(d):
                    bh = [np.full((T,) * d, 1.0 + 0j) if s == v else np.zeros((T,) * d, complex) for s in range(d)]
                    cols.append(C.r_from_b(P, bh, nu))
                prof = axis_profile(lambda: (cols[v][s] for v in range(d) for s in range(d)), T)
                rates[("rb", T, k)] = fit_rate(prof, T)
                print(f" rb T={T} k={k}: rate {rates[('rb', T, k)]:.4f}", flush=True)
                n = L ** k
                for u in ((0, 0, 0, 0), (1, 0, 0, 0)):
                    Phi = {(a, b): C.Phi_f(d, T, n, a, b, u) for a in range(d) for b in range(d) if a != b}

                    def fsyms():
                        for v in range(d):
                            r = cols[v]
                            for (a, b) in PLANES:
                                yield n ** (5.0 - d) * (-1.0) * (Phi[(a, b)] * r[b] - Phi[(b, a)] * r[a])
                    prof = axis_profile(fsyms, T)
                    rates[("fb", u, T, k)] = fit_rate(prof, T)
                    print(f" fb u={u} T={T} k={k}: rate {rates[('fb', u, T, k)]:.4f}  profile x=1..8: "
                          f"{' '.join(f'{v:.2e}' for v in prof[1:9])}", flush=True)
                    del Phi
                if k == 1:
                    Pc = C.pi_coex(d, T, PLANES)
                    rep = C.rep_symbols(d, T, k, (1.0,), (1, 0, 0, 0), R, Pc, PLANES)
                    prof = axis_profile(lambda: (rep[i][j] for i in range(6) for j in range(6)), T)
                    xs = np.arange(3, T // 2 - 1)
                    ls = -np.polyfit(np.log(xs), np.log(prof[xs]), 1)[0]
                    er = fit_rate(prof, T)
                    rl = np.polyfit(np.log(xs), np.log(prof[xs]), 1, full=True)[1]
                    re_ = np.polyfit(xs, np.log(prof[xs]), 1, full=True)[1]
                    print(f" rep(K_u+Pi_coex) u=(1,0,0,0) T={T}: log-log slope {ls:.2f}, exp rate {er:.3f}, "
                          f"residual power {float(rl[0]) if len(rl) else 0:.2e} vs exp {float(re_[0]) if len(re_) else 0:.2e}; "
                          f"profile x=1..8: {' '.join(f'{v:.2e}' for v in prof[1:9])}", flush=True)
                del cols
            del P, R
    exp_keys = [kk for kk in rates if kk[0] in ("R", "rb", "fb")]
    c1 = all(rates[kk] >= eta1 for kk in exp_keys)
    c2 = True
    for kind in ("R", "rb"):
        for T in (16, 24, 32):
            vs = [rates[(kind, T, k)] for k in (1, 2, 3) if (kind, T, k) in rates]
            if len(vs) > 1:
                c2 &= max(vs) / min(vs) <= 1.10
    for u in ((0, 0, 0, 0), (1, 0, 0, 0)):
        for T in (16, 24):
            vs = [rates[("fb", u, T, k)] for k in (1, 2)]
            c2 &= max(vs) / min(vs) <= 1.10
    c3 = all(max(rates[("R", T, k)] for T in (16, 24, 32)) / min(rates[("R", T, k)] for T in (16, 24, 32)) <= 1.10
             for k in (1, 2, 3))
    print(f" C1 (all rates >= eta* = {eta1:.4f}): {'PASS' if c1 else 'FAIL'}")
    print(f" C2 (k-stability <= 1.10): {'PASS' if c2 else 'FAIL'}")
    print(f" C3 (T-stability of R <= 1.10): {'PASS' if c3 else 'FAIL'}")
    # C4: singularity search, k = 1, n = 3, kappa = 1
    n = 3; k = 1; kap = (1.0,)
    vals = [0.0, np.pi / 2, np.pi]
    combos = sorted(set(tuple(sorted(c)) for c in itertools.product(vals, repeat=3)))
    rw = np.arange(-np.pi, np.pi + 1e-9, 0.05); iw = np.arange(0.05, 3.0 + 1e-9, 0.05)

    def Den(w, pp):
        B = blocks(np.array([w, pp[0], pp[1], pp[2]], dtype=complex), n, k, kap)
        return np.prod(B["beta"]) * B["Psi"]
    best = (np.inf, None)
    for pp in combos:
        G = np.array([[abs(Den(a + 1j * b, pp)) for b in iw] for a in rw])
        for i in range(1, len(rw) - 1):
            for j in range(0, len(iw) - 1):
                nb = G[max(i - 1, 0):i + 2, max(j - 1, 0):j + 2]
                if G[i, j] <= nb.min() + 1e-300:
                    w = rw[i] + 1j * iw[j]
                    for _ in range(60):
                        f = Den(w, pp); hh = 1e-6
                        fp = (Den(w + hh, pp) - Den(w - hh, pp)) / (2 * hh)
                        if fp == 0:
                            break
                        w = w - f / fp
                    if abs(Den(w, pp)) < 1e-10 and 0 < w.imag < best[0]:
                        best = (w.imag, (w, pp))
    msing = best[0]
    mm = rates[("R", 32, 1)]
    c4 = abs(mm / msing - 1) <= 0.15 if np.isfinite(msing) else False
    print(f" C4: nearest zero of Den: Im w = {msing:.4f} at w = {best[1][0] if best[1] else None}, p_perp = "
          f"{best[1][1] if best[1] else None}; measured R rate (T=32, k=1) {mm:.4f}; ratio {mm / msing:.3f}: "
          f"{'PASS' if c4 else 'FAIL'}")
    print("Part C:", "PASS" if (c1 and c2 and c3 and c4) else "FAIL (see sub-checks)")


# ------------------------------------------------------------- Part D: composite slice functional (d = 4, L = 3, k = 2)
PERMS = list(itertools.permutations(range(d)))
OFFS = list(itertools.product(range(-(L - 1) // 2, (L - 1) // 2 + 1), repeat=d))


def h_one(a, N):
    """one-step S4' slice functional on a lattice of side N (own units): avg_sigma avg_y int_{P^sigma(c_X -> y)} a."""
    Nc = N // L
    X = np.array(list(itertools.product(range(Nc), repeat=d)))
    c = L * X + (L - 1) // 2
    out = np.zeros(len(X))
    for off in OFFS:
        for sg in PERMS:
            q = c.copy(); tot = np.zeros(len(X))
            for al in sg:
                t = off[al]
                if t > 0:
                    for _ in range(t):
                        tot += a[al][tuple((q % N).T)]; q[:, al] += 1
                elif t < 0:
                    for _ in range(-t):
                        q[:, al] -= 1; tot -= a[al][tuple((q % N).T)]
            out += tot
    out /= len(OFFS) * len(PERMS)
    return out.reshape((Nc,) * d)


def qstr(a, N, s):
    Nc = N // s
    out = []
    for mu in range(d):
        line = np.zeros_like(a[mu])
        for j in range(s):
            line += np.roll(a[mu], -j, axis=mu)
        v = line.reshape(sum(([Nc, s] for _ in range(d)), [])).sum(axis=tuple(range(1, 2 * d, 2))) / s ** d
        out.append(v)
    return out


def dscal(lam):
    return [np.roll(lam, -1, axis=mu) - lam for mu in range(d)]


def bmean(f, s):
    Nc = f.shape[0] // s
    return f.reshape(sum(([Nc, s] for _ in range(d)), [])).mean(axis=tuple(range(1, 2 * d, 2)))


def qroot(a, N):
    hs = h_one(a, N)
    qs = qstr(a, N, L)
    dh = dscal(hs)
    return [qs[mu] - dh[mu] for mu in range(d)]


def part_D():
    print("Part D: composite slice functional, d = 4, L = 3, k = 2, coarse T = 2")
    Tc = 2; N = Tc * L * L; N1 = Tc * L
    fields = [[RNG.normal(size=(N,) * d) for _ in range(d)] for _ in range(5)]
    # axial lines through block centres
    f = [np.zeros((N,) * d) for _ in range(d)]
    o = (L * L - 1) // 2
    for X in itertools.product(range(Tc), repeat=d):
        c = np.array(X) * L * L + o
        for mu in range(d):
            for t in range(-o, o):
                idx = c.copy(); idx[mu] += t
                f[mu][tuple(idx % N)] = 1.0
    fields.append(f)
    f = [np.zeros((N,) * d) for _ in range(d)]
    for X in itertools.product(range(Tc), repeat=d):
        base = np.array(X) * L * L + (L * L - L) // 2
        for off in itertools.product(range(L), repeat=d):
            for mu in range(d):
                f[mu][tuple((base + np.array(off)) % N)] = RNG.normal()
    fields.append(f)
    fields.append([np.full((N,) * d, 1.0) for _ in range(d)])
    e1 = e3 = 0.0; r4 = 0.0
    C4 = 4 * L * L / (L - 1)
    for a in fields:
        h1 = h_one(a, N)
        q1 = qroot(a, N)
        h2 = bmean(h1, L) + h_one(q1, N1)
        un = h_one(qstr(a, N, L), N1) + h1[(slice((L - 1) // 2, None, L),) * d]
        e1 = max(e1, np.max(np.abs(h2 - un)))
        q2 = qroot(q1, N1)
        q9 = qstr(a, N, L * L); dh2 = dscal(h2)
        e3 = max(e3, max(np.max(np.abs(q2[mu] - (q9[mu] - dh2[mu]))) for mu in range(d)))
        e2b = sum(a[mu] ** 2 for mu in range(d))
        loc = bmean(e2b, L * L) * (L * L) ** d
        with np.errstate(divide="ignore", invalid="ignore"):
            rr = np.where(loc > 0, h2 ** 2 / (C4 * loc), 0.0)
        r4 = max(r4, np.max(rr))
    e2 = 0.0
    for _ in range(3):
        lam = RNG.normal(size=(N,) * d)
        dl = dscal(lam)
        h1 = h_one(dl, N); q1 = qroot(dl, N)
        h2 = bmean(h1, L) + h_one(q1, N1)
        ref = bmean(lam, L * L) - lam[(slice(o, None, L * L),) * d]
        e2 = max(e2, np.max(np.abs(h2 - ref)))
    ok = e1 <= 1e-12 and e2 <= 1e-12 and e3 <= 1e-12 and r4 <= 1
    print(f" D1 recursion vs unrolled {e1:.1e}; D2 h2(d lam) = M lam - lam(c) {e2:.1e}; D3 composite identity {e3:.1e}; "
          f"D4 max |h2|^2/((4L^2/(L-1)) sum_B a^2) = {r4:.4f}")
    print("Part D:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    part = sys.argv[1]
    {"A": part_A, "B": part_B, "C": part_C, "D": part_D}[part]()
    print(f"time {time.time() - T0:.1f} s, peak RSS {rss():.0f} MB")
