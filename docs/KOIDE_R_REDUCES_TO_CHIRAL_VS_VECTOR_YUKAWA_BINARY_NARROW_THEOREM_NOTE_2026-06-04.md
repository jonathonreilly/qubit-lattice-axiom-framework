# Koide r on the Clean Lepton Lane Reduces to One Gated Bit: Chiral vs Vector Generation Yukawa (Narrow Theorem)

**Date:** 2026-06-04
**Type:** narrow_theorem
**Claim type:** narrow_theorem (exact Frobenius-Schur structure) + conditional reduction.
Sharpens the block-4 (#2614) open lead into a rigorous, concrete binary.
**Claim scope:** the Frobenius-Schur indicators of the C3 generation isotypes are `nu(trivial) =
+1` (real type → the singlet parameter `a` is real) and `nu(omega) = 0` (complex type → the
doublet parameter `b` is complex). Consequently the singlet contributes **one** fluctuation mode
in both the vector and chiral cases, while the doublet contributes **two** real modes (vector
`Re b, Im b`) or **one** holomorphic mode (chiral `b`). So the Koide ratio on the clean
color-singlet lepton lane is exactly:

> `r = 1/2` (Q=2/3, kappa=2) ⟺ the generation Yukawa fluctuation is **chiral / holomorphic**
> (`b` counted once); `r = 1` (Q=1, kappa=1) ⟺ it is **vector / real** (`Re b, Im b` counted
> separately).

The whole question reduces to **one gated bit** — chiral or vector — set by the open
staggered-Dirac mass structure (substep 4).
**actual_current_surface_status:** the FS structure and the weighting→r map are exact (sympy);
the **selection** of the bit (chiral vs vector) is GATED. Conditional on the open staggered-Dirac
mass gate. Not retained on the current surface.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_koide_r_reduces_to_chiral_vs_vector_yukawa_binary_exact.py`](./../scripts/audit_companion_koide_r_reduces_to_chiral_vs_vector_yukawa_binary_exact.py)

## Context (physics-loop dirac-corner-coupling, block 5)

Block 4 (#2614) identified the chirality-graded **supertrace / holomorphic** count as the one
untested route to the Koide `(1,1)` weighting (r=1/2): it counts the complex doublet parameter
`b` once, where the plain trace counts `(Re b, Im b)` twice. A natural objection: *"a uniform
'count complex modes' would rescale everything and preserve the (1,2) ratio."* This note refutes
that objection with the **Frobenius-Schur** structure and sharpens the lead into a clean binary.

## Statement

1. (**FS types**) For C3, the Frobenius-Schur indicators are `nu(rho) = (1/|G|) sum_g chi_rho(g^2)`:
   `nu(trivial) = +1` (**real** type) and `nu(omega) = nu(omega-bar) = 0` (**complex** type).
   Hence `a` (trivial-isotype coefficient) is real, `b` (doublet coefficient) is complex.
2. (**mode counts**) The real-type singlet contributes **1** fluctuation mode in both cases
   (`a` is self-conjugate). The complex-type doublet contributes **2** real modes (`Re b, Im b`,
   vector) or **1** holomorphic mode (`b`, chiral).
3. (**weighting → r**) With `E_singlet = 3a^2`, `E_doublet = 6|b|^2` and weights `(w_s, w_d)`,
   the extremum sits at singlet energy fraction `x = w_s/(w_s+w_d)`, giving
   `r = (1-x)/(2x)`. So vector `(1,2) → r = 1` and chiral `(1,1) → r = 1/2`.
4. (**objection refuted**) A uniform "count complex modes" gives `(1/2, 1)`, which is
   proportional to `(1,2)` → still `r = 1`. The `(1,1)` weighting is therefore **not** uniform
   complex counting; it requires the FS asymmetry — the real-type singlet keeps a full mode
   while only the complex-type doublet drops `2 → 1`.
5. (**the binary**) `r ∈ {1/2, 1}` exactly, selected by one bit: chiral (`b` once) vs vector
   (`b` twice).

All seven checks pass exactly (sympy).

## Why this matters

- It makes the block-4 mechanism **rigorous**: the `(1,1)` does not come from a flavor-dependent
  admission (block 3) nor from a uniform rescaling (refuted here); it comes from the **intrinsic
  Frobenius-Schur types** of the C3 irreps combined with a **chiral/holomorphic** readout.
- It compresses the entire Koide-`r` question on the clean color-singlet lepton lane into a
  **single, sharp, gated bit**: *is the generation Yukawa fluctuation chiral or vector?* Every
  other ingredient (the isotype split, the energies, the FS types, the weighting→r map) is exact
  and settled. The framework already carries a chirality grading `eps=(-1)^{x+y+z}` with
  `{eps,D}=0` (kinetic, on main); whether it makes the **mass/Yukawa** fluctuation chiral is the
  open substep-4 gate.

## What is NOT claimed

- Does **not** select the bit: whether the generation Yukawa is chiral or vector is **gated**
  (staggered-Dirac mass, substep 4). This note proves the **reduction**, not the answer.
- Does **not** claim r=1/2 is derived; it shows r=1/2 is equivalent to a single, sharply-stated,
  framework-internal condition (chiral Yukawa) that has never been evaluated.
- Conditional on the open staggered-Dirac mass gate.

## Trace gate

```yaml
trace_class: blocker_sharpening
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: reduces_to_one_bit
artifact_role: narrow_theorem
next_trace_action: "evaluate the gated bit: compute the generation Yukawa fluctuation determinant on the hw=1 corners with the staggered-Dirac mass and determine whether it is chiral (holomorphic, b once -> r=1/2) or vector (real, b twice -> r=1)."
```

## Forbidden imports

- The Frobenius-Schur indicators, the C3 characters, and the isotype energies are reproven from
  primitives. No PDG values as derivation inputs; literature (FS theory, staggered fermions) is
  comparator only.

## Cross-references

- `SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md` (block 4,
  #2614) — the open lead this note sharpens.
- `MULTIFACTOR_CONNES_LOTT_PURCHASES_NOT_DERIVES_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`
  (block 3, #2611) — the flavor-dependent admission this note's mechanism avoids.
- `KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md` — the isotype energies
  `E_+ = 3a^2`, `E_⊥ = 6|b|^2`.
