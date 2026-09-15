---
claim_id: native_weyl_local_interaction_covariance_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "Derive the formal Grassmann boost criterion for adding a derivative-free local potential to a supplied Weyl normal generator. Classify charge-preserving quartics for one Weyl pair and the leading vertex of real symmetric even orbital-density kernels. Construct an explicit finite-range native density interaction with nonzero invariant leading quartic, within the stated small-coupling Weyl model class. Bare vertex, formal classical bracket and imported dressed two-point statements have separate domains. No renormalized four-point, quantum gravity or nonzero interacting continuum limit is asserted."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_weyl_local_interaction_covariance_2026_09_13.py
---

# Native Weyl local interactions and their covariance condition

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Target and premises

Find which local fermion interactions preserve a supplied classical Weyl
normal bracket, and whether a nonzero such interaction can occur as the
leading vertex of an explicit native density coupling. A positive construction
is given below. Its coefficient vanishes under fixed weak-coupling engineering
scaling; a finite interacting continuum theory remains a separate problem.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Local polynomial classification, finite native construction and a smooth few-particle vertex estimate."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Consistent interactions for the same native Weyl matter and supplied geometry."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Test radiative covariance and a mechanism for finite physical interactions or native dynamical geometry."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

The [minimal framework memo](MINIMAL_AXIOMS_2026-06-29.md) is the ontology
reference. The quantum tensor/CAR interpretation, selected Hamiltonian,
continuous time, Weyl identification, smooth geometry and its classical
normal generator are supplied model inputs. Native number operators use the
conditional representation in the
[current-main edge/CAR source](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md).
No result from an unmerged sibling proposal is required by this note.

| Statement | Domain and evidence | Remaining boundary |
|---|---|---|
| Local potential changes the normal bracket by its boost variation | Formal Grassmann functionals, direct Euler calculation | No quantum operator constraint algebra |
| Five real Hermitian charge-preserving quartics, three with separate valley number | One specified Weyl pair, representation and component proof | No flavor or gauge-content selection |
| Density-kernel classification and explicit invariant stencil | Bare four-leg vertex of a specified two-orbital carrier | No radiatively preserved four-point identity |
| Native finite support and smooth vertex limit | Even CAR operators and fixed smooth few-particle states | No interacting ground-state convergence from this estimate |
| Weak-coupling dressed Weyl two-point function | Named imported theorem after matching its model hypotheses | Its metric and normalization cannot replace the bare ones silently |

All results here are author proposals pending independent review. The primary
challenges calculations by several methods, but is not independent audit.
The invariant forms and standard Weyl machinery were known during development.
No experimental data, fitted prefactor or empirically selected coupling is used.

## Derivative-free potentials and the graded bracket

Work on a smooth closed spin three-manifold, or with compact support. For the
native comparison use a three-torus with fixed spin structure. The metric g
is positive definite. Write ordinary odd spinors q=(det g)^(-1/4) psi, where psi is
a half-density. At a normal frame the spinor part of the even graded Poisson
bracket obeys {q_a(x),qbar_b(y)}=-i delta_ab delta(x-y); the bracket between
the two odd coordinates is symmetric. Globally the ordinary-spinor delta
has the corresponding invariant-volume normalization. For even F,G, local
right and left derivatives give

    {F,G}=-i sum_a [(F <-d/dq_a)(d/dqbar_a ->G)
                         +(F <-d/dqbar_a)(d/dq_a ->G)].       (1)

In particular {qbar A q,qbar B q}=-i qbar[A,B]q. This identity concerns
Grassmann symbols. Normal-ordering an operator is a separate step.

Let U(q,qbar) be a real even derivative-free local polynomial, without explicit
coordinate dependence and invariant under spatial spin rotations. Add

    V[N]=int N sqrt(det g) U(q,qbar)                           (2)

