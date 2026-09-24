# POST: recent births in the full original ensemble

**Result: PASS for the scoped recent-birth source lemma and full-ensemble
variance lower bound.** The root's central argument agrees with the sealed
independent PRE. Its weaker explicit constant is valid. The five-state toy is
consistent with an explicit finite GKLS cascade and is correctly separated
from the microscopic cube theorem. No consequential error requiring a change
to that bounded central conclusion was found.

The sharper no-first-birth remainder and separate Fisher statement attributed
to other provisional campaign work were not released for this check and are
not certified here. The weaker no-first-birth estimate independently proved
in PRE suffices for every use in the central recent-birth argument. No other
active packet or new root gap work was read. This is not a publication or
audit verdict.

## Frozen inputs and coverage

The unchanged PRE is SHA256
`82b7a4734b2fcfba45022c11859abdaa2239468e8b6a6ddc93f15481b1a41a25`.
Its eleven-member seal is
`71ed041319a34f1a58a53bddbf1e7686094cb7fc7a0ca92886dbb6209868828f`.
Every member was reverified before the release was read.

Only the following released packet and members of its two seals were read:

| Input | SHA256 |
| --- | --- |
| Complete RECENT_BIRTH_FULL_ENSEMBLE_ENERGY_PERSONAL_DERIVATION.md | `5d462335236e20329c9fecac8970cf8ee6393f3af7506ee7db9dbe560e94d74e` |
| AUTHOR_SEAL.json | `f158f2aad27dd8b4f4ef13e8d348ef2ef9ed049f42bc1ff92623e98ade62ae5f` |
| CONTROL_SEAL.json | `0ebde9f2bede5748005aa574d25f2f4a0415f8989f3bdc7d13bb2950925c4ecd` |
| Complete recent_birth_controls.py | `1d56ded6fa3ee1ef8b739c7117d0be2aeff24c2d28f651aceda6be258ad35fc6` |
| Complete result and stdout, identical bytes | `e1e59a8f0faff148503e536bcbe6bdd20678a088eae72e816509d471fdcb1a5a` |
| Complete execution record | `9e05977d658e724b3587f95d8020836a1aebb0ca07dc520043da15f1c86b6145` |

The stderr file is empty. All eight originals, including both seals, have
frozen copies under `released_sources/` and exact paths, sizes and hashes in
`POST_SOURCE_PINS.json`. The complete proof, control source, all eight result
rows, stdout, stderr, execution record and seals were inspected. Applicable
instructions and source assumptions are those already read and pinned in PRE.
The inherited model and effort were retained, without delegation.

## 1. Exact decomposition and normalization agree

The root uses

    x_i(s,t)=V_6(t-s) L_i V_4(s) U_4 Omega,

whereas PRE uses the same vector before the scalar jump prefactor,

    v_i(s,t)=V_6(t-s) j_i V_4(s) U_4 Omega.

Thus `x_i=sqrt(kappa) epsilon^-1 v_i`. The root's exact integral
`rho_6(t)=sum_i integral_0^t |x_i><x_i| ds` is identical to PRE's decomposition.
It includes exactly one first birth and no second birth by the observation
time. The full N=4 and N=8 blocks remain in the normalized ensemble. They are
discarded only as nonnegative contributions to H^2 or to a centered square.

In particular the N=8 Hamiltonian being zero does not mean its contribution
to `(H-mu)^2` is zero. The root's law of total variance includes the terminal
block and does not make that mistake. No physical postselection, modified
instrument, finite-amplitude replacement process or time-binned law is used.

The source normalization also reconciles the moment powers exactly:

    epsilon^6 ||H x_i||^2 = kappa epsilon^4 ||H v_i||^2.

Multiplying by the recent-age integration element `ds=epsilon^2 d tau`
therefore gives the same epsilon^-4 second-moment and variance scale as PRE.
The squared source norm tends to `kappa b_i exp(-48 kappa t)`, so a fixed compact
fast-age slice has total probability of order epsilon^2. Its first-high
population is of order epsilon^4, at energy of order epsilon^-4.

## 2. Required input facts and provisional scope

Root equation (2) records a stronger estimate for the pre-first-birth high
remainder, `O(epsilon^3 exp(-cs/epsilon))+O(epsilon^4)`, attributed to a
different provisional candidate. That sharper decay statement was not read
or established by this POST. It is unnecessary here: the root itself uses
only an O(epsilon^3) difference from the Hermitian low embedding on a fixed
positive-time interval.

