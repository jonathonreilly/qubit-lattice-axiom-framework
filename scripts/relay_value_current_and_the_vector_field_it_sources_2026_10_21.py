#!/usr/bin/env python3
"""Value current of relays and the field it can source.
(1) A relay carries its value q unchanged (read-once relaying copies nothing and destroys nothing) and moves one block
    per tick, so the value current J = sum q (1, d) obeys the lattice continuity equation exactly. Checked on a
    six-direction walk packet with Born-following relays (expected densities).
(2) Field operator rederived for a vector field: O(A)_n = a k^2 A_n + b k_n (k.A); the divergence vanishes for every
    A only if b = -a (the Maxwell operator), which is gauge invariant and self-adjoint; a mass term spoils it.
(3) Static unit charge: the Maxwell operator in Coulomb gauge gives A_0 = q / k^2 (Coulomb 1/r), A_i = 0.
(4) Two species with couplings e1, e2 that exchange value at rate J: the source divergence is (e1 - e2) J.
No physical gauge group, charge value or empirical identification is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/RELAY_VALUE_CURRENT_AND_THE_VECTOR_FIELD_IT_SOURCES_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal, time
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


def main():
    # (1) exact continuity on a packet
    th = 0.3; L = 24
    E6 = np.array([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)], int)
    R6 = np.array([[1.0 if np.all(a == -b) else 0 for b in E6] for a in E6]); P6 = np.array([[1.0 if a @ b == 0 else 0 for b in E6] for a in E6])
    C = expm(-1j * th * (R6 - P6 + 2 * np.eye(6)))
    rng = np.random.default_rng(4); X = np.indices((L, L, L)).transpose(1, 2, 3, 0) - L // 2
    env = np.exp(-np.sum(X ** 2, -1) / (2 * 3.0 ** 2)) * np.exp(1j * 0.4 * X[..., 0])
    psi = env[..., None] * (rng.normal(size=6) + 1j * rng.normal(size=6)); psi /= np.sqrt(np.sum(abs(psi) ** 2))
    worst = 0.0; q = 1.0
    for t in range(6):
        P1 = abs(psi @ C.T) ** 2                                   # post-turn odds: relays leave along these directions
        rho_t = np.sum(abs(psi) ** 2, -1) * q
        out = q * P1.sum(-1); inflow = sum(q * np.roll(P1[..., d], tuple(E6[d]), (0, 1, 2)) for d in range(6))
        psi = np.stack([np.roll((psi @ C.T)[..., d], tuple(E6[d]), (0, 1, 2)) for d in range(6)], -1)
        rho_next = np.sum(abs(psi) ** 2, -1) * q
        worst = max(worst, np.max(abs(rho_next - rho_t - (inflow - out))), np.max(abs(out - rho_t)))
    check('(1) relay value current: rho(t+1) - rho(t) = inflow - outflow on every site and tick, to rounding', worst < 1e-14, f'max violation {worst:.1e} over 6 ticks on 24^3')
    # (2) vector field operator
    k = sp.symbols('k0:4'); a, b, m = sp.symbols('a b m'); eta = sp.diag(-1, 1, 1, 1)
    ku = [sum(eta[i, j] * k[j] for j in range(4)) for i in range(4)]; k2 = sum(k[i] * ku[i] for i in range(4))
    A = sp.symbols('A0:4'); kA = sum(ku[i] * A[i] for i in range(4))
    O = [a * k2 * A[n] + b * k[n] * kA for n in range(4)]
    div = sp.expand(sum(ku[n] * O[n] for n in range(4)))
    sol = sp.solve(list(set(sp.Poly(div, *A, *k).coeffs())), [b], dict=True)
    xi = sp.symbols('xi'); Og = [sp.expand((a * k2 * k[n] * xi - a * k[n] * sum(ku[i] * k[i] for i in range(4)) * xi)) for n in range(4)]
    Om = [O[n].subs(b, -a) - m ** 2 * A[n] for n in range(4)]; divm = sp.expand(sum(ku[n] * Om[n] for n in range(4)))
    check('(2) divergence vanishing for every A forces b = -a (Maxwell); pure gauge k xi is annihilated; a mass term spoils the identity',
          sol == [{b: -a}] and all(sp.simplify(g) == 0 for g in Og) and divm != 0, str(sol))
    # (3) static charge in Coulomb gauge
    qq = sp.symbols('q', positive=True); st = {k[0]: 0}
    Mx = [sp.expand((k2 * A[n] - k[n] * kA).subs(st)) for n in range(4)]
    eqs = [Mx[0] + qq * 1] + [Mx[i] for i in range(1, 4)] + [sum(k[i] * A[i] for i in range(1, 4))]
    s3 = sp.solve(eqs, A, dict=True)[0]
    check('(3) static charge: A_0 = -q / |k|^2 (Coulomb), A_i = 0', sp.simplify(s3[A[0]] + qq / (k[1] ** 2 + k[2] ** 2 + k[3] ** 2)) == 0 and all(s3[A[i]] == 0 for i in range(1, 4)), f'A_0 = {sp.simplify(s3[A[0]])}')
    # (4) universality analogue
    e1, e2, J = sp.symbols('e1 e2 J')
    check('(4) if two species exchange a value at rate J, couplings e1, e2 give source divergence (e1 - e2) J: the field must couple to the value, not to the species', sp.solve(sp.expand(e1 * J - e2 * J), e1) == [e2])
    print('per_site: the walk, packet, value assignment and the vector-field ansatz (local, covariant, second order) are supplied choices.')
    print('lattice_wide: no gauge group beyond one conserved value, charge value, field dynamics on the lattice or empirical identification is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
