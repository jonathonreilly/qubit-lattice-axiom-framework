# Empty start at fixed time: expansion in formation intensity

Independent derivation, completed before reading any new author calculation
after the post-seal geometry review. The graph is finite, the initial state
is empty, time t and motion intensity kappa are fixed, and the supplied
generator is L=kappa H+epsilon B. Weights are strictly positive, symmetric
and row-six; proposals in H are fixed and symmetric. B includes its diagonal
holding-rate terms. Let b=BN be the total unscaled birth hazard.

**Result.** The first possible motion correction to E[N_t] is order epsilon^4.
Its full-semigroup coefficient is nonnegative for every t,kappa>=0 and is
increasing and concave in kappa. If the two-record hazard is not constant on
motion classes, it is strictly positive for t,kappa>0. These statements concern
the coefficient, not finite-epsilon monotonicity of the complete expectation.

## Coefficient with the full motion semigroup

Write `<f,g>_m=sum_(N(s)=m) w(s) f(s)g(s)`, an **unnormalized** inner product,
and let H_m be motion restricted to level m. Define

\[
G_2(\kappa,t)=\frac13\int_0^t(t-v)^3
\langle b,(I-e^{\kappa vH_2})b\rangle_2\,dv.
\tag{1}
\]

Then, at fixed finite t and kappa,

\[
E_\kappa[N_t]-E_0[N_t]
=\epsilon^4G_2(\kappa,t)+O(\epsilon^5).
\tag{2}
\]

No small-kappa, short-time, equilibration or rare-event approximation is made
inside (1). E_0 means kappa=0, with the same epsilon and birth rule.

**Proof and factorials.** A Taylor coefficient means the epsilon derivative
divided by its factorial. Duhamel expansion writes its order-r row as

\[
\int_{0<s_1<\cdots<s_r<t}
\delta_0 B P_{s_2-s_1} B\cdots P_{s_r-s_{r-1}}B P_{t-s_r}
\,ds_1\cdots ds_r,\qquad P_v=e^{\kappa vH}.
\tag{3}
\]

The omitted initial P_(s_1) fixes the empty state. The independently checked
identities delta_0 BH=delta_0 B^2H=0, together with P_v N=N, show that the
population coefficients through r=3 are exactly
t^r delta_0 B^rN/r!, independent of kappa.

At r=4, the only surviving semigroup between birth operators is the gap
v=s_4-s_3. Integrating the first two insertion times gives s_3^2/2, and then
integrating s_3 from zero to t-v gives (t-v)^3/6. Therefore the coefficient
difference is

\[
\int_0^t\frac{(t-v)^3}{6}\,
\delta_0B^3(P_v-I)b\,dv.
\tag{4}
\]

The density delta_0B^3/w equals -2b on level two plus a function in ker H.
Detailed balance hence gives
`delta_0B^3(P_v-I)b=2<b,(I-P_v)b>_2`, proving (1).
This uses the complete generator B, not an operator containing only insertion
off-diagonals. The effect can occur on a three-site graph despite there being
at most three actual births.

## Sign, dependence on kappa, and checks of limits

The operator -H_2 is self-adjoint and nonnegative in this inner product.
Choose an orthonormal eigenbasis in this inner product and let c_lambda be
b's coefficient for each
positive eigenvalue lambda, with multiplicities understood. Then

\[
G_2(\kappa,t)=\frac13\sum_{\lambda>0}c_\lambda^2
\int_0^t(t-v)^3(1-e^{-\kappa\lambda v})\,dv.
\tag{5}
\]

Every summand is nonnegative, strictly increasing and strictly concave in
kappa when t>0 and its amplitude is nonzero. Thus G_2 has these strict
properties precisely when H_2b is nonzero. The same conclusion can be read
from the stationary hazard autocorrelation; no count-sector connectivity
assumption is needed.

Let Pi_2 be the weighted projection onto ker H_2, which averages separately
on each actual motion class. Put V_2=||b-Pi_2b||_2^2 and
D_2=-<b,H_2b>_2. Equation (5) also gives

\[
0\le G_2(\kappa,t)\le
\min\left\{\frac{\kappa t^5}{60}D_2,
\frac{t^4}{12}V_2\right\},
\quad
\lim_{\kappa\to\infty}G_2(\kappa,t)=\frac{t^4}{12}V_2.
\tag{6}
\]

At small kappa, G_2=kappa t^5 D_2/60+O(kappa^2), recovering the previously
sealed joint time-Taylor coefficient. The fast-motion limit in (6) is only
a limit of this epsilon coefficient; no uniformity of the remainder in (2)
as kappa tends to infinity is asserted.

## If the epsilon-four coefficient vanishes

The earlier weighted-deletion argument supplies a complete first-actual-order
version. Let m be the smallest occupied level with H_m b nonzero. Necessarily
m>=2. It gave

`delta_0 B^j H=0` for j<=m,

and `delta_0 B^(m+1)/w + m! b 1_(N=m)` lies in ker H. To recall why: the
weighted birth adjoint is Df-bf, where Df sums f over deletions of one record.
D preserves functions constant on motion classes, by pairing deletions across
each vacancy hop; the top level of delta_0 B^m/w is the constant m!.

