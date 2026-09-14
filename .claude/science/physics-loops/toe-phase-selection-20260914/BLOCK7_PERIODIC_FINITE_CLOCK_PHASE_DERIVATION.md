# Periodic finite-clock Villain masslessness: complete author proof draft

Personal derivation, 2026-09-14. **Provisional, pending full author review and
selective independent review.** The finite checks accompany, but do not prove,
the uniform claims. This is an explicit rederivation of a known kind of
four-dimensional finite-group Coulomb-phase mechanism, informed by the
Fröhlich–Spencer preprint. It is not a novel claim that finite clock gauge
models can have a massless phase, a derivation of the repository's selected
continuous-time Hamiltonian, or an axiom-selected law.

## 1. Statement and conventions

Let T_L=(Z/LZ)^4, with L even and L>=4. Use one canonical positive orientation
for each cell and the ordinary Euclidean inner product on cochains. Write
d_k:C^k->C^(k+1) for coboundary and delta_(k+1)=d_k^T for its adjoint.
In formulas on one-forms set d=d_1, Q=d^T d, V=Q^+. On two-forms write
P_e, P_c, P_h for the orthogonal exact, coexact and harmonic projections.
The two-form harmonic space has dimension six. The projections sum to I.

For a positive integer N>=2, link angles take values 2pi Z/N modulo 2pi.
The normalized isotropic periodic measure has density proportional to

  product_p phi_beta((d theta)_p),
  phi_beta(t)=sum_(n in Z) exp[-n^2/(2 beta)] exp(i n t), beta>0.

Poisson summation makes phi_beta strictly positive. Its real smooth score
s_beta(t)=phi_beta'(t)/phi_beta(t) is odd and bounded on the circle. Let
s_p=s_beta((d theta)_p). All statements below concern this specified model.

Define

  beta_1=(107 log 3+log 4)/(4pi^2),
  a(beta)=beta/384-beta_1, q(beta)=exp[-2pi^2 a(beta)],
  S_j(q)=sum_(r>=1) r^j q^r,
  c(beta)=[8503056 S_6(q(beta))+262144 S_5(q(beta))]/[a(beta)e],
  delta(beta)=beta c(beta).

We use c only for beta>=2000, so a>0 and every damping bound used below is
valid. The proposed theorem is:

* For beta>=2000 and beta_d=N^2/(4pi^2 beta)>=2000, every local subsequential
  limit of these equal-side even tori is translation invariant, cubic
  invariant, charge-conjugation invariant, and site/link reflection positive
  on its gauge-invariant algebra.
* For any fixed plaquette orientation, its bounded score correlation tends
  to zero at large separation but is not absolutely summable over Z^4.
* The positive time-translation contraction reconstructed in this state has
  spectrum accumulating at one from below. Its observable sector has no
  positive gap above its full eigenvalue-one subspace.

An explicit sufficient example is beta=2000, N=16384. These are conservative
existence constants, not estimates of a transition. No assertion here
identifies a unique periodic-limit phase, proves a finite-cylinder gap
limit, or sends a time lattice spacing to zero.

## 2. Exact lattice duality, including composite N

Expanding every plaquette weight and summing link characters gives the
centered discrete Gaussian on the full-rank two-form lattice

  L_N={n in Z^P : delta_2 n belongs to N Z^E},
  probability(n) proportional to exp[-||n||^2/(2 beta)].

Let its covariance be C_N(beta). Its dual lattice is exactly

  L_N^*=Z^P+(1/N)d Z^E,
  M_N=N L_N^*=N Z^P+d Z^E.

Indeed, the annihilator of ker(delta_2 mod N) in the perfect character
pairing of (Z/NZ)^P is im(d mod N). Inclusion follows by adjunction. Equality
of cardinalities follows from the identical Smith invariants of an integer
matrix and its transpose. This argument does not treat Z/NZ as a field.

Let D_N(beta_d) be the covariance of the centered discrete Gaussian on M_N
with variance parameter beta_d=N^2/(4pi^2 beta). Poisson summation with a
real linear source, differentiated twice at zero, gives the exact identity

  C_N(beta)/beta+D_N(beta_d)/beta_d=I.                 (2.1)

