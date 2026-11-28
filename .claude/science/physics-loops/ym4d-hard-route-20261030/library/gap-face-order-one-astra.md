## Repo search

The lead reports searching main and PRs 10114, 10133, 10134 and 10141.
The target-specific prior digest is absent at
`5c9a2eb894ca6de51d17c7e377043f1672bfa8dd`. The November 8 digest concerns
older RG targets. I checked its nearest transfer hit: a one-step Wilson
witness, not neutral mixing. I also checked row 1084's near hits on main
and PR 10114: SU(3) endpoint energies, a spin-half checkerboard model,
and a Gaussian residual example. Their laws differ from P4. The exact
local P4 inputs leave its neutral sector open. Sources and reuse are
recorded in step 1; no competing target owner was found.

Writer: Codex, GPT-6 family; task-assigned label `gpt-6-astra max`.
The runtime does not expose a more precise model identifier to this writer.
Research text for FINISH row 1110. Not an audit; no scientific status is granted.
This note does not cover a four-dimensional mass gap, GH2 descent, or numerical
verification. No mass gap is claimed. Only this output file is edited; no commit.

### Plan and checkpoint

1. Check repository and Sussman–Alpoge prior work and ownership. Read required inputs.
2. Disintegrate P4 over its plaquette traces. Identify the effective trace law and
   the exact reach of rigid-group charged estimates.
3. Analyze the constraint end and its first finite-volume correction in
   `1/kappa`, with the order of limits stated.
4. Condition on three sheets. Test block stability at fields of order one.
5. Apply every specified negative control. Stop at a proof, a hand
   counterexample, or one precise step with three distinct written failures.
6. Check the text and append one RESULT line, preserving every open dependency.

Current checkpoint: all six planned steps complete. NR remains open after
the three prescribed attempts. Written results: the conditional charged
port (given (3.61)), the finite-volume constraint expansion, and SSB's
counterexample to the universal single-sheet block criterion. No actual
P4 trace counterexample was obtained. The next decision is a neutral
estimate for joint four-sheet blocks or for the constraint law plus
controlled continuation. No independent check has been performed.
Sources: Sussman–Alpoge commit `31a47c543775`, downloaded once each as
`/tmp/sa-gap-face-order-one-astra.UK4PfJ/sa_ym4.tex` and `sa_ca_I.tex`.
Credit for their text: Ethan Sussman and Levent Alpoge, with Claude and Codex as
its authors. Any cited input retains its source's status.

## Step 1. Sources, ownership, and the remaining task

**Reading; no new proof yet.** The November 8 digest is for row 531's RG
obligations. It supplies no P4 mixing result. Its nearest hit,
PR 10114 `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–155`, was fetched and read at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`:
it gives a positive one-step Wilson-loop witness, not decay at arbitrary
distance. Main's `GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_`
`BOUNDED_THEOREM_NOTE_2026-09-07.md:25–40,83–118` concerns a supplied SU(3)
Hamiltonian with endpoint probes, not this Gibbs law. Main was read at
`8b11ae2bb95e641494fe75ed83d108ee712fa3a9`. The lead's broader PR search
is reported in the task; this session did not repeat that entire search.
Row 1084's recorded newer search also found no supplier. Neither search
record is itself a proof of absence.

Its other near hits were opened as well: main's
`docs/HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md:43–90`
specifies spin-half links and checkerboard occupation, not P4; PR 10114's
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/BFT_A.md:1342–1360`
has a Gaussian residual checkerboard example, not coupled spin sheets.
These are scope exclusions, not inputs to any proof below.

The local registry, open-core, and l17c have no `P4-MIX`, `GH2`,
`gap-face-order`, or checkerboard/singlet owner. Their `P4-H-*` entries
concern CA-I's background operators, a different P4. Rows 1109 and 1111
concern GH2 descent and numerical guidance, respectively. Neither owns
this assigned neutral P4 calculation. No duplicate target was found.

Required source ranges read:

- Row 1108, `gap-br2-direction-fable.md`, §§4.2 and 6.3 in full.
- Row 1076, `gap-bridge-vectors-max.md:220–240,350–385`: CB-T,
  P4-ORB, and SING. These constructions are Claude's prior work.
- Row 1053, `gap-wall-vectors-max.md:245–257,300–306`: RIG's proof
  and the explicit unresolved singlet step.
- Row 1084, `gap-checkerboard-singlet-astra.md:49–186,402–607,711–763`:
  source reading, P4-NA, P4-SIGN, P4-LIFT and limits. Those three
  counterexamples are reused, not counted among this row's three attempts.
- Row 1091, `gap-face-stability.md:20–195`: M1, M2, FST-BD's statement
  and entire proof, and its conditional applications. The criterion is
  available; its order-one field hypotheses are not supplied there.
- Row 1077, `gap-face-2d-astra.md:501–521`: the Ising example (16).
- Row 1112, `prior/gap-gauged-sigma-read-luna.md`: a literature reading,
  not a theorem supplying P4. Its negative search result is not upgraded
  to a literature-wide absence claim. No numerical evidence is used.

