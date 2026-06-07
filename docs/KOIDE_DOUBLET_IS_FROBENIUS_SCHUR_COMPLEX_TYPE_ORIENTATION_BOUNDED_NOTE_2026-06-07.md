# The C₃ Generation Doublet Is Frobenius-Schur Complex Type — the r=1/2 vs r=1 Fork Is Faithful-Complex vs Realified (Orientation Correction + Obstruction)

**Date:** 2026-06-07
**Type:** bounded reframe + obstruction note (orientation correction; NOT a closure)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_koide_doublet_frobenius_schur_complex_type_exact.py`](../scripts/audit_companion_koide_doublet_frobenius_schur_complex_type_exact.py) (sympy, 10/10 exact)

## Result

The Koide `det_C`-vs-`det_R` fork (the `r = 1/2` vs `r = 1` reading of the C₃ generation doublet) is classified
by the **Frobenius-Schur indicator** of the doublet, and the classification fixes the orientation:

- The C₃ nontrivial irreps `ω, ω̄` are **Frobenius-Schur complex type** (`FS(ω) = FS(ω̄) = 0`, since `ω ≠ ω̄`).
  The real 2-dimensional "doublet" is the **realification of a complex-type irrep**. [runner (1)]
- Therefore the two readings are: the **faithful complex-type** reading (count the doublet as **one complex
  slot**, `ω̄ = conj(ω)` determined not independent) → `r = 1/2` (`Q = 2/3`); and the **realified** reading
  (count its **two real slots**) → `r = 1` (`Q = 1`, the native `log|det|` dimension-count value). [runner (2)]
- **Orientation:** `complex / holomorphic / Dirac ↔ r = 1/2` and `real / Majorana ↔ r = 1`. This matches the
  landed, runner-verified four-cell Berezin-fork table
  ([`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](./KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)),
  and is the **inverse** of a retracted attempt that asserted `det_C = Pfaffian = Majorana → r = 1/2`
  (closed/retracted; it inverted the mapping). [runner (2c)]

## This is an orientation correction, not a closure

`FS = 0` (complex type) plus the complex `M₂(ℂ)` carrier (Quantum axiom) are **necessary but not sufficient**
to force `r = 1/2`:

- The native flavor complex structure `J_cs = (C − C²)/√3` is a genuine complex structure on the doublet
  (`J_cs² = −P_doublet`) **but commutes with the entire K/CPT-real mass family** `H = aI + bC + b̄C²`
  (`[J_cs, H] = 0`). It is therefore **measure-neutral** — silent on `r`, unable to select the faithful-complex
  reading over the realified one. [runner (3)]
- So the **selector is dynamical**, not static structure. Which reading is realized is the open
  `AC_φλ` staggered-realization gate (`staggered_dirac_realization_gate_note_2026-05-03`, Tier-A). This note does
  **not** derive `r = 1/2`; it only fixes the orientation (excluding the inverted reading) and records the
  measure-neutrality obstruction.

## Why this is worth recording

A prior attempt to close this lever asserted the **inverted** reality-type mapping (`Majorana ↔ r = 1/2`) and was
adversarially refuted and retracted. This note lands the **correct, Frobenius-Schur-grounded** orientation so the
inverted framing is not re-walked: for the C₃ doublet, `r = 1/2` is the faithful **complex** (1-slot) reading and
`r = 1` is the realified (2-slot) reading — and neither is forced by the static structure (`J_cs` measure-neutral).

## Scope — what this is and is not

- **Is:** a reproven classification (the doublet is FS-complex) + the correctly-oriented fork + the
  measure-neutrality obstruction. A bounded reframe/obstruction record.
- **Is not:** a derivation of `r = 1/2`; a claim that the realified (`r = 1`) reading is forbidden (it is the
  native `log|det|` value and remains admissible pending the selector); a new axiom, primitive, or admission;
  a statement about the **neutrino** sector (electrically neutral; outside this note).
- **Open residual:** the dynamical selector (does the realized generation kinetic readout count the FS-complex
  doublet once or twice?) = the `AC_φλ` gate.

## Forbidden-import / reprove-and-cite discipline

- The Frobenius-Schur indicators, the realification statement, the Koide arithmetic `Q = 1/3 + (2/3)r`, and the
  `[J_cs, H] = 0` measure-neutrality are **reproven** from the C₃ primitive in the runner (sympy, 10/10 exact).
- The **Frobenius-Schur indicator theorem** and the `Majorana ↔ real` / `Dirac ↔ complex` (Berezin polarization)
  correspondence are **comparators** only — named for provenance and cross-check, never derivation inputs.
- No PDG values appear; `Q = 2/3` (empirical) and `Q = 1` (realified value) are named as targets, not derived.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](./KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
- [`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](./KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
- [`FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md`](./FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](./STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)

**Independent audit required.** This note asserts no effective-status change.