For clarity, before rescaling the dual source contributes
-4pi^2 beta^2 Cov_(L_N^*)(y) to the primal covariance, while completing the
square contributes beta I. Since m=N y, this is precisely (2.1).
Both covariances are positive semidefinite, so C_N(beta)<=beta I.

The next sections prove a lower covariance bound for EVERY affine coset of
the integer-curl lattice K=d Z^E in its real span S=im d. They do not assume
the coset's Gaussian mean vanishes.

## 3. The shifted integer-curl theta function

For a real one-form a, put

  Z_K(a)=sum_(F in K+d a) exp[-||F||^2/(2 beta)].

The dual K^* is a full-rank lattice in S. The map

  y -> k=d^T y

is a bijection from K^* to Z^E intersect range Q, with inverse y=d V k and
||y||^2=k^T V k. Thus Poisson summation represents Z_K(a), up to a positive
a-independent factor, as

  sum_(rho in 2pi Z^E intersect range Q)
      exp[-beta rho^T V rho/2] exp[i rho(a)].         (3.1)

All derivatives in a of this finite-dimensional Gaussian Fourier series
converge absolutely. There is no thermodynamic interchange in this step.

Let H=(ker d+Z^E)/Z^E, a connected compact subgroup of the one-form torus.
Its annihilator is Z^E intersect range Q. Haar averaging the Fejer product

  product_e Fejer_h(A_e+a_e+h_e),  h in H,

then averaging A as a centered Gaussian of covariance beta V on range Q,
gives the Fejer regularization of (3.1). Each Fourier coefficient is a
product of numbers in [0,1] that tends to one as h->infinity. Dominated
convergence therefore holds through two derivatives, for fixed L and beta.

The subgroup H can equivalently be averaged by vertex gauge angles and
constant real one-forms modulo one. The pushforward of these compact Haar
measures is Haar on H: their real tangent spaces span ker d, and their
image is all of the connected compact group. The possible finite overlap
does not change normalized Haar measure.

## 4. A finite positive mixture of separated currents

For k>=1 set z_k=4k^2. The Fejer polynomial is

  Fejer_h(x)=1+2 sum_(k=1)^h (1-k/(h+1)) cos(2pi kx).

It is a convex combination of 1 and the factors 1+z_k cos(2pi kx), with
respective nonconstant weights 2(1-k/(h+1))/z_k. The leftover constant
weight is positive because sum_(k>=1)1/(2k^2)<1. For example
sum k^-2 <1+integral_1^infinity x^-2 dx=2 proves this strictly.

Products give positive mixture weights and at most one oscillator on each
occupied edge. **The individual initial factors can be negative.** Positivity
of each final phase integrand will be established only after Gaussian
damping. It is not assumed at this initial step.

For two factors use the exact identity

  (1+A cos x)(1+B cos y)
  =(1+3A cos x)/3+(1+3B cos y)/3
    +(1+3AB cos(x-y))/6+(1+3AB cos(x+y))/6.         (4.1)

Repeatedly apply (4.1) to currents whose edge supports have Euclidean
distance <=1, using periodic distance on the torus. In each branch two
currents are replaced by one, so the construction terminates. The branch
weights are positive and sum to one. Current supports remain disjoint;
adding or subtracting two disjoint currents cannot cancel an occupied edge.
Each final support is connected in the distance-one proximity graph, and
different final supports have distance >1. Every final integer frequency
on an occupied edge equals the original frequency up to sign.

Here is the amplitude bound with its ancestry counted explicitly. A final
current has support S of size r. Trace only operations ancestral to this
current. Its binary mergers contribute r-1 powers of three. A unary
retention contributes one power of three and drops a neighboring current.
At that operation the retained support is a subset of the final S. Choose
one dropped edge at distance <=1 from that retained support. The chosen
edge is outside S. Chosen edges at different unary retentions are distinct,
because a discarded edge never returns on this branch. Hence the number
of unary retentions is at most |N_1(S)\S|. Operations occurring only within
an eventually discarded current are not ancestors of the final amplitude.
Consequently

  K_rho <=3^(|N_1(S)|) product_(e in S) 4 k_e^2.    (4.2)

