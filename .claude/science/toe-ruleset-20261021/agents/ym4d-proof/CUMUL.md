# CUMUL — a separated fourth-cumulant witness

**Disposition.** The comparator and the free leading coefficient below
are **PROVEN**. The implication from the stated YM inputs to a non-Gaussian
reconstructed **e field** is **PROVEN conditional**. Those YM inputs remain
**OPEN**. The verdict that this is a smaller witness interface, but not a
demonstrated reduction of the dynamical obligations, is **ARGUED**.

Two distinctions determine the result. First, the separated three-point
function of the scalar free-Maxwell `F^2` in four dimensions is **zero**;
being quadratic in a Gaussian does not make every higher cumulant nonzero.
The fourth cumulant works. Second, Gaussianity here is on the named e
generators. A quadratic observable in a Gaussian underlying theory can
have this same nonzero fourth cumulant. Thus this excludes all elementary
F2 and all F3 of [WITNESS §1](WITNESS.md), including all rescalings; it does
not exclude arbitrary Wick-composite realizations in free theories.

## 1. Fixed field, domain, tests and normalization

Use exactly WITNESS's scalar separated hierarchy

    A_e = direct_sum_(n>=0) E_n,  E_n = ^0 S(R^(4n)),

where all jets of a test vanish on every pair-coincidence plane. Products
are only those admitted on that hierarchy. Do not adjoin ordinary
coincident powers `e(f)^k`. The lattice representative is

    e_a(x) = (4a^4)^(-1) sum_(mu!=nu) sum_(p in clover_mu,nu(x))
                                [1 - Re tr(U_p)/N],
    ehat_a = e_a - E_(K,R)e_a,              Z(a) = 1.             (C1)

The subtraction is a scalar at each regulator, not a replacement of the
observable by its quadratic part. All cumulants of order at least two
are independent of this subtraction. Fix `N>=2`, `d=N^2-1`. Follow
WITNESS's Wilson convention `u=g_FLOW^(-2)=2N/g_std^2`.

Here are actual test functions, fixed without fitting a YM value. Set
`epsilon=1/10000`. Let `b(s)=exp[-1/(1-s^2)]` for `|s|<1`, and zero
otherwise; set

    rho(y) = product_(mu=0)^3 b(y_mu) / (integral_R b(s) ds)^4,
    c_i = ((2i-5)/2,0,0,0),  i=1,2,3,4,
    f_i(x) = epsilon^(-4) rho((x-c_i)/epsilon),
    f_(i,lambda)(x) = lambda^(-4) f_i(x/lambda).                (C2)

Each is real, smooth, nonnegative, of integral one, and supported in a
cube of coordinate half-width epsilon about c_i. The four supports have
strictly ordered, disjoint time projections. Reflection in time zero
exchanges f1 with f4 and f2 with f3. All products on distinct subsets are
compact off-diagonal tests. A common time translation makes all four
times positive when the ordered insertion convention requires it.

For a state S write `M_B=S_|B|(tensor_(i in B) f_i)`, with labels in
increasing order and `M_empty=1`. Define its cumulant by the finite formula

    K_n(f1,...,fn) = sum_(pi partition of {1,...,n})
                       (-1)^(|pi|-1)(|pi|-1)! product_(B in pi) M_B.
                                                                    (C3)

The products on the right are products of numbers, not extra products
in A_e. In the centred hierarchy our selected coordinates reduce to

    K4 = S4(1,2,3,4) - C12 C34 - C13 C24 - C14 C23,
    Cij = S2^T(fi,fj),             B = C23.                    (C4)

For a reflection-positive centred hierarchy, `B=||[ehat(f3)]||_OS^2>=0`.
For `B>0`, use the scale-free displayed quantity

    R4 = K4 / B^2.                                            (C5)

The N5 witness itself will be the polynomial `W=K4` at one fixed lambda.
Section 4 explains why this choice and the normalized display are
compatible, and why a ratio must not silently be declared continuous at
the zero field.

## 2. Comparator theorem, including reconstruction — PROVEN

**Theorem C-GAUSS.** If the named real bosonic field family is Gaussian
after subtraction of its means, then (C3) vanishes for every `n>=3`
and every admitted separated tuple. This holds for arbitrary covariance,
nonzero means, degenerate covariance, positive tempered scalar or tensor
KL measures defining generalized free fields, and every affine linear
rescaling/mixing of the tested generators. For an OS hierarchy satisfying
the REC_LIB/REC_CONT hypotheses, the same statement holds for the
reconstructed Wightman truncated functions. Conversely a nonzero separated
K4 rules out a Gaussian reconstructed named field. The conclusion is
invariant under field-preserving unitary equivalence.

