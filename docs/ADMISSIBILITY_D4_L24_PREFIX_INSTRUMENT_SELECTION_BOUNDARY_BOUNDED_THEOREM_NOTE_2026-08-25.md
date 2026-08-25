---
claim_id: admissibility_d4_l24_prefix_instrument_selection_boundary_bounded_theorem_note_2026-08-25
claim_type: bounded_theorem
claim_scope: "On the fixed Block-192 periodic L24 Euclidean action and Block-194 event PVM, Block 195 proves an exact normalized one-shot Lueders instrument and faithful M2 dilation. It then tests the direct positive-time Schur-graph shift, the Gram-projected translation family, and the adjacent covariance predictor before any TT response. The direct shift leaves the Schur graph with residual rank two and has a negative OS-contraction witness. The projected translations are not OS self-adjoint and fail the translation composition law at order three. The raw adjacent predictor is a strict contraction, and its reflected Hermitian kernel has zero lag one but nonzero scalar lag two at both tested radii. Its radius-zero Clifford lift is algebraically exact but is not derived as a distinguished quantum subinstrument from the positive reflected kernel. Conditional on designating that lift as a trace-nonincreasing CP subchannel, two exact proper-cubic and Block-194 fiber-reflection-label covariant CPTP completions preserve the maximally mixed state and prefix normalization while producing inequivalent two-event cylinders. Full L24 time-reflection covariance of those witnesses is not claimed. Therefore none of the three tested extraction constructions selects the physical inter-crossing channel required by the preregistered gate. TT response and held-outs remain sealed. This is a narrow derivation boundary for three tested constructions, not a no-go for full OS/CAR reconstruction, parity-doubled transfer, global Euclidean process tensors, independently derived clocks or channels, gravity, Record formation, Born forcing, the axioms, or the TOE."
parents:
  - admissibility_d4_detector_conditioned_m2_pointer_discriminator_boundary_bounded_theorem_note_2026-08-25
upstream_dependencies:
  - minimal_axioms
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: advances
artifact_role: theorem
audit_required_before_effective_retained: true
bare_retained_allowed: false
one_shot_lueders_instrument: exact
coordinate_shift_os_contraction: failed
projected_shift_semigroup: failed_at_order_3
adjacent_predictor: strict_contraction
cp_completion_selection: nonunique_under_conditional_subchannel_typing
tt_response: not_executed
heldouts: sealed
broad_time_no_go: not_claimed
no_go_discipline_gate: FAIL
negative_disposition: partial-attempt-with-named-untested-routes
minimal_axiom_update: none
toe_percentage_movement: 0
---

# L24 Prefix-Instrument Selection Boundary

**Date:** 2026-08-25

**Campaign block:** 195

**Type:** `bounded_theorem`

**Standing:** proposed bounded theorem; independent audit unset

Primary runner:
[`admissibility_d4_l24_prefix_instrument_selection_boundary_2026_08_25.py`](../scripts/admissibility_d4_l24_prefix_instrument_selection_boundary_2026_08_25.py).

Cached stdout:
[`admissibility_d4_l24_prefix_instrument_selection_boundary_2026_08_25.txt`](../logs/runner-cache/admissibility_d4_l24_prefix_instrument_selection_boundary_2026_08_25.txt).

## 1. Result Up Front

The fixed Block-194 apparatus already performs one exact quantum measurement.
Its eight projectors are valid Lüders Kraus operators, their adjoint-products
sum to the identity, the maximally mixed state gives weight `1/8` to each, and the
nonidentity M2 writer realizes the same effects.  The missing ingredient is
not the one-shot PVM, its normalization, or its pointer bit.

What remains unconstructed by these routes is the physical channel between
two registered crossings.
The Block-192 action is a finite Euclidean action with a positive reflected
Schur Gram; it is not by itself a causal channel on the Block-194 `C^32`
event fiber.  Block 195 tests three response-blind ways to extract the missing
law:

1. restricting one positive-time coordinate shift to the Schur graph;
2. projecting every coordinate translation back with the exact positive
   Gram; and
3. lifting the exact adjacent covariance predictor to a CPTP map.

The first construction is not graph invariant and is not an OS contraction.
The second is not self-adjoint in the OS metric and its compressed
translations stop composing at order three.  The third yields a strict
predictor whose exact Clifford lift is not physically typed by the positive
kernel.  Conditional on tagging that lift as a trace-nonincreasing CP
subchannel, at least two exact proper-cubic/fiber-label-covariant CPTP channels
complete it but give different two-event probabilities.

The preregistered dependency gate therefore stops before TT response, history
word enumeration, pointer-cell persistence, or held-outs.  The exact positive
one-shot instrument is reusable.  The negative conclusion is deliberately
narrow: the three tested constructions do not derive a unique physical
inter-crossing channel from the present parents.

## 2. Authority And Frozen Scope

The runner binds:

- `origin/main` at `b11811704efa98a12272d572f666e530a807f6c1`;
- the current [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), byte-identical on
  main and in this worktree;
- the published Block-194 stack tip at
  `6eeae12de0ec1f8263dfef39a0b021581b82a070`; and
- the pre-target Block-195 registration at
  `28804ebe9eff1f2a86ea5bf9e7d4b96b40cf149a`.

Before calculation, Block 195 froze the literal Block-192 L24 action, mass
`2/7`, `12/12` cut, ordinary-transpose reflected construction, Block-194
eight-effect PVM and M2 dilation, physical state space `C^32`, maximally mixed
state, all 24 proper-cubic frames, temporal reflection, and the requirement
that an inter-crossing law be selected without response information.  It
forbade assuming `U=exp(-i H Delta t)`, a Wick rotation, a transfer matrix, a
physical-time interpretation of one Euclidean shift, a cadence, a ready-state
answer, or a response-selected phase or weight.

The TT source response was not evaluated.  D2, D3, H2, and X1 were not opened.
PR #7669 was not imported: it uses a distinct width-family carrier and
supplies no L24 channel or Regge-D4-L24 intertwiner.

## 3. Exact One-Shot Instrument

Let the eight Block-194 effects be `F_alpha`, where
`alpha=(s,t,sigma)`.  They are mutually orthogonal projectors on
`H_event=C^32` and satisfy

\[
 F_\alpha^\dagger=F_\alpha,
 \qquad F_\alpha F_\beta=\delta_{\alpha\beta}F_\alpha,
 \qquad \sum_\alpha F_\alpha=I_{32}.
\]

The exact one-shot selective maps

\[
 \mathcal L_\alpha(\rho)=F_\alpha\rho F_\alpha
\]

are completely positive, and

\[
 \sum_\alpha F_\alpha^\dagger F_\alpha=I_{32}.
\]

Thus their sum is trace preserving.  On
`rho_*=I_32/32`,

\[
 \operatorname{Tr}\mathcal L_\alpha(\rho_*)={1\over8}
\]

for every outcome.  The fixed Block-194 controlled unitary on
`C^32 tensor C^2` pulls the declared joint event/pointer readout back to these
same effects.  This is an exact Lüders instrument, not merely a POVM.

This closes one small but real question: the fixed apparatus can perform and
write one normalized event.  Repeating the displayed Lüders operation with
no intervening physics would be a new choice, however, not a channel derived
from the Euclidean action.

## 4. Direct Coordinate-Shift Test

The cheapest action/cut-native candidate is tested on Block 192's exact
radius-one two-component reduced copy.  In its real phase basis let `A` be the
`48 x 48` action, split it across the first and last 12 time sites, and define
the right Schur graph

\[
 V=\begin{pmatrix}I_{24}\\-d^{-1}c\end{pmatrix},
 \qquad
 G=V^T(A^{-1}+A^{-T})V.
\]

Here `G` is exactly positive by the inherited Block-192 certificate.  Let
`S=U tensor I_2` be the literal forward periodic coordinate shift and `E_N`
the first-half embedding.  The direct boundary-coordinate candidate is

