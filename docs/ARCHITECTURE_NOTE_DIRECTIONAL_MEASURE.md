---
claim_id: architecture_note_directional_measure
claim_scope: >-
  Conditional on BETA-DIRECTIONAL, the six deterministic fixed-seed fixture
  checks hold as computed; beta is supplied and is not derived by this claim.
---

# Architecture Note: Directional Path Measure

**Status:** supplied-premise bounded theorem candidate.
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Date:** 2026-04-05 (original); 2026-05-03 (review-loop repair);
2026-05-10 (REPAIR_TARGETS #1 PATH B tuned-support demotion);
2026-07-07 (supplied-beta conditional recut).
**Primary runner:**
[runner](../scripts/architecture_directional_measure_table_runner_2026_05_03.py)
(deterministic, offline, fixed fixtures and fixed seeds; latest local run
FATAL TOTAL: PASS=6 FAIL=0).
**Status authority:** independent audit lane only; source labels here are
claim-boundary declarations, not audit verdicts.
**Beta-derivation status:** **SUPPLIED PREMISE - NOT DERIVED.** The named
premise below quarantines the historical observable matching. The note does
not derive beta, does not select beta, and does not use the selection history
as claim content.

## Safe Statement

This note makes one bounded claim. Conditional on the named supplied premise
BETA-DIRECTIONAL, the deterministic runner recomputes six fixed-fixture checks:

- T1 detector-probability partition fixture consistency.
- T2 phase-free two-source visibility fixture consistency.
- T3 real detector amplitudes at k = 0.
- T4 gravity sign count over eight fixed seeds.
- T5 gravity scaling over fixed 3D gravity-card fixtures.
- T6 beta-sweep monotonicity for the Gaussian directional-weight family.

The load-bearing content is the conditional finite computation at the supplied
value and the exact algebra used by that computation. Observable matching,
nearest-rational numerology, moment matching, imported eikonal slopes, and live
historical numerical values are motivation exhibit only.

This note does not establish a derivation of beta = 0.8, uniqueness of the
angular kernel, a framework gravity law, a full 3D Sorkin theorem, or a
decoherence solution.

## Named Conditional Premises

There is one named supplied premise:

BETA-DIRECTIONAL (named conditional premise): the directional-measure Gaussian
width parameter is SUPPLIED as beta = 0.8. Its historical selection story is
motivation-tier history, stated accurately below; it is not load-bearing claim
content.

The fixed DAG fixtures, fixed seeds, and printed thresholds are executable test
conditions. They are not additional physical axioms and do not derive beta.

## Exact Identities (Unconditional)

The architecture history records the directional path-measure propagator on
finite DAGs:

```text
amplitude(edge) = exp(i k S_spent) / L^p * exp(-beta theta^2)
S_spent = delay - sqrt(delay^2 - L^2)
theta = acos(dx / L) in 3D
theta = atan2(abs(dy), dx) in 2D
```

The current runner's 2D T1/T2 fixture uses the same directional weight with
phase-free edge action `S_spent = 0`; those rows are fixture-consistency checks,
not phase-interference or k-variation checks. Its 3D T3-T5 calls consume the
helper module-global `three_d_angle_weight.BETA`, which the runner sets and
asserts equal to the supplied premise value before calling the helpers. T6 is
a beta sweep and does not use a single fixed beta value.

For assigned real beta, theta, L, delay, and k, the following identities are
plain finite algebra:

- The directional factor `exp(-beta theta^2)` is a positive real multiplier.
- Path amplitudes are finite sums of finite products over the fixture DAG.
- At k = 0 with real source amplitudes and no oscillating phase, the propagated
  detector amplitudes are real up to floating-point roundoff.
- For disjoint detector groups A and B, the finite probability sum over
  `A union B` equals the sum over A plus the sum over B.
- For a finite theta list, the runner's weighted second moment is exactly
  `sum(exp(-beta theta^2) theta^2) / sum(exp(-beta theta^2))`.

These identities do not select beta and do not prove that the Gaussian family
is uniquely determined by the accepted primitive surface.

## Conditional Chain

Under BETA-DIRECTIONAL, the runner uses beta = 0.8 for T1-T5 and includes that
value as the center point of the T6 sweep. These checks are the load-bearing
content of this note.

| id | load-bearing conditional check | deterministic condition |
| --- | --- | --- |
| T1 | detector-probability partition fixture consistency | deviation < 1e-12 |
| T2 | phase-free two-source visibility fixture consistency | V > 0.95 |
| T3 | k = 0 real amplitude | max imaginary detector amplitude < 1e-12 |
| T4 | gravity sign count | current runner truth: attract = 6/8, threshold >= 5/8 |
| T5 | gravity scaling | R(N) positive on N = 8, 12, 16, 20; R(16), R(20) > R(8) |
| T6 | beta-sweep monotonicity | weighted theta^2 decreases on the fixed beta list |

T4 reconciliation: the historical note table listed 5/8 attract. The current
runner truth is 6/8 attract over the eight fixed seeds. The old 5/8 entry is
kept below as historical table evidence; it is not the live claim.

No value from the motivation exhibit below is consumed by T1-T6.

## Motivation Exhibit

**evidence only; not load-bearing; no value below is consumed by any claim**

This section preserves the historical numerical-match record, the PATH A/PATH B
disposition history, the beta-derivation-status discussion, and the old table
context. It is kept as motivation and audit history only.

### Historical Source Boundary (2026-06-12)

**Boundary:** bounded tuned support only. Effective status is
audit-derived; this source records only the claim boundary.

The tested table was historically treated as valid at the fixed beta = 0.8
surface. The value beta = 0.8 was an empirical/tuned input selected by
observable matching, not a derived framework constant. This note may be cited
only for the bounded smoke/table checks at that fixed tuned point. It may not
be cited as a derivation of the directional-measure kernel, the angular weight,
the beta parameter, or a framework gravity law.

Promotion beyond this support requires a separate theorem closing
one of the additional-premise routes named by the angular-kernel
underdetermination boundary, and deriving beta rather than selecting it.

The 2026-07-07 recut preserves that boundary as history while retyping the
live claim: beta = 0.8 is now a named supplied premise, and the fixture algebra
under that premise is the load-bearing content.

### Repair-Pass Disposition (2026-05-10) - PATH B: Tuned Support

The 2026-05-03 REPAIR_TARGETS row #1
(`architecture_note_directional_measure`, critical, bounded_theorem,
repair_class substantive) named two disposition options: (PATH A) derive
beta = 0.8 from first principles, or (PATH B) demote to "tuned support".
The 2026-05-10 rigorization pass selected **PATH B**, on the following
standing evidence:

- beta = 0.8 corresponds to 4/5, but the accepted primitive surface
  (Cl(3) trace structure, action extremization on Z^3, causal-cone kinematics,
  leading-order SO(3) isotropy) carries no five-fold structure and no algebraic
  identity reducing to 4/5. Other candidate algebraic combinations
  (`2 N_c / (N_c^2 - 1)` for `N_c = 2,3,4`, half-integer ratios, and
  Casimir-style ratios) do not produce 4/5 either.
- Gaussian fourth-moment matching against the canonical DAG
  `<theta^2> ~= 0.84 rad^2` would set
  `beta = 1 / (2 <theta^2>) ~= 0.595`, which is not 0.8. This confirms the
  gravity-card beta = 0.8 is not a moment-matched derivation but the route-3
  observable-matched value.
- The angular-kernel underdetermination boundary note
  ([`ANGULAR_KERNEL_UNDERDETERMINATION_NO_GO_NOTE.md`](ANGULAR_KERNEL_UNDERDETERMINATION_NO_GO_NOTE.md),
  PASS=64 in its runner) is cited here only as boundary context. It records
  that, within its stated packet, `w(theta)`, and hence beta if the family is
  restricted to Gaussian, is not uniquely determined by the accepted primitive
  and constraint surface. PATH A therefore remained open unless one of three
  additional-premise routes was supplied (higher-order isotropy,
  action-Lagrangian principle, or structural observable matching); none is
  supplied by this note.

Disposition: this note was carried as **tuned support** for the directional
path measure. The bounded smoke/table claims held at beta = 0.8; the choice of
beta = 0.8 itself was a tuned input. The source boundary was simply that beta
was tuned, not derived.

Future-work derivation target (deferred): close one of the boundary note's three
additional-premise routes, then re-derive beta analytically and file a separate
promotion note. This is not in-scope for the current bounded note.

### Review-Loop Repair (2026-05-03)

The 2026-05-03 review follow-up identified two problems: (a) the empirical
pass/fail table had no runner, no reproduced computation, and no cited graph
dependency; (b) beta = 0.8 was empirically chosen with no derivation. This
repair addressed (a) mechanically and (b) by citing the existing boundary note.

**Mechanical repair (a):**
[runner](../scripts/architecture_directional_measure_table_runner_2026_05_03.py)
recomputes the table from the stated propagator on fixed DAG fixtures
(deterministic seeds) and reproduces the bounded pass/fail rows:

- T1 detector-probability partition fixture consistency on a 2D fixture.
- T2 phase-free two-source visibility fixture consistency on a 2D fixture.
  Its action increment is zero, so it is not a k-variation or
  phase-interference test.
- T3 k = 0 -> real amplitude (no oscillating phase, 3D fixture).
- T4 gravity sign 6/8 attract over fixed seeds; historical note table: 5/8.
- T5 gravity scaling R_angle(N) positive across N = 8..20 with R(20) > R(8),
  matching the canonical gravity-card protocol of `three_d_angle_weight.py`.
- T6 beta-sweep monotonicity: weighted `<theta^2>` decreases monotonically with
  beta on the fixed runner beta list.

**Beta handling (b):**
[`ANGULAR_KERNEL_UNDERDETERMINATION_NO_GO_NOTE.md`](ANGULAR_KERNEL_UNDERDETERMINATION_NO_GO_NOTE.md)
is cited at its stated scope as boundary context. The preserved boundary
statement is that the angular kernel `w(theta)` of the directional path-measure
walk is not uniquely determined by the repo baseline physical Cl(3) local
algebra plus Z^3 spatial substrate together with the named directional-measure
constraints:

1. Cl(3) trace structure.
2. Action extremization on Z^3.
3. Causal-cone kinematics.
4. Leading-order continuum-limit SO(3) isotropy.

Seven distinct kernels were recorded in the history:
`{uniform, cos, cos^2, exp(-0.4 theta^2), exp(-0.8 theta^2),
exp(-1.6 theta^2), linear_falloff}`. They all pass the four structural
constraints but produce measurably different transverse-step moments.

Closing that boundary positively requires one of three additional premises or
closure routes:

1. **Higher-order isotropy:** demand that sub-leading continuum dispersion is
   also rotationally isotropic, constraining the fourth moment of `w`.
2. **Action-Lagrangian principle:** derive or justify the angular weight via a
   continuum Lagrangian whose Euler-Lagrange equations include the angular
   preference.
3. **Direct observable matching:** pin `w` by demanding agreement with a
   specific observable.

The current `BORN_SCATTERING_COMPARISON_NOTE.md` does not select beta for this
note. It imports the fixed `L=15, x_src=5, beta=0.8` envelope from the
directional-measure architecture and does not claim that beta = 0.8 is derived
there.

The current Born note reports that the Gaussian beam-profile test at
beta = 0.8 worsens the eikonal comparison, while a broader beta sweep crosses
the target slope only at much larger beta. It also withdraws the older claim
that beta = 0.8 supplied the needed slope correction.

Therefore the current premise history is only this: beta = 0.8 is supplied by
BETA-DIRECTIONAL; the older selection story is motivation-tier history and is
not consumed by T1-T6. No closed form for beta has been derived.

The empirical `<theta^2>` of the canonical DAG
(xyz_range = 8, connect_radius = 3) is approximately 0.84 rad^2. Gaussian
moment-matching would give `beta = 1 / (2 <theta^2>) ~= 0.595`. This older
comparison remains motivation-tier history only.

After the 2026-05-03 repair the row recorded a runner that recomputes the
table, a cited boundary context that explains why beta is empirical, and a
bounded statement that does not overclaim derivation.

### Conditional Recut (2026-07-07)

The 2026-07-07 recut retypes matched values as supplied premises. The
historical numerical match remains visible in this motivation exhibit, but the
live claim no longer consumes observable matching. Conditional algebra under
BETA-DIRECTIONAL and the deterministic fixture table is now the load-bearing
claim.

This recut does not apply audit verdicts, does not edit audit records, and does
not add primitives or axioms.

### Historical Tested Constraints Table

This table is kept as historical motivation only. The live T4 value is the
runner's 6/8 attract count; the historical table entry 5/8 remains visible.

| test | 2D DAGs | 3D DAGs |
| --- | --- | --- |
| Born rule (I3) | 9.2e-16 PASS | historical table only |
| interference (V) | 0.998 PASS | fixed-DAG smoke PASS (`V = 0.9963`) |
| linearity / normalization smoke | implied by path-sum form | fixed-DAG smoke PASS |
| k = 0 -> zero | 0.000000 PASS | 0.000000 PASS |
| gravity sign | 90%+ attract | historical table: 5/8 attract |
| gravity scaling | R@25 >= R@12 PASS | R increases with N |
| family transfer | r = 2..5 DAGs, neutral on trees | historical table only |
| R_c compat | 8/10 (2 edge cases) | historical table only |
| decoherence scaling | FAIL (purity rises) | historical table only |
| b-dependence | mixed bounded response-density diagnostics | historical table only |

### Historical Interpretation (Motivation Only)

The flat path measure, uniform over all causal paths, was recorded as causing
CLT saturation of gravity. Adding a directional continuation preference was
historically observed to prevent that saturation while preserving interference,
Born rule behavior, and k = 0 -> 0 on the tested fixtures.

The directional weight also has a 3D generalization as `acos(dx / L)` without
modification. The fixed-DAG smoke test says this is not just gravity-side
support: the same 3D rule shows a real zero-field interference pattern and
preserves source-superposition linearity to machine precision.

The role recorded after the topology pivot was:

- this directional measure is the accepted unitary support layer;
- it is not, by itself, the decoherence solution;
- it is the unitary core used in later modular / gap-controlled DAG results
  where both gravity and decoherence work on the same family.

Those historical interpretations are not part of the 2026-07-07 load-bearing
claim unless separately audited.

## Unconditional Boundary

The angular-kernel underdetermination boundary note is kept prominent as
boundary context and is cited at its stated scope, not as promotion authority.

At its stated scope, the angular-kernel boundary note states that the angular kernel
`w(theta)` of the directional path-measure walk is not uniquely determined by
the accepted primitive and constraint surface.

For this note, that boundary means beta = 0.8 cannot be described here as
derived, natural, uniquely selected, or primitive-surface forced. The boundary
does not itself derive the supplied premise; it only blocks converting the
historical match into a derivation inside this note.

## Residuals / Open Derivation Targets

- Decoherence scaling is not addressed. The directional weight modifies the
  unitary propagator, while decoherence is a non-unitary record/environment
  problem.
- The 3D support is still a smoke package, not a full 3D Sorkin or three-slit
  theorem.
- The raw b-dependence, meaning deflection/readout increasing with impact
  parameter, is not fixed by this note. The old response-density hierarchy,
  finite-source correction, occupancy bridge, 4-NN and 3-NN stencil diagnostics,
  and residual probes remain motivation only. No sampler-robust residual
  closure has landed.
- beta = 0.8 is supplied, not derived. Closing this requires one of the
  boundary note's three additional-premise routes: higher-order isotropy,
  action-Lagrangian principle, or direct observable matching at the structural
  level.
- The future-work derivation target remains: close a boundary route, derive beta,
  and file a separate promotion note. This note is not that promotion note.
- The 2 R_c edge cases mean the weight slightly narrows the zero-field
  interference threshold at some geometries.
- Transfer of the joint gravity-plus-decoherence story to dynamically generated
  or higher-dimensional graph families remains future work.

Historical pre-2026 axiom-language connections remain motivation only:

- Legacy "continuation prefers local coherence" phrasing: the weight implements
  this motivation.
- Legacy "space inferred" phrasing: the angle is intrinsic to the graph, not
  imposed.
- This is a path-measure correction, not a new dynamical law.

## Citation Contract (Audit-Gated)

- Cite this note, before audit review, only as a supplied-value conditional
  fixed-fixture theorem candidate.
- The runner may be cited for deterministic recomputation of T1-T6 under
  BETA-DIRECTIONAL.
- The motivation exhibit may be cited only as evidence/history. It may not be
  cited as load-bearing derivation, selection, or observable match content for
  the live claim.
- `BORN_SCATTERING_COMPARISON_NOTE.md` remains a backticked see-also reference
  documenting the bounded eikonal comparison and the withdrawn beta-correction
  claim. It is not a load-bearing authority here.
- The angular-kernel underdetermination boundary note may be cited only at its
  stated scope as boundary context. This note does not upgrade or apply its
  audit verdict.

## Firewall

- This note may be cited only for the bounded smoke/table checks at the fixed
  supplied point beta = 0.8.
- It may not be cited as a derivation of the directional-measure kernel, the
  angular weight, the beta parameter, or a framework gravity law.
- The named premises may not be cited as derived.
- beta = 0.8 may not be described as derived, selected by first principles,
  natural, unique, or accepted.
- Observable matching is quarantined inside BETA-DIRECTIONAL as selection
  history, not as claim content.
- No closed form for beta has been derived.
- Promotion beyond supplied-value conditional support requires a separate
  theorem closing one of the boundary routes and deriving beta rather than
  selecting it.
- This note does not establish decoherence scaling, a full 3D Sorkin theorem,
  a fixed raw b-dependence law, or a new dynamical law.

## Verification

The runner is deterministic and offline. It keeps load-bearing fixture checks
separate from motivation-tier replay/provenance text, checks for the named
premise and motivation-exhibit labels in this note, and prints a final
`FATAL TOTAL: PASS=N FAIL=0` banner on success. The 2026-07-07 local run
printed:

```text
LOAD-BEARING: PASS=6 FAIL=0
MOTIVATION: PASS=6 FAIL=0
FATAL TOTAL: PASS=6 FAIL=0
ALL CHECKS: PASS=12 FAIL=0
```

Expected load-bearing fixture checks:

- T1 detector-probability partition fixture consistency.
- T2 phase-free two-source visibility fixture consistency.
- T3 k = 0 real amplitude.
- T4 gravity sign count.
- T5 gravity scaling.
- T6 beta-sweep monotonicity.

The final runner declaration must name BETA-DIRECTIONAL as supplied and state
that beta derivation, beta selection, and observable matching are not claimed.
