#!/usr/bin/env python3
"""Finite supplied lattice response, segment gauge reading and update-rule controls.
Neutralized periodic Green functions, finite Dirichlet solves, exact segment
identity and specified seeded wave/growth fixtures. No physical source, clock,
owner adoption, universal asynchronous exclusion or asymptotic growth claim.
Companion: docs/SCALE_LADDER_GRAVITY_RECORDS_TO_GEOMETRY_LOSSLESS_PASSING_AND_THE_TICK_BOUNDED_THEOREM_NOTE_2026-10-18.md
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = ('scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py', 'docs/SCALE_LADDER_GRAVITY_RECORDS_TO_GEOMETRY_LOSSLESS_PASSING_AND_THE_TICK_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md', 'outputs/records_geometry_review_2026_10_18/INPUT_CLOSURE.json', 'archive/records_geometry_review_2026_10_18/MANIFEST.json')

import itertools, os, sys, signal
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"
if not __debug__:
    raise RuntimeError("optimized Python would disable required assertions")
def _expired(signum, frame):
    raise TimeoutError("declared 1200-second primary cap reached")
signal.signal(signal.SIGALRM, _expired)
signal.alarm(AUDIT_TIMEOUT_SEC)
import numpy as np
import scipy.sparse.linalg as spl

# Exact constant definitions from the bound parent helper; no Regge action is imported.
DIRS15 = [v for v in itertools.product([0, 1], repeat=4) if any(v)]
HCOMPS = [(0,0),(1,1),(2,2),(3,3),(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


def lap3(u):
    return (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1)
            + np.roll(u, 1, 2) + np.roll(u, -1, 2) - 6 * u)


def kgrid(L):
    k = 2 * np.pi * np.fft.fftfreq(L); return np.meshgrid(k, k, k, indexing='ij')


def response(L, sign, keep):
    """Periodic inverse with singular mode removed: neutralized source when keep=1.
    For sign=+1 its source is delta-1/L^3 and mean(d)=0; for sign=-1 on
    even L its source is delta-checkerboard/L^3 and checkerboard mean(d)=0.
    """
    if sign not in (-1, 1) or not 0 < keep <= 1:
        raise ValueError("unsupported sign/keep")
    if sign == -1 and keep == 1 and L % 2:
        raise ValueError("checkerboard singular-mode convention requires even L")
    KX, KY, KZ = kgrid(L); avg = (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 3
    den = 1 - sign * keep * avg
    singular = np.zeros(den.shape, dtype=bool)
    if keep == 1:
        singular[(0,0,0) if sign == 1 else (L//2,L//2,L//2)] = True
    G = np.zeros_like(den)
    np.divide(1.0, den, out=G, where=~singular)
    return np.real(np.fft.ifftn(G))


def main():
    # ---------------- L1 lossless vs lossy
    L = 96; dA = response(L, 1, 1.0); dN = response(L, -1, 1.0)
    X, Y, Z = np.meshgrid(*[np.arange(L)] * 3, indexing='ij'); stag = (-1.0) ** (X + Y + Z)
    delta = np.zeros_like(dA); delta[0,0,0] = 1
    avg = lambda u: u + lap3(u)/6
    ra = np.max(np.abs(dA-avg(dA)-(delta-1/L**3)))
    rn = np.max(np.abs(dN+avg(dN)-(delta-stag/L**3)))
    check("neutralized torus equations and fixed singular-mode gauges", ra < 1e-12 and rn < 1e-12 and abs(dA.mean()) < 1e-14 and abs((stag*dN).mean()) < 1e-14, f"positive residual {ra:.3e}; checkerboard residual {rn:.3e}")
    check("unneutralized delta source residual mutant detected", np.max(np.abs(dA-avg(dA)-delta)) > 0.9/L**3)
    rs = np.arange(4, 17); A = np.array([dA[r, 0, 0] - dA[L // 2, 0, 0] for r in rs]); Nn = np.array([dN[r, 0, 0] - dN[L // 2, 0, 0] for r in rs])
    chess = max(abs(dN[r, 0, 0] - (-1) ** r * dA[r, 0, 0]) for r in range(1, 20))
    ranges = {}
    for eps in (0.03, 0.01):
        d = response(L, 1, 1 - eps); v = np.array([d[r, 0, 0] for r in (6, 12)])
        ranges[eps] = 6 / np.log((v[0] * 6) / (v[1] * 12))          # decay length from r d(r) ~ exp(-r/xi)
    ratio = ranges[0.01] / ranges[0.03]
    check("finite torus checkerboard conjugacy and two-epsilon screening-length diagnostic",
          chess < 1e-10 and np.all(A > 0) and abs(ratio - np.sqrt(3)) < 0.15,
          f"|lean-away - (-1)^r average| {chess:.0e}; screening range eps=0.03: {ranges[0.03]:.2f}, eps=0.01: {ranges[0.01]:.2f} (ratio {ratio:.2f}, sqrt3 = 1.73)")
    # ---------------- L2 zoom-out readings
    X, Y, Z = np.meshgrid(*[np.arange(L)] * 3, indexing='ij'); stag = (-1.0) ** (X + Y + Z)
    def block(f): return f.reshape(L // 2, 2, L // 2, 2, L // 2, 2).mean(axis=(1, 3, 5))
    R_ = 6
    pa, pn = block(dA)[R_, 0, 0] - block(dA)[L // 4, 0, 0], block(dN)[R_, 0, 0] - block(dN)[L // 4, 0, 0]
    sa, sn = block(dA * stag)[R_, 0, 0] - block(dA * stag)[L // 4, 0, 0], block(dN * stag)[R_, 0, 0] - block(dN * stag)[L // 4, 0, 0]
    check("finite two-site block means: channel exchange and sampled suppression ratio",
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
        x, info = spl.cg(spl.LinearOperator((nf, nf), matvec=op), rhs, rtol=1e-12, maxiter=6000)
        residual = np.linalg.norm(op(x)-rhs)/max(np.linalg.norm(rhs), np.finfo(float).tiny)
        print(f"Dirichlet CG free={nf} status={info} relative residual={residual:.3e}", flush=True)
        if info != 0 or not np.all(np.isfinite(x)) or not np.isfinite(residual) or residual > 2e-11:
            raise RuntimeError("Dirichlet CG convergence/residual failure")
        p = val.copy(); p[free] = x; return p
    per, hold = [], []
    for rad in (0.5, 1.5, 2.2):
        rec = Rg <= rad; n = int(rec.sum())
        p = solve(bd, np.where(bd, 1.0, 0.0), -6 * 0.01 * rec)                       # drains
        per.append(np.mean([(1 - p[c + 9, c, c]) / (1 / 9 - 1 / c), (1 - p[c + 6, c + 6, c]) / (1 / (6 * np.sqrt(2)) - 1 / c)]) / n)
        ph = solve(bd | rec, np.where(rec, 0.5, 1.0), np.zeros((Lg,) * 3))           # holds
        hold.append((n, (1 - ph[c + 9, c, c]) / (1 / 9 - 1 / c)))
    check("finite Dirichlet clusters: drain far-field proxy per site and pinned-value proxy differ",
          np.ptp(per) / np.mean(per) < 0.02 and hold[2][1] / hold[0][1] < 0.3 * hold[2][0] / hold[0][0],
          f"drain coefficient per record {', '.join(f'{x:.5f}' for x in per)}; holding: {hold[0][0]} records -> {hold[0][1]:.3f}, {hold[2][0]} -> {hold[2][1]:.3f}")
    # ---------------- L4 Ward identity on the Kuhn complex
    HC = HCOMPS; D15 = [np.array(v, float) for v in DIRS15]
    def Mmap(k):
        M = np.zeros((15, 10), complex)
        for ci, vv in enumerate(D15):
            z = (k @ vv) / 2; ph = 1.0 if z == 0 else np.expm1(2j * z) / (2j * z)
            for j, (a, b) in enumerate(HC): M[ci, j] = ph * vv[a] * vv[b] * (2 if a != b else 1) / (2 * np.linalg.norm(vv))
        return M
    def Gam(k):
        G = np.zeros((15, 4), complex)
        for ci, vv in enumerate(D15): G[ci] = (np.exp(1j * k @ vv) - 1) * vv / np.linalg.norm(vv)
        return G
    def Tvec(T): return np.array([T[a, b] * (1 if a == b else 2) for a, b in HC])
    worst_c, best_n = 0.0, np.inf
    for kk in [np.array([0.02, -0.01, 0.015, 0.01j]), np.array([0.004, 0.003, -0.002, 0.005j])]:
        M = Mmap(kk); G = Gam(kk)
        C = np.array([[1j*((kk[a] if b == j else 0)+(kk[b] if a == j else 0)) for j in range(4)] for a,b in HC])
        sv = np.linalg.svd(M, compute_uv=False)
        assert sv[-1] > 1e-6 and abs(kk @ kk) > 1e-10
        check("segment gauge identity at " + str(tuple(kk)), np.linalg.norm(M@C-G) < 1e-12, f"smallest singular value {sv[-1]:.6g}")
        Lr = np.linalg.pinv(M); LG = Lr @ G; kn = np.linalg.norm(kk)
        assert np.linalg.norm(LG-C) < 1e-12
        S = np.zeros((4, 4), complex); S[3, 3] = 1.0; Pi = np.eye(4) - np.outer(kk, kk) / (kk @ kk); Tq = Pi @ S @ Pi.T
        worst_c = max(worst_c, np.linalg.norm(Tvec(Tq) @ LG) / (kn * np.linalg.norm(Tvec(Tq))))
        best_n = min(best_n, np.linalg.norm(Tvec(S) @ LG) / (kn * np.linalg.norm(Tvec(S))))
    check("two nondegenerate segment fixtures: transverse symmetric source pairing and unprojected temporal source contrast",
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
    check("specified leapfrog fixture: n=1 growth and n=2 finite pulse speeds near one",
          s1 is None and s2 is not None and all(abs(v - 1) < 0.08 for v in sp.values()), "speeds " + ", ".join(f"{k} {v:.3f}" for k, v in sp.items()))
    roots_one = np.roots([1, 10, 1]) # lambda=12, n=1
    roots_two = np.roots([1, 1, 1])  # lambda=12, n=2
    check("leapfrog checkerboard characteristic roots", np.max(np.abs(roots_one)) > 9 and np.max(np.abs(np.abs(roots_two)-1)) < 1e-12)
    # ---------------- L6 random clocks
    rng = np.random.default_rng(3)
    u = np.exp(-Rw ** 2 / 18.0); up = u.copy(); s = 0.25
    for t in range(150):
        m = rng.random(u.shape) < 0.5; new = 2 * u - up + s * lap3(u); up = np.where(m, u, up); u = np.where(m, new, u)
    async_peak = shell(u, (1, 0, 0)); async_amp = float(np.max(np.abs(u)))
    assert np.isfinite(async_amp)
    print(f"seeded asynchronous fixture: peak radius={async_peak:.3f}, amplification={async_amp:.6g}; amplification is not nonpropagation", flush=True)
    # A remote growing pulse is a counterexample to the original OR diagnostic.
    def quiet_localized(radius, amplification):
        return radius < 10 and amplification <= 1.0
    check("growing remote pulse rejected by localization diagnostic", not quiet_localized(20, 2))
    u = np.exp(-Rw ** 2 / 18.0); up = u.copy(); dtp = 0.35; T = 0.0; snaps = {}
    while T < 36:
        dt = rng.uniform(0.15, 0.55); un = u + (dt / dtp) * (u - up) + dt * (dt + dtp) / 2 * lap3(u); up, u, dtp = u, un, dt; T += dt
        for mk in (16, 34):
            if mk not in snaps and T >= mk: snaps[mk] = (T, u.copy())
    (t1, a1), (t2, a2) = snaps[16], snaps[34]
    spr = [(shell(a2, d) - shell(a1, d)) / (t2 - t1) for d in ((1, 0, 0), (1, 1, 0), (1, 1, 1))]
    check("specified coherent variable-step fixture: three finite pulse speeds near one; asynchronous amplitude reported separately",
          np.ptp(spr) < 0.06 and abs(np.mean(spr) - 1) < 0.08, f"coherent random ticks: speeds {', '.join(f'{v:.3f}' for v in spr)}")
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
    check("one-dimensional finite pulse-delay fixture agrees with leading weak-well travel-time formulas",
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
    check("finite Pauli-sine propagator shell weights versus specified scalar heat-kernel monotonicity",
          leak < 1e-6 and inside_front > 0.25 and monotone, f"complex: share in 0.6t-1.1t {inside_front:.2f}, beyond 1.1t {leak11:.1e}, beyond 1.3t {leak:.1e}")
    # ---------------- L9 the record cone
    Lr_ = 81; cr = Lr_ // 2
    def grow(p, T):
        Rm = np.zeros((Lr_,) * 3, bool); Rm[cr, cr, cr] = True; g = np.random.default_rng(1)
        boundary = np.zeros_like(Rm); boundary[[0,-1],:,:] = True; boundary[:,[0,-1],:] = True; boundary[:,:,[0,-1]] = True
        first_boundary = None; wrapped_proposals = 0
        for tick in range(T):
            for axis in range(3):
                wrapped_proposals += int(np.count_nonzero(np.take(Rm,-1,axis=axis) & ~np.take(Rm,0,axis=axis)))
                wrapped_proposals += int(np.count_nonzero(np.take(Rm,0,axis=axis) & ~np.take(Rm,-1,axis=axis)))
            nb = (np.roll(Rm, 1, 0) | np.roll(Rm, -1, 0) | np.roll(Rm, 1, 1) | np.roll(Rm, -1, 1) | np.roll(Rm, 1, 2) | np.roll(Rm, -1, 2)) & ~Rm
            Rm |= nb & (g.random(Rm.shape) < p)
            if first_boundary is None and np.any(Rm & boundary): first_boundary = tick+1
        print(f"growth p={p} ticks={T}: first boundary contact={first_boundary}, cross-face neighbor proposals={wrapped_proposals}; periodic-box diagnostic", flush=True)
        if p == 1.0 and T < cr:
            coords = np.indices(Rm.shape)-cr
            assert np.array_equal(Rm, np.abs(coords).sum(axis=0) <= T)
            assert first_boundary is None and wrapped_proposals == 0
        P = np.stack(np.nonzero(Rm), 1).astype(float) - cr; r = np.linalg.norm(P, axis=1) + 1e-9
        ext = []
        for d in ((1, 0, 0), (1, 1, 1)):
            u = np.array(d, float) / np.linalg.norm(d); sel = (P @ u) / r > 0.995; ext.append(r[sel].max())
        return ext[1] / ext[0], ext[0] / T
    r1, v1 = grow(1.0, 30); r5, v5 = grow(0.05, 300)
    check("finite periodic growth extents: deterministic diamond fixture and seeded p=.05 torus ratio, with boundary diagnostics",
          abs(r1 - 1 / np.sqrt(3)) < 0.03 and r5 > 0.85 and v5 < 0.3 * v1, f"body/axis {r1:.3f} (p=1), {r5:.3f} (p=0.05); axis speed {v1:.2f} vs {v5:.3f} sites/tick")

    print("per_element: neutralized finite Green equations and segment matrix entries retain their explicit normalization and sources.")
    print("per_site: finite Dirichlet source clusters and seeded update masks are checked; physical record-to-stress identification is untested.")
    print("per_mode: segment rank, complex momentum pairing and the specified propagator are checked at the declared finite fixtures.")
    print("per_block: plain and checkerboard two-site block means are compared on one fixed periodic Green-function box.")
    print("lattice_wide: periodic finite boxes only; unbounded growth, general asynchronous integrators and physical clock laws are untested.")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}", flush=True)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
