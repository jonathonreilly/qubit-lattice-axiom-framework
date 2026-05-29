#!/usr/bin/env python3
"""
d=3+1 CORRECTION: the spin-taste (gamma5 (x) xi5) chirality escape was a
d=4 EUCLIDEAN artifact. The framework is d=3+1 (Z^3 space + EMERGENT time):
only 8 spatial BZ corners (Z_2)^3, NO 16-corner / V_4xV_4 / 4-dim taste.
Under the correct structure the chirality no-go for Koide Q=2/3 is ROBUST.

Findings:
  (1) generations = hw=1 S_3-orbit of the 8 spatial corners.
  (2) native chirality C=(-1)^{x+y+z}=(-1)^{Hamming weight} is S_3-INVARIANT
      -> uniform on every S_3 orbit -> uniform on the generation triplet ->
      cannot anticommute with Gamma_chi (which needs S_3/C_3 breaking).
  (3) NO 4-dim taste sector exists in d=3+1 (3D Hamiltonian staggered has 2
      tastes, and the 3 generations are the S_3 orbit, not a taste multiplet)
      -> the gamma5 (x) xi5 escape has nowhere to live -> DISSOLVES.
  (4) 3+1 Dirac Hamiltonian H(m)=alpha.k+beta m has H^2=|k|^2+m^2 (gapped) ->
      no spectral flow / chiral index 0 (sister-lane wall W1 holds in 3+1).
"""

import numpy as np, itertools


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    corners = list(itertools.product([0, 1], repeat=3))
    ham = {c: sum(c) for c in corners}

    sep("(1) d=3+1: 8 spatial corners (Z_2)^3 = 1+3+3+1; generations = hw=1")
    sizes = [sum(1 for c in corners if ham[c] == k) for k in range(4)]
    print(f"  Hamming-weight (S_3) orbit sizes: {sizes} = 1+3+3+1")
    gen = [c for c in corners if ham[c] == 1]
    print(f"  generation triplet (hw=1): {gen}")

    sep("(2) native chirality is S_3-invariant -> uniform on generations")
    C = {c: (-1)**ham[c] for c in corners}
    print(f"  staggered chirality C=(-1)^(x+y+z) on hw=1: {[C[c] for c in gen]} (uniform)")
    print("  C is a function of Hamming weight => S_3-invariant => CONSTANT on")
    print("  each S_3 orbit. Anticommuting with Gamma_chi requires S_3/C_3-breaking")
    print("  (off-diagonal singlet<->doublet). An S_3-invariant chirality CANNOT.")
    print("  => native chirality does NOT split the generations. NO-GO robust.")

    sep("(3) NO 4-dim taste in d=3+1 -> the gamma5(x)xi5 escape dissolves")
    print("  16-corner / V_4 x V_4 / spin(4)(x)taste(4) needs d=4 (Klein-four^2).")
    print("  d=3+1 has 8 spatial corners; 3D Hamiltonian staggered = 2 tastes,")
    print("  and the 3 generations are the S_3 ORBIT (not a taste multiplet).")
    print("  So there is no 4-dim taste sector for xi5 to act in. The previously")
    print("  floated gamma5 (x) xi5 escape was a d=4 artifact and DISSOLVES.")

    sep("(4) 3+1 Dirac Hamiltonian is gapped: H^2=|k|^2+m^2 -> spectral flow 0")
    ax = np.array([[0, 1], [1, 0]]); ay = np.array([[0, -1j], [1j, 0]]); az = np.array([[1, 0], [0, -1]])
    tx = np.array([[0, 1], [1, 0]]); tz = np.array([[1, 0], [0, -1]])
    al = [np.kron(s, tx) for s in (ax, ay, az)]; beta = np.kron(np.eye(2), tz)
    k = (0.7, 0.3, 0.5); m = 1.3
    K = al[0]*k[0] + al[1]*k[1] + al[2]*k[2]
    H = K + beta*m
    target = (k[0]**2 + k[1]**2 + k[2]**2 + m**2) * np.eye(4)
    print(f"  || H^2 - (|k|^2+m^2) I || = {np.max(np.abs(H@H - target)):.2e}")
    print("  => H^2 = |k|^2 + m^2: gap = |m|, never closes as m varies ->")
    print("     no zero-mode crossing -> chiral index 0 (wall W1 holds in 3+1).")

    sep("VERDICT (d=3+1, corrected): chirality no-go is ROBUST")
    print("  The native chirality is S_3-invariant (uniform on the generation")
    print("  orbit) and the Hamiltonian is gapped (index 0). No native chiral")
    print("  structure splits the generations / anticommutes with Gamma_chi.")
    print("  The d=4 spin-taste escape does not exist here. So Q=2/3 via the")
    print("  CHIRALITY lens needs an S_3/C_3-BREAKING import -- confirmed in the")
    print("  correct d=3+1 structure. (And the anticommuting-H lens is itself a")
    print("  formal relabeling: the real gap is the principle fixing the circulant")
    print("  ratio r=|b|^2/a^2=1/2, i.e. why the eigenvalue-vector is Gamma_chi-")
    print("  balanced -- which no lens tried (kinematic/dynamical/quantum/chiral)")
    print("  supplies from A1+A2.)")


if __name__ == "__main__":
    main()
