# MGX: what a mass-gap crossover would have to prove

**Decision: UNDECIDED for both the actual crossover (Option A) and a direct
uniform transfer estimate (Option B).** The existing weak-coupling trajectory
does not furnish an applicable strong-coupling coarse action or the complete
source estimate. No argument here rules out either route. The positive
results below are **PROVEN conditional implications** and an exact
normalization/control example; their hypotheses for the proposed Yang–Mills
trajectory remain **OPEN**. No MG0–MG5 row is closed.

Date: 2026-10-29. Source baseline: `f401d825dcdaac36b13f0aee885f16099d066abb`.
Source hashes and actual reading scopes are in [the manifest](checks/mgx_sources.sha256)
and [coverage record](checks/mgx_read_coverage.md). This is the bounded author
probe requested in [the brief](briefs_q/MGX/AUTHOR.md), under
[PROCESS_LIGHT](PROCESS_LIGHT.md). Review and resource history are in
[MGX_LOG](MGX_LOG.md). No scientific status is taken from planning metadata.

## 1. Target, premises and the endpoint actually available

The target is the **same** nontrivial continuum SU(N), N>=2, hierarchy used
for existence, with its complete gauge-invariant local observable algebra,
normalized physical time, valid reconstruction, and
`ker H = C Omega`, `spec H subset {0} union [m_*,infinity)`, `m_*>0`.
The excited space must be nonzero; its spectral infimum must be finite.
The full compact-simple-group Clay quantifier is outside the current SU(N)
construction. No action, continuum limit or physical identification is
derived from the repository's ontology in this probe. The Wilson model,
normalized S4' kernel and regulator geometry are supplied mathematical inputs.

[MASS_GAP_TARGET](MASS_GAP_TARGET.md), sections 2–3, and its
[review](REVIEW_MASS_GAP_TARGET_ASTRA.md) prove the spectral reduction:
diagonal reflected correlations of a family whose centered vectors span a
dense subspace of `Omega-perp`, bounded by `A_F exp(-m_* t)` with common
`m_*>0`, imply the gap. Matching to the actual hierarchy is indispensable.
`A_F` and onset `t_F` may depend on F but must be cutoff/volume independent
for the stated limiting argument. First pass to the limit at fixed physical
time within a safe finite-volume window; only then take large time.

The [local-block construction](MASS_GAP_LOCAL_BLOCK_ASTRA.md), sections 1–5,
[injectivity supplement](checks/massgap_block_injectivity.md), and
[review](REVIEW_MASS_GAP_LOCAL_BLOCK_ASTRA.md), sections 1–6, concern exactly:

- Product normalized Haar on compact SU(N) links, the **pure Wilson** action
  `S = beta_W sum_p (1-Re tr U_p/N)`, with `0<beta_W<=1/32`.
- Cubic spatial lattices and nearest-neighbor physical Euclidean time;
  full spatial magnetic factor and gauge projection. At finite spatial
  volume, `T=A k P_gauge A`, `A=exp[-(beta_W/2)sum_spatial s_p]`,
  `k(U,V)=product_e exp[beta_W w(U_e V_e^dagger)]`.
- An all-boundary, all-field estimate for the **actual** half-slab and
  Perron/Doob conditional. Its physical-time contraction is
  `r(beta_W)=beta_W/[1-12 beta_W-beta_W^2/(1-14 beta_W)]<=18/359<1`.
- A thermodynamic limit, injective positive transfer `P_infinity`, and the
  complete physical slice space at **fixed** spacing `a>0`. On that space
  `H=-a^(-1)log P_infinity`, with unique vacuum and gap at least
  `-log r(beta_W)/a`. A separate local witness proves finite excited energy
  at that fixed spacing. Continuous Hamiltonian interpolation is not a
  restoration of four-dimensional continuum rotations.

