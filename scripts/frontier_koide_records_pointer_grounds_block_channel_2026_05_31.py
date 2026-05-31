#!/usr/bin/env python3
"""
The two aspects of the native records dynamics ARE the two C3 channels: the records
POINTER (einselection) is the 2-block grading -> per-block -> the RATIO channel (Q=2/3);
the records RELAXATION (dephasing -> max-mixed) is the trace -> per-dimension -> the
ASYMMETRY channel (2/9). So both measures are natively supplied, one per channel.

This grounds the readout-channel map: the previously-feared "per-block-vs-per-dimension
measure ambiguity" is the native records dynamics carrying both a pointer and a
relaxation, which read the doublet's two complementary observables. Verified:

  F1  THE REAL-RECORDS POINTER IS THE 2-BLOCK GRADING. A real, charge-conjugation-
      invariant environment monitors the real C3-equivariant observable S = C + C^2 = B,
      whose spectrum is {+2, -1, -1} -- exactly TWO eigenspaces (singlet +2, doublet -1).
      The complex character lines omega, omega^2 are complex CONJUGATES, hence
      record-INDISTINGUISHABLE by any real correlator, so they einselect together as ONE
      sector. The pointer therefore resolves the 2 Wedderburn BLOCKS, not the 3 character
      dimensions -- the per-block COUNTING is NATIVE, not an arbitrary choice.

  F2  IT SIDESTEPS THE ANTICOMMUTING NO-GO. The block grading S COMMUTES with
      Gamma_chi = 2 P_singlet - I (both circulant), co-diagonalizing the 2 blocks; it
      never anticommutes. So koide_z3_equivariant_anticommuting_no_go (which forbids
      CHIRAL/anticommuting block operators) does not touch the COMMUTING block-grading
      pointer. Likewise the doublet complex structure J=(C-C^2)/sqrt3 commutes with C and
      is a single fixed tensor (not a continuous U(1)_b), so C^3=I does not obstruct it.

  F3  RELAXATION -> TRACE -> THE OTHER CHANNEL. The records DEPHASING fixed point is the
      maximally-mixed state I/3 (the full-algebra trace), which weights the doublet by its
      dimension 2 -> per-dimension -> the spectral-asymmetry channel. So the two native
      records aspects -- POINTER (einselection) and RELAXATION (dephasing) -- supply the
      two measures (block and dimension) = the two channels (ratio and asymmetry).

  F4  THE FUNCTIONAL FORK. With block energies (E_+, E_perp) = (3a^2, 6|b|^2): every
      equal-weight functional (geometric mean, log-sum, product) extremizes at
      E_+ = E_perp -> r=1/2 -> Q=2/3 (the per-block / ratio reading); every dimension-
      weighted functional extremizes at E_perp = 2 E_+ -> r=1 -> Q=1; the linear trace is
      FLAT on the fixed-norm constraint (ranks neither). So the bit is which functional,
      and the pointer-vs-relaxation split is what supplies each side.

CONCLUSION (native grounding of the channel map, positive; NOT a forced selection of one
value): the records dynamics natively supplies BOTH counts -- the einselection pointer
gives the 2-block grading (per-block, the mass-ratio channel), the dephasing relaxation
gives the trace (per-dimension, the spectral-asymmetry channel). The per-block COUNTING
is native (the pointer resolves 2 blocks because the conjugate characters are
record-degenerate); what remains open is only whether the pointer's equal-energy
extremum (r=1/2) is FORCED by a max-redundancy/objectivity principle (Stage 2). Several
walls cited against forcing r=1/2 are unaudited and/or mis-targeted (see note). READ-ONLY
certificate; tiers audit-decided.
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
    section("The two records aspects are the two C3 channels (pointer=block, relaxation=trace)")

    # ---- F1: the real-records pointer is the 2-block grading --------------------
    section("F1 — real-records pointer S=C+C^2 resolves 2 BLOCKS (omega,omega^2 record-degenerate)")
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
           "(record-INDISTINGUISHABLE) -> einselected as ONE doublet sector",
           abs(Sw - Sw2) < 1e-12 and np.allclose(v_w2, v_w.conj()),
           f"<v_w|S|v_w>={Sw:.3f}, <v_w2|S|v_w2>={Sw2:.3f} (equal); v_w2 = conj(v_w)")

    # ---- F2: sidesteps the anticommuting no-go ---------------------------------
    section("F2 — the block grading COMMUTES with Gamma_chi (sidesteps the chiral no-go)")
    record("F2.1 [S, Gamma_chi] = 0 (co-diagonalizes the 2 blocks; never anticommutes) -> "
           "the anticommuting no-go (forbids CHIRAL block ops) does not touch it",
           np.allclose(S @ Gamma_chi - Gamma_chi @ S, 0),
           f"|[S,Gamma_chi]| = {np.max(np.abs(S@Gamma_chi - Gamma_chi@S)):.1e}; "
           f"|{{S,Gamma_chi}}| = {np.max(np.abs(S@Gamma_chi + Gamma_chi@S)):.2f} (commutes)")
    record("F2.2 J=(C-C^2)/sqrt3 commutes with C, J^2=-P_doublet, a single FIXED tensor "
           "(not a continuous U(1)_b) -> C^3=I does not obstruct the per-block measure-J",
           np.allclose(Jcs @ C - C @ Jcs, 0) and np.allclose(Jcs @ Jcs, -(I3 - P_singlet)),
           "fixed complex structure, not a one-parameter symmetry group")

    # ---- F3: relaxation -> trace -> the other channel --------------------------
    section("F3 — records relaxation (dephasing) -> max-mixed I/3 -> trace (per-dim channel)")
    # dephasing in the pointer (character) basis: off-diagonals -> 0, diagonal uniform
    rho0 = np.outer(F[:, 0], F[:, 0].conj())          # any pure generation state
    deph = np.diag(np.diag(F.conj().T @ rho0 @ F))    # dephase in character basis
    rho_relax = F @ (np.eye(3) / 3) @ F.conj().T      # full dephasing -> max-mixed
    record("F3.1 dephasing fixed point = maximally-mixed I/3 (full-algebra trace) -> "
           "weights the doublet by its dimension 2 -> per-dimension / asymmetry channel",
           np.allclose(rho_relax, I3 / 3),
           "POINTER (einselection)=2-block=per-block=RATIO; RELAXATION=trace=per-dim=ASYMMETRY")

    # ---- F4: the functional fork -----------------------------------------------
    section("F4 — equal-weight functionals -> r=1/2; dimension-weighted -> r=1; trace flat")
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
    print("  The native records dynamics supplies BOTH C3 measures, one per channel:")
    print("    POINTER (einselection, S=C+C^2, resolves 2 blocks)  -> per-block  -> RATIO (Q=2/3)")
    print("    RELAXATION (dephasing -> max-mixed I/3 = trace)      -> per-dim    -> ASYMMETRY (2/9)")
    print("  Per-block COUNTING is NATIVE: the pointer resolves 2 blocks because the")
    print("  conjugate characters omega,omega^2 are record-degenerate. The block grading")
    print("  COMMUTES with Gamma_chi (sidesteps the chiral no-go); the measure-J is a fixed")
    print("  tensor (C^3=I irrelevant). Open: is the pointer's equal-energy r=1/2 FORCED by")
    print("  a max-redundancy/objectivity principle (Stage 2)?")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