\[
 T_{\rm coord}=E_N^T S V.
\]

If this were the restriction of the coordinate shift to the OS boundary
graph, it would obey `SV=VT_coord`.  Instead the runner derives

\[
 \operatorname{rank}(SV-VT_{\rm coord})=2.
\]

It also finds

\[
 \operatorname{rank}(GT_{\rm coord}
             -T_{\rm coord}^T G)=24
\]

and a rank-four contraction defect.  One exact diagonal witness is

\[
 (G-T_{\rm coord}^TGT_{\rm coord})_{20,20}
 =-{74727331655898590523064942942
 \over760099388132784388227824966985}<0.
\]

Therefore this literal restriction is neither graph invariant nor an OS
contraction.  The same frozen construction in the reverse orientation has
the corresponding obstruction on the reflected coordinate; selecting the
opposite arrow does not repair it.

## 5. Positive-Gram Projection Test

A more charitable construction projects every translated graph vector back
using the exact positive kernel.  Define

\[
 T_n=G^{-1}V^T(A^{-1}+A^{-T})S^nV.
\]

This construction is normalized by the existing Gram and does not insert a
TT response.  The runner derives

\[
 \operatorname{rank}(GT_1-T_1^TG)=24.
\]

The first accidental composition succeeds,

\[
 T_1^2=T_2,
\]

but the next one does not:

\[
 \operatorname{rank}(T_1^3-T_3)=2.
\]

Its first nonzero entry is

\[
 {424161474649141958655555005995533676300496869231255475132630575
 \over
 350280483331290462600206474043838198848776384440117346120766317131121343}.
\]

Thus the compressed family is not a representation of the literal L24
translations.  Iterating `T_1` anyway would define a new dynamics that no
longer equals projection of the parent coordinate translations after the
second step.

## 6. Adjacent Predictor And Even-Lag Structure

The third test asks for less.  In the radius-zero two-component copy, let
`C=A_0^{-1}` be the raw Euclidean covariance.  Its adjacent linear predictor
is

\[
 R=C_{1,0}C_{0,0}^{-1}
   =-q\sigma_z,
 \qquad
 q={153558160154\over204224113601}.
\]

Exactly `0<q<1`.  Hence

\[
 c=q^2={23580108549881513303716
 \over41707488576114153187201},
 \qquad
 d=1-c={18127380026232639883485
 \over41707488576114153187201}
\]

are both positive.  The predictor is a strict contraction, not a trace-
preserving one-Kraus quantum channel.

The Hermitian reflected kernel `H=A^{-1}+A^{-dagger}` adds a useful warning.
At both frozen radii zero and one its lag-one predictor vanishes exactly,
while its lag-two predictor is a nonzero scalar:

\[
 H^{(0)}_{2,0}(H^{(0)}_{0,0})^{-1}
 ={116476593513\over204224113601}I_2,
\]

\[
 H^{(1)}_{2,0}(H^{(1)}_{0,0})^{-1}
 ={61598134870475\over379709769775249}I_2.
\]

The parent object therefore exposes centered/even-lag correlation structure
rather than an already supplied first-order causal Markov law.  This does not rule out a
parity-doubled or two-step reconstruction; it makes that route explicit.

## 7. Exact CPTP Completion Nonuniqueness

At radius zero the full internal action is

\[
 I_{24}\otimes mI_{16}+D\otimes\Gamma_t.
\]

Because `Gamma_t^2=I`, its spectral projectors reduce the adjacent-covariance
calculation exactly to the two scalar sectors tested above.  The lifted raw
predictor is therefore

\[
 R_{16}=-q\Gamma_t,
 \qquad
 R_{32}=-qJ_R,
 \qquad
 J_R=\operatorname{diag}(\Gamma_t,\Gamma_t).
\]

It satisfies `R_32^dagger R_32=c I_32<I_32`, so it can algebraically define
the trace-nonincreasing CP map

