# Independent smooth-profile Euler limit for context exchange

## Status and precise theorem

**The stated smooth-profile limit can be proved.** For either supplied
exchange implementation, no extra endpoint-only, one-dimensional, or
unproved local-equilibrium hypothesis is needed. The positive floor on
*all* nearest-neighbor exchanges is crucial to the proof below. A deliberately
crude finite-block Poincare bound suffices; an optimal spectral-gap theorem
is unnecessary.

Let Lambda_N=(Z/NZ)^3, V=N^3, and let H_N be the unscaled context-exchange
generator from `INPUT.md`, with fixed parameters. For N>=4 its rates satisfy

\[
0<\delta\le c_e(\eta)\le C_0<\infty,
\]

uniformly in e,eta,N. One can take delta=K-|u|-2|E| in the linear
implementation, or delta=kappa0 in the positive-part implementation.
Let B_N insert each of the six occupied labels at each vacant site at
unscaled rate one. The following argument covers

\[
L_N=N H_N+\epsilon B_N,\qquad \epsilon\ge0\text{ fixed}.
\tag{1}
\]

Thus epsilon=0 is the requested pure-exchange case, and epsilon>0 is exactly
microscopic per-label birth rate epsilon/N before accelerating time by N.

For six occupied probabilities p=(p_1,...,p_6), write p_0=1-rho,
rho=sum_a p_a, m_i=sum_a p_a f_i(a), and

\[
A=u+2E\rho,\quad B=2E-u-4E\rho,\qquad
J_a^i(p)=p_a[A f_i(a)+B m_i],\quad r_a(p)=\epsilon p_0.
\tag{2}
\]

Suppose a given periodic C^2 solution on [0,T] satisfies

\[
\partial_t p+\sum_{i=1}^3\partial_{X_i}J^i(p)=r(p),
\qquad\min_{t,X,a=0,...,6}p_a(t,X)\ge\alpha>0.
\tag{3}
\]

Let nu_t^N be the product with these seven probabilities at x/N, and let
mu_t^N be the law of (1). If

\[
\mathcal H_N(0):=H(\mu_0^N\mid\nu_0^N)=o(V),
\]

then

\[
\boxed{\sup_{0\le t\le T}\frac{H(\mu_t^N\mid\nu_t^N)}{V}\longrightarrow0.}
\tag{4}
\]

For each occupied label a and smooth periodic test function phi, also

\[
\sup_{t\le T}\left|
\frac1V\sum_x\phi(x/N)\mathbf1_{\eta_t(x)=a}
-\int_{\mathbb T^3}\phi(X)p_a(t,X)\,dX\right|
\longrightarrow0
\tag{5}
\]

in probability. These are conditional theorems with the *assumed* smooth
interior solution as premise. They do not prove global smooth existence,
continuation through shocks, a weak-solution selection principle, a
diffusive correction, or exact microscopic wave eigenmodes.

## 1. The entropy-compatible flux is checked explicitly

The previous sealed calculation proves that every homogeneous product is
exchange-stationary and proves (2). In particular, the uniform seven-state
product pi_N is invariant. This follows from endpoint reversal
c(eta)-c(eta^e)=h_e and the pointwise periodic identity sum_e h_e=0.
Nothing about an inhomogeneous product being exchange-stationary is used.

Use the thermodynamic entropy and its six chemical potentials

\[
s(p)=\sum_{a=0}^6p_a\log p_a,\quad
\lambda_a=\log(p_a/p_0),\quad
S(p)=D^2s(p)=\operatorname{diag}(1/p_a)+p_0^{-1}\mathbf1\mathbf1^T.
\]

The following useful identity holds at every interior p, not just a balanced
one:

\[
S(p)J^i(p)=A f_i+2E m_i\mathbf1
=\nabla_p G_i(p),\qquad G_i(p)=(u+2E\rho)m_i.
\tag{6}
\]

Consequently S D J^i is symmetric. For clarity, its entries are

\[
(S D J^i)_{ab}
=\frac{\delta_{ab}}{p_a}[A f_i(a)+B m_i]
 +2E[f_i(a)+f_i(b)]
 -\frac{(u+4E\rho)m_i}{p_0}.
\tag{7}
\]

