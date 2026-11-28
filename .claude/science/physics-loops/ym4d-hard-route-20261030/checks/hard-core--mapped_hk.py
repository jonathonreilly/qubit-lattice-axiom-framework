#!/usr/bin/env python3
"""(HK) of Text 3.7 in the flux plane: covariant heat-kernel words at constant flux, d = 2 torus.

Written before running. N x N torus, flux theta = 2 pi m / N^2 per plaquette, Landau gauge U_2(x) = e^{i theta x_1}, with the
transition on the wrap of x_1. T_mu psi(x) = U_mu(x) psi(x + e_mu), D_mu = T_mu - 1, Dbar_mu = T_mu^* - 1, X = sum D_mu^* D_mu.
For a word W of length n: K_theta(y) := [e^{-tau X} W e^{-tau' X}](y, 0) e^{-i theta y_1 y_2 / 2}, the gauge-invariant kernel,
for |y| small against N. With T = tau + tau'. In d = 2 the claims read, with the Gaussian weight G := exp(-|y|^2/(8 T)), floored at 1e-6:

 HK2 (second order): S2 := sup_{T, y} |K_theta + K_{-theta} - 2 K_0| / (2 theta^2 T^{1 - n/2} G).
 HK1 (first order):  S1 := sup_{T, y} |K_theta - K_{-theta}| / (2 theta T^{-n/2} G).

 K_{-theta} is computed with theta -> -theta directly.

PRE-STATED criteria, for each word, over T in {4, 8, 16, 32}, tau = tau' = T/2 and tau = T, tau' = 0:
 C1. Stability in the volume: S2 and S1 at N = 64 are at most 1.5 times their values at N = 48, at m = 1.
 C2. Stability in theta: at N = 48, S2 and S1 at m = 2 are at most 1.5 times their values at m = 1.
 C3. Scaling in T, which is the claim: S2 and S1 restricted to T = 32 are at most 3 times those restricted to T = 8, at N = 64, m = 1.
 C0. Control at n = 0: K_theta(0) has second order -(1/6) tau-type area coefficient: |K_theta(0)/K_0(0) - 1| <= theta^2 T^2 for T = 32.
FAIL if any fails. Limitation: only the plane; the transverse directions factor exactly. RSS guard 2 GB.
"""
import resource
import sys

import numpy as np
import scipy.sparse as sp_


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def build(N, theta):
    """Returns T1, T2 as sparse matrices."""
    n = N * N
    idx = lambda a, b: (a % N) * N + (b % N)
    r, c1, v1, c2, v2 = [], [], [], [], []
    for a in range(N):
        for b in range(N):
            i = idx(a, b)
            # bond 1: from (a,b) to (a+1,b); wrap carries the transition of the Landau gauge
            # The gauge is centred at the origin, so its jump is at the bond from a = N//2 - 1 to N//2, and the
            # transition phase belongs there. (First run had it at a = N - 1, next to the origin: a test bug, which put a
            # flux line of size theta N beside the base point. That run reported FAIL, on C0, C1, C2. See hk.first.out.)
            ph1 = np.exp(-1j * theta * N * b) if a == N // 2 - 1 else 1.0
            ca = a if a < N // 2 else a - N  # centre the gauge at the origin
            r.append(i)
            c1.append(idx(a + 1, b))
            v1.append(ph1)
            c2.append(idx(a, b + 1))
            v2.append(np.exp(1j * theta * ca))
    T1 = sp_.csr_matrix((v1, (r, c1)), shape=(n, n), dtype=complex)
    T2 = sp_.csr_matrix((v2, (r, c2)), shape=(n, n), dtype=complex)
    return T1, T2


def flux_defect(T1, T2, N, theta):
    """Largest deviation of plaquette holonomy from e^{i theta}, on the whole torus."""
    idx = lambda a, b: (a % N) * N + (b % N)
    worst = 0.0
    for a in range(N):
        for b in range(N):
            u = (
                T1[idx(a, b), idx(a + 1, b)]
                * T2[idx(a + 1, b), idx(a + 1, b + 1)]
                * np.conj(T1[idx(a, b + 1), idx(a + 1, b + 1)])
                * np.conj(T2[idx(a, b), idx(a, b + 1)])
            )
            worst = max(worst, abs(u - np.exp(1j * theta)))
    return worst


def setup(N, theta):
    T1, T2 = build(N, theta)
    fd = flux_defect(T1, T2, N, theta)
    if fd > 1e-9:
        raise SystemExit(f"flux defect {fd} at N={N}, theta={theta}: test bug")
    I = sp_.identity(N * N, dtype=complex, format="csr")
    D1, D2 = T1 - I, T2 - I
    B1, B2 = T1.conj().T - I, T2.conj().T - I
    X = (D1.conj().T @ D1 + D2.conj().T @ D2).toarray()
    w, v = np.linalg.eigh(X)
    del X
    if rss_gb() > 1.9:
        raise SystemExit("RSS above 1.9 GB")
    return dict(N=N, theta=theta, D={"1": D1, "2": D2, "a": B1, "b": B2}, w=w, v=v)


