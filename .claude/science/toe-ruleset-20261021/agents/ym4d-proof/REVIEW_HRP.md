# Independent hostile review of HRP — 29 October 2026

The finite Wilson RP proof, zero-source bare-marginal identity, coordinate-sphere RP proof and conditional limit arguments survive this review in their stated domains. The packet is **held because the required executed exact-check evidence is absent**. The independent rerun also stopped at the mandatory priority guard. Completing that verification requires an actual compliant execution and inspection of its certificates, so the remaining work exceeds wording corrections. The two analytically predicted negative-control criterion failures are disclosed correctly and do not themselves refute the positive theorem.

This report executes `briefs_hrp/REVIEW_BRIEF_HRP.md`. It is a source review, with no audit, banking, commit, push or PR action. Only this repository file was edited. Temporary evidence and a byte-identical execution mirror are in `/private/tmp/review-hrp-k0ev7iku/`; the prescribed worktree numeric lock was created and removed by the launcher.

**Source identity and coverage.** HEAD is `1d221a0063566d5270b60cc543690d7c4d8c68ba`; the reviewed local `origin/main` is `ca2bc7ddf64790da96cd43d42017d000fbfe4808`. Remote freshness could not be checked: `git ls-remote` failed to resolve github.com. The workflow, reviewer skill and its freshness/proof-governance references match this main snapshot byte for byte. The source snapshots, full provenance verification and extracted main notes are preserved in the temporary evidence directory.

| Artifact | Reviewed SHA-256 |
|---|---|
| HRP.md | `d85027730ac0c7d4c6102ede801be3f4f8cd3b89a34910675280cde15a5f11b7` |
| HRP_LOG.md | `8431dc348de69c17d1e3525e904e65048f3a8134ee40b5d4a94fcb4d10854c2c` |
| SPHERE55.md | `658bdd59998263c824b6f3c2cc239df6b16cad8704eae0b0e44ff97413366cba` |
| HANDOFF.md | `ad2ffa6db132c302a3283050bfe2f6cb14e130d454ba2f710f24ffd7960bd4e3` |
| checks/hrp_criteria.md | `3e00f5ec5bbc32522636004aa72628c45884fe3762573c047e1105593ea82173` |
| checks/hrp_exact.py | `e951fb782c09534aac8a7c178b5963b731274fff83de6c34a5b7afe52415e2b6` |
| checks/hrp_run.sh | `893d362daf45eeb30c78a6cb1b658a4572d696b62f05ebad9813c7c72a86ba98` |

I read HRP and HRP_LOG completely, the entire current runner, its complete differences from the archived first script/launcher, criteria, manifests and receipts, and both complete appended corrections. Source examination covered ASSEMBLY55 N0/N1F/N1S/N3/F3/F25; SPHERE55 §§1–2, §§5.1–5.4, §§12–14; PANEL_P1's algebra/closure contract; OSLEAF55 D1–D9, RP-lat, CLOSURE-sep, CONTRACT-sep, trajectory, relevant errata and BRIDGE's RP export; CODEX_REVIEW_P4 §1.1 and §4.1–§4.3; CODEX_REVIEW_HINT §5 and banking item 4; PROOF S4′/S4″, Decision 4 and L9a/L9a-m/L9a′; ROTDEF's clover/chain/support definitions; RLARGE's exact chain/history definitions; SRCAN55's source tilt; and the four specified main notes at the component boundaries discussed below. Other analytic estimates, reconstruction and fermionic claims are outside this review's certification.

**1. Provenance — CONFIRMED-WITH-FIXES.** References: HRP.md:3–29; HRP_LOG.md:17–27, 91–153; checks/hrp_criteria.md:1–40.

The first 1,881 bytes of current HRP have exactly the logged initial hash `de2d53d4bfc42fc6b78580e6da82a6f40e5eb72478e1b9705d8a557e2790e3bf`. That prefix contains the heading and PRE-STATED targets only, with no derived result. The criteria have the recorded 2,734 bytes and unchanged hash, with statements/thresholds rather than computed answers. Native filesystem times give:

| File | Birth time, UTC | Relevant observation |
|---|---|---|
| HRP.md | 16:52:09.334988 | Consistent with the initial log receipt |
| hrp_criteria.md | 16:52:09.382908 | mtime 16:52:09.382975; predates both script and launcher |
| hrp_exact.py | 17:03:32.950748 | Later additions documented |
| hrp_run.sh | 17:04:10.794610 | Later timing-option change documented |

