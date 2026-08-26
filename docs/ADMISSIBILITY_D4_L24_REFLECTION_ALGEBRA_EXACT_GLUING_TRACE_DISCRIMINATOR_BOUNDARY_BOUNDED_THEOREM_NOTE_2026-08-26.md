---
claim_id: admissibility_d4_l24_reflection_algebra_exact_gluing_trace_discriminator_boundary_bounded_theorem_note_2026-08-26
claim_type: bounded_theorem
claim_scope: "For the preregistered D1 squared-radius-zero sector of the literal Block-192 two-component L24 action, exact two-half Berezin re-gluing gives the scalar identities det(M_periodic)=-2^-24 det(I-T^24)=2^-24 r^-1(1-r)^2 and det(M_AP)=2^-24 det(I+T^24)=2^-24 r^-1(1+r)^2, where r=((sqrt(53)-2)/7)^24 lies strictly between zero and one. With the frozen CAR order this selects a two-mode graded trace for the periodic carrier and an ordinary trace for the changed antiperiodic control. The normalized periodic weights on vacuum, the two one-particle sectors, and the pair sector are proportional to (1,-r,-r,r^2); hence the positive odd-parity projector, which belongs to the even CAR algebra, has value -2r/(1-r)^2<0. The two global reflection signs are inequivalent on full CAR and identical on even exterior degree, but neither changes the exact seam trace. Exhaustion of the registered 2x2x2 sign/algebra/trace tournament leaves zero cells simultaneously reflection-positive, exact-periodic-gluing, normalized, and state-positive. This is a partial narrowing of that literal periodic D1 tournament, not a no-go for antiperiodic, open/infinite-time, action-selected sector, alternative Record operator-system, cyclic, CAR/Nambu, process, gravity, axiom, or TOE routes."
parents:
  - admissibility_d4_l12_open_time_stable_os_event_boundary_bounded_theorem_note_2026-08-26
upstream_dependencies:
  - minimal_axioms
actual_current_surface_status: demotion
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
reachability_to_target: rejects_the_literal_periodic_full_or_even_car_probability_carrier_and_localizes_a_spin_sector_or_record_algebra_choice
artifact_role: theorem
conditional_surface_status: partial-narrowing
hypothetical_axiom_status: unchanged
admitted_observation_status: none
target_claim_id: admissibility_d4_l24_reflection_algebra_exact_gluing_trace_discriminator_2026-08-26
target_blocker_text: "Exact periodic re-gluing selects a normalized graded functional that is negative on the even odd-parity projector; the positive ordinary functional exactly belongs to the changed antiperiodic carrier."
next_trace_action: "Test the shortest action-faithful alternative: an exact unital descent of the periodic functional to the fixed Block-194 Record operator system, with an action-derived sector selector if the odd-parity projector is absent; otherwise compare an explicit antiperiodic carrier update against the frozen matter-mode obligations."
claim_type_reason: "Finite determinants, two-half Schur identities, transfer recurrence, reflection-sign classification, complete two-mode projector values, and all eight tournament cells are exact. Standing is demoted because smaller Record operator systems, action-selected sectors, changed spin structures, open/infinite time, cyclic/process, and gravity routes remain live."
audit_required_before_effective_retained: true
bare_retained_allowed: false
preregistration_commit: b09855d0ec
primary_checks_passed: 8
primary_mutations_rejected: 27
independent_checks_passed: 8
independent_mutations_rejected: 14
first_fixture: D1
first_squared_radius: 0
temporal_length: 24
full_action_dimension: 48
tournament_cells: 8
compatible_periodic_cells: 0
periodic_trace_type: graded
antiperiodic_control_trace_type: ordinary
graded_odd_parity_projector_sign: negative
full_car_reflection_sign_relation: inequivalent
even_exterior_reflection_sign_relation: identical
event_stage: sealed
strong_history_positivity: not_tested
causal_process: sealed
no_go_discipline_gate: PASS_for_exact_registered_periodic_D1_tournament_FAIL_for_broad_probability_spin_sector_or_TOE_no_go
negative_disposition: partial-narrowing
minimal_axiom_update: none
obligation_retirement: 0
toe_percentage_movement: 0
---

