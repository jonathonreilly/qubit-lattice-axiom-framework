# Formation-Weight Law-Expressibility on the Registrable `C_3` Menu — the Licensed Canonical Constructions Give Exactly `{1/3, 1/2}`, so the Residual Is a Finite Selection, Not a Continuum Dial (Bounded Theorem, rhalf block 14)

**Date:** 2026-07-12
**Claim type:** bounded_theorem (conditional canonical-construction
classification on one supplied carrier and its registrable quotient). This
source note adopts no premise and selects no formation weight.
**Proposed claim_scope:** conditional on this note's own Supplied-Object
Canonical-Measure Licensing Criterion, classify the probability assignments
canonically carried by the supplied `C^3` representation of `C_3` with
`K`/CPT conjugation and by its two-cell orbit-constant registrable quotient;
the licensed distinct singlet weights are exactly `{1/3, 1/2}`, the licensed
readout algebra is `C + C`, and no member is selected.
**Primary runner:**
[`scripts/frontier_formation_weight_expressibility_2026_07_12.py`](../scripts/frontier_formation_weight_expressibility_2026_07_12.py)
**Runner cache:**
[`logs/runner-cache/frontier_formation_weight_expressibility_2026_07_12.txt`](../logs/runner-cache/frontier_formation_weight_expressibility_2026_07_12.txt)
(SCORECARD: PASS=18, FAIL=0)

> **Claimed (bounded):** under the note-owned licensing criterion stated first
> in Residual Atoms, the supplied carrier and registrable quotient carry
> exactly two distinct canonical formation assignments: carrier/orbit counting
> gives singlet weight `w = 1/3`, while counting or left-regular/Hilbert-Schmidt
> weighting of the **licensed commutative quotient** gives `w = 1/2`. Thus the
> expressible set is exactly `{1/3, 1/2}`. **Not claimed:** that bare
> functoriality alone proves this completeness, that either value is derived or
> selected, that `w = 1/5` is lawful, or that this classification applies off
> the stated two-cell `C_3` menu.

## Role — classify the residual after its relocation

Block 9
([`KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md`](KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md))
exhibits the exact fork `r = 1` versus `r = 1/2` without selecting a horn.
Block 10
([`RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md))
uses the registrable-readout orbit clause to rule P-odd/K-odd data out of the
record subalgebra. A companion, in preparation, relocates the surviving
residue to a formation probability `(w, 1-w)` on the two registrable cells.
This note does not depend on that companion's file. It answers only the next
question: once the carrier and quotient are fixed, which weights are
expressible by canonical constructions already carried by those supplied
objects?

The convention is

```text
cell probabilities = (w, 1-w) = (singlet, doublet),
r = (1-w)/(2w).
```

Therefore `w = 1/3` gives `r = 1`, while `w = 1/2` gives `r = 1/2`. These are
exact fork arithmetics only; neither implication is a selection.

## Supplied object and the algebra ruling (candidate 3)

In the character basis of the supplied `C_3` carrier `H = C^3`, let

```text
P_s = diag(1,0,0),       P_d = diag(0,1,1),       P_s + P_d = I_3.
```

`K` fixes the trivial-character line and exchanges the two nontrivial
characters. The supplied two-cell menu is therefore `{P_s, P_d}`. Its cell
dimensions are `(d_s,d_d) = (1,2)`, its `K`-orbit cardinalities are
`(s_s,s_d) = (1,2)`, and each cell contributes one minimal central projection.

The registrable-readout theorem
([`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md),
read at `origin/main`) is used only at its declared supplied-context grade:
registrable **scalar** readouts are additive across the finite central-sector
decomposition and constant on `K`/CPT orbits. On this menu, an orbit-constant
readout has the form

```text
x_s P_s + x_d P_d = diag(x_s,x_d,x_d).
```

Hence the licensed registrable-readout algebra is the function algebra on the
two cells,

```text
A_reg = span_C{P_s,P_d} ~= C + C,
```

not the carrier block algebra `C + M_2`. The latter contains arbitrary
operators internal to the doublet. In particular
`D = diag(0,1,-1)` belongs to `C + M_2` but is sent to `-D` by the doublet
swap; it is P-odd/K-odd and is not constant on the `K` orbit. Licensing
`C + M_2` would therefore reintroduce precisely the within-doublet data that
the orbit clause excludes. This conclusion is no stronger than that supplied
orbit clause: if a later authority licenses internal doublet matrix readouts,
candidate 3 must be recomputed on the enlarged object.

