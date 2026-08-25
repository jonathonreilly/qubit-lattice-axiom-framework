---
claim_id: admissibility_d4_l24_exterior_natural_e8_insertion_obstruction_bounded_theorem_note_2026-08-25
claim_type: bounded_theorem
claim_scope: "On the fixed Block-192 periodic L24, m=2/7 action/cut and the Block-194 rank-four eight-projector PVM/M2 package, Block 200 constructs the literal three-boundary Schur kernels at coarse-circle sites {0,2,4} and {0,2} by independent exact routes at all nine frozen spatial radii. The D1 paired C32 lifts have ranks 96 and 64, crossing-4 pivot rank 32, non-Hermitian-defect ranks 48 and 32, and positive-definite Hermitian parts. The registered O9 operation algebra has an exact injective unital exterior representation after vacuum subtraction, with full branch rank 225 and bidegree-(1,1) branch/dephasing/identity ranks 16/128/1024. This representation is not a unital E8 event partition. More narrowly, no number-preserving exterior-natural projective extension of the eight one-particle effects can be both exhaustive on the full exterior algebra and covariant under the actual fixed-point-free Block-194 reflection: the invariant vacuum would require one reflection-covariant one-hot label, but the label involution has four two-cycles and no fixed point. The theorem does not exclude a direct Schur/Wick event functional, a covariant POVM or null outcome, a physical support/filling derived from the action, a non-number-preserving star-product/Nambu insertion, an OS/GNS quotient, an open causal boundary, Record dynamics, or another event algebra."
parents:
  - admissibility_d4_l24_event_history_interface_hankel_process_boundary_bounded_theorem_note_2026-08-25
upstream_dependencies:
  - minimal_axioms
actual_current_surface_status: demotion
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
reachability_to_target: prunes_one_insertion_family_and_preserves_live_alternatives
artifact_role: theorem
conditional_surface_status: partial-narrowing
hypothetical_axiom_status: unchanged
admitted_observation_status: none
target_claim_id: admissibility_d4_l24_exterior_natural_e8_insertion_obstruction_2026-08-25
target_blocker_text: "The literal action has a valid three-boundary kernel, but the tested exterior-natural representation does not turn the eight registered one-particle effects into an exhaustive categorical event partition on the full Grassmann exterior space."
next_trace_action: "Test a direct Schur/Wick event functional and a covariant POVM-or-null-outcome completion without treating either as a causal process; independently retain the cyclic-to-causal boundary campaign."
claim_type_reason: "The Schur equalities, ranks, positivity, PVM/reflection identities, exterior ranks, O9 algebra representation, and invariant-vacuum contradiction are exact finite-algebra results. Standing is demoted because the contradiction is conditional on number preservation, exterior naturality, projectivity, full-exterior support, and the fixed reflection action; several materially different event-functional routes remain live."
audit_required_before_effective_retained: true
bare_retained_allowed: false
preregistration_commit: 25af72ea95378ac3f83bd53be637b81b014f8723
registration_erratum_commit: 88f7eb548589ea6d507b0cdd9d6933167c1bd82c
discarded_primary_dry_runs: 2
primary_checks_passed: 5
primary_mutations_rejected: 28
independent_checks_passed: 19
independent_mutations_rejected: 17
frozen_squared_radii_checked: 9
q024_rank: 96
q02_rank: 64
crossing4_pivot_rank: 32
q024_nonhermitian_defect_rank: 48
q02_nonhermitian_defect_rank: 32
o9_exterior_representation: mathematical_control_only
action_native_e8_insertion: not_derived_in_tested_family
three_event_cylinder: sealed_after_t2
causal_process: sealed
tt_response: not_executed
heldouts: sealed
no_go_discipline_gate: PASS_for_narrow_exterior_theorem_FAIL_for_broad_history_no_go
negative_disposition: partial-narrowing
minimal_axiom_update: none
obligation_retirement: 0
toe_percentage_movement: 0
---

# L24 Number-Preserving Exterior-Natural E8 Insertion Obstruction

**Date:** 2026-08-25

**Campaign block:** 200

**Type:** `bounded_theorem`

**Standing:** proposed bounded theorem; independent audit unset

