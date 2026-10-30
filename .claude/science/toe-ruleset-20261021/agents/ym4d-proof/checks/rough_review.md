# ROUGH: fresh hostile mathematical review

Review date: 2026-10-30. This is a scoped research-note readiness review,
not an audit verdict, retained status, or authorization to commit.

## Findings and disposition

The final note supports its finite, conditional mathematical claims. I found
no remaining correctness defect in those claims after the scope corrections
below. **The requested uniform inherited-law joint rough-sector moment is
not established.** Q25, the general history envelope, the complete rooted
sum, and suitable simultaneous allocations remain substantive open inputs.
The note states this at its opening, in its result table, and at its end.
Readiness here is readiness of that partial research result and its precise
failure analysis, not successful completion of the affirmative estimate.

The initial source needed two narrow scope clarifications. The author made
them during this review, and I examined the complete two-hunk diff and the
affected arguments in this same session:

1. Q22 now declares a deterministic global `C_root>=1`. Consequently Q23
   directly implies `r<=1/(1+8 C_root)<1`; no undeclared empty-family case
   is needed in the displayed geometric-series argument.
2. Section 7.4 now places the persistent-flux field on compatible even tori,
   specifies all four link directions and both sign labels, and restricts
   `M=W P`, with `P=diag(1/L,1/L,1,...)`, to directions 1 and 2. It explicitly
   retains `M_3=M_4=I`. Without the direction qualification the mean sentence
   could be read as asserting a false formula for directions 3 and 4.

No other change to the science note was needed for this disposition. The
reviewer edited only this new review file.

## Source identity and coverage

- Candidate Git HEAD checked locally:
  `688a8ddf958e6a5ba5402d6b7fdad4d283af56df`.
- Final reviewed `ROUGH.md`: 624 lines, SHA256
  `40423aa02e8759e0993c980ab396745abfd7321d7db7e92268a78f33ea58493d`.
- Initial reviewed source, preserved by the author as
  `checks/rough_author_initial.md`, SHA256
  `5f9b27ded6692ae452f42f663e5daae1f89e1a2b6fef04a2e47918875d818aea`.
- Input manifest `checks/rough_sources.sha256`, SHA256
  `46c1f594923ffa995cf55ad2801246e583e016dd2542bdf73b5950a58f6fda97`.
  All nine entries matched at the initial check and again after the final
  source correction: REFMATCH, CHARGE, RENEW, MIXSMALL, JMBRB, REALRGA,
  PROCESS_LIGHT, HANDOFF and the ROUGH author brief.

I read the complete initial ROUGH note, including its last line, then the
entire final diff and the final last line. Necessary premises and proofs
were read directly in REFMATCH sections 1 and 3–5; CHARGE sections 1–4;
RENEW's conventions, actual contour orbit and finite-horizon tube proof;
MIXSMALL's conventions, jet calculus, gap comparison and filled-family
envelope; JMBRB's model, gap/geometric proof and joint-integration contract;
and REALRGA's actual-law, derivative, regulator and integration definitions.
No source review's favorable label was used as mathematical evidence.

This is **same-family fresh-context review: Codex reviewing Codex**. The
reviewer received a bounded source-and-task brief, not the author's full
working conversation. Shared frozen inputs and model family limit
independence. The checks below are separate analytic reconstructions;
they are not a cross-family review or machine-checked proof.

## Independent reconstruction of the finite certificate

### Nonabelian ribbons and curvature: Q4–Q6

An axial path from a centered root has at most `3(L-1)/2` transverse edges
relative to its straight leg. Each transverse displacement sweeps `L`
plaquette occurrences. Parallel displacements cancel by backtracking,
including in a noncommutative field. Thus `n<=A_L=3L(L-1)/2` for each
prescribed ribbon. Successive attachments insert conjugates of plaquettes
or their inverses. Telescoping unitary products and HS invariance give

    ||T-S||HS^2/(2N) <= n sum_p n_p f_p.

