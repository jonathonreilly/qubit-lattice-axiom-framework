---
claim_id: product_class_six_axis_pair_chsh_squares_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "On the declared six signed-axis menu, nonnegative orbit weights (p, q, r) not all zero, the product-class pair law of one edge is mu(a,b)=phi(a,b)/(6p+6q+24r). It is both the static full-conditional law and the records-only formation law of that edge. The coordinate correlator is lambda u·v with lambda=(p-q)/(3(p+q+4r)), and the equatorial CHSH square of that correlator is exactly 8 lambda^2, hence at most 8/9, strictly below 4 and strictly below 8. The setting-blind global sign has correlator lambda_1=(p-q)/(p+q+4r) and CHSH square 4 lambda_1^2, which equals 4 exactly when r=0 and pq=0, and is never 8. Any readout with values in [-1,1] that is a function of the local record, the local setting, and randomness independent of the other wing has CHSH magnitude at most 2, so its square is at most 4 and is not 8. Conditioning on both records lying on one fixed axis, when p+q>0, gives sign correlator alpha=(p-q)/(p+q) and CHSH square 4 alpha^2, equal to 4 exactly when pq=0, and never 8. No weight is selected. No two-qubit density is used. The sum rule, larger windows, and lattice-wide statements are not claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/product_class_six_axis_pair_chsh_squares_2026_10_09.py
---

# The six-axis product-class pair law has exact CHSH squares below 8

