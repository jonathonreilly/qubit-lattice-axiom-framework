# Fresh hostile review of REALRGA

The final candidate is suitable as a **scoped proposed contract and conditional mathematical note**. No material finding remains after the corrections below. Its actual SU(N) RG realization, invariant local estimates and consumer modules remain OPEN. This verdict does not assert that the proposed producer exists, confer retained/audit status, approve a campaign, or certify Yang–Mills existence or a mass gap.

Review date: 2026-10-30. This is a fresh-context, same-family Codex review, separate from authorship. It is not cross-family review or formal audit. I used written re-derivations and source inspection; no numerical computation was run or resource guard bypassed.

The disposition binds **REALRGA.md SHA256 `e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed`**, 649 lines. I read the complete original 638-line note, SHA256 `007cf62c59bb76ec7079ed6e68d8e6a4ee1d02b92d3b0f5e45b673329fd059b2`, then the complete v2 and cumulative v3 diffs and all affected final passages. A deterministic comparison confirms that [the cumulative v3 diff](realrga_author_fixes_v3.diff) is exactly the difference between [the preserved original](realrga_review_source_v1.md) and the final note. No commit was created; these files preserve the uncommitted correction history.

The scientific source pin is `cd67e1c9e6bbed8b92fee069de66ef0b25486316`. All 23 source entries in [the source manifest](realrga_sources.json) matched their recorded working-file hashes; the 22 tracked entries also matched that commit byte for byte. The untracked author brief is separately hash-bound. The workflow, reviewer skill, freshness reference, proof-governance reference and review-loop procedure were inspected at the local snapshot; the four reviewer procedure/reference files also compared equal to the cached `origin/main`. This does not establish freshness of the science against a newly fetched main. The author's failed main fetch and candidate-source limitation remain applicable.

**Findings and binding corrections.** Line references below use the final candidate.

| Finding | Correction and confirmation | Disposition |
|---|---|---|
| The original RGA17 used starred budgets without stating that they bound the step-dependent quantities. Its induction inference requires those inequalities. | Lines 433–443 now require nonnegative `lambda_q`, positive `M_q`, and uniform `0<=s_j<=s_*`, `0<=eta_j<=eta_*`, `0<=e_j<=e_*`, with finite bounds. Substitution into the recurrence now proves the stated invariant interval. | RESOLVED; no further fix. |
| Uniform convergence of jets on a merely closed evaluation set does not, by itself, prove smooth extension to a neighborhood. This mattered to the wording of RGA-C and its countable-family extension. | Lines 75–77 and 320–359 place the uniform bounds on an open real domain, with closed inner evaluation sets and compact-interior convergence. This supplies the domain needed for termwise differentiation. | RESOLVED; no further fix. |
| The JETS recurrence needed an explicit source evaluation point and law. At a nonzero base source the outer conditional law changes. | Lines 532–540 define `J_(j,B)=partial_B Phi_j(0;U_j)` and specify the unperturbed actual chain, with the corresponding tilted law required at a nonzero base point. This matches K4MATCH (7). | RESOLVED; no further fix. |
| The initial carry-over table did not explicitly classify RD3 D14–D16 or JMBRA A19–A23b. | Lines 494 and 501 now retain the integrated-event algebra, normalized-mass obstruction, reference survival, matched boundary conditions and bulk source response at their original scopes. | RESOLVED completeness correction. |

**Verdict per requested item.**

| Item and final location | Scoped verdict and reason | Further work |
|---|---|---|
| Norm, derivatives, regulators and support weights, lines 71–180 | LAND as definitions and proved calculus. Ordered Lie derivatives, mixed field/source orders, original source units and regulator multiplicities are explicit. | Actual useful regulator moments and derivative bounds remain OPEN; `p=6` is a choice, not a sufficiency theorem. |
| Positivity, differentiation, logs and integration, lines 184–312 | LAND as conditional identities/estimates. No value-only derivative estimate or uniform inverse is inferred. | Positive fibers, domination, moving-selector treatment and complete normalized-reference budgets must be supplied at the claimed model scope. |
| Mayer replacement, locality and extraction, lines 314–414 | LAND for the finite-jet cluster implication and ideal dilation benchmark. | The exact local atom representation, small joint jets, arbitrary-support localization and actual extracted contraction remain OPEN. |
| Step-to-step hypothesis and carry-over map, lines 416–521 | LAND as an exact conditional transition contract and source-scope map after the fixes. | The transition theorem, new reference budgets, relevant recursions and all-history geometry remain OPEN. |
| Consumer map, lines 523–617 | LAND as conditional interfaces. Every REALONLY consumer is covered without inferring all-order control from four-source jets. | HIER, MATCH2/MATCH4, EUC, FLOW and the common limiting seed retain their full stated obligations. |

