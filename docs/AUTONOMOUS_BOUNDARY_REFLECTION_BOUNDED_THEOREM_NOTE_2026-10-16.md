---
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: product_source_controlled_stop_bounded_theorem_note_2026-10-16
target_blocker_text: "Mathematical target: replace its externally scheduled stop by an explicit time-independent controller/plant Hamiltonian and independently specified ready state."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Complete wrapper review, canonical execution and publication conformance for the qualified conditional apparatus; retain native three-body boundary supply and incoming-packet preparation as open physical obligations."
conditional_surface_status: "Supplied literal old K, positive three-qubit boundary block, exact isolated bulk clock and independently prepared one-head incoming packet; infinite blank tail for every later time, with finite readiness and finite-apparatus horizons stated separately."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A complete-output reflection theorem for a fixed old-pair operation under explicit apparatus and preparation conditions, with quantitative finite-resource variants."
source_science_acceptance_complete: true
wrapper_root_approval: separately_recorded
canonical_execution: separately_recorded
publication: separate_from_source_acceptance
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Autonomous boundary reflection with a supplied positive boundary

Claim type: `bounded_theorem`. Source-status request: `proposed_retained`.
The actual source surface is `conditional-support`; no independent retained
audit is supplied. Root accepted the exact two mathematical sources below for
conditional provisional reuse, under the complete
[source qualification](../outputs/autonomous_boundary_reflection_2026_10_16_inputs/root/QUALIFICATION.md).
The [source decision](../outputs/autonomous_boundary_reflection_2026_10_16_inputs/root/SOURCE_ACCEPTANCE.json)
does not approve this new wrapper or certify canonical execution, publication
or physical hardware. Their actual outcomes are separately recorded in the
[publication review history](../.claude/science/physics-loops/toe-autonomous-boundary-reflection-20261016/REVIEW_HISTORY.md)
and [canonical execution record](../.claude/science/physics-loops/toe-autonomous-boundary-reflection-20261016/CANONICAL_EXECUTION.json).

**Primary runner:** `scripts/autonomous_boundary_reflection_2026_10_16.py`.
The root-owned [primary](../scripts/autonomous_boundary_reflection_2026_10_16.py)
directly imports the separately assembled
[check module](../scripts/autonomous_boundary_reflection_check_2026_10_16.py).
The [result](../outputs/autonomous_boundary_reflection_2026_10_16.json) and
[canonical cache](../logs/runner-cache/autonomous_boundary_reflection_2026_10_16.txt)
are execution evidence only when their actual run and freshness are recorded.
This wrapper does not predeclare a successful run. The
[input artifact manifest](../outputs/autonomous_boundary_reflection_2026_10_16_inputs/ARTIFACT_MANIFEST.json)
binds the root-owned historical evidence; the companion
[source manifest](../.claude/science/physics-loops/toe-autonomous-boundary-reflection-20261016/SOURCE_MANIFEST.json)
binds the unchanged embedded mathematical bodies.

## Conditional result and its resource boundaries

This is an alternative apparatus for PR9657's fixed target operation. It does
not autonomize that result's four-qubit mediator, its ramps or its source
preparation. The literal old Hamiltonian is `K=2I+Z1 Z2` and the target is
`W=((9+12i)I+(-16+12i)X1 X2)/25`. On a one-head half-line clock, supply
the Hamiltonian in equation (1), with a positive boundary block
`w n_0 (I-X1 X2)/2`. The independently prepared incoming packet is identical
for every old input. No externally timed intervention occurs during its
subsequent evolution.

Under equation (20), for every actual elapsed time `t>=2T`, the complete
ready-input isometry has error at most `epsilon` from
`exp(-2i theta) exp(-itK) W` tensored with the stated normalized outgoing clock,
where `theta=atan(4/3)`. Equation (19) retains both the full scalar and the
actual old aging. Arbitrary passive references and all old/clock outputs
remain in the comparison. The unhalved trace norm bound is twice the isometry
bound, capped at two. A possible bound-state component of the actual ready
state is controlled by the initial norm comparison; it is not assumed absent.

