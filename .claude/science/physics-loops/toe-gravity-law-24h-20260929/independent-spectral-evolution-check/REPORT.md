# Focused independent spectral evolution check

2026-09-30. This is a source-bound mathematical check, not formal review,
audit, retained status, or source landing. No blocking discrepancy was found
in the stated short-time analytic theorem for the supplied full finite
Hamiltonian. The theorem does account for finite product-rule failure and
for the loss of strict Fourier-band support during evolution. It does not
give exact finite first-class closure or a native-M2 gravitational law.

The checked author REPORT has SHA256
`93e302c06d9e6a6c85f3c538f2d765ec1dcb5734065f740b310e9144f6abd6b8`.
The formulation has SHA256
`6e2f18f095420f4c7d501dcdaf3752c80285807cb22b4b41e9aeece01bc91417`.
`SOURCE_BINDINGS.json` binds the remaining exact inputs and states their roles.
Later changes need a changed-source check; this report is not blanket coverage.

## Independence and coverage

I first read only the new CONTRACT and the complete existing spectral law
REPORT. Before opening the new proof, formulation, code, or results, I wrote
`PRECOMPARISON.md`, frozen at 02:56:21 UTC with SHA256
`b8929c03a94f6b2a0f3e868ccfa85e029b2369787f3f596045f41d51d46d3d36`.
That derivation identified the exact derivative augmentation, the adjoint
variation including the derivative of B, analytic radius loss, alias
consistency, compactness, and a needed analytic uniqueness/stability argument.
It did not presume that the candidate theorem was established.

After that freeze I read the complete author REPORT, formulation, diagnostic
source, JSON results, run log, source bindings and freeze manifest. I also read
the complete existing independent spectral-law check. No author code was
imported or executed. The new independent computation reconstructs the
three-dimensional Christoffel Hamiltonian and all six canonical components;
it is not a rerun or re-expression of the author's axial trajectory engine.
The analytic proof remains load-bearing. The floating controls below are
finite samples, not exhaustive polynomial or interval certificates.

## Exact finite Hamiltonian variation

Let the normalized grid mean be used, with density momenta p=n^3 P and
pi_ii=p_ii, pi_ij=p_ij/2. Then mean(pi:delta g)=sum(P_A delta g_A), so the
mean's volume factor cancels the density-coordinate Poisson factor. This
gives the stated velocity without an extra n^3 or off-diagonal factor.

Writing B=sqrt(det g) g^{-1}, q_l=D_l g and r_l=D_l B, skew-adjointness of
the actual Fourier derivative, not a product rule, transforms the curvature
Hamiltonian into mean(T+V), with

    V=K[r_k,ij Gamma^k_ij-r_j,ij Gamma^k_ik
         -B^ij(Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik)].

For an independent metric variation, delta r_l=D_l(B_g delta g).
Consequently the Hamiltonian gradient is

    H_g=T_g+V_g-sum_l D_l V_q_l-B_g^* sum_l D_l V_r_l,
    H_p=T_p.

The B_g factor sits outside D in this adjoint expression. Treating the nine
r matrix entries as independent when differentiating V, then evaluating on
symmetric r, correctly retains both off-diagonal contractions. Replacing
r by B_g q would instead change the finite Hamiltonian.

The equations qdot=D(T_p) and rdot=D(B_g T_p) preserve q-Dg and r-DB
exactly by an ordinary time chain rule. They introduce analysis variables,
not additional canonical degrees of freedom. Every resulting component is
an algebraic local map plus finitely many terms P(U) D_j Q(U). Thus the
augmented system has one spatial derivative loss despite the original
second spatial derivatives. This is true off its consistency manifold as
well, which matters when comparing with sampled continuum trajectories.

## Uniform analytic bounds and existence

The circular Fourier Wiener algebra estimate follows from
|wrap(k+l)|_1<=|k|_1+|l|_1. The same inequality with an additional |k|_1
factor proves the N seminorm product estimate. Neither estimate asserts
the false discrete Leibniz identity. The Cauchy estimate is uniform in J.

