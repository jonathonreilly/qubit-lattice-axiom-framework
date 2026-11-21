## Repo search

The target-specific `prior/gap-det-check-astra.md` is absent at the pinned
commit `8d50dedaea816db7326453060c96499b1ee0c6ba`. The lead's general
`prior/repo-search-2026-11-08.md` predates row 987. It records related
soft-route and hard-route snapshot work, not this determinant comparison.
Its snapshots are copies, not independent proofs. The relevant source
checks and their distance from this target follow.

The relevant hits were opened from the fetched refs, not trusted from the
digest. Main was `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`.
PR 10141 was `a2f6a430e251aa47bc3eb4f67a1dca2a88530116`, newer than the
digest; its line numbers were relocated. PR 10114 remained
`f76f6c649cff7dffbab664d8976e680e8f287fe9`.

| Hit checked | Closeness and use |
|---|---|
| Main, `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` | A determinant-weighted noncompact Maxwell law with exterior Dirichlet boundary. Its covariance comparison is a different statement, not (DET). |
| PR 10114, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/BARE_COUPLING_MATCH_ASTRA.md:362–375` | A local Haar/saddle prefactor identity on a fixed domain. It does not compare torus determinants. Credit Codex for this existing prefactor accounting; no result is imported here. |
| PR 10141, `research/ym4d/library/out-pi.md:277–349,377–382` | Theorem PI supplies conditional inverse/walk results for literal one-contour rows. The passage explicitly distinguishes them from symmetric contour-family rows. It supplies neither this two-torus theorem nor the missing identification with pr-lay. The earlier method and convention warning are reused, not rederived. |

The lead's digest reports the PR 10133 duplicates and PR 10134 search;
those searches were not rerun. This is a targeted verification of its
relevant hits, not a fresh exhaustive search or an absence theorem.

The registry has no `gap-det`, `I-loc`, or `ID-a` match. FINISH rows 989,
990 and 993 already own the earlier same-provider check and the later
identification/locality work. This file performs only the requested
cross-provider check of row 987. It does not reattack those successor tasks.

Provenance: Codex (OpenAI), 2026-11-15, checking Claude Fable 5.2 medium's
`gap-det-fable.md` at the pinned commit above. Model/effort identifiers are
not exposed in this session. Research text, not an audit; grants no status.
Row 989's requested constant correction was read before this check.
The target's SHA-256 is
`ce8f800ce83e36e3118fea66406def14f0420bc6e217c861d6fb50332b9e8a35`.
Hashes of the read source files are saved in
`/tmp/sa-gap-det-check-astra.TQmjQ9/source-manifest.json`.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for the source mechanism and definitions; Tadeusz Balaban
for the underlying construction; the named repository authors for their
conditional ports. Source assertions are not substituted for proof.

## Checkpoint

1. Check Lemma A, including spectral transfer and the trace remainder.
2. Check Lemma P and Lemma A', including quotient and distance conventions.
3. Check Corollary B with row 989's volume-independent constant.
4. Read the indexed source excerpts behind Step 4 and hm/pr-lay/hma.
5. Check (S1)-(S3), keeping identification and locality owners separate.
6. Record every verdict and one final RESULT line.

Only this file is an intended repository output. Downloads live in the new
scratch directory `/tmp/sa-gap-det-check-astra.TQmjQ9`. The outline and CA-I
were each downloaded once at `31a47c543775`; their line counts are 32,992
and 166,711. No numerical or computer-assisted proof is used.

Completed: the whole 556-line target, its abstract arguments, corrected
constant, cited Step 4 excerpts, and Step 5's conditional application.
The successor locality/identification proofs are outside this check.
The lead's next decision is whether to use this corrected implication
with separately checked inputs. No source statement or status was edited.

## Abstract statements

Line numbers below refer to `gap-det-fable.md` at the pinned commit.

**Lemma A, lines 85–218: HOLDS.** All parts (a)–(g) preserve their
hypotheses. The Schur bounds apply to columns by symmetry, even though
the tilted matrix is not symmetric. The weighted kernel algebra justifies
each exchange of sums in (c)–(d). The infinite-volume quadratic-form bounds
extend by density. They are not applied directly to non-square-summable
periodic vectors.

In (e), for each fixed pair the periodized exponential sum has a finite
bound independent of the power. Hence the estimate on every power of the
finite matrix implies its spectral-radius bound. This proves the claimed
torus gap without an illicit infinite-volume restriction. In (g), the
diagonal average is exactly independent of the torus because `l` divides
`n`. Nonzero wraps have displacement in `n Z^4`; there is no missing
factor of two. The geometric product is

\[
 \sum_{w\in\mathbb Z^4\setminus\{0\}}r^{|w|_1}
 =\left(\frac{1+r}{1-r}\right)^4-1.
\]

Its quotient by `r` increases on `(0,1)`, which proves the printed
`c_eps`. Both trace sums converge absolutely. Remarks 1, 2 and 4 hold;
Remark 3's finite version is proved explicitly as Lemma A'.

**Lemma P, lines 225–247: HOLDS.** A useful direct check is to normalize
the pullback. If `h = (n'/n)^4`, then `U = h^{-1/2} pi^*` is an isometry
onto the invariant vectors. Covariance makes that subspace reducing for
every matrix in the lemma and its transpose. Thus `Per(K) = U^T K U`
on that subspace. Products, transposes, invertible restrictions and the
quadratic-form bounds follow. For rectangular matrices the source and
target actions must both be free actions of the same group, so the fibre
sizes agree. The inverse and positivity clauses concern square matrices.
The stated rectangular extension is read with this necessary typing.

**Lemma A', lines 249–286: HOLDS.** The distance is a pseudometric on
colour coordinates, which suffices. Testing the form on a coordinate
vector gives `gamma <= A'_{xx} <= C_A`, hence `nu <= mu_0/2`.
With `rho(z) = dist(z,x)`, the diagonal
similarity in the proof has the correct sign: its inverse contributes
`exp(nu rho(x)) = 1`, and its right factor contributes
`exp(-nu rho(y))`. Its row and column errors are bounded by `gamma/2`.
Distinct quotient translations have distinct minimal lifts in `n Z^4`;
choosing one at a tie cannot enlarge the lattice sum. The diagonal trace
average uses only Gamma covariance. The stronger `l Z^4` covariance is
unnecessary, as Step 7 correctly says.

For an additional analytic check, use the integral rather than the trace
power series. Set `T = I - A/B` and

\[
 F(A)=\log A-(\log B)I
     =-\int_0^1 T(I-tT)^{-1}\,dt.
\]

The scalar identity follows by integrating `z/(1-tz)` and then applying
the spectral theorem. The same exponential conjugation bounds the
conjugated `T` by `q' = 1-gamma/(2B)`. Therefore the integrand has norm
at most `q'/(1-tq')`, and

\[
 |F(A')_{xy}|\le
 \log(2B/\gamma)\,e^{-\nu\operatorname{dist}(x,y)}.
\]

Lemma P applies to the inverse for each `t`, so `F(Per(A')) = Per(F(A'))`.
Taking the normalized trace leaves precisely the nonzero quotient
translations, bounded by the displayed geometric product. This confirms
the coefficient and the single-wrap error in A'. This is a check of the
same stated implication, not a second source of physical evidence.

**Corollary B, lines 288–311, with row 989's correction: HOLDS AFTER
CORRECTION.** Take the contextual integers `L > 1`, `0 <= j < K`,
and `m,m' >= 0`; the actual lane fixes odd `L >= 27` and much larger
admissible tori. A common `K` and common coupling sequence are essential.
The exact scalar per unit volume cancels before any estimate. Put
`u = K-j`, so the first value is **1**, not 0. The hand calculation is

\[
 L^{4u}e^{-2\nu L^{m+u}}
 \le \frac{5!}{(2\nu)^5}L^{-5m-u},\qquad
 \sum_{u=1}^{\infty}L^{-u}=\frac1{L-1}.
\]

Here `5! / 2^5 = 120/32 = 15/4`. Thus all printed powers of `L` are
correct. The function called `c_det` in row 987 still depends on `m`.
The corrected constant for the quantified (DET) claim is

\[
 C_{\det}=\frac d2\log\frac{2B}{\gamma}\,
 e^{\nu}\bigl[\coth(\nu/2)^4-1\bigr]
 \frac{15}{4\nu^5(L-1)},\qquad
 \nu=\frac{\mu_0\gamma}{2C_A}.
\]

The sharper error is `C_det L^{-5 min(m,m')}`. If a different range allowed
negative `m`, an independent fixed lower bound would be needed instead.
Choosing the coupling-dependent bottom of the range does not itself
remove coupling dependence. Row 989's `L^{-5m} <= 1` repair does.

The corollary proves an implication from (S1)–(S3). Calling (DET)
“exactly” these inputs at lines 313–314 must mean a sufficient reduction,
not an equivalence: (DET) alone does not imply periodization or a gap.

## Step 4: source ports

The outline index was searched first, with neighbouring rows read:
`chunk-07` (gauge, averages, counts, QC15–QC25), `chunk-09` (straightened
rows and pillar averages), `chunk-10` (operator conventions and PX31),
`chunk-20` (RF61), and the matching obligations. The CA full index supplies
`4.24:prf-bond-densities` and `8.22:lem-vacuum-energy-density`.
The `ca-4.12-4.19/README.md` was read; none of its stage assertions is
needed for this flat matrix check.

**YM3 mechanism, target lines 329–344: HOLDS AFTER CORRECTION.** The
source is `YM3/YM3_I.tex` at the row's actual revision `c7fef8b`, downloaded
once into this session's scratch directory. Source lines 40673–40818 give
the statement and log-series construction, including II-44-14 and
II-44-16. The log-series and Moebius-inversion descriptions are faithful.
However, II-44-37 itself is the **difference** from the trivial background;
its terms vanish there. The unnormalized constants are II-45-8,
lines 60813–60849. That definition has three branches, including

\[
 \mathsf n^{(j)}(X,b)=6\log L
 \quad\text{if }b=b_0(c),\ X=X(c).
\]

The formula `n = -E^N/2` in the target is only the nonpivot branch.
Keep the pivot branch when describing the entire normalizer. This changes
no abstract determinant estimate: the added terms are local counting
terms. It does matter to the claim that no elimination factor remains.
The local-chart sentence is at 60846–60849, not 60843–60846.

III-7-12 and its proof were read at 65335–65508. The comparison uses
the same coupling sequence, common local values, cancellation of counting
terms per volume, and a tail bound for noncommon domains. It covers both
Gaussian and regular vacuum terms under its hypotheses. II-192-10,
60870–60876, also includes the restricted Haar/gauge scalar, not only a
Gaussian scalar. The target's use of this mechanism, while replacing its
local-family comparison by periodization, is faithful. No 3D bound is
silently being claimed as a 4D theorem.

**RF61, target lines 345–356: HOLDS.** The downloaded `YM4/YM4_1400.tex`
at `c7fef8b`, 86260–86301, prints exactly the stated determinant, counts
and outstanding targets. The same passage is already in the requested
outline at `31a47c543775`, 22249–22302. It states a target, not a proof
of (S1) or (S2). The bound on the determinant follows from a uniform
spectral interval; the local-family bound and first-step sign do not.
The value of `c_k(theta_k)` and its torus independence must still be
matched when using that formula for the account's actual integral.

**hma D3/D5/Theorem 5, target lines 357–367: HOLDS.** Read hma's
definitions and imports, Lemma 1, and 188–277. D3 is the candidate
precision with the Y gauge term. D5 takes `S = I` for the full Gaussian.
Theorem 5(16) is a conditional one-torus expansion under M; it says
nothing by itself about two unrelated masks or tori. Formula (21)
supplies `(2 pi)^{|I|/2} det(A)^{-1/2}` and the stated scale factors.
Those scalar facts do not require the local expansion (15)–(19).
The new argument therefore does not inherit that entire expansion's
premise list merely by using the same matrix definition.

**Equality with pr-lay, target lines 371–380: HOLDS AFTER CORRECTION.**
The citation to hma D2 is to a nonlinear factor. The precise reason is
hma Lemma 1(4)–(5), together with pr-lay (6)–(9). At `V = 1`, all
reference contours are identity. Hence the relative gauge function is
the absolute soft gauge function, their Hessians agree, and their
gradients vanish. At `J = 0` both current corrections vanish. The
displayed flat form follows. Thus no extra physical Hessian identification
is proved by this algebraic equality.

**hm (4) and pr-lay R/W: HOLDS as conditional ports.** Read hm 1–89
and pr-lay 1–122. The quoted weighted bound, gap and inverse-existence
clauses are faithful. The imported constants already include the colour
norm conversions. The notes explicitly retain their flat, curved,
cut-down and second-jet hypotheses. This check does not prove W merely
because the background is flat.

## Step 5: application and its limits

**(S3), lines 382–391: HOLDS.** CA-II 64638 and 64666 fix bare spacing
`L^{-K}` and physical side `2 L^m`. At step `j` the spacing is
`L^{j-K}`, so the number of sites per direction is `2 L^{m+K-j}`.
The coordinates are level-j bonds, not bare bonds of spacing `L^{-K}`.
The target correctly replaces the artificial constant number of colours
per site by the actual free-coordinate count

\[
 N_{j,m}=d_L(n_{j,m}/L)^4,
 \qquad d_{\rm eff}=d_L/L^4.
\]

Use `d_eff` in Corollary B. The free-coordinate set must descend under
the quotient: blocks, pivots, and gauges on the larger torus must be
pullbacks of those on the smaller one. This is exactly the compatibility
included in (I-loc). Neither the isometric-pullback argument nor the trace
proof requires an integer `d_eff`. The quotient action is free on each
level and has the same fibre size at every level.

**(S1), periodization implication, lines 393–410: HOLDS.** Given one
common local rule for every primitive, apply it to a pulled-back field.
Its complete stencil has the same values before and after projection.
This is the intertwining relation of Lemma P. Products, sums, inverses,
and transposes then preserve it. Inverses are supplied by W, not by
locality. A derivative of a finite-range nonlinear rule is the relevant
linear stencil; its inverse need not be finite range. The proof never
needs such a false assertion.

Physical transposes also need the stated pairings. For a matrix `K`, they
are `W_in^{-1} K^T W_out`, with the fine/row/top measure weights.
On the full flat single layer these weights are constant on each index
set and identical between tori. Lemma P therefore applies to them.
SA PX33, 10681–10685, expressly requires these weight ratios.

**(I-loc) as a supplied reading: HOLDS AFTER CORRECTION.** Keep it as
an explicit common-rule hypothesis, rather than an automatic consequence
of the word “imported.” The inspected definitions support its intended
use: SA QC1–QC4, 7943–8001, use fixed patches; QC19, 8219–8241, makes
the pivot embedding local; the soft gauge at 7178–7183 uses the same
internal contours. The straightened row in 9630–9634 reads a double
block; the pillar average in 9634 and PX31 becomes the ordinary finite
block mean at identity. These are the exact objects, not the different
plain derivative or straight average.

There is one convention to retain explicitly. SA 10139 and pr-lay 74
specify only a *comparable* top weight. Comparability alone does not
specify a common translation-covariant rule on different tori. Adopt
the same local top weight on both tori (the `a = 1` flat specialization
of SA 7187 is such a choice), or retain this as part of (I-loc).
Row 990, `gap-iloc-opus.md:76–86`, already records this distinction.
Its full locality proof is not rechecked or rederived here. All primitive
patches still require the source's embedding room. Passing the spectral
bound from a larger torus does not remove the smaller torus's obligation
to realize the same operator.

**(S1), scalars, lines 412–420: HOLDS for the stated Gaussian, conditional
for its physical identification.** hma (21) gives the full matrix
Gaussian exactly. A common `tau`, frame scale, Haar scalar and gauge
scalar contribute one fixed number per coordinate or cell. The counts
are exact multiples of the number of L-blocks. SA 7493–7499 and
YM4_1400 102652–102656 supply that counting convention and the common
coupling/gauge requirement. No bound on these scalars is needed.
Elimination factors must be included too. For the explicitly defined
outline chart, QC16 and QC25 identify them; for the account's Balaban
integral their matching is (ID), not a conclusion of hma (21).

**(S2), lines 422–442: HOLDS as an implication from R and W.** At
identity the real bound is zero and the representative is axial, so R
gives `gamma = c_L`. Summing hm (4), then using
`dist_1 <= 4 dist_infinity`, gives

\[
 \mu_0=\mu_W/4,\quad C_A=B=W,\quad
 \nu=\mu_W c_L/(8W).
\]

Symmetry gives the same column bound and Schur gives the upper bound.
The stated uniformity is inherited from the imports. It is not proved
anew at identity. The spectral estimates are needed on the larger torus;
the smaller one inherits them through the separately required (S1).

**Repository-form conclusion, lines 444–452: HOLDS AFTER CORRECTION.**
With compatible coordinates, common scalar factors, (I-loc), R and W,
use the corrected constant

\[
 C_{\det}^{\rm repo}
 =\frac{d_L}{2L^4}\log\frac{2W}{c_L}\,
 e^{\nu}\bigl[\coth(\nu/2)^4-1\bigr]
 \frac{15}{4\nu^5(L-1)}.
\]

It is independent of `K,g_0,g,m,m'` when the early inputs are fixed
independently of them. To describe it as depending only on `L,p`, those
early choices must themselves be fixed as functions of `L,p`, as the
lane's order of choice intends. The matrix argument does not supply
unproved uniform input constants. It also does not identify the physical
normalizer simply by calling its precision the step form.

## Failing assertion and successor boundary

**“No elimination factor,” lines 483–484: FAILS.** This is the first
false assertion found; no failure was found in Lemmas A, P or A'.
SA QC16, 8191–8199, has `J_c(I) = L^{-3} I_3`. QC25, 8320–8349,
retains `prod_c det(J_c)^{-1}` on the constrained fibre. Thus each coarse
bond contributes `L^9`, since `det(L^{-3} I_3) = L^{-9}`. A full torus
has no fixed exterior, but its block-average constraints still eliminate
pivots. This is a hand-checkable nonunit factor at the stated background.
There is no conflict with a Gaussian integral expressed in normalized
coordinates: that integral has already factored out the elimination
Jacobian. Omitting that prefactor from the physical normalizer is the
error. It is harmless for the two-torus density only after its identical
per-cell rule is retained.

CA-I 3769–3776 defines the normalizer by reference to Balaban; CA-I
106091–106165 also transcribes a determinant **plus** the sum of
`log z^(k)(c)` and measure constants. Therefore the statement that the
account supplies nothing beyond a citation is too broad. This
transcription narrows (ID), but does not by itself prove equality with
pr-lay (7). SA 10200–10208 sketches that physical identification and
points to Balaban's background expansion. It is distinct from the
algebraic hma/pr-lay equality checked above.

The historical claim that the papers are absent is no longer true:
`cmp109.txt`, `cmp119.txt`, `balaban_cmp109_249.pdf` and
`balaban_cmp119_243.pdf` exist in the permitted paper folder. No formula
was taken from their OCR, and no scan was needed for this row's check.
The later `gap-iloc-opus.md`, `gap-idab-opus.md` and
`gap-idab-check-opus.md` already cover that reading/identification task.
I stop at that ownership boundary. This report neither endorses nor
reopens those later proofs, and does not label their inputs resolved.

## Verdict record

| Statement in row 987 | Verdict | Scope |
|---|---|---|
| Lemma A | HOLDS | Its stated infinite-lattice hypotheses. |
| Lemma P | HOLDS | Matching free quotient actions and the appropriate pairings. |
| Lemma A' | HOLDS | Exact periodization, gap and exponential row bound. |
| Corollary B | HOLDS AFTER CORRECTION | Row 989's `C_det = c_det(0)`; powers of L unchanged. |
| Step 4, YM3 port | HOLDS AFTER CORRECTION | Restore the pivot branch and distinguish the normalized difference. |
| Step 4, RF61 port | HOLDS | A stated target, not a supplied determinant estimate. |
| Step 4, hma D3/D5/Theorem 5 | HOLDS | Conditional one-torus statement; only the matrix/scalars are used. |
| Step 5, hma/pr-lay equality | HOLDS AFTER CORRECTION | Cite hma Lemma 1(4)–(5), not D2 alone. |
| (S1), periodization | HOLDS | As an implication from the explicit common-rule input and W. |
| (I-loc), claimed definition reading | HOLDS AFTER CORRECTION | Preserve the top-weight, gauge, pivot and embedding conventions. |
| (S1), scalar counting | HOLDS | For the stated matrix Gaussian with common factors; account matching is (ID). |
| (S2) | HOLDS | Conditional on R and W; neither import is discharged. |
| (S3) | HOLDS | Use `d_L/L^4` and compatible pivot patterns, as row 987 specifies. |
| Repository-form (DET) | HOLDS AFTER CORRECTION | Corrected constant; all supply/identification conditions retained. |
| Step 6, no elimination factor at identity | FAILS | QC16/QC25 leave a nonunit pivot factor. |

No numerical job, machine enumeration, Lean run, audit, status change,
paper copy into the checkout, or outward posting was performed. Shell
commands fetched/read sources and inspected bookkeeping only. The
research output remains uncommitted and unpushed on
`codex/gap-det-check-astra-20261115`.

RESULT: Lemmas A, P and A' HOLD; Corollary B and the repository-form (DET) HOLD AFTER CORRECTION with row 989's m-independent constant and the stated inputs. The Step 4 ports need the pivot-branch and citation clarifications above. The claim that elimination factors disappear at U = 1 FAILS. This check supplies the conditional matrix comparison, not an unconditional (DET) for the account's physical normalizer; later locality/identification work retains its owners, and R/W are not discharged.
