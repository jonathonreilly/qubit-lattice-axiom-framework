"""Many-record helpers: qubit ring, number-conserving gates, configuration sectors."""
import itertools
import numpy as np


def popcount(s):
    return bin(s).count('1')


def sector(N, n):
    return [s for s in range(1 << N) if popcount(s) == n]


def gate_full(N, sites, g):
    """Full 2^N operator of a gate g acting on the listed sites (basis order: bits of sites
    read as a binary number with sites[0] the most significant)."""
    k = len(sites)
    dim = 1 << N
    U = np.zeros((dim, dim), complex)
    for s in range(dim):
        loc = 0
        for i, site in enumerate(sites):
            loc |= ((s >> site) & 1) << (k - 1 - i)
        base = s
        for site in sites:
            base &= ~(1 << site)
        for new in range(1 << k):
            amp = g[new, loc]
            if amp == 0:
                continue
            t = base
            for i, site in enumerate(sites):
                if (new >> (k - 1 - i)) & 1:
                    t |= 1 << site
            U[t, s] += amp
    return U


def nc_two_site(V, phase11):
    """Number-conserving 2-qubit gate: |00>->|00>, {|01>,|10>} -> V, |11> -> e^{i phase}|11>.
    Basis order 00,01,10,11 where the first bit is the first site."""
    g = np.zeros((4, 4), complex)
    g[0, 0] = 1.0
    g[np.ix_([2, 1], [2, 1])] = V          # V acts on (|10>, |01>) = (record on first, on second)
    g[3, 3] = np.exp(1j * phase11)
    return g


def configs_of(states, N):
    return [tuple(i for i in range(N) if (s >> i) & 1) for s in states]


def one_step_reachable(C, Cp, N):
    """Perfect matching with cyclic displacement <= 1 between record sets C and C'."""
    if len(C) != len(Cp):
        return False
    for perm in itertools.permutations(Cp):
        if all(min((a - b) % N, (b - a) % N) <= 1 for a, b in zip(C, perm)):
            return True
    return False
