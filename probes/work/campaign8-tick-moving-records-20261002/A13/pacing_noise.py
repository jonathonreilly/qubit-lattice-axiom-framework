#!/usr/bin/env python3
"""A13 check 4: event-paced change makes the phase of a superposition noisy (supplied toy + arithmetic).

Two places, each with its own local events (Bernoulli p per schedule tick, independent); the change, and so
the phase of an unrecorded content, advances by omega per local event.  A superposition of the content at the
two places has visibility |E exp(i omega (n1 - n2))| = |1 - p + p e^{i omega}|^{2t}   (EXACT),
-> exp(-2 lambda (1 - cos omega)) for Poisson counts with mean lambda each.
Identification (ARGUED, A5 T2.6: internal energy must enter as mass-like mixing): omega = M c^2 tau_e / hbar
per event, lambda = t / tau_e, so V ~ exp(-t tau_e (M c^2/hbar)^2), t_coh = hbar^2 / (tau_e M^2 c^4).
"""
import numpy as np

hbar, c, tP = 1.054571817e-34, 2.99792458e8, 5.391247e-44
amu, me, mn = 1.66053907e-27, 9.1093837e-31, 1.67492750e-27


def main():
    rng = np.random.default_rng(5)
    for p, om, t in [(0.3, 0.2, 200), (0.05, 0.5, 400), (0.8, 0.05, 1000)]:
        exact = abs(1 - p + p * np.exp(1j * om)) ** (2 * t)
        M = 200000
        n1 = rng.binomial(t, p, M)
        n2 = rng.binomial(t, p, M)
        mc = abs(np.mean(np.exp(1j * om * (n1 - n2))))
        print(f"p={p}, omega={om}, t={t}: exact V={exact:.5f}, Monte Carlo V={mc:.5f} (s.e. ~{1/np.sqrt(M):.4f}); "
              f"small-omega form exp(-t p(1-p) omega^2) = {np.exp(-t*p*(1-p)*om**2):.5f}")
    print("physical scale (tau_e = Planck time unless stated):")
    for name, M in [("electron", me), ("neutron", mn), ("100 amu atom", 100 * amu), ("Cs-133", 132.905 * amu),
                    ("25,000 amu molecule", 25000 * amu)]:
        w = M * c ** 2 / hbar
        tcoh = hbar ** 2 / (tP * (M * c ** 2) ** 2)
        need = 1.0 / w ** 2          # tau_e allowing 1 s of coherence
        print(f"  {name:20s}: Mc^2/hbar = {w:.3e} /s; t_coh = {tcoh:.2e} s; tau_e for 1 s coherence <= {need:.2e} s "
              f"= {need/tP:.1e} t_P")


if __name__ == '__main__':
    main()
