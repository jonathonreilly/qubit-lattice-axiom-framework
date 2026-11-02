# Explicit lattice Green estimates for the free curvature kernel

Date: 2026-10-29. Author: Codex. Mathematical library rebuild for
`briefs_lgf/AUTHOR_BRIEF_LGF.md`, under `PROCESS_LIGHT.md`.

**Author status: PROVEN**, in the mathematical setting specified below.
Independent review is recorded separately in `checks/lgf_review.md`; author
status is not audit or retained status. No Yang–Mills hypothesis is proved here.
The constants are intentionally very loose. All powers of two below are exact
numerical constants, not fitted values or machine estimates.

## 1. Conventions and theorem

Write |x| for Euclidean norm. On Z^4, let S_j f(x)=f(x+e_j),
∇_j^+=S_j-I, and ∇_j^-=I-S_j^{-1}. Both approximate +∂_j.
For an ordered list α=((j_1,ε_1),...,(j_m,ε_m)), ε_i in {+,-}, set
∇^α=∏∇_{j_i}^{ε_i}, ∂^α=∏∂_{j_i}, and |α|=m. Repeated indices are
allowed. The empty product is the identity. All differences commute.

The positive graph Laplacian is

    Δ=Σ_j(2I-S_j-S_j^{-1})=-Σ_j ∇_j^-∇_j^+
      =8(I-P),       Pf(x)=(1/8)Σ_j[f(x+e_j)+f(x-e_j)].             (1)

On forms, d is the forward exterior derivative and d* its counting-inner-product
adjoint, with one component for each increasingly ordered orientation. Section 8
proves that dd*+d*d acts by (1) on every component. This is exactly the convention
in LINEAR_PACKAGE §1.1 and TSE55 §2.4.

Put B=[-π,π]^4, λ(p)=4Σ_j sin²(p_j/2), and

    G(x)=(2π)^(-4) ∫_B exp(ip·x)/λ(p) dp,
    G_T(x)=T^(-4) Σ_{p∈(2π/T)Z^4 mod 2π, p≠0} exp(ip·x)/λ(p).    (2)

Here T is a positive integer; G_T is periodic and has counting mean zero.
Thus ΔG=δ_0 and ΔG_T=δ_0-T^(-4), exactly, by multiplication in (2).
The integrable singularity at p=0 defines G without a regularization constant.
Let

    Φ(x)=c_4 |x|^(-2),    c_4=1/(4π²),    A=2^1000.               (3)

**Theorem LGF (PROVEN).** For every oriented α with 0≤m=|α|≤2:

    |∇^αG(x)-∂^αΦ(x)| ≤ A |x|^(-3-m),             x∈Z^4, |x|≥1; (4)
    |∇^αG_T(x)-∂^αΦ(x)|
        ≤ A |x|^(-3-m) + A T^(-2-m),              1≤|x|≤T/4.    (5)

The torus representative x in (5) is an integer vector in that Euclidean ball;
differences use the periodic extension, including when their stencils leave the
ball. For T<4 the specified domain is empty. Thus the requested numerical
constants can all be taken to be C_α=C'_α=2^1000. In particular the consumed
order-two bound is A|x|^-5+A T^-4. Orders zero and one have T^-2 and T^-3.

The graph Laplacian has leading symbol |p|², so it has the same c_4 as the
continuum operator -Σ∂_j². The inverse of I-P is eight times G and has coefficient
2/π². No random-walk normalization is silently substituted in (2).

## 2. Gaussian subtraction and the quartic symbol (PROVEN)

Set q=|p|² and h_t(y)=(4πt)^(-2) exp(-|y|²/(4t)). Direct Gaussian integration
gives the Fourier transform exp(-t|p|²). For completeness, in one dimension the
transform I(p) obeys I'(p)=-2tp I(p) by integration by parts, and
I(0)=sqrt(4πt); the Gaussian integral follows by squaring and using polar
coordinates. Taking four products proves the stated normalization. Consequently

    ∫_0^∞ h_t(x)dt=1/(4π²|x|²)=Φ(x),                 x≠0,
    f(x):=∫_1^∞ h_t(x)dt=(1-exp(-|x|²/4))/(4π²|x|²).             (6)

At zero use f(0)=1/(16π²). Substitution u=|x|²/(4t) proves (6). Also
-Σ∂²h_t=-∂_t h_t; the approximate-identity limit of h_t at t↓0 proves
-Σ∂²Φ=δ_0. Equivalently the inward flux is
2c_4 |S^3|=4π²c_4=1, with |S^3|=2π² from the same Gaussian integral.

