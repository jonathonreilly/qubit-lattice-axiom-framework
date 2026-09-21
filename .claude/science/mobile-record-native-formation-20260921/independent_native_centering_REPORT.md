# Independent native-formation centering calculation

Date: 2026-09-21. Derived before access to primary centering sources.
Taylor coefficients below are coefficients of powers of j, with no
factorial included.

**Result.** For each finite cubic torus of side N>=4, kappa,beta>0,
0<v0<1 and t>0,

\[
 E_j n_x(t)-\rho(t)=a_{3,N}(t)j^3+O_{N,t}(j^4),\qquad a_{3,N}(t)>0.       \tag{1}
\]

The first two coefficients vanish exactly. For fixed positive t and fixed
parameters,

\[
 N a_{3,N}(t)\longrightarrow
 {8\beta^2v(t)\over\kappa}H(t)\mathcal G>0,                             \tag{2}
\]
\[
 \lambda=6\beta,\quad v(t)=v_0e^{-\lambda t},\quad\rho(t)=1-v(t),
\]
\[
 H(t)=\int_0^t v(s)\rho(s)\,ds
 ={v_0\over\lambda}(1-e^{-\lambda t})
 -{v_0^2\over2\lambda}(1-e^{-2\lambda t}),\qquad
 \mathcal G=90g(0)-9\simeq2.372895443639834.                             \tag{3}
\]

Here g is the Z^3 Green kernel for generator 2 Delta, with
Delta f(x)=sum_{|e|=1}[f(x+e)-f(x)]: its total jump rate is twelve.
The uniform finite-torus hypotheses needed for (2) are proved below.
No uniform Taylor remainder or fixed-nonzero-j fluctuation result is inferred.

## 1. Finite generator and the first two coefficients

The alphabet is vacancy and the six labels with vectors +/-e_i.
Write m_x=v_(eta_x), n_x=|m_x|^2, zeta_x=1-n_x. Every undirected bond swaps
its endpoint states at rate alpha_N=kappa*N, including occupied-occupied
pairs. A vacancy x becomes a at rate

\[
 \beta\prod_{y\sim x}(1+jv_a\cdot m_y).                                \tag{4}
\]

There is no normalization by the sum over labels. All six neighbors are
distinct for N>=4. The initial law is product, with probabilities v0 and
(1-v0)/6. Translation invariance holds at all times.

For fixed N, the generator is a polynomial in j and its finite-time
matrix exponential is entire in j. Thus coefficient extraction and the
finite generator equations commute. This gives the fixed-N remainder in
(1), but provides no N-uniform bound on it.

At j=0 the exact law is product with vacancy v(t). Every homogeneous
product is invariant under constant-rate exchanges, while the uniform
birth generator evolves its marginals independently. That product curve
solves the complete finite forward equation; uniqueness proves the claim.
The same argument does not apply at j!=0.

The identities sum_a v_a=0 and sum_a v_av_a^T=2I give the exact total birth
intensity at x:

\[
 \beta\zeta_x\left[
 6+2j^2\sum_{\{y,z\}\subset\mathcal A_x}m_y\cdot m_z
 +2j^4\sum_{\substack{S\subset\mathcal A_x\\|S|=4}}
                   \sum_i\prod_{y\in S}m_{y,i}
 +2j^6\sum_i\prod_{y\in\mathcal A_x}m_{y,i}\right].                    \tag{5}
\]

A_x is the neighbor set and the pair sum is unordered. By translation
invariance stirring contributes zero to the mean of n_x. All distinct-site
vector products in (5) have zero expectation at j=0. There is no linear
term pointwise and no mean quadratic source. Hence a_(1,N)=a_(2,N)=0.
The cubic term requires a first-order correlation, not a product
substitution for the actual nonzero-j law.

## 2. Exact first-order closure

For distinct sites define

\[
 C_t(y,z)=[j]E_j[m_y(t)\cdot m_z(t)],\qquad
 T_t(x;y,z)=[j]E_j[\zeta_x(t)m_y(t)\cdot m_z(t)].                       \tag{6}
\]

Both coefficients initially vanish. Let H_2 be the unit-rate stirring
generator on an unordered pair of distinct positions: either position
moves to an unselected neighbor, and swapping the two selected positions
does nothing. Let H_3 track a distinguished vacancy-feature position and
an unordered pair of vector-feature positions. When the distinguished
position and a vector position are adjacent, their transposition exchanges
their roles; it is not blocked.

At j=0 births have zero drift on every component of m_y and drift
-lambda*zeta_x on zeta_x. The linear birth coefficient on the vector is