All manifest hashes checked. Every unchanged source still matches its initial hash; SPHERE55's original 79,626-byte prefix and HANDOFF's original 35,373-byte prefix match exactly. The first-attempt source archives match their logged hashes. The only script differences are the additional Q8 word check, crossing-4-cell assertions and invocation; the launcher changes `time -l` to `time -p`. Both sets of failed-run receipts are byte-identical. Python AST parsing, shell syntax checks and `git diff --check` succeeded; these are mechanical checks.

**Fix/qualification:** describe the first-edit claim as corroborated by the preserved prefix, log and filesystem chronology. This fresh context did not witness that edit, and these mutable local records are not an independently authenticated edit history. No contrary provenance evidence was found. This qualification is not the reason for HOLD.

**2. Flat finite-torus proof — CONFIRMED.** Fix: none to the theorem or proof. The following line-level checks include the boundary cases rather than relying on the older slab theorem.

| Step and source lines | Verdict | Independent check / required scope |
|---|---|---|
| Kernel sign and convergence, HRP.md:82–117 | CONFIRMED | `Re Tr(BA†)` is the real matrix inner product; the nonnegative exponential coefficients and uniform majorants are correct. `c=β/N`, including `β=0`, has the right normalization. |
| Haar half-link substitution, HRP.md:119–173 | CONFIRMED | Independent Haar `h_- h_+^{-1}` is Haar. Substitution in `U_- C_w U_+^{-1} C_v^{-1}` gives a conjugate of `BA†` with the displayed order. Reflection exchanges the auxiliary halves. Multiplying kernels and integrating gives the stated squares. |
| General versus gauge-invariant observables, HRP.md:63–72, 168–196 | CONFIRMED | The half-link proof applies to all bounded functions of original half-contained edges. Original crossing links are excluded. Gauge averaging is an optional second argument on disjoint vertex halves; it is not applied at shared site-boundary vertices. The L² extension follows from truncation and ordinary Cauchy–Schwarz. |
| Both link-reflection planes, HRP.md:200–228 | CONFIRMED | For `r(t)=1−t` on `Z/(2m)`, the two fixed geometric planes are `1/2` and `m+1/2`. Temporal plaquettes with bases `0,m` are precisely the two crossing families; spatial layers and remaining temporal bases pair. Both cuts appear in the product. |
| Site reflection, HRP.md:230–258 | CONFIRMED | For `r(t)=−t`, condition on all spatial links at both `0,m`. Reflection fixes their directed variables pointwise. Each plaquette belongs to a single closed half or a fixed plane. The conditional integral is an absolute square times `exp(−S_0(W))`. |
| Extent two and mixed reflection, HRP.md:185–196, 202–216, 256–268 | CONFIRMED | At extent two the two geometric temporal arcs are distinct edges, even with identical endpoint pairs. Half-link splitting still works; the matching gauge proof is correctly restricted to extent at least four. The auxiliary odd-circle result combines one site boundary with one link boundary. |

For an additional derivation of the load-bearing kernel, realify a unitary matrix as `u∈R^(2N²)`, so `|u|²=N`. For `c>0`, with `ξ` a centered real Gaussian of covariance `cI`,

```
exp(c Re Tr(BA†))
  = exp(cN) exp(−c|b−a|²/2)
  = exp(cN) ∫ exp(iξ·b) overline{exp(iξ·a)} dγ_c(ξ).
```

The Gaussian characteristic function follows by integration by parts and its value at zero. This proves kernel positivity by a Fourier integral, independently of the author's entrywise series and representation-ring expansion. Its features have modulus one, so finite products and the bounded half-integrals may be interchanged. At `c=0` use the constant feature. The split-link word, checked directly by multiplication, then yields the same integrated nonnegative form.

The sign restriction is used only for crossing kernels in the link/mixed cases. Real paired same-half couplings may be negative. Site RP needs no coupling sign at all. The optional matching gauge transformation fixes only crossing links and leaves temporal Polyakov holonomy in the remaining links; no trivial-holonomy restriction is imposed.

**3. Actual bare marginal and construction operations — CONFIRMED.** References: HRP.md:272–322; PROOF.md:1007–1020, 2051–2055, 2080–2087; RLARGE.md:45–57; ROTDEF.md:300–308; SRCAN55.md:129–140; CODEX_REVIEW_HINT.md:229,292; OSLEAF55.md:535–572. Fix: none; retain the explicit zero-source/full-chain qualifications.

