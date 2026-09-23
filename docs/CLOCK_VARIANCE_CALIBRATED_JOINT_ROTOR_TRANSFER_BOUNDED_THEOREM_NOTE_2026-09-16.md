---
claim_id: clock_variance_calibrated_joint_rotor_transfer_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/clock_variance_calibrated_transfer_check_2026_09_16.py
upstream_dependencies: []
claim_scope: "Supplied fixed finite graph and coupling; every joint delta to zero and N to infinity path."
---

# A variance-calibrated clock transfer and its joint rotor limit

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

This is a conditional mathematical result for fixed supplied g>0, external time, a finite spatial graph and finite-dimensional gauge-compatible matter. No spatial-volume or varying-coupling uniformity is asserted.

Contextual prior art: `COMPACT_DETERMINANT_CURRENTS_SIGNED_SECTORS_AND_FINITE_CYCLIC_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-14.md`, Part III (context only); the complete argument used here is given below.

## 1. Exact clock kernel and a crossover that must be priced

For c>0 define p_c(k)=exp(-c k²)/Z(c), k in Z, and v(c)=E_c k². On an N-state clock, N>=3, let X translate the angle by2pi/N and put

    Q_(c,N)=sum_k p_c(k) X^k.

The character r has eigenvalue

    lambda_r(c,N)=E_c cos(2pi r k/N)
      = [sum_m exp(-pi²(m+r/N)²/c)]
        /[sum_m exp(-pi²m²/c)].                       (1)

Poisson summation proves the second formula. It is strictly positive; the first proves it is at most1. Q is consequently a positive self-adjoint contraction. It is precisely the normalized sampled Villain temporal kernel with beta_tau=N²c/(2pi²).

For the naive rotor time scaling beta_tau=1/(g²delta), write J=delta g²N²/2, so c=pi²/J. For fixed r and fixed J in(0,infinity), delta=2J/(g²N²) and N->infinity give

    -delta^-1 log lambda_r -> (g²/2)r² D(J),
    D(J)=(2pi²/J)v(pi²/J)=1-2J v(J).                 (2)

The second identity follows by logarithmically differentiating
Z(J)=sqrt(pi/J)Z(pi²/J). For every finite J, 0<D(J)<1: positivity follows from the first expression and the strict upper bound from the second. Moreover D(J)->0 as J->0 and D(J)->1 as J->infinity. At small J the first expression is asymptotic to(4pi²/J)exp(-pi²/J); at large J the second is1-4J exp(-J)+smaller terms. A joint limit at finite J therefore changes the low-mode kinetic coefficient. These conclusions concern this actual sampled kernel, not every clock discretization.

The expansion used for(2) has an O(N^-2) energy remainder at fixed J, since all integer-Gaussian moments are finite. Uniformity over J approaching an endpoint needs an additional argument; the result below supplies a different calibration that avoids that requirement.

## 2. Existence of an exact variance calibration

v'(c)=-Var_c(k²)<0. Termwise differentiation is justified on every compact c interval. Also v(c)->0 as c->infinity, and v(c)->infinity as c->0, the latter by the Poisson identity and exponentially small dual moments. Thus for every delta,g>0 and integer N>=3 there is exactly one c=c(delta,N,g)>0 such that

    v(c)=delta g² N²/(4pi²).                         (3)

This is a mathematical matching of a supplied target kinetic coefficient. It is not a fit to observations and does not derive g from the framework. At small target variance, exp(-c) is asymptotic to v/2 and recovers the known logarithmic clock scaling. At large target variance, c is asymptotic to1/(2v) and beta_tau is asymptotic to1/(g²delta).

## 3. Uniform fourth-moment bound

We need a bound valid even in the crossover. Let mu4(c)=E_c k4. The following deliberately loose constant suffices:

    mu4(c)<=224[v(c)+v(c)²], all c>0.                (4)

For c>=1, divide the positive sums for mu4 and v and retain k=1 in the denominator. Since k²-1>=3(k-1),

    mu4/v <=sum_(k>=1) k4 exp[-(k²-1)]
      <=sum_(k>=1)k4 r^(k-1)<3, r=exp(-3)<1/16.

The last series equals(1+11r+11r²+r³)/(1-r)^5, and its value at1/16 is less than3.

