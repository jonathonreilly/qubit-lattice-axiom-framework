---
claim_id: mobile_records_local_gibbs_circulations_and_winding_transport_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For supplied bounded finite-range Gibbs interactions, local whole-record plaquette circulations and positive Metropolis swaps preserve grand and fine-count canonical Gibbs laws. The stated polar/axial example is cubic covariant and nonreversible; its contractible-cycle homogeneous label current vanishes. Permanent positive formation fills finite volume and selects an unknown mixture of full-occupancy canonical laws. A separate established one-dimensional KLS exchange has an exact finite-word Gibbs stationarity certificate, positive grand-law transport current, exponential correlations and a fine-label lift. Its symmetric orbit lift has zero separated raw-vector covariance. Neither construction supplies a three-dimensional correlated vector state with the earlier wave transport."
upstream_dependencies:
  - minimal_axioms
runner: scripts/mobile_records_local_gibbs_circulations_and_winding_transport_2026_09_21.py
---

# Local Gibbs states and transport of immutable records

**Date:** 2026-09-21  
**Type:** bounded_theorem  
**Status:** proposed_retained  
**Author support:** conditional-support; no independent audit verdict.

The mobile-record campaign needs both a suitable stationary state and a
transport mechanism. These two constructions test how far those requirements
can coexist while every record keeps its content. They use established
Markov-cycle and KLS machinery with explicit locality and current calculations.
The Hamiltonians, alphabets, rates and physical interpretation are supplied
choices, not a derivation from [the minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

Part A preserves arbitrary specified finite-range Gibbs weights using local
permutations, including a cubic-covariant irreversible example. Its equilibrium
Euler label current vanishes because its elementary stationary flows traverse
bounded contractible cycles. Part B is an explicit directional one-dimensional
countercontrol: Gibbs stationarity and nonzero transport coexist when the
configuration-space cycles can wind around the ring. These separate facts do
not imply a universal incompatibility or establish the requested joint model.

Both complete source arguments were independently reconstructed before their
author checkers were opened. Two narrow wording findings were corrected with
original bytes, diffs and acknowledgments preserved. The assembled publication
has author provenance verification; no separate independent assembly audit is
claimed. The full unchanged mathematical checks are bundled in the evidence.

## Part A. Local Gibbs-preserving whole-record circulation

2026-09-21. Personal campaign derivation; selective independent check complete.
This is a constructive state-selection comparison, not a derivation of a
Hamiltonian, quantum vacuum, physical time reversal or Euler wave theorem.

### 1. Purpose and established machinery

The earlier context exchange has uniform permutations as its finite-volume
invariant law in each count sector. Consequently its ordered late state
cannot acquire the required long-range correlations simply by changing
positive birth weights. Changing the conservative transport is an open route.
Failure of a particular inverse one-site Gibbs clock does not exclude it.

The relevant established construction is De Carlo and Gabrielli,
[Gibbsian stationary non equilibrium states, arXiv:1703.02418v3](https://arxiv.org/abs/1703.02418v3),
Sections 3 and 3.6, equations (13)-(15) and (50)-(52). A positive stationary
flow on a configuration graph is divergence free; a closed-cycle flow is
therefore stationary. Weighting a local cycle by its exterior Gibbs factor
cancels the nonlocal factor when converting flow to transition rates.
Their Section 3.3 supplies exclusion examples. The record construction and
the explicit transport cancellation below are worked out here directly.

### 2. Finite-range Gibbs specification and exact local generator

On the cubic torus of side N>=5 use the fifteen symbols from the transverse
model: vacancy0, six A labels e=+/-unit axes with b=0, and eight B labels
b=(+/-1,+/-1,+/-1) with e=0. Their immutable features are
t=(e,b/2). Distinct record identities can be carried along with these labels;
the generator only permutes entire records and empty sites.

Let H(eta)=sum_X Phi_X(eta_X) be a supplied bounded, finite-range interaction,
translation covariant and invariant under the desired cubic label action.
All inverse temperature and energy units are absorbed in H. For a plaquette
S=(x0,x1,x2,x3) in cyclic order, write

    H_S(eta)=sum_(X intersect S nonempty) Phi_X(eta_X),
    H_out=H-H_S.

H_out is unchanged by any permutation supported in S. The interaction
radius and finite alphabet bound H_S uniformly in volume. Let R move each
whole site state x_i to x_(i+1), with indices modulo4. Every displaced
record moves one nearest-neighbor step and no site has two records.
This is an atomic four-site permutation, not a one-record-at-a-time hop.

Choose local nonnegative functions a_+,a_- which are invariant under R.
They may depend on exterior local context and the orbit of the four
interior labels. Define

    r_S,+ (eta)=a_+(eta) exp(H_S(eta)),
    r_S,- (eta)=a_-(eta) exp(H_S(eta)),
    L_S f=r_S,+ [f(R eta)-f(eta)]
            +r_S,- [f(R^-1 eta)-f(eta)].                 (1)

Self transitions contribute zero and can be omitted. These are nonnegative
bounded local rates, independent of global volume or normalizing constants.
For any finite chemical potentials lambda_a, the grand Gibbs law is

    pi_lambda(eta)=Z^-1 exp[-H(eta)+sum_a lambda_a N_a(eta)].

Along an R orbit, all counts and H_out are constant, hence

    pi_lambda(eta) r_S,+ (eta)
       =Z^-1 a_+(eta) exp[-H_out(eta)+sum_a lambda_a N_a(eta)]

is constant. Each state has exactly one R predecessor and successor, even
if its orbit has length1 or2. Incoming and outgoing clockwise flows match,
and likewise counterclockwise. Thus pi_lambda L_S=0. Summing over all
plaquettes preserves the law. Conditioning on any count sector preserves
it too, since every transition conserves each N_a.

The same argument can be stated without grand chemical potentials: the
conditional Gibbs weight on S with fixed exterior and fixed multiset of
labels is preserved by (1). This is the precise locality mechanism.

To obtain irreducibility in every label-count sector, add each nearest-neighbor
whole-record swap eta->eta^xy at rate

    kappa min(1,exp[-H(eta^xy)+H(eta)]), kappa>0.          (2)

The energy difference depends on a bounded neighborhood of the bond.
Pairwise detailed balance is immediate. Adjacent transpositions generate
all permutations of site states on the connected torus, so the combined
finite generator is irreducible on each count sector and its unique law
there is the canonical Gibbs law. The same statement holds for tagged
records if identities are retained and the Hamiltonian depends only on
their fixed contents. No uniform mixing time has been proved.

### 3. Positive cubic-covariant circulation with immutable labels

For the oriented plaquette let n be its unit normal from the right-hand
rule and put

    chi_S(eta)=n dot sum_(x in S) b(eta_x)/4,
    a_+=nu(1+epsilon chi_S), a_-=nu(1-epsilon chi_S),
    nu>0, |epsilon|<1.                                  (3)

Each component of b is -1,0,1, so |chi_S|<=1. The sum is permutation
invariant. Reversing the convention for S sends R to R^-1 and chi to
-chi, leaving the generator unchanged. Under proper cubic rotations, n
and b both rotate. Under the earlier improper polar/axial convention,
both acquire the axial factor det(Q), so (3) is covariant under all48
cubic transformations when H has that symmetry. Translation covariance
also holds. No externally selected circulation axis is needed.

For an orbit of length4 with chi!=0 and epsilon!=0 the stationary forward
and backward edge flows differ by a factor
(1+epsilon chi)/(1-epsilon chi). Thus this single-plaquette generator is
not reversible. A four-distinct-label configuration on S makes R eta
different from R^-1 eta. In the lattice sum that four-site transition can
only come from the same plaquette, and the added two-site swaps cannot
cancel it. This supplies a nonreversible full-generator witness.

For example H=-K sum_(nearest x,y) t(eta_x) dot t(eta_y) is finite range
and respects the polar/axial cubic action. Nonzero K changes relative
weights of same-count arrangements. On one square containing two +e1
and two -e1 labels, the alternating arrangement has H=4K and the adjacent
like-pair arrangement has H=0, so their Gibbs probability ratio is exp(-4K).
The construction therefore supports a supplied nonuniform canonical state.
It does not establish a Coulomb phase, critical exponent, or quantum state.

The rates in (1)-(3) inspect all interactions touching a plaquette. They
are local finite-range transport rates, not a claim about the nearest-neighbor
conditional law of a one-site formation event. The original positive
nearest-neighbor birth law can be added as a separate mechanism; it does
not leave a Gibbs law with vacancies invariant.

### 4. What permanent formation permits at stationarity

Let vacancies form records at rates whose total at each empty site is at
least b_min>0, with no deletion. All conservative moves above preserve the
vacancy count V. The full generator therefore satisfies

    L V=-sum_(vacant x) total_birth_rate_x <=-b_min V.    (4)

Any finite-volume stationary law has E V=0. In particular a positive
grand Gibbs law with vacancies cannot be stationary for that full process.
Starting from any configuration, the finite chain reaches full occupancy
almost surely, with E tau_fill<=H_(V_initial)/b_min. This follows by
bounding the holding time until the next birth with an exponential of
rate b_min times the current vacancy count, regardless of intervening hops.

After formation stops at full occupancy, (1)-(2) converge within the
realized final count sector to its canonical Gibbs law. The complete
late law is a mixture over those random counts. Unlike the previous
uniform-permutation generator, the conditional state is now correlated.
Its count distribution, infinite-volume phase, and the time to approach
it remain unsolved. The previous equal-label Euler trajectory cannot be
imported: the conservative invariant family has changed.

### 5. A precise limitation of this local-cycle route for Euler transport

This part concerns additive conserved label contents and closed cycles
supported inside a bounded contractible region. It does not concern
all local irreversible rates, winding configuration cycles, Hamiltonian
dynamics, defects, or a quantum carrier.

Fix an embedding of the plaquette and its neighboring sites into Z^3
(no winding ambiguity). For a label a define the content first moment

    M_a(eta)=sum_(x in S) x 1_(eta_x=a).

The spatial displacement of that content in an R transition is
Delta M_a=M_a(R eta)-M_a(eta). In a stationary clockwise orbit its
probability flow F is constant, so the orbit's expected integrated
transport is

    F sum_(eta in orbit) [M_a(R eta)-M_a(eta)]=0.          (5)

The same holds for the reverse orbit, any linear combination of contents,
any local orbit-invariant multiplier, and arbitrary exterior conditioning.
For local reversible swaps, the forward/backward fluxes cancel in pairs.
Consequently the spatially averaged content current in every homogeneous
grand Gibbs law pi_lambda is exactly zero for (1)-(2), at every lambda.
On a translation-invariant torus this is the current per unit volume.
Local circulating currents can remain nonzero, but their displacement
sum has no transport component.

If a local-equilibrium Euler closure uses these Gibbs laws and identifies
its flux with that homogeneous expected content current, its flux function
is identically zero, and its flux Jacobian cannot reproduce the previous
nonzero transverse Euler wave sector. This is a conditional consequence
of (5), not a hydrodynamic convergence proof. Diffusive dynamics, slow
relaxation, local circulating response, and other scaling limits are not
excluded. A different conservative generator carrying a nonzero transport
current while preserving the desired Gibbs family is still an open route.

This exercise therefore resolves the narrow locality question positively
while making the next obligation sharper: selecting a correlated invariant
law and retaining the relevant propagating transport must be demonstrated
together. Neither property by itself identifies electromagnetism or a TOE.

## Part B. Correlated Gibbs transport through winding cycles

2026-09-21. Reconstructed established one-dimensional comparison, with an
explicit finite-word stationarity certificate and a fine-label lift.
Selective independent checking complete. No new universal obstruction is inferred from
the zero-current local-circulation construction.

### 1. Local record exchange and the Gibbs family

Take a ring with N>=4 and two permanent record classes, encoded by
sigma_x in {0,1}. Both values can be occupied records; zero in this section
is a class indicator, not an assertion of an observable vacant-site state.
Use the supplied dimensionless energy and chemical potential

    H=-J sum_x sigma_x sigma_(x+1),
    pi_mu=Z^-1 exp[-H+mu sum_x sigma_x], z=exp(J)>0.

Only adjacent patterns10 exchange to01 clockwise. With exterior bits
a=sigma_(x-1),d=sigma_(x+2), the rate is

    r00=r11=kappa,
    r01=2kappa z/(1+z), r10=2kappa/(1+z), kappa>0.       (1)

This exchanges entire records, preserving every record's content and
one-record capacity. The rule is local and strictly positive on allowed
clockwise exchanges. It explicitly selects a spatial direction. It is the
totally asymmetric heat-bath Kawasaki/KLS example, not a new method: see
Luck and Godreche, [arXiv:cond-mat/0604274v2](https://arxiv.org/abs/cond-mat/0604274v2),
Section2, equations(2.20)-(2.30). Their spin coupling equals J/4 in this
binary-variable convention, up to a count-dependent energy term. Their
time normalization is recovered by kappa=1/2.

### 2. A pointwise certificate valid for every ring size

Divide the master-equation stationarity residual at a configuration by
pi_mu. A word(a,b,c,d) contributes

    F(a,b,c,d)=1_(b=0,c=1) r_ad z^(a-d)
                     -1_(b=1,c=0) r_ad.                 (2)

The incoming predecessor has10 where the current word has01, and its
Gibbs ratio is z^(a-d); all chemical-potential terms cancel.
Define h on length-three binary words by the following table:

| word | h/kappa |
|---|---|
|000,001,100|0|
|010|-1|
|011,110,111|-2/(1+z)|
|101|(z-1)/(1+z)|

Substitution of the sixteen words gives the rational identity

    F(a,b,c,d)=h(a,b,c)-h(b,c,d).                         (3)

The sum of (3) telescopes around any ring. Thus pi_mu is stationary for
all N>=4 and all mu,J, including after conditioning on particle counts.
The sixteen-word certificate proves all sizes; exhaustive finite rings
are separate controls, not the proof's quantifier.

### 3. Positive current and genuinely correlated thermodynamic state

The class1 clockwise current per bond is

    j_N=E_pi[1_(sigma_0=1,sigma_1=0) r_(sigma_-1,sigma_2)].

For finite mu,J all configurations have positive weight and allowed10
words have positive rates, so j_N>0. The current reverses for class0.
This does not contradict the local-cycle cancellation: the full
configuration-space flow here contains cycles with spatial winding.

The positive transfer matrix

    T_ab=exp[J a b+mu(a+b)/2], a,b in {0,1}

has a simple largest eigenvalue Lambda and normalized strictly positive
eigenvector v. In the infinite-ring limit,

    P(a,b,c,d)=v_a T_ab T_bc T_cd v_d/Lambda^3,
    rho=v_1^2,
    j=sum_(a,d) P(a,1,0,d) r_ad >0.                      (4)

The associated two-state transition matrix is
P_ab=T_ab v_b/(Lambda v_a). Its second eigenvalue is
u=Lambda_2/Lambda with |u|<1. Every centered single-site binary function
is a multiple of sigma-rho, hence

    Cov(sigma_0,sigma_r)=rho(1-rho) u^r, r>=0.            (5)

For J!=0, det T=exp(mu)(exp(J)-1)!=0, so u!=0 and the
nearest-neighbor covariance is nonzero. This is a supplied correlated
stationary law with nonzero transport, not a critical or long-range phase.
At J=0 it reduces to independent Bernoulli labels with
j=kappa rho(1-rho). The dependence of stationary current on density is
an input to a possible Euler closure; no hydrodynamic theorem is proved here.

### 4. Lift to finitely many immutable record contents

Partition any finite label menu into nonempty classes A and B and set
sigma(label)=1_A. Use H above with this class indicator and arbitrary
finite chemical potentials lambda_a for every actual label. In a
cross-class exchange the product of chemical weights cancels, and the
stationarity residual is still exactly(2). Thus the same calculation
preserves the fine-label Gibbs measure

    pi_lambda(eta) proportional exp[-H(sigma(eta))
                                      +sum_a lambda_a N_a].

Symmetric whole-record swaps within the same class can be added; their
energy difference vanishes and they obey detailed balance. Fine label
counts remain conserved. No claim about tagged-record mixing is required
for the invariance calculation. If vacancy is one extra label assigned to
one class, conservative invariance remains true as bookkeeping. Positive
permanent births change this invariant law until full occupancy, exactly
as in the vacancy Lyapunov argument of the local-circulation note.

For the fully occupied fourteen-label restriction of the transverse menu,
the rotation-invariant partition A=six axis labels and B=eight cube labels
preserves label-orbit symmetry,
but the selected chain direction still breaks three-dimensional cubic
symmetry. With equal chemical potentials within each orbit, raw vectors
have zero conditional means given the class configuration. Distinct-site
raw vector covariances in this grand Gibbs law therefore vanish, despite
nonzero correlations of the scalar class indicator. This particular lift
does not supply the desired correlated transverse field state.

The next problem is consequently narrower than "Gibbs invariance versus
transport": obtain a three-dimensional cubic-covariant, permanently labeled
model whose invariant correlations and transport both act on the needed
vector observables, then derive its collective limit. The one-dimensional
countercontrol keeps that route open without claiming it has been solved.

## Evidence and open physical work

See [the complete evidence packet](../.claude/science/mobile-record-local-gibbs-20260921/README.md). The source-bound
runner distinguishes exact identities from floating-point full-generator
controls. The independent reconstruction uses exact arithmetic on separate
finite generators and verifies the general written stationarity arguments.

No Hamiltonian is selected by the axioms here. No phase, correlation length
suitable for a physical vacuum, hydrodynamic limit, quantum carrier, Lorentz
symmetry or gravity is derived. Combining a relevant three-dimensional vector
correlation law with propagating transport remains an open construction.
Combined pipeline, strict audit lint, negative-claim packet/schema and
changed-evidence integration remain pending before any landing candidate.
