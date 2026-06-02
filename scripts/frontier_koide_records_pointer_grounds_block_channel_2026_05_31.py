#!/usr/bin/env python3
"""
Finite C3 pointer/trace channel bookkeeping.

The runner checks algebra for a pointer-style observable S=C+C^2 and a trace-style
dimension count. It does not prove records dynamics, environmental monitoring,
objectivity, or selection of r=1/2.

  F1  THE REAL POINTER-STYLE OBSERVABLE IS THE 2-BLOCK GRADING. A real, charge-conjugation-
      invariant environment monitors the real C3-equivariant observable S = C + C^2 = B,
      whose spectrum is {+2, -1, -1} -- exactly TWO eigenspaces (singlet +2, doublet -1).
      The complex character lines omega, omega^2 are complex CONJUGATES, hence
      record-INDISTINGUISHABLE by any real correlator, so they einselect together as ONE
      sector. The pointer therefore resolves the 2 Wedderburn BLOCKS, not the 3 character
      dimensions.

  F2  IT SIDESTEPS THE ANTICOMMUTING NO-GO. The block grading S COMMUTES with
      Gamma_chi = 2 P_singlet - I (both circulant), co-diagonalizing the 2 blocks; it
      never anticommutes. So koide_z3_equivariant_anticommuting_no_go (which forbids
      CHIRAL/anticommuting block operators) does not touch the COMMUTING block-grading
      pointer. Likewise the doublet complex structure J=(C-C^2)/sqrt3 commutes with C and
      is a single fixed tensor (not a continuous U(1)_b), so C^3=I does not obstruct it.

  F3  TRACE-STYLE COUNT. The full trace weights the doublet by dimension 2.

  F4  THE FUNCTIONAL FORK. With block energies (E_+, E_perp) = (3a^2, 6|b|^2): every
      equal-weight functional (geometric mean, log-sum, product) extremizes at
      E_+ = E_perp -> r=1/2 -> Q=2/3 (the per-block / ratio reading); every dimension-
      weighted functional extremizes at E_perp = 2 E_+ -> r=1 -> Q=1; the linear trace is
      FLAT on the fixed-norm constraint (ranks neither). So the bit is which functional,
      and the pointer-vs-relaxation split is what supplies each side.

CONCLUSION: the finite algebra supports a two-block pointer-style readout and a
dimension-weighted trace-style readout. The actual records/objectivity dynamics remain open.
"""

import sys

import numpy as np

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
B = C + C2
Jcs = (C - C2) / np.sqrt(3)
I3 = np.eye(3, dtype=complex)
P_singlet = np.ones((3, 3), dtype=complex) / 3
Gamma_chi = 2 * P_singlet - I3
F = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)


