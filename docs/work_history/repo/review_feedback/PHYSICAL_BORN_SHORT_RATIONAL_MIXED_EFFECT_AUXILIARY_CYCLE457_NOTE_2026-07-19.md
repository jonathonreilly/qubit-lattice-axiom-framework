# Cycle 457 — short rational mixed-effect auxiliary compiler

Date: 2026-07-19
Authority: none
Audit: unset

## Decision

Cycle 454 left six exact rational directions between its explicit physical
surface and the fixed-G55 algebraic ceiling.  This cycle compiles two of those
directions.  It does so with a shared auxiliary service in which every
auxiliary effect class is counted, then carries the resulting programs through
train L=3, held L=6, all 24 proper-cubic frames, exact E/G, exact inverse,
leakage, deletion, anti-fit, and one-particle mass controls.

Every auxiliary effect class counted here remains an explicit incidence
column; none is projected away in the reported full surface.

The result is constructive but incomplete.  The full augmented rank rises
from 84 to 210 only because 124 explicit auxiliary columns accompany the two
new old-grade constraints; the full augmented nullity and projected-old
nullity both fall from 20 to 18.  Fifteen directions remain beyond the three
Pauli tangents.  Four of the six fixed-G55 rational directions remain
uncompiled.  There is no grade homogeneity premise.

The no-go gate therefore has the following disposition:

**Gate disposition: FAIL — partial-attempt-with-named-untested-routes.**

This is no no-go, minimum-content, shared-obstruction, or axiom-pressure claim.
It is also not Born closure, uniqueness, or a probability theorem.

## Frozen bounded short-candidate menu

The runner first reconstructs the Cycle-454 exact `152 x 104` incidence
surface at rank/nullity `84 / 20`.  It separately appends the complete exact
rational relation space of the original G55 operators.  That raises rank to
90 and leaves nullity 14, so **six exact rational directions remain after
Cycle 454**.  This algebraic completion is only a route map; it is not counted
as a physical compiler.

Before constructing any new context, the runner freezes a bounded
short-candidate menu with:

- denominator N=8;
- support at most 20 original G55 classes;
- primitive coefficient at most 25;
- exact operator equality and a positive root bounded by the identity;
- independence relative to the Cycle-454 row space.

G55 indices below are the runner's zero-based `E_i` indices.  The two selected
mixed-effect relations are

```text
25 E33
  = 2 E8 + E16 + E17 + E18
    + 2 E20 + 2 E21 + 2 E24 + 2 E25
    + E26 + E27 + E28
    + 2 E46 + 2 E47 + E48 + E49 + E50,
```

and

```text
8 E10 + 25 E29
  = 2 E8 + 8 E9
    + E20 + E21 + E24 + E25 + E28
    + E46 + E47 + E50.
```

Their supports are 17 and 12.  Their maximum coefficients are both 25.  On
division by eight, the first common root is the identity with eigenvalues
`(1,1)`; the second is a genuine mixed effect with eigenvalues `(1/2,1)`.
Both exact rows vanish in the four-coordinate radical lift, and their
incremental old-relation ranks are 85 and 86.  Thus neither row is fit after
seeing physical residuals.

The bounded menu is intentionally narrow.  In particular, it does not assert
that these are the shortest relations under every rational basis, the only
useful mixed-effect relations, or a canonical domain.

## Physical auxiliary construction

For each old class used by either relation, the construction creates an
explicit `E_i/8` class and links it by paired normalized contexts:

```text
(E_i/8, E_i/8, I-E_i/4)  = (E_i/4, I-E_i/4)
(E_i/4, E_i/4, I-E_i/2)  = (E_i/2, I-E_i/2)
(E_i/2, E_i/2, I-E_i)    = (E_i, I-E_i).
```

Coefficient 25 is assembled as `8+8=16`, `16+8=24`, and `24+1=25` in the
same `/8` units.  Each relation side is then summed with bounded-arity
addition gadgets, using no more than seven summands plus a complement in any
primitive context.  The positive and negative sides terminate on the same
registered PSD root.

All overlapping `/8`, doubling, complement, and partial-sum effects are
identified by exact operator key and reused across both relations.  Nothing
is hidden as a host-side scalar service.  Every addition gadget contributes
the explicit normalized pair `(inputs..., I-C)` and `(C, I-C)`.

The account is:

| quantity | result |
|---|---:|
| new shared addition gadgets | 72 |
| new normalized context rows | 144 |
| retained Cycle-454 plus Cycle-457 context rows | 198 |
| total base-plus-extended incidence rows | 296 |
| total effect classes | 228 |
| new auxiliary classes beyond Cycle 454 | 124 |
| maximum primitive support | 3 M2 sites |
| program register per eight-program bank | 3 M2 sites |
| pointer register | 3 M2 sites |

The physical programs use the already supplied common contact followed by the
positive square root of each effect and the literal Cycle-317 stack isometry.
The fine program retains singleton pointer labels; the paired coarse program
merges the requested inputs against their complement.  This is a finite
effect/addition compiler.  It imports neither linear extension to arbitrary
effects nor grade homogeneity.