PRE equations (P7)-(P11) independently supply the sufficient facts from the
authorized older sources. The Hermitian and no-event projectors differ by
O(epsilon^3); canonical initial data therefore have only O(epsilon^3) high
no-event coordinates. Exact contraction and uniformly bounded intertwiners
preserve that estimate. The low generator is `-iKD` plus uniformly bounded
terms in ordinary and electric-weight norms. Strong bounded-perturbation
convergence gives the same compact-time input path

    u_4(s)=exp(-24 kappa s) exp(-is H_rot,4) Omega,
    ||u_4(s)||^2=exp(-48 kappa s),

with the required common electric-weight bound. No faster high-remainder
decay or separate Fisher estimate is needed for this conclusion.

The source identities cited from the root's preparation-uniform candidate
also agree with the independent PRE derivation and its exact primitive
controls: `R_i=-F_a j_i F_a P`, the edgewise pairs `(b_i,r_i)=(2,4),(2,2),(4,6)`,
and the all-mark sum `sum_i R_i*R_i=72I`. These are operator identities on
arbitrary initial rotor field superpositions, not merely norms at Omega.
Finite-spin source maps need only be bounded uniformly and converge strongly.
Compactness of the limiting trajectory and convergence of the actual low
coordinate justify their use on the evolved input. Uniform convergence over
arbitrary moving high-field preparations is not inferred.

This independent sufficient route supports the recent-birth theorem while
leaving the distinct stronger upstream claims and their provisional status
untouched. No claim is made to have reviewed those excluded packets.

## 3. Full fast generator, compact-age limits and variance

The root retains

    Z=-i delta Pi_1(FF*-F*F)Pi_1-kappa Gamma_1/2

on the complete physical first-high sector. It retains both virtual
denominators with their opposite signs and the dark/bright coupling. The
canonical carrier `exp(-i delta tau/epsilon^2)` is kept until taking the norm.
The finite-spin semigroup convergence is only used on compact fast-time
intervals. It is not evaluated at the unbounded age `t/epsilon^2`.

The uniform source estimates have the correct hierarchy: first-high size
O(epsilon), second-high size O(epsilon^2), and low size O(1), in the root's
L_i normalization. Multiplication by epsilon^3 H kills the latter two terms.
The Riesz/Hermitian discrepancy introduces no competing leading term. The
strong identity limit of low propagation over a shrinking physical interval
is justified on the compact weighted source path, rather than from a large
operator-norm bound alone.

The root's conservative mean estimate `|<x_i,Hx_i>|=O(epsilon^-2)` is sufficient:
its squared conditional-mean subtraction is O(epsilon^-4), while the leading
second moment is O(epsilon^-6). Hence the within-path variance has the same
epsilon^6 limit. The normalized-mixture variance inequality, with all other
trajectory contributions retained as nonnegative, gives the root equation
(11), identical to PRE (P20). This requires no estimate on the total mean.

The root correctly keeps a coherent `R_++R_-` inside one propagated source
vector. Equal loss operators or equal initial source norm do not permit
replacing that source by a resolved mixture. It also uses the evolved
`u_4(t)` rather than reusing the zero-field source vector at a later time.

Root equation (14) concerns the explicitly projected first-high recent
component. Its probability, mean and second-moment scalings follow from the
same compact-age source lemma. This is intentionally narrower than PRE's
additional result for the full recent-slice mean using a weighted low bound.
The root does not identify its projected component with the full ordinary
mean or an apparatus energy cost.

## 4. Constants and order of limits

The bound `||F||<=12` gives `||G||<=288`, and
`Gamma_1=2 Pi_bright` gives `||kappa Gamma_1/2||<=kappa`. Thus
`M=288delta+kappa` is a valid bound on ||Z||. The bounded inverse exponential
estimate `||exp(-tau Z)||<=exp(M tau)` yields the root's explicit coefficient

    36 kappa delta^2 exp(-48 kappa t)/(288delta+kappa).

This is correct, positive and deliberately conservative. The independently
sealed PRE used the stronger dissipative estimate
`d||exp(tau Z)v||^2/dtau >=-2kappa ||exp(tau Z)v||^2`, obtaining instead

    36 delta^2 exp(-48 kappa t).

The second constant is an independent PRE improvement, not a correction to
an erroneous root constant. The frozen root proof is not altered or credited
with this later comparison. Both arguments first take epsilon to zero for
each fixed age cap, and then take the supremum over finite caps. The same
monotone-supremum reasoning legitimately permits a right side written with
`I_infinity(t)`, possibly infinite until separately controlled. It assumes
neither integrability nor a uniform microscopic tail estimate.

