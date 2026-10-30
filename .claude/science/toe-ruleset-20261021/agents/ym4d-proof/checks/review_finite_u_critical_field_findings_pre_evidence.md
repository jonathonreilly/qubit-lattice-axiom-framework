# Independent finite-u critical-field checks, frozen before author evidence

This is the reviewer's original analytic reconstruction. At this freeze the
reviewer has not opened `checks/finite_u_critical_field_*`, any PC author
check packet, the PC independent review, or the unfinished chart-boundary
argument. The target source itself was read in full. Statements of prior
review conclusions printed in sources, and a locating-string search in the
old STEP55 review, were not used as proof inputs.

Target: `FINITE_U_CRITICAL_FIELD_ASTRA.md`, 556 lines, SHA256
`ecace773f964a18fe6e5c14d46d38913dc52f95afbd2c8763e4766f0c286377d`.
Observed worktree HEAD: `640788a8a0816ed63f3d8e1abf57137fb0687e89`.
Observed `origin/main` / selected procedure revision:
`01589af3faf806b736c42dc2f3bd625e9edead9f`.

**Frozen mathematical finding: no blocking defect found in the stated bounded
joint-domain critical-field and covariance-extension theorem.** Author-evidence
verification and the final source/receipt check remain to be performed. This
is not a claim about a returned denominator or about physical continuum
existence or mass gap. No numerical experiment was used.

## Actual producer interface

The model is the supplied finite-t Wilson / normalized paired-S4-prime step.
The precise source is `F_epsilon = sigma^2(-log w_0-sum log j_N)+sum epsilon W`,
with `sigma^2=N/u`, fixed real `t=kappa u`, probability Haar, and the original
fine-plaquette sources. Internal tree integration has unit gauge volume and
Jacobian. The free-link count is
`4L^4 T^4-(L^4-1)T^4=(3L^4+1)T^4`; multiplication by `D=N^2-1` retains every
scalar colour, root and harmonic mode. Negative edges use inverses, and the
negative mean is the mean of individual inverse transporters.

CB proves local finite-u criticality; SA13 already proves its original-source
branch on real admitted coarse data, and IC12 proves the source-free branch
on a common complex coarse tube. SA4/FR3's shrinking curvature window is an
integral/contour hypothesis, not a prerequisite for SA13 existence. The
u-stripped tree minimizer has a different Hessian and is not consumed here.
The new substantive interface is their joint original-source/coarse atom
construction at the PC rate, and a small complete-reader critical-Hessian
tail while the positive local lift patches remain unchanged.

## Exact lift force, Hessian and local analyticity

At the lift every actual contour is V_c. Write its first variation as
`V_c X_tau`, with `X_tau` traceless. The two mean derivatives are
`V_c average X_tau` and `-(average X_tau)V_c^-1`. The numerator trace
variation cancels. The normalizer has zero derivative along this common
SL(N,C) tangent: compact Haar invariance gives zero on su(N), complex
linearity gives zero on sl(N,C). Its holomorphic invariance can also be
proved by integrating the invariant vector field along `exp(i s X)`.
Thus the kernel force vanishes separately per mean, including at complex V.
The Haar logarithm is even at zero. Only Wilson forces remain.

For a trace derivative `tr(BP)` with `tr B=0`, replace P by P-I. The coarse
plaquette defect obeys `||P-I||<=delta_*+exp(4eta)-1<=delta_*+8eta` for
`eta<=1/100`. Prefix conjugations cost at most `exp(8eta)`, and
`||P^-1-I||<=exp(4eta)||P-I||`; FU14's `4 sqrt(N) delta_hat` per scalar
insertion safely bounds both trace terms. At exactly flat complex V all
these forces vanish, for arbitrary admitted original sources. This does
not force the source Hessian to vanish.

Independently, put `Q=average theta_tau` and
`B=average ||theta_tau||^2-||Q||^2` in the real second variation. The
numerator contributes `(t/N) average ||theta_tau||^2`. Invariance of the
normalizer on a common group path identifies its variance term and gives
`-(t c_N/N) B`; rescaling by `N/u` yields
`kappa[||Q||^2+(1-c_N)B]`. The Haar expansion
`log j_N(a)=Tr(ad a)^2/24+O(a^4)=-N||a||^2/12+O(a^4)` gives
`N^2/(6u) I`. This recovers the actual CB/FU Hessian rather than the tree
one. The flat-brick recovery controls all free modes; the T=2 extra seam
is omitted only from that filling, not from the model.

