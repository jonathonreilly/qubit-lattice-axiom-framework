# K4CORR2 — diagram bounds and the unresolved renormalized correction

**Disposition: partial result; the requested uniform Yang–Mills Cbar and
positive Yang–Mills g_star² remain OPEN.** Explicit rational bounds are
obtained for three finite subfamilies and for all five **bare, regulated**
families. The latter bound diverges when its cutoffs are removed. It is
not a bound on the renormalized coefficient. The internal subtraction,
finite matching and original-law remainder estimates have not been closed.

| Author target | Result | Status |
|---|---|---|
| Write the normalized order-h² correction | Equations (4)–(6), including ghosts, insertion vertices and counterterms | **PROVEN formal**; original-law identification **OPEN** |
| Explicit elementary bound for every class | All bare classes have (13); finite separated subfamilies have (10), (12). Complete renormalized classes are not enclosed | **PROVEN** at those restricted scopes; requested uniform Cbar **OPEN** |
| Non-cancellation window and short-distance rate | Finite-regulator window (17); uniform window/rate (22)–(24) conditional on a finite matched Cbar | **PROVEN conditional**; positive actual-YM window **OPEN** |
| Exact higher-order/nonperturbative input | K4RATIO-REM and Q-LOW in (25)–(26), or K4MATCH (24) | **OPEN** producers; positive fixed-scale consequence **PROVEN conditional** |

This is a research-lane artifact under [PROCESS_LIGHT](PROCESS_LIGHT.md),
not the consolidated proof or an audit decision. Balaban and Dimock are
credited for constructive RG. No estimate of theirs is an implicit premise.
The [log](K4CORR2_LOG.md) records reading, attempts and review; the
[registration](checks/k4corr2_criteria.md) precedes the checker.

## 1. Exact target and what the preceding regularization specifies

Fix N>=2, d=N²−1, h=g_FLOW, g_std=sqrt(2N)h and x=h²=u^-1.
Use the unchanged centered clover density with Z(a)=1, and exactly
[CUMUL (C1)–(C2)](CUMUL.md): four nonnegative unit-integral product
bumps of coordinate half-width 1/10000 centered at
`((2i−5)/2,0,0,0)`, scaled by lambda. At lambda=1 every pair of
support points from different bumps has distance at least

    1−1/5000 > 1/2 =: sigma.                              (1)

Keep the smooth-test coefficients, not their center-point substitutes:

    P=lambda^16 kappa4(O1,O2,O3,O4),
    Q=lambda^8 Cov(O2,O3),             R=P/Q²,
    A4=d A/pi^8,  A2=d B0/pi^4,       R0=A4/A2²,
    3/2<A<5/3,  11<B0<13,            R0>3/(338d).          (2)

These are the free coefficients proved in CUMUL §3. All unqualified
coefficients below use lambda=1, equivalently the scale mu=1/lambda.

**Regulator provenance — PROVEN source fact.** K4CORR §5.1, immediately
after (15), explicitly says that a complete regulator, zero-mode/IR
prescription, subtraction scheme and removal still have to be specified.
REVIEW_K4CORR R6 and binding B1 confirm that gap. Its convention is
unflowed separated insertions in a regulated Euclidean Feynman gauge;
it does not select a complete regulator that this lane can reproduce.

For a concrete diagnostic calculation use the scalar heat-cutoff kernel

    D_delta(z)=integral_(delta²)^infinity
                   (4pi t)^-2 exp(−|z|²/(4t)) dt,
    <A_mu^a(y) A_nu^b(z)>_0=delta_ab delta_mu,nu D_delta(y−z),
    <c^a(y) bar c^b(z)>_0=delta_ab D_delta(y−z).            (3)

This is LGF §2 (6), rescaled. Work on R^4; its massless p=0 singularity
is locally integrable, and no discrete harmonic mode is introduced.
Cut off **interaction vertices only** to Omega_R=[−R,R]^4, R>=2.
The insertions retain the exact bumps. The ghost expectation is the
Grassmann Wick rule, not a positive scalar law. At finite delta,R all
coefficient integrals exist by the bounds below. No actual Gaussian
probability interpretation for the combined ghost/gauge integral is needed.

