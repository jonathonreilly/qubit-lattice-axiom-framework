# Full compact local moments and a nonspatial fourth-response bound

Research derivation, 2026-11-09. This is a bounded consequence of the provisional
relative-coercivity/component suppliers, not retained status or a connected
spatial estimate. Base checkout: 55fd670ff8995427b24617b2273bd3f78b7559d9;
main pin supplied by dispatch: 1e0d3b58dcda7f83152b0bb51729260247454d65.
Preflight passed; no numeric job, Git mutation, remote write, or original proof
edit. Inherited host model, worker effort medium per dispatch. Only this file
is written. The source inventory and literature scan dated 2026-11-09 in the
supervisor's pack were consulted as method maps, not imported theorems.

## 1. Statement and indispensable source class

Fix odd L>=3, kappa>0, the nested two-step forest/ownership convention of
`rough-component-bound.md`, beta=u, both kernel parameters kappa*u, u>=1,
terminal V=I, and fine side N=L^2 m with m>=3. Let pi be the actual normalized
compact posterior, with both kernel levels and every radial normalizer. Let
nu be its exact forest quotient, pi(dU)=nu(da) dh. Write d(a,I) for quaternion
chord distance, which lies in [0,2]. Constants below depend on fixed L,kappa
and the fixed forest templates, not on volume, cell location, or u.

The following consequences hold from the stated suppliers:

1. For every cell x and every 0<t<=t0, with one fixed t0>0,
   P_nu(max_{e owned by x} d(a_e,I)>=t)<=min(1,K exp(-a u t^2)).
   For t>t0 the same probability is at most K exp(-a u t0^2).
2. Every fixed finite coordinate set S and p>0 has
   E_nu max_{e in S} d(a_e,I)^p <= K_{p,S} u^(-p/2).
3. Suppose original real sources F,G are C^2, independent of V, invariant
   under the root-fixed gauge group H, AND invariant under simultaneous
   conjugation. Suppose their quotient restrictions f(a)=F(a,T=I),
   g(a)=G(a,T=I) have fixed finite reader sets and bounded global covariant
   Hessian norms in the product bi-invariant metric. Then, for distinct
   terminal links c,d and fixed tangent vectors v_c,v_d at I,

       |kappa_4,pi(F,G,A_c,A_d)| <= K_FG |v_c||v_d| / u,
       A_c=kappa*u <v_c,M_{1,c}>.

The same estimate holds under any fixed bounded rectangle of real source
tilts exp(sF+tG), with a constant depending on its radius and source
oscillations. It asserts no separation decay and no summability over c,d.

The H-invariance requirement cannot be deleted from this proof. Global
conjugation alone gives dF(I)=0 on original variables, but pi does not
concentrate at original U=I: its independent H coordinates remain Haar.
For example F(U)=w(U_e) for a fine forest edge e is smooth, local and globally
conjugation invariant, yet U_e is exactly Haar under pi for every u by the
forest construction. Thus E|F-1|^p is a strictly positive u-independent
constant. This explicitly refutes the proposed source-moment step for the
larger source class; it does not refute the target cumulant itself. For that
class one must retain the complete orbit source factor and its conditional
covariance; separate orbit means are insufficient.

## 2. Uniformity as threshold tends to zero

The relative supplier states constants epsilon_*,C_*,alpha,c_*,C_Q,rho_Q
uniformly for every exterior radius epsilon<=epsilon_*. Its contraction uses
the worst-case epsilon_*; its compact perturbation lemma uses a fixed local
q-chart, whose complement constant involves that fixed chart radius, not
epsilon. Its quadratic upper-cap estimate likewise fixes rho_Q after fixing
epsilon_*. Consequently no coefficient deteriorates as epsilon decreases.

Choose t0<=epsilon_* and p_word*Cbar*t0<=1/4, where p_word=5L and
Cbar=max(C_*,1). Choose once

    0<b<=min(1,rho_Q,1/(4*p_word)),
    integer h>=0 with C_* exp(-alpha(h+1))<=1/4.

For each threshold 0<t<=t0 run the component argument with delta0=delta=t,
but with these same b,h. Its graph radius D=2h+4, degree upper bound
Delta=(2D+1)^4-1, and neighborhood factor B_h=(2h+1)^4 are now fixed.
The stationary reference satisfies d(a*_e,I)<=t/4 on component cells.
The denominator cap remains q-radius b/sqrt(u), NOT t/sqrt(u): all its
selected mean words have distance at most p_word*(Cbar*t0+b)<=1/2 from I.
Thus the lower H_u bound remains valid even when t<<u^(-1/2).