The inverse and determinant majorants in the report are valid with the
specified entry-sum matrix norm. In particular, |tr(h^m)|<=|h|^m permits
the exponent 1/2 in the majorant (1-z)^(-1/2); a dimension-dependent
exponent is not missing. The identity matrix contributes norm 3 to the
inverse bound. Differentiating those absolutely convergent scalar majorants
gives the displayed N bounds. Ordinary component derivatives are bounded
using the actual symmetric basis matrices, whose entry norms can be 2.
This gives an explicit finite algorithm for C0, C1, C_h, and the scale
Lipschitz constant C; no unbounded grid-dependent sum is hidden in it.

The proposed C_h is safe: the metric velocity in matrix notation is
2a/sqrt(g) times [g pi g-(1/2)g tr(g pi)], hence its entry norm is bounded
by 3a |g|^2 |pi|/sqrt(g). The entry norm of pi equals the norm of the six
independent p coordinates. The other constants need not be sharp or
numerically evaluated to specify a positive, computable time.

The initial M0 is also safe without an extra factor of three: summing all
three derivative norms gives exactly the |k|_1 seminorm, bounded by the
single Cauchy estimate. The same observation applies to the vector of
initial sampling commutators. The B(g0)-I norm is finite and can be replaced
by a bound depending only on the stipulated h0 norm through the given
series majorants.

On the bootstrap ball, differentiation of the shrinking-radius norm gives
C0+(C1-v)N(U), with v=C1+1. The separately bounded metric velocity keeps
h within 3/16. The stated T0 keeps the total norm strictly inside its ball
and the radius at least 3sigma0/4. These strict bounds close continuity and
finite-dimensional continuation. Entry-norm closeness to I keeps every real
grid metric positive, and the real Hamiltonian preserves reality. No
strong-hyperbolicity or uniform Sobolev estimate has been assumed.

## Continuum limit, uniqueness, and quantitative convergence

Uniform bounds in the stronger radius give Fourier-tail compactness and,
after one radius loss, uniform time equicontinuity. Finite-mode
Arzela–Ascoli and a diagonal limit therefore give convergence in every
strictly smaller radius on the common interval. Fatou retains the stronger
radius bound. Local analytic series commute with pointwise sampling and
their interpolation errors are controlled Fourier tails. Reserving another
radius margin passes each derivative term in the integral equation to the
continuum. The limit has the consistent initial q and r; their exact
time identities show it solves the actual continuum Hamiltonian equation.

The time-ordered Volterra proof supplies the missing uniqueness and rate
step in the precomparison. For m factors between radii separated by d,
allocate d/m to each scale bound. The simplex contribution is at most
(Cm/d)^m t^m/m! <= (eCt/d)^m. The final remainder is multiplied by the
uniform stronger-radius difference bound and tends to zero for eCT<d.
This is essential; merely summing a formal perturbation expansion would
not prove uniqueness. All interpolated trajectories lie in the common
convex metric-safe ball, and time-dependent noncommuting operators retain
their order. Initial and forcing terms sum to the report's estimate (8).
The claim uses the shortened T, not uniqueness over all of T0 without a
further argument.

For the derivative-sampling defect, each original mode outside Q_J has
|k|_1>=J+1 and representative displacement at most 2|k|_1. Splitting the
exponential reserve in half gives exactly 4/(e delta) times
exp[-delta(J+1)/2]. Summing the three derivative components obeys the same
bound, since their combined displacement is bounded by 2|k|_1. The
algebraic maps commute with sampling exactly as grid data; the report does
not falsely identify trigonometric interpolation with an algebra
homomorphism.

With rho2=3sigma0/4 and rho1=sigma0/2, both the source and the initial
q/r mismatch have the claimed exp[-sigma0(J+1)/8] rate. Applying the
Volterra bound between rho1 and sigma0/4 proves the stated convergence to
actual continuum samples. The continuum sample can be inconsistent with
the finite derivative q=D_Jg without invalidating this comparison because
the augmented vector field is defined throughout the ball. Interpolant
convergence adds an even smaller sampling-tail term.

