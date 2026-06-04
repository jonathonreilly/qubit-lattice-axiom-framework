# Z_3 Character-Isomorphism Open Gate — Axis-Cycle (Weyl-Z_3) Orientation No-Go

**Date:** 2026-05-30
**Type:** no_go
**Claim type:** no_go
**Status:** formal no-go proposal. This note adds no axiom, no fitted input, and
no audit verdict. The independent audit lane sets audit and effective status.
**Status authority:** independent audit lane only. Effective status is
pipeline-derived after audit ratification and dependency closure.
**Primary runner:** [`scripts/frontier_z3_character_isomorphism_weyl_axis_cycle_orientation_no_go.py`](../scripts/frontier_z3_character_isomorphism_weyl_axis_cycle_orientation_no_go.py)

## 1. Scope

The open gate
[`Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md`](Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md)
killed only the `SU(3)_c` **center** `Z_3` as a color/generation bridge: on the
color fundamental the center character is `(3, 3 omega, 3 omega^2)`, not the
regular `(3, 0, 0)`. It explicitly left the **axis-cycle / Weyl-`Z_3`** leg —
the order-three cycle of the three `Z^3` coordinate axes, which *does* carry the
regular character `(3, 0, 0)` — as "the work still to be derived" (that note,
Section 5).

This note records the no-go increment on that surviving leg: **even with the
matching regular character, the axis-cycle cannot supply a canonical
within-charge-sector species bijection**, because its alignment to the retained
translation grading is a free 3-fold cyclic orientation with no `A_min`-canonical
preference. It reduces to `P1` (a stipulated label / orientation convention)
exactly as the center did, and so cannot be canonically derived within `A_min`.

This does not add a new axiom, primitive, or retained-surface premise, and it
does not promote the integer equality `N_gen = N_color = 3` into a retained
cross-sector structural theorem.

## 2. Repo Baseline and Imports

The repo baseline is the physical `Cl(3)` local algebra on the `Z^3` spatial
substrate, whose cubic symmetry contains the order-three axis cycle
`c: e_1 -> e_2 -> e_3 -> e_1`, represented by the permutation matrix

```text
P = [[0, 0, 1],
     [1, 0, 0],
     [0, 1, 0]],     P^3 = I,  det P = 1,  chi(e), chi(c), chi(c^2) = (3, 0, 0).
```

The retained inputs used here are: the substep-4 simultaneous-diagonalization
bridge
[`STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`](STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md)
(the carrier on which gradings act) and the `Z^3` translation grading. Standard
`Z_3` character theory is used. No physical identification of color labels with
the `Z^3` axes is assumed — that is precisely the bridge the open gate flagged,
and this note shows the axis-cycle cannot supply it canonically.

## 3. The Calculated Orientation Fact

A within-sector bijection `pi: {c_1, c_2, c_3} -> {e, mu, tau}` would be a map
`W` aligning the color Weyl-`Z_3` grading to the retained translation grading.
Both gradings carry the regular `Z_3` character, so `W` must be `Z_3`-equivariant
(`W P = P W`). The space of such `W` is the group algebra `C[Z_3]`:

```text
W = a_0 I + a_1 P + a_2 P^2.       (3-dimensional)
```

Restricting to candidate **alignments** (bijections of the three corners, i.e.
permutation matrices), exactly the **three cyclic powers** are `Z_3`-equivariant:

```text
equivariant alignments:   { I, P, P^2 }      (the 3 cyclic permutations),
non-equivariant:          the 3 transpositions  -> W = 0.
```

The three cyclic alignments `W ∝ I, P, P^2` are equally valid: they are related
by the relabeling `P` itself, which maps any operator diagonal in the carrier
basis to an **isospectral** operator with cyclically permuted eigenvalue order.
The simultaneous-diagonalization bridge forces commuting operators diagonal, but
supplies **no canonical eigenvalue order** — so there is no `A_min`-canonical
first element among `{I, P, P^2}`.

Therefore the axis-cycle orientation is a free 3-fold `P1` choice. The color
Weyl-`Z_3` reduces to `P1` exactly like the center `Z_3`, despite the matching
regular character.

## 4. Why this strictly tightens the open gate

```text
Open gate (2026-05-10):  center Z_3  -> wrong character (3,3w,3w^2)  -> killed.
                         axis-cycle  -> right character (3,0,0)       -> "still to derive".
This note:               axis-cycle  -> right character, but alignment is a free
                                        3-fold cyclic P1 choice        -> reduces to P1.
```