Define, for p∈B\{0},

    a(p)=Σ_{l∈Z^4} exp(-|p+2πl|²)/|p+2πl|²,
    R(p)=1/λ(p)-a(p),
    a_* = Σ_{l≠0} exp(-4π²|l|²)/(4π²|l|²).                    (7)

These are 2π-periodic. Unfolding the absolutely integrable a into R^4 and
then using (6) proves that its integer Fourier coefficient is f(x).
Thus the coefficient of R is E(x)=G(x)-f(x). The value of R at the single
point zero is irrelevant for this integral; its finite-torus value will be
handled explicitly, not filled in by continuity.

On B, λ≥(4/π²)q≥q/4, since sin u≥2u/π on [0,π/2]. The latter inequality
follows from concavity of sin on that interval. On |p|≤1, Taylor's formula gives

    λ=q-Q_4/12+e_6,  Q_4=Σ_j p_j^4,  |e_6|≤q³/360,
    0≤q-λ≤q²/12,
    |1/λ-1/q-Q_4/(12q²)|≤(11/360)q<q/16.                    (8)

For the last inequality use
1/λ=1/q+(q-λ)/q²+(q-λ)²/(q²λ). This also checks the sign of the quartic
term. The quartic is invariant under signed permutations, has no odd-degree
part, and decomposes as Q_4=q²/2+H_4 with Σ∂²H_4=0:
Σ∂²Q_4=12q and Σ∂²q²=24q. The directional term H_4/(12q²) need not have
a limit at zero. Cubic invariance does **not** cancel that term on a signed
permutation orbit. We retain and bound it in R. The orbit cancellation actually
needed later concerns the Hessian of Φ, not this quartic correction.

## 3. Explicit derivative and cutoff ledger (PROVEN)

This section supplies bounds for eight integrations by parts. Multiindices β
below have n=|β|≤8; constants apply to every choice of indices.

    |∂^βR(p)| ≤ 2^200 |p|^(-n)                  (0<|p|≤1),
    |∂^βR(p)| ≤ 2^200                           (p∈B, |p|≥1/2),
    0≤a_*≤2^200.                                                (9)

Here are explicit bounds proving (9), including the Gaussian aliases.

1. On 0<r=|p|≤1, |∂^β(q-λ)|≤8r^(4-n), and
   |∂^βλ|, |∂^βq|≤16r^(2-n). For n≤3 these follow by Taylor remainder;
   for n≥4 the pure-coordinate sine/cosine derivatives are at most 2 and
   mixed ones vanish. For n=0 use (8).
   Differentiating λ·λ^(-1)=1 inductively gives

       |∂^βλ^(-1)|, |∂^βq^(-1)| ≤4 n!128^n r^(-2-n).

   Indeed, after division by λ≥r²/4 the induction factor is at most
   64Σ_{k=1}^n 1/(k!128^k)<64/127<1. For multiindices the sum over
   |γ|=k of binomial(β,γ) is binomial(n,k). Leibniz applied to
   (q-λ)q^(-1)λ^(-1) therefore bounds its nth derivative by
   128 n!512^n r^(-n)<2^130 r^(-n).
2. (1-exp(-q))/q=∫_0^1 exp(-tq)dt has derivatives at most
   2^100 on |p|≤1. A usable Gaussian bound, also for the aliases, is

       |∂^β exp(-t|y|²)|≤2^100 t^(n/2) exp(-t|y|²/2), n≤8.      (10)

   To verify the numerical bound, the one-coordinate polynomial is
   n!Σ_{b=0}^{floor(n/2)}(-t)^b(-2ty)^(n-2b)/(b!(n-2b)!).
   In four coordinates there are at most 9^4 terms, total factorial factor
   at most 8!, powers of 2 at most 2^8, and
   sup_u |u|^k exp(-|u|²/2)≤8^4 for k≤8 (the k=0 case is 1).
   Their product is less than 2^60, so 2^100 is an upper bound.
3. For p∈B and l≠0, |p+2πl|≥π|l|>3|l|. For t≥1,
   Σ_l exp(-t|p+2πl|²/4)<16. One-dimensional sums are bounded by
   1+2Σ_{k≥1}exp(-9k²/4)<2, using k²≥k and exp(9/4)>4.
   For the aliases with l≠0, split the exponential in (10) into two
   factors with exponent -t|p+2πl|²/4; one supplies exp(-t/16), and
   the other has sum <16. The same bound holds with l=0 included when
   |p|≥1/2. Using exp(-|y|²)/|y|²=∫_1^∞exp(-t|y|²)dt gives

       |∂^β a_alias(p)|≤2^104∫_1^∞t^5 exp(-t/16)dt
                        ≤2^104·5!·16^6<2^137.                  (11)

   This justifies all differentiations and sums. On |p|≥1/2, λ≥1/16,
   its derivatives are ≤16, and the same reciprocal induction gives
   |∂^βλ^(-1)|≤16 n!512^n<2^130. On |p|≤1 combine steps 1–3 and
   R=(q-λ)/(qλ)+(1-exp(-q))/q-a_alias. These imply (9).

