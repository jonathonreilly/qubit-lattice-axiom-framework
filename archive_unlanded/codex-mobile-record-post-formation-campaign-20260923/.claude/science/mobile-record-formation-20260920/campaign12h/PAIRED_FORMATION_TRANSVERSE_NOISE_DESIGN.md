# Opposite-pair formation as a controlled alternative noise design

2026-09-21. Primary construction and exact finite-generator algebra; no
independent check or interacting fluctuation theorem yet. This is an
additional supplied formation rule, not the original multiplicative
single-site odds and not an axiom-derived modification. It illustrates
which fluctuation properties depend on the formation mechanism.

## 1. A vacancy-consuming two-record event

Use the fifteen-state transverse alphabet. Each occupied label a has an
opposite label bar(a), with e_bar=-e_a and b_bar=-b_a. For each unoriented
nearest-neighbor edge {x,y}, choose a fixed endpoint order. If both sites
are vacant, create the ordered pair (a,bar(a)) at microscopic rate
beta/(6N), separately for each of the fourteen possible a. Reversing the
endpoint order just replaces a by bar(a), so the rule is well defined
without a preferred edge orientation. All existing records remain unchanged.
Two vacancies are consumed in one event; there is no deletion or overwrite.

Every birth has exactly zero total e-vector and zero total b-vector. The
exchange rule also conserves those totals. Consequently the zero-mode
vectors are exact microscopic constants, including during formation.
An empty initial state keeps both total vectors identically zero.

Under a homogeneous product p with vacancy v, each site has six incident
edges and its product reaction is

    B_a(p)=beta v^2,  a=1,...,14,
    B_rho=14 beta v^2,   B_X=B_Y=0.                       (1)

The candidate homogeneous local-equilibrium trajectory is

    v(t)=v0/(1+14 beta v0 t),
    p_a(t)=p_a(0)+[v0-v(t)]/14.                          (2)

This is a product reaction coefficient, not an exact finite-volume law.
In fact the exact process immediately creates pair correlations below.
The algebraic vacancy decay differs from independent single-site births.

## 2. The reaction adjoint has the correct Euler projection

For a reference product p, the contribution of an edge ordered x,y to the
adjoint potential is

    (beta/6) sum_a [
       1_(eta_x=a,eta_y=bar(a)) v_x v_y/(p_(a,x) p_(bar(a),y))
       -1_(eta_x=0,eta_y=0)].                            (3)

At a homogeneous reference and product test q, its mean is

    V_edge(q;p)=(beta/6) sum_a
           [v^2 q_a q_bar(a)/(p_a p_bar(a))-q0^2].        (4)

There are three unoriented edges per site. Thus Vbar=3 V_edge is zero at
q=p and its first derivative there is

    D_q Vbar(p;p).delta q
      = beta v^2 sum_a delta q_a/p_a
                       +14 beta v sum_a delta q_a
      = [H(p)B(p)].delta q,                             (5)

where H is the fourteen-species categorical entropy Hessian. The first
term counts each a both as itself and as an opposite endpoint. The second
comes from the derivative of -q0^2, including all fourteen alternatives.

On a fixed interior reference compact set, the remaining Taylor term is
bounded by C|q-p|^2. The reaction adjoint is a bounded two-site observable;
the positive-floor exchange gives the same count-sector one-block bound
as before. Absolute entropy production acquires only a bounded O(N^3)
reaction term. Consequently the native-formation Euler proof's steps extend
to this two-site reaction, conditional on a C2 interior solution of
p_t+div J=B and initial H=o(N^3). This is a primary proof application,
not yet separately checked. It uses neither exact product evolution nor
a fluctuation theorem.

## 3. The birth covariance exposes the changed statistics

Let P be the permutation matrix a->bar(a) on the fourteen occupied species.
At product local equilibrium, the leading birth covariance per volume at
macroscopic time is

    Q_species=beta v^2 (I+P).                            (6)

Indeed three edges per site and fourteen alternatives with rate beta/6
give (beta v^2/2) sum_a (unit_a+unit_bar(a))
(unit_a+unit_bar(a))^T=beta v^2(I+P).
The total-density noise is twice its creation rate:
1^T Q_species 1=28 beta v^2=2 B_rho. Meanwhile

    Q_X=Q_Y=Q_XY=0                                      (7)

at leading zero-wavelength order, because E P=-E and B P=-B for the
label-observable matrices E,B. Births add records but no net vector.
This positive-semidefinite matrix is singular, as exact conservation requires.

For a fixed Fourier wave vector K on the continuum torus, write the lattice
phase exp(-i K.x/N). The vector increment of one pair birth is proportional
to e_a[exp(-i K.x/N)-exp(-i K.y/N)] (and similarly b_a).
Under a homogeneous product the exact Fourier birth brackets are

    Q_X^N(K)=(beta v^2/3) sum_i |1-exp(-i K_i/N)|^2 I,
    Q_Y^N(K)=(4 beta v^2/3) sum_i |1-exp(-i K_i/N)|^2 I.   (8)

They are O(N^-2), not identically zero at nonzero finite-lattice K.
For an arbitrary law, replacing every vacancy-pair probability by its upper
bound one yields the same bounds with v^2 replaced by one. Hence vanishing
birth vector martingale noise at this scaling is an unconditional bracket
bound; no local-equilibrium assumption is needed for that conclusion.
The positive bounded exchange generator gives its usual O(N^-1) vector
bracket bound. These martingale statements alone do not control replacement
errors in their drifts.

## 4. Exact product failure and a necessary new fluctuation analysis

At an initially homogeneous orbit-isotropic product, the derivative of
an adjacent connected vector covariance receives from the shared edge

    d/dt Cov(e_i(x),e_i(y))|_0=-beta v^2/3,
    d/dt Cov(b_i(x),b_i(y))|_0=-4 beta v^2/3.              (9)

Other edges have zero contribution to these initial covariances because
the vector means and the summed creation means vanish. The exchange
contribution is zero by product invariance. The one-site variance grows
at rates2 beta v^2 and8 beta v^2 respectively. Summing the six negative
neighbor covariances cancels that one-site growth, exactly as conservation
of the global vectors demands. Thus evolving one-site probabilities do
not determine the fluctuation covariance of this process.

If a suitable interacting finite-mode replacement theorem were proved,
the vector noise in its Euler-scale Gaussian limit would be absent for
this paired rule. Its transverse drift would still have the same supplied
curl form along (2). In particular, zero initial vector fluctuations would
remain zero in that linear limit. This last sentence is conditional on
the missing theorem, not inferred just from the bracket bound. A different
initial ensemble, scale, or correlated mechanism might be needed to produce
nontrivial vector fluctuations from an empty state.

The useful outcome is a concrete, testable design choice: independent
single births create longitudinal vector noise; local opposite-pair births
conserve the global vectors and suppress their leading birth noise. The
latter requires a new correlation theory and an explicitly changed formation
mechanism. Neither rule is selected by a desired electromagnetic analogy.