\[
 [j]B_jm_y=2\beta\zeta_y\sum_{w\sim y}m_w.                             \tag{7}
\]

In the j=0 expectation of the pair equation, the birth-at-y term survives
only when w=z; it contributes 2 beta v(t)rho(t) if y~z. The birth-at-z
term is the same. For the triple, its additional distinct vacancy factor
contributes v(t). A term w=x is zero because zeta_x m_x=0. The total
linear birth intensity at x is zero, so it adds no distinguished-site
source. Therefore the exact coefficient equations are

\[
 \partial_t C_t=\alpha_N H_2C_t+
              4\beta v(t)\rho(t){\bf1}_{y\sim z},                    \tag{8}
\]
\[
 \partial_t T_t=(\alpha_N H_3-\lambda)T_t+
              4\beta v(t)^2\rho(t){\bf1}_{y\sim z}.                  \tag{9}
\]

The projection of H_3 onto its two vector positions is exactly H_2,
including when a vector trades places with the distinguished position.
Thus v(t)C_t(y,z), independent of x on the domain of distinct triples,
solves (9), with the correct zero initial condition. Finite linear-ODE
uniqueness proves

\[
 T_t(x;y,z)=v(t)C_t(y,z).                                             \tag{10}
\]

This is an identity of first-order coefficients, not actual independence.
For adjacent y,z, the first time derivative of C at zero is
4 beta v0(1-v0), already exhibiting the non-product response.

Extracting the cubic coefficient in (5) now gives

\[
 a_{3,N}'+\lambda a_{3,N}
   =2\beta v(t)\sum_{\{y,z\}\subset\mathcal A_x}C_t(y,z),\qquad
 a_{3,N}(0)=0.                                                       \tag{11}
\]

No higher-order moment was closed or discarded.

## 3. Relative motion and the exact coefficient

Let Gamma_N be the torus with the origin removed and
A={+/-e_1,+/-e_2,+/-e_3}. Define

\[
 D_N f(r)=2\sum_{e\in\mathcal A:\ r+e\ne0}[f(r+e)-f(r)]               \tag{12}
\]

with coordinates modulo N. This is a symmetric graph walk with rate two
per surviving edge. Either of the two vector positions can produce a
given relative move, explaining the factor two. A transposition of
adjacent selected positions can reverse a labeled relative displacement,
but C_t(r)=C_t(-r), the source is even and so is the solution. Such a
reversal contributes zero. Formula (12) is the correct representation
on the even functions needed here.

Writing P_s^N=exp(sD_N), (8) becomes

\[
 C_t(r)=4\beta\int_0^t v(s)\rho(s)
            (P_{\alpha_N(t-s)}^N{\bf1}_{\mathcal A})(r)\,ds.          \tag{13}
\]

Define the sum over the fifteen unordered pairs of neighbors

\[
 F_N(u)=\sum_{\{y,z\}\subset\mathcal A}
              (P_u^N{\bf1}_{\mathcal A})(z-y).                       \tag{14}
\]

Using exp[-lambda(t-s)]v(s)=v(t) in (11) yields the exact formulas

\[
 \begin{split}
 a_{3,N}(t)
 &=8\beta^2v(t)\int_0^t v(r)\rho(r)
                         \int_0^{t-r}F_N(\kappa Nu)\,du\,dr\\
 &=8\beta^2v(t)\int_0^t F_N(\kappa Nu)H(t-u)\,du. 
 \end{split}                                                        \tag{15}
\]

The punctured torus is connected. From each starting displacement in
(14), its walk can reach A in any positive time with positive probability.
Since v(r)rho(r)>0, (15) is strictly positive for t>0. Thus the cubic
coefficient is the first nonzero coefficient. For fixed N and sufficiently
small nonzero j, the density correction has the sign of j.

There are no triangles for N>=4, so F_N(0)=0. One-step counting gives
F_N'(0)=54 for N>=5 and 60 for N=4. At N=4 an opposite-axis difference
2e_i=-2e_i has an extra route to A. A separate time-normalization check is

\[
 a_{3,N}(t)=
 \begin{cases}80,&N=4,\\72,&N\ge5\end{cases}
 \beta^2\kappa N v_0^2(1-v_0)t^3+O_N(t^4).                            \tag{16}
\]

This short-time expansion is not uniform in N.

## 4. Uniform finite-torus heat-kernel bound

The needed bound, with a constant independent of N>=4, is

\[
 p_s^N(r,q)\le C(s^{-3/2}+N^{-3}),\qquad s>0,                         \tag{17}
\]

