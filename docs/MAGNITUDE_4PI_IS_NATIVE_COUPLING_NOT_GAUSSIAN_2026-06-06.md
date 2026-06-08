# The Hierarchy Magnitude's 4π is the Native Coupling/Solid-Angle, Not the Gaussian 2π

**Date:** 2026-06-06
**Type:** boundary correction / status relocation
**Claim type:** bounded_theorem
**Status:** branch-local bounded. Corrects the status of the
`HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0` value gate: the per-mode magnitude factor is
the coupling normalization (4π = native d=3 lattice solid angle), not the Gaussian
path-integral measure (2π); the "native-2π / 2¹⁶-gap" reading was a conflation.
Sets no audit status; audit lane owns final classification.
`audit_required_before_effective_retained=true; bare_retained_allowed=false`.
**Runner:** [`scripts/magnitude_4pi_is_native_coupling_not_gaussian_2026_06_06.py`](../scripts/magnitude_4pi_is_native_coupling_not_gaussian_2026_06_06.py)
(`TOTAL: PASS=14 FAIL=0`).
**Cached log:** `logs/runner-cache/magnitude_4pi_is_native_coupling_not_gaussian_2026_06_06.txt`

## Background

The hierarchy magnitude is `v = M_Pl (7/8)^{1/4} alpha_LM^16`, with
`alpha_LM = alpha_bare/u_0`, `alpha_bare = g_bare^2/(4π) = 1/(4π)` (g_bare=1), so
the dominant suppression is `alpha_bare^16 = (4π)^-16 = 2.586e-18` (`u_0^-16` is
sub-decade, ~8.06). A prior 50-agent attack on this value gate concluded
NOT-closed, with the headline obstruction: *"the native per-mode factor is 2π
(real-Gaussian prefactor), not 4π; the genuinely-native 4π (Maradudin d=3 solid
angle) has multiplicity 1, not 16,"* and reduced the gate to the staggered-Dirac
realization gate. This note shows that verdict rests on two correctable errors.

## Statement (bounded theorem)

**(T1) The per-mode factor is the COUPLING normalization (4π), not the Gaussian
measure (2π).** The magnitude's per-factor is the coupling
`alpha_bare = g_bare^2/(4π)`, whose `4π` is the **d=3 solid angle** — the
normalization of the inverse `Z^3` graph-Laplacian (Poisson kernel)
`G(r) -> 1/(4π|r|)`. The runner re-derives the `4π` origin from the native `Z^3`
operator: the nearest-neighbor graph-Laplacian symbol `L(k) = 2 Σ_μ(1-cos k_μ) ->
|k|^2`, and the continuum inverse-Laplacian `FT[1/k^2] = 1/(4π r)` with the `4π`
the angular `∫dΩ = 4π` (assembled `r·G(r) = (4π/(2π)^3)(π/2) = 1/(4π) = 0.0796`).
This is the framework-applied Maradudin certificate
(`lattice_greens_function_maradudin_textbook_import_note`, **retained_bounded** —
a framework-local Fourier proof on the `Z^3` operator, "parallel provenance, not
imported authority"). The Gaussian path-integral measure `√(2π)/mode -> 2π` is a
**different object**; the magnitude uses the solid-angle `4π`, verified by:
`(4π)^-16 = 2.586e-18` (matches `v`), while `(2π)^-16` is off by **exactly
`2^16 = 65536`**. So the prior attack's "native 2π" was the path-integral measure,
not the magnitude's coupling factor.

**(T2) Exponent-as-COUNT dissolves the "multiplicity 1, not 16" objection.** The
exponent 16 is the native mode **count** (8 spatial `Z^3` corners × 2 temporal;
this session's `MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE` and
`MAGNITUDE_READS_MINIMAL_RECORD_BLOCK`). Hence `(4π)^-16 = (one native 4π)^(native
count 16)` — multiplicity 1 (one coupling normalization) raised to the native
count is identical to "16 separate factors." The demand for "16 distinct per-mode
solid-angle insertions" was a strictly stronger, false requirement.

**Therefore the value gate is NOT wall-blocked by a `2^16` native-2π gap, and does
NOT reduce to the staggered-Dirac realization gate via the magnitude's 4π.** The
4π is native d=3 geometry (retained_bounded), `g_bare=1` is retained, the exponent
16 is the native count. What the `(4π)^-16` magnitude still rides is a
readout/convention chain (T3), not a numeric gap.

## (T3) The honest residual (relocated, not closed)

The 4π geometry being native does not by itself derive the magnitude. The
`(4π)^-16` still rides, with verified live-ledger statuses:

| piece | role | status |
|---|---|---|
| `static_source_readout_i1_..._bridge` | the physical readout `V(r) = -C g^2 G(r)` links the coupling to the native `G(r)` | **unaudited — ADMITTED IMPORT** (its own text: "does **not** derive (P1) from the framework's one-qubit operator algebra"; it registers "the canonical lattice-gauge static-source linear-response readout") |
| `alpha_convention_i2_..._bridge` | `alpha := g^2/(4π)` | unaudited premise |
| `cl3_normalization_i3_..._bridge` | `Tr(T_a T_b)=δ/2` | unaudited premise |
| P3 (per-mode coupling dressing) | the substitution `u_0 -> alpha_LM` per mode | unaudited / admitted-open (`hierarchy_formula_honest_status` P3) |
| `g_bare ... L3a/L3b` | `g_bare=1` sub-lemmas | unaudited |

The **highest-leverage** piece is **I1**: an admitted import asserting the
framework's physical readout of the native `Z^3` Green's function is the static
potential. This is exactly the kind of "readout" the framework's **register-not-
read** principle governs — so the next attack is a *native* (register-not-read)
derivation of the I1 readout, replacing the import. That is the live frontier, and
it is a readout/import question, **not** a `2^16` numeric wall.

## Reconciliation with the 50-agent attack (it found real objects, mis-assembled)

The prior attack correctly identified both objects — the Gaussian `2π` and the
Maradudin `4π` (multiplicity 1) — but mis-assembled them: it treated the per-mode
magnitude factor as the path-integral measure (`2π`) and dismissed the `4π` for
"multiplicity 1." In fact the magnitude's per-factor **is** the coupling (`4π`,
solid angle), and multiplicity-1 raised to the native count is exactly `(4π)^-16`.
The reduction "to the staggered-Dirac realization gate via the magnitude 4π" was
an artifact of the `2π`-measure misreading; the genuine residual is the I1 readout
import (+ I2/I3/P3/L3a-b), all `unaudited`, none `retained_no_go`.

