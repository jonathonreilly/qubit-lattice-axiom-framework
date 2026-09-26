# A computable third-order formation correction below the Euler scale

2026-09-21. Conditional proof with a sealed independent reconstruction and
finite-generator numerical controls; no independent audit or retained status.
This isolates formation under **symmetric** immutable stirring, not the
nonzero-drive acoustic generator. The full finite-cycle Taylor jet agrees
with the closed response. The independent marked-particle closure and
uniform heat-kernel proof agree with the coefficient derived below.

The purpose is constructive: determine a finite-size correction that a
central-limit theory of native births may have to retain. A hydrodynamic
entropy theorem alone does not control centering at fluctuation scale.

## 1. Model, coefficients and exact unperturbed law

On the cubic torus of side N>=4, each nearest-neighbor bond swaps its two
unchanged states at microscopic rate kappa>0, independent of labels. There
are vacancy and six unit-axis labels. At a vacant x, label a forms at
microscopic rate (beta/N) product_{y~x}(1+j v_a dot v_y), |j|<1.
Work on macroscopic time, so the exchange generator has factor N and birth
intensity beta. Kappa,beta are fixed positive numbers. Initially the law is
product with vacancy v0 in (0,1) and each occupied probability (1-v0)/6.

At j=0 the evolving law is exactly product with

    v(t)=v0 exp(-lambda t), rho(t)=1-v(t), lambda=6 beta.

Finite state-space evolution is analytic in j for each fixed N,T. All series
coefficients here are coefficients of powers of j, without factorials. Let

    E_j n_x(t)=rho(t)+j m1_N(t)+j^2 m2_N(t)+j^3 m3_N(t)+...,
    E_j[v_i(x,t)v_k(y,t)]=j delta_ik C_N(y-x,t)+O_N(j^2), x!=y.

The global vector means vanish exactly by label inversion. The coefficient
C_N is independent of i by internal cubic symmetry. The O_N notation does
not assert a bound uniform in N. No conclusion about fixed nonzero j may be
obtained simply by replacing that notation with O(j^2).

## 2. First-order pair response closes exactly

Let D_N=torus\{0}, and let Delta_ref be the unit-rate lattice Laplacian on
that graph, with edges leading to the removed origin omitted. Write
b(r)=1_{r is a nearest neighbor of 0}. Then

    partial_t C_N=2 kappa N Delta_ref C_N+S(t)b,
    C_N(r,0)=0,       S(t)=4 beta rho(t)v(t)/3.             (1)

For stirring, moving either endpoint of a two-site product moves its
separation by one lattice step. Swapping the two marked endpoints leaves
their product unchanged, which explains the missing jumps to the origin.
Both endpoints give the factor 2 kappa N. At j=0 an independent uniform
birth has zero vector mean and its generator annihilates a two-site vector
product. Differentiating a birth across an adjacent marked pair gives
2 beta rho v/3 at each endpoint, hence S(t).

One can also verify closure at the level of the first density derivative
f1=d(d mu_j/d pi_t)/dj at j=0. The derivative of the birth adjoint is a sum
of nearest-neighbor dot products, with coefficient 6 beta v/rho per
directed incidence. Symmetric stirring preserves the space spanned by all
two-site dot products. Under the physical reversed uniform-birth generator,
each such function has damping 2 rho'/rho; differentiating the product
reference's two vector variances cancels that factor in its observable
covariance. Thus no hidden three-site term is needed in (1).

In particular, for three distinct sites x,y,z,

    [j^1] E_j[1_{eta_x=0} v_i(y)v_k(z)]
        =v(t) delta_ik C_N(z-y,t).                       (2)

To see this directly, under pi_t the only pair term in f1 with nonzero
expectation against v_i(y)v_k(z) has endpoints y,z. Terms containing x
vanish after multiplication by its vacancy indicator; other unmatched
endpoints have mean zero. The remaining factor at x is v(t).

## 3. The first density correction is cubic in the alignment parameter

