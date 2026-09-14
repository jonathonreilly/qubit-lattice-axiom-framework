# Cubic-ice relaxed magnetic response, graph flows and sheet winding

**Status:** proposed_retained
**Date:** 2026-09-14
**Claim type:** bounded_theorem

Author-proposed conditional mathematics; actual source status conditional-support.
Independent scientific review is pending. The supplied finite cubic-ice law
and source convention are explicit inputs. No native photon phase, empirical
electromagnetic identification or axiom-forcing conclusion is established.

The fully relaxed source curvature equals a weighted graph-flow minimum and
an auxiliary current-diffusion coefficient. For the corrected Cartesian
plaquette source, positive closed histories count spatial sheet winding,
giving chi_L(beta)=(L/beta)<W_xy^2>. Explicit allowed membrane cycles prove
strictly positive finite response in a named mobile component for every even
L, with a lower bound that can vanish with volume. Frozen zero-flux states
make the globally minimized response vanish at V>=J; at RK a thermal trace,
a mobile-component ground state and a global minimum have distinct limits.
The missing phase obligation is a bound uniform in volume in the selected
component/ensemble and parameter interval, followed by the physical Maxwell
response and native-law join.

The stochastic-matrix correspondence, variational transport principle and
winding-fluctuation stiffness principle have established prior art. This
note matches them to the actual corrected ice source, proves its spatial
homology factor and constructive cycle, and supplies finite exact certificates
and order-of-limits counterexamples. The finite spectral numbers on current
main are prior results and are explicitly reproduced as such.

**Runner:** [self-contained primary](../scripts/cubic_ice_relaxed_magnetic_response_graph_flows_and_sheet_winding_2026_09_14.py).
**Receipt:** [canonical cache](../logs/runner-cache/cubic_ice_relaxed_magnetic_response_graph_flows_and_sheet_winding_2026_09_14.txt).
**Review:** [author record](../.claude/science/physics-loops/toe-charged-phase-20260914/deliveries/block9/REVIEW_HISTORY.md).

## Premises, obligations and imports

| Supplied premise or object | Proven consequence | Open obligation |
|---|---|---|
| Finite connected stoquastic move graph, positive geometric hoppings, real diagonal potential and antisymmetric source | Exact relaxed graph variational formula, cycle criterion and dual lower certificates | No uniform Perron-weight or gap control follows |
| Matched Doob rates and stationary initial distribution | Exact current variance and finite-time bias | Arbitrary sampler time is not Hamiltonian time or a physical Record clock |
| Supplied cubic-ice square law on an even torus and corrected Cartesian source | Integer sheet winding and positive finite-temperature history formula | Phase, component and limit selection remain explicit |
| Named checkerboard mobile component | Constructive winding cycle and finite positive curvature at every even L | Lower bound 2J/|Omega_L| does not prove positive thermodynamic stiffness |
| Full zero-electric-flux sector at V>=J | Frozen zero-energy states for every source | A mobile-component response cannot replace global minimization |
| Actual finite L=2 graph and exact rational identities | Curvature 28261/99144, complete component census and thermal limit distinction | No extrapolation from L=2 is used as phase evidence |
| Auxiliary flow paths with their integrated source and bounded congestion | Exact comparison inequality | A volume-uniform comparison has not been constructed |

The law, source, geometry, thermal trace, Markov rates and auxiliary comparison
are supplied mathematical objects, not selected axioms. Ordinary finite
Perron-Frobenius, analytic eigenvalue perturbation, matrix Duhamel expansion,
Cauchy-Schwarz and integer cellular homology are used with their stated
hypotheses. No empirical target value enters the derivation or runner.
The current source convention and finite results were checked against main
`b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf`; the reading ledger records exact
source scopes. Unmerged campaign conclusions are not scientific inputs here.

## 1. Geometric move graph and finite ground state

Let Omega be a finite connected component of configurations. Each geometric
move e is an unordered edge between distinct configurations x,y, with J_e>0.
Parallel geometric moves remain separate even if their endpoints coincide.
Choose one orientation x->y per edge and antisymmetric real source a_xy=-a_yx.
For arbitrary real diagonal d_x, define

    H(theta)_xx=d_x,
    H(theta)_xy=-sum_(e:x->y) J_e exp(i theta a_e).