**Date:** 2026-10-09

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/product_class_six_axis_pair_chsh_squares_2026_10_09.py`](../scripts/product_class_six_axis_pair_chsh_squares_2026_10_09.py)

**Pinned cache:**
[`logs/runner-cache/product_class_six_axis_pair_chsh_squares_2026_10_09.txt`](../logs/runner-cache/product_class_six_axis_pair_chsh_squares_2026_10_09.txt)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact orbit enumeration, rational correlators, and an elementary bound for local readouts with values in [-1,1]."
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "It does not derive the dynamics clause, the trace rule, the menus or how settings are chosen."
source_of_blocker_text: frontier_question
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Inside the density representation already used, compute the exact CHSH maximum of the directed six-parameter family and keep that hypothesis explicit."
conditional_surface_status: "declared six-axis product-class pair and declared local readouts; not a two-qubit density"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## What is conditional

The axioms used, verbatim from
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), are:

- Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site."
- Qubit: "The full one-site possibility domain has algebraic presentation `M_2(C)`."
- Admissibility: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
- Record: "Only records are readable. A readout value is determined by record content alone."

The reading note in that memo says the distribution does not supply the
formation site, probability, or rate. This note does not derive them.

The six-element menu and the orbit weights are a declared finite law, the
same menu used by the formation census
[ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md](ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md).
That census leaves `(p, q, r)` free. This note does not repeat it and does
not select a triple. Settings used below are part of the declared comparison,
not an axiom clause.

No density operator is formed. The comparison with the density-family squares
4 and 8 is numerical. The density calculation itself is the separate note
[PROPER_CUBIC_TWO_QUBIT_BOND_INVARIANTS_BOUNDED_THEOREM_NOTE_2026-10-09.md](PROPER_CUBIC_TWO_QUBIT_BOND_INVARIANTS_BOUNDED_THEOREM_NOTE_2026-10-09.md).

## Definitions

The menu `M` is the six signed axes `±e_x, ±e_y, ±e_z` in `Z^3`. For
`a, b in M`, the product-class weight `phi(a,b)` is `p` if `a=b`, `q` if
`a=-b`, and `r` if `a·b=0`. Throughout, `p, q, r` are real and nonnegative,
and not all zero. Write `D = p+q+4r` and `Z = 6D`.

The pair law is `mu(a,b) = phi(a,b)/Z`.

A local readout assigns to each wing a value in `[-1,1]` determined by that
wing's record, that wing's setting, and randomness independent of the other
wing's record, setting, and randomness. The CHSH combination of four
correlators is `E_00+E_01+E_10-E_11`. Its square means the square of its
absolute value. The four one-minus forms are the same expression after
moving the minus onto each correlator in turn.

The coordinate readout of a unit vector `u` is `X_u(a) = a·u`. The global
sign is `s(a) = a_x+a_y+a_z`, which equals `±1` on every menu element.

## Theorem 1 — one edge has one pair law

**Conclusion.** The 36 ordered pairs fall into orbits of sizes 6, 6, and 24.
`Z = 6p+6q+24r`. For every fixed `a`, `sum_b phi(a,b) = D`. The records-only
formation law that draws the first site uniformly and the second site with
conditional weights `phi(·,a)/D` equals `mu`. The same `mu` has both
one-site conditionals equal to `phi/D`.

**Proof.** Each menu element is parallel to itself, antiparallel to one
element, and orthogonal to the other four, so the orbit sizes are
`6`, `6`, and `6·4=24`. The row sum is `p+q+4r` independently of the row,
and six rows give `Z`. Formation therefore puts mass
`(1/6)·phi(a,b)/D = phi(a,b)/Z` on each pair. Dividing `phi` by `Z` gives
the same joint, and its conditional on either coordinate is `phi/D` because
every row sums to `D`. The marginal of either site is `D/Z = 1/6`. A proper cubic rotation
preserves dots, so it preserves `phi`. ∎

## Theorem 2 — two exact correlators

**Conclusion.** `E[X_u X_v] = lambda (u·v)` with
`lambda = (p-q)/(3D)`. In particular `|lambda| ≤ 1/3`, with equality if and
only if `r=0` and `pq=0`. The global-sign correlator is
`lambda_1 = (p-q)/D = 3 lambda`, and `|lambda_1| ≤ 1`, with the same
equality case.

**Proof.** Only pairs on a coordinate axis contribute to `E[a_i b_i]`. The
four pairs on `e_z` contribute `p-q-q+p = 2p-2q`, so
`E[a_z b_z] = (2p-2q)/Z = (p-q)/(3D)`. For `i ≠ j` the four sign patterns on
those two axes are orthogonal and cancel, so the cross term is `0`.
Bilinearity gives `E[(a·u)(b·v)] = lambda (u·v)`.

The same count with the sign `s` gives unnormalized sum `6p-6q`, hence
`E[s(a)s(b)] = (p-q)/D`. For nonnegative weights,
`D-|p-q| = 2 min(p,q)+4r ≥ 0`, so `|lambda_1| ≤ 1` and `|lambda| ≤ 1/3`.
Equality holds exactly when that remainder vanishes. ∎

The rational `lambda_1` is also the odd eigenvalue of the one-neighbor kernel
in the binding-scale note. This proof does not use that spectral statement.
It counts pairs. The factor `1/3` is mandatory: at `(3,1,2)`,
`lambda = 1/18` and `lambda_1 = 1/6`.

## Theorem 3 — coordinate and global-sign squares

**Conclusion.** For unit settings, the coordinate CHSH magnitude is at most
`2√2 |lambda|`, and the equatorial settings
`e_x`, `e_y`, `(e_x+e_y)/√2`, `(e_x-e_y)/√2` attain square `8 lambda^2`.
Thus the attained square is at most `8/9`. It is strictly less than `4` and
strictly less than `8` for every allowed weight triple. The setting-blind
global sign has CHSH value `2 lambda_1` and square `4 lambda_1^2`. That
square equals `4` exactly when `r=0` and `pq=0`, and it is never `8`.

**Proof.** Let `c=v+v'` and `d=v-v'` for unit `v, v'`. Then
`|c|^2+|d|^2=4`, and the coordinate combination equals
`lambda (u·c + u'·d)`. Its absolute value is at most
`|lambda|(|c|+|d|)`, and `(|c|+|d|)^2 ≤ 2(|c|^2+|d|^2)=8`. The stated
equatorial vectors give direction sum `2√2`, whose square is `8`, so the
CHSH square equals `8 lambda^2` rather than a looser upper bound.
`8 lambda^2 ≤ 8/9` because `|lambda| ≤ 1/3`. And `8/9 < 4 < 8`.

