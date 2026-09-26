---
claim_id: cube_formation_matter_flux_dynamics_and_strong_electric_limit_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: Supplied compensated common integer-rotor formation law on the eight-vertex cube; exact finite coordinate closure after the first formation mark, matter and loop-flux motion, full second-birth evolution, and an explicit fixed-time strong-electric approximation uniform over the actual first waiting time. No physical identification is asserted.
upstream_dependencies:
- local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
- local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/cube_formation_matter_flux_dynamics_2026_09_26.py
---

# Matter and loop-flux dynamics after formation on the cube

Type: bounded_theorem
Status: proposed_retained

## Claim and supplied inputs

For the supplied common formation generator on the simple eight-vertex cube,
the first mark of the zero-field state generates a finite invariant coordinate
sector of the zero-electric-cost no-jump dynamics; this sector supports matter
and loop-flux motion and a second birth, and its full evolution approximates
the original common law at fixed magnetic time as the electric/magnetic ratio
tends to infinity, uniformly over the actual first waiting time.

This is conditional mathematics of the explicitly supplied model below.
The scientific question it advances is how an actually formed matter state
and its field evolve together in one parameter regime. The framework's
selection of this dynamics, a macroscopic limit, and an experimental
preparation/readout map are further research questions. No experimental data
are fitted or compared here. The cube, initial state, positive parameters
K, delta and kappa, and either of the two stated instruments are supplied.
The diagnostic kappa/delta=1 is chosen before evaluating the response.
Model time has no assigned conversion to seconds. The bounded electric
observable below is an explicitly chosen model probe.

The two linked inputs specify a common limit of the full compensated fast
formation law. Their model imports remain imports: tensor hard-core charged
matter, oriented integer rotors, vacancy-gated compensation, a chosen hopping
law and a chosen resolved or coherent formation instrument. In their notation,
the full microscopic Hamiltonian is
H_(epsilon,S)=delta epsilon^-4 [W+epsilon T_S+epsilon^2 C_S],
the original jumps are sqrt(kappa) epsilon^-1 j_(edge,S), and
 epsilon^2 S(S+1)=delta/K. The compensation bracket retains its vacancy gates.
We work with the resulting common generator as specified next. Our strong-K
limit is subsequent to that common limit; simultaneous microscopic,
strong-electric and volume error bounds are not claimed.

## Exact model

Vertices are binary integers 0,...,7, adjacent when their XOR is 1, 2 or 4.
A=(0,3,5,6), B=(1,2,4,7), with every edge oriented A to B. The edge order is
(01,02,04,31,32,37,51,54,57,62,64,67).
A basis word is (q,E), q_v in {0,+1,-1}, E in Z^12,
with every A occupied and div E=q-1_A. There are no tensor exchange signs.
The reference Omega has q_A=+1, q_B=0 and E=0.

F_a moves q_a to any empty adjacent b, empties a and replaces E_ab by E_ab-q_a.
Its adjoint reverses the move. The birth j_(ab,sigma), sigma=+/-1, acts only
when both endpoints are empty: it sets q_a=sigma, q_b=-sigma and adds sigma
to E_ab. Write B_(ab,sigma)=P j_(ab,sigma) F_a P, where P requires every A
occupied. The two instruments are the 24 separate B_(ab,sigma), or the 12
unnormalized edge sums B_(ab,+)+B_(ab,-). Different edges remain different
channels. No later births are discarded.

Every unordered pair of distinct A vertices overlaps on this cube. Define

    H4 = -2 sum_{a<c} (F_c F_a P)^* (F_c F_a P),
    D(q,E) = sum_{a->b : q_b=0} E_ab(E_ab-q_a),
    Gamma = sum_mu B_mu^* B_mu,
    h = K D + delta H4.

The resolved and coherent Gamma agree because the newborn signs give
orthogonal output ranges on each edge. Recycling maps are kept instrument
specific. The full common GKLS law has jumps sqrt(kappa) B_mu.
All formulas preserve the integer Gauss law. Since each integer summand of D
is a nonnegative even integer, D>=0 and D>=2 on the complement of its kernel.

