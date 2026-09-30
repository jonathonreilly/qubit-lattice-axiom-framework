---
claim_id: native_four_particle_threshold_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied qubit pair Hamiltonian with mu,tau>0: its full fifteen-channel zero-energy four-particle form exists and is strictly positive; compact rational trials give certified upper forms at mu=tau=1; and the fifteen lowest fixed-four-particle periodic levels converge after volume rescaling to that form. No many-particle equation of state, phase or on-shell scattering amplitude is asserted."
upstream_dependencies:
  - minimal_axioms
  - native_qubit_pair_density_onset_bounded_theorem_note_2026-09-30
runner: scripts/native_four_particle_threshold_2026_09_30.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Control compatible many-pair interactions or actual physical cell boundaries before inferring any dilute equation of state."
conditional_surface_status: "A theorem for a supplied Hamiltonian and fixed particle number, with explicitly limited rational variational bounds."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The stated operator and asymptotic results are proved for an explicit full-qubit model; the model and its physical interpretation are supplied."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The actual four-particle threshold and its periodic spectrum

**Type:** bounded_theorem
**Status:** conditional-support (supplied model; unaudited)

Fix mu,tau>0. On the full tensor product of one C^2 per cubic-lattice site,
use b_x=|0><1|, n_x=b_x^dagger b_x and the empty vector Omega. The quantum
state space, expectation rule, basis and the Hamiltonian below are supplied.
They are not selected by the framework axioms, an original walker, or a
physical record construction. No native dimension enlargement is involved.

The theorem concerns four physical occupied sites, at total momentum zero
on Z^3, and the FULL N=4 sector on large odd periodic cubes. Put

    a=min(tau,mu/12), ell(k)=2sum_j(1-cos k_j),
    g=integral_[-pi,pi]^3 dk/[(2pi)^3 ell(k)]<=sqrt(3)pi/8.

There is a Hermitian form T0 on Sym^2 C^5, with the Frobenius norm on complex
symmetric matrices, satisfying

    T0[A]=inf_(chi finite physical orbit support) E(Phi_A+chi),
    T0 >= (2a/g)I_15 >= [16a/(sqrt(3)pi)]I_15.             (1)

The incoming Phi_A is defined below on actual occupation configurations;
it is not a freely assigned bosonic field in the collision region. For any
fixed R>=14, the physical guarded frame V_L and its zero-energy Schur form
S_L, defined in the supporting proofs, satisfy for all sufficiently large
odd L, V=L^3,

    ||V S_L-T0|| <= C_(mu,tau,R)(log L)^(-2/3),
    |V lambda_j(H_4,L)-lambda_j(T0)| <= C_(mu,tau,R)(log L)^(-2/3)
                                                        (j=1,...,15).
                                                               (2)

The remaining spectrum obeys lambda_16>=Delta_L, where

    Delta_L=a/[28000322 R^3+(4+420004830(R+4)^3)L^2].

In particular V lambda_16 grows at least linearly with L, while all fifteen
low levels lie at total momentum zero. The constants are loose; no claim
about the volume where the bound becomes numerically useful is made.

At the SUPPLIED benchmark mu=tau=1 an explicit rational compact trial gives
a positive-semidefinite-order upper matrix for all fifteen channels. Two
of its normalized directional values are

    T0[E1 E1] <= 5107142386779523/24739011624960 < 206.441,
    T0[T12 T12] <= 358372792045843/1374389534720 < 260.751. (3)

The corresponding bare values are 344 and 420. These are strict variational
improvements. They are not exact entries of T0, its eigenvalues, a certified
ordering of physical channels, or evidence for spontaneous anisotropy.
The primary emits the complete rational raw upper form and checks its full
source and residual, rather than inferring a matrix from these two values.

The proof obligations are the full-carrier positive decomposition, the
ordered-removal adjoint lift, compact-source energy continuity, affine
threshold minimization and pin capacity; the guarded physical frame/gap;
the finite and infinite Sobolev/cutoff comparison; and the exact rational
trial. Each is proved in this note or its two owned supporting proofs.
There is no open terminal lemma in the stated fixed-particle theorem.
The strongest additional obligation for a many-particle application is a
compatible, density-uniform interaction lower bound with physical boundary
and higher-cluster errors controlled at the leading energy scale.

The theorem excludes mu=0 or tau=0, even-volume stabilizer conventions,
small periodic cells and growing R or particle number. Those cases have
not been settled by the present constants or limit.

## Law, carrier and positive rows

