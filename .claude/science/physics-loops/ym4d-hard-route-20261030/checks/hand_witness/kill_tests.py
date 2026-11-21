#!/usr/bin/env python3
"""Kill tests for library/witness-by-hand.md. Criteria: CRITERIA.md, written first.

Evidence only. No step of the note rests on this script.
"""
from __future__ import annotations

import itertools
import json
import math
import os
import resource
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS: dict[str, object] = {}


def guard() -> None:
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = rss / 2**30 if sys.platform == "darwin" else rss / 2**20
    if rss > 2.0:
        sys.exit(f"RSS guard: {rss:.2f} GB")


def report(name: str, ok: bool, detail: str) -> None:
    RESULTS[name] = {"pass": bool(ok), "detail": detail}
    print(f"{name}: {'PASS' if ok else 'FAIL'}  {detail}", flush=True)


def rel(x, y) -> float:
    return float(abs(x - y) / max(abs(x), abs(y), 1e-300))


# ---------- W1, W2: the cubic form ----------

def increments(k, a, mu, nu):
    """e[s][i]: signed increment s of field i on the plaquette (0; mu, nu)."""
    e = np.zeros((4, 3), complex)
    for i in range(3):
        wm, wn = np.exp(1j * k[i][mu]), np.exp(1j * k[i][nu])
        e[0, i] = a[i][mu]
        e[1, i] = a[i][nu] * wm
        e[2, i] = -a[i][mu] * wn
        e[3, i] = -a[i][nu]
    return e


def V_def(e):
    P = e.sum(axis=0)
    return sum(np.linalg.det(np.stack([P, e[s], e[t]], axis=1))
               for s in range(4) for t in range(s + 1, 4))


def V_tri(e):
    return sum(np.linalg.det(np.stack([e[p], e[q], e[r]], axis=1))
               for p, q, r in itertools.combinations(range(4), 3))


def form(k, a):
    tot = 0j
    for i, j, l in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        pair = np.sum(a[i] * a[j] * np.cos(k[l] / 2))
        vec = np.sum(2 * np.sin((k[i] - k[j]) / 2) * a[l])
        tot += pair * vec
    return tot


def plane_formula(k, at, mu, nu):
    tot = 0j
    for i, j, l in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        tot += (at[i][mu] * at[j][mu] * np.cos(k[l][mu] / 2)
                * 2 * np.sin((k[i][nu] - k[j][nu]) / 2) * at[l][nu])
        tot += (at[i][nu] * at[j][nu] * np.cos(k[l][nu] / 2)
                * 2 * np.sin((k[i][mu] - k[j][mu]) / 2) * at[l][mu])
    return -2j * tot


def w1(rng):
    worst = dict(a=0.0, b=0.0, c=0.0, d=0.0)
    ctrl = []
    for _ in range(200):
        k1, k2 = rng.uniform(-np.pi, np.pi, (2, 4))
        k = [k1, k2, -k1 - k2]
        at = [rng.normal(size=4) + 1j * rng.normal(size=4) for _ in range(3)]
        a = [at[i] * np.exp(1j * k[i] / 2) for i in range(3)]
        total = 0j
        for mu in range(4):
            for nu in range(mu + 1, 4):
                e = increments(k, a, mu, nu)
                v = V_def(e)
                worst["a"] = max(worst["a"], rel(v, V_tri(e)))
                cyc = np.roll(e, 1, axis=0)
                rev = -e[::-1]
                worst["b"] = max(worst["b"], rel(v, V_def(cyc)), rel(v, V_def(rev)))
                worst["c"] = max(worst["c"], rel(v, plane_formula(k, at, mu, nu)))
                total += v
        worst["d"] = max(worst["d"], rel(total, -2j * form(k, at)))
        # W1e: same plane waves and increments, half angles of k^3 shifted by 2 pi in one slot
        ks = [k[0], k[1], k[2].copy()]
        ks[2][0] += 2 * np.pi
        ats = [a[i] * np.exp(-1j * ks[i] / 2) for i in range(3)]
        ctrl.append(rel(total, -2j * form(ks, ats)))
    report("W1a", worst["a"] < 1e-11, f"worst {worst['a']:.2e}")
    report("W1b", worst["b"] < 1e-11, f"worst {worst['b']:.2e}")
    report("W1c", worst["c"] < 1e-11, f"worst {worst['c']:.2e}")
    report("W1d", worst["d"] < 1e-11, f"worst {worst['d']:.2e}")
    report("W1e", float(np.median(ctrl)) > 1e-3, f"control median rel diff {np.median(ctrl):.2e}, must be large")


def bil(x, y):
    return np.sum(x * y)


def form_general(k, a1, a2, a3):
    return form(k, [a1, a2, a3])