Set u=delta t, R=K/delta, r=kappa/delta, and let P0 project onto ker D
within the six-particle sector. Write H0=P0 H4 P0, G0=P0 Gamma P0.
The proposed finite no-jump generator is A0=-iH0-rG0/2.

## Exact finite construction and formation outputs

The runner starts from all nonzero coordinates of B_mu Omega. It repeatedly
applies the full integer primitive paths of H4 and Gamma, retaining a target
only when D=0. An empty queue establishes coordinate closure. A resource
ceiling exits with failure; there is no field cutoff. Independently built
two-hole output incidences S give H4=-2 S^T S and second-birth incidences J
give Gamma=J^T J. The complete matrices agree after indexing by full (q,E).

The first 24 resolved marks have squared norm 2; each coherent mark has
squared norm 4. Their union contains 36 basis words. The closed sector C
contains 252 coordinates, 36 matter words, and |E_e|<=1. It is invariant
under H0 and G0. H0 has diagonal -14 and 2232 directed off-diagonal entries;
every one changes matter and electric field. This is a coordinate support,
not a claim about the minimal Hilbert cyclic span of a fixed generator.
The checker finds [H0,G0] nonzero, so replacing the loss by a scalar during
this dynamics would change the evolution.

The finite field bound also has a direct proof. Start with a D=0 word whose
fields have magnitude at most one. On an edge ending at a vacancy,
E_ab is 0 or q_a. An outward move makes it -q_a or 0. The two destinations
in F_c F_a must be distinct vacancies. The adjoint moves only remove B
particles. Edges ending at B sites still occupied in the final word have
received no adjoint move, so retain magnitude at most one. Edges at finally
vacant sites satisfy the final D=0 condition, giving the same bound.
For B_mu^* B_mu, the birth and its adjoint cancel at the marked edge, leaving
one outward and one inward move; the same argument applies. Opposite-sign
cross terms vanish in the coherent loss. This proves invariance of the finite
box under the projected operators without positing a rotor cutoff. The
exhausted coordinate search then selects C inside that box.

Applying the original second birth from C produces 816 distinct fully occupied
basis words, with maximum |E_e|=2. Every such word has D=0, F_a=0 and B_mu=0.
Consequently these outputs remain fixed. If J_mu denotes the full map from C
to their span T, the exact projected trace-one state from rho supported on C is

    rho_6(u) = exp(u A0) rho exp(u A0^*),
    rho_T(u) = r sum_mu integral_0^u J_mu rho_6(s) J_mu^* ds.

The identity sum J_mu^* J_mu=G0 preserves total trace. The coherent and
resolved terminal states can differ, even though their loss agrees.
Full occupancy ends births on this cube; larger graphs have further sectors.

## Matter and field witnesses

The runner gives an exact three-step H0 path whose endpoints have the same
q and different integer fields, with divergence-free difference supported on
one square face. Each path amplitude is -2, and the corresponding H0^3
matrix element is -8. Thus the projected dynamics includes a closed matter
rearrangement that changes loop flux. The explicit words are printed for
inspection; the statement concerns the cube with its actual colored matter.

For a fixed face, define its oriented cycle vector
z=(0,1,-1,0,0,0,0,0,0,-1,1,0), and the diagonal bounded observable
O(q,E)=sin[(pi/2) z.E], evaluated exactly as 0,1,0,-1 modulo four.
It commutes with D. Apply the supplied impulse exp(-i eta O) immediately after
the first mark and read the full-state expectation of O at u, including T.
Let chi(u) be its derivative at eta=0. For normalized first mark (0,1,+),
chi'(0)=-24; for (0,1,-), it is 0; for the coherent edge mark it is -12.
These statements concern the normalized first outputs of Omega.

Indeed chi(u)=i Tr(rho [O, exp(u L0^*)O]). Its initial Hamiltonian slope is
sum_ij v_i H0_ij (O_i-O_j)^2 v_j/(v^T v).
The dissipative contribution vanishes here: O, all J_mu, G0 and the initial
vectors are real, and the dissipative adjoint of O is real symmetric, so its
commutator with O has zero expectation in a real vector. This argument holds
for every r>=0. Exact charge/occupancy unitary curvatures are also printed,
with the dissipator explicitly excluded from those curvature quantities.

