---
claim_id: born_form_from_lawful_graded_constraint_composite_gleason_bridge_note_2026-07-04
claim_type: bounded_theorem
claim_scope: "Bridge-conditional: if a lawful graded record-conditioned constraint exists and exposes full neighbor-composite projection menus, Gleason's theorem forces Born trace form on the composite and therefore on single-site restrictions. The grading primitive and entangled-menu eligibility are assumed here, not adopted."
upstream_dependencies:
  - minimal_axioms
bridge_inputs:
  - gleason_theorem_1957
runner: scripts/born_form_composite_gleason_bridge_2026_07_04.py
---

# Born Form From Lawful Graded Constraint via Composite Gleason (Bridge Note)

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; the grading primitive and entangled-menu
eligibility are assumed here, not adopted.
**Audit-status authority:** independent audit lane only. This note sets no audit
verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or enlarged
here. The graded-constraint premise is conditional input only.
**Primary runner:**
[`scripts/born_form_composite_gleason_bridge_2026_07_04.py`](../scripts/born_form_composite_gleason_bridge_2026_07_04.py)
**Runner cache:**
[`logs/runner-cache/born_form_composite_gleason_bridge_2026_07_04.txt`](../logs/runner-cache/born_form_composite_gleason_bridge_2026_07_04.txt)

## Purpose

The landed framework supplies a `Z^3` nearest-neighbor lattice, one-site
possibility algebra `M_2(C)`, local admissibility by nearest-neighbor
conditions, and Record content: Records form.; when present, a record locks
exactly one admissible local possibility, records are permanent, one site
carries at most one record, only records are readable, and finite scalar readout
is additive over disjoint records. Those axioms do not supply probabilities,
weights, dynamics, update rules, or record-production processes.

This note isolates one conditional mathematical point in the graded-constraint
program: if record influence on possibility menus is lawfully graded, and if
the local lattice structure exposes the full projection lattice of a neighbor
composite, then the form of that grading is forced. The note does not claim that
the grading primitive exists.

## Authorities and Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — source for
  the `Z^3` nearest-neighbor lattice, one-site `M_2(C)` possibility domain,
  local admissibility by nearest-neighbor conditions, and Record sentences used
  above. These axioms do not supply probabilities, weights, dynamics, update
  rules, or record-production processes.
- Gleason's theorem (1957) — named bridge input only; this note uses the
  dimension `>= 3` trace-form consequence and does not re-prove the theorem.

## Bridge Input

**Bridge input:** Gleason's theorem (1957) - every non-negative frame function
on the projection lattice of a Hilbert space of dimension >= 3 has the form
`w(P) = Tr(rho P)` for a density operator `rho`.

This is cited as classical mathematics, not re-proved. The framework-specific
content is the lattice/composite use of that bridge: a one-site `M_2(C)` surface
has the usual dimension-2 loophole, while a nearest-neighbor bonded pair has
`M_2 tensor M_2 = M_4`, so the composite is inside Gleason's dimension range.

## Hypotheses

**H1 (grading exists).** There is a weight function `w >= 0` defined on every
projection of the relevant algebra, with `w(0) = 0` and `w(identity) = 1`, and
with menu-normalization `sum_i w(P_i) = 1` on every eligible menu (finite
orthogonal resolution of the identity). This is the candidate primitive: it is
assumed here, not claimed, derived, approved, or registered.

**H2 (additivity).** For orthogonal projections `P` and `Q`, the grading is
additive: `w(P + Q) = w(P) + w(Q)`.

**H3 (non-contextuality).** The value `w(P)` does not depend on which admissible
menu embeds `P`.

**H4 (composite menus realized).** Menus range over neighbor-composite
algebras: a bonded nearest-neighbor pair carries `M_2 tensor M_2 = M_4`, `w` is
defined on the full projection lattice of the composite, and every finite
orthogonal resolution of the composite identity - including resolutions that
contain entangled projections - is menu-eligible, so H2 applies to all
orthogonal pairs in `Proj(M_4)`. Without this full projection-measure strength
a partial menu assignment is not a frame function and Gleason does not apply
(refutation-seat finding, 2026-07-04).

H4 is a substantive physical hypothesis, not axiom content. The minimal axioms
supply site-local possibility domains with neighbor-dependent availability -
not a pair-level possibility domain, not bonded-pair selection, not
configuration-independent menu eligibility, and not records that lock composite
entangled possibilities. Any registration of the graded-constraint primitive
must therefore specify: which neighbor pairs carry composite menus; whether
eligibility depends on the record configuration; how pair menus coexist with
site-local admissibility; and in what sense entangled projections are
alternatives. Those four items are the registration's specification burden,
declared here rather than hidden.

## Results

**R1 (single-site exception, constructive).** On one `M_2(C)` site alone,
H1-H3 do not force the Born form. Rank-1 one-site projections are indexed by
Bloch directions `n`, with binary menus `{P(n), P(-n)}`. Any assignment
`g(n) >= 0` with `g(n) + g(-n) = 1` is a normalized frame function on those
menus. A non-quadratic example is the hemisphere/sign rule used by the runner:
`g(n)=1` when `(n_z,n_y,n_x)` is lexicographically positive and `g(n)=0`
otherwise, with the equator made well-defined by the same lexicographic tie
rule. It normalizes every antipodal menu and is non-contextual on the one-site
binary menus, and it extends to rank `0` and rank `2` by `g(0) = 0`,
`g(I) = 1`. Its non-quadraticity is exact, not merely sampled: any trace form
is affine in the Bloch direction, so `g(e_x) = g(e_z) = 1` with `g(I) = 1`
forces the value `1/2` at the direction `(e_x - e_z)/sqrt(2)`, while the
lexicographic rule assigns `0` there. Three directions plus normalization
refute every `2x2` trace form at once; the sampled least-squares fit is kept
only as a secondary bound and control.

