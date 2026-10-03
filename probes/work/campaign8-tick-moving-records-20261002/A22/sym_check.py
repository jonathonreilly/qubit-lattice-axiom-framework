#!/usr/bin/env python3
"""A22 task 1 (supplied toy): which number-conserving steps / interactions keep the joint staggering
Lambda = prod_s sigma_s^{n_s} (sigma = + - - + period 4) as a time-doubler symmetry,
    Lambda U Lambda^-1 = (-1)^N U   (many-body, all N at once),
and checks the 'flipped sector is free' claim in the 2-excitation sector.

Ring of L qubits (L = 0 mod 4).  Gate on bond (s,t): g(theta, phi) = exp(-i theta SWAP) * diag(1,1,1,e^{i phi}) in
basis |n_s n_t> = 00,01,10,11.  Even layer = bonds (2j,2j+1), odd layer = bonds (2j+1,2j+2).
"""
import numpy as np
from itertools import product

L = 8
dim = 2 ** L
PI = np.pi
sig = np.array([1, -1, -1, 1] * (L // 4))
basis = np.array(list(product([0, 1], repeat=L)))[:, ::-1]   # basis[i, s] = n_s of state i (s=0 least significant)
idx = basis @ (1 << np.arange(L))
assert np.all(idx == np.arange(dim))
N = basis.sum(1)
Lam = np.prod(np.where(basis == 1, sig[None, :], 1), axis=1).astype(float)
parN = (-1.0) ** N

SW = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], complex)


def gate(theta, phi=0.0, diag=None):
    # exp(-i theta SWAP) = cos(theta) 1 - i sin(theta) SWAP  (SWAP^2 = 1)
    g = np.cos(theta) * np.eye(4) - 1j * np.sin(theta) * SW
    g = g @ np.diag([1, 1, 1, np.exp(1j * phi)])
    if diag is not None:
        g = g @ np.diag(diag)
    return g


def apply2(M, g, s, t):
    """Left-multiply full operator M (dim x dim) by 2-qubit gate g on sites s, t (s -> first index of g)."""
    out = np.zeros_like(M)
    bs, bt = basis[:, s], basis[:, t]
    loc = 2 * bs + bt
    for a in range(4):
        sa, ta = a >> 1, a & 1
        # target states: replace (n_s, n_t) by (sa, ta)
        tgt = idx - (bs << s) - (bt << t) + (sa << s) + (ta << t)
        np.add.at(out, tgt, g[a, loc][:, None] * M)
    return out


def layer(M, g, parity, step=1):
    for j in range(parity, L, 2):
        M = apply2(M, g, j, (j + step) % L)
    return M


def diag_layer(M, phases):
    return np.exp(1j * phases)[:, None] * M


def nnn_diag(phi2):
    """diagonal phase phi2 on configurations with n_s n_{s+2} = 1 (all s)."""
    return phi2 * sum(basis[:, s] * basis[:, (s + 2) % L] for s in range(L))


def nnn_full(M):
    for s0 in range(0, L, 4):
        M = apply2(M, gate(PI / 2), s0, s0 + 2)
        M = apply2(M, gate(PI / 2), s0 + 1, (s0 + 3) % L)
    return M


def build(th_e, th_o, ph_e=0.0, ph_o=0.0, extra=None):
    U = np.eye(dim, dtype=complex)
    U = layer(U, gate(th_e, ph_e), 0)
    U = layer(U, gate(th_o, ph_o), 1)
    if extra is not None:
        U = extra(U)
    return U


def lam_residual(U):
    LUL = Lam[:, None] * U * Lam[None, :]
    return np.linalg.norm(LUL - parN[:, None] * U) / np.linalg.norm(U), np.linalg.norm(LUL - U) / np.linalg.norm(U)


m = 0.6
cases = [
    ("S1 step: full swap (even) + partial swap pi/2-m (odd)", dict(th_e=PI / 2, th_o=PI / 2 - m)),
    ("+ |11> phase 0.9 on odd (equal-sign) bonds", dict(th_e=PI / 2, th_o=PI / 2 - m, ph_o=0.9)),
    ("+ |11> phase 0.9 on even (flipped, full-swap) bonds", dict(th_e=PI / 2, th_o=PI / 2 - m, ph_e=0.9)),
    ("+ diagonal NNN phase n_s n_{s+2} (0.7)", dict(th_e=PI / 2, th_o=PI / 2 - m,
                                                   extra=lambda U: diag_layer(U, nnn_diag(0.7)))),
    ("+ staggered on-site phase 0.3 (-1)^s n_s", dict(th_e=PI / 2, th_o=PI / 2 - m,
                                                     extra=lambda U: diag_layer(U, 0.3 * basis @ ((-1.0) ** np.arange(L))))),
    ("BREAK: even layer partial, theta_e = pi/2 - 0.1", dict(th_e=PI / 2 - 0.1, th_o=PI / 2 - m)),
    ("BREAK: + NNN partial swap layer exp(-i 0.3 SWAP_{s,s+2})", dict(th_e=PI / 2, th_o=PI / 2 - m,
        extra=lambda U: layer(layer(U, gate(0.3), 0, step=2), gate(0.3), 1, step=2))),
    ("+ extra FULL-swap layer on flipped pairs (0,2),(1,3),(4,6),(5,7)", dict(th_e=PI / 2, th_o=PI / 2 - m,
        extra=lambda U: nnn_full(U))),
    ("small steps: theta_e = theta_o = 0.05 (no full swap)", dict(th_e=0.05, th_o=0.05)),
]
print(f"ring L={L}, sigma={sig.tolist()}, m={m}")
print("residuals  ||L U L^-1 - (-1)^N U|| / ||U||   and   ||L U L^-1 - U|| / ||U||")
for name, kw in cases:
    U = build(**kw)
    un = np.linalg.norm(U.conj().T @ U - np.eye(dim))
    r1, r2 = lam_residual(U)
    print(f"  {name:70s} doubler {r1:.1e}   plain {r2:.1e}   (unitarity {un:.1e})")

