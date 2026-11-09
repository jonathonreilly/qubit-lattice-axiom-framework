# Independent check of the buffered compact-core ratio

2026-11-09. Research signal **advance** for the frozen local ratio and mixed
derivative statement. No material mathematical defect was found. This is a
research check only, with no audit verdict, retained status, spatial connected
bound or mass-gap conclusion.

## Frozen sources and findings

The complete 170-line `parts/buffered-core-conditional-ratio.md` was read from
`/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics`, pack
`.claude/science/physics-loops/su2-gauge-aligned-response-20261108`.
Its SHA-256 is
`204f48f463fb69eebb6b309996c663698dadd5969728f2a311176e21b53b42c7`.

| Input | SHA-256 |
|---|---|
| arbitrary-boundary-interior-moments.md | c58acdf2d0391847c631a358fcad2bd280e8f563c19947f976118272a4426d11 |
| compact-forest-exchange.md | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 |

The strengthened moment argument at the matching hash was independently
checked in this session in `gates/arbitrary-boundary-moments-check.md`,
SHA-256 `d4e7ae28bc3bcfedb4286dd9ef93c8bc5deb03b2a479ec3bb0efe9a68f85fdb3`.
The exact forest law and source reconstruction were checked in the earlier
reports. This report reuses that matching input coverage and independently
reconstructs the new probability, ratio and derivative steps below.
The inherited source base/main pins and applicable instructions are unchanged.
The supervising model/effort were preserved, with no substitution. No numeric
job, source edit, Git/network mutation, status operation or new external
theorem was used. Only this report was written; earlier reports are unchanged
and no editable prompt changed.

| Severity | Finding |
|---|---|
| Critical / high | None found. The derivative is of an actual normalized event probability and the complete ratio, with orbit variables retained. |
| Medium | None found. The buffer and u thresholds, fifth-cumulant coefficient, and multivariate chain rule are valid. |
| Scope boundary, already explicit | `Z_good` integrates the event that not every S-cell is rough. It is not the unrestricted integral `Z_R`, nor an all-good chart integral. The formulas below use precisely that complement. |

## 1. Buffer choice under an arbitrary quotient exterior

For fixed delta>0, `C_*(2h+1)^4 q_*^h` tends to zero because q_*<1. Hence a
single integer h satisfies equation (1), independently of S, u, torus size
and exterior. For every x in S, `N_h(x) subset N_h(S)=R`, so the arbitrary-
exterior exponential-moment estimate applies with each radius equal to h.
Its upper exponent is

```
t_* C_* |S| + t_* C_* u |S| (2h+1)^4 q_*^h
    <= t_* C_* |S| + t_* u delta^2 |S|/4.
```

On the simultaneous rough event, distinct cell ownership gives
`T_S>=delta^2 |S|/2`. Markov therefore subtracts
`t_* u delta^2 |S|/2`, leaving exactly equation (2). If
`u>=8 C_*/delta^2`, the remaining positive constant term is at most
`t_* u delta^2 |S|/8`, which proves the claimed eta exponent in (3).

The additional condition eta<=1/2 used for the ratio/derivative bounds can,
for example, be imposed by
`u>=8 log(2)/(t_* delta^2)` as well as the displayed threshold. The draft
states this condition separately; it is not silently implied by the first
threshold. Periodic saturation to a whole-torus R is allowed by the moment
supplier and changes none of these inclusions. The proof does not condition
on immediate neighbors of each S-cell and makes no such probability claim.

## 2. Positive integrals and the actual denominator

The indicators of B_S and its complement partition the fixed regional domain,
so `Z_R=Z_bad+Z_good` exactly, with the same exterior, full kernel factors,
Haar measures and normalization conventions in every integral. A positive
identity cap inside R lies in B_S^c for delta>0; all model densities are
strictly positive. Therefore `Z_good>0`, including at arbitrary rough exterior.

Algebra then gives `Z_bad/Z_good=p/(1-p)` and
`log(Z_R/Z_good)=-log(1-p)`. For p<=1/2,
`p/(1-p)<=2p` and `-log(1-p)<=p/(1-p)`, verifying (5). At delta=2 the
endpoint rough event is Haar-null and the same conclusions hold with p=0.

The wording about a compact denominator is read through these exact
definitions: p uses the unrestricted compact regional integral Z_R, while
the ratio denominator Z_good has the stated B_S^c indicator. Nothing in the
proof replaces Z_good by a small-field chart or by a product of one-cell
normalizations. An excluded outside factor is constant in a_R and h and
cancels even when it depends on terminal parameters; it is common to all
three integrals.