Reverse entries are conjugates. H(0) is real stoquastic and irreducible.
A scalar shift of -H(0) gives a nonnegative irreducible matrix with positive
diagonal. Perron-Frobenius therefore gives a simple ground energy E0 and a
strictly positive real normalized vector psi_x, sum psi_x^2=1. For a component
with at least two states, its finite excited gap is positive. No lower bound
uniform in component/volume follows.
The simple branch E0(theta) is analytic near theta=0 and even by conjugation.
A singleton has no source edges and all response formulas below give zero.

Let B be the edge-by-vertex incidence matrix, (B phi)_e=phi_y-phi_x,
and w_e=J_e psi_x psi_y>0. Every edge sum below is over these unoriented
geometric edges once. This fixes all factors of two.

## 2. Exact relaxation is a weighted graph minimization

The first-order eigenvector correction is purely imaginary, because H'(0)
is imaginary antisymmetric and the unperturbed ground vector is real.
Every imaginary tangent vector has the form i psi_x phi_x, modulo the
irrelevant constant phase. Thus second-order minimization over normalized
vectors is exhausted by phases at first order; real amplitudes begin only
at second order and give no extra second-order energy lowering at a stationary
ground state.

Directly, for psi(theta)_x=psi_x exp(i theta phi_x),

    <psi(theta)|H(theta)|psi(theta)>-E0
       =2 sum_e w_e [1-cos(theta(a_e+(B phi)_e))].

Expanding and minimizing the first-order correction therefore gives

    C(a):=E0''(0)=2 min_phi sum_e w_e (a_e+(B phi)_e)^2.       (1)

This can also be obtained by differentiating the finite eigenvalue equation:
C=<psi|H''|psi>-2 sum_(m>0)|<m|H'|psi>|^2/(E_m-E0).
The minimizer solves

    B^T W B phi=-B^T W a,   W=diag(w_e).                    (2)

Connectedness makes the only null vector constant, so fixing one phi or its
psi^2 mean determines a unique solution. A sparse Poisson solve, a complete
spectral sum and the direct phase Rayleigh quotient are different checks.

Consequences hold for every diagonal potential d, not only an RK point:

    0 <= C(a) <= 2 sum_e w_e a_e^2;
    C(a)=0 iff a is a real graph gradient.

The second condition is equivalent to zero circulation on every graph cycle,
including length-two cycles made from distinct parallel moves. If it holds,
a basis rephasing removes the source for every theta, not just to quadratic
order. If it fails, C(a)>0 at every finite d with J_e>0 on this component.
Thus strict positivity of finite component curvature alone does not locate a
thermodynamic phase transition.

For several sources a=A lambda the response is a positive semidefinite
matrix 2 A^T W^(1/2) P_cycle W^(1/2) A, where P_cycle is orthogonal projection
onto ker(B^T W^(1/2)). Its rank is the dimension of the source image in real
graph cohomology. This is a statement about the specified move graph.

## 3. Dual flows supply lower certificates

For any edge flow j with B^T j=0, Cauchy-Schwarz gives

    C(a) >= 2 (a.j)^2 / sum_e j_e^2/w_e.                    (3)

The denominator must be positive; zero j is omitted. When C(a)>0, equality
is attained by j=W(a+B phi) for the minimizing phi. The following dual
maximum also covers C(a)=0, with the zero flow allowed:

    C(a)/2 = max_(B^T j=0) [2 a.j-sum_e j_e^2/w_e].         (4)

For one directed cycle with source period h, its unit flow yields
C>=2 h^2/sum_cycle(1/w_e). For edge-disjoint cycles, optimizing their separate
amplitudes gives the sum of these lower bounds. These are constructive finite
lower certificates, not assertions that a useful uniform packing exists.
At RK, w=J/|Omega|. A single rare large cycle gives a bound suppressed by
|Omega|; existence of a nontrivial cycle is therefore much weaker than a
positive thermodynamic stiffness.

## 4. Reversible current diffusion and its exact finite-time bias

Set pi_x=psi_x^2 and let a continuous-time Markov chain jump along each
geometric edge x->y with rate r_xy=J_e psi_y/psi_x. Its generator is

    (L f)_x=sum_y r_xy(f_y-f_x)
           =-[diag(psi)^-1(H(0)-E0)diag(psi) f]_x.