Sussman–Alpoge: read the index README, searched chunk files and obligations,
then read `chunk-02:81–105`, `obligations:16–31`, and outline
`588–599,2195–2257`. GL3 already gives the positive SU(2) convolution
coefficients. The passage at 588–599 explicitly separates clustering from
a positive mass gap. Searches for P4-MIX, gauge-Higgs, gauged sigma,
principal chiral, four-sheet, and two-dimensional O(4)/O(n) returned no
matching supplier in the downloaded outline, CA-I, or CA-I 4.12–4.19
index. The index's Euclidean O(4) rotation hits are different objects.
No CA-I theorem is imported. This is a bounded search conclusion.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text. The Bessel formula is theirs here; it is not rederived.

**Contract (open).** Write b=beta_M. On a finite free square-lattice
subgraph, or a two-dimensional torus, let q_i(u) belong to K=SU(2)=S^3.
Set

\[
 H_u=q_1(u)q_2(u)q_3(u)^{-1}q_4(u)^{-1},\quad x_u=\operatorname{Re}H_u,
\qquad
 d\mu_{b,\kappa}\propto
 e^{b\sum_{uv}\sum_{i=1}^4\operatorname{Re}(q_i(u)q_i(v)^{-1})
       +\kappa\sum_u x_u}\prod_{u,i}dq_i(u).
\]

Every unoriented longitudinal bond is counted once. Haar measures are
probability measures. Distance d is ambient longitudinal lattice l1
distance, periodic on tori. The first target is
`|Cov(x_u,x_v)| <= C_b exp(-a_b d(u,v))` at kappa=b in [2.3,2.6],
with constants independent of the graph or torus size. A fixed-volume
asymptotic formula does not establish this target. The larger target also
contains multi-site corner singlets, which are not functions of x alone.

Step 1 outcome: prior constructions have been located; all three new routes
remain to be attempted. The named common step will be the estimate for the
actual effective trace law, rather than an association port.

## Step 2. Orbit conditioning and the exact trace law

### 2.1 An orbit lift (argued)

Use P4-ORB as an input. Put `h(t)=t+i sqrt(1-t^2)`, for -1<=t<=1.
At each longitudinal site introduce four independent Haar variables g_j.
The map

\[
 q_1=g_1g_2^{-1},\quad q_2=g_2g_3^{-1},\quad
 q_3=g_4g_3^{-1},\quad q_4=g_1h(t)^{-1}g_4^{-1}                 \tag{O1}
\]

has holonomy `g_1 h(t) g_1^{-1}`. Its image is the entire trace-t orbit.
Its pushforward Haar law is the conditional product-Haar law on that
orbit. Indeed both laws are invariant under the four corner actions.
For a transitive compact-group action, integrating f(gp) over Haar g is
independent of p. Integrating that identity against any invariant
probability proves uniqueness of the invariant probability. This also
defines the endpoint orbit laws at t=+1 and t=-1.

The one-site trace density is

\[
 \rho(t)dt=\frac2\pi\sqrt{1-t^2}\,dt.                         \tag{O2}
\]

To see its normalization and origin, a unit quaternion has polar form
`cos(theta)+n sin(theta)` with n uniform on S^2. The round S^3 volume
element is proportional to `sin^2(theta) dtheta dn`; its theta integral
is pi/2. Substitute t=cos(theta). The holonomy of four independent Haar
variables is Haar, by integrating the last variable first. Thus (O2)
is the required product-Haar disintegration, not an assumed scalar law.

Let S_b(g,t) denote the longitudinal action after (O1), and set

\[
 W_b(t)=\int e^{S_b(g,t)}\prod_{u,j}dg_j(u).
\]

Then the actual marginal and conditional laws are exactly

\[
 d\nu_{b,\kappa}(t)=\frac1{Z_{b,\kappa}}
 W_b(t)\prod_u e^{\kappa t_u}\rho(t_u)dt_u,\qquad
 d\mu(g\mid t)=W_b(t)^{-1}e^{S_b(g,t)}\prod_{u,j}dg_j(u).       \tag{O3}
\]

The conditional law is independent of kappa. W_b is a finite positive
continuous function, but there is no volume-independent locality bound
on its logarithm in (O3). Integrating out g is an operation, not such a
bound. At b=0, W_b=1. At kappa=0 the original four sheets are independent;
their known mixing is a cited boundary case, not a bound for all tilts
`exp(kappa sum t)` of (O3).

### 2.2 Conditional charged decay actually does port (argued, given (3.61))

This uses a nonlinear orbit lift, not the same-terminal auxiliary network
ruled out by P4-LIFT. Fix t and all g-sheets except g_j. Each corner has
two incident transverse edges. On any longitudinal bond, their sum is
of the form

\[
 b\operatorname{Re}\bigl(g_j(u)[U_{uv}+V_{uv}]g_j(v)^{-1}\bigr),
 \qquad U_{uv},V_{uv}\in SU(2).                               \tag{O4}
\]

For an incoming transverse edge, replace its traced quaternion by its
inverse and cycle its factors. This puts g_j in the same order as for
an outgoing edge. Factors h(t), and the other corner variables, enter
U and V only. Every product of unit quaternions has norm one.

Any nonzero quaternion U+V is `|U+V| T` for a unit quaternion T.
Thus (O4) is one right-twisted O(4) bond with strength
`c_uv=b|U+V| <= 2b`. If U+V=0 set c_uv=0 and choose any T.
Conditioning on the other three g-sheets therefore gives exactly the
source's bounded right-twist class, with upper coupling 2b. There is no
on-site field in this conditional law. All factors independent of g_j
cancel from its normalization.