The open gate left exactly one bridge candidate open (the axis-cycle); this note
closes it to `P1`. Both `Z_3` candidates a skeptic could name — center and
axis-cycle — are now shown to be unable to supply a canonical color/generation
or within-sector species bijection within `A_min`. The only escape is a
non-`Z_3`-equivariant input, which is `P1` (label/orientation), `P2` (a
`C_3`-breaking primitive, foreclosed within `A_min` by the A3 campaign
[`AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md`](AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md)),
or `P3` (PDG spectrum-matching, forbidden by the retained-grade rule).

This is the same `C_3` orbit-indistinguishability wall as the `delta`-pattern
leg, now recorded for the within-sector label-orientation atom.

## 5. Boundary

This no-go does not establish:

- a retained positive theorem, a new structural primitive, or a load-bearing
  color/generation bridge;
- a promotion of the integer equality
  [`N_gen = N_color = 3`](CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md);
- a charged-lepton Lane 6 closure, a Koide closure, a `y_tau` Ward identity, or
  any empirical mass claim.

It forecloses one bridge route: the axis-cycle / Weyl-`Z_3` cannot canonically
fix the within-sector orientation; that orientation is a `P1` convention. It
keeps the `delta`-pattern leg and the Brannen amplitude-equipartition atom
`|b|^2/a^2 = 1/2` strictly separate (those are distinct open/foreclosed atoms,
not addressed here).

## 6. Audit consequence

```yaml
claim: z3_character_isomorphism_weyl_axis_cycle_orientation_no_go
closure_proposal: no_go
foreclosed: axis_cycle_weyl_z3_as_canonical_within_sector_species_bijection
mechanism: regular_character_matches_but_alignment_is_free_3fold_cyclic_P1_orientation
tightens: z3_character_isomorphism_color_generation_open_gate_note_2026-05-10  # beyond center-only kill
escape_inputs_only: [P1_label_orientation, P2_C3_breaking_primitive_foreclosed, P3_PDG_forbidden]
generation_bridge_status: not_closed
forbidden_imports_used: false
audit_status_authority: independent audit lane only
```

## No-go discipline gate (N1-N8)

**Status:** PASS for the narrow within-sector orientation no-go only. The claim
being closed is **not** a repo-wide "no Z_3 character isomorphism" theorem and
**not** a denial that `N_gen = N_color = 3`. It is the single structural
statement that the axis-cycle / Weyl-`Z_3` (the `{I, P, P^2}` intertwiner family
on the carrier of the substep-4 simultaneous-diagonalization bridge) cannot fix
a *canonical* `A_min`-preferred within-sector species bijection
`pi: {c_1, c_2, c_3} -> {e, mu, tau}`; the three equivariant alignments are
isospectral relabelings with no canonical first element, so the orientation is a
free 3-fold `P1` choice.

### N1 - Alternative route enumeration

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Equivariant-intertwiner route | Pick a single canonical `W` aligning the axis-cycle grading to the translation grading. | The `Z_3`-equivariant `W` span the 3-dim group algebra `C[Z_3] = {a_0 I + a_1 P + a_2 P^2}`; among permutation alignments exactly `{I, P, P^2}` qualify and they are mutually isospectral relabelings, so no member is canonical. | ATTEMPTED |
| Transposition-alignment route | Use a non-cyclic corner swap (a transposition) to break the 3-fold tie. | A transposition is not `Z_3`-equivariant; it forces `W = 0` (Section 3), so it supplies no alignment at all rather than a canonical one. | ATTEMPTED |
| Eigenvalue-order route | Let the simultaneous-diagonalization bridge pick a canonical eigenvalue order, hence a canonical first element of `{I, P, P^2}`. | The substep-4 bridge forces commuting operators diagonal but supplies **no** canonical eigenvalue order; cyclic relabeling by `P` is isospectral, so the bridge cannot privilege one cyclic power. | ATTEMPTED |
| Center-`Z_3` route | Reuse the `SU(3)_c` center `Z_3` as the species-bijection carrier. | Already killed upstream: on the color fundamental the center character is `(3, 3w, 3w^2)`, not the regular `(3, 0, 0)`; it never reaches the within-sector bijection stage (this note only handles the surviving axis-cycle leg). | OUT OF SCOPE (killed upstream) |
| `C_3`-breaking primitive route (P2) | Add an axis-distinguishing primitive that singles out one cyclic orientation. | A `C_3`-breaking selector is `P2`, foreclosed within `A_min` by the A3 campaign `AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md`; it is not available without a new primitive. | ATTEMPTED (P2 foreclosed) |
| PDG spectrum-matching route (P3) | Fix the orientation by matching `(c_1, c_2, c_3)` order to the observed `(m_e, m_mu, m_tau)` ordering. | Reading the orientation off the PDG mass order is `P3`, forbidden by the retained-grade (no spectrum-matching) rule; it imports the answer rather than deriving it. | ATTEMPTED (P3 forbidden) |
| `delta`-pattern / amplitude route | Borrow the `delta`-pattern leg or the Brannen `|b|^2/a^2 = 1/2` atom to fix the within-sector labels. | Those are distinct atoms on separate surfaces (Section 5); they address pattern/amplitude, not the corner-to-flavor label orientation, and are explicitly kept separate here. | OUT OF SCOPE (separate atom) |