Detailed balance is pi_x r_xy=w_e=pi_y r_yx. This is auxiliary stochastic
time; it is not a physical Record clock. Define the accumulated antisymmetric
source current A_t=sum_jumps a_(X_before,X_after), and start in stationarity.
Its mean is zero. Define the drift b_x=sum_y r_xy a_xy and G=-L on mean-zero
functions. Then pi b=0 and the minimizing phi in (2) satisfies G phi=b.

The finite stationary jump-current variance is

    Var(A_t)/t = d0-(2/t) int_0^t (t-s)<b,exp(-sG)b>_pi ds,
    d0=2 sum_e w_e a_e^2.                                  (5)

One derivation differentiates the tilted Markov generator: its off-diagonal
rates are r_xy exp(lambda a_xy), with unchanged diagonal. Antisymmetry and
detailed balance give pi L'_0 f=-<b,f>_pi, while L'_0 1=b and
pi L''_0 1=d0. Duhamel's second derivative gives (5), including its minus
sign. Evaluating the spectral integral gives the exact identity

    Var(A_t)/t = C(a)
      +(2/t)<b,G^-2(1-exp(-tG))b>_pi.                      (6)

Consequently the finite-time ratio decreases to C(a) from above, and

    0 <= Var(A_t)/t-C(a) <= 2 ||phi||_pi^2/t.               (7)

Here phi has zero pi mean. A known gap gamma gives the weaker explicit bound
2||b||_pi^2/(gamma^2 t). The finite-time error of an exact stationary expectation
is separate from sampling error and from failure to equilibrate. An arbitrary
Monte Carlo acceptance rule changes L and its diffusion coefficient, even if
it preserves pi; the rates must match the supplied Hamiltonian or be corrected.

At RK the wavefunction is uniform on the chosen component and every geometric
jump rate is exactly J, so neither psi nor a population projection is needed.
Away from RK, the exact Doob rates require the ground vector. Section 5 gives
a different positive closed-history representation valid for every V without
knowing that vector.

## 5. Closed positive histories give the exact finite-temperature source observable

For a finite matrix write H(0)=D-T, with positive geometric off-diagonal
hoppings T. Dyson-expand exp[-beta(D-T)] in ordered jump times and close the
configuration path in the trace. Every zero-source history weight is positive:
it is a product of J_e and exp[-sum dwell_time d_x]. There is no sign problem
at theta=0 for this supplied bosonic occupation Hamiltonian. Source insertion
multiplies each closed history by exp(i theta A_history). Hence

    Z(theta)/Z(0)=<exp(i theta A_history)>_(beta,theta=0),
    F_beta''(0)=Var_beta(A_history)/beta,                   (8)
    F_beta=-beta^-1 log Z.

Path reversal makes the mean current zero. Formula (8) is a direct positive
history observable; it does not require imaginary-source continuation or an
assumed single exponential correlation. It is the model-specific application
of the established winding-fluctuation stiffness principle, not its invention.
The trace must specify its component/sector. At finite volume on one simple
component, beta->infinity recovers C(a). With degenerate disconnected components,
differentiation and this limit can fail to commute with taking the global
minimum; section 8 supplies an actual cubic-ice example.

## 6. Actual Cartesian source measures spatial sheet winding

On an even L^3 cubic torus put n_i(r) in {0,1}, require three occupied links
incident at each vertex, and E_i(r)=epsilon(r)(n_i(r)-1/2), epsilon=(-1)^sum r.
A geometric alternating square flip p=(r;i,j) changes

    Delta E=-epsilon(r) s_p partial p,   s_p=2 n_i(r)-1.

The Cartesian xy source attaches a_p=epsilon(r)s_p to xy moves and zero to
other orientations. These are the same definitions as current main's corrected
Cartesian-source note; the missing epsilon defines a different response.
For a closed configuration history, form its signed integer spatial two-chain

    S=sum_jumps epsilon(r)s_p p.

Since the electric configuration returns, partial S=0. Every closed integer
two-chain on the cubic three-torus has three integral homology components.
Pairing with the constant xy two-cochain gives

    A_history=sum_(xy faces) S_p = L^2 W_xy,  W_xy integer. (9)