Use the following explicit C^12 cutoff (higher smoothness is unnecessary):

    b(s)=1                     for s≤0,
         [25!/(12!)²]∫_s^1 u^12(1-u)^12 du   for 0<s<1,
         0                     for s≥1;
    χ(p)=b((4|p|²-1)/3).

The normalizing integral is (12!)²/25!, as follows by twelve integrations
by parts. Thus χ=1 on |p|≤1/2 and χ=0 on |p|≥1. The coefficient sum of
b' is at most 2^42 (25!/(12!)²<2^30); eight derivatives cost at most
25^8<2^40. Applying the chain rule to a quadratic costs less than 2^60
for derivatives of order ≤8: there are at most 8!·2^8 terms and each
quadratic derivative is at most 4. Hence

    |∂^βχ|≤2^150,             |β|≤8.                          (12)

Let ψ_-=1-χ and ψ_j(p)=χ(2^jp)-χ(2^(j+1)p), j≥0. Then
ψ_-+Σ_{j≥0}ψ_j=1 off zero; ψ_j is supported in ρ/4≤|p|≤ρ,
ρ=2^-j. Put Q_α(p)=∏(exp(ip_j)-1) for forward factors and
∏(1-exp(-ip_j)) for backward factors, in the indicated ordered list.
Leibniz and |exp(iu)-1|≤|u| give, for r≤1,

    |∂^β Q_α(p)|≤2^12 r^(m-n),                 m≤2, n≤8.       (13)

When n>m the negative power only enlarges the elementary bound. From
(9), (12), (13), scaling, and r≥ρ/4, we get

    |∂^β(ψ_j Q_α R)|≤2^600 ρ^(m-n),
    |∂^β(ψ_- Q_α R)|≤2^600.                                  (14)

For transparency, the shell product costs at most
2^159·2^200·2^16·2^12·2^16·3^8<2^600; these factors cover the
cutoff, R, radial conversions, Q_α, and Leibniz. The outer product is
smaller. It is smooth and periodic across the boundary of B, since χ vanishes
there and a, λ, Q_α are periodic.

## 4. Fourier coefficients and periodization of the remainder (PROVEN)

Let r_{j,α}(x) be the integer Fourier coefficient of ψ_j Q_αR, and
r_{-,α} the coefficient of ψ_-Q_αR. The shell volume is at most 16ρ^4.
The L^1 estimate and eight integrations by parts in a coordinate with
|x_i|≥|x|/2 yield

    |r_{j,α}(x)|≤2^640 ρ^(4+m)(1+ρ|x|)^(-8),
    |r_{-,α}(x)|≤2^640 (1+|x|)^(-8).                          (15)

Boundary terms vanish for shell functions because they are compactly supported
and C^8; for the outer function, opposite boundary terms cancel at integer x.
More explicitly the two shell bounds before combining are
2^604ρ^(4+m) and 2^612ρ^(4+m)(ρ|x|)^(-8). Combining them with
1+y≤2max(1,y) proves (15). Eight integrations need only the regularity
already established, not an unspecified smooth cutoff.

Split the dyadic sum at ρ|x|=1. The small-scale geometric sum has ratio
2^(-4-m), and the other has ratio 2^(-4+m), at most 1/4. This gives

    |∇^αE(x)|≤2^700(1+|x|)^(-4-m),                 m≤2.        (16)

For example the sum before replacing |x| by 1+|x| is less than
2^650|x|^(-4-m) for |x|≥1; at zero it is less than 2^642.
The symbol decomposition is L^1-convergent by (14), so its coefficient
sum really equals Q_αR, rather than only an asymptotic expansion.

For any one shell or the outer function F, its coefficients are absolutely
summable by (15). Its Fourier series equals F: convolution with the elementary
product Fejér kernels tends uniformly to the continuous periodic F, while
absolute convergence identifies the same limit with the Fourier series.
(The kernels are the squared geometric sums divided by their lengths; their
integrals are one and their mass outside any fixed neighborhood tends to zero.)
Finite Fourier orthogonality then proves, without an imported periodization
formula,

    T^(-4)Σ_{p∈grid_T} exp(ip·x)F(p)=Σ_{n∈Z^4} r_F(x+nT).     (17)

