---
claim_id: admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_bounded_theorem_note_2026-08-25
claim_type: bounded_theorem
claim_scope: "For the frozen Block-77 raw-label D4 gauge symbol, the fifteen-row Regge vertex-displacement symbol, the full four-axis half-lattice grading u_mu^2=z_mu^-1, and C=diag(u_mu), Block 196 proves an exact placement-grade Ward obstruction before reflection, action, or response. The known C=I one-cell prefilter reproduces at rank(A)=rank([A|b])=798 in 800 unknowns, with the two freedoms fixed by spatial permutation covariance and the registered D1/H1 rank-ten minor. The physically typed target splits into four singleton-grade systems; each has rank 798 and augmented rank 799. Exactly 28 of 60 direction-grade blocks are inconsistent: every active mixed-edge grade fails, beginning with d=1100,g=0 at rank 40 versus augmented rank 41. More strongly, on that row the raw equations force the same regular Laurent entry M_01 to equal 1/2 along z_0=1 and zero along z_1=1, contradicting its common value at z_0=z_1=1. Thus no entrywise regular Laurent M of any finite support solves this frozen raw-symbol equation. This is not a no-go for centered-symbol diagrams, rational or nonlocal multipliers, a derived alternative placement complex or split carrier, other Regge formulations, OS/GNS/CAR reconstruction, process tensors, gravity, Records, the axioms, or the TOE."
parents:
  - admissibility_d4_l24_prefix_instrument_selection_boundary_bounded_theorem_note_2026-08-25
upstream_dependencies:
  - minimal_axioms
actual_current_surface_status: demotion
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: partial-attempt-with-named-untested-routes
hypothetical_axiom_status: unchanged
admitted_observation_status: none
target_claim_id: admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_2026-08-25
target_blocker_text: "The frozen raw-label D4 tensor gauge image cannot be mapped by an entrywise regular Laurent tensor-to-edge leg to the vertex-based Regge gauge image while preserving the physical half-lattice placement leg C=diag(u_mu)."
next_trace_action: "Pivot to the preregistered full OS/GNS/CAR history reconstruction; retain centered-symbol and alternative-placement carrier constructions as explicit live gravity routes."
claim_type_reason: "The exact rank census and universal corner contradiction are theorems for the displayed raw-symbol regular-Laurent contract. Standing is demoted because five materially distinct carrier or history constructions remain untested and the no-go-discipline gate fails N1 and N7."
audit_required_before_effective_retained: true
bare_retained_allowed: false
preregistration_commit: 3241d452c580f7a09597c3e40070ab95669507bd
parent_commit: 9bc5dfe2fc7b0bd1c7e5547f0ca621986e71f21d
carrier_census: 15_22_40_exact
raw_identity_prefilter: exact_rank_798_augmented_rank_798
full_placement_grading: exact
singleton_grade_systems: 4
singleton_grade_rank: 798
singleton_grade_augmented_rank: 799
inconsistent_direction_grade_blocks: 28
first_exact_witness: d_1100_grade_0_rank_40_augmented_rank_41
regular_laurent_corner_obstruction: exact_support_independent
independent_rank_reconstruction: exact_5_of_5
reflection_induction: sealed_after_ward_failure
action_riesz_response: sealed
heldouts: sealed
no_go_discipline_gate: FAIL
negative_disposition: partial-attempt-with-named-untested-routes
broad_regge_d4_no_go: not_claimed
broad_history_no_go: not_claimed
minimal_axiom_update: none
obligation_retirement: 0
toe_percentage_movement: 0
---

# Regge--D4 Full Half-Lattice Placement/Reflection Intertwiner Boundary

**Date:** 2026-08-25

**Campaign block:** 196

**Type:** `bounded_theorem`

**Standing:** proposed bounded theorem; independent audit unset

Primary runner:
[`admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_2026_08_25.py`](../scripts/admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_2026_08_25.py).

