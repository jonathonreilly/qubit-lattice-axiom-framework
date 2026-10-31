# Second independent hostile review of SOFTHARD

Reviewed 29 October 2026. All local paths below are relative to this directory. Line references denote the inspected checkout unless explicitly called historical. This review concerns the operative, repaired SOFTHARD comparison and proposed return contract. It is not an independent certification of every theorem in its quoted registry, a retained-status decision, or a proof of a hard-return construction.

**Result: no material defect found in that scope.** The finite-dimensional arguments survive independent derivation. The repaired cubic estimate has the advertised conditional, unweighted scope. The return statement now preserves the external measure, explicitly retains zero-reference and singular residues, and requires the missing consumer conversions. Its existence and uniform estimates remain OPEN. Earlier reviewers' verdicts were treated as assertions to test, not proof authority.

## Source identity and method

Read SOFTHARD.md, SOFTHARD_LOG.md and all three requested prior reviews, then followed the cited arguments and consumer statements identified below. Large sources were searched and read at the relevant offsets. No numerical or symbolic check program was executed. Read-only scripts were used for hashes, quotation matching and source bookkeeping; the original validators were inspected, not replayed. No other file was edited and no commit was made.

Checkout HEAD: `9658cc870d82401001e56b29f351aec5f5f58fa1`. Cached `origin/main`: `01589af3faf806b736c42dc2f3bd625e9edead9f`. No remote freshness is claimed.

The reviewed byte identities are:

| File | SHA-256 |
|---|---|
| SOFTHARD.md | `890c3726f86ad7dc557f5c16a8f6e99a014896acee18a480ef44f81fc6069968` |
| SOFTHARD_LOG.md | `635547412b25b33e37c832f40a095922d730299f873e9fd9893e1fba874a55d7` |
| REVIEW_SOFTHARD.md | `c15c26b926a8682b01eab8670991eef9b12bd17bd555c2d1b42fd87aa913c174` |
| REVIEW_SOFTHARD_R2.md | `02b7b7ee556df6f501bc0c206497192423b01633c1907fa3bd6ff2019d75ab0b` |
| REVIEW_SOFTHARD_R3.md | `ced9c69bf687f313f359a19eda1392e44cc492ccd1c303aad2facc809eb628f2` |
| PROOF.md | `ae55788084e0946faa221743e7fe92419e4faef348f00b98aeceeced625e4b40` |

## Findings, ranked by severity

No critical, high or medium finding. The following are minor locator or evidence-handling defects; none supplies a mathematical counterexample to the operative memo.

**F1 — LOW: historical line numbers are unsafe as live locators.** SOFTHARD.md:307,345,383–428 uses the S26 interval `PROOF.md:308–354` and its `Pnnn` identifiers. That interval is now **423–469**, with the corresponding identifiers shifted by 115. The frozen revision is identified at SOFTHARD.md:345, so this is not evidence that its original coverage was fabricated. It is a reproducibility hazard when “now” or “current” is read against today's checkout. The current interval contains the 44 science bullets covered by the crosswalk; their identity, not the obsolete offsets, is the relevant coverage evidence. Its SHA-256, joining the 47 lines with newlines and no final newline, is `386683c028b0fd36dea757a5932273f6d289820ce1a71e563dd343ffb7e98832`.

*Fix:* preserve historical reviews, but give the live memo a commit-qualified registry anchor, interval hash and current locator map. Apply the same convention to its other shifted PROOF references. Do not reinterpret an old numbered interval as the current scientific registry.

**F2 — LOW: the structural coverage predicate can pass vacuously.** `checks/sh_revision_v2_check.py:277–292` selects science bullets from the literal range 308–354 and tests only whether any selected number lacks an assignment. An empty selected set passes. Lines 293–295 test the presence of fix markers, not whether the fixes satisfy their consumers. The checker explicitly disclaims semantic certification at line 289; that disclaimer is correct. Other guards can still fail the overall run, so this is a defect in this individual gate, not a claim that the whole validator always passes.

*Fix:* in a new validator version, require the expected nonempty cardinality and pinned registry identity, locate named entries, and compare their assignments. Keep this result labelled structural coverage. Mathematical and consumer review must remain separate. Preserve the frozen checker and receipt as historical evidence.

**F3 — LOW: process success is not scientific success for two supporting checks.** `checks/r55u_2_tu3poly.py:202–215` and `checks/r55u_3_interp.py:59–68` print predicate failures but unconditionally return zero. In the former, inputs are constructed as `F = curl(a)` at line 172: the resulting closedness test cannot establish the claim for all closed analytic families. The reconstruction discrepancies and deliberately altered controls are nevertheless meaningful and can fail. The interpolation predicates can also fail; they are finite samples, not the tensor-product proof in arbitrary dimension. CODEX_REVIEW_TUNIF2.md:22–24 already acknowledges these limitations, so they are not a newly discovered refutation of its mathematics.