Define the *continuum* smoothed torus function

    f_T(z)=∫_1^∞[Σ_{n∈Z^4}h_t(z+nT)-T^(-4)]dt
          =T^(-4)Σ_{k∈Z^4\{0}} exp(i2πk·z/T)
                         exp(-|2πk/T|²)/|2πk/T|².             (18)

The heat periodization identity used here follows by integrating its Fourier
coefficients over a cell, unfolding to R^4, and using the Gaussian transform
in §2. Both heat series converge absolutely for t>0. The zero coefficient is
T^-4 and every other coefficient decays exponentially at large t.
At integer z=x, grouping k modulo T in (18) gives the exact relation

    E_T(x):=G_T(x)-f_T(x)
       =T^(-4)Σ_{p∈grid_T, p≠0} exp(ip·x)R(p)-T^(-4)a_*.     (19)

The final term is essential: continuum nonzero modes k=Tl alias to the
discrete zero mode. For m≥1 its difference vanishes; for m=0 it is kept.

We now prove, for T≥4 and |x|≤T/4,

    |∇^α(E_T-E)(x)|≤2^710 T^(-4-m),               m≤2.         (20)

Each F=ψ_jQ_αR vanishes near zero. If ρT<1, its grid contains no nonzero
point of its support (the nearest possible point has norm 2π/T), so its
finite Fourier sum is zero. The error for this shell is just -r_{j,α}(x),
bounded by 2^640ρ^(4+m); summing these shells costs at most
2^641T^(-4-m). For ρT≥1, (17) shows that the error is the sum with n≠0.
Since |x+nT|≥(3/4)T|n| and

    Σ_{n≠0}|n|^-8
      ≤Σ_{k≥1}[(2k+1)^4-(2k-1)^4]k^-8
      ≤80Σ_{k≥1}k^-5≤100,

its absolute value is at most 2^650ρ^(m-4)T^-8.
Sum the geometric sequence down to ρT≥1; the result is at most
2^652T^(-4-m). The outer term is at most 2^650T^-8 and a_*T^-4
at m=0 is at most 2^200T^-4. This proves (20), with ample margin.

This also specifies the otherwise ambiguous order-zero lattice image sum:
sum the absolutely convergent images of each Fourier shell, then sum the
shells, and include the alias zero-mode term in (19). For m≥1, (16) makes
the images of ∇^αE absolutely summable even without shell grouping, and
dominated convergence gives the equivalent ordinary image series.

## 5. Uniform continuum torus bounds, and completion of (4)–(5) (PROVEN)

For ordinary partial derivatives of orders m≤2, direct differentiation of
h_t gives

    |∂^αh_t(y)|≤16 t^(-2-m/2) exp(-|y|²/(8t)).                (21)

The first two polynomial factors are -y_i/(2t) and
y_i y_j/(4t²)-δ_ij/(2t); maximizing a polynomial times a Gaussian proves
(21), including repeated indices. A finite oriented difference of order m
is the integral of ∂^α along m unit intervals with the corresponding forward
or backward translates. If |x|≤T/4 and T≥4, every evaluation point z
has |z|≤T/4+2≤3T/4. Thus, for n≠0, |z+nT|≥T|n|/4.

Subtract (6) from (18), splitting the t integral at T². The image part
for 1≤t≤T² is at most

    16 T^(-2-m) Σ_{n≠0}∫_0^1 s^(-2-m/2)
                                      exp(-|n|²/(128s))ds
       ≤2^41 T^(-2-m).                                        (22)

Here split the exponential into two equal factors. The first is at most
exp(-1/(256s)), and the sum of the second is bounded by
(1+sqrt(256π))^4<33^4<2^21, using the decreasing-Gaussian integral
bound for each one-dimensional sum. Since m≤2, the remaining integral is
at most ∫_0^1 s^-3 exp(-1/(256s))ds≤256²∫_0^∞u exp(-u)du=2^16.
The constant subtraction contributes at most T^-2 at m=0 and zero otherwise.

For t≥T², the nonzero Fourier modes of the periodic heat kernel give a
bound, after integration, of

    T^(-2-m) [(2π)^m/(4π²)]
                 Σ_{k≠0}|k|^(m-2)exp(-4π²|k|²)
       ≤2^10 T^(-2-m).                                        (23)

The sum is less than 16: |k|≥1, m≤2, and the product geometric-Gaussian
bound of §3 applies even more strongly. The infinite heat tail costs at
most 16T^(-2-m) by (21). Equations (22)–(23), including the interval
representations of differences, show

    |∇^α(f_T-f)(x)|≤2^43 T^(-2-m).                            (24)

The bound holds also at x=0; no singular Φ occurs in it. Combining (20)
and (24) gives |∇^α(G_T-G)(x)|≤2^712T^(-2-m).