**Cited input and source check.** OpenAI, *Sharp mass bounds for the
two-dimensional O(4) model*, commit
`4eaee87548250b2682affda7d05d947c05554bae`, pp. 13 and 27–29:
(3.61) controls an observable with identically zero average under common
left multiplication. Fixed right twists are allowed. Its coarse collar
and torus-size requirements are retained. Section 3.11 then restricts
arbitrary-observable mixing to the untwisted zero-field ferromagnet.
The PDF was downloaded into the new directory
`/tmp/o4-gap-face-order-one-astra.qxTa9y/` and those pages were extracted
and read. An initial guessed LaTeX URL returned HTTP 404; the PDF succeeded.
This is a source/interface reading, not verification of the whole paper.

For completeness, the deduction from (3.61) is as follows. Suppose F has
zero corner-j average identically, and F and H have separated fixed
supports. In the lifted variables this is zero average under common
left multiplication of g_j on F's support. Choose a coarse-cell region
containing that support, with the source's collar, disjoint from H.
Condition on t, the other three g-sheets everywhere, and g_j outside
this region. H is now fixed. The conditional action inside is (O4),
with the boundary pins prescribed by this conditioning. Apply (3.61),
then multiply by H and integrate the conditioning. It gives

\[
 |\mathbb E[FH\mid t]|
 \le C_{2b}\|F\|_\infty\|H\|_\infty |\operatorname{supp}F|
       e^{-c_{2b}d_{\rm pin}/s(2b)}.                         \tag{O5}
\]

For translated fixed supports the collar can be put at a fixed fraction
of their separation. Small separations use the trivial bound. Free
subgraphs are padded with zero bonds as in the source. On tori both
sides must accommodate its cells and collars; choose L_0 accordingly.
The constants do not depend on t or kappa. Rigid invariance also gives
`E[F|t]=0`, so (O5) is a conditional charged covariance bound.
The same estimate survives integration over t.

This establishes the charged part asked for in route 1, conditional on
the cited theorem. RIG alone would give only its twist-cost starting
point. The explicit reduction (O4) is what permits this particular port.
Neither (O4) nor (O5) uses amplitude association.

### 2.3 The first failure: the eliminated response is neutral (argued)

Write t_u=cos(theta_u) and use h=e^{i theta}. At fixed finite graph
S_b is smooth on the closed theta cube. Let

\[
 Y_u=\partial_{\theta_u}S_b(g,\cos\theta).
\]

Only q_4 at u depends on theta_u in (O1), and `|Y_u|<=b deg(u)`.
Differentiation under the compact integral gives

\[
 \partial_{\theta_u}\log W_b=\mathbb E_{g\mid\theta}Y_u,\qquad
 \partial_{\theta_u}\partial_{\theta_v}\log W_b
  =\mathbb E_{g\mid\theta}\partial_{\theta_v}Y_u
       +\operatorname{Cov}_{g\mid\theta}(Y_u,Y_v).            \tag{O6}
\]

For distinct nonadjacent u,v, the first term is zero: no bond depends
on both theta variables. Each Y_u is invariant under **every rigid
corner action**. To verify this, apply common left multiplication to
one entire g_j sheet. Every longitudinal trace, hence S_b, is invariant
for every theta. Differentiate that identity in theta_u.
Consequently averaging Y_u over any corner leaves it unchanged.
Subtracting its probability mean does not make its corner average
identically zero. The hypothesis of (O5) fails.

This is a specific neutral covariance that enters the effective trace
interaction after the charged variables have been dealt with. No bound
on it follows from (O5). In particular, the total-covariance identity
for the target reads

\[
 \operatorname{Cov}_{\mu}(x_u,x_v)
 =\operatorname{Cov}_{\nu}(t_u,t_v):                          \tag{O7}
\]

the conditional covariance given all t is zero, and the covariance of
the conditional means is the entire quantity. Dropping that second
term would delete the target.
The general warning to keep this term is already in the soft-route
`CODEX_REVIEW_SEAM.md:21–46` on PR 10114, read at the same ref above.
(O7) applies that existing warning to this exact disintegration.

**Named step NR (open).** For the measure (O3), at kappa=b in the stated
window, find a>0 and C<infinity, independent of the graph or torus,
such that

\[
 \sup_u\sum_v e^{a d(u,v)}
 \left|\left.\partial_{z_u}\partial_{z_v}
 \log\int e^{\sum_w z_wt_w}\,d\nu_{b,b}(t)\right|_{z=0}\right|
 \le C.                                                     \tag{NR}
\]

This is the minimal trace target in summable response form, not a
claimed reduction to an easier theorem. Pointwise exponential decay
implies it with a smaller exponent, since square-lattice shells have
at most a constant times r+1 sites; the reverse implication is immediate
by keeping one summand. No association hypothesis is attached.

**Route 1 fails at NR:** even a uniform-in-t charged theorem leaves
(O6) and (O7) unestimated. The precise attempted use of that theorem
on Y_u fails its centering hypothesis. This is not P4-NA, P4-SIGN, or
P4-LIFT, and none of those failures is counted again.

Step 2 outcome: exact trace law and conditional charged port written.
NR remains open. Next: the constrained endpoint and its first correction.

## Step 3. The constrained end and its first correction

### 3.1 Exact endpoint (argued; fixed finite volume)