def w2(rng):
    wa = wb = wc = 0.0
    eps = np.zeros((3, 3, 3))
    for p in itertools.permutations(range(3)):
        eps[p] = np.linalg.det(np.eye(3)[list(p)])
    for _ in range(200):
        k1, k2 = rng.uniform(-np.pi, np.pi, (2, 4))
        k = [k1, k2, -k1 - k2]
        kh = [2 * np.sin(q / 2) for q in k]
        D = [np.cos(q / 2) for q in k]
        Y12 = 2 * np.sin((k[0] - k[1]) / 2)
        wa = max(wa, float(np.max(np.abs(Y12 - (D[1] * kh[0] - D[0] * kh[1])))),
                 float(np.max(np.abs(kh[2] + D[1] * kh[0] + D[0] * kh[1]))),
                 abs(bil(Y12, kh[2]) - (bil(kh[1], kh[1]) - bil(kh[0], kh[0]))))
        for m in range(4):
            s = sum(np.cos(k[l][m] / 2) * np.sin((k[i][m] - k[j][m]) / 2)
                    for i, j, l in ((0, 1, 2), (1, 2, 0), (2, 0, 1)))
            wa = max(wa, abs(s))
        a1 = rng.normal(size=4) + 1j * rng.normal(size=4)
        a2 = rng.normal(size=4) + 1j * rng.normal(size=4)
        H = lambda q, a: bil(q, q) * a - q * bil(q, a)
        lhs = form_general(k, a1, a2, kh[2])
        rhs = bil(H(kh[1], a2), D[2] * a1) - bil(H(kh[0], a1), D[2] * a2)
        wb = max(wb, rel(lhs, rhs), abs(form_general(k, kh[0], kh[1], kh[2])))
        # (3.4)
        v = []
        for i in range(3):
            x = rng.normal(size=4) + 1j * rng.normal(size=4)
            x = x - kh[i] * bil(kh[i], x) / bil(kh[i], kh[i])
            v.append(x)
        u = [v[i] / bil(kh[i], kh[i]) for i in range(3)]
        h = [rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)) for _ in range(3)]
        def field(i, c, f):
            return (1.0 if c == f else 0.0) * u[i] + h[i][c, f] * kh[i]
        Z = 0j
        for a_, b_, c_ in itertools.permutations(range(3)):
            for f_, g_, h_ in itertools.permutations(range(3)):
                Z += (eps[a_, b_, c_] * eps[f_, g_, h_]
                      * form_general(k, field(0, a_, f_), field(1, b_, g_), field(2, c_, h_)))
        t = [np.trace(m) for m in h]
        am = lambda M, N: np.trace(M) * np.trace(N) - np.trace(M @ N)
        lam = [bil(v[0], D[2] * kh[1]), bil(v[1], D[0] * kh[2]), bil(v[2], D[1] * kh[0])]
        rhs = 6 * form_general(k, u[0], u[1], u[2])
        for i, j, l in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
            rhs += 2 * t[l] * bil(v[i], D[l] * v[j]) * (1 / bil(kh[i], kh[i]) - 1 / bil(kh[j], kh[j]))
            rhs -= am(h[j], h[l]) * lam[i]
        wc = max(wc, rel(Z, rhs))
    report("W2a", wa < 1e-11, f"worst {wa:.2e}")
    report("W2b", wb < 1e-10, f"worst {wb:.2e}")
    report("W2c", wc < 1e-9, f"worst {wc:.2e}")


# ---------- W3: Theorem S ----------

def kgrid(N=400001, scale=1.0):
    """k = scale tan(theta / 2): trapezoid on theta, exponentially accurate for smooth decay."""
    th = (np.arange(N) + 0.5) / N * 2 * np.pi - np.pi
    k = scale * np.tan(th / 2)
    dk = (2 * np.pi / N) * scale / (2 * np.cos(th / 2) ** 2)
    return k, dk