Primary runner:
[`admissibility_d4_l24_e8_three_event_effect_cylinder_insertion_2026_08_25.py`](../scripts/admissibility_d4_l24_e8_three_event_effect_cylinder_insertion_2026_08_25.py).

Independent no-import checker:
[`independent_admissibility_d4_l24_e8_three_event_effect_cylinder_insertion_2026_08_25.py`](../scripts/independent_admissibility_d4_l24_e8_three_event_effect_cylinder_insertion_2026_08_25.py).

SHA/input-bound cached stdout:
[`primary`](../logs/runner-cache/admissibility_d4_l24_e8_three_event_effect_cylinder_insertion_2026_08_25.txt)
and
[`independent`](../logs/runner-cache/independent_admissibility_d4_l24_e8_three_event_effect_cylinder_insertion_2026_08_25.txt).

## 1. Result Up Front

Block 200 resolves a real ambiguity in the post-Block-199 program.

The action side is not the immediate failure.  The literal three-boundary
Schur kernel exists, is invertible, composes exactly under nested Schur
elimination, and has a positive-definite Hermitian part at every frozen
radius.  The tempting positive `H=C+C*` pair-kernel still fails the exact
three-time composition law, so the full three-boundary kernel cannot be
replaced by a pairwise Markov shortcut.

The failure occurs at the action-to-event interface.  The eight Block-194
effects partition the one-particle `C^32` event fiber, but the exterior algebra
generated by the Grassmann variables also contains a vacuum and states with
occupation in more than one event-label subspace.  The canonical exterior
functor therefore produces occupation patterns, not exactly one of eight
categorical outcomes.

Vacuum subtraction gives a clean positive result for the separately typed
operation algebra `O9=span{id,L_alpha}`.  It preserves the exact Lueders
composition table and keeps dephasing distinct from identity.  It does not
turn `E8=span{F_alpha}` into a complete eight-outcome event partition on the
full exterior space.

There is also a sharp obstruction to repairing only the vacuum while keeping
the exterior construction projective, number-preserving, and covariant.  The
vacuum is one-dimensional and invariant.  A complete projective partition
must assign it to exactly one label.  The actual Block-194 reflection pairs
all eight labels and fixes none, so any one-label assignment breaks
reflection covariance.  Equal splitting is covariant and normalized, but it
is a POVM assignment, not an idempotent projective one.

This is a narrow exterior-functor theorem, not an action/history no-go.  T3--T6
stop before any 512-word cylinder, triple selector, causal process, response,
held-out prediction, Record/Born claim, gravity result, axiom edit, obligation
retirement, or TOE percentage movement.

## 2. Registration And Protocol Disclosure

The original preregistration was committed at `25af72ea95378ac3f83bd53be637b81b014f8723`.
It correctly separated the primary `E8` effect target from the conditional
`O9` operation target, but wrote the doubled exterior legs in the reverse
order from its own frozen column-vectorization convention.

Two primary dry runs exposed only the already frozen T0--T2 disposition before
the independent convention audit returned.  No T3--T5 value was executed or
observed.  Those dry runs are discarded as evidence.  The audit correction
was committed at `88f7eb548589ea6d507b0cdd9d6933167c1bd82c`:

\[
 \operatorname{vec}(KXK^\dagger)
   =(\overline K\otimes K)\operatorname{vec}X.
\tag{1}
\]

The corrected packet also freezes the actual reflection permutation rather
than incorrectly turning proper-cubic context covariance into a transitive
fixed-label action.  Both evidentiary runners start from the amended commit.
The primary then passes `5/5` checks and rejects `28/28` mutations; the
independent no-import checker passes `19/19` checks and rejects `17/17`
mutations.

## 3. Exact Three-Boundary Action Kernel

On the twelve-site coarse circle let

\[
 Q_s=I_{12}+{2I_{12}-V-V^T\over4\delta_s},
 \qquad \delta_s=m^2+s,
 \qquad m={2\over7},
\tag{2}
\]

where `V` is the periodic one-step coarse shift.  The frozen radii are

\[
0,{3\over4},1,{5\over4},{3\over2},2,3,
{7+\sqrt3\over4},{10+\sqrt3\over4}.
\tag{3}
\]

