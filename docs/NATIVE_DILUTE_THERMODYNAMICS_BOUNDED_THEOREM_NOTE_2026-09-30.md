---
claim_id: native_dilute_thermodynamics_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: "For the supplied full-qubit pair Hamiltonian with fixed mu,tau>0: the mean-density thermodynamic energy has dilute coefficient t0/8, the grand energy and every thermodynamic ground-density accumulation have coefficients -2/t0 and 4/t0, and the ordered exact-number dilute energy envelopes equal t0/8, where t0 is the coherent minimum of the full physical fifteen-channel threshold form."
upstream_dependencies:
  - minimal_axioms
  - native_qubit_pair_density_onset_bounded_theorem_note_2026-09-30
  - native_four_particle_threshold_bounded_theorem_note_2026-09-30
runner: scripts/native_dilute_thermodynamics_2026_09_30.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Investigate actual pair correlations and collective excitations for the same supplied model."
conditional_surface_status: "Dilute thermodynamic statements for the explicit full-qubit model and ordered limits."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The operator estimates and limits are derived for a supplied Hamiltonian; its physical selection and quantum interpretation are separate inputs."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Dilute thermodynamics of a local qubit pair Hamiltonian

**Type:** bounded_theorem
**Status:** conditional-support (supplied model; unaudited)

**Target.** For the unchanged explicit full-qubit pair Hamiltonian with fixed
mu,tau>0, prove that its actual fifteen-channel four-particle threshold form
determines the leading dilute mean energy, grand energy, grand-ground density
and ordered exact-particle-number energy envelopes.

The Hilbert tensor product, basis, quantum expectation rule, Hamiltonian and
chemical-potential perturbation are supplied mathematical objects. The theorem
uses the actual two-dimensional site factors and all physical occupation
configurations. It does not select a framework Hamiltonian or a realized state.
The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix that premise boundary;
the approved units, kinetic-form and realized-state grants are left unchanged.

## Quantified statement and proof map

On periodic cubes with V=L^3 define N=sum_x n_x and

    e_L(rho)=min_(Gamma>=0,Tr Gamma=1,Tr Gamma N=rho V) Tr(Gamma H0)/V,
    g_L(nu)=min spec(H0-nu N)/V,
    E_L(N)=min spec(H0 restricted to exact particle number N).

Let T0 be the full physical zero-energy threshold form on Sym^2 C^5 with
its Frobenius norm and actual incoming normalization defined below. Put

    t0=min_(||z||=1)<z tensor z,T0 z tensor z>,
    a=min(tau,mu/12), c0=a/99090432.

This is a coherent minimum of a full fifteen-channel form, not its least
unrestricted eigenvalue. Strict positivity T0>=2a/g gives t0>0. All conclusions
hold for each fixed positive mu,tau; no uniform zero-coupling limit is asserted.
The limits e(rho)=lim_L e_L(rho) for0<=rho<=1/2 and g(nu)=lim_L g_L(nu)
for real nu exist. At volume first and then rho or nu decreasing to zero,

    e(rho)=t0 rho^2/8+o(rho^2),
    g(nu)=-2nu^2/t0+o(nu^2),
    rho_gr(nu)=4nu/t0+o(nu).

The last statement holds uniformly over EVERY thermodynamic accumulation
of densities of finite-volume grand-ground density matrices, including
degenerate ground eigenspaces. It is an onset ratio, not a differentiability
or compressibility assumption. Their internal energy density is
2nu^2/t0+o(nu^2). For nu<0 the vacuum is the finite-volume ground state.

For every family of integer sequences with N_L(rho)/L^3 -> rho at each fixed
rho>0, both ordered canonical dilute envelopes satisfy

    lim_(rho down0) liminf_(L->infinity) E_L(N_L(rho))/(L^3 rho^2)
      =lim_(rho down0) limsup_(L->infinity)
                            E_L(N_L(rho))/(L^3 rho^2)=t0/8.

Odd particle numbers and nondivisible volume sequences are included. Equality
of the two canonical envelopes at each fixed nonzero rho is not a conclusion.
Neither an unrestricted simultaneous L,rho limit nor any joint finite-size
rate is used. The mathematical results concern energies and mean densities;
phase, ODLRO, state polarization, excitation spectra, preparation efficiency,
original-record observables and physical-source identification remain outside
the claimed conclusions.

