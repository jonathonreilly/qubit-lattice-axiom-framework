---
claim_id: current_preserving_refinement_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Supplied one-dimensional free massive chain: coherent real state/current-preserving refinements, doubled coefficient/even-CAR limit, physical cell sectors and explicit actual-time incompatibility."
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
runner: scripts/current_preserving_refinement_identity_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: supports
target_claim_id: null
target_blocker_text: "Determine what exact actual-current preservation changes in the supplied-chain continuum refinement."
source_of_blocker_text: frontier_question
next_trace_action: "Review the exact supplied-model construction as a partial-narrowing proposal; keep physical selection and formal no-go packet obligations open."
conditional_surface_status: "Chosen model, state and normalized actual current; equal-time doubled limit with restricted physical time-limit sector."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Ordinary mathematical proof with explicit supplied-model premises; no empirical or framework-selection conclusion."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

Status: proposed_retained

Primary runner: [source identity and reconstruction only](../scripts/current_preserving_refinement_identity_2026_10_12.py).
It checks named bytes and exact reconstruction, with zero mathematical predicates
or scientific mutations. It cannot supply an N5 proof certificate or packet PASS.

**Author/checker pairing:** The selected model and effort are unchanged. Root is
a coauthor. The separate review context froze its independent derivation before
author-target exposure. The final source-bound review and root source gate accept the scoped proposal;
the additional paired-cell local-quotient check followed author exposure.
No blind or model-diverse review is claimed.


# Current-preserving refinement of the supplied massive chain

**Author proof proposal, 2026-10-12.** Exact preservation of the actual
normalized current and chosen state is possible after relaxing exact energy
compatibility. The construction includes both inverse branches of the current
on the full Brillouin zone. Its completed coefficient space has two copies of
the usual two-component continuum space. Fixed ordinary cell inputs reach
only one copy; alternating cell inputs reach the other. The additional copy
has energy diverging as the spacing decreases. It is not a derived extra
light particle. Actual time evolution converges on the ordinary fixed-cell
sector, but does not converge on the whole constructed limit as all positive
spacings tend to zero.

This is a pure proof under the supplied model, state, current normalization
and even-CAR identification. No scientific numerical runner, formal proof
assistant, empirical prediction, framework state-selection claim, independent
review receipt or audit verdict is asserted.

## 1. Contract and exact parents

Write S for this note's directory and E=S/current_preserving_refinement.
E/PLAN.md and E/source_inventory.json were sealed before this task's proof
execution, at 15:19:58 UTC. The complete parent snapshots are:

| Parent | SHA-256 | Mathematical use |
|---|---|---|
| CONCRETE_GAPPED_CHAIN_PROBE.md | `0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd` | Actual spin density/current, coefficient symbol, selected state |
| LOCAL_EVEN_CONTINUUM_PROBE.md | `7be1a72e2b59c5c61b68ead6d663e8d4e179b21e2497243a2859a4082ea7813b` | Real coefficient convention, actual time sign, covariance, cells, even JW |
| ENERGY_ADAPTED_REFINEMENT_PROBE.md | `65d49c82eb14b88e4880983eb8b41ecb5141cb0ff00f4e5e4760bbb12a151b9d` | Explicit comparison and alias normalization, rederived below |

The separately checked SHARP_CURRENT_REFINEMENT_PROBE.md at
`2a6948ab1d98584ac77b3486f8ec1927d88fbb55cd0276123b6c24750f9d6a42`
is comparison context for exact-energy refinement, not a premise of this
construction. Necessary parent passages were refreshed; this agent's earlier
full/source-bound review coverage at these unchanged hashes is reused. This
does not supply a fresh transitive review of the parent spin construction.

Root is considering the same target. This author had already reviewed the
energy construction and is not blinded to it. Root's new reconstruction is
withheld until the analytic core is frozen. During this derivation root
emphasized the distinction between coefficient multiplicity and light
particles, and the distinction between all-scale and dyadic time limits.
Those are disclosed coauthor scope prompts, not independent evidence.