### N2 - Wall-independence audit

The collapsed wall set for this within-sector no-go has **one** wall: the
`C_3` orbit-indistinguishability of the three corners under the only retained
inputs in play (the substep-4 carrier and the `Z^3` translation grading). The
three equivariant alignments `{I, P, P^2}` form a single free `C_3` orbit with
no `A_min`-canonical first element. The apparent multiplicity of escapes
(`P1`, `P2`, `P3`) are **not** independent walls; they are the three exhaustive
*kinds* of input that would have to be added to break that one orbit
(stipulated label, `C_3`-breaking primitive, or spectrum-match). What could
change the verdict is a *new* retained, `A_min`-internal canonical eigenvalue
order on the carrier (none exists today); supplying it would not modify the
character arithmetic but would give a different, derived first element. This is
the same `C_3` orbit wall as the `delta`-pattern leg, here recorded for the
within-sector label-orientation atom.

### N3 - Hidden-wall scan

The phrases "canonical", "regular character", "Weyl-`Z_3`", and "orientation"
are **not** used as hidden retained inputs for the negative result. The
load-bearing inputs are explicit and finite:

1. the axis-cycle permutation `P` (with `P^3 = I`, `det P = 1`, character
   `(3, 0, 0)`), a property of the `Z^3` cubic substrate;
2. standard `Z_3` character theory and the fact that the `Z_3`-equivariant
   intertwiners are exactly `C[Z_3] = {a_0 I + a_1 P + a_2 P^2}`;
3. the substep-4 simultaneous-diagonalization bridge
   `STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`
   as the carrier, which forces diagonality but **supplies no canonical
   eigenvalue order**;
4. the `Z^3` translation grading as the grading the alignment must match.

No PDG value, no color/axis identification, and no `C_3`-breaking primitive is
silently assumed; those are exactly the escape inputs the note declares it does
**not** use. Any broader generation-bridge or Koide claim is explicitly left out
of scope (Section 5).

### N4 - Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| `Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md` | The surviving axis-cycle leg flagged there as "the work still to be derived" (Section 5 of that note): can the regular-character `Z_3` supply a canonical within-sector bijection? | Exactly that leg — the axis-cycle alignment is shown to be a free 3-fold `P1` orientation. | yes (the direct tightening target) |
| `AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md` | `C_3`-breaking primitives are foreclosed within `A_min`. | Used only to certify that the `P2` escape (a `C_3`-breaking orientation selector) is unavailable; it is not itself the within-sector no-go. | yes (closes the P2 escape) |
| `STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md` | Simultaneous diagonalization forces commuting operators diagonal. | Used as the carrier and to establish that diagonalization gives **no** canonical eigenvalue order, hence no canonical first element of `{I, P, P^2}`. | yes (load-bearing carrier) |
| `CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md` | The integer equality `N_gen = N_color = 3` as cross-sector context. | Cited only to mark what is **not** promoted; the integer count is not used to derive the within-sector orientation. | no (context only, **not load-bearing** for this no-go) |

The non-matching witness (the integer-equality note) is context only and is not
used as load-bearing proof of this orientation no-go.

### N5 - Rhetoric audit