\[
 \Psi(\rho)=R_{32}\rho R_{32}^\dagger=cJ_R\rho J_R.
\]

The raw covariance `A^{-1}` is not Hermitian, while the positive reflected
kernel has exactly zero lag-one predictor.  Therefore the parent has not
derived `Psi` as a distinguished physical subinstrument: designating it as
one is a conditional typing choice.  The global minus sign is a Kraus phase
and drops out of `Psi`.  Even under that conditional designation, the missing
CP complement is not selected.  On `C^32`, `J_R` is a Hermitian unitary, it
commutes with all 24 proper-cubic
representations, and it implements the frozen reflected event relabelling.
Consider two channels:

\[
 \Phi_A(\rho)=cJ_R\rho J_R+d\rho,
 \qquad
 \Phi_B(\rho)=J_R\rho J_R.
\]

Equivalently, they can be represented by the Kraus lists

\[
 \{qJ_R,\sqrt d I\},
 \qquad
 \{qJ_R,\sqrt d J_R\}.
\]

More invariantly,

\[
 \Phi_A-\Psi=d\,\operatorname{Id},
 \qquad
 \Phi_B-\Psi=d\,\operatorname{Ad}_{J_R}
\]

are both CP.  Thus, conditional on the declared `Psi`, `Phi_A` and `Phi_B` are
completions of the same CP subchannel in the basis-independent CP order.
Their completeness identities are exact:

\[
 cJ_R^\dagger J_R+dI=I,
 \qquad
 (c+d)J_R^\dagger J_R=I.
\]

Both maps are CPTP, unital, proper-cubic covariant, covariant under the
Block-194 fiber-reflection event relabelling, and preserve `rho_*`.  Full L24
coordinate/time-reflection covariance is not established for these witnesses.
They are not the same channel.  The fiber reflection maps `F_0` to `F_7`.
After the first outcome `F_0`, their only nonzero second-outcome cylinders are

\[
 p_A(0,0)={d\over8},\qquad p_A(0,7)={c\over8},
\]

and

\[
 p_B(0,0)=0,\qquad p_B(0,7)={1\over8}.
\]

Both obey

\[
 \sum_\beta p_A(0,\beta)
 =\sum_\beta p_B(0,\beta)={1\over8},
\]

so ordinary prefix coarse-graining does not distinguish them.  Their distinct
cylinder probabilities prove that positivity, trace preservation, the fixed
state, the declared symmetries, the PVM, and this conditionally designated CP
subchannel do not select a unique completion.

These two channels are conditional witnesses of complement freedom, not
proposed physical laws and not intrinsically action-compatible channels.  A
stronger reconstruction from the complete Euclidean algebra could type a
different CP object and select one channel or neither.

## 8. Precise Missing Datum And Stop

The first missing datum is

\[
 \boxed{\Phi_{\rm phys}:M_{32}\longrightarrow M_{32},
 \text{ an action-selected CPTP inter-crossing channel}}
\]

together with its physical time orientation and its placement before or after
the fixed PVM interaction.  On an OS route this means deriving:

1. a positive-time translation that descends to the OS quotient as a
   contraction;
2. an identification of that quotient with the Block-194 event fiber; and
3. a trace-preserving channel, unique up to declared physical equivalence,
   from the descended transfer object.

Once any CPTP channel is genuinely supplied, two-step prefix addition is
elementary:

\[
 \sum_{\beta,j}
 (F_\beta L_jF_\alpha)^\dagger(F_\beta L_jF_\alpha)
 =F_\alpha\left(\sum_jL_j^\dagger L_j\right)F_\alpha
 =F_\alpha.
\]

The difficulty is selection of `L_j`, not this normalization identity.  The
preregistered rule treats multiple inequivalent compatible channels as a
dependency failure.  Block 195 therefore stops here.  It neither computes a
TT history response nor mistakes tensoring fresh M2 cells for a derivation of
stable physical Records.

## 9. No-Go Discipline Gate -- FAIL / Demotion