The local analytic input is CB9 at real t, not a large-u FK assertion.
The normalizer proof was checked in STEP55 INV/PR/NZ with S5-S7: recenter
so the difference of the two means is scalar, then its residual exponent
is bounded by `epsilon_E s(W)`. The tilted-Haar estimate
`E_t[t s exp(epsilon_E t s)]<=A_N 2^(A_N+1)` gives a uniform zero-free
centered logarithm for small fixed epsilon_E. The uncentered vacuum is
excluded only from derivative bounds and retained in F. The local fine and
coarse Cauchy count is finite; the scalar envelope conversion `vK` in FU5
pays the exchange between sums and coefficient suprema.

## Lift parametrix and complete readers

For every principal compression, weighted conjugation changes both scalar
absolute row and column sums by at most gamma/4. Starting at accretivity
3gamma/4 leaves gamma/2, so an inverse entry is bounded by
`(2/gamma) exp(-m d_1)`. Summing all `n0` coordinates per owner gives the
stated coth fourth-power bound. This does not remove torus multiplicities.

`chi_A K G_A chi_A=chi_A^2` follows by restricting the middle product to A.
Hence `KP=I-Rcal` with `R_A=-[K,chi_A]G_A chi_A`; the sign is negative.
The collar puts any residual endpoint inside A and every reader in S_A.
`G_A>=B^-1 I=2c0 I` on real data implies each entire
`D_A=chi_A(G_A-c0 I)chi_A` is positive. Entrywise independent weakening of
D_A would not preserve this assertion and is not done.

The per-patch residual row is bounded by
`C_chi r0 b_abs g_inv/R`. There are at most 2J nonzero cutoff differences
for each neighbor pair, and at most J final cutoffs in a column. For a mark,
first count at most J patches and at most n_R rows per patch. Thus FU8's
M and B budgets follow without an extensive sum. Since
`beta s_R=1`, p and the numerator of r are independent of R; one may choose
R first. Holding a larger original-block beta fixed would invalidate this
argument, and the source does not do so.

For atom products the union weight is at most the product of weights.
A mark in the left factor uses the right row sum; a mark in the right
factor uses the left column sum. This proves FU9. The exact ordered
inverse is `P(I-Rcal)^-1`, and its j-th nontrivial term has bounds
`p r^j` and `(j+1)n_R p r^j`. Geometric summation gives FU10.
Symmetrizing the individual products preserves both endpoint sums and
full labels, since the exact total is symmetric. With `r<=1/4` and
`pr<=c0/32`, its M norm is at most `c0/24`, stronger than `c0/16`.
The diagonal singleton family contributes `c0 exp(beta)` to M and
`n0 c0 exp(beta)` to B, as paid by FU11.

## Nonlinear atom algebra and joint fixed point

For matrix atoms A and vector atoms h, split a marked union between the A
label and the h label. This gives
`V(Ah)<=B(A) root(h)+M(A) marked(h)<=Q(A)V(h)`.
The root estimate uses M(A). All products meet at a scalar slot and retain
connected full original-reader labels. At finite T one may group the atom
functions by connected supports to obtain a fixed Banach space; positive
absolute majorants still dominate this grouping. Bounded holomorphic
functions on each projected product domain are complete in supremum norm.

The local Taylor expansion is an infinite convergent series. Cauchy gives
`|c_alpha|<=H a^(-|alpha|)` and
`sum_alpha H (t/a)^|alpha|=H(1-t/a)^(-q)=f(t)`.
Differentiating gives the force series; removing constant and linear terms
leaves S(t). A root mark costs S(t), an attached mark costs t S'(t).
For a difference, a mark can be at the root, at the varying attachment, or
at another attachment; the combined majorant is
`2 S'(t)+t S''(t)`, exactly the derivative of `S+tS'`.
The Hessian Q bound costs two root endpoints and one possible attached
mark, giving the `f''` and `t f'''` terms with the factor two for M+B.
The finite counts d1 and d2 overcount all outputs/ordered endpoints.

The exact force is
`g+K a+H_epsilon a+N_0(a)+N_epsilon(a)`.
At a flat background g is zero but H_epsilon is generally not. Dropping
this linear source term would fail the actual stationarity equation.
It is present in FU20. The choices in FU18 are possible since N'(0)=0
and D_H(0,0)=0; rho pays its nonzero source Hessian. After choosing
R and the potentially large A_G, tau and rho can be fixed, then positive
delta_* and eta can pay the force. No parameter depends on u, T or p.
The contraction is at most 1/4 and maps the tau ball into tau/2.
The fixed point has the stated factor-two bound since `(1-1/4)^-1<2`.