For an elementary proof, sum the closed-chain boundary equation on x-links
over z. It makes sum_z S_xy(x,y,z) independent of y; the y-link equation
makes it independent of x. This common integer is W_xy. Summing over x,y
then gives (9). Equivalently, cube boundaries pair to zero and a fundamental
xy sheet has L^2 faces. Local plaquette flips preserve the
spatial electric flux, but their closed history can sweep a nonzero spatial
sheet. This W is a magnetic-source history winding, not the spatial electric
flux of one configuration.

For that source, the finite-temperature intensive response is exactly

    chi_L(beta)=L^-3 F_beta''(0)=(L/beta)<W_xy^2>_beta.      (10)

This also proves periodicity in theta with period 2pi/L^2. The source endpoint
unitary on main is consistent with the same integer periods. Open subcomplexes
with no second homology and exact sources have zero closed-history winding;
one must not substitute an arbitrary boundary twist for this observable.
The uniform bound still needed for a nonzero infinite-volume coefficient is
control of <W_xy^2> on the beta/L scale in the actual selected ground phase,
with justified order of limits. Counting flippable faces does not provide it.

## 7. Exact actual L=2 mobile-component result

A separately implemented axis-major construction gives 864 configurations and 3456
unoriented geometric moves, 1152 active for the xy source. At J=V=1 let
Delta=B^T B be the integer graph Laplacian and b=-B^T a. Direct integer
matrix action verifies

    P(Delta)b=0,
    P(z)=z^6-52z^5+1092z^4-11816z^3
                    +69072z^2-204608z+235008.              (11)

Since P(0)!=0, the exact mean-zero Poisson solution is

    phi=[204608-69072 Delta+11816 Delta^2-1092 Delta^3
                   +52 Delta^4-Delta^5]b/235008.          (12)

The equation Delta phi=b is checked on all 864 coordinates with rational
arithmetic, without accepting a floating-point eigenvalue or rational fit.
Substitution in (1) gives

    chi_2=28261/99144,
    direct flippability term=1/3.                         (13)

The exact polynomial certificate fixes this finite number; it is not a
thermodynamic stiffness. Separate full dense spectral sums agree with the
weighted graph solve at V=1,.95,.9, yielding approximately .285050028242,
.286566088925 and .287751063895. These agree with the current source note's
finite numbers; the new certificate and transport interpretation do not
relabel its previous computation as a new phase result.

The exact corrector variance is ||phi||_pi^2=5241841/91014192. Thus the
stationary open-current estimator has an absolute curvature bias at most
5241841/(45507096 t); divide this by eight for chi_2. Sturm isolation of
the six roots of P puts every current-coupled decay rate strictly between
3 and 15. This is a finite current-channel bound, not a lower bound for
the full graph gap or for any larger volume.

An all-configuration recursive degree census gives 9600 ice states in 937
move components on L=2. Of these 760 are singleton frozen components.
The cycle-period criterion detects nonzero xy response on 77 components;
100 additional non-singleton components have no active xy move. There is no
active-but-exact xy source component in this finite census. These counts
are checks at L=2 only; no connectivity classification for general L follows.

## 8. Global and component limits at RK

For every even L, define the periodic electric configuration

    E_x(r)=(-1)^y/2, E_y(r)=(-1)^z/2, E_z(r)=(-1)^x/2.     (14)

Each component is independent of its own coordinate, so div E=0, and every
spatial electric flux vanishes by even-period cancellation. On an xy square
the two y-links have the same electric sign and cannot participate in an
oriented circulation. The corresponding statement holds for yz and zx.
Thus no square is flippable. In occupation variables this is

    n_x=(1+(-1)^(x+z))/2,
    n_y=(1+(-1)^(x+y))/2,
    n_z=(1+(-1)^(y+z))/2.

Every V>=J ring Hamiltonian with arbitrary plaquette phases is

    H(theta)=J sum_p P_p(theta)+(V-J) N_f,

where P_p(theta) is the positive unnormalized two-state RK projector. The
configuration (14) is annihilated by every term. Therefore the global ground
energy in the full zero-electric-flux sector is exactly zero at every theta,
for every V>=J, including RK. Its globally minimized source curvature is zero.
This coexists with (13), because the mobile component is a different sector
choice inside the same electric-flux sector.