**Finite algebra proof.** Introduce formal commuting source variables
`z1,...,zn` and work modulo `z_i^2=0`; only distinct-subset moments are
needed. A Gaussian family has

    sum_B M_B product_(i in B) z_i
       = exp[sum_i mu_i z_i + sum_(i<j) Cij z_i z_j].           (C6)

Indeed, expanding the exponential assigns each index to a singleton mean
or to a paired covariance, each partition with coefficient one. Taking
the finite formal logarithm gives a polynomial of degree at most two.
Expanding `log(1+x)` gives exactly (C3): a partition with k blocks occurs
`k!` times in the kth power and is multiplied by `(-1)^(k-1)/k`.
Therefore every mixed coefficient of degree n>=3 vanishes. No convergence
of a moment-generating function, positive-definiteness assumption on a
finite covariance matrix, or finite KL mass support was used. If some
covariances vanish, the same polynomial identity applies. A tensor test
is just a finite component sum; the resulting mean and bilinear
covariance can be arbitrary, so the proof is unchanged. Any finite set
of tests in a larger Gaussian family uses only this finite argument.

**Exact OS interface.** Use [REC_LIB §18](REC_LIB.md) with the analytic
producer [REC_CONT §§1,11](REC_CONT.md): normalized S0, component reality,
E1/E2/E3 and the all-order E0' bound

    |S_n(F)| <= alpha (n!)^beta ||F||_(s n),1                (C7)

on the flat spaces, with a single triple `(s,alpha,beta)`. These are
inputs on the actual hierarchy, not consequences of this witness.
REC_CONT provides the matching holomorphic functions on the ordered
forward tubes; REC_LIB gives their tempered boundaries and the fields on
the original OS Hilbert space. It supplies neither the actual YM inputs
nor a mass gap or unique vacuum.

Here is the additional cumulant step, rather than an assertion that
Euclidean non-Gaussianity automatically survives a quotient. Form the
holomorphic version of (C3) from the continued functions `cal W_|B|`
at each ordered subtuple. Every subtuple belongs to its tube because a
sum of future-cone gaps is still a future-cone gap. Each product uses
disjoint variable slots, so its boundary is a tensor product of
distributions, not an undefined coincident product. The finite sum has
the same type of polynomial tube growth.

For a Gaussian Euclidean hierarchy this holomorphic cumulant vanishes
on an open ordered Euclidean slice by (C6) and the matching theorem.
Distributional equality on this interior slice is equality of the
continuous analytic representatives. The slice is totally real of full
real dimension: its directions are obtained by multiplying each time
coordinate by i. Restricting a holomorphic Taylor series to those real
directions proves that all Taylor coefficients vanish. Analytic
uniqueness on the connected tube makes the cumulant identically zero,
and hence its tempered boundary is zero.

In the reverse direction, the boundary-value uniqueness in REC_LIB
§7 (L-BV) identifies the Gaussian Wick products of the reconstructed
two-point function with their analytic continuations. If the reconstructed
field were Gaussian, the continued cumulant and therefore its matching
Euclidean value on our ordered supports would vanish. A nonzero value
in (C4) contradicts this. No arbitrary contact extension of S is used;
REC_LIB §2 shows that contact distributions vanish on E_n and that the
ordered data determine the separated hierarchy. The field-preserving
unitary in §18 preserves these same data.

For the landed finite Cartesian tensor class the matching is
`cal W_n(jx)=C^(tensor n) S_n(x)`, with
`C=direct_sum_r diag(i,1,1,1)^(tensor r)` and the specified reflection J
(REC_LIB §15, REC_CONT (1.1)). Every term of the cumulant has the same
factor `C^(tensor n)`, which is invertible. Thus zero/nonzero is
preserved componentwise with the correct tensor law. For representations
outside that class the Euclidean algebra identity still holds, but this
note does not claim an unavailable reconstruction theorem. An OS theory
is asserted only when its reconstruction hypotheses are met. QED.

