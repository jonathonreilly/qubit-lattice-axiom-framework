# Independent mathematical review of LGF

Date: 2026-10-29. Reviewer: a fresh Codex context that authored none of
`LGF.md`. This is **same-family review: Codex reviewing Codex**. The review
reconstructed the estimates and supplied alternate checks of the polynomial
coefficient and kernel signs; shared model family and source material remain
correlation limits. There was no numerical experiment, interval computation,
proof-assistant run, or imported theorem used to establish the verdict.

**Finding: no blocking mathematical defect in the reviewed final note.**
All four author-brief targets are supported under the stated graph-Laplacian,
counting-inner-product, base-point and zero-mode conventions. The one finding
was an editorial locator error at `LGF.md:559`: the R9 quotation is at
`CODEX_REVIEW_TSE.md:142`, not line 141. The coordinator corrected that line
in place during this review. I read the correction and verified that reversing
that single replacement reproduces the original frozen SHA-256 exactly.
There are no other changes to the reviewed mathematical note.

Here **LAND means mathematical readiness for lane consolidation only**. It
does not authorize a commit, PR, publication, audit, retained status, or
adoption into the inherited TSE55 files. This review changed only this file;
it changed no editable prompts or platform instructions.

## Source identity and scope

All lane paths below are relative to
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.

| Source | SHA-256 |
|---|---|
| **LGF.md, final reviewed revision** | `40ea604c79f17027129628bc8b31f5fd6209da21dded864bf45a422dad24505e` |
| LGF.md, original frozen revision | `53d82728c0bb478d259726c2043f6ed3a075866dd44a3cb67d16b8d7b5902fd7` |
| LGF_LOG.md, read before completion bookkeeping | `138e49deb73f05ef0b343d24bb2373329f9b35ea8fb1bb275df9de1b142cf772` |
| PROCESS_LIGHT.md | `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab` |
| briefs_lgf/AUTHOR_BRIEF_LGF.md | `dc358ffa750b051d70afd4fc34f56d68f1b7b3ecca5c4e5d289adb38ee38dd2c` |
| checks/lgf_criteria.md | `9c1c6fd66a7490d863dbdc08395b456246d12d8c2f3aaedd19b6cf97167e4729` |
| TSE55.md | `d02cc8b265c20da5fc59812a59d68e12d3c9a550d9f9df0890db1c61a38f7340` |
| CODEX_REVIEW_TSE.md | `b70b1236e525fe5e3c83cd99b9f7142801a0a215f7e4a34879cdca50917d3edf` |
| LINEAR_PACKAGE.md | `0a2649ff5dbda9963a65ac62770a831d5e9737b9694ea873f28f008496e8e7ad` |

Working HEAD was `fcdd32c83bc5aed08ef4f3aa5da512e668d8b216`; the local
`origin/main` ref was `ca2bc7ddf64790da96cd43d42017d000fbfe4808`.
I used the physics-claim-reviewer skill and proof-search-governance reference
from that main revision, after reading the installed skill and checking the
applicable source. Their SHA-256 values were respectively
`9a8c01717424c8c5c7b0420cd38a68c80179ae518b88591fe926dd21486096af`
and `be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258`.
The working `SCIENCE_WORKFLOW.md` matched main, SHA-256
`71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`.
The prior author reported successful fetches; that report was read, not
independently verified by this reviewer. The coordinator later confirmed an
observed main-fetch exit status of zero, but the initial planning-fetch result
was truncated and unverified. A final `ai/execution` refresh failed with exit
255 because opening `FETCH_HEAD` was denied. Planning freshness is therefore
unverified; the local planning ref read was
`56c5c0ab64f532c5784e895b2f9aa6894fa334e0`. This reviewer performed no remote
fetch and wrote no repository metadata. This provenance correction changes
neither the reviewed proof hash nor the mathematical verdict.

Read in full: LGF, its frozen log, process, author brief, criteria and reviewer
checklist. Also inspected the source-identity manifest, TSE55 lines 176–208,
its §6.3 and explicit base-point declaration at line 225; R9 and R11 in
CODEX_REVIEW_TSE; and LINEAR_PACKAGE §1.1. The verdict covers LGF's mathematics
and its stated scalar input to FREE, not the other arguments in those files.
Future log/manifest completion bookkeeping does not change the mathematical
source bound above; any substantive source change requires affected review.

