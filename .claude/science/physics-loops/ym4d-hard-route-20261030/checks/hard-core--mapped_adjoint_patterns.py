#!/usr/bin/env python3
"""Lemma AD of `library/composite-adjoint.md` on fields that are not constant flux. Consumer: (R3), (SB) at order 1.

Written before running. `hard-core--mapped_adjoint.py` tested constant flux only, where concentration cannot occur. The lemma's proof rests on an exact expansion of Q^o at a background:

 Res := Q^o - P_U,   P_U theta (c) := avg_x (legs of the line of x, with their exact transport),
 Res = avg_x (Ad(V') - Ad(Omega_x)) cs'_x + avg_x E_x [eps_x] + G_0 [eps_0],

with cs'_x the contour sum at y' to x', E_x := dexp(A) ell(v_x) - 1, and G_0 := e^{i A} - avg_x (1 + E_x) e^{i v_x}, on charged components at a Cartan background. So, for each parent c and bond b,

 (W)  |Res[c, b]| <= C_w ( L^{-2} sum_{x : b in path_x} ( |v_x - A| + v_x^2 + A^2 ) + avg_x v_x^2 1(b in path_0) ),   d = 2.

The first-order terms of E_x and of G_0 are of size |v_x - A|, zero respectively: that cancellation is the content of (W).

Then the proof bounds the l^2 norm of the right side by Hoelder against the plaquette angles:

 (N)  ||Res||_{2 -> 2} <= C_N L^2 max_B E(B),  E(B)^4 := sum over plaquettes p in B and its two neighbours along each axis of theta_p^4, with theta_p the adjoint angle.

Fields: fine links with charged phases u, not critical. Kinds:
 random: independent Gaussian phases of size amp on all bonds, so plaquette angles of size about 2 amp, with no smoothness.
 strip: u_1(x_0) with plaquette angle +f on the column of block centres and -f on a column next to it, so all flux sits next to the axis of the comb: the concentrated case.
 far: the same, with the columns as far from the centres as possible.
 smooth: plaquette angle f cos(2 pi x_0 / N) cos(2 pi x_1 / N), roughly.
Amplitudes: chosen so that the largest |v_x| over all parents is about 0.1 and about 0.3. L = 3, 5, 7, 9; nc = 4.

PRE-STATED criteria.
 W1. (W) holds with C_w = 3 on every case, for every c and b.
 W2. Control: at v = 0 (amp = 0) ||Res|| <= 1e-12.
 W3. Control on (W): if the term |v_x - A| is replaced by the bound with |v_x - A| removed, (W) fails on some case. Otherwise (W) has no power; reported.
 N1. (N) holds with C_N = 1 on every case.
 N2. Reported: R := ||Res|| / (L^2 max_B E(B)) by kind and L, and the kind that maximises it.
FAIL if W1, W2 or N1 fails.

Limits. d = 2, one level, Cartan background. In d = 2 the bound (N) is not sharp: the case that saturates it needs d = 4, where a stage-one ladder has L^2 plaquettes in a block of L^4. RSS guard 2 GB.
"""
import importlib.util
import os
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sharp_lam", os.path.join(HERE, "hard-core--mapped_sharp_lam.py"))
lam = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lam)
sh = lam.sh
tp = sh.tp
RealBg = tp.Bg


def make_field(L, nc, kind, amp, rng):
    g = RealBg(L, nc, 0)
    N, h = g.N, g.h
    u = np.ones((2, N, N), dtype=complex)
    if kind == "random":
        u = np.exp(1j * amp * rng.standard_normal((2, N, N)))
    else:
        col = np.zeros(N)
        if kind == "strip":
            for i in range(nc):
                col[(h + L * i) % N] = amp
                col[(h + L * i + 1) % N] = -amp
        elif kind == "far":
            for i in range(nc):
                col[(L * i) % N] = amp
                col[(L * i + L - 2) % N] = -amp
        elif kind == "smooth":
            col = amp * np.cos(2 * np.pi * np.arange(N) / N)
        phi = np.concatenate([[0.0], np.cumsum(col)[:-1]])
        for x0 in range(N):
            for x1 in range(N):
                u[1, x0, x1] = np.exp(1j * phi[x0])
    g.u = u
    return g


def build(g, L, nc):
    tp.Bg = lambda L_, nc_, m_: g
    try:
        out = sh.build_sharp(L, nc, 0)
    finally:
        tp.Bg = RealBg
    return out