**Scope of F2/F3.** This is all Gaussian states on the chosen generators,
not merely a marked covariance subclass or a finite list of masses.
Gaussian mixtures that are not themselves Gaussian are not asserted to
be in F3. Nor is a Wick square declared Gaussian on its own generators.
The free e used next is already a counterexample to that latter claim.

## 3. Exact free-YM leading term — PROVEN at the free scope

### 3.1 Rebuild the normalization and curvature kernel

The normalization agrees with [TSE55 §§2.1,2.4](TSE55.md) and
WITNESS (E10)–(E13); the following fixes the factors without importing a
decimal coefficient. For generators `tr(t^a t^b)=delta_ab/2`, use link
coordinates `U=exp(i sqrt(2N) B^a t^a)`. Expansion of the trace gives

    1-Re tr(U_p)/N = (1/2) sum_a (dB)_p^a^2 + O(B^3).

Thus the Wilson quadratic action is `(u/2) sum_(p,a) (dB)_p^a^2`.
Each unoriented plaquette occurs at four clover corners with both
orientations. Expanding (C1), or distributing its weights, gives the
source quadratic form `sum_(a,p) w_f(p)(dB)_p^a^2`, with
`w_f(p)=(1/4) sum_(x in corners(p)) f(x)` (TSE55 §2.1).
In the continuum, after `B=A/sqrt(u)`, this is

    q_u(x) = (1/u) sum_(a=1)^d sum_(I=mu<nu) :F_I^a(x)^2:
           = F_(mu nu)^a F_(mu nu)^a/(2u),                  (C8)

where the last expression sums ordered mu,nu and is understood with the
same centring. This is a free reference field, not an identity replacing
the interacting e. Gauge-invariant free curvature can be calculated from
`<A_mu^a(x) A_nu^b(y)>=delta_ab delta_mu,nu/(4 pi^2 |x-y|^2)`;
longitudinal gauge terms cancel under the exterior derivatives.

Put `s=|z|^2`, `H(z)=I-2zz^T/s`, `J(z)=Lambda^2 H(z)`, with the six
unordered two-form components in an orthonormal basis. Differentiating
`D(z)=1/(4pi^2 s)` gives

    pi^2 partial_mu partial_rho D
           = -delta_mu,rho/(2s^2) + 2 z_mu z_rho/s^3,
    G_(mu nu,rho sigma)(z)
           = -delta_nu,sigma partial_mu partial_rho D
             +delta_nu,rho partial_mu partial_sigma D
             +delta_mu,sigma partial_nu partial_rho D
             -delta_mu,rho partial_nu partial_sigma D
           = J_(mu nu,rho sigma)(z)/(pi^2 |z|^4).          (C9)

The last equality follows by expanding the two-by-two minors of H;
the terms quartic in z cancel. H is a reflection, so J is orthogonal,
symmetric and even in z. Consequently

    tr[G(z)G(-z)] = 6/(pi^4 |z|^8),
    K2^q(x,y) = 12 d/(pi^4 u^2 |x-y|^8).                (C10)

### 3.2 Connected Wick contractions and the failed cubic candidate

At each vertex q there are two curvature legs. Normal ordering removes
self-pairings. A connected pairing of n>=3 vertices is exactly a single
cycle through all n vertices: every vertex has degree two. For any
undirected cycle each vertex can assign its two labelled legs to its two
neighbours in two ways, giving `2^n` pairings. The edge contractions force
one common colour around the cycle, giving d; summing the two-form
indices gives a matrix trace. For n=2 there are two pairings. Hence

    K3^q = (8d/u^3) tr(G12 G23 G31),
    K4^q = (16d/u^4) [tr(G12 G23 G34 G41)
                      +tr(G12 G24 G43 G31)
                      +tr(G13 G32 G24 G41)].              (C11)

One may also obtain the cycles by expanding the finite-dimensional
Gaussian integral `log E exp(sum_i z_i X^T W_i X)
= -(1/2) tr log(I-2 C sum_i z_i W_i)` near zero; completing the square
proves this determinant formula. The pairing argument above does not
need a continuum determinant or a trace-class assertion.

The Hodge star on two-forms in Euclidean four-space obeys `star^2=I`.
From its definition by oriented volume and the inner product, an
orthogonal map Q satisfies

    star (Lambda^2 Q) = det(Q) (Lambda^2 Q) star.

