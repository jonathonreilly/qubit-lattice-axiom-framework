# Hostile review of LGF

2026-10-29. Reviewer: Codex, in a fresh context, with no authorship of the
reviewed files. **Same-family review: Codex reviewing Codex.** The required
reading included the earlier `checks/lgf_review.md`; this review is independent
of authorship, but was not blind to that report's conclusion. Its verdict was
not used as mathematical evidence.

**Finding: no blocking mathematical defect found in this source revision.**
The four requested results are supported, including the explicit constants,
zero-frequency accounting, and the free curvature consumer. LAND here means
readiness of this mathematical library entry for lane consolidation. It does
not establish interacting Yang–Mills claims or confer an audit/retained grade.
The inherited TSE55 wording still needs the binding corrections listed below.

## Scope and source identity

All relative paths are in
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
The controlling task is `briefs_lgf/REVIEW_BRIEF_LGF.md`, including its
instruction to write only this report and make no commits. The earlier author
log's different output-path decision at `LGF_LOG.md:57–61` does not change this
review's write boundary.

| Source | SHA-256 |
|---|---|
| LGF.md, all 605 lines | `40ea604c79f17027129628bc8b31f5fd6209da21dded864bf45a422dad24505e` |
| LGF_LOG.md, all 122 lines | `2619e256dde14d9b4be7657f288d12d0af8b44d7ba9d9cc7418eef0893134382` |
| checks/lgf_criteria.md | `9c1c6fd66a7490d863dc08395b456246d12d8c2f3aaedd19b6cf97167e4729` |
| checks/lgf_review.md, all 244 lines | `6287e286d177f4b0faaf64a203471f7e09408f9126903428d5ca77c1b5f3d463` |
| checks/lgf_source_manifest.json | `5c922a93e90576570562656db5d90b6ba150edf9ff56c76eacef15bfb9d83f12` |
| briefs_lgf/AUTHOR_BRIEF_LGF.md | `dc358ffa750b051d70afd4fc34f56d68f1b7b3ecca5c4e5d289adb38ee38dd2c` |
| briefs_lgf/REVIEW_BRIEF_LGF.md | `ec04cbfe8656d37ac6b418585646c378a5b6c9e1f6da82f9b33dc1f9d7fcccea` |
| TSE55.md | `d02cc8b265c20da5fc59812a59d68e12d3c9a550d9f9df0890db1c61a38f7340` |
| CODEX_REVIEW_TSE.md | `b70b1236e525fe5e3c83cd99b9f7142801a0a215f7e4a34879cdca50917d3edf` |
| LINEAR_PACKAGE.md | `0a2649ff5dbda9963a65ac62770a831d5e9737b9694ea873f28f008496e8e7ad` |
| PROCESS_LIGHT.md | `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab` |

Working HEAD: `fcdd32c83bc5aed08ef4f3aa5da512e668d8b216`, branch
`claude/ym4d-lgf`. Both main and planning fetch commands returned exit 0 in
this review. The resulting refs were respectively
`ca2bc7ddf64790da96cd43d42017d000fbfe4808` and
`56c5c0ab64f532c5784e895b2f9aa6894fa334e0`.
Planning supplied no mathematical premise. These observations do not
authenticate the earlier author's fetch history.

Applied `SCIENCE_WORKFLOW.md`, the physics-claim-reviewer skill and its
proof-search-governance reference from the identified main revision; their
working copies were checked byte-for-byte against that revision. Read the
entire LGF packet and process, TSE55's object/normalization and curvature-law
definitions at 68–155, its LGF/FREE argument at 179–208, base-point convention
at 223–226 and import status at 443–444; read CODEX_REVIEW_TSE R9 and R11 and
LINEAR_PACKAGE §1.1. Other TSE55 claims are not independently certified here.

## Verdict for every requested item