## 3. Original sources and event-probability derivatives

At fixed quotient exterior, the exact forest law still has independent
reference Haar orbit coordinates. The sourced regional density is on the
joint variables `(a_R,h)`, with all remaining a coordinates fixed to z.
Keeping `exp(sF(U(a,h))+tG(U(a,h)))` inside that integral is necessary for
gauge-variant sources. At zero sources the h integral is one, so the checked
rough-event probability applies to precisely this baseline. Sources may read
outside quotient coordinates or orbit endpoints; those are either fixed or
integrated as defined, and their global sup norms still give uniform bounds.

For a selected final kernel, differentiating its output gives
`A_c=kappa u <v_c,M_(1,c)>`, with `|A_c|<=kappa u |v_c|`. Its radial
normalizer is output-independent but remains in the measure. For an excluded
kernel, the score of W_R is zero; the original kernel factor already canceled.
The indicators, selected reader family, exterior coordinates and sources are
fixed under the terminal variations.

For distinct terminal links, each score depends on its own terminal parameter
only. Thus every mixed derivative of one log-weight insertion with respect
to any *other* label among `(s,t,c,d)` vanishes. Successively differentiating
the normalized expectation of the fixed indicator yields exactly
`D_I p = kappa_(|I|+1)(1_B,(X_i)_(i in I))`. This checks all subsets I, not
only the highest derivative. It also explains why no repeated-link derivative
may be inserted into the formula. The event's discontinuity in a causes no
problem: its indicator is parameter-independent and bounded, so dominated
differentiation of the compact integral applies.

In every partition term of this cumulant there is exactly one block containing
the indicator. Bound that expectation by p times the sup norms of its other
arguments, and bound all remaining blocks by their sup norms. No indicator
factor is lost to centering. The absolute partition sums are

```
k=1: 1+1 = 2;
k=2: 1+3+2 = 6;
k=3: 1+7+12+6 = 26;
k=4: 1+15+50+60+24 = 150.
```

This verifies the fifth-cumulant coefficient 150 and every lower-order
coefficient needed by the chain rule. The computation is algebraic; no
probabilistic independence or source invariance is required.

## 4. Mixed logarithmic chain rule and its constant

For `f(p)=-log(1-p)`, `f^(j)(p)=(j-1)!/(1-p)^j`. The four derivative
directions commute because the terminal directions act on distinct link
factors and the two sources are scalar parameters. The labeled mixed chain
rule is therefore the sum over set partitions displayed in equation (8),
with no additional block factorials.

For a partition with j blocks, multiplying the already checked event-derivative
bounds produces exactly one factor for each of the four labels. Hence its
score growth is u^2, independent of how the labels are partitioned, and its
source factor is `||F||_infinity ||G||_infinity`. It also produces p^j.
At p<=1/2, replacing p^j by p and `(1-p)^(-j)` by 2^j gives precisely the
draft's conservative C4 sum. An independent evaluation by block sizes gives

```
one block (4):                 300;
two blocks (3,1) or (2,2):   1264;
three blocks (2,1,1):        2304;
four singleton blocks:      1536;
total C4:                   5404.
```

The displayed definition of C4 is therefore finite and valid; 5404 is one
explicit value for it. Combining p<=eta^|S| proves (9) without assuming the
rough-event probability stays small in a nonidentity terminal neighborhood.
The derivatives are estimated directly in the law at the stated point.

Finally, differentiating `log Z_R-log Z_good` directly yields the full
regional fourth cumulant minus the fourth cumulant under B_S^c conditioning,
with the same sources, scores and orbit variables. This matches the event
chain rule and independently checks the sign and normalization of the claimed
response difference. Both conditional covariances and source-only orbit terms
are included in these two cumulants.

## Exact scope

The checked result is a uniform arbitrary-quotient-exterior bound for this
buffered simultaneous-core event, its exact positive complement ratio, and
the source-two/terminal-two mixed response difference. It does not compare
the full regional law to an all-good chart. It supplies no separation decay,
factorization for overlapping buffers, response of a subsequently averaged
exterior law, or bound on a different coarse conditional denominator.
Those restrictions are stated in the draft and remain necessary downstream.
Reopen this check if the event, frozen source, exterior convention, normalizing
integral, derivative labels or buffered-moment supplier changes.