These hypotheses are stronger than having a small marginal coefficient,
an auxiliary Gaussian gap, or a finite Perron eigenvalue. The older
[finite-transfer construction](MASS_GAP_CONSTRUCTION_ASTRA.md), section 1,
has a positive all-beta bound which degenerates with spatial volume; that
degeneration is not an upper bound on the true physical gap.

## 2. Coupling normalization and the controlled scale interval

**PROVEN normalization identity.** Compare action coefficients, not symbols
called g. [FLOW](FLOW.md), lines 20–40, uses

    u_k = 1/g_flow,k^2 = beta_W = 2N/g_std,k^2.

The local-block note's `beta=2N/g_K^2` therefore uses a standard-coupling
normalization if identified with FLOW; it must not be read as
`2N/g_flow,K^2`. For a non-Wilson action, FLOW's u is its Hessian marginal
projection, and only coincides with a Wilson coefficient after the remainder
has been specified. The endpoint threshold corresponds to

    u <= 1/32,    g_flow^2 >= 32,    g_std^2 >= 64N.             (1)

FLOW's full conditional argument, lines 187–237 and 392–458, gives

    u_j-u_n = sum_(k=j)^(n-1) (b_k+rho_k),
    |rho_k| <= C_rho g_flow,k^2,
    b_-(n-j)log L-R <= u_j-u_n <= b_+(n-j)log L+R,              (2)

while the required preceding couplings lie in `0<g_flow,k<=gamma`.
Here `b_±=b±C_rho gamma^2/log L`, `b=11N^2/(12pi^2)` under the named
one-loop premise, and `C_rho gamma^2<=b log L/2`.
The remainder proof explicitly uses `g_flow,k<=1`; shrink gamma to at most
one. The tuning theorem keeps **every** node through K in that weak window,
so `u_k>=gamma^(-2)>=1`. Its guaranteed endpoints do not meet (1).
The reviewed [one-loop unit](REVIEW_UNIFORM_ONE_LOOP_COUPLING_ASTRA.md),
final disposition, still excludes nonlinear finite-u flow and the physical
gap; a one-loop result does not discharge (SF-g), full returns, continuity
and the required finite-volume compatibility.

There is a quantifier subtlety: (2) assumes weak inputs only through n-1.
It does **not** forbid an individual final output from leaving the weak
window, nor prove its full action is admissible for the strong endpoint.
No general no-overshoot theorem is asserted. Choosing a very large L also
changes the constants and admissible window; (2) supplies no uniform
large-L shortcut to the endpoint class.

**ARGUED scale picture, not a continuation theorem.** With physical scale
`ell_k=a L^k`, the formal one-loop continuation from `(ell_ref,u_ref)` is

    u(ell) = u_ref-b log(ell/ell_ref),
    ell_sc/ell_ref = exp[(u_ref-1/32)/b].                       (3)

Thus it is **inverse squared coupling** that decreases linearly in log
length; g itself is not asserted to grow linearly in log length. Logarithmic
running alone is no impossibility argument: the formal scale in (3) is
finite for fixed u_ref, and can be fixed in physical units as `a->0`.
But the controlled weak interval ends at `u=gamma^(-2)`, before `1/32`.
Continuing (3) beyond it assumes the missing infrared dynamics. The absence
of an already proved gap does not extend the beta-function control region.
The exact RG, if defined, need not obey perturbative running there.

## 3. What has to match at a physical block

For a continuous positive normalized composite S4' kernel K, finitely many
bounded local finite-cutoff insertions F_i, and finite complex sources J_i,
the exact coarse density and source-dependent weight are

    exp[-S_eff(V)] proportional to integral exp[-S_a(U)] K(V|U)dU,
    W(V;J)=integral exp[-S_a(U)+sum_i J_i F_i(U)] K(V|U)dU.       (4)

These finite integrals exist when the supplied kernel does, independently
of a perturbative representation. That fact supplies no uniform locality
bound. FLOW's Def F-g, lines 146–153, is instead a representation near the
trivial field involving the tree functional, determinant, polymers and
returned terms. Gauge symmetry permits larger loops, multi-loop terms and
interactions across several time layers. A local Hessian or small-field
polymer bound is not an all-compact-field bound on (4). In particular the
tree functional itself is not asserted to be the elementary Wilson action.

