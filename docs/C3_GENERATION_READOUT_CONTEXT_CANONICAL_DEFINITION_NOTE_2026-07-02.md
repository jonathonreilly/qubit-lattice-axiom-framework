# The Canonical C_3 Generation Readout Context — Definition

**Date:** 2026-07-02
**Type:** meta (definition; labeling-convention ratification)
**Claim type:** meta
**Status authority:** independent audit lane only. This note sets no audit
status and predicts no audit outcome. The ratification below is effective only
upon owner approval recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md`.

## Purpose

Two landed surfaces describe a two-cell structure on the supplied `hw=1`
circulant class and use different cell names for it. This note fixes the
canonical object once, so that later notes cite one definition instead of
re-establishing the identification pairwise.

## Definition

The **canonical `C_3` generation readout context** is the supplied readout
context on the `hw=1` generation factor (identified with `C^3`, cyclic shift
`U`, supplied circulant class `Y = a I + b U + conj(b) U^{-1}`) whose two cells
are:

1. the **singlet cell**: the algebra unit direction `I`;
2. the **doublet cell**: the Hilbert-Schmidt orthocomplement of the unit
   inside the circulant span (represented by `B = J - I`).

With Hilbert-Schmidt normalization `||I||^2 = 3`, `||B||^2 = 6`, `<I, B> = 0`.

## Ratified naming equivalence

The following are two namings of the same two cells of this one context, not
two independent structures:

- the **outcome naming**: the singlet outcome `s` and the doublet `K`-orbit
  outcome `d`, with component-dictionary registered weights `p_s = a^2`,
  `p_d = 2|b|^2` (as used by
  `docs/OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`);
- the **channel naming**: the unit channel `I` and the complement channel `B`,
  with channel Hilbert-Schmidt energies `(3 a^2, 6 |b|^2)` (as used by
  `docs/FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md` and its
  generator-channel table).

The registered weights and the channel energies are the same quadratic
contents up to the common factor `N = 3`, which cancels from every equal-cell
condition.

## Does NOT

- Does not supply a weighting, normalization, probability rule, occupancy
  rule, dictionary selection, or any value of `r` or `Q`.
- Does not select among scoring rules and does not close any wall.
- Does not modify any axiom or primitive; this is a naming ratification on
  already-landed surfaces (the import-retirement path for labeling
  conventions).
- Does not set audit status; rows citing this definition remain subject to
  independent audit.

## Dependencies

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (Record readability and additivity
  sentences; Qualification discipline).
- The two landed surfaces named above, cited for their existing cell namings.