This section is load-bearing.  The exact positive one-shot instrument, the
three tested construction results, and the explicit completion witnesses can
ship.  A general time, OS, history, Record, or TOE negative cannot.  The
discipline gate is `FAIL`, and the negative disposition is
`partial-attempt-with-named-untested-routes`.

### N1 -- normalized alternative-route enumeration: FAIL

Three normalized extraction routes were attempted.  Six materially distinct
routes remain live.  Every live route is marked `UNTESTED -- N1 FAIL`; their
existence prevents route closure.

| normalized route | physical mechanism / terminal obligation | status | evidence / outcome |
|---|---|---|---|
| direct Schur-graph shift | literal `S=U tensor I_2` / invariant OS graph and contraction | ATTEMPTED | graph residual rank two; contraction defect has an exact negative diagonal |
| positive-Gram compression | kernel-orthogonal projection of `S^n` / self-adjoint compositional transfer | ATTEMPTED | metric-symmetry residual rank 24; `T_1^3-T_3` rank two |
| adjacent predictor completion | raw covariance lift, physical subinstrument typing, then CPTP complement / unique proper-cubic and fiber-label-covariant channel | ATTEMPTED | lift is exact but the positive kernel does not type it as a subinstrument; conditional tagging leaves two distinct completions and full time-reflection covariance is unproved |
| full OS/GNS/CAR reconstruction | positive-time algebra and quotient / selected transfer contraction and event-fiber identification | UNTESTED -- N1 FAIL | live; not equivalent to the tested one-particle Schur restrictions |
| parity-doubled two-step state | enlarge state by even/odd phase or one memory cell / first-order CPTP law on enlarged fiber | UNTESTED -- N1 FAIL | live and motivated by exact zero lag one/nonzero lag two |
| global Euclidean process tensor | positive multi-time functional / normalized quantum comb and consistent restrictions | UNTESTED -- N1 FAIL | live; the L24 direct-sum coordinate is not already such a tensor product |
| independently derived clock/transfer | Hamiltonian, apparatus clock, or environment from new physical input / unique channel and cadence | UNTESTED -- N1 FAIL | live but must be derived or registered, not assumed |
| Regge-D4-L24 intertwiner/Riesz route | action/source carrier map and positive dual / gravity-selected observable and transfer structure | UNTESTED -- N1 FAIL | frozen immediate fallback |
| autonomous formation and persistence | environment/amplifier with fresh cells / durable readable Records | UNTESTED -- N1 FAIL | downstream of channel selection |

Because live mechanisms remain, this block cannot support a broad no-go.

### N2 -- full directional wall-independence audit: PASS

The collapsed wall set is `{W1,W2,W3}`: `W1` is the exact one-shot event
instrument; `W2` is one action-selected physical inter-crossing law, including
positive-time descent, event-fiber identification, physical orientation/PVM
ordering, and a unique CPTP channel; and `W3` is autonomous Record formation
and persistence.  Their current states are `PASS`, `FAIL for the three tested
extractions`, and `UNTESTED`.

Prefix coarse-graining is not retained as an independent wall.  Once `W1` and
the TP/channel portion of `W2` are supplied with an ordering, the identity in
Section 8 proves the prefix sum automatically.  Likewise, the former
“transfer” and “unique channel” rows are collapsed into `W2` because the
transfer matters here only through a typed descended channel.

| pair | first direction | reverse direction | independent? |
|---|---|---|---|
| W1 / W2 | a normalized PVM supplies no inter-event evolution, time orientation, or environmental completion | an action-selected channel need not specify this registered PVM or its pointer realization | yes |
| W1 / W3 | a one-step pointer flip is not autonomous formation or durability | a durable bit does not prove the declared PVM interaction | yes |
| W2 / W3 | a typed CPTP history law may erase rather than stabilize a pointer and supplies no formation site/rate | persistent Records do not select the microscopic channel, time orientation, or cylinder weights | yes |

