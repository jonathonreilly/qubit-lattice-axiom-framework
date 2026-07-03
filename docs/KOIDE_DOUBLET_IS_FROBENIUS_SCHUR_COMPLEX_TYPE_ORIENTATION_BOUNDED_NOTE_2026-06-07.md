# The C₃ Generation Doublet Is Frobenius-Schur Complex Type — the r=1/2 vs r=1 Fork Is Complex-Type vs Realified Readout (Orientation Correction + Obstruction)

**Date:** 2026-06-07
**Type:** bounded reframe + obstruction note (orientation correction; NOT a closure)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_koide_doublet_frobenius_schur_complex_type_exact.py`](../scripts/audit_companion_koide_doublet_frobenius_schur_complex_type_exact.py) (sympy, 12/12 exact)
**Cached output:** [`logs/runner-cache/audit_companion_koide_doublet_frobenius_schur_complex_type_exact.txt`](../logs/runner-cache/audit_companion_koide_doublet_frobenius_schur_complex_type_exact.txt)

## Result

The Koide `det_C`-vs-`det_R` fork (the `r = 1/2` vs `r = 1` reading of the C₃ generation doublet) splits into a
**Frobenius-Schur classification** (a reproven fact) and a **readout selection** (the open gate):

- The C₃ nontrivial irreps `ω, ω̄` are **Frobenius-Schur complex type** (`FS(ω) = FS(ω̄) = 0`, since `ω ≠ ω̄`).
  The real 2-dimensional "doublet" is the **realification of a complex-type irrep**. [runner (1)]
- The Koide lever `Q = 1/3 + (2/3) r` (`r = |b|²/a²`) is **reproven from the C₃ circulant spectrum**
  `λ_k = a + 2|b|cos(δ + 2πk/3)` via `Q = (Σλ_k²)/(Σλ_k)²`. [runner (2a)–(2c)]
- The two **readouts** of the same circulant — the **complex-type / holomorphic readout** (the doublet as
  **one complex slot**, `ω̄ = conj(ω)` determined not independent) and the **realified / dimension-count
  readout** (its **two real slots**) — map to `r = 1/2` (`Q = 2/3`) and `r = 1` (`Q = 1`, the native
  `log|det|` value) respectively. The **slot-count → r mapping is the landed Berezin-fork table's** (cited
  below), **not reproven here**; runner (2d),(2e) check only the resulting arithmetic `Q(1/2)=2/3`, `Q(1)=1`.
- **Orientation.** The landed, runner-verified four-cell Berezin-fork table
  ([`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](./KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md))
  maps `holomorphic / Dirac ↔ r = 1/2` and `real / Majorana ↔ r = 1`. The Frobenius-Schur **complex** typing
  establishes the doublet is **not** a real/self-conjugate (`FS = +1`) irrep. This rules out the **inverted**
  `Majorana → r = 1/2` reading of a retracted attempt (`det_C = Pfaffian = Majorana → r = 1/2`,
  closed/retracted). It does **not** rule out the **realified / Majorana → `r = 1`** cell of the Berezin table
  (the admissible realification of the complex-type irrep, = the native `log|det|` value); that cell remains
  open pending the selector. The FS typing does **not** by itself prove `r = 1/2` is selected. [runner (1),(2)]

## This is an orientation correction, not a closure

**Bottom line:** `r = 1/2` is a **registered (admitted) pattern, not forced by the minimal axioms** — the
`(1,1)`-vs-`(1,2)` readout selection is the open `AC_φλ` gate, and the framework's native `log|det|` /
second-order modulus reading gives `r = 1`. This note only fixes the **reality-type orientation** of the fork
(ruling out the inverted `Majorana → r = 1/2` reading); it does **not** select `r = 1/2`.

`FS = 0` (complex type) plus the complex `M₂(ℂ)` carrier (Quantum axiom) are **necessary but not sufficient**
to force `r = 1/2`:

- The native flavor complex structure `J_cs = (C − C²)/√3` is a genuine complex structure on the doublet
  (`J_cs² = −P_doublet`) **but commutes with the entire K/CPT-real mass family** `H = aI + bC + b̄C²`
  (`[J_cs, H] = 0`). It is therefore **measure-neutral** — silent on `r`, unable to select the complex-type /
  holomorphic readout over the realified one. [runner (3)]