Keep b fixed and let kappa tend to infinity. This is an auxiliary end
outside the requested interval, so it needs a continuation argument
before it can say anything at kappa=b.

Set A=q_1, B=q_2, C=q_3 and D=ABC^{-1}, site by site. Then

\[
 q_4=H^{-1}D,\qquad
 d q_1d q_2d q_3d q_4=dA\,dB\,dC\,dH.                       \tag{K1}
\]

The second identity follows from Haar invariance under multiplication
and inversion in the last variable. For an oriented version of each
unoriented bond write

\[
 K_{uv}=D_uD_v^{-1},\quad c_{uv}=\operatorname{Re}K_{uv},\quad
 E(D)=\sum_{uv}c_{uv},\quad
 J_u(D)=\sum_{v\sim u}\operatorname{Im}(D_uD_v^{-1}).           \tag{K2}
\]

Define `z_kappa=int exp(kappa Re h) dh=2 I_1(kappa)/kappa`, using
Sussman–Alpoge's GL3 with its constant exponential canceled. Let
`lambda_kappa(dh)=exp(kappa Re h)dh/z_kappa`. The exact marginal on
A,B,C is proportional to

\[
 e^{b[E(A)+E(B)+E(C)]}\Psi_\kappa(D)\,dA\,dB\,dC,
\quad
 \Psi_\kappa(D)=\mathbb E_{h\sim\lambda_\kappa^{\otimes V}}
 \exp\!\left[b\sum_{uv}\operatorname{Re}
                (h_u^{-1}K_{uv}h_v)\right].                 \tag{K3}
\]

For each fixed neighborhood of 1, lambda_kappa gives its complement
mass tending to zero. For example compare `Re h<=1-epsilon` with the
positive-Haar-measure set `Re h>1-epsilon/2`; the ratio is at most a
fixed constant times `exp(-kappa epsilon/2)`. Compactness makes the
bond factor in (K3) uniformly continuous and bounded. Thus, at fixed
finite V, `Psi_kappa(D) -> exp(b E(D))`, uniformly in D.

The limiting law is

\[
 d\mu_\infty(A,B,C)\propto
 \exp\{b[E(A)+E(B)+E(C)+E(ABC^{-1})]\}\,dA\,dB\,dC.           \tag{K4}
\]

It is the constraint `q_1 q_2=q_4 q_3`, not a product of three O(4)
sheets. P4-ORB identifies its one-site manifold as
`SU(2)^4/SU(2)_diag`, of dimension nine. The explicit global coordinates
A,B,C show that it is diffeomorphic to SU(2)^3. This diffeomorphism does
not remove the fourth bond term in (K4). No mixing theorem for (K4)
is supplied by the one-copy theorem cited here.

At this endpoint x_u=1 identically, so its covariance vanishes for the
kinematic reason alone. That gives no rate for fluctuations of x at
finite kappa, and no estimate for other singlets of (K4).

### 3.2 First correction, with its remainder scope (argued)

Use the unit-radius S^3 Laplacian, so a quaternion coordinate satisfies
`Delta h_alpha=-3 h_alpha`. For every smooth f on a finite product of
copies of SU(2),

\[
 \mathbb E_{\lambda_\kappa^{\otimes V}} f(h)
 =f(1)+\frac1{2\kappa}\sum_u\Delta_u f(1)
       +O_{f,V}(\kappa^{-2}).                               \tag{K5}
\]

Here is the local estimate behind (K5). In exponential coordinates
`h=exp(v)`, |v|<pi, Haar volume is a constant times
`(sin|v|/|v|)^2 d^3v`, and `Re h=cos|v|`. Choose a fixed small delta>0.
The complement of |v|<delta is exponentially small by the preceding
comparison, also after multiplying by any fixed power of kappa.
Within that ball,

\[
 \cos r=1-r^2/2+O(r^4),\qquad (\sin r/r)^2=1+O(r^2).
\]

The Taylor remainders have fixed bounds on [0,delta]. Shrink delta so
that the `O(kappa r^4)` term is at most `kappa r^2/4`. The inequality
`|e^s-1|<=|s|e^{|s|}` then bounds the difference from the scaled Gaussian
by a constant times `(r^2+kappa r^4)exp(-kappa r^2/4)`.
Changing variables z=sqrt(kappa)v in these integrals gives

\[
 \mathbb E v_a=0,\quad
 \mathbb E(v_av_b)=\delta_{ab}/\kappa+O(\kappa^{-2}),\quad
 \mathbb E|v|^4=O(\kappa^{-2}).                              \tag{K6}
\]

Odd moments vanish by radial symmetry. The Gaussian coordinate variance
is one: integrate the derivative of `z_a exp(-|z|^2/2)` over R^3,
with the boundary term tending to zero. All higher polynomial Gaussian
integrals are finite by integration by parts or a radial integral.
Taylor-expand f to degree three, with a fourth-derivative remainder.
Independence removes cross-site quadratic terms; odd terms vanish.
The trace of the Hessian in normal coordinates is Delta. These facts
prove (K5), including the claimed error. Its constant can be chosen
from the fourth-derivative bound of f, the finite number |V|, and the
Gaussian-moment bounds just described. It is not claimed uniform in V.