Averaging the actual paired contours proves the stated W, the identity
for d, `delta<=d<=W f`, and `sum_p W_cp<=A_L^2`. This works on lifted
paths before torus projection; retaining occurrences handles wrapping.
It requires no commuting plaquettes or small-curvature hypothesis.

Independently expanding the averaged squared triangle inequality gives
`||V-S||HS^2/(2N)<=2(delta+psi)+2d<=2psi+4W f`. For a coarse plaquette,
the straight square gives `f(S_P)<=L^2 sum_p q_Pp f_p`. The discrepancy
between its four links and the output links contributes four more norm
terms. Squaring these five terms with factor five gives exactly

    A_Pp=5L^2 q_Pp+20 sum_boundary W_cp,
    B_Pc=10 (boundary occurrence count),
    sum_p A_Pp<=5L^4+80A_L^2.

For a positive roughness threshold epsilon, if both the input-action term
and the gap term were smaller than `epsilon^2/(4N)`, their sum would
contradict `f(V_P)>=epsilon^2/(2N)`. With four boundary occurrences this
gives the displayed `epsilon^2/(160N)` individual gap alternative. The
improved input-action threshold is a current-level statement; the note
does not reidentify it as unused original action.

### Backward demands, overlaps and capacity: Q7–Q11

At one elimination step the contributions to fine curvature are
`xi_j+W_j^T eta_j+A_j^T v_(j+1)`, and those to the current gap are
`eta_j+B_j^T v_(j+1)`. Finite downward induction gives Q8. Every matrix is
nonnegative, so no signed cancellation or inverse is hidden in this step.
The recursion is linear in the entire selected demand family: overlapping
regulator multiplicities add before any bound, as REALRGA requires.

Using `g_c=b_c t_c`, Q9 with no prior expenditure implies pointwise

    -S_0+Ecal <= -sum_G D_G + sum_c b_c t_c psi_c.

With prior expenditure, its fractions must occupy the additional z slots;
the raw Q15 theorem correctly specifies `z=0`. Q11's sharing allocation
uses exactly r_p in total at each multiply claimed plaquette and only
extracts a positive lower charge where a genuine witness or allocated-sum
lower bound has been supplied. A backward reader cone by itself provides
neither. These are sufficient capacity tests, not a construction of
positive charge for every possible rough core.

### Kernel and raw forward integration: Q12–Q16

For the cap estimate, cubes of side `1/(2Nt)` in the `2N^2` real matrix
coordinates have HS diameter at most `1/(sqrt(2)t)`. Representatives in
occupied cubes cover SU(N) by operator balls of radius `1/t`, with at most
`(1+4Nt)^(2N^2)` balls. Haar invariance and the cover give the lower mass
bound. Trace duality and `||M||op<=1` make h 1-Lipschitz, so its exponent
loses at most one in the cap about a maximizer. Therefore
`A_t>=1/C_N(t)`, with precisely the note's C_N.

The tilted-event numerator is bounded by
`exp[-(1-b)t a]` for `0<=b<=1`. Division by A_t proves Q12, including
`b=1`; the exact `b=a=0` integral is one. Direct exponent collection also
gives Q14. In particular `exp(bt delta)` is a positive expense and cannot
be silently dropped. A regulator consumes b of the gap's exponent, so the
original full gap price is unavailable a second time.

After extracting the original charges, integrate the latest output first
using the uniform tilted-event bound and conditional product kernels,
then repeat backwards. This proves Q15 with the stated all-output,
finite-horizon, distinct-gap and deterministic-schedule conditions.
Past-adapted choices require the uniform deterministic per-step bound
explicitly stated in the note. Neither independence of fine fields nor
independence of rough cores is used. Unused normalized outputs cost one.
Q16 follows from the pointwise partition identity with its common F and
cost envelope; it cannot be applied to separately optimized suprema.

## Actual denominator and all required jets: Q17–Q20

