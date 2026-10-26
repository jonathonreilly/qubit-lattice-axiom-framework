#!/usr/bin/env python3
"""Finite Regge/EH normalization diagnostics and conditional coefficient algebra.

On supplied Kuhn cubic and coned D4 geometries, evaluate sampled metric-form
ratios and static point-source responses on the stated finite momentum sets
and torus. These tests do not prove continuum convergence or carrier independence.
If one supplies EH matching, the metric/source identification, action sign and
unit conventions, coefficient comparison gives G = a^2/(8 pi kappa).
The response uses S = -(kappa/2) h^T K h - (E/2) h_tt, so
h = -(E/(2 kappa)) K^+ e_tt and S_on = -E h_tt/4.
The raw Kuhn position-space discrepancy is retained; block averaging is a
different readout. No physical Newton constant or Planck identification follows.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/REGGE_ACTION_PER_CELL_AND_THE_CONDITIONAL_GRAVITY_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-21.md',
    'scripts/scale_ladder_gravity_d4_cone_common_cone_spins_zero_one_two_2026_10_18.py',
    'scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py',
    'docs/CANDIDATE_LAWS.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/SCALE_LADDER_GRAVITY_D4_CONE_COMMON_CONE_SPINS_ZERO_ONE_TWO_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/work_history/repo/review_feedback/GRAVITY_REVIEW_SCOPE_AND_RECOVERY_2026-10-18.md',
    'archive/gravity_review_2026_10_18/MANIFEST.json',
    'docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
)

import contextlib, io, itertools, os, sys, time, signal
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
_T0 = time.monotonic()
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    import scale_ladder_gravity_d4_cone_common_cone_spins_zero_one_two_2026_10_18 as D

PASS = FAIL = 0
HC = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
TICK = 3                       # supplied tick index (HC position 3 is h_tt)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def kuhn_complex():
    E = np.eye(4, dtype=int); sims = []
    for perm in itertools.permutations(range(4)):
        p = np.zeros(4, int); vs = [(tuple(p), 0)]
        for a in perm: p = p + E[a]; vs.append((tuple(p), 0))
        sims.append(vs)
    return D.Complex([np.zeros(4)], sims)


def d4_complex():
    OFF, S = D.d4cone(); return D.Complex(OFF, S)


class Carrier:
    def __init__(self, C):
        self.terms = C.terms; self.E = C.E
        self.V = np.array(C.evec); self.O = np.zeros((C.E, 4)); self.l = np.linalg.norm(self.V, axis=1)
        for (t1, t2, rel), c in C.ekey.items(): self.O[c] = C.OFF[t1]
        self.W = np.array([[v[a] * v[b] * (2 if a != b else 1) / (2 * ll) for a, b in HC] for v, ll in zip(self.V, self.l)])

    def M(self, ks):
        z = ks @ self.V.T; zs = np.where(abs(z) < 1e-14, 1.0, z)
        ph = np.where(abs(z) < 1e-14, 1.0, (np.exp(1j * z) - 1) / (1j * zs)) * np.exp(1j * ks @ self.O.T)
        return ph[:, :, None] * self.W[None]

    def K(self, ks):
        """10x10 Hermitian kernel: H^dag K H = m^dag Q m with m = M H (Q = Hessian of sum A delta in Bloch form)."""
        ks = np.atleast_2d(np.asarray(ks, float)); M = self.M(ks); K = np.zeros((len(ks), 10, 10), complex)
        for a, d in self.terms:
            ra, rd = (np.einsum('ke,kej->kj', self._row(t, ks), M) for t in (a, d))
            K += 0.5 * (np.conj(ra)[:, :, None] * rd[:, None, :] + np.conj(rd)[:, :, None] * ra[:, None, :])
        return K

    def _row(self, t, ks):
        idx, anc, w = t; r = np.zeros((len(ks), self.E), complex)
        ph = np.exp(1j * ks @ np.asarray(anc, float).T) * w[None]
        for n in range(len(idx)): r[:, idx[n]] += ph[:, n]
        return r


def Fcont(k):
    """Continuum: (1/2) H^dag F H = cell average of the 2nd-order sqrt(g)R for h = Re(H e^{ikx}) (Euclidean),
    from sqrt(g)R_2 = -1/4 (d h_mn)^2 + 1/2 (d_m h_mn)^2 - 1/2 d_m h_mn d_n h + 1/4 (d h)^2 up to divergences."""
    k = np.asarray(k, float); k2 = k @ k; F = np.zeros((10, 10)); I = np.eye(10)
    def mat(Hv):
        Hm = np.zeros((4, 4))
        for j, (a, b) in enumerate(HC): Hm[a, b] = Hm[b, a] = Hv[j]
        return Hm
    for i in range(10):
        for j in range(10):
            A, B = mat(I[i]), mat(I[j])
            F[i, j] = (-0.25 * k2 * np.sum(A * B) + 0.5 * (k @ A) @ (k @ B) - 0.25 * ((k @ A @ k) * np.trace(B) + np.trace(A) * (k @ B @ k))
                       + 0.25 * k2 * np.trace(A) * np.trace(B))
    return F


def static_response(car, L, kappa=1.0, chunk=1500):
    """h_tt(x) on an L^3 spatial torus for a static deposit E=1 on the tick direction: h = -(E/(2 kappa)) K^+ e_tt."""
    g = 2 * np.pi * np.fft.fftfreq(L); kx, ky, kz = np.meshgrid(g, g, g, indexing='ij')
    ks = np.stack([kx.ravel(), ky.ravel(), kz.ravel(), np.zeros(kx.size)], 1)
    hk = np.zeros(len(ks)); hc = np.zeros(len(ks)); e = np.zeros(10); e[TICK] = 1.0
    for s in range(0, len(ks), chunk):
        kk = ks[s:s + chunk]; Kb = car.K(kk); nz = np.linalg.norm(kk, axis=1) > 1e-12
        sol = np.einsum('kij,j->ki', np.linalg.pinv(Kb[nz], rcond=1e-7, hermitian=True), e)
        hk[s:s + chunk][nz] = -0.5 * np.real(sol[:, TICK]) / kappa
        hc[s:s + chunk][nz] = 1.0 / np.sum(4 * np.sin(kk[nz, :3] / 2) ** 2, axis=1)   # cubic-Laplacian Green kernel, ~ 1/(4 pi r)
    hx = np.real(np.fft.ifftn(hk.reshape(L, L, L))); cx = np.real(np.fft.ifftn(hc.reshape(L, L, L)))
    return hx, cx


def main():
    rng = np.random.default_rng(7)
    cars = {}
    for name, build in (('Kuhn cubic', kuhn_complex), ('coned D4', d4_complex)):
        cars[name] = Carrier(build())
    print('carriers: ' + '; '.join(f'{n}: {c.E} edge classes, {len(c.terms)} hinge classes per unit cell (volume 1)' for n, c in cars.items()))

    # (1) Finite sampled diagnostic for proposed Regge/EH factor one half
    for name, car in cars.items():
        worst = 0.0; rows = []
        for _ in range(4):
            kd = rng.standard_normal(4); kd /= np.linalg.norm(kd); H = rng.standard_normal(10); r = []
            for s in (0.05, 0.025):
                r.append(np.real(H @ car.K(s * kd)[0] @ H) / (H @ Fcont(s * kd) @ H))
            rr = (4 * r[1] - r[0]) / 3; worst = max(worst, abs(rr - 1)); rows.append(rr)
        check(f'(1) {name}: sampled 2 Hess(sum A delta) / Hess(cell integral sqrt(g)R) near 1 for four random h (Richardson .05/.025)',
              worst < 1e-3, 'ratios ' + ', '.join(f'{x:.5f}' for x in rows))
        H = np.zeros(10); H[7] = 1.0; kk = np.array([0.01, 0, 0, 0.0])
        tt = np.real(H @ car.K(kk)[0] @ H) / (H @ Fcont(kk) @ H)
        check(f'(1) {name}: transverse-traceless wave h_12(x_0) gives the same ratio', abs(tt - 1) < 1e-4, f'{tt:.7f}')
    Qe, Mh = D.regge(np.eye(4)); kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); H = rng.standard_normal(10)
    rr = [np.real(np.conj(Mh(s * kd) @ H) @ Qe(s * kd) @ (Mh(s * kd) @ H)) / (H @ Fcont(s * kd) @ H) for s in (2e-3, 1e-3)]
    check('(1) Kuhn cubic, analytic-derivative Hessian of the repo Regge code: same ratio', abs(rr[1] - 1) < 1e-5, ', '.join(f'{x:.7f}' for x in rr))

    # (2) Supplied Euclidean action/source: h_tt = E/(kappa k^2);
    # transverse spatial diagonals have the opposite sign in an axis frame.
    k3 = np.array([0.3, -0.2, 0.1, 0.0]); e = np.zeros(10); e[TICK] = 1
    hs = -0.5 * np.linalg.pinv(Fcont(k3), rcond=1e-10) @ e; k2 = k3 @ k3
    check('(2) supplied quadratic action -(kappa/2) h F h - E h_tt/2: comparator static tick response h_tt = -(E/2kappa)[F^+]_tt = E/(kappa k^2); G = 1/(8 pi kappa) only conditional on EH matching and units',
          abs(hs[TICK] * k2 - 1) < 1e-10, f'k^2 h_tt = {hs[TICK] * k2:.12f} (h_tt is gauge invariant at k_t = 0)')

    # (3) lattice static response, k-space and position space, kappa = 1
    for name, car in cars.items():
        dev = []
        for kd in (np.array([1, 0, 0, 0.]), np.array([1, 1, 0, 0.]) / np.sqrt(2), np.array([1, 1, 1, 0.]) / np.sqrt(3)):
            kk = 0.02 * kd; s = -0.5 * np.linalg.pinv(car.K(kk)[0], rcond=1e-7, hermitian=True) @ e
            dev.append(np.real(s[TICK]) * (kk @ kk))
        check(f'(3) {name}: sampled static k^2 h_tt near E/kappa along three spatial directions at |k| = .02', max(abs(np.array(dev) - 1)) < 2e-3,
              ', '.join(f'{x:.5f}' for x in dev))
    L = 24
    x = np.minimum(np.arange(L), L - np.arange(L)); X3 = np.sqrt(x[:, None, None] ** 2 + x[None, :, None] ** 2 + x[None, None, :] ** 2)
    def blk(f): return sum(np.roll(f, (i, j, k), (0, 1, 2)) for i in (0, 1) for j in (0, 1) for k in (0, 1)) / 8
    def fit(h, g):
        m = (X3 >= 4) & (X3 <= 9); A = np.stack([8 * np.pi * g[m], np.ones(m.sum())], 1)
        co, *_ = np.linalg.lstsq(A, h[m], rcond=None); res = h[m] - A @ co
        return co[0], np.sqrt(np.mean(res ** 2)) / np.sqrt(np.mean((h[m] - h[m].mean()) ** 2))
    for name in cars:
        hx, gx = static_response(cars[name], L)
        c_raw, q_raw = fit(hx, gx); c_blk, q_blk = fit(blk(hx), blk(gx))
        if name == 'coned D4':
            check(f'(3) coned D4: position-space h_tt on the {L}^3 torus, fit h = 8 pi c E G_lattice(r) + const over 4 <= r <= 9, gives c = 1/(8 pi) = {1 / (8 * np.pi):.5f} within 2%',
                  abs(c_raw * 8 * np.pi - 1) < 0.02 and q_raw < 0.05, f'c = {c_raw:.5f}, relative residual {q_raw:.3f}; 2^3-block averaged c = {c_blk:.5f}')
            self_kc = hx[0, 0, 0]
        else:
            check(f'(3) Kuhn cubic: raw position-space h_tt is dominated by soft zone-boundary modes; after 2^3 block averaging the fit gives c = 1/(8 pi) within 5%',
                  abs(c_blk * 8 * np.pi - 1) < 0.05 and q_raw > 0.2, f'raw c = {c_raw:.5f} (relative residual {q_raw:.2f}); block-averaged c = {c_blk:.5f} (residual {q_blk:.3f})')

    # (4) dressing scales as E^2/kappa; bare deposit action has no G
    Es = np.array([0.1, 0.25, 0.5]); kappas = np.array([1.0, 2.0])
    U = np.array([[-0.25 * E * (E * self_kc / kap) for E in Es] for kap in kappas])   # on-shell (1/2) x linear term, h_tt(0) for E = kappa = 1
    sc = U / (Es[None] ** 2 / kappas[:, None])
    check('(4) on-shell dressing of a static deposit per tick is -(1/4) E h_tt(0) = X E^2/kappa with one lattice constant X',
          np.ptp(sc) < 1e-12, f'X = {sc[0, 0]:.5f} (coned D4, {L}^3 torus); a "|dressing| = 1 quantum" rule gives kappa = |X| E^2, which depends on E (algebraic scaling, not a new result)')

    print('supplied: carriers, flat Euclidean lengths, tick index 3, metric reading, signed source/action, units, kappa, torus, radii, rcond; EH matching is an additional condition.')
    print('computed here: finite sampled Regge/EH ratios and torus response fits, including raw Kuhn discrepancy; conditional algebra G = a^2/(8 pi kappa) if EH matching, metric/source and unit conventions are supplied.')
    print('not established: continuum convergence, carrier independence, universal 1/r law, kappa selection, physical rung, Newton constant or Planck identification.')
    print('elapsed_seconds', round(time.monotonic() - _T0, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
