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
