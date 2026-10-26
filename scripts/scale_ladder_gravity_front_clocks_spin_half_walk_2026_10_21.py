#!/usr/bin/env python3
"""Front clocks on a supplied spin-1/2 split-step walk in 3D.
Candidate tick rates per front per tick, compared with m^2/eps (m/gamma): chirality flips counted by occupation
(product 4 eps pL pR, geometric 2 th sqrt(pL pR)), flips set by the chirality coherence th*psibar psi/psi^dag psi
(mid-coin), and the phase eps - k.v. Plane waves at decreasing coin angle with fixed k/th, then packets.
No physical clock law, gravitational redshift or derivation of the flip rule is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = ('docs/SCALE_LADDER_GRAVITY_FRONT_CLOCKS_SPIN_HALF_WALK_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

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

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex); Z = np.zeros((2, 2))
AL = [np.block([[s, Z], [Z, -s]]) for s in (sx, sy, sz)]; BETA = np.block([[Z, np.eye(2)], [np.eye(2), Z]])


def walk(th):
    Cm = expm(-1j * th * BETA); half = expm(-0.5j * th * BETA)
    def S(i, k):
        w, V = np.linalg.eigh(AL[i]); return V @ np.diag(np.exp(-1j * k[i] * w)) @ V.conj().T
    def U(k): return S(2, k) @ S(1, k) @ S(0, k) @ Cm
    def top2(k):
        w, V = np.linalg.eig(U(k)); om = -np.angle(w); i = np.argsort(om)[-2:]; return om[i], V[:, i]
    return Cm, half, U, top2


def plane_rates(th, k, b, rng=None):
    """tick rates for eigenband b (of the two positive bands) at momentum k."""
    Cm, half, U, top2 = walk(th); m = top2(np.full(3, 1e-9))[0].mean()
    oms, V = top2(k); u = V[:, b] / np.linalg.norm(V[:, b]); eps = oms[b]
    def omb(kk):
        o2, V2 = top2(kk); return o2[int(np.argmax(abs(V2.conj().T @ u)))]
    h = 1e-6 * th; v = np.array([(omb(k + h * e) - omb(k - h * e)) / (2 * h) for e in np.eye(3)])
    mid = half @ u; pL = float(np.sum(abs(u[:2]) ** 2)); pR = 1 - pL
    return dict(target=m * m / eps, coherent=th * float(np.real(np.vdot(mid, BETA @ mid))), phase=eps - k @ v,
                product=4 * eps * pL * pR, geometric=2 * th * np.sqrt(pL * pR), v=np.linalg.norm(v))


def main():
    # ---------------- plane waves: finite decreasing-error observations at fixed k/th as th decreases
    for ratio, kd in ((1.0, (1, 1, 0)), (2.0, (1, 1, 1)), (2.0, (2, 1, 0))):
        kd = np.array(kd, float) / np.linalg.norm(kd); errs = []
        for th in (0.05, 0.025, 0.0125):
            r = [plane_rates(th, ratio * th * kd, b) for b in range(2)]
            errs.append((th, max(abs(x['coherent'] / x['target'] - 1) for x in r), max(abs(x['phase'] / x['target'] - 1) for x in r), r[0]['v']))
        e = [x[1] for x in errs]; p = [x[2] for x in errs]
        check(f'coherent and phase finite errors decrease toward m^2/eps over three th values (k = {ratio:g} th along {np.round(kd, 2)})',
              e[0] > e[1] > e[2] and e[2] < 0.6 * e[0] and e[2] < 0.03 and p[0] > p[1] > p[2] and p[2] < 0.6 * p[0] and p[2] < 0.012,
              '; '.join(f'th={x[0]}: |v| {x[3]:.3f}, coherent error {x[1]:.2%}, phase error {x[2]:.3%}' for x in errs))
    # ---------------- occupation-based flip counts depend on the spin state
    th = 0.05; k = th * np.array([1.0, 0, 0]); Cm, half, U, top2 = walk(th); oms, V = top2(k); Q, _ = np.linalg.qr(V)
    rng = np.random.default_rng(3); prod, geo, coh = [], [], []
    for _ in range(6):
        c = rng.normal(size=2) + 1j * rng.normal(size=2); u = Q @ (c / np.linalg.norm(c)); eps = oms.mean()
        pL = float(np.sum(abs(u[:2]) ** 2)); mid = half @ u
        prod.append(4 * eps * pL * (1 - pL)); geo.append(2 * th * np.sqrt(pL * (1 - pL))); coh.append(th * float(np.real(np.vdot(mid, BETA @ mid))))
    check('on the axis the two positive bands are degenerate: occupation counts vary with the spin state, the coherent rate does not',
          np.ptp(prod) > 1e-3 and np.ptp(geo) > 1e-3 and np.ptp(coh) < 1e-12,
          f'spread over six spin states: product {np.ptp(prod):.2e}, geometric {np.ptp(geo):.2e}, coherent {np.ptp(coh):.1e}')
    # ---------------- packets (L=48, th=.1, k-width 1/10)
    th = 0.1; L = 48; Cm, half, U, top2 = walk(th)
    g = 2 * np.pi * np.fft.fftfreq(L); K = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    def Sk(i, kv):
        w, V = np.linalg.eigh(AL[i]); return np.einsum('ab,nb,cb->nac', V, np.exp(-1j * kv[:, i:i + 1] * w[None, :]), V.conj())
    Uk = Sk(2, K) @ Sk(1, K) @ Sk(0, K) @ Cm; w, V = np.linalg.eig(Uk); om = -np.angle(w); order = np.argsort(om, 1)
    pos = np.take_along_axis(V, order[:, None, -2:], 2)
    epsk = np.take_along_axis(om, order[:, -2:], 1)
    # Keep the original supplied packet construction below. Only its spectral
    # measurement uses orthonormal projectors, including at band degeneracies.
    spectral = pos.copy()
    degenerate = abs(epsk[:, 1] - epsk[:, 0]) < 1e-10
    spectral[degenerate], _ = np.linalg.qr(spectral[degenerate])
    gram = spectral.conj().swapaxes(1, 2) @ spectral
    assert np.max(abs(gram - np.eye(2))) < 1e-8
    assert np.max(abs(Uk @ spectral - spectral * np.exp(-1j * epsk)[:, None, :])) < 1e-8
    def spectral_target(psi):
        F = np.stack([np.fft.fftn(psi[..., a]).reshape(-1) for a in range(4)], -1)
        weights = abs(np.einsum('nab,na->nb', spectral.conj(), F)) ** 2
        norm = np.sum(abs(F) ** 2)
        assert abs(weights.sum() / norm - 1) < 1e-8
        return float(np.sum(weights * th * th / epsk) / norm)
    def packet(k0, seed):
        rng = np.random.default_rng(seed); A = np.exp(-np.sum((K - k0) ** 2, 1) * 100.0 / 2)
        c = rng.normal(size=2) + 1j * rng.normal(size=2); ref = pos[np.argmin(np.sum((K - k0) ** 2, 1))] @ (c / np.linalg.norm(c))
        coef = np.einsum('nab,a->nb', pos.conj(), ref); vec = np.einsum('nab,nb->na', pos, coef) * A[:, None] * np.exp(1j * K @ np.full(3, 24.0))[:, None]
        return np.stack([np.fft.ifftn(vec[:, a].reshape(L, L, L)) for a in range(4)], -1)
    rows = []
    for name, parts in (('at rest', ((0, 0, 0), )), ('moving along (1,1,0)', ((th / np.sqrt(2), th / np.sqrt(2), 0), )), ('two crossing', ((th, 0, 0), (-th, 0, 0)))):
        outs = [packet(np.array(p, float), 7 + i) for i, p in enumerate(parts)]; psi = sum(outs); psi /= np.sqrt(np.sum(abs(psi) ** 2))
        mid = psi @ half.T; dens = 2 * th * np.real(np.sum(np.conj(mid[..., :2]) * mid[..., 2:], -1)); rho = np.sum(abs(psi) ** 2, -1)
        rows.append((name, dens.sum() / rho.sum(), np.abs(dens).sum() / rho.sum(), spectral_target(psi), float(rho[dens < 0].sum() / rho.sum())))
    check('packets: the signed coherent clock is within 3% of the packet-averaged m^2/eps',
          all(abs(r[1] / r[3] - 1) < 0.03 for r in rows),
          '; '.join(f'{r[0]}: signed {r[1]:.5f} vs {r[3]:.5f}' for r in rows))
    check('packets: the overlap is negative on part of the packet weight, and an unsigned count overshoots where packets cross',
          rows[2][4] > 0.03 and rows[2][2] / rows[2][3] - 1 > 0.02 and rows[2][2] > rows[2][1],
          '; '.join(f'{r[0]}: negative weight {r[4]:.2%}, unsigned {r[2]:.5f}' for r in rows))
    print('per_site: the walk, coin angle, mid-coin evaluation, band selection and packet construction are supplied choices.')
    print('per_block: momenta, angles, lattice size, packet width and seeds are fixed in this source.')
    print('lattice_wide: no physical clock law, redshift, flip-rule derivation or empirical identification is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
