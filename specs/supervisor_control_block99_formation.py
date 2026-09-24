#!/usr/bin/env python3
"""Supervisor control for block 99 (floating point and sampling; evidence, not proof).

W1: 96 records formed one at a time on an empty 16^3 torus, each at an empty site chosen in proportion to that site's clock, the clock field
    slaved to the records already present (block 53: log w = 6 log(kappa) sum_r G(z - r), log(kappa) = -g): nearest-neighbour contacts
    among the formed records against g (60 formed sets per g), against uniform placement; and the contact count the pair weight exp(U(1))
    predicts at low density. Block 95's control W3 gives the other half: the same 96 records moving on their clocks at g = 1 put 95 per
    cent of themselves in one cluster.
"""
import math

import numpy as np


def zero_mean_kernel(L):
    k = 2 * np.pi * np.fft.fftfreq(L)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    E = 6 - 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz))
    E[0, 0, 0] = 1.0
    inv = 1.0 / E
    inv[0, 0, 0] = 0.0
    return np.real(np.fft.ifftn(inv))


def main():
    L, N, runs = 16, 96, 60
    V = L ** 3
    G = zero_mean_kernel(L)
    rng = np.random.default_rng(99)
    uniform = N * (N - 1) / 2 * 6 / (V - 1)
    print("W1: %d records formed one at a time on %d^3, each at an empty site in proportion to its clock; %d formed sets per coupling" % (N, L, runs))
    print("  uniform placement: expected contacts %.2f" % uniform)
    for g in (0.0, 0.5, 1.0, 2.0):
        contacts = []
        for _ in range(runs):
            occ = np.zeros((L, L, L), bool)
            logw = np.zeros((L, L, L))
            pos = []
            for _n in range(N):
                w = np.exp(logw)
                w[occ] = 0.0
                s = rng.choice(V, p=w.ravel() / w.sum())
                x = np.unravel_index(s, (L, L, L))
                occ[x] = True
                pos.append(x)
                logw += -6 * g * np.roll(np.roll(np.roll(G, x[0], 0), x[1], 1), x[2], 2)
            c = 0
            for p in pos:
                for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                    if occ[tuple((np.array(p) + np.array(d)) % L)]:
                        c += 1
            contacts.append(c)
        pred = uniform * math.exp(-6 * g * (G[1, 0, 0]))
        print("  g = %.1f: contacts %.2f +- %.2f; low-density prediction uniform x exp(U(1)) = %.2f" % (g, np.mean(contacts), np.std(contacts) / math.sqrt(runs), pred))


if __name__ == "__main__":
    main()