## Exact augmented rank and deletion controls

| surface | rows x columns | full augmented rank | full augmented nullity | projected-old nullity |
|---|---:|---:|---:|---:|
| Cycle 454 input | `152 x 104` | 84 | 20 | 20 |
| Cycle 457 full physical surface | `296 x 228` | 210 | 18 | 18 |

The trace-grade witness has residual
`4.0882747497410426e-15`.  The three Pauli tangent columns retain rank three
and have incidence residual `3.706110199210812e-15`.  The maximum exact-to-
physical effect residual is `1.4593798782361722e-15`; the maximum train/held
class residual is `1.1221884467222164e-15`; and the maximum literal
Cycle-317 stack-isometry residual is `1.4228618493537337e-15`.

Deletion is dependency-closed at the route level: a route deletion includes
its final relation contexts and any auxiliary service unique to that route.
Shared services used outside the deleted route remain present.

| deletion | exact rank | full nullity | projected-old nullity |
|---|---:|---:|---:|
| all 144 Cycle-457 rows | 84 | 144 | 20 |
| both dependency-closed relation routes | 195 | 33 | 20 |
| isotropic-mixed-closure route only | 198 | 30 | 19 |
| paired-axis-mixed-closure route only | 207 | 21 | 19 |

The two route closures contain 18 and 6 rows.  Each single-route deletion
restores exactly one old-grade freedom; deleting both restores the Cycle-454
projected-old nullity of 20.  The larger full nullities after deletion count
the deliberately retained isolated auxiliary columns and are not silently
projected away.

## Physical packet, covariance, and mass controls

The 144 new contexts are instantiated independently at train L=3 and held
L=6, for 288 new physical programs.  Across 152 involved effect classes this
gives 758 active pointer cases and 1546 idle pointer cases.  The result is:

| control | result |
|---|---:|
| maximum physical effect residual | `1.1221884467222164e-15` |
| maximum completeness residual | `1.4180152179851575e-15` |
| maximum fixed-bank isometry residual | `3.0254092164018233e-15` |
| maximum exact E/G residual | `0.0` |
| maximum exact inverse residual | `0.0` |
| leakage / packet / idle failures | `0 / 0 / 0` |
| proper-cubic frames | 24 |
| all-frame packet cases | 7296 |
| frame failures | 0 |
| one-particle mass relative residual | `2.220446049250313e-16` |

The physical-encoding covariance tuples `(L, failures, encoding residual,
block residual, unique blocks)` are `(3,0,0,0,152)` and
`(6,0,0,0,152)`.  Thus the new finite programs preserve the supplied mass
fixture and transform covariantly under the tested proper-cubic action.

Candidate packets are not actual Records.  Coherent norms are not
probabilities.  There is no occurrence, probability, frequency, or Born-law
selection.  The pointer exercise tests a reversible bounded packet codec and
nothing stronger.

## Anti-fit and scope controls

Changing the coefficient of `E33` by one makes the exact radical-lift relation
nonzero.  Three deliberately out-of-menu inputs are refused: denominator
seven, support above 20, and coefficient 26.  The held size, rotated frames,
deletion surfaces, exact coefficient corruption, and idle pointer cases are
therefore distinct from the frozen selection pass.

The constructive novelty claim is repo-local and narrow: this is the first
campaign artifact to turn two of Cycle 454's remaining mixed G55 rational
directions into fully counted, shared-auxiliary physical programs.  It is not
a claim of historical priority, a derivation of the effect domain, or an
extension of a prior field-theory engine.

## N1 — Alternative route enumeration

1. **Two short denominator-eight directions — ATTEMPTED / CONSTRUCTIVE.**
   The frozen pair reduces projected-old nullity by exactly two.
2. **The other four fixed-G55 rational directions — LIVE / NOT COMPILED.**
   They remain between rank 86 and the algebraic rank-90 ceiling.  The next
   screened representative already needs denominator 37, support 25, and
   coefficient magnitude 100; that is evidence about this short menu, not a
   wall.
3. **Alternative rational bases and lattice reduction — LIVE / NOT
   EXHAUSTED.**  A better basis can change denominators, support, and auxiliary
   cost while spanning the same quotient.
4. **Other already physical G55 rays or mixed-effect spectral addition DAGs —
   LIVE / PARTLY SCREENED.**  The present menu selects only two roots.
5. **A larger finite physical effect inventory — LIVE / NOT ATTEMPTED.**  New
   exact collisions can change both incidence rank and auxiliary economy.
6. **The parametric Cycle-317 effect continuum — LIVE / NOT ATTEMPTED HERE.**
   Its same-ray and mixed-projective forcing is broader than this finite G55
   compiler and remains an explicit counter-route.
7. **Continuous POVM/Gleason-Busch closure — LIVE / NOT ATTEMPTED.**  Its
   eligibility, continuity, and state-selection premises are not imported by
   this cycle.

Because several named constructive routes remain live, no negative conclusion
can pass N1.