Consequently the left-regular representation of the **licensed** algebra has
one basis direction in each simple summand. Its minimal central projections
have regular ranks `(1,1)`, so normalized left-regular/Hilbert-Schmidt
weighting gives `w = 1/(1+1) = 1/2`. The tempting `w = 1/(1+2^2) = 1/5`
belongs to the unlicensed `C + M_2` block algebra and is not expressible on
`A_reg`.

## Candidate-by-candidate classification

| candidate | canonical object actually used | exact singlet weight | disposition |
|---|---|---:|---|
| 1. restriction of carrier trace | normalized trace on `H = C^3` | `Tr(P_s)/Tr(I_3) = 1/3` | **licensed** |
| 2. count minimal central projections | atomic count on `{P_s,P_d}` | `1/(1+1) = 1/2` | **licensed** |
| 3. left-regular / Hilbert-Schmidt block count | regular module of `A_reg = C + C` | `1/(1+1) = 1/2` | **licensed, coincides with 2** |
| 3-alt. use `C + M_2` | regular module of an enlarged block algebra | `1/(1+4) = 1/5` | **not licensed** |
| 4. count members of each `K` orbit | orbit counting `(1,2)` | `1/(1+2) = 1/3` | **licensed, coincides with 1** |

Candidates 1 and 4 are different descriptions in general: one counts carrier
dimension and the other counts orbit members. On this fixed carrier they agree
cell by cell because `d_i = s_i` for both cells. No supplied invariant on this
carrier separates their probability assignments, so they are one element of
the set of distinct weights, with two canonical provenance descriptions.

## T1 — the licensed candidate set is finite and exact

> **T1.** Under the Supplied-Object Canonical-Measure Licensing Criterion, the
> set of distinct law-expressible singlet weights on the supplied two-cell menu
> is
>
> ```text
> W_expr = {1/3, 1/2}.
> ```

The supplied objects carrying canonical finite measures are: the carrier
`H`, whose trace gives cell ranks `(1,2)`; the `K`-orbit set, whose counting
measure gives `(1,2)`; the two quotient atoms, whose counting measure gives
`(1,1)`; and the regular module of the licensed algebra `A_reg = C + C`, whose
ranks are again `(1,1)`. Normalizing these four vectors produces only
`(1/3,2/3)` and `(1/2,1/2)`. The table exhausts the supplied objects admitted
by the criterion, so the distinct set is finite. The completeness step is
conditional on that criterion; the individual trace, orbit-counting,
atom-counting, and regular-rank computations are not.

## T2 — both fork endpoints are lawful members, neither is selected

Let

```text
rho_dim  = I_3/3,
rho_cell = diag(1/2,1/4,1/4).
```

Then `Tr(rho_dim P_s) = 1/3`, `Tr(rho_dim P_d) = 2/3`, and `r = 1`; while
`Tr(rho_cell P_s) = 1/2`, `Tr(rho_cell P_d) = 1/2`, and `r = 1/2`. Thus both
fork endpoints are realized by positive, unit-trace, K-even density operators
and both belong to `W_expr`. Block 9 supplies the exact `r = 1`/`r = 1/2`
fork at its bounded grade. The graded-constraint companion, read once as
`origin/claude/science/rhalf-graded-constraint-boundary-20260711:docs/GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md`,
identifies `rho_dim = I_3/3` as the full-symmetry zero-information point and
`rho_cell` as the designated-two-cell per-cell-equipartition point, conditional
on that note's own proposed-surface hypotheses. Those identifications prove
lawfulness and arithmetic, not a preference.

## T3 — the dial changes species, conditionally and without a selection

> **T3.** If T1's licensing criterion is accepted, the formation-weight
> residue is no longer “derive an arbitrary real `w`.” It is “select one member
> of the finite lawful set `{1/3, 1/2}`.”