This choice completes a *bare diagnostic* in K4CORR's formal continuum
setting. It is not claimed to preserve all gauge identities or to be the
Wilson regulator. Symmetry-restoring counterterms and original-observable
matching remain required. In particular delta is a UV regulator to remove,
not a positive physical flow time or a new observable.

## 2. All order-h² terms — PROVEN formal

Let s=sqrt(2N), `f_mu,nu^a=partial_mu A_nu^a−partial_nu A_mu^a`,
and `C_mu,nu^a=f^{abc}A_mu^b A_nu^c`. Repeated ordered mu,nu are
summed. Write the vertices as

    X_i0=(1/2) integral f_i f²,
    X_i1=s integral f_i f C,
    X_i2=(s²/2) integral f_i C² + X_ct,i,2,
    V1=(s/2) integral_Omega f C
                  +s integral_Omega f^{abc}(partial_mu bar c^a)A_mu^b c^c,
    V2=(s²/4) integral_Omega C² + S_ct,2.                  (4)

The factors follow by expanding `(f+shC)²/2` at a source and
`(f+shC)²/4` in the action. In the diagnostic calculation `ct=0` is
part of its definition. That choice is not used for the renormalized YM
coefficient. The original lattice action also has Haar, discretization
and operator-matching contributions; they are not included by renaming V2.

For n=2, use I={2,3}; for n=4, use all four labels. The full formal
coefficient, with counterterms where present, is

    D_n = sum_r kappa0(X_r2, X_s0:s!=r)                    [F1]
        + sum_(r<s) kappa0(X_r1,X_s1,X_t0:t!=r,s)          [F2]
        − sum_r kappa0(X_r1,X_s0:s!=r,V1)                  [F3]
        − kappa0(X_r0:r in I,V2)                          [F4]
        +(1/2) kappa0(X_r0:r in I,V1,V1).                 [F5] (5)

Every line is one joint connected cumulant. To prove completeness,
tilt the Gaussian by the leading sources, put
`A_t=sum t_i X_i1−V1`, `B_t=sum t_i X_i2−V2`, and expand its normalized
logarithm through h². Its h² term is
`<B_t>_t+kappa_t(A_t,A_t)/2`, minus its value at t=0. Distinct-source
differentiation gives (5). The two orderings cancel the half for F2
and F3; it remains for F5. Gaussian contractions internal to a vertex
are included unless explicitly excluded below. Centering only changes
the source-linear term.

After a justified renormalized/matched limit, the desired coefficient is

    R/R0=1+c x+O_form(x²),
    c=D4/A4−2D2/A2.                                      (6)

The formal even-power notation assumes the complete field/coupling
reversal symmetry described in K4CORR §3. It supplies no error estimate.
The common running logarithm and common multiplicative insertion factor
cancel as proved there; they do not remove the remaining graph families.

## 3. Component and pairing ledger — PROVEN

Expand every f into its two derivatives and every C into its color sum.
In a basis `tr(T^a T^b)=delta_ab/2`,
`f^{abc}=−2i tr([T^a,T^b]T^c)`. Matrix Cauchy–Schwarz and
`||AB||_HS<=||A||_HS||B||_op<=||A||_HS||B||_HS` imply
`|f^{abc}|<=sqrt(2)<=2`. Also `s<=2N`, while `s²=2N` is kept exact
for quartic vertices. Thus absolute coefficient sums, before contractions,
are bounded by the following rational polynomials:

| Vertex without ct | Coefficient bound | Number of fields | Total derivatives |
|---|---:|---:|---:|
| X0 | L0=32d | 2 | 2 |
| X1 | L1=128N d³ | 3 | 1 |
| X2 | L2=64N d⁵ | 4 | 0 |
| V1, gauge plus ghost | T1=80N d³ | 3 | 1 |
| V2 | T2=32N d⁵ | 4 | 0 |

For example X0 costs `(1/2)16d·4`, X1 costs `16d³·2·2·2N`,
and X2 costs `(1/2)16d⁵·4·2N`. The gauge cubic costs 64N d³ and
the ghost cubic 16N d³. These deliberately overcount zero components.
Source integrations cost `||f_i||_1=1`; a bulk integration costs
`V=|Omega_R|=(2R)^4`. No bump normalization quadrature is necessary.

