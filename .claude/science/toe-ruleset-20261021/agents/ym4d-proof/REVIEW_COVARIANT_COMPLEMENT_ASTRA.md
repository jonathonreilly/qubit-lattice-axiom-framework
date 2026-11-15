# Independent review of fixed-coarse-field cut boundary layers

**The frozen bounded theorem is supported.** The original-product-Haar cap,
local conditional-density estimate, elementary shell bounds, and their
specified returned-gas and raw complex-source extensions are valid at the
stated scope. No binding source repair is required. This review grants no
whole-PR disposition, audit status, continuum existence, or physical mass gap.

Reviewer: fresh restricted-input Astra/max context, 29 October 2026. This is
same-family review, with no authorship of the target and no cross-family
claim. The reviewed [source](COVARIANT_COMPLEMENT_ASTRA.md) is SHA-256
`af4c8206ccc2ce86274e5f92643e28154abb010b7f413d5cf578035efb1eaa7b`.
Its [author receipt](checks/covariant_complement_receipt.json) is SHA-256
`a9536686abb45d8f5fae790fd0c7685ce159a1a0f961cd8cdcd5145fb31d22d4`,
and its [read manifest](checks/covariant_complement_read_manifest.json) is
SHA-256 `57b7e15eb8d0bb48f9966265e09852a61a334e811e6432554175a3f7ade89f44`.
The [review receipt](checks/review_covariant_complement_receipt.json) binds
this report, exact source/input identities, [reading coverage](checks/review_covariant_complement_read_manifest.json),
[initial checks](checks/review_covariant_complement_entry.json), and executions.

## Exact accepted scope

Fix d=4, SU(N), N>=2, odd L>=3, T>=2, u>=1, the stated compact positive
kappa interval, and normalized probability Haar on every original positive
fine link. Coarse V and all frozen fine links are arbitrary real group
variables. The cut is precisely H3's product of interior-plaquette cuts;
it is not the stronger all-plaquette/root-mismatch event or SA's white sector.

The block estimate requires the explicit smaller cut ceiling CC7 and has
degree `(N^2-1)4L^3(L-1)`. The crossing-edge estimate has degree `N^2-1`
and requires no CC7 ceiling. The real-source local density argument allows
any fixed finite R in `|epsilon_p|<=R`; application of the returned gas also
requires H20c's smaller source domain, H21/H21a's u threshold, and H15's
completion constants for that same epsilon_1. Shell estimates retain
`tau>=0`, `eta>0`, and `tau+eta<=delta_H`. Their constants may be extremely
large at fixed N,L,epsilon_1; no practical coupling threshold is inferred.

For a retained failure collection F, the extension applies only when the
complete endpoint-block set of the integration witness avoids the full
union of failure collars. A bounded nonnegative exterior insertion may be
arbitrarily correlated but must be independent of the integrated variables.
At complex sources the result is a raw absolute envelope relative to the
positive history mass at `Re(epsilon)`. It is not a normalized complex
probability or nonvanishing theorem.

## Independent proof reconstruction

### Actual kernels and their complete readers

I checked the S4-prime path and arithmetic-mean definitions in PROOF's
setting and Decision-4 kernel, H1–H5, and CB1–CB4. Canceling the common
`exp(-kappa u)` in numerator and normalizer gives exactly CC1. Every root
leg stays in its own endpoint block; no polar mean, hard block constraint,
or selected chart has replaced the compact kernel.

For a differentiable mean, differentiation under the positive compact
normalizer gives its actual tilted expectation. Both the numerator derivative
and the expectation are bounded by `t||dot M||op`, so their difference is
bounded by `2t||dot M||op`. The estimate remains valid at degenerate means
and does not select a maximizer. Unitary word differentiation counts every
occurrence, including inverse or repeated occurrences. Each edge meets six
Wilson plaquettes, and the only kernels reading an internal edge have its
block as an endpoint: at most eight. The resulting CC5 constant is a safe
upper bound. Successive shortest group geodesics may leave the cut; this is
harmless because the smooth density and its modulus are defined on the
whole compact link space.

For a crossing edge, only the straight segment of the coarse link through
that specified face can use it. Fixing its three transverse offsets leaves
L choices of longitudinal offset and all 24 paired orders. Each word uses
it once, giving `24L/(24L^4)=L^-3`. At T=2 the opposite coarse-link label
uses the other block face, not an added far seam of the induced vertex graph.
This proves the single-reader CC6 bound and checks the actual periodic
consumer rather than an abstract finite-range kernel.

