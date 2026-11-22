lead: openai/gpt-6-luna/high laptop-codex-runner (row 1394)

> Restored by the lead (Claude Opus 5.5, 2026-11-22). The run wrote this file at the repository root instead of the lane folder, and the runner removed it before the next launch. The text below was rebuilt by replaying the run's own five write commands from its log; its last command reported the same 92 lines. Two limits of the run, stated by the run itself: it did not find the lane library or the account sources (the header points to LOCAL:ym4d-lead/sa; the run looked elsewhere), so its repo search used the main repository refs only. Nothing here was checked by another model.

# Repo search — gap-carry-lit-luna

**Terms:** `Lanford`, `Koch and Wittwer`, `computer-assisted fixed point`, `interval arithmetic`, `Tomboulis`, `(TB)_n`, `Ito and Seiler`, `step-scaling`, `Schrödinger-functional`, `gradient-flow coupling`, `twisted coupling`, `order-one coupling`, `last scale`, `block action`.

**Refs searched:** the main repository checkout: `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141`; Markdown and TeX. Exact full-ref searches for the named computable fixed-point methods and recent gauge step-scaling terms returned no clearly relevant proof hit in the bounded output inspected. Focused mass-gap searches produced the hits below. The Y-M registry search for `gap-carry`, `K-flow`, `(TB)_n`, `order-one ... block`, and `last-scale` found no row owning this literature question; it has adjacent but different Balaban last-scale rows B109-last-scale and B122b-last-scale.

**Relevant repo hits and closeness:**

- `research/mass-gap/library/gap-crux-fp.md` (origin/main), §§1.4–1.5, lines 94–100: exact statement: “Theorem S says $s_{k+1}\le K s_k^2$ when $s_k<1/K$. This is the strong end of a step-scaling inequality ... Balaban's work ... controls a different coupling at the weak end. The crux is the middle: no quantity is known that is controlled at both ends, and no inequality is known in between.” This directly frames the order-one band, but is a repository synthesis and does not establish a literature-wide negative result or discuss computer-assisted fixed-point spaces.
- `research/mass-gap/library/gap-crux-fp.md`, §2.4, row c4: exact statement: a same-coupling recursion is required by that route; “Every known comparison of this kind (Migdal and Kadanoff) is one-sided for the free energy and gives nothing for a ratio,” with Tomboulis (2007) and Ito–Seiler (2007) cited as recalled. This is a prior route assessment, not a fresh source reading.
- `research/mass-gap/library/gap-skeleton-max.md`, lines 336–361: exact statement: the all-coupling claim rests on `A(alpha)>A^+(alpha)`, “shown only where the strong-coupling expansion converges”; its own comparison says Tomboulis inserts an approximate recursion between bounds on `Z` and the ratio `Z^-/Z`, the step Ito and Seiler dispute. Closeness: exact to the disputed bridge but not a post-2015 status update.
- `research/mass-gap/library/prior/gap-crux-lit-nonab.md`, line 246: exact statement: Ito–Seiler identify the unproved large-`beta` inequality `A(alpha)>A^+(alpha)` and a possible failure of implicit-function continuation; it disputes that proof, not the confinement conjecture. Closeness: exact obligation identification, prior summary.
- `research/mass-gap/library/prior/gap-crux-lit-2.md`, lines 261–265 and 211: Kanazawa’s published theorem is a finite-volume twisted-boundary Wilson-loop bound conditional on exponential twisted-partition-function decay; the prior search records no order-one verification for 4D Wilson SU(2). This is adjacent to twist schemes but is not an inequality for the continuum step-scaling function.

The broader repo search also hit `research/mass-gap/ROWS.md` rows 661–662, which reproduce earlier coverage of Tomboulis/Ito–Seiler and a literature digest. Those findings are represented by the specific notes above; no separate target result was found in PR refs. This repo-search section is evidence of prior work and is not an audit or a science-status claim.

## Plan / checkpoint

