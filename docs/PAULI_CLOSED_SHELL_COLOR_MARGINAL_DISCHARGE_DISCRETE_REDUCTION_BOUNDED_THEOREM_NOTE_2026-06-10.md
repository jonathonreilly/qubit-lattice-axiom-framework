# Pauli Filling Forces the Color Marginal `I₃/3` in Closed-Shell Sectors

**Date:** 2026-06-10
**Type:** bounded_theorem (closed-shell discharge and open-shell residual for admission (B)'s purity core)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_pauli_closed_shell_color_marginal_discharge_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_pauli_closed_shell_color_marginal_discharge_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=16 FAIL=0`, exact, no MC.

## Dependency boundary

- [`COLOR_DEPOLARIZATION_ADM2_GATING_ADMISSIONS_COLLAPSE_TO_TWO_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_DEPOLARIZATION_ADM2_GATING_ADMISSIONS_COLLAPSE_TO_TWO_NARROW_THEOREM_NOTE_2026-06-09.md)
  is the source-side admission-split context: the global color-neutrality input
  has an orientation component and a purity/color-marginal component.
- [`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md`](MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md)
  is the source-side necessary-condition note that identifies
  `rho_color = I3/3` as the relevant marginal condition for the gauge-link
  step-measure premise.
- [`COLOR_EINSELECTION_MATTER_UNITARY_PRIMITIVITY_REQUIRES_BACKGROUND_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_EINSELECTION_MATTER_UNITARY_PRIMITIVITY_REQUIRES_BACKGROUND_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09.md)
  records the named color-diagonal free-hopping surface and the background-
  connection boundary.
- [`CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md`](CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md)
  and
  [`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
  are cited as representation/fermion-context support. This runner recomputes
  the finite Fock-space facts it consumes.
- [`COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md`](COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md)
  is the inherited symmetric-base to physical-color bridge boundary. This note
  does not close that bridge.

## The admission under attack

The gauge-dynamics campaign consolidated ADM-2's color-depolarization input onto two
admissions; **admission (B)** is the global color-neutrality input in the
admission-collapse note linked above. Its orientation component was separated by
the orientation-equivalence note; its purity component is the color marginal
condition `Tr rho_color^2 = 1/3`, which the past-hypothesis reduction note left
as an orthogonal residual. The mechanism used here is fermionic filling.

## The theorems (exact — runner `PASS=16 FAIL=0`)

**(T1) Pauli forces the local singlet at exact full filling.** The 3-fermion sector of a
cell's three color modes is **one-dimensional** — no wavefunction choice exists — and
**all eight** `su(3)` charges annihilate the forced state (residual `0`); its one-body
color matrix is exactly `I₃`. This is the occupancy-forced, second-quantized sharpening of
the representation-theoretic baryon singlet
([`CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02`](CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md),
under `CL3_COLOR_AUTOMORPHISM_THEOREM`). **"Singlet"/"neutrality"
language applies to this sector only.**

**(T2) Honest catch.** The exactly-full sector is **hopping-frozen** (the color-diagonal
hop annihilates it) — dynamically trivial.

**(T3) Closed-shell discharge (genuine many-body computation).** For the **named**
color-diagonal free hopping (`H = Σ_c h_spat ⊗ |c⟩⟨c|`; the framework's free hopping form,
the named surface linked above), when the per-color filling is a **closed shell** (non-degenerate
Fermi level — verified: many-body gap `3.0` in the runner's `L=3, n_f=1` instance), the
fixed-`N` ground state is **unique**, and the **measured** color-resolved one-body matrix
at every site — all nine entries, from the actual many-body ground state, nothing
hard-coded — has cross-color coherences **exactly zero** (`2.6×10⁻¹⁷`) and equal diagonal:
`ρ_color(x) = I₃/3` (`10⁻¹⁶`). **The ADM-2 necessary marginal condition holds in the
closed-shell sector with no extra measure/weight input** (necessary, not sufficient). This is a
property of the *named closed-shell sea*, **not** a claim about which state the physical
vacuum is. Consistent with the free-hopping context linked above: free dynamics cannot
*create* depolarization; here the closed-shell sea *is* depolarized and the free flow
conserves it.

**(T3b) Open-shell failure — the earned caveat, with finite `Z³` examples.** At a degenerate
Fermi level the forcing **fails**: the runner exhibits a state *in the degenerate ground
manifold* (degeneracy `20` in its instance) with per-color counts `(1.98, 1.21, 2.82)` and
`ρ_color(x) ≠ I₃/3` (dev `0.21`) **at the ground energy**. On finite cubic `Z³`
half-filling samples the runner documents Fermi-level degeneracies `12` at `L=3` and
`20` at `L=4`; the closed-shell discharge therefore does **not** cover those half-filled
seas. **The color-symmetric selection on the open-shell degenerate manifold is
an extra, weight-like condition: a named residual where the weight-dial guard re-opens. It
is not discharged here.**

**(T4) Discrete reduction — two conditions.** On **sharp-count** states (eigenstates of
the three color number operators — number/Cartan-diagonal eigenstates, the defensible
count reading), the color coherences vanish **exactly** (count selection rule), and
`ρ_color(x) = I₃/3` **iff** the registered color counts are **equal *and*** the per-color
local spatial profiles **agree**. Both teeth are exhibited (equal counts + unequal
profiles fails; unequal counts fails outright at dev `0.33`). The excitation residual of
(B)-purity thereby reduces from a continuous singlet/confinement admission to **two
discrete/derived-type conditions**. And — the earlier global-invariance example,
reproduced —
`ρ_color = I₃/3` is **strictly weaker** than global neutrality (`|F⟩ = Σ_i|i⟩|i⟩/√3` has
`ρ_A = I₃/3` with total `su(3)` charge residual `1.63`): this note forces only the
**marginal** condition, except at exact full filling (T1).

## The ledger for admission (B) after this note

```
orientation        previously separated by predictive equivalence
purity, closed-shell sectors   discharged here for the named free-hopping sea
purity, exact full filling     forced by Pauli (T1) — dynamically frozen (T2)
purity, open shells (documented finite Z³ half-filling instances)
                   NAMED RESIDUAL: the degenerate-manifold selection — weight-like,
                   weight-dial guard re-opens; NOT discharged
purity, excitations (sharp-count)
                   REDUCED to: count equality AND profile agreement (discrete)
```

## What this does NOT claim

- **No ADM-2 sufficiency** (the marginal condition is necessary only; the step-measure
  question is the mapped wall). **No confinement derivation.** **No claim about which
  state the physical vacuum is** (the staggered realization gate is the existing separate
  lane). The symmetric-base→physical-SM-color bridge boundary is inherited exactly as the
  baryon-singlet note records it; the supplied `C³` carrier conditionality as throughout.
- The open-shell residual is **not** minimized: it appears already in the checked finite
  `Z³` half-filled seas, and its resolution (a selection on the degenerate manifold) is
  exactly the kind of weight-like input the framework's weight-dial guard exists to
  police.
- No new axiom, primitive, measure, or weight is introduced. `r` is untouched (it lives in
  the generation factor; no part of this argument reaches it).

## Cross-references

- Admission split and marginal condition:
  [`COLOR_DEPOLARIZATION_ADM2_GATING_ADMISSIONS_COLLAPSE_TO_TWO_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_DEPOLARIZATION_ADM2_GATING_ADMISSIONS_COLLAPSE_TO_TWO_NARROW_THEOREM_NOTE_2026-06-09.md)
  and
  [`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md`](MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md).
- Orientation and purity residual context:
  [`COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md)
  and
  [`COLOR_PURITY_DOES_NOT_REDUCE_TO_PAST_HYPOTHESIS_SLOT_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_PURITY_DOES_NOT_REDUCE_TO_PAST_HYPOTHESIS_SLOT_NARROW_THEOREM_NOTE_2026-06-09.md).
- The representation singlet (sharpened by T1): [`CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02`](CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md)
- Free-hopping color conservation context:
  [`COLOR_EINSELECTION_MATTER_UNITARY_PRIMITIVITY_REQUIRES_BACKGROUND_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_EINSELECTION_MATTER_UNITARY_PRIMITIVITY_REQUIRES_BACKGROUND_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09.md).
- Pauli irrep support:
  [`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10`](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
- Standard math (method only): second quantization / Jordan–Wigner; Slater determinants;
  closed/open shells; number-operator selection rules.