also with the trivial upper bound one. The finite-volume term cannot be
discarded when integrating to infinite time at fixed N.

Here is a proof. Use counting-measure norms and energies. The ordinary
full-torus generator 2 Delta has negative eigenvalues
-4 sum_i[1-cos(2pi k_i/N)]. The elementary estimates
1-cos u >= c dist(u,2pi Z)^2 and
sum_{k=0}^{N-1}exp[-c s min(k,N-k)^2/N^2] <= C(1+N/sqrt(s))
give its diagonal heat kernel at most C(s^(-3/2)+N^(-3)).
Cauchy-Schwarz gives the same bound off diagonal. For any full-torus F,

\[
 \|F\|_2^2
 \le C(s^{-3/2}+N^{-3})\|F\|_1^2+sE_{\rm full}(F),\quad
 E_{\rm full}(F)=-\langle F,2\Delta F\rangle.                         \tag{18}
\]

Indeed the first term bounds <F,P_sF>, while
<F,(I-P_s)F> <= s E_full follows from its nonnegative spectral values.
Optimizing s above the threshold
||F||_2^2 >= C N^(-3)||F||_1^2, and using that threshold in the other
case, gives the finite-volume Nash inequality

\[
 \|F\|_2^{10/3}\le
 C[E_{\rm full}(F)+N^{-2}\|F\|_2^2]\|F\|_1^{4/3}.                     \tag{19}
\]

Extend f on Gamma_N by F(0)=sum_{a in A}f(a)/6. Then

\[
 \|F\|_1\le(7/6)\|f\|_1,\qquad
 \|f\|_2^2\le\|F\|_2^2\le(7/6)\|f\|_2^2.
\]

Any two neighbors of the missing origin can be connected avoiding it by
a path of length at most four: perpendicular directions use their
two-step corner, and opposite directions detour through another axis.
These paths exist for every N>=4. The identity

\[
 \sum_{a\in\mathcal A}|f(a)-F(0)|^2
 ={1\over6}\sum_{\{a,b\}\subset\mathcal A}|f(a)-f(b)|^2
\]

and path Cauchy-Schwarz give

\[
 E_{\rm full}(F)\le11 E_N(f),\qquad E_N(f)=-\langle f,D_Nf\rangle.     \tag{20}
\]

For the explicit loose constant, each energy is twice the sum over
undirected edges. Bound every one of the fifteen paths by four times
the sum of squared differences on all punctured edges. The six added
edges then cost at most ten punctured energies. Therefore (19) transfers to

\[
 \|f\|_2^{10/3}\le
 C[E_N(f)+N^{-2}\|f\|_2^2]\|f\|_1^{4/3}.                             \tag{21}
\]

Apply this to f=p_s^N(r,.), whose L1 norm is one. For
z(s)=||p_s^N(r,.)||_2^2, symmetry gives z'=-2E_N(p_s), hence

\[
 z'\le-cz^{5/3}+CN^{-2}z.
\]

Above a constant times N^(-3), this implies z'<=-c' z^(5/3).
The energy also makes z nonincreasing. Integration yields
z(s)<=C(s^(-3/2)+N^(-3)). Since z(s)=p_(2s)^N(r,r), semigroup
Cauchy-Schwarz proves (17). This explicitly verifies the uniform
punctured-torus hypothesis; no imported heat-kernel theorem is required.

## 5. Infinite-volume constant and the growing-torus limit

Let D_infinity be (12) on Z^3 minus {0}. Its bounded jump rates give a
nonexplosive construction. For a fixed bounded time interval, a finite
torus walk starting a bounded distance from the origin couples to it
until a boundary identification is reached. Its jump number is dominated
by a rate-twelve Poisson process, so the probability of at least cN steps
tends to zero. Thus its kernels converge at fixed times. Taking the
limit in (17) gives p_s^infinity(r,q)<=Cs^(-3/2).

For R>=1, (17) gives the decisive uniform tail control

\[
 \int_R^{\kappa Nt}F_N(s)\,ds
 \le CR^{-1/2}+C\kappa t/N^2,                                       \tag{22}
\]

with the integral zero if its upper endpoint is smaller than R.
For bounded small times use F_N<=15. Fixed-time convergence plus (22)
therefore yields

\[
 \int_0^{\kappa Nt}F_N(s)\,ds\longrightarrow
 \mathcal G=\sum_{\{y,z\}\subset\mathcal A}
     E_{z-y}^{\infty}\int_0^\infty{\bf1}_{R_s\in\mathcal A}\,ds.       \tag{23}
\]

