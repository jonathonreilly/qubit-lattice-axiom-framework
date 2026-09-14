---
claim_id: periodic_finite_clock_villain_covariance_and_observable_masslessness_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "For the specified isotropic four-dimensional finite-Z_N Villain measure on equal even periodic tori, an explicit uniform affine integer-curl covariance estimate and exact lattice duality imply clustering but nonsummable bounded plaquette-score correlations when beta and N^2/(4pi^2 beta) are at least 2000. Every local subsequential limit has a gapless observable OS transfer sector. The model, clock order and couplings are supplied. No selected continuous-time Hamiltonian, finite-cylinder gap limit, photon dispersion, native formation law or axiom update is inferred."
upstream_dependencies: []
runner: scripts/periodic_finite_clock_villain_covariance_and_masslessness_2026_09_14.py
---

# Periodic finite-clock Villain covariance and observable masslessness

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

A uniform estimate on shifted integer-curl lattices, applied on both sides
of exact electric–magnetic duality, proves a directional discontinuity in
the field covariance of a specified finite clock model. Its physical
plaquette score is bounded and clusters. Reflection positivity and Euclidean
isotropy then imply a gapless observable transfer sector. The argument keeps
winding currents and harmonic modes, and gives conservative finite sufficient
parameters: beta=2000 and N=16384.

This is a self-contained derivation of a known kind of finite-group massless
phase mechanism. Independent review is pending. It is not a claim to have
invented finite-clock Coulomb phases or derived the microscopic law from the
framework axioms.

## Status, target and imports

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03
target_blocker_text: "Establish an actual-state massless sector in a finite gauge carrier, and identify its relation to the selected Hamiltonian."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Review the uniform phase proof, then derive and control the anisotropic relation to a selected continuous-time law."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Uniform analytic covariance and observable-transfer conclusions for an explicitly supplied model, accompanied by finite mathematical challenges."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The contextual consumer is
`U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`
at main revision `5deabeb698a27c2c3f68c5df685af2521ef15307`. Its section 5
uses a separate oscillator comparison and leaves the many-link Hamiltonian
phase open. The present theorem addresses the actual interacting isotropic
Euclidean clock measure. Identifying its transfer with that consumer's
continuous-time Hamiltonian remains a separate obligation; no theorem or
audit status from the consumer is imported.

| Input | Role | Provenance | Physical identification |
|---|---|---|---|
| Four-dimensional cubic complex and equal even periodic tori | Specified geometry and state sequence | Defined below | Native spacetime selection is not claimed |
| Finite clock alphabet, isotropic Villain weight, beta and N | Complete supplied probability law | Defined below | Native action and coupling selection remain open |
| Poisson summation, Haar characters, Hodge linear algebra and spectral theorem | Mathematical machinery | Explicit hypotheses and applications below | No empirical parameter import |
| Bounded plaquette score and OS reconstruction | Chosen physical-model observable and transfer | Constructed below | Identification with empirical electromagnetism remains open |
| Fejer/cosine ensemble strategy | Proof method | Fröhlich–Spencer primary preprint, cited in section 12 | No external phase theorem is used as a premise |

The proof-obligation graph is acyclic:

| Obligation | Disposition in this source | Consequence |
|---|---|---|
| Full-rank lattice dual and covariance normalization | Section 2, finite character and Poisson derivations | Exact complementary covariance identity |
| Uniform shifted-curl theta bound | Sections 3–7, positive mixture, exact damping and geometry | Covariance lower bound for every affine coset |
| Primal/dual sector mixing with topology | Section 8, total covariance and integral Hodge map | Uniform projector sandwich including finite-volume harmonics |
| Sufficient parameter region | Section 9, explicit elementary inequalities | Separated angular covariance intervals |
| Bounded observable and local-limit passage | Section 10, exact contact identity and bounded Fourier density | Clustering and nonsummability in the same limiting state |
| Observable transfer gap implication | Section 11, site/link positivity, slab identity and isotropy | Gapless sector above the full invariant subspace |

No open lemma is used as a proved intermediate step of this model theorem.
The strongest remaining physical obligation is a controlled identification
with a selected native Hamiltonian and its observable algebra. Neither that
identification nor the theory-of-everything target is renamed as a solved
covariance estimate.

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
valid. The theorem for this supplied model is:

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
Its annihilator is Z^E intersect range Q. For an integer cutoff J, Haar
averaging the Fejer product

  product_e Fejer_J(A_e+a_e+eta_e),  eta in H,

