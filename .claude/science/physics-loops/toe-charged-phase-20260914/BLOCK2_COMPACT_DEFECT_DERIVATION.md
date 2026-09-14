# Compact Villain defect-sector probe

Author derivation in progress; uses the explicitly provisional loop-filling
and coefficient bound in BLOCK2_LOOP_CURVATURE_DERIVATION.md. No independent
review, no compact Coulomb-phase conclusion, and no Hamiltonian identification.

## 1. Exact extension of the determinant on physical Villain sectors

Use the full internal cochain complex of a contractible rectangular box,
with C=d1 from links to plaquettes and D2=d2 from plaquettes to three-cells.
This is a different boundary convention from the exterior Dirichlet Maxwell
exhaustion in the noncompact field construction. Normalize compact charge to
integer e=1; weak coupling is controlled by beta in the Maxwell term.

For each rooted closed fermion walk gamma choose the integer plaquette
filling s_gamma from the stable-axis construction. The convergent log-loop
expansion defines a real function on all real plaquette fields,

    L_tilde(F)=2 Re sum_gamma a_gamma exp(i<s_gamma,F>).

Here a_gamma includes the exact spin trace, M^(-length), alternating log
sign and 1/length. At F=C theta+2 pi n with integer plaquette n,

    exp(i<s_gamma,F>)=exp(i<gamma,theta>).

Hence exp L_tilde(F) equals the paired massive determinant on EVERY Villain
sector. The statement uses integer charge and integer filling multiplicities;
a generic real charge in the same 2pi convention would not obey it.

The area/incidence proof applies to arbitrary plaquette variations u, giving

    |Hess L_tilde(F)[u,u]| <= c_d,m(q)||u||^2.

No Bianchi condition on u is needed. The coefficient series and derivative
series converge uniformly per plaquette by the same polynomial-times-q^n
majorant. The extension away from physical affine sectors depends on filling
choice, but all its physical sector values are the original determinant.

For the d=4 Wilson blocks with real r,t0 every spin trace is real: expand the
product in real Clifford coefficients, reduce every gamma word to a signed
ordered Clifford monomial, and use zero trace for every nonempty monomial.
For a nonempty ordered monomial of even degree choose a contained gamma;
for odd degree choose an absent gamma (odd degree is at most 3 in d=4).
Conjugation by that gamma reverses the monomial sign, proving its trace
vanishes. The identity monomial has trace 4. Thus the spin trace is real.
Each loop then contributes a real coefficient times cos(<s_gamma,F>), so
L_tilde is even on the FULL plaquette space. This coefficient-level argument
is stronger than evenness restricted to exact fields. Generic complex
hoppings require a separate evenness proof or an explicitly evenized model.

Set S(F)=beta||F||^2/2-L_tilde(F), beta>c=c_d,m(q). Then, on the full
plaquette vector space,

    kappa I <= Hess S(F) <= K I,
    kappa=beta-c>0, K=beta+c, S(-F)=S(F).

## 2. Marginal curvature without a volume prefactor

Decompose plaquette space orthogonally as X=range C and Y=X^perp. For y in Y
set

    Z(y)=integral_X exp[-S(x+y)] dx, R(y)=-log Z(y).

Gaussian tails and bounded derivatives justify differentiation. For vectors
v in Y the exact second derivative is

    R''[v,v]=E S_yy[v,v]-Var(S_y[v]).

Brascamp-Lieb in x bounds the variance by
E <S_xy v,S_xx^(-1) S_xy v>. Thus R'' is bounded below by the expectation
of the Schur complement of S_xx in Hess S. Since Hess S>=kappa I,
min_u <(u,v),Hess S (u,v)> >=kappa||v||^2; its minimizer is exactly the
Schur-complement quadratic form. The upper bound follows by dropping the
nonnegative variance. Consequently

    kappa I_Y <= Hess R(y) <= K I_Y.