A canonical edge in Z^4 has 107 canonical edges at distance <=1 from it,
including itself: 23 parallel and 28 in each of the other three directions.
The periodic neighborhood has no more members, since it is the image of
the corresponding lifted neighborhoods. Thus |N_1(S)|<=107r. Also
log(4k^2)<=k^2 log4 for every integer |k|>=1. It follows that

  K_rho <= exp[beta_1 ||rho||^2].                  (4.3)

Vertex gauge averaging now removes the noncoclosed factors. To justify
this factorwise step, expand a final cosine product. Supports of different
currents have disjoint endpoint sets, since their distance is >1. A signed
sum of participating currents has zero divergence exactly when each
participating current does. Every term involving a noncoclosed current
therefore vanishes in the vertex gauge integral. The remaining factors
are coclosed. **Winding currents remain:** their harmonic averages can
cancel in products and are not taken factorwise.

## 5. Exact local Gaussian damping with harmonic currents retained

Color edges by their orientation and the three transverse coordinate
parities. On an even torus these 32 colors are well defined, and no two
edges of one color share a plaquette. For each current choose a color B_rho
with at least 1/32 of its squared norm and keep its occupied edges. Selected
edges from different currents cannot share a plaquette either, since the
currents have distance >1. On this torus Q_ee=6.

Put u_rho(e)=rho_e/6 on selected edges and zero elsewhere, and

  rho_tilde=rho-Q u_rho,
  z_rho=K_rho exp[-beta/2 sum_(e in B_rho) rho_e^2/6].

The new current is coclosed, has the same harmonic component, and vanishes
on its selected edges. For any signed sum R=sum sigma_rho rho that survives
the harmonic average, R belongs to range Q. With u=sum sigma_rho u_rho,

  R^T V R-(R-Q u)^T V(R-Q u)
    =2 R^T u-u^T Q u
    =sum_(rho with sigma_rho !=0) sum_(e in B_rho) rho_e^2/6.  (5.1)

Disjoint original supports and the plaquette nonadjacency of all selected
edges justify every vanishing cross term in (5.1). Terms failing harmonic
neutrality vanish before and after this operation, since Q u has zero
harmonic component. Expanding the cosine product therefore proves the
identity of Gaussian/harmonic integrals with factors transformed to

  1+z_rho cos[rho_tilde(A)+rho(h)+rho(a)].           (5.2)

The external source phase is the ORIGINAL rho(a). It is not rho_tilde(a).
The damping exponent in this convention is beta/2, not beta. Both changes
give explicit finite counterexamples in the accompanying private checks.

From (4.3) and the selected weight bound,

  0<z_rho<=exp[-a(beta)||rho||^2].                  (5.3)

For beta>=2000, a>15/8 and ||rho||^2>=4pi^2 for a nonzero current. Thus
z_rho<1/2 and EVERY transformed factor is strictly positive, at all real
Gaussian, harmonic and source phases. This is where pointwise positivity
becomes available.

## 6. Uniform source curvature: local and large currents

For 0<=z<1, differentiation of log(1+z cos x) gives

  |[log(1+z cos x)]''|<=z/(1-z).                  (6.1)

For example, |cos x+z|<=1+z cos x follows on squaring, and proves (6.1).
It remains to bound, for every final ensemble and w in range Q,

  sum_rho [z_rho/(1-z_rho)] |rho(w)|^2
        <=c(beta)||d w||^2,                      (6.2)

uniformly in L, all frequencies and the Fejer order.

Let r be the number of occupied edges of rho. Always ||rho||^2>=4pi^2 r.
We divide the currents at r=L/8. The support separation is used for
packing, not as a statistical independence assertion.

### Small currents: r<L/8

Connect the r support edges by at most r-1 extra unit edges using a spanning
tree in their proximity graph. Nearest points of coordinate unit edges
with integer endpoints can be chosen as endpoints; when their distance is
<=1, they coincide or one unit lattice edge joins them. The resulting
connected graph contains at most 2r-1 edges. A nonzero-winding simple cycle
on T_L requires at least L edges. Our graph has fewer than L edges, so all
its closed walks have zero winding (decompose a closed walk into simple
cycles). It admits a consistent lift to Z^4, preserving divergence. A
spanning-tree path between any two lifted vertices has length <=2r-1.
Hence the lifted support lies in a box of side R<=2r-1<=3r.