The two cancellations needed later are therefore

\[
\partial_t\lambda-Sr
=-\sum_i(DJ^i)^T\partial_i\lambda,
\qquad
\sum_i\partial_i\lambda\cdot J^i(p)=\sum_i\partial_iG_i(p).
\tag{8}
\]

The second expression integrates to zero on the periodic continuum torus.
The entropy flux itself can be written lambda dot J^i-G_i. A real spectrum
at the balanced state alone would not have supplied these nonlinear entropy
identities; (6)-(7) check the load-bearing condition directly.

## 2. A global dissipation budget, including slow births

Put f_t=d mu_t^N/d pi_N and define the unit-swap Dirichlet expression

\[
\mathcal D_N(f)=\sum_{e}\mathbb E_{\pi_N}
[(\sqrt{f(\eta^e)}-\sqrt{f(\eta)})^2].
\tag{9}
\]

Here every unoriented nearest-neighbor edge occurs once. The elementary
inequality

\[
a(\log b-\log a)
\le b-a-(\sqrt b-\sqrt a)^2
\]

and pi_N-invariance of H_N give

\[
\mu H_N\log f\le-\delta\mathcal D_N(f).
\]

For births, the inequality a(log b-log a)<=b-a gives
mu B_N log f <= mu B_N^*1 <= V, with adjoint relative to pi_N: each
occupied site contributes +1 to B_N^*1, each vacancy contributes -6.
Since 0<=H(mu|pi_N)<=V log 7, integration yields

\[
\int_0^T\mathcal D_N(f_t)\,dt
\le\frac{V(\log7+\epsilon T)}{\delta N}.
\tag{10}
\]

This budget does not assume translation invariance, independence, or a
product form for mu_t. The context dependence of c disappears only after
using its uniform lower bound; it has not been silently replaced by an
endpoint-only rate.

## 3. The block replacement is proved for this generator

Take an odd side length ell>=5 and an open cubic block Q_ell of m=ell^3
sites, embedded in the large torus. Let q^ell(x) be its six empirical
occupied probabilities after translating it by x. For direction i, average
the actual local currents

\[
j_a^i(x,\eta)
=c_i(x,\eta)[\mathbf1_{\eta(x)=a}-\mathbf1_{\eta(x+e_i)=a}]
\]

over anchors whose complete four-site support lies inside the block, dividing
by m. Denote this block average by j_bar_a^i. There are
(ell-3)ell^2 such anchors per direction; the omitted boundary fraction is
3/ell. Define the bounded nonnegative discrepancy

\[
\chi_\ell=\sum_{a=1}^6\sum_{i=1}^3
|\overline j_a^i-J_a^i(q^\ell)|.
\]

Three explicit steps give the needed replacement.

**Finite-block mixing comparison.** Every unit adjacent transposition inside
Q_ell is controlled by (9), regardless of the values of the outer context
sites. Neighboring transpositions connect all arrangements with a fixed
seven-component count vector. The conditional uniform measure on each such
sector is denoted gamma_k. A crude, sufficient Poincare constant is

\[
\operatorname{Var}_{\gamma_k}F
\le C_{\rm P}(m)\,\mathcal D_{\gamma_k}(F),
\qquad C_{\rm P}(m)=m^2 7^m.
\tag{11}
\]

Here D_gamma is the unit-swap expression with F in place of sqrt f. To
prove (11), snake a Hamiltonian path through the cubic block and sort the
colors along it using neighboring transpositions. Any two arrangements in
the sector can be joined by at most m^2 swaps. For a sector of M<=7^m
states, expand variance as the average over ordered pairs, erase loops from
the paths, telescope F along them, and apply Cauchy-Schwarz. This gives a constant at most
m^2 M/4 with the convention (9), so (11) is a safe upper bound. Singleton
sectors have zero variance.

If beta is any block law, retain its count-vector probabilities and replace
each conditional law by gamma_k, obtaining beta_can. Applying (11) to the
square root of each conditional density, then Cauchy-Schwarz over sectors,
gives