def w3(rng):
    c0 = 0.7
    ws = np.array([0.4, 1.1, 2.5, 7.0])
    cs = np.array([0.9, 0.3, 1.7, 2.2])
    def D(k):
        return c0 + np.sum(cs[:, None] * 2 * ws[:, None] / (ws[:, None] ** 2 + k ** 2), axis=0)
    k, dk = kgrid()
    Dk = D(k)
    wa = wb = wc = 0.0
    for _ in range(30):
        z, zp = rng.uniform(0.3, 4, 2) + 1j * rng.uniform(-3, 3, 2)
        lhs = np.sum(Dk / ((z + 1j * k) * (zp + 1j * k)) * dk) / (2 * np.pi)
        rhs = np.sum(cs / ((z + ws) * (zp + ws)))
        wa = max(wa, rel(lhs, rhs))
        E = np.sum(Dk * z / (z ** 2 + k ** 2) * dk) / (2 * np.pi)
        wb = max(wb, rel(E, c0 / 2 + np.sum(cs / (z + ws))))
        v, x = rng.uniform(0.2, 3), rng.uniform(-3, 3)
        # shift the grid centre to the Poisson peak
        k2 = k * v + x
        dk2 = dk * v
        U = np.sum(D(k2) * (v / np.pi) / (v ** 2 + (x - k2) ** 2) * dk2)
        cf = c0 + np.sum(cs * 2 * (v + ws) / ((v + ws) ** 2 + x ** 2))
        wc = max(wc, rel(U, cf))
    report("W3a", wa < 1e-7, f"worst {wa:.2e}")
    report("W3b", wb < 1e-7, f"worst {wb:.2e}")
    report("W3c", wc < 1e-6, f"worst {wc:.2e}")

    # W3d: full D, contact included. psi-hat(k) = 1 / (1 + i k), a = 0.5. For a > 0 the contact
    # term gives c_0 (psi * psi)(-a) = 0, so the atoms alone must reproduce the integral.
    a = 0.5
    N = 2 ** 22
    Kmax = 4000.0
    kk = (np.arange(N) - N / 2 + 0.5) * (2 * Kmax / N)
    dkk = 2 * Kmax / N
    lhs = np.sum(np.exp(-1j * kk * a) * D(kk) / (1 + 1j * kk) ** 2) * dkk / (2 * np.pi)
    rhs = np.sum(cs * np.exp(-ws * a) / (1 + ws) ** 2)
    diff = rel(lhs, rhs)
    report("W3d", diff < 1e-5, f"lhs {lhs.real:.8e} imag {lhs.imag:.1e}, atoms {rhs:.8e}, rel {diff:.2e}")

    # W3e: sign of the longitudinal test, time domain against Fourier
    m = 1.3
    w0 = 1.9
    sig = 0.15
    t0 = 3.0
    # Laplace and Fourier transforms of the Gaussian bump phi(t) = exp(-(t - t0)^2 / (2 sig^2))
    phit = lambda w: sig * np.sqrt(2 * np.pi) * np.exp(-w * t0 + w ** 2 * sig ** 2 / 2)
    time_form = (m ** 2 / (2 * w0)) * (w0 ** 2 * phit(w0) ** 2 - m ** 2 * phit(w0) ** 2)
    N = 2 ** 22
    Kmax = 200.0 / sig
    kk = (np.arange(N) - N / 2 + 0.5) * (2 * Kmax / N)
    dkk = 2 * Kmax / N
    ph = sig * np.sqrt(2 * np.pi) * np.exp(-1j * kk * t0 - kk ** 2 * sig ** 2 / 2)
    four = -m ** 2 * np.sum((kk ** 2 + m ** 2) / (kk ** 2 + w0 ** 2) * ph ** 2) * dkk / (2 * np.pi)
    d = rel(time_form, four.real)
    report("W3e", d < 1e-6, f"time {time_form:.6e}, Fourier {four.real:.6e}, rel {d:.2e}")

    # W3f: Hankel form of exp(-k^2): K(tau) = exp(-tau^2 / 4) / (2 sqrt(pi))
    tgrid = np.linspace(0.05, 6, 160)
    K = np.exp(-((tgrid[:, None] + tgrid[None, :]) ** 2) / 4) / (2 * np.sqrt(np.pi))
    ev = np.linalg.eigvalsh(K)
    report("W3f", ev[0] < -1e-6 * ev[-1], f"lowest {ev[0]:.3e}, top {ev[-1]:.3e}")


# ---------- W4: clip and the free bound ----------