Apply (K5) to the exponential in (K3). At h=1, differentiation of one
bond gives an outgoing gradient `Im K_uv` at u and Laplacian `-3c_uv`.
For the gradient, differentiate `Re(e^{-t e_a}K)` at t=0 and use
`Re(e_a K)=-(Im K)_a`. Incoming bonds give the same outgoing convention
by inversion of the traced word. Consequently

\[
 Q_u(D):=\left.\frac{\Delta_u e^{b\sum\operatorname{Re}
 (h_r^{-1}K_{rs}h_s)}}{e^{bE(D)}}\right|_{h=1}
 =-3b\sum_{v\sim u}c_{uv}+b^2|J_u(D)|^2.                    \tag{K7}
\]

Summing over u counts each bond twice. Expanding the logarithm of
(K5) therefore gives

\[
 \log\Psi_\kappa(D)
 = b E(D)-\frac{3b}{\kappa}E(D)
       +\frac{b^2}{2\kappa}\sum_u|J_u(D)|^2
       +O_{b,V}(\kappa^{-2}).                               \tag{K8}
\]

This is uniform in A,B,C at each fixed finite volume: the required
smooth derivatives are bounded on their compact parameter space, and
`exp(bE(D))>=exp(-b|E|)`. Choose kappa large enough that the relative
Taylor error is at most 1/2 before expanding the logarithm. This order
of choices can depend on V. No thermodynamic limit has been exchanged
with the expansion.

### 3.3 Which neutral observable the correction exposes (argued)

There is a more precise fixed-volume diagnostic. For distinct
**nonadjacent** u,v,

\[
 \lim_{\kappa\to\infty}\kappa^4
       \operatorname{Cov}_{b,\kappa}(x_u,x_v)
       =\frac14\operatorname{Cov}_{\mu_\infty}(Q_u,Q_v).       \tag{K9}
\]

To justify the order and the differentiations, temporarily give each
site its own kappa_u and put t_u=1/kappa_u. The normalized one-site
integration operator has the expansion
`I+(t_u/2)Delta_u+t_u^2 B_u+O(t_u^3)`, with B_u acting only at u.
The value of B_u is unnecessary for a mixed derivative at distinct
sites. Here is why the expansion has bounded derivatives through order
three at t=0. After rescaling v=sqrt(t)z, replace f by its even part in
each v-variable; radial integration leaves the integral unchanged.
Use a smooth cutoff at `|z|<=t^(-1/12)`. Outside it the Gaussian bound
is `exp(-c t^(-1/6))`, with any fixed number of derivatives and polynomial
factors absorbed. Inside it `t|z|^4<=t^(2/3)`. Expand cos r, the Haar
Jacobian, the even part of f, and the remaining exponential through
degree six in t, using integral Taylor remainders. Smoothness of f on
the compact group supplies every needed finite derivative bound.
Parity removes half-integer powers. After at most three t-derivatives,
the remainders are bounded by `C t^4 (1+|z|^M) exp(-|z|^2/4)` for a
fixed finite M; differentiating the cutoff contributes only the same
exponentially small tail. The normalizing integral has a positive
limit, so division preserves these derivative bounds. Apply this
argument in each of the finitely many sites. It gives a C^3 extension
to the closed t-orthant and the stated multivariate Taylor expansion.
Thus no derivative of an uncontrolled big-O expression is being used.

After removing the product of z_kappa_u factors, the constant term of
the partition function is Z_infinity. Its coefficient of t_u is
`Z_infinity E_infinity[Q_u]/2`. For nonadjacent u,v, no bond contains
both variables h_u,h_v. At fixed other h, its exponential factors into
one function of h_u and one of h_v. Hence

\[
 \left.e^{-bE(D)}\Delta_u\Delta_v
 e^{b\sum\operatorname{Re}(h_r^{-1}K_{rs}h_s)}\right|_{h=1}
 =Q_u(D)Q_v(D).
\]

The coefficient of t_ut_v in the partition function is therefore
`Z_infinity E_infinity[Q_u Q_v]/4`. Passing to its logarithm subtracts
the product of the linear coefficients and gives
`Cov_infinity(Q_u,Q_v)/4`. Finally
`partial_kappa_u=-t_u^2 partial_t_u`, and distinct-site mixed
derivatives of the original log partition function equal
`Cov(x_u,x_v)`. The removed single-site normalizers have zero mixed
derivative. Set all t=1/kappa and take the limit. The Taylor remainder
contributes O_{b,V}(kappa^{-5}) after these two derivatives, proving (K9).

Each Q_u is a local corner singlet: Re(D_uD_v^{-1}) is invariant, and
the current J_u conjugates under the left endpoint rotation, preserving
its norm. Thus (K9) again asks for a neutral correlation, now of the
constrained interacting law (K4). Charged decay in (O5) does not estimate it.

### 3.4 Second failure at NR

There are two concrete gaps in this route. First, the starting law
(K4) has no neutral mixing bound among the cited inputs. The fact
`Cov(x_u,x_v)=0` at the constraint is vacuous; (K9) exposes its first
nontrivial distant coefficient. Second, the correction is not controlled
at kappa=b. In (K8) the first correction to `bE(D)` has relative
magnitude `3/kappa`, which exceeds one throughout [2.3,2.6]. The
current-square coefficient is b/2 there. Neither quantity is a small
parameter in this expansion.