\[
\|\beta-\beta_{\rm can}\|_{\rm TV}
\le\sqrt{C_{\rm P}(m)\mathcal D_{Q_\ell}(d\beta/d\pi_{Q_\ell})}.
\tag{12}
\]

One uses TV(r gamma,gamma)<=sqrt(Var_gamma sqrt r) for E_gamma r=1.
This is a comparison with unrestricted *unit swaps*, not an assertion that
the actual context generator with an arbitrarily frozen exterior is itself
canonical-stationary.

**Uniform canonical sampling.** Under gamma_k, at most eight distinct sites
can be coupled to independent samples with empirical probabilities q=k/m,
with mismatch probability at most C/m: draw population indices with
replacement and count possible repeated indices. This estimate is uniform
even when some counts vanish. Thus the mean of an interior four-site current
differs from J(q) by O(1/m). Two disjoint current supports have covariance
O(1/m); only O(m) pairs of anchors overlap. Hence the variance of each block
average is O(1/m). Including the omitted boundary anchors,

\[
\sup_k\mathbb E_{\gamma_k}\chi_\ell
\le C(\ell^{-1}+m^{-1/2})\le C/\ell.
\tag{13}
\]

The constants depend on the fixed rate bound and the finite alphabet, not
on k,N,ell. This is the exact place where the independently computed product
current (2) enters the local-equilibrium argument.

**Localizing the dissipation.** Marginalizing a density cannot increase the
swap Dirichlet expression for an edge lying wholly in the block; this is the
reverse triangle inequality for the relevant L^2 norms. Summing over all
translated blocks counts each global edge at most m times. Equations
(10)-(13) therefore imply the explicit integrated replacement bound

\[
\frac1V\sum_x\int_0^T\mathbb E_{\mu_t^N}
\chi_\ell(\tau_x\eta_t)\,dt
\le\frac{CT}{\ell}
 +C\sqrt{\frac{T\,m^3 7^m(\log7+\epsilon T)}{\delta N}}.
\tag{14}
\]

This goes to zero by first taking N to infinity at fixed ell and then ell
to infinity. It also gives an explicit slow diagonal choice: take odd ell
tending to infinity with ell^3<=log N/(2 log 7). No sharp spectral-gap or
one-dimensional hydrodynamic theorem has been imported.

For a smooth bounded weight F(t,x/N), replacing a weighted sum of individual
currents by the weighted block average costs at most
C V(ell/N+1/ell), uniformly in the configuration. This follows by shifting
the summation variable inside the block average. Combining this elementary
spatial averaging with (14) is the correct current replacement. Linear
single-site occupations can likewise be replaced by q^ell, at cost
O(V ell/N).

## 4. Relative-entropy closure

Let psi_t=d nu_t^N/d pi_N. The exchange part of the entropy derivative uses
the *forward* microscopic currents, because exactly

\[
H_N\log\psi_t
=\sum_{x,i}j^i(x,\eta)\cdot
[\lambda(t,(x+e_i)/N)-\lambda(t,x/N)].
\tag{15}
\]

Also partial_t log psi_t=sum_x(eta_x-p_x) dot partial_t lambda_x, where
eta_x is the six-component occupation vector. For births, a direct
single-site computation gives

\[
\epsilon\frac{B_N^*\nu_t^N}{\nu_t^N}
=\sum_x(\eta_x-p_x)\cdot S(p_x)r(p_x).
\tag{16}
\]

For example, the left contribution is -6epsilon at a vacancy, and
epsilon p_0/p_a at occupied label a. Applying the jump entropy inequality
to the birth term with density d mu/d nu, and to the exchange term with
density d mu/d pi as in Section 2, yields

\[
\begin{split}
\dot{\mathcal H}_N\le&-N\delta\mathcal D_N(f_t)
-\sum_{x,i}\mathbb E_{\mu_t}[j^i(x)]\cdot N\Delta_i\lambda_x\\
&-\sum_x\mathbb E_{\mu_t}[\eta_x-p_x]\cdot
[\partial_t\lambda_x-S(p_x)r(p_x)].
\end{split}
\tag{17}
\]