Write e_i for unit lattice vectors, and D={+/-2e_i,+/-e_i+/-e_j:i<j}.
There are eighteen graph neighbors. Set m_x=sum_(d in D)n_(x+d), N=sum_x n_x,

    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j),
    Q_E1=(d_1-d_2)/sqrt2, Q_E2=(d_1+d_2-2d_3)/sqrt6,
    Q_Tij=(1/2)sum_(s,t) v_ij^(s,t).

The same full-carrier law as the [landed density-onset note](NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md) is

    H=mu N-2mu sum_(x,A=E1,E2) Q_A^dagger Q_A
             -mu sum_(x,A=T12,T13,T23) Q_A^dagger Q_A
      +mu sum_x n_x binom(m_x,2)
      +tau sum_(x,j,A)|Q_A(x+e_j)-Q_A(x)|^2.              (4)

Here |O|^2=O^dagger O. The last sum is W. Its interaction diameter is four;
this is not a derivation of a nearest-neighbor admissibility rule. Define
D0=sum_i d_i and the nonnegative diagonal operator
Ddiag=sum_x n_x(m_x-1)(m_x-2)/2. Direct completion of squares gives

    H=S+mu Ddiag+W,
    S=(2mu/3)sum_x|D0(x)|^2
       +(mu/4)sum_(x,i<j)sum_(r<s)|v_ij^r(x)-v_ij^s(x)|^2. (5)

To check the carrier multiplicity, axial edges have one center and plane
edges two. Thus2sum d_i^dagger d_i+sum v_r^dagger v_r=sum_x n_x m_x.
The four-word identity sum_(r<s)|v_r-v_s|^2=4sum|v_r|^2-|sum v_r|^2,
the E projector, and1-m+binom(m,2)=(m-1)(m-2)/2 prove(5) on every occupation
sector. Positivity uses the integer values of m, not a classical-state
restriction. All summands conserve particle number.

Let Egrad15=sum_(x,j,t)||[B_t(x+e_j)-B_t(x)]psi||^2 for all three d and
twelve signed v. The orthogonal singlet/E split and each plane's
constant/orthogonal split, together with ||gradient f||^2<=12||f||^2, give

    Egrad15<=6 S_E/mu+12 S_T/mu+W/tau,
    E(psi)>=mu<Ddiag>+a Egrad15.                         (6)

This is a SIMULTANEOUS bound: S+W supply the gradients before mu Ddiag is
added. Adding separately known lower bounds on H would not justify(6).

## Pair normalization and the actual fifteen channels

Use nine unique forward edges d=2e_i,e_i+eta e_j (i<j,eta=+/-1). Translate
axial midpoint anchors and discard the duplicated plane-gradient copy.
For an unordered edge represented as{x,x+d}, the uniform normalized pair
amplitudes form a real 9 by 5 matrix U. The three axial rows are

    (1/sqrt2,1/sqrt6,0,0,0),
    (-1/sqrt2,1/sqrt6,0,0,0), (0,-2/sqrt6,0,0,0).

For each plane ij its two rows have entry -eta/sqrt2 in the T_ij column
and zero elsewhere. Then U^T U=I5. This includes the factor 1/sqrt2 needed
because the original uniform Q_T sum has pair norm squared2V, whereas the
E sums have norm squaredV. Define the formal uniform creators
C_a^dagger=sum_(x,d)U_(d,a)b_x^dagger b_(x+d)^dagger.

For a symmetric complex 5 by 5 matrix A, define Phi_A on every four-site
occupation as the coefficient of

                  (1/sqrt2)sum_(a,b) A_ab C_a^dagger C_b^dagger Omega. (7)

All matchings of that occupation are summed; overlaps vanish by the actual
qubit algebra. For two well separated graph edges d,e the coefficient is
sqrt2(UAU^T)_(d,e). The fifteen-dimensional norm is ||A||_HS: an off-diagonal
orthonormal basis vector has its two entries1/sqrt2. No independent dimer
coordinates are introduced for multiply matchable configurations.

On a separated pair, each individual constant U wave is killed by S and W,
and Ddiag=0. Every nonzero positive row of Phi_A is therefore supported in
a bounded collision region. Thus E(Phi_A) is finite and F_A=H Phi_A is a
compact physical source on four-site translation orbits. This source can
include nonmatching configurations after a pair moves. They must be retained.

## A compact-source inverse from physical removal amplitudes

The K=0 Hilbert space is l2 of unordered four-site translation orbits, with
one coefficient per orbit. Finite sets in Z^3 have no translation stabilizer.
For a graph residual e and removed edge d, set

    (Tpsi)_(d,e)(r)=psi({0,e,r,r+d}) if all four sites are distinct,
                   0 otherwise.                        (8)