This does not imply negative physical stiffness, divergence of the
expansion, or a counterexample to clustering. It means that truncating
(K8) and declaring stability at kappa=b has no justified error bound.
Even a future mixing theorem for (K4) would still need a uniform
perturbation and continuation estimate. Row 1077's example (16) forbids
replacing that estimate by the words "the endpoint has a gap".

**Route 2 fails at NR:** the leading distant trace response is a
constraint-law neutral covariance (K9), and the fixed-volume
1/kappa expansion supplies neither its spatial bound nor a controlled
bridge to kappa=b. This is a different failure from the orbit-score
attempt and from all three ports of row 1084.

Step 3 outcome: constraint law and first correction written, including their
finite-volume limits. Next: the field-conditioned block criterion.

## Step 4. Conditioning three sheets and testing large blocks

### 4.1 Exact field law and the block sum (argued)

By M1 of row 1091, conditioning three sheets makes the fourth an O(4)
sheet in a field. For q_4 the direction is exactly D=ABC^{-1}:

\[
 d\mu(q_4\mid A,B,C)\propto
 e^{bE(q_4)+\kappa\sum_u D_u\cdot q_4(u)}\prod_u dq_4(u).
                                                               \tag{B1}
\]

Write the external field vector as `mathcal H_u=kappa D_u`, distinct
from the holonomy H_u. Thus `|mathcal H_u|=kappa`. The same holds
for any of the four sheets. Changing one other quaternion at u changes
mathcal H_u with Lipschitz constant kappa, since multiplication and inversion
of unit quaternions preserve the round metric. There are three other
sheets, not the six neighbors of an edge in the full face.

Apply the existing FST-BD criterion; do not reprove it. On a large torus
use every translate of an ell by ell square in each one sheet. A site
belongs to ell^2 such blocks. Suppose a conditional block, with arbitrary
same-sheet boundary pins and its actual field directions, had coefficients
R(v,w)>=0 such that

\[
 |\operatorname{Cov}(F,a\cdot q(v))|
 \le |a|\sum_{w\in\Lambda_\ell}R(v,w)\operatorname{Lip}_w F.   \tag{B2}
\]

Suppose also that p(y,w) bounds its response to changing one same-sheet
boundary pin y in the sense of FST-BD (C). These are hypotheses, not
consequences of the zero-field theorem.

Vary one quaternion in another sheet along a shortest round geodesic.
The field direction in (B1) stays on the sphere of radius kappa.
Differentiating its finite integral gives
`d E_s F/ds=Cov_s(F, (d mathcal H_v(s)/ds) dot q(v))`.
Integrating (B2) along this
path yields the influence coefficient `kappa R(v,w)`. No interpolation
through a nonexistent zero field is required for this statement.

With distance `d((u,i),(v,j))=|u-v|_1+1_{i!=j}`, the averaged criterion
would follow from

\[
 \Gamma_\ell(a):=\frac1{\ell^2}
 \left[\sum_{w\in\Lambda_\ell}\sum_{y\in\partial\Lambda_\ell}
 e^{a|w-y|_1}p(y,w)
 +3\kappa e^a\sum_{v,w\in\Lambda_\ell}
 e^{a|v-w|_1}R(v,w)\right]<1.                               \tag{B3}
\]

Here the outer boundary contains the neighboring sites only. To check
the normalization, fix a target site. Each position w in the reference
square corresponds to exactly one translated block containing it.
Other-sheet changes occur at every v in that block, with three choices
of sheet. Summing these contributions gives precisely the second term
in (B3). The number of blocks containing the target is ell^2.
This proves the counting in (B3).

A block much larger than a correlation length can reduce a boundary
term proportional to ell after division by ell^2. It does **not** give
that factor for the other-sheet fields, which act throughout its area.
For example the hypothetical bound `R(v,w)<=X exp(-2a|v-w|_1)` gives
the bulk contribution at most

\[
 3\kappa e^a X S_a,\qquad
 S_a=\sum_{z\in\mathbb Z^2}e^{-a|z|_1}
     =\left(\frac{1+e^{-a}}{1-e^{-a}}\right)^2,                \tag{B4}
\]

with no factor tending to zero with ell. Establishing (B2) uniformly
at fields of order one, with a small enough integrated response, is
exactly the extra task. Zero-field decay alone supplies neither part.

### 4.2 The direct FST-F constants cannot reach this window (argued)

The whole-sheet version of row 1091, adapted from six neighbors to
three, would use a covariance bound with constants X,a for **all** fields
of norm at most kappa. Its explicit sufficient condition is
`3 kappa e^a X S_a<1`. At zero field on any unpinned finite graph the
one-site marginal is Haar. Take F=G equal to one real quaternion
coordinate at a single site. Its variance is 1/4, by symmetry of the
four coordinates and the identity sum q_alpha^2=1; its round Lipschitz
constant is one. Therefore X>=1/4. Since `e^a S_a>=1`, the proposed
sufficient constant is at least `3 kappa/4>1` for kappa in [2.3,2.6].

This refutes the use of **that explicit sufficient bound** at the
requested coupling. It does not imply the true influence sum exceeds
one on a large connected square. A sharper field-specific estimate
or a different block family is not ruled out by this arithmetic.

### 4.3 A hand obstruction to every pure single-sheet block contraction