For0<c<=1, put d=pi²/c>9. The dual variance obeys
v(d)<=2 sum_(k>=1) k² exp(-d k²)<=3 exp(-d).
Here use k²-1>=3(k-1) and the geometric second-moment sum; exp(-3d)<1/16. The differentiated Poisson identity gives

    v(c)=[1-2d v(d)]/(2c)>=1/(4c),

because6d exp(-d)<=54 exp(-9)<1/2. Also Z(c)>=sqrt(pi/c) by Poisson summation. On each interval[k-1,k],
k4 exp(-c k²)<=(x+1)^4 exp(-c x²). Using(x+1)^4<=8(x4+1) and the two Gaussian integrals gives

    2 sum_(k>=1)k4 exp(-c k²)
      <=6sqrt(pi)c^(-5/2)+8sqrt(pi)c^(-1/2).

After division by Z(c), mu4<=6c^-2+8<=14c^-2<=224v(c)². Combining the two ranges proves(4). No finite sampling supplies this bound.

## 4. Quantitative one-link energy matching

Let h=2pi r/N, and use calibration(3). For the centered representative |r|<=N/2 put z=h²v/2=delta g²r²/2. The elementary cosine remainder implies

    0<=lambda_r-1+z<=h4 mu4/24.

If z<=1/2, set u=1-lambda_r in[0,z]. Since
0<=-log(1-u)-u<=u²/[2(1-u)]<=u²,

    |-delta^-1 log lambda_r-(g²/2)r²|
      <= h4 mu4/(24delta)+z²/delta
      <=400 r4 [g²/N²+delta g4].                    (5)

The last constant follows from(4), pi²<10, and direct substitution of(3): the two coefficients before enlargement are224pi²/6 and224/24+1/4. The r=0 eigenvalue is exactly1 and both sides vanish. At fixed finite r, (5) tends to zero along EVERY sequence delta->0,N->infinity, with g fixed. No condition on delta N² is imposed. This does not approximate all high clock modes uniformly.

A direct one-step bound avoids the logarithm and is useful for products:

    |lambda_r-1+delta g²r²/2|
      <=(224pi²/6)delta g²r4/N²
         +(224/24)delta²g4r4.                       (6)

It needs no small-z restriction; the right side may simply become uninformative for high modes.

## 5. Actual spatial weights and a fixed finite complex

Fix a finite spatial cell complex, with E oriented links and P oriented plaquettes, integer incidence and curl satisfying divergence times curl-adjoint=0. Free cubes and periodic cubic tori are included; no limit of their size is taken in this theorem. The continuum-angle Hilbert space is

    H_space=L2((R/2piZ)^E,normalized Haar) tensor H_matter,

where H_matter is finite dimensional. In the Fourier basis, each E_l has integer eigenvalues. Supply a Hermitian matrix-valued finite Laurent polynomial h(theta) satisfying the gauge-covariance rule for fixed integer onsite charges. The usual finite-volume charged Peierls hopping plus an onsite operator preserving local charges is included. A scalar shift, depending on this fixed graph, makes h(theta)>=0 for every theta. That shift is remembered in the limiting Hamiltonian.

Put

    K=(g²/2)sum_l E_l²,
    V(theta)=g^-2 sum_p[1-cos((C theta)_p)],
    H=K+V+h.                                         (7)

H is positive self-adjoint on D(K): V+h is a bounded Hermitian multiplier. Finite Fourier polynomials with matter-vector coefficients form a core. Indeed they are a core for K, and the K and H graph norms are equivalent under a bounded perturbation. No small-g assumption is made; g>0 is fixed.

For0<delta<g²/4, set y=delta/(2g²)<1/8. Define the positive normalized spatial factor

    b_y(phi)=[sum_(k in Z)y^(k²)exp(i k phi)]
                   /[sum_(k in Z)y^(k²)],
    B_delta(theta)=product_p b_y((C theta)_p).         (8)

Poisson summation proves positivity; pairing the Fourier terms and cos<=1 proves b_y<=1. The tail2 sum_(k>=2)y^(k²)<=2y4/(1-y5), together with the denominator1+2y+tail, proves uniformly in phi

    b_y(phi)=1-2y(1-cos phi)+O(y²).

