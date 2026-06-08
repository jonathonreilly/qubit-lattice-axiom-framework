# The I1 Static-Source Readout is Native Field-Integration, Not a Standalone Import

**Date:** 2026-06-06
**Type:** reframe / import relocation
**Claim type:** bounded_theorem
**Status:** branch-local bounded. Reframes the I1 static-source-readout admitted
import (the highest-leverage residual of the hierarchy magnitude per
`MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN_2026-06-06`) as native
field-integration read via register-not-read. RELOCATES, does not eliminate, the
readout bridge. Sets no audit status; audit lane owns final classification.
`audit_required_before_effective_retained=true; bare_retained_allowed=false`.
**Runner:** [`scripts/i1_static_readout_is_native_field_integration_2026_06_06.py`](../scripts/i1_static_readout_is_native_field_integration_2026_06_06.py)
(`TOTAL: PASS=10 FAIL=0`).
**Cached log:** `logs/runner-cache/i1_static_readout_is_native_field_integration_2026_06_06.txt`

## Background

The hierarchy magnitude's coupling `alpha_bare = g^2/(4π)` rides the **I1** bridge
(`STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE`, unaudited), which registers as
an **admitted import** "the canonical lattice-gauge static-source linear-response
readout": `W(R,T) ~ exp(-V(R) T)`, with `V(R)` identified at leading order with
the gauge-propagator (graph-Laplacian Green's function) on `Z^3`. Its own text:
the bridge "does **not** derive (P1) from the framework's one-qubit operator
algebra." `MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN` named I1 the
highest-leverage residual and flagged it as a candidate for a register-not-read
native readout. This note takes that run.

## Statement (bounded theorem)

**(T1) I1's content is the standard native field-integration result.** Integrating
out the framework's quadratic (leading-order) gauge field — kinetic term the `Z^3`
graph-Laplacian — coupled to two static sources gives, by completing the square,
the interaction `V(r) = -g^2 G(r)` **exactly**, where `G` is the inverse `Z^3`
graph-Laplacian. The runner verifies `V(r)` is exactly `-g^2 G(r)` (the
interaction *is* the gauge propagator). In the massless limit `G(r) -> 1/(4π r)`
(the native solid angle, via `L(k)->|k|^2` and the inverse-Laplacian
decomposition; cf. `MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN`,
`lattice_greens_function_maradudin_textbook_import_note` **retained_bounded**), so
`V(r) -> -g^2/(4π r) = -alpha_bare/r` with `alpha_bare = g^2/(4π) = 1/(4π)`
(`g_bare=1`, **retained**). This is the textbook Coulomb-from-field-integration —
no lattice-gauge linear-response convention is imported; it is the exact
consequence of the native quadratic field + native Green's function.

**(T2) The interaction lives in the field, read via register-not-read — not a
lattice-gauge convention.** A sharp adversarial point: A3's finite-additivity over
**disjoint** records gives `I = I_1 + I_2`, with **no** `r`-dependence — so the
static potential is *not* a readout-additivity quantity. The runner confirms the
`r`-dependent `V(r)` cannot be an additive readout of disjoint sources. Instead the
interaction is carried by the **field** coupling the sources; register-not-read
registers the realized **sourced-field config's energy**, which includes that field
interaction `= -g^2 G(r)`. So I1's "static-source readout" is the **registered
energy of the native sourced-field configuration** — the framework's general
energy readout applied to the native gauge field — not a separate lattice-gauge
import.

## (T3) Honest scope — this RELOCATES I1, it does not eliminate the readout bridge

The reframe trades the **standalone lattice-gauge import** for native
field-integration **plus the framework's general energy-readout bridge**. What it
rests on (with live-ledger statuses):

| piece | status |
|---|---|
| field-integration `->` `V(r)=-g^2 G(r)` (complete the square) | native (this runner; exact) |
| gauge propagator `=` inverse `Z^3` graph-Laplacian `-> 1/(4π r)` | **retained_bounded** (Maradudin framework-applied) |
| `W~exp(-VT)` large-`T` decay `=` lowest energy | **retained_bounded** (RP two-step transfer matrix) |
| Kubo leading-order linear response | **retained_bounded** (`linear_response_true_kubo_note`) |
| energy readout `=` field-integrated energy | **Observable-Principle / register-not-read bridge** (framework-wide non-axiom parent — *substituted for* I1, not eliminated) |
| Casimir `C` | computable (retained Casimir rows) |
| quadratic source normalization | exact support in `I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08` |

So the **standalone** I1 import (the lattice-gauge static-source linear-response
convention) is **eliminated** — folded into native field-integration + the general
energy-readout bridge + retained pieces. The residual is the **general** energy
readout (used framework-wide for masses, not specific to this) + Casimir + leading
order — not a standalone import. This is a relocation to more-native, framework-
wide machinery, **not** a from-nothing closure of the readout itself.

## 2026-06-08 Native Quadratic Source-Normalization Bridge

The native field-integration half of this relocation now has a restricted
finite-lattice bridge:

[`I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md`](I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md)

That bridge proves, on the zero-mean finite periodic lattice, that the leading
quadratic gauge-source action

```text
S[phi; J] = (1/(2 g^2)) <d phi, d phi> - <J, phi>
```

has stationary equation `L phi = g^2 J` and completed-square effective action

```text
S_eff[J] = -(g^2/2) <J, L^+ J>.
```

For two static source records this gives the separation-dependent cross term
`V_cross(r) = -g^2 s_1 s_2 G(r)`, with exact source-amplitude and `g^2`
scaling. This removes the native quadratic gauge-source action/normalization as
a standalone convention inside the I1 packet.

The general energy-readout bridge remains open. This update narrows the I1
residual; it does not promote the row or claim full retained closure.

## Honest meta-note (for the audit lane)

This is the 4th register-not-read-flavored result in this session's magnitude arc
(`MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE`, `MAGNITUDE_READS_MINIMAL_RECORD_BLOCK`,
`MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN`, and this). They share a pattern:
*the record registers X (a count, the minimal block, the field energy); the
continuum / convention / standalone import is a reconstruction.* Each is bounded on
the register-not-read principle (`record_outcome_observable_principle_canonical_
proposal_note`, meta) extended to a new domain. The audit lane should weigh these
register-not-read applications **together** — whether the principle genuinely
extends to readout-scale, mode-count, and source-readout, or is being
over-applied. This note flags that explicitly rather than presenting the
relocation as settled.

## What this note does NOT claim

- Does **not** close the hierarchy magnitude or derive `v`. P3 (per-mode coupling
  dressing), the energy-readout bridge, Casimir, and `u_0` (sub-decade) remain.
- Does **not** eliminate the energy-readout bridge — it substitutes the framework's
  general Observable-Principle readout for the standalone lattice-gauge import.
- Does **not** assert the native quadratic gauge action beyond its leading-order
  (plaquette-expansion) form; higher orders are not addressed.
- Sets no audit status.

## Load-bearing dependency and context references

- `STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE` (**unaudited**, admitted
  import) — the import this reframes.
- `lattice_greens_function_maradudin_textbook_import_note` (**retained_bounded**) —
  the native `Z^3` Green's function `G(r)->1/(4π r)` (the gauge propagator).
- `axiom_first_rp_two_step_transfer_matrix_positivity` (**retained_bounded**) —
  the `W~exp(-VT)` large-`T` decay.
- `linear_response_true_kubo_note` (**retained_bounded**) — Kubo linear response.
- `g_bare_forced_by_ward_rep_b_independence_abstract_narrow_theorem_note`
  (**retained**) — `g_bare=1`.
- `record_outcome_observable_principle_canonical_proposal_note` (**meta**) — the
  register-not-read / energy-readout principle (T2, T3).
- `MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN_2026-06-06` (bounded) — names I1
  the highest-leverage residual; this attacks it.

## Forbidden imports check

- No PDG observed values consumed (`alpha_bare`/`v` appear only as labelled
  background, in no PASS condition).
- No NEW import introduced; the result **removes** a standalone import (I1) by
  folding it into native field-integration + the framework's existing readout
  bridge. Kubo / RP / Maradudin are the existing retained_bounded pieces.
- No fitted selectors; no new axiom or mechanism proposed.
- All cited statuses verified on the live ledger.

## Validation

`scripts/i1_static_readout_is_native_field_integration_2026_06_06.py`
(`PASS=10 FAIL=0`): Section A (integrate out the native quadratic field ->
`V(r) = -g^2 G(r)` exactly; the interaction is the propagator), Section B (the
`r`-dependent interaction is NOT additive-over-disjoint-sources -> it is the
registered energy of the coupled field config), Section C (massless limit
`r·G(r) -> 1/(4π)` analytically; `V(r) -> -alpha_bare/r`, `alpha_bare = g^2/(4π)`),
Section R (the relocation residual: native field-integration + general
energy-readout bridge + native G + RP + Kubo + Casimir + leading order).

## Reading rule

This note is the claim boundary for: I1's static-source readout content is the
exact native field-integration result (`V(r) = -g^2 G(r) -> -alpha_bare/r`, native
4π), read via register-not-read as the registered energy of the native
sourced-field configuration — eliminating the **standalone** lattice-gauge import
by folding it into native field-integration + the framework's general
energy-readout bridge. It does **not** close the magnitude (the energy-readout
bridge, P3, Casimir, `u_0` remain) and flags itself as one of four register-not-
read applications the audit lane should weigh together.
