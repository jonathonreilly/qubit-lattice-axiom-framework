# Tick-Cell Selection by the Translation and Variation Clauses

**Date:** 2026-07-09
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** On the landed site-licensed period-2 one-axis tick surface,
the current minimal-axiom wording supplies two load-bearing clauses: one-site
translation covariance of the fixed rule, evaluated at the site-modulus level
under the local `U(1)` gauge quotient, and nonvacuous variation with
nearest-neighbor conditions. Over the landed unitary cell classification, the
survivors of both clauses are exactly the two dispersive mover cells, one at
each winding sign. Composing this result with the landed dichotomy gives
`|v| = 1` edge/tick exactly, with no selection between the two windings. The
flat gapped cell family realizes nonvacuous varying conditioning and is
excluded by the translation clause; the vacuous diagonal family is excluded
by the variation clause. Scope: period-2 blocking, with larger unit cells a
named open; the parent's `P1'`/`P2` premises and readout normalization `r=1`
are inherited as named conditionals; the result is one-axis, while the `3D`
protocol question belongs to the sibling note; there is no `Tier-A` registry
change, and this note does not modify the registered kinetic-isotropy
primitive or set an audit status.
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:**
[`scripts/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.py`](../scripts/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.py)
**Runner cache:**
[`logs/runner-cache/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.txt`](../logs/runner-cache/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.txt)

## Why This Note Exists

The landed dichotomy note leaves this exact residual sentence:

> P4's surviving content is only "the realized tick is dispersive (nonflat)".

This note supplies that bit on this surface from two clauses in the current
minimal axioms. The Lattice wording is:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

The Admissibility translation clause is:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

The Admissibility variation clause is:

> For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions.

Here standard translations include one-site steps. The period-2 cell is an
analysis device, not extra axiom structure. For one Grassmann component per
site, the allowed site frames are local `U(1)` phases; matrix-element moduli
are therefore gauge invariant. Particle-hole pairing terms remain
outside the parent's Q-conserving surface declaration.

## Statement

The classified Bloch family is

```text
U(z) = [[alpha, p + q/z], [r + s*z, delta]].
```

Torus unitarity computes `p*conjugate(q)=0` and
`s*conjugate(r)=0`. Together with normalization balance, the support branches
are `none/none`, `p/r`, `p/s`, `q/r`, and `q/s`; orthogonality forces
`alpha=delta=0` on the two mover branches. The six named representatives are
DIAGONAL, EXCHANGE, PAIRING, UMIX at `theta=pi/4`, `U_R`, and `U_L`.

**T1 - translation-clause computation.** Unrolling the representatives into
`8x8` site matrices on the `L=8` ring gives these one-site modulus defects:

| cell | defect |
|---|---:|
| DIAGONAL | `0.000000000000` |
| EXCHANGE | `1.000000000000` |
| PAIRING | `1.000000000000` |
| UMIX | `0.707106781187` |
| `U_R` | `0.000000000000` |
| `U_L` | `0.000000000000` |

DIAGONAL is on-site. Every `U_R` row receives from its left neighbor and every
`U_L` row from its right neighbor. EXCHANGE, PAIRING, and UMIX alternate their
off-site reception direction with parity. Five random local phase gauges per
cell preserve every modulus and the defect. Explicit gauges for both movers
also make their hop phases uniform and give full one-site covariance; on the
even ring, the computed global phase satisfies `g^L=product(hop phases)`.

**T2 - variation-clause computation.** The primary site-level functional asks
whether any off-diagonal site-matrix entry is nonzero. It is false only for
DIAGONAL and true for every other representative. The secondary blocked
coefficient-algebra dimensions are:

| cell | site-level conditioning | blocked dimension |
|---|---:|---:|
| DIAGONAL | false | `1` |
| EXCHANGE | true | `1` |
| PAIRING | true | `4` |
| UMIX | true | `4` |
| `U_R` | true | `4` |
| `U_L` | true | `4` |

The blocked functional is blind to within-cell bonds: EXCHANGE has blocked
dimension `1` despite genuine site-level conditioning. This is why the
site-level functional is primary.

**T3 - selection.** Applying both computed clauses leaves exactly
`{U_R, U_L}`. Their determinant windings are `-1` and `+1`. Both survive, so
there is no selection between the two windings and no chirality claim.

**T4 - dichotomy composition.** On the momentum grid, the mover spectra match
the exact cell-momentum slopes `-1/2` and `+1/2`. Thus both have edge speed
`1` and curvature `0`. EXCHANGE, PAIRING, and UMIX have flat spectra. The
landed dichotomy therefore turns the selected nonflat cells into the exact
per-axis statement `|v| = 1` edge/tick on this surface.

**R1 - remove translation.** The conditioning-only survivors are
`{EXCHANGE, PAIRING, UMIX, U_R, U_L}`. The three named flat cells survive, so
the variation clause alone does not force dispersiveness; in particular, the
flat UMIX family is a nonvacuous varying witness.

**R2 - remove variation.** The translation-only survivors are
`{DIAGONAL, U_R, U_L}`. DIAGONAL survives while its site-level conditioning is
false. Both clauses are load-bearing.

**R3 - unitarity rejector.** Replacing the `U_R` amplitude `q` by `0.9*q`
computes torus-unitarity residual `0.190000000000`, so the perturbed object is
outside the licensed unitary inventory.

**R4 - inventory rejector.** Replacing `U_R` by EXCHANGE before running the
same two-clause filter changes the survivor set to `{U_L}`. The selection gate
therefore reads the constructed cell data.

## Proof Sketch

The runner proceeds in the following probe-first order.

- `S1` derives the licensed offsets from site distance, extracts the Laurent
  coefficients of the torus-unitarity equations, enumerates the allowed
  support branches, and derives the zero diagonal amplitudes of the movers.
- `S2` constructs the six representatives, verifies torus unitarity, computes
  their determinants, and extracts windings `0`, `-1`, and `+1` from those
  determinants.
- `S3` unrolls each Bloch cell on the ring and prints every site-space modulus
  matrix and reception row before checking the reception patterns.
- `S4` computes
  `max_xy ||T U T^dag|[x,y]-|U|[x,y]|` and probes positive UMIX angles through
  `pi/2`.
- `S5` applies five deterministic random local phase gauges to each cell and
  checks modulus and defect invariance.
- `S6` computes the primary off-diagonal site functional, then forms the
  unital `*`-algebra generated by the two cross-cell coefficient blocks and
  records its dimension.
- `S7` applies both clause predicates to the computed inventory and reads the
  two mover survivors and their opposite windings.
- `S8` recomputes the bands on a momentum grid, matches the mover spectra to
  the exact half-cell slopes, and checks the three flat-cell spectra.
- `S9` reruns the filter with each clause removed.
- `S10` tests the nonunitary amplitude perturbation and the wrong inventory.
- `S11` uses three deterministic random phase seeds per mover, constructs the
  cyclic local gauges, checks the product condition, and verifies full
  one-site covariance after gauging.

All selection predicates consume the printed matrices or tables. In
particular, the wrong-inventory leg changes the answer instead of reproducing
the target set.

## Consequence And Residual

This supplies the dispersiveness input of the per-axis chain on the stated
site-licensed period-2 surface. Composed with the landed dichotomy, it gives
the exact speed statement while preserving both winding signs.

The named conditionals remain: the parent's `P2` unitary-tick reading, the
readout normalization `r=1` from the landed interface no-go, the periodicity
scope, selection of the `3D` protocol in the sibling analysis, and class-level
transport beyond the representative surface. The `P1'` site-strict reading is
also inherited. This note makes no registry change and does not modify the registered kinetic-isotropy primitive.