The complete proof has the following dependencies, with no target-equivalent
terminal lemma left open inside this quantified statement:

* The [landed density theorem](NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md) supplies the actual law,
  simultaneous bare gradients, local spectator pin and all-density coercivity.
  Its conditional supplied-model hypotheses are retained here.
* The exact stacked [threshold theorem](NATIVE_FOUR_PARTICLE_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-30.md) supplies the full physical
  N4 energy completion, compact-source inverse and strict positivity. Its
  supporting proofs and source are inherited provisional inputs of this
  coherent unit, with exact base identity in the delivery provenance.
* The [physical boundary proof](NATIVE_DILUTE_PHYSICAL_BOUNDARY_PROOF_2026-09-30.md) proves safe open cells, boundary
  penalty averaging, actual spectator pins, guarded compression/gap and full
  relative Neumann capacity with the physical matching constraints.
* The [cell-interaction proof](NATIVE_DILUTE_CELL_INTERACTION_PROOF_2026-09-30.md) constructs actual compact collision
  corrections and a compatible centered residual, pricing high components,
  boundary clusters, all internal tensors and the comparison penalty. Its
  limits are fixed particle number followed by ordered deformation limits.
* The [lower and limits proof](NATIVE_DILUTE_LOWER_AND_LIMITS_PROOF_2026-09-30.md) proves the R-cubed bad-particle bound,
  exact finite-five-mode sphere identity, actual particle-number tail cutoff,
  uniform all-state dilute lower, mean/grand limits, concave density secants
  and deterministic exact-number block transfer.
* The full unitary variational upper with a volume-uniform remainder is proved
  below. It reaches every finite compact threshold correction before taking
  its infimum; no l2 threshold minimizer is assumed.

These are one argument. Periodic block Hamiltonians occur only in the bounded
norm thermodynamic/upper transfer. Physical lower cells retain their real
boundary rows and an explicit penalty debit. Internal fragmentation is priced
through the finite-mode identity rather than excluded by a state ansatz.

## Actual law and pair normalization

At each site use b_x=|0><1|, n_x=b_x^dagger b_x and Omega the empty product
vector. Distinct sites commute and b_x^2=0. The graph offsets are
D={+/-2e_i,+/-e_i+/-e_j:i<j}, with18 neighbors, and m_x=sum_(d in D)n_(x+d).
The literal bare/collective annihilators are

    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j),
    Q_E1=(d1-d2)/sqrt2, Q_E2=(d1+d2-2d3)/sqrt6,
    Q_Tij=(1/2)sum_(s,t) v_ij^(s,t).

P_E and P_T denote the sums of Q^dagger Q in their two and three components.
The law is

    H0=mu N-2mu sum_x P_E(x)-mu sum_x P_T(x)
          +mu sum_x n_x binom(m_x,2)
          +tau sum_(x,j,A)|Q_A(x+e_j)-Q_A(x)|^2.

It is finite range, of interaction diameter four, and number conserving.
The exact full-carrier completion is H0=S+mu Ddiag+W, where

    S=(2mu/3)sum_x|d1+d2+d3|^2
       +(mu/4)sum_(x,i<j,r<s)|v_ij^r-v_ij^s|^2,
    Ddiag=(1/2)sum_x n_x(m_x-1)(m_x-2)>=0.

Axial edges have one center and plane edges two. Thus
2sum d_i^dagger d_i+sum v_r^dagger v_r=sum n_x m_x; the four-word difference
identity and1-m+binom(m,2)=(m-1)(m-2)/2 prove this completion. Splitting
collective and orthogonal components and using the lattice gradient norm
bound12 gives the SIMULTANEOUS inequality

    H0>=mu Ddiag+a Egrad15.

The fifteen gradients are those of all literal d and signed v fields.
The density source proves this and H0>=c0 N(N-2)/V on every sector.

Use nine forward graph edges d=2e_i,e_i+eta e_j. Their constant normalized
pair amplitudes form U with axial columns(1,-1,0)/sqrt2 and(1,1,-2)/sqrt6,
and one column(-1,+1)/sqrt2 on each plane's two orientations. U^T U=I5.
This corresponds to R=(Q_E1,Q_E2,Q_T12/sqrt2,Q_T13/sqrt2,Q_T23/sqrt2).
For symmetric complex A the physical incoming four-site profile is the
literal coefficient of

    Phi_A=(1/sqrt2)sum_(a,b) A_ab C_a^dagger C_b^dagger Omega,
    C_a^dagger=sum_(x,d)U_(d,a)b_x^dagger b_(x+d)^dagger.