**PROVEN projection control.** In SU(2), add `c sum_p s_p^2`, `c>0`, to a
Wilson action. Since `s_p=O(B^2)` at the trivial field, its added Hessian and
FLOW marginal projection vanish. Yet on a plaquette with two independently
varied links in `{I,-I}` and the others I, the added values are
`0,4c,4c,0`; their mixed difference has absolute value `8c`.
Taking one such local term, or its symmetric translation sum, shows directly
that zero Hessian projection does not bound the interaction norm. This is
a local, gauge-invariant polynomial example, not a realization of the
actual RG output, a massless model, or a claim of reflection positivity.

A literal application of the endpoint theorem therefore needs the exact
Wilson action and its slab factorization, or a proved extension controlling
**all** induced interactions. A positive marginal density alone does not
prove reflection positivity or a nearest-time Markov transfer on coarse
links. Enlarging the slice to retain memory is a possible route, but needs
its own transfer and observable matching proof. The correlation criterion
below avoids assuming that the coarse links themselves have such a transfer.

Source transport is a second, coupled requirement. With `mu_c` the coarse
marginal of the normalized joint law and sesquilinear covariance,

    Cov_mu(F,G)=Cov_mu_c(E[F|V],E[G|V])
                 + E_mu_c Cov(F,G|V).                          (5)

**PROVEN:** expand `E[conj(F)G|V]` into its conditional covariance and product
of conditional means, then subtract the product of unconditional means.
All normalizers are included. At the exactly independent kernel `K=1`,
`mu_c` is product Haar, but `W(V;J)=Z_a(J)` retains every fine connected
correlation in a source-dependent constant. Dropping it changes the theory.
The finite-transfer source, equations (21)–(23), already establishes this
control. Higher source derivatives and repeated-link products also have to
be transported; forward images of coarse loops do not give an inverse
map for the fine physical algebra. Source radius, kernel remainders,
original-law tails and failed-return estimates from coordinator lanes
remain named inputs, not results recomputed or granted here.

## 4. A sufficient coarse-action criterion, including non-Wilson terms

This is a library entry rebuilding the elementary Gibbs-comparison method
of Dobrushin in the conventions needed here. It is a **PROVEN conditional
finite-volume estimate**, not an estimate of the actual S4' output.

On a finite compact product of coarse link spaces on a nondegenerate cubic
lattice (periodic spatial sides at least four), with positive continuous
density, assume an exact continuous real interaction decomposition
`S_eff=beta_W sum_p s_p+sum_X R_X`, `beta_W>=0`, with all boundary terms included.
The mixed oscillation `Delta_ij R_X` is the supremum of the absolute
four-term difference from changing i and j separately, over **all** fields.
Put `tau_i` equal to the integer time coordinate of a link's initial vertex.
Fix `nu>0`. For an open time slab, define the symmetric nonnegative matrix,
with zero diagonal,

    C_ij = beta_W m_ij + (1/4) sum_(X contains i,j) Delta_ij R_X,
    q_nu = sup_i sum_(j!=i) exp[nu |tau_i-tau_j|] C_ij <= q_* < 1. (6)

Here `m_ij` counts common elementary plaquettes. Couplings across a periodic
time seam must instead use the cyclic time distance and the safe separation
to the seam; no bound through an uncounted short wrap path is permitted.
Assume absolute summability of the interaction defining the conditional
laws, and (6) uniformly in cutoff, spatial volume, slab and exterior data.

For pure Wilson in four dimensions, each link has six incident plaquettes
and three other links per plaquette, and `|tau_i-tau_j|<=1` per incidence.
The Wilson mixed oscillation is at most `4 beta_W`. Thus the explicit
sufficient condition for (6) is

    18 beta_W exp(nu) + epsilon_nu <= q_* < 1,
    epsilon_nu=(1/4)sup_i sum_(j!=i) exp[nu |tau_i-tau_j|]
                                      sum_(X contains i,j)Delta_ij R_X. (7)