def w4(rng):
    n = 2_000_000
    z = rng.normal(size=(n, 3))
    chi = np.sum(z ** 2, axis=1)
    m4 = float(np.mean(chi ** 4))
    ok = abs(m4 - 945) / 945 < 0.02
    worst = -np.inf
    # correlated colours, P = 1, rho = 0.6, X = (1 / 2) P chi^2_3
    z2 = 0.6 * z + 0.8 * rng.normal(size=(n, 3))
    X, Xp = 0.5 * np.sum(z ** 2, axis=1), 0.5 * np.sum(z2 ** 2, axis=1)
    cov = lambda a, b: float(np.mean(a * b) - np.mean(a) * np.mean(b))
    for r in (1, 2):
        ms = float(max(np.mean(X ** (2 + r)), np.mean(Xp ** (2 + r))))
        for b in (2.0, 5.0, 10.0, 20.0):
            Y, Yp = np.minimum(X, b), np.minimum(Xp, b)
            delta = abs(cov(Y, Yp) - cov(X, Xp))
            bound = 2 * ms * b ** (-r)
            worst = max(worst, delta / bound)
    report("W4a", ok and worst <= 1.0, f"E chi^8 = {m4:.1f}, worst Delta / bound = {worst:.3f}")

    good = True
    for nn in (1, 3, 5, 7):
        # (a, b) plane: x runs over the n^2 values in the plane; square(x) has side n
        count = np.zeros((3 * nn, 3 * nn))
        for xa in range(nn):
            for xb in range(nn):
                count[xa:xa + nn, xb:xb + nn] += 1
        # transverse: x_c, x_d fixed to p_c, p_d, so n^2 transverse plaquette positions, each with this table
        table = count / nn ** 4
        total = table.sum() * nn ** 2
        good = good and table.max() <= nn ** -2 + 1e-15 and abs(total - nn ** 2) < 1e-9
    report("W4b", good, "w_p <= n^-2, sum w_p = n^2 at n = 1, 3, 5, 7")

    out = {}
    fine = True
    for nn, S in ((1, 6), (1, 8), (3, 6), (3, 8), (5, 6)):
        N = nn * S
        grid = (2 * np.pi / S) * (np.arange(N) - N // 2)
        p = np.meshgrid(grid, grid, grid, grid, indexing="ij", sparse=True)
        def sn(u):
            with np.errstate(divide="ignore", invalid="ignore"):
                val = np.sin(u / 2) / (nn * np.sin(u / (2 * nn)))
            return np.where(np.abs(np.sin(u / (2 * nn))) < 1e-14, 1.0, val)
        s = [sn(q) for q in p]
        prod = s[0] * s[1] * s[2] * s[3]
        lam = 4 * nn ** 2 * sum(np.sin(q / (2 * nn)) ** 2 for q in p)
        j1 = np.abs(s[0] * prod) ** 2 * np.abs(1 - np.exp(-1j * p[1])) ** 2
        j2 = np.abs(s[1] * prod) ** 2 * np.abs(1 - np.exp(-1j * p[0])) ** 2
        with np.errstate(divide="ignore", invalid="ignore"):
            term = np.where(lam > 1e-12, (j1 + j2) / lam, 0.0)
        val = float(np.sum(term) / S ** 4)
        out[f"n{nn}_S{S}"] = val
        fine = fine and val <= 1.0
        guard()
    near = abs(out["n1_S8"] - 0.5) < 0.05
    report("W4c", fine and near, json.dumps(out))


# ---------- W5: the order of choice ----------

def w5():
    bad = 0
    for A, al, r, a0, Ap, alp, Cs, kap, Ms in (
        (3.0, 2.0, 8.0, 1e-3, 2.0, 1.0, 1.0, 0.5, 5.0),
        (50.0, 4.0, 2.0, 1e-5, 9.0, 3.0, 2.0, 0.25, 40.0),
        (1.0, 0.5, 1.0, 1e-2, 0.5, 0.0, 1.0, 1.0, 1.0),
    ):
        B1 = max(1.0, (8 * A / a0) ** (2 / r))
        gam = 2 * al / r + 2 * alp
        B = 7.5 * B1 * (2 + 3 * Ap) * Ap * Cs ** 2 * Ms
        m = math.ceil(gam) + 1
        t1 = max(1.0, 4 * B * 2 ** gam * math.factorial(m) * (2 * kap) ** (-m) / a0)
        for t in np.geomspace(t1, 1e4 * t1, 200):
            logL = float(t)
            b = max(1.0, (8 * A / a0) ** (1 / r) * (1 + logL) ** (al / r))
            tau2 = 2 * A * (1 + logL) ** al * b ** (-r)
            Cn = Ap * (1 + logL) ** alp
            # log of the smoothing error, to avoid overflow
            lerr = (math.log(7.5) + 2 * math.log(b) + math.log(2 + 3 * Cn) + math.log(Cn)
                    + 2 * math.log(Cs) + math.log(Ms) - 2 * kap * logL)
            if tau2 > a0 / 4 * (1 + 1e-12) or lerr > math.log(a0 / 4) + 1e-12:
                bad += 1
    report("W5", bad == 0, f"{bad} violations")


def main():
    rng = np.random.default_rng(20261101)
    w1(rng)
    guard()
    w2(rng)
    guard()
    w3(rng)
    guard()
    w4(rng)
    guard()
    w5()
    with open(os.path.join(HERE, "kill_tests.json"), "w") as fh:
        json.dump(RESULTS, fh, indent=1)
    bad = [k for k, v in RESULTS.items() if not v["pass"]]
    print("FAILED:", bad if bad else "none")


if __name__ == "__main__":
    main()
