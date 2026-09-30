# Independent pre-comparison spectral constraint derivation

This is a root analytic check begun from the target contract, before reading
any spectral-route coefficient source or runner. The worker's brief identified
ADM, a full odd Fourier carrier, a low-band evaluation and a conservative
5B<=J condition. Those choices are shared; no coefficient calculation is.
This is not a formal source review or an adopted framework law.

Use g_ij=delta_ij+h_ij, symmetric momentum tensor pi^ij, and six independent
canonical momenta P_ii=pi^ii, P_ij=2pi^ij for i<j. The supplied continuum
canonical functionals are

 C[N]=integral N {a/sqrt(g) [g_ik g_jl pi^ij pi^kl-(g_ij pi^ij)^2/2]
                         -K sqrt(g) R(g)},
 G[xi]=integral pi^ij L_xi g_ij.

Here {g,P}=+1 in the six-entry convention and G generates positive Lie
variation of g. For the former block112 kinetic normalization a=1/(4alpha).
These are continuum comparator inputs, not a derivation from the axioms.

## Algebraic kinetic jets

Let t=tr h, u=tr(h^2), and regard pi as a symmetric flat matrix. Put
 A0=tr(pi^2)-(tr pi)^2/2,
 A1=2tr(h pi^2)-(tr pi)tr(h pi),
 A2=tr(h pi h pi)-(tr(h pi))^2/2.

Counting h and pi as degree one, the kinetic pieces through degree four are
 T2=a A0,
 T3=a[A1-t A0/2],
 T4=a[A2-t A1/2+(t^2/8+u/4)A0].

The momentum generator is exactly degree one plus degree two:
 G1=2 integral pi^ij partial_i xi_j,
 G2=integral pi^ij[xi^k partial_k h_ij+h_ik partial_j xi^k
                                           +h_kj partial_i xi^k].
There is no G3 in these metric coordinates. The inverse metric is
 delta-h+h^2+O(h^3). These formulas follow by direct matrix multiplication
and det(I+h)^(-1/2), without a finite-difference product rule.

## Continuum normal-bracket sign and coefficient

For the curvature convention
 R_ij=partial_k Gamma^k_ij-partial_j Gamma^k_ik
       +Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik,
variation of the potential V[N]=-K integral N sqrt(g)R gives

 delta V[N]/delta g_ij=K sqrt(g)[N Einstein^ij
                               -nabla^i nabla^j N+g^ij Delta N].

The kinetic momentum derivative is 2aN/sqrt(g) times
 S_ij=pi_ij-(tr_g pi)g_ij/2. Its contraction with
 nabla^i nabla^j M-g^ij Delta M equals pi^ij nabla_i nabla_j M:
the two trace pieces cancel in three dimensions. Algebraic NM terms cancel
on antisymmetrizing. Therefore

 {C[N],C[M]}=2aK integral pi^ij[N nabla_i nabla_j M-M nabla_i nabla_j N]
            =aK G[g^(-1)(N dM-M dN)].

The first-derivative NM cross term vanishes against symmetric pi. The sign
is positive for the displayed Hamiltonian and canonical convention.
Diffeomorphism covariance of the scalar density gives
 {G[xi],C[N]}=C[xi dot dN],
 {G[xi],G[eta]}=G[[xi,eta]], [xi,eta]=xi dot d eta-eta dot d xi.
Field-dependent smearing must remain inside PB when checking Jacobi.

## Optional same-metric scalar as an explicit different matter input

For an independent real canonical pair phi,p_phi, the supplied scalar terms

 C_phi[N]=1/2 integral N[p_phi^2/sqrt(g)
                        +aK sqrt(g)g^ij partial_i phi partial_j phi],
 G_phi[xi]=integral p_phi xi^i partial_i phi

give the same aK structure coefficient directly from the scalar PB. Mixed
metric/scalar normal brackets are algebraic in N M and cancel on
antisymmetrization: C_phi has no metric momentum and the gravity potential
has no scalar variable. The sum transforms as one scalar density under the
sum of both Lie generators. Thus this optional common-action input is
compatible at continuum level. It is NOT the original finite-difference
walker or marked rotor instrument and cannot repair those by substitution.

## Finite Fourier coefficient transfer to be compared

Let n=2J+1 and all independent grid canonical variables be available. Define
D_j by multiplier ik_j for integer modes -J,...,J and pointwise grid products.
It is skew adjoint for the normalized grid sum. Do not impose a projected
Poisson bracket or delete high variables before differentiating.

At a low-band evaluation, each field and each independent smearing has
coordinate bandwidth B. A degree-p smeared local differential polynomial
has first variation containing p factors (p-1 fields and one smear), hence
bandwidth at most pB. This includes the terms obtained by discrete summation
by parts; D does not increase support. If the entire expression tree has
at most five low-band factors at every multiplication, 5B<=J prevents any
alias in those values and functional derivatives. The normalized quadrature
then equals its continuum torus mean on every involved term.

For normal brackets through field degree three one needs C1,...,C4:
p+q-2<=3, so p+q<=5 (terms with p=0 are absent). Nested brackets through
degree two need p+q+r-4<=2, so at most six field degrees before two
contractions, leaving at most five factors after including three smearings.
Every needed intermediate derivative/product must be checked against that
count explicitly; this is not justified by the final integral alone.
For the scalar extension its background is phi=p_phi=0 and it begins at
degree two. The same total-degree count applies.

The finite-grid canonical bracket always obeys Jacobi. That fact alone does
not prove the proposed structure functions describe its constraints. The
transfer argument must first establish the relevant coefficient identities,
including derivative-of-structure terms. No invariant low-band flow follows:
nonlinear products generate higher modes, even if a finite-order evaluation
identity is exact. No full-zone lattice diffeomorphism theorem is asserted.

## Open coverage at this pre-comparison stage

The worker's explicit curvature jets, exact grid normalization/rephasing,
full coefficient-transfer tree, tests and claim scope have not been read.
This pre-comparison provides independent kinetic coefficients, bracket signs,
scalar cross-cancellation and a support-count candidate for the eventual
focused check. It does not yet certify the complete spectral construction.