To compare on the infinite lattice, first take r=|x|≥4. Every stencil
segment then stays at norm at least r/2. Repeated differentiation gives

    |∂^βΦ(y)|≤2^n(n+1)! |y|^(-2-n),                   n≤4.    (25)

For a direct check through the only required orders, the sums of absolute
coefficients of the differentiated expressions in y/|y| and Kronecker deltas
are 1, 2, 10, 72, 696. For example, at order four the all-coordinate term
has coefficient 384, the six one-delta terms have coefficient 48 each,
and the three two-delta terms have coefficient 8 each. Each listed sum is
at most 2^n(n+1)!. We have discarded c_4<1. Taylor along the at most two
unit intervals therefore bounds the difference between ∇^αΦ(x) and
∂^αΦ(x) by 2^20r^(-3-m) (zero if m=0).
Also f-Φ=-∫_0^1h_t dt away from zero. Equation (21), the substitution
u=|y|²/(8t), and u^a≤1+u² for 0≤a≤1 show, for |y|≥2,

    |∂^α(f-Φ)(y)|≤2^30 |y|^(-4-m),                 m≤2.       (26)

For example, after substitution the remaining tail is bounded by
exp(-|y|²/16)∫_0^∞(1+u²)exp(-u/2)du=18exp(-|y|²/16);
use |y|²exp(-|y|²/16)≤16. This is far below the stated constant.
Together (16), (25), (26) prove (4) at r≥4 with constant 2^800.

For 1≤r<4, avoid differentiating Φ across zero. From (2),
|G(x)|≤G(0)<2^12: use λ≥|p|²/4, contain B in the ball of radius 8,
and integrate 4|p|^-2 in polar coordinates (even discarding the Fourier
normalization gives less than 2^12). Hence |∇^αG(x)|<2^14,
while |∂^αΦ(x)|≤2^10. Multiplying by r^(3+m)≤4^5 gives a bound
less than 2^25. This handles all origin-crossing stencils. Increasing
2^800 to A=2^1000 proves (4), and (24), (20) then prove (5) with the
same A for its two separate summands.

## 6. The image orbits and the zero-mode quadratic (PROVEN)

This section makes precise the cancellation sketched in TSE55. Define the
zero-mean *continuum* torus Green distribution, smooth away from its source, by

    K_T(z)=∫_0^∞[Σ_{n∈Z^4}h_t(z+nT)-T^-4]dt,
    -Σ∂_j²K_T=Σ_{n∈Z^4}δ_{Tn}-T^-4.                         (27)

For z outside T Z^4 the small-t integral converges by Gaussian decay; the
large-t integral converges by the nonzero-mode representation of §4.
Integrating the heat equation proves (27). Its distributional mean on one
cell is zero, since the heat kernel has integral one at each t. The singularity
|z|^-2 is locally integrable in four dimensions.

Partition Z^4\{0} into finite orbits O under coordinate permutations and
independent sign changes. In any orbit,

    Σ_{n∈O} n_i n_j=(|O|/4)δ_ij |n|²,
    Σ_{n∈O}∂_i∂_jΦ(Tn)=0,                                  (28)

because ∂_i∂_jΦ(y)=c_4[8y_i y_j|y|^-6-2δ_ij|y|^-4].
The odd first and third Taylor terms vanish by inversion. Hence, for |z|<T/2,
the following orbit-grouped series is defined without a conditional ordering
of the orbits:

    S_T(z)=Φ(z)+Σ_O Σ_{n∈O}[Φ(z+Tn)-Φ(Tn)].                  (29)

Indeed, subtract the Taylor polynomial of degree three inside each orbit;
all its terms except the removed constant cancel by (28) and inversion.
Using (25) at order four and |Tn+θz|≥T|n|/2 bounds the remainder by

    2^21 |z|^4 T^-6 Σ_{n≠0}|n|^-6
         ≤2^28 |z|^4 T^-6,                                (30)

since Σ|n|^-6≤80Σ_{k≥1}k^-3≤120<2^7. The analogous estimates for the
first two differentiated series follow by subtracting the corresponding
Taylor polynomials: they are bounded respectively by
2^30|z|³T^-6 and 2^30|z|²T^-6. Third derivatives are ordinarily absolutely
summable, since their tails are bounded by a constant times |n|^-5;
Σ|n|^-5≤80Σk^-2≤160. Thus (29) is C^3 away from zero and termwise
harmonic there. It is invariant under the same signed permutations as K_T.