If every setting reads `s`, all four correlators equal `lambda_1`, so the
CHSH value is `2 lambda_1`. Its square is `4 lambda_1^2 ≤ 4`, and it equals
`4` exactly at the equality case of Theorem 2. Since that square is at most
`4`, it is not `8`. ∎

Signed axis settings stay inside the menu and do not reach the equatorial
square. If `u'=ε u` with `ε=±1`, the form `u·v+u·v'+u'·v-u'·v'` collapses
to `2 u·v` or `2 u·v'`. If `u·u'=0`, each signed axis meets at most one of
`u` and `u'`, so the four absolute dots sum to at most `2`. Swapping the
two settings of one wing, or flipping a setting sign, stays inside the
signed axes and moves the minus among the four correlators. The direction
combination is therefore at most `2`, and it is attained, for example by
`u=v=e_x` and `u'=v'=e_y` after the minus is placed on a zero cross term.
The coordinate CHSH magnitude on signed axes is at most `2|lambda|`, and
that square is at most `4/9`. The runner exhausts all `6^4` tuples.

## Theorem 4 — local bound, and one conditional square

**Conclusion.** Every local readout with values in `[-1,1]` has CHSH
magnitude at most `2`. The square of that value is at most `4` and is not
`8`. Separately, on the event that both records lie on one fixed axis, which
has mass `(p+q)/(3D)`, the conditional sign correlator is
`alpha=(p-q)/(p+q)` whenever `p+q>0`. Sign settings of that single axis have
CHSH magnitude `2|alpha|` and square `4 alpha^2`. The square equals `4`
exactly when `pq=0` and `p+q>0`, including when `r>0`, and it is never `8`.
When `p=q=0` the event is empty and the conditional law is undefined.

**Proof.** For real `B, B'`,
`(|B+B'|+|B-B'|)^2 = 2(B^2+B'^2) + 2|B^2-B'^2| = 4 max(B^2,B'^2)`.
If both wings' outcomes lie in `[-1,1]`, the CHSH combination at each atom
of the local data is at most `|B+B'|+|B-B'| = 2 max(|B|,|B'|) ≤ 2`.
Averaging preserves the inequality. The value `2` is a match to the
classical number, not to `2√2`. The sixteen deterministic sign pairs are a
control for the `±1` special case; their maximum magnitude is `2`.

On the one-axis event the four surviving pairs have weights `p,q,q,p` and
sign products `+1,-1,-1,+1`. The conditional expectation is
`(2p-2q)/(2p+2q)=alpha` when `p+q>0`. All four setting pairs of a
setting-blind sign readout have this same correlator, so the CHSH value is
`2 alpha`. Then `4 alpha^2=4` if and only if `|p-q|=p+q`, which for
nonnegative `p,q` is `pq=0` with `p+q>0`. Orthogonal weight does not appear
in this conditional denominator. And `4 alpha^2 ≤ 4 < 8`. The event mass is
`(2p+2q)/Z=(p+q)/(3D)`. ∎

This conditional square is the CHSH of one probability space, the one-axis
event. It is not a license to add correlators that were conditioned on
different axes. Those are different events.

## What this does not do

- It does not identify `mu` with a two-qubit density. Under that different
  hypothesis, the earlier bond note attains CHSH square `8` at two positive
  corners. Those corners are not points of this menu law.
- It does not derive the dynamics clause, the trace rule, or a choice of
  settings. The records-only formation bound `|CHSH| ≤ 2` in
  [DYNAMICS_CLAUSE_BELL_VALUES_OF_RECORD_LAWS_RECORDS_ONLY_FORMATION_STAYS_AT_TWO_THE_DYNAMICS_CLAUSE_REACHES_TWO_ROOT_TWO_BOUNDED_THEOREM_NOTE_2026-09-24.md](DYNAMICS_CLAUSE_BELL_VALUES_OF_RECORD_LAWS_RECORDS_ONLY_FORMATION_STAYS_AT_TWO_THE_DYNAMICS_CLAUSE_REACHES_TWO_ROOT_TWO_BOUNDED_THEOREM_NOTE_2026-09-24.md)
  is a different kernel family. It is not a premise here.