The next path this opens is the `3D` protocol-selection sibling together with
the larger-periodicity extension; neither is supplied here.

## Boundaries

- The result is restricted to the landed site-licensed period-2 unitary cell
  inventory for one Grassmann component per site.
- It is a one-axis statement. A simultaneous `3D` tick is outside this proof.
- Larger unit cells remain a named open.
- The local gauge quotient is `U(1)`. Matrix phases may carry gauge or flux
  content, while the selection functional uses site-matrix moduli.
- The parent's Q-conserving declaration is inherited; particle-hole pairing terms
  are outside this surface.
- The current axiom wording is used as a premise. No claim is made about other
  admissibility wordings.
- There is no selection between the two windings, no chirality claim, no
  `Tier-A` registry change, and no audit outcome is assigned.

## Dependencies

- [`STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md`](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  - The site-licensed period-2 dichotomy and its P4 residual.
- [`REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md`](REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md)
  - The variation-clause selection pattern and note structure.
- [`REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md`](REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md)
  - The site-primary and blocked-algebra conditioning semantics.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  - The quoted Lattice and Admissibility clauses.

Context only: `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`,
`KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md`.

## Runner And Cache

Primary runner:
[`scripts/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.py`](../scripts/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.py)

Runner cache:
[`logs/runner-cache/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.txt`](../logs/runner-cache/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.txt)

Current local runner result:

```text
TOTAL: PASS=31 FAIL=0
```

## Changelog

- **2026-07-09.** Initial narrow theorem note and deterministic numpy/sympy
  runner. The runner reports `TOTAL: PASS=31 FAIL=0`.