**Independent mathematical checks.**

For the group calculus I treated each invariant vector field as a derivation, without using commutativity of two same-species directions. For an ordered word `I`, repeated Leibniz gives a sum over subsets of positions, with the original order on each factor. Splitting the fine/coarse/source counts produces the three binomial coefficients. Dividing by `a! b! c!` cancels those coefficients; every split remains inside `a+b<=p, c<=q`. Enlarging the resulting nonnegative convolution proves RGA8. The same argument with labelled subsets gives the square-free source product rule. It does not create higher derivatives. Iterated coordinate-chain differentiation produces the set-partition formula RGA9; a source-dependent field substitution can indeed consume extra field derivatives. No global logarithm of SU(N) is needed.

The regulator issue survives already at derivative order zero: two factors bounded by `G_m` are bounded in their product by `G_(2m)`, not uniformly by `G_m`. The multiplicity labels and the requirement to remove any remaining regulator before the unregulated Mayer bound are therefore substantive. RGA14 follows by differentiating the **whole** density-integrand product, bounding its jet norm, and integrating the resulting joint regulator. Separate moments cannot replace this mixed integral. Fixed masks permit this argument; moving hard boundaries do not acquire smoothness from positivity.

For normalization, writing `N(y)=int F_y w_y` and `Z(y)=int w_y` and differentiating `N/Z` gives RGA10, including the negative normalization term. Differentiating `Z*Z^-1=1` gives the ordered-subset inverse recurrence. Applying this to `Z=exp(log Z)` recovers the log partition formula with ordered block derivatives, so noncommuting Lie words have not been silently symmetrized. The estimate `|h_M|<=1` gives the kernel bounds directly, including at `M=0`. Real positivity proves existence of the real logarithm on a nonzero fiber; it proves neither small derivatives nor a volume-uniform inverse. The log-determinant series follows eigenvalue by eigenvalue for the stated positive real matrix and `||A||<1`; it supplies none of the missing Hessian, local-support or gauge-slice inputs.

I reconstructed the cluster accounting from connected selections and marked roots. Exact component factorization first turns the selected-set sum into a hard-core gas. A connected selected set rooted at atom `i` has a spanning tree; summing its unordered child sets is bounded by the exponential tree recursion. The overlap incidence estimate is `sum_(j overlaps i) b_j<=Q|H_i|`, so `b_i` is a supersolution. Marking an atom whose support contains the physical root bounds the integrated gas at rate `mu+1` by `Q`. For the logarithm, the alternating connected-graph coefficient is bounded by the spanning-tree sum: the optional edges in each ordered Kruskal class contribute either zero or unit modulus. Physical-root marking changes `1/m!` to `1/(m-1)!`; repeated polymer labels must remain. Repeating the incidence argument spends the second unit of support exponent and yields the claimed `mu` bound. RGA8 applies to every product in both stages, so the same majorant controls all included derivatives. Scaling original atoms by a real counting parameter of magnitude below two changes `Q` to at most `2Q<=1/2`; the absolutely convergent formal exponential identity then proves positivity at one. This uses no complex physical-source estimate and bounds no empty-support prefactor.

The extraction benchmark has the correct scale: the `r`th derivative of `L^4 F(L^-2 x)` is `L^(4-2r)` times the corresponding derivative at the contracted argument. For `r>=3` this is at most `L^-2`. Zero jets through degree two allow Taylor integration to control the omitted lower derivatives on the ball. It remains an ideal operator calculation. After the RGA17 repair, `C_q x_j^2<=C_q M_q x_j` gives `x_(j+1)<=theta_q M_q+B_q e_*q<=M_q`. Uniform window bounds also multiply in their actual time order; no commutation or stationarity is needed. A common lag envelope bounds both birth lifetimes and fixed-terminal accumulation, while a separate lifetime bound alone does not.

For the four-source interface, coefficient extraction from the conditional exponential followed by the outer logarithm gives the partition sum, including the four triple/single terms and all other proper subsets. With K4MATCH's `P=lambda^16*kappa_4(O_1,O_2,O_3,O_4)` and `X_i=u*lambda^4*O_i`, multilinearity gives `partial_1234 L=u^4 P`; distinct labels introduce no `4!`. Original kernels must remain fixed under this observable derivative. I also checked the second-cumulant/terminal-covariance convention against WITNESS E10–E12.