| Resource regime | Supplied apparatus and readiness | Complete isometry error and time domain |
|---|---|---|
| Infinite-tail theorem | Exact normalized incoming packet, one-head clock, infinite blank tail, stated boundary-strength tolerance | `epsilon` for every `t>=2T`, equations (19)-(20) |
| Explicit finite readiness | Same infinite apparatus, packet truncated by (A3); an implemented preparation may have a separately certified error `eta_a` | `epsilon+eta_p+eta_a` for every `t>=2T`; finite input support does not remove the tail |
| Finite apparatus | Clock length `M` obeying (A5), positive far-end correction, the same finite-support input and optional preparation error | `epsilon+eta_p+eta_a+zeta` only for `2T<=t<=Tobs`, with the stated isometric embedding |

The fixed dyadic choice `J=3/16, w=1/4` has nominal maximum added incident
load `13/16` at the boundary clock site, interior clock load `3/4`, and added
old-site load `1/4`. The unchanged literal old block has norm three and is
accounted separately. In the permitted boundary-strength interval the maximum
added boundary-clock load is `7/8` and the added old load is at most `5/16`.
The boundary is a single positive three-qubit block on a connected triple of
diameter two; no two-body synthesis or unspecified gadget is supplied.
The one-head total modeled energy lies in `[1,4]` at nominal coefficients.
That sector enclosure does not bound total fabrication, preparation, cooling
or infinite-lattice cost. The all-future apparatus is infinite even when the
initial packet has finite support. Accuracy increases the incoming preparation
scale and waiting time; the sufficient bound is `T=O(J^-1 epsilon^-3)`.

The static-fault result covers only the declared boundary coefficient.
Old-field errors, bulk disorder, general noise and extra heads are outside it.
Exact capture, apparatus reset, indefinite reuse, Record formation,
microscopic control supply and physical energy identification remain open.
The theorem is persistent approximate completion with an escaping clock in
the free-old interaction picture. It does not supply a stationary complete
state or an autonomous realization of the original mediator.

## Imports, provenance and open bridges

The source base is `c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc`. Process authority
is the supplied current-main revision
`5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2`; its workflow, delivery and conformance
sources are identified in the companion source manifest. No editable prompt,
physical axiom or primitive registry is changed by this proposal.

| Input | Role | Provenance | Open bridge or boundary |
|---|---|---|---|
| Literal K and exact W | Fixed mathematical target | PR9657 head above; target note SHA256 `b25d812dc1a4cdad2959f003ddd36346f2de0058292c74c7d0e07c9c5e395a4d` | Target provenance only; the mediator theorem is not a load-bearing construction import |
| Ordinary Fourier/Parseval identities and bounded selfadjoint evolution | Mathematical tools | Stated and used explicitly in sections 2-4 of the unchanged candidate | Their hypotheses are checked there; no spectral completeness excluding bound states is assumed |
| Bessel contour estimate for the finite horizon | Load-bearing mathematical import | Section 5 of the [native half-line clock note](NATIVE_HALFLINE_CLOCK_COMPLETION_FINITE_HORIZONS_AND_PERMANENCE_BOUNDED_THEOREM_NOTE_2026-09-14.md), SHA256 `87d8c6f4b98563cd827f0d8264ec2575c689ec4d7ac018fe5b87d89006181ed3` | Imported with the actual spectral enclosure in (A4); no claim of new general half-line machinery |
| Positive clock hopping, connected three-qubit boundary and blank sites | Installed conditional Hamiltonian | Explicit equations (1) and (21), not derived from PR9657 controls | Native physical supplier remains open; the provisional boundary is load-bearing |
| Incoming packet independent of old/reference input | Supplied readiness | Equations (5), (13) and (A3) | Finite coefficient integrals and support bound are specified; a native preparation procedure and its resource price remain open |
| Infinite tail or a chosen finite horizon | Apparatus extent | Candidate section 6 and addendum section 2 | Infinite blank sites are required by the stated all-future construction; finite `M` gives only its stated horizon |

Scattering gates and the outgoing half-line permanence strategy are prior
machinery, acknowledged in the unchanged source. This proposal claims the
specified conditional construction and estimates, with no global novelty
claim. The earlier seven-stage two-rail route and the separate two-body
numerical fit are not premises of this result.

