#!/usr/bin/env python3
"""Finite diagnostics for a supplied eight-mode block walk and CAR/Fock reading.
The paired note proves conditional matrix factorization and differentiable-
eigenbranch velocity identities. Finite grid minima do not establish a global
gap, continuum Dirac identification, physical fermions or a record source.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/BLOCK_OF_EIGHT_ONE_MODE_SITES_CARRIES_A_GAPPED_DIRAC_BAND_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED = time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 300-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np, sympy as sp
from scipy.linalg import expm

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1., -1]).astype(complex); AL = [SX, SY, SZ]


def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for i in range(3): R[i, perm[i]] = sg[i]
            if np.isclose(np.linalg.det(R), 1): out.append(R)
    return out


def spin_of(R):
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if np.isclose(ang, 0): return np.eye(2)
    w, vecs = np.linalg.eig(R); ax = np.real(vecs[:, np.argmin(abs(w - 1))]); ax /= np.linalg.norm(ax)
    for s in (1, -1):
        V = np.cos(ang / 2) * np.eye(2) - 1j * np.sin(ang / 2) * s * (ax[0] * SX + ax[1] * SY + ax[2] * SZ)
        if all(np.allclose(V @ AL[j] @ V.conj().T, sum(R[i, j] * AL[i] for i in range(3))) for j in range(3)): return V
    raise RuntimeError('no spin rotation')


def S(i, k): return np.cos(k[i]) * np.eye(2) - 1j * np.sin(k[i]) * AL[i]
def UL(k): return S(2, k) @ S(1, k) @ S(0, k)
Q = np.full(3, np.pi); I2 = np.eye(2)


def U8(k, t1, t2):
    D = np.zeros((8, 8), complex)
    D[0:2, 0:2] = UL(k); D[2:4, 2:4] = UL(-k); D[4:6, 4:6] = UL(k + Q); D[6:8, 6:8] = UL(-k - Q)
    Mm = np.zeros((8, 8))
    for (a_, b_) in ((0, 2), (4, 6)): Mm[a_:a_ + 2, b_:b_ + 2] = t1 * I2; Mm[b_:b_ + 2, a_:a_ + 2] = t1 * I2
    for (a_, b_) in ((0, 6), (4, 2)): Mm[a_:a_ + 2, b_:b_ + 2] = t2 * I2; Mm[b_:b_ + 2, a_:a_ + 2] = t2 * I2
    return D @ expm(-1j * Mm)


def cones(U, n=40):
    grid = 2 * np.pi * np.arange(n) / n - np.pi; found = []
    for a_ in grid:
        for b_ in grid:
            for c_ in grid:
                k = np.array([a_, b_, c_])
                if np.min(abs(np.angle(np.linalg.eigvals(U(k))))) < 0.03 and all(np.linalg.norm(((k - p + np.pi) % (2 * np.pi)) - np.pi) > 0.3 for p in found): found.append(k)
    return found


def chir(U, k0):
    h = 1e-4; M = np.zeros((3, 3)); Hf = lambda k: 1j * (U(k) - U(k).conj().T) / 2
    for j in range(3):
        e = np.zeros(3); e[j] = h; D = (Hf(k0 + e) - Hf(k0 - e)) / (2 * h)
        for i, s in enumerate(AL): M[i, j] = np.real(np.trace(D @ s)) / 2
    return int(np.sign(np.linalg.det(M)))


def U8b(K, t1, t2):
    D = np.zeros((8, 8), complex); D[0:2, 0:2] = UL(K); D[2:4, 2:4] = UL(-K); D[4:6, 4:6] = -UL(K); D[6:8, 6:8] = -UL(-K)
    Mm = np.zeros((8, 8))
    for (a_, b_) in ((0, 2), (4, 6)): Mm[a_:a_ + 2, b_:b_ + 2] = t1 * I2; Mm[b_:b_ + 2, a_:a_ + 2] = t1 * I2
    for (a_, b_) in ((0, 6), (4, 2)): Mm[a_:a_ + 2, b_:b_ + 2] = t2 * I2; Mm[b_:b_ + 2, a_:a_ + 2] = t2 * I2
    return D @ expm(-1j * Mm)
AL8 = [np.kron(np.diag([1, -1, 1, -1]), A) for A in AL]   # L:+sigma, R:-sigma (U_L(-K) moves sigma=+1 toward -i), L':+, R':-
def substeps(K):
    Mm = np.zeros((8, 8))
    for (a_, b_) in ((0, 2), (4, 6)): Mm[a_:a_ + 2, b_:b_ + 2] = .05 * I2; Mm[b_:b_ + 2, a_:a_ + 2] = .05 * I2
    for (a_, b_) in ((0, 6), (4, 2)): Mm[a_:a_ + 2, b_:b_ + 2] = .5 * I2; Mm[b_:b_ + 2, a_:a_ + 2] = .5 * I2
    return expm(-1j * Mm)
def S8(i, K):
    w, V = np.linalg.eigh(AL8[i]); return V @ np.diag(np.exp(-1j * K[i] * w)) @ V.conj().T
sgn = np.diag([1, 1, 1, 1, -1, -1, -1, -1]).astype(complex)
Ub = lambda K: sgn @ S8(2, K) @ S8(1, K) @ S8(0, K) @ substeps(K)


def main():
    rng = np.random.default_rng(1); worst = 0.0
    for _ in range(50):
        K = rng.uniform(-np.pi, np.pi, 3)
        worst = max(worst, np.max(abs(np.sort(np.angle(np.linalg.eigvals(U8b(K, .05, .5)))) - np.sort(np.angle(np.linalg.eigvals(U8(K, .05, .5)))))))
    check('the block-local eight-mode update has the same spectrum as the momentum-shifted form', worst < 1e-12, f'max difference {worst:.1e} over 50 random block momenta')
    g = np.linspace(-np.pi, np.pi, 25)
    mn = min(np.min(abs(np.angle(np.linalg.eigvals(U8b(np.array([a_, b_, c_]), .05, .5))))) for a_ in g for b_ in g for c_ in g)
    check('25^3 sampled minimum agrees with .05 at m=.05,M=.5; no global lower bound', abs(mn - 0.05) < 2e-3, f'min |quasi-energy| {mn:.4f} on 25^3')
    check('the update factors as block-local mass, three block substeps and a sign on L\', R\'', np.allclose(Ub(np.array([.3, -.2, .5])), U8b(np.array([.3, -.2, .5]), .05, .5)))
    rows = []
    for kd, km in (((1, 1, 0), 0.04), ((1, 2, 3), 0.05), ((1, 0.15, 0.05), 0.03)):
        kd = np.array(kd, float) / np.linalg.norm(kd); K = km * kd; w, V = np.linalg.eig(Ub(K)); om = -np.angle(w)
        i = int(np.argmin(np.where(om > 0, om, 9))); u = V[:, i] / np.linalg.norm(V[:, i])
        def omb(KK):
            w2, V2 = np.linalg.eig(Ub(KK)); return -np.angle(w2[int(np.argmax(abs(V2.conj().T @ u)))])
        h = 1e-6; v = np.array([(omb(K + h * e) - omb(K - h * e)) / (2 * h) for e in np.eye(3)])
        st = substeps(K) @ u; mean = []
        for a_ in range(3): mean.append(np.real(np.vdot(st, AL8[a_] @ st))); st = S8(a_, K) @ st
        rows.append(np.abs(np.array(mean) - v).max())
    check('three supplied momenta: staged mean step agrees with tracked eigenphase derivative; no physical source identification', max(rows) < 1e-6, f'max |mean step - v| {max(rows):.1e}')
    print('per_site: CAR/Fock interpretation and eight labelled block modes, the assignment of block modes to L, R, L\', R\', the substep order and the two masses are supplied choices.')
    print('lattice_wide: no matter content, exact cubic covariance, removal of sublattice copies or physical masses is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
