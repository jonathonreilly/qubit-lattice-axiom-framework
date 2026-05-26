# PMNS Oriented Cycle Selection Structure

**Date:** 2026-04-16 (2026-05-18: claim_scope formalized as bounded
conditional algebraic reduction of the oriented-cycle channel per
audit verdict boundary instruction; 2026-05-19: admitted-context
block + class-A retain — carrier and channel-value-law authorities
declared as explicit admitted imports, retained scope held to the
class-A finite algebraic identities the runner verifies; 2026-05-26:
raw-matrix rescope removes sole-axiom-free-point and graph-first
selected-axis readings from binding scope).
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-26 raw-matrix rescope):** the source-side
bounded content of this note is exactly the three **class-A finite algebraic
identities** verified by the runner:

- (CA-1) the exact `C_3` fixed locus on the oriented forward-cycle
  channel is `c_1 = c_2 = c_3 = sigma`, equivalently `A_fwd = sigma C`;
- (CA-2) on the specified identity block `I_3`, the oriented-cycle
  coefficients vanish exactly, so `sigma = 0` on that specified block;
- (CA-3) the residual swap-conjugation map `A_fwd ↦ P_23 A_fwd^dagger
  P_23` has fixed locus `c_1 = conjugate(c_3)`, `c_2` real, and a
  generic cycle triple is not fixed.

These are exact finite linear-algebra identities on `M_3(ℂ)`. The note
uses the upstream `pmns_oriented_cycle_channel_value_law_note` only for
the oriented-cycle channel/value-law authority. It does **not** load-bear
on (a) the identification of a sole-axiom free-point active block with
`I_3`, or (b) the identification of a graph-first selected-axis route with
the swap-conjugation antiunitary condition `A_fwd = P_23 A_fwd^dagger
P_23`. Those two readings are excluded interpretation targets, not
premises of this row. This is **explicitly NOT** a value-selection theorem.
**Status authority:** independent audit lane only.
**Status:** support - structural or confirmatory support note
**Script:** `scripts/frontier_pmns_oriented_cycle_selection_structure.py`

## 2026-05-26 raw-matrix rescope of the 2026-05-19 repair

This section supersedes the parts of the 2026-05-19 repair that treated
the sole-axiom-free-point and graph-first selected-axis readings as admitted
premises. They are no longer premises. The binding scope is the raw finite
matrix algebra the runner verifies.

### Dependency and excluded-interpretation block

The following boundaries are explicit so no reader can mistake context for a
result of this restricted packet:

- **Admitted import I-1 (carrier).** The oriented forward-cycle
  channel — i.e. the carrier on which `A_fwd = c_1 E_12 + c_2 E_23 +
  c_3 E_31` is meaningful as the load-bearing object — is **imported**.
  Its provenance is the upstream channel-value-law lane (see
  `PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`,
  audit row `pmns_oriented_cycle_channel_value_law_note`). The
  derivation of this carrier from primitives (sole axiom +
  retained-grade inputs) is NOT performed inside the present note.
- **Admitted import I-2 (channel-value-law authority).** The native
  oriented-cycle observable / value law that gives `A_fwd` its
  channel-level meaning — and against which any future value-selection
  law would be tested — is **imported** from the same upstream
  `pmns_oriented_cycle_channel_value_law_note` lane (currently
  `audited_clean` / `retained` on the independent audit lane). The
  present note's three class-A identities post-compose with that
  upstream channel law; they do not regenerate it.
- **Excluded interpretation E-1 (sole-axiom free-point active block =
  `I_3`).** Class-A check (CA-2) operates on the specified matrix `I_3`.
  This note does not claim that any sole-axiom free point has active block
  `I_3`, and that identification is not a premise of this row.
- **Excluded interpretation E-2 (graph-first ⇒ swap-conjugation
  antiunitary).** Class-A check (CA-3) computes the fixed locus of the
  prescribed antiunitary map `A_fwd = P_23 A_fwd^dagger P_23`. This note
  does not claim that the graph-first selected-axis route induces that map,
  and that identification is not a premise of this row.

### Class-A retain (exactly what stays retained)

The retained content of this note is exactly three class-A finite
algebraic identities on `M_3(ℂ)`, all verified by the registered
runner `scripts/frontier_pmns_oriented_cycle_selection_structure.py`:

