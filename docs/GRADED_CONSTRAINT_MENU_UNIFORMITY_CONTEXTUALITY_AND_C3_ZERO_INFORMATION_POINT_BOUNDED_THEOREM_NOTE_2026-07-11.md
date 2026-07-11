---
claim_id: graded_constraint_menu_uniformity_contextuality_and_c3_zero_information_point_bounded_theorem_note_2026-07-11
claim_type: bounded_theorem
claim_scope: "Boundary theorems, conditional on the graded-constraint registration proposal's own hypotheses (Class D, cited only as proposed), on the advertisement 'the r = 1/2 class returns as the zero-information limit (uniform on symmetric menus)': (A) 'uniform on every menu' is contextual -- it contradicts the proposal's orthogonal-additivity and non-contextuality clauses on any lattice carrying a menu and a proper refinement; (B) under the proposal's own H1-H4 (Born form) plus R4's full-symmetry premise, the zero-information point of the canonical C_3 generation context is r = 1 (rho = I/3), while r = 1/2 is the diag(1/2,1/4,1/4) per-cell-equipartition point of the designated two-cell menu and is not invariant under the full automorphism group; (C) the advertised r = 1/2 holds only under two named supplied choices -- two-cell menu designation and per-cell equipartition -- neither paid by H1-H4, R4 symmetry, or 'no conditioning records', and the two-cell menu is not a symmetric menu because no automorphism of the supplied structure carries its rank-1 singlet cell to its rank-2 doublet cell. Derives and prefers no r value; refutes nothing (nothing is landed)."
upstream_dependencies:
  - minimal_axioms
bridge_inputs:
  - gleason_theorem_1957
runner: scripts/frontier_graded_constraint_menu_uniformity_c3_zero_info_2026_07_11.py
---

# Menu-Uniformity Contextuality and the Zero-Information Point of the Graded-Constraint Surface on the C_3 Generation Context (Bounded Note)

