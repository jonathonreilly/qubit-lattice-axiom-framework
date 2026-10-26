#!/usr/bin/env python3
"""Fixed seeded Dirichlet-grounding diagnostics for a supplied scalar lattice wave.
Transmitted u-squared centroid changes and scalar confined-mode frequencies are numerical
readouts only, not physical forces or clocks. Grounding retains the parent diagonal.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = ('docs/SCALE_LADDER_GRAVITY_REMOVED_SITES_REPEL_AND_BLUESHIFT_BOUNDED_THEOREM_NOTE_2026-10-21.md',)

import sys, os, signal, time, json, hashlib
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
import scipy.sparse as sp, scipy.sparse.linalg as spl

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


LX, LY = 360, 200
X, Y = np.meshgrid(np.arange(LX) - 180.0, np.arange(LY) - 100.0, indexing='ij')
R = np.hypot(X - 60, Y)


def removed_mask(f, seed=5):
    rng = np.random.default_rng(seed); live = np.ones((LX, LY), bool)
    if f > 0: live[(R < 20) & (rng.random((LX, LY)) < f)] = False
    return live


def pass_packet(m, k, live, b=26.0, dt=0.25):
    w = np.sqrt(m * m + 2 * (1 - np.cos(k))); vg = np.sin(k) / w; T = 260 / vg
    env = np.exp(-((X + 100) ** 2) / (2 * 14.0 ** 2) - (Y - b) ** 2 / (2 * 10.0 ** 2))
    u = env * np.cos(k * X) * live; v = w * env * np.sin(k * X) * live
    for _ in range(int(T / dt)):
        lap = sum(np.roll(u, s, a) for a in (0, 1) for s in (1, -1)) - 4 * u
        v += dt * (lap - m * m * u) * live; u += dt * v; u *= live
    E = u * u; mk = X > 120
    assert np.isfinite(E).all() and E[mk].sum() > 0 and E.sum() > 0
    return float((E[mk] * Y[mk]).sum() / E[mk].sum()), float(E[mk].sum() / E.sum()), vg


def lowest(f, seed=9):
    rr = np.random.default_rng(seed); n = 61; xs = np.arange(n) - 30; XX, YY = np.meshgrid(xs, xs, indexing='ij')
    inside = (np.hypot(XX, YY) < 28) & ~((np.hypot(XX, YY) < 20) & (rr.random((n, n)) < f))
    print(f'spectral probability={f} live_count={inside.sum()} grounded_inside_count={np.count_nonzero(np.hypot(XX,YY)<28)-inside.sum()}')
    idx = -np.ones((n, n), int); idx[inside] = np.arange(inside.sum()); rows, cols, vals = [], [], []
    for (i, j) in zip(*np.where(inside)):
        rows.append(idx[i, j]); cols.append(idx[i, j]); vals.append(4.0)
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ii, jj = i + di, j + dj
            if 0 <= ii < n and 0 <= jj < n and inside[ii, jj]: rows.append(idx[i, j]); cols.append(idx[ii, jj]); vals.append(-1.0)
    A = sp.csr_matrix((vals, (rows, cols))); return float(spl.eigsh(A, k=1, sigma=0, which='LM')[0][0])


def main():
    fs = (0.005, 0.01, 0.02)
    config = dict(grid=[LX, LY], periodic=True, packet_seed=5, spectral_seed=9,
                  probabilities=fs, mass_momentum_pairs=((0.0, 0.5), (0.5, 0.95)),
                  spectral_mass=0.1, dt=0.25, travel_parameter=260,
                  packet_center=(-100,26), widths=(14,10), grounding_center=(60,0),
                  grounding_radius=20, detection='X>120', spectral_box=61,
                  spectral_outer_radius=28, integrator='velocity-first symplectic Euler')
    encoded = json.dumps(config, sort_keys=True)
    print('configuration:', encoded)
    print('configuration_sha256:', hashlib.sha256(encoded.encode()).hexdigest())
    # Independent sparse incidence/recurrence results, rounded to 2 decimals.
    # Half a unit of the displayed final decimal is a rounding comparison,
    # not a convergence tolerance or a mathematical proof.
    expected_shifts = ((3.96, 9.98, 14.50), (3.86, 5.63, 9.01))
    for case, (m, k) in enumerate(config['mass_momentum_pairs']):
        c0, d0, vg = pass_packet(m, k, removed_mask(0.0)); shifts = []; detected = []
        for f in fs:
            live = removed_mask(f)
            c, d, _ = pass_packet(m, k, live); shifts.append(c - c0); detected.append(d)
            print(f'packet mass={m} probability={f} grounded_count={np.count_nonzero(~live)} detected_fraction={d:.9f} centroid={c:.9f}')
        steps = int((260/vg)/.25)
        check(f'mass {m}: fixed transmitted u-squared centroid changes match independent rounded values',
              np.all(np.abs(np.array(shifts)-expected_shifts[case]) <= .005),
              f'semidiscrete group speed {vg:.9f}; steps {steps}; time {steps*.25}; baseline detected fraction {d0:.9f}; baseline centroid {c0:.9f}; shifts {shifts}')
        check(f'mass {m}: finite detected fractions and supplied-scheme stability bound',
              all(0 < d <= 1 for d in [d0]+detected) and .25*np.sqrt(8+m*m)<2)
    m = config['spectral_mass']; eigenvalues = [lowest(f) for f in (0.0,)+fs]
    base = np.sqrt(m*m+eigenvalues[0]); rel = np.sqrt(m*m+np.array(eigenvalues[1:]))/base-1
    # Independent smallest-algebraic solve, rounded to 5 decimal places.
    check('fixed grounded-disk relative frequencies match independent rounded values',
          np.all(np.abs(rel-np.array([.05903,.23219,.49803])) <= .000005),
          f'eigenvalues {eigenvalues}; baseline frequency {base:.9f}; mass {m}; relative changes {rel}')
    check('nested fixed masks have nondecreasing lowest eigenvalues', np.all(np.diff(eigenvalues)>=0))
    chain = np.array([[1.,-1,0],[-1,2,-1],[0,-1,1]])
    grounded = np.linalg.eigvalsh(chain[np.ix_([0,2],[0,2])])
    deleted = np.linalg.eigvalsh(np.zeros((2,2)))
    check('three-path grounding differs from incident-edge deletion',
          np.array_equal(grounded,[1.,1.]) and np.array_equal(deleted,[0.,0.]),
          f'grounded {grounded}; induced deletion {deleted}')
    print('per_site: zero amplitude is Dirichlet grounding with unchanged parent diagonal, not incident-edge deletion.')
    print('per_block: all geometry, initial data, seeds, masses, time stepping and readouts are supplied fixed model inputs.')
    print('lattice_wide: the finite diagnostics assign no force, physical clock, matter density or gravitational mechanism.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