Applicable physics-loop/workflow/primitive/proof-search instructions are
bound to main `72a7cf00adf0756a215a247d344df21d06a1d582`; the existing
planning identity is `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`.
The parent forbids Git mutations and assigns root packaging, so this task
uses the supplied revision without fetching or creating a branch. Bounded
statement queries are in E/statement_search.json. Their generic matches do
not establish this construction or a novelty claim. No unrelated ledger or
open-PR inventory was audited. Interactions, higher dimensions and boosts
are outside this task.

## 2. Actual symbols and reality

Fix m,v>0. For every c>0 use H_c=ell^2(Z;C^2), with position conjugation
Gamma_c, and the unitary Fourier transform

    (L_c z)(q)=sqrt(c/(2pi)) sum_j z_j exp(-icqj),
    q in B_c=(-pi/c,pi/c).                              (C1)

The continuum transform is (Lf)(p)=(2pi)^(-1/2) int exp(-ipx)f(x)dx.
Reality in either momentum coordinate is h(-p)=conjugate(h(p)). Set

    sigma_c=sqrt(m^2/4+v^2/c^2),
    g_c=sigma_c/2+m/4, J_c=sigma_c/2-m/4,
    D_c(q)=-2J_c sin(cq) sigma_x-2(g_c-J_c cos(cq)) sigma_y,
    E_c(q)^2=m^2+4v^2 sin^2(cq/2)/c^2,
    theta_c(q)=arg(g_c-J_c exp(-icq)),
    F_c(q)=exp(-i theta_c(q) sigma_z/2),
    C_0=-sigma_y, P_0=(1+C_0)/2,
    F_c D_c F_c*=E_c C_0, P_c=F_c* P_0 F_c.             (C2)

The argument is single-valued with real part at least m/2. Hence theta_c
is odd and F_c(-q)=conjugate(F_c(q)). The actual coefficient time action
is exp(+itD_c), and the chosen state has covariance 2<z,P_c w>, with
conjugate-linear first inner product. These signs follow from Local L3-L5;
at J=0 they give omega(XY)=i and the actual -gZ clock.

Concrete C4/C28 gives actual current symbol 4J_c g_c sin(cq) times 1.
Since 4J_c g_c=v^2/c^2, the normalization in the question is exactly

    K_c=(c/v^2)P_actual,c,  K_c(q)=sin(cq)/c times 1.    (C3)

This is not a substitution of geometric momentum for the current. Both
D_c and K_c are bounded self-adjoint at fixed c. They are anti-real:
Gamma_c D_c Gamma_c=-D_c and Gamma_c K_c Gamma_c=-K_c. Their groups
exp(+itD_c) and exp(+isK_c), rather than the generators themselves, preserve
the real space. Odd CAR fields below are auxiliary; only even products are
identified with actual bilateral spin elements.

## 3. Full-zone current disintegration

Put I_c=(-1/c,1/c), w_c(p)=sqrt(1-c^2p^2), and, away from null endpoints,

    q_c,0(p)=arcsin(cp)/c,
    q_c,1(p)=sgn(p) pi/c-arcsin(cp)/c.                 (C4)

The low branch covers (-pi/(2c),pi/(2c)). The second covers the two outer
arcs, joined through the periodic endpoint at p=0. Values at p=0 may be
assigned arbitrarily there. Each branch is odd almost everywhere; their
derivatives are respectively +1/w_c and -1/w_c. In particular, discarding
the second branch would discard a positive-measure subspace, not only an
endpoint or a zero-current mode.

Define T_c by

    (T_c phi)_r(p)=w_c(p)^(-1/2) phi(q_c,r(p)), r=0,1. (C5)