No closed wall is renamed as an open one.  In particular, the exact Lüders
instrument remains a positive result even though the inter-crossing channel
is missing.

### N3 -- hidden-wall scan: PASS

The phrase scan covered `we assume`, `by construction`, `as is standard`,
`the framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `standard QFT`, `registered`, and `canonical`, plus close
variants.

| hit | classification |
|---|---|
| `preregistered` in the scope and stop rule | procedure/evidence: commit `28804ebe9e` freezes the dependency gate; registration supplies no physical law |
| `registered crossings` in the scope | target terminology for the intended event sequence; the computation does not infer a crossing schedule |
| `normalized` and `normalization` | explicit TP/prefix terminal obligations and refit prohibitions, not imported values |
| `naturally` | no substantive hit; the note instead names each tested construction and its equations |
| `canonical` | no substantive physical-selection hit; temporal reflection and PVM are called fixed/frozen |
| all other required phrases | no substantive hit |

The Euclidean coordinate shift is never called physical time.  The two CPTP
maps are explicit counter-witnesses to selection, not background dynamics.
No desired TT response, cadence, event word, source phase, or held-out result
enters any dependency calculation.

### N4 -- citation-by-citation residual matching: PASS

| cited authority with file and lines | witness residual | current residual | match and use |
|---|---|---|---|
| `docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md:159-212` | finite reflected Schur Gram is positive and has a fixed internal marginal | the graph shift and projected translations fail terminal transfer conditions | yes for the exact Gram/action input only; positivity is not cited as a negative witness |
| `docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md:355-375` | reflection and write congruence are algebraic and do not derive physical translation, readability, or permanence | current parents lack a selected inter-crossing CPTP law | yes for premise typing; the current exact residuals are newly computed |
| `docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md:134-182` | eight orthogonal projectors and faithful M2 dilation | current one-shot Lüders instrument is exact | exact positive inheritance, not evidence for a history no-go |
| `docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md:231-238` | one-step pointer write lacks formation, permanence, and physical time | current channel/Record wall is downstream | yes for the named residual only |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:116-123,175-187` | transition values, time, updates, persistence, source/action, and physical-observable identification are downstream | Block 195 needs a selected time-oriented channel | yes only for axiom boundary; it does not prove any matrix residual |

The rank, sign, composition, predictor, and cylinder residuals are computed by
the Block-195 runner.  Older notes establish only literal inputs and scope.

### N5 -- execution resolution: PASS

per_element: checked the eight exact Block-194 Lueders Kraus projectors, one reduced action fiber, one conditional lifted CP subchannel, and two exact CPTP completions.

per_site: checked one adjacent L24 covariance predictor and one fixed first-to-second event prefix; no physical time step was assumed.

per_mode: checked the frozen radius-zero and radius-one reflected lag-one/lag-two kernels; no TT source response or held-out point was evaluated.

per_block: checked one-shot instrument, coordinate shift, metric projection, covariance predictor, and channel completion as separate dependency blocks.

lattice_wide: checked and not executed -- no full OS/CAR reconstruction, global process tensor, autonomous Record persistence, Regge bridge, nonlinear gravity, or retained TOE theory is claimed.

### N6 -- partial-closure, convention, and axiom scan: PASS

| positive or partial path | status after Block 195 | next closure test |
|---|---|---|
| one-shot measurement | exact Lüders instrument, uniform baseline, complete PVM, and faithful M2 dilation | preserve; do not redo pointer algebra |
| naive Schur restriction | exact bounded failure | do not call the coordinate shift physical evolution |
| Gram-projected translations | exact order-three composition failure | a different quotient/algebra construction must supply its own composition proof |
| adjacent predictor | exact strict coefficient and even-lag structure | use only as a constraint, not a supplied channel |
| multi-time reconstruction | open | full OS/GNS/CAR, parity-doubled, or process-tensor construction may still close it |
| Regge-D4-L24 bridge | open and now highest leverage | solve the response-blind one-cell Ward/covariance/reflection intertwiner before Riesz inversion |