Evenness implies R'(0)=0. Integrating along the segment from zero to y gives

    exp[-K||y||^2/2] <= Z(y)/Z(0) <= exp[-kappa||y||^2/2].  (C2.1)

The ratio is for an actual constrained marginal. Comparing separate
Gaussian partition functions would instead introduce an unjustified
volume-growing factor and is not the argument used here.

## 3. Periodization and integer sector labels

Let Gamma=C Z^E, an integer lattice spanning X. Push normalized link Haar
measure on T^E through C to Haar measure on X/(2pi Gamma). Decompose the
Villain integer plaquettes into cosets [n] in Z^P/Gamma and unfold the
fundamental domain separately in each coset. This gives a common
sector-independent covolume factor times

    sum_[n] Z(2pi Q n), Q=I-P_X.

The tangent shift 2pi P_X n is absorbed in x. Gauge-kernel multiplicities
are accounted for by the Haar pushforward; no unnormalized gauge volume
is silently set to one. The factor is 1/covol(2pi Gamma), for Euclidean Lebesgue measure on X.
It cancels in all sector ratios. Surjectivity of the pushforward follows
because every x in X has a real link preimage; changing that preimage by
2pi integer links changes x by 2pi Gamma.

For the full cell complex of a contractible box, integral cellular
cohomology H^2=0 gives ker(D2 over Z)=C Z^E. Thus the sector label is
m=D2 n, with one coset per admissible integer three-cochain m. H^3=0
identifies the admissible set with ker d3 in dimensions where that next
map is present. An explicit integer contracting homotopy proves these claims. On an interval,
let h:C^1->C^0 be (hf)(x)=sum_(t=0)^(x-1) f(t), and let pi on C^0
replace a function by its value at the base vertex, with pi=0 on C^1.
Then dh+hd=I-pi. On the graded tensor product of d interval complexes use

    H=h_1 tensor I + pi_1 tensor h_2 tensor I + ...
      + pi_1 tensor ... tensor pi_(d-1) tensor h_d.

The tensor differential has its usual degree signs. The displayed h_i terms
are graded tensor maps; the preceding pi factors force preceding degrees
to zero whenever the term is nonzero. Cross terms cancel by the graded
Leibniz rule and the interval identities telescope, giving

    dH+Hd=I-pi_1 tensor ... tensor pi_d.

All matrices have integer entries. On a closed positive-degree cochain z,
the final projection vanishes, so z=d(Hz) with an INTEGER primitive. This
establishes exactness over the integers, including degree 2 and degree 3;
real rank counts would not suffice. The separate integer-matrix runner checks
the full identity on boxes in dimensions 2,3,4 and checks unit nonzero Smith
invariant factors on the one-interval boxes.

Writing y_m=2pi Q n, (C2.1) compares each actual determinant-coupled defect
sector with the no-defect sector. Since D2 P_X=0 and ||D2||^2<=4d,

    ||y_m||^2 >= (pi^2/d)||m||^2,
    w(m)=Z(y_m)/Z(0) <= exp[-a||m||^2],
    a=kappa pi^2/(2d), w(0)=1.                            (C2.2)

The operator-norm estimate follows by compression of the infinite cubical
exterior derivative, whose Fourier norm is at most |q(k)|<=2sqrt(d).

## 4. A density bound, not a phase theorem

Let N3 be the number of three-cells and Qm=||m||^2. For 0<s<a, the normalized
sector ensemble obeys

    E exp(s Qm) <= [sum_(z in Z) exp(-(a-s)z^2)]^N3,

because its partition function is >=w(0)=1 and dropping the integer
closed-current constraint only enlarges the numerator. Jensen and s=a/2 give

    E Qm/N3 <= (2/a) log theta(a/2)
                <= 4 exp(-a/2)/[a(1-exp(-3a/2))],         (C2.3)
    theta(b)=sum_(z in Z) exp(-b z^2).