### Nonabelian cap and the polynomial denominator

For the complete axial tree, the off-tree loop is filled by commuting the
single edge step past the later-coordinate suffix. There are at most
`3(L-1)/2=A` elementary exchanges. With negative coordinates the step may
cancel an inverse step after these exchanges; the same bound holds. Each
exchange is an actual conjugated plaquette, all within the block. Telescoping
products of unitaries gives `||I-W_e||op<=A epsilon_1`. This argument never
uses an abelian Stokes formula.

CC7 gives both an injective small logarithm and its tracelessness. Indeed
`||log W_e||op<=2A epsilon_1`, so the sum of the N eigenangles has absolute
value at most `2NA epsilon_1<=pi/4`; because it is a multiple of 2pi it is
zero. The principal-log central branch cannot enter. All tree-edge logs
vanish.

For an actual four-edge plaquette after contraction, let
`s=sum_edges ||a_e||op<=8A epsilon_1<=1/4`. The product derivative bounds
`||P'||<=s`, `||P''||<=s^2` and the convergent logarithm series give
`||F''||<=s^2[(1-s)^-1+(1-s)^-2]<=6s^2`. Since F(0)=0, the elementary
zero-endpoint Green kernel bounds
`||F(t)-tF(1)||<=192A^2 epsilon_1^2 t(1-t)`.
The ceiling `epsilon_1<=1/(384A^2)` makes this coefficient at most
`theta_1/2`, with `theta_1=2 arcsin(epsilon_1/2)`. The operator-norm cut is
exactly the principal-angle cut, and integrating the sine derivative yields
the simultaneous CC10 margin. Degenerate extremal eigenvalues cause no
problem: only operator norms and monotonic scalar inequalities are used.

At `t=1-32r/epsilon_1`, transforming back by the same fixed vertex gauges
moves each link by at most `64 sqrt(N) A r` in the HS group metric and leaves
plaquette slack at least 8r. Perturbing each original link by distance less
than r loses at most 4r. Thus the entire product cap, including tree links,
lies in the strict original cut. No crossing link or fixed V is transformed.
The gauge operation constructs a cap center; it is not a change of integration
variables and needs no quotient Jacobian or omitted gauge-volume factor.

In the exponential Haar chart, the differential of exp acts trivially on
Cartan directions and by the stated sinc determinant on each real root
plane. The given small HS radius is injective and supplies the positive
`c_H r^D` group-ball bound. Translating each ball preserves its Haar mass.
All `n_l` original links therefore contribute, giving the product volume
power `D n_l`, not a gauge-reduced dimension.

The density has a maximizer on the compact closed cut. Its cap has radius
`r_0/(1+u)` and is within the stated `O(r)` link distance of that maximizer.
CC5 bounds its logarithmic density loss by a fixed constant because
`u/(1+u)<=1`. Dividing the maximum density by this explicit lower bound for
the local integral proves CC12–CC13. The same construction on the unrestricted
crossing group proves CC14. This comparison uses neither a lower bound for
the global cut partition function nor a selected-sector denominator.
Conditionals under the global measure are needed only almost everywhere;
local formulas remain well defined for arbitrary prescribed exterior data.

### Shells, gas tilt and the exact source envelope

For `tau+eta<=delta_H`, the principal log is traceless and maps the group
shell into the difference of two homogeneous op-norm balls in real
su(N), dimension D. Their volume difference is bounded by a constant times
`eta(tau+eta)^(D-1)`, also when tau<eta. Smoothness of an operator-norm level
set is unnecessary. Every actual elementary plaquette has a witness edge
occurring once, and a root-straight path has a unique crossing witness.
Holding the other word variables fixed reduces its holonomy or mismatch to
`A U_e^(+/-1) B`, which preserves Haar. For an interior witness, CC13 first
bounds the density with respect to the complete block's product Haar and
Fubini then integrates the one-edge shell. This establishes CC16 for the
actual law, including seams.

