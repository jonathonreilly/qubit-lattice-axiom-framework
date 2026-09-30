---
claim_id: native_qubit_pair_density_onset_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: "For the explicitly defined finite-range Hamiltonian on one tensor-factor qubit per site of each cubic torus L>=5, positivity, an exact six-dimensional ground kernel, volume-uniform particle-density coercivity and two-sided chemical-potential onset bounds. The Hamiltonian, quantum state space and expectation rule are supplied. No phase, tensor polarization, physical record instrument or framework-law selection is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/native_qubit_pair_density_onset_2026_09_30.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Determine the interacting collective channels and an actual record observable for this supplied model."
conditional_surface_status: "The stated finite-volume inequalities hold for the explicitly supplied qubit Hamiltonian."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A constructive many-particle theorem for a specified local model; its Hamiltonian and physical identification are not derived from the framework."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A local qubit pair Hamiltonian with controlled density onset

**Type:** bounded_theorem
**Status:** proposed_retained

The proposed classification is a conditional mathematical theorem. Formal
audit remains required; author computations and focused checks confer no
retained grade. Here “qubit” means the actual two-dimensional tensor factor
at each site, with commuting operators at distinct sites. No bosonic pair
replacement is made.

**Target.** Prove positivity, the exact finite-torus ground kernel, and
volume-uniform upper and lower density/energy bounds near zero chemical
potential for the Hamiltonian explicitly defined below.

For every L>=5, V=L^3, and mu,tau>0, define

    a=min(tau,mu/12), c=a/99090432,
    A=10199347200(182mu+240tau), B=3870720.

The theorem is

    H0>=c N(N-2)/V,    H0>=0,
    ker H0=span{Omega, sum_x Q_A(x)^dagger Omega : A=1,...,5}.

The span has dimension six. For Hnu=H0-nu N and nu>0, every finite-volume
ground-state density matrix has particle density rho satisfying

    nu/(A+nu B) <= rho <= min(1,nu/c+2/V),                 (1)
    -(nu+2c/V)^2/(4c) <= E0(Hnu)/V <= -nu^2/(A+nu B).    (2)

Thus thermodynamic accumulation densities are bounded above and below by
positive multiples of nu as nu decreases to zero; their energies are bounded
between negative multiples of nu^2. This is an onset bound, without an
assumption of condensation, a differentiable equation of state or a mode
identification. The constants are deliberately loose.

## Supplied objects and proof obligations

Use the cubic torus (Z/LZ)^3 and the full Hilbert tensor product of C^2 over
its sites. Choose b_x=|0><1|, n_x=b_x^dagger b_x, N=sum_x n_x and the empty
product vector Omega. The choice of basis, quantum state/expectation rule,
Hamiltonian and chemical-potential perturbation are mathematical inputs.
They are not selected by the framework's one-site algebra alone.

The proof obligations are: the full-carrier completion of squares; pair
geometry and uniform zero states; the exact kernel; bare-pair gradient
control; a point-pinned three-dimensional Poincare estimate; occupation
localization and its volume bound; and an exact normalized unitary trial
with a volume-uniform remainder. All are proved here. The runner supplies
finite exact controls rather than replacing the all-volume proofs.

The model has finite interaction diameter four, not a derivation of the
axioms' nearest-neighbor admissibility law. mu and tau are arbitrary supplied
positive energy parameters. The theorem holds without a continuum limit,
thermodynamic ground-state uniqueness, an empirical normalization or a
realized-state selection. L<5 and mu*tau=0 are outside the stated uniform
coercivity theorem. Boundary cases are discussed after the proof.

## Operators and full-carrier positivity

Let the pair graph have displacements D={+/-2e_i, +/-e_i+/-e_j : i<j},
eighteen distinct neighbors on every stated torus. Write m_x=sum_(d in D)n_(x+d).
At each center define fifteen bare pair annihilators

    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=s t b_(x+s e_i)b_(x+t e_j), i<j, s,t=+/-1,

and five collective components

    Q_E1=(d_1-d_2)/sqrt(2),
    Q_E2=(d_1+d_2-2d_3)/sqrt(6),
    Q_Tij=(1/2)sum_(s,t) v_ij^(s,t).