The only registration-compatibility result presently named for the relocation
is the companion block, in preparation. Block 10 and the registrable-readout
source fix why the menu must be P-even/K-even; they do not choose a measure on
that menu. The companion locates the probability at formation and checks its
registration compatibility; it supplies no selector between carrier trace and
quotient-atom count. No other selection argument is landed at the grades
consumed here. In particular, symmetry of the unequal-rank two-cell menu,
maximum entropy, dynamics, a preferred state, and a preference for one
canonical trace over another are not supplied. **This note selects nothing.**

## T4 — robustness away from the present menu

> **T4.** The classification tracks the supplied invariants rather than the numerals `1`, `2`, and `3`: on a hypothetical two-cell carrier with dimension and orbit-size vectors `(1,3)` and the same commutative two-atom quotient, carrier/orbit counting gives `w = 1/(1+3) = 1/4` while quotient counting and its regular trace still give `w = 1/2`, so the distinct set becomes `{1/4,1/2}`; on a hypothetical menu of three structurally identical singleton cells, all four licensed constructions give the single probability vector `(1/3,1/3,1/3)`. Thus changing the supplied cell structure changes, or can collapse, the classified set; the present `{1/3,1/2}` is not exported to other menus.

## Completeness sweep — what the supplied invariants do and do not license

The cellwise invariant vocabulary visible at the stated quotient is

| invariant | singlet cell | doublet cell | use at this grade |
|---|---:|---:|---|
| carrier dimension `d_i` | `1` | `2` | carrier trace |
| `K`-orbit size `s_i` | `1` | `2` | orbit counting |
| number of quotient atoms represented by the cell | `1` | `1` | central-projection counting |
| regular rank in `A_reg = C + C` | `1` | `1` | licensed regular/HS trace |
| `C_3` representation type modulo `K` | trivial singleton | unordered nontrivial conjugate pair | identifies the two cells and reproduces the orbit multiplicity; supplies no further positive measure |

The eigencharacters of the **group action** are structural, but after the
`K` quotient their orientation is only the unordered pair `{omega,omegabar}`.
By contrast, numerical eigenvalues of a circulant coupling, mass operator, or
state are coupling/state dependent and are not supplied invariants. Weighting
by such values would import the very state-dependent choice excluded by the
classification target. A chosen group-algebra polynomial, spectral projector,
Laplacian, or Casimir can also be written down from the representation, but a
choice of which positive polynomial or which spectral functional is to become
the formation measure is not carried by the registrable quotient. Under the
licensing criterion it is an additional construction, not an automatic new
weight. If such a formation operator is later supplied, T1 must be enlarged.
For maximal clarity, normalizing `P_s` or `P_d` as a density operator would
give the exact endpoint weights `w = 1` or `w = 0`, and normalizing the
canonical `C_3` graph Laplacian would again support only the nontrivial sector,
giving `w = 0`. SOCMLC excludes these not because their algebra is wrong, but
because each turns a chosen cell/spectral operator into the formation state;
that choice is not supplied. This is a direct, contestable boundary example.

The family most likely to disguise an external dial is

```text
f_i = d_i^alpha,          w(alpha) = 1/(1 + 2^alpha).
```

It is a genuine continuum when `alpha` is free, so it is not law-expressible.
Nor does declaring `alpha` to be an integer make every power structural:
`alpha = 0` is licensed here by quotient-atom counting, `alpha = 1` by the
carrier trace, and a square is licensed only when an actual regular/HS block
construction supplies it. For the actual quotient that construction squares
the simple-block dimensions `(1,1)`, not the carrier cell dimensions `(1,2)`.
No supplied tensor-power carrier or `C + M_2` readout algebra licenses
`d_i^2`, and no named construction licenses higher powers. Likewise formulas
such as `d_i+1`, indicator functions of a representation label, or arbitrary
polynomials are invariant **formulas** but not canonical measures carried by a
supplied object. Admitting all such formulas would defeat finiteness; excluding
them is exactly the contestable judgment isolated as Residual Atom 1.

For comparison, the symmetries alone allow the whole K-even state family

```text
rho(w) = diag(w, (1-w)/2, (1-w)/2),       0 <= w <= 1.
```

This family shows why “K-even and functorial-looking” is not itself a
selection law. T1 classifies the canonical measures carried by the supplied
objects under the named criterion; it does not claim that representation
symmetry mathematically forbids all other invariant density operators.