For HIER, ordered set partitions are bounded by `n!` times the `2^(n-1)` positive compositions. Together with `product_B |B|!<=n!`, this gives unconditional cumulant exponent `p0+1`; the moment expansion costs at most one additional `n!`, giving `b0=p0+2`. Centering removes singleton unconditional moments. The collision-flat Taylor estimate cancels the worst `delta^-5n` majorant using order `5n`; the separately retained `a^-4n` point bound handles separations below the cutoff. The stated `10n+1`, `s=11` and `beta=p0+3` are sufficient. This requires the full all-order, small-separation module and common convergence.

The flat symmetry implication follows from convex secants with the cutoff limit taken before the source tends to zero. The sphere implication follows from actual-law total covariance and `|Cov(F_k,S_k)|<=||F_k-EF||_2 inf_c||S_k-c||_infinity`, retaining the terminal term and fixing `J` first. The scalar response bound follows by differentiating the stated scalar recurrence and bounding the logarithm of its positive factors using the strict `q_*<1` margin. None of these calculations supplies the separate spatial derivative kernel, matching coefficients, reflection positivity or continuum sequence.

The hypothesis graph is not circular as a conditional specification: RGA-C consumes joint jets and factorization; the induction consumes a transition theorem; the consumers consume their named additional modules. Those terminal obligations are substantial, and several are the full desired estimates at their interface. Repackaging them does not establish proximity to an actual-model RG proof. The note states this limitation explicitly and makes no route-exhaustion claim.

**Actual read coverage and limits.** The complete AUTHOR brief, PROCESS_LIGHT, SCIENCE_WORKFLOW, physics-claim-reviewer skill, skill-freshness reference and proof-search-governance reference were read. Relevant model/depth passages of review-loop were read. The adjacent REVIEW brief was read at final confirmation; its suggested filename yields to the explicit author-path restriction and this dispatch, so this report is the reviewer's sole written file.

| Pinned source | Mathematical passages read for this review |
|---|---|
| REALONLY | Complete file, lines 1–592. |
| CHARGE | 36–268, 306–579. |
| RD3 | 23–168, 170–591. |
| RD4 | 25–203, 260–277, 336–461, 521–638. |
| JMBRA | 24–704. |
| JMBRB | 84–155, 176–377, 381–514, 550–687. |
| RENEW | 27–146, 207–339, 398–438, 454–560. |
| LFPRICE | 28–199, 202–546, 549–709. |
| LIB1 | 43–439; complete LIB1_NORM_CONTROL_FIX and REVIEW_LIB1_NORM_CONTROL_ASTRA. |
| STEP55 | CX lines 483–525, plus locator searches. |
| K4MATCH | 28–49, 149–190, 283–366, plus normalization locators. |
| WITNESS | 505–594. |
| TQ2 | 284–390. |
| N5B | 153–214, 475–526. |

This is a targeted check of the necessary premises and carry-over scopes, not a fresh certification of every old source theorem. The complete REALRGA log, criteria, 173-line diagnostic script, source manifest, result, stdout and stderr were inspected. Partial/truncated initial tool output was not counted as completed reading; the missing portions of the new note were read separately.

I checked the attribution locators in the primary papers: [Bauerschmidt–Brydges–Slade](https://arxiv.org/pdf/1907.05474v2), Definition 7.1.2, (7.1.9), and the adjacent product lemma; [Brydges–Slade](https://arxiv.org/pdf/1403.7244v2), Definition 3.3, Proposition 3.7 and the section 5.1 proof location. They concern different field spaces and do not establish this gauge-model induction. The primary abstracts of Dimock's [Large fields](https://arxiv.org/abs/1212.5562) and [Convergence](https://arxiv.org/abs/1304.0705) confirm the scalar three-dimensional scope stated in the note. These checks support attribution only.

The diagnostic receipt is correctly **NOT RUN**, with an empty checks object. The recorded niceness is zero and stderr says `nice: setpriority: Operation not permitted`. The result and stdout are byte-identical. Their criteria hash is `7f24db01d74e26275e63fb13f9f0f7251302a4ed9020569504acf7c672f00e60`; their script hash is `71c8bb774c21f2095a2b194ffe638210cb54d7db45041ad44083adb52cc67d6b`; both match the inspected files. Static inspection shows finite Bernoulli, conditional-jet and repeated-label Mayer diagnostics, not a gauge estimate or a proof of the induction. Their mutation controls were not executed. No PASS count is used in this verdict.

Only `checks/realrga_review.md` was written by this reviewer. No source, prompt, audit, ledger, git ref or PR was modified.

VERDICT: LAND