For completeness, an explicit filling uses the coordinate-ordered path
P(x) from the box's minimum corner b to x. For a positive edge e=(x,j),
let K_1(e) be minus the jk plaquette strips for k>j and k-coordinate
b_k,...,x_k-1; coordinates below k are fixed at x and those above k at b.
Telescoping the strips gives

  boundary K_1(e)=P(x)+e-P(x+e_j).

There are at most 3R plaquettes per edge. Summing against a closed rho
cancels all vertex paths and produces a filling mu with delta_2 mu=rho,

  ||mu||_1<=3R||rho||_1<=9 r^(3/2)||rho||_2.

Project this filling back to the torus. Thus

  |rho(w)|^2<=81 r^3 ||rho||^2 max_(p in box) |d w(p)|^2.     (6.3)

Assign each current to one plaquette attaining this maximum. For fixed
r and p, all supports assigned to p lie within coordinate distance <=3r
(allowing endpoint padding) of p. A cube with at most 9r lattice origins
per coordinate is a conservative cover. It contains at most 4(9r)^4
canonical edges, including periodic identifications. The supports are
disjoint and each has r edges, so at most 26244 r^3 currents are assigned
to a fixed p at size r.

Use z/(1-z)<=2 exp(-a||rho||^2), split the exponential into two equal
factors and use t exp(-at/2)<=2/(ae). With b=2pi^2 a, summing (6.3) and
the packing estimate yields

  small-current contribution
       <=[8503056/(ae)] sum_(r>=1) r^6 exp(-br) ||dw||^2.   (6.4)

### Large currents: r>=L/8, including every winding current

The first positive eigenvalue of the scalar torus Laplacian is
4 sin^2(pi/L)>=16/L^2. The one-form Hodge Laplacian is componentwise scalar,
and Q equals it on range Q. Hence

  ||w||^2<=L^2||dw||^2/16.

There are at most 4L^4/r disjoint currents of size r. Cauchy–Schwarz and
the same split of the activity give

  large-current contribution
  <=[L^6/(ae)] sum_(r>=L/8) r^-1 exp(-br) ||dw||^2
  <=[262144/(ae)] sum_(r>=1) r^5 exp(-br) ||dw||^2.          (6.5)

The second step uses L<=8r separately in each summand. It covers large
contractible currents and winding currents without any filling assumption.
Equations (6.4)-(6.5) prove (6.2) with the displayed c(beta).

## 7. Positive integration and all affine cosets

Fix a finite transformed ensemble. Along a source line a+t w the logarithm
of its pointwise positive product (5.2) has second derivative at least
-c(beta)||dw||^2. The logarithm of its Gaussian/harmonic integral has the
same lower bound: differentiating a log integral adds the nonnegative
variance of the first log derivative. Taking the positive mixture of all
ensembles preserves the bound by the same identity. There are finitely
many terms at each Fejer order, so no integrability interchange is hidden.

The C^2 convergence in section 3 and strict positivity of the theta limit
then give

  d^2/dt^2 log Z_K(a+t w)|_(t=0)>=-c(beta)||dw||^2          (7.1)

for every a and w in range Q, uniformly in L. Directions outside range Q
can first be projected since only d a affects the theta function.

For a field source f in S choose w=V d^T f, so dw=f. Completing the square
in the discrete Gaussian on K+d a gives

  Var_a(<F,f>)=beta||f||^2
          +beta^2 d^2/dt^2 log Z_K(a+t w)|_(t=0)
      >=beta(1-delta(beta))||f||^2.                       (7.2)

The sign of the source shift is immaterial for the second derivative.
For a general affine translate b+K in C^2, split b into its S and S^perp
parts. The perpendicular part is deterministic, contributes a constant to
the Gaussian norm and linear source, and contributes no covariance. Thus
the general statement is

  Cov_(b+K)(F)>=beta(1-delta(beta)) P_e                    (7.3)

for EVERY affine translate, regardless of its conditional mean.

The signed Hodge map from the periodic primal lattice to its translated
dual is an integral isometry and takes delta_3 Z^C to d Z^E on the dual
lattice. In the explicit cell convention used by the finite runner,
star_2 delta_3=-d_1 star_3. Its minus sign leaves the integer lattice and
the covariance estimate unchanged. Therefore (7.3) applies to the integer
coexact lattice with P_e replaced by P_c and identical constants.