The constant is absolute on y<=1/8. Since b_y is bounded away from zero on that interval, its square root has the same uniform Taylor control. On the fixed finite complex,

    M_delta(theta)=exp[-delta h(theta)/2] B_delta(theta)^(1/2)
      =I-delta[V(theta)+h(theta)]/2+O_graph,g,h(delta²) (9)

in multiplier norm. The scalar B commutes with h, so M is positive and contractive. Its finite-clock version is the exact sampling at N angles per link.

Let Q_delta,N be the E-fold tensor product of the calibrated one-link kernel of sections1-4, acting trivially on matter, and form the ACTUAL transfer

    T_delta,N=M_delta,N Q_delta,N M_delta,N.           (10)

It is a strictly positive self-adjoint contraction in the finite clock space. No logarithm of a truncated quadratic magnetic potential replaces(10).

## 6. Joint consistency on one common Hilbert space

Let I_N={-floor(N/2),...,ceil(N/2)-1}. Embed the normalized finite-clock Fourier basis indexed by I_N^E into the corresponding integer Fourier vectors by J_N. This is an isometry. Finite Fourier polynomials eventually lie in its image; J_N J_N*->I strongly. Extend the finite transfer by zero:

    Ttilde_delta,N=J_N T_delta,N J_N*.

For a fixed finite Fourier polynomial f, equation(6) and the product of the finitely many link eigenvalues give

    ||Qtilde_delta,N f-f+delta Kf||
       <=C_f[delta²+delta/N²].                       (11)

The estimate is uniform over all sufficiently large N and small delta, with no restriction on delta N². Expanding a finite product produces O(delta²) cross terms because every frequency in f is fixed. The per-link O(delta/N²) error remains separately priced. The exact zeroth-order map is the identity on this core once N contains its frequency support.

Sampling multiplication by any fixed Laurent polynomial is exact on f once N contains the support of that polynomial times f: no Fourier mode wraps. Therefore(9) becomes in the common Hilbert space

    Mtilde_delta,N f=f-delta(V+h)f/2+O_f(delta²).      (12)

The same holds with f replaced by Kf and by(V+h)f, both finite Fourier polynomials. Q and M are contractions, so the norm remainders in(12) remain bounded after the other factor acts. Inserting(11)-(12) into(10), and using Q(V+h)f=(V+h)f+O_f(delta), yields

    ||Ttilde_delta,N f-f+delta Hf||
       <=C_f[delta²+delta/N²].                       (13)

No uniform estimate on every high-energy unit vector is asserted. The constants depend on the finite graph, fixed coupling, matter multiplier and test polynomial. The proof neither differentiates an unbounded high-mode commutator nor assumes that a finite energy subspace is preserved by the magnetic interaction.

## 7. From core consistency to the actual transfer product

Consider an arbitrary sequence delta_j->0 and integers N_j->infinity. Write

    A_j=(I-Ttilde_(delta_j,N_j))/delta_j.

A_j is a positive bounded self-adjoint operator on the common Hilbert space, with value delta_j^-1 on the orthogonal complement of the clock image. Equation(13) gives A_j f->Hf on the core. For any such f,

    ||(A_j+1)^-1(H+1)f-f||
      =||(A_j+1)^-1(H-A_j)f||<=||(H-A_j)f||->0.      (14)

The image(H+1)core is dense because the core is graph-dense and H+1 has a bounded everywhere-defined inverse. The resolvents are contractions, so(14) extends by density to strong convergence of(A_j+1)^-1 to(H+1)^-1.

For fixed t>0, set z=(1+x)^-1. The function exp(-t x), extended by zero at x=infinity, is a continuous function of z on[0,1], vanishing at z=0. Uniform polynomial approximation with zero constant term and the strong resolvent convergence prove

    exp(-t A_j)->exp(-t H) strongly.                 (15)

Let n_j=floor(t/delta_j), eventually at least1. Replacing t by n_j delta_j on the left of(15) changes its operator norm by at most

    |t-n_j delta_j|/[e min(t,n_j delta_j)],

from the maximum of x exp(-s x). This tends to zero. Finally, for every integer n>=1, scalar calculus on0<=lambda<=1 gives

    |lambda^n-exp[-n(1-lambda)]|<=2/n.               (16)