The normalizer in Decision 4 integrates the same numerator over each outgoing coarse link. Reverse integration over `U_K,…,U_1` therefore leaves exactly `exp(−S_0(U_0))` and its Wilson partition function. Neither a terminal coarse weight nor a conditioning indicator occurs in that zero-source definition. Kernel parameters selected as deterministic functions of the chosen trajectory do not change this identity.

S4′/S4″ is a deterministic bare-link map, distinct from the auxiliary coarse random field. Averaging contours changes the kernel center, and division by its field-dependent normalizer is essential; neither reweights the fully marginalized bare law. Real reflected centering and normalization change the observable. Choosing another bare coupling changes which Wilson measure is used and requires its sign/symmetry hypotheses anew. The source tilt really changes the coefficient to `u_0−(1/2)Σ_corners η(x)`, while retaining the kernels. Conditioning on a coarse field/history generally changes the law. HRP correctly excludes those changed laws from its unconditional marginal/RP assertion. The lane and standard coupling normalizations are distinguished, and existence of the selected real trajectory remains an input.

**4. Supports, domains and limits — CONFIRMED.** References: HRP.md:324–356, 483–577; ROTDEF.md:117–131; PANEL_P1.md:54–65; OSLEAF55.md:149–194, 292–365, 767–769, 791–795, 859–876. Fix: none; preserve the separate ordinary-polynomial and restricted-domain exports.

The clover stencil stays within coordinate distance `a` of its insertion. Distance greater than `a` from both link-plane boundaries suffices; the site version includes links on the fixed slice. An exhausting torus eventually contains every fixed compact positive-time support and its stencil. The common reflection, paired real volume/normalization factors, and exactly one complex conjugation make the displayed lattice RP identity correct.

For each fixed polynomial, only finitely many expectations are used, on the already chosen common sequence. HRP explicitly consumes convergence of those products and any continuity needed to reach them from a determining family. Moving a link plane by `a/2` requires the named test-function continuity if one compares with a fixed continuum plane; site reflection avoids that error.

For the restricted OS domain, compact time-ordered tests have all insertion times distinct and positive. Their reflected tensor products avoid every coincidence. Continuity of the limiting distributions on `^0S_n` and convergence on the required compact separated tests are separately consumed from H_reg/(EXT). Boundary flatness makes cutoff derivatives harmless and supplies the stated density argument. Ordinary `e(f)²` is not silently admitted. Fixed-radius closure is local to the stated cap domain; radius-uniform continuity/convergence and a common diagonal are additional inputs for the second limit. None of the analytic Yang–Mills estimates, reconstruction or algebra acceptance is proved by this review.

**5. Sphere coordinate RP and the appended repairs — CONFIRMED.** References: HRP.md:360–479; SPHERE55.md:123–163, 196–245, 297–303, 581–590, 843–908; HANDOFF.md:520–554. Fix: none to the construction, proof or appended corrections.

This is the actual doubled digital ball with a collar, not a replacement lattice. The condition `Σ a²(|k_ν|+1/2)²≤R²` is sign-invariant. A chart cube crossing `x_μ=0` has its μ-interval centered at zero. A boundary 3-face crossing the plane has the same free μ-interval, and its collar prism is fixed. Every interaction 2-face is either a chart square or `e×[0,1]`; these exhaust the action's cells, with multiplicities combined in the effective coefficient.

For a crossing seam square, `e=(v,θ_μv)`. The seam edges `C_v,C_w` preserve chart coordinates and lie in opposite halves; the two chart copies of `e` are the crossing links. Direct multiplication gives

```
B_s C_w B_n^{-1} C_v^{-1}
  ~ h_{s,+}^{-1} C_w h_{n,+}
       (h_{s,-}^{-1} C_v h_{n,-})^{-1},
```

where `~` denotes conjugacy and hence equality of traces after the half-link substitution. The two factors are reflected copies. Chart crossing squares have the factorization checked in item 2; the remaining plaquettes pair within their halves. The actual coefficient is `β̂_p=(1/4)Σ_(Q⊃p) 2N/G(aΩ(z_Q))²`, exactly as SPHERE55:160–163 defines it. Real finite nonzero `G` and radial `Ω` make it positive and reflection-paired, including prism centers. Haar reference measure is invariant under edge permutations/inversions; the Wilson density itself is not called a product measure.

No regulator change or new seam hypothesis is needed for finite coordinate RP. SO(4) invariance of the continuum cap state transports it to all great spheres through the base point; translations of the flat limiting state then give affine planes. Those state-invariance inputs remain separate. The appended SPHERE55 erratum accurately quotes and repairs the earlier “cross-check” inconsistency, and replaces the constant-β shorthand by the incidence sum. The HANDOFF append accurately repairs F25 without rewriting the historical text or promoting the result to banked status.