Then T_c is unitary from L^2(B_c;C^2) onto L^2(I_c;C^2) direct-sum
L^2(I_c;C^2). Indeed, splitting the q integral into the central arc and
the two outer arcs and changing variables gives

    int_Bc |phi(q)|^2 dq
      =sum_r int_Ic |phi(q_c,r(p))|^2 dp/w_c(p).       (C6)

The inverse on branch r is sqrt(w_c(sin(cq)/c)) times the r component
at p=sin(cq)/c. Compact continuous functions away from the endpoints
are dense, so the formula extends onto all L2. The half density diverges
with exponent -1/4 at the critical values, but C6 proves integrability
in the correct measure. No derivative-domain conclusion follows from C6.
The negative derivative on the outer branch is handled by its absolute
Jacobian; it does not insert a negative norm or a conjugation. The real
involution remains reflection plus conjugation on each component.

Let H_*=L^2(R;C^2) direct-sum L^2(R;C^2), with its usual position-real
subspace. Define the low continuum frame and the target covariance by

    D(p)=-vp sigma_x-m sigma_y, E(p)=sqrt(m^2+v^2p^2),
    F(p)=exp(-i arctan(vp/m) sigma_z/2),
    P(p)=F(p)*P_0 F(p), P_*=P direct-sum P_0.          (C7)

Use identity frame on the outer component; this is an explicit target
coordinate choice. With i_c extension by zero in each copy, define

    J_c=(L^-1 direct-sum L^-1)
          diag(F*,1) i_c T_c M_(F_c) L_c.             (C8)

Every factor is unitary or isometric. All factors respect the real
involution. Thus J_c is a real isometry with exactly the range

    R_c= [L^-1 L^2(I_c;C^2)] direct-sum
         [L^-1 L^2(I_c;C^2)],    Q_c=J_c J_c*.         (C9)

The target frame does not shrink the range. R_a is contained in R_b for
every 0<b<a, and their union as c decreases to zero is dense in H_*.

## 4. Coherent state and current preservation

For all 0<b<a, set G_(b,a)=J_b* J_a, with G_(a,a)=1. Range inclusion gives

    G_(b,a)*G_(b,a)=1,
    J_b G_(b,a)=J_a,
    G_(d,b)G_(b,a)=G_(d,a), 0<d<b<a.                 (C10)

Explicitly, for |p|<1/a and r=0,1,

    (L_b G_(b,a)z)(q_b,r(p))
      =sqrt(w_b(p)/w_a(p)) F_b(q_b,r(p))*
             F_a(q_a,r(p)) (L_a z)(q_a,r(p)),          (C11)

and the fine function vanishes elsewhere. The r-specific target frames
cancel. This also verifies composition directly across arbitrary scales,
without requiring an integer scale ratio.

Let K_* be multiplier p on both target copies, with maximal domain
int p^2(|h_0|^2+|h_1|^2)dp<infinity. Each R_c lies in its domain, so

    K_* J_c=J_c K_c,
    P_* J_c=J_c P_c,
    exp(+isK_b)G_(b,a)=G_(b,a)exp(+isK_a).             (C12)

There is no unbounded-domain inference hidden in C12: K_* is bounded
by 1/c on R_c. P_* satisfies Gamma P_* Gamma=1-P_* and is a projection,
so it defines the usual pure quasifree real-CAR state.

The real isometries induce injective unital isometric CAR maps. A direct
justification restricts finitely many real orthonormal vectors to an even
dimensional finite subspace, uses its faithful full Clifford matrix algebra,
then takes norm completion. Restriction to even products and the parent's
compatible finite even-JW maps yields actual even-spin refinement maps.
Equation C12 identifies all two-point functions; quasifree Pfaffians and
norm density then give exact preservation of the chosen state. Current
group compatibility follows on finite even words and then in norm. No
identification of the odd spin algebra is made.

The completed even-CAR inductive algebra of this system is

    CAR(H_*,R)^even.                                  (C13)