## Residual Atoms

1. **Supplied-Object Canonical-Measure Licensing Criterion (SOCMLC; this
   note's own named element).** A menu probability is licensed only when its
   unnormalized cell masses are the ranks or multiplicities of a canonical
   finite measure/trace on an object actually supplied here: the carrier, the
   `K`-orbit set, the quotient atom set, or the regular module of the licensed
   quotient algebra. Normalization must then be forced. Merely writing a
   parameter-free invariant formula, choosing a positive group-algebra
   polynomial, selecting a cell, or applying an unprovided tensor/power
   functor does not license a formation measure. This is stricter than bare
   mathematical naturality and is a classification convention, not a theorem
   derived from the minimal axioms. A hostile reader who rejects SOCMLC
   rejects T1's **finiteness/completeness**, not any candidate arithmetic or
   the `A_reg = C + C` ruling.
2. **The supplied-context orbit clause.** The conclusion that registrable
   scalar readouts are constant on the doublet is consumed at the
   registrable-readout note's bridge-carried declared grade, not as generic
   Record-axiom content. Enlarging the physical readout algebra beyond that
   clause could license `C + M_2` and add `1/5`.
3. **The formation selector.** Neither the minimal axioms nor the supplied
   carrier/quotient chooses between their two canonical measures. The
   Qualification in
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) bars an
   unfixed choice, while that memo explicitly leaves formation weights outside
   axiom content. This note supplies no selector.
4. **The fixed-menu scope.** The carrier is exactly `C^3`, the group action is
   exactly the supplied `C_3` action with `K` conjugation, and the registrable
   menu is exactly the singlet/doublet quotient. T4 shows why changing those
   invariants requires a new classification.

## What This Does Not Claim

- **Not** a derivation, selection, or preference for `w = 1/3`, `w = 1/2`,
  `r = 1`, or `r = 1/2`. Both assignments remain lawful and unselected.
- **Not** an unconditional theorem that all parameter-free natural
  transformations of the representation form a two-element set. T1 is
  conditional on SOCMLC, and that boundary is deliberately exposed.
- **Not** a universal rejection of `C + M_2`. It is unlicensed as the
  registrable scalar-readout object at the quoted orbit-constancy grade; an
  independently supplied noncommutative doublet readout would change the
  problem.
- **Not** a use of coupling eigenvalues, observed values, fitted inputs,
  comparators, thresholds, or orientation data. All arithmetic is exact and
  structural.
- **Not** a classification for a different carrier, a refined menu, a menu
  with different orbit sizes, or a three-cell registration. T4 gives only
  exact counterfactual checks of dependence on those invariants.
- **Not** a premise adoption or a change to any status surface.

## Reprove-and-cite ledger

- **Reproven here (runner):** the two projectors and their ranks; the `K` swap
  and the P-odd internal-doublet witness; the orbit-constant algebra
  `A_reg = C + C`; all five candidate arithmetics including the excluded
  `C + M_2` value; equality of carrier dimension and orbit size on this
  carrier; the exact set deduplication; both density operators, their K
  invariance, their menu probabilities, and the fork map to `r`; the
  nonconstant `d^alpha` family at its structural test points; the full K-even
  invariant state family as a no-selection guard; and both T4 counterfactuals.
- **Cited at declared grade:** block 9's exact fork; block 10's P-evenness
  ruling; the registrable-readout theorem's bridge-carried orbit constancy and
  scalar-additivity scope (read from `origin/main`); the minimal-axiom
  Qualification and explicit exclusion of formation weights; and the
  branch-qualified graded-constraint companion's exact `rho_dim`/`rho_cell`
  identifications, conditional on its proposed-surface hypotheses. The
  relocation/registration-compatibility companion is cited only as
  **“companion, in preparation”** and no file content is consumed.

## Verification

```bash
python3 scripts/frontier_formation_weight_expressibility_2026_07_12.py
python3 scripts/precompute_audit_runners.py --push-mode none --force --runners scripts/frontier_formation_weight_expressibility_2026_07_12.py
```

Expected: 18 numbered `[PASS]` lines, then `TOTAL: PASS=18 FAIL=0`, followed by
a short verdict-first summary. Exit code is 0 iff `FAIL=0`.
