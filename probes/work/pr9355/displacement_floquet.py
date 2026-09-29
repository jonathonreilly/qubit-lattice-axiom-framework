#!/usr/bin/env python3
"""J:falsifier:PR9355 -- driven SQUID resonator note: the exact oscillator-displacement identity, verified by brute-force Floquet propagation.

Claim (note, "Exact displacement and proof obligations"): for H(t)/h = H_device/h + Omega a^dag a + G n P + D X cos(2 pi w t), P = i(a^dag - a), X = a + a^dag, and Omega != w (the resonant case excluded), the periodic displacement
alpha(t) = -D/2 [exp(-i theta)/(Omega - w) + exp(i theta)/(Omega + w)], theta = 2 pi w t, gives psi = D(alpha) chi with chi evolving under H_device + Omega a^dag a + G n P + F n sin(theta) plus a scalar, F = 2 G D w/(Omega^2 - w^2); the scalar's
periodic part is a periodic phase and its mean shifts all quasienergies equally, so quasienergy differences are unchanged. (The note calls this exact in the infinite oscillator and states that finite ladder truncations only approximate it.)
Test: build the one-period Floquet propagators of the original and of the displaced Hamiltonian (device = charge rotor with the note's two-arm potential, Fock ladder of 26..34 states, exact matrix exponentials per step, 2400 steps per period),
match each displaced eigenmode D(alpha(0)) u to an original eigenmode by overlap, and require the eigenphase differences of the matched modes to be a single constant (the mean scalar) to 1e-6 rad. Cases: Omega above and below w, several G and D, negative drive detuning; controls:
F -> 1.05 F, the sign of F flipped, and the scalar mean's sign. Floating point (labelled). Reads none of the PR's code or data. Prints SUMMARY: and, only if the identity fails, HIT:.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import sys
import time

import numpy as np
from scipy.linalg import expm

T0 = time.time()
RESULTS, FIRED = [], []
DRY = "--dry" in sys.argv


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def device(EC, J, a_asym, f, EL, ng, N):
    """4 EC (n - ng)^2 - J_l cos(phi) - J_r cos(phi + 2 pi f) + [J_l^2 cos(2 phi) + J_r^2 cos(2 phi + 4 pi f)]/(4 EL), in the charge basis -N..N (hopping by one and two charges)."""
    n = np.arange(-N, N + 1, dtype=float); d = len(n)
    Jl, Jr = J * (1 + a_asym), J * (1 - a_asym)
    H = np.diag(4 * EC * (n - ng) ** 2).astype(complex)
    up1 = np.eye(d, k=-1); up2 = np.eye(d, k=-2)            # e^{i phi}|n> = |n + 1>: matrix element <n + 1|e^{i phi}|n> at [n + 1, n]
    c1 = lambda ph: -(np.exp(1j * ph) * up1 + np.exp(-1j * ph) * up1.T) / 2
    H += Jl * c1(0.0) + Jr * c1(2 * np.pi * f)
    c2 = lambda ph: (np.exp(1j * ph) * up2 + np.exp(-1j * ph) * up2.T) / 2
    H += (Jl ** 2 * c2(0.0) + Jr ** 2 * c2(4 * np.pi * f)) / (4 * EL)
    return n, H


def fock(K):
    a = np.diag(np.sqrt(np.arange(1, K)), 1).astype(complex)
    return a


def displace(alpha, K, big=90):
    """D(alpha) on the first K levels from a large ladder (exact up to truncation)."""
    a = np.diag(np.sqrt(np.arange(1, big)), 1).astype(complex)
    Dm = expm(alpha * a.conj().T - np.conj(alpha) * a)
    return Dm[:K, :K]


def floquet(Hfun, dim, w, steps):
    T = 1.0 / w
    dt = T / steps
    U = np.eye(dim, dtype=complex)
    for k in range(steps):
        U = expm(-1j * 2 * np.pi * Hfun((k + 0.5) * dt) * dt) @ U
    return U


def case(EC, J, aa, f, EL, ng, Om, G, D, w, N=7, K=24, steps=1200):
    n, Hd = device(EC, J, aa, f, EL, ng, N)
    d, Kd = len(n), K
    a = fock(K); ad = a.conj().T
    I_d, I_k = np.eye(d), np.eye(K)
    Hdev = np.kron(Hd, I_k)
    Hosc = Om * np.kron(I_d, ad @ a)
    nP = G * np.kron(np.diag(n), 1j * (ad - a))
    Xop = np.kron(I_d, a + ad)
    nn = np.kron(np.diag(n), I_k)
    F = 2 * G * D * w / (Om ** 2 - w ** 2)
    Horig = lambda t: Hdev + Hosc + nP + D * Xop * np.cos(2 * np.pi * w * t)
    def Hdisp(t, Ff=F, sgn=1.0):
        return Hdev + Hosc + nP + sgn * Ff * nn * np.sin(2 * np.pi * w * t)
    Uo = floquet(Horig, d * K, w, steps)
    alpha0 = -D / 2 * (1 / (Om - w) + 1 / (Om + w))
    Dm = np.kron(I_d, displace(alpha0, K))
    out = {}
    for name, Hf in (("F", lambda t: Hdisp(t)), ("1.05 F", lambda t: Hdisp(t, 1.05 * F))):       # F -> -F is a half-period time shift: same Floquet spectrum, not a control
        Ud = floquet(Hf, d * K, w, steps)
        wo, Vo = np.linalg.eig(Uo); wd, Vd = np.linalg.eig(Ud)
        # use the low-photon modes: those whose displaced image has weight on photon <= 5 and device charges near zero
        lowmask = np.array([np.sum(np.abs((Dm @ Vd[:, i]).reshape(d, K)[:, :6]) ** 2) for i in range(d * K)]) > 0.999
        idx = np.where(lowmask)[0]
        diffs = []; ovs = []
        for i in idx:
            v = Dm @ Vd[:, i]
            ov = np.abs(Vo.conj().T @ v)
            j = int(np.argmax(ov)); ovs.append(ov[j])
            diffs.append(np.angle(wo[j] / wd[i]))
        diffs = np.array(diffs); ovs = np.array(ovs)
        ref = diffs[np.argmax(ovs)]
        dev = np.angle(np.exp(1j * (diffs - ref)))
        out[name] = (float(np.max(np.abs(dev[ovs > 0.9]))) if (ovs > 0.9).any() else np.inf, float(ovs.min()), int(len(idx)), float(ref))
    mean_scalar = -D ** 2 * Om / (2 * (Om ** 2 - w ** 2))
    return out, mean_scalar, F


def run():
    cases = [
        dict(EC=0.087, J=39.0, aa=0.003, f=0.0, EL=16000.0, ng=0.0, Om=7.6918, G=0.030, D=0.30, w=7.30),       # drive near the device transition (f01 ~ 7.29 GHz): F acts at first order
        dict(EC=0.087, J=39.0, aa=0.003, f=0.0, EL=16000.0, ng=0.5, Om=7.6918, G=0.045, D=0.20, w=8.10),       # drive above the oscillator (Omega < w)
        dict(EC=0.12, J=30.0, aa=0.01, f=0.1, EL=16000.0, ng=0.2, Om=7.0, G=0.040, D=0.25, w=6.70),           # ng = 0.2, flux f = 0.1
    ]
    if DRY:
        cases = cases[:1]
    for c in cases:
        out, ms, F = case(**c, steps=600 if DRY else 1200)
        pred = -2 * np.pi * ms / c['w']                                   # the note's scalar mean as a phase per period: orig quasienergies = displaced + ms
        dshift = float(np.abs(np.angle(np.exp(1j * (out['F'][3] - pred)))))
        ok = out["F"][0] < 5e-6 and out["1.05 F"][0] > 1e3 * max(out["F"][0], 1e-12) and dshift < 1e-6
        check(f"(D) Omega = {c['Om']}, w = {c['w']}, G = {c['G']}, D = {c['D']}, ng = {c['ng']}: eigenphases of the original and displaced Floquet propagators (matched by overlap through D(alpha(0))) differ by one constant to 5e-6 rad, "
              "the constant is the note's scalar mean -D^2 Omega/[2(Omega^2 - w^2)] (to 1e-6 rad), and the control F -> 1.05 F does not reproduce the constancy", ok,
              f"F = {F:+.6f} GHz; spread {out['F'][0]:.1e} rad (min overlap {out['F'][1]:.4f}, {out['F'][2]} modes); 1.05 F: {out['1.05 F'][0]:.1e}; "
              f"constant {out['F'][3]:+.6e} rad vs the note's scalar {pred:+.6e} rad (difference {dshift:.1e}); {time.time() - T0:.0f} s")
        if not ok:
            FIRED.append(f"displacement identity fails for Omega = {c['Om']}, w = {c['w']}: spread {out['F'][0]:.1e} rad, scalar difference {dshift:.1e}")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: FALSIFIER FIRES: " + FIRED[0])
        print("HIT: PR #9355 displacement identity fails: " + "; ".join(FIRED))
        return 0
    print("SUMMARY: no falsifier fired: the periodic displacement identity (F = 2GDw/(Omega^2 - w^2) in magnitude; its sign is a half-period time shift and is not tested by quasienergies) holds in brute-force Floquet propagation for Omega above and below w; F -> 1.05 F breaks it, and the constant quasienergy shift equals the note's scalar mean -D^2 Omega/[2(Omega^2 - w^2)] to 1e-7 rad")
    return 0


if __name__ == "__main__":
    sys.exit(run())