Both copies are required for density. Its complex coefficient spectral
multiplicity for current p is four; its positive-polarization fiber has
dimension two. A single two-component Dirac coefficient carrier has the
respective multiplicities two and one.

There is also a class-wide coefficient statement, separate from C8's time
behavior. Any complex-linear isometry from the *full* H_a to H_b that
intertwines K_a,K_b must, in the two-branch spectral coordinates, be a
measurable 4-by-4 unitary on |p|<1/a and zero outside that band. To see
this, intertwining the bounded self-adjoint operators intertwines their
polynomials, then continuous functions, then spectral indicators by bounded
strong approximation. Thus the map commutes with multiplication by each
measurable scalar indicator after band inclusion. Apply that module identity
to the four constant coordinate vectors on finite intervals: their images
define a measurable matrix, and simple functions determine the operator.
Isometry forces its columns orthonormal almost everywhere; equal finite
fiber dimensions make the matrix unitary. No decomposability assumption
was inserted. A countable sequence c_n decreasing to zero is cofinal among
all spacings. These fiber unitaries can be absorbed successively along that
sequence, leaving the standard nested four-component bands. Consequently
any such coefficient inductive system has current multiplicity four.
It cannot be identified by a current-intertwining coefficient isometry
with the full single-copy current-p carrier. This statement does not
classify arbitrary abstract isomorphisms of the even C*-algebras.

## 5. Actual energy and an even time-defect witness

In C8 coordinates the actual coefficient energy on R_c is

    H_c^*(p)=diag(e_c,0(p) D(p)/E(p), e_c,1(p) C_0),
    e_c,0(p)^2=m^2+(2v^2/c^2)(1-w_c(p)),
    e_c,1(p)^2=m^2+(2v^2/c^2)(1+w_c(p)).              (C14)

This follows from cos(c q_c,0)=w_c and cos(c q_c,1)=-w_c, including
both energy signs through the two-component matrices. For |p|<1/a,

    J_b(D_b G_(b,a)-G_(b,a)D_a)J_a*
      =diag((e_b,0-e_a,0)D/E,(e_b,1-e_a,1)C_0) Q_a. (C15)

Here J_a* is understood on the target; C15 vanishes off R_a. The low
energy squared is m^2+2v^2p^2/(1+w_c), so e_b,0<e_a,0 for p!=0.
The high energy strictly increases as c decreases: both c^-2 and w_c
increase, hence e_b,1>e_a,1 throughout the common band. All these are
positive-measure statements, not reliance on a singleton zero mode.

The exact coefficient group defect norm is

    ess sup_(|p|<1/a) max_(r=0,1)
            2 |sin(t(e_b,r(p)-e_a,r(p))/2)|.           (C16)

It follows by simultaneous diagonalization of the fixed target matrices.
For sufficiently small nonzero t it is positive. Equality at t=0 is
retained, and no lower bound uniform over all t is claimed.