There is a useful independent way to identify its third derivatives. Direct
differentiation of h_t through order three gives the loose bound
2^20 t^(-2-m/2)exp(-|y|²/(8t)), m≤3, by the same polynomial calculation
as (21). Its integral for m=3 is at most 2^30|y|^-5:
substitute u=|y|²/(8t) and use ∫u^(3/2)exp(-u)du≤∫(1+u²)exp(-u)du=3.
Consequently, at every nonsource z, the integral of the absolute values of
all third-derivative image terms is finite. Fubini, (6), and (27) give

    ∂_i∂_j∂_k K_T(z)=Σ_{n∈Z^4}∂_i∂_j∂_kΦ(z+Tn)
                    =∂_i∂_j∂_k S_T(z).                     (31)

All third derivatives of K_T-S_T vanish on the connected punctured ball.
Its Hessian is therefore constant and the difference is a quadratic polynomial.
Signed-permutation invariance removes its linear part and makes its quadratic
part b|z|². Applying -Σ∂² to the difference in (27) gives -8b=-T^-4.
We have proved the exact local identity

    K_T(z)=S_T(z)+C_T+|z|²/(8T^4),       0<|z|<T/2.           (32)

The sign and coefficient are fixed, not an O(T^-4) ansatz. The polynomial
is a local correction to this image prescription; it is not itself periodic.
Scaling the heat integral shows C_T=T^-2 C_1. An explicit bound is
|C_T|≤2^45T^-2: take z→0 in K_T-Φ, use (24) for f_T-f, and bound the
remaining t∈(0,1) nonzero images by (22), plus the constant T^-4.
This argument gives the bound for T≥4; scaling from T=4 extends it to
every positive real T in the continuum identity.

In particular, differentiating (32) twice adds δ_ij/(4T^4). The image
Hessians at z=0 cancel orbit by orbit, and their displacement remainders are
absolutely bounded as above. This proves precisely why there is no logarithmic
loss from summing a bare |n|^-4 bound. For a forward/backward finite difference
of the polynomial, the result is also δ_ij/(4T^4).

To relate this continuous identity to the lattice without a hidden assertion,
write G=f+E and G_T=f_T+E_T, as in (7), (19). The difference between K_T
and f_T is the explicitly subtracted heat integral on (0,1), and between Φ
and f the same infinite-volume heat integral. Their nonzero images converge
absolutely with all required derivatives. The remaining lattice images are
those of E, governed by (15)–(20); at derivative orders one and two they are
absolutely summable. Thus the continuum orbit prescription, the short heat
integral, the lattice remainder and the alias constant together give a fully
defined lattice periodization. Neither a raw divergent sum of G nor an
unqualified rearrangement of Hessians is used. The discrete operator also
satisfies Δ|x|²=-8, checking the same background polynomial coefficient.

## 7. Full counterexample to the uncorrected order-zero wording (PROVEN)

The assertion refuted here is solely the existence of a finite C, independent
of T, such that |G_T(x)-Φ(x)|≤C|x|^-3 for every 1≤|x|≤T/4.
It is not a claim that the corrected theorem or any Yang–Mills construction
is impossible.

Let a=(5/32)², b=(7/32)² and define a nonnegative C^4 function on R^4 by

    φ(y)=[(|y|²-a)(b-|y|²)]^5   if a<|y|²<b,
          0                    otherwise.                   (33)

It is positive on a nonempty open annulus and supported strictly within
1/8<|y|<1/4. The fifth-order vanishing at each boundary makes its first
four derivatives continuous. Expanding the degree-20 polynomial bounds all
derivatives of orders ≤4 by 2^100 on its support: its coefficient sum is
less than 2^30 and differentiation costs at most 20^4<2^18.
Also 0≤φ≤1. Set φ_T(x)=φ(x/T), periodically extended, and H_T=G_T-Φ
where this test and its nearest neighbors are supported. For T≥64 these
points lie in T/8<|x|<T/4, so no source or periodic boundary is encountered.

Taylor's formula and the continuum harmonicity of Φ give there

    ΔH_T(x)=-T^-4-ΔΦ(x),       |ΔΦ(x)|≤2^50 T^-6,
    |Δφ_T(x)|≤2^102 T^-2.                                    (34)

For the first bound, the centered stencil's second-order term vanishes;
its fourth-order remainder is at most (1/12)Σ_j sup|∂_j^4Φ| along the
unit intervals. Use (25), |x+te_j|≥|x|/2 and |x|≥T/8. This is less
than 2^50T^-6. The second bound follows by integrating the second derivatives
of φ along the centered stencil. Both bounds are uniform in T.

If the uncorrected assertion held, self-adjoint summation by parts would give

    |Σ_x H_T(x)Δφ_T(x)|≤2^115 C T^-1 →0,                     (35)