For a degree list ell=(ell_1,...,ell_v), the number of connected
labelled bosonic pairings is the finite integer

    nu(ell)=sum_(pi partition of {1,...,v})
         (−1)^(|pi|−1)(|pi|−1)!
         product_(B in pi) m(sum_(i in B) ell_i),          (7)
    m(q)=0 for q odd;  m(q)=(q−1)!! for q even; m(0)=1.

Indeed each pairing decomposes uniquely into its vertex-connected
components. Expanding the logarithm of their finite moment polynomial
removes precisely the disconnected pairings. This also proves the
connected-contraction rule used in (5). Even ghost monomials have signs
but factor over disconnected components; their admissible contractions
are a subset of this unsigned bosonic majorant. They are never assigned
positive physical amplitudes.

The exact counts are:

| Family | Degrees | nu for n=2 | nu for n=4 | No-self nu for n=2,4 |
|---|---|---:|---:|---:|
| F1 | (4,2,...,2) | 12 | 576 | 0,288 |
| F2 | (3,3,2,...,2) | 15 | 720 | 6,360 |
| F3 | (3,2,...,2,3) | 90 | 7200 | 36,4176 |
| F4 | (2,...,2,4) | 72 | 5760 | 24,3456 |
| F5 | (2,...,2,3,3) | 720 | 86400 | 360,55296 |

These are **majorant counts**, not evaluated YM diagrams. The checker
independently enumerates all labelled pairings, tests connectivity, and
compares with (7). For the no-self version of (7), inclusion-exclusion
selects k_i forbidden internal pairs at vertex i with multiplicity
`binom(ell_i,2k_i)(2k_i−1)!!`; this supplies a second independent count.

## 4. Uniform bounds on finite subfamilies

### 4.1 External-only contractions without self-pairs — PROVEN

For the continuum D(z)=1/(4pi²|z|²), direct differentiation, or
LGF (25), gives `|partial^alpha D(z)|<=2^m(m+1)! |z|^(-2−m)`
for m<=2. Every primitive contraction between our distinct supports
is therefore bounded by

    H=512,                                               (8)

since m=0,1,2 give bounds 4,32,384 at |z|>=1/2. The same estimate
could be obtained in lattice units away from diagonals using LGF
(4)–(5), with its explicit 2^1000 error constants. LGF (41) controls
the free curvature limit; it does not control an internal interaction.

Let D_n^ext be exactly F1+F2 in (5), with bare vertices, and retain
only pairings with no pair inside a vertex. These integrals are absolutely
convergent. The table gives

    |D4^ext| <= H^5[4·288 L2 L0³ + 6·360 L1² L0²]
              = 9·2^73 N(1+15N)d^8 =: B4,
    |D2^ext| <= 6 H³ L1² = 3·2^42 N² d^6 =: B2.          (9)

For an elementary check of the small counts, degree (4,2) cannot pair
without a self-pair, and (3,3) has 3!=6 pairings. For (4,2,2,2),
the quartic vertex has a double edge to one of three others and a
triangle through the remaining two. There are 96 labelled pairings
per choice, giving 288. For (3,3,2,2), no-self inclusion-exclusion gives
`945−8·105+22·15−24·3+9=372`; subtract the disconnected triple-edge
and double-edge components, `6·2=12`, giving 360.

Using pi<4 in the positive lower bounds in (2),

    |D4^ext/A4−2D2^ext/A2| <= C_ext,
    C_ext = 3·2^90 N(1+15N)d^7 +(3·2^51/11)N²d^5.        (10)

This is an explicit rational bound for this sub-sum, not Cbar for c.
Deleting the omitted self-pairs would change the target. In particular,
centering X2 does not remove its quadratic tadpole remainder (§6).

### 4.2 A quartic vertex joining four distinct supports — PROVEN

Within F4 for n=4, retain the pairings in which the four bulk A legs
join one leg at each distinct X0. The remaining four external legs pair
in three ways. The count is `4!·2^4·3=1152`. Each bulk-external
primitive edge is bounded by `4|y−x_i|^-3`; each of the two remaining
external edges is bounded by H.

The following elementary integral is uniform over the support points:

    integral_R4 product_(i=1)^4 |y−x_i|^-3 dy < 2^26.     (11)

