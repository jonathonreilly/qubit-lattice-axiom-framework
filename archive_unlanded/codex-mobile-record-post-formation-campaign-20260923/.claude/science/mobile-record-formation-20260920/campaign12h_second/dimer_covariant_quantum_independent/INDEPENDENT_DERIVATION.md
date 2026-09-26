# Independent reconstruction of the supplied mixed encoding

The complete frozen note at SHA-256
`5b53badd77e2a61b100eb8a3b048986895e78f9904f12d5b79b41dbb25b2a91a`
was read before this reconstruction. Its checker and outputs remain unopened.
The inherited classical wave coefficients are used only as a conditional
target; no quantum dynamics is inferred from the classical process.

## Density, covariance and readout

In the orthonormal basis `s,t_i=(sigma_i tensor I)s`, the encoding is
`rho=[[q,w^dagger],[w,r I]]`, with q+3r=1 and q,r>0. Its two transverse
triplet eigenvalues are r; the remaining eigenvalues are

`(q+r +/- sqrt((q-r)^2+4||w||^2))/2`.

Strict positivity is equivalent to `||w||^2<qr`. On the two supplied label
orbits, the squared norms are lambda_A^2 and 3lambda_B^2, so the stated
maximum condition is exactly the needed uniform strict inequality. The
rational example gives Schur complements 13/32 and 55/128. Equality produces
a singular state; exceeding the inequality can produce a negative eigenvalue.

For proper rotations, a simultaneous physical spin rotation acts in this
basis as diag(1,R), and w transforms to Rw. Endpoint swap is diag(-1,I_3),
so it sends w to -w and exchanges opposite oriented colors. This is not a
claim of full polar/axial reflection covariance.

Let `A_i=|s><t_i|+|t_i><s|` and
`B_i=i(|t_i><s|-|s><t_i|)`. Direct Pauli multiplication gives
`A_i=(sigma_1i-sigma_2i)/2` and
`B_i=-(sigma_1 cross sigma_2)_i/2`, including the minus sign. Their means
are 2Re(w_i) and 2Im(w_i). Thus the population image has exactly six real
tangent dimensions; the remaining seven tangent directions are lost. A and
B orbit-isotropic averages both give rho_0, regardless of their orbit masses.
This readout of means does not give perfect one-sample label identification.

At rho_0, products give

`<A_i A_j>=<B_i B_j>=(q+r)delta_ij`,
`<A_i B_j>=i(q-r)delta_ij`.

Consequently `V=(q+r)I_6`, `Sigma=2(q-r)J`, and
`<O_a O_b>=V+i Sigma/2`, whose eigenvalues are 2q and 2r, each threefold.
The limiting CCR has rank six for q!=r. At q=r=1/4 its expectation form
vanishes although the individual finite-block commutators are not zero.
For example, at q=1/2,r=1/6, the centered empirical average of
`-i[A_1,B_1]` has exact mean-square variance 20/(9K).

## Ordered Weyl products, with an explicit remainder

Fix a finite sequence of real tests z_j and put `Z_j=z_j.O` and
`M=sum_j ||Z_j||`. Commutativity between distinct tensor factors gives the
exact product factorization stated in the source. The one-block trace of
the ordered product equals `1+b/K+r_K`, where

`b=-1/2 (sum z_j)^T V (sum z_j)
   -i/2 sum_(j<l) z_j^T Sigma z_l`.

The coefficient follows from the diagonal second-order terms
`-<Z_j^2>/2` and ordered cross terms `-<Z_j Z_l>`. The order is essential.
The group-commutator word `A_1,B_1,-A_1,-B_1` has zero summed test but
limiting characteristic value `exp[-2i(q-r)]`. At the rational example this
is `exp(-2i/3)`, not its complex conjugate.

A direct norm bound suffices for convergence. Multiplying the absolutely
convergent exponential series, the norm of the total degree-n coefficient
is at most M^n/n!. Therefore

`|r_K| <= exp(M/sqrt(K))*M^3/(6 K^(3/2))`,
`|b| <= M^2/2`.

Set `R=exp(M)M^3/6` and `D=M^2/2+R`. For K>=2D, the one-block factor is
within 1/2 of one, so its principal logarithm satisfies