*Fix:* any future check version should aggregate required predicates and control firings into a nonzero failure exit status, retain discrepancy counts, and state its input class. Do not use an exit code, exactness-by-construction, or sampled interpolation as evidence of cutoff/volume uniformity. No rerun is needed to establish this finding.

## What I independently re-derived

1. **Normalized hard and mixed chains preserve the fine marginal, not arbitrary conditional laws** — SOFTHARD.md:71–77,297–299,434–456. For a measurable map B, the probability kernel δ_B has K1=1. Integrating the last variable first, repeatedly, gives `∫F(U_0) dμ(U_0) ΠK_j = ∫F dμ`, including an integrable fine-source insertion. The same proof works for mixed normalized kernels and a link partition chosen from the input before integrating the output. It does not work after imposing an unintegrated coarse cut, conditioning on a coarse value, or selecting a particular history. Therefore the fine-observable RP statement follows, while coarse-density analyticity, backward estimates and seam transparency do not. The memo makes this distinction.

2. **The hard-map and regularity obstructions are limited as claimed** — SOFTHARD.md:81–96. Arithmetic matrix averaging need not land in SU(N). At zero mean the soft exponent is constant in the output, so the kernel stays Haar as stiffness increases. A mean-only endpoint-biequivariant choice at zero would satisfy `B(0)=h B(0) h'^{-1}` for independent h,h', which is impossible. This does not prohibit a map using the full fine configuration. At a fixed unique maximum, compactness gives a strict gap outside each neighbourhood and hence Laplace concentration; this supplies no uniform estimate through zero/degenerate means. For a regular submersion, the pushed density has the coarea factor `1/sqrt(det DB DB*)` on the appropriate quotient. The identity map on U(1) pushes a discontinuous density to itself, whereas convolution with the finite-stiffness analytic kernel smooths it. This refutes automatic transfer for arbitrary fine weights, not analyticity of every particular Wilson pushforward.

3. **The Gaussian comparison and source shift** — SOFTHARD.md:100–109. With `C=A^{-1}`, A positive on the stated gauge complement and Q full row rank, Woodbury gives

   `C_κ = C − CQᵀ(κ^{-1}I+QCQᵀ)^{-1}QC`.

   Its hard limit is the covariance on `ker Q`, equivalently `Z(ZᵀAZ)^{-1}Zᵀ` for a basis Z of that kernel. On `Qx=b`, a source `ξ·Qx` is constant. Direct completion gives

   `κ||Qx−b||²/2 − ξ·Qx = κ||Qx−b−ξ/κ||²/2 − ξ·b − ||ξ||²/(2κ)`.

   Neither this finite-dimensional limit nor restriction of an energy lower bound establishes uniform hard critical-map derivatives. For a nonlinear constraint the second variation includes its multiplier/constraint-curvature term. Thus deleting a soft penalty, or testing a bare negative direction, does not supply the missing constrained Hessian. SOFTHARD.md:357 retains this distinction.

4. **The normalizer and analyticity distinction** — SOFTHARD.md:153–177,287–289,470–479; STEP55.md:243–257. Taking minus the logarithm of `ρ(U) exp(−tψ_M(V))/N_t(M)` gives the plus `log N_t(M)` in the exact conditional action. Normalizing in V does not make that term constant in U. The raw polar-tube upper estimate concerns a V-independent integrable fine weight and does not imply a zero-free normalized ratio. A positive two-atom real mixture can have complex zeros, so real positivity alone is insufficient. For a group-valued center B(U), Haar translation makes the forward normalizer independent of U; the holomorphic extension uses `(tr(V^{-1}B)+tr(B^{-1}V))/2`. Compactness bounds that integrand on compact complex V sets, giving holomorphy for an integrable fine weight even if B is only measurable there. This proves neither fine-variable regularity of B nor a returned denominator bound. The H4 discussion does not claim otherwise.