Summing birth labels eliminates every odd power of j in the instantaneous
total birth intensity. Its second-order term is exactly

    [j^2] R_j n_x
      =2 beta 1_{eta_x=0}
           sum_{unordered distinct y,z in neighbors(x)} v_y dot v_z.

Every corresponding product expectation is zero at j=0. Therefore
m1_N=m2_N=0. Using (2), the third coefficient obeys

    m3_N'=-lambda m3_N+6 beta v(t)
          sum_{unordered y,z in neighbors(0)} C_N(z-y,t),
    m3_N(0)=0.                                           (3)

The factor 6 is 2 from the six-label second moment times 3 vector
components. No neighbor pair in this sum is adjacent to one another on the
cubic lattice. Stirring must propagate the initially nearest-neighbor pair
response to those separations. Consequently very-short-time and large-N
limits are not interchangeable.

For fixed finite N the semigroup in (1) is positive. Connectivity and S>0
give C_N(r,t)>0 and m3_N(t)>0 for t>0. This is a statement about the third
Taylor coefficient; it is not an all-j monotonicity theorem.

## 4. Three-dimensional large-N coefficient

Define the infinite-lattice Green function for the **unit-rate** Laplacian

    -Delta G=delta_0,
    G(r)=(2pi)^(-3) integral_[-pi,pi]^3
                exp(i k dot r)/[2 sum_i(1-cos k_i)] dk.

The integral is finite in dimension three. It is positive and tends to zero
at infinity. At a nearest neighbor, G(0)-G(e_i)=1/6. Removing the edge to
the origin therefore gives

    -Delta_ref [6G(r)]=b(r),       r!=0.                 (4)

Hence the integrated heat semigroup on the punctured infinite lattice
applied to b is 6G. For each fixed r!=0,t>0, (1) consequently predicts

    N C_N(r,t) -> [4 beta rho(t)v(t)/kappa] G(r).         (5)

The required passage can be made with a heat-kernel bound. The finite
punctured tori satisfy, with constants independent of N,

    (exp(u Delta_ref)b)(r) <= C[(1+u)^(-3/2)+N^(-3)].

The complete uniform bound is proved in Section 4a. It uses a bounded-energy
extension across the missing origin and a Fourier proof of the finite-volume
Nash inequality. No mixing-time assertion is imported.

After u=2 kappa N(t-s), the left side of (5) is

    (1/(2 kappa)) integral_0^(2 kappa Nt)
         S(t-u/(2 kappa N)) (exp(u Delta_ref^N)b)(r) du.

For fixed u the torus kernel converges to the infinite-graph kernel:
a finite number of jumps sees the same graph, and the remaining jump-count
tail is bounded by a Poisson tail. The integrated large-u tail is bounded
by C/sqrt(U)+C Nt/N^3, uniformly in N. Splitting at fixed U, then taking
N and U to infinity, proves (5). It also supplies a uniform bound for N C_N on fixed time
intervals, permitting dominated convergence in (3).

Among the fifteen unordered pairs of six neighbors, three have separation
2e_i and twelve have separation e_i+/-e_j. Put

    A_star=3G(2e_1)+12G(e_1+e_2)=15G(0)-3>0.             (6)

The second equality follows from the harmonic equation at e_1:
6G(e_1)=G(0)+G(2e_1)+4G(e_1+e_2), and G(e_1)=G(0)-1/6.
Equation (3) then gives the explicit coefficient

    N m3_N(t) -> D(t),
    D(t)=(24 beta^2 A_star/kappa)
          integral_0^t exp[-lambda(t-s)] rho(s)v(s)^2 ds
        =(4 beta A_star/kappa) v0^2 z
              [(1-z)-(v0/2)(1-z^2)],
    z=exp(-lambda t).                                    (7)

D(t)>0 for every t>0 and interior initial density. Kappa is fixed before
the large-N limit. The coefficient proportional to 1/kappa does not justify
taking kappa to zero, where the spatial spreading premise changes.