1. **(CA-1) `C_3`-covariance fixed locus.** For `A_fwd = c_1 E_12 +
   c_2 E_23 + c_3 E_31` with `(c_1, c_2, c_3) ∈ ℂ^3`, conjugation by
   the projected cycle operator `C` sends `(c_1, c_2, c_3) ↦ (c_2,
   c_3, c_1)`. The fixed locus of this cyclic permutation on `ℂ^3`
   is the diagonal `{(sigma, sigma, sigma) : sigma ∈ ℂ}`, equivalently
   `A_fwd = sigma C`. Class-A finite linear-algebra identity.
2. **(CA-2) Identity-block vanishing.** The oriented-cycle coefficients
   of `I_3` (extracted by `oriented_cycle_coeffs_from_block`) are all
   exactly zero, so `sigma = 0` on `I_3`. Class-A finite arithmetic
   identity on a specified `3 × 3` matrix.
3. **(CA-3) Swap-conjugation antiunitary fixed locus.** The map
   `A_fwd ↦ P_23 A_fwd^dagger P_23` (with `P_23` the `(23)` permutation)
   restricted to the cycle channel has fixed locus exactly `c_1 =
   conjugate(c_3)`, `c_2` real, and a generic complex triple is not
   fixed. Class-A finite linear-algebra identity on `M_3(ℂ)`.

These three statements use the oriented-cycle channel/value-law authority
I-1/I-2 above and otherwise are pure finite-dimensional linear algebra over
`ℂ` on `M_3(ℂ)`. They do not require E-1 or E-2 as premises.

### Out-of-binding-scope (explicitly not retained)

The following readings of the same algebra are explicitly **not**
retained by this note:

- any claim that the sole axiom by itself derives a nontrivial cycle
  value or selects `sigma = 0` on physical grounds (CA-2 is an algebra
  fact on `I_3`, not a derivation of the active-block identification);
- any claim that the graph-first route physically forces `c_1 =
  conjugate(c_3)`, `c_2` real (CA-3 is a fixed-locus computation for a
  prescribed antiunitary map, not a derivation that that map is the
  graph-first reduction);
- any reading of CA-1 + CA-2 + CA-3 as a value-selection theorem on
  the oriented-cycle channel (the three statements only **structure**
  the channel; the value-selection law remains an open positive target).

### Honest scope-narrow audit trail

This 2026-05-26 repair is honest narrowing only. It keeps admitted imports
I-1/I-2 for the oriented-cycle channel/value-law authority, excludes E-1/E-2
from binding scope, and restricts the source-side bounded content to the
three class-A identities (CA-1)/(CA-2)/(CA-3) the runner verifies. It does
not change any algebraic equality or hand-authored audit verdict. The
source-side `claim_type = bounded_theorem` is unchanged; the independent
audit lane owns the refreshed `audit_status`.

## Question

Once the oriented forward cycle channel has an exact native observable/value
law, what exact selection structure remains on that channel?

## Answer

Three exact statements survive:

- exact `C_3` covariance collapses the cycle channel to one complex slot
  `sigma C`
- on the specified identity block `I_3`, `sigma = 0` on that exact
  `C_3`-covariant locus
- the prescribed residual swap-conjugation map reduces the cycle channel to
  the `3`-real subfamily
  `c_1 = conjugate(c_3)`, `c_2 real`

So the raw matrix structure of the oriented-cycle channel is fixed. Any
sole-axiom free-point or graph-first selected-axis interpretation is outside
this note.

## Exact chain

### 1. Exact `C_3` covariance

Write the oriented forward-cycle block as

`A_fwd = c_1 E_12 + c_2 E_23 + c_3 E_31`.

Conjugation by the projected cycle operator `C` permutes the coefficients
cyclically:

`(c_1, c_2, c_3) -> (c_2, c_3, c_1)`.

Therefore the exact `C_3`-fixed locus is

`c_1 = c_2 = c_3 = sigma`,

equivalently

`A_fwd = sigma C`.

### 2. Specified identity block

On the specified identity block `I_3`, the oriented-cycle coefficients vanish
exactly, so

`sigma = 0`.

This is a matrix identity on `I_3`, not a derivation that a sole-axiom
free point has active block `I_3`.

### 3. Prescribed swap-conjugation map

For the prescribed residual antiunitary map on the cycle channel,

`A_fwd = P_23 A_fwd^dagger P_23`.

Its fixed locus is

- `c_1 = conjugate(c_3)`
- `c_2` real

this map reduces the cycle channel from three complex coefficients to three
real parameters:

- `Re c_1`
- `Im c_1`
- `c_2`

## Consequence

This is not a full value-selection law. It does not yet derive the values from
`Cl(3)` on `Z^3` alone.