def apply_heat(s, tau, psi):
    return s["v"] @ (np.exp(-tau * s["w"]) * (s["v"].conj().T @ psi))


def kernel(s, word, tau, taup):
    N = s["N"]
    psi = np.zeros(N * N, dtype=complex)
    psi[0] = 1.0
    psi = apply_heat(s, taup, psi)
    for ch in reversed(word):
        psi = s["D"][ch] @ psi
    psi = apply_heat(s, tau, psi)
    K = psi.reshape(N, N)
    a = np.arange(N)
    a = np.where(a < N // 2, a, a - N)
    y1, y2 = np.meshgrid(a, a, indexing="ij")
    return K * np.exp(-1j * s["theta"] * y1 * y2 / 2), y1, y2


WORDS = ["", "11", "12", "1a", "1212", "1122", "1a2b", "121212", "112122", "1a2b1a"]
TS = [4, 8, 16, 32]


def scan(N, m, zero):
    theta = 2 * np.pi * m / N**2
    sp, sm = setup(N, theta), setup(N, -theta)
    out = {}
    for w in WORDS:
        n = len(w)
        per_T = {}
        for T in TS:
            s2 = s1 = 0.0
            for tau, taup in ((T / 2, T / 2), (T, 0.0)):
                Kp, y1, y2 = kernel(sp, w, tau, taup)
                Km, _, _ = kernel(sm, w, tau, taup)
                K0, _, _ = kernel(zero, w, tau, taup)
                G = np.maximum(np.exp(-(y1**2 + y2**2) / (8 * T)), 1e-6)
                mask = (np.abs(y1) <= N // 4) & (np.abs(y2) <= N // 4)
                d2 = np.abs(Kp + Km - 2 * K0) / (2 * theta**2 * T ** (1 - n / 2) * G)
                d1 = np.abs(Kp - Km) / (2 * theta * T ** (-n / 2) * G)
                s2 = max(s2, float(d2[mask].max()))
                s1 = max(s1, float(d1[mask].max()))
            per_T[T] = (s2, s1)
        out[w] = per_T
    del sp, sm
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")
    return out, theta


def agg(t):
    return max(v[0] for v in t.values()), max(v[1] for v in t.values())


def main():
    z48 = setup(48, 0.0)
    r48_1, th48 = scan(48, 1, z48)
    print(f"done N=48 m=1 rss={rss_gb():.2f}GB", flush=True)
    r48_2, _ = scan(48, 2, z48)
    print(f"done N=48 m=2 rss={rss_gb():.2f}GB", flush=True)
    del z48
    z64 = setup(64, 0.0)
    r64_1, th64 = scan(64, 1, z64)
    print(f"done N=64 m=1 rss={rss_gb():.2f}GB", flush=True)
    ok = True
    for w in WORDS:
        a48, a64, a48b = agg(r48_1[w]), agg(r64_1[w]), agg(r48_2[w])
        c1 = a64[0] <= 1.5 * a48[0] and a64[1] <= 1.5 * a48[1] + 1e-9
        c2 = a48b[0] <= 1.5 * a48[0] and a48b[1] <= 1.5 * a48[1] + 1e-9
        s8, s32 = r64_1[w][8], r64_1[w][32]
        c3 = s32[0] <= 3 * s8[0] + 1e-9 and s32[1] <= 3 * s8[1] + 1e-9
        ok = ok and c1 and c2 and c3
        print(
            f"word '{w}' n={len(w)}: S2={a48[0]:.3g}/{a64[0]:.3g}/{a48b[0]:.3g} S1={a48[1]:.3g}/{a64[1]:.3g}/{a48b[1]:.3g} "
            f"T8->T32 S2 {s8[0]:.3g}->{s32[0]:.3g} S1 {s8[1]:.3g}->{s32[1]:.3g} C1={c1} C2={c2} C3={c3}",
            flush=True,
        )
    K, _, _ = kernel(setup(64, th64), "", 16.0, 16.0)
    K0, _, _ = kernel(z64, "", 16.0, 16.0)
    rel = abs(K[0, 0] / K0[0, 0] - 1)
    c0 = rel <= th64**2 * 32**2
    print(f"C0 |K_theta(0)/K_0(0) - 1| = {rel:.3e}, theta^2 T^2 = {th64**2*32**2:.3e}, {c0}")
    ok = ok and c0
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
