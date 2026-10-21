#!/usr/bin/env python3
"""Mass on a two-chirality split-step cell: which mass terms gap every cone.
L walk U_L(k) = S_z S_y S_x, R walk U_L(-k). Same-site mass m couples L(k) and R(k); the staggered mass
M (-1)^(x+y+z) couples L(k) and R(k+Q), Q = pi(1,1,1). Checks: cone sets and chiralities, gaps with m alone and
with m and M, the minimum over the zone, and the long-wavelength dispersion. No matter content is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/TWO_CHIRALITY_SPLIT_STEP_MASS_GAPS_EVERY_CONE_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

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


def main():
    cL = cones(UL); cR = cones(lambda k: UL(-k))
    key = lambda p: tuple(np.round((((p + np.pi) % (2 * np.pi)) - np.pi) / np.pi * 2).astype(int) % 4)
    sL = {key(p): chir(UL, p) for p in cL}; sR = {key(p): chir(lambda k: UL(-k), p) for p in cR}
    shared = set(sL) & set(sR); onlyL = set(sL) - set(sR)
    check('cone sets: L and R share four momenta with opposite chirality; L has four more that R lacks',
          len(cL) == 8 and len(cR) == 8 and len(shared) == 4 and all(sL[s] == -sR[s] for s in shared) and len(onlyL) == 4,
          f'shared {sorted(shared)}; L only {sorted(onlyL)} (units of pi/2, mod 4)')
    grid = np.linspace(-np.pi, np.pi, 25)
    def zone_min(t1, t2):
        return min(np.min(abs(np.angle(np.linalg.eigvals(U8(np.array([a_, b_, c_]), t1, t2))))) for a_ in grid for b_ in grid for c_ in grid)
    m_only = zone_min(0.05, 0.0); both = zone_min(0.05, 0.5); both2 = zone_min(0.02, 1.0)
    check('same-site mass alone leaves zero-quasi-energy points; with the staggered mass the minimum gap over the zone equals the same-site mass',
          m_only < 1e-6 and abs(both - 0.05) < 2e-3 and abs(both2 - 0.02) < 2e-3, f'm=.05, M=0: {m_only:.1e}; m=.05, M=.5: {both:.4f}; m=.02, M=1: {both2:.4f} (25^3 grid)')
    rows = []
    for kd in ((1, 0, 0), (1, 1, 0), (1, 1, 1)):
        kd = np.array(kd, float) / np.linalg.norm(kd)
        for km in (0.02, 0.04):
            eps = np.sort(abs(np.angle(np.linalg.eigvals(U8(km * kd, 0.02, 0.5)))))[0]; rows.append((kd, km, eps, np.sqrt(0.02 ** 2 + (np.cos(0.5) * km) ** 2)))
    worst = max(abs(r[2] / r[3] - 1) for r in rows)
    check('light band near k=0 follows sqrt(m^2 + cos(M)^2 k^2) within 1.5% for |k| <= 2m on three directions (the staggered mass M slows it uniformly)', worst < 0.015, f'max relative deviation {worst:.2%}')
    print('per_site: two chirality components per site, the substep order, the momentum-reversed R walk and the two mass terms are supplied choices.')
    print('lattice_wide: no matter content, one-qubit realization, exact cubic covariance or physical mass values are established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