## 4a. Uniform heat estimate on the punctured tori

Use counting measure and Dirichlet energy

    E_D(f)=sum_{unoriented edges in D_N} |f(x)-f(y)|^2.

For N>=4 the six neighbors of the removed origin are distinct. Any two can
be joined inside D_N by a path of length at most four. Perpendicular
neighbors use their common diagonal intermediate vertex (length two).
Opposite neighbors use a different coordinate direction as a detour (length
four). These paths avoid the origin also on the N=4 torus.

Extend f to the full torus by F(0)=m, the average over the six neighbors,
and F=f elsewhere. The exact variance identity and path Cauchy-Schwarz give

    sum_y |f(y)-m|^2 = (1/6) sum_{y<z}|f(y)-f(z)|^2
                      <=10 E_D(f).

The last deliberately loose bound uses fifteen paths of length at most
four, with every edge used at most fifteen times. Consequently

    E_T(F)<=11 E_D(f),
    ||F||_1<=(7/6)||f||_1,
    ||f||_2^2<=||F||_2^2<=(7/6)||f||_2^2.                (8)

The L1 estimate uses |m|<=sum_neighbor|f|/6; the L2 estimate uses Jensen.
Both are valid for real or complex f.

Here is the finite-torus Nash estimate with a uniform constant:

    ||F||_2^(10/3)
      <=C [E_T(F)+N^(-2)||F||_2^2] ||F||_1^(4/3).        (9)

For completeness, use the orthonormal Fourier transform and representatives
k_i in [-N/2,N/2]. The eigenvalue is
4 sum_i sin^2(pi k_i/N), bounded below by c|k/N|^2.
For 1/N<=R<=1, the contribution of |k/N|<=R to Parseval is at most
C R^3 ||F||_1^2, since there are at most C(NR)^3 frequencies and each
squared Fourier coefficient is at most N^(-3)||F||_1^2. The complement
contributes at most C R^(-2) E_T(F). Optimizing R proves (9) when the
optimizer lies in [1/N,1]. At the lower endpoint the residual bound
||F||_2^2<=C N^(-3)||F||_1^2 is absorbed by the N^(-2) term in (9).
At the upper endpoint, use ||F||_2<=||F||_1 and the fact that the
optimizer exceeding one means E_T(F)>=c||F||_1^2. A zero function is
trivial; endpoint constants can be enlarged uniformly. Equivalently the
split gives

    ||F||_2^2 <= C E_T(F)^(3/5)||F||_1^(4/5)
                     +C N^(-3)||F||_1^2,

which implies (9) by separating which of its two terms is at least half
the left side. These arguments involve finite Fourier sums only.

Combining (8) and (9) transfers (9) to D_N, with E_D in place of E_T.
Let P_t=exp(t Delta_ref), f_t=P_t delta_x and y(t)=||f_t||_2^2.
Positivity and conservation give ||f_t||_1=1, and differentiation gives

    y'(t)=-2 E_D(f_t),
    E_D(f_t)>=c y(t)^(5/3)-N^(-2)y(t).                  (10)

If y>=C0 N^(-3) for a sufficiently large fixed C0, the last term is
absorbed into half the first, so y'<=-c1 y^(5/3). Also y is always
nonincreasing and y(0)=1. Integrating until this threshold is reached,
and then using monotonicity, yields

    y(t)<=C[(1+t)^(-3/2)+N^(-3)].                       (11)

The semigroup identity gives P_(2t)(x,x)=y(t). Cauchy-Schwarz applied
to P_t(x,y)=sum_z P_(t/2)(x,z)P_(t/2)(z,y) gives the same bound for every
x,y after changing C. Summing over the six neighbors proves the bound
used in (5). Constants do not depend on N, r or t.

For each fixed t and fixed vertices, the finite-torus kernels tend to
the infinite punctured-lattice kernel: uniformize at rate six, couple
steps until reaching a representative-box boundary, and use the tail
of a Poisson(6t) jump count. Thus (11) also implies the infinite-graph
bound C(1+t)^(-3/2). Its potential of b is finite.