## N2 — Wall-independence audit

The denominator-eight, support-20, coefficient-25, fixed-G55, and two-root
bounds define one nested search resolution.  They are not independent walls.
Failure outside this menu would not establish a shared substrate obstruction.
The collapsed wall set for a constitutional negative claim is empty.

## N3 — Hidden-wall scan

The load-bearing inputs are listed below rather than disguised as framework
consequences.  In particular, effect functionality, common contact,
positive-square-root dilation, packet invocation, class equality, the G55
inventory, and the finite menu are supplied.  Exact operator equality does not
by itself supply a physical relation; that is why every auxiliary class and
context is retained in the rank surface.

## N4 — Residual matching

| source | source resolution | Cycle-457 use | match? |
|---|---|---|---|
| Cycle 454 | explicit scaled-ray auxiliaries, rank/nullity `84/20` | retained starting surface | yes |
| Cycle 448 | exact rational G55 relation ceiling, old nullity 14 | route map only | yes |
| Cycle 317 | bounded contact dilation and stack isometry | literal program construction | yes |
| Cycle 440 | finite protected packet and all-24 audit | codec/covariance control | yes |
| continuum comparator | trace representation on a broader eligible domain | not installed | no; live counter-route only |

No continuum conclusion is inferred from a finite exact-rational residual.

## N5 — Rhetoric audit

“Remaining,” “ceiling,” and “short” always refer to the fixed G55 rational
lift and the stated N=8/support/coefficient menu.  “Exact” refers to symbolic
operator equality or sparse reversible equality, not to empirical truth.
“Physical” means compiled through the campaign's declared M2/contact/packet
fixtures; it does not mean derived from the axioms or selected by nature.

## N6 — Partial-closure path scan

The next partial closures remain constructive: compile the other four quotient
directions with a cost-aware rational basis; enlarge the finite effect
inventory; or install an explicitly justified parametric eligibility route.
Any of these can lower the residual nullity without invoking a new axiom.  The
present result therefore gives a route and a cost account, not a stopping
theorem.

## N7 — Steelman

A hostile reviewer should grant the strongest positive result: two exact,
independent mixed-effect directions survive a full auxiliary count, deletion,
held-size, all-frame, inverse, leakage, anti-fit, and mass audit, lowering
projected-old nullity from 20 to 18.  The same reviewer should reject Born
closure: nullity 18 still leaves 15 directions beyond the Pauli tangents, the
fixed-G55 rational ceiling itself is 14, four quotient directions are live,
and broader finite and continuous domains have not been attempted.

## N8 — Cross-cycle echo

The constructive chain is Cycle 317 bounded dilation, Cycle 440 protected
finite packets, Cycle 448 exact rational route mapping, Cycle 454 explicit
same-ray auxiliary arithmetic, and Cycle 457 shared mixed-effect auxiliary
arithmetic.  The cross-cycle echo is constructive: each later cycle exposes
rather than suppresses the auxiliary cost of an algebraic relation.  No prior
negative verdict is repeated, and no echo upgrades this partial result into
an obstruction.

## Supplied / derived / open

### Supplied

- the M2 substrate, common contact fixture, Cycle-317 Kraus/dilation and stack
  isometry, and the L=3/L=6 one-particle fixtures;
- the Cycle-440 G55 effect inventory, effect-functionality premise, installed
  finite menus, pointer codec, invocation rule, and proper-cubic action;
- the Cycle-448 exact radical-coordinate lift and the complete fixed-G55
  rational relation-space computation;
- the Cycle-454 `152 x 104`, rank-84/nullity-20 explicit auxiliary surface;
- exact equality as the class-sharing rule and the frozen N=8 menu bounds.

### Derived

- the two exact relation rows and their independence over the Cycle-454 row
  space;
- the explicit shared `/8`, doubling, coefficient-25, partial-sum, complement,
  and common-root construction;
- 72 gadgets, 144 new rows, 124 new classes, and the complete `296 x 228`
  physical incidence surface;
- full augmented rank 210, full augmented nullity 18, projected-old nullity
  18, and the dependency-closed deletion results;
- train/held physical equivalence, exact E/G and inverse, zero leakage, all-24
  covariance, anti-fit rejection, and preservation of the one-particle mass
  fixture at the reported residuals.

### Open

- physical compilation and cost minimization for the other four exact
  fixed-G55 rational quotient directions;
- whether another rational basis yields materially shorter shared services;
- which larger finite or parametric effect domain is physically eligible;
- derivation of effect functionality, class equality, contact, invocation,
  record formation, state/grade selection, occurrence, probability,
  frequencies, or the Born rule;
- homogeneity, uniqueness, continuum closure, empirical selection, and any
  shared-substrate obstruction or axiom pressure.

The optimal next experiment is a cost-aware lattice-reduced compilation of
the remaining four fixed-G55 quotient directions, with the candidate basis
frozen before physical fitting and the same full auxiliary, deletion,
held-size, all-24, anti-fit, and mass controls.