At `beta_W<=1/32`, the Wilson part is at most `(9/16)exp(nu)`.
Any `0<nu<log(16/9)` leaves a positive remainder allowance
`epsilon_nu<1-(9/16)exp(nu)`. This is a concrete all-field perturbation
budget; smallness of `beta[R]` or of the Hessian is not this condition.

For bounded complex local f,g with supports at least d time units apart,
(6) implies

    |Cov(f,g)| <= B_f B_g exp(-nu d)/(1-q_*),
    B_f=sum_i delta_i f,    delta_i f=sup |f(U)-f(U'_i)|.         (8)

Proof. For probabilities whose log likelihood ratio has range L, normalize
its density ratio r so `E r=1`. The constant case gives TV=0. Otherwise,
with `m<=r<=M`, `M/m<=exp(L)`, the extremal
two-endpoint distribution bounds `TV<= (M-1)(1-m)/(M-m)`; maximizing over m
at fixed M/m gives `tanh(L/4)<=L/4`. Changing j therefore changes the i
conditional by at most C_ij in TV. For real functions, use the finite
single-site conditional generator `L_hb=sum_i(E_i-I)` and its semigroup T_s.
The one-coordinate inequalities are `delta_j(E_j g)=0` and
`delta_i(E_j g)<=delta_i g+C_ji delta_j g` for i!=j. The product/Euler
limit then gives `delta(T_s g)<=exp[s(C^T-I)]delta(g)`.
Since C is symmetric with row sum below one, this tends to zero, so T_s g
converges uniformly to its mean. The conditional-expectation identity gives

    Cov(f,g)=integral_0^infinity sum_i E[Cov_i(f,T_s g)] ds,
    |Cov(f,g)| <= (1/4) sum_ij delta_i f D_ij delta_j g,
    D=(I-C)^(-1)=sum_(n>=0) C^n.

The factor 1/4 follows from Cauchy–Schwarz and the range bound on each real
conditional variance: for X in [m,M],
`Var X<=(M-E X)(E X-m)<=(M-m)^2/4`.
Submultiplicativity of the exponential time weight
gives `sum_j exp[nu |tau_i-tau_j|](C^n)_ij<=q_*^n`, hence
`D_ij<=exp[-nu |tau_i-tau_j|]/(1-q_*)`. This proves (8) with factor 1/4
for real f,g. Splitting each complex function into real/imaginary parts
proves the stated conservative factor 1. This auxiliary heat-bath time
only proves a Euclidean covariance inequality; it is never physical time.
Any boundary limit in which these local covariances converge preserves (8). No coarse OS
reconstruction is inferred from this estimate. QED.

This is one sufficient endpoint extension, substantially stronger than a
gauge-invariant mass gap. Failure of (7) would only reject this certificate;
it would not disprove clustering or crossover.

## 5. Complete transport and MG3: a settling implication for Option A

**OPEN producer contract.** Choose a common sequence of fine cutoffs/volumes
and exact coarse blocks of physical side `ell_a -> ell`, with
`0<ell_-<=ell_a<=ell_+<infinity`. For every member F of a physical family
whose centered reconstructed vectors have dense complex span in
`Omega-perp`, supply its actual centered fine reflected pair `(A_a,B_a,n)` such that
`Cov_mu(A_a,B_a,n)=C_a,F(n ell_a)`. This includes renormalizations, products,
centering and all returning/complement sectors. Choose an integer onset n_F
independent of cutoff and volume. For every n>=n_F inside a safe time window,
whose upper end tends to infinity, require:

1. The actual coarse law satisfies (6) uniformly with fixed `nu>0,q_*<1`.
2. The centered conditional means `f=E[A_a|V]`, `g=E[B_a,n|V]` have L2 norms
   at most `M_F`. For every integer `R>=0`, there are centered local
   approximants `f_R,g_R`, each with oscillation sum at most `B_F`, L2 error
   at most `D_F exp(-kappa R)`, and supports separated by at least
   `n-d_F-2R` coarse time units. All constants are cutoff/volume independent;
   `M_F,B_F,D_F,d_F` may depend on F. `kappa>0` is common to the family.
3. The **second** term of (5), with these reflected fine sources, obeys
   `|E_mu_c Cov(A_a,B_a,n|V)| <= K_F exp(-sigma n)+eta_a,F(n)`, with common
   `sigma>0`, finite cutoff-independent `K_F`, and `eta_a,F(n)->0` for each
   fixed n along the same hierarchy. Taking eta identically zero is allowed.
4. MG0 supplies the matching reconstructed limit, including continuity
   sufficient for `n ell_a -> n ell`. MG4 supplies a nonzero excited space.

**PROVEN implication.** Set `R=floor(n/4)` and take `n>=max(n_F,4,2d_F)`.
The covariance error from replacing f,g by f_R,g_R is at most
`(2M_F+D_F)D_F exp(-kappa R)` by L2 Cauchy–Schwarz. Equations (5),(8) give

    0 <= C_a,F(n ell_a) <= A_F exp(-c n)+eta_a,F(n),
    c=min(nu/2,kappa/4,sigma)>0,
    A_F=exp(nu d_F)B_F^2/(1-q_*)
               +(2M_F+D_F)D_F exp(kappa)+K_F.                  (9)

The lower inequality is from the matched reflected fine correlation, not
from arbitrary coarse covariances. All constants and the onset are uniform
in cutoff/volume. First fix n and pass to the same continuum hierarchy;
the window eventually contains it and eta vanishes. Thus
`C_F(n ell)<=A_F exp(-cn)` for every sufficiently large integer n.
An unbounded arithmetic sequence of physical times suffices: for
`0<=b<c/ell`, spectral positivity gives

    exp(-b n ell)||E_H([0,b])v_F||^2 <= C_F(n ell),

so that spectral projection annihilates each v_F. Its boundedness and dense
span annihilate the full centered space. Consequently the physical gap is
at least `c/ell >= c/ell_+>0` and the vacuum is unique. No interchange of
cutoff removal and large-time asymptotics is used. Nonzero excited space
plus self-adjoint H implies some nonzero spectral weight in a finite energy
interval, since `E_H([0,E])` tends strongly to I as `E->infinity`. QED.

This explicitly locates MG2/MG3: a common coarse action **and** localized
conditional means **and** the conditional remainder on the same sequence.
The source remainder may vanish at each fixed time instead of obeying its
own exponential bound; (9) retains that possibility. These requirements
are sufficient, not asserted necessary or mutually independent. They are
a demanding nonperturbative package, not a nearly completed lemma.

## 6. Option B: direct physical transfer at a fixed physical block time

Let `P_a,V` be the actual positive self-adjoint normalized physical transfer
contraction at step a, `P Omega=Omega`, `||Omega||=1`, and
`Pi=|Omega><Omega|`. Choose integers b_a with
`ell_-<=a b_a<=ell_+`. A concrete sufficient **OPEN** estimate is

    ||P_a,V^(b_a)(I-Pi)|| <= r_* < 1,                           (10)

uniform in cutoff and spatial volume, with centered lattice vectors
`v_a,F` satisfying `||v_a,F||^2<=M_F<infinity` and matching the complete
same continuum hierarchy. Finite-time-circle trace correlations must be
identified with these ground-state forms by an actual uniform limit/error
argument; they are not automatically the same object.

**PROVEN implication.** Write a lattice time `t=ma` as `m=nb_a+s`,
`0<=s<b_a`. Positivity, contraction and commutation with Pi give

    0<=<v_a,F,P^m v_a,F><=M_F r_*^n
       <=(M_F/r_*) exp[-(-log r_*)t/ell_+].                    (11)

For `r_*=0` use any larger r in (0,1) in (10)–(11). The fixed-time limit
and dense-family spectral argument now give MG3's positive physical rate,
provided MG0/MG2 matching and MG4 hold. A weaker sufficient replacement is
the diagonal bound `C_a,F(n a b_a)<=A_F r_*^n` for the dense family, with
uniform onset, constants and fixed-n time matching as in section 5.
Neither bound has been produced for the proposed continuum trajectory.
An auxiliary heat-bath gap cannot be substituted into (10).

At an **actual fixed physical coarse spacing** ell, the pure-Wilson endpoint
would supply `r_*<=18/359` and rate `log(359/18)/ell`. Using its theorem at
fixed bare beta and then sending its own step a to zero instead makes the
lower energy bound grow like `1/a`; it does not produce the required
nontrivial finite-energy continuum hierarchy. Likewise, mere positivity
of cutoff gaps is insufficient: `P_a=diag(1,exp(-a^2))` at step a has
`H_a=diag(0,a)`, and its positive excited energy tends to zero. This is an
exact two-state diagnostic, not a Wilson model or numerical experiment.

## 7. Decision, plausibility and the next discriminating work

| Item | Status | What is established / what would settle it |
|---|---|---|
| Normalization and tuned-window comparison | PROVEN from stated definitions | Guaranteed weak nodes have u>=1; the pure Wilson endpoint requires u<=1/32. No claim forbids a final uncontrolled output or a different RG. |
| Literal endpoint applicability to the actual S4' output | OPEN | Identify the complete action at fixed physical block size and prove its all-field admissibility; small marginal projection does not suffice. |
| Non-Wilson extension and transport reduction | PROVEN conditional | (6)–(9) imply a uniform physical decay rate with all source remainders retained. Actual coefficients/maps remain unestimated. |
| Direct transfer alternative | PROVEN conditional / producer OPEN | (10), or the uniform dense diagonal version, with same-hierarchy matching implies the gap. Positivity alone supplies no uniform r_*. |
| Overall crossover and positive continuum gap | UNDECIDED | Neither a realized sufficient package nor a matching-premise obstruction to all live routes has been supplied. |

**ARGUED plausibility.** The logarithmic scale picture is compatible with a
fixed physical crossover, and the strong endpoint leaves a nonzero weighted
interaction allowance. This makes the mechanism mathematically coherent.
There is no evidence here that the actual flow enters that allowance, or
that its full fine-source remainder decays. The direct route avoids an
action-class comparison but still needs an infrared physical-transition
estimate. Neither route receives a GO based on the conditional lemmas.

The next useful output is an actual bound at a fixed physical block for
`epsilon_nu`, together with the complete two-source conditional remainder
in (5), or an all-sector block transition estimate (10). A further one-loop
coefficient, source-free coarse action, selected scalar correlator or finite
matrix positivity check would leave that decision unchanged. The active
source-radius, finite-coupling remainder and original-law tail work can feed
these contracts at its declared scope; none is assumed to have done so.

Method credit: Balaban's constructive effective-action program and Dimock's
exposition motivate the multiscale organization. The primary
[Balaban record](https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/Renormalization-group-approach-to-lattice-gauge/991031665200104646),
[Dimock abstract](https://arxiv.org/abs/1108.1335v2), and
[Shen–Zhu–Zhu strong-coupling abstract](https://arxiv.org/abs/2204.12737v1)
were checked only for attribution/scope. Dimock's cited example is scalar
phi4 in d=3; it supplies no d=4 YM crossover. The local comparison library
was rebuilt above. No remembered item [m], external theorem, numerical fit,
new axiom or independent-review count carries the missing infrared proof.

Numerical checks: **not run**, because the sandbox rejected nice. See
[criteria/resource record](checks/mgx_criteria.md). Independent review is
required before this research note is recommended for coordinator use;
its report is [checks/mgx_review.md](checks/mgx_review.md). This is not a
consolidated public proof, a global no-go packet or an audit verdict.