To verify the sign, apply Q to the defining wedge product of two
two-forms: their inner product is unchanged and their volume form is
multiplied by det(Q). For the reflection H, det(H)=-1. Therefore star
anticommutes with every G(z). The product of three such matrices also
anticommutes with star, and cyclicity of the finite trace gives

    tr(G12 G23 G31)
      = tr(star G12 G23 G31 star) = -tr(G12 G23 G31) = 0. (C12)

This proves vanishing at every three distinct points and for all our
separated smears. The proposed **nonzero free n=3 leading coefficient
fails**. Interactions may supply a nonzero three-point function, but that
would need a different leading calculation and matching estimate.

### 3.3 Four-point coefficient and genuine smooth tests

At the four centres (C2), every displacement is along the time axis.
Then `J0=diag(-1,-1,-1,1,1,1)`, `J0^4=I`. The three inverse fourth-power
edge products are `1/81`, `1/256`, `1/20736`. Equation (C11) gives exactly

    K4^q(lambda c1,...,lambda c4)
      = [96d/(pi^8 u^4 lambda^16)] (1/81+1/256+1/20736)
      = 169d/(108 pi^8 u^4 lambda^16).                    (C13)

The point two-point coefficient for c2,c3 is `12d/(pi^4 u^2 lambda^8)`.
The corresponding point ratio is `169/(15552 d)`. Point values are used
to calculate the kernel, not substituted for smooth Schwinger tests.

Here is the **exact leading coefficient for the fixed smooth tests**.
Write `Gtilde=pi^2 G`, and define the finite, absolutely convergent
integrals

    A = 16 integral product_(i=1)^4 [f_i(x_i) d^4 x_i]
                  sum_(c in {1234,1243,1324})
                        tr product_(edges ij in c) Gtilde(x_i-x_j),
    B0 = 12 integral f2(x) f3(y) |x-y|^(-8) d^4x d^4y,
    A4 = d A/pi^8,                 A2 = d B0/pi^4.         (C14)

These exact integrals, with the explicit normalized bump (C2), are the
coefficient definition; **A is not asserted to equal 169/108 after
smearing**. Homogeneity gives exactly

    lambda^16 K4^q(f_(1,lambda),...,f_(4,lambda)) = A4/u^4,
    lambda^8  K2^q(f_(2,lambda),f_(3,lambda)) = A2/u^2,
    R4^q = A/(d B0^2).                                    (C15)

Both the proof bound below and a finite rational interval calculation
certify

    3/2 < A < 5/3,            11 < B0 < 13,
    3/(338d) < R4^q < 5/(363d).                           (C16)

**A uniform hand bound on the whole support.** For an edge with centre
distance l in {1,2,3}, write `z=+/- l e0 + delta`. Each coordinate of
delta has magnitude at most `2epsilon`, so `|delta|<=4epsilon=1/2500`.
The scalar `a=(l/|z|)^4` satisfies `|a-1|<1/500`, `a<501/500`;
these follow by cross-multiplying `(2500/2501)^4` and `(2500/2499)^4`.
For `v=z/|z|`, the norm difference of the rank-one projections onto v
and e0 is the sine of their angle. It follows that

    ||H(z)-H(e0)|| <= 8epsilon/(l-2epsilon),
    ||J(z)-J0|| <= 16epsilon/(l-2epsilon)
                     <= 8/4999 < 1/600.

The exterior-square bound follows by restricting `H tensor H` to the
antisymmetric subspace and telescoping its two factors. Therefore

    ||l^4 Gtilde(z)-J0||
          < 1/500 + (501/500)(1/600) < 1/250.

Telescoping a product of four matrices bounds its difference from
`J0^4=I` by `(251/250)^4-1 < 1/60`. Its trace lies between
`6(1-1/60)` and `6(1+1/60)`. Summing the three positive centre edge
weights proves the stronger support-wise bound

    9971/6480 < integrand defining A < 10309/6480.

This lies inside (3/2,5/3). For B0, use
`12(2500/2501)^8 <= 12|x-y|^-8 <= 12(2500/2499)^8`, which lies
inside (11,13). The bumps integrate to one, so these bounds persist
under smearing without computing their normalization integral. The
ratio bounds in (C16) follow by division of positive rational bounds.