## What this note does NOT claim

- Does **not** close the value gate or derive `v`. The I1 static-source readout is
  an admitted import; P3 (per-mode dressing) and I2/I3 are admitted premises;
  `g_bare` L3a/L3b are unaudited. The gate rests on these.
- Does **not** claim the 4π's *coupling role* is native — only that the **4π
  geometry** (the d=3 solid angle / `Z^3` Poisson kernel) is native (retained_
  bounded), and that the magnitude uses the solid-angle 4π, not the Gaussian 2π.
- Does **not** upgrade any unaudited bridge; it relocates the residual and names
  I1 as the highest-leverage import.
- Sets no audit status.

## Load-bearing dependency and context references

- `lattice_greens_function_maradudin_textbook_import_note` (**retained_bounded**) —
  framework-applied `Z^3` Poisson-kernel `G(r)->1/(4π r)`; the native 4π (T1).
- `bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_note` (**retained_
  bounded**) — native BZ Haar `d^3k/(2π)^3`.
- `g_bare_forced_by_ward_rep_b_independence_abstract_narrow_theorem_note`
  (**retained**) — `g_bare=1`.
- `static_source_readout_i1_..._bridge` (**unaudited**, admitted import) — the I1
  readout; the relocated highest-leverage residual (T3).
- `alpha_convention_i2_...`, `cl3_normalization_i3_...` (**unaudited** premises);
  `hierarchy_formula_honest_status` (P3, admitted-open).
- `HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30` (**open_gate**) —
  the gate whose status this corrects.
- `MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06`,
  `MAGNITUDE_READS_MINIMAL_RECORD_BLOCK_2026-06-06` (bounded) — the exponent-as-
  count results used in T2.

## Forbidden imports check

- No PDG observed values consumed (`v`/`alpha_LM` appear only as labelled
  background, in no PASS condition).
- No new literature comparator adopted; the Maradudin 4π is the framework-applied
  retained_bounded certificate; the I1 readout is flagged as the existing admitted
  import (not newly introduced here).
- No fitted selectors; no new axiom or mechanism proposed.
- All cited statuses verified on the live ledger.

## Validation

`scripts/magnitude_4pi_is_native_coupling_not_gaussian_2026_06_06.py`
(`PASS=14 FAIL=0`): Section E1 (`(4π)^-16` matches; `(2π)^-16` off by exactly
`2^16`; `u_0^-16` sub-decade), Section N (native `Z^3` symbol `L(k)->k^2`; `4π` =
d=3 solid angle; assembled `r·G(r)=1/(4π)`; Gaussian 2π a distinct object,
`4π/2π=2`), Section E2 (`(4π)^-16 = (one 4π)^(count 16)`; multiplicity-1
dissolved), Section R (the residual chain: I1 import + I2/I3 + P3 + L3a/L3b).

## Reading rule

This note is the claim boundary for: the hierarchy magnitude's per-mode factor is
the coupling normalization `4π` (the native d=3 `Z^3` solid angle / Poisson
kernel), **not** the Gaussian measure `2π` (the prior attack's `2^16` gap was that
conflation); and `(4π)^-16 = (one native 4π)^(native count 16)` dissolves the
"multiplicity 1, not 16" objection. It does **not** close the gate: the
`(4π)^-16` magnitude rides the I1 static-source-readout import (+ I2/I3/P3/L3a-b).
The next path is a register-not-read native derivation of the I1 readout.
