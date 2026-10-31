#!/usr/bin/env python3
"""The separated form of the rectangle: T on a near cluster against a far plaquette energy.

Cluster: Gamma_1 = l(y_k), Gamma_2 = sigma_k l(y_(k+1)) sigma_k^-1, Gamma_3 = tau_k Lam tau_k^-1, with Lam
a plaquette in the (3,4) plane inside the square, q a far plaquette in the (3,4) plane at (R, 0, c, c).
The supports of the cluster and of s_q are at distance about R, so this is a correlator of
two separated local gauge-invariant observables.

Formula from checks/witness_separated.py, with -12 V_q kept on both sides:
  <T s_q>_c = L_q / beta^3 on the Wilson weight,  L_q^G on the Gaussian potential in Feynman gauge.
Claim (parts/witness.md, Text 3.9): sum_k L_q^G(k) / P_k = -24 P(Lam, q) Flux[E_q] + O(V_q terms),
and sum_k L_q(k) / P_k is smaller by a power of R.

PRE-REGISTERED CRITERIA (written before the first run).
 W1 IDENTITY: sum_k L_q^G / P_k agrees with -24 P(Lam, q) Flux[E_q] to relative 1e-3 at R >= 6.
 W2 SEPARATION: |sum_k L_q / P_k| / |sum_k L_q^G / P_k| decreases with R and is below 0.5 at the
    largest R. FAIL means the separated form does not separate at this range.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_separated import B_terms, V_at  # noqa: E402
from witness_stokes import lasso_steps, steps_between  # noqa: E402
from witness_tree_coeff import Lat, check_rss, curl, current, field_E, path_links, plaq  # noqa: E402


def run(lat, D, R):
    c = (D - 1) // 2
    lam = (0, 0, c, c)
    q = (R, 0, c, c)
    corners = [(0, 0, 0, 0), (0, 0, D, 0), (0, 0, D, D), (0, 0, 0, D)]
    Eq = field_E(lat, current(lat, path_links(lat, q, plaq(3, 4))))
    Elam = field_E(lat, current(lat, path_links(lat, lam, plaq(3, 4))))
    Es = {y: field_E(lat, current(lat, path_links(lat, y, plaq(1, 2)))) for y in corners}
    Jq = current(lat, path_links(lat, q, plaq(3, 4)))
    P_lq = float(np.sum(Jq * Elam))
    s_full, s_gauss = 0.0, 0.0
    for k, y in enumerate(corners):
        z = corners[(k + 1) % 4]
        L1 = path_links(lat, y, plaq(1, 2))
        L2 = path_links(lat, y, lasso_steps(steps_between(y, z), plaq(1, 2)))
        L3 = path_links(lat, y, lasso_steps(steps_between(y, lam), plaq(3, 4)))
        E1, E2, E3 = Es[y], Es[z], Elam
        Pk = float(np.sum(current(lat, L2) * E1))
        Pi = [float(np.sum(Jq * E)) for E in (E1, E2, E3)]
        bs = B_terms(lat, (L1, L2, L3), (E1, E2, E3), Eq)
        Vq = V_at(lat, (E1, E2, E3), q, 2, 3)
        Lf = 12.0 * (sum(Pi[i] * (bs[i][0] + bs[i][1]) for i in range(3)) - Vq)
        LG = 12.0 * (sum(Pi[i] * bs[i][1] for i in range(3)) - Vq)
        s_full += Lf / Pk
        s_gauss += LG / Pk
    P3 = curl(lat, Eq, 2, 3)
    flux = float(np.sum(P3[0, 0, 0:D, 0:D]))
    return s_full, s_gauss, -24 * P_lq * flux, P_lq


def main():
    T = 32
    lat = Lat(4, T)
    for D in (3,):
        for R in (6, 8, 10, 12):
            sf, sg, pred, plq = run(lat, D, R)
            print(f"D={D} R={R}: sum L_q/P={sf:.5e} sum L_q^G/P={sg:.5e} -24 P Flux={pred:.5e} W1rel={abs(sg-pred)/abs(pred):.1e} ratio={abs(sf/sg):.4f} P(Lam,q)={plq:.3e} rss={check_rss():.2f}GB", flush=True)


if __name__ == "__main__":
    main()