**Pre-registered finite check.** [Criteria](checks/cumul_criteria.md)
precede [the exact implementation](checks/cumul_exact.py).
It independently enumerates pairings and contracts the six components,
checks the differentiated and exterior-square kernels, and evaluates
rational interval matrices on the entire product of support cubes.
The exact counts are 2,8,48; the three four-cycle multiplicities are 16.
It checks nonzero means, the zero-covariance case algebraically, and
affine rescaling. Factor/cycle/subtraction controls detect their specified
errors. [All 25 checks passed](checks/cumul_results.json); there was no
floating-point sign or quadrature decision. The rejected nonzero cubic
candidate is explicitly recorded as failed. This is free-field and
finite-algebra evidence, not a numerical YM lower bound.

## 4. Finite moments, the normalized ratio, and N5 — PROVEN

For general means, (C3) is a polynomial in the 15 nonempty-subset moments
of four fixed tests. For the centred family, (C4) uses exactly seven
coordinates: one S4 and six S2's. It is continuous in the finite-moment
topology, and hence along any common sequence on which these coordinates
converge. A lower bound `K4_j>=c>0` passes to the limit. Absolute values
can be used if only `|K4_j|>=c` is supplied, since modulus is continuous.
The support lies in one fixed compact region, and §2 proves the OS
transfer. These are precisely the finite-moment/local/quotient clauses
of [ASSEMBLY55 N5](ASSEMBLY55.md), consumed by N1F and
[PANEL_P1 §3](PANEL_P1.md). N5's analytic form needs no change.
Its named comparator must explicitly be Gaussian **on e**, as in §2.
This does not silently redefine “all free physical theories.”

For any constant `a!=0` and any deterministic shift, centring or (C3)
gives `K_n[a e+b]=a^n K_n[e]` for n>=2: in the formal logarithm a shift
adds only degree one and rescaling replaces z by az. Consequently
`B -> a^2 B`, `K4 -> a^4 K4`, and (C5) is invariant, including under
negative a. Every rescaled Gaussian with B>0 has R4=0, regardless of its
spectral measure. A Gaussian with B=0, including the zero field or a
deterministic field obtained by a=0, still has K4=0. It cannot equal the
YM data in §5, for which B>0 and K4>0. No `0/0` value is used as a proof.

**Continuity qualification.** R4 is a continuous finite-coordinate
functional on the open domain B>0 and on every stratum B>=b>0. It is
not a globally continuous witness at the zero field. In fact, if a
nonconstant scale-invariant functional were continuous there, scaling
any finite moment tuple by `a->0` would make its value equal to its value
at zero. This contradiction precludes the proposed global extension.
Thus use the globally continuous polynomial K4 for N5 and the ratio for
normalization on the positive-B region. Section 5 supplies both a
positive denominator margin and the polynomial's fixed lower bound.
This is why no weakening or alteration of N5 is required. Ratios alone,
with a denominator allowed to vanish along the cutoff sequence, would
not supply N5.

## 5. Exact Yang–Mills obligations — all OPEN here

These are sufficient obligations on one actual Wilson law, not new
axioms, and are not discharged by the free calculation. The minimal
direct witness input is one fixed tuple with convergent coordinates,
`liminf_j K4_j>0` and `liminf_j B_j>0`. The AF construction below is a
more structured sufficient producer of that input.

**C-ALG (common fields and reconstruction).** Use (C1), the fixed
separated hierarchy, its E(4) action, reflection, permutations and real
structure. Produce the actual YM E0'/E1/E2/E3/(Re)/S0 hypotheses (C7),
with the requisite continuum and lattice-to-continuum observable maps,
and apply REC_LIB/REC_CONT to this same hierarchy. No flowed density,
auxiliary soft noise, moving normalization Z(a), or sharp-time product
is substituted for e. This is WITNESS E-ALG with the now-landed abstract
reconstruction interface stated explicitly. All-order growth and the
actual common YM hierarchy remain inputs.

**C-SEQ/MOM (one sequence and the needed moments).** Choose one sequence
`(K_j,R_j)` with `a_j=L^-K_j ->0`, `R_j ->infinity` for the whole
determining hierarchy and the seven centred coordinates (C4) at the
eventually fixed lambda. Require their convergence to the values of
C-ALG, with uniform test-space extension estimates sufficient to pass
from dense tests to the exact bumps (C2). A concrete sufficient bound
for these orders is a common finite-order distribution seminorm bound
`|S_(n,j)(F)|<=C_n ||F||_(p_n),1` on E_n for n=2,4, together with dense
test convergence; full reconstruction needs the stronger all-order
contract (C7). If means are not subtracted in the chosen hierarchy,
require all 15 moments in (C3) instead.