# Exact Reflection/Algebra/Gluing Trace Discriminator

**Date:** 2026-08-26

**Campaign block:** 203

**Type:** bounded theorem

**Standing:** proposed bounded theorem; independent audit unset

Primary runner:
[admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.py](../scripts/admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.py).

Independent no-import checker:
[independent_admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.py](../scripts/independent_admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.py).

SHA/input-bound cached stdout:
[primary](../logs/runner-cache/admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.txt)
and
[independent](../logs/runner-cache/independent_admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.txt).

## 1. Result Up Front

Block 203 resolves the sign/algebra/gluing choice for the registered first
target, and it does not produce a positive periodic Record state.

For the exact D1 squared-radius-zero action, the periodic seam selects a
graded two-mode trace.  The antiperiodic seam selects the ordinary trace.  The
normalized periodic functional has occupation-sector weights

\[
 (P_{00},P_{10},P_{01},P_{11})
 \longmapsto
 \frac{(1,-r,-r,r^2)}{(1-r)^2},
 \qquad
 r=\left(\frac{\sqrt{53}-2}{7}\right)^{24},
 \quad 0<r<1.
\]

The central odd-parity projector

\[
 P_{\rm odd}=P_{10}+P_{01}
\]

is a positive operator in the fermion-even CAR algebra, but

\[
 \omega_{\rm periodic}(P_{\rm odd})
 =-\frac{2r}{(1-r)^2}<0. \tag{1}
\]

Thus restricting the *words* to even fermion parity does not make the
periodic graded functional positive.  The opposite global reflection sign
repairs the open one-particle form, but it cannot change the temporal seam or
equation (1).  The positive ordinary functional belongs exactly to the
changed antiperiodic carrier.

All eight preregistered cells have therefore been exhausted.  None is at once
reflection-positive on its declared algebra, exactly re-gluing to the
periodic action, normalized, and positive as a state.

This is real route progress but not TOE closure.  It makes a physical choice
explicit: the literal periodic `L24` object can remain a spectral/graded
bookkeeping carrier, or the theory must derive a smaller Record operator
system/sector selection, rebuild the temporal spin structure, or obtain the
state from open/infinite time.  None of those choices is made here.

There is no axiom edit, no retired obligation, and no TOE percentage movement.

## 2. Frozen Object And Exact Two-Half Gluing

Let

\[
 A_b=I_{24}\otimes mI_2+D_b\otimes\sigma_z,
 \qquad m=\frac27,
 \qquad \sigma_z={\rm diag}(1,-1), \tag{2}
\]

where `D_b` is the centered temporal difference with boundary multiplier
`b=+1` for periodic time and `b=-1` for the AP control.  The evidentiary cut is

\[
 0,\ldots,11\mid12,\ldots,23. \tag{3}
\]

Writing the full matrix in two-half blocks,

\[
 A_b=\begin{pmatrix}H_L&B_b\\C_b&H_R\end{pmatrix},
\]

both oriented seam blocks have exact rank four.  Direct exact elimination
gives

\[
 \det A_b=\det H_L\,
 \det\!\left(H_R-C_bH_L^{-1}B_b\right). \tag{4}
\]

The runner checks (4) against the direct `48 x 48` determinant for both seam
choices.  It also permutes the two internal components and verifies

\[
 \det A_b=\det(mI_{24}+D_b)^2. \tag{5}
\]

No scalar determinant substitutes for (4); equation (5) is a separately
checked factorization of the already reconstructed full action.

## 3. The Seam Selects The Trace Type

The temporal recurrence for one component is generated by

\[
 T=\begin{pmatrix}2m&1\\1&0\end{pmatrix}. \tag{6}
\]

At even length 24, `det(T^24)=1`.  If

\[
 q=\frac{\sqrt{53}-2}{7},\qquad r=q^{24}, \tag{7}
\]

then the two eigenvalues of `T^24` are `r` and `r^{-1}`.  Direct finite
determinants and the transfer recurrence agree exactly:

\[
\begin{aligned}
 \det(mI+D_{\rm P})
 &=-2^{-24}\det(I-T^{24})
  =2^{-24}r^{-1}(1-r)^2\\
 &=\frac{648686052261462293325}
 {12555467579756800534183936}, \tag{8}\\
 \det(mI+D_{\rm AP})
 &=+2^{-24}\det(I+T^{24})
  =2^{-24}r^{-1}(1+r)^2\\
 &=\frac{41707488576114153187201}
 {803549925104435234187771904}. \tag{9}
\end{aligned}
\]

With the preregistered CAR order, second quantization of the stable transfer
mode gives

\[
 \operatorname{Tr}\Gamma(r)^{\otimes2}=(1+r)^2,
 \qquad
 \operatorname{Tr}\left((-1)^N\Gamma(r)^{\otimes2}\right)=(1-r)^2.
 \tag{10}
\]

The positive zero-point factors are fixed by (8)--(9), rather than fitted:

\[
 Z_{{\rm vac},P}=2^{-24}(r^{-1}-1)>0,
 \qquad
 Z_{{\rm vac},AP}=2^{-24}(r^{-1}+1)>0. \tag{11}
\]

Equations (8)--(11) select the graded trace for the literal periodic seam and
the ordinary trace for the changed AP seam.  Swapping those labels breaks the
exact finite determinant identity.

## 4. Reflection Sign Versus Observable Algebra

Block 202's open-half form is reconstructed rather than merely cited.  For
the frozen reflection sign,

\[
 K_-=E_+^T\Theta_-A_{\rm open}^{-1}E_+,
 \qquad {\rm inertia}(K_-)=(0,22,2), \tag{12}
\]

and for the opposite global sign,

\[
 K_+=-K_-,
 \qquad {\rm inertia}(K_+)=(2,22,0). \tag{13}
\]

Both reflections obey action covariance.  They are inequivalent on a full
CAR algebra containing degree-one fields.  On exterior degree `q`, however,

\[
 \bigwedge{}^q K_-=(-1)^q\bigwedge{}^qK_+. \tag{14}
\]

Because `rank(K_+)=2`, the nonzero even lift consists only of degrees zero and
two.  The two signs therefore induce the same even-exterior form.  This
collapses the sign tournament on the even algebra, as the panel required.

The important point is that changing `Theta` does not change `A_b`, its seam,
or equations (8)--(10).  Reflection positivity can reject a sign, but it
cannot turn a periodic graded trace into an ordinary one.

## 5. Complete Projector Positivity Test

In the ordered two-mode occupation basis

\[
 |00\rangle,|10\rangle,|01\rangle,|11\rangle,
\]

the two normalized functionals are:

| positive projector | parity | AP ordinary value | periodic graded value |
|---|---:|---:|---:|
| `P00` | even | `1/(1+r)^2` | `1/(1-r)^2` |
| `P10` | odd state / even operator | `r/(1+r)^2` | `-r/(1-r)^2` |
| `P01` | odd state / even operator | `r/(1+r)^2` | `-r/(1-r)^2` |
| `P11` | even | `r^2/(1+r)^2` | `r^2/(1-r)^2` |
| `Podd=P10+P01` | central even operator | `2r/(1+r)^2` | `-2r/(1-r)^2` |
| `Peven=P00+P11` | central even operator | `(1+r^2)/(1+r)^2` | `(1+r^2)/(1-r)^2` |

Every ordinary weight is strictly positive and their sum is one.  The graded
weights also sum to one, but the two one-particle projectors and their central
sum have strictly negative values.  Hence:

- determinant positivity is not state positivity;
- global even-word sign cancellation is not positivity on the even CAR
  algebra; and
- selecting only the even state sector would change the functional from the
  exact periodic graded trace.

A fixed-even-sector state proportional to `(1,0,0,r^2)` is positive, but its
partition factor is `1+r^2`, not `(1-r)^2`.  It is therefore a live new
sector-selection route, not a passing tournament cell.

## 6. Exhaustive Tournament

The table abbreviates reflection positivity as `RP`, exact periodic re-gluing
as `glue`, and positivity of the normalized functional on the declared
algebra as `state`.