The even algebra sees a real defect. Choose normalized orthogonal positive
polarization packets u,v in the outer copy, with disjoint compact current
supports inside I_a. In the pure quasifree Fock representation the even
CAR element B=a*(u)a*(v) has norm one and creates u wedge v from the vacuum.
The difference of the two evolved vacuum matrix elements has derivative
at t=0 equal to i times the strictly positive integral of
(e_b,1(p)-e_a,1(p))+(e_b,1(p')-e_a,1(p')) against |u(p)|^2|v(p')|^2.
Compact support makes this differentiation bounded. Thus the refined
actual even time actions differ for small nonzero t. A phase on a single
odd field has not been used as an observable witness.

On each fixed compact p set, direct expansion of C14 gives

    e_c,0(p) -> E(p),
    e_c,1(p)=2v/c+c(m^2-v^2p^2)/(4v)+O(c^3),          (C17)

uniformly. The second line gives an especially sharp limit warning. For
the fixed outer B above and sufficiently small c,

    alpha_c^time(t)(B)=exp(i4vt/c) B+o(1)             (C18)

in the common CAR norm, for fixed t; field continuity controls the uniform
O(c) packet phase error. These are the actual embedded finite-scale actions
on the same element B, which lies in their common band algebras. For any
fixed t!=0, the sequences c_n=4v|t|/(2pi n) and
d_n=4v|t|/((2n+1)pi) have limiting phases +1 and -1. Hence no full
all-spacing c->0 point-norm time limit exists on C13. The two subsequential
limits have norm distance 2 on B. The real and imaginary parts of B
also detect failure, so this is a statement about even observables.

This quantifier does not assert failure at every time on every prescribed
subsequence. On c_n=c_0 2^-n, choose t=pi c_0/(6v); the leading phases
are exp(i(2pi/3)2^n) and alternate between two distinct values, while the
error tends to zero. Thus this dyadic system also has a concrete nonzero
time with no limit and cannot supply a full limiting time group. Other
dyadic times, such as t=pi c_0/(2v), have leading phase one and may converge
on this witness. Subtracting the outer diverging energy or projecting out
that sector would be a changed dynamics or a restricted carrier.

## 6. Ordinary and alternating physical cells

Use exactly the parent's physical cells

    (C_c f)_j=c^(-1/2) int_[cj,c(j+1)] f(x)dx,
    (M_c z)_j=(-1)^j z_j.                              (C19)

C_c is a real contraction, M_c is a real unitary, and compact position
support gives finite even-spin support in the cell hull. For smooth compact
Fourier support, direct integration and the Fourier sum give

    (L_c C_c f)(q)=sum_l exp(ic(q+2pi l/c)/2)
         sinc(c(q+2pi l/c)/2) fhat(q+2pi l/c).          (C20)

The cell integral of exp(ikx) is sqrt(c)exp(ick(j+1/2))sinc(ck/2).
It fixes the positive phase and rules out extra c or 2pi factors in C20.
If fhat is supported in [-M,M] and cM<pi/2, only the central alias is
present and its support lies wholly in the low current branch. In C8
coordinates, q_c,0(p)->p, w_c->1 and F_c(q_c,0(p))->F(p) uniformly on
that compact set. Dominated convergence, followed by density and
||J_c C_c||<=1, proves for every f in L2

    J_c C_c f -> (f,0).                               (C21)

In particular, fixed ordinary cell inputs do not exhaust H_*. Their limiting
coefficient subspace is the first summand, a closed proper subspace.

Alternation gives the exact periodic Fourier shift

    L_c M_c z(q)=L_c z(q-pi/c),                        (C22)

where the right side is read periodically. At q=q_c,1(p), q-pi/c is
congruent to -q_c,0(p) for both signs of p. Thus for compact Fourier
support the low output of J_c M_c C_c g is exactly zero at sufficiently
small c, while its high output is

    w_c(p)^(-1/2) F_c(q_c,1(p))
       exp(-ic q_c,0(p)/2) sinc(c q_c,0(p)/2)
                                    ghat(-q_c,0(p)). (C23)

There is no extra minus sign or residual half-cell phase. The denominator
inside the high-branch argument is g_c+J_c exp(ic q_c,0); its real part
grows as v/c and its imaginary part stays bounded on compact p. Hence
F_c(q_c,1(p))->1 uniformly. Formula C23 tends to ghat(-p). The same
contraction/density argument, now using ||J_c M_c C_c||<=1, gives

    J_c M_c C_c g -> (0,Rg), (Rg)(x)=g(-x),            (C24)

for every L2 input. A normalized compactly supported g therefore supplies
nonvanishing, physically local oscillatory sections in the second copy.
The second branch is not negligible merely because C21 holds.

Taking finite products of cells C_c f+M_c C_c g gives, by the CAR norm
estimate and telescoping, the corresponding finite products with coefficient
(f,Rg). All packets may be real and compactly supported. Thus the doubled
equal-time coefficient algebra is reached by two physical envelopes. In
the physical coordinate convention (f,g), obtained by reflecting the second
target copy, its covariance is P direct-sum P_0 and its current is
p direct-sum (-p). The high component has the constant polarization P_0;
this supplies no second finite-energy relativistic dispersion.

Actual time evolution of ordinary fixed cells still has the intended limit:

    J_c exp(+itD_c) C_c f -> (exp(+itD)f,0),            (C25)

uniformly on bounded t intervals for each fixed L2 f. Prove it first on
compact Fourier support using C14/C17/C21; the high component is then zero.
Density and unitarity extend it to all f. For general f, its small high
norm stays small under the high unitary even though its phase is rapid.
Finite even words and their chosen-state moments inherit C25. This proves
a physical single-species sector limit, not an exhaustion of C13.

## 7. Local sections and actual spatial shifts

There is an explicit equal-time local comparison that also controls arbitrary
norm-convergent sections. In this paragraph use the physical target
coordinates and write Jtilde_c=(1 direct-sum R)J_c. Pair adjacent sites and
put

    u_j=(z_(2j)+z_(2j+1))/sqrt(2),
    v_j=(z_(2j)-z_(2j+1))/sqrt(2),
    B_c z=(j_(2c)u,j_(2c)v),                          (C26)

where j_(2c) is the ordinary step-function isometry. B_c is real isometric
onto the two-copy step space at cell size 2c, whose projection tends
strongly to identity. Its adjoint satisfies

    ||B_c*(f,g)-(C_c f+M_c C_c g)|| ->0.              (C27)

In fact B_c*(f,g)=C_c Q_(2c)^cell f+M_c C_c Q_(2c)^cell g exactly,
as follows by inserting the two pair averages. Hence the norm in C27 is
at most ||Q_(2c)^cell f-f||+||Q_(2c)^cell g-g||, which tends to zero
for every L2 pair. Equations C21/C24 imply
Jtilde_c B_c*->1 strongly. Extend it to a real unitary

    V_c=Jtilde_c B_c*+W_c(1-B_c B_c*),                (C28)

choosing any real unitary W_c between the infinite-dimensional orthogonal
complements of the step range and band range. Then V_c->1 and V_c*->1
strongly, and Jtilde_c=V_c B_c exactly. The induced even-CAR maps tend
point-norm to identity, by finite-word continuity and norm density. Thus
for the same bounded section x_c, its B_c images converge in norm if and
only if its Jtilde_c images do, with identical limit. This is a comparison
to paired-cell two-copy Haar embeddings, not to the single-copy embedding.

For a bounded open interval I, microscopic sections supported on cells
wholly inside I have B_c images in the doubled even algebra of I enlarged
by 2c. Any norm limit belongs to the doubled local algebra of I. Here is
the needed outer-continuity justification: for coefficient subspaces
L2(I_epsilon;R^4) decreasing to L2(I;R^4), their orthogonal projections
converge strongly. The trace-preserving CAR conditional expectations onto
those subspaces converge point-norm to that onto L2(I;R^4). On finite
words this follows by orthogonal decomposition and the tracial Wick
contractions on the complement; contractivity and polynomial density give
the general assertion. An element fixed by all these expectations is fixed
by their limit. Endpoints have measure zero. Conversely, compactly supported
two-envelope words, then norm density and diagonal approximation, furnish
inner-cell local sections for every element of that doubled algebra. Hence
the local quotient of these norm-convergent sections is exactly

    CAR(L2(I;R^2) direct-sum L2(I;R^2))^even.         (C29)

The construction of a conditional expectation just used is independent of
the chosen physical state: it uses the CAR trace only as a mathematical
norm projection. No tracial physical state was substituted for P_*.
Equation C29 is an equal-time algebra statement. It does not supply a
time-covariant doubled continuum net, which C18 explicitly obstructs for
the unmodified actual dynamics.

Current and physical spatial shifts remain different at finite scale. A
physical grid displacement ell=Nc has multipliers

    low:  exp(-i ell q_c,0(p)),
    high: (-1)^N exp(+i ell q_c,0(p))                 (C30)

in the common current coordinates. This follows directly from C4 and
exp(-i ell q). The exact current action instead has exp(+is p) on both
copies. Even when a nonzero ell is a grid displacement at both scales,
q_a,0 and q_b,0 differ on every nonzero momentum interval, so C11 does
not intertwine those physical shifts. A nonconstant phase ratio is
detected by the rank-one projection of a positive-band packet, an even
number observable. At the continuum level in physical two-envelope
coordinates, shifts through an even number of cells have the ordinary
geometric limit on both envelopes. Odd cell parity flips the outer envelope;
mixed low/high even words detect that sign. Arbitrary rounded physical
shifts therefore need a parity convention before a full doubled shift
limit can be asserted. Ordinary fixed low-cell inputs retain the usual
single-copy translation limit.

No finite-scale locality is inferred from C29. C11 vanishes on nonempty
fine-momentum arcs where |sin(bq)/b|>1/a. A nonzero finite-support vector
has a trigonometric-polynomial Fourier transform and cannot vanish there.
Thus nonzero refined coefficient vectors have infinite support. Truncating
their ell2 tails still gives quasilocal even-CAR elements in norm. No
uniform physical-tail or exponential-locality bound is asserted.

## 8. Failed shortcuts, boundaries and next check

The one-branch arcsine map is not an isometry of the full original chain;
it loses half the spectral fiber. The map without w_c^(-1/2) fails C6.
Using the outer signed derivative as a measure gives a negative norm.
Treating K_c as a real operator instead of an anti-real generator gives
the wrong CAR reality test. Inferring full-limit exhaustion from C21 is
refuted by C24. Inferring compatible actual time from preserved state is
refuted by C15 and the even witness C18. An outer scalar energy shift
would remove a leading phase only after modifying the actual dynamics.

These are scoped failures, not a universal ban on other refinement
categories. Restricting the original coefficient carrier, retaining only
the low physical sector, relaxing exact current preservation, or changing
the high dynamics changes the stated contract and remains a distinct
question. The earlier energy-preserving map is a concrete complementary
choice: it preserves actual energy but has a finite-scale current defect.

For the no-go-discipline boundary: N1 has these genuine alternatives but
no five-family exclusion certificate is claimed or fabricated. N2 treats
coefficient multiplicity and this map's time behavior as distinct statements,
not a counted list of independent universal walls. N3 records the model,
state, full carrier, normalization, real-isometry class and coordinate choice
explicitly. N4 uses the sharp exact-energy result only as comparison, not a
proof about the relaxed class. N5 distinguishes modes, fixed inputs, the
full coefficient space and even observables. N6 no new axiom is required
to define a restricted sector or changed dynamics; neither equals the
original full contract. N7 the strongest escape is the valid ordinary-cell
single-species limit C25, which this note keeps. N8 the earlier energy
construction is preserved as a different tradeoff. No N1-N8 packet PASS,
general interacting obstruction or theorem about arbitrary C*-isomorphisms
is asserted.

The strongest proved candidate is the all-scale real state/current
construction C8-C13 together with its complete branch accounting and
physical section comparison. Its proof is elementary Hilbert/spectral/CAR
analysis using the pinned actual-model inputs. Independent review should
target the full-zone Jacobian and realness, the spectral multiplicity lemma,
the alternating-cell phase/reflection, the even time witness, and the
paired-cell local quotient. No proof-assistant certificate or re-audit of
the parent's full spin/GNS construction is supplied. The physical choice
of model, m,v, selected quasifree state and normalized current remains
conditional. Approved framework primitives do not select those inputs.

The remaining frontier question is which physical restriction or dynamics
criterion should select among these inequivalent refinement contracts; this
note makes no selection. Root alone packages. Completed ENERGY review and
all repository/audit/prompt/axiom surfaces remain unmodified by this task.

## 9. Post-freeze chronology and exact erratum

The full 498-line analytic core was frozen at 15:34:14 UTC with SHA-256
`b5a80216d91bb1d525a605ba825c3c46a5130fd47ca4ed7f3444242ca778d637`.
Its immutable original remains in E/frozen/; E/CORE_FREEZE.json binds the
plan and source inventory. No numerical or symbolic scientific execution
preceded or followed that seal.

Only after that seal was the entire root reconstruction read, at SHA-256
`8182f9251de4c084edf4da8f4c073a8fa17a03d206720bdf0559fd50fe40b338`.
E/ROOT_EXPOSURE.json records the post-freeze exposure. The constructions
agree after a fixed target frame change diag(F*,1), which cancels from the
refinement maps. The root uses a different equivalent dyadic time witness.
Its optional optimized energy-defect norm was not imported or pursued.
The author's alternating-cell calculation, paired-cell local quotient and
class-wide coefficient multiplicity argument were already in the frozen
core. This reconciliation is coauthor comparison, not independent review.

Root's full-core read identified one literal wording error after C18. The
original says, "Norms of the two subsequential limits differ by 2 on B."
Both limits B and -B have norm one. The corrected sentence says, "The two
subsequential limits have norm distance 2 on B." This is the only change
to the frozen analytic core; equations and quantified conclusions remain
unchanged. E/FINAL_CORE_ERRATUM.diff preserves the exact correction, and
E/FINAL_APPENDIX.diff preserves the whole difference from the frozen source.

The instruction revision 72a7cf00... in section 1 was the earlier supplied
and actually read snapshot, not a claim about latest main. Root subsequently
reported main 34ab625..., resolved read-only here as
`34ab62523138756eded9bdcc8a35fd2ff61f926f`. All thirteen captured applicable
workflow/skill/foundation files are byte-identical at those two revisions;
E/instruction_inventory.json records both sets of hashes and the preserved
read snapshots. No fetch, instruction edit or repository mutation occurred.
This identity comparison is bookkeeping, not a second reading of changed
instructions: no differences were found in those files.

A fresh focused reviewer separately reconstructed the target before source
exposure, according to root's coordination record. That review is a separate
artifact, owned by its reviewer. This author note does not certify its own
independence or predict the review outcome. E/RECOVERY.md records the current
handoff and exact verification limits; E/final_manifest.json binds the final
source and evidence. No parent audit status or editable prompt changed.


## Publication dependencies and disposition

The [concrete-chain theorem](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md)
supplies the actual density/current, coefficient matrix and chosen state. The
[local-even-continuum theorem](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md)
supplies the real coefficient signs, covariance, cell and even-spin conventions.
These are the two direct scientific dependencies. Their published bytes are
bound to SHARP head `7c0570a4a20a768349f3d88960303f8637e7fe33`, regular PR9497. ENERGY and SHARP are comparison/ancestry only;
the branch accounting and alias formulas used here are rederived in this proof.

The exact original source, author chronology, failures, neutral review plan,
pre-exposure independent derivation and final comparison are preserved byte-exactly
in the branch packet. Publication changes only metadata and this explicit wrapper.
The two-copy coefficient multiplicity is not a second light physical particle.
The equal-time local quotient does not establish full actual-time covariance,
finite-scale support locality, limiting boosts or arbitrary mixed-flow limits.

Disposition: partial-narrowing review proposal, conditional-support. N1 five-family
coverage and N5 formal no-go certificate readiness remain pending. No no-go packet
PASS, universal obstruction, mathematical runner PASS, retained audit verdict or
new physical axiom is asserted. Ordinary proof review, identity support, a regular
PR and later landing/audit decisions remain separate.