Bounds alone do not imply the convergence of an unbounded moment from
weak convergence of random variables. This contract asks for the actual
separated moment convergence, not that invalid implication. A route
through probability laws would need the corresponding uniform
integrability separately. No coincident `E e(f)^4` or its continuum
existence is assumed here. Product tests with distinct supports are
enough for the witness; higher-order OS inputs are still necessary for
the existence of the theory. No fresh subsequence is selected for each
term of the cumulant.

**C-TR (the same tuned trajectory).** Fix odd `L>=3`, N and nonzero
`g_ref` in the admissible regime, as in WITNESS E-TR. The actual coupling
at scale `k=K-m` must satisfy, uniformly in K,R,

    0<U_-(m)<=u_k<=U_+(m)<infinity,
    U_-(m)->infinity as m->infinity,  lambda_m=L^-m.       (C17)

WITNESS (E8), with its logarithmic two-sided brackets, is sufficient.
For the sliced free reference below also require its FLOW-pw and K-dec
inputs with their original scopes. No exact one-loop beta coefficient
is imported. AF growth in (C17) alone does **not** imply any composite
four-point matching or lower bound.

**C-4MATCH (connected relative lower matching).** On this law put

    P_(K,R)(m) = lambda_m^16 K4_(K,R)(f_(1,lambda_m),...,f_(4,lambda_m)),
    Q_(K,R)(m) = lambda_m^8 C23_(K,R)(lambda_m).

With the **exact A4 from (C14)**, prove

    |P_(K,R)(m) - A4 u_k^-4|
          <= A4 u_k^-4 [r4(m)+h4(K-m)+v4(R/lambda_m)],     (C18)

where the nonnegative functions on the right tend to zero as their
arguments tend to infinity, uniformly on the stated trajectory. The
bound concerns the actual connected function, with all three
disconnected subtractions and centring already performed. It fixes
both the coefficient and its normalization; an arbitrary multiplicative
constant or an O(1) relative error would not be this estimate.

**C-2MATCH/UP (denominator and other upper inputs).** For the **exact A2
from (C14)** prove the corresponding bound

    |Q_(K,R)(m) - A2 u_k^-2|
          <= A2 u_k^-2 [r2(m)+h2(K-m)+v2(R/lambda_m)].     (C19)

Also give finite uniform bounds on all six `|lambda_m^8 Cij|`, for
example `<=B_ij u_k^-2`, to control the disconnected terms and their
moment limits. Together with (C18), these give

    |lambda_m^16 S4_centred|
       <= [C4 + B12 B34 + B13 B24 + B14 B23] u_k^-4

where C4 bounds the connected coefficient in the domain in question.
The n=2/4 extension and convergence requirements remain C-SEQ/MOM;
these few upper bounds do not replace all-order E0'. A two-point E-TS
bound or PL-1L can help with (C19) for this test pair, but not with
(C18). Uniform absolute upper bounds alone cannot prove its positive
lower bound or the sign of the connected subtraction.

**C-ORIGINAL (producer accounting).** Equations (C18)–(C19) must include
all normalized conditional kernels, terminal terms, background regions,
large-field contributions and source-normalization errors of the original
law, uniformly in volume. The fixed source radius, finite-coupling kernel,
original-law coercivity/tails and any interacting remainder produced by
coordinator lanes may be named inputs only at their stated scopes.
None is claimed here to deliver the required four-source derivative.
This clause is bookkeeping for C-4MATCH/C-2MATCH, not an additional
already-proved theorem.

### 5.1 A precise analogue of PL-1L, and what it would have to control

At a finite regulator let `W_i` be the diagonal plaquette weight matrix
`w_(f_(i,lambda))`, and let `G_run=sum_l mathcal K_l/u_l` be WITNESS's
specified one-colour free curvature model. The leading connected source
derivatives are exactly

    P_run = 16d lambda^16 sum_(c in {1234,1243,1324})
                     Tr(W_c1 G_run W_c2 G_run W_c3 G_run W_c4 G_run),
    Q_run = 2d lambda^8 Tr(W_2 G_run W_3 G_run).             (C20)

