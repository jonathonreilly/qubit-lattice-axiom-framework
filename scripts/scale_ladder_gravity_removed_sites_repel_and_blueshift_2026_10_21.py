#!/usr/bin/env python3
"""Removed sites as a medium: a supplied 2D lattice Klein-Gordon wave with a disk in which a fraction of sites
is removed from the flow (amplitude held at zero, links to them deleted). Packets of zero and nonzero mass pass
the disk at fixed impact parameter; their sideways shift is compared with the no-removal run. The lowest mode of
a region containing the disk is compared with and without removals. No gravity field, physical identification or
derivation of the record-removal clause is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = ('docs/SCALE_LADDER_GRAVITY_REMOVED_SITES_REPEL_AND_BLUESHIFT_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

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
    return float((E[mk] * Y[mk]).sum() / E[mk].sum()), float(E[mk].sum() / E.sum()), vg


def lowest(f, seed=9):
    rr = np.random.default_rng(seed); n = 61; xs = np.arange(n) - 30; XX, YY = np.meshgrid(xs, xs, indexing='ij')
    inside = (np.hypot(XX, YY) < 28) & ~((np.hypot(XX, YY) < 20) & (rr.random((n, n)) < f))
    idx = -np.ones((n, n), int); idx[inside] = np.arange(inside.sum()); rows, cols, vals = [], [], []
    for (i, j) in zip(*np.where(inside)):
        rows.append(idx[i, j]); cols.append(idx[i, j]); vals.append(4.0)
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ii, jj = i + di, j + dj
            if 0 <= ii < n and 0 <= jj < n and inside[ii, jj]: rows.append(idx[i, j]); cols.append(idx[ii, jj]); vals.append(-1.0)
    A = sp.csr_matrix((vals, (rows, cols))); return float(spl.eigsh(A, k=1, sigma=0, which='LM')[0][0])


def main():
    fs = (0.005, 0.01, 0.02)
    for m, k in ((0.0, 0.5), (0.5, 0.95)):
        c0, d0, vg = pass_packet(m, k, removed_mask(0.0)); shifts = []
        for f in fs:
            c, d, _ = pass_packet(m, k, removed_mask(f)); shifts.append(c - c0)
        check(f'mass {m}: the packet is shifted away from the disk at every removal fraction', min(shifts) > 1.0,
              f'group speed {vg:.3f}; detected fraction without removals {d0:.3f}; shifts at ' + ', '.join(f'{f:.1%}: {s:+.2f}' for f, s in zip(fs, shifts)) + ' sites (positive = away)')
    m = 0.1; base = np.sqrt(m * m + lowest(0.0)); rel = [np.sqrt(m * m + lowest(f)) / base - 1 for f in fs]
    check('the lowest mode of a region containing the disk rises in frequency as sites are removed', rel[0] > 0 and rel[0] < rel[1] < rel[2],
          f'no removals {base:.5f} (rest frequency {m}); relative change ' + ', '.join(f'{f:.1%}: {r:+.2%}' for f, r in zip(fs, rel)))
    print('per_site: the Klein-Gordon discretization, removal rule (amplitude zero, links deleted), masses and momenta are supplied choices.')
    print('per_block: geometry, impact parameter, seeds, removal fractions, time step and detection window are fixed in this source.')
    print('lattice_wide: no gravity field, long-range response, physical identification or derivation of the record-removal clause is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