For `B_3={0,2,4}`, `B_2={0,2}`, and the corresponding complements, define

\[
 S_B=(Q_s)_{BB}-(Q_s)_{BI}(Q_s)_{II}^{-1}(Q_s)_{IB}.
\tag{4}
\]

Both runners independently establish, at all nine radii,

\[
 S_B=\bigl((Q_s^{-1})_{BB}\bigr)^{-1},
\tag{5}
\]

the determinant identities, positive definiteness, reflection symmetry, and
the nested identity

\[
 S_{02}=S_{024}^{02,02}
 -S_{024}^{02,4}(S_{024}^{44})^{-1}S_{024}^{4,02}.
\tag{6}
\]

This notation is literal on the coarse circle.  It must not be confused with
the separate extraction of full-L24 physical times `(0,2,4)` at even-sector
positions `(0,1,2)` used only for the `H` control below.

For D1, the incoming and outgoing spatial radii are respectively zero and
one.  Pairing their `C^16` fibers gives the Block-194 `C^32` event dimension.
The corresponding three- and two-boundary matrices have

\[
 \operatorname{rank}Q_{024}=96,
 \quad \operatorname{rank}Q_{02}=64,
 \quad \operatorname{rank}Q_{44}^{024}=32.
\tag{7}
\]

Their non-Hermitian defects have ranks `48` and `32`.  Their Hermitian parts
factor into the positive scalar Schur kernels and `2m I_16`, giving inertias

\[
 (96,0,0),\qquad(64,0,0)
\tag{8}
\]

in positive/null/negative order.  Thus non-Hermiticity is not a convergence
failure here.  The important typing result is that the `C^32` event fiber is
an incoming/outgoing pairing.  Equality of dimensions does not itself supply
an action-to-event intertwiner.

## 4. The Pairwise Positive-Kernel Shortcut Still Fails

On the literal D1 full-L24 control, set `C=A^{-1}` and `H=C+C*`.  The primary
and independent implementations reproduce

\[
 [H_{42}H_{20}-H_{40}]_{00}
 ={1860588125181794168951\over3216875861507134647600}\ne0,
\tag{9}
\]

\[
 [H_{42}H_{22}^{-1}H_{20}-H_{40}]_{00}
 =-{2234183456333136028\over714473894240060471595}\ne0,
\tag{10}
\]

with normalized residual rank `32`, and predictor residual

\[
 -{67663841820374976848\over41707488576114153187201}\ne0.
\tag{11}
\]

Positive entries or a positive Hermitian kernel therefore do not provide the
needed three-time gluing law.  The full Schur kernel in section 3 remains the
correct action object.

## 5. E8 Effects And O9 Operations Stay Distinct

The eight Block-194 effects obey

\[
 F_\alpha F_\beta=\delta_{\alpha\beta}F_\alpha,
 \qquad \sum_\alpha F_\alpha=I_{32},
 \qquad \operatorname{rank}F_\alpha=4.
\tag{12}
\]

They span the commutative effect algebra `E8`.  The corresponding Lueders
operations

\[
 \mathcal L_\alpha(X)=F_\alpha X F_\alpha
\tag{13}
\]

satisfy

\[
 \mathcal L_\alpha\mathcal L_\beta
 =\delta_{\alpha\beta}\mathcal L_\alpha,
 \qquad
 \Delta=\sum_\alpha\mathcal L_\alpha\ne\operatorname{id}.
\tag{14}
\]

The operation algebra

\[
 \mathsf O_9=\operatorname{span}\{
 \operatorname{id},\mathcal L_0,\ldots,\mathcal L_7\}
\tag{15}
\]

has exact dimension nine.  This is not the dimension of `E8`, and it is not a
64-control process frame.

## 6. Positive O9 Exterior Control

On `Fock=Lambda(C^32)`, define

\[
 \Gamma_+(K)=\Gamma(K)-P_{\rm vac}
 =\bigoplus_{n=1}^{32}\wedge^n K.
\tag{16}
\]

With the corrected column-vectorized doubled order, set

\[
 \widehat P_\alpha
 =\overline{\Gamma_+(F_\alpha)}\otimes\Gamma_+(F_\alpha).
\tag{17}
\]

