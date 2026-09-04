---
claim_id: canonical_two_cell_context_c3_ew_instance_bounded_note_2026-07-02
claim_type: bounded_theorem
claim_scope: "Bounded support: defines a note-level canonical two-cell frame as the unit direction plus Hilbert-Schmidt orthocomplement inside a supplied finite-dimensional matrix *-algebra; verifies the landed C3 context and the M3 unit/traceless frame as exact instances; checks the common-factor identity and kappa-sensitive off-diagonal witness. This does not adopt the EW instance premise, set kappa_EW, close the EW kappa no-go, or import any sibling-PR result."
upstream_dependencies:
  - minimal_axioms
  - c3_generation_readout_context_canonical_definition_note_2026-07-02
  - ew_kappa_weighting_not_axiom_derivable_no_go_note_2026-06-09
runner: scripts/frontier_ctx_instantiation_canonical_two_cell_2026_07_02.py
---

# Canonical Two-Cell Contexts: C3 Instance And EW Instance Witnesses (Bounded Note)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Audit-status authority:** independent audit lane only. This note does not set,
predict, or estimate any audit verdict, and it edits no audit-lane-owned registry
or audit data file.
**Actual current surface status:** bounded support. The parent EW `kappa_EW`
no-go remains unchanged; no value of `kappa_EW` is claimed; no sibling PR result
is imported.
**Primary runner:**
[`scripts/frontier_ctx_instantiation_canonical_two_cell_2026_07_02.py`](../scripts/frontier_ctx_instantiation_canonical_two_cell_2026_07_02.py)
**Cached runner output:**
[`logs/runner-cache/frontier_ctx_instantiation_canonical_two_cell_2026_07_02.txt`](../logs/runner-cache/frontier_ctx_instantiation_canonical_two_cell_2026_07_02.txt)

## Firewall

- This is a note-level bounded theorem about a finite algebraic frame and two
  exact instance witnesses. It is not axiom, primitive, policy, or registry
  content.
- The parent EW no-go
  [`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md)
  remains standing: the approved axiom and primitive baseline supplies no
  weighting rule.
- The EW identification is a named instance premise with witnesses. Cardinality
  `8/9` is consistent with the `M_3` unit/traceless split, but cardinality alone
  does not supply the Hilbert-Schmidt cell structure.
- The note does not set `kappa_EW`, select an EW readout context, import sibling
  PR results, close or retire any wall, or adjudicate the parent lane.

## Supplied Surface

From
[`C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`](C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md):

- the singlet cell is the algebra unit direction `I`;
- the doublet cell is the Hilbert-Schmidt orthocomplement of the unit inside the
  circulant span, represented by `B=J-I`;
- `||I||^2=3`, `||B||^2=6`, and `<I,B>=0`;
- the outcome naming and channel naming are two namings of the same two cells of
  one context, with channel energies `(3a^2,6|b|^2)` equal to the registered
  weights `(a^2,2|b|^2)` up to a common factor `3`.

From
[`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md):

- the EW color readout uses `Pi_phys = C + kappa_EW S`;
- the central-sector partition gives the cardinality count `8/9`;
- that count does not pick the inter-sector weight `kappa_EW`.

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

- sites and possibilities are distinguished by supplied structure alone;
- readout value is determined by record content alone;
- scalar readout is additive on supplied finite pairwise-disjoint record
  collections.

## Canonical Two-Cell Frame

Given a supplied finite-dimensional matrix `*`-algebra with unit and
Hilbert-Schmidt inner product, the canonical two-cell frame considered here is:

1. the unit direction;
2. the Hilbert-Schmidt orthocomplement of the unit inside the supplied algebra.

This is a note-level definition for the bounded calculation below. It classifies
only supplied instances; it does not create a new framework axiom.

On the landed `C_3` context, the supplied algebra is the `hw=1` circulant span.
The frame is exactly the landed one: `I` and `B=J-I=U+U^2`, with exact
Hilbert-Schmidt data `||I||^2=3`, `||B||^2=6`, and `<I,B>=0`.
All six slot-relabeling permutation automorphisms fix `I` and preserve `B`.

## Common-Factor Identity

For the landed `C_3` naming equivalence, channel energies and registered weights
agree up to the common factor `3`:

`(3a^2,6|b|^2)=3(a^2,2|b|^2)`.

Therefore the equal-cell condition is invariant under the naming change:

`a^2 = 2|b|^2` iff `3a^2 = 6|b|^2`.

The runner checks this identity exactly on rational samples.

## EW Instance Witness

On `M_3(C)` with the Hilbert-Schmidt inner product, the same note-level frame is
the unit direction `I_3` and its traceless orthocomplement. Exact witnesses:

- `Tr(I_3)=3` and `||I_3||^2=3`;
- the traceless subspace has dimension `3^2-1=8`, witnessed by eight exact
  traceless matrices with rank `8` over `Q`;
- `I_3` is Hilbert-Schmidt orthogonal to that traceless subspace;
- the cardinality fraction is `8/9=(3^2-1)/3^2`;
- conjugation by the six `3x3` permutation matrices fixes `I_3`, preserves
  tracelessness, and preserves the Hilbert-Schmidt inner product.

This supports the named EW instance premise: if the EW readout context is
supplied as this `M_3` unit/traceless two-cell frame, it matches the parent's
`8/9` count and channel naming. The premise is not adopted here; it remains a
science/governance input.

## Kappa Consequence

For contents `(x_C,x_S)`, the normal-form expression
`Pi = x_C + kappa_EW x_S` is additive in the cell contents. At equal-cell-content
states, ratio readouts cancel the common `(1+kappa_EW)` factor. Off diagonal,
where `x_C != x_S`, the ratio is genuinely `kappa_EW`-sensitive.

This is a boundary statement only. It does not determine `kappa_EW`; it identifies
where a weighting rule would still be load-bearing.

## Residue Map

After this bounded support note, the remaining live content is:

1. whether the EW readout context is admitted or derived as the `M_3`
   unit/traceless instance;
2. any sibling class-result audits needed before downstream use;
3. the still-missing weighting rule for `kappa_EW`.

Those are science/audit/governance tasks outside this note.

## Does NOT

- Does not close the EW `kappa_EW` no-go or claim any value of `kappa_EW`.
- Does not adjudicate any sibling PR or import sibling results.
- Does not add an axiom, primitive, policy rule, or registry entry.
- Does not set, retag, or predict any audit status or effective status.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`](C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md)
- [`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md)

Context-only sibling surfaces are intentionally not dependency links.

## No-Promotion Statement

This note promotes nothing. It records exact finite algebra supporting a named EW
instance premise and leaves all status decisions to the independent audit lane.