5. **The repaired trivial-background cubic bound, including the dangerous norm and scale steps** — SOFTHARD.md:349–357; NORMS.md:189–243,507–556; TUNIF.md:244–405; CODEX_REVIEW_TUNIF2.md:29–258; LINEAR_PACKAGE.md:63–270.

   I checked the root-average cancellation `Q=Q_str−dh`, the scalar-root identity `Qd=d ev`, and the geometric estimate giving `q_0=1+d(L+1)/(2L)`, hence 11/3 only at d=4,L=3. Residual transport telescopes the κ ratios; it does not multiply κ_+/κ_- once per level.

   For twisted potential reconstruction I checked the finite-shift division identity, the transverse closedness/vanishing-period argument, the compensating spread component, and the cancellations in `D∧b=F`. Periodicity of the analytic symbols is a required input, not a consequence of the finite examples. The harmonic correction replaces the torus mean by the correct `L^{-k}` coarse mean. The same representative must then be corrected at top roots by one interpolated fine scalar. Tensor-product hat interpolation gives a gradient sup factor `s^{-1}` and a column-sum factor `s^{d−1}`; odd centered root grids nest because `(ab−1)/2=(a−1)/2+a(b−1)/2`. Whole-transport read-range and harmonic terms contribute fixed constants. This supplies the paired potential bounds `P L^{-n}` and `P L^{(d−1)n}`, subject to the named linear-locality inputs.

   I explicitly did **not** use NORMS.md:106's false equality between the absolute tensor row sum and its bilinear sup. Summing absolute coefficients first, using the local vertex coefficient masses and the linear maps' row/column bounds, controls the stronger absolute row sum. The two Wilson slot assignments have exponents `(d−2)k−k−k` and `−2k+(d−1)k−k`, both `(d−4)k`. The two soft assignments have exponents `n+d−1−2n` and `−(d−1)(n−1)+(d−1)n−n`, both `d−1−n`. Consequently

   `Σ_{n=1}^k L^{d−1−n} ≤ L^{d−1}/(L−1)`.

   This is 27/2 for d=4,L=3 and 125/4 for d=4,L=5. It is a uniform unweighted cubic implication with finite repaired constants. It is not a weighted moment bound, a quartic estimate, a nontrivial-background theorem, or an estimate for a newly selected hard representative. The frozen linear analytic-strip/locality theorems and exact critical-value/vertex identification remain premises; I did not independently re-prove their entire provenance.

6. **The conditional-covariance distinction in I5** — SOFTHARD.md:375; TSE55.md:146–166. Use the decreasing future filtration of the Gaussian Markov chain. Its conditional-mean increments are orthogonal; being jointly Gaussian, they are independent. Their covariance sum includes the terminal conditional-mean covariance. For a quadratic observable, Wick expansion of an independent current fluctuation z and surviving coarse field c gives `2a_i²+4a_iΣ_{j>i}a_j`; summing including the top term gives `2(Σ_i a_i)²` entrywise. The identity is generic. The individual conditional covariances and response operators change when the kernel changes. Fine-marginal invariance does not identify those operators. No Yang–Mills approximation or LGF estimate follows from this calculation.

7. **The repaired HRT measure identity, its residues and its next consumer** — SOFTHARD.md:528–603. Write `μ^0=λ_h(dξ)ν_{h,ξ}` with both interior levels integrated. Then for a bounded external test f,

   `∫ f χ_hχ_ret A dμ^0 = ∫ f Z_ret dλ_h`,

   and on the defined positive-reference set this equals `∫ f Z_ref Xi dλ_h`. Keeping λ_h is essential: normalized conditional probabilities do not cancel its pushforward Jacobian. The coarea density is only the regular-chart representation; it cannot dispose of singular sectors or multiply redundant delta equations.

   At `Z_ref(0)=0<Z_ret(0)` the ratio does not exist. The memo keeps exactly that mass in R and requires a separate coverage theorem to remove it. Small components cannot be reclassified as the large-history sea. Source absolute continuity justifies removing a sector where both real masses vanish; it does not remove a positive residue. Reintroduced variables preserve the external marginal and inserted generating function, not the original interior law. Future factors must depend only on ξ unless included in A before this operation.

   The output is correctly defined as the joint measure M(dV,dW) relative to `dHaar(V)K_{j+1}(dW|V)`, with a singular remainder S. A density chosen only almost everywhere in V for each fixed W would not suffice on a hard graph. The required joint Radon–Nikodym representation and analytic two-field extension are explicitly open. The terminal operation has no extra K_K or W and also covers K=1. These checks address the actual earlier fixed-V obstruction, rather than accepting R3's verdict.

8. **The quantitative bookkeeping and its quantifiers** — SOFTHARD.md:605–649; HIST.md:198–372,548–578; RLARGE.md:186–216,299–311; FLOW.md:430–470; SRCCD55.md:972–1017; RECOVERY_CLUSTER_ASTRA.md:264–392. The constants are required before j,K,T,history and datum. The domain includes feasible holonomy sectors and does not replace them by a globally small potential. Original η sources are distinct from coefficient variations ζ. A sup bound alone gives no physical volume-fraction derivative factor; HRT separately demands the marked norm with its zero-weight rule. Two-field transport and extraction are also separate estimates, not Cauchy consequences of a ratio bound.

   The displayed irrelevant-budget arithmetic is exact: `(1/2)(1/64)+1/256+1/256=1/64`. The `g_j^6/(4C_ext)` bound pays the claimed extracted increment only after the actual operator bound C_ext is established. The own-sequence flow bracket fixes its lower slope and remainder before the error constant/weak-coupling threshold; it does not borrow a terminal trajectory to prove itself.

   In the history count, the per-level number of placements grows as `L^{4(K−1−j)}`. The shadow bound contributes a further exponential cost per remaining level. Combining the size lower bound `n_sharp+1` with the flow bracket makes the scale sum converge only with HIST's strict inequality `(n_sharp+1)a beta_- > 4+c_B`, after all price losses. HRT requires those inequalities; it does not assume an unqualified entropy saving. Its reference is Z(empty), not a silently substituted small-field partition function. A finite seam collar does not contain infinite covariance tails: their connectors and norm costs remain explicit.

