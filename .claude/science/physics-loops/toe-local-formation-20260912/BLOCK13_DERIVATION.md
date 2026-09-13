# An elementary positive native Ward scalar certificate

This strengthens Block12 by replacing every inherited scalar interval with
an elementary positive-series bound and replacing the long trial coefficients
with fixed three-decimal rationals. The first prescribed calculation passes:
the author interval is approximately[7.40692,329.05340] in h²alpha units.
It does not use the elliptic oracle, source A-node catalog, or source odd-moment
certificates. Their values informed earlier discovery but are not premises of
this new certificate. Independent source review remains pending.

## 1. Uniform return bound and all scalar suppliers

For X=4 sum_a sin²k_a, the distribution is X=6(1-Z), with
Z=(cos x+cos y+cos z)/3. Its law is symmetric. Let p_(2n)=E Z^(2n).
Equal positive/negative coordinate steps give

    p_(2n)=binom(2n,n) sum_(j=0)^n binom(n,j)²binom(2j,j)/36^n.

For Z>=0, Z^(2n)<=exp[-2n(1-Z)]. On[-pi,pi]^3,
1-Z>=2|x|²/(3pi²), by concavity of sine on[0,pi/2]. Translation by(pi,pi,pi)
exchanges the signs of Z. Twice the positive-part integral is therefore
bounded by the Gaussian integral on R³, giving

    p_(2n)<=3sqrt3 pi^(3/2)/(32 n^(3/2))<n^-3/2, n>=1.

The final strict constant follows from27(22/7)^3<1024 and pi<22/7.
One elementary proof of the latter is the positive integral
integral_0^1 x^4(1-x)^4/(1+x²) dx=22/7-pi, by polynomial division.
Thus for N256 the return tail is at most integral_256^infinity x^-3/2 dx=1/8.
Writing P_N=sum_(n=0)^N p_(2n), monotone convergence gives

    P_N/6 <= A0=E X^-1 <=(P_N+1/8)/6.                   (13.1)

For r=-1,1,3,5,7,9 and a=r/2, the averaged binomial series gives

    L_r=6^a sum_(n>=0) binom(a,2n)p_(2n).               (13.2)

After N256 the coefficients have a fixed sign and decreasing absolute value.
For consecutive even indices their ratio is
(a-m)(a-m-1)/[(m+1)(m+2)], with m even and m>a; its absolute value is less
than1 because a>=-1/2. Consequently the signed tail in(13.2) lies between
zero and binom(a,514)/8. Outward rational square roots enclose the prefactor.
The series interchange is justified by absolute summability: the binomial
coefficients are bounded for each fixed a, and sum p_(2n)<infinity; odd
absolute powers of Z are bounded by the preceding even powers. C0=L_-1.
All needed odd radial moments and inverse moments now have finite rational
certificates from the same fixed return count. The exact even moments are

    M_n=sum_(a+b+c=n) n!/(a!b!c!)
                    binom(2a,a)binom(2b,b)binom(2c,c).

No sampled momentum value is used to bound an infinite scalar.

## 2. Reconstructing the native infinite impurity gap

Set h=1 here. On a finite fully antiperiodic even cubic torus, K is the actual
real skew nearest-neighbor pi-flux matrix, with one-particle frequencies at
most2sqrt3 and no zero frequency. The free Fock Hamiltonian is the quadratic
operator(i/4)gamma^T K gamma with its vacuum energy E0=-Tr|iK|/4 subtracted.
For a two-leg set A take d_j=-K_(0j) on the two chosen neighbors and zero
elsewhere, a=e0, B_A=i gamma(a)gamma(d). This is precisely the bond-reversal
perturbation DeltaK=2(ad^T-da^T), not a new source or a mean-field defect.

Let A_L(s)=<a,(s²-K²)^-1 a> and D_L(s) be the signed opposite-pair entry.
Coordinate symmetry gives s²A_L+6D_L=1. On the center and normalized signed
neighbor sum, the two-by-two resolvent is

    [[s A_L,-sqrt2 D_L],[sqrt2 D_L,s B_L]],
    B_L=A_L for perpendicular pairs, B_L=D_L for opposite pairs.

The matrix determinant lemma therefore gives the exact ratios

    d_O=1-(8/9)(1-z)²,
    d_P=(1+2z)²/9+8s²A_L², z=s²A_L.                    (13.3)

Both are at least1/9. Pairing positive and negative skew frequencies and
integrating log[(s²+b²)/(s²+a²)] gives pi(b-a), hence the finite Fock minimum
relative to the original vacuum is

    DeltaE_(A,L)=-(1/(2pi)) integral_0^infinity log d_(A,L)(s) ds.

There is no omitted vacuum-energy constant or parity division. Restricting a
physical parity sector can only increase this all-parity lower bound.

For each s>0, AP Riemann sums converge to A(s). The following uniform bounds
justify the energy-shift limit without importing a finite inverse-square bound.
Near zero, d>=1/9, d_O<=1 and d_P<=1+8/s², since0<=s²A_L<=1 andA_L<=s^-2.
Thus |log d| is dominated by log9+log(1+8/s²), an integrable function near0.
For s>=4 put u=s², w=1-uA_L. Then0<=w<=6/u and
0<=6/u-w=E[X²/(u(u+X))]<=42/u² (the local moments are6,42 for all sufficiently
large even tori). Expanding (13.3) gives

    |d_P-1|<=168/u²+288/u³<=186/u²,
    |d_O-1|<=32/u².