Partition space into nearest-point cells. On cell i, when r=|y−x_i|<=1,
each other distance is at least sigma/2=1/4: otherwise both it and r
would violate the pair separation. The integrand is at most
`4^9 r^-3`, whose unit-ball integral is at most `32·4^9`.
When r>1, all four distances are at least r, and the integral is at
most `2pi² integral_1^infinity r^-9 dr<4`. Summing four cells gives
`4(32·4^9+4)<2^26`. This is a direct L1 estimate; it needs no unstated
Hölder/Young endpoint hypothesis.

Consequently this signed sub-sum D4^star obeys

    |D4^star| <=1152 T2 L0^4 4^4 H² 2^26
                =9·2^84 N d^9,
    |D4^star/A4| <= C_star=3·2^101 N d^8.                 (12)

This includes its full infinite-volume integration, not just a compact
region. There is no corresponding four-distinct-support star for n=2.
Thus C_safe=C_ext+C_star is a fully explicit bound for a nonempty finite
sub-sum of c. Its omitted complement is not known to vanish or obey
the same bound. No positivity claim for full YM uses C_safe.

## 5. All five bare families at a regulator — PROVEN

LGF (21) follows directly from the first two derivatives of the Gaussian
heat kernel. Discarding its exponential and integrating t>=delta² gives

    |partial^alpha D_delta(z)|<=16 delta^(-2−m), m<=2.

An F1/F2 monomial has n+1 edges and 2n−2 derivatives, hence exponent
`2(n+1)+(2n−2)=4n`. The corresponding F3/F4 and F5 exponents are
4n+4 and 4n+8. This tracks all derivatives including ghost derivatives.
Triangle inequality, the vertex ledger and the connected counts give

    |D_n^bare(delta,R)| <= M_n(delta,R),                  (13)

    M2 =16³ delta^-8 [24 L2 L0+15 L1²]
        +V16^4 delta^-12 [180 L1 T1 L0+72 T2 L0²]
        +360 V²16^5 delta^-16 T1² L0²,

    M4 =16^5 delta^-16 [2304 L2 L0³+4320 L1² L0²]
        +V16^6 delta^-20 [28800 L1 T1 L0³+5760 T2 L0^4]
        +43200 V²16^7 delta^-24 T1² L0^4,
    V=(2R)^4.

Every number in (13) is exact. It includes self-pairs, all five bare
families and both cubic species. It does **not** bound unspecified
counterterms. Using all pairings instead of the connected ones would
give a looser upper bound but would not compute the cumulant.

For completeness, the free denominators at this regulator can be
bounded without replacing them prematurely by A2,A4. Denote their
exact smooth-test values by A2_delta,A4_delta. If `0<delta<=2^-20`,

    |A4_delta−A4| <=2^63 d delta^6 < A4/2,
    |A2_delta−A2| <=2^49 d delta^6 < A2/2.                (14)

Here is a uniform proof. Set r>=1/2, q=r²/8>=1/32, t0=q/delta²>=1.
The omitted heat integral of a scalar second derivative is at most
`16 q^-2(1+t0)e^-t0`. Since `e^t>=t^4/24` and `1+t<=2t` for t>=1,
this is at most `768 q^-5 delta^6<2^35 delta^6`.
Four scalar terms make one curvature entry, and its six-dimensional
operator norm error is at most `E=2^40 delta^6`. The continuum curvature
operator has norm at most 16 on these supports; E<=2^-80<1.
Telescoping the three four-cycles, with trace bound six, gives
`48d·24E·17³<2^23 d E`. The two-cycle error is at most
`12d E(32+E)<2^9 d E`. These are (14); their upper bounds are below
`3d/(4·4^8)<A4/2` and `11d/(2·4^4)<A2/2` respectively.

In this bare model the first ratio coefficient is defined using its
own leading coefficients:

    c_bare(delta,R)=D4^bare/A4_delta−2D2^bare/A2_delta.

Thus the following constant and window are explicit:

    C_bare(delta,R)=2^18 M4/(3d)+2^10 M2/(11d),
    |c_bare(delta,R)|<=C_bare(delta,R),                    (15)
    x_star,bare(delta,R)=1/[2 C_bare(delta,R)]>0.          (16)

