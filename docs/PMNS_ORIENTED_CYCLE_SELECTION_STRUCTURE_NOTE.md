# PMNS Oriented Cycle Selection Structure

**Date:** 2026-04-16 (2026-05-18: claim_scope formalized as bounded
conditional algebraic reduction of the oriented-cycle channel per
audit verdict boundary instruction; 2026-05-19: admitted-context
block + class-A retain — carrier and channel-value-law authorities
declared as explicit admitted imports, retained scope held to the
class-A finite algebraic identities the runner verifies).
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-19 narrowing):** the **retained** content
of this note is exactly the three **class-A finite algebraic
identities** verified by the runner:

- (CA-1) the exact `C_3` fixed locus on the oriented forward-cycle
  channel is `c_1 = c_2 = c_3 = sigma`, equivalently `A_fwd = sigma C`;
- (CA-2) on the identity block `I_3`, the oriented-cycle coefficients
  vanish exactly, so `sigma = 0` on that block;
- (CA-3) the residual swap-conjugation map `A_fwd ↦ P_23 A_fwd^dagger
  P_23` has fixed locus `c_1 = conjugate(c_3)`, `c_2` real, and a
  generic cycle triple is not fixed.

These are exact finite linear-algebra identities on `M_3(ℂ)`. The note
does **NOT** retain (a) the carrier / oriented-cycle channel itself,
(b) the upstream native observable / value law on that channel, (c)
the identification of the sole-axiom free-point active block as the
identity block `I_3`, or (d) the identification of the graph-first
selected-axis route with the residual antiunitary condition `A_fwd =
P_23 A_fwd^dagger P_23`. Items (a) and (b) (collectively "carrier +
channel-value-law authority") are **admitted imports** from the
upstream `pmns_oriented_cycle_channel_value_law_note` lane. Items (c)
and (d) are **admitted premises** registered as open class D bridge
targets (see §"2026-05-19 audit-conditional repair" below). This is
**explicitly NOT** a retained value-selection theorem and does not
purport to derive the carrier or channel-value law from primitives.
**Status authority:** independent audit lane only.
**Status:** support - structural or confirmatory support note
**Script:** `scripts/frontier_pmns_oriented_cycle_selection_structure.py`

## 2026-05-19 audit-conditional repair: admitted-context block + class-A retain

This section is the load-bearing repair record. It does not change any
algebraic content of the chain below, the runner output, or any
runner-checked numerical equality. It tightens the language so that
two previously-implicit load-bearing imports are **explicit admitted
context**, and locks the retained scope to the class-A finite
algebraic identities the runner actually verifies.

### Admitted-context block (explicit imports)

The following are **not derived in this note**. They are imported as
admitted context from the surrounding oriented-cycle channel chain
and are flagged explicitly here so no reader can mistake them for
results retained by this note's restricted packet:

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
- **Admitted premise P-1 (sole-axiom free-point active block = `I_3`).**
  The identification of the active block at the sole-axiom free point
  with the identity block `I_3` is **a premise**, not a theorem of this
  note. Class-A check (CA-2) operates on `I_3` as data; promoting (CA-2)
  beyond a class-A identity on `I_3` would require a retained source
  note proving that the sole-axiom free point really has active block
  equal to `I_3`. This is the open class D bridge listed below.
- **Admitted premise P-2 (graph-first ⇒ swap-conjugation antiunitary).**
  The identification of the graph-first selected-axis route with the
  residual antiunitary condition `A_fwd = P_23 A_fwd^dagger P_23` is
  **a premise**, not a theorem of this note. Class-A check (CA-3)
  computes the fixed locus of this prescribed antiunitary map on
  `M_3(ℂ)`; it does not show that the graph-first route induces
  exactly this map. Promoting (CA-3) beyond a class-A identity on a
  prescribed antiunitary involution would require a retained source
  note proving the graph-first ⇒ swap-conjugation reduction. This is
  the second open class D bridge listed below.

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

These three statements are all **conditional on the imports I-1,
I-2, P-1, P-2 above**. They are pure finite-dimensional linear
algebra over `ℂ` on `M_3(ℂ)`; nothing about them depends on first-
principles physical content beyond the admitted carrier and the
admitted premises.

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

This 2026-05-19 repair is honest narrowing only. It (a) makes admitted
imports I-1, I-2 and admitted premises P-1, P-2 explicit in the
boundary block, (b) restricts the **retained** content of the note to
the three class-A identities (CA-1)/(CA-2)/(CA-3) the runner verifies,
and (c) preserves the prior route history (the §"Audit dependency
repair links" and §"Honest auditor read" sections below remain
unchanged). It does NOT change any algebraic content, runner output,
runner-checked equality, or audit-data row. The note's `audit_status`
and `claim_type = bounded_theorem` are unchanged by this repair.

## Question

Once the oriented forward cycle channel has an exact native observable/value
law, what exact selection structure remains on that channel?

## Answer

Three exact statements survive:

- exact `C_3` covariance collapses the cycle channel to one complex slot
  `sigma C`
- at the sole-axiom free point, `sigma = 0`, so the sole axiom selects only the
  trivial cycle law on that exact `C_3`-covariant locus
- on the graph-first selected-axis route, the residual antiunitary symmetry
  reduces the cycle channel to the `3`-real subfamily
  `c_1 = conjugate(c_3)`, `c_2 real`

So the carrier and observable law are closed, and the remaining gap is only a
value-selection law on that reduced channel.

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

### 2. Sole-axiom free point

At the sole-axiom free point, the active block is the identity block `I_3`.
Its oriented-cycle coefficients vanish exactly, so

`sigma = 0`.

Therefore the sole axiom by itself does not select a nontrivial cycle value on
the exact `C_3`-covariant locus.

### 3. Graph-first selected-axis route

On the graph-first route, the strongest exact residual antiunitary reduction on
the cycle channel is

`A_fwd = P_23 A_fwd^dagger P_23`.

Its fixed locus is

- `c_1 = conjugate(c_3)`
- `c_2` real

So the graph-first selected-axis route reduces the cycle channel from three
complex coefficients to three real parameters:

- `Re c_1`
- `Im c_1`
- `c_2`

## Consequence

This is not a full value-selection law. It does not yet derive the values from
`Cl(3)` on `Z^3` alone.

What it does prove is that the remaining positive target is no longer vague:

> any future nontrivial retained PMNS law must select values on the reduced
> oriented-cycle channel, and on the graph-first route that channel is already
> only `3` real dimensional.

## Boundary

This is a selection-structure note, not a closure theorem. Per the
2026-05-19 admitted-context repair, the retained content is exactly
the three class-A finite algebraic identities (CA-1) / (CA-2) / (CA-3)
verified by the runner. All three are **conditional on the admitted
imports declared above**:

- the **carrier** (admitted import I-1) and the **upstream
  channel-value-law authority** (admitted import I-2) — both imported
  from the `pmns_oriented_cycle_channel_value_law_note` lane and NOT
  derived inside this note;
- the **sole-axiom free-point ⇒ `I_3`** identification (admitted
  premise P-1) and the **graph-first ⇒ swap-conjugation antiunitary**
  identification (admitted premise P-2) — both registered as open
  class D bridge targets below.

It closes only the class-A finite algebraic identities listed in
§"2026-05-19 audit-conditional repair / Class-A retain":

- (CA-1) the exact `C_3`-fixed locus on the cycle channel is
  `c_1 = c_2 = c_3 = sigma`;
- (CA-2) on the block `I_3`, the oriented-cycle coefficients vanish
  exactly, so `sigma = 0` on `I_3`;
- (CA-3) the residual swap-conjugation map has fixed locus
  `c_1 = conjugate(c_3)`, `c_2` real, and a generic triple is not
  fixed.

It does **not** derive (a) the carrier, (b) the channel-value law,
(c) the sole-axiom free-point ⇒ `I_3` identification, (d) the
graph-first ⇒ swap-conjugation reduction, or (e) any nontrivial
cycle-value selection law. Items (a)/(b) are admitted imports from
upstream; (c)/(d) are open class D bridge targets; (e) is an open
positive target outside this note's scope.

## Command

```bash
python3 scripts/frontier_pmns_oriented_cycle_selection_structure.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope, which remains conditional algebra on the C3-fixed locus and the residual swap-conjugation fixed locus given the imported channel-law authority and the imported sole-axiom free-point and graph-first residual-antiunitary premises.

One-hop authorities cited:

- [`pmns_oriented_cycle_channel_value_law_note`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  — currently `audited_clean` / `retained` (audit row:
  `pmns_oriented_cycle_channel_value_law_note`). This is the upstream
  retained authority for the native oriented-cycle observable / value law
  that the present note's selection-structure result post-composes with.

Open class D registration targets named by the 2026-05-05 audit verdict
as `missing_bridge_theorem`:

- The graph-first residual antiunitary condition `A_fwd = P_23 A_fwd^dag P_23`
  is imported as a premise, not derived inside the present note's restricted
  packet. Closing it would require a retained source note proving that the
  graph-first selected-axis route induces exactly this residual antiunitary
  reduction on the oriented forward-cycle channel.
- The sole-axiom free-point identification of the active block as the
  identity block `I_3` is imported as a premise, not derived inside the
  present note. Closing it would require a retained source note proving
  that at the sole-axiom free point the active block is exactly `I_3`,
  which then forces `sigma = 0` on the C3-covariant locus.

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
chain above wires those premises as explicit open class D registration
targets without altering the runner-checked content. Effective status
remains `audited_conditional`. The note's `audit_status` is unchanged by
this addendum.

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