| Brief item | Verdict, source and reason | Fix |
|---|---|---|
| 1. Conventions | **CONFIRMED.** LGF 14–56, 490–515; LINEAR_PACKAGE 57–60; TSE55 93, 132–150, 194–201. The positive graph operator, counting inner product, forward exterior derivative, backward adjoint, zero-mean torus inverse and coupling-one curvature law agree. | None in LGF. Carry these definitions into TSE55 explicitly. |
| 2(i). Infinite lattice | **CONFIRMED.** LGF 58–214, 316–346. Gaussian subtraction leaves a symbol of order zero; the explicit derivative ledger and eight integrations give the stated remainder. Shifted and origin-crossing differences are covered. | None. Preserve the uncentered-difference convention; do not promote the stated rate to a sharper derivative rate. |
| 2(ii). Order-two torus | **CONFIRMED.** LGF 216–314, 348–433. Shellwise periodization handles the lattice singularity; the heat comparison gives uniformity; the grouped continuum image identity has the stated quadratic term. | None. Keep the shell/orbit prescription and the alias constant; an unqualified image sum is not an equivalent proof. |
| 2(iii). Orders zero and one | **CONFIRMED.** LGF 245–314, 435–486. The positive estimates give the corrections `T^-2` and `T^-3`, independently of the counterexample. | Replace TSE55's ambiguous all-orders torus wording before adopting this result there. |
| 2(iv). Weitzenböck and Feynman gauge | **CONFIRMED.** LGF 490–548. Exterior algebra gives the scalar Hodge Laplacian and the exact projection covariance, with the correct four kernel signs. | None. Retain the quadratic, one-color, coupling-one scope. |
| 3. Order-zero counterexample | **CONFIRMED.** LGF 437–486. Its compactly supported test and neighboring stencils lie in the claimed annulus. The two summation-by-parts sides have different limits under the rejected bound. | None. This refutes the specified uniform estimate, not a Yang–Mills construction or all possible Green estimates. |
| 4. Hidden imports | **CONFIRMED within scope.** LGF 60–81, 111–225, 233–236, 350–407, 490–515 exhibit the needed analytic/algebraic steps. The references at 597–604 are attribution, not proof leaves. | None. No literature citation can replace these arguments in consolidation. |
| 5. Exact consumer | **CONFIRMED.** LGF 517–548 and 555–561 match TSE55 180–208 and CODEX_REVIEW_TSE 138–142, 162–170. The squared-kernel error also follows with the stated explicit constant. | Apply the binding TSE55 wording/status changes below; keep its other hypotheses separate. |
| 6. Checks, order of criteria, intervals and reruns | **NO NUMERICAL CHECK TO RERUN.** checks/lgf_criteria 3–5, LGF_LOG 63–68 and the complete LGF file inventory agree: there is no LGF numerical script, output or numerical proof input. The manifest hashes reproduce. | None for this analytic proof. Historical criteria-before-script chronology is not independently authenticated; with no script, that gate is inapplicable. Any later numerical proof input needs preregistration and rigorous intervals. |

## Line-by-line mathematical checks

### Operator, continuum normalization and subtraction: LGF 14–100

The multiplier of `-sum_j nabla_j^- nabla_j^+` is
`lambda(p)=sum_j(2-2 cos p_j)=4 sum_j sin^2(p_j/2)`. Its quadratic part is
`|p|^2`, not `|p|^2/8`. Integrating the displayed normalized four-dimensional
heat kernel gives `1/(4 pi^2 |x|^2)`. Thus the inverse of `I-P` has eight times
this coefficient; the note does not confuse the two Green functions.
Deleting precisely the zero Fourier mode gives both zero counting mean and
`Delta G_T=delta_0-T^-4`, including small tori.

The Gaussian alias sum unfolds correctly because x is integral. Its Fourier
coefficient is f, so the remainder is exactly `E=G-f`, not an asymptotic
substitute. The singularity is integrable in four dimensions.
Writing `delta=q-lambda`, the reciprocal identity in 93–94 gives a sixth-order
Taylor contribution at most `q/360` and a quadratic-delta contribution at most
`q/36`; their sum is `11q/360<q/16`. The sign of the quartic term is positive.
`Delta_cont Q_4=12q` and `Delta_cont q^2=24q`, so the harmonic decomposition
is correct. Signed-permutation invariance does not eliminate its directional
part, and the proof does not attempt that cancellation.

### Explicit constants and Fourier integration: LGF 102–214

For the inverse-symbol induction, grouping multiindices by derivative order
gives exactly `binomial(n,k)`. After division by the proposed bound, the
recurrence is bounded by `64 sum_{k=1}^n 1/(k!128^k)<64/127<1`.
For `|p|>=1/2` the corresponding factor is at most `256/511<1`.
The three-factor product for `(q-lambda)/(q lambda)` fits inside
`128 n!512^n |p|^-n`, hence below `2^130 |p|^-n` through order eight.