**6. Exact checks — CONFIRMED for the arithmetic design; REFUTED as a completed verification deliverable.** References: HRP.md:632–737; checks/hrp_exact.py:59–105, 108–216, 234–260, 280–345, 367–468, 471–573; checks/hrp_run.sh:1–41; HRP_LOG.md:91–153.

The source constructs rational Wilson weights by logarithmic couplings and positive configuration-independent rescaling. The transfer formula sums both temporal links and closes all four time steps. The link basis uses the reflected `(g_0,g_3)` versus positive `(g_1,g_2)` class pair; the site basis shares both fixed slices. Spatial tree gauge is legitimate for these gauge-invariant indicators. The Z2 direct enumeration uses the original links and is a different implementation. The 3D all-group models are honestly identified as decoupled sheets; additional Z2 models include all 48 strictly positive plaquette coefficients. The small sphere diagnostic uses the actual cell incidence construction with chosen radial test weights; its integrated Gram is explicitly a local six-face prism model, not the full K_a law or a computed physical coupling trajectory.

Integer numerators and positive normalization give exact rational Gram entries. The Schur-complement algorithm correctly treats negative pivots and zero pivots with nonzero residual rows. No floating eigenvalue tolerance certifies PSD. The Q8 representation check uses only exactly representable entries `0,±1,±i`; subsequent Gram arithmetic is integer/rational. These are source-level conclusions. There are no executed matrix files to certify: the only submitted `hrp_*.json` files are the source manifest and mechanical author validation.

The independent attempt used **byte-identical** current script, criteria and launcher in a temporary mirrored folder. A temporary symlink lets the script's relative lock test refer to the same actual worktree lock that the unchanged launcher acquires. Command: `sh checks/hrp_run.sh`, cwd `/private/tmp/review-hrp-k0ev7iku/.claude/science/toe-ruleset-20261021/agents/ym4d-proof`. Full receipts are in its `checks/` directory.

```
Preflight: load=2.37158203125, free_memory_percent=35
After lock acquisition: memory_pressure free percentage=35
nice: setpriority: Operation not permitted
hrp_exact.py:519: AssertionError: nice level >=10
real 0.05
user 0.02
sys 0.00
numeric_exit=1 cleanup_exit=0
```

The script exited before START, group construction or any scientific computation; stdout is empty. The launcher removed the prescribed lock exactly once, and no job remains. The resource guards were preserved. The review cannot confirm execution, PSD certificates, actual control outcomes or completion within the scientific workload's resource budget. The author reports this limitation honestly at HRP.md:732–737; the REFUTED label here concerns completion of the required deliverable, not an alleged false author PASS or an RP counterexample.

Independent **hand algebra**, not runner output, checks the planned controls:

| Control | Exact analytic check | Verdict against the requested raw-negative-eigenvalue criterion |
|---|---|---|
| One negative crossing β, script:473–478 | For the Z2 slice transfer, the ordinary matrix is `K=[[34,16],[16,34]]`, while the changed crossing step is `K_-=[[16,34],[34,16]]`. The Gram numerator is `D(K_-⊗K)D`, `D=diag(34,16,16,34)`. The vector `D^{-1}(1,1,−1,−1)` has quadratic form `−3600`, before positive normalization. | Negative direction proved analytically; execution unverified. |
| Asymmetric coupling, script:480–492; HRP.md:713–729 | The numerator is `D_-(K⊗K)D_+` with the displayed positive diagonals. Conjugation by `diag(sqrt(D_-/D_+))` gives a positive definite symmetric matrix, so all raw eigenvalues are positive. Its `(0,1)` and `(1,0)` entries differ: `544·34·40 ≠ 544·16·130`. | Criterion fails. Non-Hermiticity is a real RP defect, but is not a negative raw eigenvalue. |
| Asymmetric crossing cell, script:494–515; HRP.md:691–711 | Independent sign summation gives exactly `diag(1,0,0,0)+(3/5)E_(3,2)` in one-based indices. Raw spectrum is `1,0,0,0`; Hermitian-part spectrum is `1,3/10,−3/10,0`, and `F=a−b` gives `−3/5`. | Criterion fails, with an explicit RP witness. This malformed extended cell is not a counterexample to K_a. |