Then

\[
 \iota\!\left(a\operatorname{id}+
 \sum_\alpha b_\alpha\mathcal L_\alpha\right)
 =aI+\sum_\alpha b_\alpha\widehat P_\alpha
\tag{18}
\]

is an injective unital star-algebra representation of `O9`.  The eight
selective images are pairwise orthogonal projectors, while

\[
 \iota(\Delta)=\sum_\alpha\widehat P_\alpha\ne I.
\tag{19}
\]

For a rank-four `F_alpha`,

\[
 \operatorname{rank}\Gamma(F_\alpha)=16,
 \quad \operatorname{rank}\Gamma_+(F_\alpha)=15,
 \quad \operatorname{rank}\widehat P_\alpha=225.
\tag{20}
\]

On bidegree `(1,1)`, equation (17) reduces to
`conjugate(F_alpha) tensor F_alpha`, with selective/dephasing/identity
Liouville ranks

\[
16,\qquad128,\qquad1024.
\tag{21}
\]

The naive construction without vacuum subtraction fails orthogonality:

\[
 \Gamma(F_\alpha)\Gamma(F_\beta)=P_{\rm vac}
 \quad(\alpha\ne\beta).
\tag{22}
\]

Its branch sum has vacuum eigenvalue eight.  Vacuum subtraction repairs the
`O9` multiplication law, not `E8` event completeness.

## 7. Exact Exterior Completeness Deficit

The PVM decomposes the one-particle space as

\[
 \mathbb C^{32}=\bigoplus_{\alpha=0}^7V_\alpha,
 \qquad\dim V_\alpha=4.
\tag{23}
\]

Exterior functoriality gives

\[
 \Lambda(\mathbb C^{32})
 \simeq\bigoplus_{n_0,\ldots,n_7}
 \bigotimes_{\alpha=0}^7\Lambda^{n_\alpha}V_\alpha.
\tag{24}
\]

`Gamma_+(F_alpha)` contains only nonvacuum wedges supported entirely inside
one `V_alpha`.  Hence

\[
 \operatorname{rank}\sum_\alpha\Gamma_+(F_\alpha)=8(2^4-1)=120,
\tag{25}
\]

whereas the full exterior dimension is `2^32`.  The omitted nonvacuum
mixed-label rank is

\[
 2^{32}-1-120=4294967175.
\tag{26}
\]

On the doubled exterior space, the branch sum has rank `8*225=1800`, while
identity has rank `2^64`.  These deficits are not numerical approximations.
They express a type mismatch: the exterior functor naturally records an
occupation tuple, not one categorical label.

## 8. Invariant-Vacuum Obstruction

Let the actual fixed-context reflection act on labels as

\[
 \rho=(0\ 7)(1\ 6)(2\ 5)(3\ 4).
\tag{27}
\]

Proper-cubic rotations co-transform the detector/event context; they are not
used as a transitive permutation of this fixed label set.

Suppose projectors `P_alpha` on the full exterior space satisfy:

1. pairwise orthogonal projectivity;
2. `sum_alpha P_alpha=I`;
3. extension of `F_alpha` on exterior degree one;
4. naturality under scalar one-particle automorphisms, hence exterior-degree
   preservation; and
5. reflection covariance
   `Gamma(R)P_alpha Gamma(R)*=P_(rho(alpha))`.

The vacuum line is one-dimensional and invariant.  Therefore

\[
 P_\alpha|0\rangle=q_\alpha|0\rangle,
 \qquad q_\alpha\in\{0,1\},
 \qquad\sum_\alpha q_\alpha=1.
\tag{28}
\]

Reflection covariance requires `q_alpha=q_(rho(alpha))`.  Every contribution
to the sum then occurs in a pair, so the sum is even.  This contradicts
equation (28).  The independent checker supplies both an exhaustive zero-count
certificate for the eight one-hot assignments and a Groebner unit ideal for
the polynomial constraints.

The same proof applies to the doubled vacuum when the candidate preserves
total exterior number or bidegree.  Diagonal Liouville phase covariance alone
is weaker: it need not isolate the doubled vacuum from every `(n,n)` sector.
The theorem does not apply to a map that mixes exterior degree, changes the
outcome algebra, restricts the physical support, or weakens projectivity to
POVM effects.

