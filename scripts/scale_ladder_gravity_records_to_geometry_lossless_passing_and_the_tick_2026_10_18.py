#!/usr/bin/env python3
"""Scale ladder, gravity rung: records to geometry under lossless passing, and the tick.

Finite checks of stated toy rules on Z^3 (and Z^3 x Z_tau for the Ward check), supplied-model framing:
  L1 one record's influence under a nearest-neighbour rule: lossless averaging (+) and lossless lean-away (-) both give
     the 1/r profile (lean-away = chessboard copy); a loss eps per step screens it with range ~ 1/sqrt(eps);
  L2 one rung out (2x2x2 blocks): a plain block reading sees the averaging profile, a chessboard reading sees lean-away;
  L3 records that drain a fixed pace give additive mass (equal 1/r coefficient per record); records that hold a pace do not;
  L4 Ward identity on the Kuhn complex: a lattice displacement reads exactly as a continuum gauge change, so a conserved
     source satisfies it to rounding and a source that appears without a current (a count source at a formation event) fails;
  L5 a lean-away-in-time step rule at one sub-step per tick and light speed 1 site/tick is unstable; two sub-steps are
     stable and carry light at 1 site per tick;
  L6 per-site random clocks stop the wave; coherent random tick lengths propagate it at equal speed in all directions;
  L7 delay through a pace well: lapse-only weights give integral |Phi|; weights m = a^3/N, k = N a give twice that;
  L8 continuous-time complex two-component (qubit-like) first-order rule carries a cone (leakage beyond r = 1.3 t below 1e-6);
     the real first-order rule does not;
  L9 the record cone: certain formation gives a diamond; formation odds 0.05 per tick give a much rounder, slower front.
Supplied models only; no physical identification.
Companion: docs/SCALE_LADDER_GRAVITY_RECORDS_TO_GEOMETRY_LOSSLESS_PASSING_AND_THE_TICK_BOUNDED_THEOREM_NOTE_2026-10-18.md
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = ('scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py',)

import contextlib, io, os, sys
import numpy as np
import scipy.sparse.linalg as spl

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def lap3(u):
    return (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1)
            + np.roll(u, 1, 2) + np.roll(u, -1, 2) - 6 * u)


def kgrid(L):
    k = 2 * np.pi * np.fft.fftfreq(L); return np.meshgrid(k, k, k, indexing='ij')


def response(L, sign, keep):
    """deviation d with d = sign*keep*avg(d) + delta at the origin (exact, Fourier; the zero mode dropped)."""
    KX, KY, KZ = kgrid(L); avg = (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 3
    den = 1 - sign * keep * avg
    with np.errstate(divide='ignore'):
        G = np.where(np.abs(den) < 1e-12, 0.0, 1.0 / den)
    return np.real(np.fft.ifftn(G))


def main():
    # ---------------- L1 lossless vs lossy
    L = 96; dA = response(L, 1, 1.0); dN = response(L, -1, 1.0)
    rs = np.arange(4, 17); A = np.array([dA[r, 0, 0] - dA[L // 2, 0, 0] for r in rs]); Nn = np.array([dN[r, 0, 0] - dN[L // 2, 0, 0] for r in rs])
    chess = max(abs(dN[r, 0, 0] - (-1) ** r * dA[r, 0, 0]) for r in range(1, 20))
    ranges = {}
    for eps in (0.03, 0.01):
        d = response(L, 1, 1 - eps); v = np.array([d[r, 0, 0] for r in (6, 12)])
        ranges[eps] = 6 / np.log((v[0] * 6) / (v[1] * 12))          # decay length from r d(r) ~ exp(-r/xi)
    ratio = ranges[0.01] / ranges[0.03]
    check("L1 one record: lossless averaging and lossless lean-away give the same long-range profile (lean-away = chessboard copy); loss eps screens it, range ~ 1/sqrt(eps)",
          chess < 1e-10 and np.all(A > 0) and abs(ratio - np.sqrt(3)) < 0.15,
          f"|lean-away - (-1)^r average| {chess:.0e}; screening range eps=0.03: {ranges[0.03]:.2f}, eps=0.01: {ranges[0.01]:.2f} (ratio {ratio:.2f}, sqrt3 = 1.73)")
    # ---------------- L2 zoom-out readings
    X, Y, Z = np.meshgrid(*[np.arange(L)] * 3, indexing='ij'); stag = (-1.0) ** (X + Y + Z)
    def block(f): return f.reshape(L // 2, 2, L // 2, 2, L // 2, 2).mean(axis=(1, 3, 5))
    R_ = 6
    pa, pn = block(dA)[R_, 0, 0] - block(dA)[L // 4, 0, 0], block(dN)[R_, 0, 0] - block(dN)[L // 4, 0, 0]
    sa, sn = block(dA * stag)[R_, 0, 0] - block(dA * stag)[L // 4, 0, 0], block(dN * stag)[R_, 0, 0] - block(dN * stag)[L // 4, 0, 0]
    check("L2 one rung out: the plain block reading sees averaging and misses lean-away; the chessboard reading does the reverse",
          abs(pn) < 1e-3 * abs(pa) and abs(sa) < 1e-3 * abs(sn) and abs(pa - sn) < 1e-9, f"plain: average {pa:.4f}, lean-away {pn:.1e}; chessboard: average {sa:.1e}, lean-away {sn:.4f}")
    # ---------------- L3 drains vs holds
    Lg = 41; c = Lg // 2
    Xg, Yg, Zg = np.meshgrid(*[np.arange(Lg) - c] * 3, indexing='ij'); Rg = np.sqrt(Xg ** 2 + Yg ** 2 + Zg ** 2)
    bd = np.zeros((Lg,) * 3, bool); bd[[0, -1], :, :] = bd[:, [0, -1], :] = bd[:, :, [0, -1]] = True
    def solve(fixed, val, src):
        free = ~fixed; nf = int(free.sum())
        def op(v):
            u = np.zeros((Lg,) * 3); u[free] = v; return (6 * u - (lap3(u) + 6 * u))[free]
        g = np.where(fixed, val, 0.0); rhs = (lap3(g) + 6 * g)[free] + src[free]
        x, _ = spl.cg(spl.LinearOperator((nf, nf), matvec=op), rhs, rtol=1e-12, maxiter=6000)
        p = val.copy(); p[free] = x; return p
    per, hold = [], []
    for rad in (0.5, 1.5, 2.2):
        rec = Rg <= rad; n = int(rec.sum())
        p = solve(bd, np.where(bd, 1.0, 0.0), -6 * 0.01 * rec)                       # drains
        per.append(np.mean([(1 - p[c + 9, c, c]) / (1 / 9 - 1 / c), (1 - p[c + 6, c + 6, c]) / (1 / (6 * np.sqrt(2)) - 1 / c)]) / n)
        ph = solve(bd | rec, np.where(rec, 0.5, 1.0), np.zeros((Lg,) * 3))           # holds
        hold.append((n, (1 - ph[c + 9, c, c]) / (1 / 9 - 1 / c)))
    check("L3 records that drain a fixed pace give additive mass (same 1/r coefficient per record for 1, 19, 33 records); records holding a pace give mass growing with size, not count",
          np.ptp(per) / np.mean(per) < 0.02 and hold[2][1] / hold[0][1] < 0.3 * hold[2][0] / hold[0][0],
          f"drain coefficient per record {', '.join(f'{x:.5f}' for x in per)}; holding: {hold[0][0]} records -> {hold[0][1]:.3f}, {hold[2][0]} -> {hold[2][1]:.3f}")
    # ---------------- L4 Ward identity on the Kuhn complex
    HC = R4.HCOMPS; D15 = [np.array(v, float) for v in R4.DIRS15]
    def Mmap(k):
        M = np.zeros((15, 10), complex)
        for ci, vv in enumerate(D15):
            z = (k @ vv) / 2; ph = 1.0 if abs(z) < 1e-13 else (np.exp(2j * z) - 1) / (2j * z)
            for j, (a, b) in enumerate(HC): M[ci, j] = ph * vv[a] * vv[b] * (2 if a != b else 1) / (2 * np.linalg.norm(vv))
        return M
    def Gam(k):
        G = np.zeros((15, 4), complex)
        for ci, vv in enumerate(D15): G[ci] = (np.exp(1j * k @ vv) - 1) * vv / np.linalg.norm(vv)
        return G
    def Tvec(T): return np.array([T[a, b] * (1 if a == b else 2) for a, b in HC])
    worst_c, best_n = 0.0, np.inf
    for kk in [np.array([0.02, -0.01, 0.015, 0.01j]), np.array([0.004, 0.003, -0.002, 0.005j])]:
        Lr = np.linalg.pinv(Mmap(kk)); LG = Lr @ Gam(kk); kn = np.linalg.norm(kk)
        S = np.zeros((4, 4), complex); S[3, 3] = 1.0; Pi = np.eye(4) - np.outer(kk, kk) / (kk @ kk); Tq = Pi @ S @ Pi.T
        worst_c = max(worst_c, np.linalg.norm(Tvec(Tq) @ LG) / (kn * np.linalg.norm(Tvec(Tq))))
        best_n = min(best_n, np.linalg.norm(Tvec(S) @ LG) / (kn * np.linalg.norm(Tvec(S))))
    check("L4 Kuhn complex: through the least-squares reading a lattice displacement is exactly a continuum gauge change; a conserved source passes the Ward identity, a source appearing with no current fails at O(1)",
          worst_c < 1e-10 and best_n > 0.3, f"conserved residual <= {worst_c:.0e}; current-free source residual >= {best_n:.2f}")
    # ---------------- L5 sub-steps per tick
    Lw = 96; cw = Lw // 2
    Xw, Yw, Zw = np.meshgrid(*[np.arange(Lw) - cw] * 3, indexing='ij'); Rw = np.sqrt(Xw ** 2 + Yw ** 2 + Zw ** 2)
    def shell(u, d):
        d = np.array(d, float); d /= np.linalg.norm(d); rs_ = np.arange(4, cw - 3, 0.5)
        pts = np.round(cw + np.outer(rs_, d)).astype(int); return rs_[int(np.argmax(np.abs(u[pts[:, 0], pts[:, 1], pts[:, 2]])))]
    def run_sub(n, T):
        u0 = np.exp(-Rw ** 2 / 18.0); u1 = u0.copy(); snaps = {}
        for t in range(1, T * n + 1):
            u2 = 2 * u1 - u0 + lap3(u1) / n ** 2; u0, u1 = u1, u2
            if np.abs(u1).max() > 1e8: return None
            if t % n == 0 and t // n in (15, 35): snaps[t // n] = u1.copy()
        return snaps
    s1, s2 = run_sub(1, 35), run_sub(2, 35)
    sp = {nm: (shell(s2[35], d) - shell(s2[15], d)) / 20 for nm, d in {'axis': (1, 0, 0), 'face': (1, 1, 0), 'body': (1, 1, 1)}.items()} if s2 else {}
    check("L5 lean-away-in-time at light speed 1 site per tick: one sub-step per tick is unstable; two sub-steps are stable with speed ~1 in all directions",
          s1 is None and s2 is not None and all(abs(v - 1) < 0.08 for v in sp.values()), "speeds " + ", ".join(f"{k} {v:.3f}" for k, v in sp.items()))
    # ---------------- L6 random clocks
    rng = np.random.default_rng(3)
    u = np.exp(-Rw ** 2 / 18.0); up = u.copy(); s = 0.25
    for t in range(150):
        m = rng.random(u.shape) < 0.5; new = 2 * u - up + s * lap3(u); up = np.where(m, u, up); u = np.where(m, new, u)
    stuck = abs(shell(u, (1, 0, 0)) - 0) < 10 or np.abs(u).max() > 1.0
    u = np.exp(-Rw ** 2 / 18.0); up = u.copy(); dtp = 0.35; T = 0.0; snaps = {}
    while T < 36:
        dt = rng.uniform(0.15, 0.55); un = u + (dt / dtp) * (u - up) + dt * (dt + dtp) / 2 * lap3(u); up, u, dtp = u, un, dt; T += dt
        for mk in (16, 34):
            if mk not in snaps and T >= mk: snaps[mk] = (T, u.copy())
    (t1, a1), (t2, a2) = snaps[16], snaps[34]
    spr = [(shell(a2, d) - shell(a1, d)) / (t2 - t1) for d in ((1, 0, 0), (1, 1, 0), (1, 1, 1))]
    check("L6 per-site random clocks (half the sites update each step) stop the wave; coherent random tick lengths carry it at equal speed along axis, face and body",
          stuck and np.ptp(spr) < 0.06 and abs(np.mean(spr) - 1) < 0.08, f"coherent random ticks: speeds {', '.join(f'{v:.3f}' for v in spr)}")
    # ---------------- L7 delay through a pace well
    L1 = 3000; x = np.arange(L1) - L1 / 2; Phi = -0.02 * np.exp(-x ** 2 / (2 * 120.0 ** 2))
    def arrival(m, k, dt=0.5):
        u = np.exp(-(x + 1100) ** 2 / (2 * 12.0 ** 2)); v = -np.gradient(u); kh = 0.5 * (k + np.roll(k, -1)); t = 0.0
        while t < 3000:
            f = (kh * (np.roll(u, -1) - u) - np.roll(kh, 1) * (u - np.roll(u, 1))) / m; v += dt * f; u += dt * v; t += dt
            if t > 100 and u[int(L1 / 2 + 1100)] > 0.5 * u.max(): return t
    N_, a_ = 1 + Phi, 1 - Phi
    t0, tl, tg = arrival(np.ones(L1), np.ones(L1)), arrival(1 / N_, N_), arrival(a_ ** 3 / N_, N_ * a_)
    pred = float(np.sum(np.abs(Phi)))
    check("L7 delay through a pace well: lapse-only weights give the integral of |Phi|; weights m = a^3/N, k = N a give twice it",
          abs((tl - t0) - pred) < 1.0 and abs((tg - t0) - 2 * pred) < 1.5, f"lapse-only {tl - t0:.1f}, full {tg - t0:.1f}, integral |Phi| {pred:.2f}")
    # ---------------- L8 continuous-time complex amplitudes
    Lc = 96; KX, KY, KZ = kgrid(Lc); ph4 = 4 * (np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2); t = 30
    ax_, ay_, az_ = np.sin(KX), np.sin(KY), np.sin(KZ); A_ = np.sqrt(ax_ ** 2 + ay_ ** 2 + az_ ** 2) + 1e-300
    p0 = np.fft.ifftn(np.cos(A_ * t) - 1j * np.sin(A_ * t) * az_ / A_); p1 = np.fft.ifftn(-1j * np.sin(A_ * t) * (ax_ + 1j * ay_) / A_)
    dens = np.abs(p0) ** 2 + np.abs(p1) ** 2
    Xc, Yc, Zc = np.meshgrid(*[np.minimum(np.arange(Lc), Lc - np.arange(Lc))] * 3, indexing='ij'); Rc = np.sqrt(Xc ** 2 + Yc ** 2 + Zc ** 2)
    leak = dens[Rc > 1.3 * t].sum() / dens.sum(); leak11 = dens[Rc > 1.1 * t].sum() / dens.sum(); inside_front = dens[(Rc > 0.6 * t) & (Rc <= 1.1 * t)].sum() / dens.sum()
    dif = np.real(np.fft.ifftn(np.exp(-ph4 * t))); prof = np.array([dif[r, 0, 0] for r in range(1, 30)])
    monotone = np.all(np.diff(prof) < 0)
    check("L8 continuous time: the complex two-component first-order rule carries a cone (a third of the weight in 0.6t-1.1t, leakage beyond 1.3 t < 1e-6); the real first-order rule only diffuses (monotone, no front)",
          leak < 1e-6 and inside_front > 0.25 and monotone, f"complex: share in 0.6t-1.1t {inside_front:.2f}, beyond 1.1t {leak11:.1e}, beyond 1.3t {leak:.1e}")
    # ---------------- L9 the record cone
    Lr_ = 81; cr = Lr_ // 2
    def grow(p, T):
        Rm = np.zeros((Lr_,) * 3, bool); Rm[cr, cr, cr] = True; g = np.random.default_rng(1)
        for _ in range(T):
            nb = (np.roll(Rm, 1, 0) | np.roll(Rm, -1, 0) | np.roll(Rm, 1, 1) | np.roll(Rm, -1, 1) | np.roll(Rm, 1, 2) | np.roll(Rm, -1, 2)) & ~Rm
            Rm |= nb & (g.random(Rm.shape) < p)
        P = np.stack(np.nonzero(Rm), 1).astype(float) - cr; r = np.linalg.norm(P, axis=1) + 1e-9
        ext = []
        for d in ((1, 0, 0), (1, 1, 1)):
            u = np.array(d, float) / np.linalg.norm(d); sel = (P @ u) / r > 0.995; ext.append(r[sel].max())
        return ext[1] / ext[0], ext[0] / T
    r1, v1 = grow(1.0, 30); r5, v5 = grow(0.05, 300)
    check("L9 the record cone: certain formation gives a diamond (body/axis ~ 0.58); formation odds 0.05 per tick give a rounder (> 0.85), slower front",
          abs(r1 - 1 / np.sqrt(3)) < 0.03 and r5 > 0.85 and v5 < 0.3 * v1, f"body/axis {r1:.3f} (p=1), {r5:.3f} (p=0.05); axis speed {v1:.2f} vs {v5:.3f} sites/tick")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