This T is unscaled. Resolving the actual annihilation outputs in(6) and
retaining graph residuals proves

    E(psi)>=a sum_(d,e)||gradient(Tpsi)_(d,e)||_2^2
                                      +mu||Q_nm psi||_2^2. (9)

Here Q_nm selects physical configurations with no graph perfect matching.
A four-vertex graph with no matching either has an isolated vertex or, if
none, is a three-leaf star. In either case Ddiag>=1. This proves the second
term. Equation(9) can also be obtained by placing any finite orbit vector
in larger physical cubes, translating, and dividing its forms by volume;
it is a statement at K=0, not an unproved exceptional-fiber assertion.

For a compact physical source r, split it into r_P+r_Q according to matching.
If a matching configuration has m perfect matchings, it has2m DISTINCT
ordered residual/removed representations in(8). Assign to each coordinate
g_(d,e)(r)=r_P(S)/(2m). Then

                  <r_P,psi>=sum_(d,e)<g_(d,e),(Tpsi)_(d,e)>. (10)

Different physical orbits never share a coordinate. This is an exact
adjoint lift, including all multiple-match multiplicities. Fourier Cauchy
on Z^3 and direct-sum Cauchy in(9) give

    |<r,psi>|^2<=C(r)E(psi),
    C(r)=||r_Q||^2/mu+(1/a)sum_(d,e)<g_(d,e),ell^-1 g_(d,e)> < infinity. (11)

Indeed ell(k)>=4|k|^2/pi^2 and the three-dimensional singularity is
integrable. Integrating over the circumscribed sphere gives the bound on g
above; each Green term is at most g||g_(d,e)||_1^2.

The bounded actual realization obeys0<=H_4<=16mu+144tau. The positive
occupation term is at most12mu in N=4, while mu N=4mu; the attractive term
can be dropped for this upper bound. The two-body gradient norm is at most
24tau, and summing the six possible removed pairs bounds W_4 by144tau.
Thus(11) extends from compact to l2 vectors. For epsilon>0,

 <r,(H_4+epsilon)^-1r>
 =sup_psi[2Re<r,psi>-E(psi)-epsilon||psi||^2]<=C(r).       (12)

Monotonicity as epsilon decreases and complex polarization define a finite
form G_H(0) on every compact source. This is not a bounded inverse on all l2.

Complete compact physical vectors in the energy norm. By(11) each coordinate
functional is continuous. Every positive row is a finite combination of
coordinates, so completion elements are faithful physical profiles: if all
coordinates vanish, every limiting row vanishes, hence the energy element
is zero. Compact r has a unique Riesz representative in this completion.
The representatives (H+epsilon)^-1r converge in energy because their squared
spectral error is the integral of epsilon^2/[lambda(lambda+epsilon)^2],
dominated by1/lambda from(12). They need not converge in l2. In particular
no nonzero l2 vector has zero energy, but a threshold response can be non-l2.

## Threshold form, normalization and strict positivity

For compact chi the literal row identity is

 E(Phi_A+chi)=E(Phi_A)+2Re<chi,F_A>+E(chi).

It extends to the faithful energy completion by(11). Riesz minimization
there proves

    T0[A]=E(Phi_A)-<F_A,G_H(0)F_A>.                       (13)

This equals the compact infimum in(1) by definition of the completion,
and the l2-correction infimum by density and bounded H. The correction
minimizer is unique in the energy completion and solves H psi=0 pointwise.
The incoming row vector has finite support, so this is a nonnegative affine
projection problem. No normalizable minimizer is assumed.

For every d,e, the field T(Phi_A+chi) equals the constant
sqrt2(UAU^T)_(d,e) plus a compact correction. At the COMMON anchor r=0 it
vanishes by hard-core overlap. Scalar Fourier Cauchy gives
|u(0)|^2<=g||gradient u||^2 for compact u. Apply this to all 81 components,
then(9), to obtain E(Phi_A+chi)>=(2a/g)||UAU^T||_HS^2.
Since U^T U=I this proves(1) for every complex A. Fixed compact corrections
may first be embedded in sufficiently large odd tori; no finite-torus
constant-mode Green inverse is substituted for g.

The term “threshold” here means precisely the zero-energy quadratic form
(13). Positive-energy on-shell scattering, a scattering length convention,
resonance asymptotics beyond this energy domain, and a physical phase have
not been identified by this theorem.

## Periodic geometry and convergence

