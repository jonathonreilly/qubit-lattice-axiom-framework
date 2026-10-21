#!/usr/bin/env python3
"""One-qubit-per-site split-step walk on Z^3 as a tick update for relays.
Each tick the site qubit takes substeps along x, y, z; in substep i its sigma_i = +-1 parts move one site toward +-i.
Checks: mean step per axis equals the group velocity and the burn-and-turn source equals eps v v (shear included)
for plane waves; a Brillouin-zone scan of gapless points and their chiralities.
No physical matter content, derivation of the update or claim of exact cubic covariance is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = ('docs/ONE_QUBIT_SPLIT_STEP_WALK_RELAY_SOURCE_AND_DOUBLERS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

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
from scipy.linalg import expm
from scipy.ndimage import gaussian_filter, gaussian_filter1d

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def plane_wave_tensors(P, dirs, eps):
    """burn and turn totals per front per tick for Born odds P over step directions dirs."""
    P = P / P.sum(); burn = eps * np.einsum('d,di,dj->ij', P, dirs, dirs); turn = np.zeros_like(burn); action = 0.0
    for a in range(len(P)):
        for b in range(len(P)):
            if a != b:
                fl = 2 * eps * P[a] * P[b]; dd = dirs[b] - dirs[a]; turn -= fl * np.outer(dd, dd) / 4; action += fl * (dd @ dd) / 4
    return burn, turn, action


# ---------------- walks on Z^3: U(k) = diag(exp(-i k.d)) C
def cubic_walk(dirs, M, th):
    C = expm(-1j * th * M)
    def U(k): return np.diag(np.exp(-1j * dirs @ k)) @ C
    return C, U


def track(U, kd, km, start, n=60):
    """follow one eigenband from |k| = .02 along the ray kd, starting from the eigenvector chosen by start(om)."""
    kd = np.asarray(kd, float) / np.linalg.norm(kd); ks = np.linspace(0.02, km, n)
    w, V = np.linalg.eig(U(ks[0] * kd)); om = -np.angle(w); i = start(om); v = V[:, i]; o = om[i]
    for kk in ks[1:]:
        w, V = np.linalg.eig(U(kk * kd)); j = int(np.argmax(abs(V.conj().T @ v))); v = V[:, j]; o = -np.angle(w[j])
    return o, v / np.linalg.norm(v)


def group_velocity(U, kd, km, start):
    kd = np.asarray(kd, float) / np.linalg.norm(kd); k0 = km * kd; h = 1e-5; out = []
    eps, u0 = track(U, kd, km, start)
    for e in np.eye(3):
        vals = []
        for sgn in (1, -1):
            w, V = np.linalg.eig(U(k0 + sgn * h * e)); j = int(np.argmax(abs(V.conj().T @ u0))); vals.append(-np.angle(w[j]))
        out.append((vals[0] - vals[1]) / (2 * h))
    return eps, u0, np.array(out)


import itertools
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1., -1]).astype(complex)
AL = [SX, SY, SZ]
SS = np.array(list(itertools.product((1, -1), repeat=3)), float)


def S(i, k):
    w, V = np.linalg.eigh(AL[i]); return V @ np.diag(np.exp(-1j * k[i] * w)) @ V.conj().T


def U(k): return S(2, k) @ S(1, k) @ S(0, k)


def main():
    rows = []
    for kd, km in (((1, 0, 0), 0.1), ((1, 1, 0), 0.1), ((1, 1, 1), 0.1), ((2, 1, 0), 0.2), ((0.3, 0.5, 0.8), 0.15)):
        kd = np.array(kd, float) / np.linalg.norm(kd); k = km * kd
        w, V = np.linalg.eig(U(k)); om = -np.angle(w); i = int(np.argmax(om)); u = V[:, i] / np.linalg.norm(V[:, i]); eps = om[i]
        def omb(kk):
            w2, V2 = np.linalg.eig(U(kk)); return -np.angle(w2[int(np.argmax(abs(V2.conj().T @ u)))])
        h = 1e-6; v = np.array([(omb(k + h * e) - omb(k - h * e)) / (2 * h) for e in np.eye(3)])
        st = u.copy(); mean = []
        for a in range(3):
            mean.append(np.real(np.vdot(st, AL[a] @ st))); st = S(a, k) @ st
        mean = np.array(mean); q = (1 + mean) / 2
        Q = np.array([np.prod([q[a] if s[a] > 0 else 1 - q[a] for a in range(3)]) for s in SS])
        burn = eps * np.einsum('d,di,dj->ij', Q, SS, SS); turn = np.zeros((3, 3))
        for a in range(8):
            for b in range(8):
                if a != b: dd = SS[b] - SS[a]; turn -= 2 * eps * Q[a] * Q[b] * np.outer(dd, dd) / 4
        rows.append((km, kd, eps, np.linalg.norm(v), np.abs(mean - v).max(), np.abs(burn + turn - eps * np.outer(v, v)).max(), np.abs(burn - eps * np.outer(v, v)).max()))
    check('plane waves: mean step per axis equals the group velocity', max(r[4] for r in rows) < 1e-8, f'max |mean step - v| {max(r[4] for r in rows):.1e}')
    check('plane waves: burns + turns (independent axis signs, redraw 2 eps) equal eps v v including shear; burns alone do not',
          max(r[5] for r in rows) < 1e-8 and min(r[6] for r in rows) > 1e-3,
          f'max |burns+turns - eps v v| {max(r[5] for r in rows):.1e}; burns alone >= {min(r[6] for r in rows):.1e}; ' + '; '.join(f'|k| {r[0]} along {np.round(r[1], 2)}: eps {r[2]:.5f}, |v| {r[3]:.4f}' for r in rows))
    aniso = max(abs(r[2] / r[0] - 1) for r in rows)
    check('long-wavelength dispersion: eps/|k| within 3% of one on the sampled directions', aniso < 0.03, f'max |eps/|k| - 1| {aniso:.2%}')
    n = 48; grid = 2 * np.pi * np.arange(n) / n - np.pi; found = []
    for a in grid:
        for b in grid:
            for c in grid:
                k = np.array([a, b, c]); om = -np.angle(np.linalg.eigvals(U(k)))
                if np.min(abs(om)) < 0.03 and all(np.linalg.norm(((k - p + np.pi) % (2 * np.pi)) - np.pi) > 0.3 for p in found): found.append(k)
    def chir(k0):
        hh = 1e-4; M = np.zeros((3, 3))
        H = lambda k: 1j * (U(k) - U(k).conj().T) / 2
        for j in range(3):
            e = np.zeros(3); e[j] = hh; D = (H(k0 + e) - H(k0 - e)) / (2 * hh)
            for i, s in enumerate(AL): M[i, j] = np.real(np.trace(D @ s)) / 2
        return int(np.sign(np.linalg.det(M)))
    ch = [chir(p) for p in found]
    check('Brillouin-zone scan: eight zero-quasi-energy cones, four of each chirality',
          len(found) == 8 and sum(ch) == 0 and ch.count(1) == 4, ', '.join(f'{np.round(p / np.pi, 2)}: {c:+d}' for p, c in zip(found, ch)))
    print('per_site: the walk (substep order x, y, z), momenta, scan grid and chirality evaluation are supplied choices.')
    print('lattice_wide: no physical matter content, derivation of the update or exact cubic covariance is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