**Date:** 2026-07-11
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** boundary theorems on one advertisement of the graded-constraint
registration proposal. Everything below is conditional on the proposal's own
hypotheses; nothing here refutes the proposal, adopts a primitive, or derives
or prefers any value of `r`.
**Audit-status authority:** independent audit lane only. This note sets no audit
verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or enlarged
here. The graded-constraint core and its clauses are cited only as proposed
(Class D); the theorems are consequences of those proposed hypotheses,
conditional on them.
**Citation posture:** the registration proposal is Class D and is cited only as
proposed. The program/criterion memo is Class F and carries no premise weight;
it is cited for the wording of the advertisement it repeats, not as a premise.
The Born-form bridge note is a bounded theorem whose R1-R4 are themselves
conditional on H1-H4; it is cited at that conditional strength. The canonical
C_3 definition is a naming ratification effective only on owner approval; its
component dictionary is cited as the ratified naming it proposes.
**Primary runner:**
[`scripts/frontier_graded_constraint_menu_uniformity_c3_zero_info_2026_07_11.py`](../scripts/frontier_graded_constraint_menu_uniformity_c3_zero_info_2026_07_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_graded_constraint_menu_uniformity_c3_zero_info_2026_07_11.txt`](../logs/runner-cache/frontier_graded_constraint_menu_uniformity_c3_zero_info_2026_07_11.txt)

## Purpose

The graded-constraint registration proposal and its program memo both advertise
that the `r = 1/2` class re-enters the graded-constraint program as a
zero-information limit, uniform on symmetric menus. This note lands three
boundary facts about that advertisement, evaluated on the canonical `C_3`
generation readout context, before any lane builds on it:

- **A.** "Uniform on every menu" is not a well-posed rule: it contradicts the
  proposal's own additivity and non-contextuality clauses the moment the lattice
  contains a menu and a proper refinement of it. A uniformity claim must
  designate its menu, and symmetry alone can force uniformity only on a menu
  whose cells are one orbit of the supplied structure.
- **B.** Under the proposal's own hypotheses plus the Born note's named
  full-symmetry premise, the zero-information point of the `C_3` generation
  context is `r = 1` (the dimension-weighting point `rho = I/3`), not `r = 1/2`.
  The `r = 1/2` point is `rho = diag(1/2, 1/4, 1/4)`, which is not invariant under
  the full automorphism group; it is the per-cell-equipartition point of the
  designated two-cell menu.
- **C.** The advertised `r = 1/2` therefore holds only under two named supplied
  choices, and the two-cell menu it uses is not a symmetric menu at all, because
  no automorphism of the supplied structure carries the rank-1 singlet cell to
  the rank-2 doublet cell.

The honest consequence is not that the program fails for the Koide lane: it is
that, on this surface, `r = 1/2` is bought with menu designation plus per-cell
equipartition -- the same supplied atoms the lane has always needed -- and not
by symmetry, "no information", or the Born form.

## The advertisement being bounded (verbatim)

From the Class D registration proposal
[`GRADED_CONSTRAINT_PRIMITIVE_REGISTRATION_PROPOSAL_2026-07-04.md`](GRADED_CONSTRAINT_PRIMITIVE_REGISTRATION_PROPOSAL_2026-07-04.md),
"What it would target after review/audit" (cited only as proposed):

> - **The r = 1/2 class returns as the zero-information limit** (uniform on
>   symmetric menus) — consistency with landed results, no new selection.

From the Class F program/criterion memo
[`GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md`](GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md),
Section 5 (cited for wording only; this memo carries no premise weight):

> Binary availability plus
> symmetry can only pay uniform weights on symmetric menus (the harvested
> uniform-on-orbits results, e.g. r = 1/2).

Both sentences are read here at face value: some designated menu is symmetric,
symmetry pays uniform weights on it, and the resulting weights land the
`r = 1/2` class. Theorems A-C locate exactly which of those steps is a supplied
choice rather than a consequence.

## Authorities and inputs

- **Proposed core and clauses (Class D, cited only as proposed).** The proposal's
  core supplies a weight `w >= 0` with `w(0) = 0`, `w(identity) = 1`, "normalized
  on each menu, additive over exclusive alternatives, non-contextual across
  embedding menus, and defined on the full projection lattice of every
  nearest-neighbor composite, with every finite orthogonal resolution of the
  composite identity menu-eligible." The additivity, non-contextuality, and
  full-eligibility clauses are the hypotheses used below; they are used as
  proposed, never as landed.
- **Born form as a conditional result.** The bounded bridge note
  [`BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md`](BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md)
  fixes the hypotheses H1 (grading exists), H2 (orthogonal additivity), H3
  (non-contextuality), H4 (composite menus realized / full eligibility), and
  concludes, via Gleason's theorem as a named bridge input, that on a carrier of
  Hilbert dimension `>= 3` any such `w` has the form `w(E) = Tr(rho E)` (its R2).
  Its R4 records the full-symmetry premise verbatim:

  > R4 (zero-information limit). Under an explicit additional premise -
  > invariance of `w` under every unitary automorphism of the composite, whose
  > commutant is scalar - `rho = I/d` follows.

  R4 also states, in its own words, that this premise "is not derived from H1-H4
  or from the minimal axioms, and 'no conditioning records' alone does not supply
  it."
- **The canonical `C_3` generation readout context.** The definition note
  [`C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`](C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md)
  fixes the two-cell context on the `hw = 1` generation factor (identified with
  `C^3`, cyclic shift `U`, circulant class `Y = a I + b U + conj(b) U^{-1}`): a
  **singlet cell** (the unit direction `I`) and a **doublet cell** (its
  Hilbert-Schmidt orthocomplement `B = J - I`), with the ratified component
  dictionary `p_s = a^2`, `p_d = 2|b|^2` and channel energies `(3 a^2, 6|b|^2)`.
  The ratio convention is `r = |b|^2 / a^2`, equivalently `r = p_d / (2 p_s)`.

Concretely, in the character (`U`-eigen) basis of `C^3` the two cells are
projectors: the singlet cell `P_s = diag(1, 0, 0)` (trivial representation,
rank 1) and the doublet cell `P_d = diag(0, 1, 1)` (the two nontrivial
characters, rank 2), with the doublet refinement `P_d = P_1 + P_2`,
`P_1 = diag(0, 1, 0)`, `P_2 = diag(0, 0, 1)`. In the position basis the singlet
projector is `J/3` (`J` the all-ones matrix); the discrete Fourier transform
carries `J/3` to `diag(1, 0, 0)`, tying this presentation to the definition
note's `I`/`J` description (runner CHECK 18).

Because the generation carrier `C^3` already has dimension `3 >= 3`, the R1
dimension-2 loophole of the Born note does not arise here: conditional on the
proposal's H1-H3 and full menu-eligibility on this carrier, its bridge input
(Gleason) gives `w(E) = Tr(rho E)` on `C^3` directly, with no composite rescue
needed. This is the only way the Born form is used below, and it is used
strictly conditional on the proposed core.

## Theorem A (menu-uniformity is contextual)

**Statement.** Let a projection lattice contain a two-outcome menu `{P_s, P_d}`
and a three-outcome refinement `{P_s, P_1, P_2}` with `P_d = P_1 + P_2` and all
listed projections mutually orthogonal, both being finite orthogonal resolutions
of the identity (hence both menu-eligible under the proposed domain clause). Then
the rule "`w` is uniform on every menu" is inconsistent with the proposed
orthogonal-additivity clause (H2) together with the proposed non-contextuality
clause (H3).

**Proof.** Uniformity on the two-cell menu gives `w(P_s) = 1/2`. Uniformity on
the three-cell menu gives `w(P_s) = w(P_1) = w(P_2) = 1/3`. The cell `P_s` is
common to both menus, so H3 (the value of `w(P_s)` does not depend on which menu
embeds it) forces a single value; but `1/2 != 1/3`, a contradiction. Equivalently
through H2: from the refined menu, `w(P_d) = w(P_1) + w(P_2) = 1/3 + 1/3 = 2/3`,
while two-cell uniformity asserts `w(P_d) = 1/2`, and `2/3 != 1/2`. Either route
falsifies "uniform on every menu". The proposed full-eligibility clause is what
makes both menus available simultaneously, so this contradiction is internal to
the proposed hypotheses, not an external imposition. (Runner CHECK 05-07.) ∎

**Corollary (which menus symmetry can make uniform).** "Zero-information pays
value `X`" is not well-posed until a menu is designated. Let `G` be a group of
automorphisms of the supplied structure that preserves menu eligibility (maps
eligible menus to eligible menus) and under which `w` is required invariant
(`w(g P) = w(P)`). Then `w` is constant on each `G`-orbit of cells, so `w` is
uniform on a menu **iff** `G` acts transitively on that menu's cells -- i.e. the
cells are mutually conjugate under a symmetry preserving menu eligibility. For
unitary or antiunitary automorphisms, conjugate projections have equal rank
(rank is invariant), so a menu whose cells have unequal ranks is never a
symmetric menu. (The positive half is exercised on the three-cell menu at CHECK
08, whose three rank-1 cells are one orbit of the full automorphism group; the
rank obstruction for the two-cell menu is CHECK 15.)

## Theorem B (the zero-information point of the C_3 context is r = 1, not 1/2)

**Statement.** Adopt the proposal's own hypotheses on the generation carrier, so
that `w(E) = Tr(rho E)` (the Born note's R2, conditional on the proposed core),
and adjoin R4's full-symmetry premise transported to this carrier: invariance of
`w` under a group of unitary automorphisms of `C^3` whose commutant is scalar. By
Schur's lemma `rho = I/3` on the three-dimensional generation carrier. Then the
ratified component dictionary gives

  `w(P_s) = Tr((I/3) P_s) = 1/3`,  `w(P_d) = Tr((I/3) P_d) = 2/3`,

odds `x = w(P_d) / w(P_s) = 2`, hence `r = x/2 = 1`. This is the
dimension-weighting point: each cell is weighted by its rank (`1` for the
singlet, `2` for the doublet).

**Proof.** With `rho = I/3` and `P_s = diag(1,0,0)`, `P_d = diag(0,1,1)`, the two
traces are `1/3` and `2/3` directly. The odds `x = (2/3)/(1/3) = 2`. The
dictionary fixes the odds-to-`r` map: the normalized cell weights are
proportional to the dictionary contents, `w(P_s) : w(P_d) = p_s : p_d = a^2 :
2|b|^2`, so `x = p_d / p_s = 2|b|^2 / a^2 = 2r`, giving `r = x/2 = 1`. That the
irreducible (scalar-commutant) group forces `rho = I/3` is verified concretely:
the qutrit Weyl group generated by the clock `Z = diag(1, w, w^2)` (the supplied
`C_3` shift in the character basis) and the position shift `X` (cyclic
permutation) has a one-dimensional commutant, so `I/3` is its unique invariant
density operator (CHECK 12). (Runner CHECK 09, 16.) ∎

**The r = 1/2 point.** The `r = 1/2` point corresponds to
`rho = diag(1/2, 1/4, 1/4)` in the character basis: then `w(P_s) = 1/2`,
`w(P_d) = 1/2`, odds `x = 1`, and `r = 1/2` (dictionary: `a^2 = 2|b|^2`). This
`rho` is **not** invariant under the full automorphism group: the exhibited
automorphism `X` (the position shift, an element of the irreducible Weyl group)
conjugates `diag(1/2, 1/4, 1/4)` to `diag(1/4, 1/2, 1/4) != diag(1/2, 1/4, 1/4)`,
while it fixes `I/3` (CHECK 11). So `diag(1/2, 1/4, 1/4)` is not the
full-symmetry point at all; it is the **per-cell-equipartition** point of the
designated two-cell orbit menu -- equal weight `1/2` on each of the two cells,
then equipartitioned `1/4 + 1/4` inside the doublet cell.

**Forward reference (stated, not proved here).** Invariance under only the
*supplied* structure -- the `C_3` shift together with the antiunitary exchange of
the two doublet characters -- forces the one-parameter family
`rho = diag(p_s, p_d/2, p_d/2)` and nothing more; the full-group point `I/3` and
the equipartition point `diag(1/2, 1/4, 1/4)` are two members of this family
(with `r = 1` and `r = 1/2` respectively). The characterization of this family
and its use as a dial feed the parallel dial-shape lane and are not part of this
note; CHECK 13 records only a consistency sanity check of the family's
invariance, not a derivation.

## Theorem C (corrected advertisement)

**Statement.** The advertised sentences hold on the `C_3` generation context only
under two named supplied choices:

1. **menu designation** -- the two-cell orbit menu `{P_s, P_d}` is used, rather
   than any refinement of it; and
2. **per-cell equipartition** -- equal weight `1/2` is placed on each of the two
   cells of that menu.

Neither choice is paid by the proposal's H1-H4, by R4's full-symmetry premise, or
by "no conditioning records":

- H1-H4 alone give only the Born form `w(E) = Tr(rho E)` -- a family of possible
  `rho`, no particular value, hence no particular `r`.
- R4's full-symmetry premise pins `rho = I/3`, which is `r = 1`, not `r = 1/2`
  (Theorem B); and R4 itself states that "no conditioning records" does not
  supply even that premise.

So `r = 1/2` requires the two choices above as extra supplied structure. On the
automorphism-symmetric reading, the zero-information limit of the `C_3` context is
`r = 1`. (Runner CHECK 09-11, 14.)

**Cell-isomorphism obstruction.** The two-cell menu `{P_s, P_d}` is moreover not
a symmetric menu in the sense of Theorem A's corollary. The singlet cell has rank
1 (`Tr P_s = 1`) and the doublet cell has rank 2 (`Tr P_d = 2`). Every unitary or
antiunitary automorphism of the supplied structure preserves rank, so none maps
`P_s` to `P_d`; the two cells lie in different orbits under any such group (CHECK
15, tested over the supplied generators and their products). By the corollary,
symmetry alone cannot force uniformity on `{P_s, P_d}`. The advertisement's
parenthetical "(uniform on symmetric menus)" therefore does not apply to the
two-cell menu: its uniformity is choice (2), a designation, not a symmetry
consequence. Under the full automorphism group the symmetric menu is instead the
three-cell menu `{P_s, P_1, P_2}` (three rank-1 cells, one orbit), on which
symmetry does force uniformity `1/3` each -- and that is exactly the `rho = I/3`,
`r = 1` point.

## What this note does not claim

- It does **not** refute the graded-constraint proposal. The proposal is Class D
  and nothing has landed to refute; this note bounds one advertisement of it,
  conditional on its own hypotheses.
- It does **not** derive, select, or prefer any value of `r`. It computes what
  each named premise-set delivers and no more.
- It does **not** claim the graded-constraint program is unviable for the Koide
  lane. The honest consequence is the opposite in tone: on this surface `r = 1/2`
  is reachable, but only by supplying menu designation plus per-cell
  equipartition -- exactly the same atoms the occupancy/equipartition lane has
  always had to supply. Symmetry, "no information", and the Born form do not pay
  them.
- It sets **no** audit status and uses no effective-status or audit language.
- The Class F memo is cited for wording only; per its own qualification it
  carries no premise or interpretive weight, and nothing here rests on it as a
  premise.
- The full-symmetry premise (R4) and the Born form (R2) are used exactly at their
  own conditional strength; this note does not strengthen, adopt, or approve
  them, and does not re-derive Gleason.

## Consumers

- **The Koide occupancy / equipartition lane.** This note fixes the price tag of
  the `r = 1/2` point on the `C_3` generation context: menu designation plus
  per-cell equipartition, as named supplied structure. It is consistent with, and
  complementary to, the occupancy bridge note
  [`KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md`](KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md),
  where sector slotting gives `r = 1` and orbit slotting gives `r = 1/2` under a
  supplied one-record-one-slot reading: the two notes agree that the difference
  between `r = 1` and `r = 1/2` is a supplied designation, not a symmetry
  consequence. Downstream occupancy work should carry menu designation and
  per-cell equipartition as explicit named premises, never as "the
  zero-information limit".
- **The graded-constraint registration pipeline.** Any bounded note that carries
  the proposed core forward and invokes the "zero-information / uniform on
  symmetric menus" advertisement must first designate its menu and must not treat
  the two-cell `C_3` menu as symmetric. On the automorphism-symmetric reading the
  zero-information point is `r = 1`; `r = 1/2` is a separate designated point.
- **The parallel dial-shape lane** consumes the forward-referenced fact (Theorem
  B) that the supplied structure alone forces the one-parameter family
  `rho = diag(p_s, p_d/2, p_d/2)`; that characterization is owned by that lane,
  not here.

## Verification

The companion runner
[`scripts/frontier_graded_constraint_menu_uniformity_c3_zero_info_2026_07_11.py`](../scripts/frontier_graded_constraint_menu_uniformity_c3_zero_info_2026_07_11.py)
performs exact (sympy) checks on explicit `3x3` matrices and symbols; nothing on
the derivation paths (`w = Tr(rho P)`, the odds `x`, `r = x/2`, the dictionary
ratios) is hard-coded -- each is computed and then compared to its expected
value. It guards the four verbatim quotations against the source documents;
builds the two-menu / three-menu contradiction of Theorem A and the single-orbit
corollary; evaluates `rho = I/3 => (1/3, 2/3) => r = 1` and
`rho = diag(1/2, 1/4, 1/4) => r = 1/2` with an exhibited automorphism breaking the
latter and fixing the former, and confirms the Weyl group's scalar commutant for
Theorem B; checks the supplied-structure family as a labeled sanity check;
establishes the two-supplied-choices statement and the rank / no-cell-swap
obstruction for Theorem C; verifies the dictionary arithmetic and the two special
points; and ties the character-basis singlet to the definition note's `J/3` via
the discrete Fourier transform.

Measured runner total after final verification: `TOTAL: PASS=18 FAIL=0`.
