---
claim_id: theta_cross_sector_determinant_forcing_property_characterization_bounded_theorem_note_2026-07-17
claim_type: bounded_theorem
claim_scope: "Two route-specific minimal forcing pairs on a supplied determinant-channel surface. For a real scalar phase functional, explicit conjugate-pair cancellation together with K/CPT orbit constancy forces the phase functional to vanish. For a continuous determinant phase character, independent-block multiplication together with K/CPT orbit constancy forces character index k = 0. Exact witnesses show that neither member of either pair can be removed relative to that route. Conjugate-pair cancellation is an explicit supplied boundary condition, not a consequence of Record finite additivity. Conditional on an independently supplied quark-side route condition, orbit constancy is the remaining algebraic sufficient condition; no carrier, physical readout, cross-sector correspondence, exhaustion statement, mass orientation, gauge theta, or theta-bar closure is derived."
upstream_dependencies:
  - minimal_axioms
  - kcpt_orbit_constancy_and_determinant_character_boundary_supplied_context_bridge_note_2026-07-04
  - theta_p2_k_cpt_determinant_character_phase_erasure_bounded_note_2026-06-10
  - registrable_readout_additive_even_phase_free_narrow_theorem_note_2026-06-10
  - strong_cp_determinant_readout_bridge_narrow_theorem_note_2026-06-12
runner: scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py
---

# Theta Cross-Sector Determinant Readout: Two Conditional Phase-Erasure Forcing Pairs

**Date:** 2026-07-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** conditional algebra on supplied readout classes. The conditions below
are not adopted as framework premises or physical identifications.
**Audit-status authority:** independent audit lane only. This note sets no audit
verdict and predicts none.
**Primary runner:**
[`scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py`](../scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py)
**Runner cache:**
[`logs/runner-cache/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.txt`](../logs/runner-cache/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.txt)

## Question

The open
[`theta quark-determinant cross-sector readout obligation`](THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md)
asks whether the charged-lepton `K`/CPT occupancy carrier is the same physical
channel that controls the quark determinant readout, and whether that
identification forces `arg det(M_q) = 0`.

The existing conditional sources expose two algebraic phase-erasure routes:

- the
  [`supplied-context orbit and determinant-character bridge`](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md)
  and the
  [`determinant-character phase-erasure note`](THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md)
  use a continuous block-multiplicative determinant character together with
  `K`/CPT orbit constancy;