The numerator and denominator have the identical powers u^{3(k_R-n)/2},
where n is the actual coordinate count and k_R the actual selected-kernel
count.
All kernels, even conditionally constant normalizers, occur on both sides.
The component estimate therefore holds for every u>=1, t in (0,t0]:

    P(S is an entire t-rough component)<=eta(u,t)^|S|,
    eta(u,t)=C0 exp(-a*u*t^2),
    C0=C^(B_h)>=1, a=9c_*/64>0.

Here C can be fixed by the displayed cap/integration constants in the supplier,
using t0 throughout. There is no t-dependent cap constant, factor count,
neighbor degree, or animal count. The event/component graph varies only in
which cells are rough, not in its adjacency.

Choose T=log(2*Delta^2*C0)/a. If u*t^2>=T, the rooted animal sum gives

    P(x rough)<=eta/(1-Delta^2 eta)<=2*C0 exp(-a*u*t^2).

If u*t^2<T use probability<=1. Taking
K=max(2*C0,exp(a*T)) makes K exp(-a*u*t^2)>=1 in this second regime.
Thus both regimes give the claimed min bound. It is a family of pointwise
probability inequalities, so changing the threshold in a layer-cake integral
requires no simultaneous choice of conditional stationary fields. For t>t0
use monotonicity of the event. Whole-torus components are covered by the
supplier's a*=I case. No translation invariance or independence is used.

## 3. Compact moments and quadratic singlet observables

For X_x=max_owned d(a_e,I), layer cake and the preceding bound give, p>0,

    E X_x^p = p integral_0^2 t^(p-1) P(X_x>t) dt
      <= p*K integral_0^infinity t^(p-1) exp(-a*u*t^2) dt
         + 2^p*K exp(-a*u*t0^2)
      <= K_p u^(-p/2),   u>=1.

The last step uses the finite supremum of u^(p/2)exp(-a*u*t0^2) on [1,infinity).
A finite-set union bound gives the same result for any fixed S, with a factor
at most the number of owner cells of S. For p>=1 this implies
||d(a_e,I)||_p<=K_p/sqrt(u). For the later argument only p=4,8 are required.

On SU(2)^S with the product bi-invariant metric, conjugation fixes the identity
and acts on its tangent space as one adjoint SO(3) copy per coordinate. An
invariant linear functional on this direct sum is zero (vary one coordinate
at a time); hence df(I)=0. For each a choose shortest geodesics from I to a_e,
including any shortest choice at -I, and their product path gamma(r).
With H_f=sup ||Hess f||_op, geodesic Taylor's integral formula yields

    |f(a)-f(I)| <= (H_f/2) sum_e |log a_e|^2
                 <= (pi^2 H_f/8) sum_{e in S_f} d(a_e,I)^2.

Indeed theta<= (pi/2)*2sin(theta/2) for theta in [0,pi]. This is a global
compact bound, not a chart-conditioned Taylor remainder. It remains true
when H_f=0, since then df(I)=0 forces f constant. Minkowski and the moments
of order 2p give, for p>=1,

    ||f-f(I)||_p <= C_{p,S_f} H_f/u.

H-invariance identifies the original F with f exactly in the full law.
A fixed original support keeps finite quotient support: restriction to
T=I simply fixes its tree readers, and H-invariance avoids reconstruction
path/orbit dependence. For more general specified quotient observables their
actual reader sets, rather than original support labels, enter the constant.

## 4. Scores, partition Hölder, and the exact response identity

At terminal identity v_c is imaginary, so <v_c,I>=0. Word telescoping in the
unit quaternion norm gives, globally on the compact group,

    |A_c| <= kappa*u*|v_c|*|M_{1,c}-I|
          <= kappa*u*|v_c| sum_{e in S_c} n_{c,e} d(a_e,I).

Here S_c is the complete input-reader set of the actual level-one path mean;
n_{c,e} bounds its averaged occurrence multiplicity, including inverses.
There are finitely many readers/occurrences bounded in terms of L. Fixed tree
links contribute zero, and no terminal output is a hidden reader. It follows
that ||A_c||_p<=C_p |v_c| sqrt(u), uniformly in c and volume. Normalizers have
no terminal-V dependence and have already remained in the underlying law;
this score calculation does not drop them or replace the intermediate law.

Set X1=f-f(I), X2=g-g(I), X3=A_c, X4=A_d. For any partition P of {1,2,3,4},
Hölder within each block B and probability-space norm monotonicity imply

    product_{B in P} |E product_{i in B} Xi|
       <= product_i ||Xi||_4.