Every alternative matching is summed and every overlap vanishes. At two
separated edges the amplitude is sqrt2(UAU^T)_(d,e). The threshold is
T0[A]=inf_(finite physical orbit support chi) E(Phi_A+chi), not a free-dimer
assignment in the collision core. Its energy completion and strict positivity
are exactly those of the threshold input. No numerical T0 eigenvalues or
channel ordering are assumed in any coefficient here.

# Uniform compact-correction upper on the full physical carrier

## 1. Exact physical variational state

Write the landed model as H0=sum_x h_x, with

 H0=mu N-2mu sum PE-mu sum PT+V3+W,
 W=tau sum_(x,j,A) [Q_A(x+e_j)-Q_A(x)]* [Q_A(x+e_j)-Q_A(x)],
 V3=mu sum_x n_x binom(sum_(d in G)n_(x+d),2),
 G={+/-2e_i,+/-e_i+/-e_j:i<j}.

All b_x=|0><1| are the physical site operators. The five Q, their hard-core
products and their shared-center normalizations are those of the current
native density source, unchanged. Let
R=(QE1,QE2,QT12/sqrt2,QT13/sqrt2,QT23/sqrt2). For z inC5, ||z||=1, put

 C_z^dagger=sum_(x,A) z_A R_A(x)^dagger,
 A_z=C_z^dagger-C_z.

On every sufficiently large periodic torus, H0 Omega=0 and
H0 C_z^dagger Omega=0, with ||C_z^dagger Omega||^2=V. This uses the exact
q0 single-pair Gram, not canonical pair commutators. H0 and N conserve
particle number and H0 is nonnegative on the FULL carrier.

A finite four-site configuration S has no nonzero translation stabilizer on
Z3. Choose one representative S_sigma for each translation orbit. Let chi
have finite support in this physical N4 orbit basis. Define

 W_sigma^dagger=product_(x in S_sigma) b_x^dagger,
 X_chi=(1/sqrt2)sum_(sigma,t)
             [chi_sigma W_(S_sigma+t)^dagger-conj(chi_sigma) W_(S_sigma+t)],
 psi_L(u)=exp(u^2 X_chi) exp(u A_z) Omega,  u real.          (1)

This is an exact normalized state on all physical M2 sites. It is not a
truncated vector, a state of independent pairs, or a projection onto a
chosen matching. All four-site creation words obey original hard-core
exclusion; different pairings of the same occupation word still interfere.
For each fixed chi, X is a bounded finite-range interaction with four-site
terms, though its range can grow when improving the threshold approximation.
No preparation efficiency or physically selected source is claimed.

## 2. Uniform local commutator bounds

The landed grouping has ||h_x||<=h_*=182mu+240tau and support at most25sites.
This is a grouping bound, not a global norm made independent of volume.
For completeness, 153 triple terms contribute153mu; the onsite plus E/T
attractions give(1+16+12)mu; fifteen gradient squares give240tau. All their
sites lie among x, its six nearest neighbors and its18 length-two neighbors.

Expand A_z into literal two-site terms d_e B_e^dagger-conj(d_e)B_e, allowing
repeated physical pairs from distinct centers. Each such anti-Hermitian term
has norm|d_e|: it couples |00> to |11> and annihilates the other two states.
Let ell_z be the sum of absolute primitive coefficients at one center.
The coefficient sums of the five R fields are

 (sqrt2,4/sqrt6,sqrt2,sqrt2,sqrt2),
 ell_z<=sqrt(32/3),   alpha=4ell_z.

Each translated two-site term meets a specified site in at most two positions,
so the per-site sum of A-term norms is at most2ell_z. A commutator therefore
costs at most alpha times the size of the current support. This overcounts
shared-center words harmlessly. Similarly set

 m_chi=(1/sqrt2)sum_sigma |chi_sigma|,   beta=8m_chi.