to a supplied normal generator H[N]. The spinor kinetic part is the symmetric
Weyl operator with arithmetic lapse smearing. The metric kinetic term, if
included, is ultralocal in its momentum and lapse. Its brackets with spinors
may include a configuration connection depending locally on the metric, but
contain no derivatives of the lapse. These are explicit hypotheses; this
note does not establish the original free constraint algebra.

In one normal-coordinate direction its spinor density is

    H_m[N]=-i/2 int N(qbar alpha q' - qbar' alpha q).          (3)

Moving odd variations to the left and integrating by parts gives the left
Euler derivatives -i(N alpha q'+N' alpha q/2) with respect to qbar, and
-i(N qbar' alpha+N' qbar alpha/2) with respect to q. Equation (1) therefore
gives the lapse-gradient parts of the flows

    {q,H_m[N]}=...-(partial_i N) alpha_i q/2,
    {qbar,H_m[N]}=...-(partial_i N) qbar alpha_i/2.           (4)

Define the even derivation B_i by B_i q=alpha_i q/2 and
B_i qbar=qbar alpha_i/2. It uses the ordinary Leibniz rule because this
transformation is even. No commuting substitution for the fields is made.
All flow terms proportional to N cancel against those proportional to M.
The potential self-bracket has no derivative of delta and also cancels.
Metric cross terms are proportional to NM by the stated ultralocality.
Consequently the exact change in the normal bracket is

    {H[N]+V[N],H[M]+V[M]}-{H[N],H[M]}
      =-int sqrt(det g) (N partial_i M-M partial_i N) B^i U. (5)

The frame raises the orthonormal index in this formula. Thus the old normal
bracket is unchanged precisely when B_i U=0 for every i. Necessity is local
and coefficientwise in the exterior algebra: if int(N dM-M dN).C=0 for all
smearings, N=1 first gives div C=0; integrating the general identity then
gives C.grad N=0 for every N, hence C=0. Local cutoff smearings give the same
argument on a noncompact slice. Together with the assumed rotations this
is the proper Lorentz Lie-algebra invariance condition on U. It neither
proves that the free bracket closes nor gives quantum Ward identities.

## The invariant quartic space and its fermionic signs

Use R=q_+ and L=sigma3 q_- for the native cones specified below. Their Weyl
matrices are alpha_i=diag(sigma_i,-sigma_i). Rotations act by the same SU(2)
matrix on both species; boosts act by +sigma_i/2 on R and -sigma_i/2 on L,
and on barred components by the Hermitian conjugates. Define

    n_R=Rbar R, j_R=Rbar sigma R, n_L=Lbar L, j_L=Lbar sigma L,
    r=r0 r1, l=l0 l1,
    U_cross=n_R n_L+j_R.j_L.                                (6)

The left current in (6) uses +sigma by definition; its physical spatial
Weyl current has the opposite sign. Conjugating a pair reverses its order.
The complex charge-preserving quartic invariant space has basis

    r^dagger r, l^dagger l, r^dagger l, l^dagger r, U_cross.  (7)

There are five real Hermitian couplings: the first two, the real and
imaginary Hermitian combinations of the middle pair, and U_cross. Separate
valley phase invariance removes the two pair-transfer combinations and
leaves three real couplings.

Here is a dimension proof. The annihilator-pair representation decomposes as
wedge^2(R plus L)=two scalar copies plus the four-dimensional vector
representation. Complexifying the Lorentz algebra gives two commuting sl(2)
actions. On the mixed pair their associative envelopes generate M2 tensor I
and I tensor M2, whose products span M4. That sector is irreducible and its
commutant consists of scalars; it has no invariant vector. The two scalar
copies admit four pairings with their conjugates and the vector sector one.
Thus there are 4+1 complex invariants. The five independent polynomials (7)
are invariant, so they exhaust the space. Conjugation gives the real count.
The primary separately solves the 36-dimensional component kernel; it also
finds ten rotation-only invariants. That finite calculation is a challenge
of this argument, not its replacement.

