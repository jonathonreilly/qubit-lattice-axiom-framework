# AC_phi_lambda Registrable Cycle-Holonomy Normal Form

**Current authority (2026-07-11):** older admission labels below are historical
provenance only. The physical R-eta readout remains an `open_gate`; this note's
normal-form algebra does not supply it.
**Date:** 2026-07-01
**Claim type:** bounded_theorem
**Scope:** registrable normal form plus selector re-coordination.
**Status authority:** independent audit lane only. This note does not set an audit verdict, edit registries, register primitives, change axioms, or claim `AC_phi_lambda` retirement.
**Primary runner:** [`scripts/acphilambda_registrable_cycle_holonomy_normal_form_2026_07_01.py`](../scripts/acphilambda_registrable_cycle_holonomy_normal_form_2026_07_01.py)
## Claim
On the retained C3 generation frame, the Brannen form is
```text
H(a, |b|, delta) = a I + b C + conj(b) C^T,
b = |b| exp(i delta),
lambda_k = a + 2 |b| cos(delta + 2 pi k/3).
```
The unordered eigenvalue multiset determines and is determined by
`(a, |b|, cos(3 delta))` for `|b| >= 0`.
The registrable phase content is therefore not a chosen sign of `delta`.
At registrable resolution, the registrable phase content of the Brannen dial is exactly `cos(3 delta)`, the conjugacy class of the generation-cycle holonomy `Phi = 3 delta`.
The directed edge-coefficient product around the generation 3-cycle is
```text
b^3 = |b|^3 exp(i 3 delta),
Phi = arg(b^3) = 3 delta mod 2 pi.
```
For equal-modulus hopping data, diagonal unitary gauge changes move all
edge phases into one symmetric representative, with the orientation convention
stated below. This classifies hopping-phase data by the cycle sum `Phi`.
The identity-unit transport re-coordinates the current junction as
```text
S_sum = sum_{j=1,2} 1 / ((omega^j - 1)(omega^(2j) - 1)) = 2/3,
L3(1,2) = S_sum / 3 = 2/9,
delta(c) = c L3,
Phi(c) = 3 c L3 = c S_sum.
```
Thus `c = 1` iff `Phi = S_sum = 2/3`.
The wall is now recorded in gauge-invariant coordinates:
```text
W_cycle_holonomy_value:
  the generation-cycle holonomy of the physical charged-lepton readout equals
  the unaveraged C3 fixed-point sum: Phi = 2/3.
```
## Retained Inputs
| row | quoted retained fragment used here |
|---|---|
| [BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15](BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md) | "On the supplied C3[111] generation 3-space, a local Hermitian generator commuting with the [111] 3-fold rotation `C`, namely `[H,C]=0`, has the circulant form `H = a I + b C + conj(b) C^T`. This is the Brannen form. It has exactly three real couplings, written as `(a, |b|, delta)`." |
| [KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) | "`x_k := v_0 (1 + sqrt(2) cos(delta + 2 pi k / 3))`", `k = 0, 1, 2`; the note scopes this as a standalone trigonometric / algebraic identity and not a physical readout theorem. |
| [KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md) | "forced transverse weights `(1,2)`, and local density `2/9`"; the note also states that it does not supply the physical single-summand readout. |
| [KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md) | Type-A periodic phase sources land in `q*pi`, Type-B combinatorial rationals remain a separate rational-to-radian identification, and the sharpened residual is the period-`1 rad` versus canonical period-`2 pi rad` convention choice. |
Non-linked context, with no dependency edge (in-flight PRs; audit status set
only by the independent audit lane):
- PR #4783, `ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01`: the identity-unit wall is not derivable from rescale-invariant clauses and is not an angular convention.
- PR #4760 `ACPHILAMBDA_PHASE_DEFECT_READOUT_NORMAL_FORM_2026-07-01` (wall `W_defect_readout_selection`), PR #4771 `ACPHILAMBDA_C3_COVARIANT_READOUT_UNIT_NORMAL_FORM_2026-07-01` (normal form `I_c(R) = c |R| L` and wall `W_defect_identity_unit`), PR #4762 `PHYSICAL_READOUT_SELECTION_INDEPENDENCE_2026-07-01` (finite selection-independence witness): cited as in-flight context only; the needed normal form is restated self-contained below.
## Finite Theorem (T-A1)
Let
```text
c_k = cos(delta + 2 pi k/3),  k = 0,1,2.
```
The finite trigonometric identities are
```text
sum_k c_k = 0,
sum_k c_k^2 = 3/2,
sum_k c_k^3 = (3/4) cos(3 delta).
```
For `lambda_k = a + 2 |b| c_k`, the first elementary symmetric datum fixes
`a`, the centered second power sum fixes `|b|`, and the centered third power
sum fixes `cos(3 delta)`.
No comparison target is inserted: the runner derives these by exact symbolic
simplification.
Conversely, the multiset is invariant under `delta -> delta + 2 pi/3`, which
relabels `k`, and under `delta -> -delta`, which relabels `k -> -k`.
On the strip `3 delta in [0, pi]`, equivalently `delta in [0, pi/3]`,
`cos(3 delta)` is strictly monotone.
The unordered spectrum therefore re-derives the registrable sign strip and
the `2 pi/3` relabels from spectrum alone.
## Holonomy Identity And Symmetric Representative (T-A2)
The directed cycle product is
```text
prod_cycle b = b^3,
arg(prod_cycle b) = 3 delta = Phi mod 2 pi.
```
Since the retained cyclic shift has `det C = 1`, the same identity appears as
```text
det(b C) = b^3,
arg det(b C) = 3 delta.
```
For equal-modulus hopping data
```text
H' = |b| (exp(i theta_1) E_12 + exp(i theta_2) E_23
          + exp(i theta_3) E_31) + h.c.,
Phi = theta_1 + theta_2 + theta_3,
mu = Phi/3,
```
choose a diagonal unitary `D = diag(exp(i phi_1), exp(i phi_2), exp(i phi_3))`
with
```text
phi_2 = phi_1 + theta_1 - mu,
phi_3 = phi_2 + theta_2 - mu,
phi_1 = phi_3 + theta_3 - mu  mod 2 pi.
```
The cycle condition holds because the sum of the three increments is zero.
Then `D H' D^dagger` has the common directed-edge phase `mu`.
Orientation convention: with `E_jk = |j><k|` and the T-A1 shift
`C|k> = |k+1 mod 3>`, the displayed `E_12,E_23,E_31` edge orientation is the
`C^T` orientation. The symmetric edge representative therefore has phase
`+Phi/3` on those directed edges, equivalently `H(0, |b|, -Phi/3)` in the T-A1
`C` convention. Reversing the named cycle orientation writes the same
conjugacy class as `+Phi/3` in the usual cosine argument.
Pointer caveat: diagonal conjugations generically do not fix the einselected
pointer `S = C + C^2`. T-A1 needs no conjugation; it is direct multiset algebra
on the fixed-`S` retained frame. T-A2(ii) classifies hopping-phase data, and
the pointer-compatible relabels are exactly the `2 pi/3` fundamental-domain
shifts.
## Identity-Unit Transport (T-B)
Let `omega = exp(2 pi i/3)`. The exact finite sum is
```text
S_sum := sum_{j=1,2} 1 / ((omega^j - 1)(omega^(2j) - 1)) = 2/3.
```
The local density is the group average
```text
L3(1,2) = S_sum / 3 = 2/9.
```
Under the in-flight c-parameterized readout family, restated here
self-contained,
```text
delta(c) = c L3,
Phi(c) = 3 delta(c) = 3 c L3 = c S_sum.
```
Therefore
```text
c = 1  <=>  Phi = S_sum = 2/3.
```
The group-average factor `1/3` in the density is identified with the per-edge
distribution factor `1/3` of the cycle holonomy in the circulant
representative. Both are the same C3 order acting on the same object. Under
the no-coincidences discipline, this converts two appearances of `1/3` into
one derived structural factor.
```text
W_cycle_holonomy_value:
  the generation-cycle holonomy of the physical charged-lepton readout equals
  the unaveraged C3 fixed-point sum: Phi = 2/3.
```
This re-coordination does not derive `Phi = 2/3`: the self-contained rescale
witness is `Phi(lambda c) = lambda Phi(c)`, so homogeneous clauses still cannot
pin the unit on holonomy coordinates.
What changes is the coordinate surface: the wall now sits on the canonical
gauge-invariant holonomy conjugacy class `cos Phi`, a per-cycle accumulated
transport phase. The retained radian-bridge Type-A list covers periodic and
finite-order phase quanta of the form `q*pi`; a cycle-accumulated hopping phase
is an `R`-valued transport coordinate.
## What This Moves
| before | after |
|---|---|
| density `2/9` read as angle `delta` | holonomy `Phi` equals unaveraged sum `2/3` |
| unexplained `1/3` inside the density | `1/3` is the per-edge distribution of the same C3 cycle |
| target was a gauge representative | target is the invariant holonomy conjugacy class |
| angle-native route had a diffuse unit wall | strike point is `W_cycle_holonomy_value` |
## What Does Not Move
- No derivation is supplied for `Phi = 2/3`.
- No derivation is supplied for `c`, `r`, occurrence, Born weighting, theta, source/action, or species labels.
- The type junction from number to angle persists.
- The standing missing selector is relocated to invariant coordinates, not removed.
- The physical charged-lepton readout is still outside the fixed-locus arithmetic row.
## Cross-Lane Observation (context only)
Observation, not a derivation; no dependency is created. The theta mass-side
admission also lives on an `arg det` surface: the Tier-A registry entry
`strong_cp_theta_zero_note` (label `theta`, `docs/audit/data/premise_decision_history.json`)
reads "the discrete orientation arg det M in {0, pi} -> 0 on the K-real
reading", while PR #4783 and this note place the charged-lepton unit wall on
`arg det(b C)`. Both Tier-A admissions are therefore arg-det-phase selections.
This is observation, not a derivation, and it does not create a dependency edge.
## Audit Consequence If Retained
Rows needing `|delta| = 2/9` may cite the sharpened shape conditionally:
```text
selected C3 defect line
+ W_cycle_holonomy_value
=> |delta| = 2/9.
```
The wall `W_cycle_holonomy_value`, `W_defect_identity_unit`, and R-eta
sub-admission (ii) "density-read-as-angle" are one dependency in three
coordinate systems, not separate walls.
## Non-Claims
- This does not claim `Phi = 2/9`; the holonomy value is `Phi = 2/3`, while the representative phase is `delta = 2/9`.
- This does not claim the holonomy equation is derived.
- This does not claim the radian-bridge no-go is evaded; the Type-B-to-radian identification persists as the value equation on the invariant.
- This does not claim theta linkage is a derivation.
- No new unit convention is adopted.
- No axiom change, registry change, primitive registration, or audit-status edit is made.
## No-Go Discipline Gate
This checklist supports a bounded normal form plus re-coordination; it is not a
terminal no-go.
### N1
| route | disposition |
|---|---|
| spectrum / registrable route | ATTEMPTED here; succeeds as a normal form for `cos(3 delta)` |
| gauge-representative readout route | SUPERSEDED: target the invariant holonomy class |
| radian / Type-A periodic route | RULED OUT BY RETAINED radian row: retained periodic sources give `q*pi`, while nonzero rationals are not literal radians from those sources |
| rescale-invariant derivation of `Phi` | RULED OUT HERE by the self-contained rescale witness: homogeneous clauses cannot pin the unit |
| per-cycle accumulated transport phase route | OPEN: the named strike point is `W_cycle_holonomy_value` |
| owner primitive | GOVERNANCE |
### N2
The collapsed wall set is one wall:
```text
W_cycle_holonomy_value == W_defect_identity_unit == R-eta junction coefficient.
```
### N3
| item | hidden-wall scan |
|---|---|
| `generation-cycle holonomy` | defined by the directed edge-phase product on the retained circulant form; not a new physical import |
| `unaveraged fixed-point sum` | finite C3 arithmetic |
| `equal-modulus hopping class` | scope restriction of T-A2(ii) |
| `pointer caveat` | stated explicitly |
| `physical readout` | the standing missing selector |
### N4
Residual matching: against the radian row, this is the same Type-B-to-radian
residual now placed on the invariant. Against the non-linked #4783 context, it
is the same unit wall re-coordinated. Against #4760/#4771, it is the same
selector. Against the fixed-locus row, the arithmetic is supplied while readout
remains excluded.
### N5
The proven sentences are the finite spectrum algebra, the holonomy identity,
and the equivalence `c=1 <=> Phi=2/3`. The runner tests these at finite 3x3
symbolic resolution and makes no claim about deriving the value equation.
### N6
Live paths: derive `Phi` from a per-cycle accumulated transport or step theorem
on the selected defect; derive a rescale-breaking record-facing clause; or make
an owner primitive decision. The first path must output the holonomy value on
the selected C3 defect, the second must explain the unit in record-facing
coordinates, and the third must be explicit governance.
### N7
A hostile reviewer can say this is a change of variables dressed as progress.
Reply: the derived `1/3`, invariant targeting, and strike-point sharpening are
the audit content. Concede that the value equation itself is untouched.
### N8
Representative-versus-invariant confusions recur: the `delta` sign strip,
det-character surfaces, and theta arg-det admissions all show the same pattern.
The uniform lesson is to register invariants first, then derive their values.
## Verification
Run:
```bash
python3 scripts/acphilambda_registrable_cycle_holonomy_normal_form_2026_07_01.py
```
Expected final line:
```text
TOTAL: PASS=100 FAIL=0
```