- It does not select `(p,q,r)`.
- It does not evaluate the sum rule, a window larger than one edge, or an
  infinite-volume law.
- It does not say that a readout depending on the other wing stays at
  magnitude `2`. The dynamics note already records magnitude `4` for one
  cross-wing ancestry reading. That reading is outside Theorem 4.

## No-Go Discipline Gate

Scoped claim only: the squares in Theorems 3 and 4. A reading on which no
representation at all can have square `8` is not claimed. Gate status for
the scoped claim: the in-domain attacks below are closed by the proofs just
given. Packet status is not a route closure beyond that scope.

N1. Five attacks on the scoped squares:

1. A local `±1` readout with magnitude above `2`. Attempt: assign each
   record a sign depending on the local setting. It fails by the atom bound
   in Theorem 4. `ATTEMPTED`.
2. Unit settings whose coordinate combination has square above `8 lambda^2`.
   It fails by `|c|^2+|d|^2=4` and the equatorial attainment in Theorem 3.
   `ATTEMPTED`.
3. Nonnegative weights with `8 lambda^2 ≥ 4`. It fails because
   `|lambda| ≤ 1/3`, so the square is at most `8/9`. `ATTEMPTED`.
4. Signed-axis settings with coordinate magnitude above `2|lambda|`. The
   runner exhausts `6^4` tuples; the maximum direction combination is `2`.
   `ATTEMPTED`.
5. Treating the one-axis conditional square as an unconditional value above
   `4`, or as square `8`. The conditional space is stated separately; its
   square is `4 alpha^2 ≤ 4`. `ATTEMPTED`.

N2. The hypotheses are one bundle: nonnegative product-class weights, one
edge, and a local `[-1,1]` readout. The one-axis conditional is a different
measure, not a second independent wall under the unconditional claim. No
pairwise inflation is asserted.

N3. The proof text was scanned for the hidden-wall phrases in the discipline
list. The axiom sentences are quotations. No hidden condition is used in
place of Theorems 1–4. The menu and the settings are named as declared.

N4. The dynamics-clause note is not a witness for this residual. Its
residual is a formation kernel on windows with ancestry conditions. This
residual is the one-edge product-class law. The citation is prior art only.
The bond-invariants note is the density comparison, not a witness that the
menu law is small. No external no-go witness is load-bearing. Dropping both
citations leaves the enumerations intact.

N5. The sentence "the square is not 8" is limited to the readouts and the
one-edge law tested here. It is not a per-site claim for a larger
neighborhood, not a sum-rule claim, and not a lattice-wide claim. The runner
prints those five resolutions.

N6. This note does not say that a new axiom is required. The registered
primitives `scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive` are not used and are not walls. No convention
note found in the origin/main search turns this pair law into the singlet.

N7. Steelman, outside the scoped domain: the two-qubit density family
already attains square `8` at `(u,v)=(-1,-1)` and `(1,-1)`, and a supplied
dynamics clause attains `2√2`. Those mechanisms are real and are not closed
here. They are not counterexamples to Theorems 3 and 4, which never form
that density. The next listed computation is the directed six-parameter
maximum inside the density family.

N8. The records-only magnitude-`2` bound of the dynamics note has not been
retired. Cycle 1 did not retire it; it computed a different representation.
No searched retirement mechanism applies inside this menu law.

## Runner

`scripts/product_class_six_axis_pair_chsh_squares_2026_10_09.py` repeats the
orbit count, the two laws' common normalizer, the coordinate and sign sums,
the equatorial square, the signed-axis exhaustion, the one-axis conditional
square, and the sample check of the absolute-sum identity. A closed form
that drops the factor `3` fails the `(3,1,2)` check.