## Proof-obligation graph

| Obligation | Disposition in the supplied source | Dependency and limit |
|---|---|---|
| Boundary equation, reflection orientation and phase | Derived in candidate section 1, equations (2)-(3) | Direct substitution in the declared half-line matrix; the full scalar is retained |
| Escape bounds and exact normalized scattering solution | Derived in sections 2-3, equations (4)-(14) | Integration by parts, Parseval and exact bounded evolution; the entire physical ready state is compared |
| Complete output, reference stability and static tolerance | Derived in section 4, equations (15)-(20) | Sector orthogonality and the preceding norm bounds; all future times under the stated conditions |
| Positive full-qubit extension and incident loads | Derived in section 5, equation (21) | Finite-excitation representation, supplied boundary block, no two-body compiler |
| Explicit finite support and preparation error | Derived in addendum section 1, equations (A1)-(A3) | Norm truncation and unitary propagation; `eta_p` and `eta_a` are additional budgets |
| Finite apparatus through `Tobs` | Derived in addendum section 2, equations (A4)-(A6), using the cited contour bound | Polynomial support propagation and actual spectral radius; finite-to-infinite embedding is explicit |
| Native boundary supply, incoming-packet preparation, reset and reuse | Open physical obligations | They are conditions or excluded conclusions, not lemmas declared discharged by the mathematical proof |

Root's exact source acceptance is qualified by the evidence and limits below.
This proof graph does not convert author acceptance into an independent
retained audit.

## Review record and unchanged source bodies

The [source acceptance record](../outputs/autonomous_boundary_reflection_2026_10_16_inputs/root/SOURCE_ACCEPTANCE.json)
has SHA256 `5f0653431bf3ea5965221da4c2e9a0da873c29e1cebabc2e12574b9601be1de4`;
its controlling qualification has SHA256
`e9324bc0b3e9a811860b0a993343fa908cb78c8089f99750f5bfb4efe7078fe4`.
Root read both complete mathematical arguments, the complete
[focused checker report](../outputs/autonomous_boundary_reflection_2026_10_16_inputs/independent_check/REVIEW.md)
(SHA256 `6f54fcfe020972e4154be2f0ee59e9205155e3a80249186faac22bcdd91396df`),
and the actual diagnostic sources and selected numerical evidence. The
checker separately reconstructed boundary/bound-state, normalization, tail
and finite-path arguments and independently assembled finite Jacobi evolution
without reading the root numerical diagnostic. It shared the supplied source,
target, assumptions and model. This is source-exposed same-model analytical
and implementation checking, not blind discovery, model diversity, formal
verification, formal audit or laboratory evidence. Finite diagnostics cannot
prove the infinite-volume or every-later-time statement. Large sufficient
schedules were evaluated arithmetically; those large states were not evolved.

V2 corrects the support quantifier identified in review and changes no
numerical calculation. The historical author run used V1; the preserved
[author diagnostic](../outputs/autonomous_boundary_reflection_2026_10_16_inputs/author/diagnostic.py)
and its [execution record](../outputs/autonomous_boundary_reflection_2026_10_16_inputs/author/execution/EXECUTION.json)
must not be relabeled as a V2 execution. Both original implementations,
results and receipts remain in the root evidence pack. Canonical adaptation,
mutations, execution and final wrapper conformance have their actual status
in the companion review history and canonical execution record.

The following two bodies are unchanged in full, including their historical
provisional and pending-review language. This new wrapper and the records
above provide later metadata outside them. Their exact bytes, offsets and
hashes are recorded in the companion source manifest. A source revision must
receive a new identity and the affected review; changing a body while retaining
its old pin is not permitted.