With monomial order Rbar0,Rbar1,Lbar0,Lbar1,r0,r1,l0,l1, explicit expansion is

    U_cross=-2 [Rbar0 Lbar0 r0 l0 + Rbar1 Lbar1 r1 l1
                     +Rbar0 Lbar1 r1 l0 + Rbar1 Lbar0 r0 l1]
           =-2 (Rbar L)(Lbar R).                            (8)

For a single Grassmann species the exact identities are

    n_R j_R^i=0, n_R^2=2 r^dagger r, j_R.j_R=-3 n_R^2.      (9)

In particular the single-species density square is invariant. The commonly
used commuting-spinor current identity gives a different quartic reduction;
it cannot establish an obstruction for these fermions. Equations (8)-(9)
follow by expanding two components and using anticommutation, including
r^dagger=r1^dagger r0^dagger. The primary checks both this exterior algebra
and the bilinear bracket against ordinary finite CAR matrices.

## Specified native carrier and its onsite interaction

Choose two orbitals per cell n of Z^3 and the finite-range kinetic symbol

    h0(k)=sin k1 sigma1+sin k2 sigma2
                  +(2+zeta-cos k1-cos k2-cos k3) sigma3,
    1/2<zeta<1, kappa=acos zeta, v=sqrt(1-zeta^2),
    D=diag(1,1,v), y=D^(-1) a n.                            (10)

Its only zeros are (0,0,+/-kappa). Indeed sin k1=sin k2=0 is necessary,
and a pi coordinate makes the third coefficient at least 1+zeta>0. At zero
transverse coordinates the third coefficient is zeta-cos k3. The jets are
(sigma1,sigma2,+/-sigma3)D. The relative sigma3 change of basis in (6) gives
the desired opposite Weyl blocks. The leading normalized envelope expansion is

    c_n=a^(3/2)/sqrt(v)
                 [e^(i kappa n3) R(y)+e^(-i kappa n3) sigma3 L(y)]. (11)

The Jacobian of y makes sum c^dagger c converge to int dy(n_R+n_L) on
fixed smooth envelopes after the oscillatory cross terms vanish.

An actual onsite orbital interaction c_n0^dagger c_n1^dagger c_n1 c_n0 has
phase-zero quartic

    U_site=r^dagger r+l^dagger l+m^dagger m,
    m=r1 l0+r0 l1.                                        (12)

The omitted phases have frequencies +/-2 kappa or +/-4 kappa, which are
nonresonant in (10). The mixed pair m is a triplet component. Directly,

    B_3 U_site=-2 Rbar0 Lbar1 r0 l1+2 Rbar1 Lbar0 r1 l0.    (13)

The first two boosts and third rotation vanish; the first two rotations do
not. Thus this specified onsite leading quartic fails (5). Centering onsite
densities also gives bilinear and constant terms, which are not part of this
quartic classification. Independently rotating the two orbital species
before expanding their native phases would change the operator being tested.
Equation (13) does not rule out other interactions or an acceptable
renormalized infrared theory of this onsite model.

## Complete leading density-kernel classification

Consider real symmetric even orbital kernels, with vacuum-normal-ordered
quartic part

    W=1/2 sum_(n,m,r,s) V_rs(n-m) :n_nr n_ms:,
    Vhat(0)=[[a0,b0],[b0,c0]], Vhat(Q)=[[aQ,bQ],[bQ,cQ]],
    Q=2 kappa e3, s_0=1, s_1=-1.                           (14)

There are six real Fourier values in this restricted family. The density
components from (11) are rho_r,0=Rbar_r R_r+Lbar_r L_r and
rho_r,+Q=s_r Rbar_r L_r, with conjugate at -Q. The name +Q is a convention;
the even kernel makes its reversal immaterial. Phase averaging gives

    U_V=1/2 sum_rs Vhat_rs(0) rho_r,0 rho_s,0
                           +sum_rs Vhat_rs(Q) rho_r,+Q rho_s,-Q. (15)