At the supplied ratio r=1, numerical propagation of the full formula gives,
for the plus first mark at u=0.1, survival approximately 0.4463500032 and
chi approximately -0.4918027555. DOP853 propagation is cross-checked against
a direct matrix exponential for the no-jump vector. These are numerical
diagnostics of the exactly specified finite generator, not rigorous
floating-point error enclosures or measured excitation frequencies.

## Uniform strong-electric replacement, with the second birth

The exact target of this proof is the trace-distance bound below for the
full six-plus-eight-particle common process from an actual first mark,
uniformly over its waiting time, for fixed r,u and sufficiently large R.
The obligation chain is: bounded primitive operators; the D gap; no-jump
compression; exact terminal recycling; and actual-first-mark preparation.
All five estimates are proved here. The finite matrices establish the
specific motion witness separately. No additional closure hypothesis is
used for the infinite integer-rotor six-particle space.

On that full space ||F_a||<=3, hence ||H4||<=2*6*3^4=972.
A fixed B_(ab,sigma) has only two allowed outward destinations, so ||B||<=2
and ||Gamma||<=24*4=96. The coherent loss is the same operator. Put

    b=972+48r,    2R>b,
    v_R(u)=min{1, b u, b(2+b u)/(2R-b)},
    e_R(u)=min{2, (1+b u) v_R(u)},
    C_R(u)=min{1, (1+96 r u)e_R(u)}.

Let A=-iH4-r Gamma/2 and G_R=-iRD+A. Both G_R and its P0/Q compressions
generate contraction semigroups, since their Hermitian parts are negative.
D is self-adjoint on its diagonal domain and A is bounded, so the usual
bounded-perturbation construction applies. On Q=1-P0, D_Q>=2 and a Neumann
series around -i R D_Q gives ||(QG_RQ)^-1||<=1/(2R-b).

For a unit vector initially in P0, write x=P0 exp(uG_R)psi,
y=Q exp(uG_R)psi. Then x'=P0 A exp(uG_R)psi, so ||x'||<=b, and

    y(u)=integral_0^u exp((u-s)QG_RQ) QAP0 x(s) ds.

Integration by parts using the bounded inverse gives
||y(u)||<=b(2+b u)/(2R-b). Direct integration and contraction give b u and 1.
Duhamel's formula for x-exp(uP0AP0)psi gives at most b u v_R(u), since
v_R is nondecreasing. Therefore the full no-jump vector error is at most
e_R(u). These estimates are uniform over all unit vectors in P0.

For subnormalized pure density matrices the corresponding trace-norm error
is at most 2 e_R(u). The recycling map M(X)=sum B_mu X B_mu^* obeys
||M(X)||_1<=96 ||X||_1 for Hermitian trace-class X, by positivity and
||Gamma||<=96. Every eight-particle output is stationary, even when the
six-particle input has nonzero D and arbitrary integer fields. Integration
therefore bounds the terminal trace-norm difference by 192 r u e_R(u).
The trace distance of the complete trace-one state is at most C_R(u).
Convexity extends this to mixed initial states in P0. For states supported
on C the compressed dynamics is exactly the finite formula above.

## Actual first waiting time and bounded readouts

In the four-particle sector q_A=+1, q_B=0 and div E=0. Thus D=sum E_e^2.
Its unique zero-cost vector is Omega, and its next possible value is at
least 4: every nonzero divergence-free integer flow contains a cycle, and
the cube has girth four. Direct primitive expansion gives
H4=-84 I+V, where V=-2 sum over the six faces (U_face+U_face^*) and
||V||<=24, with <Omega,V Omega>=0. Energy conservation under RD+V then gives
R <D> <=24 and probability outside Omega at most 6/R, at every waiting time.

On this whole sector Gamma=48 I. Each resolved B has B^*B=2I, and each
coherent edge sum has B^*B=4I. Hence the first waiting time has rate 48r in
u units, and the normalized conditional first-mark maps are isometries.
For either original instrument and every finite first waiting time, the
actual normalized postmark state lies within trace distance
p_R=sqrt(min{1,6/R}) of its stated first output of Omega. Complete positivity
and trace preservation propagate this preparation error through all later
births. Combining the estimates gives

    dist(rho_actual(u), rho_finite(u)) <= min{1, p_R+C_R(u)}.