I read H's complete argument through H28 and the matching independent H
review. At real sources, its zero-source denominators are positive; its
numerator, source compensator and selectors give `a_Y,f_Y>=0`. The actual
finite returned gas has coefficient-one products and an empty term, so
`G_ret,F>=1` before any logarithm is invoked. H23–H25 supply the convergent
logarithm with full connected collar unions X and the stated uniform rooted
bound. At real sources the connected coefficients are real. Changing B can
affect only X meeting its endpoint blocks K_B; hence

`osc_B log G_ret,F <= 2 sum_(X intersects K_B) sup|V_X^F| <= 2|K_B|d_q`.

The ratio of the largest to smallest gas tilt on a reference conditional
fiber is at most this exponential. If K_B avoids all retained failure
collars, every factor in R_F and R_out is fixed on that fiber. Normalizing
the tilted conditional therefore costs at most `exp(2|K_B|d_q)`, proving
CC19. This uses full reader supports, not polymer cores, and it requires no
differentiation of the hard completion indicator. A zero total history mass
produces the trivial raw inequality without division by zero.

For complex epsilon and e=Re(epsilon), taking absolute values inside the
original positive Haar integrals gives `|N^epsilon|<=N^e`. The compensator's
modulus is exactly its value at e, so the same inequalities hold for t,a,f.
The finite gas polynomial and the original density give CC20 by the triangle
inequality. CC21 follows from the real bound with the identical positive
history mass at e. No source-vacuum term or total-volume source cost is lost:
replacing that mass by its zero-source value would require an additional
estimate, and is expressly not done.

At E=1 and R_out=1, CC18 is exactly the original H14 numerator after
canceling the common Z_cut^0 representation. For a nontrivial insertion,
CC18 measures the event on the all-cut sea representative. If an event reads
a replaced successful interior, H8 requires it in the joint bad-interior
replacement integral to identify an original pre-return event. CC18 states
this distinction correctly. No new identity for such events is supplied or
inferred by this review.

CC22 is the deterministic union bound for disagreement of finitely many
hard tests. It pays the number of tests and their actual union of readers.
It supplies no exponential support-size estimate after a radius-R ball
localization. The nonlinear minimum defining h_Y is not an elementary word
shell and remains outside CC15–CC16. CC23 follows independently from
`||M||_nHS^2<=m<=||M||_nHS` and the exact squared-distance identity; it is a
pointwise variance/alignment comparison, not a complement or reference price.

## Numerical evidence and failure accounting

The [reviewer criteria](checks/review_covariant_complement_criteria.md),
[implementation](checks/review_covariant_complement_independent.py), and
[first output](checks/review_covariant_complement_independent_01.stdout.json)
were completed before reading the author checker or its criterion file.
I had already seen the target and its quoted aggregate results, including
the failed shell ratio; this was not a blind review. No author helper was
imported. The subsequent [exposure/replay record](checks/review_covariant_complement_after_exposure.json)
distinguishes independent checks from reproduction.

The independent run passed **19/19** named predicates, including four
mutation predicates. These are aggregated finite checks, not 19 theorems
or four separate mutated-program executions. It tested:

- Noncommuting SU(3) and SU(4) L=3 blocks at curvature just below the CC7
  boundary, with large vertex gauges. Recovery error was below 4.3e-15;
  every tested contraction and full-original-link cap retained its margin.
  Contracting ungauged principal logs instead produced defects near 2.
- Literal signed paired words for every coarse link at L=3,T=2. All 1,728
  crossing edges had one reader and incidence 72/1944; all 3,456 internal
  edges had at most eight endpoint-block readers. All 5,184 positive fine
  edges belonged to six distinct plaquettes.
- Exact compact SU(2) normalizer derivatives from full sphere quadrature
  versus the independent Bessel formula, at t=.5,3,20. Errors were below
  9e-14, and the 2t modulus held. Omitting the normalizer changed the
  derivative by up to .978. Exact Haar cap volumes exceeded the HS-chart
  lower bound; using a flat one-angle measure changed the .1-radius mass
  by a factor about 300.

After inspecting the complete author main/post-hoc code, criteria, launcher,
outputs and failure records, I replayed both programs with only their output
basenames redirected into reviewer-owned files. Seeds, formulas, thresholds
and exit handling were unchanged. Every main mathematical record matched
exactly; only elapsed time differed. The main replay remains **23/24, exit1**,
with six detected mutations. At u=40 the ratio for widths .015 and .0075 is
still **2.463807379243857**, outside [1.85,2.15]. This falsifies that auxiliary
finite-width expectation. It does not falsify CC16's upper bound with a
u-dependent coefficient, which asserts no factor-two ratio. The separately
labelled post-hoc narrower-shell replay is **3/3**, with ratios 2.028365892
and 2.007083710. It does not repair or overwrite the failed criterion.