The notation A in Q_A runs over this list; it is not an additional site
species. Let P_E=sum_(A=E1,E2) Q_A^dagger Q_A and P_T=sum_(i<j)Q_Tij^dagger Q_Tij.
Define the actual Hamiltonian

    H0=mu N-2mu sum_x P_E(x)-mu sum_x P_T(x)+V3+Wtau,
    V3=mu sum_x n_x binom(m_x,2),
    Wtau=tau sum_(x,k,A) [Q_A(x+e_k)-Q_A(x)]^dagger
                              [Q_A(x+e_k)-Q_A(x)].              (3)

V3 consists of 153 positive three-site occupation projectors per center.
It vanishes on every particle sector N<=2. All terms in (3) conserve N;
the full Hamiltonian is translation and proper-cubic covariant. The E
doublet and T triplet transform orthogonally under those rotations, and
the sums of gradient squares are invariant.

Put D0=d_1+d_2+d_3 and

    S=(2mu/3)sum_x D0^dagger D0
       +(mu/4)sum_(x,i<j)sum_(r<s)(v_ij^r-v_ij^s)^dagger(v_ij^r-v_ij^s),
    Ddiag=(1/2)sum_x n_x(m_x-1)(m_x-2).

The key identity on the ENTIRE carrier is

    H0=S+mu Ddiag+Wtau.                                      (4)

Indeed sum_E Q_E^dagger Q_E=sum_i d_i^dagger d_i-D0^dagger D0/3.
For four signed plane words, sum_(r<s)(v_r-v_s)^dagger(v_r-v_s)
=4sum_r v_r^dagger v_r-(sum_r v_r)^dagger(sum_r v_r).
Each axial pair graph edge occurs at one center and each plane edge at two,
with coefficient signs disappearing in v^dagger v. Therefore

    2sum_(x,i)d_i^dagger d_i+sum_(x,i<j,r)v_ij^r^dagger v_ij^r
       =sum_x n_x m_x.

Substitution in (3), followed by
1-m+binom(m,2)=(m-1)(m-2)/2, proves (4). For integer m=0,...,18 this
polynomial is nonnegative. Equation (4) proves positivity without a
two-particle approximation or a restriction to classical configurations.

## Uniform pair states and the exact finite-volume kernel

Opposite pairs have a unique center at L>=5 and do not coincide with plane
pairs. Plane pairs have two centers with consistent signed amplitudes.
Direct contraction on Omega consequently gives uniform pair Gram matrix
V diag(1,1,2,2,2). Each Q_A(y) applied to a uniform pair state is a scalar
multiple of Omega independent of y. The gradients in Wtau annihilate them.
D0 and the plane-difference squares do too, and Ddiag is zero on these
graph-edge pair states. The five nonzero uniform vectors therefore have
zero energy. Omega also has zero energy.

Conversely, every square in (4) annihilates a zero-energy vector. Hence
Q_A(x)psi is constant in x. D0(x)psi=0 then makes each d_i(x)psi constant;
the plane-difference squares make every v_ij^r(x)psi constant as well.
In a sector N>=3, fix an output occupation word eta with N-2 particles and
an occupied site y of eta. For each bare pair type with endpoints x+u,x+v,
choose x=y-u. Its output amplitude on eta is zero because annihilation at y
leaves y empty. Constancy in x makes that amplitude zero everywhere, for
every eta and every pair type. Thus all pair annihilators kill psi. Equation
(3) would then give expectation mu N+V3, strictly positive in this sector.
The zero-energy subspace is therefore confined to N=0,2; N=1 has energy mu.

In N=2, Ddiag removes nonedges of the pair graph. The remaining constant
opposite-pair amplitudes have one sum constraint, leaving two dimensions;
each of the three planes contributes one signed constant amplitude. Shared
centers impose no further relation. The already displayed five independent
vectors span these possibilities. This proves the stated six-dimensional
kernel. Uniform pair waves are finite-torus vectors; no normalizable
infinite-volume vacuum-sector vector is inferred from them.

## From collective squares to bare gradients

For a vector psi, define

    Egrad=sum_(x,k,t) ||[B_t(x+e_k)-B_t(x)]psi||^2,

with B_t all fifteen bare pair types. The E doublet and D0/sqrt(3) are an
orthonormal transform of the three d amplitudes. In each plane, Q_T is the
normalized constant component of the four v amplitudes. Its three
orthogonal components have energy coefficient mu in S; the opposite-pair
singlet has coefficient 2mu. The elementary torus estimate
sum_(x,k)||f(x+e_k)-f(x)||^2<=12sum_x||f(x)||^2 gives

    Egrad <=6<S_E>/mu+12<S_T>/mu+<Wtau>/tau,
    <H0> >=mu<Ddiag>+a Egrad, a=min(tau,mu/12).              (5)