The complete construction and estimates are in the two owned supporting
proofs [physical periodic band](NATIVE_FOUR_PARTICLE_PERIODIC_BAND_PROOF_2026-09-30.md)
and [threshold limit](NATIVE_FOUR_PARTICLE_THRESHOLD_LIMIT_PROOF_2026-09-30.md).
They are parts of this single claim unit and primary inputs, not imported
unlanded lemmas. The band proof constructs guarded pair bookkeeping while
retaining residual particles, proves a physical gap Delta_L outside a
rank15 polar frame, and bounds its trial energy O(V^-1). It never replaces
the actual carrier by an unconstrained boson space. The limit proof retains
all ordered-removal amplitudes, the 81 simultaneous hard-core pins, the
physical compact-response domain, torus normalization and logarithmic cutoff
errors. It supplies both inequalities in(2), with no assumption of a
square-summable zero-energy minimizer.

Odd L is used for a concrete normalization reason. A translation stabilizer
of a four-set acts freely on its four vertices; its order divides4 and the
odd group order L^3, so it is trivial. Raw orbit coefficients therefore have
physical torus norm V times their orbit norm. A repeated orbit or a factor
sqrt(V) cannot be silently discarded in the Schur limit.

## Exact compact rational upper forms

The primary uses raw one-pair coordinates x=(u1,u2,v12,v13,v23), u3=-u1-u2.
An axial edge has weight ui and a plane edge e_i+eta e_j weight -eta vij.
For a four-set S let M_x(S) be the sum of the three matching weight products.
The fifteen raw monomials p(x)=(x_i x_j:i<=j) have coefficient vector M(S).
This is the physical coefficient of C_x^dagger squared/2. For normalized
z in the five U modes, x=Lz with

    u1=z1/sqrt2+z2/sqrt6, u2=-z1/sqrt2+z2/sqrt6,
    vij=z_Tij/sqrt2.

Writing q(z)=(z_i^2,sqrt2 z_i z_j:i<j) in the same ordered symmetric basis,
p(Lz)=P q(z). The physical incoming coefficient is sqrt2 M_x. Hence a raw
quadratic upper form Q gives the physical matrix2P^*QP. This factor is
checked with the literal qubit pair creation and all fifteen overlaps.

At mu=tau=1 use the1487 connected matching translation orbits as a compact
trial support. Connectivity is in the actual18-neighbor graph; no nonmatching
source or response outside that support is deleted. Let H12=12H, B12=12E(M),
F12=H12 M, A12 the actual H12 core compression. The controlled input Xi is
an integer1487 by 15 matrix with denominator d=65536. It was proposed by
rounding a floating core solve; its validity requires only its exact bytes.
No accuracy assumption about that solve is a theorem premise. The primary
reconstructs A12, all of F12 and the action on Xi from the stated law. For
chi=Xi/d,

    Qnum=d^2 B12+Xi^T A12 Xi+d(F12^T Xi+Xi^T F12),
    Q=Qnum/(12d^2),
    Rnum=d F12+H12 Xi,    r=Rnum/(12d).                  (14)

Here core products use the restricted rows of F12, whereas Rnum retains
its complete physical support. No periodic wrapping or finite-box inverse
enters these exact formulas. Since0<=H4<=160, adding the compact correction
-r/160 reduces the energy by at least ||r||^2/160. Consequently

    T0 <= 2P^* [ (1920 Qnum-Rnum^T Rnum)/(23040 d^2) ] P. (15)

The primary emits this full rational raw matrix; the displayed exact change
of basis defines its full physical fifteen-channel form. Its two displayed physical directional values give(3). A second
upper bound on the same quantity cannot establish channel ordering.

## Evidence, dependencies and unresolved frontier

All load-bearing infinite-volume and finite-volume statements are proved
above or in the two owned proofs. The numerical primary is a source-bound
finite diagnostic: exact occupation/action and positive-row reconstructions,
full compact rational-source/residual checks, normalization and finite pin
controls. These tests support rather than replace the proofs of uniform
bounds, completion, convergence and spectral separation. Author code is
reused and integrated openly; focused campaign checks are not formal review
of this newly authored unit. The canonical cache, its mutation evidence and
its provenance record give the actual executed scope and identities.

This extends the supplied model of the landed density-onset note, whose
positivity/gradient argument was restated here. Current axiom and primitive
registries do not select mu,tau, the Hamiltonian, quantum expectations or a
realized state; no empirical constants are fitted. No external dilute-gas,
scattering-completeness or de Finetti theorem is imported. No historical
priority is asserted. Other open supplied-walker or record constructions
are not inputs to this argument.

The fixedN4 result does not give a uniform many-pair Schur expansion,
physical lower cell-boundary law, exact dilute equation of state, condensate,
ODLRO, polarization selection, apparatus coupling or original-record limit.
The positive threshold lower form and rational upper forms do not close
those obligations. Integration, formal source review and audit remain
separate requirements.