Two elementary repairs expose rather than remove the wall:

- assigning the vacuum to one label is projective and normalized but breaks
  reflection covariance;
- with `P_perp=I-sum_alpha Gamma_+(F_alpha)`, assigning
  `E_alpha=Gamma_+(F_alpha)+P_perp/8` is a positive, covariant, normalized
  full-complement POVM, but it has complement-sector idempotence residual
  `1/64-1/8=-7/64`.

## 9. What The Result Does And Does Not Fix

The positive results are reusable:

- exact `Q024/Q02` action kernels at all nine radii;
- correct separation of coarse-circle and full-L24 indices;
- a positive Hermitian action boundary form despite non-Hermiticity;
- exact rejection of pairwise `H`-kernel Markov promotion;
- a faithful mathematical `O9` exterior representation; and
- a precise complement-allocation target for future event constructions.

The physical insertion target does not pass.  Because T2 is load-bearing,
the runners correctly seal T3--T6.  In particular, this block does not compute
the triple-port probability and does not select the Block-199 `b` parameter.

The minimal axioms need no edit on this evidence.  Admissibility already says
that neighboring conditions determine a probability distribution over local
possibilities.  It deliberately does not specify the distribution's form or
values, a measurement context, or an action-to-event map.  Block 200 localizes
that downstream bridge; it does not prove that the bridge must be a fifth
axiom.

An explicit future complement allocation would have to supply objects such as

\[
 R_\alpha R_\beta=\delta_{\alpha\beta}R_\alpha,
 \quad \sum_\alpha R_\alpha
 =I-\sum_\alpha\Gamma_+(F_\alpha),
 \quad \Gamma(R)R_\alpha\Gamma(R)^\dagger=R_{\rho\alpha},
\tag{29}
\]

or explain why projectors on the full exterior space are the wrong physical
object.  Equation (28) proves that (29) cannot include the invariant vacuum
under the current categorical hypotheses.  A physical support restriction,
a reflection-fixed null outcome, a POVM, degree mixing, or a direct event
functional changes at least one hypothesis and remains live.

## 10. No-Go Discipline Gate

### N1 -- alternative-route enumeration

The broad statement “the action cannot produce histories” fails.  The narrow
statement concerns only full-support, number-preserving, exterior-natural,
projective `E8` extensions with the actual reflection covariance.

| family | object / mechanism / terminal obligation | result and honesty marker |
|---|---|---|
| naive exterior functor | `Gamma(F_alpha)`; preserve the exterior functor literally; require orthogonal exhaustive branches | `ATTEMPTED`: distinct branches share the rank-one vacuum and sum to vacuum eigenvalue eight, equations (22) and (28) |
| vacuum-reduced exterior functor | `Gamma_+(F_alpha)`; remove the shared vacuum; require an exhaustive `E8` partition | `ATTEMPTED`: orthogonality is repaired but rank is only 120 of `2^32`, equation (26) |
| categorical complement allocation | projective `R_alpha` on the omitted complement; require unitality and actual reflection covariance | `ATTEMPTED`: all eight one-hot vacuum allocations fail the four two-cycle reflection; the Groebner ideal is the unit ideal |
| covariant fractional completion | full-complement POVM `E_alpha=Gamma_+(F_alpha)+P_perp/8`; use symmetry and positivity; require projectivity for the frozen target | `ATTEMPTED`: normalization/covariance pass on vacuum and mixed sectors, but complement idempotence fails by `-7/64`; this succeeds only for a relaxed POVM target |
| fixed one-particle/filling support | restrict to exterior degree one, where the eight `F_alpha` are exhaustive; require a support/filling derived from the action | `ATTEMPTED`: algebra closes on the restricted sector, but the frozen target forbids importing that support and the action has not derived it |
| ninth complement outcome / O9 | keep `I-sum P_hat_alpha` as a reflection-fixed coherence/null branch; require the original eight-outcome `E8` target | `ATTEMPTED`: this succeeds exactly as the distinct `O9` operation representation, equations (18)--(21), and therefore demonstrates why it is not `E8` |

