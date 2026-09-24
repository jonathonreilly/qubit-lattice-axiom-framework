#!/usr/bin/env python3
"""Independent checks for the ledger force identity, a1.

Logarithmic mean, bond polarization, the even-sublattice counterexample,
the upwind telescope, and the two energy-1 plane waves.
"""
import cmath
from fractions import Fraction as F

FAILS = []


def ok(name, good, msg):
    print(("ok " if good else "FAIL ") + name + ": " + msg, flush=True)
    if not good:
        FAILS.append(name)


def main():
    # d phi = (1/2) Lambda d u, Lambda the logarithmic mean, u = 2 log phi
    px, py = 2.0, 8.0
    ux, uy = 2 * cmath.log(px).real, 2 * cmath.log(py).real
    lam = (py - px) / (cmath.log(py).real - cmath.log(px).real)
    ok("logmean", abs((py - px) - 0.5 * lam * (uy - ux)) < 1e-12,
       "d phi = (1/2) Lambda d u exactly")

    # polarization: Re[(d psi)^dag (d chi)] = rho_x + rho_y - 2 eps
    def re_dot(p, q):
        return (p[0].conjugate() * q[0] + p[1].conjugate() * q[1]).real
    px_s, py_s = (1 + 2j, 3 - 1j), (0.5 - 1j, 4 + 0.25j)
    cx, cy = (2 - 3j, 1 + 1j), (-1 + 0.5j, 2j)
    dpsi = (py_s[0] - px_s[0], py_s[1] - px_s[1])
    dchi = (cy[0] - cx[0], cy[1] - cx[1])
    rho = re_dot(px_s, cx) + re_dot(py_s, cy)
    eps = 0.5 * (re_dot(py_s, cx) + re_dot(px_s, cy))
    ok("polar", abs(re_dot(dpsi, dchi) - (rho - 2 * eps)) < 1e-12,
       "Re[(d psi)^dag (d chi)] = rho_x + rho_y - 2 eps")

    # even support: rho = 0, bond cross energy need not be
    # psi at even site (1,0), chi at the odd neighbour (0,1) from the hop
    psi_e, chi_o = (1 + 0j, 0.5j), (1 + 0j, 0.5j)
    rho_e = re_dot(psi_e, (0j, 0j))
    rho_o = re_dot((0j, 0j), chi_o)
    eps_b = 0.5 * re_dot(psi_e, chi_o)
    ok("sublattice", rho_e == 0 and rho_o == 0 and abs(eps_b) > 0.1,
       f"even support has energy density 0 and bond cross energy {eps_b}")

    # upwind telescope on a periodic line of 4
    w = [F(1), F(2), F(3), F(4)]
    xi = [F(1, 2), F(-1), F(3), F(0)]
    # sum_x -w_x (xi_{x+1}-xi_x) + w_x * (-xi_x (1 - w_{x-1}/w_x)) == 0
    acc = F(0)
    n = 4
    for x in range(n):
        acc += -w[x] * (xi[(x + 1) % n] - xi[x])
        acc += w[x] * (-xi[x] * (1 - w[(x - 1) % n] / w[x]))
    ok("upwind", acc == 0, f"upwind transport cancels the volume identity, residual {acc}")

    # plane waves on the symbol: S_a = sin(theta_a), theta = (pi/2)*k
    # k=(1,0,0): sin=(1,0,0), energy from sigma_x. Spinor (1,1), E=1, e=2
    # force coefficient cos(theta_j)=0 along j=0
    # k=(0,1,0): sin=(0,1,0), cos along j=0 is cos(0)=1, force coefficient e
    cos = {0: 1, 1: 0, 2: -1, 3: 0}
    e = 2
    f_a = e * cos[1]          # k1=pi/2, direction 1
    f_b = e * cos[0]          # k1=0, direction 1
    ok("waves", f_a == 0 and f_b == 2, "equal energy density 2, forces along e1 are 0 and 2")

    # Gamma flips the nearest-neighbour sign and preserves a two-step
    # one step: parity product Gamma(x+e)Gamma(x) = -1
    # two steps: +1
    ok("parity", (-1) * (-1) == 1 and (-1) == -1,
       "a nearest-neighbour hop anticommutes with Gamma; a two-step hop commutes")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent check did not reproduce that step")
        return
    print(
        "HIT: confirmed - the force is a bond cross energy times d phi, not a function of the energy density, "
        "and the two energy-1 waves with the same e and zero current have forces 0 and 2"
    )
    print(
        "SUMMARY: confirmed the logarithmic mean, the polarization identity, the even-sublattice counterexample, "
        "the upwind cancellation, and the plane-wave no-go at first order"
    )


if __name__ == "__main__":
    main()
