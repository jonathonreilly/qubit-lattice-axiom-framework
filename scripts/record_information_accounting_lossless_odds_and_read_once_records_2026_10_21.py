#!/usr/bin/env python3
"""Information accounting for a supplied unitary walk with one record formation.
(1) supplied unitary ticks preserve the norm and purity of the odds, while the position Shannon entropy changes;
(2) Bayesian conditioning on a site record: H(X) = sum_r p(r) H(X|r) + H(R) to rounding;
(3) purified record: a controlled flip onto a record qubit keeps the joint state pure, and the record qubit's
    entropy equals H(R).
No physical information law, thermodynamic reading or derivation of the read-once clause is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/RECORD_INFORMATION_ACCOUNTING_LOSSLESS_ODDS_AND_READ_ONCE_RECORDS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED = time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 120-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def H(p):
    p = np.asarray(p, float); p = p[p > 0]; return float(-np.sum(p * np.log2(p)))


def main():
    N, th, T = 240, 0.3, 60; c, s = np.cos(th), np.sin(th); x = np.arange(N)
    env = np.exp(-(x - 100) ** 2 / (2 * 8.0 ** 2)); R = env * np.exp(0.5j * x); Lc = 0.4j * env * np.exp(0.5j * x)
    nr = np.sqrt(np.sum(abs(R) ** 2 + abs(Lc) ** 2)); R, Lc = R / nr, Lc / nr
    H0 = H(abs(R) ** 2 + abs(Lc) ** 2)
    for _ in range(T):
        R, Lc = c * R - 1j * s * Lc, -1j * s * R + c * Lc; R, Lc = np.roll(R, 1), np.roll(Lc, -1)
    psi = np.concatenate([R, Lc]); rho = np.outer(psi, psi.conj())
    norm_err = abs(np.sum(abs(psi) ** 2) - 1); purity_err = abs(np.real(np.trace(rho @ rho)) - 1)
    P = abs(R) ** 2 + abs(Lc) ** 2; H1 = H(P)
    check('supplied unitary ticks keep the state normalised and pure, while the position Shannon entropy changes',
          norm_err < 1e-12 and purity_err < 1e-12 and abs(H1 - H0) > 0.1,
          f'norm error {norm_err:.1e}, purity error {purity_err:.1e}; position entropy {H0:.4f} -> {H1:.4f} bits over {T} ticks')
    worst = 0.0; rep = []
    for j in (int(np.argmax(P)), int(np.argmax(P)) + 7, int(np.argmax(P)) - 15):
        p1 = P[j]; pr = [p1, 1 - p1]
        HX_given = [0.0, H(np.where(x == j, 0, P) / (1 - p1))]
        lhs = H(P); rhs = pr[0] * HX_given[0] + pr[1] * HX_given[1] + H(pr); worst = max(worst, abs(lhs - rhs))
        rep.append(f'site {j}: H(X) {lhs:.6f} = {rhs:.6f}, record entropy {H(pr):.4f} bits')
    check('a site record: position Shannon uncertainty falls on average by the record entropy (chain rule for conditioning)', worst < 1e-12, '; '.join(rep))
    j = int(np.argmax(P)); A = np.zeros((2 * N, 2), complex)
    for a in range(2 * N):
        site = a % N; A[a, 1 if site == j else 0] = psi[a]
    joint = A.reshape(-1); rec = A.T @ A.conj()
    ev = np.clip(np.linalg.eigvalsh(rec), 0, None); Srec = H(ev); purity_joint = abs(np.vdot(joint, joint)) ** 2
    check('purified record: the joint pure state stays normalised and the record qubit carries the record entropy as entanglement',
          abs(purity_joint - 1) < 1e-12 and abs(Srec - H([P[j], 1 - P[j]])) < 1e-12,
          f'joint pure-state purity {purity_joint:.12f}; record-qubit entropy {Srec:.6f} vs H(R) {H([P[j], 1 - P[j]]):.6f} bits')
    print('per_site: the walk, packet, record sites and the controlled-flip purification are supplied choices.')
    print('lattice_wide: the identities are standard (unitarity, the conditioning chain rule, Schmidt decomposition); no physical information law is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