The unmarked estimates also contract the ordinary scalar cube; they do
not assign arbitrary fields a small incidence norm. That cube lies in
CB's HS uniqueness ball. This identifies the result with SA13 on real
coarse data and with IC12 at zero source on their shared domain. Iteration
formulas use actual V rather than the reference center, so overlaps agree.
The real Hessian differs from K by at most gamma/4 throughout the cube
and is at least 3gamma/4. This proves only a local coordinate-density
minimum. Subtracting the two source maps and paying `(1-1/4)^-1<2`
reproduces FU23's constant.

The statements replacing delta_hat by a particular real delta_V are
**slice bounds**: evaluate the coarse coefficients at that fixed real V
(and keep the source supremum). They do not replace delta_hat in a
supremum over the entire complex coarse tube. The joint theorem is FU3
with delta_hat. This distinction is necessary for downstream use.

## Critical Hessian and interpolation

Let `Delta=F_epsilon''(a_*)-K`. Its field endpoints remain local; its
coefficient readers include the full substituted a_* atoms. Using principal
compressions of K_* as reader-local patches would be false in general.
The source instead leaves the existing D_A fixed and uses
`(K+Delta)G=I+Delta G`, hence
`K_*^-1=G(I+Delta G)^-1` and `Tcrit=sum_(j>=1)G(-Delta G)^j`.
This checks both the noncommuting order and the alternating sign.

Set `h=d_H m_G` and `b_h=d_H(m_G+b_G)`. The j-th term has endpoint bound
`m_G h^j` and marked bound `b_G h^j+j m_G b_h h^(j-1)`.
Their sums are precisely FU26. In particular
`M(Tcrit)<=m_G^2 d_H/(1-h)<=c0/24<=c0/16`.
The marked sum need only be finite. Symmetrization and every union reader
are preserved; there is no silent replacement by endpoint support.
At flat V, a_*=0 but changing the original Wilson coefficients changes the
Hessian. At curved V and zero source the critical tail need not vanish.

Resolvent subtraction bounds the sum of all local-core changes by c0/8
on the chosen complex tube. Real nonnegative whole-core weakenings leave
`c0 I+sum theta_A D_A(Vbar)>=c0 I`; the two independently weakened tails
cost c0/16 each. Thus `Re C_*>=3c0/4 I`. Absolute endpoint sums also
bound its operator norm by U_*. The exact identity
`Re C_*^-1=C_*^{-*}(Re C_*)C_*^-1` yields
`Re C_*^-1>=alpha_*/U_*^2 I`, with no substitution of PS's gamma.
The actual K_* separately has complex accretivity at least gamma/2.

A full-label spanning tree crossing a partition contains a crossing bond;
its entire matrix atom, including a diagonal entry with remote readers,
vanishes there. The surviving covariance and its original-data dependence
are block diagonal. The principal logarithm on the accretive domain and
the quadratic form split by those blocks, proving the stated normalized
Gaussian endpoint factorization. Normalization follows first on real
positive symmetric matrices and then by holomorphic continuation on the
convex accretive symmetric domain, with precision supplying domination.

## Centering, normalizers and unclosed consumers

For real parameters the original chart integral is
`h_N^n integral_Da exp(-F_epsilon(a)/sigma^2) da`.
Under `a=a_*+sigma x`, Lebesgue measure contributes sigma^d. Separating
`F_epsilon(a_*)`, `x^T K_* x/2`, and the exact remainder gives
`h_N^n (2pi sigma^2)^(d/2) det(K_*)^(-1/2)` times the normalized Gaussian
integral on `(D_a-a_*)/sigma`. This confirms FU30 including the action,
full determinant, Haar density and compact vacuum. The finite-u Haar
Jacobian is already in F and must not be supplied again.

Criticality cancels the global linear term, not each local vertex's force.
The cubic-up Taylor series is asserted only with its common fine-chart
margin. A real translation changes the domain; a complex source requires
a contour chain with its boundaries. The target correctly retains both
facts and does not claim intermediate weakened stationarity.

The PC output rate is only `(16R)^(-4)` in original blocks. Finite-order
coefficient derivatives can spend beta-beta'; they do not prove an
integrated all-order derivative expansion. RD R16 actually asks for a
`mu_0+2` input weight under its own product reference. FR spends its fixed
R-box margin and separately retains `rho delta_V^2/sigma^2` critical action.
These are not supplied by the current covariance theorem. No contour return,
unchanged history interpolation, reference cancellation, original-cut
nonvanishing, effective-level induction, continuum construction or physical
Hamiltonian gap follows from this bounded result. They remain open, without
an impossibility claim.
