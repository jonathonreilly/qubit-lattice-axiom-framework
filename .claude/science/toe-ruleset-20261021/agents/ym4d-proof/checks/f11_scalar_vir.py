"""f11 (lane C, session 8): scalar proxy for (V-IR) at n = 1, 2 with the S4' axial transporters, and Theorem G-mag (vi)'s c'_0.

Criteria: checks/f11_criteria.md (written before this script). FLOW.md §57 (Q3), (Q4).
Run:  OMP_NUM_THREADS=1 ... nice -n 10 python3 f11_scalar_vir.py > f11_out.txt
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import re
import time
import numpy as np
from scipy.special import ive
from scipy import integrate

HERE = os.path.dirname(os.path.abspath(__file__))
SMOKE = os.environ.get("F11_SMOKE") == "1"
L = 3
S = 4.0
CG = 1.0 / (96 * np.pi ** 2)
T0 = time.time()
VERD = []


def say(*a):
    print(*a, flush=True)


def verdict(name, ok, detail):
    VERD.append((name, ok))
    say(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ------------------------------------------------------------------ 4D direct torus (independent builder, link table)
def sites4(dims):
    return list(itertools.product(*[range(d) for d in dims]))


def idx4(x, dims):
    i = 0
    for c in range(4):
        i = i * dims[c] + (x[c] % dims[c])
    return i


def landau_links4(dims, f):
    """U[site, mu] = forward link from site; Landau gauge U_{x,2} = e^{i f x1}, x1-wrap link e^{-i f N1 x2}."""
    V = int(np.prod(dims))
    U = np.ones((V, 4), complex)
    for x in sites4(dims):
        i = idx4(x, dims)
        U[i, 1] = np.exp(1j * f * x[0])
        if x[0] == dims[0] - 1:
            U[i, 0] = np.exp(-1j * f * dims[0] * x[1])
    return U


def lap4(U, dims):
    V = int(np.prod(dims))
    H = np.zeros((V, V), complex)
    for x in sites4(dims):
        i = idx4(x, dims)
        H[i, i] += 8.0
        for mu in range(4):
            xp = list(x); xp[mu] += 1
            j = idx4(xp, dims)
            H[i, j] += -U[i, mu]
            H[j, i] += -np.conj(U[i, mu])
    return H


def path4(U, dims, start, end, order):
    z = list(start); ph = 1.0 + 0j
    for mu in order:
        while z[mu] != end[mu]:
            if end[mu] > z[mu]:
                ph *= U[idx4(z, dims), mu]; z[mu] += 1
            else:
                z[mu] -= 1; ph *= np.conj(U[idx4(z, dims), mu])
    return ph


def avg4(U, dims, phases=True):
    """Q_0 in 4D, L = 3, 24 orders; level-1 sites X, centre 3X + 1."""
    cd = [d // L for d in dims]
    Nc = int(np.prod(cd)); V = int(np.prod(dims))
    M = np.zeros((Nc, V), complex)
    orders = list(itertools.permutations(range(4)))
    for X in sites4(cd):
        c = [L * X[m] + 1 for m in range(4)]
        ic = idx4(X, cd)
        for jv in itertools.product(range(L), repeat=4):
            y = [L * X[m] + jv[m] for m in range(4)]
            w = np.mean([path4(U, dims, c, y, o) for o in orders]) if phases else 1.0
            M[ic, idx4(y, dims)] += L ** -4 * w
    return M


def gs_direct4(U, dims, M, C):
    H = lap4(U, dims)
    K = H + (M.conj().T @ M) / C
    sgn, ld = np.linalg.slogdet(K)
    return (ld.real + M.shape[0] * np.log(C)) / H.shape[0]


# ------------------------------------------------------------------ 2D reduced machinery (analytic Landau phases)
def harper2d(a, b, f, th1, th2):
    n = a * b
    H = np.zeros((n, n), complex)
    for x1 in range(a):
        for x2 in range(b):
            i = x1 * b + x2
            H[i, i] += 4.0
            if x1 + 1 < a:
                j, ph = (x1 + 1) * b + x2, 1.0
            else:
                j, ph = x2, np.exp(1j * th1) * np.exp(-1j * f * a * x2)
            H[i, j] += -ph; H[j, i] += -np.conj(ph)
            if x2 + 1 < b:
                j, ph = x1 * b + x2 + 1, np.exp(1j * f * x1)
            else:
                j, ph = x1 * b, np.exp(1j * f * x1) * np.exp(1j * th2)
            H[i, j] += -ph; H[j, i] += -np.conj(ph)
    return H


def link2(z, mu, f):
    return 1.0 if mu == 0 else np.exp(1j * f * z[0])


def path2(start, end, order, f):
    z = list(start); ph = 1.0 + 0j
    for mu in order:
        while z[mu] != end[mu]:
            if end[mu] > z[mu]:
                ph *= link2(z, mu, f); z[mu] += 1
            else:
                z[mu] -= 1; ph *= np.conj(link2(z, mu, f))
    return ph


def q_level2(a, b, k, f, orders):
    """Q_k in the plane 12 (weight L^-2, order average over 'orders'); rows level-(k+1) sites, cols level-k sites."""
    sk, sk1 = L ** k, L ** (k + 1)
    ok, ok1 = (sk - 1) // 2, (sk1 - 1) // 2
    nk = (a // sk, b // sk); nk1 = (a // sk1, b // sk1)
    Q = np.zeros((nk1[0] * nk1[1], nk[0] * nk[1]), complex)
    for Y1 in range(nk1[0]):
        for Y2 in range(nk1[1]):
            c = (sk1 * Y1 + ok1, sk1 * Y2 + ok1)
            for j1 in range(L):
                for j2 in range(L):
                    X = (L * Y1 + j1, L * Y2 + j2)
                    y = (sk * X[0] + ok, sk * X[1] + ok)
                    w = np.mean([path2(c, y, o, f) for o in orders])
                    Q[Y1 * nk1[1] + Y2, X[0] * nk[1] + X[1]] = L ** -2 * w
    return Q


def chain2(a, b, n, f, orders=((0, 1), (1, 0))):
    Qs = [q_level2(a, b, k, f, orders) for k in range(n)]
    M = Qs[0]
    for k in range(1, n):
        M = Qs[k] @ M
    C = 0.0; diag_dev = 0.0; offd = 0.0
    for j in range(1, n + 1):
        A = np.eye(Qs[-1].shape[0], dtype=complex)
        for k in range(n - 1, j - 1, -1):
            A = A @ Qs[k]
        AA = A @ A.conj().T
        dg = np.real(np.diag(AA))
        diag_dev = max(diag_dev, np.max(np.abs(dg - dg[0])) / dg[0])
        offd = max(offd, np.max(np.abs(AA - np.diag(np.diag(AA)))))
        C += dg[0] * L ** (-2 * (n - j)) / (S * L ** (2 * j))
    return M, C, diag_dev, offd


def c_closed(n, f):
    h = (L - 1) // 2
    ms = np.arange(-h, h + 1)
    def Nk(k):
        return L ** -2 * np.sum(np.cos(f * L ** (2 * k) * np.outer(ms, ms) / 2) ** 2)
    return sum(L ** (-4 * (n - j)) / (S * L ** (2 * j)) * np.prod([Nk(k) for k in range(j, n)]) for j in range(1, n + 1))


def alias34(l, th3, th4):
    m = np.arange(l)
    p3 = (th3 + 2 * np.pi * m) / l; p4 = (th4 + 2 * np.pi * m) / l
    def D2(p):
        x = np.arange(l)
        return np.abs(np.exp(-1j * np.outer(p, x)).sum(1) / l) ** 2
    lam = (2 - 2 * np.cos(p3))[:, None] + (2 - 2 * np.cos(p4))[None, :]
    w = D2(p3)[:, None] * D2(p4)[None, :]
    return lam.ravel(), w.ravel()


def fibre(e, MV, lam, w, C, l):
    den = e[:, None] + lam[None, :]
    gpart = np.log(den).sum()
    r = (w[None, :] / den).sum(1)
    G = (MV * r[None, :]) @ MV.conj().T
    sg, ld = np.linalg.slogdet(C * np.eye(G.shape[0]) + G / l ** 2)
    return gpart, ld.real


def grid(K, shifted):
    return [2 * np.pi * (i + (0.5 if shifted else 0.0)) / K for i in range(K)]


def D_bloch(n, a, b, f, K1, K2, Kt, shifted=True, orders=((0, 1), (1, 0))):
    l = L ** n
    M, C, _, _ = chain2(a, b, n, f, orders)
    al = [alias34(l, t3, t4) for t3 in grid(Kt, shifted) for t4 in grid(Kt, shifted)]
    gs = es = 0.0; cnt = 0
    for t1 in grid(K1, shifted):
        for t2 in grid(K2, shifted):
            e, Vv = np.linalg.eigh(harper2d(a, b, f, t1, t2))
            MV = M @ Vv
            for lam, w in al:
                g_, e_ = fibre(e, MV, lam, w, C, l)
                gs += g_; es += e_; cnt += 1
    norm = cnt * a * b * l * l
    return (gs + es) / norm, gs / norm, es / norm


# ------------------------------------------------------------------ Part R
def part_r():
    say("Part R (implementation identities)")
    rng = np.random.default_rng(11)
    dims = (6, 6, 3, 3); f = 2 * np.pi / 36
    U = landau_links4(dims, f)
    M4 = avg4(U, dims)
    C1 = 1.0 / (S * L ** 2)
    g4 = gs_direct4(U, dims, M4, C1)
    # reduced: 12 cell = (6, 6) torus, theta12 = 0; 34 torus 3 x 3 = one cell, theta34 = 0
    def red(orders):
        M2, C2, _, _ = chain2(6, 6, 1, f, orders)
        e, Vv = np.linalg.eigh(harper2d(6, 6, f, 0.0, 0.0))
        lam, w = alias34(3, 0.0, 0.0)
        g_, e_ = fibre(e, M2 @ Vv, lam, w, C2, 3)
        return (g_ + e_) / (36 * 9), C2
    gr, C2 = red(((0, 1), (1, 0)))
    verdict("R1 reduction (4D 24 orders vs 2D reduced)", abs(g4 - gr) <= 1e-12 and abs(C2 - c_closed(1, f)) <= 1e-13,
            f"G_S direct = {g4:.15f}, reduced = {gr:.15f}, |diff| = {abs(g4 - gr):.1e}; |C_1 - closed| = {abs(C2 - c_closed(1, f)):.1e}")
    gctl, _ = red(((0, 1),))
    verdict("R1-ctl (one order only; must FAIL R1)", abs(g4 - gctl) >= 1e-6, f"|diff| = {abs(g4 - gctl):.2e}")
    # R2 gauge covariance
    V = U.shape[0]
    gph = np.exp(1j * rng.uniform(0, 2 * np.pi, V))
    Ug = U.copy()
    for x in sites4(dims):
        i = idx4(x, dims)
        for mu in range(4):
            xp = list(x); xp[mu] += 1
            Ug[i, mu] = gph[i] * U[i, mu] * np.conj(gph[idx4(xp, dims)])
    g4g = gs_direct4(Ug, dims, avg4(Ug, dims), C1)
    verdict("R2 gauge covariance", abs(g4g - g4) <= 1e-12, f"|Delta G_S| = {abs(g4g - g4):.1e}")
    Mp = avg4(U, dims, phases=False)
    dctl = abs(gs_direct4(Ug, dims, Mp, C1) - gs_direct4(U, dims, Mp, C1))
    verdict("R2-ctl (no transport phases; must FAIL R2)", dctl >= 1e-3, f"|Delta G_S| = {dctl:.2e}")
    # R3 Bloch vs direct 2D torus
    a, b = 12, 3
    eb = np.sort(np.concatenate([np.linalg.eigvalsh(harper2d(a, b, f, t1, t2)) for t1 in grid(2, False) for t2 in grid(2, False)]))
    ed = np.sort(np.linalg.eigvalsh(harper2d(24, 6, f, 0.0, 0.0)))
    Db = D_bloch(1, a, b, f, 2, 2, 2, shifted=False)[0]
    Dd = D_bloch(1, 24, 6, f, 1, 1, 2, shifted=False)[0]
    verdict("R3 Bloch vs direct 2D torus", np.max(np.abs(eb - ed)) <= 1e-11 and abs(Db - Dd) <= 1e-11,
            f"spectra {np.max(np.abs(eb - ed)):.1e}, G_S {abs(Db - Dd):.1e}")
    # R4 composite covariance
    worst = 0.0; offd = 0.0; dd = 0.0
    for n in (1, 2):
        l = L ** n; fq = 2 * np.pi / (l * l * 8)
        _, C, dg, od = chain2(l * 8, l, n, fq)
        worst = max(worst, abs(C / c_closed(n, fq) - 1)); offd = max(offd, od); dd = max(dd, dg)
        say(f"    n = {n}: C_n = {C:.15e}, closed = {c_closed(n, fq):.15e}")
    verdict("R4 composite covariance", worst <= 1e-13 and offd <= 1e-14 and dd <= 1e-13,
            f"max rel |C - closed| = {worst:.1e}, offdiag = {offd:.1e}, diag spread = {dd:.1e}")


# ------------------------------------------------------------------ Part S
def m_of(t):
    return (t * t / 3) * ive(1, 2 * t) ** 2 * ive(0, 2 * t) ** 2


def cfrak_S(T):
    return 0.5 * integrate.quad(lambda u: m_of(np.exp(u)), -40, np.log(T), limit=400, epsabs=1e-15, epsrel=1e-13)[0]


def part_s():
    say("Part S (scalar proxy, s = 4, L = 3; D = G_S per fine site)")
    Qps = [8, 12] if SMOKE else [8, 12, 16, 24, 32]
    res = {}
    for n in (1, 2):
        l = L ** n
        Nt = (24 if n == 1 else 54) if SMOKE else (60 if n == 1 else 144)
        def ks(a, b, fac=1.0):
            N = Nt * fac
            return max(1, int(np.ceil(N / a))), int(np.ceil(N / b)), int(np.ceil(N / l))
        t1 = time.time()
        a0, b0 = l * 8, l
        D0 = D_bloch(n, a0, b0, 0.0, *ks(a0, b0))
        D0b = D_bloch(n, a0, b0, 0.0, *ks(a0, b0, 1.5))
        f8 = 2 * np.pi / (l * l * 8)
        D8b = D_bloch(n, a0, b0, f8, *ks(a0, b0, 1.5))
        fs, Ds, gs, es = [], [], [], []
        for Qp in Qps:
            a, b = l * Qp, l
            f = 2 * np.pi / (l * l * Qp)
            d, g_, e_ = D_bloch(n, a, b, f, *ks(a, b))
            fs.append(f); Ds.append(d); gs.append(g_); es.append(e_)
            say(f"    n = {n}, Q' = {Qp:2d}: Phi = {2 * np.pi / Qp:.5f}, f = {f:.6e}, D - D0 = {d - D0[0]:.12e}")
        gerr = max(abs(D0[0] - D0b[0]), abs(Ds[0] - D8b[0]))
        verdict(f"S-grid (n = {n})", gerr <= 1e-10, f"|D(grid) - D(1.5 grid)| = {gerr:.1e} (f = 0 and Q' = 8)")
        fs = np.array(fs); y = np.array(Ds) - D0[0]
        fm = fs.max(); z = fs / fm  # scaled columns (conditioning); coefficients rescaled by fm^-2
        A3 = np.vstack([z ** 2, z ** 4, z ** 6]).T
        a1 = np.linalg.lstsq(A3, y, rcond=None)[0][0] / fm ** 2
        Al = np.vstack([z ** 2, z ** 2 * np.log(1 / fs), z ** 4]).T
        bfit = np.linalg.lstsq(Al, y, rcond=None)[0] / fm ** 2
        verdict(f"S-IR (n = {n})", abs(bfit[1]) <= 0.1 * CG, f"f^2 log(1/f) coefficient b = {bfit[1]:.3e} (c_g = {CG:.3e})")
        if len(fs) >= 5:
            aL = np.linalg.lstsq(A3[:4], y[:4], rcond=None)[0][0] / fm ** 2
            aS = np.linalg.lstsq(A3[1:], y[1:], rcond=None)[0][0] / fm ** 2
            verdict(f"S-stab (n = {n})", abs(aL - aS) <= 0.01 * abs(a1), f"a1 (4 largest) = {aL:.6e}, (4 smallest) = {aS:.6e}")
        for nm, arr in (("g", gs), ("E", es)):
            ref = (D0[1] if nm == "g" else D0[2])
            bb = np.linalg.lstsq(Al, np.array(arr) - ref, rcond=None)[0][1] / fm ** 2
            say(f"    piece {nm}: f^2 log(1/f) coefficient = {bb:.3e} ({bb / CG:+.3f} c_g)  [reported]")
        cf = cfrak_S(l * l)
        rho = a1 - 2 * CG * np.log(l)
        say(f"    n = {n}: c^S_n = {a1:.6e}, rho_n = c^S_n - 2 c_g log l = {rho:.6e}, c^S_n - cfrak^S(l^2) = {a1 - cf:.6e}  ({time.time() - t1:.0f} s)")
        res[n] = a1
    ratio = (res[2] - res[1]) / (2 * CG * np.log(L))
    verdict("S-VIR (prediction)", abs(ratio - 1) <= 0.25, f"(c^S_2 - c^S_1)/(2 c_g log 3) = {ratio:.4f}")


# ------------------------------------------------------------------ Part G
def cprime0(eps=1e-12, ucut=np.log(1e6)):
    """kappa_0 by quadrature in u = log t up to t = e^ucut, then the tail -m_inf/(4T) (m - m_inf = -m_inf/(4t) + O(t^-2));
    scipy's ive is not usable beyond t ~ 1e9. I_b in u = log s up to s = e^20, tail 1/(2 S^2)."""
    mi = 1.0 / (48 * np.pi ** 2)
    k1 = integrate.quad(lambda u: m_of(np.exp(u)), -60, 0, limit=400, epsabs=eps * 1e-3, epsrel=eps)[0]
    k2 = integrate.quad(lambda u: m_of(np.exp(u)) - mi, 0, ucut, limit=800, epsabs=eps * 1e-3, epsrel=eps)[0]
    k2 += -mi / (4 * np.exp(ucut))
    kappa0 = k1 + k2
    def ssh(s):
        return 2 * s * np.exp(-s) / (1 - np.exp(-2 * s))
    def fa(s):
        if s < 0.05:
            return 7 * s / 360 - 31 * s ** 3 / 15120
        return (s * s / 6 - 1 + ssh(s)) / s ** 3
    Ia = integrate.quad(fa, 0, 1, epsabs=eps * 1e-3, epsrel=eps)[0]
    Ib = integrate.quad(lambda u: (1 - ssh(np.exp(u))) * np.exp(-2 * u), 0, 20, limit=400, epsabs=eps * 1e-3, epsrel=eps)[0]
    Ib += 0.5 * np.exp(-40.0)
    return 0.5 * kappa0 - Ia / (16 * np.pi ** 2) + Ib / (16 * np.pi ** 2), kappa0, Ia, Ib