using |H_T|≤2^9CT^-3 and at most 16T^4 sites. On the other hand (34) gives

    Σ_x φ_T(x)ΔH_T(x)
       =-T^-4Σ_xφ(x/T)+ε_T,       |ε_T|≤2^54 T^-2
       →-∫_{R^4}φ(y)dy<0.                                   (36)

The Riemann-sum convergence follows directly from the bounded first derivatives
in (33), by comparing each cell with its corner; its error is at most
2^111 T^-1 (use at most (4T)^4 cells and coordinate displacement sum 4/T).
Summation by parts is valid even though Φ is not
periodic globally: extend H_T arbitrarily off the support and its neighbor
stencil; both sides use only that common local set. Equations (35) and (36)
contradict equality. This supplies R11's counterexample in full, with an
explicit test function. The corrections T^-2 and T^-3 in (5) are proved by
the independent positive estimates above; they are not inferred solely from
this counterexample.

## 8. Weitzenböck, Feynman gauge, and the exact consumer (PROVEN)

Identify components of a k-form with the increasing-index basis of Λ^kR^4,
based at x. Write ε_j for exterior multiplication by e_j and ι_j for its
adjoint. Their elementary basis action gives

    ε_iι_j+ι_jε_i=δ_ij I,
    ε_iε_j+ε_jε_i=0,           ι_iι_j+ι_jι_i=0.

Since (∇_j^+)*=-∇_j^- and all shifts commute,

    d=Σ_j ε_j∇_j^+,     d*=-Σ_j ι_j∇_j^-,
    dd*+d*d=-Σ_j∇_j^+∇_j^- I=Δ_scalar I.                     (37)

This proves the lattice Weitzenböck step, rather than citing it. The quadratic
Feynman-gauge action on links is
½(||dA||²+||d*A||²)=½<A,Δ_1A>. With the constant harmonic modes removed,
the covariance is the componentwise G_T. Applying d to the Gaussian at both
ends gives dΔ_1^(-1)d*. At a nonzero Fourier mode, d is multiplication by
q∧, q_j=exp(ip_j)-1, its adjoint is contraction by conjugate q, and
|q|²=λ(p). The algebra above shows dΔ_1^(-1)d* is self-adjoint,
idempotent and the identity on im d. At p=0 it is zero. Therefore

    𝔊^F=P_ex=dΔ_1^(-1)d*,                                   (38)

also for the gauge-quotient free curvature law used in TSE55. Gauge directions
and harmonic link modes contribute no curvature. This is a statement about
that explicitly quadratic, one-color law at coupling one.

For plaquettes p=(x,μν), q=(y,ρσ), μ<ν and ρ<σ, let z=x-y be the
difference of their **base points**, as in the lane. Define
H^lat_{ij}(z)=∇_i^+∇_j^-G_T(z). Evaluating (38) gives exactly

    𝔊^F(p,q)=-δ_νσ H^lat_μρ(z)+δ_νρ H^lat_μσ(z)
             +δ_μσ H^lat_νρ(z)-δ_μρ H^lat_νσ(z).             (39)

The minus sign comes from differentiating the y argument. Let

    D_μν,ρσ(z)=-δ_νσ ∂_μ∂_ρΦ(z)+δ_νρ ∂_μ∂_σΦ(z)
               +δ_μσ ∂_ν∂_ρΦ(z)-δ_μρ ∂_ν∂_σΦ(z).           (40)

This is TSE55's -X/(4π²). Applying (5) to the at most four terms of (39)
proves, with r=|z| and 1≤r≤T/4,

    |𝔊^F(p,q)-D_μν,ρσ(z)|≤2^1002 r^-5+2^1002 T^-4.           (41)

Thus the consumer statement, in TSE55's notation, is exactly

> 𝔊^F(p,q) = D_{μν,ρσ}(x_p − x_q) + O(r^{−5}) + O(T^{−4}).

The constants in those two O terms can both be 2^1002, uniformly over
orientations and T. A convention using plaquette centers would incur a bounded
translation and another explicit O(r^-5) term; it is not the convention in
(39)–(41). In physical spacing a, the curvature kernel is multiplied by a^-4,
so the two errors become 2^1002 a|az|^-5 and 2^1002(aT)^-4.

For FREE's use in a squared kernel, |D|≤2^12r^-4 by (25). Squaring
(41) and using r≤T/4 and r≥1 absorbs the error square into a constant times
r^-9+r^-4T^-4 (for example 2^2010 suffices). Thus the precise error
structure used in FREE follows as well. This does not re-prove FREE's separate
test-function Riemann sums or its other hypotheses.

## 9. Consumers and binding wording fixes

