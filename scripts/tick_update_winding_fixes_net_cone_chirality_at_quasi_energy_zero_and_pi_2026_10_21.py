#!/usr/bin/env python3
"""Weyl cones of a tick update at quasi-energy 0 and pi, and the 3D winding that fixes their net chirality.
Two-component walks U(k) in SU(2) on Z^3. Chirality of a cone at k0 with U(k0) = s I (s = +1: quasi-energy 0,
s = -1: quasi-energy pi) is sign det M for U(k0+q) = s (1 - i sum_ij M_ij q_j sigma_i + O(q^2)).
Checks: exact cone sets of the split-step walk S_z S_y S_x; the winding W3 of split-step, coin-interleaved and
diagonal-shift walks and of the eight-mode block candidate; a quasi-local walk with W3 = 1 and one unpaired cone
at pi; equal net chirality at 0 and pi; the exponential tail that walk needs; CL-5 energy of pi-sector modes.
No matter content, no physical chirality and no adopted tick update is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/TICK_UPDATE_WINDING_FIXES_NET_CONE_CHIRALITY_AT_QUASI_ENERGY_ZERO_AND_PI_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import sys, os, signal, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED = time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 120-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1., -1]).astype(complex)
AL = [SX, SY, SZ]; I2 = np.eye(2)


# ---------- vectorised walks on an n^3 grid: arrays of shape (n,n,n,N,N) ----------
def grid(n):
    g = 2 * np.pi * np.arange(n) / n
    return np.meshgrid(g, g, g, indexing='ij')


def expsig(theta, sig):
    """exp(-i theta sig) for an array theta and a Pauli-type matrix with sig^2 = 1."""
    c = np.cos(theta)[..., None, None]; s = np.sin(theta)[..., None, None]
    return c * np.eye(sig.shape[0]) - 1j * s * sig


def split_step(K):
    return expsig(K[2], SZ) @ expsig(K[1], SY) @ expsig(K[0], SX)


def coin_walk(K, coins):
    """C4 S_z C3 S_y C2 S_x C1 with constant SU(2) coins: products of one-variable factors."""
    U = coins[0]
    for i, C in zip((0, 1, 2), coins[1:]):
        U = C @ expsig(K[i], AL[i]) @ U
    return U


def diag_walk(K):
    """coin-conditioned shifts along (1,1,0), (0,1,1), (1,0,1) with tilted spin axes."""
    n1 = (SX + SZ) / np.sqrt(2); n2 = (SY + SX) / np.sqrt(2); n3 = (SZ + SY) / np.sqrt(2)
    return expsig(K[2] + K[0], n3) @ expsig(K[1] + K[2], n2) @ expsig(K[0] + K[1], n1)


def wilson_unit(K, m):
    """Quasi-local walk U = (n0 - i n.sigma)/|n|, n0 = m + sum cos k, n_i = sin k_i (cubic covariant)."""
    n0 = m + np.cos(K[0]) + np.cos(K[1]) + np.cos(K[2])
    nv = [np.sin(K[0]), np.sin(K[1]), np.sin(K[2])]
    r = np.sqrt(n0 ** 2 + nv[0] ** 2 + nv[1] ** 2 + nv[2] ** 2)
    U = (n0 / r)[..., None, None] * I2
    for i in range(3): U = U - 1j * (nv[i] / r)[..., None, None] * AL[i]
    return U


def W3(Ufun, n):
    """(1/24 pi^2) int eps^{ijk} tr(U^-1 d_i U U^-1 d_j U U^-1 d_k U), spectral derivatives, trapezoid rule."""
    K = grid(n); U = Ufun(K); kk = np.fft.fftfreq(n, 1.0 / n)
    D = []
    for ax in range(3):
        sh = [1, 1, 1]; sh[ax] = n
        Dk = np.fft.ifft(np.fft.fft(U, axis=ax) * (1j * kk.reshape(sh))[..., None, None], axis=ax)
        D.append(np.conj(np.swapaxes(U, -1, -2)) @ Dk)
    tot = 0
    for (i, j, k), sg in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
        tot = tot + sg * np.trace(D[i] @ D[j] @ D[k], axis1=-2, axis2=-1)
    return float(np.real(np.mean(tot)) * (2 * np.pi) ** 3 / (24 * np.pi ** 2))


# ---------- pointwise cone chirality ----------
def chirality(Ufun1, k0, s):
    h = 1e-6; M = np.zeros((3, 3))
    for j in range(3):
        e = np.zeros(3); e[j] = h
        Dj = (Ufun1(k0 + e) - Ufun1(k0 - e)) / (2 * h)
        A = s * Dj                       # = -i sum_i M_ij sigma_i at the cone
        for i in range(3): M[i, j] = np.real(1j * np.trace(AL[i] @ A) / 2)
    return int(np.sign(np.linalg.det(M)))


def one(f, k):
    K = [np.array(k[i]) for i in range(3)]
    return f(K)


def cone_table(Ufun, pts):
    """For candidate points, return {0: [chir...], pi: [chir...]} where U = +I or -I."""
    out = {0: [], 1: []}
    for k in pts:
        k = np.array(k, float); U = one(Ufun, k)
        for s, key in ((1, 0), (-1, 1)):
            if np.allclose(U, s * I2, atol=1e-12): out[key].append(chirality(lambda q: one(Ufun, q), k, s))
    return out


def main():
    # 1. split-step walk: exact cone set
    half = [np.array(p) * np.pi / 2 for p in itertools.product(range(4), repeat=3)]
    t = cone_table(split_step, half)
    n0p, n0m = t[0].count(1), t[0].count(-1); npp, npm = t[1].count(1), t[1].count(-1)
    corner0 = cone_table(split_step, [np.array(p) * np.pi for p in itertools.product(range(2), repeat=3)])
    check('split-step S_z S_y S_x: 8 cones at quasi-energy 0 (4 of each chirality) and 8 at pi (4 of each)',
          (n0p, n0m, npp, npm) == (4, 4, 4, 4) and len(t[0]) + len(t[1]) == 16,
          f'0: +{n0p}/-{n0m}; pi: +{npp}/-{npm}; corners carry +1 at both 0 ({corner0[0]}) and pi ({corner0[1]}), the pi/2-points -1')
    n = 60; K = grid(n)
    f = np.cos(K[0]) * np.cos(K[1]) * np.cos(K[2]) + np.sin(K[0]) * np.sin(K[1]) * np.sin(K[2])
    on = np.all(np.isclose((np.stack(K) / (np.pi / 2)) % 1, 0) | np.isclose((np.stack(K) / (np.pi / 2)) % 1, 1), axis=0)
    gap = np.min(1 - np.abs(f[~on]))
    check('no further cones: |tr U|/2 = 1 only at those 16 points (Cauchy-Schwarz bound, 60^3 grid confirms)', gap > 1e-4, f'min 1-|cos w| off the 16 points: {gap:.2e}')

    # 2. winding of products of one-variable factors
    rng = np.random.default_rng(7)
    def rand_su2():
        q = rng.normal(size=4); q /= np.linalg.norm(q); return q[0] * I2 - 1j * (q[1] * SX + q[2] * SY + q[3] * SZ)
    coins = [rand_su2() for _ in range(4)]
    w_ss = W3(split_step, 24); w_cw = W3(lambda K: coin_walk(K, coins), 24); w_dw = W3(diag_walk, 24)
    check('W3 = 0 for the split-step walk, a random-coin walk and a diagonal-shift walk (products of one-variable loops)',
          max(abs(w_ss), abs(w_cw), abs(w_dw)) < 1e-9, f'W3 = {w_ss:.1e}, {w_cw:.1e}, {w_dw:.1e}')

    # 3. block candidate (8 modes, masses .05/.5): also a product of one-variable factors and constants
    Q = np.full(3, np.pi)
    def UL1(k): return expsig(k[2], SZ) @ expsig(k[1], SY) @ expsig(k[0], SX)
    Mm = np.zeros((8, 8))
    for (a, b) in ((0, 2), (4, 6)): Mm[a:a + 2, b:b + 2] = .05 * I2; Mm[b:b + 2, a:a + 2] = .05 * I2
    for (a, b) in ((0, 6), (4, 2)): Mm[a:a + 2, b:b + 2] = .5 * I2; Mm[b:b + 2, a:a + 2] = .5 * I2
    Em = expm(-1j * Mm)
    def Ublock(K):
        sh = K[0].shape; D = np.zeros(sh + (8, 8), complex); mK = [-x for x in K]
        D[..., 0:2, 0:2] = UL1(K); D[..., 2:4, 2:4] = UL1(mK); D[..., 4:6, 4:6] = -UL1(K); D[..., 6:8, 6:8] = -UL1(mK)
        return D @ Em
    w_bl = W3(Ublock, 16)
    check('W3 = 0 for the eight-mode block candidate', abs(w_bl) < 1e-9, f'W3 = {w_bl:.1e}')

    # 4. quasi-local walk: one unpaired cone at pi, net chirality equal at 0 and pi
    rows = []; ok = True
    corners = [np.array(p) * np.pi for p in itertools.product(range(2), repeat=3)]
    for m in (2.0, 0.5, 4.5, -2.0):
        tb = cone_table(lambda K: wilson_unit(K, m), corners); w = W3(lambda K: wilson_unit(K, m), 40)
        c0, cp = sum(tb[0]), sum(tb[1]); rows.append(f'm={m}: 0 +{tb[0].count(1)}/-{tb[0].count(-1)}, pi +{tb[1].count(1)}/-{tb[1].count(-1)}, W3={w:+.6f}')
        ok &= (c0 == cp == -round(w)) and abs(w - round(w)) < 1e-4
    check('quasi-local walk (n0 - i n.sigma)/|n|: net chirality at 0 = net chirality at pi = -W3 for every m (W3 sign: U = a0 - i a.sigma)', ok, '; '.join(rows[:2]))
    print('   ', '; '.join(rows[2:]))
    tb = cone_table(lambda K: wilson_unit(K, -2.0), corners); tb2 = cone_table(lambda K: wilson_unit(K, 2.0), corners)
    check('m=-2: exactly one cone at quasi-energy 0 (k=0, chirality +1); all 7 doublers at pi (4 of +, 3 of -), net +1',
          tb[0] == [1] and tb[1].count(1) == 4 and tb[1].count(-1) == 3 and tb2[1] == [1] and len(tb2[0]) == 7,
          'm=+2 is the mirror case (7 at 0, one at pi), U_{-m}(k) = -U_m(k - pi(1,1,1))')

    # 5. cubic covariance of the quasi-local walk under the 24 rotations
    worst = 0.0
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for i in range(3): R[i, perm[i]] = sg[i]
            if not np.isclose(np.linalg.det(R), 1): continue
            ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)); V = I2
            if not np.isclose(ang, 0):
                w_, vec = np.linalg.eig(R); ax = np.real(vec[:, np.argmin(abs(w_ - 1))]); ax /= np.linalg.norm(ax)
                for s in (1, -1):
                    Vc = np.cos(ang / 2) * I2 - 1j * np.sin(ang / 2) * s * (ax[0] * SX + ax[1] * SY + ax[2] * SZ)
                    if all(np.allclose(Vc @ AL[j] @ Vc.conj().T, sum(R[i, j] * AL[i] for i in range(3))) for j in range(3)): V = Vc
            for k in rng.uniform(-np.pi, np.pi, (5, 3)):
                worst = max(worst, np.abs(one(lambda K: wilson_unit(K, 2.0), R @ k) - V @ one(lambda K: wilson_unit(K, 2.0), k) @ V.conj().T).max())
    check('the quasi-local walk is exactly covariant under all 24 cube rotations (spin-1/2 lift)', worst < 1e-12, f'max deviation {worst:.1e}')

    # 6. its price: an exponential tail beyond every finite range
    n = 48; Uk = wilson_unit(grid(n), -2.0); C = np.fft.fftn(Uk, axes=(0, 1, 2)) / n ** 3
    x = np.minimum(np.arange(n), n - np.arange(n)); X = np.maximum(np.maximum(x[:, None, None], x[None, :, None]), x[None, None, :])
    wgt = np.sum(np.abs(C) ** 2, axis=(-2, -1)) / 2
    tails = {R: float(np.sum(wgt[X > R])) for R in (1, 2, 4, 8, 12)}
    rate = np.log(tails[4] / tails[12]) / 8
    check('m=-2 walk has weight beyond every range R, falling exponentially (not finite range)',
          all(tails[R] > 1e-30 for R in tails) and tails[1] > tails[2] > tails[4] > tails[8] > tails[12],
          'tail weight beyond R: ' + ', '.join(f'{R}:{v:.1e}' for R, v in tails.items()) + f'; decay ~exp(-{rate:.2f} R)')

    # 7. winding is additive: any finite-range-product walk U' differs from the m=2 walk somewhere by a full -1
    w_rel = W3(lambda K: np.conj(np.swapaxes(split_step(K), -1, -2)) @ wilson_unit(K, 2.0), 40)
    check('W3(U_split^dag U_m=2) = -1 (additivity), so U_split^dag U_m=2 = -I at some k: no walk with W3 = 0 is within operator distance < 2 of it',
          abs(w_rel + 1) < 1e-4, f'W3 = {w_rel:.6f}')

    # 8. CL-5 energy of modes near a pi-cone lies near pi, outside the CL-6 relay domain (energy <= 1/2)
    ks = [np.array([np.pi, np.pi, np.pi]) + 0.05 * np.array([1, .3, -.2]), np.array([np.pi, 0, 0]) + 0.05 * np.array([.2, 1, .4])]
    Es = []
    for f_, k in ((lambda K: wilson_unit(K, 2.0), ks[0]), (split_step, ks[1])):
        w_, V = np.linalg.eig(one(f_, k))
        for j in range(2): Es.append(abs(-np.angle(np.vdot(V[:, j], w_[j] * V[:, j]))))
    check('CL-5 energies of modes at |q|=0.05 from a pi-cone are within 0.06 of pi (outside the CL-6 domain)',
          all(abs(E - np.pi) < 0.06 for E in Es), 'energies ' + ', '.join(f'{E:.3f}' for E in Es))

    print('theorem: SU(2) walk => net chirality at 0 = net at pi = -W3 (the degree); any product of coins and coin-conditioned shifts has deg 0.')
    print('external input (not rederived here): SK1 of the Laurent ring C[Z^3] vanishes, so every finite-range walk has W3 = 0.')
    print('supplied: the quasi-local walk, its parameter m and its exponential tail; no adopted tick update or matter content.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