These are six materially different object/mechanism/obligation triples.  They
support the narrow theorem.  Direct Schur/Wick probabilities, non-number-
preserving Nambu symbols, OS/GNS reconstruction, a physical boundary, and a
Record decoder are untested alternatives and prevent a broad no-go.

### N2 -- wall-independence audit

The raw complement, vacuum, and label-allocation defects collapse into one
tested wall `W_I^ext`: a full-support categorical exterior insertion.  They
are not counted as separate TOE walls.

| pair | closing first closes second? | closing second closes first? | disposition |
|---|---|---|---|
| `W_I^ext` exterior insertion / `W_B` cyclic-to-causal boundary | no | no | independent |
| `W_I^ext` / triple-selector value | yes, only after lower-cylinder descent | no | selector is downstream, not independent |
| `W_B` / full causal process | only partly | no | process includes insertion and controls; not a third independent primitive wall |

The surviving independent wall set is the broader physical insertion wall
`W_I` and causal boundary wall `W_B`.  This block closes neither globally.

### N3 -- hidden-wall scan

- “Natural” is load-bearing and is defined here as exterior-functorial,
  number-preserving, and equivariant under scalar one-particle automorphisms;
  on the doubled space the theorem explicitly requires total-number or
  bidegree preservation.  Diagonal Liouville phase covariance alone is not
  silently promoted to that stronger condition.
- “Canonical” is not used as evidence.  The two canonical-looking lifts are
  explicitly tested controls.
- “Registered” refers only to the exact Block-194 PVM/M2 and `O9` domain.  It
  does not grant an action insertion, state, boundary, probability rule, or
  physical Fock interpretation.
- “By construction” statements are limited to algebraic definitions whose
  identities are independently recomputed.
- The `C^32` event fiber is an incoming/outgoing pairing; treating it as a
  single physical action or Fock fiber would be an extra condition and is not
  used.

No hidden condition is counted as a separately closed wall.

### N4 -- residual matching

| cited witness | witness residual | present residual | match / use |
|---|---|---|---|
| [Block 194 PVM/M2 note](ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) and runner | constructs eight rank-four effects, reflection map, and one-shot writer | supplies the exact input PVM, not an exterior-insertion obstruction | input authority only; not counted as a negative witness |
| [Block 195 prefix note](ADMISSIBILITY_D4_L24_PREFIX_INSTRUMENT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) and runner | tested direct restrictions, projected translations, and conditional channel completions | full-exterior categorical event insertion | no; dropped as proof of the present obstruction |
| [Block 198 even/odd note](ADMISSIBILITY_D4_L24_EVEN_ODD_TWO_STEP_OS_PARITY_HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) and runner | inherited reflected Berezin form is indefinite and fails a positive process reading | exterior vacuum/complement allocation | no; used only as a probability-use firewall |
| [Block 199 event-history note](ADMISSIBILITY_D4_L24_EVENT_HISTORY_INTERFACE_HANKEL_PROCESS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) and runner | pair data do not select a unique three-event law | action-to-event selection remains open | partial motivation only; not proof of equations (25)--(28) |
| Block 200 primary and no-import runners | exterior ranks, actual reflection cycles, one-hot enumeration, Groebner unit certificate | exact narrow theorem in sections 7--8 | yes; direct evidence |

No mismatched prior residual is used to enlarge the claim.

### N5 -- rhetoric and resolution audit

- `per_element:` checked all eight rank-four PVM effects, their multiplication,
  the naive exterior images, and vacuum-reduced `O9` images.
- `per_site:` checked the invariant vacuum, all eight projective vacuum
  completions, the four reflection two-cycles, and omitted mixed-label sectors.
- `per_mode:` checked all nine radii for Schur structure; the full `H`
  residual values are executed on the two D1 sectors `s=0,1` only.
- `per_block:` checked Schur, covariance, PVM/M2, `H`, operation typing,
  exterior representation, and categorical covariance as distinct blocks.
- `lattice_wide:` checked and not executed -- no full event intertwiner,
  512-cylinder law, causal process, response, Record/Born law, gravity result,
  axiom result, or TOE result is claimed.

