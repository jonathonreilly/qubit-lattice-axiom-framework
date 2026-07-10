# Conditional Tick-Cell Selection Under the Translation and Variation Predicates

**Date:** 2026-07-09
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** On the site-licensed, period-2, one-axis unitary-tick surface,
assume a supplied tick--Admissibility realization bridge identifies the fixed
rule's one-site translation covariance with one-site covariance of the tick
modulo local `U(1)` frames, and identifies nonvacuous variation of available
possibilities with nonzero off-site support of that tick. Under this explicitly
supplied bridge, the exact continuous support-stratum classification leaves
only the two dispersive mover families, one at each winding sign. Composing
with the landed dichotomy gives `|v| = 1` edge/tick exactly, with no selection
between the windings. The Lattice and Admissibility axioms state the motivating
clauses but do not supply the realization bridge, a transfer operator, or a
kinetic-branch selector. The result remains conditional on the parent's
site-strict license and unitary-tick readings and on period-2 blocking; it is
one-axis, with larger cells and the simultaneous three-dimensional protocol
open. It makes no primitive or Tier-A registry change and sets no audit status.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.py`](../scripts/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.py)
**Runner cache:**
[`logs/runner-cache/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.txt`](../logs/runner-cache/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.txt)

## Why This Note Exists

The landed dichotomy note leaves this residual:

> P4's surviving content is only "the realized tick is dispersive (nonflat)".

The current Lattice wording includes standard translations, and the current
Admissibility wording says both that the fixed rule is translation covariant
and that available possibilities vary with nearest-neighbor conditions. Those
sentences motivate two matrix predicates on a proposed tick realization.
They do not derive the predicates. The minimal-axiom memo explicitly says
Admissibility is not dynamics and does not choose a transfer operator or a
kinetic branch.

This note therefore isolates the honest algebraic result: if a supplied
realization bridge maps those rule-level clauses to the two tick predicates
below, the licensed period-2 family is selected exactly. Whether such a bridge
holds is a separate open physics question, not a result of this runner.

## Exact Algebraic Statement

The site-licensed Bloch family is

```text
U(z) = [[alpha, p + q/z], [r + s*z, delta]].
```

Torus unitarity gives

```text
p*conjugate(q) = 0,       s*conjugate(r) = 0,
```

and equal row/column normalizations make the total `AB` and `BA` hop norms
equal. The exact nonzero support strata are therefore

```text
none/none, p/r, p/s, q/r, q/s.
```

Orthogonality forces `alpha = delta = 0` on the `p/s` and `q/r` mover
strata. The `p/r` and `q/s` strata contain continuous flat unitary families;
they are not represented by a single matrix.

### Predicate 1: one-site tick covariance

Let `T` be the one-site shift on an even ring. Local `U(1)` frame conjugation
preserves every matrix-element modulus. Hence full covariance of a tick modulo
local frames necessarily implies

```text
M(U) = max_xy ||T U T^dag|[x,y] - |U|[x,y]| = 0.
```

For the general period-2 family, `M(U)=0` is exactly the modulus condition

```text
|alpha| = |delta|,     |p| = |s|,     |q| = |r|.
```

Modulus homogeneity is necessary but not sufficient for full covariance: an
alternating on-site phase is the elementary counterexample. The proof uses
`M(U)=0` only as a necessary filter. It then constructs explicit local gauges
for every surviving mover and verifies full one-site covariance.

### Predicate 2: off-site tick support

Define

```text
O(U) = true  iff  U[x,y] != 0 for at least one x != y.
```

This is a property of the tick matrix, not by itself a statement that the
Admissibility availability sets vary with neighbor conditions. The supplied
tick--Admissibility realization bridge is the additional premise that makes
that identification on this surface.

### Exact support-stratum selection

The two predicates act on the full continuous support strata as follows.

| support stratum | `M(U)=0` on the nontrivial stratum | `O(U)` | result |
|---|---:|---:|---|
| `none/none` | true | false | on-site family removed by `O` |
| `p/r` | false | true | `|p|=|s|=0` would collapse it to on-site |
| `q/s` | false | true | `|q|=|r|=0` would collapse it to on-site |
| `q/r` | true | true | mover `U_R`, winding `-1` |
| `p/s` | true | true | mover `U_L`, winding `+1` |

Thus `M(U)=0` and `O(U)` leave exactly the two mover strata. Since every fully
translation-covariant tick must satisfy `M(U)=0`, and arbitrary phase-decorated
movers are explicitly gauge-uniformizable, the same survivor statement holds
for full one-site covariance modulo the allowed local frames.

On an even ring the mover gauges reduce the hop phases to a common phase `g`.
The cyclic condition is

```text
g^L = product_x h_x,
```

which always has an `L`th-root solution. This establishes full covariance for
both surviving phase-decorated families, not merely modulus covariance.

## Conditional Physical Reading

Under the supplied tick--Admissibility realization bridge, the two matrix
predicates are the tick-level realizations of the quoted translation and
variation clauses. Only under that premise does the exact algebraic selector
discharge the dichotomy's dispersiveness input on this surface.

Both mover determinants are monomials with windings `-1` and `+1`. Their
eigenvalues have cell-momentum slopes `-1/2` and `+1/2`; converting from the
two-site cell to site units gives edge speed `1`, with zero curvature. The
landed dichotomy therefore yields the conditional per-axis statement
`|v| = 1` edge/tick. This is a real-time band statement. It does not supply an
OS0/Wick/readout identification or a value of any separate readout
normalization.

## Refutation And Boundary Legs

**Remove modulus homogeneity.** Off-site support alone admits the continuous
flat `p/r` and `q/s` strata. Thus the off-site predicate alone does not force
dispersiveness.

**Remove off-site support.** A translation-homogeneous on-site tick survives.
Thus the translation predicate alone does not force dispersiveness.

**Leave the unitary surface.** Replacing the `U_R` amplitude `q` by `0.9*q`
gives torus-unitarity residual `0.19`, so the perturbed object is outside the
licensed unitary family.

**Change the representative inventory.** Replacing the displayed `U_R`
representative by EXCHANGE changes the representative-level survivor set to
`{U_L}`. This diagnostic confirms that the executable filter reads the
constructed matrices; the support-stratum proof, not this replacement test,
is the class-wide argument.

**Remove the realization bridge.** The four axioms permit an availability rule
and a tick operator to remain independently supplied. A translation-covariant,
varying availability rule paired with a flat tick, or a neighbor-independent
availability rule paired with a mover tick, is not excluded by this runner.
These are falsifiers of any claim that the axioms alone perform the selection.
They are why the bridge is explicit and why the result remains bounded.

## Proof And Runner Coverage

The runner performs the following checks.

- It derives the allowed Laurent offsets from site distance and the five
  nonzero support strata from the torus-unitarity constraints.
- It derives the exact modulus conditions under a one-site shift and applies
  them to every support stratum, rather than only six matrices.
- It constructs six useful representatives to print site-space reception
  patterns and to exercise the executable predicate filter.
- It probes continuous points in both nontrivial flat strata as corroboration;
  the support-stratum argument is the load-bearing completeness proof.
- It checks determinant windings, mover band slopes, the factor of two from
  cell to site units, flat-family spectra, and the nonunitary rejector.
- It verifies local-frame invariance of the modulus filter and constructs
  explicit phase-uniformizing gauges for both mover families.
- It prints the tick--Admissibility realization bridge as a supplied premise
  that the runner does not derive.

An independent check parameterized both continuous flat strata on a different
ring size and recovered modulus defect `|sin(theta)|`; a manual characteristic-
polynomial reduction independently gives constant spectra for the flat strata
and cell slopes `+/-1/2` for the movers.

## Consequence And Residual

The durable result is an exact algebraic selector on the full licensed
period-2 support classification, conditional on the tick--Admissibility
realization bridge and the inherited site-strict/unitary-tick readings. It
does not derive a realized tick from the four axioms.

The remaining open physics is the realization bridge itself, larger unit
cells, the simultaneous three-dimensional protocol, and any downstream
OS0/readout map. No chirality or winding-sign selection follows.

## Boundaries

- The tick--Admissibility realization bridge is supplied, not derived. The
  Lattice, Qubit, Admissibility, and Record axioms do not choose the tick.
- The result is restricted to the site-licensed, period-2 unitary family for
  one Grassmann component per site. Larger cells remain open.
- The parent's site-strict license and unitary-tick readings are inherited as
  named conditionals. Particle-hole pairing terms remain outside the parent's
  Q-conserving surface.
- The result is one-axis. A simultaneous three-dimensional tick is outside the
  proof.
- Local frames are `U(1)`. Modulus homogeneity is used as a necessary filter;
  full covariance is separately constructed for the surviving movers.
- The claim is class-wide only within the exact five support strata above.
- There is no winding-sign selection, chirality claim, OS0/readout conclusion,
  primitive change, Tier-A change, or assigned audit outcome.

## Dependencies

- [`STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md`](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  - The site-licensed period-2 family, the dichotomy, and the inherited
    site-strict/unitary-tick conditionals.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  - The exact Lattice and Admissibility wording and the explicit boundary that
    Admissibility does not choose dynamics or a kinetic branch.

Context only: `REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md`,
`REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md`,
`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`,
`KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md`,
`KINETIC_BW_OS0_IDENTIFICATION_BRIDGE_INTERFACE_NO_GO_NOTE_2026-06-16.md`.

## Runner And Cache

Primary runner:
[`scripts/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.py`](../scripts/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.py)

Runner cache:
[`logs/runner-cache/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.txt`](../logs/runner-cache/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.txt)

Current local runner result is recorded in the SHA-pinned cache.

## Changelog

- **2026-07-09.** Initial note and deterministic numpy/sympy runner.
- **2026-07-10.** Review-loop iteration 1 made the tick--Admissibility
  realization bridge explicit, removed the unrelated `r=1` readout premise,
  added the class-wide support-stratum proof, and separated modulus homogeneity
  from full local-frame covariance.