The minimal axioms should not be amended to hide this missing bridge.  Their
current authority already says that Admissibility is not a dynamics axiom and
does not select a transfer operator or transition weights, while update laws,
time, persistence, and source/observable identification remain downstream
(`docs/MINIMAL_AXIOMS_2026-06-29.md:108-130,173-187`).  A future derivation
could close the channel wall without changing an axiom.  A future physical
model might instead establish that a new primitive is genuinely required;
three failed extraction attempts are not enough to make that decision.

### N7 -- strongest steelman: FAIL for a negative

> **Hostile reviewer:** You tested one-particle Schur restrictions, not the
> full reconstruction theorem.  A reflection-positive Euclidean fermion
> system can require an algebra of positive-time observables, quotient by its
> null ideal, and a GNS/CAR representation before translation becomes a
> contraction.  The exact zero lag-one and nonzero lag-two structure also
> advertises a parity-doubled state: one memory bit could turn the two-step
> kernel into a first-order channel on a larger fiber.  Alternatively a global
> L24 process tensor could have consistent marginals without identifying the
> time coordinate as 24 tensor-product system copies.  None of those objects
> is equivalent to `E_N^T S V` or the displayed Gram projection.  Your two
> CPTP completions prove underdetermination only under the tested predictor
> constraints; a complete reconstruction could supply an extra equation that
> selects a unique Choi matrix.  If the quantum-history route remains costly,
> the response-blind Regge-D4-L24 intertwiner can connect the already-derived
> source/action structures before any observable is chosen.  These are
> concrete, falsifiable, untested escape mechanisms.

The parent supplies a finite positive reflected Schur Gram but explicitly
stops short of physical translation and permanent dynamics
(`docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md:159-212,355-375`).
That is exactly the setting in which the steelman's larger-algebra
reconstruction could differ from the tested compressions.  The steelman is
scientifically credible and names terminal obligations.  N7 therefore forces
negative demotion.

### N8 -- cross-cycle retirement/mechanism audit: PASS

| earlier wall | later campaign / mechanism | retired? | lesson for Block 195 |
|---|---|---|---|
| Block-191 lacked one common temporal carrier | Block 192 constructed the minimal L24 Weyl carrier and positive reflected Gram (`docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md:109-212`) | yes for the frozen endpoints and Gram | a new representation can retire a wall; local proxy failures were not universal |
| Block-193 lacked a selected detector and explicit pointer | Block 194 solved the nondemolition classifier and constructed the exact M2 dilation (`docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md:88-182`) | yes within the declared detector family | preserve the PVM; channel selection is a distinct wall |
| Block-194 left full-L24 observability live | Block 195 tests the prerequisite normalized inter-crossing law before response | no; three extraction routes fail or are underdetermined | the pincer now shifts to the Regge bridge while fuller reconstruction routes stay live |
| present Regge-D4-L24 carrier wall | no later campaign yet | no | next execute the one-cell intertwiner feasibility system before observable/Riesz selection |

No previous bounded negative is recycled as proof that the present live routes
cannot work.

### Gate disposition

| gate | status |
|---|---|
| N1 alternative routes | FAIL -- six materially distinct routes remain live |
| N2 directional wall audit | PASS |
| N3 hidden-wall scan | PASS |
| N4 residual matching | PASS |
| N5 execution resolution | PASS |
| N6 partial/axiom/convention scan | PASS |
| N7 strongest steelman | FAIL for a negative -- credible reconstruction routes remain |
| N8 cross-cycle echo | PASS |
| overall no-go discipline | **FAIL; negative demoted** |

Allowed disposition: the exact one-shot instrument, the observed residuals of
the three tested extraction routes, and the two explicit channel-completion
witnesses.  Forbidden disposition: a no-go for OS reconstruction, physical
time, histories, Records, gravity, Born forcing, axiom completion, or the TOE.

## 10. Portfolio Consequence

