---
claim_id: finite_range_canonical_tensor_mixed_constraint_boundary_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: No regular finite-support canonical tensor jet with the supplied staggered linear generators, proper cubic covariance, generically invertible transverse-traceless kinetic symbol and nonzero affine scalar-lapse moment satisfies the specified off-shell mixed constraint identity at momentum degree two. Arbitrary finite kinetic pairing, lapse centering, cubic momentum generators and the declared regular constraint mixing are included. Changed carriers, degenerate symbols, weaker identities and infrared limits are outside this result.
runner: scripts/finite_range_canonical_tensor_mixed_constraint_2026_09_30.py
---

**Type:** bounded_theorem
**Status:** proposed_retained

# A finite-range canonical tensor seed fails its next mixed constraint equation

The supplied flat-strain lapse bracket does not extend to the stated next
mixed lapse/shift equation, even after allowing every finite-range quadratic
momentum pairing with the same nondegenerate long-wavelength tensor form.
The obstruction is a two-component matrix identity: it would require the
logarithmic derivative of a finite Laurent polynomial to have a nonzero
constant coefficient. No sampled momentum rank or restricted-radius search
is used to infer this quantified conclusion.

This is a theorem about an explicitly supplied canonical comparator. It does
not establish an inconsistency of the minimal axioms or exclude other lattice
gravity constructions. Exact enlarged gauge and clock constructions below
make some of the changed-premise alternatives concrete.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "higher strain orders of a nonlinear constraint are absent"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Construct an explicitly changed-carrier or controlled infrared completion with its actual matter and clock source."
conditional_surface_status: exact necessary mixed-bracket obstruction within the stated supplied canonical class
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: The theorem is conditional on the supplied continuous canonical carrier and exact mixed identity; it neither derives physical gravity nor excludes changed carriers or infrared symmetry.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Definitions, conventions and hypotheses