## 8. Coset decomposition and the two-sided covariance bound

Partition L_N into cosets of delta_3 Z^C, which is a sublattice since
delta_2 delta_3=0. Each conditional distribution is one of the affine
Gaussians in (7.3). Total covariance adds the positive covariance of the
conditional means, so

  C_N(beta)>=beta(1-delta(beta))P_c.                      (8.1)

Similarly d Z^E is a sublattice of M_N. Its affine-coset lower bound gives
D_N(beta_d)>=beta_d(1-delta(beta_d))P_e. Substitution in (2.1) yields

  beta(1-delta(beta))P_c <= C_N(beta)
       <=beta P_c+beta delta(beta_d)P_e+beta P_h.          (8.2)

In addition C_N(beta)<=beta I by (2.1). Harmonic modes have not been
discarded at finite volume. Each fixed local matrix element of P_h tends
to zero like L^-4.

## 9. A conservative parameter certificate

Elementary bounds log3<1.1, log4<1.4 and pi>3 imply beta_1<10/3. For
beta=2000, a>15/8, and hence q<exp(-135/4)<2^-48, using log2<.7.
For 0<=q<=1/1024,

  S_5(q)=q(1+26q+66q^2+26q^3+q^4)/(1-q)^6,
  S_6(q)=q(1+57q+302q^2+302q^3+57q^4+q^5)/(1-q)^7.

Both are at most 2q. Indeed the larger numerator divided by q is bounded
by 1+719q, the smaller denominator is at least 1-7q by Bernoulli, and
(1+719/1024)/(1-7/1024)<2. Consequently

  delta(2000)<(3200/3)*8765200*2^-48<1/1000.               (9.1)

Here beta/a<3200/3 and e>2 account for all factors. Since beta/a decreases
as beta increases, while q, S_5 and S_6 decrease, delta(beta) is decreasing
for a>0. Thus delta(beta)<1/1000 for every beta>=2000. In particular
delta(beta)+delta(beta_d)<1 under the stated parameters.

For beta=2000 and N=16384, even the rough pi<4 bound gives
beta_d>N^2/(64*2000)>2000. This exhibits finite parameters without numerical
critical-coupling extrapolation.

## 10. Physical score, contact term and infinite-volume spectrum

For distinct plaquettes, differentiation of the Fourier expansion gives

  E(s_p s_q)=-E(n_p n_q), p!=q,
  E(n_p^2)=E[-phi_beta''((d theta)_p)/phi_beta((d theta)_p)].

Charge conjugation sets all one-point means to zero. Define
kappa=E[-(log phi_beta)''((d theta)_p)]; isotropy makes it orientation
independent. The exact contact identity is

  C_s(p,q)=kappa delta_(p,q)-C_N(beta)(p,q).               (10.1)

The diagonal insertion is -phi''/phi, not the square of phi'/phi. All
physical expressions on the right of the insertion identities are bounded
local functions at fixed beta and N.

Take any local subsequential limit along even L->infinity, available by
compactness of the finite link alphabet. The preceding identities pass to
this limit. The finite-range test-form version of (8.2) passes as well:
the Fourier projectors converge to their infinite-volume lattice versions,
and the local harmonic matrix elements vanish. The additional bound
C_N<=beta I passes to a bounded positive convolution operator C_n on
ell^2(Z^4;R^6). Its Fourier multiplier S_n is an L-infinity matrix density.
Since the Brillouin torus has finite measure, its entries are integrable;
the Riemann–Lebesgue lemma gives C_n(x)->0. Equation (10.1) then gives
C_s(x)->0 for each orientation component.

For k!=0 write v_i(k)=exp(i k_i)-1. For plaquette orientation ij,

  P_e,ij,ij(k)=(|v_i|^2+|v_j|^2)/sum_a |v_a|^2,
  P_c,ij,ij(k)=1-P_e,ij,ij(k).

If its score covariance were in ell^1(Z^4), its Fourier transform would
be continuous. Equation (10.1) would then give a continuous representative
of the same diagonal of S_n. The almost-everywhere bounds (8.2) extend
pointwise away from zero by continuity. Along an axis outside {i,j},
the diagonal is at least beta(1-delta(beta)); along an axis in {i,j}, it
is at most beta delta(beta_d). Their limiting intervals are disjoint by
(9.1). No continuous value at zero is possible. Thus the bounded score
correlation clusters but is not absolutely summable.