Repeating (3)--(4) then proves

\[
E_\kappa[N_t]-E_0[N_t]
=\epsilon^{m+2}G_m(\kappa,t)+O(\epsilon^{m+3}),
\]
\[
G_m(\kappa,t)=\frac1{m+1}\int_0^t(t-v)^{m+1}
\langle b,(I-e^{\kappa vH_m})b\rangle_m\,dv.
\tag{7}
\]

This is the first actual nonzero order for t,kappa>0. Its coefficient is
strictly positive, increasing and concave in kappa. With class-centered
variance V_m and Dirichlet energy D_m,

\[
G_m\le\min\left\{
\frac{\kappa t^{m+3}D_m}{(m+1)(m+2)(m+3)},
\frac{t^{m+2}V_m}{(m+1)(m+2)}\right\}.
\tag{8}
\]

If no such m exists, the deletion argument keeps every pure-birth Taylor row
stationary for H; the entire empty-start law is independent of kappa.
The uniform-weight model and complete graphs are examples. For a fixed pair
0<=kappa_1<kappa_2 and t>0, (7) implies a larger expected population at kappa_2
for sufficiently small positive epsilon whenever m exists. This does not
establish the comparison at arbitrary epsilon.

## Exact witness and direct full-generator check

Use the three-site path, unit proposals and W=(3/2,1/2,1). In a fixed ordered
content pair a,b, put g=W_ab and Delta=(W^2)_ab-6. The three position states
have weights (g,1,g), and the hazard differs by Delta at the separated pair.
Its nonconstant symmetric mode has eigenvalue (1+2g)/(1+g) and weighted
variance 2g Delta^2/(1+2g). Summing the six equal and six opposite pairs gives
the exact two-mode expression

\[
G_2(\kappa,t)=\frac13\left[
\frac98 I(8\kappa/5,t)+\frac34 I(4\kappa/3,t)\right],
\tag{9}
\]
\[
I(r,t)=\int_0^t(t-v)^3(1-e^{-rv})dv
=\frac{t^4}{4}-\frac{t^3}{r}+\frac{3t^2}{r^2}
-\frac{6t}{r^3}+\frac{6(1-e^{-rt})}{r^4},\quad r>0,
\]

with I(0,t)=0 by continuity. Here D_2=14/5, V_2=15/8, and
G_2(1,1)=0.03708500612134838642189322865... . Thus the expectation on this
graph has expansion

\[
18t\epsilon-54t^2\epsilon^2+108t^3\epsilon^3
+\left[-\frac{649}{4}t^4+G_2(\kappa,t)\right]\epsilon^4
+O(\epsilon^5).
\tag{10}
\]

The executable check independently constructs all 343 configuration states
and both exact rational generators. It then obtains the epsilon coefficients
by a block-matrix exponential solving
`y'_r=kappa y_r H+y_(r-1)B`, with y_0(0)=delta_0 and y_r(0)=0 for r>0.
This retains the full motion evolution and does not fit finite-epsilon data.
Its first four population coefficients and the difference at order four are
compared with (1), with (9) as an additional exact-form check. The suite also
uses a general positive row-six matrix with unequal edge proposals, uniform
weights, and a complete-graph control.

All 15 block-exponential parameter checks pass; the largest absolute numerical
discrepancy is 5.565e-11 (declared tolerance 2e-8). The generator construction,
pure-birth coefficients, class means, energies and variances use exact rational
arithmetic. Block exponentials and the general spectral checks use floating
arithmetic; the exact two-mode expression and a separate integral quadrature
use 70-digit mpmath arithmetic. Numerical evidence supports the calculation;
the sign and monotonicity proofs are (5) and (7), not the parameter scan.

## Scope, reproduction, and source boundary

For t=0, kappa=0 or epsilon=0 the corresponding difference vanishes. A full
graph with no effective hops is covered by the no-m case. Motion classes,
not assumed count sectors, enter Pi_m. This is a fixed-time epsilon expansion;
setting t proportional to 1/epsilon would invalidate the stated remainder
usage. No fixed-event, infinite-volume or finite-epsilon monotonicity theorem
is inferred. Bounds for a uniform-in-time or uniform-in-volume epsilon
remainder have not been supplied.

Run `python3 check.py > RUN.log` in this directory. `RESULTS.json` records
the complete checks and library versions; `SEAL.json` pins all outputs and
this report. The only model is the previously checked source at commit
`689941783bea870e08458e079ddb208257d0083d`, with original note hashes
`8cc06519d7f3acc088b1e450c151f0870ab21d2987ef2b0224d40ba6a5e7e4e2`
and `423eba32f704e510331bfbb6dba78ea0a35db129854547b155fd76f27248d917`.
The weighted-deletion identities are in the unchanged parent-directory
independent report, SHA-256
`fff040b1b6b3acc5929ab267fe04905bf3aed7d014b4733d615687f97a7bdb84`.
No new primary source or result message was consulted before sealing, and
no file outside this assigned continuation directory was modified.