Neither proof establishes a matching upper bound or a full pointwise variance
coefficient. The normalized N=6-start ordinary-energy theorem remains a
different problem. Mixed variance is not identified with energetic quantum
Fisher information; a lower bound on variance cannot reverse `F_Q<=4 Var`.

## 5. Analytic interpretation of the five-state toy

The complete code has a consistent explicit GKLS interpretation. In basis
`|a>, |l>, |d>, |b>, |f>` (initial, born low, dark, bright, terminal), choose

    H_high=delta epsilon^-4(I+epsilon^2 G),
    G=[[0,g],[g,0]],
    J_1=sqrt(kappa)(sqrt(b)|l>+epsilon sqrt(r)|d>)<a|,
    J_2=sqrt(2kappa) epsilon^-1 |f><b|.

All other Hamiltonian blocks vanish. The initial survival probability is
`q=exp(-lambda t)`, with `lambda=kappa(b+epsilon^2 r)`. The born low population
is `kappa b(1-q)/lambda`. Put `D=|d><d|`,
`Z=-i delta G-kappa|b><b|`, `A_m=Z+lambda epsilon^2 I/2`, and
`K_h=-i delta epsilon^-4 I+epsilon^-2 Z`. Direct first-birth integration gives

    rho_high=kappa epsilon^4 r q
         integral_0^(t/epsilon^2) exp(tau A_m)D exp(tau A_m*) d tau,
    rho_high,low=kappa epsilon sqrt(br) q
         (lambda I+K_h)^-1[exp(t(lambda I+K_h))-I]|d>.

These are precisely the implemented Lyapunov and resolvent formulas. The
terminal population is the remainder required by the absorbing second jump,
and the full density has unit trace. The recent high-density expression is
the same positive integral with its upper limit replaced by the age cap.
The quadrature expression subtracts each source ket's own squared mean and
therefore tests the same within-path variance used in the analytic inequality.

For omega=delta g, the hand-derived infinite-time Lyapunov solution satisfies

    X_22=1/(2kappa),
    X_11=1/(2kappa)+kappa/(2omega^2),
    X_12=i/(2omega),
    Tr X=1/kappa+kappa/(2omega^2).

At the reported parameters it gives `2.68491124260355`, matching the saved
integral. Z is strictly stable for these positive parameters. The small
positive scalar shift in A_m leaves it stable at all eight reported cases;
thus the integral/Lyapunov representation used in the code is legitimate.
This stable two-dimensional toy is not a test of the cube's complete rotor
spectrum, its large-spin limit, or its algebraic long-time tail.

The Fisher routine uses the standard spectral formula on the subnormalized
three-dimensional born block. This equals the full five-state result here:
the remaining two blocks are orthogonal scalar probabilities with zero H,
and H has no cross-block matrix elements. No extra normalization by the born
probability is required. The small reported Fisher/variance ratio is a toy
observation, not a bound for the actual cube's mixed-state Fisher information.

The field named `field_only_mutant_high_probability` is assigned the literal
zero in the source. It is a zero comparator for discarding the high component,
not a separately propagated or executed mutated GKLS model. No stronger
mutation-testing claim should be attached to that field.

## 6. Evidence checks and limits

The root execution record reports exit code zero and 0.7096904579084367 seconds
wall time. The internal control timer reports 0.033462333027273417 seconds.
The complete stdout equals the complete result file byte-for-byte; stderr is
empty; both the execution record and result identify the pinned source hash.

The two observation times are .6 and 1.2, with four epsilons at each. The stored
initial and born-low probabilities, target coefficients and Fisher/variance
ratios agree with their displayed scalar formulas. Probability sums differ from one by at most
floating roundoff. The smallest-step relative scaled-variance errors are about
2.21e-4 and 5.04e-6, respectively, in this toy only. The source's density-
positivity and quadrature checks are floating diagnostics, not interval
certificates or exact-arithmetic matrix bounds.

No duplicate toy or cube simulation was run or imported. The independent
standard-library `post_evidence_check.py` verifies all source/seal bindings,
the full output correspondence, the hand-derived scalar integral formula,
and arithmetic consistency of all eight stored rows. Its complete results and
logs are retained as `POST_EVIDENCE_CHECK.json`, `.log`, and `.stderr`.
That check is evidence validation, not an independent numerical replication.
The independently reconstructed scientific algebra remains the primitive
source checks frozen in PRE; the analytic comparison is given above.

No computational failure occurred or was discarded in this POST. The weaker
constant, literal zero comparator, stronger unreviewed upstream remainder,
and finite toy's limited scope are preserved explicitly. PRE, author files,
other active packets, publication surfaces and audit state remain unchanged.
This report and the released-source/evidence packet have their own POST seal.
