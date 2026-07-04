# Tier-A K/CPT Orientation Invariance For The AC_phi_lambda Gate: Bounded Candidate Route

**Date:** 2026-06-09 (2026-06-10: the determinant-character phase-erasure
lemma moved to its own note,
`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`,
so the strong-CP route stands free of this note's staggered-gate dependency;
the filename keeps the original title per the no-rename rule) (2026-06-12:
the orientation lemma is restated on the supplied circulant class stipulated
in-note; the staggered-Dirac gate note is context, not load-bearing — the lemma
consumes no content from it.) (2026-07-04: the unordered-multiset
registrability premise is now cited to its named bridge note and a dated
downstream-hygiene line is added to the Boundary, per the 2026-07-04
conditional-audit repair note `missing_bridge_theorem`.)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome and does not edit the audit-lane-owned Tier-A
registry.
**Primary runner:** [`scripts/frontier_tier_a_korbit_determinant_orientation_invariance_2026_06_09.py`](../scripts/frontier_tier_a_korbit_determinant_orientation_invariance_2026_06_09.py)
**Runner cache:** [`logs/runner-cache/frontier_tier_a_korbit_determinant_orientation_invariance_2026_06_09.txt`](../logs/runner-cache/frontier_tier_a_korbit_determinant_orientation_invariance_2026_06_09.txt)

## Boundary

This note preserves a useful algebraic route without claiming the Tier-A
registry has already changed.

It proves one bounded fact:

1. For the supplied `AC_phi_lambda` circulant class stipulated in-note below,
   conjugation maps `delta` to `-delta`, while the unordered spectrum is
   invariant under that flip.

(The companion determinant-character phase-erasure lemma, formerly stated
here, now lives in
`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
with its own runner; it is context for this note, not load-bearing.)

It does not strip the `AC_phi_lambda` admission by itself, derive
`|delta| = 2/9`, or change `docs/audit/data/tier_a_admissions.json`.
Those moves require later registry/audit handling and any missing bridge named
below.

**Downstream hygiene (2026-07-04):** the lemma's registrable-species premise
(the species surface is exactly the unordered mass multiset) is not this
note's content and is not axiom content; it is carried by the cited bridge
note `UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md`,
whose audit status is set only by the independent audit lane. This note's
conclusion remains bounded on that bridge plus the `k -> -k` relabel
convention; if the registrable surface is ever enlarged beyond the unordered
multiset, the conclusion must be re-derived, not assumed.

## Determinant Readout Lemma (Moved)

The K/CPT determinant-character phase-erasure lemma, its hostile guard, and
the named determinant-readout bridge open moved to
`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
(context, not load-bearing here), so the strong-CP mass-orientation route
carries no dependency on the staggered gate surface used below.

## `AC_phi_lambda` Orientation Lemma

This lemma is stated on a supplied circulant class, stipulated here: the
three-parameter Hermitian circulant family below, with `a` real, `B > 0`,
`delta` real, and `C` the cyclic 3-shift. The lemma is self-contained algebra
on this supplied circulant class and consumes no content from any other note.
Physically, this family is the `AC_phi_lambda` gate surface of the
staggered-Dirac realization lane
(`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`, context, not
load-bearing: the identification of the physical gate surface with this class
is carried by the `AC_phi_lambda` admission itself, which supplies its own gate
surface). Write the relevant Hermitian circulant as

```text
H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T.
```

Complex conjugation sends this matrix exactly to `H(-delta)`. The elementary
symmetric polynomials of the three eigenvalues agree at `delta` and `-delta`;
the flip permutes the eigenvalue labels by `k -> -k`.

Therefore, conditional on the registrable species surface being exactly the
unordered mass multiset — the premise carried by the named bridge
[`UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md`](UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md)
— and on the `k -> -k` relabel being convention, the sign
of `delta` is not extra registrable content. The even datum, equivalently
`cos(3 delta)` or `|delta|` on the chosen fundamental domain, is the remaining
candidate atom.

This does not derive the magnitude `|delta| = 2/9`. It also does not rule out a
future orientation-sensitive bridge if the registrable surface is enlarged
beyond the unordered multiset.

## Registry Consequence

The only supported consequence is a candidate route for future Tier-A registry
review:

- `AC_phi_lambda`: the orientation lemma may help reduce the admission to a
  magnitude-only atom only after the unordered-multiset registrability bridge is
  retained or confirmed as already supplied by existing audited surfaces.

(The strong-CP theta consequence of the determinant lemma is stated in the
moved note named above.)

No new axiom, primitive, admission, normalization, probability rule, comparator,
or audit verdict is introduced here.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) for current
  Record finite additivity and content-determination only; the registrable
  unordered-multiset species surface used downstream is carried by
  [`UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md`](UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md),
  not by the axiom text itself.

Context (not load-bearing: both lemmas are self-contained algebra on their
supplied classes — the determinant-character computation and the circulant
conjugation identity — and use no content from the context note; the bridge
that would supply the determinant-class readout is the named open above):

- `KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` for the
  determinant-orbit context.
- `THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
  for the moved determinant-character lemma (the strong-CP-side companion).
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` for where the supplied
  circulant class arises physically as the `AC_phi_lambda` gate surface; the
  orientation lemma is self-contained algebra on the supplied class stipulated
  in-note and consumes no content from the gate note.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status
authority.
