#!/usr/bin/env python3
"""J:attack-g:PR9359 -- PROOF STEP BY BRUTE FORCE: the spatial-averaging identity of the microscopic-transmon note.

Note: 'A spatially uniform local harmonic on a rectangular junction with linear imposed phase acquires signed sinc(m B/Bnode), and two such arm potentials add with relative phase exp(i m psi)': (1/L) integral_{-L/2}^{L/2} exp[i m (phi + 2 pi (B/Bnode) x/L)] dx = exp(i m phi) sinc(m B/Bnode),
and the charge-basis hopping at signed order m of the two-arm potential is c_|m| [Ja sinc(|m| B/Ba) + Jb sinc(|m| B/Bb) exp(i m psi)], with c_m the Fourier coefficients of the normalised local potential (fundamental -cos(phi)), sinc(z) = sin(pi z)/(pi z).

Verified here literally by numerical quadrature, without using the closed form: the local short-channel potential U(phi) = r_tau(phi)/(-a_1) is averaged over the junction width for each arm at the note's B/Bnode values (x-integral by Gauss-Legendre with 200 nodes), the two arms are added with the phase psi
(second arm evaluated at phi + psi), and the resulting periodic potential V(phi) is Fourier-analysed on 8192 points; its charge-basis matrix elements (Fourier coefficients at order m) are compared with the closed form (1/2) c_m [Ja sinc(m B/Ba) + Jb sinc(m B/Bb) exp(i m psi)] for m = 0..14, several tau and psi (including psi = pi and a generic psi), and
the note's statement 'at psi = pi odd harmonics subtract and even harmonics add algebraically' is checked on the same coefficients.
Prints SUMMARY:; HIT only if a coefficient disagrees.
"""
import sys, numpy as np
B, BA, BB = 0.15, 0.8, 0.8 * 256 / 178
ALPHA = (256 * 257 - 178 * 143) / (256 * 257 + 178 * 143)
def sinc(z): return np.sinc(z)
def local(ph, tau):
    s = np.sin(ph / 2) ** 2
    return 4 * s / (1 + np.sqrt(1 - tau * s))
def coeffs_of(f, M=8192, mmax=14):
    ph = (np.arange(M) + 0.5) * 2 * np.pi / M
    v = f(ph)
    return np.array([np.sum(v * np.exp(-1j * m * ph)) / M for m in range(mmax + 1)])
xs, ws = np.polynomial.legendre.leggauss(200)
ok_all = True; rows = []
for tau in (0.0, 0.117141, 0.5, 0.9):
    a = np.array([2 * c.real for c in coeffs_of(lambda p: local(p, tau))]); a1 = a[1]
    for psi in (np.pi, 0.0, 1.234):
        Jsum = 1.0; Ja, Jb = Jsum * (1 + ALPHA) / 2, Jsum * (1 - ALPHA) / 2
        def arm(ph, J, Bn):
            # (1/L) integral over x in [-L/2, L/2] of U(phi + 2 pi (B/Bn) x/L): substitute u = x/L in [-1/2, 1/2]
            u = 0.5 * xs; w = 0.5 * ws
            return J * sum(wi * (-local(ph + 2 * np.pi * (B / Bn) * ui, tau) / a1) for ui, wi in zip(u, w))
        V = lambda ph: arm(ph, Ja, BA) + arm(ph + psi, Jb, BB)
        num = coeffs_of(V)
        exact = np.zeros(15, dtype=complex)
        for m in range(1, 15):
            cm = -a[m] / a1                                            # cosine coefficient of the normalised local potential
            exact[m] = 0.5 * cm * (Ja * sinc(m * B / BA) + Jb * sinc(m * B / BB) * np.exp(1j * m * psi))
        # order m of V(phi) = sum_m (h_m e^{i m phi} + c.c.): the exponent coefficient of e^{i m phi} is the hopping element
        err = np.max(np.abs(num[1:] - exact[1:]))
        scale = np.max(np.abs(exact[1:]))
        ok = err < 1e-10 * max(scale, 1.0)
        ok_all &= ok; rows.append((tau, psi, err))
        print(f"   tau = {tau:g}, psi = {psi:.4f}: max |numerical - closed form| over m = 1..14 is {err:.2e} (largest coefficient {scale:.3f})", flush=True)
        if abs(psi - np.pi) < 1e-12:
            alg = np.array([0.5 * (-a[m] / a1) * (Ja * sinc(m * B / BA) + (-1) ** m * Jb * sinc(m * B / BB)) for m in range(1, 15)])
            e2 = np.max(np.abs(num[1:] - alg))
            ok_alg = e2 < 1e-10
            print(f"      psi = pi: h_m = (1/2) c_m [Ja sinc(m B/Ba) + (-1)^m Jb sinc(m B/Bb)] (odd orders subtract, even orders add algebraically) reproduces the numerical coefficients to {e2:.2e}: {ok_alg}")
            ok_all &= ok_alg
print(f"[{'PASS' if ok_all else 'FAIL'}] the numerically averaged, arm-summed potential has the charge-basis coefficients (1/2) c_m [Ja sinc(m B/Ba) + Jb sinc(m B/Bb) exp(i m psi)] to 1e-10 for m = 1..14, tau in (0, 0.117, 0.5, 0.9), psi in (pi, 0, 1.234)")
if ok_all:
    print("SUMMARY: no purchase: quadrature over the junction width and Fourier analysis reproduce the note's sinc-envelope hopping coefficients for both arms to 1e-10, at psi = pi and a generic psi, and the odd-subtract / even-add statement at psi = pi holds")
else:
    print("SUMMARY: a coefficient disagrees: " + str([r for r in rows if r[2] > 1e-10][:2])); print("HIT: the spatial-averaging identity does not reproduce the closed-form coefficients")
sys.exit(0)