| Frozen body | Bytes | SHA256 |
|---|---:|---|
| [CANDIDATE_V2.md](../outputs/autonomous_boundary_reflection_2026_10_16_inputs/frozen_sources/CANDIDATE_V2.md) | 13239 | `694484853b731991d97f11f5d9a3a012ff30b9badb7fe57a7c57f6fee7e2fd36` |
| [FINITE_READINESS_ADDENDUM.md](../outputs/autonomous_boundary_reflection_2026_10_16_inputs/frozen_sources/FINITE_READINESS_ADDENDUM.md) | 4856 | `ce01691b49abf924d2fc610cf2dd6c71c565c0c21df6f1bc39960ecb2c546a2f` |


<!-- BEGIN UNCHANGED SOURCE: CANDIDATE_V2.md; SHA256=694484853b731991d97f11f5d9a3a012ff30b9badb7fe57a7c57f6fee7e2fd36 -->
# Static boundary reflection for the fixed old-pair gate

Provisional root derivation, 2026-10-16. Not independently checked, retained,
or a native hardware result. This is an alternative conditional apparatus for
the target of PR9657, not an autonomous implementation of its four-qubit
mediator or its prescribed ramps. Those two source qubits may be retained as
uncoupled |00> spectators if that output register is desired.

## Target, sources and added premises

Keep the literal old pair K=2I+Z1 Z2 and the target

    W=((9+12i)I+(-16+12i)X1 X2)/25
      =exp(i theta) exp(i theta X1 X2), theta=atan(4/3).

Both W and X1 X2 commute with K. The exact source is PR9657 head
c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc, with note SHA
b25d812dc1a4cdad2959f003ddd36346f2de0058292c74c7d0e07c9c5e395a4d.
The existing native half-line clock note at that head, SHA
87d8c6f4b98563cd827f0d8264ec2575c689ec4d7ac018fe5b87d89006181ed3,
already supplies the general outgoing-tail strategy, positive one-hot clock
extension and finite-horizon versus infinite-apparatus distinction. This
proposal does not claim those ideas as new. Scattering gates are also prior
literature: Childs, arXiv:0806.1972, sections I-II (background mechanism, no
theorem from that paper is required below).

New conditional resources are a half-line of clock qubits, one independently
prepared incoming one-head packet, positive clock hopping, and one positive
three-qubit boundary block. That three-body block has not been derived from
the two-body controls of PR9657. It has fixed support, rather than a sequence
of supplied target-unitary hopping bonds. Infinite blank sites remain an
infinite resource. A finite approximation has a finite horizon only.

## 1. Hamiltonian and conditional boundary scattering

On the one-head clock space l2(N0), let J>0 and

    h0=2J I-J sum(n>=0)(|n+1><n|+|n><n+1|),
    Pminus=(I-X1 X2)/2, Pplus=I-Pminus,
    H=K tensor I + I tensor h0 + w Pminus tensor |0><0|.       (1)

Nominally w=4J/3. Permit the explicit fault family J<=w<=5J/3;
there are no other faults in this theorem. K remains literally present with
its original coefficients. K commutes with all added terms. There is no
externally timed intervention during evolution.

In the Pplus old sector the clock is h0. In Pminus it is hw=h0+w|0><0|.
Put E(k)=2J(1-cos k), 0<k<pi. Direct substitution at n=0 and in the bulk gives

    phi_w(k,n)=(exp(-ikn)+r_w(k)exp(ikn))/sqrt(2pi),
    r_w(k)=-(w+J exp(ik))/(w+J exp(-ik)).                       (2)

These are bounded generalized eigenfunctions with energy E(k). In particular
r_0(k)=-exp(2ik). For real w, |r_w(k)|=1 on this open band. At k0=pi/2,

    r_0(k0)=1,
    r_(4J/3)(k0)=(-7-24i)/25=exp(-2i theta),
    R=Pplus+exp(-2i theta)Pminus=exp(-2i theta)W.               (3)

The scalar exp(-2i theta) is retained in the full isometry comparison.
Replacing the incident momentum by its opposite or silently conjugating the
reflection coefficient changes the operation.

For w>J there is also a bound state, proportional to (-J/w)^n, with energy
2J+w+J^2/w above the band. It is not omitted by assuming the physical input
has zero overlap with it: the initial comparison below bounds the complete
physical input's deviation from an exact continuum solution, hence also its
bound-state component. No completeness assertion excluding a bound state is
used.