Zero densities of mu can be handled by the usual positive-density
regularization; nu and pi are strictly positive. Equation (16) cancels the
reference reaction contribution exactly, not by an assumed reaction closure.

Replace N Delta_i lambda by partial_i lambda, at cost O(V/N); perform the
spatial averaging and (14); and use (8). The leading block integrand becomes

\[
-\sum_i\partial_i\lambda\cdot
\{J^i(q^\ell)-DJ^i(p)(q^\ell-p)\}.
\]

Its constant term is -sum_i partial_i G_i(p), whose lattice sum is O(V/N)
by periodicity and a Riemann-sum estimate. Its linear term cancels. The
remaining absolute value is bounded by C|q^ell-p|^2, since the fluxes are
polynomials with bounded second derivatives on the closed simplex. Block
count vectors need not be interior for this last assertion.

Here is a uniform entropy bound for this quadratic term. Under nu_t^N let
p_bar^ell(x) be the mean of q^ell(x). For
Z_x=m|q^ell(x)-p_bar^ell(x)|^2, the bounded-Bernoulli exponential-moment
estimate, componentwise Chernoff bounds, and a six-component union bound give

\[
\nu_t^N(Z_x\ge z)\le12e^{-z/3},\qquad
\mathbb E_{\nu_t^N}e^{Z_x/6}\le13.
\]

Translated blocks can be colored with at most 8m colors so that supports in
each color are disjoint (take N sufficiently larger than ell). Pad with
empty classes to exactly 8m colors and apply Holder's inequality. Independence
inside each color then gives

\[
\log\mathbb E_{\nu_t^N}
\exp\!\left[\frac1{48}\sum_x|q^\ell(x)-\overline p^\ell(x)|^2\right]
\le\frac{V\log13}{8m}.
\]

The entropy inequality and |p_bar^ell(x)-p_x|<=C ell/N imply

\[
\mathbb E_{\mu_t}\sum_x|q^\ell(x)-p_x|^2
\le96\mathcal H_N(t)+\frac{12\log13}{m}V
 +C V(\ell/N)^2.
\tag{18}
\]

All constants are independent of N,ell,t in the stated ranges. Combining
(14),(17),(18), dropping the remaining nonpositive Dirichlet term, and
applying Gronwall gives, for some fixed C_T,

\[
\sup_{t\le T}\frac{\mathcal H_N(t)}V
\le C_T\left[
\frac{\mathcal H_N(0)}V+\frac1\ell+\frac1m
 +\frac\ell N+\left(\frac\ell N\right)^2
 +\sqrt{\frac{m^3 7^m}{N}}\right].
\tag{19}
\]

The constants may depend on the profile, alpha, T, fixed parameters,
delta, and epsilon. The logarithmic block choice after (14) makes every
error vanish. This proves (4); the very poor quantitative block constant
does not weaken the limiting statement.

## 5. Empirical convergence and its topology

Under nu_t^N, a fixed smooth test average has exponentially small
probability of a fixed deviation, uniformly in t. The event form of the
entropy inequality and (4) transfer this concentration to mu_t^N.
This proves convergence at each fixed time, uniformly in the bound on its
failure probability.

To obtain the supremum in (5), the test-average martingale has expected
quadratic variation bounded by

\[
C T\left(\frac1{NV}+\frac{\epsilon}{V}\right).
\]

Indeed an exchange changes the test average by O(1/(NV)) and its total rate
is O(NV); a birth changes it by O(1/V) and has total rate O(epsilon V).
The drift is uniformly bounded for a C^1 test function. Doob's inequality,
a fixed fine time grid, and then refinement of that grid prove uniform-time
convergence. The deterministic target in (3) has the required time
regularity. This is weak macroscopic profile convergence, not pointwise
convergence of a binary single-site occupation to a fractional probability.

## 6. Distinct birth scaling and invalid proof routes

Fixed microscopic birth rate epsilon under the same time acceleration gives
N H_N+N epsilon B_N, not (1). For a balanced homogeneous product with
p_0(0)=v_0 in (0,1), the previously checked exact product flow is