The same compact-interval/tail split works with the bounded continuous
weight H(t-s/(kappa N)). Changing variables in (15) gives

\[
 N a_{3,N}(t)={8\beta^2v(t)\over\kappa}
  \int_0^{\kappa Nt}F_N(s)H(t-s/(\kappa N))\,ds
 \longrightarrow {8\beta^2v(t)\over\kappa}H(t)\mathcal G.             \tag{24}
\]

This proves (2) and a_(3,N)=Theta(N^(-1)) at fixed t>0.

To identify Gcal explicitly, use the ordinary Green kernel

\[
 g(r)=\int_0^\infty p_s^{2\Delta}(r,0)\,ds
 ={1\over(2\pi)^3}\int_{[-\pi,\pi]^3}
     {e^{ik\cdot r}\over4\sum_i(1-\cos k_i)}\,dk.                    \tag{25}
\]

The integrand is locally integrable at zero in dimension three.
It follows that g is bounded and tends to zero at infinity by Fourier
approximation (Riemann-Lebesgue), and -2 Delta g=delta_0. Cubic symmetry
gives g(e_i)=g_1 and g(0)-g_1=1/12. Removing the edge to the origin gives

\[
 -D_\infty[6g](r)={\bf1}_{r\in\mathcal A},\qquad r\ne0.              \tag{26}
\]

Dynkin's identity represents the occupation integral through T as
6g(r)-6E_r g(R_T). The last expectation tends to zero: outside a large
finite set g is small, and the infinite-volume heat bound makes the
probability of that finite set tend to zero. Hence the individual
potential in (23) is 6g(z-y).

There are three opposite-axis neighbor pairs and twelve perpendicular
pairs. Put g_2=g(2e_1), g_d=g(e_1+e_2). Harmonicity at e_1 says
6g_1=g(0)+g_2+4g_d. Consequently

\[
 \mathcal G=6(3g_2+12g_d)
 =108g_1-18g(0)=90g(0)-9.                                         \tag{27}
\]

Its positivity follows from (23), independently of any decimal
evaluation. In discrete-time simple-random-walk normalization,
g(0)=G_SRW(0)/12 and Gcal=(15/2)G_SRW(0)-9.

An additional exact finite-volume identity makes the zero mode explicit.
Let g_N be the mean-zero full-torus Green kernel satisfying
-2 Delta g_N=delta_0-N^(-3). On Gamma_N, define

\[
 U_N(r)={6N^3\over N^3-1}
        \left[g_N(r)+{g_N(0)\over N^3-1}\right].
\]

It has zero mean on Gamma_N and

\[
 -D_NU_N={\bf1}_{\mathcal A}-{6\over N^3-1}.                          \tag{28}
\]

Indeed g_N(0)-g_N(e_i)=(1-N^(-3))/12. Thus

\[
 \int_0^S F_N(s)\,ds={90S\over N^3-1}
 +\sum_{\{y,z\}\subset\mathcal A}
      [U_N(z-y)-(P_S^NU_N)(z-y)].                                   \tag{29}
\]

The stationary term is O(N^(-2)) at S=kappa Nt, but diverges as
S tends to infinity with N fixed. This distinguishes (23) from an
incorrect finite-volume uncentered infinite-time Green integral.

## 6. Independent executable checks and provenance

The checker imports no primary implementation. It assembles all
7^4=2,401 states of a four-cycle with the same alphabet, symmetric
exchanges and the product over its two neighbors. This is a degree-two
normalization control, not the three-dimensional target. The complete
generator is Q0+jQ1+j^2Q2, assembled in integer units of 1/6 with beta=1/6
and exchange rate 3/2. All coefficient column sums vanish. At v0=1/2,
exact integer/rational matrix products give

    [j^3 t^3] E n_0(t) = 1/36.

A four-block triangular matrix exponential independently propagates the
first four j coefficients of the full law. At t=0.7 its density coefficients
are

    [0.7517073481042953,
     2.2442984970449942e-17,
     6.1257422745431e-18,
     0.001575877562643943].

The uniform-birth product law agrees to 9.76e-19, and (10), checked on
every distinct triple, agrees to 1.39e-17. For this four-cycle, the
relative walk is a three-site path and the opposite-to-adjacent probability
equals 2(1-exp(-6s))/3. The separately integrated relative ODE and closed
kernel quadrature give respectively 0.0015758775626439465 and
0.001575877562643947 for the same cubic coefficient. Direct physical
generators at +/-j give odd-response ratios approaching it for
j=0.2,0.1,0.05. Finite-time exponentials are floating-point controls,
distinct from the exact rational short-time assertion.

