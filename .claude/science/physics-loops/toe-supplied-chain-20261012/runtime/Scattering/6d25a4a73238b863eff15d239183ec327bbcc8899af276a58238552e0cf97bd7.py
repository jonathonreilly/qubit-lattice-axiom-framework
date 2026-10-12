"""Finite representatives of formulas in the frozen proof; not a proof engine."""
from itertools import permutations
from math import factorial, sqrt
import numpy as np


def energy(k, g, J):
    return 2 * np.sqrt(g*g + J*J - 2*g*J*np.cos(k))


def velocity(k, g, J):
    return 4*g*J*np.sin(k) / energy(k, g, J)


def spin_product(coefficients):
    """Product of spin lowering sums, right factor acting first."""
    state = {0: 1.0 + 0j}
    for packet in reversed(coefficients):
        new = {}
        for bits, amplitude in state.items():
            for site, coefficient in enumerate(packet):
                if coefficient == 0:
                    continue
                if bits & (1 << site):
                    continue
                key = bits | (1 << site)
                new[key] = new.get(key, 0j) + coefficient*amplitude
        state = new
    return state


def car_product(coefficients):
    """Literal finite CAR creators with occupied-left parity."""
    state = {0: 1.0 + 0j}
    for packet in reversed(coefficients):
        new = {}
        for bits, amplitude in state.items():
            for site, coefficient in enumerate(packet):
                if coefficient == 0 or bits & (1 << site):
                    continue
                occupied = (bits & ((1 << site) - 1)).bit_count()
                phase = (-1)**occupied
                key = bits | (1 << site)
                new[key] = new.get(key, 0j) + phase*coefficient*amplitude
        state = new
    return state


def cone_sign(n, t):
    return 1 if t > 0 else (-1)**(n*(n-1)//2)


def wavefunction(packet_values, antisymmetric):
    """S4 evaluated at one momentum tuple; rows label packets."""
    n = len(packet_values)
    total = 0j
    for perm in permutations(range(n)):
        parity = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        phase = (-1)**parity if antisymmetric else 1
        total += phase*np.prod([packet_values[i, perm[i]] for i in range(n)])
    return total / sqrt(factorial(n))


def out_coordinate(symmetric_value, momenta, g, J):
    speeds = velocity(np.asarray(momenta), g, J)
    epsilon = np.prod([np.sign(speeds[j]-speeds[i])
                       for i in range(len(speeds)) for j in range(i+1, len(speeds))])
    return epsilon*symmetric_value


def packet_coefficients(packet_samples, k, g, J, t, sites):
    """Trapezoid Fourier coefficients on k_j=-pi+2pi*j/N."""
    samples = packet_samples*np.exp(1j*t*energy(k, g, J))
    transformed = np.fft.ifft(samples)
    sites = np.asarray(sites, dtype=int)
    return transformed[sites % len(k)] * np.where(sites % 2, -1, 1)


def pair_error(u, w, sign):
    """Spin permanent versus signed CAR determinant on increasing pairs."""
    first = np.outer(u, w)
    second = np.outer(w, u)
    difference = first + second - sign*(first-second)
    return float(np.linalg.norm(np.triu(difference, 1)))


def filter_vacuum(k, g, J, transform):
    return transform(energy(k, g, J), k)