## Constraints and diagnostic normalization

The finite momentum density follows directly from skew summation by parts
in the given G[X]: J_k=pi^ij q_k,ij-2D_j(g_ik pi^ij). Both it and the
literal curvature scalar density use at most one derivative of a local
map of U. Their scale Lipschitz estimate from sigma0/4 to sigma0/8 converts
the state error into a density error. For their separate sampling error
one uses the available stronger continuum radius, not just sigma0/4;
this preserves the advertised exponent.

The continuum identity {G[X],C[1]}=0 gives Jdot=0. The independently checked
continuum CC sign gives {C[N],C[1]}=-G[aK g^{-1}dN], hence
Cdot=partial_j(aK g^ij J_i). Initially zero continuum densities therefore
stay zero. This argument depends on the full continuum algebra already
derived for this supplied law, not on finite coefficient closure or a
finite first-class assertion. The finite constraints can have initial and
subsequent sampling errors.

Inspection of the diagnostic's reflection and translation restriction
supports its reduction to x-dependent diagonal fields: the discarded
off-diagonal variations vanish by actual Hamiltonian symmetries. Its
off-diagonal-free complex-step test and pulled-back Kasner momentum are
normalized correctly. For Kasner exponents p_i, the latter is
pi^ii=sqrt(g)(p_i-1)/(a t g_ii), including the coordinate-stretch factor.
The diagnostic data satisfy the stated small-metric analytic hypothesis.
The saved trajectory errors decrease as reported, but I did not rerun the
trajectory. Its duration 0.01 is not a numerically certified lower bound
for the theorem's T, as the report itself says.

## Independent full-carrier control

`check_full_variation.py` uses real Fourier-sine derivative matrices,
literal three-dimensional Christoffel curvature, arbitrary real fields in
all six metric and momentum coordinates, and couplings a=1.3, K=0.7.
Local independent-slot complex derivatives construct the augmented
adjoint gradient; separate complex derivatives of the original integrated
Hamiltonian test it. All 324 coordinate derivatives on n=3 agree within
4.524e-16. Twenty-four fixed-seed dense tangent directions on n=5 agree
within 3.192e-16. The kinetic velocity also agrees with its direct matrix
formula within 1.388e-16. Original and integrated-by-parts energies agree
within 3.47e-18.

Negative controls are nonzero: using DB=B_g Dg changes r by 2.230e-4 and
changes H by 3.549e-8 on n=3. Omitting the B_g D V_r adjoint term changes
the gradient by 0.006625 there, and by 0.006979 on n=5. Thus the control
actually detects the dangerous finite chain-rule substitution. It also
exercises off-diagonal normalization and all three spatial derivatives.

The one job took 4.754 seconds wall, 3.055 CPU seconds, and 34,816,000 bytes
reported peak RSS, below the priced 30 CPU-second/150 MB limits. CPU was
capped and numerical thread variables were 1. Deadline and stop sentinel
were checked before execution and before each grid. `full_variation.json`
contains the complete results. There was no heavy job, author rerun,
shared edit, or external-source computation.

## Scope and residual obligations

At the exact source-bound scope, the proof establishes a common positive
analytic time, uniform convergence of the actual sampled Hamiltonian
evolutions, and controlled finite constraint error for compatible continuum
initial data. This is materially beyond a coefficient-band identity.
It still supplies the analytic initial data, continuous tensor carrier,
nonlocal spectral derivative, Hamiltonian, lapse and continuum comparison.
It provides no Sobolev well-posedness, long-time stability, exact finite
constraint surface, invariant strict band, original-walker coupling,
physical record clock, native realization, or axiom modification.

This check does not independently certify every prior-art comparison in
the author's manifest. The selected main d31 source comparison files were
unchanged at the observed origin/main 30a9461; the proof itself is bound to
the explicit campaign law and the exact files above. No formal disposition
or downstream claim is implied.