To verify it, put u=1-lambda. For u<=1/2, the difference is bounded by n u² exp(-n u)<=4/(e²n). For u>1/2 it is at most exp(-n/2)<=2/n. Endpoints are included. The spectral theorem applies(16) to Ttilde_j. Hence

    J_(N_j) T_(delta_j,N_j)^(floor(t/delta_j)) J_(N_j)*
       ->exp(-tH) strongly, every t>0,              (17)

along every joint path. At t=0 interpret the embedded finite identity as J_N J_N*, which converges strongly to I. This is a product limit of the exact compact transfer, not merely a statement about its separate factors. No total operator-norm rate or spatial-volume-uniform convergence follows from the core constants.

## 8. Exact Gauss restriction

Let D be the tail-minus-head spatial incidence. In a matter charge basis b, the U(1) physical projector P selects integer Fourier labels n with

    Dn=Q(b).

The finite-clock projector P_N selects the same equation modulo N. The chosen h is gauge compatible, so(7) preserves P and(10) preserves P_N. For any fixed integer n and finite matter charge Q(b), Dn-Q(b) has finitely many fixed integer components. Once N exceeds their absolute values, congruence to zero is equivalent to equality. Therefore

    J_N P_N J_N*->P strongly.                       (18)

For f in the physical finite-Fourier core, P_N f=f for every sufficiently large N. The consistency proof and product limit restrict to that core; contraction and density extend them to the full physical space. Equivalently the embedded products with P_N converge strongly to exp(-tH)P. This retains any nonempty allowed physical charge sector. Extra modular states at finite N are not silently equated to integer-Gauss states before the limit.

## 9. Scientific scope and checks

The calibration removes a regulator-order ambiguity for the supplied finite-volume coupled Hamiltonian. It does not show that the microscopic interaction weakens because spatial volume grows. Fixed-time-step finite-clock phases, the infinite-volume ground state, a uniform anisotropic defect expansion, photon poles, infrared charge flow and native law/time selection remain separate obligations. In particular this theorem takes N to infinity and cannot establish a fixed finite-payload phase.

The numerical check compares positive Poisson eigenvalues with direct integer-jump Fourier sums, and a full N^4 angle-space Gauss calculation with the reduced physical ring transfer. It compares actual repeated transfers with a separately constructed rotor Hamiltonian on three joint paths. On the inverse-square and inverse-cube paths, uncalibrated sampling approaches a different evolution while the calibrated errors decrease. These are finite diagnostics; equations(4),(13)-(18) supply the proposed general proof.

Personal review of the first successful run exposed a relative-accuracy defect: a tiny crossover gap was lost when taking log of a number near1, despite the absolute tolerance passing. The original source and output are preserved. The corrected implementation uses the exact positive sine-squared deficit and log1p, with a relative assertion. Numerical cutoffs remain floating comparisons, not rigorous tail intervals. These statements describe the original author campaign; they are historical provenance, not current independent-review or cache claims.

## Historical working derivations

The following complete working texts preserve the original exploratory arguments. Their provisional language and prior-art claims are historical; the current theorem and its hypotheses are in sections 1–8 above.

### Historical BLOCK01_WORKING_TRANSFER_MATCHING.md

#### Working transfer matching: Fourier coefficients before phase transport