The **truncated ratio polynomial** satisfies

    R_bare^[1]=[A4_delta/A2_delta²](1+c_bare x)
                    > A4_delta/(2 A2_delta²)>0
    for 0<=x<x_star,bare.                               (17)

This statement is about a truncated formal polynomial. It is not a
positivity theorem for a full regulated gauge/ghost measure, and not
a bound for Wilson YM. Even the full first-order numerator and denominator
truncations must be distinguished from truncating their ratio.

**Failed uniformization attempt.** All terms of M4 are positive
monomials in delta^-1 with powers at least 16, including a nonzero
delta^-24 term. Hence `M4(delta/2,R)>=2^16 M4(delta,R)`.
The bound also grows with V. Its resulting window shrinks to zero
under regulator removal. This proves failure of this *majorant* to
supply a uniform window, not divergence of the renormalized coefficient
or impossibility of a better calculation.

## 6. Attempt at the remaining internal subtraction estimate

### 6.1 The actual internal singularities — PROVEN diagnostic facts

External separation does not separate bulk y,z from one another or
from an insertion. Three missing regions survive the preceding bounds:

* **Tadpoles:** `D_delta(0)=1/(16pi² delta²)`. Contractions of two
  fields inside a quartic insertion leave a quadratic operator, in
  addition to scalar terms. Subtracting its expectation removes the
  scalar, not the quadratic part. For example in SU(2), using
  `T^a=sigma_a/2` gives `f^{312}=1`, and
  `C_12^3=A_1^1 A_2^2−A_1^2 A_2^1`. The square includes
  `(A_1^1)²(A_2^2)²`; its first-factor contraction leaves
  `D_delta(0)(A_2^2)²`. The sum's gauge-consistent counterterm
  treatment cannot be replaced by centering the scalar insertion.
* **Two bulk vertices:** the ghost part of F5 contains two differentiated
  scalar propagators between y,z. Away from zero,
  `sum_mu |partial_mu D(z)|²=1/(4pi^4 |z|^6)`, and

      integral_(epsilon<|z|<rho) sum_mu |partial_mu D(z)|² dz
              =(epsilon^-2−rho^-2)/(4pi²).              (18)

  The ghost loop can be attached through its two gauge legs to a path
  through all external quadratic insertions, so connected subtraction
  does not remove this topology. Equation (18) diagnoses failure of an
  absolute scalar majorant. It does not assert that the sum of YM and
  ghost tensors has this divergence after counterterms.
* **Insertion collisions and their intersections:** F3, F4 outside
  (12), and F5 also permit two or more incident lines to approach one
  external insertion. In F5 a bulk-bulk collision can occur inside the
  same small neighborhood. Isolated one-variable subtractions must be
  made compatible on these nested/intersecting regions.

These are explicit attempted integration regions. They cannot be
bounded by applying Young or Hölder to a locally nonintegrable
`|z|^-4` or `|z|^-6` absolute kernel. Cancellation/subtraction must
precede such inequalities. This leaves renormalized bounds as a live
route; it is not a no-go theorem for that route or for YM.

### 6.2 A subtraction library through quadratic degree — PROVEN

For k=0,1,2, phi in C^(k+1) on the closed ball B_rho, let T_k phi
be its Taylor polynomial at zero and
`M_(k+1)=max_(|alpha|=k+1) sup_Brho |partial^alpha phi|`.
Taylor's integral remainder along the line tz, and
`|z|_1<=2|z|` in four dimensions, give

    |phi(z)−T_k phi(z)|
       <=[2^(k+1)/(k+1)!] |z|^(k+1) M_(k+1).

Consequently

    integral_(|z|<rho) |phi(z)−T_k phi(z)|/|z|^(4+k) dz
       <= [32·2^(k+1)/(k+1)!] rho M_(k+1),                (19)

with exact constants 64,64,128/3 for k=0,1,2. A kernel dominated
by `K|z|^(-4−k)` multiplies the bound by K. The factor 32 bounds
the sphere area 2pi². This also supplies the missing degree-two
subtraction for a single |z|^-6 singularity, provided its remaining
test factor has a bounded third derivative in that region.

