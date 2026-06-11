"""Free bilinear exact-log quasilocal Lieb-Robinson bridge.

Companion to
docs/FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md.

This runner checks the missing composition step between the retained
transfer-matrix log quasilocality theorem and the parent microcausality row:
an exponentially decaying bilinear hopping kernel with finite weighted
overlap norm gives a finite-velocity Lieb-Robinson bound by a direct
weighted-path expansion.

Scope: free U=1 bilinear two-step sector only. Gauged/interacting log-transfer
locality is not checked here.
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from transfer_matrix_log_quasilocality_check_2026_06_10 import (  # noqa: E402
    C_strip,
    dispersion,
    eta_star,
    kernel_1d,
    kernel_3d,
)

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(cond)
    FAIL += int(not cond)
    return cond


def shell_sum_bound(eta: float, mu: float, m: float, d: int, rmax: int = 5000) -> float:
    """Closed shell-sum upper bound for W_mu from the cited kernel bound.

    Q1 of the log-quasilocality theorem gives
        |h(z)| <= C exp(-eta ||z||_inf).
    Since ||z||_1 <= d ||z||_inf, the weighted sum with exp(mu ||z||_1)
    converges when eta > d mu.
    """
    assert eta > d * mu
    C = C_strip(eta, m, d)
    total = C
    for r in range(1, rmax + 1):
        shell = (2 * r + 1) ** d - (2 * r - 1) ** d
        term = C * shell * math.exp(-(eta - d * mu) * r)
        total += term
        if term < 1e-14 and r > 50:
            break
    return total


def weighted_norm_1d_resolvable(m: float, mu: float, ncut: int = 200, nfft: int = 8192) -> float:
    """Numerical partial weighted norm over the resolvable 1D window.

    The analytic shell sum supplies the infinite tail. Summing the FFT kernel
    all the way to N/2 is the wrong numerical test because machine-floor
    coefficients get multiplied by exp(mu n).
    """
    h = kernel_1d(m, nfft)
    ns = np.arange(1, ncut + 1)
    return float(abs(h[0]) + 2.0 * np.sum(np.abs(h[ns]) * np.exp(mu * ns)))


def weighted_norm_3d(m: float, mu: float, n: int = 64) -> float:
    h = kernel_3d(m, n)
    off = np.minimum(np.arange(n), n - np.arange(n))
    dx, dy, dz = np.meshgrid(off, off, off, indexing="ij", sparse=True)
    dist = dx + dy + dz
    return float(np.sum(np.abs(h) * np.exp(mu * dist)))


def pauli_ops() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    sp = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    sm = np.array([[0.0, 0.0], [1.0, 0.0]], dtype=complex)
    return sx, sy, sz, sp, sm


def embed_one(op: np.ndarray, site: int, L: int) -> np.ndarray:
    out = np.array([[1.0]], dtype=complex)
    eye = np.eye(2, dtype=complex)
    for i in range(L):
        out = np.kron(out, op if i == site else eye)
    return out


def embed_two(op1: np.ndarray, i: int, op2: np.ndarray, j: int, L: int) -> np.ndarray:
    out = np.array([[1.0]], dtype=complex)
    eye = np.eye(2, dtype=complex)
    for k in range(L):
        if k == i:
            out = np.kron(out, op1)
        elif k == j:
            out = np.kron(out, op2)
        else:
            out = np.kron(out, eye)
    return out


def expm_hermitian(c: complex, H: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(H)
    return vecs @ np.diag(np.exp(c * vals)) @ vecs.conj().T


def comm_norm(A: np.ndarray, B: np.ndarray) -> float:
    return float(np.linalg.norm(A @ B - B @ A, ord=2))


def finite_chain_hamiltonian_from_kernel(m: float, L: int) -> tuple[np.ndarray, float]:
    """Small hard-core bilinear test Hamiltonian using the exact-log kernel.

    This is only a finite-matrix witness for the theorem's constants. The
    theorem itself is the weighted-path proof in the note.
    """
    _sx, _sy, sz, sp, sm = pauli_ops()
    h = kernel_1d(m, 8192)
    dim = 2 ** L
    H = np.zeros((dim, dim), dtype=complex)
    h0 = float(h[0])
    for i in range(L):
        n_i = 0.5 * (np.eye(dim, dtype=complex) - embed_one(sz, i, L))
        H += h0 * n_i
    for i in range(L):
        for j in range(i + 1, L):
            c = float(h[j - i])
            H += c * (embed_two(sp, i, sm, j, L) + embed_two(sm, i, sp, j, L))
    local_weight = abs(h0) + 2.0 * sum(abs(float(h[r])) for r in range(1, L))
    return H, local_weight


def main() -> None:
    print("FREE BILINEAR EXACT-LOG QUASILOCAL LR BRIDGE")
    print("=" * 72)
    print("Scope: U=1 bilinear two-step sector; exact H=-log(T_hat^2)/(2 a_tau).")
    print()

    m = 0.3
    eta = 0.8 * eta_star(m)
    mu1 = 0.5 * eta
    W1 = weighted_norm_1d_resolvable(m, mu1)
    B1 = shell_sum_bound(eta, mu1, m, 1)
    check("Q1: d=1 weighted overlap W_mu is finite and below the cited strip-bound shell sum",
          W1 < B1 and math.isfinite(W1),
          f"eta={eta:.6f}, mu={mu1:.6f}, W_mu={W1:.6f}, shell_bound={B1:.6f}")

    mu3 = 0.18 * eta_star(m) / 3.0
    eta3 = 0.8 * eta_star(m)
    W3 = weighted_norm_3d(m, mu3, n=64)
    B3 = shell_sum_bound(eta3, mu3, m, 3)
    check("Q2: Z^3 weighted overlap W_mu is finite when 3*mu < eta < arcsinh(m)",
          W3 < B3 and math.isfinite(W3),
          f"eta={eta3:.6f}, mu={mu3:.6f}, W_mu(64^3)={W3:.6f}, shell_bound={B3:.6f}")

    # Symbolic path-bound identity checked numerically on a grid:
    # sum_paths prod |h| <= exp(-mu d) W_mu^n.
    h = kernel_1d(m, 8192)
    offsets = np.arange(0, 80)
    weights = np.array([abs(float(h[k])) for k in offsets])
    W_path = float(weights[0] + 2.0 * np.sum(weights[1:] * np.exp(mu1 * offsets[1:])))
    path_ok = True
    worst = 0.0
    for nstep in range(1, 5):
        conv = np.array([1.0])
        step = np.zeros(2 * len(offsets) - 1)
        center = len(offsets) - 1
        step[center] = weights[0]
        for k in range(1, len(offsets)):
            step[center + k] = weights[k]
            step[center - k] = weights[k]
        for _ in range(nstep):
            conv = np.convolve(conv, step)
        conv_center = (len(conv) - 1) // 2
        for dist in range(2, 18):
            val = conv[conv_center + dist]
            bound = math.exp(-mu1 * dist) * (W_path ** nstep)
            ratio = val / bound if bound else 0.0
            worst = max(worst, ratio)
            if ratio > 1.000001:
                path_ok = False
    check("Q3: weighted convolution path bound holds for sampled path lengths",
          path_ok, f"worst sampled path/bound ratio={worst:.6f}")

    L = 7
    H, W_finite = finite_chain_hamiltonian_from_kernel(m, L)
    _sx, _sy, sz, _sp, _sm = pauli_ops()
    O0 = embed_one(sz, 0, L)
    normO = float(np.linalg.norm(O0, ord=2))
    finite_ok = True
    worst_ratio = 0.0
    for site in range(2, L):
        Oy = embed_one(sz, site, L)
        d = site
        for t in (0.02, 0.05, 0.1):
            U = expm_hermitian(1j * t, H)
            At = U @ O0 @ U.conj().T
            measured = comm_norm(At, Oy)
            bound = 2.0 * normO * normO * math.exp(-mu1 * d + 4.0 * W1 * t)
            ratio = measured / bound if bound else 0.0
            worst_ratio = max(worst_ratio, ratio)
            if measured > bound + 1e-10:
                finite_ok = False
    check("Q4: finite hard-core bilinear matrix witness obeys the quasilocal LR envelope",
          finite_ok,
          f"L={L}, finite local weight={W_finite:.6f}, theorem W_mu={W1:.6f}, "
          f"worst measured/bound={worst_ratio:.6e}")

    # Falsification leg: a positive symbol with algebraic Fourier tail has no
    # stable exponential weighted norm as the cutoff grows.
    p = 2.0 * np.pi * np.arange(8192) / 8192
    E = dispersion(0.5, p)
    tail = np.zeros_like(E)
    for k in range(1, 400):
        tail += k ** -3.0 * np.cos(k * p)
    E_bad = E + 0.05 * tail
    h_bad = np.fft.ifft(E_bad).real
    def bad_weight(cut: int) -> float:
        ns = np.arange(1, cut + 1)
        return float(abs(h_bad[0]) + 2.0 * np.sum(np.abs(h_bad[ns]) * np.exp(mu1 * ns)))
    b100 = bad_weight(100)
    b300 = bad_weight(300)
    check("Q5: long-range-tailed positive comparator does not have the stable exponential weighted norm",
          b300 > 1.5 * b100,
          f"W_bad(100)={b100:.3e}, W_bad(300)={b300:.3e}")

    print()
    print(f"RESULT: for any mu with 0 < d*mu < eta < arcsinh(m), W_mu < infinity and")
    print("        ||[alpha_t(A_x), B_y]|| <= 2||A||||B|| exp(-mu d(x,y) + 4 W_mu |t|).")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
