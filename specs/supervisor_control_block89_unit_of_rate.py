#!/usr/bin/env python3
"""Supervisor control for block 89 (disjoint machinery: floating-point zone sums and real-space spectra; evidence, not proof).

W1: zone averages on midpoint grids to 256^3: <1/|s|>, <|s|>, chi = <sum cos^2/|s|>, chi_a = 9<s_x^2(s_y^2+s_z^2)/|s|^3>; the identity
    3<1/|s|> = chi + <|s|>; the thresholds <1/|s|>/4 (log) and chi/12 (linear); (chi_a + 2<|s|>)/72 and chi_a/72.
W2: real space, 6^3 torus: the walk with bond amplitudes e^{+-delta} on every axis - its full spectrum against sqrt(sum sin^2 k + 3 sinh^2 delta)
    over the torus's wave vectors; and the relation E_sea,log(delta) = cosh(delta) E_sea,lin(tanh delta).
W3: the balance at all strengths in log rates with the law quadratic in log rates: for kappa across the threshold, the local character of the
    uniform field, an interior local minimum, the barrier and the first delta beyond it where the energy falls below the uniform value.
W4: the crowd (block 85's machinery, 3x3 torus, 4 and 6 records) under the log alternation: its second-order coefficient per site against the
    linear one plus the Jensen term |E(0)| per site.
"""
import itertools
import sys

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spl

SIG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]


def zone(L):
    k = 2 * np.pi * (np.arange(L) + 0.5) / L
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    return np.sin(kx) ** 2, np.sin(ky) ** 2, np.sin(kz) ** 2


def w1():
    print("W1: zone averages and thresholds")
    for L in (64, 128, 256):
        a, b, c = zone(L)
        s = np.sqrt(a + b + c)
        inv, ms = float(np.mean(1 / s)), float(np.mean(s))
        chi = float(np.mean((3 - (a + b + c)) / s))
        chia = float(9 * np.mean(a * (b + c) / s ** 3))
        print(f"  L={L}: <1/|s|>={inv:.5f} <|s|>={ms:.5f} chi={chi:.5f} chi_a={chia:.5f}; 3<1/|s|> - chi - <|s|> = {3 * inv - chi - ms:.1e}; "
              f"kappa_c log {inv / 4:.5f} vs linear {chi / 12:.5f}; beta_c log {(chia + 2 * ms) / 72:.5f} vs linear {chia / 72:.5f}")


def walk_log(L, delta):
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    N = L ** 3
    H = np.zeros((2 * N, 2 * N), dtype=complex)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = idx(x, y, z)
                for a, (dx, dy, dz) in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                    coord = (x, y, z)[a]
                    t = np.exp(delta * (-1) ** coord)
                    j = idx(x + dx, y + dy, z + dz)
                    blk = SIG[a] * t / 2j
                    H[2 * i:2 * i + 2, 2 * j:2 * j + 2] += blk
                    H[2 * j:2 * j + 2, 2 * i:2 * i + 2] += blk.conj().T
    return H


def w2():
    print("W2: 6^3 torus, amplitudes e^{+-delta}: spectrum against sqrt(sum sin^2 + 3 sinh^2 delta)")
    L = 6
    for delta in (0.2, 0.5):
        H = walk_log(L, delta)
        ev = np.sort(np.linalg.eigvalsh(H))
        ks = 2 * np.pi * np.arange(L) / L
        pred = np.sort(np.array([sgn * np.sqrt(sum(np.sin(k) ** 2 for k in kv) + 3 * np.sinh(delta) ** 2) for kv in itertools.product(ks, ks, ks) for sgn in (1, -1)]))
        pred = np.sort(np.concatenate([pred]))
        e_log = float(np.sum(ev[ev < 0])) / L ** 3
        a, b, c = zone(64)
        s2 = a + b + c
        e_lin_scaled = float(np.cosh(delta) * -np.mean(np.sqrt(s2 + np.tanh(delta) ** 2 * (3 - s2))))
        e_log_zone = float(-np.mean(np.sqrt(s2 + 3 * np.sinh(delta) ** 2)))
        print(f"  delta={delta}: max |spectrum - prediction| = {np.max(np.abs(ev - pred)):.2e} (the 6^3 torus's wave vectors: pairs k, k+pi e_j folded); "
              f"zone: cosh(d) E_lin(tanh d) = {e_lin_scaled:.6f}, E_log = {e_log_zone:.6f}")