## 2. Packet and an elementary uniform escape estimate

Take 0<sigma<=pi/6, k0=pi/2, and

    f(k)=sqrt(15)/(4 sqrt(sigma)) [1-((k-k0)/sigma)^2]
         for |k-k0|<=sigma, and zero elsewhere.

It is continuous, absolutely continuous on its support with zero endpoint
values, and L2-normalized. Its exact norms are

    F0=||f||_1=sqrt(15 sigma)/3,
    F1=||f'||_1=sqrt(15)/(2 sqrt(sigma)).                       (4)

For real s define clock vectors on n>=0 by

    a_s(n)=(2pi)^(-1/2) integral f(k) exp(-ikn-iE(k)s) dk,
    b_s^w(n)=(2pi)^(-1/2) integral f(k)r_w(k)exp(ikn-iE(k)s) dk,
    psi_s^w=a_s+b_s^w.                                       (5)

For any absolutely continuous g supported in [k0-sigma,k0+sigma], a subset
of [pi/3,2pi/3], and vanishing at those support endpoints, either
nonstationary phase kn+E(k)t or its negative has derivative magnitude at
least n+v t, where v=sqrt(3)J. Integration by parts gives, for t>0,

    |(2pi)^(-1/2) integral g(k)exp(i[kn+E(k)t]) dk|
      <= [||g'||_1+(2J/v)||g||_1]/[sqrt(2pi)(n+v t)].          (6)

Indeed |E''|<=2J and t/(n+vt)<=1/v; no monotonicity of E'' is needed.
For vt>=1, sum(n>=0)(n+vt)^(-2)<=1/(vt)^2+1/(vt)<=2/(vt).
Consequently the norm of this vector on n>=0 is at most

    [||g'||_1+(2/sqrt(3))||g||_1]/sqrt(pi v t).                (7)

This estimate holds for every t satisfying vt>=1, not only an asymptotic
sequence or time average.

For w in [J,5J/3] and k in [pi/3,2pi/3], the denominator
D=w^2+J^2+2wJ cos k is at least J^2. Differentiation of (2) gives

    |r_w'(k)|=2J |J+w cos k|/D <=11/3.                       (8)

For w=0 the derivative magnitude is2 and satisfies the same upper bound.
Define

    CA=F1+(2/sqrt(3))F0,
    CB=F1+(11/3+2/sqrt(3))F0.                                (9)

Then for every s,T with vs,vT>=1,

    ||a_s||<=CA/sqrt(pi v s),
    ||b_-T^w||<=CB/sqrt(pi v T),                              (10)

uniformly over the nominal plus sector w=0 and the admitted minus-sector
range [J,5J/3]. The norm in (10) is the entire half-line clock norm.

## 3. Normalization and exact dynamics without a spectral-completeness import

The synthesis map in (5) is bounded from L2 on the band to l2(N0), by
restriction of the two full-integer Fourier maps. E(k) is bounded. Thus
psi_s^w is norm differentiable and the directly checked eigenfunction
identity implies i d_s psi_s^w=hw psi_s^w. Since hw is bounded selfadjoint,

    psi_s^w=exp[-i(s-r)hw]psi_r^w.                            (11)

Its norm is constant. On the full integer line, Parseval gives ||a_-T||=1.
The part with n<0 tends to zero as T tends to infinity: write n=-m, m>=1,
and use (6)-(7) on phase mk+E(k)T. Therefore ||a_-T|| on n>=0 tends to1.
Equation (10) gives ||b_-T^w|| tending to0. It follows that

    ||psi_s^w||=1 for every real s.                           (12)

This argument establishes the needed normalized solutions without asserting
that their continuum span contains every physical clock state.

Fix T with vT>=1 and define the same ready clock for both old sectors,

    A_T=||a_-T||, chi=a_-T/A_T.                               (13)

Whenever CB/sqrt(pi vT)<1, A_T>=1-CB/sqrt(pi vT)>0 by (12).
The initial joint product state chi is independent of the old input. From
the reverse triangle inequality and (12),

    ||chi-psi_-T^w||<=2||b_-T^w||.                            (14)

The state on the left is the actually prepared input, including any bound
state overlap. Both compared vectors evolve under the same hw; this error
does not accumulate with elapsed time.

## 4. Complete output for every later time and static coefficient error

Let q_w(k)=r_w(k)/r_0(k). By (8), |q_w'(k)|<=17/3 throughout the band.
At fixed k, differentiation in w yields

    |partial_w r_w(k)|=2J sin k/D<=2/J                       (15)

for w in [J,5J/3]. Therefore, writing delta_w=w-4J/3,

    sup_band |q_w(k)-exp(-2i theta)|
       <=(17/3)sigma+2|delta_w|/J=:Delta.                    (16)

The w=0 sector is exactly q_0=1. Parseval followed by half-line restriction
shows ||b_s^w-exp(-2i theta)b_s^0||<=Delta. For s>=T, set

    B_s=||b_s^0||, beta_s=b_s^0/B_s.                          (17)

If CA/sqrt(pi vT)<1, then B_s>=1-||a_s||>0. Its scalar normalization is
positive real; beta_s retains the entire Fourier phase exp[-iE(k)s] and
reflection phase r_0(k). The reverse triangle inequality with (12) gives
|B_s-1|<=||a_s||. Combining (10), (14), (16) and (17),

    ||exp[-i(T+s)hw]chi-exp(-2i theta)beta_s||
      <=2CB/sqrt(pi vT)+2CA/sqrt(pi vs)+Delta                (18)

in the minus sector. In the plus sector replace the target scalar by1;
the same right hand side bounds it. Orthogonality of Pplus and Pminus now
gives the operator norm bound on the complete ready-input isometry,

    || exp[-itH](I_old tensor |chi>)
       - exp(-2i theta) exp(-itK)W tensor |beta_(t-T)> ||
       <= 2(CA+CB)/sqrt(pi vT)+(17/3)sigma+2|delta_w|/J,       (19)
    for every t>=2T.

Tensoring an arbitrary passive reference leaves this bound unchanged. For
any joint old/reference density, the trace norm error of the complete old,
clock and reference output is at most twice the right hand side, capped at2.
No subsystem is discarded. Uncoupled |00> source spectators can be tensored
onto both sides with zero change. This is persistent approximate completion
in the free-old interaction picture, with an escaping clock. It is not a
stationary total state, exact capture, selected Record, or apparatus reset.

An explicit sufficient choice for isometry error epsilon, 0<epsilon<=1, is

    sigma=3epsilon/68,
    |delta_w|<=J epsilon/8,
    T>=max{1/v, 16(CA+CB)^2/(pi v epsilon^2)}.               (20)

Then the three terms in (19) are at most epsilon/2, epsilon/4 and
epsilon/4. This also ensures the strict positive normalization conditions
above; each of CA/sqrt(pi vT), CB/sqrt(pi vT) is at most epsilon/4.
The band condition holds since sigma<=3/68<pi/6. The admitted fault lies
in [J,5J/3]. Nominal w needs no finite coefficient approximation when J is
chosen below. The packet width and incoming travel time still grow with
accuracy: CA+CB=O(epsilon^(-1/2)), hence T=O(J^(-1)epsilon^(-3)).
The coefficient tolerance in (20) is independent of how late t is read.
This conclusion is restricted to this one static boundary-strength fault,
not arbitrary clock disorder, old-K error, multi-head leakage or noise.

## 5. Positive qubit realization and actual local costs

For clock qubits c_n, write a_n=|0><1|_n and n_n=a_n^dagger a_n. Install

    H_clock=J n_0 + sum(n>=0) J[n_n+n_(n+1)
                               -a_(n+1)^dagger a_n-a_n^dagger a_(n+1)],
    H_boundary=w n_0 Pminus.                                (21)

Each hopping bond is positive, has norm2J, and has two-clock-qubit support.
The boundary term is positive with normw and support c_0, old1, old2.
Number is conserved. On the one-head sector (21) gives exactly (1).
On each finite-number sector H_clock is bounded by4J N; the orthogonal
direct sum of those bounded positive selfadjoint restrictions defines a
nonnegative selfadjoint operator. Adding bounded positive H_boundary and
bounded positive K preserves selfadjointness and nonnegativity. This is the
vacuum finite-excitation representation, not an infinite-density thermal
representation. The input is one-head; arbitrary clock input is not covered.

Each interior clock site has incident-block load4J. Clock0 has3J+w.
Each old site has added loadw, in addition to the unchanged literal K block
of norm3. A chain old1-old2-clock0-clock1-... embeds the support in Z3;
the boundary is a connected triple of diameter2, not an ordinary nearest-
neighbor two-body interaction. No unspecified gadget is included.

For the nominal dyadic choice J=3/16, w=1/4, the largest added load is
13/16 at clock0; old added load is1/4 and interior clock load3/4. The
boundary block is (I-Zc0)(I-X1 X2)/16. It is a single positive three-qubit
block, not four separately positive Pauli summands. All coefficients are
fixed dyadic values, independent of the desired accuracy. Under the admitted
fault range the boundary-site load remains<=7/8 and old added load<=5/16.
These added-load bounds do not include the old norm3 in an artificial cap1.

In the one-head sector, 0<=h_clock<=4J and 0<=H_boundary<=w, so
1<=H<=3+4J+w. For the nominal dyadic choice this is [1,4]. Static total
mean energy and variance are conserved; K is separately conserved. Clock
free energy and boundary energy need not separately be conserved. This
bounded modeled excitation energy does not price preparation, fabrication,
cooling, an infinite blank lattice or a physical identification of energy.

## 6. Readiness, limits and next checks

The ready vector (13) has infinite support but is a normal one-head state.
For every rho>0 it can be replaced by a normalized finite-support vector
within rho in norm. Exact unitary propagation then adds at most rho to
(19), uniformly for every later time. This existence statement is simply
density of finite-support vectors; it does not yet provide a finite
preparation algorithm or an explicit truncation size. Infinite blank tail
sites are still needed for the all-future construction. A fixed finite chain
can reflect the outgoing packet and is not covered by (19) at unbounded time.

The next independent checks must verify the incoming/outgoing convention,
the half-line boundary equation, normalization argument including the bound
state, full-output phase and old aging, tail constants and fault uniformity,
and the full-qubit positivity/load statement. A numerical finite-chain
experiment can falsify wrong formulas and test finite wavepackets; it cannot
certify the all-future or infinite-volume theorem. Strict two-body boundary
hardware, native incoming-packet preparation, arbitrary noise, finite reuse
and physical energy/Record identifications remain open.

<!-- END UNCHANGED SOURCE: CANDIDATE_V2.md -->


<!-- BEGIN UNCHANGED SOURCE: FINITE_READINESS_ADDENDUM.md; SHA256=ce01691b49abf924d2fc610cf2dd6c71c565c0c21df6f1bc39960ecb2c546a2f -->
# Explicit finite readiness and finite-apparatus horizons

Provisional root extension of CANDIDATE_V2.md. Not yet independently checked.
This derives quantitative replacements for the density statement in section6;
it does not change the infinite-tail theorem or turn a finite clock into a
permanent halt device. All symbols use the candidate's conventions.

## 1. Finite-support ready packet

Use (20), so A_T=||a_-T||>=3/4, and choose 0<eta_p<=1/2. For n>2JT the
phase -kn+E(k)T has derivative magnitude at least n-2JT. Integrating by
parts with the same compact support as the candidate gives

    |a_-T(n)| <= [F1/(n-2JT)+2JT F0/(n-2JT)^2]/sqrt(2pi).

Let N be an integer and d=N-2JT>=max(1,2JT). Then for every n>=N the
second term is bounded by F0/(n-2JT). Summing the squares gives

    ||1_(n>=N) a_-T|| <= (F1+F0)/sqrt(pi d).                 (A1)

For any nonzero vector a with ||a||=A and a nonzero orthogonal truncation P a,

    ||a/A-Pa/||Pa|||| <=2||(I-P)a||/A.                       (A2)

The normalization is positive real, preserving phase. By A_T>=3/4, the
right side here is at most4||(I-P)a||. Therefore it is sufficient to take

    N=ceil[2JT+max{1,2JT,16(F1+F0)^2/(pi eta_p^2)}],
    chi_N=1_(0<=n<N) a_-T / ||1_(0<=n<N) a_-T||.             (A3)

This guarantees ||chi_N-chi||<=eta_p. The discarded norm is at mosteta_p/4,
so the truncated vector is nonzero. Because the physical dynamics is unitary,
the infinite-clock theorem with this finite-support independent ready state
has isometry error at mostepsilon+eta_p for every t>=2T. Trace error is at
most2(epsilon+eta_p), capped at2. No clock/source part is discarded.

Equation(A3) supplies an explicit finite vector through ordinary one-dimensional
integrals; those integrals are computable but are not asserted to be exactly
emitted coefficients of a finite machine. A separately certified prepared
vector within eta_a of chi_N costs at mosteta_a uniformly in later time.
The input support size is O(JT+1/(sigma eta_p^2)); under(20) it is
O(epsilon^-3+epsilon^-1 eta_p^-2). This is a resource upper bound, not an
optimized preparation cost or a native packet-preparation theorem.

## 2. Finite chain through a stated physical observation horizon

For M>=N use clock sites0,...,M-1 and add the positive far-end term J n_(M-1)
to (21), preserving the constant2J diagonal in its one-head matrix. Let
h_w,M be the resulting finite one-head operator with the same boundary w.
Its spectrum and the infinite spectrum lie in[0,4J+w], hence both lie in
[0,17J/3] for w=0 or J<=w<=5J/3. Set c=Rho=17J/6 and

    A_infinity=(h_w-cI)/Rho, A_M=(h_w,M-cI)/Rho.

Both are selfadjoint contractions. For any input supported on0,...,N-1,
degree k<d_M=M-N+1 polynomials in these operators give identical vectors
after embedding the finite chain: a path of that degree cannot reach the
first removed site M. This includes the boundary potential and the diagonal
shift, which do not propagate support.

Use the Jacobi-Anger/Chebyshev expansion

    exp(-ixA)=J0(x)I+2 sum(k>=1)(-i)^k Jk(x) Tk(A).

The common scalar exp(-ict) is retained. Since ||Tk(A)||<=1, subtracting the
two evolutions gives

    ||exp(-ith_w)chi_N-embed exp(-ith_w,M)chi_N||
       <=4 sum(k>=d_M)|Jk(Rho t)|
       <=4 exp[-mu d_M+Rho t sinh(mu)]/[1-exp(-mu)], mu>0.    (A4)

The last bound follows by shifting the Bessel generating-function contour;
equivalently it is the same contour inequality proved in section5 of the
existing native half-line clock note, with the actual spectral radius here.
It is uniform on0<=t<=Tobs after replacing t by Tobs. It is not a claim that
individual Bessel absolute values are monotone in time.

Given zeta>0 and Tobs>=2T, choose

    M>=N, and M-N+1 >=
      [Rho Tobs sinh(mu)+log(4/((1-exp(-mu))zeta))]/mu.       (A5)

Then on the complete old/clock/reference output, for every2T<=t<=Tobs,

    isometry error <=epsilon+eta_p+zeta,
    trace norm error <=min(2,2(epsilon+eta_p+zeta)).          (A6)

For a prepared-vector error eta_a add it separately. The old K evolution
commutes with this comparison and uses actual elapsed t throughout. The
finite and infinite clock spaces are compared by the natural isometric
embedding; the target beta_(t-T) remains the stated normalized half-line
vector. This is an operational distance with an explicit embedding, not a
claim that the finite apparatus literally contains omitted output sites.

At fixed mu, the sufficient finite clock size is linear in J Tobs plus N
and log(1/zeta). The added far-end load is3J; other local loads are unchanged.
The whole finite-qubit clock operator norm grows with M, while the prepared
one-head energy bound remains fixed. Finite M has a stated horizon only;
later returns to the entrance are outside(A6). Infinite blank tail, supplied
three-body boundary hardware and readiness remain explicit resources.

<!-- END UNCHANGED SOURCE: FINITE_READINESS_ADDENDUM.md -->