The model definitions come from the
[staggered curvature comparator](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md)
and its [flat-strain lapse calculation](ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
We assume their displayed canonical tensor carrier and stencils as mathematical
inputs; their wider physical or status claims are not hypotheses of this proof.
All needed definitions are restated here.

There are six independent real pairs with

    {h_A(x),P_B(y)} = delta_AB delta_xy.

Diagonal components live at vertices; h_ij,P_ij for i<j live at ij-face centers.
The full symmetric matrix momentum has off-diagonal entry P_ij/2, not P_ij.
Set the spacing to one. Put D_i^+f(x)=f(x+e_i)-f(x),
D_i^-f(x)=f(x)-f(x-e_i), and Delta_i=D_i^-D_i^+.
The linear curvature functional R1[N] is specified by

    dR1[N]/dh_jj = -sum_(i!=j) Delta_i N,
    dR1[N]/dh_ij = 2(N00-N10-N01+N11).

It has no constant term. Let C1[N]=-K R1[N], and let

    G1[X] = sum_j P_jj 2D_j^- X_j
             + sum_(i<j) P_ij (D_i^+X_j+D_j^+X_i).

Thus {h,G1} is the positive displayed strain relabelling. For the supplied
DeWitt kinetic density, canonical antisymmetrization gives the seed bond field

    F0_j(N,M) = K/(4alpha) (N_x M_(x+e_j)-M_x N_(x+e_j)).

This sign is opposite to computing the positive spatial potential +K R1 with
the same canonical bracket and generator. The present proof freezes C1=-K R1
and positive G1; it does not silently inherit the other sign. It does not use
F0, K/alpha matching, or the lapse-lapse seed identity as a theorem premise.

The original kinetic density at beta=-alpha is

    T2[N] = sum_x N [sum_j P_jj^2-(sum_j P_jj)^2/2]/(4alpha)
                 + sum_(ij faces) A[N] P_ij^2/(8alpha).

The normalized face family A[N]=a(N00+N11)+(1/2-a)(N10+N01) has the same
leading antisymmetric bracket for every real a. Nonnegative weights restrict
a to [0,1/2]; proper quarter rotations fix the scalar-covariant choice a=1/4.
Here the theorem allows a much larger kinetic class: any real finite-support
translation-covariant quadratic momentum density, linear in N, whose axial
TT uniform-lapse symbol F is generically invertible. The supplied continuum
normalization F(1)=I_2/(4alpha), alpha!=0, implies this condition. Individual
finite-momentum zeros are permitted. No uniform positivity of F is assumed.

The complete theorem hypotheses are:

| Hypothesis | Exact content and role |
|---|---|
| Canonical carrier and background | The six pairs above, expanded at h=P=0, with no additional canonical species or independent constraints |
| Regular field expansion | C=C1+C2+C3+..., G=G1+G2+G3+..., with no constant terms; degree is total h,P degree |
| Time reversal | h is even, P odd; C is even and G odd. Thus G2 is hP, C2 has hh and PP, and G3 includes both hhP and PPP |
| Translation and proper cubic covariance | The actual staggered tensor transformation, with scalar lapse and vector shift; reflections are not required |
| Finite support | Every relevant homogeneous kernel, including smearing and structure kernels, has finite total support in all relative slots. No common radius bound across candidates is imposed |
| Kinetic nondegeneracy | det F is not the zero Laurent polynomial; matching the supplied nonzero TT continuum form is sufficient |
| Exact mixed equation | The degree-two off-shell polynomial identity written below, for arbitrary fields and smearings, including regular same-order constraint mixing |
| Lapse moment | U0 is translation-covariant bilinear with U0(1,x)=mu0*x+mu1 and mu1!=0; ordinary scalar-lapse normalization gives mu0=0,mu1=1 |

The regular mixing permits G1[W1(P;X,N)] as well as C1[U1]. U1 and W1 are
arbitrary finite kernels of the indicated degree/parity. The identity is
stronger than an unspecified equation only on a possibly singular common
constraint surface. Singular redefinitions, new constraints and changed
linear generators are outside the theorem. Analyticity beyond the required
finite Taylor jet is unnecessary.

The proof-obligation graph has four internal leaves: canonical TT isolation;
uniform/affine plateau reduction; the general affine kinetic-density form;
and rational-matrix elimination followed by the Laurent constant coefficient.
They are proved in that order below. The finite-support and nondegeneracy
assumptions are explicit input leaves, not target-equivalent lemmas. The
changed-carrier controls are separate constructions rather than proof inputs.

## The necessary momentum-quadratic equation

At h=0, the degree-two mixed identity requires

    {G1[X],T3[N]} + {G2[X],T2[N]} + {G3_PPP[X],C1[N]}
          = T2[U0(X,N)] + G1[W1(P;X,N)].                 (1)

All quadratic potential and h-linear structure terms vanish in this slice.
Keeping G3_PPP is essential: time reversal does not justify deleting it.
A full completion must also satisfy the other mixed, lapse-lapse, shift-shift
and field-dependent Jacobi equations. Failure of (1) is already necessary
failure, so no successful evaluation of those additional equations is claimed.
The theorem also does not claim their finite-radius enumeration is exhaustive
of all possible physical gravity formulations.

Use fields uniform transversely and normalize their transverse zero Fourier
modes canonically. Equivalently include the transverse area in both functionals
and their reduced symplectic form; it cancels from (1). A proper quarter turn
about x acts as minus the identity on

    q=((h_yy-h_zz)/2,h_yz),   p=(P_yy-P_zz,P_yz).

These are two independent canonical pairs. Their complement has rotation
eigenvalues +1,+1,+i,-i; its rotation matrix plus I is invertible, with
determinant 8. Therefore an invariant quadratic form or constant-x-shift
bilinear generator cannot mix this TT block with its complement. Both TT
components must be kept: proper C4 alone does not split them into independent
one-dimensional irreducible sectors. Arbitrary off-diagonal and chiral matrix
kernels are allowed. Neither TT component has a half-x stagger displacement.

For arbitrary axial TT momentum profiles the linear momentum constraint
vanishes as a density: P_xx=P_xy=P_xz=0, and transverse differences vanish.
Consequently G1[W1]=0 for every W1. At constant x shift, G1[1] is identically
zero. The differentials of C1[1] and C1[x] vanish because they contain second
differences of the lapse. Hence the T3 and PPP terms cannot contribute to (1)
for the uniform and affine smearing tests.

These tests do not require inadmissible infinite sums. First take compact
axial field profiles, a finite transverse cylinder, and compact smearings that
are constant or affine on a plateau containing every differentiated kernel
support. For each proposed finite kernel, choose this plateau after its radius
is known. Boundary derivatives of G1 and C1 then have disjoint support from
the relevant T3 and G3 derivatives. Arbitrarily large periodic boxes give the
same local identities away from their seams. No fixed small torus or global
periodic affine coordinate is assumed.

## General kinetic density, canonical bracket and matrix contradiction

On this block write

    G2[1]=p^T D q,  T2[1]=p^T F p/2,  T2[x]=p^T B p/2.

D,F are finite 2x2 convolution matrices. Their Laurent symbols use
(Sf)_x=f_(x+1); define M^sharp(z)=M(1/z)^T. Reality and symmetry give
F^sharp=F, but D^sharp=-D is not assumed. An arbitrary density placement gives

    B=X F+A,                                             (2)

where X multiplies by the coordinate and A is a finite convolution. Indeed a
symmetrized pair with offsets a,b and arbitrary 2x2 real coefficient M gives

    F(z)=M z^(b-a)+M^T z^(a-b),
    A(z)=-a M z^(b-a)-b M^T z^(a-b).

Finite sums cover every quadratic lapse density after translating its lapse
anchor. Thus no midpoint convention is hidden. A need not be self-adjoint;
A-A^sharp=zF' makes B self-adjoint.

Direct canonical differentiation gives

    {p^T Dq,p^T Fp/2}=p^T(D F+F D^sharp)p/2.

Equation (1) on all compact p therefore implies the symmetric matrix identities

    D F+F D^sharp=mu0 F,
    D B+B D^sharp=mu0 B+mu1 F.                           (3)

Substitute (2), eliminate the X terms with the first equation, and invert F
over the field of rational functions. This inverse is an algebraic device,
not an assumption that a bounded physical inverse exists at every momentum.
The remaining identity is

    [D,X]+[D,A F^(-1)]=mu1 I_2.

For finite convolution [S^r,X]=rS^r, hence

    zD'(z)+[D(z),A(z)F(z)^(-1)]=mu1 I_2.

Take the ordinary finite 2x2 matrix trace. A rational-matrix commutator has
zero trace, regardless of noncommutation of D,F,A. Therefore

    z (tr D)'=2mu1.                                      (4)

The constant coefficient on the left is zero for every finite Laurent
polynomial; the right is the nonzero constant 2mu1. This contradiction proves
the theorem. It uses neither diagonalization, parity, cubic ADM normalization,
CC/GG closure nor a matter dispersion. Higher regular field degrees cannot
repair an already inconsistent homogeneous degree-two equation.

## Singular and approximate controls

Generic invertibility is load-bearing. The exact matrices

    F=diag(1,0), D=[[0,1],[0,0]], A=[[0,1/2],[1/2,0]]

satisfy (3) for mu0=0,mu1=1. The A term is realizable by the density
(N_(x+1)-N_x)p1_x p2_x/2. This reduced pair has a singular TT kinetic block
and fails the supplied nondegenerate continuum normalization. It is not a
full arbitrary-lapse solution, but shows why merely assuming F nonzero would
invalidate the proof. The singular Legendre branch alpha+3beta=0 is not
obtained by substituting into an inverse kinetic formula; it requires its own
Dirac constraint analysis and is not silently covered as a regular six-pair
completion here.

For F=I and commuting A, the central derivative D=(z-z^-1)I/2 gives the
nonzero affine residual (cos k-1)I at z=exp(ik). It tends to zero quadratically
near k=0. The formal local expression D=log(z)I solves the differentiated
identity on a branch, but is not a single-valued finite Laurent symbol.
Neither control supplies a full nonlinear infrared limit; both identify a
concrete premise change requiring analysis.

## Distinct construction routes and what they actually establish

These controls challenge any extrapolation to all discrete nonlinear symmetry.
They are independent mathematical mechanisms, not additional counted walls.

**Generalized cochain contractions.** On any finite graded complex d^2=0,
let I lower degree by one and D_I=dI+Id. Expansion gives [d,D_I]=0 and
[D_I,D_J]=D_(I D_J-D_J I). The image is a Lie algebra; quotienting by the
kernel transfers Jacobi. On a cycle's zero-plus-one complex, contractions are
arbitrary matrices, their associative product is I star J=I d J, and their Lie
bracket is I d J-J d I. Cotangent generators p^T D_I q have exactly that
canonical bracket. This is an explicit first-class enlarged spatial family.
The restricted scalar action M_X(S-1) does not close: at n>=4,
{J_0,J_1} for J_x=p_x(q_(x+1)-q_x) is p_0(q_2-q_1). Set p_0=q_2=1 and
all other entries zero; every J_x vanishes but this bracket is one. The
enlarged cochain family avoids this witness by admitting more contractions.
It is not the fixed six-strain/lapse carrier. A finite physical anchor and
normal generator with its actual gauge quotient remain unconstructed.

**Endpoint link gauge covariance.** For invertible internal transports U_xy,
(D_U psi)_xy=U_xy psi_y-psi_x transforms exactly by g_x when
psi'_x=g_x psi_x and U'_xy=g_x U_xy g_y^-1. Cotangent moment maps of this
vertex gauge group close. For orthogonal g acting on a frame E, its Gram
metric E^T E is invariant, so this internal action has zero linear metric
variation rather than the supplied symmetrized strain difference. It is a
positive local nonlinear symmetry control, with spatial/normal geometric
identification still a different obligation.

**Equivariant canonical pullback.** The derivative-only linear ideal generated
by C1 and G1 vanishes on the entire translation-fixed locus. Every regular
translation-equivariant map preserves that locus; so does regular recombination
of the pulled-back ideal. At h=0 and constant P_xx=e,P_yy=-e, the target
kinetic density is e^2/(2alpha), nonzero for e!=0. It cannot be generated by
this restricted pullback route. This invariant does not require locality or
canonicity and does not exclude starting with extra constraints or a different
carrier.

**Independent clock parametrization.** For finite canonical z and supplied
local Hamiltonians H_a, add pairs T_a,Pi_a and set F=sum T_a H_a.
On its common flow domain, one canonical map Phi=exp({F,.}) gives

    C_a=Phi(Pi_a)=Pi_a+integral_0^1 exp(s{F,.})H_a ds.

All C_a commute exactly. At equal clocks T_a=t, summing their dressed
Hamiltonians gives H_total because {t H_total,H_total}=0. For quadratic H_a
these finite-dimensional flows are complete. This is a genuine first-class
extension, not a proof that the original H_a are first-class. Gauge T=0
solves Pi_a=-H_a(z) and leaves every original z allowed; it does not impose
H_a(z)=0. A chain H_i=p_i q_(i+1) gives the exact endpoint density
sum_(n=0..L-2) (-t)^n p_0 q_(n+1)/(n+1)!, displaying support to the chain's
end. For three sites, H0=p0 q1,H1=p1 q2,H2=p0 q2 gives
C0=Pi0+H0-T1 H2/2, C1=Pi1+H1+T0 H2/2, whose clock derivatives cancel
{H0,H1}=H2. Extra clocks and a physical reduction are explicit new content.

For cochain or clock routes, the missing construction of normal constraints,
compatible sources and the desired physical gauge reduction is target-equivalent
within that route. Reaching that lemma is not evidence of near-completion.
All supplied continuous variables and actions remain comparator hypotheses.

## No-Go Discipline Gate

N1: The normalized attack families and their exact dispositions are:

| Family and marker | Primary object and mechanism | Result of the actual attempt | Terminal obligation and strength |
|---|---|---|---|
| Canonical deformation — ATTEMPTED | Finite tensor jets; affine matrix-trace invariant | Equation (4) excludes the stated class for every finite support; proof in the matrix section | None inside the scoped necessary obstruction; full physical completion changes a hypothesis |
| Cochain contraction — ATTEMPTED | Graded complex; nilpotent differential and contraction commutator | Exact enlarged spatial algebra; the displayed scalar constraint-surface witness rejects only the diagonal restriction | A physical bounded anchor plus normal generators and quotient; target-equivalent within this route |
| Endpoint gauge action — ATTEMPTED | Edge transports; endpoint group action and moment maps | Exact local covariance; frame Gram invariance does not equal the required strain relabelling | Derive geometric normal/spatial action and physical reduction; unknown/comparable strength |
| Equivariant pullback — ATTEMPTED | Derivative constraint ideal; translation-fixed locus invariant | The homogeneous kinetic witness defeats pullback/recombination of this ideal | Add or derive genuinely new constraint content; weaker route than the full target |
| Canonical clocks — ATTEMPTED | Extended canonical carrier; one simultaneous canonical map | Exact commuting constraints and synchronous dynamics; original H_a=0 is not imposed | Prove local gravitational reduction and sources; target-equivalent within this route |

Each ATTEMPTED entry has its derivation in the corresponding construction
paragraph and an exact control in the primary/imported runner. These new
proofs, not an inherited retained-status citation, are the witness authority.
Five normalized families were ATTEMPTED: canonical deformation/matrix
invariant; generalized cochain contraction algebra; endpoint link moment maps;
equivariant pullback of a derivative ideal; canonical clock extension. Their
objects, mechanisms, exact successes/failures and terminal obligations are
stated above. Polynomial support radii and different verifiers count as one
family, not extra routes. No family is called ruled out by prior authority.
The cochain, link and clock constructions are successful changed-carrier
controls, not five defeated gravity theories. Focused source review accepted
this interpretation of five attempted mechanisms; it supplies no claim of
exhaustive search or broader physical impossibility.

N2: Only one main obstruction is claimed: the necessary canonical mixed
identity in the stated class. A fixed ultralocal kinetic witness, finite-radius
certificates and the matrix theorem are not counted as independent walls.
The pullback and toy cochain witnesses concern different restricted mechanisms;
no implication in either direction or independent-wall count is asserted.
The clock construction changes the carrier before the main theorem applies.

For completeness, the relations among the distinct diagnostics are recorded
without manufacturing independent walls:

| Pair | Does closing the first close the second? | Reverse implication? | Disposition |
|---|---|---|---|
| Canonical mixed / diagonal-cochain witness | Unresolved across changed carriers | Unresolved | Different stipulated objects; no independence assertion |
| Canonical mixed / pullback witness | Unresolved for changed initial ideals | Unresolved | Pullback failure is a restricted construction test |
| Canonical mixed / clock reduction | No implication established | No implication established | Extra clock carrier changes the theorem's domain |
| Diagonal-cochain / pullback | No implication established | No implication established | Neither test supplies the other's carrier/ideal |
| Diagonal-cochain / clock reduction | No implication established | No implication established | Successful enlarged constructions remain open physically |
| Pullback / clock reduction | No implication established | No implication established | Both involve canonical maps but distinct input and output constraints |

N3: Canonical continuous fields, background expansion, time reversal, actual
staggering, covariance, finite support, generic invertibility and exact lapse
moment are explicit hypotheses. The primitives are not invoked to select
this carrier, bracket, law, clock or source. Ordinary matrix/Poisson algebra
is mathematical machinery; it imports no physical identification.

N4: The two linked sources supply only the displayed seed definitions. Their
leading lapse bracket and walker-only residual do not prove this next mixed
result and are not used as no-go witnesses. The internal witness (4) attacks
exactly the declared mixed equation. The cochain example attacks only its
nearest-neighbor scalar restriction; the pullback invariant only its stated
ideal; the clock example only automatic recovery of H_a=0 and this construction's
uniform locality. No mismatched prior witness carries the theorem.

The precise witness matching record is:

| Witness | Residual addressed | Residual claimed closed | Match |
|---|---|---|---|
| Matrix proof, equation (4) | Degree-two mixed identity with finite kernels and invertible TT symbol | Exactly that identity class | Yes |
| Cochain construction's scalar phase point | Fixed J_x=p_x(q_(x+1)-q_x) constraint ideal | Only that toy restriction | Yes |
| Translation-fixed-locus proof | Pullback/recombination of the derivative-only linear ideal | Only that route | Yes |
| Clock quotient and endpoint chain coefficient | This canonical extension's reduction and uniform locality | No automatic H_a=0 recovery; no uniform range for this construction | Yes |
| Linked seed notes | Supplied stencils and leading-order context | No next-order impossibility attributed to them | Context only; not counted as witnesses |

N5: Per element, exact canonical derivatives and Laurent coefficients are
checked. Per site, the scalar constraint-surface and homogeneous witnesses
are evaluated. Per mode, the full two-component symbol, including noncommuting
matrices and a singular control, is checked. Per block, exact finite-position
Hessians and cochain/clock brackets are controls. The lattice-wide all-finite-
support conclusion follows from the analytic proof and plateau reduction;
finite checks alone do not establish it. No native many-body gravity phase,
full matter system or complete nonlinear constraint algebra is executed.

N6: No axiom revision is demanded. Enlarged gauge carriers, a different seed,
degenerate kinetic sectors, nonlocal kernels and controlled infrared closure
change explicit hypotheses. The three constructive mechanisms above supply
partial structure without silently registering a primitive. Whether any gives
a physically selected gravity law remains unresolved.

N7: The strongest objection is to assume the physical lattice must realize
this exact microscopic canonical hypersurface form. A collective phase may
have a different background, extra transforming sources, nonlocal effective
kernels or only emergent infrared symmetry. Cochain and clock constructions
prove that exact discrete first-class algebra is possible with changed data.
A counter-route inside the theorem would have to exhibit its finite kernels,
nondegenerate TT symbol and nonzero lapse moment while violating none of the
reduction steps; equation (4) forbids that. The stated alternatives are live
outside the theorem and refute a universal gravity/axiom interpretation.

N8: Prior source repeatedly leaves nonlinear completion and physical source
selection open. The actual recent viability proposal PR9363 was read at
fd51a1f4c7f38c124d6f0f7dde396198eadf8b36; its walker-only restrictions are
not promoted into the present coupled theorem. The landed cochain work and
soft-spin2 finite-stencil/source analysis were inspected as related mechanisms;
none supplies a complete native nonlinear law. The original leading lapse
identity is context, not new science here. This unit adds the necessary next
mixed-order matrix obstruction and explicit changed-premise controls.

## Evidence, imports and review boundary

The primary runner supplies exact distinct-representation controls; its
source-bound cache is generated only by runner_cache. The analytic quantified
proof above, not a predetermined output banner, establishes all finite supports.
Discovery independent checking verified canonical TT normalization, actual
proper rotation, general lapse centering, noncommuting elimination, a finite-
position Hessian and the singular stress example before source packaging.
One independent source reviewer found no mathematical defect at this bounded
scope and accepted the five distinct attempted constructions under N1. A missing
status-reason field and incomplete mutation-family coverage were identified for
repair. The final source/input binding, repaired mutation evidence and twelve
conformance dispositions are recorded in the accompanying milestone pack. Full
pipeline, strict audit lint and combined changed-evidence validation remain for
the later integrated landing candidate. No audit verdict, overall landing PASS
or effective retained status is asserted.

Axiom pressure is limited: no inconsistency of the current axioms is proved;
they do not select the supplied comparator law. The optional exact canonical
completion fails inside the stated class. Constructive enlarged-carrier and
approximate alternatives remain viable research targets, with explicit physical
identification and source obligations. No completed TOE is claimed.
