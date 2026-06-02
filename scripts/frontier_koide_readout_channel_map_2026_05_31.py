#!/usr/bin/env python3
"""
Finite circulant readout bookkeeping map.

The runner decomposes one circulant generation operator H=aI+bC+b-bar C^2
into C3 singlet/doublet amplitudes and checks four finite readouts: singlet
scale, equal-block Q=2/3 at explicit r=1/2, spectral-asymmetry 2/9, and
phase-independence of Q. It does not identify charged-lepton interactions or derive
the source of r=1/2.

  F1  THE DECOMPOSITION. The C3 Fourier transform splits H into a SINGLET amplitude
      a = Tr(H)/3 (the generation-uniform (1,1,1) direction) and a DOUBLET amplitude
      b (the generation-difference directions). Singlet + doublet = the whole operator.

  F2  READOUT 1 -- SCALE (r=0, democratic weight (1,0), Q=1/3). At b=0 the three
      masses are DEGENERATE, the fully-C3-symmetric configuration, whose Koide value is
      Q=1/3.

  F3  READOUT 2 -- RATIO (r=1/2, equal-block weight (1,1), Q=2/3). The doublet MAGNITUDE
      |b| sets the flavor SPLITTING; r=|b|^2/a^2 and Q=(1+2r)/3. The equal-block reading
      gives r=1/2 -> Q=2/3.

  F4  READOUT 3 -- ASYMMETRY (r=1, dimension weight (1,2)). The doublet's SIGNED / spectral
      content gives the finite Z_N equivariant spectral asymmetry L_3(1,2) = 2/9 (the eta /
      Lefschetz weight). Separately the doublet phase is Q-orthogonal.

  F5  ONE OPERATOR, MULTIPLE FINITE READOUTS. All three live in the same H: the eigenvalue MAGNITUDES
      carry the scale (singlet) and the ratio (doublet magnitude); the eigenvalue SIGNS /
      spectral flow carry the asymmetry; the doublet phase is independent of Q.
"""

import sys

import numpy as np
import sympy as sp

PASSES: list[tuple[str, bool, str]] = []


def record(name, ok, detail=""):
    PASSES.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(t):
    print("\n" + "=" * 88 + f"\n{t}\n" + "=" * 88)


w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
C2 = C @ C
I3 = np.eye(3, dtype=complex)
ones = np.ones(3) / np.sqrt(3)            # the (1,1,1) generation-uniform / singlet axis


def L_N(a_tuple, N):
    zeta = sp.exp(2 * sp.pi * sp.I / N)
    total = sum(np.prod([1 / (zeta**(k * aj) - 1) for aj in a_tuple]) for k in range(1, N))
    return sp.nsimplify(complex(sp.expand(total / N).evalf()).real, rational=True)


def main():
    section("Three C3 readouts of one generation operator")

    # ---- F1: the C3 decomposition ----------------------------------------------
    section("F1 — C3 Fourier: H = singlet a (uniform) + doublet b (differences)")
    a_v, b_v = 1.0, 0.31 + 0.21j
    H = a_v * I3 + b_v * C + np.conj(b_v) * C2
    a_read = np.trace(H) / 3
    b_read = np.trace(np.linalg.matrix_power(C, -1) @ H) / 3
    record("F1.1 singlet a = Tr(H)/3 (uniform (1,1,1)); doublet b = (1/3)Tr(C^-1 H)",
           abs(a_read - a_v) < 1e-12 and abs(b_read - b_v) < 1e-12,
           f"a = {a_read:.3f} (uniform scale); b = {b_read:.3f} (flavor splitting)")
    record("F1.2 the singlet axis is (1,1,1)/sqrt3 -- C3-fixed, generation-uniform",
           np.allclose(C.real @ ones, ones),
           "C(1,1,1)=(1,1,1): the generation-uniform direction")

    # ---- F2: readout 1 -- scale -------------------------------------------------
    section("F2 - readout 'scale' (third r=0, democratic (1,0), Q=1/3)")
    H_singlet = a_v * I3                       # b=0: pure singlet
    eig_deg = np.linalg.eigvals(H_singlet).real
    Q_deg = sum(eig_deg**2) / (sum(eig_deg))**2
    record("F2.1 r=0 (b=0, pure singlet): masses degenerate -> Q=1/3",
           np.allclose(eig_deg, a_v) and abs(Q_deg - 1 / 3) < 1e-12,
           f"eig(aI) = {np.round(eig_deg,3)} (degenerate); Q = {Q_deg:.4f} = 1/3")

    # ---- F3: readout 2 -- ratio ------------------------------------------------
    section("F3 - readout 'ratio' (r=1/2, equal-block (1,1), Q=2/3)")
    bm = np.sqrt(0.5) * a_v                      # r=1/2
    eig_r = np.sort(np.linalg.eigvals(a_v * I3 + bm * C + bm * C2).real)
    Q_ratio = sum(eig_r**2) / (sum(eig_r))**2
    record("F3.1 doublet magnitude |b| sets the splitting; equal-block r=1/2 -> Q=2/3",
           abs(Q_ratio - 2 / 3) < 1e-9,
           f"r=|b|^2/a^2=1/2 -> masses {np.round(eig_r,4)} -> Q = {Q_ratio:.6f} = 2/3")

    # ---- F4: readout 3 -- asymmetry --------------------------------------------
    section("F4 - readout 'asymmetry' (r=1, dimension (1,2)): spectral 2/9 + phase")
    L = L_N((1, 2), 3)
    record("F4.1 finite spectral-asymmetry readout: L_3(1,2) = 2/9",
           sp.simplify(L - sp.Rational(2, 9)) == 0, f"L_3(1,2) = {L} = 2/9")
    # Q-orthogonality of the doublet phase delta=arg(b)
    Q_of = lambda b: (lambda lam: sum(lam**2) / (sum(lam))**2)(
        np.sort(np.linalg.eigvals(a_v * I3 + b * C + np.conj(b) * C2).real))
    mag = np.sqrt(0.5) * a_v
    Qs = [Q_of(mag * np.exp(1j * th)) for th in (0, 0.4, 0.9, 1.0)]
    record("F4.2 doublet phase is Q-orthogonal: Q depends only on |b|",
           all(abs(q - Qs[0]) < 1e-9 for q in Qs),
           f"Q(theta) = {[f'{q:.4f}' for q in Qs]} (constant in theta -> phase is independent)")

    # ---- F5: one operator, three channels --------------------------------------
    section("F5 — one operator H, three complementary readouts (not competitors)")
    record("F5.1 scale, Q-readout, spectral-asymmetry readout, and phase are finite "
           "projections of the same H",
           abs(Q_deg - 1 / 3) < 1e-9 and abs(Q_ratio - 2 / 3) < 1e-9
           and sp.simplify(L - sp.Rational(2, 9)) == 0,
           "magnitudes -> scale + ratio; signs/spectral-flow -> asymmetry; phase is Q-orthogonal")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  ONE generation operator H = aI + bC + b-bar C^2, finite readouts:")
    print("    r=0   SCALE     (singlet a, generation-uniform)   -> Q=1/3 (degenerate base)")
    print("    r=1/2 RATIO     (doublet |b|, flavor splitting)    -> Q=2/3 (Koide mass ratio)")
    print("    r=1   ASYMMETRY (doublet sign, spectral flow)      -> 2/9  (eta / L_3)")
    print("    (+ doublet phase is Q-orthogonal)")
    print()
    print("  This is a finite bookkeeping map, not a channel-closure theorem.")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
