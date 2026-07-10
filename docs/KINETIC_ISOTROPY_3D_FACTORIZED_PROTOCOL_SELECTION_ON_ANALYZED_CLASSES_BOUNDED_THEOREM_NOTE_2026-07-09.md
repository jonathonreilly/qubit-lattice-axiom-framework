# Conditional 3D Protocol-Factor Filtering on the Analyzed Period-2 Classes

**Date:** 2026-07-09
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** Algebraic predicate-filter theorem for the named ten-member
period-2 protocol inventory on the one-Grassmann-per-site `Z^3` carrier. The
factor-modulus-homogeneity filter, the nonvacuous all-axis factor-support
filter, and the composite-word dispersiveness filter compute the four-member
candidate set `{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT}`. A conditional
physical reading requires a separately supplied 3D protocol--Admissibility
realization bridge and a supplied word-level dispersiveness condition. The
filters are necessary shadows of the quoted rule-level clauses, not a proof of
full protocol covariance or a derivation of the realized protocol. The
stronger survivor-equivalence and unit-slope characterization fails on this
inventory because of the explicit `P_WEIGHT` representative.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.py`](../scripts/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.py)
**Runner cache:**
[`logs/runner-cache/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.txt`](../logs/runner-cache/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.txt)

## Why This Note Exists

The landed 3D note names this underived realization input:

> The load-bearing extra input is the **factorized-realization input**: the realized 3D protocol is the symmetric per-axis decorated-shift cycle. This note does not derive that selection.

This note tests three explicit algebraic predicates on a finite protocol
inventory. It does not identify those predicates with Admissibility by fiat.
The current
[`TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md`](TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md)
makes the relevant boundary precise in one axis: a tick--Admissibility
realization bridge is supplied, modulus homogeneity is necessary but not
sufficient for full local-frame covariance, and the simultaneous 3D protocol
remains open. This note preserves that boundary at protocol-factor level.

The computed filters exclude the named nonfactorized competitors, but they do
not recover the symmetric cycle uniquely. The weighted word `P_WEIGHT` passes
all three filters while failing the stronger residual-equivalence and
unit-slope tests.

## Supplied Conditional Physical Reading

The algebraic table below is unconditional on its stated constructions. To
read it as a necessary filter on a realized Admissibility protocol, one must
separately supply both of the following inputs.

1. **3D protocol--Admissibility realization bridge.** A realized sequential
   protocol is supplied with the constituent-factor semantics used here;
   translation covariance of the fixed rule requires each constituent factor
   to be fully covariant modulo local `U(1)` frames and therefore to have zero
   site-modulus translation defect; nonvacuous variation together with proper
   cubic axis transitivity requires nonzero constituent-factor support on all
   three axes. The two computed factor predicates are only necessary
   consequences of this bridge. Their converses are not claimed.
2. **Composite-word dispersiveness condition.** The realized composite word
   is supplied to be dispersive in the characteristic-polynomial sense used
   by the runner. The current Wave A note proves a one-axis conditional result
   under its own bridge; it does not supply this simultaneous word-level
   condition.

Even with those inputs, the conditional conclusion is only this: if the
realized protocol lies in the named inventory, it must lie in the computed
four-member candidate set. The runner does not establish full proper-cubic
covariance of every candidate, exhaust all protocol classes, or select which
candidate is realized. In particular, binary all-axis factor support is much
weaker than full protocol covariance.

## Computed Divergences From The Stronger Characterization

The stronger tested characterization says that every three-filter survivor is
the symmetric cycle up to octant choice, a central sign, and central quantized
whole-cell translations. The runner computes three narrower facts.

1. The constructed `P_WEIGHT = S_1 S_1 S_2 S_3` obeys
   `P_WEIGHT = exp(-i k_1) S_2 S_3`; it is not the symmetric three-axis cycle
   times a central scalar. Therefore the stated residual-equivalence does not
   hold for every survivor in this inventory.
2. The same word has composite site-slope magnitudes `(2,1,1)`, not
   `(1,1,1)`. Every elementary decorated mover still has magnitude one on its
   own axis.
3. `P_MIX4` and `P_STAIR` pass a support-and-dispersion-only filter, but they
   do not pass removal of factor-modulus homogeneity when the all-axis binary
   support requirement is retained. Their `[1,1,0]` pattern is independently
   removed by that support requirement, so the factor-modulus filter has no
   unique exclusion witness in this ten-member inventory.

## Algebraic Statement

The motivating framework clauses are:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

> For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions.

Translations here are the standard one-site translations of `Z^3`; the
period-2 blocking is an analysis device. Local `U(1)` site frames preserve
matrix-element moduli. Thus full factor covariance would imply the
factor-modulus test used below, but zero modulus defect alone does not imply
full covariance. The alternating diagonal protocol is an explicit false
positive at that intermediate filter. Likewise, proper cubic rotations act
transitively on axes, but binary all-axis factor support is only a necessary
shadow of full protocol covariance.

The constructed inventory and full pre-filter probe are:

| Protocol | Constructed word or tick | Maximum constituent-factor modulus defect | Constituent-factor support | Support uniform | Composite dispersive |
|---|---|---:|---:|---:|---:|
| `P_SYM` | `S_1 S_2 S_3` | `0` | `[1,1,1]` | yes | yes |
| `P_SYM_OCT` | `S_1^- S_2 S_3`, with the reverse mover constructed from reversed offsets | `0` | `[1,1,1]` | yes | yes |
| `P_REORDER` | `S_2 S_1 S_3` | `0` | `[1,1,1]` | yes | yes |
| `P_WEIGHT` | `S_1 S_1 S_2 S_3` | `0` | `[1,1,1]` | yes | yes |
| `P_AXIS` | `S_1`, with decorated and bare forms checked | `0` | `[1,0,0]` | no | yes |
| `P_MIX4` | planar mixed four-cycle | `1` | `[1,1,0]` | no | yes |
| `P_STAIR` | planar parity-conditioned staircase | `1` | `[1,1,0]` | no | yes |
| `P_PAIRFLAT` | commuting-pairing product at `theta=pi/5` | `0.38471` | `[1,1,1]` | yes | no |
| `P_CANCEL` | opposite decorated movers paired on every axis | `0` | `[1,1,1]` | yes | no |
| `P_DIAG` | diagonal period-2 phases | `0` | `[0,0,0]` | yes | no |

The computed filter sequence is:

- **Factor-modulus-homogeneity filter.** The zero-defect set is
  `{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT, P_AXIS, P_CANCEL, P_DIAG}`.
  This is a necessary-condition set, not the set of fully covariant protocols.
- **Nonvacuous all-axis factor-support filter.** The set becomes
  `{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT, P_CANCEL}`. Support is read from
  constituent factors, not from the composite matrix; `P_CANCEL` therefore
  passes this filter even though its composite is the identity.
- **Composite-word dispersiveness filter.** The set becomes
  `{P_SYM, P_SYM_OCT, P_REORDER, P_WEIGHT}`.
- **Survivor-structure test.** The runner recomputes pairwise decorated
  anticommutation, `P_REORDER = -P_SYM`, and
  `S_i^2 = exp(-i k_i) I`. It also constructs the octant variant directly.
  For the specified weighted word, however,
  `P_WEIGHT = exp(-i k_1) S_2 S_3`, and a scalar-multiple test against
  `P_SYM` is false. The residual-equivalence characterization is therefore
  false for this computed candidate set.
- **Composite-slope test.** `P_SYM` and `P_SYM_OCT` have composite site-slope
  magnitudes `(1,1,1)`. `P_MIX4` and `P_STAIR` have
  `(1/2,1/2,0)`. Each decorated mover has magnitude one on its own axis, but
  the specified `P_WEIGHT` composite has `(2,1,1)`.

## Proof Sketch

The runner reconstructs the `2^3` Bloch-cell and `L=4` site-ring operators,
the eta-decorated shifts, the mixed cycle, the staircase, the site-license
degree table, and the `P12` plus `Vg = diag((-1)^(p0*p1))`
projective-covariance check. Every inventory member and every elementary
factor is checked for unitarity on both representations. The opposite-axis
mover is built from the reversed offset convention before its inverse
relation is tested.

For each constituent factor `F`, the runner evaluates
`max_a max_entries ||T_a F T_a^dag|-|F||`. It scans actual site-level
nearest-neighbor support of the factor list to obtain the binary support
vector. Momentum dependence of the composite word is tested through
characteristic-polynomial coefficients at fixed momenta, avoiding band-order
assumptions. These are three different resolutions; the runner does not
silently identify factor support with composite support. It explicitly checks
that `P_CANCEL` has factor support `[1,1,1]` but composite support `[0,0,0]`,
and that `P_DIAG` has zero modulus defect while failing full local-frame
covariance because diagonal local frames cannot change its translated phases.

For `P_PAIRFLAT`, the three `M_i` are pairwise commuting Hermitian unitaries.
Their product is unitary, has momentum-independent bands
`exp(i theta (s_1+s_2+s_3))` for `s_i` in `{-1,+1}`, and passes the explicit
`P12` axis-permutation conjugation. Its constituent-factor site-modulus defect
is positive, so the weak factor-support predicate by itself does not force
dispersiveness.

The exact fourth-power identities give the mixed-cycle and staircase slope
magnitudes `(1/2,1/2,0)`. The central mover-square identities give one edge
per tick for each elementary decorated factor. Direct composite-square
identities give `(1,1,1)` for the symmetric and octant words and `(2,1,1)`
for the specified weighted word.

The removal and rejector checks are:

- A support-and-dispersion-only filter admits `P_MIX4` and `P_STAIR`, both
  with nonunit quantized slopes. Removing only factor-modulus homogeneity
  while retaining all-axis binary support does not admit either protocol.
- Removing all-axis support uniformity admits `P_AXIS`.
- Removing composite-word dispersiveness admits flat composite `P_CANCEL`.
  The word-level condition is therefore load-bearing and separately supplied.
- `P_PAIRFLAT` is `P12`-axis-permutation covariant, has all-axis factor
  support, is flat, and has positive factor-modulus defect.
- Replacing eta-decorated factors by bare shifts preserves all three weak
  protocol filters. The bare factors commute, while the decorated factors
  anticommute. Thus the filters do not select the eta decoration or flux
  class; those come from the landed parent chain.
- Replacing `P_SYM` by `P_MIX4` changes the computed three-filter stack; the
  candidate set contains `P_SYM`, while the corrupted set does not.

## Consequence And Residual

The durable result is the exact four-member candidate set under three named
algebraic filters on the stated inventory. It is not a derivation of the
factorized-realization input. Under the separately supplied 3D
protocol--Admissibility bridge and word-level dispersiveness condition, it is
only a necessary candidate filter for a realized protocol already known to
lie in this inventory.

The specified `P_WEIGHT` representative prevents extending the filter result
to the stronger residual-equivalence or unit-slope characterization. A full
proper-cubic protocol-covariance theorem, a one-mover-per-axis word-domain
restriction, or a class-transport theorem could prune the candidate set; none
is supplied here.

The remaining boundaries are:

- octant and handedness choice;
- the central sign from factor ordering;
- quantized whole-cell translation factors, with the parity of the remaining
  decorated-mover word kept explicit;
- the supplied word-level dispersiveness condition;
- period-2 scope; the mod-3 six-cycle staircase variant lives outside the
  analyzed cell;
- representative inventory and class transport;
- the inherited unitary-tick reading.

This note does not modify the registered kinetic-isotropy primitive and does
not alter the eta decoration class supplied by the landed parent chain.

## No-Go Discipline Gate For The Computed Divergence

The negative content is only the representative-level statement that the
specified residual-equivalence characterization fails for the computed
candidate set because `P_WEIGHT` is an explicit counterexample. It is not a
class-wide no-go against stronger protocol selection.

### Alternative-route enumeration (No-Go Discipline N1)

All routes below were attempted on the stated inventory by the primary runner
and independently reduced with the Clifford word relations.

1. Remove `P_WEIGHT` with factor-modulus homogeneity: it has zero defect.
2. Remove it with nonvacuous all-axis factor support: its support is
   `[1,1,1]`.
3. Remove it with composite-word dispersiveness: its characteristic
   polynomial depends on momentum.
4. Absorb it by factor reordering: anticommutation supplies central signs but
   does not restore the missing odd `S_1` factor.
5. Absorb it by octant reversal: octant cycles retain one odd mover on every
   axis, whereas the weighted word has even first-axis mover parity.
6. Absorb it by a central whole-cell translation: a central scalar times the
   symmetric cycle has squared-phase exponents `(2n_1+1,2n_2+1,2n_3+1)`,
   which cannot equal `(2,1,1)` for integer `n_i`.
7. Rescue unit slope at factor resolution: every elementary factor has unit
   slope, but the composite square fixes the weighted word's slope magnitudes
   to `(2,1,1)`.

### Wall-independence audit (No-Go Discipline N2)

For the bounded physical reading, the collapsed conditional set is: inherited
site-strict/unitary/one-component/period-2 surface; supplied 3D realization
bridge; supplied word dispersiveness; and representative-inventory/class-
transport scope. No member closes another.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| inherited surface / realization bridge | no | no | yes |
| inherited surface / word dispersiveness | no | no | yes |
| inherited surface / inventory transport | no | no | yes |
| realization bridge / word dispersiveness | no | no | yes |
| realization bridge / inventory transport | no | no | yes |
| word dispersiveness / inventory transport | no | no | yes |

The algebraic `P_WEIGHT` counterexample itself uses the displayed word and
residual class, not the physical realization bridge.

### Hidden-wall scan (No-Go Discipline N3)

The constituent-factor semantics, the bridge, word dispersiveness, unitary
surface, period-2 cell, and representative inventory are explicit above.
“Constructed” refers to the displayed inventory, not a completeness claim.
The registered kinetic-isotropy primitive is context only and supplies no
selector or dynamics. No readout normalization is used.

### Residual matching (No-Go Discipline N4)

| Authority | Authority residual | Residual used here | Match and treatment |
|---|---|---|---|
| landed 3D simultaneous-tick note | symmetric factorized realization is supplied | test whether the weak filters recover that realization | match; this note leaves selection open |
| landed one-axis Wave A note | tick predicates require a supplied bridge; 3D is open | 3D factor/word predicates | not a supplier; its boundary is preserved explicitly |
| minimal-axiom memo | rule-level translation/rotation and variation clauses; no tick dynamics | protocol-factor predicates | not an identification; the separate bridge is explicit |
| site-license dichotomy | one-axis dispersive ticks saturate | simultaneous composite-word dispersiveness | not a word-level supplier; the condition is explicit |

No mismatched prior negative result is used as evidence for the `P_WEIGHT`
counterexample.

### Rhetoric audit (No-Go Discipline N5)

The scalar-equivalence failure is tested for the specified protocol word and
the four-member representative set. The slope comparison explicitly
distinguishes elementary factors from composite words. Nothing is claimed for
unlisted protocols, larger cells, transported classes, or the full lattice-
wide realization problem.

### Partial-closure path scan (No-Go Discipline N6)

A full 3D realization/covariance theorem, a derived one-mover-per-axis word
restriction, or class transport could remove `P_WEIGHT` from the physical
candidate set. These are theorem paths, not new axioms or labeling
conventions, and remain open.

### Steelman (No-Go Discipline N7)

The strongest objection is that `P_WEIGHT` may lie outside the intended
physical domain once full proper-cubic protocol covariance or a
one-mover-per-axis realization rule is imposed. That objection is plausible
and is why no universal no-go is claimed. It does not defeat the narrower
calculation: under the three displayed weak filters on the stated inventory,
`P_WEIGHT` survives and is not equivalent to the symmetric cycle under the
specified central residuals.

### Cross-cycle echo (No-Go Discipline N8)

The current Wave A review found the same rule-to-tick overread and repaired it
by adding an explicit realization bridge and necessary-filter language. This
note applies that repair at 3D protocol-factor level. The landed 3D parent also
keeps factorized realization and amplitude-mixing classification open. No
stronger closure is inferred here.

**No-Go Discipline result:** PASS for the narrow computed divergence; broader
physical and class-wide characterizations remain open.

## Dependencies

- [KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md](KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  supplies the 3D constructions, factor identities, and bounded-class scope;
  its factorized-realization input remains underived.
- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  supplies the one-axis flat/saturating dichotomy, not the simultaneous
  word-level dispersiveness condition.
- [TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md](TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md)
  supplies the conditional one-axis predicate theorem under its own
  tick--Admissibility bridge and fixes the current-main premise boundary used
  here; it does not supply the 3D protocol bridge.
- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)
  supplies the quoted rule-level clauses and the explicit boundary that
  Admissibility does not choose a transfer operator or kinetic branch.

Context only: `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`,
`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`.

## Runner And Cache

Primary runner:
[`scripts/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.py`](../scripts/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.py)

Runner cache:
[`logs/runner-cache/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.txt`](../logs/runner-cache/kinetic_isotropy_3d_factorized_protocol_selection_2026_07_09.txt)

Current local runner result:

```text
TOTAL: PASS=42 FAIL=0
```

## Changelog

- **2026-07-09.** Initial bounded note and deterministic runner.
- **2026-07-10.** Review-loop iteration 1 narrowed the result to an algebraic
  necessary-filter theorem, made the 3D realization bridge and word-level
  dispersiveness condition explicit, aligned the Wave A citation with current
  `main`, and replaced branch-local gate labels with descriptive names.
