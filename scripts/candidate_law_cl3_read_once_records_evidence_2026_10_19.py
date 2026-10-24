#!/usr/bin/env python3
"""Finite supplied lattice models behind the read-once record proposal (alias CL-3).
Part A: a lossless 1D two-component walk with a position record at every tick, learning update.
Part B: a 2D double slit with site-hopping burn fronts steered by the wave (Bell-type jump rates),
never revisiting a burnt site; which-slit sorting of readable trails against the Englert bound.
No physical identification, universal dynamics classification or derivation of the clause.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = ('docs/CANDIDATE_LAWS.md', 'docs/CANDIDATE_LAW_CL3_READ_ONCE_RECORDS_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-19.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED = time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 1500-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def part_a():
    """Two-component walk: coin of angle th mixes right/left components, then they shift by +-1."""
    rng = np.random.default_rng(12)
    N, th, T, runs = 3000, 0.05, 600, 200
    c, s = np.cos(th), np.sin(th); kk = 2 * np.pi * np.fft.fftfreq(N); x = np.arange(N)
    A = np.exp(-((kk - 0.06) ** 2) / (2 * 0.004 ** 2)); V2 = np.zeros((2, N), complex)
    for n in np.where(A > 1e-8)[0]:
        k = kk[n]; U = np.diag([np.exp(-1j * k), np.exp(1j * k)]) @ np.array([[c, -1j * s], [-1j * s, c]])
        w, V = np.linalg.eig(U); i = int(np.argmax(-np.angle(w))); V2[:, n] = A[n] * V[:, i] * np.exp(1j * k * N / 2)
    R0, L0 = np.fft.ifft(V2[0]), np.fft.ifft(V2[1]); nr = np.sqrt(np.sum(abs(R0) ** 2 + abs(L0) ** 2)); R0, L0 = R0 / nr, L0 / nr
    def tick(R, L):
        R, L = c * R - 1j * s * L, -1j * s * R + c * L; return np.roll(R, 1), np.roll(L, -1)
    def mean_x(R, L):
        P = abs(R) ** 2 + abs(L) ** 2; return float(np.sum(P * x) / P.sum())
    R, L = R0.copy(), L0.copy(); xs = [mean_x(R, L)]
    for _ in range(T): R, L = tick(R, L); xs.append(mean_x(R, L))
    v_free = (xs[100] - xs[0]) / 100; v_free_late = (xs[600] - xs[500]) / 100
    vg = c * np.sin(0.06) / np.sin(np.arccos(c * np.cos(0.06)))
    check('A1 unrecorded walk keeps its group speed', abs(v_free - vg) < 0.01 and abs(v_free_late - vg) < 0.01,
          f'group speed {vg:.4f}; measured {v_free:.4f} (ticks 0-100), {v_free_late:.4f} (ticks 500-600)')
    X = np.zeros((runs, T + 1))
    Rf, Lf = R, L
    for r in range(runs):
        R, L = R0.copy(), L0.copy(); P = abs(R) ** 2 + abs(L) ** 2; j = rng.choice(N, p=P / P.sum())
        keep = x == j; R, L = np.where(keep, R, 0), np.where(keep, L, 0); nr = np.sqrt(P[j]); R, L = R / nr, L / nr; X[r, 0] = j
        for t in range(T):
            R, L = tick(R, L); P = abs(R) ** 2 + abs(L) ** 2; j = rng.choice(N, p=P / P.sum())
            keep = x == j; R, L = np.where(keep, R, 0), np.where(keep, L, 0); nr = np.sqrt(P[j]); R, L = R / nr, L / nr; X[r, t + 1] = j
    seg = [(X[:, b] - X[:, a]) / (b - a) for a, b in ((0, 100), (100, 200), (500, 600))]
    v = [float(g.mean()) for g in seg]; se = [float(g.std(ddof=1) / np.sqrt(runs)) for g in seg]
    check('A2 a position record at every tick drags the mean speed toward zero (late speed + 3 standard errors < 0.3 group speed)',
          v[0] > v[1] and v[2] + 3 * se[2] < 0.3 * vg,
          f'mean speed {v[0]:.4f}+-{se[0]:.4f} (0-100), {v[1]:.4f}+-{se[1]:.4f} (100-200), {v[2]:.4f}+-{se[2]:.4f} (500-600); {runs} runs, seed 12')
    check('A3 the recorded body spreads more than twice as wide as the unrecorded packet', X[:, -1].std() > 2 * np.sqrt(np.sum((abs(Rf) ** 2 + abs(Lf) ** 2) * (x - xs[-1]) ** 2)),
          f'recorded spread {X[:, -1].std():.1f} sites; unrecorded packet width {np.sqrt(np.sum((abs(Rf) ** 2 + abs(Lf) ** 2) * (x - xs[-1]) ** 2)):.1f} sites at tick {T}')
    print('A-note: the record lifetime does not enter this update. Keeping the conditioned odds after the record ends reproduces A2;')
    print('        restoring the unconditioned odds reproduces A1, i.e. the record then has no later effect.')


def part_b():
    rng = np.random.default_rng(2)
    LX, LY = 130, 161; J = 1.0; cy = LY // 2; SX = 105; dt = 0.04; TT = 95.0
    bins = np.arange(-60, 62, 3); cen = (bins[:-1] > -30) & (bins[:-1] < 30)
    up_half = (bins[:-1] >= 3) & (bins[:-1] < 30); dn_half = (bins[:-1] > -33) & (bins[:-1] <= -6)
    def contrast(h, mask):
        h = np.asarray(h, float)[mask]; return float((h.max() - h.min()) / (h.max() + h.min()))
    xg = np.arange(LX)[:, None]; yg = np.arange(LY)[None, :] - cy
    def setup(slits):
        wall = np.zeros((LX, LY), bool); wall[40, :] = True
        for sl in slits: wall[40, cy + sl - 2: cy + sl + 3] = False
        return wall
    def Hpsi(p, wall):
        q = np.zeros_like(p); q[1:] += p[:-1]; q[:-1] += p[1:]; q[:, 1:] += p[:, :-1]; q[:, :-1] += p[:, 1:]
        q = -J * q; q[wall] = 0; return q
    def step(p, wall):
        k1 = -1j * Hpsi(p, wall); k2 = -1j * Hpsi(p + dt / 2 * k1, wall); k3 = -1j * Hpsi(p + dt / 2 * k2, wall); k4 = -1j * Hpsi(p + dt * k3, wall)
        return p + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    def psi0(wall):
        p = np.exp(-((xg - 18) ** 2) / (2 * 6.0 ** 2) - yg ** 2 / (2 * 30.0 ** 2) + 1j * 1.2 * xg).astype(complex); p[wall] = 0
        return p / np.linalg.norm(p)
    yy = np.arange(LY) - cy; refc = []
    for sl, mask in ((-9, dn_half), (9, up_half)):
        wall = setup([sl]); psi = psi0(wall); flux = np.zeros(LY)
        for _ in range(int(TT / dt)):
            flux += dt * 2 * np.imag(np.conj(psi[SX, :]) * (-J) * psi[SX - 1, :]); psi = step(psi, wall)
        refc.append(contrast(np.histogram(yy, bins, weights=np.maximum(flux, 0))[0], mask))
    check('B1 one slit open: no fringes in its own half of the screen', max(refc) < 0.3, f'contrast {refc[0]:.3f} (lower), {refc[1]:.3f} (upper)')
    wall = setup([-9, 9]); psi = psi0(wall); NW = 3000
    P0 = (np.abs(psi) ** 2).ravel(); idx = rng.choice(LX * LY, NW, p=P0 / P0.sum())
    w = np.stack(np.unravel_index(idx, (LX, LY)), 1)
    burnt = np.zeros((NW, LX, LY), bool); burnt[np.arange(NW), w[:, 0], w[:, 1]] = True
    hit = np.full(NW, np.nan); slit = np.zeros(NW); D4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]; flux = np.zeros(LY)
    for _ in range(int(TT / dt)):
        live = np.isnan(hit); i, j = w[:, 0], w[:, 1]; rho = np.abs(psi[i, j]) ** 2 + 1e-300; rates = np.zeros((NW, 4))
        for d, (dx, dy) in enumerate(D4):
            ii, jj = np.clip(i + dx, 0, LX - 1), np.clip(j + dy, 0, LY - 1)
            cur = 2 * np.imag(np.conj(psi[ii, jj]) * (-J) * psi[i, j]); ok = ~wall[ii, jj] & ~burnt[np.arange(NW), ii, jj]
            rates[:, d] = np.where(ok, np.maximum(cur, 0) / rho, 0)
        tot = rates.sum(1); jump = live & (rng.random(NW) < np.minimum(tot * dt, 1))
        for n in np.where(jump)[0]:
            d = rng.choice(4, p=rates[n] / tot[n]); w[n] += D4[d]; burnt[n, w[n, 0], w[n, 1]] = True
            if w[n, 0] == 40: slit[n] = np.sign(w[n, 1] - cy)
            if w[n, 0] >= SX: hit[n] = w[n, 1] - cy
        flux += dt * 2 * np.imag(np.conj(psi[SX, :]) * (-J) * psi[SX - 1, :]); psi = step(psi, wall)
    ok = ~np.isnan(hit) & (slit != 0); yh = hit[ok]; up = slit[ok] > 0
    wave_c = contrast(np.histogram(yy, bins, weights=np.maximum(flux, 0))[0], cen)
    front_c = contrast(np.histogram(yh, bins)[0] + 1e-9, cen)
    check('B2 both slits: wave flux and front arrivals both show fringes', wave_c > 0.9 and front_c > 0.9,
          f'wave flux contrast {wave_c:.3f}; front contrast {front_c:.3f}; {int(ok.sum())} of {NW} fronts reached x={SX}')
    pa = float(np.mean(yh[up] > 0)); pb = float(np.mean(yh[~up] > 0)); D = abs(pa - pb)
    Va = contrast(np.histogram(yh[up], bins)[0] + 1e-9, up_half); Vb = contrast(np.histogram(yh[~up], bins)[0] + 1e-9, dn_half)
    V = 0.5 * (Va + Vb)
    check('B3 sorting fronts by a readable trail gives which-slit predictability with fringes kept: D^2+V^2 > 1', D > 0.8 and V > 0.8 and D * D + V * V > 1.4,
          f'P(upper half|upper slit) {pa:.3f}, P(upper half|lower slit) {pb:.3f}, D {D:.3f}; group contrasts {Va:.3f}, {Vb:.3f}; D^2+V^2 {D*D+V*V:.3f}')


def main():
    part_a()
    part_b()
    print('per_site: the coin angle, record rule, jump rates and no-revisit constraint are supplied choices.')
    print('per_block: geometries, seeds, packet parameters, bins and contrast windows are fixed in this source.')
    print('lattice_wide: no physical record dynamics, interpretation of the Englert bound beyond this model, or derivation of the clause is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