On L=2 at RK, the zero-flux sector consists of the 864-state mobile component
and sixteen singleton frozen components. At theta=0 the trace has seventeen
zero-energy vectors. At fixed nonzero theta near zero the mobile branch has
positive energy, while the sixteen frozen branches stay at zero. Hence

    lim_(beta->infinity) [L^-3 F_beta''(0)] = chi_mobile/17,
    L^-3 [d²/dtheta² lim_(beta->infinity) F_beta(theta)]_0=0. (15)

Differentiation and zero-temperature limiting do not commute for this
specified disconnected degenerate ensemble. A uniform superposition of all
880 configurations is another RK ground state, with different component
weights; neither is forced by the local Hamiltonian alone.
For V<J the uniform mobile RK vector has trial energy (V-J)<N_f><0, so
on this L=2 zero-flux sector the ground state lies in the mobile component.
The limit V increases to J selects its positive curvature. General-volume
mobile-component selection and a stable detuned photon phase remain open.


## 9. Constructive membrane cycles on every even torus

Let Omega_L be the component containing n_i(r)=r_i mod 2. On a plane z=z0,
the corresponding xy electric field is the boundary of the face height

    h(x,y)=(-1)^z0 [(-1)^x-(-1)^y]/4.

Indeed E_x(x,y)=h(x,y)-h(x,y-1) and
E_y(x,y)=-h(x,y)+h(x-1,y). Neighboring heights differ by 1/2.
Order all L^2 xy faces by decreasing initial h and flip each exactly once.
When a face is reached, each initially higher neighbor has already decreased
by one and each initially lower neighbor has not moved. Every neighbor is
therefore 1/2 below the current face. The face is flippable with coefficient
epsilon s_p=+1, and its flip lowers its height by one. This proves the full
sequence is allowed. The final height differs by a constant, so every electric
link and occupation returns to its starting value. The source period is L^2.

The three height classes +1/2,0,-1/2 have respectively L^2/4,L^2/2,L^2/4
faces. No two faces within a class share a link, so the sequence has three
parallel rounds of local flips. This supplies a closed history, not a claim
about its stochastic probability or physical time. The L distinct planes give
edge-disjoint cycles in the configuration graph, meeting only at the common
starting configuration.

For every real V and J>0, the positive Perron weights make each cycle's dual
bound (3) strictly positive on Omega_L. At RK, w=J/|Omega_L|. Summing the L
edge-disjoint cycle bounds gives

    chi_L >= 2J/|Omega_L| > 0.                            (16)

The source is one xy orientation and chi_L=C/L^3. This is an explicit finite
lower bound; it can decay exponentially with volume and is not a positive
thermodynamic K. It proves why a finite positive response at every L is
compatible with the remaining phase uncertainty. The global frozen-state
result in section 8 continues to apply when the full zero-flux sector, rather
than Omega_L, is minimized at V>=J.

## 10. The first winding order grows with spatial area

A closed history of n square flips obeys |A_history|<=n, while (9) requires
A_history=L^2 W. Consequently every history with fewer than L^2 flips has
zero xy winding. In a trace of H(theta)^n, diagonal insertions do not change
the configuration or add source. Therefore, for every real V,

    Tr H(theta)^n = Tr H(0)^n for 0<=n<L^2.               (17)

This holds on any component. On Omega_L the constructive cycle in section 9
attains length L^2. At that minimal order, a nonzero winding history uses
only off-diagonal xy moves of the same source sign. Its contribution to
Tr[-H(theta)]^(L^2) has positive weight J^(L^2); no diagonal insertion or
opposite phase can cancel its positive winding coefficient. Hence the
finite-temperature curvature on this component has a strictly positive
leading term of order beta^(L^2-1) as beta decreases to zero. Its coefficient
counts actual minimal closed move sequences and is independent of V. On L=2
there are 1216 oriented closed sequences of each source sign at order four,
giving chi_2(beta)=(19/81) beta^3+O(beta^4) at J=1 on the mobile component.

This is a statement about the finite-volume Taylor expansion; its remainder
has not been bounded uniformly in L. It explains why a history expansion
truncated at a fixed number of local moves cannot see the winding response
once L^2 exceeds that number. Resummation, a long-history observable or a
global flow construction remains available. It is not a limitation of every
method using local mathematics and not an axiom obstruction.

## 11. A precise route for a uniform lower bound

