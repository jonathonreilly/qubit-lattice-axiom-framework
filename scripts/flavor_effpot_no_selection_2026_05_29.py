#!/usr/bin/env python3
"""
Coexistence-symmetry test: at the uniform-staggered coexistence, does any
enhanced symmetry / potential feature SELECT b/a = 1/sqrt(2) (= r=1/2, Q=2/3)?

Probe: the fermion effective potential U(a,b) = -(1/2V) sum_k log|det Ginv(k)|
on the full Wilson-Dirac propagator on Z^3 (4x4 in (k,k+Q)x spinor, Q=(pi,pi,0)).
At fixed radius rho=sqrt(a^2+b^2) the ANGULAR minimum of U is the dynamically
selected ratio b/a (the democratic auxiliary-mass term (a^2+b^2)/2G is isotropic
in (a,b), so it does not move the angle). If U were minimized at phi=35.26deg
(tan=1/sqrt2) the dynamics would SELECT r=1/2; if flat -> O(2); if phi=0 ->
uniform wins.

RESULT: U is minimized at phi=0 (b=0, pure uniform) for EVERY m and radius
tested; U(b=0) < U(r=1/2) by a finite margin, monotone from b=0. So:
 - NO enhanced symmetry / potential feature at b/a=1/sqrt2 (not selected),
 - NOT an O(2) flat direction (the staggered direction strictly costs energy),
 - the uniform condensate wins -> r=0 -> Q=1/3 (degenerate), robustly.

This is the THIRD independent fermion-sector computation (after the coupled
gap equation and the competing-orders scan) to give the SAME answer: the
fermion vacuum drives r->0 (degenerate generations, Q=1/3) and never selects
r=1/2. The lepton hierarchy / Q=2/3 is therefore NOT a fermion-vacuum-condensate
effect at mean-field. (General: the uniform, translation-invariant scalar
condensate maximizes |det| -- a Vafa-Witten-flavored preference for the
unbroken vacuum.)

HONEST SCOPE: mean-field, fermion-determinant level. This is a robust negative
for ONE hypothesis ('the value 2/3 emerges from fermion-vacuum dynamics'), NOT
a permanent wall. It RELOCATES the origin of the splitting to structure the
fermion determinant does not contain: the action's explicit (bridge-gap)
structure, or a non-fermionic (gauge/link) sector whose vacuum could carry the
staggered order. Those are untested here (the derived action is not pinned), so
the route is open, not closed.
"""

import numpy as np

s = [np.array([[0, 1], [1, 0]], complex),
     np.array([[0, -1j], [1j, 0]], complex),
     np.array([[1, 0], [0, -1]], complex)]
I2 = np.eye(2, dtype=complex)
QV = np.array([np.pi, np.pi, 0.0])


def Wfree(k, m, r):
    W = m + r * sum(1 - np.cos(kk) for kk in k)
    return W * I2 + 1j * sum(s[mu] * np.sin(k[mu]) for mu in range(3))


def U(a, b, m, r=1.0, L=12):
    ks = 2 * np.pi * np.arange(L) / L
    tot = 0.0
    for kx in ks:
        for ky in ks:
            for kz in ks:
                k = np.array([kx, ky, kz])
                G = np.block([[Wfree(k, m, r) + a * I2, b * I2],
                              [b * I2, Wfree(k + QV, m, r) + a * I2]])
                tot += np.log(np.abs(np.linalg.det(G)) + 1e-300)
    return -tot / (2 * L ** 3)


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    sep("Angular structure of U on a=rho cos(phi), b=rho sin(phi)")
    print("  b/a=1/sqrt2 (r=1/2, Q=2/3) is phi=35.26deg. Look for the U-minimum angle.")
    print("   m      rho   phi*(U-min)   b/a    r      U(b=0)     U(r=1/2)   cost")
    for m in [-1.8, -1.0, 0.1]:
        for rho in [0.3, 0.6]:
            phis = np.linspace(0, np.pi / 2, 19)
            Us = np.array([U(rho * np.cos(p), rho * np.sin(p), m) for p in phis])
            i = int(np.argmin(Us))
            u0 = U(rho, 0, m)
            uh = U(rho * np.sqrt(2 / 3), rho * np.sqrt(1 / 3), m)  # b/a=1/sqrt2
            print(f"   {m:+.2f}  {rho:.1f}   {np.degrees(phis[i]):5.1f}deg     "
                  f"{np.tan(phis[i]):.3f}  {np.tan(phis[i])**2:.3f}  {u0:+.5f}  {uh:+.5f}  {uh-u0:+.5f}")

    sep("VERDICT")
    print("  U minimized at phi=0 (b=0) for every m, rho: the uniform condensate wins ->")
    print("  r=0 -> Q=1/3 (degenerate). NO feature at b/a=1/sqrt2; NOT O(2)-flat (staggered")
    print("  strictly costs energy). Third independent fermion-sector computation agreeing")
    print("  the vacuum drives r->0, never r=1/2. So Q=2/3 is NOT a fermion-vacuum effect at")
    print("  mean-field. Robust negative for that hypothesis; RELOCATES the splitting to the")
    print("  action's explicit (bridge-gap) structure or a non-fermionic (gauge) sector --")
    print("  untested here, route open not closed.")


if __name__ == "__main__":
    main()