The displayed Gaussian derivative polynomial is correct, with overall scale
`t^(n/2)` after `u=sqrt(t)y`. Its term and factorial bounds cover mixed as well
as repeated-coordinate derivatives. For aliases, coordinatewise
`|p_j+2 pi l_j|>=pi |l_j|` for nonzero l_j gives the required vector bound.
The Gaussian sum is less than 16; splitting its exponential supplies
`exp(-t/16)` on both specified domains. The integral constant
`2^104 * 5! * 16^6` is below `2^137`. This verifies (9), not just boundedness
of R without its derivative constants.

The cutoff is C^12 at both junctions because its first derivative vanishes
to order twelve there. Its normalization, coefficient sum and quadratic-chain
derivatives fit under `2^150`. In the shell product, radial conversions cost
at most `4^8` each and the Leibniz sum at most `3^8`, within (14).
For the outer product, the separate global bound
`|partial^beta Q_alpha|<=4*2^n` suffices; no small-momentum estimate is being
applied outside its domain.

Shell volume, normalization and `|x_i|>=|x|/2` give the two explicit bounds
`2^604 rho^(4+m)` and `2^612 rho^(4+m)(rho|x|)^-8` before interpolation.
Eight integrations are permitted by the established regularity. Shell boundary
terms vanish, and outer boundary terms cancel because all relevant derivatives
are periodic and x is integral. The resulting dyadic ratios are
`2^(-4-m)` and `2^(-4+m)`; neither is borderline for `m<=2`.
This proves (16), including at zero, by an L1-convergent multiplier expansion.

### Periodization and uniformity: LGF 216–314

The individual shell coefficients are absolutely summable. The supplied Fejér
argument identifies their sum with the original continuous periodic function;
finite grid orthogonality then proves (17) with the chosen Fourier sign.
This does not assume absolute summability of the unsplit order-zero E.

Grouping continuum modes modulo T leaves modes `k=T l`, `l!=0`, in the
discrete zero class. They contribute `+T^-4 a_*` to f_T, so (19) correctly has
`-T^-4 a_*`. Positive-order differences kill that constant.

For small shells, `rho T<1` excludes every nonzero grid point. Their total
error is at most `2^641 T^(-4-m)`. For the other shells, the image distance is
at least `3T|n|/4`. Supremum-norm shell counts are
`(2k+1)^4-(2k-1)^4=64k^3+16k`, giving `sum |n|^-8<=100`.
The close numerical inequality needed here is exact:
`100(4/3)^8=6553600/6561<1024`.
Thus the `2^650` coefficient in 260 really suffices. The remaining geometric
sum, outer term and alias term fit well below `2^710 T^(-4-m)`.
For m>=1, the absolute dyadic coefficient majorant is summable over images,
justifying the final interchange in 267–269.

The heat derivative estimate (21) covers both mixed and repeated indices.
An oriented difference is an integral of that derivative over translated unit
intervals. Even at T=4 and m=2 these points satisfy `|z|<=3T/4`, hence every
nonzero image has distance at least `T|n|/4`. There is no omitted stencil
restriction. T<4 has no lattice point in the theorem's stated nonempty-radius
domain.

In (22), the prefactor 16, Gaussian sum below `2^21`, and remaining integral
below `256^2=2^16` give `2^41`. The constant subtraction costs at most T^-2
only for m=0. The large-time nonzero-mode tail has exactly the factor in (23);
the infinite heat tail is at most `16 T^(-2-m)`. Thus (24) is uniform in T.
Together with (20), it gives the three correction powers claimed in (5).

### Infinite-volume comparison and small separations: LGF 316–346

Direct differentiation of `|y|^-2` gives coefficient sums
`1,2,10,72,696`; at order four this is `384+6*48+3*8`. They fit within
`2^n(n+1)!`. At r>=4 every stencil segment has norm at least r/2; integrating
one further derivative along its displacement bounds the derivative/difference
mismatch by the stated `2^20 r^(-3-m)`.

For (26), heat substitution gives a factor
`16*8^(1+m/2)|y|^(-2-m)` times a tail integral of `u^(m/2) exp(-u)`.
The displayed exponential split and `|y|^2 exp(-|y|^2/16)<=16` supply the
extra inverse-square decay with margin below `2^30`.
For `1<=r<4`, the direct integral bound is valid: containing B in the radius-8
ball gives even the unnormalized integral at most `256 pi^2<2^12`.
At most four translated values bound a second difference; the singular
continuum function is differentiated only at the nonzero base point.
The resulting constants lie below the separate `A=2^1000` coefficients in
(4) and (5). Neither coefficient needs to grow with T or orientation.