Consider an auxiliary move graph on the same configurations, with positive
edge weights w'_f and source a'_f. Supply for every oriented auxiliary edge
f=(x,y) a path gamma_f of actual geometric moves from x to y, with

    a'_f=sum_(e in gamma_f) oriented a_e.

Repeated actual edges count with multiplicity. Cauchy-Schwarz on this path
gives, for every phi,

 w'_f(a'_f+phi_y-phi_x)^2
 <= w'_f |gamma_f| sum_(e in gamma_f)(a_e+(B phi)_e)^2.

Thus, if the explicitly defined congestion obeys

 rho=max_e [sum_f w'_f |gamma_f| multiplicity(e,gamma_f)]/w_e,

then the variational responses satisfy C_actual>=C_auxiliary/rho. This
comparison requires the correct integrated source, not just matching
endpoints or stationary measures. Different paths may differ by a winding
period and hence represent different source experiments.

A uniform phase certificate could therefore consist of C_auxiliary>=k L^3
and rho<=rho0 with k,rho0 positive and independent of L, in a specified
ground-state component/ensemble and parameter interval. None of those
uniform bounds is supplied here. The explicit single-sheet paths prove
finite positivity but their presently controlled packing only gives (16).
Classical loop samplers with improved mixing cannot be substituted for the
Hamiltonian dynamics without this comparison or another controlled rate
conversion. A restricted actual nine-configuration cube with four active
source edges has exactly zero response: its allowed spatial moves are
contractible. This diagnostic changes the move set and is not a counterexample
to the full periodic model or to its all-volume membrane construction.
A thermodynamic curvature bound would still need the transverse
spectrum, electric response, phase stability and native-law identification
before it establishes the proposed physical photon branch.


## Proof and falsification coverage

| Argument | Different calculation path | Scope |
|---|---|---|
| Relaxed response and optimal flow | Weighted Poisson solution and complete dense Kubo sum at three detunings | Actual 864-state component; general identity proved above |
| Exact RK corrector | Integer Krylov action, rational Poisson residual at every configuration, Sturm root isolation | Exact finite number; no large-volume gap claim |
| Current diffusion | Independent block-matrix moment evolution and spectral finite-time formula on a nonuniform reversible multigraph | Finite matched Markov process, including parallel moves |
| Positive thermal winding | Laurent matrix history coefficients through order 48 and complete thermal spectral response at six parameter pairs | Actual six-state component; explicit positive-series tail bound |
| Component and ensemble limits | Exhaustive recursive ice census, flux preservation on every move, full mobile thermal spectrum plus sixteen frozen states | All L=2 configurations; general frozen construction proved separately |
| Membrane homology | Actual local legality, signed spatial boundary, return state and source period on L=2,4,6,8 | Proof covers every even L; no history-probability estimate |
| Minimal winding order | Exact integer traces at one through four jumps | General lower order follows from the integer sheet factor |
| Uniform comparison target | Weighted path energy inequality and a nontrivial auxiliary graph; restricted actual contractible cube | No useful large-volume congestion bound supplied |

For the positive-series check, choose M>=max d_x, so G=M I-H(0) is entrywise
nonnegative. The trace expansion of exp(beta G) keeps an integer source
Laurent coefficient for each history. Let R=beta ||G||_infinity, N be its
matrix dimension, and retain orders n<=K. The omitted partition weight is at
most N exp(R) Pr[Poisson(R)>K]. Since |A|<=n, the omitted second moment is
at most N exp(R){R^2 Pr[Poisson(R)>K-2]+R Pr[Poisson(R)>K-1]}.
The common exp(-beta M) cancels from the moment/partition ratio. The runner
propagates these positive remainder bounds to the ratio; floating-point
roundoff in its separate matrix checks is controlled by declared tolerances,
not claimed covered by the exact Taylor remainder. The largest reported
Taylor ratio bound is below 7e-29 for these six finite examples.

## No-Go Discipline Gate

### N1 — materially distinct routes

Every entry below is ATTEMPTED. This list tests the scoped inference limits;
it is neither an exhaustive search nor a count of independent axiom walls.

| Route | Attempt and outcome | Evidence |
|---|---|---|
| Full state relaxation | Include every imaginary first-order eigenvector correction; yields exact nonnegative graph response, smaller than direct flippability | Sections 1–2 and finite spectral/Poisson comparison |
| Weighted cycle flows | Construct winding paths and dual witnesses; succeeds for finite positive response, current bound can vanish with volume | Sections 3 and 9, explicit legal sheet histories |
| Positive thermal histories | Avoid unknown detuned Perron amplitudes by a trace expansion; succeeds for a matched finite-temperature observable | Sections 5–6 and six positive-series/spectral comparisons |
| Ground-sector selection | Test whether a global zero-flux minimum must inherit mobile stiffness; explicit frozen states disprove that inference at V>=J | Section 8, full finite census and thermal limit |
| Local truncation and topology | Restrict to a contractible cube and to bounded jump order; active local moves can have zero response, and winding begins only at L^2 moves | Section 10 and restricted nine-state cube |
| Dynamics comparison | Translate an auxiliary sampler through actual source-preserving paths; gives a valid lower-bound criterion, while uniform congestion remains open | Section 11 and finite weighted path check |

### N2 — wall dependence and collapse

The diagnoses are source topology, ensemble/limit selection, transport weight
control and rate matching. They do not add up to four independent physical
obstructions.

| Pair | Relation and disposition |
|---|---|
| Topology / ensemble | A mobile component has winding cycles while a frozen component does not. Selecting a full minimum can change topology; preserve the distinction inside one sector-selection question. |
| Topology / transport weight | Nontrivial periods give finite positivity, but arbitrarily small weights can make it tiny. One is a necessary geometric condition and the other quantitative control. |
| Topology / rate matching | Matching endpoints without matching integrated source can discard a winding period. Source matching is part of a valid comparison, not a new phase wall. |
| Ensemble / transport weight | The thermal weights of disconnected ground components differ from configuration counts and from selecting the mobile branch. Fix the ensemble before estimating conductance. |
| Ensemble / rate matching | A sampler confined to one component does not sample a full-sector thermal trace. Rate and sector identity are both premises of the observable map. |
| Transport weight / rate matching | Changing rates changes conductance. A congestion theorem can relate them; absence of that bound is one unresolved quantitative comparison, not two failures. |

The weak single-cycle lower bound and a fixed-order history truncation are
limitations of these estimates, not proof that the actual thermodynamic
stiffness vanishes. The only exact vanishing claims concern stated gradient
sources, restricted contractible moves, or the full V>=J frozen-state minimum.

### N3 — hidden conditions

Finite connectedness, strict positivity of geometric hoppings, source orientation,
parallel-edge multiplicity, a simple finite ground branch and real diagonal
potentials are explicit in section 1. Stationarity and exact Doob rates belong
to the current identity; the positive trace formula is a distinct ensemble.
The integer homology factor requires the stated periodic even cubic geometry
and the corrected Cartesian epsilon sign. The membrane proof specifies its
starting component. The all-state census and the seventeen-component thermal
limit are L=2 statements. Uniform component selection, detuning stability,
large-volume response, real-time pole normalization and physical identification
are not hidden in the words ice, photon, RK or Hamiltonian.

### N4 — source and witness matching

| Source or witness | Residual actually addressed | Claimed closure |
|---|---|---|
| Hermele–Fisher–Balents cond-mat/0305401v3, selected cubic/RK/phase and magnetic-trial sections | Prior cubic three-dimer law, phase argument and mixing limits | Correct model comparison and prior physical argument; no rigorous uniform theorem imported |
| Henley cond-mat/0311345v1 pp1–3 and selected examples | RK dynamics/classical correspondence | Prior correspondence, with component and rate qualifications |
| Castelnovo et al. cond-mat/0502068v1 section3 pp12–15 | Stochastic-matrix form and detailed balance | Prior mathematical framework; finite mapping reconstructed here |
| Pollock–Ceperley PRB36,8343 pp1–4, especially sectionIII.A | Winding distribution and stiffness | Established principle credited; the ice sheet factor is derived directly |
| 1408.5477v1, selected introduction and section9.2 | Current-cycle and cellular-homology language | Context only; no large-deviation result used |
| Current Cartesian-source note and primary, scopes in ledger | Correct physical source sign and prior finite spectral values | Definitions reproduced and finite results checked through a different graph representation |
| Written proofs and paired primary | Exact finite response, sheet construction, fixed-order cancellation and frozen-sector counterexample | Only the quantified finite and conditional statements above |

### N5 — resolution and rhetoric

Per element, exact rational correctors and integer source periods are checked.
Per site, the full finite ice degree census and Gauss conditions are checked.
Per mode, every eigenstate enters the finite Kubo response and the exact current
channel is isolated. Per block, actual closed histories and membrane sequences
are reconstructed. Lattice-wide finite-volume family claims come from the
written proofs; a volume-uniform interacting photon phase is not simulated or
established. The finite number 28261/99144 is not a fitted macroscopic constant.

### N6 — constructive partial closure

The mobile component has an explicit winding witness for every even L.
The positive trace estimator removes the need to know detuned Perron amplitudes.
A path-congestion comparison or a direct divergence-free flow packing could
supply a uniform lower bound. Selecting V<J or a physically justified component
can avoid the exact frozen-minimum example. None of these surviving routes
requires an axiom update. The native-law and physical-response join remain
separate work; no new primitive, interpretation stance or editable prompt is
introduced by this unit.

### N7 — strongest surviving alternative

The strongest objection to any broad negative conclusion is the established
physical adjacent-Coulomb-phase argument and the possibility that a dense set
of typical long histories carries finite winding transport. The explicit
positive cycle and exact positive history weights support that possibility.
Neither our weak cycle packing nor a fixed-order truncation constrains those
typical histories sufficiently. This objection defeats a claim of no photon
phase or an axiom wall. The task left open is to prove the quantitative
transport and phase statements under the actual component/limit choices.

### N8 — cross-cycle echo and marginal value

The corrected Cartesian-source note already distinguishes its source from
occupation-oriented signs and reports finite relaxed response. Historical
finite-detuning magnetic and spectral notes hold production and physical
Maxwell conclusions. The RK bridge note already imports the adjacent-phase
argument with connectivity limits. Those results are not relabelled as new
phase closure here. The new joined object is the exact graph/transport/sheet
observable map, its constructive all-even-L winding witness, and the actual
frozen-sector order-of-limits example. Related source searches, including the
no-go ledger, are recorded in the author review; no retired universal wall is
revived from a failed bounded computation.

## Sources and reproduction

Primary sources are [Hermele, Fisher and Balents](https://arxiv.org/abs/cond-mat/0305401v3),
[Henley](https://arxiv.org/abs/cond-mat/0311345v1),
[Castelnovo and collaborators](https://arxiv.org/abs/cond-mat/0502068v1),
[Pollock and Ceperley](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.36.8343)
and the [current-cycle mathematics source](https://arxiv.org/abs/1408.5477v1).
The reading ledger fixes PDF hashes, pages read and repository source scopes.
No full review of the unread portions or replay of historical production runs
is claimed.

Run the paired primary with Python 3, NumPy, SciPy and SymPy. It reads no
scientific files. Eight substantive check families challenge the derivations
through the different representations listed above. Canonical execution uses
a declared 90-second envelope and records exact source hash, output and runtime.
Full source/output receipts for load-bearing mutations are in the author packet.

## Review record

The author cold-read the complete note and primary before delivery; the exact
source-bound reading and mutation results are recorded in the packet. An initial
restricted-cube diagnostic selected a frozen starting cube and was corrected
to an active cube; that failed attempt is preserved in the working history.
All these checks are personal author evidence. Independent scientific review
remains pending.

Focused syntax, cache/hash, local-link, vocabulary, whitespace, N5 and mutation
checks are recorded in the packet. The citation manifest is regenerated by its
owning tools. Full pipeline, strict global lint and combined changed-evidence
validation remain deferred under conformance section 12 to the exact integrated
current-main candidate; they are not reported as passed. There is no author
main merge, scientific audit verdict or effective-retention update.

## Claim-status certificate

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
target_blocker_text: Establish volume-uniform magnetic response and a native finite-qubit photon phase with matched electric and transverse dynamical response.
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: Independently review the exact source and limit map; construct a uniform transport bound in a selected phase and complete the physical Maxwell join.
conditional_surface_status: Supplied finite cubic-ice Hamiltonian, component, source and ensemble; native existence and uniform phase response remain open.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Exact matched finite response theorem and explicit scoped ensemble/topology counterexamples; no general photon or axiom no-go.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