These are Hilbert-space-valued amplitudes on the full hard-core carrier.

## Point-pinned amplitudes in three dimensions

For a free rectangular grid C with largest side at most twice the smallest,
and f(p)=0 at any vertex, the following uniform estimate holds:

    sum_(x in C)|f(x)|^2 <=448 |C| sum_(edges xy in C)|f(x)-f(y)|^2. (6)

Normalized Neumann cosine modes have squared absolute value <=8/|C| and
eigenvalues lambda_n=4sum_i sin^2(pi n_i/(2s_i))>=4|n|^2/smax^2.
For the point difference, Cauchy-Schwarz in this basis bounds its square by
Dirichlet energy times

    sum_(n!=0)|phi_n(x)-phi_n(p)|^2/lambda_n
       <=(8smax^2/|C|)sum_(n!=0)1/|n|^2
       <=56smax^3/|C|<=448.

For the middle bound count nonnegative modes by largest coordinate r:
(r+1)^3-r^3<=7r^2, each with |n|^2>=r^2. Summing over x proves (6).
On a torus rectangle use the cyclic interval's free path order; on the whole
torus choose one cut in each coordinate. Every edge used is an actual torus
edge. The estimate also holds for vector-valued amplitudes componentwise.

Let B be an inner box and C its one-site enlargement in every coordinate,
as DISTINCT torus sites. For each bare type and output word eta with at
least one occupied site y in B, define f_eta^t(x)=<eta|B_t(x)|psi>.
Its pin x=y-u lies in C. Applying (6) gives

    M_C^(B,+):=sum_(t,x in C)sum_(eta:eta intersects B)|f_eta^t(x)|^2
       <=448 |C| Egrad_C.                                  (7)

The restriction on eta is independent of x and can be dropped from the
positive gradient sum after applying Poincare. No noncommuting number
projector is moved through an annihilator.

On each occupation configuration, 1<=(m-1)(m-2)/2+m. If N_B>=3, removal
of any graph pair leaves a particle in B. Every graph edge incident to B
appears among the bare words centered in C. The directed count
sum_(x in B)n_x m_x counts each edge at most twice, while the bare word
count counts it at least once. Since these bare norms are diagonal
occupation counts, the inequality holds for arbitrary coherent states:

    <N_B 1_(N_B>=3)> <=<Ddiag_B>+896 |C| Egrad_C.             (8)

Ddiag_B uses the actual full-torus neighbors of its centers in B.

## Occupation localization and coercivity

In a fixed sector N>=4 set q=floor((N/4)^(1/3)). Partition each coordinate
circle into q consecutive intervals of lengths differing by at most one.
There are q^3 disjoint inner boxes. For q=1 take the whole torus as C;
otherwise enlarge each interval by one at each end, capped at length L.
The resulting rectangles have aspect ratio <=2. Each site lies in at most
three enlarged intervals per coordinate, so each selected free edge occurs
in at most 27 rectangles. Also

    max|C| <=(ceil(L/q)+2)^3<=64V/q^3<=2048V/N,
    sum_B <N_B 1_(N_B>=3)> >=N-2q^3>=N/2.

The first uses q>=((N/4)^(1/3))/2 and L/q>=1; the whole-torus case obeys
the same bound. Summing (8) gives

    N/2 <=<Ddiag>+49545216 (V/N) Egrad.

Using (5), a<=mu/12 and N<=V yields

    <H0> >=a N^2/(99090432 V), N>=4.                       (9)

For N=3 every output already has a pin. Applying (6) to the whole torus
and the same counting gives <H0>>=a N/(896V), a stronger estimate than
the claimed c N(N-2)/V. N=0,2 are covered by positivity; N=1 has energy mu
and the claimed right side is negative. Number conservation combines all
sectors into the operator inequality. In any state of density rho,

    <H0>/V >=c(rho^2-2rho/V).                              (10)

## An exact normalized trial with a uniform remainder

Let K=sum_x K_x, K_x=i[Q_E1(x)^dagger-Q_E1(x)] and
psi(u)=exp(-iuK)Omega. The real parameter u labels trial states. This is
the full unitary state, not a finite Taylor truncation or a bosonic state.
K Omega=i sum_x Q_E1(x)^dagger Omega has norm squared V and particle
number two. Thus H0 kills both Omega and K Omega.