# ---- 2-excitation sector: flipped-sector (sigma_x1 sigma_x2 = -1) dynamics equals FREE bosons; equal-sign does not
print("\n2-excitation sector, S1 step (m=0.6): hard-core qubit evolution vs free-boson evolution of the same one-particle step")
U = build(PI / 2, PI / 2 - m)
one = [i for i in range(dim) if N[i] == 1]
pos1 = {i: int(np.argmax(basis[i])) for i in one}
u1 = np.zeros((L, L), complex)
for i in one:
    for k in one:
        u1[pos1[k], pos1[i]] = U[k, i]
two = [i for i in range(dim) if N[i] == 2]
pos2 = {i: tuple(np.nonzero(basis[i])[0]) for i in two}
rng = np.random.default_rng(1)
for label, want in (("flipped (sigma sigma = -1)", -1), ("equal-sign (sigma sigma = +1)", +1)):
    sel = [i for i in two if sig[pos2[i][0]] * sig[pos2[i][1]] == want]
    v = np.zeros(dim, complex); v[sel] = rng.normal(size=len(sel)) + 1j * rng.normal(size=len(sel)); v /= np.linalg.norm(v)
    # free bosons: symmetric matrix psi[x1,x2] (x1 != x2 initially), psi -> u psi u^T, allow double occupancy
    psi = np.zeros((L, L), complex)
    for i in sel:
        a, b = pos2[i]; psi[a, b] = psi[b, a] = v[i] / np.sqrt(2)
    worst_leak, worst_diff = 0.0, 0.0
    w = v.copy()
    for t in range(12):
        w = U @ w
        psi = u1 @ psi @ u1.T / U[0, 0]          # vacuum phase counted once (U[0,0] = <empty|U|empty>)
        leak = np.sum(np.abs(np.diag(psi)) ** 2)            # double occupancy (impossible for qubits)
        q = np.zeros(dim, complex)
        for i in two:
            a, b = pos2[i]; q[i] = np.sqrt(2) * psi[a, b]
        worst_leak = max(worst_leak, leak); worst_diff = max(worst_diff, np.linalg.norm(q - w))
    print(f"  start in {label:28s}: max double-occupancy weight of free bosons {worst_leak:.2e}, "
          f"max ||qubit - free|| over 12 ticks {worst_diff:.2e}")

# ---- one-particle spectrum: invariance under rotation by pi  <=>  max(theta_e, theta_o) = pi/2 ;  doubler mass
print("\none-excitation spectrum on a ring of 4000 sites (closed form + check):  pi-rotation invariance and doubler mass")
K = 2 * PI * np.arange(2000) / 2000


def onebody_phases(te, to):
    c = np.cos(te) * np.cos(to) - np.sin(te) * np.sin(to) * np.cos(K)
    w = np.arccos(np.clip(c, -1, 1))
    ph = np.concatenate([te + to + w, te + to - w]) % (2 * PI)
    return np.sort(ph)


def hausdorff_circle(a, b):
    d = np.abs(((a[:, None] - b[None, :]) + PI) % (2 * PI) - PI)
    return max(d.min(1).max(), d.min(0).max())


for te, to in ((PI / 2, PI / 2 - 0.3), (PI / 2 - 0.3, PI / 2), (PI / 2 - 0.05, PI / 2 - 0.35), (0.6, 0.6), (0.05, 0.05), (1.2, 0.9)):
    ph = onebody_phases(te, to)[::7]
    hd = hausdorff_circle(ph, (ph + PI) % (2 * PI))
    M_ord, M_dbl = abs(te - to), PI - te - to
    print(f"  theta_e={te:.3f} theta_o={to:.3f}: dist(spectrum, spectrum+pi) = {hd:.3f};  cone masses: ordinary |te-to| = {M_ord:.3f}, "
          f"doubler pi-te-to = {M_dbl:.3f}; occupied arc length = {2*(te+to) - 2*abs(te-to):.3f} + gap(s)")

# light speed vs doubler mass for the massless walk theta_e = theta_o = theta : v = sin(theta) = cos(M/2)
print("\nmassless walk theta_e = theta_o = theta: band slope at the cone vs cos(M_doubler/2)")
for th in (PI / 2, 1.2, 0.6, 0.1, 0.006):
    q = 1e-4
    c = np.cos(th) ** 2 - np.sin(th) ** 2 * np.cos(PI + q)
    v = np.arccos(c) / q
    print(f"  theta={th:.4f}: slope {v:.6f}   cos(M/2) = {np.cos((PI - 2*th)/2):.6f}   (cells per tick)")