then averaging A as a centered Gaussian of covariance beta V on range Q,
gives the Fejer regularization of (3.1). Each Fourier coefficient is a
product of numbers in [0,1] that tends to one as J->infinity. Dominated
convergence therefore holds through two derivatives, for fixed L and beta.

The subgroup H can equivalently be averaged by vertex gauge angles and
constant real one-forms modulo one. The pushforward of these compact Haar
measures is Haar on H: their real tangent spaces span ker d, and their
image is all of the connected compact group. The possible finite overlap
does not change normalized Haar measure.

## 4. A finite positive mixture of separated currents

For k>=1 set z_k=4k^2. The Fejer polynomial is

  Fejer_J(x)=1+2 sum_(k=1)^J (1-k/(J+1)) cos(2pi kx).

It is a convex combination of 1 and the factors 1+z_k cos(2pi kx), with
respective nonconstant weights 2(1-k/(J+1))/z_k. The leftover constant
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
The parallel count is 5 collinear edges plus 6 transverse unit offsets
with 3 overlapping longitudinal positions. A perpendicular orientation has
20 zero/one transverse-offset cases and 8 remaining axial-distance-one
cases. The periodic neighborhood has no more members, since it is the image
of
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

  1+z_rho cos[rho_tilde(A)+rho(eta)+rho(a)].           (5.2)

The external source phase is the ORIGINAL rho(a). It is not rho_tilde(a).
The damping exponent in this convention is beta/2, not beta. Both changes
give explicit finite counterexamples in the accompanying finite checks.

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
lattice. In the explicit cell convention used here and in the finite runner,
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
For G equal to one plaquette score supported in times [0,1], the cluster
property already proved makes
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

## 12. Literature and contribution boundary