\[
p_0^N(t)=v_0e^{-6N\epsilon t}.
\tag{20}
\]

It tends to zero at every positive Euler time. The finite-reaction profile
would instead have vacancy probability v_s(t)=v_0e^{-6epsilon t}>0.
In this exact example the relative entropy *per site* of the fast-birth law
against that slow-birth product tends to

\[
-\log(1-v_s(t))>0.
\tag{21}
\]

Thus reusing the finite-reaction conclusion at fixed microscopic epsilon
would be false, even with an initially exact homogeneous product. It would
also lose the assumed positive vacancy density for the actual limiting law.

Two other tempting routes are insufficient or false:

- A single fluctuating local current cannot be replaced by its product mean
  inside an absolute value. Already for u=E=0,K=1 and all seven probabilities
  1/7, one species has mean edge current zero but mean absolute edge current
  12/49. The block average in (13)-(14) is necessary.
- A vacancy-only hop floor would not give the block ergodicity used here.
  A completely occupied block has no such swaps. The supplied new generator
  has a floor for exchanges between unequal occupied labels too. The proof
  does not transfer unchanged to the earlier vacancy-only dynamics, nor
  does it assume a frozen-exterior context generator has uniform canonical
  stationary laws.

No failed mathematical route was used to bypass an open estimate. The
context-dependent block replacement has been supplied above. No claim is
made after the smooth solution loses its stated regularity or interior
bound, with an N-dependent vanishing floor, or about optimal errors.

## 7. Independent controls, identities, and source seal

`independent_check.py` is independently written and imports only standard
Python modules and SymPy. `RUN.log` preserves its full output and
`RESULTS.json` preserves the same structured results, byte-for-byte. All
32 focused check groups passed with Python 3.13.5 and SymPy 1.14.0.
The checker verifies (6)-(8)
symbolically for all three axes, all seven single-site cases of (16),
finite-population current sampling, and the exact distinction (20).

The finite mixing controls use an *open comparison block*, not an invalid
period-two torus implementation of the context rate. On a 2 by 2 by 2 cube,
all 20,160 arrangements of two vacancies and one of each occupied label are
connected by adjacent swaps. All 10,080 arrangements of a chosen completely
occupied count vector are likewise connected; restricting to vacancy-only
hops leaves just the initial arrangement reachable. A four-site path checks
all 210 count sectors of its 2,401 seven-color configurations. These examples
can falsify a mistaken sector claim; the arbitrary-block proof is the
sorting argument in (11), not an extrapolation from the examples.

The first checker run was interrupted after an unnecessarily large symbolic
expansion of a redundant linear-cancellation expression. Grouping its
coefficient matrix before introducing arbitrary derivative symbols resolved
the execution problem without changing an identity or premise. The full
traceback is `INTERRUPTED_SYMBOLIC_ATTEMPT.log`; its original source hash and
execution history are recorded in `EXECUTION_NOTES.md`. The final complete
run above includes that same identity. No partial run was counted as a pass.

The only prior mathematical source used is this checker's earlier sealed
independent context-exchange result, whose identities were verified before
this work:

| File in `../independent_context_exchange/` | SHA-256 |
|---|---|
| `INPUT.md` | `f20f6ebd367456ee24667bd3dcd52f30961ecd1673a21ffc996cd297bcbcdd96` |
| `REPORT.md` | `277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713` |
| `independent_check.py` | `f1c5145fdde96ef17b4a85f738d0d31456b5f32944edcc59af6ebe38ebb58404` |
| `PRE_SOURCE_SEAL.json` | `7e924cc17d429c64ceb8e1b626f874dc6386ac2618ec7399af2879dce8f4d5f5` |

No new primary Euler derivation, primary context note, simulation, outcome,
or external literature source was read. The proof uses elementary finite
state comparisons and explicitly derived entropy estimates. The independent
output hashes and these dependency identities are recorded in
`PRE_SOURCE_SEAL.json`. This is a bounded scientific derivation, not a formal
audit or a retained-status decision.