## Verdict by author-brief item

| Item | Verdict and evidence | Required mathematical fix |
|---|---|---|
| Operator, normalization, torus, differences (brief 15–20) | Confirmed. LGF 14–56 and 490–515 give the positive graph Laplacian, forward/backward differences, zero-mean inverse, and componentwise Hodge operator. Its symbol has quadratic coefficient one, so `c_4=1/(4π²)`; the inverse of `I-P` is eight times this Green function. Matches LINEAR_PACKAGE 57–60 and TSE55 194–201. | None. Preserve these conventions in consolidation. |
| (i), infinite lattice (brief 23–25) | Confirmed for every ordered oriented difference of orders 0–2, including repeated directions and origin-crossing stencils. LGF 58–214 and 316–346 establish the bound with `2^1000`. | None. |
| (ii), order-two torus (brief 26–28) | Confirmed, uniformly for every integer T with nonempty domain. LGF 216–314 proves the estimate through shellwise periodization and heat comparison; 348–433 separately proves the image-orbit prescription and exact quadratic correction. | None. Do not replace the prescribed grouping with a raw image sum. |
| (iii), corrected orders zero and one, counterexample (brief 29) | Confirmed. LGF 245–314 gives the `T^-2` and `T^-3` terms; 435–486 gives a valid local summation-by-parts contradiction to the uncorrected order-zero assertion. | None. The refutation is confined to that quantified estimate. |
| (iv), exact consumer and gauge reduction (brief 30–32) | Confirmed. LGF 488–548 supplies the exact discrete kernel, `D=-X/(4π²)`, the requested `O(r^-5)+O(T^-4)` statement, and FREE's squared-kernel error. | None. FREE's other hypotheses and Riemann sums remain separate. |
| Explicit constants, proof method, hidden imports (brief 34–38) | Confirmed by the reconstruction below. The quartic anisotropy is retained, not falsely canceled. No cited literature theorem is a proof leaf. | None. |
| Optional numerics (brief 40–46) | Omitted as declared. The LGF check inventory contained criteria and source bookkeeping, not a numerical runner. No scientific computation was run in this review; no numerical resource guard was bypassed. | None; no numerical acceptance claim is made. |
| Consumers, residue, binding wording fixes (brief 48–54) | Correct, with the R9 locator finding now fixed. LGF 550–605 distinguishes the library result from the interacting and retained-status obligations. | Implement the listed inherited-source fixes only in the later authorized consolidation. |

## Reconstruction of the load-bearing estimates

### Fourier subtraction and constants through order eight

At LGF 86–100, putting `δ=q-λ` yields
`1/λ-1/q=δ/q²+δ²/(q²λ)`. The sixth-order Taylor remainder contributes
at most `q/360`; the last term contributes at most `q/36`, giving exactly
`11q/360`. The decomposition `Q_4=q²/2+H_4` follows from the two displayed
Laplacians. The note correctly does not use cubic invariance to eliminate
the directional degree-zero term.

For LGF 113–151, the reciprocal induction is valid for arbitrary multiindices:
grouping the Leibniz terms by derivative order gives the factor
`64 Σ_{k=1}^n 1/(k!128^k)<1`. Away from the origin the corresponding factor
is bounded by `256 Σ_{k=1}^n 1/(k!512^k)<1`.
In the three-factor product for `(q-λ)/(qλ)`, the derivative-order sums are
bounded by `128 n!512^n r^-n`; even at n=8 this is below `2^130 r^-n`.
The Gaussian derivative polynomial has the stated powers of t after setting
`u=√t y`, and the stated term-count bound is more than sufficient for `2^100`.
For aliases, `|p+2πl|≥π|l|` for every nonzero l in the chosen cell.
The split exponential supplies `exp(-t/16)` on the two claimed domains;
`2^104·5!·16^6<2^137`. Thus both bounds in (9), including the zeroth
derivative and alias constant, have ample explicit margin.