| reflection | algebra | trace | RP | glue | state | compatible |
|---|---|---|---:|---:|---:|---:|
| frozen | full CAR | ordinary | no | no | yes | no |
| frozen | full CAR | graded | no | yes | no | no |
| opposite | full CAR | ordinary | yes | no | yes | no |
| opposite | full CAR | graded | yes | yes | no | no |
| frozen | even CAR | ordinary | yes | no | yes | no |
| frozen | even CAR | graded | yes | yes | no | no |
| opposite | even CAR | ordinary | yes | no | yes | no |
| opposite | even CAR | graded | yes | yes | no | no |

There are exactly zero compatible cells.  This is not an underdetermined
choice between several positive conventions; it is an incompatibility between
same-action periodic gluing and state positivity on both registered algebras.

The AP control is deliberately outside the table.  It has exact ordinary
gluing and a positive two-mode state, but it changes the temporal carrier and
must separately satisfy the frozen matter-mode and reflection obligations.

## 7. What This Does And Does Not Decide

This block decides that the literal periodic `L24` D1 zero-radius functional
is not a normalized positive state on either the declared full CAR algebra or
its full fermion-even subalgebra.  It also decides that a global reflection
sign cannot repair that mismatch.

It does not decide:

- whether the Block-194 commutative Record operator system excludes the
  offending parity projector and admits a faithful unital positive descent;
- whether a Gauss law or an action-derived superselection rule uniquely fixes
  an even state sector;
- whether the physical carrier should be antiperiodic rather than periodic;
- whether open/infinite time supplies the physical state while `L24` is only a
  spectral regulator;
- whether a cyclic insertion, alternative two-slice algebra, CAR/Nambu lift,
  or process functional closes histories;
- formation/permanence dynamics, Born forcing, gravity, or the TOE.

No minimal-axiom edit follows yet.  The unresolved choice is downstream
physics: carrier/spin structure, sector selection, or observable/event
algebra.  A successful explicit construction can still retire that import.

## 8. No-Go Discipline Gate

### N1 -- normalized alternative-route enumeration

The broad claim that the action cannot support probabilities is rejected.
The exact claim is only exhaustion of the registered periodic D1 tournament.

| family | object / mechanism / terminal obligation | honest result |
|---|---|---|
| opposite reflection on full CAR | change the graded anti-automorphism sign / repair open odd-field RP / retain exact periodic state | `ATTEMPTED`: (13) repairs RP, but (1) is unchanged and negative |
| fermion-even CAR | restrict the algebra / cancel global exterior signs / require positivity on every even positive operator | `ATTEMPTED`: signs coincide, but `Podd` is even and has the negative value (1) |
| ordinary same-action trace | use a positive thermal density / require the literal periodic two-half determinant | `ATTEMPTED`: all weights are positive, but (8)--(10) show ordinary trace matches AP, not periodic time |
| fixed-even sector | compress to even states / remove the negative odd block / reproduce the complete periodic functional | `ATTEMPTED`: the positive factor `1+r^2` does not equal the exact graded factor `(1-r)^2`; an extra sector law is required |
| AP spin rebuild | change the seam / obtain the ordinary positive functional / re-satisfy matter and reflection obligations | `ATTEMPTED` as a control: (9) succeeds, but it is a different carrier and therefore cannot certify the literal periodic target |
| determinant-only probability | use positive `det A_P` / treat the partition number as a state / require positive effects | `ATTEMPTED`: (8) is positive while the explicit positive projector (1) is negative |

These are distinct in primary object, mechanism, or terminal obligation.  The
first six attacks suffice to stress the narrow tournament claim.  Alternative
Record operator systems, open/infinite time, cyclic/process constructions,
CAR/Nambu, and gravity remain live outside it.

### N2 -- wall-independence audit

The collapsed load-bearing set contains two walls:

- `W_glue`: the positive ordinary trace does not exactly re-glue the periodic
  action; it exactly re-glues the AP carrier;
- `W_state`: the trace that does exactly re-glue the periodic action is graded
  and is negative on `Podd` in both declared algebras.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `W_glue`, `W_state` | no | no | yes |

If periodic gluing selected the ordinary trace, `W_glue` would close while the
present graded functional would remain nonpositive.  If an action-derived
physical algebra removed `Podd`, `W_state` could close while the ordinary/AP
identity would remain.  The frozen reflection failure is not counted as a
third independent wall because the opposite sign repairs it and neither sign
changes the two load-bearing walls.