**SSB (argued counterexample to a method, not to NR).** On a free
longitudinal graph with no bonds, at kappa in [2.3,2.6], no family of
blocks each contained in one sheet can satisfy both (C) and (D_0) of
FST-BD with the round metric and gamma<1. The block sizes are arbitrary.
This includes a one-vertex free subgraph and arbitrarily many isolated
vertices. P4 itself has independent plaquette sites on these graphs.

Proof. At one site, fix the other three quaternions to 1. The conditional
mean of the remaining one is `m(kappa) 1`, where

\[
 m(\kappa)=I_2(\kappa)/I_1(\kappa).                           \tag{B5}
\]

This is the normalized fundamental eigenvalue in Sussman–Alpoge GL3.
More generally the mean is m(kappa) times the field direction, by Haar
invariance and rotations fixing that direction. Changing any one of the
three other quaternions from 1 to exp(t i) rotates that direction to
exp(+t i) or exp(-t i). The sign depends on the position in the word
and disappears in an absolute influence bound.

Use F equal to the i-coordinate of the target quaternion. It has
one-site Lipschitz constant one and depends on no other variable.
Its expectation changes by `+m(kappa) sin t` or `-m(kappa) sin t`.
The input distance is |t| for |t|<pi. In (C), divide by |t| and let
t tend to zero. For every block containing the target, each of its
three same-site outside-sheet variables therefore requires
`k^V_{x->u}>=m(kappa)`. Other sites are independent and cannot reduce
this inequality. Sum over those variables and over all n_u blocks
containing u. Condition (D_0) requires

\[
 \gamma\ge3m(\kappa).                                       \tag{B6}
\]

The Bessel recurrence and GL4 give, entirely by hand,

\[
 m(\kappa)=\frac{\kappa}{4+\kappa I_3(\kappa)/I_2(\kappa)}
 \ge\frac{6\kappa}{24+\kappa^2},\qquad
 3m(\kappa)\ge\frac{18\kappa}{24+\kappa^2}
 \ge\frac{1035}{769}>1.                                    \tag{B7}
\]

For the last inequality use `kappa>=23/10` in the numerator and
`kappa<=13/5` in the denominator: their bounds are 1035/25 and 769/25.
No numerical evaluation of a special function occurs. The contradiction
between (B6) and gamma<1 proves SSB.

The conditional densities depend continuously on the fixed quaternions.
The strict margin in (B7) therefore also persists near the displayed
boundary values; this is not a choice of a conditional law on a null set.

SSB is deliberately weaker than a no-go theorem for block methods.
It shows that enlarging blocks **within one sheet** cannot make the
full criterion uniformly true over the requested free-subgraph class.
The obstruction holds even when the trace covariances are exactly zero
between different sites. It is therefore a limitation of this sufficient
criterion, not slow neutral mixing. A proof can treat these graphs by
another argument, use blocks containing all four sheets, or exploit a
metric and observable class adapted to the neutral sector. None of those
repairs is supplied by merely taking ell large in the stated recipe.

### 4.4 Third failure at NR

Applying FST-BD at order-one field strength fails at its influence
hypothesis and contraction sum, for the explicit reasons (B3)–(B7).
The needed uniform pinned-field covariance estimate is not in the
one-copy source; even the direct FST-F sufficient constants cannot
meet the condition, and the universal single-sheet block version has
the exact obstruction SSB.

If all four sheets in a spatial square are instead integrated together,
the troublesome inter-sheet terms become internal. But its boundary
response is then a neutral response of the interacting P4 block. It is
not (B2) for one O(4) sheet, and no supplied theorem proves its contraction.
That is a possible next method, not a completed third-route proof.

**Route 3 fails at NR:** large one-sheet blocks supply no area gain for
the fields; the explicit sufficient constants fail, and SSB prohibits
the uniform single-sheet contraction as stated. No violation of NR has
been found. This failure uses neither amplitude association nor a
conditional-sign or same-terminal auxiliary-spin representation.

Step 4 outcome: all three prescribed routes have been attempted and written.
NR remains open after three distinct failures. Required controls and the
final scope check remain.

## Step 5. Required controls and the stop decision

### 5.1 Compact U(1) control (guide for the compact model)

For U(1), fix the **full holonomy** exp(i theta) before introducing
corner variables. Its conjugacy class is a point. Conditioning only on
cos(theta) would require both holonomy branches, unlike SU(2)'s single
trace orbit. On each full-holonomy orbit the corner parametrization
has the circle analogue of (O1). The crucial citation in (O5) stops:
the conditional corner field is a twisted XY sheet,
not the SU(2)/S^3 sheet of (3.61). The noncommuting bracket used in that
paper's (3.7) is absent. No exponential charged estimate is imported
for the circle by changing its name.

The harmonic test also stops a group-blind constraint-gap inference.
Writing `q_i=exp(i phi_i)`, the quadratic energy is

\[
 \frac b2\sum_{uv}\sum_{i=1}^4(\phi_i(u)-\phi_i(v))^2
 +\frac\kappa2\sum_u(\phi_1+\phi_2-\phi_3-\phi_4)^2.         \tag{U1}
\]

The on-site Hessian has rank one, since it is kappa times the outer
product of (1,1,-1,-1) with itself. Three combinations therefore remain
massless in this quadratic model. Their gradient energies are rigid
corner singlets. In the two-dimensional Gaussian description, a
nonzero gradient-gradient covariance has an inverse-square tail,
and Wick's identity gives an inverse-fourth-power tail for its squared
gradient energy. Thus charged information in other sectors cannot
prove clustering of all neutral energies.