A four-site X-term has norm|chi_sigma|/sqrt2 and has four possible translates
through each site. Its commutator costs at most beta times support size.
Each A step adds at most one site and each X step at most three; using three
for both gives a convenient common bound. Define

 F_m(s)=product_(j=0,...,m-1)(s+3j), F_0(s)=1.

For ANY prescribed sequence of r A and s X commutators acting on an operator
O with initial support q,

 ||ad_A^r ad_X^s O||<=alpha^r beta^s F_(r+s)(q)||O||.      (2)

The notation denotes that particular ordered nesting; the same bound works
for every interleaving. Proof: expand into local connected sequences, drop
every disjoint commutator, bound each one by2 times the local norm, and count
choices using the current support cardinality. Repeated terms are included.
It is not assumed that the sum of all sequences itself has small support.
Summing the h_x gives (2) timesVh_* with q25, and summing n_x gives V withq1.
The constants depend on chi and couplings, never onV. Any fixed-chi torus
large enough to embed its terms has these bounds; global occupation remains
unrestricted. Spatial range affects that embedding size, not the cardinality
bound. This is why no V*u^2<<1 hypothesis is needed.

## 3. An actual uniform sixth-order energy remainder

For anti-Hermitian A and realu, conjugation exp(-uA) O exp(uA) is norm preserving.
Integral Taylor remainder therefore bounds orderm by
|u|^m ||ad_A^m O||/m!, and likewise for X at parameteru^2.
The number phase exp(i pi N/2) fixes H0,N,Omega,X and sends A to-A.
Every vacuum expectation used below is even inu.

Expand the X conjugation to second order, then the A conjugations:

 e^(-u^2X) H0 e^(u^2X)
 =H0+u^2[H0,X]+(u^4/2)[[H0,X],X]+R_X,
 ||R_X||<=|u|^6 ||ad_X^3 H0||/6.

The H0-only expectation has no terms through degree3, because H0 kills both
Omega and A Omega; its degree5 also vanishes by parity. For [H0,X], the
vacuum expectation is zero, odd derivatives vanish, and retaining its
A-degree2 leaves an orderu4 remainder, multiplied byu2. For the double-X
term retain its vacuum expectation; its first A derivative is zero and its
remaining second-order error is multiplied byu4/2. Thus

 |<H0>_(psi_L(u))/V - e4_L u^4| <= D_chi |u|^6,           (3)
 D_chi=h_*[alpha^6 F6(25)/720
          +alpha^4 beta F5(25)/24
          +alpha^2 beta^2 F4(25)/4
          +beta^3 F3(25)/6].

This is an integral remainder for the full unitary state, valid at every
realu with its stated loose bound. It is not a finite-volume asymptotic with
an unspecified V-dependent error. All orderings are kept in the double
conjugation; no BCH commutativity is used.

The same calculation for N needs only the fourth-order remainder. Its pulse
part has second coefficient2V. The single-X commutator has zero vacuum and
first-A expectation because it changes particle number by4; the double-X
remainder is already orderu4. Therefore

 |<N>_(psi_L(u))/V-2u^2|<=B_chi u^4,                      (4)
 B_chi=alpha^4 F4(1)/24
          +alpha^2 beta F3(1)/2+beta^2 F2(1)/2.

These statements hold for complexz andchi. The number phase is enough for
parity; no reality assumption on the state is being imposed.

## 4. Identifying the coefficient without losing identical-pair factors

The vector expansion at fixed finite volume gives

 psi_L(u)=Omega+u C_z^dagger Omega
       +u^2[(C_z^dagger)^2 Omega/2 -V Omega/2 +X_chi Omega]+O_L(u^3).

Indeed C_z C_z^dagger Omega=V Omega. Because H0 kills the first two vectors,

 e4_L=V^-1 <(C_z^dagger)^2 Omega/2+X_chi Omega,
                  H0[(C_z^dagger)^2 Omega/2+X_chi Omega]>.  (5)

Only this coefficient calculation uses a fixed-volume vector expansion;
(3) supplies the uniform error for the actual state. The vacuum component
is harmless because H0 Omega=0.

In the infinite translation-orbit convention of the threshold source,
Phi_z is the physical matching profile(C_z^dagger)^2 Omega/sqrt2.
Let F_z=H4 Phi_z; it has FINITE relative support and finite row-square energy
E_bare(z). The bounded N4 operator obeys0<=H4<=16mu+144tau.
For finite-supportchi define

 E_z(chi)=E_bare(z)+2 Re<chi,F_z>+<chi,H4 chi>.             (6)