It remains to justify its explicit value, rather than assume uniqueness
of an inverse on an infinite graph. W(r)=6G(r), r!=0, is bounded,
nonnegative, tends to zero at infinity and satisfies -Delta_ref W=b.
For this bounded generator, differentiation of P_t W gives exactly

    W-P_t W=integral_0^t P_s b ds.

On a fixed finite set, the heat bound makes P_t W tend to zero; outside
that set W is uniformly small. More explicitly, split the expectation
into the finite set and its complement, use a finite sum of kernel
bounds on the first and sup W on the second, then enlarge the set.
This proves P_t W(r)->0 and establishes integral_0^infinity P_s b ds=6G(r).
Together with the integrable tail estimate already given, this closes
the large-N proof of (5)-(7). The sealed independent reconstruction supplies its own marked-particle
closure and uniform finite-torus proof, with the same coefficient. Its
normalization uses the Green function for 2 Delta, exactly half of G here.

## 5. Fluctuation-scale implication and its exact limit

The zero Fourier mode at central-limit normalization has mean
N^(3/2)[E_j n_x(t)-rho(t)]. Its third Taylor coefficient is
N^(3/2)m3_N(t), which by (7) grows as sqrt(N) D(t).

Thus the first nonzero perturbative density response is negligible for the
Euler law but not for its naive fluctuation centering. This identifies a
specific deterministic correction to compute before claiming a native-birth
central-limit theorem centered at the product reaction solution.

It does **not**, by itself, disprove such a theorem for a fixed nonzero j:
that would require uniform control of higher Taylor coefficients or another
argument. It also does not establish the corresponding coefficient for the
nonreversible axis-balanced wave generator. The present calculation is a
controlled symmetric-stirring test case and a concrete next obligation for
the interacting formation lane.

## 6. Completed primary controls and remaining obligations

`native_formation_centering_check.py` assembles the complete 2401-state
four-cycle generator and its 9604-state Taylor jet through order three,
separately from the punctured-relative-position response. On that cycle
use its two-neighbor formation footprint and its one neighbor pair; the
six internal labels and per-label beta are unchanged. At beta=.2,
kappa=.75,v0=.4, eight times through t=.7, the first two mean-density
coefficients vanish to below4e-17. All pair coefficients and the
vacancy-weighted pair projection agree to below1.1e-17; the third density
coefficient agrees to below4.8e-18 (final value .00163432385382513).
These are numerical matrix-exponential controls with exact integer-scaled
generator assembly, not exact arithmetic evaluation of the exponential.

A separate three-dimensional response computation at beta=.2,kappa=.75,
v0=.6 uses N=4,8,16,24,32,48,64 with no fitted coefficient. At t=1,
N m3_N rises from .02697975 at N=8 to .03322368 at N=64, versus the
Green-function target .03897323. The N=4 value is .04296748: the finite
size sequence is not globally monotone and must not be reported as such.
The Green quadrature gives G(0)=.2527310098587 and A_star=.79096514788;
its QUADPACK error estimate is not an interval certificate. All seven
cases and the full finite-cycle output are preserved, including that
small-torus deviation.

The independent report is `independent_native_centering/REPORT.md`, SHA
`24b168b662c0e6f72f1b2f95a6efe7fb3440eb5b5d57addf951020335fe05f4e`.
Seal SHA `cb26009a925ecd6861de994e57df67f904f906e5beac33aae6e6ed958b8a5d8e`
binds ten artifacts, three source dependencies and two instruction snapshots,
all verified. The complete report and checker have been read; eleven controls
include a separately assembled full cycle jet and finite-torus Poisson checks.
These checks do not replace the proof or constitute formal retention.

Next obligations: if seeking a fixed-j statement, control the remainder
uniformly in N. The driven exchange generator requires its own response
analysis. The present result supplies neither of those extra conclusions.
