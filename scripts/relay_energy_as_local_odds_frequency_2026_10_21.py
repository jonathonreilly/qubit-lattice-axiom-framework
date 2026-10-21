#!/usr/bin/env python3
"""Relay energy as the local odds frequency, with no packet-frequency input.
On supplied lossless walks a relay's energy is the odds-weighted mean phase advance of its site's direction amplitudes
in one tick. Checks: steadiness of the total energy and its approach to the packet frequency (1D), and the
deterministic local momentum balance with the burn and turn assignment (1D and six-direction 3D packets).
No physical energy identification, field equation or derivation of the rules is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = ('docs/RELAY_ENERGY_AS_LOCAL_ODDS_FREQUENCY_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

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
    N = 6000; kk = 2 * np.pi * np.fft.fftfreq(N)
    def packet_1d(k0, wid):
        A = np.exp(-((kk - k0) ** 2) * wid ** 2 / 2); V2 = np.zeros((2, N), complex); om = np.zeros(N)
        for n in np.where(A > 1e-9)[0]:
            Uk = np.diag([np.exp(-1j * kk[n]), np.exp(1j * kk[n])]) @ np.array([[c1, -1j * s1], [-1j * s1, c1]])
            w, V = np.linalg.eig(Uk); i = int(np.argmax(-np.angle(w))); vv = V[:, i] * np.exp(-1j * np.angle(V[0, i]))
            V2[:, n] = A[n] * vv * np.exp(1j * kk[n] * N / 2); om[n] = -np.angle(w[i])
        R, L = np.fft.ifft(V2[0]), np.fft.ifft(V2[1]); nr = np.sqrt(np.sum(abs(R) ** 2 + abs(L) ** 2))
        return R / nr, L / nr, float(np.sum(A ** 2 * om) / np.sum(A ** 2))
    rows = []
    for wid in (30.0, 60.0, 120.0):
        R, L, ombar = packet_1d(0.06, wid); Es = []; res = base = 0.0
        for t in range(161):
            R1, L1 = c1 * R - 1j * s1 * L, -1j * s1 * R + c1 * L; Rn, Ln = np.roll(R1, 1), np.roll(L1, -1)
            Pp, Pm = abs(R) ** 2, abs(L) ** 2; rho = Pp + Pm + 1e-300
            eps = (Pp * -np.angle(Rn * np.conj(R) + 1e-300) + Pm * -np.angle(Ln * np.conj(L) + 1e-300)) / rho
            Es.append(float(np.sum(eps * rho)))
            if 70 <= t < 90:
                Pp1, Pm1 = abs(R1) ** 2, abs(L1) ** 2; D = Pp1 - Pp
                F = 2 * (2 * eps * Pp * Pm / rho) + abs(D); sig = -F; f = 2 * eps * D; dust = eps * (Pp1 + Pm1)
                sm = lambda a: gaussian_filter1d(a, wid / 2, mode='wrap')
                dS = (np.roll(sm(sig), -1) - np.roll(sm(sig), 1)) / 2; dD = (np.roll(sm(dust), -1) - np.roll(sm(dust), 1)) / 2
                res += np.sum((sm(f) + dS) ** 2); base += np.sum(dD ** 2)
            R, L = Rn, Ln
        rows.append((wid, np.mean(Es), np.ptp(Es), ombar, np.sqrt(res / base)))
    check('1D packets: total relay energy under the local rule is steady over 160 ticks and approaches the packet frequency',
          all(r[2] < 2e-4 for r in rows) and abs(rows[-1][1] / rows[-1][3] - 1) < 1e-4 and abs(rows[0][1] / rows[0][3] - 1) > abs(rows[-1][1] / rows[-1][3] - 1),
          '; '.join(f'width {r[0]:.0f}: energy {r[1]:.6f} (spread {r[2]:.1e}) vs frequency {r[3]:.6f}' for r in rows))
    check('1D packets: with local energy the momentum residual falls with width',
          rows[0][4] > rows[1][4] > rows[2][4] and rows[2][4] < 0.3 * rows[0][4], '; '.join(f'width {r[0]:.0f}: residual {r[4]:.4f}' for r in rows))
    th = 0.3
    E6 = np.array([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)], float)
    R6 = np.array([[1.0 if np.allclose(a, -b) else 0 for b in E6] for a in E6]); P6 = np.array([[1.0 if abs(a @ b) < 1e-9 else 0 for b in E6] for a in E6])
    C6, U6 = cubic_walk(E6, R6 - P6 + 2 * np.eye(6), th)
    start6 = lambda om: int(np.where(abs(om - th) < 0.05)[0][np.argmax(om[abs(om - th) < 0.05])])
    def local_3d(L, wid, kd, km):
        kd = np.asarray(kd, float) / np.linalg.norm(kd); _, u0 = track(U6, kd, km, start6); k0 = km * kd
        g = 2 * np.pi * np.fft.fftfreq(L); Kv = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
        A = np.exp(-np.sum((Kv - k0) ** 2, -1) * wid ** 2 / 2); sel = A > 1e-6
        Us = np.exp(-1j * np.einsum('ni,di->nd', Kv[sel], E6))[:, :, None] * C6[None]
        w, V = np.linalg.eig(Us); j = np.argmax(abs(np.einsum('nde,d->ne', V.conj(), u0)), 1)
        vec = V[np.arange(len(j)), :, j]; ph = np.einsum('nd,d->n', vec.conj(), u0); vec = vec * (ph / abs(ph))[:, None]
        Pk = np.zeros((L, L, L, 6), complex); Pk[sel] = A[sel][:, None] * vec
        ph0 = np.exp(1j * np.einsum('...i,i->...', Kv, np.full(3, L // 2)))
        psi = np.stack([np.fft.ifftn(Pk[..., d] * ph0) for d in range(6)], -1); psi /= np.sqrt(np.sum(abs(psi) ** 2))
        Dd = E6[None, :, :] - E6[:, None, :]; idx = np.arange(6)
        def nxt(p):
            q = p @ C6.T; return np.stack([np.roll(q[..., d], tuple(E6[d].astype(int)), (0, 1, 2)) for d in range(6)], -1)
        def div(T):
            return np.stack([sum((np.roll(T[..., i, j], -1, j) - np.roll(T[..., i, j], 1, j)) / 2 for j in range(3)) for i in range(3)], -1)
        def smooth(T):
            out = np.empty_like(T)
            for i in range(3):
                for j in range(3): out[..., i, j] = gaussian_filter(T[..., i, j], wid / 2, mode='wrap')
            return out
        res = base = 0.0; T = 16
        for t in range(T):
            P = abs(psi) ** 2; psi1 = psi @ C6.T; P1 = abs(psi1) ** 2; rho = P.sum(-1) + 1e-300; pn = nxt(psi)
            if T // 2 - 2 <= t < T // 2 + 2:
                eps = np.sum(P * -np.angle(pn * np.conj(psi) + 1e-300), -1) / rho
                ex = 2 * eps[..., None, None] * P[..., :, None] * P[..., None, :] / rho[..., None, None]
                D = P1 - P; pos = np.maximum(D, 0); neg = np.maximum(-D, 0)
                F = ex + neg[..., :, None] * pos[..., None, :] / (pos.sum(-1) + 1e-300)[..., None, None]; F[..., idx, idx] = 0
                sig = -np.einsum('...ab,abi,abj->...ij', F, Dd, Dd) / 4
                f = eps[..., None] * (D @ E6); dust = eps[..., None, None] * np.einsum('...d,di,dj->...ij', P1, E6, E6)
                fsm = np.stack([gaussian_filter(f[..., i], wid / 2, mode='wrap') for i in range(3)], -1)
                res += np.sum((fsm + div(smooth(sig))) ** 2); base += np.sum(div(smooth(dust)) ** 2)
            psi = pn
        return np.sqrt(res / base)
    out3 = [(wid, local_3d(L, wid, (1, 1, 0), 0.3)) for wid, L in ((3.0, 32), (5.0, 40), (8.0, 56))]
    check('six-direction packets along (1,1,0): with local energy the momentum residual falls with width',
          out3[0][1] > out3[1][1] > out3[2][1] and out3[2][1] < 0.6 * out3[0][1], '; '.join(f'width {o[0]:.0f}: residual {o[1]:.3f}' for o in out3))
    print('per_site: the walks, coin angles, packets, phase-advance evaluation and smoothing are supplied choices.')
    print('lattice_wide: no physical energy identification, field equation or derivation of the rules is established.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