Exploration, no theorem or phase claim yet. Let delta>0, g>0. For a rotor with T=(g²/2)sum E² and V=g^(-2)sum[1-cos curl theta], the symmetric transfer is exp(-delta V/2) exp(-delta T) exp(-delta V/2). The exact temporal kernel with normalized Haar measure is phi_(1/(g²delta))(theta'-theta), where phi_beta(theta)=sum_n exp[-n²/(2beta)] exp(i n theta).

A normalized spatial Villain factor is W_beta(theta)=phi_beta(theta)/phi_beta(0). Put q=exp[-1/(2beta)]. At q small, W=1+2q(cos theta-1)+O(q²). The induced potential -delta^-1 log W therefore has leading coefficient2q/delta. Supplying beta_s=delta/g² makes this coefficient exponentially small in1/delta rather than1/g². To match the cosine coefficient, q_s must instead satisfy q_s/delta ->1/(2g²), e.g. beta_s=[2log(2g²/delta)]^-1. Prove uniform-in-angle remainder and track its volume dependence; do not silently linearize one winding image.

Finite-clock complication: sampling the temporal heat kernel on N angles and normalizing its row sum gives character eigenvalue

    lambda_r(delta,N) = sum_m exp[-a(r+mN)²] / sum_m exp[-a(mN)²],
    a=delta g²/2.

At fixed N and delta->0, this tends to1 with exponentially small generator, by the angle-space Poisson form. It is not automatically exp[-delta g² principal(r)²/2]. Under N->infinity and J=aN² fixed, expansion suggests an effective low-mode coefficient

    (g²/2) r² D(J),
    D(J)=1-2J E_J[m²]
        =(2pi²/J) E_(pi²/J)[k²],

with the expectations over normalized integer Gaussians. The limits should be D(0)=0 and D(infinity)=1. Derive all limits, signs, remainder control and physical-sector witness independently. A logarithmic temporal beta scaling at fixed N can instead approach a nearest-neighbor clock kinetic operator; current main's qutrit transfer is related prior art, not a new general principle.

The unresolved phase step is still a uniform anisotropic compact-defect estimate in the matched law. These matching observations alone do not supply it.

#### Prior-art correction and new target

Current main COMPACT_DETERMINANT_CURRENTS_SIGNED_SECTORS_AND_FINITE_CYCLIC_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-14.md PartIII already proves both logarithmic temporal and inverse-logarithmic spatial matching, including the frozen fixed-N rotor-scaling counterexample and the finite-box generator. These are prior results, not new accomplishments of this campaign. The new target is the joint clock/time crossover and a variance-calibrated transfer valid along every delta->0,N->infinity path.

Write the exact normalized clock kernel as Q_x=E_x X^K with integer-Gaussian probability proportional to x^(K²). Let sigma²(x)=E_x K². It is continuous strictly increasing from0 toinfinity. Choose x=x(delta,N) by

    sigma²(x)=delta g² N²/(4pi²).

The low Fourier character has angle h=2pi r/N. If the fourth moment obeys mu4<=C(sigma²+sigma4), the cosine remainder and logarithm yield

    | -delta^-1 log lambda_r - (g²/2)r² |
       <= C r4 [g²/N²+delta g4]

for delta g²r² sufficiently small. This would remove the order restriction for fixed low modes. It is a matching choice for a supplied coupling, not a physical value derived from axioms.

A full fixed-volume proof may use the actual positive symmetric transfer, an O(delta²+delta/N²) consistency estimate on finite Fourier polynomials, and the common-Hilbert positive operator A_delta,N=(I-T_delta,N)/delta. Core convergence gives strong resolvent convergence by a direct resolvent identity; scalar comparison between T^n and exp[-n(I-T)] gives the product limit. This could include bounded gauge-compatible matter and exact mod-N Gauss projection. All details remain to be established, including uniform integer-Gaussian moment constants and source conventions.

### Historical BLOCK02_VARIANCE_CALIBRATED_TEMPORAL_TRANSFER_WORKING.md

#### A variance-calibrated clock transfer and its joint rotor limit

Author derivation in progress, 2026-09-16. The exact Fourier matching is for a supplied coupling and external time step. It selects no native dynamics and proves no phase. The basic fixed-N logarithmic matching and spatial inverse-logarithmic matching already appear in current main's COMPACT_DETERMINANT_CURRENTS_SIGNED_SECTORS_AND_FINITE_CYCLIC_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-14.md PartIII. The new target here is uniform matching along arbitrary joint clock/time paths.

#### 1. Exact clock kernel and a crossover that must be priced

For c>0 define p_c(k)=exp(-c k²)/Z(c), k in Z, and v(c)=E_c k². On an N-state clock, N>=3, let X translate the angle by2pi/N and put

    Q_(c,N)=sum_k p_c(k) X^k.

The character r has eigenvalue

    lambda_r(c,N)=E_c cos(2pi r k/N)
      = [sum_m exp(-pi²(m+r/N)²/c)]
        /[sum_m exp(-pi²m²/c)].                       (1)

Poisson summation proves the second formula. It is strictly positive; the first proves it is at most1. Q is consequently a positive self-adjoint contraction. It is precisely the normalized sampled Villain temporal kernel with beta_tau=N²c/(2pi²).

For the naive rotor time scaling beta_tau=1/(g²delta), write J=delta g²N²/2, so c=pi²/J. For fixed r and fixed J in(0,infinity), delta=2J/(g²N²) and N->infinity give

    -delta^-1 log lambda_r -> (g²/2)r² D(J),
    D(J)=(2pi²/J)v(pi²/J)=1-2J v(J).                 (2)

The second identity follows by logarithmically differentiating
Z(J)=sqrt(pi/J)Z(pi²/J). For every finite J, 0<D(J)<1: positivity follows from the first expression and the strict upper bound from the second. Moreover D(J)->0 as J->0 and D(J)->1 as J->infinity. At small J the first expression is asymptotic to(4pi²/J)exp(-pi²/J); at large J the second is1-4J exp(-J)+smaller terms. A joint limit at finite J therefore changes the low-mode kinetic coefficient. These conclusions concern this actual sampled kernel, not every clock discretization.

The expansion used for(2) has an O(N^-2) energy remainder at fixed J, since all integer-Gaussian moments are finite. Uniformity over J approaching an endpoint needs an additional argument; the result below supplies a different calibration that avoids that requirement.

#### 2. Existence of an exact variance calibration

v'(c)=-Var_c(k²)<0. Termwise differentiation is justified on every compact c interval. Also v(c)->0 as c->infinity, and v(c)->infinity as c->0, the latter by the Poisson identity and exponentially small dual moments. Thus for every delta,g>0 and integer N>=3 there is exactly one c=c(delta,N,g)>0 such that

    v(c)=delta g² N²/(4pi²).                         (3)

This is a mathematical matching of a supplied target kinetic coefficient. It is not a fit to observations and does not derive g from the framework. At small target variance, exp(-c) is asymptotic to v/2 and recovers the known logarithmic clock scaling. At large target variance, c is asymptotic to1/(2v) and beta_tau is asymptotic to1/(g²delta).

#### 3. Uniform fourth-moment bound

We need a bound valid even in the crossover. Let mu4(c)=E_c k4. The following deliberately loose constant suffices:

    mu4(c)<=224[v(c)+v(c)²], all c>0.                (4)

For c>=1, divide the positive sums for mu4 and v and retain k=1 in the denominator. Since k²-1>=3(k-1),

    mu4/v <=sum_(k>=1) k4 exp[-(k²-1)]
      <=sum_(k>=1)k4 r^(k-1)<3, r=exp(-3)<1/16.

The last series equals(1+11r+11r²+r³)/(1-r)^5, and its value at1/16 is less than3.

For0<c<=1, put d=pi²/c>9. The dual variance obeys
v(d)<=2 sum_(k>=1) k² exp(-d k²)<=3 exp(-d).
Here use k²-1>=3(k-1) and the geometric second-moment sum; exp(-3d)<1/16. The differentiated Poisson identity gives

    v(c)=[1-2d v(d)]/(2c)>=1/(4c),

because6d exp(-d)<=54 exp(-9)<1/2. Also Z(c)>=sqrt(pi/c) by Poisson summation. On each interval[k-1,k],
k4 exp(-c k²)<=(x+1)^4 exp(-c x²). Using(x+1)^4<=8(x4+1) and the two Gaussian integrals gives

    2 sum_(k>=1)k4 exp(-c k²)
      <=6sqrt(pi)c^(-5/2)+8sqrt(pi)c^(-1/2).

After division by Z(c), mu4<=6c^-2+8<=14c^-2<=224v(c)². Combining the two ranges proves(4). No finite sampling supplies this bound.

#### 4. Quantitative one-link energy matching

Let h=2pi r/N, and use calibration(3). For the centered representative |r|<=N/2 put z=h²v/2=delta g²r²/2. The elementary cosine remainder implies

    0<=lambda_r-1+z<=h4 mu4/24.

If z<=1/2, set u=1-lambda_r in[0,z]. Since
0<=-log(1-u)-u<=u²/[2(1-u)]<=u²,

    |-delta^-1 log lambda_r-(g²/2)r²|
      <= h4 mu4/(24delta)+z²/delta
      <=400 r4 [g²/N²+delta g4].                    (5)

The last constant follows from(4), pi²<10, and direct substitution of(3): the two coefficients before enlargement are224pi²/6 and224/24+1/4. The r=0 eigenvalue is exactly1 and both sides vanish. At fixed finite r, (5) tends to zero along EVERY sequence delta->0,N->infinity, with g fixed. No condition on delta N² is imposed. This does not approximate all high clock modes uniformly.

A direct one-step bound avoids the logarithm and is useful for products:

    |lambda_r-1+delta g²r²/2|
      <=(224pi²/6)delta g²r4/N²
         +(224/24)delta²g4r4.                       (6)

It needs no small-z restriction; the right side may simply become uninformative for high modes.

#### 5. Full finite-volume transfer: proof plan to complete

For a fixed finite spatial graph use one calibrated Q per link. Let y=delta/(2g²), and use the existing normalized spatial Villain B_y(curl theta). Its uniform expansion is1-delta g^-2(1-cos)+O(delta²). The actual positive symmetric transfer is B_delta^(1/2) Q_delta^(tensor E) B_delta^(1/2), not its quadratic approximation. It commutes with the finite-clock gauge projection.

Embed the centered clock Fourier basis into l2(Z^E). Finite trigonometric polynomials are eventually contained in this image. Their one-step consistency should be

    ||(T_delta,N-I+delta H)f||
       <=C_f[delta²+delta/N²],
    H=(g²/2)sum E²+g^-2 sum[1-cos curl theta].

The spatial expansion has an operator-norm remainder on each finite graph. Multiplication of a finite Fourier polynomial by the leading cosine potential is another such polynomial; this prevents an unpriced high-mode commutator in the consistency proof. A bounded gauge-compatible matter multiplier can be included by an additional symmetric sandwich after a finite-volume scalar shift.

Extend the finite transfer by zero on the orthogonal complement of the embedded clock space. Then A_delta,N=(I-T_delta,N)/delta is positive and bounded. If A_delta,N f->Hf on the finite-Fourier core, the identity

    ||(A_delta,N+1)^-1(H+1)f-f||<=||(H-A_delta,N)f||

and density of(H+1)core give strong resolvent convergence. Uniform polynomial approximation in(1+x)^-1 yields strong heat-semigroup convergence. The scalar difference between lambda^n and exp[-n(1-lambda)] on[0,1] tends uniformly to zero, so the actual transfer products converge as well. Verify the bound, time rounding and the mod-N physical projector passage before promoting this plan to a theorem.

No thermodynamic phase, actual ground-state convergence uniform in volume, fixed finite-N rotor law, real-time physical clock selection, or native axiom result follows from this finite-volume bridge.

## Evidence and boundary obligations

- N1: Naive sampled scaling, variance calibration and noncommuting-factor tests address the stated supplied model. They are not five independent attacks on a physical impossibility claim; negative certification is withheld.
- N2: Native law/time selection, spatial thermodynamic control, fixed payload, volume-uniform defects and interacting gapless matter remain OPEN. Distinct obligations are not a proof of independent exclusion routes.
- N3: Coupling, time, finite graph, finite-dimensional matter and gauge-compatible Laurent multiplier are supplied. Scalar shifts are tracked; nonempty physical sectors are required for normalized states.
- N4: Core residuals are C_f(delta²+delta/N²); compactness sends the sequence limit before the Fourier cutoff. The heat majorant depends on graph size and coupling.
- N5: The program executes finite ring configurations and finite Fourier modes. Whole-lattice checks here mean only the explicitly enumerated finite ring. Infinite-mode identities and every-joint-path limits are written proofs, not executed lattice simulations. Cutoff comparisons are floating diagnostics, not interval bounds.
- N6: Uniform anisotropic estimates, direct Hamiltonian arguments and alternative finite-clock constructions remain open research routes.
- N7: The principal finite-graph objection is modular high-mode spectral escape; the explicit theta floor and compactness argument address it only under the stated assumptions.
- N8: Prior fixed-clock and spatial matching are contextual prior art; no earlier result is promoted to a thermodynamic phase. No native clock, coupling, physical phase or axiom update follows.

[Canonical program](../scripts/clock_variance_calibrated_transfer_check_2026_09_16.py) · [Current cache](../logs/runner-cache/clock_variance_calibrated_transfer_check_2026_09_16.txt) · [Exact original recovery](work_history/review_loop/pr8162/README.md).
