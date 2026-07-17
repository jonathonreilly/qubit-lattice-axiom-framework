# Mixed-Pauli selector/canonical-pair tournament — Cycle 254

Date: 2026-07-17
Status: partial narrowing of three explicit bounded Pauli grammars
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/mixed_pauli_selector_canonical_pair_tournament_cycle254_2026_07_17.py
```

## Result up front

Cycle 254 searches for bounded commuting Pauli selectors inside the exact
Cycle-251 auxiliary even-CAR commutant.  A successful family would reduce the
rough physical code from exponent \(7N-1\) to \(6N\), preserve both matter
parities at odd and even L, commute with the mapped matter update, require no
marked root or global parity service, and form one proper-cubic,
coarse-translation-covariant local code family.

Three declared grammars are exhausted:

1. **Complete radius-one star grammar.** A seed is any product of the seven
   auxiliary parities \(\widetilde B\) in the center-plus-six-neighbor star and
   the six incident auxiliary hops \(\widetilde A\).  All 8,191 nonidentity
   seeds are completed under all 24 proper-cubic frames and all coarse-cell
   unit translations.
2. **Complete radius-two axial-cross grammar.** A seed is any product of 13
   axial \(\widetilde B\)'s at distances 0,1,2 and the 12 consecutive axial
   \(\widetilde A\) hops.  The 33,554,431 nonidentity words are exhausted by
   reducing the 4,096 hop masks to 240 proper-cubic orbits and solving the
   commutation conditions exactly as affine equations in all 13 parity bits.
3. **Full Manhattan-ball cubic scalar-shell grammar.** Four parity shells and
   three edge shells—central radial, outer axial, and face-diagonal—give 127
   nonidentity scalar templates on the complete radius-two Manhattan ball.

There is **no nontrivial mixed-Pauli survivor** in any grammar.  Radius one
leaves exactly the 127 nonzero parity-only words.  The axial-cross search
leaves only the zero-hop class, with all 13 parity bits free.  The scalar-shell
search leaves 31 commuting templates, but its 16 A-dressed cases use the
24-edge face-diagonal cycle shell, whose auxiliary boundary is zero; modulo
the physical stabilizers they are still parity-diagonal.

The diagonal fallback is physically valid but insufficient.  Nearest-neighbor
\(\widetilde B_x\widetilde B_y=+1\) rows are bounded weight 12, commuting,
phase-consistent, exactly frame/translation covariant, and add rank \(N-1\)
at L=3,4,5 and held-out L=6.  They have zero leakage against every mapped
matter generator and hence against the fixed free-plus-contact update at
\(\beta=-0.3,g=0.37\).  But \(P_m=P_g=b^N\): at even volumes L=4 and L=6 they
fix \(P_m=+1\), deleting the odd matter sector.

This is an exact candidate-grammar disposition, not a general radius-two,
Pauli, Clifford, subsystem, measurement, or non-Pauli no-go.  The full
radius-two Manhattan grammar with nonscalar seeds, bounded Clifford circuits
whose images leave the declared row supports, multi-phase compiler schedules, and
measurement-assisted preparation remain live.  Rank matching also does not
construct a bounded state-preparation E.  Cycle 254 therefore ships only a
partial narrowing and creates no axiom pressure.

## Exact quotient used by the search

Cycle 251 proves that every physical Pauli commuting with the mapped matter
algebra is represented, modulo code stabilizers, by the auxiliary even-CAR
algebra.  A local auxiliary word can be reduced to a pair \((b,d)\):

- \(b\) is the set of cell-parity generators \(\widetilde B_x\);
- \(d=\partial e\) is the mod-two endpoint boundary of the selected auxiliary
  hops \(\widetilde A_e\).

Cycle products of A's have \(d=0\) and are stabilizer-equivalent to the same
word without that cycle.  The exact commutation form is

\[
 \omega((b,d),(b',d'))
 =b\cdot d'+d\cdot b'+d\cdot d'\pmod 2.
\]

This quotient eliminates representation noise without introducing a
Jordan--Wigner order.  Every framed/translated seed is checked against every
translate whose finite supports overlap; disjoint translates commute
automatically.  A proper-cubic covariant Abelian selector group containing a
row must contain its complete symmetry orbit, so one noncommuting orbit pair
rejects that row even if other seed orbits are added.

## Radius-one complete exhaustion

The radius-one star contains seven B choices and six A choices, hence
\(2^{13}-1=8191\) nonidentity words.  The search returns:

| result | exact count |
|---|---:|
| symmetry-orbit-commuting seeds | 127 |
| seeds with nonzero A-boundary | 0 |
| surviving seed set | all \(2^7-1\) nonzero B-only words |

Thus no mixed row can appear in any Abelian proper-cubic/translation-covariant
selector family built from this complete radius-one grammar.  This also
rejects a canonical-X layer in the same grammar: a conjugate of a nontrivial
diagonal selector needs nonzero auxiliary boundary, while a lattice of
canonical X representatives must commute away from its paired Z rows.

The full frame-orbit ranks of the 127 diagonal survivors are:

| L | N | seeds with rank \(N-1\) | rank-matched seeds retaining both parities |
|---:|---:|---:|---:|
| 3 | 27 | 59 | 59 |
| 4 | 64 | 24 | 0 |
| 5 | 125 | 59 | 59 |
| 6 held out | 216 | 24 | 0 |

The even-volume result is not special to nearest-neighbor equalities.  Any
translation-invariant diagonal family of rank \(N-1\) has a one-dimensional
orthogonal kernel.  Translation invariance forces its nonzero kernel vector
to be the all-ones vector.  Therefore its row space is the even-weight
subspace, which contains total parity exactly when N is even.  Every diagonal
rank-matched survivor has the same even-volume parity defect.

## Radius-two axial-cross affine exhaustion

The axial cross has 13 B bits and 12 A-edge bits.  For a fixed A-edge mask,
the self-, translation-, and framed-orbit commutators are affine-linear in the
13 B bits:

\[
 b\cdot T(Fd)+d\cdot T(Fb)=d\cdot T(Fd).
\]

The 24 proper frames partition the 4,096 edge masks into 240 exact orbits.
Solving all affine systems gives one consistent orbit representative:

```text
edge mask = 0
solution dimension in B bits = 13
auxiliary boundary size = 0
```

Because the axial edge graph is a forest, no nonzero edge mask has zero
boundary.  Thus all \(2^{25}-1=33,554,431\) nonidentity words are accounted
for and every commuting word is B-only.  This is complete for the axial-cross
grammar, not for the full radius-two ball.

## Radius-two full-ball scalar shells

The Manhattan ball contains 25 cells and 36 internal nearest-neighbor edges.
Cycle 254 exhausts the cubic-scalar templates formed from:

| template shell | size |
|---|---:|
| center B | 1 |
| radius-one axial B | 6 |
| radius-two axial B | 6 |
| radius-two face-diagonal B | 12 |
| center-to-radius-one A | 6 |
| radius-one-to-radius-two axial A | 6 |
| radius-one-to-face-diagonal A | 24 |

Of 127 nonidentity shell products, 31 have commuting translation orbits.
Fifteen are B-only.  The other 16 include the 24-edge face-diagonal shell,
but every vertex has even incidence, so its boundary is zero.  These are
A-cycle dressings of the same diagonal quotient rows.  No scalar template
with nonzero A-boundary survives.

The nonscalar full-ball grammar has 25 B generators and a rank-24 edge-boundary
space, or \(2^{49}\) distinct quotient words before symmetry reduction.  It is
not exhausted here and is explicitly outside the negative claim.

## Physical fallback controls

The runner lifts the nearest-neighbor equality fallback to the actual
Cycle-247 rough-terminal code and obtains:

| L | selector rows | independent increment | code exponent | matter parity fixed? |
|---:|---:|---:|---:|---|
| 3 | 81 | 26 | 162 | no |
| 4 | 192 | 63 | 384 | yes, \(+1\) |
| 5 | 375 | 124 | 750 | no |
| 6 held out | 648 | 215 | 1296 | yes, \(+1\) |

At every size:

- the signed stabilizer group is phase-consistent;
- selector mutual anticommutations and matter/update leakage are zero;
- support is two adjacent puncture cells and physical Pauli weight is 12;
- deleting one row from an extracted independent tree basis lowers rank by
  one; and
- the complete redundant family, not the tree basis, is exact under all 24
  proper-cubic frames and the three positive coarse-cell unit translations.

The extracted tree is used only for a deletion/rank test.  It is not supplied
to the update and is not proposed as a covariant selector.

## Why bounded state-preparation E does not follow

Rank matching selects a code dimension, not a local encoder.  The diagonal
equalities impose

\[
 \widetilde B_x\widetilde B_y=+1
\]

at every separation on the connected torus.  Maximum coarse-graph separation
is 3,6,6,9 at L=3,4,5,6.  A selected auxiliary state therefore has repetition/
GHZ-type correlations across growing distance.  Cycle 254 constructs no
bounded-depth circuit that prepares those correlations or conditionally ties
their common bit to matter parity.  On even volumes the stronger parity
failure already rejects the family before preparation is considered.

The mixed-orbit exhaustions also find no bounded canonical-X layer within the
three grammars: all nontrivial conjugate candidates have nonzero A-boundary,
and none has a mutually commuting symmetry orbit.  This is a grammar result,
not a lower bound against arbitrary Clifford QCA, non-Clifford encoders,
measurements, ancilla reset, or a dynamical schedule.

## Covariance, marker, and time firewall

“Translation” here means coarse-cell unit translations of the supplied
puncture/macro-cell roles.  It is not homogeneous one-site translation on
undifferentiated physical M2 factors.  The inherited Cycle-237 period-16
physical role marker, its 4,096 translated sectors, and marker-sector
initial/boundary/realized-state selection remain supplied.

The selector is a spatial code constraint.  It is not a clock, elapsed time,
a generator rate, a Record, or a realized-history law.  The derived-time
firewall remains closed.  No schedule tested here is called physical time,
and the wrapped Cycle-230 phase remains neither physical energy nor a source.

## Supplied-structure inventory

Cycle 254 supplies rather than derives:

1. the Cycle-251 auxiliary \(\widetilde B,\widetilde A\) presentation and its
   parity lock \(P_g=P_m\);
2. the Cycle-247 rough-terminal graph, constraints, torus/Wilson rows, and
   bounded ordering-gauge repair;
3. the radius-one star, radius-two axial cross, and scalar shell grammars;
4. the choice that one seed's full frame/translation orbit is admitted as a
   selector family;
5. the \(+1\) eigenvalue convention for every selector row;
6. periodic L=3,4,5 and held-out L=6;
7. the fixed Cycle-230 \(\beta=-0.3\), \(g=0.37\), and free-plus-contact order;
8. the coarse puncture/macro-cell partition;
9. the inherited period-16 physical role marker and selected marker sector;
10. ordinary complex quantum mechanics and stabilizer/Pauli composition; and
11. any preparation, reset, measurement, or realized selection of one code
    state.

No axiom, foundation, Qualification, primitive, registry, policy, queue, or
audit-status surface is edited.

## Dependency ledger

| wall | Cycle-254 disposition |
|---|---|
| \(C_{ref}\) | unchanged: marker sector, puncture roles, and parity-sector preparation remain supplied |
| \(C_{num}\) | sharpened: every rank-matched diagonal covariant family loses odd parity at even N |
| \(C_{wrap}\) | unchanged; selector arithmetic is not phase/time/energy selection |
| \(C_{int}\) | fixed contact/update commute exactly with all tested selectors, but no full-Fock E exists for the fallback |
| \(C_{local}\) | narrowed: complete radius one plus two declared radius-two grammars contain no useful mixed row; full nonscalar radius two and bounded preparation remain open |
| \(C_{source}\) | unchanged; no gravity/resource/source mechanism is tested |

The result distinguishes an unfinished local-encoding search from a shared
substrate obstruction.  It supplies no constitutional evidence.

## N1–N8 no-go-discipline gate

Gate status: PASS for the narrow grammar dispositions; FAIL for any general
Pauli/Clifford/radius-two no-go.  The shipped claim is therefore a partial
narrowing.

### N1 — Alternative-route enumeration

| Route | Honesty | Exact attempt/disposition |
|---|---|---|
| full radius-one mixed seed orbit | ATTEMPTED | all 8,191 seeds; 127 commuting, all B-only |
| multiple radius-one seed orbits | ATTEMPTED | any admitted mixed row brings its non-Abelian symmetry orbit; unions cannot repair that pairwise failure, while diagonal unions inherit the parity theorem |
| full radius-two axial cross | ATTEMPTED | all \(2^{25}-1\) words via 240 edge orbits and affine B solutions; no nonzero edge mask survives |
| full-ball cubic scalar shells | ATTEMPTED | all 127 templates; A-dressed survivors have zero boundary and are quotient-diagonal |
| diagonal rank-matched selector | ATTEMPTED | physical L=3–6 ranks close; both-parity condition fails exactly at even N |
| bounded covariant canonical-X layer in these grammars | ATTEMPTED | a conjugate requires nonzero boundary; no mutually commuting mixed orbit survives |

The full nonscalar radius-two ball, larger radius, non-Pauli constraints,
measurement/reset, and staggered compiler schedules are not ruled out.  They are
outside the narrow claim rather than silently counted as failures.

### N2 — Wall-independence audit

The raw candidate gates are:

- \(K_{mix}\): a nontrivial mixed covariant Abelian row exists;
- \(K_{parity}\): a rank-\(N-1\) family retains both parities at even N;
- \(K_E\): the selected image has a bounded preparation/intertwiner.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| \(K_{mix},K_{parity}\) | no | within the tested Pauli grammars yes: the diagonal theorem makes mixing necessary | no; collapse parity failure downstream of no mixed survivor |
| \(K_{mix},K_E\) | no | no: a non-Pauli or dynamical E need not expose a mixed stabilizer row in this grammar | yes |
| \(K_{parity},K_E\) | no | a full-Fock E must retain parity, but parity rank alone supplies no E | no; E is the stronger downstream compiler gate |

Thus Cycle 254 does not advertise three independent walls.  It reports one
scoped row-grammar failure and one still-open downstream preparation problem.
For the even-L diagonal fallback, parity failure already rejects the candidate;
preparation is not counted as an additional reason for that rejection.

### N3 — Hidden-wall scan

The search explicitly supplies its neighborhoods, generator presentation,
symmetry-orbit rule, periodic domains, +1 signs, marker, and fixed update.
“By construction” is not used as a proof step.  “Framework provides,”
“naturally,” “obviously,” and “standard QFT” are absent.  “Canonical” names
the tested Pauli-pair target, not a hidden admission.  “Background” and
“registered” are absent.  The unsearched nonscalar radius-two quotient is
quantified as \(2^{49}\), promoted to the open-route list, and not hidden by
the scalar-shell result.

### N4 — Residual matching

| Witness | Witness residual | Cycle-254 residual | Match/use |
|---|---|---|---|
| Cycle 251 note lines 17–27 | exact auxiliary even-CAR commutant and parity lock | search space for commuting physical selectors | yes; retained basis |
| Cycle 251 note lines 193–208 | diagonal equality rank closes but even volume loses odd parity; mixed selectors live | exhaustive radius-one and scoped radius-two mixed search | yes |
| Cycle 251 note lines 160–171 | one tree Gram--Schmidt canonicalization grows | local symmetry-orbit canonical layer | no; motivation only, not a witness for the new negative |
| Cycle 247 note lines 268–277 | coarse-cell/frame covariance with supplied roles | covariance scope of selector family | yes; same residual |
| Cycle 237 note lines 283–342 | marker law family versus selected marker sector | auxiliary selector/preparation | no; retained supply firewall only |

Nonmatching citations are not used as proof of the grammar negative.

### N5 — Rhetoric audit

| Resolution | Tested? | Exact statement |
|---|---|---|
| one generator element | yes | each B/A word reduces to \((b,d)\) |
| one radius-one block | yes, complete | no mixed seed has an Abelian full symmetry orbit |
| one radius-two axial block | yes, complete | no mixed axial-cross seed has an Abelian full symmetry orbit |
| one radius-two scalar block | yes, complete for seven shells | mixed-looking survivors have zero boundary |
| arbitrary radius-two block | no | no negative claim |
| lattice-wide arbitrary Pauli/Clifford family | no | no negative claim |

Accordingly the note says “no survivor in the declared grammar,” never “local
mixing is impossible.”  “Bounded state-preparation E does not follow” is
restricted to rank matching and the tested repetition fallback; it is not a
universal encoder no-go.

### N6 — Partial-closure path scan

Several non-axiom closure paths remain:

- enlarge the affine method to nonscalar full-ball edge-boundary orbits;
- introduce two or more compiler phases so individual noncommuting spatial rows
  are never simultaneous stabilizers;
- use measurement/reset to prepare a parity-correlated code sector;
- retain a fixed-parity operational theory if odd-sector coherence is not an
  operational requirement; or
- accept the Cycle-251 auxiliary sector as an explicit input rather than
  selecting it.

These are representation, schedule, or operational-scope decisions.  No new
axiom is required merely because the present grammars fail.

### N7 — Steelman

> This search is far from a radius-two Clifford no-go.  The full Manhattan
> ball has \(2^{49}\) distinct quotient words, while the nonscalar portion is
> sampled only by the axial cross; the scalar-shell test cannot see chiral or
> oriented multiplets whose complete 24-frame orbit may commute collectively.
> A finite-depth Clifford can also map a simple seed outside the declared
> row-support grammar, and a two-phase Floquet or measurement/reset protocol
> need not realize all selector rows as one simultaneous Abelian group.  Cycle
> 251 already showed that changing representation converts apparent rank
> defects into exact auxiliary algebra.  The strongest conclusion available
> here is therefore the three-grammar census, not an obstruction to bounded
> encoding.

The steelman is convincing.  It forces the partial-narrowing classification.

### N8 — Cross-cycle echo

- Cycle 235's periodic even-sector restriction was softened by the boundary
  and gauging representations of Cycles 245 and 247.
- Cycle 247's \(N-1\) “excess logical” interpretation was corrected by Cycle
  251's exact auxiliary even-CAR commutant.
- Cycle 237 turned a preferred origin into a covariant marker-sector family,
  while leaving state selection explicit.
- Cycle 251's tree canonicalization grew extensively, but it explicitly kept
  radius-one/two Clifford and mixed-selector routes live.

These echoes show that rank and locality failures have repeatedly been retired
by a new representation or code-family viewpoint.  Cycle 254 tests two of the
live mixed routes but does not foreclose the same mechanism at larger grammar,
multiple compiler phases, or non-Pauli preparation.

## Time firewall

- campaign: inherited 12-hour goal remains active;
- runner scope: finite exact GF(2) quotient arithmetic plus physical L=3–6
  stabilizer checks;
- authority: none;
- audit: unset;
- derived-time firewall: active;
- constitutional edits: forbidden and not made;
- next retask: nonscalar full-Manhattan radius-two orbit solving or an explicit
  staggered/measurement preparation, not axiom drafting.
