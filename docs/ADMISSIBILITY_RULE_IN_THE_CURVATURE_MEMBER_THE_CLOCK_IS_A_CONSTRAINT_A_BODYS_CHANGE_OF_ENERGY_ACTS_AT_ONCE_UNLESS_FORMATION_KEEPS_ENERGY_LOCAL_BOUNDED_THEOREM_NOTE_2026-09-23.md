---
claim_id: admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_a_bodys_change_of_energy_acts_at_once_unless_formation_keeps_energy_local_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For an explicit nonzero-mode quadratic action: scalar constraint, two TT frequencies, clock elimination away from a singular kinetic ratio and scoped source-ramp identities."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
  - admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
  - admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_2026_09_23.py
---

# A constrained quadratic clock mode and its source derivatives

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
Supply real symmetric h, scalar u, K>0, wbar>0, alpha>0, beta real, and nonzero real vector p. In a lattice-symbol application p_j=2sin(k_j/2). Define
R1=p²tr h-p.h.p,
R2=-(p²/4)tr(h²)+(hp).(hp)/2-(p.h.p)tr h/2+p²(tr h)²/4.
The action is L=[alpha tr(hdot²)+beta(tr hdot)²]/wbar+K wbar(u R1+R2)-e(t)u.
This is a supplied quadratic mode model with no time derivative ofu and no strain-stress source. Algebraically aligning p withz is a choice of basis, not an exact cubic-lattice spatial rotation.

## Theorem T1 — spatial invariance
R1 andR2 are unchanged by h to h+p xi^T+xi p^T. On h=(I-pp^T/p²)phi they are2p²phi andp²phi²/2. For h=2lambda I, the u equation gives p²lambda=e/(4K wbar).
The spatial-potential invariance is not a gauge invariance of the full kinetic action under arbitrary time-dependent xi.

## Theorem T2 — mode equations
Write h=[[phi+a,b,cx],[b,phi-a,cy],[cx,cy,2xiL]] with p alongz. Variation gives
2K wbar p²phi=e,
(4alpha/wbar)a''=-K wbar p²a, and likewise forb,
d/dt[(alpha+beta)xiL'+beta phi']=0.
Thus two TT modes have frequency squared K wbar²p²/(4alpha). Other longitudinal/vector sectors may have zero-frequency/free motion; they are not absent degrees of freedom.
The p=0 multiplier instead requires e0=0. A torus with net source needs a separately declared background or zero-mode treatment.

## Theorem T3 — elimination and its singular case
For alpha+beta!=0, substitute phi=e/(2K wbar p²) and xiL''=-beta phi''/(alpha+beta) in thephi equation:
u=-e/(4K wbar p²)+alpha(alpha+3beta)e''/[K²wbar³(alpha+beta)p⁴].
The conserved integration constant in xiL' drops out. At beta=-alpha/3 the derivative term vanishes.
At beta=-alpha the divided formula is inapplicable; the longitudinal equation instead forces e''=0. Rest initial data force its slope tozero in this zero-stress model. These facts do not determine which physical formation processes are allowed.

## Theorem T4 — a specified ramp
Inside0<t<tau take e=Delta_e[3(t/tau)²-2(t/tau)³], with constants outside. This glued ramp is C1, not C2. For alpha+beta!=0 the right-limit clock contribution at0 is6alpha(alpha+3beta)Delta_e/[K²wbar³(alpha+beta)p⁴tau²]. It can vanish. A smoother ramp with zero initial second derivative has no such jump.
After the ramp the derivative term vanishes and the static term remains, for the nonsingular coefficient range. This mode calculation does not prove that every packet or every spatial clock changes immediately. No retarded matter theory, arrival time, infinite-volume inverse-square-kernel asymptotic or sufficiency of local energy conservation is established.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Nonzero momentum, mean-source compatibility and nonsingular coefficient domains matter. A constraint formula is not by itself a physical causality theorem.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
The operators, domains, boundary conditions and state assumptions stated above are explicit mathematical hypotheses. They do not add a framework axiom or primitive.

### N4 — Dependencies
The dependencies below identify the actual supplied inputs; earlier stronger conclusions are not imported.

### N5 — Resolution
The canonical runner checks the finite examples and identities stated above using exact arithmetic. General conclusions require the displayed arguments, not extrapolation from samples. Historical simulations are deferred.

### N6 — Primitive boundary
No new primitive, species selection, filling rule or physical interpretation is adopted.

### N7 — Strongest objection
Nonzero momentum, mean-source compatibility and nonsingular coefficient domains matter. A constraint formula is not by itself a physical causality theorem.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8590; no premise adoption or retained grade is inferred.
- [admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8592; no premise adoption or retained grade is inferred.
- [admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8571; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8895 head `a0cf3d4a41ef8443bfe161012e3c178e80151807`, branch `physics-loop/admissibility-induced-law-block101-the-clock-is-a-constraint-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