1. Checked first for an existing target gap-carry note; none was present. Created this output with the plan before research.
2. Read the available `GOAL.md`, required `FINISH.md` sections, target/comparison rows, and repository workflow map. The local `sa-index` and account files are absent, so no source-line selection from them was possible.
3. Searched the repository refs named by the user before evaluating the methods; exact hits, claims, and closeness are recorded above.
4. Reviewed accessible primary sources for the three requested literature slices; omissions in reported coordinate counts/costs and bounded-search limitations are stated explicitly below.
5. Determined whether a qualifying published order-one step was found and recorded the bounded outcome below.

## Search log

- 2026-11-22: Created this checkpoint first, as requested; then checked required repository sources and recorded missing paths.
- 2026-11-22: Completed the literature review and bounded conclusion below.

## Required local sources and bounded coverage

- The pinned local checkout is `5de95b1baa00998d60d3e939eb52153a5e2ec8b2`. It contains the required lane `GOAL.md` and `FINISH.md`; I read the full goal and the requested `FINISH.md` sections (“Build on published work,” “Working efficiently,” “Rules”), plus the target row and comparison rows 1002, 1025, 1007–1012, and 1379. The local checkout has no tracked `library/` tree at that commit. The required `library/sa-index/` (README, chunks, obligations), `library/lit-balaban.md`, `library/open-registry.md`, and `library/prior/repo-search-2026-11-08.md` were therefore unavailable. The output path was created for this note.
- The user-specified outline and account paths under LOCAL:sa are absent from this machine (LOCAL:sa does not exist). I did not search outside the permitted locations. Consequently I could not use the index to select source ranges or independently inspect the cited account/outline passages. No Balaban paper was downloaded.
- The repository-side registry check and exact prior-work claims above were made against the separate the main repository checkout checkout and the five refs named in the request. The adjacent Balaban last-scale rows do not own this literature survey. This note builds on, and does not repeat, the earlier row coverage summarized above.

## (a) Computer-assisted fixed points and flows

### Lanford: Feigenbaum fixed point

Lanford’s proof is an exact computer-assisted existence/uniqueness proof for the one-dimensional period-doubling fixed point. The function space is even analytic functions on a complex domain containing the real interval, with a supremum norm; the implementation represents functions by a real scalar plus a weighted `ell1` sequence of Taylor coefficients. The approximate fixed point is a polynomial (degree 20 in the initial construction, with a small ball around it); finitely many matrix entries are bounded directly and the infinite tail is controlled analytically. The proof encloses the residual and derivative and establishes a contraction (the paper reports a derivative bound below 0.9 and residual below `4e-6`). The program is a rigorous numerical proof, not an unchecked floating-point inference. The paper does not report a wall-clock cost. This is a scalar functional equation for a one-dimensional dynamical system, not a lattice RG transformation or a nonhierarchical field theory.

Hertling and Spandl later analyze the computational complexity of this Feigenbaum computation: their algorithm keeps `10+m` coefficients at iteration `m`, uses polynomial degree `20+2m`, controls the omitted tail, and gives polynomial bit-complexity (reported as `O(n^4 M(n))` for `n`-digit precision). That is a complexity bound for computing this one-dimensional fixed point, not a resource estimate for gauge-theory block actions.