Accordingly the phrase is “the tested exterior-natural categorical lift does
not close,” never “the action has no event law.”  Both cached runner outputs
must carry these five substantive resolution lines.

### N6 -- partial-closure and primitive scan

The current premise registry and
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) were checked.  `minimal_axioms` supplies the
existence of the local Admissibility distribution but no form, value,
measurement context, action/event map, or probability normalization rule.
The approved realized-state primitive supplies pointwise evaluation only and
explicitly supplies no probability rule, state, state selection, weighting,
or boundary.  The scale-reference and kinetic-isotropy primitives are
irrelevant to this insertion residual.

No approved primitive closes the tested bridge, but this is not written as
“a new axiom is required.”  Live partial-closure paths are a direct event
functional, an action-derived physical support, a covariant POVM, a ninth
null outcome, a non-number-preserving symbol algebra, or an OS/GNS/boundary
construction.  Renaming `O9` as `E8` would be a type error, not an import-
retirement convention.  No current open PR supplies the missing event map.

### N7 -- strongest steelman

A hostile reviewer can bypass the theorem's representation target entirely.
The action may define all 512 three-event probabilities directly as a positive
normalized Schur/Wick functional on event polynomials, without representing
the eight outcomes as projectors on the full exterior Fock space.  A covariant
POVM can likewise split the invariant vacuum, and an OS/GNS quotient can make
null exterior directions disappear before the event algebra is represented.
On the doubled space, a Nambu/Bogoliubov construction might also evade the
proof by failing total-number and bidegree preservation while retaining the
declared one-particle restriction.
The terminal obligation is explicit: derive one of those constructions from
the frozen action, reproduce every lower marginal without fitted
normalization, and compute the triple-port selector.  None is ruled out here.

This steelman defeats every broad action/history no-go.  It does not defeat
the narrow theorem because it changes the primary object or one of its stated
hypotheses.

### N8 -- cross-cycle echo

- Block 191 lacked one common temporal carrier;
  [Block 192](ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) retired that local
  obstruction by enlarging to the exact `L=24` carrier.  The analogous lesson
  here is to keep enlarged/non-number-preserving representations live rather
  than turning a family theorem into a global one.
- Block 193 lacked a detector orientation and pointer; Block 194 derived a
  unique ray within its family and an exact M2 dilation.  Missing event
  structure can therefore be a downstream theorem rather than an axiom edit;
  an action-derived support or decoder remains a valid target.
- Block 195 showed that a complete one-shot PVM does not select a repeated
  instrument or causal channel.  Its wall remains live; Block 200 does not
  recycle it as an exterior theorem.
- Block 198 showed that one inherited reflected Berezin family is indefinite.
  Block 200 avoids the prior overreach by keeping the positive Schur kernel,
  indefinite moment family, and event representation separate.
- Block 199 showed that identical complete one-/two-event tables permit
  different triples.  Its strongest steelman was an action-native insertion;
  Block 200 executes one normalized exterior family and leaves the direct
  functional alternative live.
- Earlier POVM/Gleason and projective-instrument notes close conditional
  representation theorems only after additivity, state, or instrument
  hypotheses.  They show a legitimate bounded-bridge path, not an
  axiom-native supplier of the missing action functional.

Similar walls have been retired elsewhere by adding an explicit bounded
bridge and later auditing its import.  That mechanism remains available here
and is included in the next-campaign portfolio.

**N1--N8 disposition:** `PASS` for the narrow exterior-natural categorical
obstruction.  `FAIL` for a broad action/history/axiom no-go, which is demoted
and not shipped.

## 11. Reproduction Summary

Primary baseline:

```text
[PASS] A
[PASS] T0
[PASS] T1
[PASS] T2
[PASS] S
TOTAL: PASS=5 FAIL=0
```

Primary mutation harness:

```text
baseline_exit=0; rejected=28; gate_matches=28; total=28; harness_failures=0
```

Independent baseline:

```text
TOTAL: PASS=19 FAIL=0
```

Independent mutation harness:

```text
TOTAL: PASS=18 FAIL=0
```

No review-loop was used.  Audit status remains unset and can be assigned only
by the independent audit lane.