def analyse(g, L, nc):
    g, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres = build(g, L, nc)
    N, h = g.N, g.h
    nb = 2 * N * N
    P = np.zeros_like(Qo)
    Wb = np.zeros((Qo.shape[0], nb))
    Wn = np.zeros((Qo.shape[0], nb))
    vmax = 0.0
    for i in range(nc):
        for j in range(nc):
            y0 = (h + L * i, h + L * j)
            for mu in range(2):
                c = i * nc + j + mu * nc * nc
                data = {}
                for r0 in range(-h, h + 1):
                    for r1 in range(-h, h + 1):
                        data[(r0, r1)] = lam.legs(g, y0, (y0[0] + r0, y0[1] + r1), mu)
                om0 = data[(0, 0)][1]
                vs = {k: np.angle(val[1] / om0) for k, val in data.items()}
                A = float(np.mean(list(vs.values())))
                vbar2 = float(np.mean([v**2 for v in vs.values()]))
                vmax = max(vmax, max(abs(v) for v in vs.values()))
                for (r0, r1), (lg, om) in data.items():
                    nc1 = abs(r0) + abs(r1)
                    for b, co in lg[nc1 : nc1 + L]:
                        P[c, b] += co / L**2
                    v = vs[(r0, r1)]
                    weight = abs(v - A) + v**2 + A**2
                    weight0 = v**2 + A**2
                    for b in {bb for bb, _ in lg}:
                        Wb[c, b] += weight / L**2
                        Wn[c, b] += weight0 / L**2
                for b in {bb for bb, _ in data[(0, 0)][0]}:
                    Wb[c, b] += vbar2
                    Wn[c, b] += vbar2
    Res = Qo - P
    op = float(np.linalg.norm(Res, 2))
    # Plaquette angles and E(B).
    theta = np.zeros((N, N))
    for x0 in range(N):
        for x1 in range(N):
            xp0, xp1 = (x0 + 1) % N, (x1 + 1) % N
            theta[x0, x1] = np.angle(g.u[0, x0, x1] * g.u[1, xp0, x1] * np.conj(g.u[0, x0, xp1]) * np.conj(g.u[1, x0, x1]))
    Emax = 0.0
    for i in range(nc):
        for j in range(nc):
            s = 0.0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di != 0 and dj != 0:
                        continue
                    ii, jj = (i + di) % nc, (j + dj) % nc
                    s += np.sum(theta[L * ii : L * ii + L, L * jj : L * jj + L] ** 4)
            Emax = max(Emax, s**0.25)
    a = np.abs(Res)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(a > 1e-13, a / np.maximum(Wb, 1e-300), 0.0)
        ratio0 = np.where(a > 1e-13, a / np.maximum(Wn, 1e-300), 0.0)
    guard()
    return dict(op=op, E=Emax, vmax=vmax, w=float(np.max(ratio)), w0=float(np.max(ratio0)), R=op / (L**2 * Emax) if Emax > 0 else 0.0)


def main():
    ok = True
    rng = np.random.default_rng(404)
    print("Controls", flush=True)
    for L in (3, 5):
        g = make_field(L, 4, "random", 0.0, rng)
        r_ = analyse(g, L, 4)
        good = r_["op"] <= 1e-12
        ok = ok and good
        print(f" W2 L={L}: ||Res||={r_['op']:.1e}: {good}", flush=True)
    print("Cases", flush=True)
    best = {}
    w0max = 0.0
    for L in (3, 5, 7, 9):
        nc = 4
        for kind in ("random", "strip", "far", "smooth"):
            for target in (0.1, 0.3):
                # Scale the amplitude to reach the target largest |v_x|: two passes.
                amp = {"random": 0.02, "strip": 0.02, "far": 0.02, "smooth": 0.02}[kind]
                g = make_field(L, nc, kind, amp, np.random.default_rng(7))
                r0 = analyse(g, L, nc)
                amp = amp * target / max(r0["vmax"], 1e-9)
                g = make_field(L, nc, kind, amp, np.random.default_rng(7))
                r_ = analyse(g, L, nc)
                good = r_["w"] <= 3 and r_["R"] <= 1
                ok = ok and good
                w0max = max(w0max, r_["w0"])
                best[(L, kind)] = max(best.get((L, kind), 0.0), r_["R"])
                print(f" L={L} {kind} target={target}: vmax={r_['vmax']:.3f} ||Res||={r_['op']:.5f} E={r_['E']:.5f} R={r_['R']:.4f} (W) ratio={r_['w']:.3f} without the first-order term {r_['w0']:.2f}: {good} rss={rss_gb():.2f}GB", flush=True)
    print(f" W3: largest ratio with |v_x - A| removed: {w0max:.2f}", flush=True)
    for L in (3, 5, 7, 9):
        print(f" N2 L={L}: " + " ".join(f"{k}={best[(L, k)]:.4f}" for k in ("random", "strip", "far", "smooth")), flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