### N3 -- hidden-wall scan

- “CAR” means the explicitly constructed two-mode CAR algebra and frozen
  occupation order; no unnamed statistics category is used.
- “Even CAR” means the full parity-even subalgebra, including its odd-sector
  central projector.  It does not mean postselection onto even states.
- “Exact gluing” means equations (4), (8), and (9), with both seam
  orientations; it is not a fitted normalization.
- “Positive” means nonnegative on every positive operator in the declared
  finite algebra, not merely a positive determinant or partition function.
- “Selected” refers only to the algebraic seam identity.  It is not a claim
  that the minimal axioms make periodic time physical.
- No “standard QFT,” background time arrow, filling, sector weight, Record
  effect, or gravity input is load-bearing.

The scan exposes no hidden condition inside the narrow claim.  The CAR type
and observable algebras are explicit tournament inputs, which is why other
operator systems remain live.

### N4 -- residual matching

| cited witness | witness residual | present residual | match and use |
|---|---|---|---|
| [Block 202](ADMISSIBILITY_D4_L12_OPEN_TIME_STABLE_OS_EVENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md), equations (7)--(11) | global reflection sign on the literal open full-field form | sign row of the current tournament | exact input/control; current runners reconstruct it |
| [P2 AP trace bridge](P2_PHASE_BLINDNESS_FROM_RP_TRANSFER_TRACE_BRIDGE_NOTE_2026-05-28.md), lines 108--124 | AP determinant has an `I+T` ordinary-trace factor | AP changed-carrier control | exact mechanism match for the control only; dropped as proof of periodic (8) |
| [Block 196](ADMISSIBILITY_D4_L24_BEREZIN_OS_SPIN_STRUCTURE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md), lines 264--304 | finite-circle reflection depends on seam/spin compatibility | trace/state positivity after exact gluing | different residual; motivation only and dropped as proof |
| [Block 198](ADMISSIBILITY_D4_L24_EVEN_ODD_TWO_STEP_OS_PARITY_HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md), lines 292--298 | one inherited even exterior word has negative RP norm | graded state is negative on the central odd-sector projector | different object and residual; context only and dropped as proof |
| current exact runners, `finite_action_facts` / `facts` and projector gates | periodic/AP determinant identities and complete D1 state table | exact residuals `W_glue` and `W_state` | yes; sole direct evidence |

No prior periodic RP failure is used to infer the new graded projector result.

### N5 -- rhetoric and resolution audit

per_element: checked every vacuum, two one-particle, pair, and total parity projector value in the exact D1 two-mode ordinary and graded functionals.

per_site: checked both oriented seams of the literal periodic and antiperiodic L24 actions under the fixed 0..11 | 12..23 two-half cut.

per_mode: checked the D1 squared-radius-zero stable transfer mode exactly; not executed — the second D1 radius and all other carrier/radius targets remain sealed.

per_block: checked the full two-component 48-dimensional action, exact two-half Schur re-gluing, four-sector CAR functional, and all eight tournament cells.

lattice_wide: checked and not executed — no all-carrier spin rebuild, Record descent, history process, gravity response, axiom amendment, retention, or TOE closure is claimed.

The negative phrase is “no compatible cell in the registered periodic D1
zero-radius tournament.”  It is not “periodic fermions never define a state,”
“Records cannot be derived,” or “the TOE route is closed.”  These five lines
also land verbatim in primary cached stdout.

### N6 -- partial-closure and primitive scan

No new minimal axiom is asserted.  The four axioms require probabilities to
be coherent once present; they do not specify the temporal spin structure,
CAR sector, or exact Record operator system.

Legitimate partial closures are:

- treat periodic `L24` as a spectral regulator and derive the physical state
  from the already-live open/infinite-time positive route;
- explicitly rebuild an AP carrier and re-prove compatibility with the frozen
  matter modes and event map;
- derive a Gauss/superselection constraint from the action, then prove that
  its sector compression exactly replaces rather than postselects the
  periodic functional;
- derive an exact unital map to the fixed Block-194 commutative PVM and test
  whether its positive cone contains the offending parity projection; or
- ratify a spin/trace convention as downstream theory data, bound the theorem
  under that import, and later audit whether the import can be retired.