def w3():
    print("W3: the balance in log rates, E(delta) = -<sqrt(|s|^2 + 3 sinh^2 delta)> + 6 kappa delta^2 (grid 128^3)")
    a, b, c = zone(128)
    s2 = a + b + c
    ds = np.linspace(0, 6, 3001)
    E = np.array([-np.mean(np.sqrt(s2 + 3 * np.sinh(d) ** 2)) for d in ds])
    for kap in (0.30, 0.25, 0.23, 0.2277, 0.225, 0.22, 0.21, 0.20, 0.18, 0.15, 0.10):
        tot = E + 6 * kap * ds ** 2
        d1 = np.diff(tot)
        maxima = [i for i in range(1, len(tot) - 1) if d1[i - 1] > 0 and d1[i] <= 0]
        minima = [i for i in range(1, len(tot) - 1) if d1[i - 1] < 0 and d1[i] >= 0]
        below = [i for i in range(1, len(tot)) if tot[i] < tot[0] - 1e-12 and (not maxima or i > maxima[0])]
        loc = "local minimum" if tot[1] > tot[0] else "unstable"
        mi = f"interior minimum at delta={ds[minima[0]]:.3f} (rest energy sqrt3 sinh = {np.sqrt(3) * np.sinh(ds[minima[0]]):.3f})" if minima else "no interior minimum"
        ba = f"barrier at delta={ds[maxima[0]]:.3f} of height {tot[maxima[0]] - (tot[minima[0]] if minima else tot[0]):.4f}" if maxima else "no barrier"
        fb = f"below the uniform value from delta={ds[below[0]]:.3f}" if below else "never below"
        print(f"  kappa={kap}: uniform {loc}; {mi}; {ba}; {fb}")


def compressed_ground(H1, n_rec):
    d = H1.shape[0]
    site = np.arange(d) // 2
    basis = [s for s in itertools.combinations(range(d), n_rec) if len({site[o] for o in s}) == n_rec]
    index = {s: i for i, s in enumerate(basis)}
    by_o = {o: [o2 for o2 in range(d) if abs(H1[o2, o]) > 1e-14] for o in range(d)}
    rows, cols, vals = [], [], []
    for s, i in index.items():
        sset = set(s)
        used = {site[o] for o in s}
        for pos, o in enumerate(s):
            for o2 in by_o[o]:
                if o2 != o and o2 in sset:
                    continue
                if o2 != o and site[o2] != site[o] and site[o2] in used:
                    continue
                new = list(s)
                new[pos] = o2
                order = sorted(range(n_rec), key=lambda k: new[k])
                sgn = 1
                p = list(order)
                for q in range(len(p)):
                    while p[q] != q:
                        r = p[q]
                        p[q], p[r] = p[r], p[q]
                        sgn = -sgn
                rows.append(index[tuple(new[k] for k in order)])
                cols.append(i)
                vals.append(sgn * H1[o2, o])
    Hm = sps.csr_matrix((vals, (rows, cols)), shape=(len(basis), len(basis)))
    return float(np.linalg.eigvalsh(Hm.toarray())[0]) if len(basis) < 800 else float(spl.eigsh(Hm, k=1, which="SA")[0][0])


def torus2d(L, delta, log):
    grid = np.indices((L, L)).reshape(2, -1)
    n = L * L
    H = np.zeros((2 * n, 2 * n), dtype=complex)
    for a in range(2):
        g = grid.copy()
        g[a] = (g[a] + 1) % L
        T = np.zeros((n, n))
        T[np.arange(n), np.ravel_multi_index(g, (L, L))] = 1
        amp = np.exp(delta * (-1.0) ** grid[a]) if log else 1 + delta * (-1.0) ** grid[a]
        t = np.diag(amp)
        H += np.kron((t @ T - T.T @ t) / 2j, SIG[a])
    return H


def w4():
    print("W4: the crowd on the 3x3 torus under the log alternation vs linear + Jensen")
    L = 3
    N = L * L
    for n in (4, 6):
        E0 = compressed_ground(torus2d(L, 0.0, True), n) / N
        e = 0.05
        c_log = -(compressed_ground(torus2d(L, e, True), n) / N + compressed_ground(torus2d(L, -e, True), n) / N - 2 * E0) / e ** 2
        c_lin = -(compressed_ground(torus2d(L, e, False), n) / N + compressed_ground(torus2d(L, -e, False), n) / N - 2 * E0) / e ** 2
        print(f"  n={n}: E(0) per site {E0:.5f}; second difference log {c_log:.4f}, linear {c_lin:.4f}, difference {c_log - c_lin:.4f} (Jensen: |E(0)| = {-E0:.4f}; the linear one includes the small tori's linear zero-mode term)")


def main():
    w1()
    w2()
    w3()
    w4()


if __name__ == "__main__":
    sys.exit(main())
