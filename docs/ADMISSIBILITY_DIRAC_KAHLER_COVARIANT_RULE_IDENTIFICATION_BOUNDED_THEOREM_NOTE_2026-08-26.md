---
claim_id: admissibility_dirac_kahler_covariant_rule_identification_bounded_theorem_note_2026-08-26
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md
claim_type: bounded_theorem
claim_scope: "Finite exact matrix-pair spin diagonalisation on Z_6 x Z_4; a twelve-verdict twist dictionary on that extent; an exact four-extent parity census; target-conditional cell encodability over QQ(c,v) with two replacement-target controls; a minimal real 4 x 4 Cl(3,0) exhibit; and separate exact Schur identities on Block 171's committed bench. The available premises do not select a unique generator pair, Hodge target, or bridge to the Block 171 action."
runner: scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "finite covariant-encoding exhibits with the physical selection map still missing"
source_of_blocker_text: review_loop
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Supply and gate an independent selector for the ordered generator pair and Hodge target, then derive an explicit bridge from that selected construction to Block 171's Q before asserting one physical rule."
conditional_surface_status: "stacked on unmerged ancestor artifacts; scientific content is proposed for retention and remains audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite-dimensional linear algebra and exact algebraic representation theorems, with explicit counterexamples to the stronger selection claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-axiom-closure-block200-transfer-robustness-boundary-package-20260826
parent_commit: 4a21fefcce3f161dca9e13b64212add7db003349
current_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
registered: 0
adopted: 0
axiom_movement: none
---

# Finite covariant-encoding exhibits and the missing selection map

**Date:** 2026-08-26

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author proposal only; independent audit is
required before any effective retained status.

**Standing:** conditional support on an unmerged PR stack. Nothing is
registered, adopted, or added to the axioms.

## Result

The runner preserves four exact results:

1. For the declared pair
   `A = sx`, `B = -sz`, the finite covariant nearest-neighbour matrix on
   `Z_6 x Z_4` spin-diagonalises at all four wrap twists. The resulting scalar
   matrix has `96` nonzero entries. Its exact site-sign comparison with the
   periodic, wrap, and one-edge-seam lane matrices gives twelve verdicts on
   this extent.
2. Once a scalar `4 x 4` target `L` is declared, the sixteen-word cell ansatz
   has a unique preimage at every anchor parity. This holds for the imported
   `shear_hodge(c,v)` and for two unrelated replacement targets. It is an exact
   encodability theorem, not a theorem selecting the imported target.
3. A real triple of pairwise anticommuting positive involutions has no `2 x 2`
   or odd-dimensional realization. An exact `4 x 4` triple exists and carries
   all `24` proper cubic rotations by exact intertwiners.
4. On Block 171's own committed bench, its own `Q` satisfies the exact Schur
   identity, the stated local-block support facts, and the end-to-end `W9`
   profile identity. These facts are retained independently: this block
   supplies no equation connecting that `Q` to `A`, `B`, or `Omega`.

The stronger draft claim is withdrawn. The exact lane-sign census contains six
ordered generator pairs, not one. The same target-preimage certificate also
holds for the two unrelated replacement targets tested here. Therefore the
measured premises do not identify
a unique physical covariant rule or show that the four result blocks are
readings of one object.

## Authority and dependencies

The construction is inherited from, and does not alter:

