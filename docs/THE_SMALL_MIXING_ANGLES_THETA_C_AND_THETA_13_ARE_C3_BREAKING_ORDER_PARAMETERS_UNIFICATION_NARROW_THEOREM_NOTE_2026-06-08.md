# The Small Mixing Angles θ_C and θ₁₃ Are C₃-Breaking Order Parameters — a Quark/Lepton Unification (Narrow Theorem)

**Date:** 2026-06-08
**Claim type:** bounded_theorem (structural unification: both small mixing angles are C₃-breaking order parameters; the √(mass-ratio) magnitude is the GST residual)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/mixing_angles_are_c3_breaking_order_parameters_runner.py`](../scripts/mixing_angles_are_c3_breaking_order_parameters_runner.py)
**Cached output:** [`logs/runner-cache/mixing_angles_are_c3_breaking_order_parameters_runner.txt`](../logs/runner-cache/mixing_angles_are_c3_breaking_order_parameters_runner.txt)

## Audit context

The Cabibbo angle θ_C is already reduced in the framework to a mass ratio (`|V_us| ≈ √(m_d/m_s)`,
[`CKM_FROM_MASS_HIERARCHY`](CKM_FROM_MASS_HIERARCHY_NOTE.md);
[`DOWN_TYPE_MASS_RATIO_CKM_DUAL`](DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md), `m_d/m_s = α_s(v)/2`;
`|V_us| = 0.2251` vs PDG `0.2243`). This note supplies the **structural** statement that unifies it
with the companion reactor-angle result: **both small mixing angles are C₃-breaking order
parameters** — the framework's C₃-symmetric leading order has **no** mixing, so every small angle is a
C₃-breaking deviation.

## Safe statement

**Theorem (the small mixing angles are C₃-breaking order parameters).**

1. **Quark: C₃-symmetric ⟹ no Cabibbo.** C₃-equivariant (circulant) up- and down-mass matrices are
   co-diagonalized by the DFT, so `V_CKM = U_up†U_dn = I` (verified). Equivalently — basis-independently —
   shared-C₃ circulants **commute** (`‖[M_up,M_dn]‖ = 0`), so `V_CKM` is a **permutation**
   ([`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY`](QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md),
   `retained_no_go`). A nonzero Cabibbo (off-permutation) **requires** `[M_up,M_dn] ≠ 0` — i.e.
   **C₃-breaking** (verified: `‖[M_up,M_dn+εP]‖` grows from 0 with the breaking ε). So **θ_C is the
   quark C₃-breaking deviation.**
2. **Lepton: C₃-symmetric ⟹ no θ₁₃.** The C₃-symmetric neutrino records give the trimaximal PMNS
   column (the C₃ singlet) with a **2-fold degenerate doublet**, so θ₁₃ = 0 at C₃-symmetric order; θ₁₃
   is the C₃-doublet-breaking deviation
   ([`THETA13_IS_THE_C3_DOUBLET_BREAKING_MEASURE`](THETA13_IS_THE_C3_DOUBLET_BREAKING_MEASURE_SQRT2_DERIVED_THETA_E_THE_RESIDUAL_NARROW_THEOREM_NOTE_2026-06-08.md),
   this session). So **θ₁₃ is the lepton C₃-breaking deviation.**
3. **Unified.** Both θ_C and θ₁₃ are **C₃-breaking order parameters**: the leading order is
   C₃-symmetric (`V_CKM = I`, trimaximal PMNS), and nonzero angles measure departures from that
   limit. This note does not derive the amount of breaking. For the geometric-mean (GST) breaking
   texture, the angles scale as `sin θ ≈ √(mass ratio)` (verified: tight in the hierarchical limit;
   ~10% at the physical `m_d/m_s ≈ 0.05` — the Cabibbo-haze level).

## Why this is the answer to "go after θ_C"

- θ_C is already *numerically* reduced to `√(m_d/m_s) = √(α_s(v)/2)`. This note gives its **structural
  meaning**: θ_C is the C₃-breaking of the quark sector — the same mechanism that makes θ₁₃ the
  C₃-doublet breaking of the lepton sector. The small-mixing sector is **one phenomenon** (C₃-breaking),
  not a list of unrelated small numbers.
- It pins the residual cleanly: the *existence* of the angles is the C₃-breaking (structural);
  the *magnitude* `√(mass ratio)` is the **GST texture** (geometric-mean breaking) — a named
  upstream residual shared by the small-angle account.

## Boundary (honest)

- **Structural unification + location, not the magnitudes.** The √(mass-ratio) magnitudes (θ_C, θ₁₃
  values) rest on the GST texture (admitted) + the mass ratios (the down-quark hierarchy → α_s); this
  note derives that both angles are C₃-breaking, not their numerical values.
- The GST `sin θ ≈ √(m₁/m₂)` is the hierarchical-limit relation (~10% at the physical ratio).
- The size of the C₃ breaking is an upstream mass-structure question.

## Forbidden imports check

No new axiom. A_min + the retained circulant boundary + the companion θ₁₃ result + the trimaximal
column; standard mixing geometry (3×3 / 2×2, reproduced). The GST texture is *named* as the magnitude
residual, not imported as a derivation. Memory-safe.

## Runner check breakdown

Class A: (A1) circulant quark masses ⟹ `V_CKM = I`; (A2) circulants commute (permutation), C₃-breaking
⟹ non-commuting ⟹ Cabibbo; (A3) C₃-symmetric lepton ⟹ degenerate doublet ⟹ θ₁₃=0, breaking ⟹ θ₁₃≠0;
(A4) both are C₃-breaking, √(mass-ratio)-scaled (GST). Expected `runner_check_breakdown = {A: 4, B: 0,
C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

C₃-equivariant circulant quark masses give `V_CKM = I` (and commute ⟹ permutation, the retained
boundary), so a nonzero Cabibbo requires non-commuting mass matrices = C₃-breaking (verified by the
commutator growing from zero with the breaking). The C₃-symmetric neutrino sector gives the trimaximal
column with a degenerate doublet, so θ₁₃ = 0 at C₃-symmetry and is the doublet-breaking. Hence both
small mixing angles are C₃-breaking order parameters; it does not derive the amount of breaking.
For the geometric-mean (GST) texture they scale as √(mass ratio). The note is honest that it unifies and locates
(both = C₃-breaking) rather than deriving the magnitudes, which rest on the named GST texture and the
mass ratios. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/mixing_angles_are_c3_breaking_order_parameters_runner.py
```