- the
  [`registrable-readout note`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
  separates Record finite additivity from the extra phase-group homomorphism
  boundary and explicitly warns that finite additivity alone still admits
  `sum_j cos(theta_j)`.

This note isolates two minimal algebraic forcing pairs. It does not claim a
global biconditional for every combination of readout properties. In
particular, it does not prove anything about a functional required to satisfy
both route-local conditions simultaneously without orbit constancy.

## Supplied Surface And Conditions

Each determinant record carries nonzero complex data
`z = |z| exp(i phi)`. Phase dependence is evaluated at fixed `|z|` on the
circle `phi in R/(2 pi Z)`.

The first route uses a real scalar phase functional `h(phi)` and two supplied
conditions:

- **Conjugate-pair cancellation.** The scalar readout is finitely additive over
  disjoint determinant records and, as an additional supplied normalization,
  the phase contribution of the pair `(phi, -phi)` is the zero phase
  contribution. Thus `h(phi) + h(-phi) = 0`.
- **K/CPT orbit constancy.** Conjugate determinant records have the same scalar
  phase readout, so `h(-phi) = h(phi)`.

The cancellation normalization is not supplied by Record finite additivity.
The current
[`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md) supply finite scalar
additivity over disjoint records only. The pair cancellation is an explicit
boundary condition of this route.

The second route uses a continuous determinant phase character
`f_k(exp(i phi)) = exp(i k phi)`, with integer `k`, and two supplied
conditions:

- **Independent-block character law.** Direct sums multiply determinants, and
  the phase readout respects the product as a continuous circle character.
- **K/CPT orbit constancy.** The character has the same value at `phi` and
  `-phi` for every phase.

The
[`mass-determinant readout bridge`](STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md)
states this second interface conditionally; it does not prove that the physical
quark readout belongs to the class.

## Results

### Conjugate-pair-cancellation route

If conjugate-pair cancellation and orbit constancy both hold, then

```text
h(-phi) = -h(phi)   and   h(-phi) = h(phi),
```

so `h(phi) = 0` for every phase.

The pair is minimal relative to this route:

- Without orbit constancy, define the readout of a finite disjoint collection
  `C` by `I_sin(C) = sum_{phi in C} sin(phi)`. It is real, smooth,
  well-defined on the phase circle, finitely additive under disjoint union, and
  cancels every conjugate pair. It still registers phase and is not
  orbit-constant.
- Without conjugate-pair cancellation, define
  `I_cos(C) = sum_{phi in C} cos(phi)`. It is real, smooth, finitely additive,
  and orbit-constant, but a conjugate pair contributes `2 cos(phi)` and the
  readout registers phase.

These are full finite-record readouts, not merely parity checks on a symbolic
single-record function.

### Determinant-character route

Every continuous character of the determinant phase circle has the form
`f_k(exp(i phi)) = exp(i k phi)` with `k in Z`. Orbit constancy requires

```text
exp(i k phi) = exp(-i k phi)   for every phi,
```

which forces `k = 0`. The registered character is phase-free inside this
supplied class.

This pair is also minimal relative to its route:

- Without orbit constancy, `f_1(exp(i phi)) = exp(i phi)` is a continuous,
  single-valued character at every finite block arity and registers phase.
- Without the character law, `cos(phi)` is smooth, real, single-valued, and
  orbit-constant but still registers phase. It fails the character law because
  `cos(pi) != cos(pi/2) cos(pi/2)`.

### Cross-sector consequence: a conditional reduction only

If a quark determinant channel is independently shown to carry either
conjugate-pair cancellation or the continuous determinant-character law, then
`K`/CPT orbit constancy is the other sufficient algebraic condition in the
corresponding forcing pair. Transporting orbit constancy is therefore a
one-condition algebraic target only after the route-local condition is
supplied.

This is not the physical cross-sector theorem. The open obligation still
requires construction of the quark carrier, identification of its physical
readout, and proof of the cross-sector correspondence. Algebraic similarity,
shared notation, and historical decision text remain insufficient.

Everything here is mass-side registered content. The gauge-side slot and
`theta_bar = theta_gauge + arg det(M_u M_d)` are untouched.

## No-Go Discipline Gate

The narrow negatives are only the route-relative non-removability statements
above. They are not universal no-go claims about future readout constructions.

### N1 — alternative attacks on the two negative boundaries

For “the route-local condition without orbit constancy does not guarantee
erasure,” both `I_sin` and `f_1` survive the following distinct rescue attempts:

| attempted rescue | exact disposition | marker |
|---|---|---|
| require continuity/smoothness | `sin(phi)` and `exp(i phi)` are smooth | ATTEMPTED |
| require a single-valued function on the phase circle | both are `2 pi`-periodic | ATTEMPTED |
| restrict to fixed `|z| = 1` | both witnesses live entirely on that locus | ATTEMPTED |
| require arbitrary finite record/block arity | finite sums of `sin` and finite products of `exp(i phi)` preserve their route laws | ATTEMPTED |
| avoid principal-argument branch artifacts | both witnesses are defined directly on `exp(i phi)` and are branch-independent | ATTEMPTED |
| impose the exact conjugation action | both transform nontrivially under `phi -> -phi`, which is precisely the missing orbit condition | ATTEMPTED |

For “orbit constancy without the route-local condition does not guarantee
erasure,” `I_cos(C) = sum cos(phi)` survives:

| attempted rescue | exact disposition | marker |
|---|---|---|
| require a real scalar | `I_cos` is real | ATTEMPTED |
| require continuity/smoothness | `cos` is smooth | ATTEMPTED |
| require a single-valued circle function | `cos` is `2 pi`-periodic | ATTEMPTED |
| restrict to fixed `|z| = 1` | the witness lives there | ATTEMPTED |
| retain finite Record additivity | the finite sum is additive under disjoint union | ATTEMPTED |
| require exact orbit constancy at every finite arity | termwise evenness gives exact constancy | ATTEMPTED |

### N2 — independence of the two conditions in each route

| condition pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| route-local cancellation / character law; orbit constancy | no — `I_sin` / `f_1` obey the route-local law but not orbit constancy | no — `I_cos` is orbit-constant but obeys neither route-local law | yes |

No wall-count claim is made for the physical obligation; its carrier, readout,
and correspondence criterion is quoted rather than reclassified here.

### N3 — hidden-condition scan

| wording | classification |
|---|---|
| “supplied” route conditions | explicit non-satisfying boundary conditions; not framework content |
| “registered phase” | defined as fixed-radius phase dependence of the supplied readout; no physical identification |
| “determinant character” | explicit continuous circle-character class linked to the source bridge |
| finite Record additivity | current minimal-axiom content only; explicitly separated from pair cancellation and phase-group homomorphism |
| fixed radius and phase circle | explicit mathematical domain; joint radius-phase dependence remains outside scope |

### N4 — residual matching

| cited source | source residual | residual used here | match |
|---|---|---|---|
| [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md), lines 75-83 and 138-146 | homomorphism is supplied; finite additivity admits `sum cos` | finite additivity is not promoted to phase cancellation | exact |
| [`KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md`](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md), lines 91-129 | homomorphism plus orbit constancy kills the phase; `cos` is the hostile guard | determinant-character forcing pair only | exact |
| [`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`](THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md), lines 24-65 | `k = 0` inside a supplied continuous character class; evenness alone is insufficient | same route-relative boundary | exact |
| [`THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md`](THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md), lines 21-26 | carrier, readout, and cross-sector correspondence remain open | physical consequence remains open | exact |

### N5 — rhetoric and resolution

The positive and negative algebra is checked per determinant record, per finite
disjoint record collection, and per finite independent-block product. No
lattice-wide, action-level, joint radius-phase, physical-exhaustion, or
individual-functional biconditional is claimed. “Minimal” always means minimal
within one named two-condition forcing route.

### N6 — partial-closure paths and primitive boundary

The primitive registry was checked. The axioms and three approved primitives
supply no determinant channel, pair cancellation, character law, `K`/CPT
orbit indexing, cross-sector correspondence, or physical exhaustion. This is
not phrased as “a new axiom is required.” The legitimate path is a retained
derivation of the carrier/readout/correspondence criterion in the open
obligation; partial algebraic closures remain conditional until then.

### N7 — steelman

The strongest objection is that conjugate-pair cancellation is an added
normalization equivalent to oddness, not a landed consequence of Record, and
that the two odd-side conditions together without orbit constancy have no
submitted common witness. That objection defeats the original global
property-set biconditional. This note accepts the objection: cancellation is
an explicit supplied condition, the results are two separate forcing pairs,
and no combined-property or global exhaustion claim remains.

### N8 — cross-cycle echo

The closest repo echoes are the registrable-readout repair that separated
finite Record additivity from phase-group homomorphism, the supplied-context
bridge that relocated orbit constancy outside the reset Record axiom, and the
[`theta mass determinant axiom-update no-go`](THETA_MASS_DETERMINANT_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md)
that kept determinant-character algebra conditional on a physical interface.
Each earlier wall was narrowed by premise relocation rather than declared a
new axiom. The same mechanism is applied here: every extra condition is named,
and the physical bridge stays open.

**No-Go Discipline status: PASS** for these route-relative counterexample
boundaries. The broader property-set iff is not shipped.

## Non-Claims

- No physical quark determinant readout, carrier, cross-sector identity,
  exhaustion theorem, orientation selector, gauge-theta result, or theta-bar
  closure is derived.
- No axiom or approved primitive supplies or is enlarged by a route condition.
- No measured, fitted, lattice-MC, PDG, or literature value is consumed.
- No audit verdict or effective status is authored.

## Verification

The paired runner checks the two forward eliminations and full route-relative
counterexamples: finite-record additivity and conjugate-pair cancellation for
`I_sin`; finite-block character composition for `f_1`; finite-record
additivity, orbit constancy, and phase registration for `I_cos`; symbolic block
determinant multiplication; circle wrapping and branch-independent witness
behavior; and source needles for the exact physical boundary. It does not test
or claim the physical cross-sector bridge.
