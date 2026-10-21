#!/usr/bin/env python3
"""Supplied lossless walks with relay fronts: burn and turn contributions to a source tensor.
Fronts follow the Born odds every tick (exchange flow 2*eps*P_d*P_d' per pair, plus the minimal net flow),
step one link per tick, add eps*d d per burn and -(d'-d)(d'-d)/4 per turn. Checks: exact plane-wave totals
(1D two-component walk, six-direction and eight-diagonal walks on Z^3), deterministic local momentum balance
for packets of increasing width (1D and six-direction), and the turn-action clock against m/gamma.
No physical identification, derivation of the turning rule or universal dynamics classification.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = ('docs/SCALE_LADDER_GRAVITY_BURN_AND_TURN_SOURCE_TENSOR_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

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


def main():
    th1 = 0.05; c1, s1 = np.cos(th1), np.sin(th1)
    # ---------------- 1D plane waves: two components step +1 / -1, coin angle th1
    rows = []
    for k in (0.0, 0.03, 0.06, 0.12):
        U = np.diag([np.exp(-1j * k), np.exp(1j * k)]) @ np.array([[c1, -1j * s1], [-1j * s1, c1]])
        w, V = np.linalg.eig(U); i = int(np.argmax(-np.angle(w))); eps = -np.angle(w[i]); u = V[:, i]
        v = c1 * np.sin(k) / np.sin(eps) if k else 0.0
        burn, turn, action = plane_wave_tensors(abs(u) ** 2, np.array([[1.0], [-1.0]]), eps)
        rows.append((k, eps, v, burn[0, 0], burn[0, 0] + turn[0, 0], eps * v * v, action, th1 ** 2 / eps))
    err = max(abs(r[4] - r[5]) for r in rows); bad = min(abs(r[3] - r[5]) for r in rows)
    check('1D plane waves: burns + turns equal eps v^2; burns alone do not', err < 1e-12 and bad > 1e-3,
          '; '.join(f'v={r[2]:.3f}: burns {r[3]:.5f}, burns+turns {r[4]:.5f}, eps v^2 {r[5]:.5f}' for r in rows))
    cl = max(abs(r[6] / r[7] - 1) for r in rows)
    check('1D clock: turn action per tick equals m^2/eps (m/gamma, m = th) within 1%', cl < 0.01,
          '; '.join(f'v={r[2]:.3f}: action {r[6]:.5f}, m^2/eps {r[7]:.5f}' for r in rows))
    # ---------------- 1D packets: deterministic local momentum balance
    N = 6000; x = np.arange(N); kk = 2 * np.pi * np.fft.fftfreq(N)
    def packet_1d(k0, wid):
        A = np.exp(-((kk - k0) ** 2) * wid ** 2 / 2); V2 = np.zeros((2, N), complex)
        for n in np.where(A > 1e-9)[0]:
            Uk = np.diag([np.exp(-1j * kk[n]), np.exp(1j * kk[n])]) @ np.array([[c1, -1j * s1], [-1j * s1, c1]])
            w, V = np.linalg.eig(Uk); i = int(np.argmax(-np.angle(w))); vv = V[:, i] * np.exp(-1j * np.angle(V[0, i]))
            V2[:, n] = A[n] * vv * np.exp(1j * kk[n] * N / 2)
        R, L = np.fft.ifft(V2[0]), np.fft.ifft(V2[1]); nr = np.sqrt(np.sum(abs(R) ** 2 + abs(L) ** 2)); return R / nr, L / nr
    out1 = []
    for wid in (30.0, 60.0, 120.0):
        k0 = 0.06; eps = np.arccos(c1 * np.cos(k0)); R, L = packet_1d(k0, wid); res = []; base = []; fsz = []
        for t in range(160):
            Pp, Pm = abs(R) ** 2, abs(L) ** 2; R1, L1 = c1 * R - 1j * s1 * L, -1j * s1 * R + c1 * L
            Pp1, Pm1 = abs(R1) ** 2, abs(L1) ** 2; rho = Pp + Pm + 1e-300
            ex = 2 * eps * Pp * Pm / rho; D = Pp1 - Pp; F = 2 * ex + abs(D)
            sig = -F; f = 2 * eps * D; dust = eps * (Pp1 + Pm1)
            if 70 <= t < 90:
                sm = lambda a: gaussian_filter1d(a, wid / 2, mode='wrap')
                dS = (np.roll(sm(sig), -1) - np.roll(sm(sig), 1)) / 2; dD = (np.roll(sm(dust), -1) - np.roll(sm(dust), 1)) / 2
                res.append(np.sum((sm(f) + dS) ** 2)); base.append(np.sum(dD ** 2)); fsz.append(np.sum(sm(f) ** 2))
            R, L = np.roll(R1, 1), np.roll(L1, -1)
        out1.append((wid, np.sqrt(sum(fsz) / sum(base)), np.sqrt(sum(res) / sum(base))))
    check('1D packets: with the turn stress the momentum residual falls with width; the turn impulse alone does not',
          out1[0][2] > out1[1][2] > out1[2][2] and out1[2][2] < 0.6 * out1[0][2] and min(o[1] for o in out1) > 0.3,
          '; '.join(f'width {o[0]:.0f}: impulse {o[1]:.3f}, residual {o[2]:.4f} (relative to |d_x burn stress|)' for o in out1))
    # ---------------- six-direction and eight-diagonal walks on Z^3
    th = 0.3
    E6 = np.array([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)], float)
    R6 = np.array([[1.0 if np.allclose(a, -b) else 0 for b in E6] for a in E6]); P6 = np.array([[1.0 if abs(a @ b) < 1e-9 else 0 for b in E6] for a in E6])
    C6, U6 = cubic_walk(E6, R6 - P6 + 2 * np.eye(6), th)
    start6 = lambda om: int(np.where(abs(om - th) < 0.05)[0][np.argmax(om[abs(om - th) < 0.05])])
    E8 = np.array([(a, b, c) for a in (1, -1) for b in (1, -1) for c in (1, -1)], float)
    H8 = np.array([[int(np.sum(p != q)) for q in E8] for p in E8])
    C8, U8 = cubic_walk(E8, 1.0 * (H8 == 1) - 0.5 * (H8 == 2) + 0.3 * (H8 == 3), th)
    start8 = lambda om: int(np.where(om > 1e-6)[0][np.argmin(om[om > 1e-6])])
    for name, U, dirs, start, cases in (('six-direction', U6, E6, start6, ((1, 1, 0), (2, 1, 0), (1, 1, 1))),
                                        ('eight-diagonal', U8, E8, start8, ((1, 1, 0), (1, 1, 1), (2, 1, 0)))):
        errs, rep = [], []
        for kd in cases:
            eps, u, v = group_velocity(U, kd, 0.3, start); P = abs(u) ** 2
            burn, turn, action = plane_wave_tensors(P, dirs, eps); target = eps * np.outer(v, v)
            mean_ok = np.allclose(P @ dirs, v, atol=1e-5)
            errs.append((abs(burn + turn - target).max(), abs(burn - target).max(), mean_ok))
            rep.append(f'k along {kd}: |v| {np.linalg.norm(v):.3f}, shear xy {(burn + turn)[0, 1]:+.5f} vs eps v_x v_y {target[0, 1]:+.5f}')
        check(f'{name} walk plane waves: mean step equals group velocity and burns + turns equal eps v v including shear',
              all(e[2] for e in errs) and max(e[0] for e in errs) < 1e-8 and min(e[1] for e in errs) > 1e-3,
              f'max |burns+turns - eps v v| {max(e[0] for e in errs):.1e}; burns alone >= {min(e[1] for e in errs):.1e}; ' + '; '.join(rep))
    # ---------------- six-direction packets: deterministic local momentum balance in 3D
    def local_3d(L, wid, kd, km):
        kd = np.asarray(kd, float) / np.linalg.norm(kd); eps, u0 = track(U6, kd, km, start6); k0 = km * kd
        g = 2 * np.pi * np.fft.fftfreq(L); Kv = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
        A = np.exp(-np.sum((Kv - k0) ** 2, -1) * wid ** 2 / 2); sel = A > 1e-6
        Us = np.exp(-1j * np.einsum('ni,di->nd', Kv[sel], E6))[:, :, None] * C6[None]
        w, V = np.linalg.eig(Us); j = np.argmax(abs(np.einsum('nde,d->ne', V.conj(), u0)), 1)
        vec = V[np.arange(len(j)), :, j]; ph = np.einsum('nd,d->n', vec.conj(), u0); vec = vec * (ph / abs(ph))[:, None]
        Pk = np.zeros((L, L, L, 6), complex); Pk[sel] = A[sel][:, None] * vec
        ph0 = np.exp(1j * np.einsum('...i,i->...', Kv, np.full(3, L // 2)))
        psi = np.stack([np.fft.ifftn(Pk[..., d] * ph0) for d in range(6)], -1); psi /= np.sqrt(np.sum(abs(psi) ** 2))
        Dd = E6[None, :, :] - E6[:, None, :]; idx = np.arange(6)
        def div(T):
            return np.stack([sum((np.roll(T[..., i, j], -1, j) - np.roll(T[..., i, j], 1, j)) / 2 for j in range(3)) for i in range(3)], -1)
        def smooth(T):
            out = np.empty_like(T)
            for i in range(3):
                for j in range(3): out[..., i, j] = gaussian_filter(T[..., i, j], wid / 2, mode='wrap')
            return out
        res = base = fs = 0.0; T = 16
        for t in range(T):
            P = abs(psi) ** 2; psi1 = psi @ C6.T; P1 = abs(psi1) ** 2; rho = P.sum(-1) + 1e-300
            if T // 2 - 2 <= t < T // 2 + 2:
                ex = 2 * eps * P[..., :, None] * P[..., None, :] / rho[..., None, None]
                D = P1 - P; pos = np.maximum(D, 0); neg = np.maximum(-D, 0)
                F = ex + neg[..., :, None] * pos[..., None, :] / (pos.sum(-1) + 1e-300)[..., None, None]; F[..., idx, idx] = 0
                sig = -np.einsum('...ab,abi,abj->...ij', F, Dd, Dd) / 4
                f = eps * D @ E6; dust = eps * np.einsum('...d,di,dj->...ij', P1, E6, E6)
                fsm = np.stack([gaussian_filter(f[..., i], wid / 2, mode='wrap') for i in range(3)], -1)
                dsig = div(smooth(sig)); ddust = div(smooth(dust))
                res += np.sum((fsm + dsig) ** 2); base += np.sum(ddust ** 2); fs += np.sum(fsm ** 2)
            psi = np.stack([np.roll(psi1[..., d], tuple(E6[d].astype(int)), (0, 1, 2)) for d in range(6)], -1)
        return np.sqrt(fs / base), np.sqrt(res / base)
    out3 = [(wid,) + local_3d(L, wid, (1, 1, 0), 0.3) for wid, L in ((3.0, 32), (5.0, 40), (8.0, 56))]
    check('six-direction packets moving along (1,1,0): with the turn stress the residual falls with width; the impulse alone does not',
          out3[0][2] > out3[1][2] > out3[2][2] and out3[2][2] < 0.6 * out3[0][2] and min(o[1] for o in out3) > 0.5,
          '; '.join(f'width {o[0]:.0f}: impulse {o[1]:.3f}, residual {o[2]:.3f} (relative to |div burn stress|)' for o in out3))
    # ---------------- clock: turn action is eps(<|d|^2> - v^2); m/gamma needs |d| equal to the coarse light speed
    rep = []; worst = 0.0
    for kd in ((1, 1, 0), (1, 1, 1)):
        eps, u, v = group_velocity(U6, kd, 0.3, start6); _, _, action = plane_wave_tensors(abs(u) ** 2, E6, eps)
        ident = eps * (1 - v @ v); mg = th ** 2 / eps; worst = max(worst, abs(action / mg - 1))
        rep.append(f'k along {kd}: turn action {action:.4f} (identity eps(1-v^2) {ident:.4f}), m^2/eps {mg:.4f}')
    check('six-direction walk: turn action per tick differs from m^2/eps by more than 5% (the 1D clock identity does not carry over)', worst > 0.05, '; '.join(rep))
    print('per_site: coin angles, coins, the exchange rule, the per-turn stress and eps = band frequency are supplied choices.')
    print('per_block: lattice sizes, packet widths, momenta, smoothing widths and tick windows are fixed in this source.')
    print('lattice_wide: no physical source identification, derivation of the turning rule, gravity field equation or clock law is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
