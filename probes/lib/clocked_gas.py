#!/usr/bin/env python3
"""Clocked record gas (block 95, PR #8860): records on an L^3 torus, one per site, clock field slaved to them by block 53's law,
log w_z = 6 log(kappa) sum_r G(z - r) with log(kappa) = -g (G the zero-mean lattice kernel); a record hops to an empty neighbour at rate
w_x/6 (timed by the site it leaves, block 97). Stationary law exactly block 95's pair law exp(6 g sum_pairs G). Direct-method simulation;
averages weighted by expected holding times.

usage: clocked_gas.py L N g events seed
prints: the time-weighted fraction of records touching another, the largest cluster's share, S(k_min), and SUMMARY."""
import math
import sys

import numpy as np
from numba import njit


def zero_mean_kernel(L):
    k = 2 * np.pi * np.fft.fftfreq(L)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    E = 6 - 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz))
    E[0, 0, 0] = 1.0
    inv = 1.0 / E
    inv[0, 0, 0] = 0.0
    return np.real(np.fft.ifftn(inv))


@njit(cache=True)
def many_records(G, L, lam, n, steps, seed, every):
    np.random.seed(seed)
    V = L * L * L
    occ = -np.ones(V, dtype=np.int64)
    pos = np.zeros((n, 3), dtype=np.int64)
    i = 0
    while i < n:
        s = np.random.randint(V)
        if occ[s] < 0:
            occ[s] = i
            pos[i, 0] = s // (L * L)
            pos[i, 1] = (s // L) % L
            pos[i, 2] = s % L
            i += 1
    dirs = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    logw = np.zeros(n)
    for i in range(n):
        acc = 0.0
        for j in range(n):
            acc += G[(pos[i, 0] - pos[j, 0]) % L, (pos[i, 1] - pos[j, 1]) % L, (pos[i, 2] - pos[j, 2]) % L]
        logw[i] = 6 * lam * acc
    empt = np.zeros(n, dtype=np.int64)
    R = np.zeros(n)
    burn = steps // 5
    sw = 0.0
    s_contact = 0.0
    s_sk = 0.0
    s_big = 0.0
    kmin = 2 * math.pi / L
    parent = np.zeros(n, dtype=np.int64)
    for t in range(steps):
        tot = 0.0
        for i in range(n):
            c = 0
            for e in range(6):
                s = ((pos[i, 0] + dirs[e, 0]) % L) * L * L + ((pos[i, 1] + dirs[e, 1]) % L) * L + (pos[i, 2] + dirs[e, 2]) % L
                if occ[s] < 0:
                    c += 1
            empt[i] = c
            R[i] = math.exp(logw[i]) * c / 6
            tot += R[i]
        if t >= burn and t % every == 0:
            h = 1.0 / tot
            sw += h
            con = 0
            for i in range(n):
                if empt[i] < 6:
                    con += 1
            s_contact += h * con / n
            sk = 0.0
            for ax in range(3):
                re = 0.0
                im = 0.0
                for i in range(n):
                    re += math.cos(kmin * pos[i, ax])
                    im += math.sin(kmin * pos[i, ax])
                sk += (re * re + im * im) / n
            s_sk += h * sk / 3
            # largest cluster (nearest-neighbour contact), union-find
            for i in range(n):
                parent[i] = i
            for i in range(n):
                for e in range(0, 6, 2):
                    s = ((pos[i, 0] + dirs[e, 0]) % L) * L * L + ((pos[i, 1] + dirs[e, 1]) % L) * L + (pos[i, 2] + dirs[e, 2]) % L
                    j = occ[s]
                    if j >= 0:
                        ri = i
                        while parent[ri] != ri:
                            ri = parent[ri]
                        rj = j
                        while parent[rj] != rj:
                            rj = parent[rj]
                        if ri != rj:
                            parent[ri] = rj
            big = 0
            for i in range(n):
                ri = i
                while parent[ri] != ri:
                    ri = parent[ri]
                parent[i] = ri
            for i in range(n):
                c = 0
                for j in range(n):
                    if parent[j] == i:
                        c += 1
                if c > big:
                    big = c
            s_big += h * big / n
        u = np.random.random() * tot
        acc = 0.0
        k = n - 1
        for i in range(n):
            acc += R[i]
            if acc >= u:
                k = i
                break
        while R[k] == 0.0:
            k -= 1
        # a uniformly chosen empty neighbour
        m = np.random.randint(empt[k])
        for e in range(6):
            s = ((pos[k, 0] + dirs[e, 0]) % L) * L * L + ((pos[k, 1] + dirs[e, 1]) % L) * L + (pos[k, 2] + dirs[e, 2]) % L
            if occ[s] < 0:
                if m == 0:
                    old = pos[k, 0] * L * L + pos[k, 1] * L + pos[k, 2]
                    x0, x1, x2 = pos[k, 0], pos[k, 1], pos[k, 2]
                    occ[old] = -1
                    occ[s] = k
                    pos[k, 0] = (pos[k, 0] + dirs[e, 0]) % L
                    pos[k, 1] = (pos[k, 1] + dirs[e, 1]) % L
                    pos[k, 2] = (pos[k, 2] + dirs[e, 2]) % L
                    for j in range(n):
                        if j == k:
                            continue
                        logw[j] += 6 * lam * (G[(pos[j, 0] - pos[k, 0]) % L, (pos[j, 1] - pos[k, 1]) % L, (pos[j, 2] - pos[k, 2]) % L]
                                              - G[(pos[j, 0] - x0) % L, (pos[j, 1] - x1) % L, (pos[j, 2] - x2) % L])
                    acc2 = 0.0
                    for j in range(n):
                        acc2 += G[(pos[k, 0] - pos[j, 0]) % L, (pos[k, 1] - pos[j, 1]) % L, (pos[k, 2] - pos[j, 2]) % L]
                    logw[k] = 6 * lam * acc2
                    break
                m -= 1
    return s_contact / sw, s_sk / sw, s_big / sw




if __name__ == "__main__":
    L, N, g, events, seed = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    G = zero_mean_kernel(L)
    touch, sk, big = many_records(G, L, -g, N, events, seed, 50)
    rho = N / L ** 3
    emin = 2 - 2 * math.cos(2 * math.pi / L)
    print("L %d N %d rho %.5f g %.3f events %d seed %d" % (L, N, rho, g, events, seed))
    print("touching %.4f largest_cluster_share %.4f S_kmin %.3f mean_field_limit_g %.4f" % (touch, big, sk, emin / (6 * rho * (1 - rho))))
    print("SUMMARY: L=%d N=%d g=%.3f largest_cluster_share=%.4f touching=%.4f S_kmin=%.3f" % (L, N, g, big, touch, sk))