For the actual cubic relative walk, independently assembled sparse
matrices check symmetry, row sums, the N=4 versus N>=5 short-time counts
and the finite Fourier Poisson identity (28). The largest observed
Poisson residual on N=4,5,8 is 4.45e-16.

The ordinary return kernel is [exp(-4s)I_0(4s)]^3. Integrating with s=u^2
and a scaled Bessel function gives g(0)=0.1263655049293315, with a
quadrature error estimate 1.41e-15, and Gcal as in (3). This quadrature
supports the exact integral representation rather than proving it.

For beta=1/6,kappa=1,v0=1/2,t=1, the limit of N*a3 is
0.020172388182670586. Direct relative-ODE computations give:

| N | N*a_(3,N) |
|---|---:|
| 4 | 0.028902260827190884 |
| 6 | 0.018189184246163004 |
| 8 | 0.01579716378511724 |
| 12 | 0.015143352600109142 |
| 16 | 0.015420746903926466 |
| 24 | 0.016084055481088218 |
| 32 | 0.01656825384799962 |

The visible sequence is not monotone, and side 32 is still about 18%
below the limit. The uniform proof establishes (2), not a fitted
finite-size trend. There were no stochastic simulations.

One checker execution completed eleven control groups without assertion
failures. Its full raw log equals RESULTS.json byte for byte. ATTEMPTS.json
records the command and script hash. A separate rejected report-file
patch, caused by a missing Add File plus prefix, is retained in
PATCH_FAILURE.json; it changed no file and no mathematics. There are no
discarded attempts. A dependency-inventory command also stopped before any
read or write because its repository-root parent index was off by one;
BOOKKEEPING_FAILURE.json retains that error and its correction. All
dependency identities subsequently matched. Reproduce from this directory:

    OPENBLAS_NUM_THREADS=1 python3 independent_check.py

## 7. Scope and remaining questions

* The exact finite-N claim concerns Taylor coefficients at j=0.
  The small-j sign is a fixed-N claim. No N-uniform Taylor remainder,
  fixed-j sign, or fixed-j N^(-1) asymptotic has been proved.
* For the zero-mode fluctuation
  Z_N=N^(-3/2)sum_x[n_x-rho(t)], the mean's cubic coefficient equals
  N^(3/2)a_(3,N), asymptotic to the positive constant in (2) times sqrt(N).
  This is a coefficient-level centering effect. It does not justify
  interchanging j differentiation and N limits, settle a fixed-j
  fluctuation law, or establish non-tightness from a first moment alone.
  Translation invariance keeps every nonzero discrete Fourier-mode
  mean zero; this deterministic mean bias is a zero-mode issue.
* Kappa is fixed and positive in (2). At kappa=0 the cubic coefficient
  is zero: the pair source is adjacent, while two neighbors of x are not
  adjacent on these triangle-free tori. Thus (2) is not uniform as
  kappa tends to zero. Higher no-stirring orders are not classified.
* The coefficient vanishes at t=0 and when v0=0 or beta=0. The exact
  formulas also extend to empty initial state v0=1 and give a positive
  coefficient at t>0 with beta,kappa>0, but the stated interior initial
  law suffices. Growing time horizons, other dimensions, and simultaneous
  parameter limits are outside (2).
* The finite-volume stationary mass must be retained, as in (17), (22)
  and (29). A finite-volume infinite-time uncentered Green integral is
  divergent.

Rejected shortcuts include assuming product evolution for j!=0;
inferring an even density function merely because (5) contains even
explicit powers; dropping the distinguished vacancy without checking
its swaps; replacing two-particle relative motion by a rate-one walk;
and applying the N-dependent short-time expansion (16) at fixed t
as N grows. Each would erase a source or change the result.

There is no unresolved proof obligation for the stated cubic coefficient
or its fixed-time three-dimensional asymptotic. A uniform nonzero-j
remainder and the actual fixed-j fluctuation problem remain separate,
unproved questions.

The only previously sealed mathematical report consulted for this task
is the independent native Euler report, SHA-256
dddec2c24051a77ff46e5c333e4a63c269ddb4b1739f60ba8543b8b0fcde023c.
Its product-law warning is consistent with the result, but none of its
Euler or fluctuation claims substitutes for the closure and heat-kernel
proof above. DEPENDENCIES.json records its report/seal/checker and the
process snapshots. PRE_SOURCE_SEAL.json binds all new evidence before
primary-source access. No external theorem, primary centering calculation,
simulation, Git state, audit state, prompt or production source was
imported or modified.