In the order used for (8), the coefficients are aQ-a0 and cQ-c0 on the two
same-spin mixed monomials, -bQ on each mixed exchange monomial, and -b0 on
each same-valley pair monomial and each opposite-spin diagonal mixed
monomial. Comparing with (7)-(8) proves the equivalence

    U_V is Lorentz invariant
       iff b0=0, a0=aQ+bQ, c0=cQ+bQ;
    then U_V=(bQ/2) U_cross.                               (16)

For clarity, the diagonal mixed monomials in this comparison are
Rbar0 Lbar1 r0 l1 and Rbar1 Lbar0 r1 l0. They occur in no invariant of (7),
so they first force b0=0. The remaining mixed coefficients must match (8),
giving the other two equations. This also proves necessity without relying
on a numerical rank. The three-dimensional allowed Fourier subspace has
only a one-dimensional nonzero quartic image; two directions have zero
local quartic. An orbital-blind kernel sets a0=b0=c0 and aQ=bQ=cQ, and (16)
then requires both values zero. This classifies this leading vertex only.

## A finite density stencil with a nonzero invariant vertex

Let rho3_n=n_n0-n_n1, and choose

    u(+/-e3)=t/2, u(+/-2e3)=-t/2, u(0)=0,
    uhat(q)=t(cos q3-cos 2q3), V_rs=s_r s_s u.               (17)

All other values are zero. Then Vhat(0)=0, while
Vhat(Q)=uhat(Q)[[1,-1],[-1,1]]. By (16),

    U_V=-uhat(Q) U_cross/2,
    uhat(Q)=2t sin(3 kappa) sin(kappa).                     (18)

For t nonzero and (10) this coefficient is nonzero. The endpoint zeta=1/2
would make this particular stencil zero; it is excluded. No uniform
nonzero bound is claimed near either endpoint.

The microscopic interaction is simply

    W=(t/2) sum_n [rho3_n rho3_(n+e3)-rho3_n rho3_(n+2e3)]. (19)

It is Hermitian, translation invariant, even under all coordinate
reflections, and invariant under exchange of the two orbital densities.
Centering each density by 1/2 cancels in rho3 itself. The cells in each
product are distinct, so no onsite CAR contraction adds a bilinear term.

In the native edge/CAR representation, place orbital r at virtual vertex
(2n1+r,n2,n3). Its number is n_nr=(1-B_v)/2. Thus rho3_n=(B_v1-B_v0)/2,
and each term (19) is a finite sum of products of native vertex operators.
The interaction needs no new species or valley projector. For an explicit
kinetic placement, choose candidate y bonds at tails with odd x+y. All x/z
bonds and the other y bonds are protected. A candidate diagonal y hop has
the protected detour +x,+y,-x. An orbital-changing y hop can order its x and
y steps so the y tail has even x+y. Model x hops have virtual x displacement
at most three, and z hops are diagonal in the orbital. Thus all kinetic
terms in (10) have protected paths of length at most three. This edge/CAR
representation is conditional, not uniquely selected by the framework. Each interaction
term in (19) spans at most two z cells and the two orbital vertices.

For physical Hamiltonian (H0+lambda W-nu N_staggered)/a, (11) gives

    g_cross=-lambda a^2 uhat(Q)/(2v).                       (20)

The coefficient t, the density-difference channel and the stencil are
chosen data. Equation (18) exhibits an available invariant interaction;
it does not select these data dynamically.

## Weak-coupling theorem: exactly what is imported