Independent checker:
[`admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_independent_check_2026_08_25.py`](../scripts/admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_independent_check_2026_08_25.py).

Cached stdout:
[`admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_2026_08_25.txt`](../logs/runner-cache/admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_2026_08_25.txt).

Independent cached stdout:
[`admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_independent_check_2026_08_25.txt`](../logs/runner-cache/admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_independent_check_2026_08_25.txt).

## 1. Result Up Front

The first physically typed Regge--D4 carrier attempt stops at its earliest
coefficientwise Ward gate.

The inexpensive raw-column-identity prefilter is real and exact.  On the
fifteen positive Regge edge rows its one-cell system has 800 coefficients,

\[
 \operatorname{rank}A=\operatorname{rank}[A|b]=798.
\]

Spatial permutation covariance fixes its two free coefficients to
`sqrt(2)/12`.  One common ten-row minor is exactly `i/1024` at D1 and
`-(sqrt(3)-i)/2048` at H1.  This remains useful algebra, but it identifies
link-centered D4 gauge columns directly with vertex-based Regge displacement
columns and is therefore not the physical chain.

The explicit placement leg changes the answer.  On the minimal group-closed
half-lattice extension

\[
 u_\mu^2=z_\mu^{-1},
 \qquad
 C=\operatorname{diag}(u_0,u_1,u_2,u_3),
\]

the target equation

\[
 M\Gamma_D=G_R C
\tag{1}
\]

splits into four singleton placement grades.  Every grade system has

\[
 \operatorname{rank}A_g=798,
 \qquad
 \operatorname{rank}[A_g|b_g]=799.
\tag{2}
\]

The affine solution set is empty.  This is not caused by the 22-edge
reflection completion, the 40-edge frame orbit, a rank-ten sample, an action
inverse, or a response: it occurs on one mixed base edge before any of them is
opened.

There is also a support-independent reason.  For `d=(1,1,0,0)` and grade
`g=0`, the same regular Laurent coefficient `M_01` is forced to equal
`1/2` on one coordinate hyperplane and zero on the other.  The two
hyperplanes meet at the all-one momentum point, so no entrywise regular
Laurent `M` of any finite support can satisfy (1) for this frozen raw
symbol and placement leg.

The result is a sharp route localization, not TOE progress by itself.
No axiom or obligation is retired and every TOE percentage remains unchanged.

## 2. Authority And Pre-Target Freeze

The runner binds:

- `origin/main` at `b11811704efa98a12272d572f666e530a807f6c1`;
- the Block-195 parent at
  `9bc5dfe2fc7b0bd1c7e5547f0ca621986e71f21d`;
- the complete pre-target registration at
  `3241d452c580f7a09597c3e40070ab95669507bd`; and