### Image orbits and polynomial: LGF 348–433

Within each signed-permutation orbit, the second moment is isotropic.
Consequently the Hessian coefficients `8/4` and `-2` cancel exactly.
Inversion cancels first and third Taylor terms. Subtracting through degree
three leaves a fourth-order remainder bounded by a constant times
`|z|^4 T^-6 |n|^-6`. The stated constants cover the directional factors
`|z|_1<=2|z|` and the factor `2^6` from distance. The corresponding first
and second differentiated remainders fit under `2^30`; the shell sum is at
most 120. Third derivatives have an ordinary absolutely summable `|n|^-5`
tail, with shell sum at most 160. This proves the required local C^3
convergence and harmonicity of S_T.

Integrating the third heat derivative gives an absolute bound
`2^30 |y|^-5`. On compact sets away from sources this is a summable common
majorant, so the differentiations and Fubini step in (31) are legitimate.
All third derivatives of `K_T-S_T` vanish on the connected punctured ball.
The difference is one quadratic polynomial; cubic symmetry leaves only
`C_T+b|z|^2`. Applying the background equation fixes
`-8b=-T^-4`, hence `b=1/(8T^4)` with positive sign.

Heat scaling and the same small-time image bound give
`C_T=T^-2 C_1` and `|C_T|<=2^45 T^-2` as claimed.
The polynomial is local, not a separately periodic function. Its every
oriented second difference is `delta_ij/(4T^4)`.
The lattice comparison in 423–433 retains the short heat integral, remainder
shells and alias constant; it does not silently replace G_T with K_T.

As an independent algebraic discriminator, away from a lattice source,

    sum_j [nabla_j^+ nabla_j^- G_T(x) - partial_j^2 Phi(x)] = T^-4.

This follows directly from the discrete Poisson equation and continuum
harmonicity. It checks both the background sign and the trace of the proposed
quadratic correction without using the image argument. Dropping the
background term or reversing its coefficient would violate this identity.

### Summation-by-parts counterexample: LGF 435–486

The function (33) is C^4, nonnegative and positive on an open annulus.
Its fifth-order boundary zeros are sufficient; infinite smoothness is not
required. For T>=64, its support and neighboring lattice sites lie strictly
between radii T/8 and T/4. The polynomial coefficient/derivative bounds in
449–451 have substantial margin.

The centered stencil's continuum second-order term vanishes on Phi, leaving
the fourth-derivative error in (34). The two uniform bounds there imply
`sum H_T Delta phi_T=O(C/T)` under the rejected assertion, whereas
`sum phi_T Delta H_T=-T^-4 sum phi(x/T)+O(T^-2)`.
The stated first-derivative Riemann-sum bound makes the latter tend to
`-integral phi<0`. Extending H_T off the common support-and-neighbor set
does not change either side of the finite self-adjoint identity. The
contradiction is valid for every proposed finite uniform C.
It proves neither order-one optimality nor a broader no-go statement; LGF
does not claim either. The positive corrected bounds were proved separately.

### Gauge reduction and exact consumer: LGF 488–548

The anticommutation relations with `(nabla_j^+)*=-nabla_j^-` give (37)
componentwise. At a nonzero mode, with `q_j=exp(ip_j)-1`, the curvature
covariance is `q wedge iota_conj(q)/|q|^2`, the orthogonal projector onto
exact two-forms. On links perpendicular to q, the ungauge-fixed quadratic
form already has eigenvalue `|q|^2`; adding Feynman gauge affects only a
direction annihilated by d. Constant harmonic links also have zero curvature.
This establishes the gauge-quotient identification used in TSE55 142–150.

Independently expanding two position-space curls gives (39): a forward
y-difference of G_T(x-y) is a negative backward difference in z. The four
Kronecker-delta signs and their continuum replacement are therefore correct.
A second exact check is

    sum_{mu<nu} G^F_{mu nu,mu nu}(z) = 3(delta_0(z)-T^-4).

Each diagonal scalar second difference occurs three times. At zero, symmetry
gives each plane variance `(1-T^-4)/2`; away from zero, the trace is
`-3T^-4`, agreeing with the polynomial correction and its curvature signs.
These controls would reject a sign or normalization reversal.