The numerator and denominator generally integrate over different spaces
and use different densities. Q17 allows this and never identifies Z_A
with the integral of the opened numerator. Positive fixed sectors,
dominated differentiation and uniform score bounds over the respective
integration variables and direction choices are essential hypotheses.
The explicit path-based scores supplied in the note are such bounds at
finite reader count. Their locality and uniform size are not automatic.

A check independent of quoting the reciprocal partition formula is to
differentiate `D D^-1=1`. If `M_S^-` bounds `|D_S D|/D` and
`R_I=D|D_I D^-1|`, then

    R_empty=1,
    R_I <= sum_(nonempty S subset I) M_S^- R_(I\S).

Unrolling this recursion orders the blocks of each set partition and
therefore gives exactly `|pi|!`, as in Q17. For the numerator, repeated
Leibniz gives the exponential partition polynomial with coefficient one.
Combining the two gives C with different plus/minus arrays. Order inside
each derivative block is preserved, so this argument does not commute
same-species group derivations.

All sixteen subsets of four original labels are present, without an
extra four-label factorial. The downward-closed field set `a+b<=6`
includes mixed fine/coarse derivatives, and the combined order can reach
ten. Product estimates distribute the labelled sources among factors;
extra repeated-label terms in the product of seminorms only enlarge its
nonnegative bound. They do not replace a four-source coefficient.

The path estimates also check directly: an rth Wilson-plaquette derivative
has at most `4^r` occurrence choices, each carrying the appropriate frozen
field weight. A kernel contour has at most `ell=5L-4` occurrences, and
including its output gives `lambda=ell h_f+h_c`. The numerator score costs
`t lambda^r`; the differentiated log normalizer costs
`lambda^r L_r(t)`. Earlier kernels must each be included. Original-source
derivatives do not retune any kernel. Mixed field/source derivatives of
the action do survive, and reciprocal-normalizer derivatives generally
survive even when higher pure-source scores of the exponent vanish.

Q18's source identity is exact for the linear tilt. Its absorption follows
from `x exp(-epsilon x)<=1/(e epsilon)`, reserving `sum epsilon_i` only
once. It does not pay denominator jets. Q19 is the product seminorm bound
under the same integral; it differentiates the complete quotient density.
Q20 then extracts only the actually supplied lower charge and leaves the
unchanged denominator and uncharged integral in C. It is a valid bound,
not a proof that C is local or at most one. Fixed-sector assumptions do
not remove moving-cut boundary terms: their estimate remains named FR.

## Full roots and histories: Q21–Q25

The disjoint-bump example correctly distinguishes a pointwise history sum
from the norm's sum of suprema. A common y-independent mass envelope as
in Q21 permits the latter sum; a bound on each history separately does
not. MS23 genuinely supplies such an envelope only for its filled-family
output/source problem, with all earlier fields integrated and the extra
output-weight condition. It supplies no retained fine/exterior jets for
an arbitrary local core.

For the conditional encoding, a deterministic spanning-tree traversal
with `2(n-1)` steps determines the connected vertex set. There are at most
`Delta^(2(n-1))` such walks through a fixed root. Under the stated
one-placement-per-fixed-label encoding, `(n+1)^4<=16^n`; multiplying by
the assumed D^n decoration bound gives Q22. D must actually encode times,
absences, mergers and complete readers as the text requires. No uniform
such encoding is established for the model's general history family.

The final root-cover hypothesis charges every support root to at most
C_root fixed possible skeleton roots. Thus the full sum is bounded by
`C_root r/(1-r)`. Q23 makes it at most 1/8, leaving the separate 1/8 small
budget. This argument does not cover long readers when its support-size
or root-cover hypotheses fail; Q24 explicitly retains that obligation.
Exact factorization across complete components is also separate. Counting
and separate marginal bounds cannot supply it on an interacting law.

Q25 remains a substantial version of the desired local inherited-law
comparison. It has not become a solved weaker lemma by being named. It
must hold with the actual denominator, all selected overlaps, all jets
and a common summable history envelope. The note correctly says so.