The kinetic symbol (10) is the explicit two-band example in
[Giuliani, Mastropietro and Porta, arXiv:1907.00682v3](https://arxiv.org/pdf/1907.00682v3).
Their equation (2.19) matches (19) with w_rs=s_r s_s u/2: the source has no
outer 1/2 in its interaction. This potential is real, even, finite range,
volume independent after periodicization, and obeys its required reflections.
The two-node kinetic hypotheses are also retained. In particular v1=v2=1,
v3=v and the extracted longitudinal quadratic coefficient is zeta; it is
bounded below by 1/2. Taylor remainders are controlled by sine/cosine
derivatives. Node separation and v are comparable because kappa/sin kappa
is bounded on (0,pi/3). Away from the nodes a compactness bound excludes
zeros, including the endpoint with the merged-node neighborhood removed.

For fixed potential and zeta, Theorem 2.1 supplies an existential small
lambda interval and analytic staggered counterterm nu(lambda), keeping the
nodes fixed. The ground-state two-point function has the dressed Weyl form
of (2.27), with analytic velocities and Z and a vanishing relative remainder.
Volume precedes zero temperature. No threshold, counterterm or dressed
velocity is computed here; no anomaly coefficient is used.

This import controls a different object from (15). It neither identifies
the bare boost metric with the dressed one nor preserves the bare quartic
ratios under renormalization. It supplies no gravitational Ward identity.
At fixed small lambda, the engineering coefficient (20) vanishes as a^2.
Choosing lambda proportional to a^-2 to keep it finite leaves the theorem's
small-coupling domain. Neither engineering observation proves that all
interacting limits fail or that a particular strong-coupling limit exists.

## Smooth matrix elements and a direct even-sector challenge

Fix zeta away from node merger, and smooth compactly supported envelopes
(or compatible periodic ones) of finitely many particles. Expand the finite
normal-ordered quartic using (11). For the nonzero phases, discrete
summation by parts divides by e^(i m kappa)-1 for m=2 or 4; these denominators
are nonzero. Repeated differences of a fixed smooth envelope gain powers
of a. The zero-phase terms give (15). Taylor-expanding the finitely shifted
envelopes and taking the Riemann sum gives the four-leg matrix element with
an O(a) remainder if lambda a^2 stays bounded. Constants depend on fixed
envelopes, potential and zeta. This is neither a many-body operator-norm
estimate nor a ground-state or repeated-interaction convergence theorem.

For a supplied curved metric, weight each bond by the endpoint average of
f=N/sqrt(det g_cone). Since q=(det g)^(-1/4) psi,
N sqrt(det g) U(q)=N U(psi)/sqrt(det g) for a quartic. The same finite-stencil
estimate therefore matches (2). The metric source is prescribed and its
microscopic transformation law is not derived.

An independent calculation path within the author primary uses an even
two-particle Slater state. Set kappa=pi/4, v=1/sqrt(2), L=16,32,64 and
a=2pi/L. Its two waves have internal spinors u and sigma3 vspin, momenta
kappa+a and -kappa+2a along z, and amplitudes L^(-3/2). Distinct allowed
momenta make them orthonormal even when internal spinors overlap. Direct
antisymmetrized position amplitudes yield

    <rho3_n rho3_(n+ell e3)>=2/L^6 [
       (u^dagger sigma3 u)(vspin^dagger sigma3 vspin)
                       -|u^dagger vspin|^2 cos((2 kappa-a)ell)],
    <W>=-|u^dagger vspin|^2
                  [cos(2 kappa-a)-cos(4 kappa-2a)]/L^3       (21)

for t=1. The first term cancels between the two separations. The diagnostic
scaling lambda=v/a^2 gives

    <lambda W/a> -> -v |u^dagger vspin|^2/(2pi)^3,           (22)

equal to the matrix element of -U_cross/2 with normalization (11). The
primary computes amplitudes without inserting (21), for four spinor pairs,
and compares the resulting finite values and a stated O(a) bound. A first
three-pair set was insensitive to removing the relative sigma3 because its
chosen overlaps had equal magnitudes. That ineffective mutation is preserved;
a fourth coherent spinor pair now distinguishes the two operators. Coarse
errors are not required to decrease monotonically. These are states over
the empty Fock vacuum, not the interacting ground state of the imported
theorem. The scaling in (22) is a vertex diagnostic outside that theorem.

## Optional finite filters and their limitation

A second native route helps delimit the onsite finding (13). Finite Laurent
filters f_+(k)=(1+sin k3/v)/2 and f_-(k)=(1-sin k3/v)/2 select the values
1,0 at the respective nodes. Define R_n=f_+ c_n and L_n=sigma3 f_- c_n.
Normal-ordered polynomials r^dagger r, l^dagger l and U_cross then have the
specified leading vertices. Wrong-node leakage on smooth envelopes is O(a).
They are not separate exact canonical species: at v=.8,

    {R_n0,L_n0^dagger}=(1/4-1/(8v^2)) I != 0.              (23)

Their actual six-mode CAR operators are Hermitian and parity preserving.
The exact identity c_i^dagger c_j^dagger c_k c_l
=delta_jk c_i^dagger c_l-(c_i^dagger c_k)(c_j^dagger c_l)
expresses every term through even bilinears. Endpoints in the three adjacent
z cells and two orbital vertices have x/z paths of length at most three.
This alternate construction is not needed for (19) or for its density-class
theorem match; a general filtered quartic is not automatically in that class.

## Negative-claim discipline and open obligations

N1, alternatives: the direct density stencil, finite filters, derivative
interactions, dynamical gauge mediation and different strong-coupling limits
are distinct routes. Only the first two are constructed here. Failure of
the specific onsite symbol does not close the other routes.
N2, independence of restrictions: equation (13) is an algebraic variation;
the small-coupling boundary of (20) is a different analytical domain issue.
Neither proves the other or an axiom-wide obstruction.
N3, hidden hypotheses: fixed cone basis, Grassmann order, charge symmetry,
even density kernels, nonresonant nodes and bare versus dressed objects are
explicit. Dropping them changes the classified family.
N4, residual matching: nonzero renormalized interactions, quantum constraints
and autonomous native geometry are open, not disguised terminal lemmas of
this bounded theorem.
N5, rhetoric: the primary emits five scope resolutions. They are disclosures,
not scientific PASS checks or a negative-packet certificate.
N6, partial closure: (19) directly supplies a nonzero invariant bare vertex
while keeping the finite native density model and its weak-coupling theorem.
N7, steelman: even the onsite model can have useful infrared physics; bare
anisotropy alone does not determine its renormalized observables.
N8, cross-cycle echo: no prior lattice or local-algebra obstruction is promoted
to physical impossibility. The result uses a specified Weyl identification.

The strongest remaining physical target is not a one-step extension of (16):
construct a native interacting continuum with finite physical coupling and
compatible geometry, or prove a precisely quantified obstruction to that
construction. This note does not force a change to any framework axiom.

## Sources, reproduction and review status

The author reread the interaction definitions in sections 2.2-2.3 and the
statement and discussion of Theorem 2.1 of the primary Weyl paper above;
its full multiscale proof was not reconstructed. Its theorem is an import.
For spinor signs, selected section 2 passages around equations 2.52-2.75 of
[Dreiner, Haber and Martin, arXiv:0812.1594v6](https://arxiv.org/pdf/0812.1594v6)
were read. The 313-page review was not read in full. Equations (7)-(9) are
proved here by representations and components rather than imported signs.

Current-main comparisons, read in full, were
`INTERACTING_RP_FULL_ALGEBRA_FIXED_A_GAUGE_INVARIANT_FOUR_FERMION_BOUNDED_NOTE_2026-06-05.md`
and `QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`.
The former concerns a different supplied finite staggered/gauge construction
and leaves its Lorentz continuum open. The latter distinguishes local algebra
from physical boost identification. Neither supplies an audit status here.

Run `python3 scripts/native_weyl_local_interaction_covariance_2026_09_13.py`.
The primary declares this note as input and a 60-second budget. The packet
under `.claude/science/physics-loops/native-local-quartic-20260913/` preserves
source-bound canonical, author review and mutation records. Exact finite
CAR checks challenge the exterior implementation; the direct two-particle
amplitudes challenge the native vertex coefficient. Method diversity within
one author's work does not replace independent mathematical review. No
retained status, main landing or audit verdict is granted by these records.