## Consumer and literature checks

I compared the joint three-level input/two-field output to HIST's SF^J formulation, the coupling-extraction budget and empty-history distinction to RLARGE, the parameter order to FLOW F-ind, the full stationary-action/determinant/cutoff factors to RECOVERY_CLUSTER_ASTRA, and the marked-source requirement to SRCCD55's E12 defect. The statement demands the actual conversions; it does not assert that its displayed fixed 1/64 class already equals every sharper consumer class. This is a specified open sufficient construction, not a discharged application of soft CL^J.

The historical quotation manifest contains 28 local quotations and six PDF quotations. All 28 local quotations were independently located in their sources, and all 34 quotations remain present in the memo after whitespace normalization. This checks textual fidelity only. I also checked the present 44-entry registry against the comparison crosswalk; coverage is not proof of its entries. The I2–I4 generic/conditional reuse claims were checked against their cited hypotheses and qualified source dispositions, not promoted into new hard-law theorems. No load-bearing step was justified by an `[m]` memory-only citation.

The literature comparison does not import a four-dimensional nonabelian return theorem. Dimock I's cluster theorem assumes an ultralocal probability measure, specified decay and smallness; it cannot by itself normalize a constrained hard return. [Dimock I, Appendix B, Theorem 27](https://arxiv.org/pdf/1108.1335v2). Dimock II's operative representation is in §3.3, equations (199)–(202), with a soft Gaussian block kernel; its remarks distinguish the recycling step omitted for that scalar model. [Dimock II](https://arxiv.org/pdf/1212.5562v2). Dimock III's Lemma 20 is a scalar Neumann-boundary coercivity estimate: block averaging and path Cauchy–Schwarz control the coarse gradient, while the elementary triangle/Jensen estimate controls the mass term. Its boundary resummation also consumes a counting lemma from Part II. [Dimock III, Appendices B–C](https://arxiv.org/pdf/1304.0705v1).

The axial exposition is abelian, and Proposition 5 explicitly leaves a Gaussian computation to an earlier reference; it is not a complete nonabelian gauge proof. [Covariant Axial Gauge](https://arxiv.org/pdf/1410.2798v3). The multiscale paper supplies a three-dimensional mechanism; the absorption at equation (376) needs its constants checked when reconstructed, as the memo already warns. [Multiscale Block Averaging](https://arxiv.org/pdf/1712.10029v3). The QED estimates likewise do not give the requested hard SU(N), d=4 theorem. [Ultraviolet Stability for QED in d=3](https://arxiv.org/pdf/2009.01156v2). These are source/scope checks and selected elementary reconstructions, not complete independent proofs of those papers.

## What I did not re-derive or verify

- I did not construct an admissible global hard map, prove HRT's support coverage/nonzero denominator, build the constrained analytic atlas, remove R or S, prove the marked-source/transport bounds, or close the history/base/terminal estimates. They are expressly open at SOFTHARD.md:651, not missing premises concealed in a proved theorem.
- I did not independently prove every theorem in the S26 registry or every transitive theorem cited by its entries. In particular the full N2 uniform locality/analytic-symbol package, all Node A/BL-TILT/off-global applications, weighted higher critical-map jets, actual Yang–Mills source/LGF estimates, seam transparency, non-freeness, OS reconstruction and physical mass gap are not certified here. The conditional cubic calculation must not be detached from its named premises.
- I did not recompute every advertised numerical constant in inherited theorems, reauthenticate every old timestamp/manifest, or reproduce the old numerical outputs. Full code inspection covered the structural revision validator and the two cubic-support checks discussed in F3; other check claims were inspected only to the extent needed for the cited argument. No new PASS result is asserted.
- The ten historical PDF paths, including the later recovery paths, were unavailable in this checkout. The recovery JSON receipts report successful earlier byte recovery; that report is not a fresh hash authentication by me. I inspected the versioned arXiv sources linked above instead. I did not read every page of every cited paper or reconstruct their entire citation trees.
- KEEP-SOFT remains a reasoned provisional choice, not a theorem establishing optimality over all hard or hybrid constructions. This review does not turn that recommendation, the source inventory, or the HRT target into scientific closure.

The surviving obligations are concrete and falsifiable. The memo's final claims remain within those limits; the minor findings above do not change that conclusion.

VERDICT: CONFIRM
