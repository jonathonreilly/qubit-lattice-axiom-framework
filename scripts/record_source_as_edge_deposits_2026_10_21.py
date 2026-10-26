#!/usr/bin/env python3
"""Finite diagnostics for supplied ensemble weights and signed D4 tensor span.
Step weights eps P_a and ordered-pair weights 2 eps P_a P_b multiply a chord
coefficient -1/4; these are not derived realized-turn probabilities. The note
proves conditional covariance cancellation and exact signed span. eps is the
chosen eigenphase, v a differentiable-branch derivative; no physical source or
geometry response is identified.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/RECORD_SOURCE_AS_EDGE_DEPOSITS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED = time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 300-second aggregate cap exceeded; streamed diagnostics retained')
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
    """Supplied ensemble step/chord weights for normalized P; no realized-turn law."""
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


def main():
    th = 0.3
    E6 = np.array([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)], float)
    R6 = np.array([[1.0 if np.allclose(a, -b) else 0 for b in E6] for a in E6]); P6 = np.array([[1.0 if abs(a @ b) < 1e-9 else 0 for b in E6] for a in E6])
    C6, U6 = cubic_walk(E6, R6 - P6 + 2 * np.eye(6), th)
    start6 = lambda om: int(np.where(abs(om - th) < 0.05)[0][np.argmax(om[abs(om - th) < 0.05])])
    worst = 0.0; bad = 1e9; rep = []
    for kd in ((1, 1, 0), (2, 1, 0), (1, 1, 1)):
        eps, u, v = group_velocity(U6, kd, 0.3, start6); P = abs(u) ** 2; P /= P.sum(); T = np.zeros((4, 4)); Tb = np.zeros((4, 4))
        for a_ in range(6):
            s = np.r_[1.0, E6[a_]]; T += eps * P[a_] * np.outer(s, s); Tb += eps * P[a_] * np.outer(s, s)
            for b_ in range(6):
                if a_ != b_: c = np.r_[0.0, E6[b_] - E6[a_]]; T -= 2 * eps * P[a_] * P[b_] * np.outer(c, c) / 4
        U4 = np.r_[1.0, v]; worst = max(worst, abs(T - eps * np.outer(U4, U4)).max()); bad = min(bad, abs(Tb - eps * np.outer(U4, U4)).max())
        rep.append(f'k along {kd}: T00 {T[0,0]:.5f}, T0x {T[0,1]:+.5f}, Txy {T[1,2]:+.5f}')
    check('three sampled eigenbranches: supplied step/pair weights sum to eps u u, u=(1,v); step-only mismatch in these samples', worst < 1e-8 and bad > 1e-3,
          f'max error {worst:.1e}; steps alone off by >= {bad:.1e}; ' + '; '.join(rep))
    vecs = set()
    for pos in itertools.combinations(range(4), 2):
        for sg in itertools.product((1, -1), repeat=2):
            v = np.zeros(4); v[pos[0]], v[pos[1]] = sg; vecs.add(tuple(v))
    M = np.array([np.outer(v, v)[np.triu_indices(4)] for v in map(np.array, vecs)])
    check('numerical rank illustration: D4 outer products span Sym(4) with real signed coefficients', len(vecs) == 24 and np.linalg.matrix_rank(M) == 10, f'rank {np.linalg.matrix_rank(M)} of 10')
    print('per_site: the walk, coin, eigenphase and band selection, step weights eps P, ordered-pair weights 2 eps Pa Pb, chord coefficient -1/4 and embedding (1,d) are supplied choices.')
    print('lattice_wide: no gravity field equation, edge-length dynamics, coupling value or physical identification is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