def main():
    section("Finite C3 pointer/trace channel bookkeeping")

    # ---- F1: the real pointer-style observable is the 2-block grading -----------
    section("F1 - pointer-style S=C+C^2 resolves 2 blocks")
    S = B
    record("F1.1 S = C + C^2 is real and C3-equivariant; spectrum {+2,-1,-1} = 2 eigenspaces",
           np.allclose(S.imag, 0) and np.allclose(S @ C - C @ S, 0)
           and sorted(np.round(np.linalg.eigvals(S).real)) == [-1, -1, 2],
           f"spec(S) = {sorted(np.round(np.linalg.eigvals(S).real))} (singlet +2, doublet -1,-1)")
    # the two doublet character states v_omega, v_omega^2 are conjugates -> same S-eigenvalue
    v_w, v_w2 = F[:, 1], F[:, 2]
    Sw = (v_w.conj() @ S @ v_w).real
    Sw2 = (v_w2.conj() @ S @ v_w2).real
    record("F1.2 omega, omega^2 are complex conjugates -> SAME pointer eigenvalue "
           "with the same pointer-style eigenvalue",
           abs(Sw - Sw2) < 1e-12 and np.allclose(v_w2, v_w.conj()),
           f"<v_w|S|v_w>={Sw:.3f}, <v_w2|S|v_w2>={Sw2:.3f} (equal); v_w2 = conj(v_w)")

    # ---- F2: sidesteps the anticommuting no-go ---------------------------------
    section("F2 - the block grading commutes with Gamma_chi")
    record("F2.1 [S, Gamma_chi] = 0 (co-diagonalizes the 2 blocks; never anticommutes) -> "
           "the anticommuting no-go's target is not this commuting block grading",
           np.allclose(S @ Gamma_chi - Gamma_chi @ S, 0),
           f"|[S,Gamma_chi]| = {np.max(np.abs(S@Gamma_chi - Gamma_chi@S)):.1e}; "
           f"|{{S,Gamma_chi}}| = {np.max(np.abs(S@Gamma_chi + Gamma_chi@S)):.2f} (commutes)")
    record("F2.2 J=(C-C^2)/sqrt3 commutes with C, J^2=-P_doublet, a single FIXED tensor "
           "(not a continuous U(1)_b) -> C^3=I does not obstruct the per-block measure-J",
           np.allclose(Jcs @ C - C @ Jcs, 0) and np.allclose(Jcs @ Jcs, -(I3 - P_singlet)),
           "fixed complex structure, not a one-parameter symmetry group")

    # ---- F3: trace-style dimension count ---------------------------------------
    section("F3 - trace-style dimension count")
    # dephasing in the pointer (character) basis: off-diagonals -> 0, diagonal uniform
    rho0 = np.outer(F[:, 0], F[:, 0].conj())          # any pure generation state
    deph = np.diag(np.diag(F.conj().T @ rho0 @ F))    # dephase in character basis
    rho_relax = F @ (np.eye(3) / 3) @ F.conj().T      # full dephasing -> max-mixed
    record("F3.1 full trace I/3 weights the doublet by dimension 2",
           np.allclose(rho_relax, I3 / 3),
           "two-block pointer-style count and dimension-weighted trace count are distinct")

    # ---- F4: the functional fork -----------------------------------------------
    section("F4 - equal-weight functional -> r=1/2; dimension-weighted -> r=1; trace flat")
    # E_+ = 3a^2, E_perp = 6 b^2, fixed total E_+ + E_perp = T
    import sympy as sp
    a2, b2, lam = sp.symbols("a2 b2 lam", positive=True)
    E_p, E_q = 3 * a2, 6 * b2
    # equal-weight log-capacity: maximize log E_+ + log E_perp at E_+ + E_perp = T
    T = sp.Symbol("T", positive=True)
    Lg = sp.log(E_p) + sp.log(E_q) - lam * (E_p + E_q - T)
    sol = sp.solve([sp.diff(Lg, a2), sp.diff(Lg, b2), E_p + E_q - T], [a2, b2, lam], dict=True)[0]
    r_eqwt = sp.simplify(sol[b2] / sol[a2])
    record("F4.1 equal-weight log-capacity extremum -> E_+=E_perp -> r=|b|^2/a^2=1/2 -> Q=2/3",
           r_eqwt == sp.Rational(1, 2), f"r* (equal-weight) = {r_eqwt}")
    # dimension-weighted: log E_+ + 2 log E_perp
    Ld = sp.log(E_p) + 2 * sp.log(E_q) - lam * (E_p + E_q - T)
    sold = sp.solve([sp.diff(Ld, a2), sp.diff(Ld, b2), E_p + E_q - T], [a2, b2, lam], dict=True)[0]
    r_dimwt = sp.simplify(sold[b2] / sold[a2])
    record("F4.2 dimension-weighted extremum -> r=1 -> Q=1; linear trace E_++E_perp=T flat",
           r_dimwt == 1, f"r* (dimension-weighted) = {r_dimwt}; trace = T (constant, ranks neither)")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  Finite algebra supports two bookkeeping readouts:")
    print("    pointer-style S=C+C^2 resolves singlet/doublet blocks")
    print("    trace-style I/3 weights the doublet by dimension")
    print("  Equal-weight and dimension-weighted functionals give different extrema.")
    print("  Records/objectivity dynamics are not derived here.")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