- [Block 200 finite transfer probes](ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_ROBUSTNESS_BOUNDARY_PACKAGE_BOUNDED_THEOREM_NOTE_2026-08-26.md)
- [Block 190 lane kernel and seam/wrap fork](ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md)
- [Block 171 committed bench](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md)
- [Block 105 Hodge input](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
- [Gravity-mainline campaign charter](../.claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md)

The exact implementation is
[the Block-201 runner](../scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py).

## 1. Finite matrix-pair exhibit

Set

```text
sx  = [[0,1],[1,0]],
sz  = [[1,0],[0,-1]],
A   = sx,
B   = -sz,
Omega(t,x) = sx^(t mod 2) sz^(x mod 2).
```

The covariant matrix uses `A/2` and `B/2` on forward nearest-neighbour
links and transpose-negative blocks on reverse links. On `Z_6 x Z_4`, exact
congruence by the block-diagonal matrix assembled from `Omega(t,x)` gives

```text
non-scalar 2 x 2 blocks = 0 at every twist in {+1,-1}^2,
nonzero scalar entries  = 96.
```

Exact site-sign propagation on the same `Z_6 x Z_4` matrix yields

| covariant twist | periodic lane | wrap lane | one-edge seam lane |
| --- | :---: | :---: | :---: |
| `(+,+)` | yes | no | no |
| `(+,-)` | no | no | no |
| `(-,+)` | no | yes | yes |
| `(-,-)` | no | no | no |

This is a twelve-verdict dictionary on `Z_6 x Z_4`. No `Z_8 x Z_4` dictionary
is claimed.

The separate Block-190 fork is reproduced on `Z_8 x Z_4` at
`m=9/20`, `c=5/13`, and unit volume:

```text
nnz(Q_seam - Q_seam^T) = 144,
nnz(Q_wrap - Q_wrap^T) = 160.
```

The kernel-level wrap-to-seam sign is not a symmetry of the fixed reflection
and Hodge completion:

```text
nnz(E K_wrap E - K_seam) = 0,
nnz([E,Ps]) = 24,
nnz([E,H])  = 16,
stage-2 link residual = 0,
stage-2 Hodge residual = 96 covariant entries = 48 scalar entries.
```

These exact finite calculations are positive content. They demonstrate a
working representation; they do not select it.

## 2. Generator-pair census and finite extent contrast

For the stated integer powers and the exact lane-sign predicate, the runner
square-normalizes each generator axis as `sign(G^2)G`. The admitted ordered
axis pairs drawn from `sx`, `sz`, and `i sy` are

```text
(sx,sz), (sx,i sy), (sz,sx), (sz,i sy), (i sy,sx), (i sy,sz).
```

All six are trace-orthogonal and anticommute. Because `(i sy)^2=-I`, imposing
positive square removes the four pairs containing `i sy`, but still leaves the
two ordered pairs `(sx,sz)` and `(sz,sx)`. Lane signs plus that signature choice
therefore still do not select an ordering, orientation, or physical
interpretation.

The exact non-Clifford period-two frame
`S=[[1,1],[0,1]]` supplies a further counterexample if the generator class is
not imposed: it reproduces the same lane signs while its two transformed
couplings have nonscalar squares and nonzero anticommutator.

The finite extent measurements are

```text
Z_6 x Z_4: 0 non-scalar blocks,
Z_8 x Z_4: 0 non-scalar blocks,
Z_8 x Z_3: 16 non-scalar blocks,
Z_7 x Z_4: 8 non-scalar blocks.
```

This is an exact contrast among four extents. No necessary-and-sufficient
all-extent parity theorem is asserted.

## 3. Target-conditional cell encodability

Let the four cell corners be `(0,0),(0,1),(1,0),(1,1)`, and declare the word
blocks

```text
W_ij = sx^delta_t sz^delta_x.
```

For a declared scalar target `L`, solve

```text
Psi_cell^T CP Psi_cell = L tensor I_2
```

for the sixteen scalar word coefficients in `CP`. With the imported symbolic
`shear_hodge(c,v)`, the system has

```text
64 equations,
16 unknowns,
coefficient rank 16,
augmented rank 16,
affine dimension 0
```

at all four anchor parities. The displayed coefficient matrix differs from the
target at `(1,2)` only because the directed word there is labelled `sx sz`
rather than `sz sx=-sx sz`. Replacing that one word label changes neither `CP`
nor the encoded form and gives exact residual zero.

Two unrelated rational `4 x 4` replacement targets are also tested at every
anchor. All eight replacement cases have the exact certificate

```text
(coefficient rank, augmented rank, affine dimension, residual)
= (16,16,0,0).
```

A completely general `8 x 8` target congruence has rank `64/64` because
`Psi_cell` is invertible. These rank facts prove unique preimages after a target
is declared. They cannot choose the Hodge target or confer geometric status on
it.

## 4. Minimal real `Cl(3,0)` exhibit

There is no real `2 x 2` triple of pairwise anticommuting matrices squaring to
`+I`. Diagonalizing the first involution forces the other two to be
antidiagonal. Writing their off-diagonal entries as `(b,c)` and `(d,e)`, the
square conditions give `bc=de=1`, while anticommutation gives `be+cd=0`.
Substitution reduces this to

```text
b^2 + d^2 = 0,
```

contradicting invertibility over the reals.

Dimension `3` is excluded separately and exactly. If invertible `n x n`
matrices obey `AB=-BA`, then

```text
det(AB) = det(-BA) = (-1)^n det(BA).
```

For odd `n`, `det(AB)=-det(AB)`, impossible for invertible `A` and `B` over the
reals. Together with the `2 x 2` obstruction, this excludes dimensions
`1,2,3`.

The `4 x 4` exhibit

```text
G1 = sx tensor I_2,
G2 = sz tensor sx,
G3 = sz tensor sz
```

has three zero square residuals and three zero anticommutator residuals. All
`24` determinant-`+1` signed permutation matrices have exact invertible
intertwiners; every conjugation residual vanishes. Thus `4 x 4` is the minimal
real home for this positive-signature triple.

This representation theorem is retained. Nothing in the lane-sign census
selects this triple as a physical lift.

## 5. Separate Block 171 Schur identities

The runner imports Block 171's own `Site` and `Env` classes and evaluates its
committed `12x4` bench with `N=24`, `T=6`, `tstar=5`, and four site rows.

For the base record and four declared far additions:

- all four normalized `W9` components move by exact nonzero rationals;
- `Q[ss,ss]`, `Q[ss,rr]`, and `Q[rr,ss]` are unchanged;
- the direct coupling support is exactly the two time slots `{0,4}`;
- both inverse certificates and the Schur-complement identity have zero
  residual;
- the normalized diagonal of `herm(Schur^-1)` matches Block 171's own profile
  componentwise at residual `(0,0,0,0)`;
- all measured far dependence is in the environment correction, whose changes
  have nonzero-entry counts `(1,4,5,1)`.

These are exact facts about Block 171's finite matrix. Calling the identity a
probabilistic marginal would require the surrounding Gaussian interpretation,
which is not re-derived here. More importantly, the runner never identifies
Block 171's `Q` with the `A/B/Omega` construction. The Schur result therefore
does not close the covariant-rule selection problem.

## No-Go Discipline Gate

The narrow derived boundary is: **the stated lane signs, target-preimage rank,
and imported Schur identity do not by themselves select one physical
covariant rule.** This is not a claim that no selection theorem can exist.

### N1 — Alternative routes

| Route | Marker | Attempt and outcome |
| --- | --- | --- |
| Scalar lane signs | ATTEMPTED | The exact census contains six admitted ordered pairs, so the signs do not select one. |
| Orthogonality and anticommutation | ATTEMPTED | All six census pairs pass these algebraic tests. |
| Positive-square signature | ATTEMPTED | This removes the four pairs containing `i sy` but leaves both `(sx,sz)` and `(sz,sx)` and supplies no orientation selector. |
| Unique cell preimage | ATTEMPTED | Two unrelated replacement targets receive the same `(16,16,0,0)` certificate at every anchor, so invertibility does not select the Hodge. |
| Block 171 Schur identity | ATTEMPTED | The identity is exact, but no equation maps `A`, `B`, or `Omega` to Block 171's `Q`. |

These routes test distinct proposed selectors: output signs, algebraic class,
signature, target inversion, and record-block structure.

### N2 — Wall independence

The failures are not counted as five independent no-go walls. They are five
tests of one missing ingredient: a selection-and-bridge theorem that chooses
the ordered pair and target and then derives the record matrix from them.

### N3 — Hidden-wall scan

No canonical basis, orientation, standard Dirac-Kähler identification,
Gaussian measure, continuum convention, or background geometry is imported as
a selector. `A=sx`, `B=-sz`, the Hodge target, and Block 171's `Q` are all
declared inputs to their respective calculations.

### N4 — Residual matching

| Artifact | Its residual | Current residual | Match/use |
| --- | --- | --- | --- |
| [Block 190](ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md) | finite lane kernel and fork | pair selection | construction authority only |
| [Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md) | finite Hodge assembly | target selection | target authority only |
| [Block 171](ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md) | finite record bench | missing `A/B/Omega -> Q` bridge | exact independent evidence only |
| This runner | six-pair census and replacement-target controls | non-selection from current premises | direct exact witnesses |

No prior no-go is counted as proof of the present boundary.

### N5 — Rhetoric audit

The five execution-certificate lines below are byte-identical to the primary
runner output. They preserve the exact positive results and identify the
unexecuted selection steps at the relevant resolutions.

### N6 — Partial-closure paths

At least three non-axiom routes remain open: derive an orientation/signature
selector from the finite construction; derive the Hodge from the selected
pair rather than declaring it; or construct an exact map from the selected
pair and Hodge to Block 171's `Q`. Any one would add real information; all
three together would support the proposed one-rule interpretation.

### N7 — Steelman

The strongest hostile case is that the surrounding lattice construction may
already contain an orientation convention, positive-signature condition,
target-selection equation, and record-action map which this block failed to
encode. If supplied and gated, those data could select one pair and make the
four exact result blocks parts of one construction. Therefore the broad claim
that such an identification is impossible is withdrawn. Only non-selection by
the presently executed premises is retained.

### N8 — Cross-cycle echo

[Block 200](ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_ROBUSTNESS_BOUNDARY_PACKAGE_BOUNDED_THEOREM_NOTE_2026-08-26.md)
likewise separates exact finite evidence from an unproved identity bridge. Its
retirement mechanism is analogous but not identical: add a theorem carrying
finite calculations to the stronger identification. No cited landed artifact
supplies the selection-and-bridge theorem used here.

**Gate disposition:** `PASS` for the narrow exact non-selection witnesses;
`FAIL/WITHDRAWN` for qualified or unqualified uniqueness, unique Hodge
selection, a same-rule identification with Block 171, or any claim that no
future selection theorem can exist.

N5: per_element: The declared matrix pair is an exact finite exhibit, not a selected dynamical or physical rule; zero objects are registered or adopted.
N5: per_site: The twist dictionary is gated only on Z_6 x Z_4, and the even/odd contrast is reported only for the four measured extents.
N5: per_mode: Rank-16 cell inversion is target-conditional encodability; two unrelated replacement targets receive the same exact certificate, so no Hodge target is selected.
N5: per_block: The real Cl(3,0) exhibit and the imported Block 171 Schur identities remain separate exact results because no same-rule bridge is supplied.
N5: lattice_wide: The six-pair census and rational counterexample defeat uniqueness from lane signs alone; no generic-parameter, continuum, gravity, or Nature claim is made.

## Arithmetic controls

- Every runner input is exact SymPy integer, rational, or symbol.
- The runner contains no `nsimplify` call and no Python float literal.
- The imported Hodge helper is checked for returned SymPy `Float` atoms at all
  argument patterns used here.
- The baseline contains `34` checks in families `A` through `H` and `34`
  declared claim-only mutations. Each mutation must fail exactly its assigned
  family.
- Primary stdout is kept below the repository runner-output ceiling.

## Limitations and reopen conditions

Not supplied:

- a physical or admissibility selector for an ordered generator pair;
- a derivation selecting `shear_hodge(c,v)` from that pair;
- a bridge from `A/B/Omega` to Block 171's `Q`;
- a twist dictionary beyond `Z_6 x Z_4`;
- a general extent-parity theorem;
- a probabilistic derivation of the Block 171 profile;
- dynamics, an energy or mass interpretation, gravity, a continuum limit, or a
  claim about Nature.

Reopen the one-rule identification after a proposed selector and same-rule map
are written as exact equations with independent mutation gates.

## Reproduction

```bash
python3 scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py
python3 scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py --list-mutations
```

## Decision cut

Nothing is registered or adopted. No landed ancestor is edited. The valid
finite spin-diagonalisation, cell-encoding, Clifford, and Block 171 Schur
results are retained as proposal-grade content. The unsupported unique-rule,
unique-target, same-rule, generic-extent, continuum, and Nature readings are
withdrawn.