The C^12 cutoff is genuinely C^12 at its junctions: its derivative is
proportional to `s^12(1-s)^12`. The normalization follows by integration by
parts, and the coefficient/chain-rule bounds imply (12). For the outer
multiplier, independently of the small-r estimate (13), the elementary
bound `|∂^βQ_α|≤4·2^n` suffices. This also fits the ledger for (14).
All periodic boundary derivatives needed in the eight integrations by parts
match. The compact shells have no boundary terms. The resulting two bounds
combine into (15), and the dyadic ratios are precisely `2^(-4-m)` and
`2^(-4+m)`; the latter is at most 1/4 for m≤2. This verifies (16), including
x=0, rather than only a formal symbol asymptotic.

### Discrete periodization, aliases, and torus uniformity

LGF 216–243 uses absolute Fourier convergence for each individual shell,
not for the unsplit order-zero image sum. Finite Fourier orthogonality gives
(17) with the stated sign convention. Grouping the continuum Fourier modes
by their class modulo T leaves the nonzero modes `k=Tl` in the discrete
zero-frequency class. Their contribution is **positive** `T^-4 a_*` in
`f_T`, hence **negative** `-T^-4 a_*` in `E_T`. This confirms (19) and its
disappearance under positive-order differences.

For (20), shells with `ρT<1` have no supported grid frequency; their errors
sum to at most `2^641 T^(-4-m)`. For `ρT≥1`, the image distances satisfy
`|x+nT|≥3T|n|/4`. The count of points in a supremum-norm shell is
`64k³+16k≤80k³`, so `Σ|n|^-8≤100`. In particular
`100(4/3)^8<2^10`, justifying the displayed `2^650` image constant.
The remaining geometric sum and outer term fit inside (20). For m≥1,
the same absolute dyadic coefficient majorant underlying (16) dominates the
partial sums, so the asserted interchange with the ordinary image sum is
valid. At m=0 the prescribed shell order and alias constant remain essential.

LGF 273–314 covers shifted stencils even when T=4: every sampled continuum
point has norm at most `T/4+2≤3T/4`. Thus a nonzero image is at distance at
least `T|n|/4`. In (22), the one-dimensional Gaussian sums give a product
less than `2^21`, the remaining s-integral is at most `2^16`, and the heat
prefactor is 16, yielding `2^41`. The periodic large-time tail has the
explicit Fourier factor in (23); the infinite-volume heat tail is at most
`16 T^(-2-m)`. These calculations also justify the interchanges and (24).
No lower bound on T beyond the stated T≥4 was silently used; for T<4 the
integer domain of (5) is empty.

### Infinite-volume comparison and small stencils

The sums of absolute radial-derivative coefficients at LGF 321–326 are
`1,2,10,72,696`; in particular the fourth-order sum is
`384+6·48+3·8=696`. They are bounded by (25). For r≥4 the whole difference
stencil stays at distance at least r/2. Its displacement error is bounded
using at most two integrals of an order-(m+1) derivative, within `2^20`.
In (26), heat substitution produces
`16·8^(1+m/2) r^(-2-m) ∫_{r²/8}^∞u^(m/2)e^-u du`.
Splitting the exponential and using `r²e^(-r²/16)≤16` gives the claimed
`2^30` margin. At small r the direct positive Fourier integral bounds
`G(0)<2^12` without differentiating a singular continuum function across
zero. All resulting constants fit below the separate `2^1000` summands in
(4) and (5).

## Independent checks of the orbit polynomial and curvature signs

For LGF 362–388, a signed-permutation orbit has isotropic second moment.
In the Hessian of `c_4|y|^-2`, the `8/4` and `-2` terms therefore cancel
exactly. Inversion cancels first and third Taylor coefficients. Taylor's
fourth derivative and `|z|<T/2` give the displayed absolutely summable
`|n|^-6` remainder. Differentiating once and twice leaves corresponding
third- and second-order Taylor remainders governed by the same fourth
derivative. Third derivatives of the original images are themselves
absolutely summable as `|n|^-5`.

The heat-integral check at LGF 390–399 is valid: its integrated third
derivative is bounded by `2^30|y|^-5`, so Fubini applies to the entire image
family at a nonsource point. All third derivatives of `K_T-S_T` vanish.
Connectedness of the punctured four-dimensional ball then implies a single
quadratic polynomial; signed permutations leave only `C_T+b|z|²`.