This calculation is **guide** for the compact P4 model, exactly as in
row 1076; it is not a new compact-U(1) theorem. In particular x itself
reads the massive combination in (U1). Counting the other three modes
does not refute the minimal x-covariance target even in the Gaussian
test. No purported SU(2) counterexample is based on this control.

### 5.2 Product with a U(1) face (argued diagnostic)

For an independent product law `mu_SU2 tensor mu_U1`, an observable
depending only on the second factor has exactly its second-factor
covariance. A corner-invariant bond energy in that factor remains a
singlet of the product group. Consequently a massive SU(2)-charged
sector cannot exclude a slow neutral covariance in the other factor.
If the supplied massless U(1) control is used, its slow covariance
persists unchanged in the product. The Gaussian calculation above is
the verified harmonic version; no compact-model massless theorem is
newly proved here.

Every conclusion of this note respects that distinction. (O5) only
concerns observables charged under the specified SU(2) corner; NR is
not inferred from it. (K4) has no asserted gap based on homogeneity or
nonabelian symmetry alone. FST-BD still requires its quantitative
influence hypothesis for the entire observable algebra.

### 5.3 Ising (16) and the three old ports (argued compatibility)

Row 1077's Ising cycle has a unique unperturbed ground state and gap
one, yet its gap closes at perturbation strength 1/N. Its pin breaks
translation invariance, so it is not a counterexample to an O(4)
hypothesis. It does rule out an inference from an endpoint gap and
small per-site perturbation norm alone. Route 2 explicitly stops
before that inference. Its fixed-volume error is not promoted to a
uniform stability theorem. Route 3 asks for (C) and a contraction sum,
not for that gap-and-norm premise.

P4-NA, P4-SIGN and P4-LIFT remain in force at their stated scopes:

- No amplitude association is used for the conditional trace law or
  the field-conditioned sheet.
- No ferromagnetic conditional pair-Ising representation is asserted.
- (O1) is a nonlinear terminal map with redundant corner variables.
  Its conditional bonds have twists. It is outside the same-terminal
  untwisted auxiliary network prohibited by P4-LIFT; it supplies only
  the charged conclusion (O5), not the missing full-observable theorem.

These are compatibility checks against existing counterexamples. They
are not three extra failures counted toward this task's stop rule.

### 5.4 Marks, exact stop, and next mathematical decision

| Mark | Statement and limit |
|---|---|
| argued | (O1)–(O3): orbit lift and exact effective trace law. |
| argued, given a cited input | (O5): conditional charged decay uniform in the trace field, given OpenAI (3.61) at maximum bond strength 2b, with its collar and torus-size hypotheses. |
| argued | (O6)–(O7): the effective response and target covariance remain neutral. |
| argued | (K4), (K8), (K9): constrained law, first correction, and the leading distant trace covariance, all at fixed finite volume. |
| argued | (B1)–(B4): conditional field law and the actual area contribution in the one-sheet block sum. |
| argued counterexample | SSB: the pure single-sheet FST-BD contraction cannot hold uniformly over the free-subgraph class at kappa in [2.3,2.6]. This does not refute trace mixing. |
| guide | Compact-U(1) extrapolation from the rank-one harmonic mass term; no simulation or numerical fit was made. |
| open | NR, even at kappa=b; hence the minimal target, the larger G-invariant-observable statement, and local uniformity in kappa. |

The stop rule is met at the single named step NR, with three written
attempts: orbit elimination fails on the neutral score covariance in
(O6); the constrained-end expansion leaves (K9) and an uncontrolled
continuation to kappa=b; single-sheet block conditioning fails at
(B3)–(B7). These are failures of the stated attempts, not a theorem
that NR is unprovable, or that the face route must be abandoned.

The concrete next decision is whether to control the neutral response
of a **joint four-sheet block**, or prove a uniform neutral estimate
for (K4) together with a controlled continuation. Neither is silently
accepted here. No counterexample with b in [2.3,2.6] and
0<kappa<=b to the actual x covariance has been obtained.

This file has no independent check and no Lean certificate. The source
reading and the author's hand recheck grant no status. All new
mathematical calculations above are written arguments; no machine
arithmetic, numerical experiment, enumeration, or formalization is a
premise. Tools only fetched sources, extracted selected pages, searched
text, and wrote this note. Only the requested repository output is
changed. No commit or push is made.

## Step 6. Author's final read

I read the whole output and rechecked the quaternion order in (O1),
(K1) and (B1), the factor 1/2 in (K5), the double bond count in (K8),
the nonadjacency condition in (K9), and the normalization in (B3).
The U(1) control retains its two holonomy branches at fixed trace.
The source (3.61) is used only in its charged class. Every asymptotic
remainder retains its finite-volume scope. SSB is expressly a
counterexample to a sufficient method, with no inference against P4.
This is the author's hand read, not an independent check.

The checkout remains pinned at the task revision. The sole repository
change is this uncommitted output file. All mathematical conclusions
retain the marks in §5.4.

RESULT: open at NR after three distinct written attempts; argued conditional charged decay given OpenAI (3.61), the fixed-volume constraint law and first 1/kappa correction with (K9), and an argued counterexample SSB to universal pure single-sheet FST-BD contraction; no counterexample to the actual P4 trace covariance, no status granted, and no mass gap claimed.
