# C4b check

Provenance: a fresh-context checker of the same model family. All code is new: a position-space engine (`vc_core.py`) with Euler-operator brackets, √gR from Christoffels, and divergence tests via E_N. The covariant Weyl operator was built from the LC spin connection, and G_f^(1) from the symmetric-gauge lift; neither was fitted. Saved by the supervisor from the hand-back.

**Total: 23 PASS, 0 FAIL** in its own runners. C4b's own runner was audited by back-substitution: 21/21, and no solution fails.

**Harness hazard found.** `sympy.solve` silently drops parameter-only equations. C4b is not affected.

## Verdicts

- **B1/B2: confirmed.**
  - The G2 normalisation is not hidden: the common lapse rule forces μ = λ_f. The half-density weight is forced (w = ½). The symmetric square root is irrelevant at this order.
  - **Correction:** the only input selecting K1 = K2 is a = 1, i.e. h_member = (EᵀE)^(−1) − δ, which is fixed by definition. The invariant result is γ = a_s K1/K2 = 1: B21's equivalence (d), realised for the spinor walker. The spinor-specific parts are C1 (λ_f = ν) and A2.
- **A2: confirmed** with a different engine.
- **G1/G2: confirmed independently.**
  - c = ¼ is unique; with the other connection sign, no c works.
  - T is ε_abc ω_abc, the totally antisymmetric part of the LC spin connection. It is not torsion: use "totally antisymmetric LC spin connection (axial part of the anholonomy)".
  - G3: through second order, the covariant operator equals walker + ¼∫N T^(2) n.
  - **Not new in the repo.** Block 65 (the blind-walk note, 2026-09-21) has the exact lattice version: a twist-weighted scalar hop, ½ div ϑ = −⅛ε·T. The 09-13 native-Weyl note uses the full covariant D_g.
  - **Caveat fix:** block 65 has the first-order lattice term; only the second-order T^(2) is missing.
- **C1/C2: confirmed** with a constructed G_f^(1).
  - {G, G} at χχ̄ closes exactly. (λ_f, β) ∈ {(0,0), (ν, ν²)} along the tested line.
  - This agrees with the 09-13 note's P7/P13, the joint polar action. So the spin-½ note's Result 4 "needs a triad" is too strong; record the conflict.
- **F1/F2: confirmed.**
  - The covariant walker closes at r = 1 and 2.
  - The bare walker fails: 96 residual equations, and is inconsistent even with an arbitrary 33-candidate correction (rank 17 vs 18).
- **Scope.**
  - Equal cones v_walker² = K2/(4α) hold for every a_s.
  - With v = 1 fixed, closure forces α = K2/4 = a_s K1/4. Block 62 T4 says "nothing here forces that value"; within these premises, closure does.
  - Suggested wording: "Closure with the walker (speed 1) puts both cones at the walker's top speed and forces α = K2/4; with a_s = 1 this is block 62's α = K/4 with a single K."
- **Not checked independently:** A1a/A1b, D1/D3, E1/E2, G4. They pass the audit.