What it proves is the raw algebraic target any later interpretation would have
to use:

> any future nontrivial PMNS law using this prescribed cycle channel must
> select values on a `3`-real-dimensional fixed family once the
> swap-conjugation map is imposed.

## Boundary

This is a raw selection-structure note, not a closure theorem. Per the
2026-05-26 raw-matrix rescope, the bounded content is exactly the three
class-A finite algebraic identities (CA-1) / (CA-2) / (CA-3) verified by
the runner.

The oriented-cycle carrier / channel-value-law authority is imported from
the `pmns_oriented_cycle_channel_value_law_note` lane. The sole-axiom
free-point and graph-first selected-axis interpretations are excluded
targets, not premises.

It closes only the class-A finite algebraic identities listed in
§"2026-05-19 audit-conditional repair / Class-A retain":

- (CA-1) the exact `C_3`-fixed locus on the cycle channel is
  `c_1 = c_2 = c_3 = sigma`;
- (CA-2) on the specified block `I_3`, the oriented-cycle coefficients
  vanish exactly, so `sigma = 0` on `I_3`;
- (CA-3) the residual swap-conjugation map has fixed locus
  `c_1 = conjugate(c_3)`, `c_2` real, and a generic triple is not
  fixed.

It does **not** derive (a) the carrier, (b) the channel-value law,
(c) the sole-axiom free-point ⇒ `I_3` identification, (d) the
graph-first ⇒ swap-conjugation reduction, or (e) any nontrivial
cycle-value selection law. Items (a)/(b) come from the retained upstream
channel-value-law authority; (c)/(d) are excluded interpretation targets;
(e) is an open positive target outside this note's scope.

## Command

```bash
python3 scripts/frontier_pmns_oriented_cycle_selection_structure.py
```

## Audit dependency repair links

This graph-bookkeeping section records the explicit dependency link named by a
prior conditional audit so the audit citation graph can track it. It does not
promote this note or change the audited claim scope, which is now raw matrix
algebra on the C3-fixed locus and the prescribed residual swap-conjugation
fixed locus, given the imported channel-law authority.

One-hop authorities cited:

- [`pmns_oriented_cycle_channel_value_law_note`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  — currently `audited_clean` / `retained` (audit row:
  `pmns_oriented_cycle_channel_value_law_note`). This is the upstream
  retained authority for the native oriented-cycle observable / value law
  that the present note's selection-structure result post-composes with.

Excluded interpretation targets named by the 2026-05-05 audit verdict:

- The graph-first residual antiunitary condition `A_fwd = P_23 A_fwd^dag P_23`
  is no longer imported as a premise. The present row proves only the fixed
  locus of that prescribed map. A separate source note would be required to
  claim that a graph-first selected-axis route induces exactly this map.
- The sole-axiom free-point identification of the active block as the
  identity block `I_3` is no longer imported as a premise. The present row
  proves only that the specified matrix `I_3` has zero oriented-cycle
  coefficients. A separate source note would be required to identify any
  sole-axiom free point with that block.

Both open class D items match the 2026-05-05 audit verdict's
`notes_for_re_audit_if_any` field exactly:
"add a retained bridge proving the graph-first residual antiunitary
condition and the sole-axiom free-point identity block within the
restricted dependency chain."

## Honest auditor read

The 2026-05-05 audit recorded this row as `audited_conditional` with the
observation that the runner's A=8 algebraic checks (cyclic permutation
under C3, vanishing oriented-cycle coefficients on `I_3`, fixed locus of
the residual swap-conjugation map, generic-coefficient nonfixedness)
close on their own terms but are class A finite-dimensional algebra,
not first-principles derivations from the sole axiom. The cited upstream
authority `pmns_oriented_cycle_channel_value_law_note` is retained for
the native channel law, but the present note still imports the
graph-first residual antiunitary condition and the free-point identity-block
identification as premises not closed by the restricted packet. The cite
chain above now excludes those readings from binding scope without altering
the runner-checked content. The independent audit lane owns the refreshed
`audit_status`; this addendum only makes the source-side boundary explicit.

## Scope of this rigorization

This rigorization is class B (graph-bookkeeping citation) plus class D
(open-target registration). It does not change any algebraic content,
runner output, or load-bearing step classification. It records the
upstream authority the audit verdict expected and explicitly registers
the two open class D bridge-theorem targets named by the verdict's
`notes_for_re_audit_if_any` field. It mirrors the live cite-chain
pattern used by the
`DM_NEUTRINO_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md` cluster
(commit `8e84f0c23`).