The broad phrases "no-go", "cannot supply", "foreclosed", and
"orientation-forced" are scoped to a single claim: the axis-cycle / Weyl-`Z_3`
cannot fix an `A_min`-**canonical** within-sector species bijection
`pi: {c_1, c_2, c_3} -> {e, mu, tau}` on the substep-4 carrier, because its
alignment is a free 3-fold `P1` cyclic orientation. The note does **not** claim:
that no `Z_3` structure relates color and generation (the regular characters do
match); that the integer equality `3 = 3` is false; that a `Z_3` bijection
cannot be *stipulated* (it can — that is precisely the `P1` cost being named);
or that the `delta`-pattern leg or the Brannen `|b|^2/a^2 = 1/2` atom are
addressed here. An over-broad reading ("Z_3 character isomorphism is dead") is
explicitly disclaimed: only the *canonicity within `A_min`* of the within-sector
orientation atom is foreclosed.

### N6 - Partial-closure path scan

Non-axiom partial-closure paths remain open and are **not** new axioms:

- a future `A_min`-internal derivation of a canonical eigenvalue order on the
  substep-4 carrier (a derived order, not a stipulation, would supply a
  non-`P1` first element of `{I, P, P^2}`);
- independent positive work on the separate `delta`-pattern leg and the Brannen
  amplitude-equipartition atom `|b|^2/a^2 = 1/2`, which are distinct atoms not
  closed here;
- any non-`Z_3`-equivariant *derived* structure (as opposed to a stipulated
  `P1` label or a `C_3`-breaking `P2` primitive) that future retained results
  might expose.

This note calls none of these a new axiom; it only states they are not the
axis-cycle equivariant-alignment argument, which is the boundary of the present
no-go.

### N7 - Steelman

The strongest objection: the substep-4 bridge already fixes a *specific* basis
in which the commuting operators are diagonal, so the identity element `I` of
`{I, P, P^2}` is the "obvious" canonical alignment — and an obvious canonical
choice would defeat the `P1` claim. This objection fails because the diagonal
basis is itself defined only up to the cyclic relabeling `P` (the bridge fixes
diagonality, not the *labeling/order* of the degenerate-by-symmetry corners): `P`
maps any carrier-diagonal operator to an isospectral operator with cyclically
permuted eigenvalue order, so "the basis the bridge picked" has no `A_min`-
preferred origin among the three cyclically related orderings. Picking `I` as
"first" silently re-imports the very orientation convention (`P1`) the note is
naming. The steelman would block a broader claim ("no basis is fixed at all"),
which this note does not make; it does not break the scoped claim, which is only
that **no element of `{I, P, P^2}` is `A_min`-canonical**.

### N8 - Cross-cycle echo

Prior negative-claim overclaims in this repo often failed by collapsing a single
representative (one symmetry, one operator, one expression) into a whole-lane
closure — e.g. earlier "Z_3 isomorphism" framings that read one matching
character as a derived color/generation bridge. This note avoids that echo three
ways: (1) it keeps the boundary at one atom (the within-sector *orientation*),
explicitly leaving the `delta`-pattern leg, the `|b|^2/a^2 = 1/2` amplitude
atom, and the integer count `3 = 3` outside scope (Section 5); (2) it does
**not** generalize from the center-`Z_3` kill to "all `Z_3`" — it separately
handles the surviving axis-cycle leg with the matching regular character; and
(3) it foreclose only *canonicity within `A_min`*, conceding that a stipulated
(`P1`) bijection exists, so it does not parlay one open atom into a claim that
the generation bridge or Koide lane is closed (Section 5 boundary).

## 7. Runner

```bash
python3 scripts/frontier_z3_character_isomorphism_weyl_axis_cycle_orientation_no_go.py
```

Expected summary:

```text
SCORECARD: PASS=10 FAIL=0
```

The runner certifies the axis-cycle regular character `(3,0,0)` and the center
character `(3,3w,3w^2)`, that the equivariant intertwiner family is the 3-dim
group algebra `{I,P,P^2}`, that exactly the three cyclic permutations align
(transpositions give `W = 0`), and that cyclic relabeling is isospectral with
permuted order (no canonical first element) — so the orientation is a free
3-fold `P1` choice.

## 8. Related Surfaces

- Center-leg open gate (tightened here):
  [`Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md`](Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md)
- `C_3` orbit-indistinguishability (delta-pattern leg):
  [`AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md`](AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md)
- Carrier / simultaneous-diagonalization bridge:
  [`STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`](STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md)
- Integer-equality cross-sector context:
  [`CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md`](CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md)

This note is a formal no-go and asserts no closure of the generation-bridge or
Koide lanes.