## Failure and obstruction checks

- **Global-cap failure, Q26–Q27.** Four n_j link caps cost
  `8N^2 log(1+4N/zeta)n_j`. Six n_j plaquettes, each with action at most
  `8u_j zeta^2`, cost `48u_j zeta^2 n_j`. There are `4n_j/L^4` last kernels;
  their numerator upper and denominator lower bounds together cost
  `16kappa u_j n_j/L^4`. This reconstructs the displayed d_j for the scalar
  original-charge comparison, with retained cuts satisfied by the cap.
  The local price test fails as volume/core ratio grows. An insufficient
  upper majorant is not a lower bound on the true moment. Jets, insertions
  and source changes keep their additional bills.
- **Depth-capacity failure, Q28.** A chosen straight-square occurrence
  contributes at least `5L^2` to each transport matrix. A nested chain
  therefore contributes at least `(5L^2)^R` to one original coefficient.
  For terminal demand `a u_R`, Q9 necessarily imposes the displayed
  inequality. Constant couplings, or a polynomial `u_0/u_R`, violate it
  at large R. These are explicit test coupling classes, not a derived RG
  trajectory. The coefficients upper-bound transport; they do not
  lower-bound physical curvature or the actual moment.
- **Conditional-kernel obstruction, Q29.** On the specified SU(2) periodic
  field, the axial factors cancel for direction 1 and its L straight-link
  phases average to the sum of L roots of unity. Hence its actual mean is
  zero. Haar normalization gives `delta=1`, `psi=0`, and exactly
  `exp(a m t)` for the moment. For any a>0 this rules out the specified
  t-independent C^m bound, even at m=1. It says nothing against an
  original-field integral that pays its charge. RM23's divided seminorm
  and this unpaid integral are different assertions.
- **Future tilt.** For positive K(E), choosing H=1_E gives K^H(E)=1.
  This disproves unrestricted reuse of the forward gap price under a
  changed conditional law. It does not identify the actual Z_A with that
  particular tilted reference; the raw event mass remains available once.
- **Persistent flux and filled-family payment.** For directions 1 and 2,
  the odd sign average gives P and the trace identity is
  `2N psi=tr[(I-W*V)* P (I-W*V)]`. Since P is positive definite, its zero
  occurs only at W. Thus `delta=1-tr(P)/N=2(1-1/L)/N` despite zero gap.
  Directions 3 and 4 have identity mean and zero deficit. The RENEW tube
  proof controls finitely many outputs at fixed horizon; the original
  tube has positive measure and its distinct 12 plaquettes pay the stated
  raw charge. CHARGE's geometric fractions total less than one, and its
  all-cut estimate uses its stated coupling, cut and depth restrictions.
  The ratio test for `B^R exp(-lambda L^(4R)n_R)` is correct at fixed
  terminal volume and yields a uniform majorant by taking n_R>=1. It does
  not exchange the persistence limit with an infinite history sum or
  prove filled ancestry for arbitrary localized rough cores.

These are two failed sufficient techniques, one precisely restricted
conditional-kernel obstruction, and preserved positive special cases.
They do not prove all-history divergence, route exhaustion or a no-go for
the desired inherited-law estimate. The N1–N8 discussion does not claim a
complete negative-claim packet or logical independence of its open walls.

## Verification limits

The parent reported `/usr/bin/nice -n 10 /usr/bin/true` was refused with
`setpriority: Operation not permitted`. I did not bypass or rerun that
guard and ran no mathematical numerical experiment. Verification here is
analytic reconstruction plus small deterministic file/hash bookkeeping.
The final source and all nine frozen inputs were rechecked after the
author's edits. No external service, audit/ledger file, commit or retained
status was used or changed. This review establishes neither a general
all-history bound nor the missing FR/KR/TC model estimates, and makes no
exhaustive literature or novelty claim.

VERDICT: LAND