Every term in (6) is an actual physical configuration form. For a sufficiently
large torus, the finitely many compact orbits inchi,F and H4chi have no
translation identifications, and their normalized orbit vectors are
V^-1/2 sum_t |S+t>. The X definition gives
X_chi Omega=sqrt(V/2) chi_L, while(C_z^dagger)^2 Omega/2 corresponds to
sqrt(V/2) Phi_z,L. Hence(5) equals

                         e4_L=(1/2) E_z(chi).             (7)

The incoming profile is not square summable on the infinite relative space.
Equation(7) does NOT assert an isometry of the entire finite-torus N4 fiber.
Far-separated torus configurations may have translation stabilizers. They
are outside the compact collision/source supports and cannot change(6):
the original N2 zero equations cancel H Phi exactly for separated pairs.
Equivalently the bare pulse coefficient is a finite connected commutator
coefficient, so embeds locally without depending on those distant orbits.
The fixed finite cross term andchi term then embed directly. Choose L larger
than twice the diameter of all these finitely many connected supports and
any translated overlaps needed by the four commutators. Such a finite L_chi
exists; no all-size alias assertion or fixed cutoff independent ofchi is used.

The profile normalization in(7) fixes the factor one-half before every
threshold minimization. It follows from the literal creator coefficient and
physical orbit normalization, rather than a pair-boson convention.

## 5. Reaching the physical relaxed threshold infimum

The physical threshold theorem defines

 T(z)=inf_(chi in l2) E_z(chi)
     =E_bare(z)-<F_z,G_H(0)F_z>,  T(z)>0.                 (8)

Strict positivity follows from T0>=2a/g in the threshold source. The zero-energy
minimizer need not belong tol2. This causes no gap here. Its resolvent
approximants chi_epsilon=-(H4+epsilon)^-1 F are inl2 and approach the infimum
in quadratic-form value, by the finite inverse form proved there. Since H4 is
bounded and F is finite, finite-support approximations of any chi_epsilon
converge in(6). Thus for everyepsilon>0 there is a FINITE chi with

                 T(z)<=E_z(chi)<=T(z)+epsilon.            (9)

Neither an l2 limiting minimizer nor a numerical Green-matrix evaluation is
assumed. The state(1), with this fixedchi, equations(3)-(4),(7) and its explicit
finite constants provide the desired actual many-particle upper embedding.
The order is fixedaccuracy -> fixedchi -> arbitrarily largeL -> smallu.
The remainder constants may diverge asaccuracy tends tozero; they are never
used uniformly inthat further limit.


## Evidence and source-review boundary

The proofs above and in the three owned proofs carry the all-volume and
infinite-volume quantifiers. The primary is a bounded finite control of
literal pair words, boundary row/anchor structure, centered-source and
finite-mode normalization, and exact-number bookkeeping. It does not compute
a thermodynamic ground state or certify an infinite limit by extrapolation.
Its actual source, input identities, execution cache and scratch mutation
records are recorded in the unit pack after execution. An unexecuted check
is not a result. Author reuse of earlier controls is disclosed explicitly.

Earlier focused independent reconstructions checked the source-bound campaign
lemmas. They remain evidence about those frozen sources, with their actual
independence limits; they are not formal source review of this newly composed
unit. A historical boundary control used837 complete plane-family rows on a
5-cube, a strict subset of the1017 individual complete rows. The preserved
clarification and independent control bind that distinction. The mathematical
proof uses complete individual rows; no numerical C_pin value is imported.

No historical priority claim is made. The exact finite-dimensional sphere
identity is derived here; no external dilute-gas theorem is imported. The
provisional threshold base, supplied model and quantum interpretation remain
explicit dependencies. No authority, primitive, audit status or source law
is changed. Integration and audit remain separate requirements.

Historical author preparation, actual failed controls, mutation results and source-review provenance remain recoverable through [PR #9413](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9413) at frozen head `d6197654f4100621083f72a421da2b8aff6b7391`. They are provenance, not current proof premises or audit authority. The canonical argument and its linked current supporting proofs own the theorem; finite runner controls do not supply its analytic quantifiers.