`|K log(1+b/K+r_K)-b| <= R/sqrt(K)+D^2/K`.

This proves the ordered Weyl limit and an O(K^-1/2) error for each fixed
sequence, with a finite sequence-dependent constant. It is an elementary
product-state argument, not an interacting quantum CLT or a uniform theorem
over changing frequencies or growing word length.

For uniformly bounded triangular arrays z_j(x), the same constants apply
block by block. Summing logarithms gives the empirical average of the local
quadratic expression b_x plus an O(K^-1/2) remainder. Pairwise empirical
inner-product convergence then gives the stated finite-family limit. The
limiting bracket is the onsite form integrated against that limiting spatial
inner product. In the uniform torus/Riemann-sum setting this is the usual
spatial delta kernel. Arbitrary arrays alone should not be taken to identify
a different prescribed continuum measure or an infinite-dimensional topology.

## Conditional wave normalization and energy

Starting only from the stipulated equations
`Xdot=a curl Y`, `Ydot=-b curl X`, with a,b>0, the rescaled means
`U=2lambda_A X`, `Vfield=2lambda_B Y` have coefficients
`a lambda_A/lambda_B` and `b lambda_B/lambda_A`. Their equality requires
`lambda_B/lambda_A=sqrt(a/b)` and gives speed c=sqrt(ab). Scaling both
lambdas down preserves this ratio and ensures positivity. Equal fourteen
color weights give a=gamma/7,b=4gamma/7, so the rational example's ratio 1/2
has the stated normalization. The new quantum covariance is the covariance
of the supplied pair observables; it is not obtained by identifying it with
the classical color-count covariance.

Curl is self-adjoint on periodic real fields. At nonzero Fourier Q its
Hermitian symbol `C=i[Q cross]` has eigenvalues +|Q|,-|Q|,0. With
`Sigma=s0 J`, s0=2(q-r)!=0, the target L=c J diag(C,C) has the unique
quadratic Hessian

`H=Sigma^-1 L=(c/s0)diag(C,C)`.

It is Hermitian but indefinite, with two positive, two negative and two
zero directions at Q!=0. The negative directions are physical real Fourier
pairs: for Q along z, the real transverse field
`F(z)=(cos z,sin z,0)` satisfies curl F=-F. Its Hessian energy has the negative
sign when c/s0>0; the opposite helicity reverses that sign. Changing the sign
of s0 cannot make both helicities positive. Removing longitudinal modes
removes the zeros, not the opposite signs.

The flow is nevertheless skew-adjoint and preserves both V and Sigma. A
positive conserved norm is not the Hessian generating this flow with the
onsite bracket: the identity Hessian generates onsite rotations instead.
The conclusion is only the stated positive-quadratic-vacuum-energy boundary
for this bracket and full transverse helicity space. Excited-state
linearization, a restricted helicity sector, a different bracket or extra
fields are not excluded.

## Derivative-bracket alternative and zero modes

Take canonical periodic vector fields (Qpot,P), set E=-P and B=CQpot.
For each Fourier mode the linear observable map is
`T=[[0,-I],[C,0]]`. Its bracket is

`T J T^dagger=[[0,C],[-C,0]]`.

The canonical positive semidefinite Hessian is diag(C^2,I)=T^dagger T.
Hamilton's equations then give Edot=C B and Bdot=-C E, including the source's
signs. At Q!=0 the derivative bracket has rank four. The observable map has
rank five because B is transverse while E may retain a longitudinal component;
electric Gauss selection is a separate initial condition. The unobservable
longitudinal Qpot is a gauge direction of this map.

At Q=0, B=curl Qpot is zero. More generally it has zero spatial mean on the
periodic box. The construction therefore does not parameterize arbitrary
harmonic magnetic fields without a separately supplied sector. The source
offers this explicit construction rather than claiming every periodic Maxwell
state is in its image, so this is a scope clarification, not a contradiction.

No microscopic quantum generator, electric-Gauss preparation, unchanged
primitive-projector interpretation or coupling to formation follows from
these identities. The contextual references are not used as theorem imports.
