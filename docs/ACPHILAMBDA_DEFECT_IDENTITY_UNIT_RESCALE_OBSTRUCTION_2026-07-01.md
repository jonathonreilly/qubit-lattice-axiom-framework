# AC_phi_lambda Defect Identity-Unit Rescale Obstruction And Junction Localization

**Date:** 2026-07-01
**Claim type:** bounded_theorem
**Scope:** bounded route no-go / selector narrowing + wall consolidation over
the enumerated homogeneous premise surface.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, adopt a
convention, or claim `AC_phi_lambda` retirement.
**Primary runner:**
[`scripts/acphilambda_defect_identity_unit_rescale_obstruction_2026_07_01.py`](../scripts/acphilambda_defect_identity_unit_rescale_obstruction_2026_07_01.py)

## Target

Inside the selected local C3 fixed-defect scalar class, finite additive scalar
readout has the one-parameter normal form

```text
I_c(R) = c * |R| * L,    L = L3(1,2) = 2/9,
```

and the charged-lepton phase value is the identity-unit member `c = 1`. The
normal form and the wall name

```text
W_defect_identity_unit:
  the physical charged-lepton phase readout uses the identity unit c=1 on the
  selected local C3 fixed-defect density line
```

are stated by the in-flight phase-defect stack (PR #4760, PR #4771, with the
selection-independence witness PR #4762); their audit status is set only by
the independent audit lane. This note is self-contained: the normal form is
re-derived below from the Record axiom clause alone, so nothing here depends
on those files landing.

This note proves four bounded results about `W_defect_identity_unit` and
localizes it exactly.

## Self-Contained Normal Form

The [Record axiom](MINIMAL_AXIOMS_2026-06-29.md) supplies, verbatim:

```text
Only records are readable. For any finite collection of pairwise-disjoint
records, scalar readout I is additive, with I(empty)=0.
```

On a class of selected-defect records whose scalar dependence factors through
the single density value `L = L3(1,2) = 2/9` (retained
[`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
fixed-locus arithmetic), additivity determines `I` from the singleton value
`u = I({D})`: for `n = |R|` pairwise-disjoint records, `I(R) = n*u`. Writing
`c = u/L` gives `I_c(R) = c*|R|*L`, and conversely every real `c` defines a
finite additive readout. The identity-unit member is `c=1`, `I({D}) = 2/9`.

## Result T1 — Rescale Obstruction On The Scanned Premise Surface

**Claim.** Every readout-facing clause in the current premise surface is
invariant under the global unit rescale `I -> lambda * I` (`lambda != 0`).
The premise-satisfying set on the selected defect line is therefore closed
under rescale and contains the full line `{I_c}`; no derivation drawn from
this scanned surface can single out the identity-unit member `c = 1`.

The scanned clauses, with their sources:

| Clause | Source | Rescale behavior |
|---|---|---|
| `I(empty) = 0` | Record axiom | invariant (`lambda * 0 = 0`) |
| additivity over finite disjoint collections | Record axiom | invariant (linearity) |
| a record locks exactly one available local possibility | Record axiom | value-free: constrains which possibility, never the scalar |
| invariance under repeated readout | Record axiom | value-free |
| dependence only through the local density line | selected-class definition | invariant (equal densities keep equal values) |
| translation / proper cubic-rotation covariance | Lattice axiom + selected context | invariant |
| disjoint-refinement consistency (composite reads the sum of parts) | additivity corollary | invariant |
| same unit serves all lanes/sectors | cross-lane covariance | invariant (a global `lambda` preserves unit-sharing) |
| `scale_reference_primitive` granted content | [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md): "This is a units conversion, not a physics axiom. It carries zero dimensionless content: no mass ratio, coupling, mixing angle, phase, selector, readout bridge, or empirical fit is supplied by it." | grants nothing dimensionless; `c` is dimensionless |
| `kinetic_isotropy_primitive` granted content | [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md), same boundary clause | grants no selector/readout bridge |
| `realized_state_primitive` granted content | [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md): "This is pointwise evaluation, not a state-selection rule. It carries zero state-contingent content: no state, ..., normalization rule, or value is supplied by it." | grants evaluation of an already-selected functional; selecting the functional is the wall |

The Record axiom's registry node
([`docs/audit/data/axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json),
`minimal_axioms`) states the exclusion directly:

```text
It still supplies no context-selection rule, formation rule (which admissible
possibility a new record locks, at which site, with what weight, or at what
rate), weighting, normalization, probability, update law,
measurement/decoherence dynamics, K/CPT structure, central-sector
decomposition, source/action bridge, physical observable bridge, or downstream
theory consequence.
```

The runner verifies each encoded clause is satisfied by `lambda * I` whenever
it is satisfied by `I`, over exact rational grids. The scan is
refutation-shaped: a premise clause that secretly broke the rescale symmetry
would fail the invariance check and falsify this result.

**Corollary (shape criterion).** A solution set closed under rescale can
have a unique member only at the fixed point of the rescale group, the zero
readout. Homogeneous record/covariance/consistency clauses can therefore at
most force `I = 0`; they can never single out a specific nonzero unit, and
adding more of them cannot change that. Any successful derivation of `c = 1`
must contain at least one rescale-breaking (inhomogeneous) readout clause, or
must produce the phase natively in a variable that has no unit freedom at all
(see T3).

## Result T2 — The Atom-Count Normalization Pins The Wrong Member

The one rescale-breaking normalization available from bare record structure
is the count: "one locked atom reads `1`". The count `N(R) = |R|` is a legal
finite additive readout (it is the occupancy-type surface). But on the
density line it is the member

```text
u = N({D}) = 1  =>  c = u / L = 1 / (2/9) = 9/2  !=  1,
```

so a phase readout equal to the count would register `|delta| = 1` per
surviving atom, not `2/9`. Exact arithmetic: `9/2 != 1`. The count route is
therefore doubly blocked: identifying the phase readout with the count is
itself an unproven selection, and even granted, it selects the wrong member.

The repaired variant — "one locked atom reads one unit of the density `L`" —
is the constraint `I({D}) = L`, which is `c = 1` verbatim. As a premise it
restates the target; it is exactly the normalization the finite rescale
witnesses are free to deny, and the Record axiom's registry exclusion
("supplies no ... weighting, normalization, probability ... physical
observable bridge") says the axiom does not supply it. The Record clause
"locks exactly one local possibility" constrains which possibility is locked,
never the scalar value a readout surface attaches to the lock.

## Result T3 — Angle-Side Rigidity: The Unit Freedom Is Not An Angular Convention

The retained charged-lepton surface is the circulant chamber form

```text
x_k = v0 * (1 + sqrt(2) * cos(delta + 2*pi*k/3)),   k in Z3
```

([`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md),
retained;
[`BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md`](BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md),
retained_bounded: Hermitian generators commuting with the cyclic shift have
this circulant form; no derivation of `delta` is audited there).

Consider an angular-unit rescale of the readout surface, `theta -> c*theta`,
applied to all angles the surface reads. Two exact facts:

1. **Lattice closure.** The read generation lattice `{c * 2*pi*k/3 mod 2*pi}`
   equals the Z3 character lattice `{2*pi*k/3}` iff `c` is an integer with
   `c mod 3 != 0`. No continuous `c` survives; the angular spacing `2*pi/3`
   is pinned by the forced circulant structure (`omega^3 = 1`).
2. **Registered-spectrum preservation.** Among the surviving integers, the
   registered unordered spectrum `{x_k}` is preserved for all offsets `delta`
   iff `c = +1` or `c = -1`. The member `c = -1` is conjugation — exactly the
   sign already stripped by the registrable unordered-spectrum layer
   (`|delta|`). Even the discrete lattice survivors `c = 2, 4, ...` change
   the registered multiset (runner check: at `delta = 2/9` the `c = 2` read
   differs from the `c = 1` read by more than `0.3` in a spectrum of order
   one), so they are different readouts, not re-descriptions.

**Consequence (junction localization).** The `c`-line freedom of the unit
normal form cannot be absorbed as an angular unit convention: on the retained
surface the angular variable carries no continuous unit freedom, and beyond
the stripped sign no discrete freedom either. Distinct `c` are physically
distinct readouts. The entire one-parameter freedom therefore sits at the
density-to-angle junction — the identification of the fixed-locus density
number `2/9` with the angular offset `delta` — and nowhere else.

That junction already has two registered names:

- Tier-A `AC_phi_lambda` sub-admission (ii), verbatim from
  [`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json):
  "the delta readout identification
  R-eta (density-read-as-angle; the magnitude 2/9 is retained-bounded
  fixed-locus arithmetic conditional on R-eta, not an admitted number)".
- The retained_no_go row
  [`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md),
  scope: the
  listed sources "do not derive the literal 2/9-radian selected-line bridge;
  the Type-B-to-radian identification remains primitive."

**Consolidation.** `W_defect_identity_unit` names no new wall. In normal-form
coordinates it is the unit coefficient of the R-eta density-read-as-angle
junction. One wall, three names: `W_defect_identity_unit` (unit normal form),
R-eta sub-admission (ii) (Tier-A registry), Type-B-to-radian identification
(radian-bridge row). Audit surfaces should treat these as one dependency, not
two or three.

## Result T4 — The Standing Interfaces Are Unit-Blind

Four interfaces that might have been expected to pin the unit provably cannot:

1. **Koide guardrail.** `Q = p2/e1^2 = 2/3` exactly for every `delta` and
   `v0` (retained identity; re-verified symbolically in the runner). A
   `delta`-blind functional is `c`-blind.
2. **Born-facing normalization.** Projective normalization `sum p = 1` is
   satisfiable for every `c` (choose the overall factor); the normalization
   interface rejects no member. Probability normalization fixes state-weight
   scale, not the angular offset unit.
3. **Cross-lane transport.** The same-unit-across-lanes clause is itself
   rescale-invariant: transport propagates one global `c` but cannot pin its
   value unless some lane independently supplies an absolute pin, and the
   scanned surface contains none.
4. **Ratio / unit-bypass.** The multiplicative unit-bypass pattern (live in
   the in-flight source-response lane, e.g. response-ratio normal forms)
   does not port to an additive angular offset: `v0`-rescale leaves all
   registered ratios invariant (that is the vacuous `Y0`/`g0`-type
   convention), while `delta -> c*delta` moves registered ratios (runner
   check: the smallest-over-middle ratio moves by more than `3*10^-2`
   between `c=1` and `c=1/2`). The unit `c` is substantive physics, not a
   vacuous rescaling convention — so the convention-adoption route does not
   dispose of it either.

## What This Moves

| Before | After |
|---|---|
| `W_defect_identity_unit` a candidate for derivation from Record additivity + atom-unit normalization | blocked on the scanned surface: additivity is rescale-invariant (T1); the count pins `9/2` (T2); count-in-`L`-units restates the target (T2) |
| unit freedom possibly an angular normalization convention | refuted: the angle side is rigid; distinct `c` are distinct physics (T3) |
| unit freedom possibly a vacuous `Y0`/`g0`-type convention | refuted: registered ratios move with `c` (T4) |
| `W_defect_identity_unit` a possibly new wall beside R-eta | consolidated: it is the R-eta junction coefficient in normal-form coordinates (T3) |
| winning-route shape unconstrained | constrained: angle-native output or a rescale-breaking readout clause (T1 corollary) |

## The Next Paths This Opens

The obstruction is constructive about what a winning theorem looks like:

- **Angle-native route (sharpest).** Derive the charged-lepton phase directly
  as an angle on the retained circulant/U(1) surface — an eta/holonomy or
  same-surface source/action theorem whose output *is* the angular offset.
  On that route no unit parameter ever arises: the angular variable has no
  unit freedom (T3), and the retained boundary row
  [`PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md`](PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md)
  records that U(1) phase is native on the finite Hilbert surface. The
  remaining work is then a same-surface equality: show the produced angle
  equals the fixed-locus density value `2/9` by derivation.
- **Rescale-breaking bridge.** Supply a record-facing readout clause that is
  genuinely inhomogeneous — e.g. a derived instrument/registration theorem
  fixing a singleton readout value from named retained structure. T2 shows
  the bare count is available but pins `9/2`; a winning clause must pin the
  density-line member, and must derive rather than declare it.
- **Owner-governance primitive.** The narrow operational selector
  (`P_readout_selection` instance for this lane) remains an explicit
  owner-approval option if bridge-first work is intentionally bypassed. It is
  a governance route, not a derivation.

## Non-Claims

This note does not claim:

- the direct C3 defect scalar or the identity unit `c=1` is false;
- `c = 1` cannot be derived by a future angle-native, eta/holonomy,
  source/action, or record-facing rescale-breaking theorem;
- the C3 arithmetic (`L3(1,2) = 2/9`) or the unit normal form is reopened;
- the R-eta admission is retired, re-graded, or newly created;
- the Record axiom is defective, or any axiom edit is needed;
- probability, occurrence, theta, source/action, metric, or
  measured-observable gates are closed;
- any convention is adopted (convention adoption is audit-decided and is in
  any case shown inapplicable here by T4.4).

## Audit Consequence If Retained

Rows that need `|delta| = 2/9` keep the sharpened dependency shape

```text
selected C3 defect-density line
  + physical identity-unit readout selector (== R-eta junction coefficient)
  -> |delta| = 2/9,
```

with three additions from this note: (i) the selector is not derivable on the
scanned homogeneous premise surface; (ii) it is not a vacuous convention, so
convention adoption is not the disposal route; (iii) it is the same
dependency as Tier-A sub-admission (ii) R-eta — dependency graphs should not
count `W_defect_identity_unit` and R-eta as independent walls.

## No-Go Discipline Gate

This checklist supports only a bounded route no-go over the scanned surface
plus positive rigidity/consolidation theorems. It is not a terminal no-go: the
angle-native and rescale-breaking bridge routes are live and are named with
their required shape.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Record-additivity route | Derive `c=1` from the Record readout clause. | BLOCKED HERE (T1): every Record clause is rescale-invariant; the c-line is one orbit. |
| Atom-count normalization route | "One locked atom reads 1" forces identity units. | BLOCKED HERE (T2): pins `c = 9/2 != 1`; also an unproven class selection. |
| Count-in-density-units route | "One locked atom reads one unit of `L`". | BLOCKED HERE (T2): restates `c=1`; excluded as axiom content by the registry node text. |
| Realized-state evaluation route | Read `c=1` off pointwise evaluation at the realized state. | BLOCKED at the primitive's own boundary: evaluation of an already-selected functional; "no ... normalization rule, or value is supplied by it". Selecting the functional is the wall. |
| Scale/kinetic primitive route | Use an approved primitive to supply the unit. | BLOCKED at their boundary text: "zero dimensionless content: no ... phase, selector, readout bridge"; `c` is dimensionless. |
| Angular-convention route | Absorb `c` as an angle-unit convention. | REFUTED HERE (T3): the angle side admits only `c = +-1`; `-1` is the stripped sign. |
| Vacuous-convention route | Treat `c` like `Y0`/`g0` vacuous rescalings. | REFUTED HERE (T4): registered ratios move with `c`. |
| Born-normalization route | Pin the unit via `sum p = 1`. | BLOCKED HERE (T4): satisfiable for every `c`. |
| Cross-lane transport route | Import the unit from another lane. | NOT A PIN on the scanned surface (T4): transport is homogeneous; no lane holds an absolute pin. |
| Ratio/unit-bypass route | Port the source-lane multiplicative bypass. | BLOCKED HERE (T4): offsets do not cancel in ratios. |
| C3-arithmetic route | Force the unit from the fixed-locus arithmetic. | OUT OF SCOPE BY RETAINED TEXT: the fixed-locus row excludes physical readout from its scope. |
| Source/action or eta/holonomy route | Produce the phase natively as an angle, or a rescale-breaking insertion. | OPEN — the named live shape (see "Next Paths"). |
| Record-facing instrument/registration theorem | Derive an inhomogeneous readout clause. | OPEN — must pin the density-line member, not the count. |
| Owner primitive route | Approve the narrow selector operationally. | GOVERNANCE OPTION, not a derivation. |

### N2 - Wall-Independence Audit

Collapsed wall set: one wall,

```text
W_defect_identity_unit == R-eta density-read-as-angle junction coefficient.
```

The consolidation (T3) removes a potential double-count: the unit selector
and the R-eta sub-admission are the same dependency. Occurrence,
source/action, theta, and metric gates are separate lanes, not counted here.

### N3 - Hidden-Wall Scan

| Term | Classification |
|---|---|
| `selected local C3 fixed-defect scalar class` | Input from the in-flight normal-form stack; re-derived here self-contained; its physical selection is the enclosing wall, not assumed. |
| `density line` / `L = 2/9` | Retained fixed-locus arithmetic; its scope excludes physical readout, and this note uses only the arithmetic. |
| `retained circulant surface` | Retained rows quoted with scope; no `delta` derivation is imported from them. |
| `rescale-breaking clause` | Shape criterion produced by T1; not itself a premise. |
| `angular unit` | Probe variable of T3; the theorem shows it does not exist as a freedom on the retained surface. |
| `physical` | Marks the missing selector, exactly as in the independence witness. |

No hidden admission is used; no new admission is proposed.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| in-flight PR #4771 unit normal form | `W_defect_identity_unit` open | same wall, now obstructed on the scanned surface and consolidated onto R-eta | yes |
| in-flight PR #4762 independence witness | current premises do not select the readout class | upgraded from a two-point witness to orbit closure under rescale (T1) | yes |
| `koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24` | Type-B-to-radian identification primitive | same junction, reached from the normal-form side | yes |
| Tier-A sub-admission (ii) R-eta | density-read-as-angle identification admitted | shown to be the same dependency as the unit selector | yes |
| `planck_target3_phase_unit_edge_statistics_boundary_note_2026-04-25` | absolute dimensional action quantum not derived (U(1) phase native) | same wall-class on a different lane: absolute unit identifications need non-homogeneous input | yes |

### N5 - Rhetoric Audit

The proven sentences are: (T1) every clause on the *scanned, enumerated*
premise surface is rescale-invariant, hence that surface does not derive
`c=1`; (T2) the count pins `9/2`; (T3) angular rescales preserving the
retained structure are exactly `+-1`; (T4) the four named interfaces are
unit-blind. Tested at finite singleton/disjoint-record resolution and on the
retained circulant chamber form. No claim is made about routes that supply
new inhomogeneous structure or produce the phase angle-natively; those are
the named live paths.

### N6 - Partial-Closure Path Scan

Live paths, with required shape (from the T1 corollary):

- angle-native eta/holonomy or source/action theorem whose output is the
  angular offset itself, followed by a same-surface equality with `2/9`;
- record-facing instrument/registration theorem deriving an inhomogeneous
  singleton readout clause that pins the density-line member;
- owner-approved narrow operational selector (governance).

### N7 - Steelman

A hostile reviewer can press two objections. First: T1 scans a *named* clause
list; a derivation might use structure not on the list. Correct — that is why
the result is scoped to the enumerated surface, with the scan
refutation-shaped and the corollary stated as a shape criterion rather than a
universal impossibility. Second: the consolidation (T3) might be read as
mere renaming. The reply is that it has audit content: it prevents
double-counting the unit selector and R-eta as independent walls, and it
proves the freedom cannot be pushed into the angular variable — which refutes
two seemingly-open disposal routes (angular convention, vacuous convention)
that renaming alone would leave open.

### N8 - Cross-Cycle Echo

The same wall-class — an absolute unit/normalization identification that
homogeneous structure cannot supply — recurs as: the radian bridge
(this junction, 2026-04-24), the absolute action quantum
(`planck_target3`, retained_no_go), the EW `kappa_EW` physical readout, the
quark scalar readout underdetermination, and the source-lane unit normal
forms now in flight. The uniform lesson holds here: finite algebra reduces a
selector to one parameter; picking the physical member needs a bridge with
non-homogeneous content or a variable with no unit freedom.

## Verification

Run:

```bash
python3 scripts/acphilambda_defect_identity_unit_rescale_obstruction_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=106 FAIL=0
```