**R2 (composite rescue).** A bonded neighbor pair has Hilbert dimension `4`,
which is `>= 3`, so Gleason applies to any `w` satisfying H1-H4 on the pair.
There is a density operator `rho` on the pair such that `w(E) = Tr(rho E)` for
composite projections `E`. For embedded single-site projections this gives
`w(P tensor I) = Tr(rho (P tensor I)) = Tr(rho_1 P)`, where `rho_1` is the
partial trace over the neighbor. Thus the single-site restriction is quadratic:
it has Born form. The value of `rho` is determined by conditioning, here by
records, but this note does not derive those values.

**R3 (exception voided).** The R1 rogue functions do not extend to any grading
that satisfies H1-H4 on the neighbor composite. If such an extension existed,
R2 would force the embedded single-site restriction to have the quadratic Born
form `Tr(rho_1 P)`, contradicting the explicit non-quadratic R1 assignment. The
nearest-neighbor lattice is what makes a composite available; H4's full
composite projection measure is what voids the dimension-2 loophole. The
attribution matters: adjacency alone pays for nothing here without H4's
strength.

**R4 (zero-information limit).** Under an explicit additional premise -
invariance of `w` under every unitary automorphism of the composite, whose
commutant is scalar - `rho = I/d` follows. This full-symmetry premise is named
here; it is not derived from H1-H4 or from the minimal axioms, and "no
conditioning records" alone does not supply it. Under it, weights are uniform
on symmetric menus: `1/2` on embedded one-site rank-1 binary alternatives in a
pair, and `1/4` on the Bell-basis rank-1 composite menu. This is consistent
with the landed uniform-on-orbits results and adds no new selection claim.

## No-Go Discipline Gate

- **N1 route inventory:** direct one-site Gleason is unavailable in dimension
  `2`; imposing H1-H3 alone leaves the constructive rogue `g`; using the
  neighbor composite invokes an explicit bridge input plus H4; deriving grading
  values from records is downstream and not attempted.
- **N2 primitive boundary:** H1 is the candidate primitive. The note assumes it
  only to determine form; it does not approve, register, rename, or strengthen
  any primitive.
- **N3 hidden-wall scan:** H4 does not smuggle dynamics - no rates, histories,
  updates, transition kernels, Hamiltonians, or record-production. It DOES
  import pair-level menu ontology beyond the minimal axioms (pair possibility
  domain, entangled alternatives, eligibility structure); that import is
  declared inside H4 as the registration's specification burden rather than
  hidden.
- **N4 bridge-source honesty:** Gleason's theorem is imported as named
  classical mathematics. The runner checks the finite-dimensional consequences
  used here; it does not pretend to re-prove Gleason.
- **N5 steelman:** "This is just textbook Gleason." Reply: the bridge input is
  textbook, but the framework content is R1/R3 plus H4's declared specification
  burden - one `M_2(C)` site admits rogue frame functions, and the neighbor
  composite is where H4's projection-measure strength voids the loophole.
- **N6 hidden-value scan:** The theorem fixes form, not values. Record
  conditioning of `rho`, if admitted anywhere, is downstream content outside
  this note.
- **N7 scope guard:** The note does not touch orientation, scale, rate, time,
  readout-context selection, record production, or physical persistence. It is
  only a conditional bridge about menu weights.
- **N8 audit hygiene:** No audit verdict is set, forecast, or implied; no axiom
  or primitive file is changed; no claim is made that H4 follows from the
  minimal axioms.

## Non-Claims

- Does **not** claim H1, the graded-constraint primitive, is approved or exists.
- Does **not** derive weight values; record-conditioning of `rho` is downstream.
- Does **not** touch orientation, rate, scale, record production, dynamics,
  update rules, or persistence.
- Does **not** set an audit verdict or close a wall.
- Does **not** re-prove Gleason's theorem; Gleason is the named bridge input.

## Verification

The companion runner is a mechanical harness, not the proof: the load-bearing
steps are the named bridge input and the exact R1 contradiction. It performs
needle checks against the note and the minimal axiom memo; constructs the R1
rogue frame function and verifies the exact three-direction contradiction
against every `2x2` trace form, keeping the sampled least-squares
Hermitian-trace-form fit (a superset of Born density forms) as a secondary
bound with a Born-form control; verifies partial-trace bookkeeping identities
for product, Bell, and maximally mixed states (implementation checks, not R2
evidence); checks embedded and Bell menu normalization; checks the maximally
mixed consequences for the separately-premised R4 limit; and exercises
additivity and non-contextuality rejectors. R3 is carried as a corollary of
the bridge input plus the exact R1 contradiction, and the runner labels it so.

Measured runner total after final verification: `TOTAL: PASS=24 FAIL=0`.