The history seam has reached its preregistered stop efficiently.  Enumerating
`8^24` words would add no information because the inter-crossing map is not
selected; even a compressed recurrence would merely iterate an inserted law.
The immediate campaign therefore returns to the independent portfolio
recommendation: a response-blind Regge-to-D4/L24 carrier/intertwiner gate.

A route-pivot preflight corrected its typing.  The 15 positive Regge edge
directions are closed under coordinate permutations but not under time
reflection or the full 24-frame proper-spatial action.  Their time-reflection
union has 22 orientations; the full proper-spatial orbit modulo edge reversal
has 40.  Therefore a `15 x 10` map can be only the Ward/S3 prefilter.  The
reflection gate is `22 x 10`, and a full-frame claim requires the 40-edge
induced carrier or an explicitly equivalent orientation bundle.

An exploratory, non-preregistered coefficientwise solve already finds the
one-cell `15 x 10` raw-label Ward system consistent: rank and augmented rank
are 798 in 800 unknowns; permutation covariance fixes the two remaining
parameters to `sqrt(2)/12`; and the resulting map has rank ten at D1 and H1.
One common ten-row minor is exactly `i/1024` at D1 and
`-(sqrt(3)-i)/2048` at H1, so those prefilter ranks are symbolic rather than
numerical.
This raw-identity solve is only an algebraic prefilter.  The D4 gauge columns
are link centered, whereas the Regge columns are vertex displacements; their
time-reflection representations differ by a temporal Laurent placement
factor.  The mismatch is hidden at D1/H1 because their transfer has zero time
component.  Block 196 must independently reproduce the prefilter and freeze
the existing link-to-vertex placement map before the Ward equation, rather
than silently identify columns or fit a new gauge-carrier map.  It then targets
the still-unknown 22/40-orientation reflection lift and stops before inversion,
Riesz selection, or TT response on placement failure, carrier nonclosure, rank
loss, covariance failure, or unresolved normalized map freedom.  Nothing in
this preflight is a Block-195 claim or a retained result.

The same preflight exposes the earliest next discriminator.  An honest chain
map needs a gauge-carrier leg `C(z)`, for example
`M(z) Gamma_D(z)=G_R(z) C(z)`, with `C(1)=I`.  At the fixed temporal Nyquist
point `z_t=-1`, the raw D4 link reflection is `I_4` while the Regge vertex-
vector reflection is `diag(1,1,1,-1)`.  Equivariance forces the time row or
column of `C` to vanish, hence `rank C<=3`.  This suggests an exact
single-cover obstruction if global rank four is required.  Midpoint averaging
has the same zero; an invertible half-shift instead requires a doubled or
half-lattice placement carrier.  Block 196 will treat this as known exploratory
input to reproduce, then test the still-live doubled 22/40-edge route.  It is
not a no-go for doubled carriers or full OS/GNS/CAR reconstruction.

## 11. Claim Boundary And TOE State

Block 195 proposes bounded support only.  It does not claim:

- that all OS, GNS, CAR, parity-doubled, or process-tensor routes fail;
- a physical-time law, cadence, channel, Hamiltonian, or global history;
- a permanent Record, formation site/rate, or persistence mechanism;
- a gravity observable or nonlinear gravity theory;
- a Born derivation, axiom amendment, or newly approved primitive;
- retirement of a derivation obligation;
- movement of any TOE percentage; or
- a retained positive end-to-end theory.

The TOE lane scores remain unchanged:

| lane | current / local / retained |
|---|---:|
| Records | 95 / 92 / 50 |
| causal time | 76 / 72 / 41 |
| matter | 95 / 96 / 75 |
| gravity/source | 70 / 45 / 29 |
| Born/history | 84 / 63 / 34 |

The significant progress is decision quality, not score movement.  The fixed
PVM is now known to be a valid one-shot instrument; the first missing history
datum is isolated to an action-selected inter-crossing channel and time
orientation.  Three cheap constructions have been grounded exactly, so the
campaign can leave this seam without confusing more word enumeration with
TOE progress.