Fröhlich and Spencer's *Massless phases and symmetry restoration in Abelian
gauge theories and spin systems*, CMP 83 (1982), DOI
10.1007/BF01213610, supplies the organizing Fejer/cosine ensemble method.
The primary source read for this derivation is the
[public preprint](https://omeka.ihes.fr/document/P_81_40.pdf), particularly
its current-ensemble construction and masslessness estimates.

The conventions and estimates needed here are derived in the text: the
selected-link damping identity has its factor one-half fixed by direct
Gaussian algebra; the external phase uses the original current; affine
cosets have arbitrary means; and periodic winding currents are integrated
jointly rather than discarded. The explicit finite-group dual covariance,
conservative periodic packing estimate, contact observable and OS gap
implication complete this supplied-model argument. No published-paper error
or novelty priority is asserted.

The parameter constants are intentionally loose. They establish a nonempty
finite region for this theorem and give no critical coupling, exact photon
dispersion, renormalized stiffness, pointwise power law, or quantitative
charge potential. The result does not identify a continuous-time limit or
prove that finite spatial transfer gaps converge. A phase statement for the
selected clock or monopole-penalty Hamiltonian needs its own matched state
and anisotropic analysis.

## 13. Executable evidence and its limits

The standalone runner is
`scripts/periodic_finite_clock_villain_covariance_and_masslessness_2026_09_14.py`.
It declares a 180-second audit timeout and reads no external scientific
input or package integrity file. Its canonical cache is
`logs/runner-cache/periodic_finite_clock_villain_covariance_and_masslessness_2026_09_14.txt`.
The runner computes fifteen finite check families:

- primal residue moments versus dual character filters on cube lattices,
  including composite clock orders, and separate composite annihilator sets;
- selected-link Gaussian integrals with wrong-factor and wrong-phase
  counterexamples, and positivity-sensitive phase curvature;
- shifted Gaussian source identities, including a shifted covariance larger
  than beta, so centered upper bounds are kept separate from coset bounds;
- every leaf of square Fejer mixtures at orders one and two, recovering exact
  rational closed-current coefficients, plus sampled arbitrary-graph ancestry;
- complete sparse Hodge and Laplacian identities on the even side-four torus,
  six harmonic two-forms and a pair of opposite winding loops;
- explicit integer edge-chain contractions and an independently enumerated
  107-edge neighborhood, with exact rational sufficient-parameter arithmetic;
- real-score contact identities from angle convolutions versus integer
  moments, for both circle and finite-clock cube measures;
- a stable evaluation of the bounded score at beta=2000,N=16384 using
  Gaussian images, without dividing underflowed Fourier sums;
- bounded complex slab insertions, a sharp separation-minus-one example,
  and a clock physical transfer compared with a separately enumerated Markov
  path law; and
- angular Fourier projectors, a centered vector in a degenerate invariant
  space, and an anisotropic Gaussian example separating spatial decay from
  a temporal gap.

Floating comparisons use the tolerances declared in the source; the circle
contact check uses a 128-point angle quadrature and truncated Fourier sums.
These numerical comparisons do not supply rigorous quadrature error bounds.
The Fejer coefficients and integer chain identities have separate exact
arithmetic checks. Finite graph samples supplement the general ancestry and geometry proofs;
they do not replace them. The stable high-beta score evaluation is not a
phase simulation. The infinite-volume conclusion rests on sections 2–11.
All author checks were performed personally. Independent review and formal
retention remain pending.

## No-Go Discipline Gate

The scoped negative conclusion is absence of a positive gap above the full
invariant subspace of the specified periodic-limit OS transfer. It is not a
no-go for a microscopic carrier, alternative dynamics or the axioms.

### N1 — Materially distinct attempted evasions

| Honesty | Mathematical object and attempted evasion | Why it does not evade this theorem |
|---|---|---|
| ATTEMPTED | Observable algebra: use the diagonal contact term to remove the field's angular jump | Section 10 derives the exact score/contact identity; an additive constant cannot join the disjoint directional intervals. Circle and finite-clock angle convolutions check the sign and diagonal insertion. |
| ATTEMPTED | Spectral representation: attribute nonsummability entirely to a degenerate ground subspace | Section 11 uses clustering to annihilate the score vector's projection onto the FULL invariant subspace. The finite degenerate-space example preserves the distinction from centering against one ground vector. |
| ATTEMPTED | Spacetime geometry: retain a temporal gap while allowing slowly decaying spatial correlations | Section 11 derives a uniform displacement bound from actual cubic invariance of the limiting law. The supplied anisotropic OU example shows why this hypothesis matters; it is outside the isotropic theorem. |
| ATTEMPTED | Cohomology: concentrate the effect in winding currents or finite torus harmonic modes | Sections 5–6 keep winding factors in the harmonic integral and bound large currents, while section 8 retains the harmonic projector until its local entries vanish. The opposite-winding pair changes the integral when deleted. |
| ATTEMPTED | Statistical sector mixing: shift electric or magnetic cosets so the centered Gaussian estimate fails | Sections 3–7 prove a uniform phase-curvature lower bound for every affine coset. Section 8 applies total covariance; no centered upper bound is imposed on individual cosets. The shifted-source example explicitly has covariance greater than beta. |

These families differ in observable identity, spectral projection, geometric
symmetry, topology or conditional probability. Each authority is the new
self-contained derivation in the indicated section, subject to review. None
is marked ruled out by prior retained authority. Their count is not a proof
of exhaustion; the theorem stands on its quantified analytic argument.

### N2 — Conditions and implication accounting

There is one scoped gap conclusion under the explicit model contract, not a
list of independently closed framework walls. Its technical estimates are
proved in the displayed dependency graph. There are no pairs in an asserted
independent-wall set to tabulate or collapse. Identification with a selected
native law is a separate open target, not counted as multiple independent
conditions or used as a premise of the model theorem.

### N3 — Hidden-condition scan

The load-bearing conditions are explicit: dimension four; even side L>=4;
canonical oriented cells; finite N; the supplied isotropic Villain law;
beta,beta_d>=2000; all affine cosets; periodic rather than relative boundary;
and gauge-invariant local OS observables. Canonical here names an orientation
convention, not a uniqueness or selection claim. Gauge averaging uses
separated endpoint sets; harmonic averaging is joint. Positive integration
is applied after damping, when the factors are positive. The bounded
spectral density, clustering and full invariant projection are proved before
the gap step. No generic-QFT locality of -log T is assumed. The model
probability law is an explicit input; no native primitive
implication is used to select it.

### N4 — Residual matching

| Cited source or witness | Residual actually addressed | Use here and match |
|---|---|---|
| Fröhlich–Spencer preprint, current-ensemble construction | Method for controlling gauge-current activities | Method provenance only; the required all-shift and torus statements are proved here, not imported as a matching retained no-go |
| This source, section 10 and primary runner contact checks | A physical score's diagonal and off-diagonal relation to Fourier moments | Exact matching observable in this theorem |
| This source, section 11 and primary runner spectral examples | Gap implication with full invariant projection and isotropy | Exact matching hypotheses; examples with missing hypotheses are kept outside the theorem |

No prior no-go is used as evidence against a different residual. The
contextual Hamiltonian and spin-ice notes in N8 supply no proof premise.

### N5 — Resolution and rhetoric

The per-element result concerns theta derivatives and positive factors; the
per-site result concerns finite incidence and gauge conditions; the per-mode
result concerns Fourier projectors and transfer spectral identities; the
per-block result concerns specified finite cube, square and torus systems.
The lattice-wide masslessness statement is an analytic theorem under the
model hypotheses. The executable does not perform the thermodynamic limit.
The five resolution lines in its canonical cache state these limits
explicitly. No finite example is promoted into an axiom obstruction.

### N6 — Partial closure and primitive boundary

The law and its isotropy are supplied in the definition. This note neither
requests a new axiom nor asserts that no existing primitive can support a
future identification. A controlled anisotropic limit, a direct Hamiltonian
bound, or a different allowed carrier remains a legitimate route to the
physical target. The framework's structural kinetic normalization is not
silently expanded into selection of this full probability law. No premise
registry, approved primitive or axiom text is changed.

### N7 — Steelman

A hostile reviewer should demand that the actual finite-clock Hamiltonian,
with its chosen time scale and possible monopole penalties, inherit these
correlations. Fixed-N clock transfer kernels can have a singular anisotropic
limit, and a proof whose constants require both couplings large need not
survive it. The concrete terminal obligation is a uniform covariance or
spectral estimate on that identified time-limit family. This objection is
valid against an extrapolated Hamiltonian claim, which is not made here.
Inside the stated periodic isotropic model, the serious evasion would be a
failure of the uniform affine-coset curvature estimate; sections 3–7 give
its explicit positive representation and geometry rather than assuming the
desired masslessness. Its independent review remains required.

### N8 — Cross-cycle comparison

The current-main source
`U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`,
sections 5–6, separates a supplied oscillator from the interacting many-link
phase. That residual remains open in that source; the present actual-state
Euclidean result is a distinct contribution with a still-unmatched time
limit. The current-main source
`SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`,
sections 5–7, separates a variational magnetic expectation from a phase or
lower stiffness estimate. The present theorem uses covariance and OS
reconstruction rather than that trial expectation. Neither source is used
as an impossibility witness, and neither open physical obligation is
retroactively declared retired. These source-scope comparisons are at main
revision `5deabeb698a27c2c3f68c5df685af2521ef15307`; no audit verdict is
inferred from their prose.

The gate records five substantive attempted evasions and the proof's exact
scope. It supplies no route-exhaustion, axiom-update or independent-review
certificate.

## Author review record

The frozen primary runner was challenged with eighteen targeted changes:
dual covariance sign; composite annihilator translation; doubled Gaussian
damping; phase second-derivative sign; affine source-curvature sign; cosine
mixture weight; retained amplitude ancestry; Hodge cell translation; periodic
coloring alias; chain
homotopy orientation; neighborhood cutoff; sufficient clock order; circle
and clock score signs; slab separation exponent; clock transfer link count;
directional projector component; and deletion of winding pairs. Each raised
an assertion failure in its designated check. The final source was not
modified by those in-memory fault injections.

The first clock-sign injection matched both the angle and integer variable
names and changed both comparison sides; it was therefore an invalid
single-path challenge. The driver was narrowed to the angle computation
only, and that fault was detected. This correction is recorded rather than
counting the overbroad first injection as evidence.

The full source and finite checks were reviewed personally. This is author
review, not an independent audit. Source topology and the canonical cache
are prepared on the stated current-main base. Integrated pipeline, strict
lint and exact combined-tree evidence gates remain required before landing.

## Falsifiers and verification

The model theorem fails if its all-shift positive representation or uniform
curvature estimate fails for an admitted even torus; if the scaled dual
lattice or covariance identity is incorrect; if topology invalidates the
small/large-current bounds; if the score contact identity fails; or if the
same limiting state lacks either reflection positivity or the stated
isotropy. The supplied finite counterexamples identify particularly easy
ways to make these errors. Passing their checks does not replace review of
the universal proof.

Run the primary executable through `scripts/runner_cache.py` with its declared
180-second timeout. The expected finite-family count is fifteen, with no
failed assertions. Formal retained status belongs to the independent audit
path, and the integrated-current-main validation gates remain landing work.
