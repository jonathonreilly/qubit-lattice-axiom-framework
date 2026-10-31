"""f13 (lane C, session 10): FLOW.md §73 (T1), (T3) numerically, and the vector bordered identity (T4)-(T5), (T7) (a).

Criteria: checks/f13_criteria.md (written before this script).
Part A: Lemma FINE-IR, x_0(q) = [eps^2] tau log Delta_U / (q^2/2), by a 2D proper-time quadrature (symmetrised form).
Part B: Y_n(P) := x_n(P) - 2 c_g log(1/P) = x_0(P/l) - 2 l^2 h_n(P/l)/P^2 - 2 c_g log(1/P), h_n from the f12 functions
        (checks/f12_proxy_2pt.py, executed UNCHANGED into a namespace; its md5 is printed).
Part C: SU(2) root sector at Cartan backgrounds on the torus 6x6x3x3, l = 3: the identities of (T4), (T5), and E_U = H D_U.
Run:  OMP_NUM_THREADS=1 ... nice -n 10 python3 f13_uir_vbord.py > f13_out.txt
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import hashlib
import time
import numpy as np
from scipy.special import ive

sys.dont_write_bytecode = True
L = 3
CG = 1.0 / (96 * np.pi ** 2)
SMOKE = os.environ.get("F13_SMOKE") == "1"
T0 = time.time()
VERD = []
HERE = os.path.dirname(os.path.abspath(__file__))


def say(*a):
    print(*a, flush=True)


def verdict(name, ok, detail):
    VERD.append((name, bool(ok)))
    say(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# =============================================================== Part A: fine polarisation x_0(q)
def ive_s(nu, x):
    """scaled Bessel e^{-x} I_nu(x) (scipy's ive returns nan above ~1e9): Hankel asymptotic series above 1e5."""
    x = np.asarray(x, float)
    out = np.empty_like(x)
    sm = x < 1e5
    out[sm] = ive(nu, x[sm])
    xb = x[~sm]
    mu = 4.0 * nu * nu
    term = np.ones_like(xb)
    acc = np.ones_like(xb)
    for k in range(1, 7):
        term = term * (-(mu - (2 * k - 1) ** 2) / (k * 8.0 * xb))
        acc = acc + term
    out[~sm] = acc / np.sqrt(2 * np.pi * xb)
    return out


def _grid(q, h, umin=-16.0, extra=34.0):
    qh2 = 2.0 - 2.0 * np.cos(q)
    umax = extra + np.log(1.0 / qh2)
    u = np.arange(umin, umax + 0.5 * h, h)
    return np.exp(u)


def x0_sym(q, h=0.1):
    s = _grid(q, h)
    S = s[:, None]
    T = s[None, :]
    tau = S + T
    cq = np.cos(q)
    omc = 2.0 * np.sin(q / 2) ** 2                      # 1 - cos q
    R = np.sqrt(S * S + T * T + 2.0 * S * T * cq)
    dR = 2.0 * S * T * omc / (tau + R)                 # tau - R
    B1 = ive_s(1, 2 * tau) / (2 * tau)                  # (I_0 - I_2)(2 tau)/2 = I_1(2 tau)/(2 tau), scaled
    I0 = ive_s(0, 2 * tau)
    omc2 = (S - T) ** 2 * omc / (R * R)                 # 1 - cos 2 psi
    B2 = 0.5 * (ive_s(1, 2 * R) / R + omc2 * ive_s(2, 2 * R))   # (I_0 - cos2psi I_2)(2R)/2, scaled
    f = (S * T) ** 2 * B1 * B2 * I0 * I0 * np.exp(-2.0 * dR)
    J = h * h * f.sum() / 1.0
    return 16.0 * np.sin(q / 2) ** 2 / q ** 2 * J


def x0_unsym(q, h=0.1):
    # A_W = int dk 2cos k1 / lam = int dT 2 ive1(2T) ive0(2T)^3
    u = np.arange(-16.0, 60.0 + 0.5 * h, h)
    Tt = np.exp(u)
    AW = h * np.sum(Tt * 2.0 * ive_s(1, 2 * Tt) * ive_s(0, 2 * Tt) ** 3)
    s = _grid(q, h, umin=-40.0)                         # this integrand is ~ s t at small s, t (not (s t)^2)
    S = s[:, None]
    T = s[None, :]
    tau = S + T
    cq = np.cos(q)
    omc = 2.0 * np.sin(q / 2) ** 2
    R = np.sqrt(S * S + T * T + 2.0 * S * T * cq)
    dR = 2.0 * S * T * omc / (tau + R)
    f = (S * T) * 4.0 * (ive_s(1, 2 * tau) / (2 * tau)) * ive_s(0, 2 * R) * ive_s(0, 2 * tau) ** 2 * np.exp(-2.0 * dR)
    AS = h * h * f.sum()
    return (AW - AS) / (2.0 * q * q)


_X0 = {}
PS_B = [0.05, 0.1, 0.2, 0.4, 0.8, 1.6, 2.4]


def x0(q, h=0.1):
    key = (round(q, 15), h)
    if key not in _X0:
        _X0[key] = x0_sym(q, h)
    return _X0[key]


def part_a():
    say("Part A (Lemma FINE-IR: fine scalar polarisation x_0(q))")
    hA, hB = (0.2, 0.1) if SMOKE else (0.1, 0.05)
    qs = [1e-3, 2e-3, 5e-3, 1e-2, 2e-2, 5e-2, 0.1, 0.3, 0.6, 0.8]
    worst = 0.0
    for q in qs:
        a, b = x0(q, hA), x0(q, hB)
        worst = max(worst, abs(a - b) / abs(b))
        say(f"    x_0({q:g}) = {b:.13e}   (h = {hB}: step-halving rel change {abs(a - b) / abs(b):.1e})")
    worstB = 0.0
    for n in range(1, (3 if SMOKE else 5) + 1):
        for P in PS_B:
            q = P / L ** n
            a, b = x0(q, hA), x0(q, hB)
            worstB = max(worstB, abs(a - b) / abs(b))
    say(f"    step halving at the Part B q = P/3^n values: max rel change {worstB:.1e}")
    worst = max(worst, worstB)
    verdict("A1 step control (all q used)", worst <= 1e-10, f"max rel change under h -> h/2 = {worst:.1e} (threshold 1e-10)")
    for q in (0.3, 0.6):
        xs, xu = x0(q, hB), x0_unsym(q, hB)
        rel = abs(xs - xu) / abs(xs)
        verdict(f"A2 symmetrisation identity q = {q}", rel <= 1e-9, f"sym = {xs:.13e}, unsym = {xu:.13e}, rel = {rel:.1e} (threshold 1e-9)")
    sl = -(x0(1e-2, hB) - x0(1e-3, hB)) / (np.log(1e-2) - np.log(1e-3))
    rel = abs(sl - 2 * CG) / (2 * CG)
    verdict("A3 log slope (S10-F1)", rel <= 1e-3, f"-dx_0/dlog q on [1e-3, 1e-2] = {sl:.10e}, 2c_g = {2 * CG:.10e}, rel = {rel:.1e} (threshold 1e-3)")

    def fit(qmin, qmax):
        qq = np.array([q for q in [1e-3, 2e-3, 5e-3, 1e-2, 2e-2, 5e-2, 0.1] if qmin <= q <= qmax])
        y = np.array([x0(q, hB) - 2 * CG * np.log(1 / q) for q in qq])
        A = np.stack([np.ones_like(qq), qq ** 2 * np.log(qq), qq ** 2], 1)
        return np.linalg.lstsq(A, y, rcond=None)[0][0]
    a0 = fit(1e-3, 0.05)
    a0b = fit(2e-3, 0.1)
    say(f"    [reported] a_0 = {a0:.12e} (window [1e-3, 0.05]); window [2e-3, 0.1]: {a0b:.12e}; change {abs(a0 - a0b):.1e}")
    return a0, hB


# =============================================================== Part B: (VC)/(UIR) for the scalar proxy
def load_f12():
    path = os.path.join(HERE, "f12_proxy_2pt.py")
    src = open(path, "rb").read()
    ns = {"__name__": "f12mod", "__file__": path}
    exec(compile(src, path, "exec"), ns)
    return ns, hashlib.md5(src).hexdigest()


def part_b(a0, hA):
    say("Part B ((VC)/(UIR): Y_n(P) = x_n(P) - 2 c_g log(1/P), scalar proxy L = 3, s = 4)")
    f12, md5 = load_f12()
    say(f"    f12 functions from checks/f12_proxy_2pt.py, md5 {md5} (executed unchanged)")
    Ps = PS_B
    nmax = 3 if SMOKE else 5
    rho_f12 = {1: -1.6066720951e-3, 2: -1.7525401957e-3, 3: -1.7663394360e-3, 4: -1.7678560623e-3}

    def Y(n, P, NK, h_u):
        l = L ** n
        p = P / l
        h = f12["h_of_p"](n, NK, p, h_u)
        return x0(p, hA) - h / (p * p / 2.0) - 2 * CG * np.log(1 / P)      # = x_0(P/l) - 2 l^2 h_n(P/l)/P^2 - 2c_g log(1/P)

    Yv = {}
    for n in range(1, nmax + 1):
        t1 = time.time()
        if SMOKE:
            main, alt = (8, 0.3), (10, 0.3)
        elif n <= 4:
            main, alt = (16, 0.3), (12, 0.3)
        else:
            main, alt = (16, 0.15), None
        Yv[n] = np.array([Y(n, P, *main) for P in Ps])
        if n <= 4 or SMOKE:
            Ya = np.array([Y(n, P, *alt) for P in Ps])
            d = np.max(np.abs(Yv[n] - Ya))
            verdict(f"B1 step control n = {n}", d <= 1e-9, f"max_P |Y(N_K={main[0]}) - Y(N_K={alt[0]})| = {d:.1e} (h_u = {main[1]}; threshold 1e-9)")
        else:
            Y1 = np.array([Y(n, P, 12, 0.15) for P in Ps])
            Y2 = np.array([Y(n, P, 12, 0.1) for P in Ps])
            d = np.max(np.abs(Y1 - Y2))
            verdict(f"B1 step control n = {n}", d <= 1e-9, f"max_P |Y(h_u=0.15) - Y(h_u=0.1)| at N_K = 12 = {d:.1e} (threshold 1e-9)")
            say(f"    [reported] n = 5: max_P |Y(N_K=16,h_u=0.15) - Y(N_K=12,h_u=0.15)| = {np.max(np.abs(Yv[n] - Y1)):.1e}")
        say("    n = %d (%.0f s): Y_n(P) = %s" % (n, time.time() - t1, ", ".join("%.12e" % v for v in Yv[n])))
        if n in rho_f12:
            say(f"    [reported] Y_n(0.05) - (a_0 - rho_n[f12]) = {Yv[n][0] - (a0 - rho_f12[n]):.3e}")
    Dn = {}
    for n in range(2, nmax + 1):
        diff = np.abs(Yv[n] - Yv[n - 1])
        Dn[n] = diff.max()
        say(f"    [reported] |Y_{n} - Y_{n-1}|(P) = " + ", ".join("%.4e" % v for v in diff) + f"; max {Dn[n]:.4e} at P = {Ps[int(diff.argmax())]}")
        if n >= 3:
            r = Dn[n] / Dn[n - 1]
            verdict(f"B2 ratio n = {n}", r <= 0.2, f"Delta_{n}/Delta_{n-1} = {r:.5f} (threshold 0.2; L^-2 = 0.11111)")
            verdict(f"B3 uniformity n = {n}", diff[0] <= 2 * diff[3], f"|dY|(0.05) = {diff[0]:.4e} vs 2|dY|(0.4) = {2 * diff[3]:.4e}")


# =============================================================== Part C: vector bordered identity (SU(2) root sector)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
TG = [1j * s for s in SIG]          # T_a = i sigma_a; coordinates x^a along T_a; <Y,Z> = -1/2 tr(YZ)
DIMS = (6, 6, 3, 3)
NS = int(np.prod(DIMS))
LV = 3
LDIMS = tuple(d // LV for d in DIMS)
NLS = int(np.prod(LDIMS))
ROOT = (0, 1)


def expm_su2(Xc):
    """exp of sum_a x^a T_a, Xc shape (..., 3) real."""
    th = np.sqrt((Xc ** 2).sum(-1))
    c = np.cos(th)
    sn = np.where(th > 1e-300, np.sin(th) / np.where(th > 0, th, 1.0), 1.0)
    out = np.zeros(Xc.shape[:-1] + (2, 2), complex)
    out[..., 0, 0] = c
    out[..., 1, 1] = c
    for a in range(3):
        out = out + (sn * Xc[..., a])[..., None, None] * TG[a]
    return out


def dag(A):
    return np.conj(np.swapaxes(A, -1, -2))


def roll(A, mu, k):
    return np.roll(A, -k, axis=mu)          # roll(A, mu, 1)[x] = A[x + mu]


def coords(Xm):
    """su(2) matrix -> coordinates along T_a: x^a = -1/2 tr(T_a X) ... with <T_a,T_b> = delta: x^a = -1/2 Re tr(T_a X)."""
    return np.stack([-0.5 * np.real(np.einsum("ij,...ji->...", TG[a], Xm)) for a in range(3)], -1)


def grad_S(U):
    """dS/dx^a_b at U (chart U_b e^{x T}), S = sum_P (1 - 1/2 Re tr U_P). U shape DIMS + (4, 2, 2)."""
    g = np.zeros(DIMS + (4, 3))
    for mu in range(4):
        St = np.zeros(DIMS + (2, 2), complex)
        Um = U[..., mu, :, :]
        for nu in range(4):
            if nu == mu:
                continue
            Un = U[..., nu, :, :]
            St = St + roll(Un, mu, 1) @ dag(roll(Um, nu, 1)) @ dag(Un)
            Unb = roll(Un, nu, -1)
            St = St + dag(roll(Unb, mu, 1)) @ dag(roll(Um, nu, -1)) @ Unb
        SU = St @ Um                       # d/dt Re tr(U e^{tT} St) = Re tr(T St U)
        for a in range(3):
            g[..., mu, a] = -0.5 * np.real(np.einsum("...ij,ji->...", SU, TG[a]))
    return g


def S_wilson(U):
    s = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            P = U[..., mu, :, :] @ roll(U[..., nu, :, :], mu, 1) @ dag(roll(U[..., mu, :, :], nu, 1)) @ dag(U[..., nu, :, :])
            s += np.sum(1.0 - 0.5 * np.real(np.trace(P, axis1=-2, axis2=-1)))
    return s


def site_index(x):
    return np.ravel_multi_index(tuple(x), DIMS)


def link_rows():
    """root-sector real index of link (x, mu, a), a in ROOT."""
    return lambda x, mu, a: ((site_index(x) * 4 + mu) * 2 + a)


LIDX = link_rows()


def background(theta, eps, p, vth):
    Xc = np.zeros(DIMS + (4, 3))
    x2 = np.arange(DIMS[1])
    for mu in range(4):
        Xc[..., mu, 2] = theta[mu]
    Xc[..., 0, 2] += eps * np.cos(p * x2 + vth)[None, :, None, None]
    return expm_su2(Xc)


def hessian_root(U, h=1e-4):
    """root block of the symmetrised exponential-chart Hessian, central differences with Richardson."""
    nr = NS * 4 * 2
    Hm = np.zeros((nr, nr))
    allx = list(np.ndindex(*DIMS))
    for x in allx:
        for mu in range(4):
            for a in ROOT:
                col = LIDX(x, mu, a)
                gs = []
                for hh in (h, h / 2):
                    pr = []
                    for sgn in (1, -1):
                        V = U.copy()
                        e = np.zeros(3)
                        e[a] = sgn * hh
                        V[x + (mu,)] = U[x + (mu,)] @ expm_su2(e)
                        pr.append(grad_S(V)[..., :, list(ROOT)].reshape(-1))
                    gs.append((pr[0] - pr[1]) / (2 * hh))
                Hm[:, col] = (4 * gs[1] - gs[0]) / 3
    return 0.5 * (Hm + Hm.T), Hm


def Ad(g, Xm):
    return g @ Xm @ dag(g)


def D_matrix(U):
    """root block of D_U: (D lam)_b = Ad(U_b^{-1}) lam(x) - lam(x + mu); rows link-root, cols site-root."""
    nr, nc = NS * 4 * 2, NS * 2
    Dm = np.zeros((nr, nc))
    for x in np.ndindex(*DIMS):
        for mu in range(4):
            xp = list(x)
            xp[mu] = (xp[mu] + 1) % DIMS[mu]
            for a in ROOT:
                col_x = site_index(x) * 2 + a
                col_xp = site_index(xp) * 2 + a
                v = coords(Ad(dag(U[x + (mu,)]), TG[a]))
                for a2 in ROOT:
                    Dm[LIDX(x, mu, a2), col_x] += v[a2]
                    Dm[LIDX(x, mu, a2), col_xp] -= (1.0 if a2 == a else 0.0)
    return Dm


def level_sites():
    return [tuple(LV * X[i] for i in range(4)) for X in np.ndindex(*LDIMS)]


def M_and_level(U):
    """straight-path decimation: M (level-link-root x fine-link-root), level links V, level gradient D_l."""
    lsites = list(np.ndindex(*LDIMS))
    nlr = len(lsites) * 4 * 2
    Mm = np.zeros((nlr, NS * 4 * 2))
    V = {}
    for iX, X in enumerate(lsites):
        for mu in range(4):
            ys = []
            for j in range(LV):
                y = [LV * X[i] for i in range(4)]
                y[mu] = (y[mu] + j) % DIMS[mu]
                ys.append(tuple(y))
            Us = [U[y + (mu,)] for y in ys]
            V[(iX, mu)] = Us[0] @ Us[1] @ Us[2]
            for j in range(LV):
                Rj = np.eye(2, dtype=complex)
                for k in range(j + 1, LV):
                    Rj = Rj @ Us[k]
                for a in ROOT:
                    v = coords(Ad(dag(Rj), TG[a]))
                    for a2 in ROOT:
                        Mm[(iX * 4 + mu) * 2 + a2, LIDX(ys[j], mu, a)] += v[a2]
    Dl = np.zeros((nlr, len(lsites) * 2))
    for iX, X in enumerate(lsites):
        for mu in range(4):
            Xp = list(X)
            Xp[mu] = (Xp[mu] + 1) % LDIMS[mu]
            iXp = lsites.index(tuple(Xp))
            for a in ROOT:
                v = coords(Ad(dag(V[(iX, mu)]), TG[a]))
                for a2 in ROOT:
                    Dl[(iX * 4 + mu) * 2 + a2, iX * 2 + a] += v[a2]
                    Dl[(iX * 4 + mu) * 2 + a2, iXp * 2 + a] -= (1.0 if a2 == a else 0.0)
    iota = np.zeros((NS * 2, len(lsites) * 2))
    for iX, X in enumerate(lsites):
        for a in ROOT:
            iota[site_index(tuple(LV * X[i] for i in range(4))) * 2 + a, iX * 2 + a] = 1.0
    return Mm, Dl, iota


def ld(A):
    s, v = np.linalg.slogdet(A)
    return v, s


def E_formula(U, J):
    """(E lam)_b = 1/2 [Ad(U_b^{-1}) lam(x) + lam(x + mu), J_b], J_b = sum_a dS/dx^a T_a; root block."""
    nr, nc = NS * 4 * 2, NS * 2
    Em = np.zeros((nr, nc))
    for x in np.ndindex(*DIMS):
        for mu in range(4):
            xp = list(x)
            xp[mu] = (xp[mu] + 1) % DIMS[mu]
            Jb = sum(J[x + (mu, a)] * TG[a] for a in range(3))
            for a in ROOT:
                w1 = Ad(dag(U[x + (mu,)]), TG[a])
                v1 = coords(0.5 * (w1 @ Jb - Jb @ w1))
                v2 = coords(0.5 * (TG[a] @ Jb - Jb @ TG[a]))
                for a2 in ROOT:
                    Em[LIDX(x, mu, a2), site_index(x) * 2 + a] += v1[a2]
                    Em[LIDX(x, mu, a2), site_index(xp) * 2 + a] += v2[a2]
    return Em


def analyse(U, label):
    t1 = time.time()
    gS = grad_S(U)
    Hs, Hraw = hessian_root(U)
    asym = np.abs(Hraw - Hraw.T).max()
    del Hraw
    Dm = D_matrix(U)
    Mm, Dl, iota = M_and_level(U)
    # gauge invariance (full su(2) not needed: root lam, all gradient components)
    E = Hs @ Dm
    nl = iota.shape[1]
    KF = Hs + Dm @ Dm.T
    Delta = Dm.T @ Dm
    Ep = np.eye(NS * 2) - iota @ iota.T
    At = Hs + Mm.T @ Mm + Dm @ Ep @ Dm.T
    keep = np.where(np.abs(np.diag(Ep)) > 0.5)[0]
    Dp = Delta[np.ix_(keep, keep)]
    KinvM = np.linalg.solve(KF, Mm.T)
    KinvD = np.linalg.solve(KF, Dm @ iota)
    X = np.eye(Mm.shape[0]) + Mm @ KinvM
    b = Mm @ KinvD
    delta = np.eye(nl) - (Dm @ iota).T @ KinvD
    g = iota.T @ np.linalg.solve(Delta, iota)
    lA, sA = ld(At)
    lK, sK = ld(KF)
    lX, sX = ld(X)
    lB, sB = ld(delta + b.T @ np.linalg.solve(X, b))
    rel1 = abs(lA - (lK + lX + lB)) / abs(lA)
    lDp, _ = ld(Dp)
    lDe, _ = ld(Delta)
    lg, _ = ld(g)
    rel2 = abs(lDp - (lDe + lg)) / abs(lDp)
    cov = np.max(np.abs(Mm @ Dm - Dl @ iota.T))
    Ef = E_formula(U, gS)
    say(f"    [{label}] S = {S_wilson(U):.6e}, max|grad S| = {np.abs(gS).max():.3e}, max|H - H^T| (raw FD) = {asym:.2e}, signs (A, K_F, X, B) = {sA:+.0f}{sK:+.0f}{sX:+.0f}{sB:+.0f}, {time.time() - t1:.0f} s")
    say(f"    [{label}] log det A~ = {lA:.12e}; log det K_F + log det X + log det(delta + b^T X^-1 b) = {lK + lX + lB:.12e}")
    say(f"    [{label}] max|delta| = {np.abs(delta).max():.3e}, max|b - D_l g| = {np.abs(b - Dl @ g).max():.3e}, ||E||_F = {np.linalg.norm(E):.6e}, max|E - E_formula| = {np.abs(E - Ef).max():.3e} (max|E| = {np.abs(E).max():.3e})")
    # (T5) two-step chain: Lambda_1 = level sites, Lambda_2 = first level site
    lev_rows = np.where(np.abs(np.diag(iota @ iota.T)) > 0.5)[0]
    l2 = lev_rows[:2]
    keep2 = np.setdiff1d(np.arange(NS * 2), l2)
    lhs, _ = ld(Delta[np.ix_(keep2, keep2)])
    gi = np.linalg.inv(g)
    pos2 = [list(lev_rows).index(r) for r in l2]
    rest = np.setdiff1d(np.arange(nl), pos2)
    step1, _ = ld(gi[np.ix_(rest, rest)])
    rel6 = abs(lhs - (lDp + step1)) / abs(lhs)
    return dict(rel1=rel1, rel2=rel2, cov=cov, dmax=np.abs(delta).max(), bmax=np.abs(b - Dl @ g).max(),
                Enorm=np.linalg.norm(E), rel6=rel6, Ediff=np.abs(E - Ef).max())


def part_c():
    say("Part C (vector bordered identity; SU(2) root sector at Cartan backgrounds, torus 6x6x3x3, l = 3)")
    theta = (0.21, 0.13, 0.37, 0.29)
    eps, vth = 1e-3, 0.3
    rf = analyse(background(theta, 0.0, 0.0, 0.0), "flat twisted")
    r1 = analyse(background(theta, eps, 2 * np.pi / 6, vth), "plane wave p = 2pi/6")
    r2 = analyse(background(theta, eps, 4 * np.pi / 6, vth), "plane wave p = 4pi/6")
    verdict("C1 (T4) det identity, flat", rf["rel1"] <= 1e-9, f"rel = {rf['rel1']:.1e} (threshold 1e-9)")
    verdict("C1 (T4) det identity, plane wave", r1["rel1"] <= 1e-9, f"rel = {r1['rel1']:.1e} (threshold 1e-9)")
    verdict("C2 ghost Jacobi, plane wave", r1["rel2"] <= 1e-10, f"rel = {r1['rel2']:.1e} (threshold 1e-10)")
    verdict("C3 M D_U = D_l iota^T, plane wave", r1["cov"] <= 1e-12, f"max = {r1['cov']:.1e} (threshold 1e-12)")
    verdict("C4 delta = 0 at flat", rf["dmax"] <= 1e-7, f"max|delta| = {rf['dmax']:.1e} (threshold 1e-7)")
    verdict("C4 b = D_l g at flat", rf["bmax"] <= 1e-7, f"max|b - D_l g| = {rf['bmax']:.1e} (threshold 1e-7)")
    ratio = r2["Enorm"] / r1["Enorm"]
    verdict("C5 E_U = O(eps p^2) (S10-F4)", abs(ratio / 3.0 - 1) <= 1e-3, f"||E(4pi/6)||/||E(2pi/6)|| = {ratio:.8f} vs 3 (threshold 1e-3 rel)")
    verdict("C6 (T5) two-step ghost decimation, plane wave", r1["rel6"] <= 1e-10, f"rel = {r1['rel6']:.1e} (threshold 1e-10)")
    say(f"    [reported] max|E - E_formula|: flat {rf['Ediff']:.1e}, p = 2pi/6 {r1['Ediff']:.1e}, p = 4pi/6 {r2['Ediff']:.1e}; ||E||_F/eps = {r1['Enorm'] / eps:.6e}, {r2['Enorm'] / eps:.6e}")
    say(f"    [reported] defect sizes: max|delta| = {r1['dmax']:.3e} (2pi/6), {r2['dmax']:.3e} (4pi/6); max|b - D_l g| = {r1['bmax']:.3e}, {r2['bmax']:.3e}")


if __name__ == "__main__":
    say(f"f13 (lane C, session 10) start {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC; SMOKE = {SMOKE}")
    a0, hA = part_a()
    part_b(a0, hA)
    part_c()
    npass = sum(ok for _, ok in VERD)
    say(f"Summary: {npass}/{len(VERD)} verdict lines PASS; total {time.time() - T0:.0f} s")