The D in (40) is exactly TSE55's `-X/(4 pi^2)`. The statement in LGF 536 is
the same consumer as TSE55 200–201, with base points, r=|x_p-x_q| and
`1<=r<=T/4`. The source's line wrap has no mathematical effect:

> 𝔊^F(p,q) = D_{μν,ρσ}(x_p − x_q) + O(r^{−5}) + O(T^{−4}).

Four applications of (5) give each O constant `B=2^1002`. For the squared
kernel, the cross term is bounded by `2^1015(r^-9+r^-4 T^-4)`, and the
error square by `B^2[r^-9+(2+1/256)r^-4 T^-4]`, using r>=1 and r<=T/4.
Both fit under `2^2010(r^-9+r^-4 T^-4)`. This is precisely the scalar input
of FREE at TSE55 205 and R9 at CODEX_REVIEW_TSE 138–142. The physical-spacing
conversion in LGF 541–542 follows from the degree-four homogeneity.
The consumer table's R9 locator, line 142, and the R11 quotations are correct.

## Imports, checks and verification limits

No load-bearing remembered asymptotic or literature lemma was identified.
Gaussian integration, Taylor remainder, Fourier reconstruction, heat
periodization and exterior algebra have adequate derivations in the note.
Basic finite-dimensional Gaussian covariance and elementary calculus are
used in their stated domains. No numerical approximation enters a proof
constant. Powers of two and the rational bounds above are exact analytic
bounds, not floating-point measurements requiring interval certification.

For attribution context only, the linked
[Lawler–Limic book](https://www.math.uchicago.edu/~lawler/srwbook.pdf)
and [Uchiyama publisher page](https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/greens-functions-for-random-walks-onn/080445758FA185A7BFEFB2B6A2E87C05)
were opened. The Fukai–Uchiyama DOI could not be retrieved by the browsing
tool. No external theorem was used to discharge an LGF proof obligation;
the cited works were not audited in full.

All ten source/artifact hashes recorded in `checks/lgf_source_manifest.json`
matched the actual files. Inventory found only the two LGF notes, two briefs,
criteria, earlier review and manifest before this report was created.
There was no numerical runner to inspect or rerun. No scientific numerical
job, interval quadrature, FFT, resource-guard bypass or proof-assistant check
was performed. Executed Python was confined to inventory, hashes and source
identity checks. In particular, this report does not infer the historical
creation order of untracked files from a manifest or file timestamps.

The same-family context and the required exposure to the prior report limit
independence; agreement between reports is not an additional proof. The
decisive evidence here is the checked derivation, its hypotheses, exact
constants and the independent Poisson/curvature identities above.

## Binding fixes and disposition

No binding mathematical fix to LGF.md is required by this review. Before
consolidating its result into TSE55, the following inherited-source fixes
remain binding; they have not been made by this task:

1. **TSE55 194–199:** specify `Delta=8(I-P)`, the Fourier inverse, counting
   mean-zero convention and oriented differences. Retain `c_4=1/(4 pi^2)`;
   a simple-random-walk Green function must be divided by eight.
2. **TSE55 197:** replace the ambiguous torus clause by (5), including
   `T^-2`, `T^-3`, `T^-4` at orders zero, one, two, or restrict that clause
   explicitly to order two. The uncorrected order-zero claim is false.
3. **TSE55 198–200:** replace the image sketch with the grouped local identity
   (32), its quadratic coefficient, and the lattice shell/alias construction
   (19)–(20). Retain the explicit Weitzenböck and gauge-quotient reduction.
4. **TSE55 194, 443–444 and its corresponding status summaries:** replace
   the stale import/ARGUED pointer with the actual reviewed library source and
   review identity. Do not rewrite historical R11 as if its original import
   had been verified then, and do not convert review readiness into audit status.
5. **TSE55 FREE and CODEX_REVIEW_TSE R9's downstream use:** preserve every
   other condition and the separate test-function/Riemann-sum obligations.
   This review supplies LGF only; it does not establish PL-1L, H_int or TS for
   the interacting measure.

Only `REVIEW_LGF.md` was written. No source note, existing check, editable
prompt, audit/ledger file or platform instruction was changed; no commit or
PR was created. Any change to the reviewed mathematical source or its actual
premises requires affected re-review against the source identity above.

VERDICT: LAND