- the current [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

The registration froze the following before any target coefficient was read:

1. the fifteen Regge base directions, existing 22-edge reflection union, and
   one mechanically induced 40-edge proper-spatial carrier;
2. the Block-77 raw D4 symbol and component conversion
   `(3,0,1,2,6,8,9,4,5,7)`;
3. the full four-axis ring `u_mu^2=z_mu^-1` and
   `C=diag(u_mu)`;
4. exactly four singleton grades on every tensor slot, with row-face one-cell
   support, for 3200 coefficients;
5. no independently fitted 22/40 rows, no pseudoinverse, no response-selected
   normalization, and no post-result support or carrier repair; and
6. action, Riesz, D1/H1 response, and held-outs sealed until every carrier
   gate passed.

The first registration draft proposed only temporal doubling.  Before target
execution, two independent checks showed that it was not closed under spatial
half-turns.  A second typing check showed that a single placement coset for
`M` could not match the grade decomposition of the literal raw equation.
The panel accepted the symmetry-forced full grading and the four decoupled
singleton systems as pre-execution type repairs, then made that specification
the final freeze.

## 3. Exact Carrier And Known-Prefilter Controls

The edge authorities are the
[Kuhn/Coxeter Regge construction](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)
and the
[22-edge time-reflection completion](ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md).
The tensor/gauge authority is the
[raw incidence Fierz--Pauli carrier](ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md).

The exact carrier census is:

| stage | construction | row count | role |
|---|---|---:|---|
| base | nonzero `{0,1}^4` directions | 15 | coefficient solve |
| reflection | base plus its time-reflected labels and anchor translations | 22 | time-reflection control |
| full frame | all 24 proper-spatial images modulo edge reversal | 40 | proper-spatial closure |

For the 40-edge carrier, a reversed image is represented by its negative and
anchored at the unreversed image direction.  The corresponding Laurent phase
is retained.  Exact group composition holds for all 24 frames, and the
22-edge time reflection is an involution.

The runner then reconstructs the known `C=I` prefilter rather than importing
its numerals.  The row-face support is

\[
 \{s:0\leq s_\mu\leq d_\mu\}.
\]

Every row system is full column rank except `d=1111`, where the rank is
`158/160`.  Spatial `S_3` covariance fixes its two homogeneous freedoms.
The lexicographically first common nonzero ten-row minor uses zero-based rows

\[
 (0,1,2,3,4,5,7,8,9,11)
\]

and gives the exact D1/H1 values stated above.  This is a positive control for
the coefficient engine, not evidence that the physical placement equation
passes.

## 4. Why The Full Placement Grading Is Necessary

The [raw D4 carrier](ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md)
puts diagonal tensor components on vertices, off-diagonal components on face
centers, and gauge parameters on link centers.  Its physical-center-to-label
vector chart is

\[
 U_\xi=\operatorname{diag}(e^{iq_\mu/2}).
\]

Therefore the link-to-vertex gauge leg is

\[
 C=U_\xi^\dagger=\operatorname{diag}(u_\mu),
 \qquad u_\mu^2=z_\mu^{-1}.
\]

A single coarse Laurent cover already fails at temporal Nyquist: the raw-link
time-reflection representation becomes `I_4` while the vertex
representation is `diag(1,1,1,-1)`, forcing an equivariant leg to rank at
most three.  A temporal-only double cover also fails: at
`z_x=z_y=-1` the spatial half-turn raw-link representation is `I_4`
while the vertex representation is `diag(-1,-1,1,1)`, forcing rank at
most two.

The full four-axis grading repairs those representation defects.  Signed
frames permute or invert the `u_mu`, and
`u_mu^-1=z_mu u_mu` keeps the four singleton grades closed.  The formal
group laws, deck count 16, covariance of `C`, and unit determinant all pass.
The failure occurs one step later.

## 5. Grade Decomposition Of The Raw Ward Equation

Let

\[
 A=\mathbb K[z_0^{\pm1},z_1^{\pm1},z_2^{\pm1},z_3^{\pm1}],
\qquad
 R=\bigoplus_{\epsilon\in(\mathbb Z_2)^4}A\,u^\epsilon.
\]

The literal raw D4 gauge matrix and Regge displacement matrix are both
even-grade:

\[
 (\Gamma_D)_{aa,a}=2(1-z_a^{-1}),
\tag{3}
\]

\[
 (\Gamma_D)_{ab,a}=\sqrt2(z_b-1),
 \qquad
 (\Gamma_D)_{ab,b}=\sqrt2(z_a-1),
\tag{4}
\]

\[
 (G_R)_{d,a}={d_a\over\sqrt{d\cdot d}}(z^d-1).
\tag{5}
\]

Writing `M=sum_epsilon u^epsilon M_epsilon`, equation (1) separates
coefficientwise:

\[
 M_{e_a}\Gamma_D=G_R E_{aa},
 \qquad a=0,1,2,3,
\tag{6}
\]

and

\[
 M_\epsilon\Gamma_D=0
\]

for every other grade.  The registration therefore retained exactly the four
inhomogeneous singleton grades and excluded the twelve unforced homogeneous
grades.

The one-cell target is

\[
 M_{dA}
 =\sum_{g=0}^3 u_g\sum_{s\leq d}c_{dAgs}z^s.
\tag{7}
\]

It is four independent 800-variable Ward systems, with proper-spatial and
reflection covariance imposed across the four solutions simultaneously.

## 6. Exact Rank Census

After invertibly rescaling diagonal tensor unknowns by two, off-diagonal
unknowns by `sqrt(2)`, and the weight-`k` target by `sqrt(k)`, all
coefficient matrices are rational with entries in `{0,+1,-1}`.

For one direction `d` and one singleton grade `g`:

| `k=abs(d)` | variables | coefficient rows | rank | augmented rank |
|---:|---:|---:|---:|---:|
| 1 | 20 | 36 | 20 | 20 for every `g` |
| 2 | 40 | 64 | 40 | 41 if `d_g=1`, otherwise 40 |
| 3 | 80 | 112 | 80 | 81 if `d_g=1`, otherwise 80 |
| 4 | 160 | 192 | 158 | 159 for every `g` |

For each fixed grade:

- the pure axial row `d=e_g` passes uniquely;
- the seven directions containing `g` and at least one other axis fail;
- the seven inactive directions have the unique zero solution; and
- the assembled system has rank 798 and augmented rank 799.

Across all four grades, 28 of the 60 direction-grade blocks are inconsistent.
The first declared witness is

\[
 d=(1,1,0,0),\quad g=0,\qquad
 \operatorname{rank}A=40,\quad
 \operatorname{rank}[A|b]=41.
\tag{8}
\]

A separate checker that imports no primary-runner code independently rebuilds
all 60 rational systems.  It reproduces the seven weight/activity rank orbits,
the four `798/799` assembled systems, the 28 inconsistencies, an explicit left-
null witness for (8), and the Laurent-corner contradiction (`5/5` gates).

The four axial maps alone are not a Regge carrier: the eleven mixed edge
directions are load-bearing in the fifteen-row complex.  Consequently neither
normalization nor an induced 22/40 row can repair (8).

## 7. Support-Independent Regular-Laurent Corner Theorem

The obstruction is stronger than the registered one-cell count.

**Lemma.**  Keep the raw symbols (3)--(5), the ten tensor slots, and
`C=diag(u_mu)`.  No entrywise regular Laurent matrix `M`, at any finite
support, satisfies (1).

**Proof.**  It is enough to use row `d=(1,1,0,0)` and singleton grade
`g=0`.  Set `z_2=z_3=1`.  In gauge column zero, then set
`z_0=1`.  All terms except the `h_01` term vanish, so (3)--(6) give

\[
 \sqrt2(z_1-1)M_{01}(1,z_1)
 ={z_1-1\over\sqrt2}.
\]

As a Laurent-polynomial identity,

\[
 M_{01}(1,z_1)={1\over2}.
\tag{9}
\]

Gauge column one has zero target in grade `u_0`.  Setting `z_1=1` leaves

\[
 \sqrt2(z_0-1)M_{01}(z_0,1)=0,
\]

hence

\[
 M_{01}(z_0,1)=0.
\tag{10}
\]

A regular Laurent polynomial has a single value at the common point
`z_0=z_1=1`.  Equations (9) and (10) require that value to be both
`1/2` and zero, a contradiction.  The argument never refers to a support
radius.  QED.

The lemma does not apply to a rational multiplier with a pole on one of the
two hyperplanes, to a different centered-symbol diagram, to a non-diagonal or
independently derived placement leg, or to an enlarged tensor carrier that
splits the shared off-diagonal incidence.

## 8. Mechanism And Stop Rule

In plain language, a mixed Regge edge listens to two coordinate displacement
directions.  The ten-slot D4 tensor stores those two contributions in one
shared off-diagonal face component.  The physical placement leg puts the two
gauge directions on different half-grid grades.  The shared face component is
then asked to take one nonzero boundary value for the first grade and zero for
the second at the same corner.  It cannot do both while remaining a regular
local Laurent field.

This explains why the raw `C=I` algebra can pass while the physically typed
leg fails: `C=I` leaves the two gauge columns in the same grade, where the
off-diagonal component can cancel them jointly.  The half-lattice placement
separates precisely the cancellation the prefilter used.

The registered stop fires at T2.  Therefore the following were not executed:

- target 22-edge reflection gluing;
- target 40-edge induction and shared-row overlap;
- the 4096-point target faithfulness census;
- the Regge/D4 action quotient and Riesz dual;
- L24 source composition, D1/H1 response, TT response, and held-outs.

No favorable response was available to select or repair a coefficient.

## 9. No-Go Discipline Gate -- FAIL / Demotion

This section is load-bearing.  The exact raw-contract theorem can ship.  A
general Regge--D4, gravity, history, axiom, or TOE no-go cannot.  The current
origin-main No-Go Discipline gate is `FAIL` and the negative disposition is
`partial-attempt-with-named-untested-routes`.

### N1 -- normalized alternative-route enumeration: FAIL

The attempted family and five materially distinct live families differ in
primary object, mechanism, and terminal obligation.

| family | object and mechanism | terminal obligation | status |
|---|---|---|---|
| frozen raw regular-Laurent chain | ten-slot raw D4 symbol, `C=diag(u)`, regular Laurent `M` | exact Ward chain before reflection/action | ATTEMPTED; closed by (8)--(10) |
| centered-symbol carrier | centered D4 and edge-centered Regge symbols, then conjugate the complete diagram | exact chain, 22/40 covariance, rank ten, and raw-label descent | UNTESTED -- N1 FAIL |
| rational or nonlocal carrier | fraction-field, quasilocal, or nonlocal Fourier multiplier | pole cancellation or admissible domain, quotient regularity, and physical descent | UNTESTED -- N1 FAIL |
| alternative placement complex | derived non-diagonal `C`, split incidence carrier, different cover, or justified quotient | derive rather than fit placement, then prove group closure, faithfulness, and action compatibility | UNTESTED -- N1 FAIL |
| full OS/GNS/CAR reconstruction | positive-time algebra, null quotient, and CAR/GNS representation | identify the L24 event fiber and obtain an action-selected contraction/CPTP history law | UNTESTED -- N1 FAIL |
| global process tensor | positive multi-time Choi comb with causal normalization | identify frozen PVM/source marginals and prove action-selected uniqueness | UNTESTED -- N1 FAIL |

N1 therefore fails for every broad negative.

### N2 -- collapsed wall audit: PASS after collapse

Support size, other singleton grades, 22/40 gluing, rank census,
normalization, action quotient, Riesz dual, and response are not independent
failures.  The first necessary raw-symbol equation stops them.

The broad open set collapses to:

- `W_C`: a different physical carrier formulation remains untested;
- `W_N`: rational, quasilocal, and nonlocal operator classes remain untested;
- `W_H`: a carrier-independent selected history law remains untested.

| pair | first closes second? | reverse? | independent? |
|---|---|---|---|
| `W_C` / `W_N` | no | no | yes |
| `W_C` / `W_H` | no | no | yes |
| `W_N` / `W_H` | no | no | yes |

The rank contradiction is one frozen-contract obstruction, not three
independent TOE walls.

### N3 -- hidden-condition scan: PASS with qualifiers

The required phrases and close variants were scanned.

| phrase or use | classification |
|---|---|
| `physical-center chart` | Block-77 coordinate authority; it does not establish unique physical selection |
| `minimal group-closed` | minimal only inside the chosen half-lattice grading, not among all complexes or quotients |
| `frozen`, `only allowed`, `preregistered` | procedural anti-fit conditions; they supply no physics |
| `regular Laurent` | load-bearing mathematical domain and retained in every negative headline |
| `support-independent` | licensed only by the universal corner proof in Section 7 |
| `canonical edge representative` | label convention with an exact anchor phase; downstream of the T2 failure |
| `naturally`, `obviously`, `standard QFT` | no load-bearing hit |

Calling this chart or `C` physically necessary outside the frozen target
would fail N3.

### N4 -- residual matching: PASS

| cited authority | actual residual | use here |
|---|---|---|
| [Regge second variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) | fifteen edge directions and vertex-displacement gauge map | exact positive input only |
| [22-edge reflection completion](ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | reflection carrier and anchor translations | exact input/control; not negative evidence |
| [raw incidence carrier](ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md) | raw/centered placement equations and D4 gauge symbol | exact input and centered-symbol escape |
| [common-action source basis](ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md) | ten-slot ordering and downstream source/action | ordering only; action and response remain sealed |
| [Block 195](ADMISSIBILITY_D4_L24_PREFIX_INSTRUMENT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md) | three history-channel extractions fail to select a channel | route-ranking parent only; different residual |

The Block-196 runner carries the entire new rank and corner proof.  No prior
negative is borrowed as evidence for it.

### N5 -- resolution and rhetoric audit: PASS

The primary runner prints these same five substantive lines, so they land in
its cached stdout:

per_element: checked the frozen d=1100, grade-g=0 necessary Ward coefficient block; exact rank is 40 and augmented rank is 41.

per_site: checked and not executed -- no centered-symbol, changed-placement, quotient, or independently derived alternative site stencil is constructed.

per_mode: checked and not executed -- the obstruction is coefficientwise; no rational/nonlocal class or complete 4096-point torus census is executed.

per_block: checked only the frozen raw-symbol regular-Laurent chain equation; 22/40 gluing, action quotient, Riesz selection, and response stop downstream.

lattice_wide: checked and not executed -- no universal Regge-D4 bridge, OS/GNS/CAR reconstruction, process tensor, gravity law, or TOE closure is tested.

The allowed negative is: “No regular Laurent `M` solves the frozen raw-symbol
chain equation.”  The note does not say that no Regge--D4 intertwiner, local
carrier, gravity law, OS/CAR reconstruction, or TOE exists.

### N6 -- partial closure, convention, and axiom scan: PASS

| live path | present evidence | terminal test |
|---|---|---|
| centered-symbol diagram | the known `C=I` coefficient map is exact but physically untyped in raw labels | construct all tensor, gauge, and edge chart legs together; prove descent |
| rational/nonlocal map | generic fraction-field left inverses are not excluded by the corner | control poles, quotient domains, reflection, and physical locality |
| alternative placement/split carrier | the contradiction uses one shared off-diagonal tensor slot and diagonal `C` | derive an enlarged or different carrier from the action and prove its source map |
| OS/GNS/CAR | Block 195 leaves full reconstruction live | build a reflection-positive functional, exact descended translations, and a unique CPTP comb |
| global process tensor | not tested by a one-step chain equation | construct positive causal Choi marginals and action-selected uniqueness |

These paths do not currently require an axiom amendment.  The
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select a source/action,
physical observable, placement complex, transfer law, or history channel.
The present contradiction is mathematical inside one candidate contract, not
evidence that a new axiom is necessary.

### N7 -- strongest hostile steelman: FAIL for a broad negative

> A hostile reviewer should reject any claim that this closes the physical
> carrier.  Block 77 explicitly distinguishes centered tensor/gauge symbols
> from their raw-label representatives through placement conjugations, and
> the current calculation freezes only one raw-label diagram with diagonal
> `C`.  The actionable counterroute is to construct the complete centered
> Regge--D4 chain, conjugate tensor, gauge, and edge legs together, and test
> its 22/40 covariance and base-torus descent.  If a regular conjugation still
> fails, a rational or quasilocal multiplier can evade the corner provided
> its poles cancel on the physical quotient.  A derived split incidence
> carrier could also give the two incident gauge grades separate tensor slots.
> None of those mechanisms has been tested, and OS/CAR or a positive process
> tensor bypasses this diagram entirely.

The steelman is concrete and terminally testable, so N7 forces demotion.

### N8 -- cross-cycle echo: PASS

The repository contains several direct cautions against universalizing a
carrier-local obstruction:

- the [Block-118 Floquet wall](ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-16.md)
  left a half-space reflection-intertwiner route open, and
  [Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md)
  constructed the positive completion;
- Block 191's missing common temporal carrier was repaired by the
  [Block-192 L24 construction](ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md);
- the Block-98 scalar Laurent alias wall was not generalized to a changed
  calculus, and the
  [Dirac--Kahler Hodge construction](ADMISSIBILITY_DIRAC_KAHLER_COCHAIN_HODGE_QUADRATIC_WARD_SHELL_LOCALITY_OS_REENTRY_BOUNDED_THEOREM_NOTE_2026-08-14.md)
  later canceled its complete alias family on a different carrier; and
- Block 196 itself retired the single-cover and temporal-only representation
  defects before execution by using the full group-closed grading.

The same lesson applies here: the exact corner theorem stands, while changed
formulations remain live.

### Gate disposition

| gate | result |
|---|---|
| N1 | FAIL -- five normalized live families |
| N2 | PASS after dependency collapse |
| N3 | PASS only at frozen raw regular-Laurent scope |
| N4 | PASS; prior negatives are not used as proof |
| N5 | PASS; source text and primary-runner stdout both carry the certificate |
| N6 | PASS; constructive paths remain and no axiom pressure follows |
| N7 | FAIL; the centered-symbol steelman is actionable |
| N8 | PASS; multiple carrier/reconstruction retirements were found |
| overall | FAIL; demote to `partial-attempt-with-named-untested-routes` |

## 10. TOE And Axiom Disposition

The result is significant route progress but not lane completion:

| lane | previous working score | Block-196 movement | reason |
|---|---:|---:|---|
| Records | 95 / 92 / 50 | 0 | no formation, persistence, or autonomous write |
| causal time | 76 / 72 / 41 | 0 | no selected transfer or Lorentzian update |
| matter | 95 / 96 / 75 | 0 | existing D4 source/action preserved, not extended |
| gravity/source | 70 / 45 / 29 | 0 | leading raw local bridge is closed, no positive replacement constructed |
| Born/history | 84 / 63 / 34 | 0 | OS/CAR/process reconstruction remains unexecuted |

The triples retain the campaign's established meanings: derivation readiness,
validation confidence, and retained/end-to-end closure.  They are not
probabilities.

No line of the minimal axioms should be changed on this evidence.  The result
does not prove that gravity needs a new axiom; it proves that one frozen
ten-slot raw-label finite-Laurent chain is algebraically impossible.  The
next campaign follows the preregistered pivot to full OS/GNS/CAR history
reconstruction, while the centered/split-carrier routes remain explicit
gravity opportunities for the separate gravity lane.

## 11. Reproduction

Run:

```bash
python3 scripts/admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_2026_08_25.py
python3 scripts/admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_independent_check_2026_08_25.py
```

Expected terminal lines include:

```text
[PASS] T2: the frozen placement-aware Ward target is exactly inconsistent before any induction
WITNESS: d=1100 grade=0 rank=40 augmented_rank=41
CORNER: regular-Laurent M_01 has M_01(1,z1)=1/2 and M_01(z0,1)=0
TOTAL: PASS=11 FAIL=0
TOTAL: PASS=5 FAIL=0
```

The successful runner exit means that the bounded theorem and all stop rules
were reproduced.  It does not mean the attempted intertwiner passed.