As an alternate local check of b, let `H=K_T-Φ`, which is smooth at zero.
The background equation gives `Σ∂_j²H=T^-4`. Cubic symmetry forces
`Hess H(0)=aI`, hence `a=T^-4/4`. The regular orbit series has zero Hessian
at zero by its fourth-order remainder. The polynomial must consequently
have `b=a/2=1/(8T^4)`, with a **positive** sign. Independently,
`Δ_lattice|x|²=-8`, so this same coefficient produces the required negative
background `-T^-4`. Every oriented second difference of the polynomial is
`δ_ij/(4T^4)`. The heat scaling and bound for C_T in LGF 411–415 are valid;
the small-time image estimate used there is bounded by the same positive
integral as (22). This corroborates (32), not merely its big-O consequence.

For LGF 490–522, exterior multiplication and contraction give the scalar
Hodge operator directly. At a nonzero mode, write `q_j=e^(ip_j)-1`.
Then `d=q∧`, `d*=ι_bar(q)`, and
`q∧ι_bar(q)+ι_bar(q)q∧=|q|²`. Thus `dΔ^-1d*` is exactly the orthogonal
projector onto exact two-forms. On the link space orthogonal to q, the
ungauge-fixed quadratic operator is already `|q|²I`; Feynman gauge only
adds the gauge direction, which contributes no curvature. This checks the
gauge-quotient identification without a physical gauge-invariance import.

An independent position-space sign check starts with
`Cov(A_ν(x),A_σ(y))=δ_νσG_T(x-y)`. A forward y-difference is a **negative
backward z-difference**. Expanding the two curls therefore yields exactly
the four signs in (39). As a separate discriminator, for a fixed plane at
coincidence cubic symmetry and the zero-mode equation give
`𝔊^F_{μν,μν}(0)=(1-T^-4)/2≥0`; reversing the leading sign would fail this.
In the continuum at `z=re_1`, the diagonal entries for planes 12 and 23 are
respectively `-1/(π²r⁴)` and `+1/(π²r⁴)`. These agree with `-X/(4π²)` in
TSE55 180–185 and its reflection-tensor form.

The base points match TSE55's explicit declaration at line 225. Four
applications of (5) give (41). For its square, if `B=2^1002`, the error
square is bounded by
`B²[r^-9+(2+1/256)r^-4T^-4]`, using r≥1 and r≤T/4.
The cross term is at most
`2^1015[r^-9+r^-4T^-4]`. Thus the stated `2^2010` squared-error constant
is sufficient. The physical-spacing conversion also follows by homogeneity.

## Counterexample, remaining obligations, and fixes

LGF 442–486 supplies an admissible nonnegative C^4 test: its support has
strict margins inside the annulus, and for T≥64 all neighboring sites remain
inside the domain of the hypothetical estimate. The centered stencil kills
the continuum second-order term of Φ, leaving an explicit `O(T^-6)` error.
The test's discrete Laplacian is `O(T^-2)`. Under the proposed uncorrected
bound, one summation-by-parts side tends to zero as `O(C/T)`; the other tends
to `-∫φ<0`. Arbitrary extension outside the common local stencil does not
affect this identity. The bounded-derivative Riemann-sum error also tends
to zero with the displayed constant. This refutes only the uncorrected
order-zero torus estimate. It neither proves that an order-one correction
is optimal nor rules out any Yang–Mills construction, and the note makes
neither claim.

No mathematical fix or unresolved proof leaf remains in LGF's stated scope
as assessed by this review. The R9 locator correction is confirmed in the
final source above. LGF 563–578 correctly lists the binding inherited-source
fixes for later authorized consolidation: explicit normalization and
differences, corrected torus orders, the regulated image prescription,
replacement of stale imported/ARGUED labels with the actual library/review
status, and retention of FREE/TS's other conditions. TSE55 itself was not
edited or promoted by this review. Its interacting inputs, the separate
FREE test-function arguments, consolidation and any independent audit remain
outside this verdict. Method credit to Spitzer, Lawler–Limic, Uchiyama,
Fukai–Uchiyama, and the lane's credit to Balaban and Dimock remain attribution,
not unexamined proof premises.

VERDICT: LAND
