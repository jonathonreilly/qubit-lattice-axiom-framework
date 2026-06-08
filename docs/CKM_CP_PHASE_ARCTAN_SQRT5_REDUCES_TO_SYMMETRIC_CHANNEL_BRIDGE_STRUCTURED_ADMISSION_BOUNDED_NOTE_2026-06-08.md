# CKM CP-Phase δ_CKM = arctan√5 Reduces to the Single `cos²δ = 1/n_quark` Bridge — an Open-Gate Admission, Not Derivable From the Axioms (Flavor-Side Complement to the Strong-CP and Koide Admissions)

**Date:** 2026-06-08
**Type:** bounded obstruction note (flavor-side; locates the open boundary under the CKM-atlas package; NOT a closure)
**Claim type:** no_go
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_ckm_cp_phase_arctan_sqrt5_structured_admission_exact.py`](../scripts/audit_companion_ckm_cp_phase_arctan_sqrt5_structured_admission_exact.py) (sympy, 14/14; status block is an executable parse of the cited notes)

## Result

The CKM-atlas package carries the exact CP-phase identity
`δ_CKM = arccos(1/√6) = arctan(√5) = 65.905…°`
([`CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md`](./CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md),
[`CKM_ATLAS_AXIOM_CLOSURE_NOTE.md`](./CKM_ATLAS_AXIOM_CLOSURE_NOTE.md)). This note records that the **entire predictive
content of that angle reduces to one bridge**, `cos²δ = 1/n_quark`, and that the bridge is **not derivable** from the
kinematic axioms `{Lattice, Quantum, Record}` as the framework stands: it is an **admission (an open gate)**,
structurally parallel to the strong-CP `θ_gauge`
([`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](./STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md))
and the charged-lepton Koide `r = |b|²/a²`
([`KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md`](./KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md))
admissions.

**Forced skeleton (computed, exact — runner (A)).** Writing the Wolfenstein apex as `ρ = r√w_A1`, `η = r√w_perp`
with `w_A1 + w_perp = 1`:

- `cos²δ = ρ²/(ρ²+η²) = w_A1`, **independent of the CP radius `r`** (`r` cancels identically). So the angle does
  **not** ride on the radius `r² = 1/6` at all — only on the weight `w_A1`.
- The totally-symmetric ("democratic") projection weight of a single basis state in an `n`-state module is exactly
  `w_A1 = |⟨dem|e_i⟩|² = 1/n` (the all-ones unit vector has each component `1/√n`). At `n = 6`: `w_A1 = 1/6`, so
  `tan δ = √5`, `cos δ = 1/√6`, `δ = arctan(√5)`.

That much is genuinely forced once one **grants** that (i) the CP-even real part `ρ` is the symmetric-channel
projection, (ii) the CP-odd imaginary part `η` is its complement, and (iii) the count is `n_quark = 6`. Those three
grants are exactly the load-bearing admissions, and each is exhibited as un-forced below.

**Non-forcing demonstrations (computed, exact — runner (B), the freedom shown explicitly).**

| # | demonstration | what it shows |
|---|---|---|
| B1 | symmetric-block dim `1 → 65.9°`, `2 → 54.7°`, `3 → 45°` on the same 6-state module | the `1 + 5` split is a **choice**, not forced (matches the `rho_eta_to_delta` disclaimer) |
| B2 | democratic angle in **3-generation** space `= arccos(1/√3) = 54.7°` ≠ atlas `65.9°` | the count `n = 6 = 2(weak)×3(color)` is load-bearing; a **generational** CP phase set by the **weak×color** count is an un-forced bridge |
| B3 | native CP-odd phases: circulant `arg(b) ≈ 2/9 rad ≈ 12.7°` and `Z₃` source `2π/3 = 120°` | both ≠ `65.9°` — `δ_CKM` is **not** the framework's native phase |
| B4 | `η² = 1/n_pair² − 1/n_color² = 5/36`, `ρA² = 1/n_color² = 1/9`, `η² + ρA² = 1/n_pair² = 1/4` | the "inverse-square count" reading is an exact **re-encoding** of `(ρ,η)`, not an independent forcing |