Exact quoted text below comes from the local sources identified in LGF_LOG.md.
These are source quotes, not imported mathematical premises.

| Consumer | Exact quote and locator | What this entry supplies |
|---|---|---|
| TSE55 §2.4, LGF, lines 194–201 | “**(LGF) [m], IMPORTED-standard, not re-derived here.**” and “𝔊^F = P_ex = dΔ⁻¹d* (Feynman gauge, Weitzenböck: componentwise scalar Laplacian)” | Equations (1)–(5), (37)–(41) rebuild these steps with explicit conventions and bounds. |
| TSE55 §2.4, Lemma FREE, lines 202–208 | “**Lemma FREE (PROVEN-HERE given (LGF)).**” and “\|𝔊^F² − D²\| ≤ C(r^{−9} + r^{−4}T^{−4})” | The order-two theorem and the last paragraph of §8 supply this scalar-kernel input. |
| CODEX_REVIEW_TSE R9, line 142 | “Thus **Theorem TS's displayed ¼ and 7/4 bounds are CONFIRMED as a CONDITIONAL implication** of its precise weighted error hypothesis, K-dec, FLOW-pw plus the terminal trajectory condition, and the needed LGF estimate.” | LGF is supplied as a mathematical library result; all other listed conditions remain separate. |
| CODEX_REVIEW_TSE R11, lines 158–170 | “The infinite-lattice estimate and the **uniform second-difference torus bound** are imported, not proved by ts55_1 or the tensor identity.” | §§2–6 give the missing proof, including zero frequency and finite differences. |
| CODEX_REVIEW_TSE R11 | “A general torus version needs a **`T^{−2}` correction at order 0** (and the natural order-1 correction is `T^{−3}`), or should be restricted explicitly to the **order-2 estimate actually used by FREE**, with its stated `T^{−4}` correction.” | Equation (5) proves all three corrected forms; §7 proves the uncorrected order-zero form false. |

Binding fixes for a later authorized edit of TSE55 (TSE55 is not edited here):

1. Specify Δ, G and G_T by (1)–(2), the counting mean-zero convention, and
   the oriented finite differences. Retain c_4=1/(4π²); divide a random-walk
   Green function by eight if using that alternative normalization.
2. Replace “the same holds ... with an extra ... T^-4 at |α|=2” by (5),
   or explicitly restrict the torus clause to |α|=2. An order-zero assertion
   without its T^-2 correction is false.
3. Replace the sketch about image cancellation by the exact local identity
   (32) and its prescribed grouping, together with the lattice correction
   (19)–(20). Do not describe a bare unregularized sum of G as convergent.
4. Replace the LGF import pointer and its repeated imported/ARGUED labels
   (including §6.3 and the claim table) with this entry and its actual review
   status. The Weitzenböck and curvature signs are supplied in §8.
5. Keep FREE and TS conditional on their other hypotheses. This entry changes
   neither the interacting measure nor the status of PL-1L or H_int as a whole.

## 10. Residue, provenance, and verification limits

Theorems (4), (5), (32), the counterexample, and (41) are PROVEN in this
note's stated mathematical setting. There is no load-bearing [m] or literature
lemma. Elementary Gaussian integrals, Taylor remainder, Fourier reconstruction,
periodization, and all estimates used have been exhibited here. The constants
are not intended as practical thresholds for FREE. No sharper general rate is
claimed for uncentered differences: their displacement from a derivative at
the base point naturally produces an order r^(-3-m) error.

OPEN outside this entry: the interacting Yang–Mills inputs; consolidation into
the lane's single reviewed proof document; authorized adoption of the binding
TSE55 wording fixes; any independent audit/retained-status decision. No axioms,
audit files, ledger files, prompts, or inherited science files were edited.
Independent review and its exact source identity belong in checks/lgf_review.md.
No numerical experiment or formal proof-assistant check is claimed.

Method credit: Spitzer, *Principles of Random Walk*; Lawler and Limic,
[*Random Walk: A Modern Introduction*, §4.3](https://www.math.uchicago.edu/~lawler/srwbook.pdf);
Uchiyama, [*Green's Functions for Random Walks on Z^N*](https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/greens-functions-for-random-walks-onn/080445758FA185A7BFEFB2B6A2E87C05);
Fukai and Uchiyama, [*Potential kernel for two-dimensional random walk*](https://doi.org/10.1214/aop/1041903213).
These are attribution for Fourier/potential-kernel methods, not proof inputs;
the two-dimensional paper is not asserted to supply a four-dimensional theorem.
The broader gauge-theory lane credits Balaban and Dimock; no result of theirs
is used as an unproved step in this scalar library entry. This file remains a
research-lane artifact, pending the process's separate consolidation stage.