The last path may be a convention/bridge ratification rather than a new axiom.
This note therefore does not label the residual “axiom required.”

### N7 -- strongest hostile steelman

A hostile reviewer should reject the choice of the full even CAR algebra as
the physical event algebra.  Observable Records are the fixed commutative
Block-194 PVM/operator system, not every parity-preserving CAR operator.  It is
possible that an exact unital descent annihilates or never contains
`Podd` while preserving all registered Record effects, or that an
action-derived Gauss constraint removes the odd state block before the
functional is normalized.  In either case the graded periodic functional
could be positive on the actual Record cone despite failing on the larger
even CAR algebra.  The terminal obligation is concrete: construct that map or
constraint, prove exact periodic re-gluing and unital positivity, and recover
the eight fixed effects without fitted sector weights.

This steelman defeats every broad probability or periodic-carrier no-go and
sets the next direct Born/history challenger.  It does not defeat the narrow
tournament result because the two preregistered algebras explicitly include
`Podd` and the exact table exhausts them.

### N8 -- cross-cycle echo

- Block 196 turned a periodic reflection failure into a live AP/seam repair.
  That mechanism is explicitly retained here as the changed-carrier control.
- Block 198 showed that an even-word restriction did not repair a different
  inherited periodic RP form.  The present block does not inherit that result;
  it checks the new central parity projector directly.
- Block 201 rejected a raw determinant event normalization without rejecting
  action-derived probabilities.  Blocks 202--203 followed its partial-closure
  path through a boundary state and now isolate the trace/state mismatch.
- Block 202 showed that a sign convention can rescue an open form.  The new
  exact seam calculation demonstrates why the same convention mechanism does
  not change the periodic trace type.
- The P2 AP trace bridge shows a similar sign wall retired by changing temporal
  spin structure.  That same mechanism can apply here only after the frozen
  matter-mode compatibility is re-proved.
- Earlier sector-weight ledgers repeatedly distinguish normalization of a ray
  from selection among sectors.  The fixed-even alternative is therefore
  queued as a selection theorem, not silently normalized into success.

No cross-cycle echo repairs the exact declared cells.  Several echoes do
repair broader claims, which is why the disposition remains partial narrowing.

**N1--N8 disposition:** PASS for exhaustion of the exact registered periodic
D1 zero-radius sign/algebra/trace tournament.  FAIL for a broad probability,
spin-structure, sector, Record, history, gravity, axiom, or TOE no-go, none of
which is shipped.

## 9. Axiom And TOE Accounting

| item | before | after | reason |
|---|---:|---:|---|
| obligations retired | 0 | 0 | no positive end-to-end dependency closed |
| minimal axioms | unchanged | unchanged | spin, sector, and event algebra remain downstream theory data |
| Records lane | 95 / 92 / 50 | 95 / 92 / 50 | no normalized Record state or retained theorem |
| causal-time lane | 76 / 72 / 41 | 76 / 72 / 41 | no process or causal trace recursion |
| matter lane | 95 / 96 / 75 | 95 / 96 / 75 | AP/matter compatibility is untested |
| gravity/source lane | 70 / 45 / 29 | 70 / 45 / 29 | separately staffed; no gravity result here |
| Born/history lane | 84 / 63 / 34 | 84 / 63 / 34 | periodic full/even-CAR route narrowed, not closed positively |

The significant progress is a decision, not a percentage: extending the
literal periodic full/even-CAR state construction is no longer productive.
The next work must change a load-bearing object—Record operator system,
action-derived sector, temporal spin structure, or open/infinite-time state.

## 10. Reproduction And Standing

```bash
python3 scripts/admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.py
python3 scripts/admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.py --self-test-mutations
python3 scripts/independent_admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.py
python3 scripts/independent_admissibility_d4_l24_reflection_algebra_gluing_discriminator_2026_08_26.py --self-test-mutations
```

Expected scorecards are primary `PASS=8 FAIL=0`, primary mutations `27/27`,
independent `PASS=8 FAIL=0`, and independent mutations `14/14`.

The claim is proposed and bounded.  Only the independent audit lane can set a
retained verdict.  No audit verdict is applied here.