The fourth cumulant is the sum of these products with coefficients
(|P|-1)!*(-1)^(|P|-1). The absolute coefficient sum is
1+7+12+6=26. Cumulants of order >=2 are unchanged by adding constants to
an argument (differentiate the log generating function). Consequently

    |kappa_4(F,G,A_c,A_d)|
       <=26 ||f-f(I)||_4 ||g-g(I)||_4 ||A_c||_4 ||A_d||_4
       <= C H_f H_g |v_c||v_d|/u.

No supports are assumed disjoint, except that c and d must be distinct for
the following mixed terminal derivative identity. This is only a magnitude
bound: retaining its constant while summing over arbitrary distant links
would introduce a volume factor.

Precisely, put N_V(s,t)=integral p_V(U) exp(sF(U)+tG(U)) dU, with every
normalizer from the exact chain. Compactness and C^2 terminal kernels permit
these finite derivatives under the integral. For distinct terminal links,
D_d A_c=0; sources have no explicit V dependence. The derivative-of-log
identity is therefore exactly

    partial_s partial_t D_c D_d log N_V(s,t)|_{V=I}
       = kappa_4,pi_{s,t}(F,G,A_c,A_d).

For the same link the general formula includes
kappa_3,pi_{s,t}(F,G,D_d A_c), with the second derivative understood in the
chosen link-coordinate/vector-field convention. It cannot be silently
identified with a fourth cumulant alone.

For real source tilts on |s|<=s0, |t|<=t0_source, the Radon–Nikodym derivative
against pi lies at most

    B=exp(s0*osc(F)+t0_source*osc(G)).

Thus every Lp estimate used above acquires at most B^(1/p), retaining its u
power. The fourth-Hölder bound acquires at most B overall. This proves the
asserted bounded-real-tilt extension at V=I, not a complex-source or
nonidentity-terminal neighborhood estimate.

Normalization must be stated for the requested generating quantity. If Q is
the normalized coarse density Q_V(s,t)=N_V(s,t)/Z_coarse(s,t), then exactly

    log Q_V=log N_V-log Z_coarse.

If Z_coarse integrates over all terminal V and hence is V-independent,
D_c D_d annihilates its source-dependent log, giving the displayed identity
also for log Q. Source derivatives alone do not annihilate this subtraction.
For a local/exterior conditional Q with a normalizing denominator that still
depends on the varied terminal/exterior data, its mixed derivative must
instead retain the corresponding denominator response with a minus sign.
The present full-posterior theorem supplies the numerator case just specified;
it does not assert a uniform estimate for every such exterior conditional.

For sources lacking H-invariance the exact generating factor is
A_st(a)=integral_H exp(sF_a(h)+tG_a(h))dh; its source derivatives include
Cov_{h|a,s,t}(F_a,G_a). The proof above never replaces this by separately
averaged f,g. Its H-invariant scope makes that covariance identically zero.

## 5. Remaining boundary and source identities

This derivation closes threshold-uniform one-cell tails, all fixed local
moments, and the full-compact O(u^-1) fourth cumulant for the explicitly
H-invariant, globally conjugation-invariant C^2 source class, conditional on
the supplied component/relative theorems. Independent checking of this new
consequence is pending. It does not close spatial connected response,
connected-log activities, all depths, arbitrary terminal fields, or mass gap.
The broader globally-conjugation-invariant-only source class has the explicit
source-moment obstruction in section 1; no theorem refuting its target
fourth cumulant is asserted. No editable prompt file was changed.

Load-bearing sources read: `parts/rough-component-bound.md` in full;
`parts/local-relative-coercivity.md` in full; `gates/relative-component-check.md`
in full; `parts/compact-forest-exchange.md` sections 1–2 and 5 for exact law,
root-fixed orbit, reconstruction, and source conventions. The last file's
exchange proof is not an input. Search records were reused only as route maps;
this elementary tail integration and cumulant partition argument imports no
external clustering theorem. The relative supplier's fixed-q-cap argument is
not the shrinking rough threshold t; confusing those radii would invalidate
the constant-uniformity audit.

SHA-256 source pins (worker checkout, 2026-11-09):

| Source | SHA-256 |
|---|---|
| rough-component-bound.md | 1a4c40385f1fc492033f261f8ed938bed23f32475eb9a116347fd7361f9e9c44 |
| local-relative-coercivity.md | 6b7c3a0eba818566fad0cb34f13998a3cf98de632761d7942ca527c51c80cb37 |
| compact-forest-exchange.md | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 |
| relative-component-check.md | b73a1bf25fdfa16fc8f9655e502cf45d00a70297774eda28a827c07168fe8dcc |

Reopen the consequence if any supplier's complete-reader convention,
exterior-uniform constants, ownership/forest geometry, or source class changes.