The author's pre-mathematical Darwin resource-limit rejection remains in its
original empty stdout, stderr and resource records. Its mechanical Markdown
parser failure remains separately recorded. Neither is counted as a
mathematical predicate. The reviewer's initial optional psutil preflight also
failed before any mathematical execution; the [record](checks/review_covariant_complement_environment_probe_failure.json)
preserves this, and native Darwin memory/RSS checks supplied the replacement.

All three reviewer mathematical executions passed the read-only coordinator
lock, native `memory_pressure -Q` free-memory gate, load<20, nice15, and
one-thread gates. Peak observed RSS was below 69 MiB; runtimes were about
2.27s, 1.45s and .24s. The 90-second CPU/wall and 300-MiB RSS limits were not
reached. These non-interval finite diagnostics challenge implementation and
normalization; the written arguments above supply the quantified theorem.

## Literature and remaining interfaces

The source correctly credits Balaban and Dimock while rebuilding the
finite-dimensional nonabelian cap and Haar estimates. I refreshed
[Dimock's axial-gauge introduction and sections 2.1–2.2](https://arxiv.org/html/1410.2798v3):
its stated gauge fields are abelian and its main application is d=3. It
supplies context rather than the present nonabelian cut-domain proof.
[Balaban's original CMP116 introduction, printed pages1–2](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf)
explicitly separates localization of the fluctuation action from its
exponentiated expansion; I read that scan's extracted text, not a summary.
The DOI endpoint failed in this pass, and no whole-paper read or PDF-byte
hash is claimed. [Dimock's scalar large-field paper, Appendix F](https://arxiv.org/html/1212.5562v2)
requires independent site fluctuations and small localized interactions.
The present interacting cut law has not been shown to meet those hypotheses.

Actual consumer reads confirm the source boundary. Sea11–Sea16 integrate V
with its own cut reference; they are not fixed-V bounds. HIST's joint return
integrates next-level interiors, unlike the current-fine-link conditional
here. PLD9.4 requires a normalized localized sea logarithm and derivatives.
LARGE55 I3/I5 and E13/E14 require the returned action, the reference-region
price and the allowed small boundary cost. None is discharged by a positive
conditional denominator. SA4 and SA30–SA33 remain separately scoped selected-
sector arguments; their independent review was pending at dispatch, and no
SA theorem is a premise of CC4–CC21.

Still missing are the full hard-cut complement estimate, boundary control
for the optimized completion selector, all retained-failure prices, support-
size localization through whitening, the normalized source-sensitive sea
integration with complex nonvanishing, and matching higher-level action and
source returns. Nonlinear RG, continuum existence and a physical continuum
spectral gap remain open. The elementary limits here do not constitute a
no-go theorem for other routes.

During final packaging, the shared literature register changed after the author
freeze. The original author pin was verified at review entry; it is preserved,
not restamped. The consumed B03/B06/B07 statements were read again and remain
unchanged. Current SA/UL review-status rows are not new mathematical inputs to
this review. The [failed pin check](checks/review_covariant_complement_packaging_failure01.json),
[current register snapshot](checks/review_covariant_complement_literature_current.txt),
and [visible worktree delta](checks/review_covariant_complement_literature_worktree_diff.txt)
are retained. All 21 author artifacts and the other 14 pinned inputs remain
exact. No mathematical re-execution is justified by this context-only change.

This is one source-review iteration, with zero binding source findings,
zero author fixes, no skipped binding defect, and the explicitly preserved
failed auxiliary numerical expectation. Model data and normalization are
supplied mathematical hypotheses, not new physical primitives. The evidence
is not Nature-grade retention or an audit verdict. Repository-wide combined
validation, current-main preservation, complete PR10114 disposition and any
landing decision remain with the coordinator; they were not executed or
claimed by this unit reviewer. No commits, pushes, source edits, audit writes,
ledger changes or shared-status changes were made by this reviewer.

**VERDICT: LAND**, solely for the frozen bounded original-law boundary-layer
unit and its stated hypothesis/consumer restrictions.