These are finite Gaussian quantities, and §3's contraction proof gives
their factors. The new interacting analogue can be stated without an
unproved decomposition of higher cumulants:

    PL-4C: |P_(K,R)-P_run| <= C_err,4 u_k^(-4-theta4),
                     theta4>0, uniformly.                 (C21)

Equivalently, P_(K,R) is `lambda^16` times the mixed four-source
derivative at zero of `log E_(K,R) exp(sum_i z_i O_a(f_i,lambda))`.
At a finite lattice this identity follows by differentiating the
normalized finite Wilson integral. Subtracting deterministic means
does not change the fourth derivative. A usable producer must control
this **connected logarithmic derivative**, including the denominators
and all histories in the original law. The orthogonality that splits
a covariance into WITNESS's D_i does not make a fourth cumulant the
sum of four-insertion slice terms: conditional covariances and conditional
means create mixed terms. No such unproved slice identity is used here.

In addition to (C21), the reference must satisfy

    |P_run - A4 u_k^-4|
       <= C_AF,4 u_k^-5 + A4 u_k^-4 [h4(K-m)+v4(R/lambda)], (C22)

and the two-point analogues with powers 2 and 3. Given separated kernel
bounds, the step from a kernel error to the four-cycle error is elementary:
expand `product_(i=1)^4 (G_i+E_i)-product_i G_i` by telescoping. If each
`G_i=O(u_k^-1)` in the rescaled support norm and `E_i=O(u_k^-2)`, the
sum is O(u_k^-5). The fixed separated supports and finite colour/tensor
sums make the constants finite. LGF's free discretization/torus bounds,
K-dec and FLOW-pw can feed that reference step; the exact hypotheses
and their use for these weights still have to be supplied. They say
nothing about the interacting difference (C21).

Thus source-dependent Gaussian dominance, background covariance control,
the quadratic images with leading factor **one**, running-coupling
identification, terminal control, and summed large-field errors are still
needed. C-4MATCH requires their four-insertion versions and control of
the disconnected cancellations. All those claims remain OPEN; writing
down (C21) is not deriving it. A direct proof of (C18) could bypass this
particular sliced production route.

### 5.2 Fixed-scale conditional conclusion

Choose m_star sufficiently large that r2 and r4 are small. Then choose
fixed depth and radius thresholds so that each bracket in (C18),(C19)
is at most 1/2. This choice precedes the cutoff/volume limit. Set
`lambda_star=L^-m_star` once and for all. On a tail of the one sequence,

    A4/(2u_k^4) <= P_j <= 3A4/(2u_k^4),
    A2/(2u_k^2) <= Q_j <= 3A2/(2u_k^2).                    (C23)

It follows that the actual, unscaled, fixed-test cumulant obeys

    K4_j >= c = lambda_star^-16 A4/[2 U_+(m_star)^4] > 0,
    B_j  >= b = lambda_star^-8 A2/[2 U_+(m_star)^2] > 0.   (C24)

The corresponding finite upper bound for B uses U_- and the upper half
of (C23). Since the same u_k appears in numerator and denominator,

    R4_j = P_j/Q_j^2 >= 2 A4/(9 A2^2)
                            > 1/[507 (N^2-1)].           (C25)

C-SEQ/MOM passes (C24) and (C25) to the reconstructed field. By §2 it
is not Gaussian and not an elementary generalized free field. N1F can
consume the continuous polynomial witness in (C24) without modifying
N5. N is fixed: (C25) is not a bound uniform in N->infinity.

There is no `m=m_j->infinity` witness, no moving supports in the final
limit and no infinite list of moments in W. The AF hierarchy is a
sufficient way to locate one fixed scale, not the definition of W.
Discarding a finite prefix of the one sequence changes none of its
limits. This proves the stated conditional implication and no YM input.

## 6. Relation to NG-ax and comparison with WITNESS

**Source availability.** The mandated grep of
`../ym4d-existence/E/EXISTENCE.md` failed because that file is absent in
this supplied workspace. Targeted filename searches in the lane copies
and plausible project roots did not recover it. This is recorded in
[the log](CUMUL_LOG.md), not replaced by a claim to have read the file.

The available [HINT55 §5 and §6 table](HINT55.md), lines 417 and 434,
reports NG-ax's decimal `0.012827 N(N^2-1)g^4` as a tree-level lattice
corner one-point observable with an `f^{abc}`-odd structure, tested
against sign-symmetric/axial Gaussian laws. It explicitly describes the
decimal as float sums not reverified there, and warns about soft-kernel
noise and its comparator class. This is an indirect report, not a
verified value or theorem imported into CUMUL. Its numeric coefficient,
precise coupling dictionary and actual source formula cannot be
certified from the missing primary source and remain unverified here.