Here u is time since the first mark, and the bound is uniform in the waiting
time before that mark. If r=0 the comparison theorem for a supplied initial
state still holds, but there is no actual first event. We assume r>0 when
conditioning on that event. This is a fixed-cube, fixed-r, fixed-u statement;
the loose constants are not a quantitative moderate-R simulation guarantee.

For ||O||<=1, expectations differ by at most twice that distance.
The same controlled limit applies to the impulse response above: its initial
Hermitian perturbation is X=-i[O,rho], with ||X||_1<=2. Its positive and
negative parts have trace at most one and stay supported in P0 for an ideal
first output. Applying the uniform state bound to these two parts bounds
the response error from dynamics by 4 C_R(u). The preparation contribution
is at most 4 p_R by the commutator trace-norm inequality. Thus
|chi_actual(u)-chi_finite(u)|<=4 min{1,p_R+C_R(u)}.
This controls the derivative directly; no interchange of a derivative and
an unquantified limiting statement is used.

## Status, dependencies and verification

The proof uses finite-graph integer flows, elementary operator norm bounds,
a contraction-semigroup Duhamel estimate, and trace-class positivity. Those
mathematical steps are shown above. The common model is a supplied input;
its derivation from the microscopic compensated law is the parent dependency,
not independently re-proved here. Both parent texts were byte-identical at
main e37967e326c2bdb429bd3106d34158bd5420e9c0 to those used for the probe.
The strongest further obligation for observational use is a controlled
macroscopic state/observable/dynamics construction with a specified physical
preparation and readout. This note establishes the finite conditional bridge
stated above and leaves that further question open.

An independent reconstruction used simultaneous two-hole incidences and
birth-output incidences without reading the primary code or its expected
sector size. It found the same integer matrices and terminal coordinates.
The publication runner carries both implementations so their equality is
reproducible. A separate independent review reconstructed the full-space error
bound, the uniform actual-first-event preparation estimate and the impulse
normalization, and found no blocking mathematical defect in that scope.
Its local primitive check was written before reading the publication runner,
with the claimed target numbers disclosed. Its finite-time response check
shared the integer matrices but used a block matrix exponential and centered
finite differences of the actual impulse, corroborating the sign, normalization
and terminal contribution through different numerical machinery. This is
source-readiness evidence; the common-limit parent theorem and physical
identification were outside that independent reconstruction.

## Review record

The independent incidence reconstruction was frozen before the primary
implementation or its expected sector dimension was disclosed. Publication
packaging only moved that implementation into a callable helper and removed
its file-output wrapper. The later proof reviewer checked the final scientific
argument and the two implementation paths. No scientific correction was
requested. Scratch mutations to the hopping Gauss sign, magnetic coefficient,
coordinate closure, terminal recycling, propagation and incidence multiplicity
all caused the checks to fail. The coherent and resolved recycling distinction
and the fixed-cube, fixed-time limit remain explicit. These author and review
checks supply no formal audit status.

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Explicit finite supplied-model theorem with exact integer reconstruction and a proved strong-electric error bound.
audit_required_before_effective_retained: true
bare_retained_allowed: false
trace_class: frontier_discovery
target_claim_id: cube_formation_matter_flux_dynamics_and_strong_electric_limit_bounded_theorem_note_2026-09-26
target_blocker_text: Compute common matter and field response after actual formation in a shared controlled regime.
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: Conditional finite theorem and reproducible exact plus numerical runner.
next_trace_action: Test whether this populated matter-field dynamics has a controlled extension to larger cyclic graphs and a specified macroscopic observable.
```

## Reproduction and actual scientific inputs

Run `python3 scripts/cube_formation_matter_flux_dynamics_2026_09_26.py`.
Its integer reconstruction is exhaustive for the declared coordinate component.
Numerical propagation uses NumPy/SciPy. The cache is produced through
`scripts/runner_cache.py`; it binds the runner and both declared parent notes.
The runner performs no external scientific data reads. The declared parent
texts supply the model definitions; the cache reads them for byte binding.

- [Common compensated formation generator](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Local pair form of the magnetic dynamics](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md).
