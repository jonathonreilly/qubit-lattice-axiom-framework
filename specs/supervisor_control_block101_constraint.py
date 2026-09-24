#!/usr/bin/env python3
"""Supervisor control for block 101 (floating point; evidence, not proof). Taken from the probes worker's check
(J:derive:delay-of-the-rate-field-with-the-curvature-member:a1, worker w-jonathonsmac4f50-j03c0, section E), re-run by the supervisor.

A 48 x 48 plane slice, K = wbar = alpha = 1, beta = 1/2 (strain speed c_T = 1/2); a Gaussian body of width 1.5 whose energy is switched on
smoothly over tau_r = 2; the clock field from block 101's law u = -e/(4 K wbar p^2) + alpha(alpha + 3 beta) e''/(K^2 wbar^3 (alpha + beta) p^4);
a walk packet at rest (wave number pi/2 along y) at distances 8 and 16: the force on its momentum, d<S_x>/dt = <i [H_w, S_x]>, before the
switch-on, at label time 0.05, and after it, against block 54's -E<grad u> and the strains' arrival times r/c_T.
"""
import numpy as np

# ---------------------------------------------------------------- E: executed 2D-slice control (floating point)
Lx = 48
Kv, wbv, alv, bev = 1.0, 1.0, 1.0, 0.5
Cq = alv * (alv + 3 * bev) / (Kv ** 2 * wbv ** 3 * (alv + bev))
cT = wbv * np.sqrt(Kv / (4 * alv))
kx = 2 * np.pi * np.fft.fftfreq(Lx)
KX, KY = np.meshgrid(kx, kx, indexing="ij")
P2 = 4 * np.sin(KX / 2) ** 2 + 4 * np.sin(KY / 2) ** 2
P2[0, 0] = 1.0
X, Y = np.meshgrid(np.arange(Lx), np.arange(Lx), indexing="ij")
c0 = Lx // 2
blob = np.exp(-((X - c0) ** 2 + (Y - c0) ** 2) / (2 * 1.5 ** 2))
blob /= blob.sum()
tr = 2.0


def e_of(tq, d0):
    sq = np.clip(tq / tr, 0, 1)
    return d0 * (3 * sq ** 2 - 2 * sq ** 3)


def edd_of(tq, d0):
    if tq <= 0 or tq >= tr:
        return 0.0
    return d0 * (6 - 12 * tq / tr) / tr ** 2


def u_field(tq, d0):
    ek = np.fft.fft2(blob) * e_of(tq, d0)
    eddk = np.fft.fft2(blob) * edd_of(tq, d0)
    uk = -ek / (4 * Kv * wbv * P2) + Cq * eddk / P2 ** 2
    uk[0, 0] = 0.0
    return np.real(np.fft.ifft2(uk))


sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])


def Sop(psi, ax):  # (T - T^dag)/(2i) along axis ax
    return (np.roll(psi, -1, axis=ax) - np.roll(psi, 1, axis=ax)) / (2j)


def Hw(psi, w):
    phs_ = np.sqrt(w)[..., None]
    f = phs_ * psi
    g = np.einsum("ab,xyb->xya", sx, Sop(f, 0)) + np.einsum("ab,xyb->xya", sy, Sop(f, 1))
    return phs_ * g


def force(psi, w):  # d<S_x>/dt = <i [H_w, S_x]>
    return float(np.real(np.vdot(psi, 1j * (Hw(Sop(psi, 0), w) - Sop(Hw(psi, w), 0)))))


def packet(r):
    """positive-energy packet at rest: wave number pi/2 along y (group speed cos(pi/2) = 0), coin (1, i)/sqrt 2 (+ branch of sigma_y)"""
    g = np.exp(-((X - (c0 + r)) ** 2 + (Y - c0) ** 2) / (2 * 3.0 ** 2)) * (1j ** Y)
    psi = np.zeros((Lx, Lx, 2), complex)
    psi[..., 0] = g
    psi[..., 1] = 1j * g
    return psi / np.linalg.norm(psi)


rows = []
for r in (8, 16):
    for d0 in (0.02, 0.04):
        psi = packet(r)
        f_before = force(psi, np.ones((Lx, Lx)))
        f_early = force(psi, np.exp(u_field(0.05, d0)))
        f_after = force(psi, np.exp(u_field(tr, d0)))
        en = float(np.real(np.vdot(psi, Hw(psi, np.ones((Lx, Lx))))))
        ux = u_field(tr, d0)
        wts = np.sum(np.abs(psi) ** 2, axis=2)
        grad = np.sum(wts * (np.roll(ux, -1, 0) - np.roll(ux, 1, 0)) / 2)
        rows.append((r, d0, f_before, f_early, f_after, en, -en * grad))
        print(f"EXEC E r={r} Delta_e={d0}: packet energy {en:.4f}; d<S_x>/dt before {f_before:+.3e}, at t=0.05 {f_early:+.3e}, after the switch-on {f_after:+.3e} "
              f"(block 54's -E <grad u> = {-en * grad:+.3e}); TT wave would arrive at t = {r / cT:.0f}")
lin = all(abs(rows[i + 1][4] / rows[i][4] - 2) < 1e-3 for i in (0, 2))
print("linear in Delta_e:", lin, "; after-switch-on force against -E<grad u> within 5 per cent:", all(abs(r_[4] / r_[6] - 1) < 0.05 for r_ in rows))
