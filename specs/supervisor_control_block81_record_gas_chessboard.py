#!/usr/bin/env python3
"""Supervisor control for block 81 (disjoint machinery: floating-point sampling and dense diagonalisation; evidence, not proof).

W1: the three-dimensional record gas of block 39 at half filling on periodic lattices of side 6 and 8, sampled by transit moves with the
    ratio acceptance and by content re-draws (both in detailed balance with the static law with vacancies at scale c = g c_0):
    the staggered structure factor <(sum_x eps_x n_x)^2>/N and the recorded neighbours per record, against random placement, at the
    allowed scales g = 1, 2, 4 and the excluded g = 1/2, 1/4, 1/8.
W2: the walk H = sum_a sigma_a S_a on a 6^3 torus with the coin-scalar record potential c n_x (block 79's clause, c = 3/5) for three
    backgrounds: the chessboard, a sampled equilibrium arrangement at g = 1, and records on every site; the eigenvalues in (0, c).
"""
import random
import sys

import numpy as np

CONTENTS = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]


def omega(a, b, p, q, r):
    if a[0] != b[0]:
        return r
    return p if a[1] == b[1] else q


def lattice(L):
    N = L ** 3
    nb = np.zeros((N, 6), dtype=np.int64)
    eps = np.zeros(N, dtype=np.int64)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = (x * L + y) * L + z
                eps[i] = (-1) ** (x + y + z)
                k = 0
                for d in (1, -1):
                    nb[i, k] = (((x + d) % L) * L + y) * L + z
                    nb[i, k + 1] = (x * L + (y + d) % L) * L + z
                    nb[i, k + 2] = (x * L + y) * L + (z + d) % L
                    k += 3
    return N, nb, eps


def sample_gas(L, p, q, r, g, sweeps_eq, sweeps_meas, seed):
    rng = random.Random(seed)
    N, nb, eps = lattice(L)
    c0 = 6.0 / (p + q + 4 * r)
    W = [[g * c0 * omega(a, b, p, q, r) for b in CONTENTS] for a in CONTENTS]
    n_rec = N // 2
    occ = [0] * N
    cont = [-1] * N
    for i in rng.sample(range(N), n_rec):
        occ[i] = 1
        cont[i] = rng.randrange(6)
    records = [i for i in range(N) if occ[i]]
    nbl = nb.tolist()
    epsl = eps.tolist()

    def local_weight(site, content, exclude):
        w = 1.0
        for k in nbl[site]:
            if k != exclude and occ[k]:
                w *= W[content][cont[k]]
        return w

    stag2 = []
    bonds_l = []
    for sweep in range(sweeps_eq + sweeps_meas):
        for _ in range(N):
            # transit: a record hops to an empty neighbour with the ratio acceptance
            slot = rng.randrange(n_rec)
            i = records[slot]
            j = nbl[i][rng.randrange(6)]
            if not occ[j]:
                w_old = local_weight(i, cont[i], j)
                w_new = local_weight(j, cont[i], i)
                if w_new >= w_old or rng.random() < w_new / w_old:
                    occ[i], occ[j] = 0, 1
                    cont[j], cont[i] = cont[i], -1
                    records[slot] = j
            # content re-draw (heat bath given the recorded neighbours)
            i = records[rng.randrange(n_rec)]
            weights = [local_weight(i, a, -1) for a in range(6)]
            u = rng.random() * sum(weights)
            acc = 0.0
            for a in range(6):
                acc += weights[a]
                if u <= acc:
                    cont[i] = a
                    break
        if sweep >= sweeps_eq and (sweep - sweeps_eq) % 5 == 0:
            s = sum(epsl[i] for i in records)
            stag2.append(s * s / N)
            b = 0
            for i in records:
                for k in nbl[i]:
                    if occ[k] and k > i:
                        b += 1
            bonds_l.append(b)
    random_stag2 = N / (4.0 * (N - 1))
    random_bonds = 3 * N * 0.5 * (n_rec - 1) / (N - 1)
    return float(np.mean(stag2)), random_stag2, float(np.mean(bonds_l)), random_bonds, occ


def walk_spectrum(L, occ, c):
    N, nb, eps = lattice(L)
    dim = 2 * N
    H = np.zeros((dim, dim), dtype=complex)
    sig = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]
    for i in range(N):
        for a in range(3):
            plus, minus = nb[i, a], nb[i, a + 3]                                  # neighbour order: +x, +y, +z, -x, -y, -z
            # (S_a psi)(x) = (psi(x + e_a) - psi(x - e_a)) / (2i)
            H[2 * i:2 * i + 2, 2 * plus:2 * plus + 2] += sig[a] / (2j)
            H[2 * i:2 * i + 2, 2 * minus:2 * minus + 2] -= sig[a] / (2j)
        if occ[i]:
            H[2 * i, 2 * i] += c
            H[2 * i + 1, 2 * i + 1] += c
    assert np.allclose(H, H.conj().T)
    ev = np.linalg.eigvalsh(H)
    inside = int(np.sum((ev > 1e-9) & (ev < c - 1e-9)))
    return ev, inside


def main():
    print("W1: half-filled record gas on periodic lattices; staggered structure factor and recorded neighbours per record (random placement in brackets)")
    saved = {}
    for L, trips, scales, eq, meas in ((6, ((3, 1, 2), (12, 1, 2)), (1.0, 2.0, 4.0, 0.5, 0.25, 0.125), 600, 2400), (8, ((3, 1, 2),), (1.0, 4.0, 0.25), 400, 1600)):
        for (p, q, r) in trips:
            for g in scales:
                s2, s2r, b, br, occ = sample_gas(L, p, q, r, g, eq, meas, seed=L * 1000 + int(g * 1000) + p)
                if L == 6 and (p, q, r) == (3, 1, 2) and g == 1.0:
                    saved["sampled"] = occ
                n_rec = L ** 3 // 2
                print(f"  L={L} ({p},{q},{r}) g={g:g}: <stag^2>/N = {s2:.3f} [{s2r:.3f}]; neighbours per record {2 * b / n_rec:.3f} [{2 * br / n_rec:.3f}]", flush=True)
    print("W2: the walk on the 6^3 torus with the coin-scalar record potential c n_x, c = 3/5; eigenvalues strictly inside (0, c)")
    L = 6
    N = L ** 3
    chess = [1 if ((i // (L * L)) + ((i // L) % L) + (i % L)) % 2 == 0 else 0 for i in range(N)]
    full = [1] * N
    for name, occ in (("chessboard", chess), ("sampled equilibrium arrangement at g = 1", saved["sampled"]), ("records on every site", full)):
        ev, inside = walk_spectrum(L, occ, 0.6)
        print(f"  {name}: eigenvalues in (0, c): {inside} of {2 * N}; nearest to c/2 = 0.3: {min(abs(ev - 0.3)):.4f}; lowest {ev[0]:.4f}, highest {ev[-1]:.4f}")


if __name__ == "__main__":
    sys.exit(main())