Because d>=1/9, |log d|<=9|d-1|. These uniform s^-4 bounds supply domination
at infinity. This establishes DeltaE_(A,L)->DeltaE_A with the same integral
and infinite Green entry, independently of the older finite-gap theorem.

It remains to show DeltaE_A>1/4, using elementary inequalities. Cauchy-Schwarz
and EX=6,EX²=42 give1-s²A(s)>=6/(s²+7). The opposite determinant then yields

    DeltaE_O>177/686>1/4,

by keeping g+g²/2 in-log(1-g), g=(8/9)(1-s²A)², and integrating the two
rational functions. The integrals follow from s=sqrt7 tan(theta) and the
cosine-power recurrence; the bound sqrt7<8/3 is rationally checked.

For P, (13.1) supplies A0<=17/60; this loose bound is verified from the same
finite return sum. With a0=17/60 define

    P(y)=1/9+(4a0/9+8a0²)y²+(4a0²/9)y^4, w(y)=1-P(y).

On0<=y<=1, d_P(y)<=P(y)<1. For u=s²>=1/3, monotonicity in A and the
Cauchy-Schwarz bound give d_P<=1-(24-8/u)/(u+7)²<=1. These ranges cover all
s>=0, so every omitted part of the negative logarithm is nonnegative. Retain
12 positive logarithm powers on[0,1] and lower rectangles on[1,20]:

    DeltaE_P >= (7/44) sum_(n=1)^12 (1/n) integral_0^1 w(y)^n dy
      +(7/44) sum_(j=16)^319 (1/16)
            [24-8/(j/16)²]/[((j+1)/16)²+7]² >1/4.       (13.4)

This is a finite rational inequality, since1/(2pi)>7/44. The rectangle
numerator is evaluated at its increasing left endpoint and the denominator
at its increasing right endpoint. No monotonicity of their ratio is assumed.

Finally, for every finite local CAR polynomial O,

    <O Omega_L,D_(A,L) O Omega_L>
       =<O* [H0,O]>_L+<O* B_A O>_L
       >=DeltaE_(A,L)<O*O>_L.

All operators on the right are local, and their Gaussian correlations converge
by bounded AP Riemann sums (the finitely many Dirac nodes have measure zero).
The limiting inequality holds on local polynomial vectors. These form a core:
finite-particle truncations are a core for dGamma(omega), local one-particle
approximations are dense, and the free generator is bounded on each fixed
particle-number sector. B_A is bounded. Closing the form gives D_A>=1/4
in the infinite original-vacuum representation. This route uses neither an
impurity ground vector nor a presumed nonzero overlap of two vacua.

## 3. The bounded Ward scalar and simple rational witness

Define the scalar by the actual bounded native expression

    8alpha=Re[<x,T x>-<x,Tg v>],
    x_A=-D_A^-1 Omega, v_A=D_A^-1 J_A D_A^-1 Omega,
    J_A=2i gamma(d_A), g=gamma(a),

where T is disjoint-pair adjacency on the15 two-leg subsets. Its connection
to the original third-order star Dirac-node coefficient is the separately
identified primary source bridge. The positive scalar theorem itself can be
stated directly for this fully specified bounded expression; no scalar sign
is assumed by that definition.

The square-summable Ward vector w_A=6K^-1d_A exists because (13.1) is finite.
Cubic magnetic symmetry, or the explicit radial table, gives w_A(0)=2 and
w_A dot d_A=0. Thus W_A=gamma(w_A) has[W_A,D_A]=-J_A. Its exact source
norms and covariance table are those derived in Block12, now supplied wholly
by (13.1)-(13.2). The same Clifford recurrence proves its vacuum and W-source
moments through10. They are checked by the different native Fock construction.

Fix the following rationals before any new scalar evaluation:

| Class | p0 | p1 | p2 | q0 | q1 | q2 |
|---|---:|---:|---:|---:|---:|---:|
| P |3091/1000|-663/500|3/20|1973/1000|-487/500|1/8|
| O |707/250|-559/500|117/1000|1719/1000|-97/125|19/200|

They are simply rounded earlier trial coefficients, not newly fitted
physical inputs. For xhat=-p(D)Omega and yhat=-q(D)W Omega, keep the full
vhat=yhat-Wxhat. Use the quartic majorant delta1/4,t4,u8 for each source.
The source moments, trial norms and all90 nominal terms give

    a<1871/200, b<2724/125, E<1473/1000, F<1761/125,
    1345<N<1347.

Here a,b bound the full trial norms and E,F bound their errors, as in Block12.
The exact coarse comparison error6[E(2a+E+b+F)+aF] is1286.244234<1287.
Consequently

    7 < h²alpha < 330.                                  (13.5)

The first sharper enclosure is[7.40692207,329.05339815]. Every scalar supplier
is generated afresh by the elementary N256 series. The rounded p,q are fixed
witness coefficients, not presumed physical values or asserted optimal fits.
No claim about an interacting phase at fixed electric coupling or an
axiom-forcing wall follows.
