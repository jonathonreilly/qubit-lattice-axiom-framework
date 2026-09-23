#!/usr/bin/env python3
"""Supervisor control for block 96 (floating point; evidence, not proof).

W1: the full generator of clocked record motion (block 95's slaved clock field, log kappa = -1) on larger systems: three records on a
    ring of ten, and two records on the 4^3 torus, for hops timed by the site left (a = 1), the bond (a = 1/2) and the site entered (a = 0):
    largest imaginary part of any eigenvalue (the note's T1: zero), against the same chains with a circulation added (x-hops in the +x
    direction at twice the rate of -x hops).
W2: a record with direction memory in three dimensions (continue with probability p, else turn to one of the other five directions):
    over a 24^3 grid of wave vectors, the largest imaginary part of the leading (density) multiplier at long waves |k| < 0.8 (T2: zero)
    and over the whole zone (short waves can oscillate), the smallest |k| with a non-real leading multiplier against the line's
    threshold arcsin((1 - p)/p) (the persistence scale), the fraction of wave vectors with a non-real multiplier, and the largest modulus
    of a non-real multiplier as |k| -> 0 (the oscillating direction modes decay at a rate bounded away from zero).
"""
import itertools
import math

import numpy as np


def zero_mean_kernel(L, dim):
    k = 2 * np.pi * np.fft.fftfreq(L)
    grids = np.meshgrid(*([k] * dim), indexing="ij")
    E = 2 * dim - 2 * sum(np.cos(g) for g in grids)
    E[(0,) * dim] = 1.0
    inv = 1.0 / E
    inv[(0,) * dim] = 0.0
    return np.real(np.fft.ifftn(inv))


def clocked_generator(L, dim, n, a, lam, circulate):
    G = zero_mean_kernel(L, dim)
    sites = list(itertools.product(range(L), repeat=dim))
    states = [frozenset(c) for c in itertools.combinations(range(len(sites)), n)]
    index = {s: i for i, s in enumerate(states)}
    coord = np.array(sites)

    def field(z, C):
        return 2 * dim * lam * sum(G[tuple((coord[z] - coord[r]) % L)] for r in C)
    Q = np.zeros((len(states), len(states)))
    steps = [tuple(s if i == j else 0 for i in range(dim)) for j in range(dim) for s in (1, -1)]
    lookup = {tuple(c): i for i, c in enumerate(sites)}
    for s in states:
        for x in s:
            for st in steps:
                y = lookup[tuple((coord[x] + np.array(st)) % L)]
                if y in s:
                    continue
                s2 = (s - {x}) | {y}
                r = math.exp(a * field(x, s) + (1 - a) * field(y, s))
                if circulate and st[0] == 1:
                    r *= 2
                Q[index[s2], index[s]] += r
                Q[index[s], index[s]] -= r
    return Q


def main():
    print("W1: largest |Im| of the generator's eigenvalues, clocked record motion (log kappa = -1)")
    for (L, dim, n) in ((10, 1, 3), (4, 3, 2)):
        for a in (1.0, 0.5, 0.0):
            row = []
            for circ in (False, True):
                Q = clocked_generator(L, dim, n, a, -1.0, circ)
                ev = np.linalg.eigvals(Q)
                row.append(np.max(np.abs(ev.imag)))
            print("  %d record(s) on %s, a = %.1f: in detailed balance %.1e; with a circulation %.3f (states: %d)"
                  % (n, "a ring of %d" % L if dim == 1 else "%d^3" % L, a, row[0], row[1], Q.shape[0]))
    print("W2: a record with direction memory in three dimensions, 24^3 grid of wave vectors")
    dirs = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
    ks = 2 * np.pi * np.arange(24) / 24
    for p in (0.5, 0.9, 0.99):
        T = np.full((6, 6), (1 - p) / 5)
        np.fill_diagonal(T, p)
        lead_im_long = 0.0
        lead_im_all = 0.0
        first_complex = float("inf")
        nonreal = 0
        small = []
        for kx in ks:
            for ky in ks:
                for kz in ks:
                    kv = np.array((kx, ky, kz))
                    ev = np.linalg.eigvals(np.diag(np.exp(-1j * dirs @ kv)) @ T)
                    order = np.argsort(-np.abs(ev))
                    kk = np.linalg.norm(((kv + np.pi) % (2 * np.pi)) - np.pi)
                    lead_im_all = max(lead_im_all, abs(ev[order[0]].imag))
                    if abs(ev[order[0]].imag) > 1e-9:
                        first_complex = min(first_complex, kk)
                    if kk < 0.8:
                        lead_im_long = max(lead_im_long, abs(ev[order[0]].imag))
                    if np.max(np.abs(ev.imag)) > 1e-9:
                        nonreal += 1
                    if 0 < kk < 0.3:
                        cplx = ev[np.abs(ev.imag) > 1e-9]
                        if len(cplx):
                            small.append(np.max(np.abs(cplx)))
        print("  p = %.2f: leading multiplier's largest |Im| at |k| < 0.8: %.1e (over the whole zone: %.2f); smallest |k| with a non-real leading multiplier %.3f (line: arcsin((1 - p)/p) = %.3f); wave vectors with some non-real multiplier %.3f; non-real multipliers at |k| < 0.3 have modulus at most %.4f (k = 0 value (6p - 1)/5 = %.4f)"
              % (p, lead_im_long, lead_im_all, first_complex, math.asin(min(1.0, (1 - p) / p)), nonreal / 24 ** 3, max(small) if small else float("nan"), (6 * p - 1) / 5))

if __name__ == "__main__":
    main()