Sources: Lanford, [“A Computer-Assisted Proof of the Feigenbaum Conjectures”](https://people.math.harvard.edu/~knill/history/lanford/papers/LanfordCollectedWork.pdf); Hertling and Spandl, [“Computing a Solution of Feigenbaum’s Functional Equation in Polynomial Time”](https://doi.org/10.2168/LMCS-10(4:7)2014).

### Koch–Wittwer: hierarchical scalar models

Koch and Wittwer’s 1986 result is explicitly a non-Gaussian RG fixed point for hierarchical scalar lattice field theories. Their 1993 account describes a nonlinear RG operator on a Banach space of analytic functions; an extension of interval arithmetic to that function space proves existence and local uniqueness, with bounds evaluated on a computer. These are genuine rigorous RG fixed-point results at a nontrivial fixed point. The model is hierarchical. The accessible abstract does not specify the number of retained coordinates or execution cost, so neither is inferred here. The 1996 Koch–Schenkel–Wittwer paper is a computer-assisted proof and exposition for the Feigenbaum equation/logic-programming method, not evidence of a nonhierarchical four-dimensional gauge RG step.

Sources: Koch and Wittwer, [1986 paper record and DOI](https://doi.org/10.1007/BF01207260); [1993 conference abstract](https://interval.louisiana.edu/NAARV-93-abstracts.pdf); Koch, Schenkel, and Wittwer, [author-hosted 1996 paper](https://web.ma.utexas.edu/users/koch/papers/prolog.pdf).

### Later interval arithmetic: nonhierarchical tensor RG

Ebel, Kennedy, and Rychkov’s 2x1 tensor RG is the closest positive example found that is both rigorous and applied to a nonhierarchical lattice model. It treats square-lattice Ising and XY high-temperature regimes. Each tensor leg belongs to an infinite-dimensional separable Hilbert space, and rigorous component estimates use a weighted Hilbert–Schmidt norm. The authors form a finite “hat tensor” master map bounding 63 orthogonal sectors; the theorem shows that sector deviations at most `0.02` flow to the high-temperature fixed point. Their implementation uses interval arithmetic (reported initial precision `10^-21`, subsequently `10^-17`) and reports 15 master-map iterations for the stated parameter example. No wall-clock cost is reported. Although the underlying tensor legs are infinite-dimensional and the lattice is nonhierarchical, the theorem controls a specific small high-temperature box through 63 sector envelopes; it does not establish that a general 4D non-Abelian block action lies in that box. Its certified domain is high temperature, not the requested order-one last-scale gauge step.

Source: Ebel, Kennedy, and Rychkov, [“Tensor Renormalization Group Meets Computer Assistance”](https://arxiv.org/html/2506.03247).

**Finding for (a):** rigorous computer-assisted renormalization examples exist, including a nonhierarchical 2D tensor flow, but the reviewed proofs do not supply a published order-one-coupling step whose controlled space is shown to contain a four-dimensional non-Abelian gauge block action. For Lanford/Koch–Wittwer, coordinate count or runtime was not found in the accessible cited source; for the tensor result, the finite control description is 63 sectors and the paper reports iterations/precision but no wall-clock cost.

## (b) Non-Abelian step scaling since 2020

The bounded search was for proved inequalities on a non-Abelian lattice-gauge step-scaling function in twisted-boundary, gradient-flow, or Schrödinger-functional schemes. It found numerical determinations and continuum extrapolations, but no theorem-level inequality of the requested kind. Examples illustrate the distinction:

- Hasenfratz, Rebbi, and Witzel’s SU(3), eight-flavor gradient-flow step-scaling result is based on generated gauge configurations and measurements, with continuum extrapolation; this is a numerical nonperturbative determination, not a rigorous enclosure/proof of an inequality. [Paper](https://arxiv.org/abs/2210.16760).
- The SU(3) twisted-gradient-flow strong-coupling study uses simulations and twisted boundary conditions to determine a step-scaling sequence. Its strong-coupling reach makes it relevant as numerical evidence, but it does not prove a step-scaling inequality. [Paper](https://arxiv.org/abs/2403.13607), [published version](https://doi.org/10.1140/epjc/s10052-024-13261-z).
- A 2025 SU(N) twisted-gradient-flow scale-setting paper describes determining the scale; its stated eventual goal is a step-scaling determination, so it is not itself such a result. [Paper](https://arxiv.org/abs/2501.18449).

This is a bounded search result, not a proof that no such theorem exists. The repo prior on Kanazawa’s twisted-boundary Wilson-loop estimate is adjacent but conditional on exponential twist decay and is not a proved step-scaling inequality at order-one coupling (see Repo search above).

## (c) Tomboulis obligation after Ito–Seiler

The repo’s prior work calls the remaining bridge `(TB)_n`: the common matching/interpolation inequality needed to compare the true model’s odd-flux weight to the positive-character comparison model across the decimation step. That label is the repo’s bookkeeping shorthand; the papers do not use it as a named theorem. Row 1025 already records the precise unresolved point: at `r=1`, the flow is the cited Ito result, while the exact `A(alpha)>A^+(alpha)` / ratio bridge and a valid matching parameter remain unproved in the covered argument.

The primary dispute located is Ito and Seiler’s 2007–08 exchange with Tomboulis. Ito–Seiler state that the interpolation function’s implicit-function branch is only local: the implicit function theorem does not establish continuation to the required endpoint `lambda=1`; a global continuation/contraction argument is missing. They also explain the tension between choosing `r<1` to keep interpolation parameters bounded away from one and taking `r` toward one to reach large beta. Their discussion says the relevant `A >= A+` estimate is established only in the small-coefficient/high-temperature regime, not in the needed general regime, and uses U(1) as a diagnostic for the gap. Tomboulis’s reply disputes that these are missing links; it does not provide an independently accepted proof resolving the continuation/bridge objection in the sources located.

Post-2015 search did not find a published repair of this specific interpolation/ratio obligation. Chatterjee’s 2021 paper provides broader context that the four-dimensional non-Abelian confinement/mass-gap problem remains open, but is not itself a technical analysis of `(TB)_n`; it should not be treated as proof that no later repair exists. The repo’s row 1025 and its cited primary papers remain the closest specific treatment found.

Sources: Ito and Seiler, [arXiv:0711.4930](https://arxiv.org/abs/0711.4930), [“Further discussion…” arXiv:0803.3019](https://arxiv.org/abs/0803.3019); Tomboulis, [reply arXiv:0712.2620](https://arxiv.org/abs/0712.2620); Chatterjee, [“A probabilistic mechanism for quark confinement”](https://par.nsf.gov/servlets/purl/10339807).

## Decisive outcome and limits

**No qualifying published step was found in this bounded search.** The nearest qualifying shape is the computer-assisted, nonhierarchical 2D tensor RG, but it proves flow only from a small high-temperature neighborhood (`0.02` in 63 sector bounds), not at order-one coupling and not for a four-dimensional non-Abelian block action. The hierarchical scalar proofs and Feigenbaum proofs do not supply that missing scope. Recent non-Abelian step-scaling results located are simulation-based rather than rigorous inequalities. No post-2015 source was found that repairs the specific Tomboulis matching/ratio bridge identified by Ito and Seiler.

This is an empty search result within the sources and paths that could be inspected, not a universal no-go theorem. The requested local outline index, Balaban quotation file, open registry, and Sussman–Alpoge source files were missing at their specified paths, so this note cannot certify completeness against those materials. No Monte Carlo or unchecked floating-point calculation was used as proof. No Lean-kernel computation was performed or claimed.

## Search log (continued)

- 2026-11-22: Read the available pinned-checkout instructions, target/comparison FINISH rows, and remote-repository prior hits. Confirmed the local index/account paths are unavailable before attempting any outline/account line selection.
- 2026-11-22: Reviewed primary Lanford, Koch–Wittwer, later interval/tensor-RG, non-Abelian step-scaling, and Ito–Seiler/Tomboulis sources. Logged exact method scope and omitted costs rather than estimating them.
- 2026-11-22: Concluded no found source meets the combined order-one coupling + four-dimensional non-Abelian block-action function-space + stated size/cost criterion. This is a bounded negative search only.

RESULT (2026-11-22): No qualifying published order-one-coupling renormalization step was found in the bounded search; the nearest nonhierarchical rigorous tensor-RG result is a 2D high-temperature theorem controlled by 63 sector bounds of size 0.02, with no stated wall-clock cost.