The last estimate uses z^2>=1+3(z-1) for positive integers z and log(1+x)<=x.
For d=4,m=4,q=1/20,beta=100, the exact majorant certificate
c<=6.6164 gives kappa>=93.3836. In (C2.3), a>115 using pi>3.14.
The positive rational Taylor partial sum through degree 200 proves
exp(57.5)>9*10^24, and exp(172.5)>100 already follows from 1+172.5.
Consequently the displayed upper bound is strictly less than 4*10^(-27).
This is a conservative supplied-model parameter point, not a physical fit.

Occupied-current-cell density is also bounded by this expression, since a
nonzero integer component has square at least one. This bound is independent
of volume and does not assert that the whole finite box is defect-free.

## 5. Exact stronger consumer still missing

The full Villain field obeys dF=2pi m, so the exact Bianchi identity used in
the noncompact non-summability theorem no longer holds. Conditional covariance
at fixed defect sector gives a transverse lower bound for F, but the defect
contribution can fill the vanishing Fourier directions. Projecting to P_X F
would restore closure at the price of a nonlocal observable; that does not
solve the local-field problem.

A possible terminal estimate is a small long-wavelength current covariance,
schematically Cov(m) <=epsilon d2 d2^* with sufficiently small epsilon.
Along an axis outside a tested plaquette plane, dF=2pi m would then bound
that plaquette's Fourier covariance above by 4pi^2 epsilon. Its transverse
lower bound is 1/K, so 4pi^2 epsilon<1/K would preserve a directional
separation. This is a proposed consumer, not a proved implication for the
actual interacting current ensemble until its limiting and normalization
hypotheses are established. Density (C2.3) alone supplies no such estimate.

Summing closed interacting monopole loops with a controlled area/response
bound remains the phase task. Positivity, convexity and the individual
sector Gaussian comparison do not automatically supply positive Fourier
type or an infrared-uniform cluster expansion. No axiom update follows.

## 6. Two distinct inference controls

BLOCK2_RESPONSE_DENSITY_COUNTEREXAMPLE.md gives a stationary ensemble of
closed integer currents with component second moment rho and required
infrared-response coefficient at least rho L^3/2. It is a comparison
ensemble, not the determinant-coupled gas. The finite direct-boundary Fourier
check verifies the area enhancement and exact integer conservation. Thus
one must use more of the actual action than density and closedness.

Positive Fourier type also fails for a supplied member of the actual Wilson
family. On a single open square, with four spin components, r=2,t0=2,M=80,
exact integer complex-matrix determinants obey

    det D(flux 0)  =2793699536637539555790009139456,
    det D(flux pi) =2793707190016896642234870398976.

Both are positive, the second is strictly larger, and M>8*t0*(|r|+1)/2.
The paired weight therefore has W(pi)>W(0). A continuous function of positive
Fourier type would obey |W(phi)|<=W(0). This supplies an actual family
counterexample to an unrestricted positive-Fourier-type import; it does not
settle the special r=1 family, and does not disprove phase stability.
The source proof in Frohlich-Spencer section 2.12 uses positive Fourier type
at equation (2.99). Its use for the present family needs replacement or a
separately verified narrower hypothesis.

A full four-dimensional box gives a second certificate, with all 16 vertices
of {0,1}^4, the same r=2,t0=2 and M=10000. Change one corner link from +1
to -1. The length-two trace is unchanged and the exact fourth-power trace
difference is -1344. Therefore the leading change in log W is +672/M^4.
Both log-series tails together, starting at length 6 by bipartiteness, are
bounded by (4*64/6)q^6/(1-q), q=24/M. Exact rational comparison gives

    log W(flipped link)-log W(all links +1)
       >=672/M^4-(4*64/6)q^6/(1-q)>0.

This verifies the obstruction on a full d=4 box, using an independent finite
trace/remainder certificate rather than an ill-conditioned float subtraction.