- So the **selector is dynamical**, not static structure. Which reading is realized is the open
  `AC_φλ` staggered-realization gate (`staggered_dirac_realization_gate_note_2026-05-03`, Tier-A). This note does
  **not** derive `r = 1/2`; it only fixes the orientation (excluding the inverted reading) and records the
  measure-neutrality obstruction.

## Bounded/no-go discipline

- **N1 routes.** The note tests the faithful complex-type route, the realified
  readout route, the Koide lever arithmetic, the static flavor complex
  structure `J_cs`, and the inverted Majorana-to-`r=1/2` reading. The first
  two remain allowed readings, the arithmetic matches the existing fork table,
  `J_cs` is measure-neutral, and the inverted reading is ruled out.
- **N2 wall independence.** The only live wall is the selector wall: which
  readout is realized. It is not split into independent wall counts.
- **N3 hidden-wall scan.** The slot-count-to-`r` bridge is explicitly cited to
  the landed Berezin-fork table; this runner checks arithmetic and
  Frobenius-Schur type, not that bridge.
- **N4 residual matching.** The residual is exactly readout selection
  (`complex-type/holomorphic` versus `realified/dimension-count`), not the
  existence of the complex-type doublet.
- **N5 rhetoric audit.** The note does not say `r=1/2` is forced, and it does
  not forbid the realified `r=1` reading.
- **N6 partial closure.** A future selector theorem can still close the gate by
  deriving which readout the realized staggered generation carrier records.
- **N7 steelman.** A reader could argue that complex type should select the
  holomorphic readout by default. The exact commutation `[J_cs,H]=0` defeats
  that as a static proof because the complex structure is measure-neutral.
- **N8 cross-cycle echo.** This matches the repository's r-dial posture:
  `r=1/2` is a real candidate outcome, not an exclusive value forced by the
  current static algebra.

## Why this is worth recording

A prior attempt to close this lever asserted the **inverted** reality-type mapping (`Majorana ↔ r = 1/2`) and was
adversarially refuted and retracted. This note lands the **correct, Frobenius-Schur-grounded** orientation so the
inverted framing is not re-walked: for the C₃ doublet, `r = 1/2` is the **complex-type / holomorphic** (1-slot)
readout and `r = 1` is the **realified / dimension-count** (2-slot) readout — and neither is forced by the static
structure (`J_cs` measure-neutral).

## Scope — what this is and is not

- **Is:** a reproven classification (the doublet is FS-complex) + the correctly-oriented fork + the
  measure-neutrality obstruction. A bounded reframe/obstruction record.
- **Is not:** a derivation of `r = 1/2`; a claim that the realified (`r = 1`) reading is forbidden (it is the
  native `log|det|` value and remains admissible pending the selector); a new axiom, primitive, or admission;
  a statement about the **neutrino** sector (outside this note's scope).
- **Open residual:** the dynamical selector (does the realized generation kinetic readout count the FS-complex
  doublet once or twice?) = the `AC_φλ` gate.

## Forbidden-import / reprove-and-cite discipline

- The Frobenius-Schur indicators, the realification statement, the Koide lever `Q = 1/3 + (2/3)r` (**derived from
  the C₃ circulant spectrum** `λ_k = a + 2|b|cos(δ + 2πk/3)` via `Q = (Σλ_k²)/(Σλ_k)²`, not asserted), and the
  `[J_cs, H] = 0` measure-neutrality are **reproven** from the C₃ primitive in the runner (sympy, 12/12 exact).
- The **Frobenius-Schur indicator theorem** and the `Majorana ↔ real` / `Dirac ↔ complex` (Berezin polarization)
  correspondence are **comparators** only — named for provenance and cross-check, never derivation inputs. The
  `holomorphic ↔ r=1/2` / `Majorana ↔ r=1` orientation is the landed Berezin-fork table's; this note cross-checks
  consistency with it, it does not re-derive the table.
- No PDG values appear; `Q = 2/3` (empirical) and `Q = 1` (realified value) are named as targets, not derived.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](./KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
- [`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](./KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
- [`FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md`](./FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](./STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)

**Independent audit required.** This note asserts no effective-status change.