**Admission status (executable cross-check of the cited files; runner (C)).** The two grants that the forced skeleton
needs — the CP-even↔symmetric / CP-odd↔complement **channel assignment**, and the raw radius `r² = 1/n_quark` — both
ride the bilinear tensor carrier `K_R`, which
[`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](./S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md) records as
**`claim_type: open_gate`, a class-A definition only**, with three explicitly-unclosed upstream derivation gaps and
its physical-tensor-primitive interpretation **asserted, not derived**. The `1 + 5` split itself is disclaimed as
**"NOT forced by the Cl(3)/Z³ baseline"** by the narrow theorem that owns the algebra
([`CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md`](./CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md),
the only `retained` row in the chain).

**Conclusion (runner closing block).** The bridge `cos²δ = 1/n_quark` is therefore **not derivable** from
`{Lattice, Quantum, Record}`: `δ_CKM = arctan(√5)` is an **admission (an open gate)**. The cleanest closure target is a
retained-grade bridge identifying `K_R` with a physical readout primitive **and** fixing the CP-even↔symmetric /
CP-odd↔complement channel assignment (the `K_R` note's open gaps #2 and #3).

## Parallel picture for the three famous-anomaly matches

| sector | admission | the un-derived dynamics it rides on |
|---|---|---|
| **strong-CP** | `θ_gauge = 0` | the un-derived gauge action-class (the `F̃F` slot) |
| **charged-lepton** | Koide `r = |b|²/a² = 1/2` | the un-derived matter realization (the within-record resolution) |
| **CKM CP phase** | `cos²δ = 1/n_quark` (this note) | the un-derived `K_R` channel assignment + `n = 6` identification |

In all three the *kinematic* axioms fix the **structure** but not the **value**, because the value rides on a
**dynamics**/realization the axioms do not supply. The framework's one piece of independent empirical contact here — the
**sub-σ** agreement of `δ_CKM = 65.905°` with the world-average unitarity-triangle angle `γ` (HFLAV Summer 2025
`≈ 66.4⁺²·⁷₋₂·₈°`; CKMfitter `≈ 65.6⁺⁰·⁹₋₂·₇°`; UTfit `≈ 65.8 ± 2.2°`; note the newest *direct* LHCb-2025
combination sits lower, so the pull is sensitivity-dependent) — is a **postdiction on the admitted bridge**: it
consistency-checks `cos²δ = 1/n_quark` against data, but it does **not** forward-falsify the axioms, and it accrues as
such **whether or not** this admission ever closes. (This note makes **no** claim about the leptonic `δ_CP`, whose
status is a separate, conditional matter on a different, unaudited chain.)

## Scope — what this is and is not

- **Is:** a computed reduction (runner (A)) showing the angle's whole content is `cos²δ = w_A1`, radius-independent,
  plus exact demonstrations (runner (B)) that the chosen `1 + 5` split, the count `n = 6`, and the channel
  assignment are each un-forced, plus an executable cross-check (runner (C), which parses the cited notes) of the
  framework's own `open_gate` status for the carrier they ride on — concluding that the bridge is an admission.
- **Is not:** a claim that `δ_CKM ≠ arctan(√5)`, or that the CKM-atlas package is wrong (it is import-clean and
  internally exact); a new axiom, primitive, or admission; a derivation of the `K_R` gaps; a closure of the CKM CP
  phase. The atlas package's bounded/conditional status is unchanged.
- **Residual:** `δ_CKM = arctan(√5)` reduces to the `K_R` **channel-assignment + physical-primitive** bridge and the
  `n = 6` (weak×color, not generation) identification — the open targets.

## Forbidden-import / reprove-and-cite discipline

- The forced skeleton (radius-independent trig; `w_A1 = 1/n` democratic-projection geometry, both symbolic and the
  explicit `n = 6` projector) and every non-forcing demonstration (the split-dependence, the 3-generation-vs-6
  count, the native-phase mismatch, the inverse-square re-encoding) are **reproven** from sympy primitives in the
  runner (exact).
- The CKM-atlas notes, the `rho_eta_to_delta` narrow theorem, and the `K_R` primitive note are **comparators** for
  provenance / cross-check, never derivation inputs; the runner's status block (C) is an **executable parse** of those
  files, not hard-coded. The measured `γ` (direct world average `≈ 66.4°`, HFLAV Summer 2025; indirect global fit
  `≈ 65.6–65.8°`) is a **comparator** only — named for provenance, never a derivation input.
- No PDG value enters any derivation; `γ` is a downstream comparator. `α_s` does not enter the angle (it sets the
  CKM magnitudes and `J_0` only).

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`CKM_ATLAS_AXIOM_CLOSURE_NOTE.md`](./CKM_ATLAS_AXIOM_CLOSURE_NOTE.md)
- [`CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md`](./CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md)
- [`CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md`](./CKM_CP_PHASE_RHO_ETA_TO_DELTA_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](./S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)
- [`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](./STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md)
- [`KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md`](./KOIDE_DOUBLET_IS_FROBENIUS_SCHUR_COMPLEX_TYPE_ORIENTATION_BOUNDED_NOTE_2026-06-07.md)

**Independent audit required.** This note asserts no effective-status change.