**Where this attempt stops — OPEN.** On an overlapping insertion/bulk
collision that derivative bound is not uniform: the other propagators
can be singular at the same point. One needs a full compatible forest
or a joint sector decomposition, its explicit derivative norms, the
finite local terms, the ghost/gauge identities and the IR limit. This
note has not constructed and bounded that complete operation for (5).
Neither (19) alone nor setting all finite local terms to zero is a
certificate for c. In particular no numerical value of the missing
complement is assigned.

For a precise ledger, let D_n^fin denote the subfamilies bounded by
(9), plus (12) for n=4. Once a matched renormalized D_n exists, define
its complement by subtraction. Then

    c=c_fin+c_rem,        |c_fin|<=C_safe,
    |c_rem|<=C_rem   would give   Cbar=C_safe+C_rem.        (20)

Here **C_rem is not supplied**. This equation is an obligation, not
the requested explicit Cbar. Replacing it by an unknown derivative
supremum would leave the same missing task. The stronger alternative
of bounding D4 and D2 separately also remains open.

The subtraction method is attributed to Bogoliubov, Parasiuk, Hepp and
Zimmermann. Pottel's [configuration-space paper](https://arxiv.org/abs/1706.06762)
and [normal-product paper](https://arxiv.org/abs/1708.04115) were consulted
at abstract scope for orientation only. No convergence or matching
theorem from those papers is imported into (19) or (20).

## 7. What an actual finite Cbar would buy

**PROVEN conditional.** Suppose the missing renormalized matching and
subtraction calculation yields a fixed finite bound `|c|<=Cbar`, Cbar>0,
in FLOW units, independent of delta,R and the common short scale.
Then the order-x ratio truncation has the explicit window

    g_star²=1/(2 Cbar),
    R^[1]=R0(1+c x)>R0/2>3/(676d),   x<g_star².          (21)

Its sign conclusion concerns the normalized cumulant at this order.
It does not automatically control the unnormalized numerator coefficient,
which has an additional common operator-normalization factor.

Under precisely K4CORR §4's conditional FLOW hypotheses, put

    lambda_m=L^-m, v_m=b_*m,
    b_*=[11N²/(12pi²)]log L,
    E_m=U+R_F+C_rho/(U−R_F)
          +(C_rho/b_-)log[1+b_-m/(U−R_F)], U>R_F.

For E_m<=v_m/2, FLOW gives |u−v_m|<=E_m and therefore

    |c/u−c/v_m| <=2 Cbar E_m/v_m²,
    |c/u|<=2 Cbar/v_m.                                  (22)

The proof retains the denominator:
`|1/u−1/v_m|<=E_m/[v_m(v_m−E_m)]<=2E_m/v_m²`.
It follows that the isolated correction has rate

    c h²(lambda_m)=c/[B log(1/lambda_m)]
              +O(log log(1/lambda_m)/log(1/lambda_m)²),
    B=11N²/(12pi²).                                     (23)

A sufficient scale for (21) is `v_m>4 Cbar` together with
`E_m<=v_m/2`. Since pi<4 and log L>=log 3>1, one explicit rational
part of this requirement is

    m>768 Cbar/(11N²).                                  (24)

The other condition uses the supplied FLOW constants; none is claimed
numerically established for the actual chain. In particular FLOW
§110 still leaves UNIV hypotheses open. No choice of m repairs the
divergent cutoff dependence of C_bare in (15). Equations (21)–(24)
cannot yet be instantiated with a proved uniform Yang–Mills Cbar.

## 8. The exact higher-order and nonperturbative remainder input

The following sufficient estimate names what must be proved on the
**original Wilson law**, after supplying c and its finite bound:

**K4RATIO-REM (OPEN).** There are constants H,J>=0, S>0 and x0>0,
uniform in the common trajectory, with the matched coefficient c, such
that for `x=u_k^-1<=x0` at the fixed CUMUL tuple,

    |R_(K,R)(m)/R0−1−c x|
        <=H x²[1+log(1/x)] + J exp(−S/x) + eta_(K,R)(m), (25)

where x<=1, eta is nonnegative and tends to zero along the one common
cutoff/volume limit for each fixed m. The first term is a quantitative
version of the higher-order `O(g^4 log)` relative remainder. The second
is an explicitly sufficient nonperturbative form, not an assumed
instanton estimate; a different proved vanishing bound could replace it.
All constants require actual producers. An unbounded formal O symbol
is insufficient.

**Q-LOW (OPEN).** On the same domain/sequence,

    |Q/(A2 x²)−1|<=1/2.                                 (26)

This gives a positive denominator and its absolute scale. It can be
produced by CUMUL C-2MATCH or K4MATCH (24) with its own coefficient
and remainder bounds. It does not follow from the ratio estimate.

The estimates must include the unflowed clover's local source matching,
all finite normalizers, the fourteen conditional terms in K4MATCH (5),
terminal integration, background/large-field regions and exterior errors.
Coordinator outputs for source radius, finite-coupling kernels and
coercivity/tails are named inputs only within their stated scopes.
K4RATIO-REM together with Q-LOW is a sufficient packaging of lower
matching, not a claimed easier replacement for the dynamical target.

For explicit bookkeeping, let `T=3H/2+J/S²`. If x<=1/2, elementary
`log(1/x)<=1/x` and `exp(S/x)>=(S/x)²/2` give

    H x²[1+log(1/x)]+J exp(−S/x)<=T x.

Thus take

    x < min(x0,1/2,1/[2max(1,Cbar)],1/[8max(1,T)]),
    eta_(K,R)(m)<=1/8,                                  (27)

and impose (26) there. The remainder is at most 1/4 and the first
correction has magnitude less than 1/2. Consequently

    R/R0>1/4,       R>3/(1352d),
    P=R Q²>A4 x^4/16.                                  (28)

The exponential estimate is simply the positive Taylor series for exp;
no numerical nonperturbative action S is imported. If constants in
(27) are supplied by rational enclosures, the threshold is rational too.

Choose one m_star meeting these conditions and keep lambda_star fixed.
With the same trajectory's finite upper bound u<=U_+(m_star),

    kappa4_(K,R)>A4/[16 lambda_star^16 U_+(m_star)^4]>0.   (29)

The common separated-moment convergence CUMUL C-SEQ/MOM passes this
polynomial lower bound to the limit. A ratio limit alone, with Q allowed
to vanish, would not supply it. The reconstruction and all-order OS
conditions remain separate. As in CUMUL, a positive fourth cumulant
excludes Gaussian fields **on e**; free theories with composite e are
not thereby excluded.

## 9. Verification and remaining scientific task

The [checker](checks/k4corr2_exact.py) uses integers and Fractions.
Its [first run](checks/k4corr2_attempt01_results.json) passed all **97**
registered exact assertions, including direct normalized-moment checks
of (5) for n=2,4, independent pairing counts and mutation controls.
It evaluates no renormalized YM integral. Scientific completion is
separately recorded **OPEN / NOT PASSED** in that result file.

The [resource receipt](checks/k4corr2_attempt01_run.json) records one
serial child, nice 20, five thread limits equal to one, five exclusive
locks (existing locks opened read-only), 52% native free memory and
combined peak RSS 37,584,896 bytes. All load averages were below 2.
No RLIMIT_AS, pools or failed numerical run was used. Scientific
majorants use exact rational arithmetic; resource readings are telemetry.

Claim type: a bounded mathematical result for stated diagram subsets
and a formal regulated model. Actual target status: **OPEN**. Trace:
upstream support for REVIEW_K4CORR B1 and the K4MATCH lower-matching
input, not their discharge. No axiom, empirical coefficient or new
framework primitive is assumed. Source hashes are in
[the manifest](checks/k4corr2_sources.json).

The next decisive work is a complete compatible subtraction and finite
matching estimate for the complement in (20), with both regulator limits.
After that, (25)–(26) still require original-law producers. The present
author result does not meet the requested full Cbar or positive actual-YM
window. Independent review is recorded separately; author algebra and
review agreement do not constitute an audit status.

**Fresh hostile review: HOLD for completion of the brief.** The
[independent review](checks/k4corr2_review.md) found no mathematical defect
in the stated partial results, reproduced all 97 registered assertions,
and independently verified all 20 connected/no-self counts by weighted
multigraph enumeration. It identifies the missing uniform renormalized
enclosure as binding B1. Naming the downstream actual-law remainder
satisfies that portion of the brief; proving it remains OPEN. This is
same-family Codex review, not cross-family review or an audit decision.