This is a directional discontinuity argument, not a claimed exact photon
dispersion or a pointwise power-law asymptotic.

## 11. Reflection positivity and the reconstructed gap

Translations, cubic symmetries and charge conjugation hold on every equal
periodic torus and pass to local limits. Site reflection positivity follows
by conditioning on the fixed reflection planes and factorizing the two
halves. For link reflection, fix the crossing normal links on the two
reflection planes to the identity. Those crossing links form a forest for
even L>=4, so this is a valid finite gauge fixing on gauge-invariant
functions. Every crossing plaquette weight is a positive character sum:
its finite-Z_N Fourier coefficient in residue r is
sum_(n congruent r mod N) exp[-n^2/(2 beta)]>0. Expanding those sums expresses
the reflected integral as a sum of squared half-integrals with positive
weights. This proves link reflection positivity in the same state. There
is no claim that log(phi_beta) has nonnegative Fourier coefficients.

For the gap implication, form the OS space from bounded gauge-invariant
local functions at times >=0, with inner product
(F,G)=E[(Theta_0 F)G], modulo null vectors. Reflection includes complex
conjugation. Time translation induces T[F]=[tau_1 F]. Translation and
reflection symmetry make it symmetric. Link reflection about time -1/2
makes (F,T F)>=0. Site reflection positivity and Cauchy–Schwarz imply

  ||T F||^2<=||F|| ||T^2 F||.

Iterating the corresponding norm inequality and using
||[tau_m F]||<=||F||_infinity gives ||T F||<=||F||, including the null-vector
case. Thus T descends and extends to a positive self-adjoint contraction.
Spatial translations U_y are commuting unitaries and commute with T.

Let P_1 be its FULL eigenvalue-one projection. It need not have rank one.
For any centered score slab G, the cluster property already proved makes
(G,T^t G)->0 (reflection may change its sign and translate its anchor).
The spectral theorem then implies P_1[G]=0.

For bounded slab functions F,G supported in times [0,1], put
F^sharp=tau_1 Theta_0 F. The exact geometry is

  E[F tau_(R,y) G]=([F^sharp],T^(R-1) U_y[G]), R>=1.

If T had a spectral gap gamma>0 below its full P_1, every pair of the
centered score slabs would therefore satisfy

  |E[F tau_(R,y)G]|<=||F||_infinity||G||_infinity exp[-gamma(R-1)].

Rotate a largest coordinate of a separation x into the time direction.
Cubic invariance preserves the bound and only changes score orientation
or sign. This would give a common constant times
exp[-gamma max(||x||_infinity-1,0)] for each score correlation on Z^4,
which is absolutely summable. Section 10 contradicts this. Hence no such
gap exists. The nonzero score sector forces spectral values below one
arbitrarily close to one; degeneracy inside P_1 does not provide a loophole.
On the positive spectral support, H=-log T is correspondingly gapless.

## 12. Provenance and remaining review gates

The organizing literature source is Fröhlich–Spencer, *Massless phases and
symmetry restoration in Abelian gauge theories and spin systems*, CMP 83
(1982), DOI 10.1007/BF01213610, read through the public preprint
https://omeka.ihes.fr/document/P_81_40.pdf. In particular the Fejer/cosine
ensemble strategy and Gaussian current damping are recognizable machinery.
The present draft supplies its own convention-fixed damping identity,
uniform affine-coset argument, periodic harmonic treatment, conservative
packing estimates, finite-group covariance duality and score-to-OS argument.
It does not rely on a preprint contour factor or silently import a centered
estimate as an all-shift theorem.

Private finite challenges currently cover exact primal/dual covariance on
cube lattices (including composite N), the sign and half-factor in local
damping, positivity of phase integration, all finite Fejer mixture leaves
on a square, arbitrary-graph ancestry samples, periodic Hodge identities,
opposite winding loops and an explicit integer chain homotopy. The general
proof remains the text above. The next gate is a complete adversarial
author reread, with special attention to reflection planes, phase quotient,
packing and limit passage. No independent review has occurred, no retained
status is asserted, and this draft has not yet been submitted as a PR.