**Binding fix:** execute the frozen scientific runner under the original lock/resource conditions in an environment permitting the required nice priority, preserve all matrices/certificates/receipts, and independently inspect them. Report the two raw-spectrum failures as failures; the brief explicitly allows that reporting. The source schedules 25 positive Gram outputs and five control/control-Hermitian-part outputs; these counts are an execution plan, not observed results. An expected exit 2 for disclosed control failures must be distinguished from assertion/resource failure. Any script change requires an identified new revision and review of the affected evidence. Do not bypass the priority guard or retrospectively convert the failed prerequisite into a successful run.

**7. Exact consumer statement and banking scope — CONFIRMED-WITH-FIXES.** References: HRP.md:739–772; ASSEMBLY55.md:137–181, 402–415, 529–531; PANEL_P1.md:54–65; CODEX_REVIEW_P4.md:246–263; OSLEAF55.md:341–369. The mathematics supplies the appropriate conditional interfaces, but §9 paraphrases them instead of satisfying the brief's word-for-word banking requirement.

**Binding wording fix:** include these exact consumer statements in §9, together with their qualifications:

> N1F / ASSEMBLY55 N3: “The approximants to every positive-half polynomial obey reflection positivity, or have negative errors tending to zero, for one common time reflection.”

For the zero-source Wilson state and the reflection-compatible local bare-link/clover maps proved here, the inequality is exact eventually for every fixed positive-half polynomial; there is no polynomial-dependent subsequence. Convergence of the required products, the common algebra and any extension to its declared continuum domain remain H_reg/(EXT)/ALG hypotheses. Retain PANEL_P1's additional sentence: “Localization/renormalization errors are controlled in the same moment topology.” For the exact maps here those errors vanish eventually.

> N1S / ASSEMBLY55 N3: “RP for great spheres through the base point S”.

At finite cutoff HRP proves the four coordinate reflections. At fixed R it gives the quoted great-sphere property on the specified cap domain after the separately supplied continuum convergence and SO(4)_S state invariance. Radius-uniform convergence/continuity and the supplied translation-invariance step give the flat-limit affine-plane property. The ordinary-moment version and the restricted OS-domain version remain distinct conditional statements; the latter does not silently replace literal N1F/N1S. No declaration that H_reg, H_Euc, the trajectory or the physical theory exists should accompany this export.

**Import check — CONFIRMED at the listed component scopes.** References: HRP.md:594–630. Fix: none; retain the explicit exclusions.

| Pinned origin/main source | Check of HRP's use |
|---|---|
| June 5 Wilson temporal-gauge bridge, §§0–3 | Its open two-slice carrier is explicit. Character multiplicities, convergence, matrix-coefficient factorization and integrated bounded-observable kernel are valid components; they alone supply no periodic theorem. HRP proves the periodic extension itself. |
| May 10 gauge-half Cauchy–Schwarz note, claim scope and G1–G3 | Substitution of its special reflection-Hermiticity and invariant-half-action hypotheses gives its weighted norm identity on the integrable domain. These are not generic Wilson half-observable hypotheses. HRP uses it only for scope comparison. |
| June 2 plaquette-decomposition note, §§1–6 | Both periodic crossing families and the complete-temporal-gauge criterion `P=I` are correctly identified. The note proves decomposition/support facts rather than integrated RP. Its name “site reflection” for `t↦−1−t` is geometrically incorrect; HRP correctly identifies it as link reflection. |
| April 29 parent, scope, dependencies and reroute | This includes separate fermionic/blocked and joint-Gram obligations. HRP neither imports nor certifies those results. Its IMPORTED-NOT-YET-REVERIFIED designation is appropriate. |

The primary [FILS preprint](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/FROHLICH/1978-1980/P_78_224/P_78_224_web.pdf), §2, Theorems 2.1–2.2, supports the stated method attribution: positive paired interactions preserve the generalized form, and commuting halves identify it with RP. The [Seiler book page](https://link.springer.com/book/10.1007/3-540-11559-5) supplies metadata and identifies subscription content; its detailed hypotheses were not reverified. The Osterwalder–Seiler DOI was inaccessible through the web tool in this review. Neither unavailable text is load-bearing; the author marks recalled attribution accordingly.

**Binding disposition and recovery.** Complete item 6's compliant execution/certificate review and item 7's exact export wording. Preserve the two reported control-criterion failures and all scope qualifications. Items 1–5 and the component import checks require no new physics argument on the frozen sources. The author corrections remain append-only, and no regulator change is called for. Source hashes must be refreshed if any argument, runner, criterion or necessary premise changes. The same-source provenance check found no concurrent changes during review. H_reg/(EXT), common-algebra acceptance, cap invariance, trajectory/diagonal construction, H_int, reconstruction, existence and a physical mass gap remain separate obligations.

VERDICT: HOLD