The present leading term is rebuilt in §§3.1–3.3. It is a **connected
four-point function of the composite e**, not the reported odd corner
one-point function. In the fixed WITNESS coupling convention it is
proportional to `(N^2-1) g_FLOW^8`; only one colour loop survives the
Gaussian contractions. The reported object has a different colour
factor and coupling power. There is no valid substitution of its
decimal for A4, and its null class does not supply C-GAUSS. The relevant
common lesson is the need for a remainder small relative to a correctly
identified leading coefficient; that resemblance is not a proof of
either matching estimate. The failed scalar three-point candidate
(C12) also cannot be rescued by citing that different cubic observable.

| Obligation | WITNESS AF-e / E-TS route | Present CUMUL route |
|---|---|---|
| Comparator proved | Finite canonical Wick class F1 | Every elementary GFF/Gaussian on e, F2/F3 |
| Observable data in final witness | Countable short-distance two-point hierarchy | One fixed four-test tuple; seven centred coordinates |
| N5 finite-moment form | AF-e requires a changed witness clause | Polynomial K4 fits it unchanged; ratio used on B>0 |
| Common algebra, sequence, actual reconstruction | E-ALG/SEQ and all-order OS inputs | Same requirements, C-ALG/SEQ/MOM |
| Tuning | E-TR and UV brackets | Same trajectory; one sufficiently short fixed scale suffices |
| New dynamical lower estimate | Two-point E-TS; PL-1L is sufficient | Connected four-point C-4MATCH; PL-4C is sufficient |
| Upper/normalization control | Two-point envelope and image normalization | Two-point denominator and all pairings, four-point connected matching and moment control |
| Free composite realizations | F1 exclusion has its stated scope | Not excluded by K4: free Maxwell (C13) is an explicit example |

**Verdict — ARGUED.** This gives a clean conditional F2/F3 non-Gaussianity
criterion with fewer witness/interface requirements: no infinite-scale
functional, no N5 rewrite, no new flowed or time-zero algebra. It has
**not** been shown to require fewer YM estimates. The new connected
four-source matching contains harder cancellation and source-control
requirements than the already-open two-point PL-1L; no implication from
E-TS or PL-1L to C-4MATCH has been proved. F1 and elementary F2/F3 are
different comparator classes, so this comparison is not an ordering of
all non-freeness theorems. Combining separate F1 and elementary-Gaussian
exclusions would still not establish exclusion of every possible
generalized-free-field composite or every Gaussian underlying net.

## 7. Provenance, verification and status boundary

The proof is the printed finite combinatorics, covariance calculation,
support bounds and conditional OS argument. Cumulants/Wick pairing are
classical methods, with credit to Isserlis and Wick. The reconstruction
strategy is credited to Osterwalder and Schrader and to Glaser, with
the exact local library inputs specified in §2. For terminology only,
the primary [Duetsch–Rehren paper, p.2](https://arxiv.org/pdf/math-ph/0209035)
was consulted: it distinguishes Gaussian generalized-free generators
from their composite fields. No literature theorem carries a step of
the argument. Balaban and Dimock are credited for the broader constructive
Yang–Mills program; no bound from their work is silently assumed here.
No result recalled only from memory is used as an input; the unverified
NG-ax report is labelled as such rather than promoted to a proof.

[Source identities](checks/cumul_sources.json), [exact results](checks/cumul_results.json)
and [resource receipt](checks/cumul_run.json) are retained. The serial
check used an exclusive lock, nice 20, all numerical-library thread
counts one, load1 2.085, native free-memory 48%, and combined peak RSS
42,319,872 bytes. No pools, commits, axiom changes, audits, ledger edits,
or changes to existing source files were made.

**Fresh hostile review: LAND, with no binding fixes.** The
[separate-context review](checks/cumul_review.md) re-derived the comparator,
free coefficient, smooth bounds and conditional implication. It is
same-family Codex review, not cross-family review or an audit grade.
Only this provenance paragraph changed after the reviewed scientific
text; final hashes are in [verification](checks/cumul_verification.json).
Full Yang–Mills existence, the interacting lower bound and a mass gap
remain OPEN.