Each K_x has four-site support and norm <=2sqrt(2)<3. Each site lies in
exactly four translated supports. Group H0=sum_x h_x using the onsite
term, its five attractions, 153 triples and fifteen pair gradients based
at x. The support lies in {x}, its six unit neighbors and its eighteen
pair-graph neighbors: at most 25 sites. Since ||Q_A||<=2,

    ||h_x|| <=(1+16+12+153)mu+15*16tau=182mu+240tau.

For an operator initially supported on s sites, each nonzero nested
commutator has at most 4s choices at the first step, costs a norm factor
at most six per step, and adds at most three sites. Expanding into
connected sequences, including repeated terms, gives

    ||ad_K^r O|| <=24^r product_(j=0,...,r-1)(s+3j)||O||.

This bounds individual sequences before summing them; it does not assume
that the whole commutator has small support. Consequently

    ||ad_K^4 H0|| <=24 A V,   ||ad_K^4 N|| <=24 B V,
    A=24^4*25*28*31*34*(182mu+240tau)/24,
    B=24^4*1*4*7*10/24.

The energy's first four coefficients through order three vanish because
each matrix element has H0 against Omega or K Omega on at least one side.
The number expectation has second derivative 4V. Its odd derivatives vanish
by the number phase exp(i pi N/2), which sends K to -K and fixes N and
Omega. Integral Taylor remainder, with the global commutator bounds, proves
for the exact trajectory at every finite volume

    0<=<H0>_u/V<=A u^4,
    |<N>_u/V-2u^2|<=B u^4.                                (11)

There is no assumption V u^2<<1. Taking u^2=nu/(A+nu B) gives the upper
bound in (2). H0>=0 then implies E0>=-nu<N>, hence the lower density bound
in (1). Independently, (10), Jensen's inequality and E0<=0 imply the upper
density bound. Completing the resulting quadratic in rho proves the lower
energy bound in (2). Every ground density matrix satisfies these estimates.

## Limits, physical scope and trace

For fixed 0<nu<=nu_star, thermodynamic accumulation points obey

    nu/(A+nu_star B)<=rho<=nu/c,
    -nu^2/(4c)<=e<=-nu^2/(A+nu_star B).

The bounded finite-range local interaction permits the usual elementary
boundary comparison: replacing open-cube by periodic boundary terms changes
the energy by O(L^2), so the density lower energy bound also holds for a
translation-invariant infinite state. Uniform pair vectors themselves need
not exist in its representation. At nu<0 positivity makes the vacuum the
unique finite-volume ground state; at nu=0 the kernel is the displayed span.
tau=0 removes the gradient estimate and admits a different degeneracy; no
uniform positive c is asserted there.

The result is a concrete interacting model on full M2 site factors. Its
dilute two-particle zero states and density inequalities supply a controlled
starting point for studying collective matter. They do not specify a
condensate, an order parameter, a Goldstone spectrum, two tensor
polarizations, a readable permanent-record process, a source/action bridge
or a gravitational constraint algebra. Those are separate unresolved
questions. The strongest remaining physical obligation is a controlled
collective spectrum together with an actual record observable and source;
that obligation is stronger than the theorem proved here.

## Imports and premise authority

The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply the premise
boundary. The tensor-product quantum realization, chosen basis, expectation
rule, (3), positive mu,tau, chemical potential and selected trial states are
explicit mathematical inputs introduced here, not framework deductions.
The approved units, kinetic-form and realized-state primitives keep their
registered grants; none is classified as an unapproved import. No empirical
target, fitted parameter or new foundation is used. No physical state is
selected by the variational construction.

## Evidence and review record

Focused independent reconstructions checked the full positivity identity,
uniform pair contractions, spectator pins, box geometry, Poincare constants,
number-sector combination and exact trial remainder. Those checks are
provisional source-bound mathematical checks, not a formal audit. The primary
runner tests literal local and sparse finite-torus operators, partition and
pin geometry, rational graph resistance and trial constants. The analytic
argument above supplies the all-volume quantifiers.

The primary runs within its declared120-second envelope. Fourteen scratch
mutation families exercise local E/T weights, cubic covariance, the stabilizer,
internal projection, distinct torus sites, the graph Laplacian, hard-core pins,
occupation counting, the coercivity constant, local generator, number
normalization, uniform triplet Gram and variational minimizer. Each altered
family must fail at its actual assertion. Source-bound outputs, mutations and
review disposition are preserved in the accompanying milestone pack.
Combined landing validation and independent audit remain separate requirements.
No phase or framework-law status is inferred from those controls.