def part_g():
    say("Part G (Theorem G-mag (vi): c'_0 by quadrature vs f9 G2)")
    c0, k0, Ia, Ib = cprime0()
    c0b = cprime0(eps=1e-13, ucut=np.log(1e7))[0]
    say(f"    kappa_0 = {k0:.12e}, I_a = {Ia:.12e}, I_b = {Ib:.12e}, c'_0 = {c0:.12e}")
    verdict("G-acc", abs(c0 - c0b) <= 1e-9, f"|change| = {abs(c0 - c0b):.1e}")
    ext = 1.387447087e-3 - 1.556e-6 * 0.509 / 0.491
    verdict("G-c0 (prediction)", abs(c0 - 1.38583e-3) <= 5e-6, f"c'_0 = {c0:.6e} vs f9 extrapolation {ext:.6e}: |diff| = {abs(c0 - ext):.1e}")
    try:
        txt = open(os.path.join(HERE, "f9_out.txt")).read()
        rows = re.findall(r"Q =\s+(\d+): phi = ([0-9.]+), psi = [0-9.e+-]+, c' = ([0-9.e+-]+)", txt)
        for Q, ph, cp in rows:
            say(f"    f9 Q = {int(Q):3d}: phi = {float(ph):.5f}, c'(phi) - c'_0 = {float(cp) - c0:+.3e}, /phi = {(float(cp) - c0) / float(ph):+.3e}")
    except OSError as exc:
        say(f"    f9_out.txt not read: {exc}")


if __name__ == "__main__":
    say(f"f11 (lane C, session 8) start {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC; SMOKE = {SMOKE}")
    part_g()
    part_r()
    part_s()
    npass = sum(ok for _, ok in VERD)
    say(f"Summary: {npass}/{len(VERD)} verdict lines PASS (controls are lines that must FAIL their test and PASS here when they do)")
    say("  " + "; ".join(f"{nm}: {'PASS' if ok else 'FAIL'}" for nm, ok in VERD))
    say(f"elapsed {time.time() - T0:.1f} s")
