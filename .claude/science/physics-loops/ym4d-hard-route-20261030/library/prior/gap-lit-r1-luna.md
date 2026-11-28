# R1 literature scan — R1 trigger, 2026-11-23

## Repo search

Searched `/Users/jonreilly/Projects/Physics` with `git grep -n -i -E '<terms>' origin/main pr/10114 pr/10133 pr/10134 pr/10141 -- '*.md' '*.tex' | head` (each command bounded):

1. `mass gap|area law|stiffness|good[- ]cell|contraction estimate|order[- ]one coupling|order[- ]one` produced mostly unrelated uses of “area law” and “stiffness.” No qualifying published result surfaced. The narrower follow-up `one-cube|order-one.{0,30}(gap|coupl)|neutral.{0,30}(cell|observable)|non-abelian.{0,30}(mass gap|area law|stiffness)|good[- ]cell|local two-sector` found the nearest internal gauge-lane matches:
   - `origin/main:.claude/science/physics-loops/su2-gauge-aligned-response-20261108/PROOF_TREE.md:45` calls Vc “Small-background compact connected response.” Lines 46–48 leave rough terminals/new conditional classes, depth/cutoff control at physical scales, and a positive physical spectral gap open. It is close in object type (local gauge-cell response), but not an order-one estimate and expressly leaves critical steps open.
   - `origin/main:.claude/science/physics-loops/su2-gauge-aligned-response-20261108/gates/two-step-compact-polymer-check.md:66` says, “The good-cell implication has the correct constants,” for its principal-angle chart implication under the internal small-background condition `T_X<q`. This is a local internal implication, not the requested published order-one selective bound or a 4D neutral-observable readout.
2. A third bounded query, `gap-mech-direction3|K-I|K-II|M-neutral|cell contraction|Wilson action.{0,40}order-one|order-one.{0,40}Wilson`, was noisy due to common identifiers and yielded no additional YM statement. The first broad output was also noisy; this documents a bounded search, not an exhaustive claim about every mention. The hits are credited and not redone below.

## Plan

1. Predecessor `library/prior/gap-lit-r1-luna.md` was absent. Read predecessor scans `gap-mech-lit-luna.md` (row 1379) and `gap-gauge-stiffness-read-opus.md` (row 1012); do not repeat their coverage. Read GOAL.md, required FINISH sections, row 1442-1443 trigger definition, open registry, and index/source lines needed to confirm scope and ownership.
2. Check public `github.com/openai/math` for Yang–Mills material added since row 1379, and `github.com/ethanwsussman/Yang--Mills-LLM-experiment` for commits after `31a47c543775`. Read only; post nothing.
3. Search arXiv hep-th, hep-lat, math-ph, and math.PR for relevant work posted 2026-11-15 through 2026-11-23. For each candidate, record observable, ensemble, scale/regime, selective inequality and hypotheses, where non-abelian structure enters, how a 4D neutral observable would read it, and evidence class.
4. Append each source/search result immediately. Stop at bot checks, sign-in, or paywalls. Do not pay or commit PDFs; download only into a newly created empty `/tmp` subfolder if needed.

## Search log and findings

### Scope check and local source access

- This output did not exist before the run. The two predecessor files are read: `gap-mech-lit-luna.md` already covers the 2D O(4) sharp-mass paper and the 2D Ding–Huang–Yang loop-soup proof; `gap-gauge-stiffness-read-opus.md` covers the pre-2026-11-15 gauge stiffness, SF, strong-coupling, and spin-wave literature and the earlier `openai/math` snapshot. Those sources are not repeated below.
- `library/open-registry.md` has no entry for this literature scan or its R1 trigger. The precise current band obligation remains distinct: row 1442's R1 asks for a published/postable order-one-coupling selective inequality. Row 1443 requires a named observable, ensemble, scale, and 4D-neutral readout. No other registry owner covers this literature scan.
- The requested local outline `/Users/jonreilly/sa/YM4_sketch_500.tex` is absent (`ls /Users/jonreilly/sa` reports no such directory), so its indexed lines could not be checked. `library/sa-index/README.md`, the relevant rows of chunks 01, 29, 30, and obligations were checked first. The index says lines 31871–31882 prove only that polynomial decay need not imply a mass gap; lines 32487–32490 mark external OS reconstruction, full-theory identification and any mass-gap estimate as separate; lines 588–599 require a spectral interval exclusion. This is consistent with GOAL's separate later mass-gap target, but the source wording is not independently verified here.

### Public `openai/math` current contents

The local `git ls-remote` attempt could not resolve `github.com`, so I checked the public GitHub pages and raw catalog through the web reader. The current `main` README reports 721 manuscripts in 373 families. Its `CONTENTS.md` search for `Yang--Mills`, `Yang-Mills`, and `lattice gauge` has no matches. `history.md` lists updates through 29 October, with the latest new results dated 26 October; none is Yang–Mills. Thus I found no Yang–Mills write-up/folder in the current public catalog added after the predecessor scan. This is catalog/history coverage rather than an exhaustive scan of all 721 manuscript texts; it does not reproduce the predecessor's earlier repository audit.

### Sussman–Alpoge repository update after base `31a47c543775`

The public history exposes commit [`af07f3e982b7ee089c8a357ca52a1627af425217`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/commit/af07f3e982b7ee089c8a357ca52a1627af425217), titled “Update YM4 proof sketch and add matching 505-page PDF,” changing `YM4_sketch_500.tex` (+7,091/−134 lines) and the PDF. The raw TeX at this commit was readable; no PDF was downloaded. The repository README labels YM4 unfinished and the material work in progress, not satisfactorily vetted.

- **Observable, ensemble, scale/regime:** the revised outline is for the renormalized scalar `tr(F^2)` observable in four-dimensional Wilson `SU(2)` theory. Its finite-cutoff starting law is the Wilson measure `Z_beta^{-1} exp(-beta A(U)) dU`; the stated construction uses a volume-first subsequential continuum limit along an admissible weak-coupling sequence, not an order-one-coupling regime (TeX lines 44–65, 125–131, 4213–4218).
- **Selective inequality / hypotheses:** no R1 inequality was found. The text explicitly says polynomial clustering does not imply a positive mass gap, and that a separate spectral-support exclusion estimate is required (lines 528–538 and 4183–4190). It proves a finite-dimensional uniform *scalar block-constrained* gap, but says this gives neither vector-field coercivity nor a physical Hamiltonian mass gap (lines 543–551, 689–701). Closest to a cell-event estimate, the outline claims under its law of RG histories that the probability a cell is live or created is at most (Ce^{-cp_0(g_k)}), uniformly in volume (line 20913). This is an outline-level assertion at small coupling (glegamma_star), with history events rather than a fixed-physical-scale observable; it does not compare with compact U(1). The text itself warns that a related event can become likely as volume grows, and that its history-law theorem gives no bound on the bare plaquettes in a fixed physical box (line 21575). A separate pointwise reserve hypothesis is explicitly refuted on unrestricted bare fields by a plaquette with (U_p=-I); the proposed site-reserve ratio diverges (lines 4799–4813). That counterexample constrains a proof route but is not the requested positive order-one selective estimate. The phrase searches for `stiffness`, `area law`, `good-cell`/`good cell`, `selective`, and `one-cube` found no named theorem of those types. The outline does include many local RG obligations, but no candidate found here met row 1443's observable/ensemble/scale/selectivity/readout requirements.
- **Non-Abelian structure:** the model uses `SU(2)` link variables and Wilson plaquette action, with non-Abelian group integration. The finite-dimensional scalar Poincaré estimate itself is a scalar graph/block calculation, not a non-Abelian-selective result.
- **4D neutral readout:** `tr(F^2)` is a gauge-invariant scalar observable and the theorem aims at its scalar sector, but no new order-one estimate connects it to a neutral mass-gap, decay, stiffness, or good-cell readout.
- **Evidence class / distance from R1:** revised LLM-drafted research outline with detailed claims and open obligations; not independently verified here and not a Lean-kernel proof of this R1 statement. The separate block-constrained inequality is an exact elementary finite-dimensional calculation but has the wrong operator/observable target. The new text itself leaves physical mass gap open, so this update does not satisfy R1.

Access to the raw `.tex` was available, so the mass-gap/band question was read; GitHub's rendered blob page had a cache miss, but this did not prevent reading the raw source. The 505-page PDF was not read or downloaded. Search terms in the updated TeX: `mass gap`, `stiffness`, `good-cell`/`good cell`, `area law`/`area-law`, `order-one`/`order one`, `one-cube`, `single-cell`, `selective`, `band`, and `coupling`.

### arXiv candidate: Drummond–Giménez Umbert–Mitra (20 Nov 2026)

**James Drummond, Bruno Giménez Umbert, and Prahar Mitra, “Bulk Wilson Loops from I,” arXiv:2611.27739v1 [hep-th], submitted 20 Nov 2026.** [Official arXiv record](https://arxiv.org/abs/2611.27739); [full HTML](https://arxiv.org/html/2611.27739). Read the abstract and introduction, especially §§1 and 4 summary (HTML lines 37–68, 270–290).

- **Observable, ensemble, scale/regime:** expectation of a null polygonal Wilson loop in four-dimensional Minkowski Yang–Mills, represented by a proposed operator on future null infinity. The paper computes only the first nontrivial perturbative order, `O(g^2)` (single-gluon exchange); no Gibbs ensemble, lattice scale, or infrared/correlation-length regime is stated.
- **Statement and hypotheses:** analytically matches the rational integrand of the bulk Wilson loop to a Carrollian boundary calculation at `O(g^2)`. This is a perturbative observable identity, not an inequality, decay estimate, stiffness bound, or good-cell probability.
- **Non-abelian structure:** Yang–Mills Lie-algebra gauge field with the commutator in `F=dA+g[A,A]`; at `O(g^2)` the loop expectation reduces to single-gluon exchange. The reported matching does not isolate a non-abelian-selective mechanism or compare against compact U(1).
- **4D neutral readout:** the Wilson loop is gauge-invariant, so it is a neutral observable in the basic sense. The paper gives no route from its null-infinity perturbative expectation to a fixed-physical-scale Euclidean neutral spectral or correlation estimate.
- **Evidence class and distance from R1:** analytic perturbative calculation in a theoretical paper, not a numerical claim; far from R1 because it neither controls order-one coupling nor proves a selective inequality.

### arXiv search log, 2026-11-15 through 2026-11-23

Queries run (exact terms, on the public search reader):

1. `site:arxiv.org/abs/ "lattice gauge" "Nov 2026" mass gap`
2. `site:arxiv.org/abs/ "Yang-Mills" "Submitted on" "Nov 2026"`
3. `site:arxiv.org/abs/ "Wilson loop" OR "area law" arXiv November 2026 Yang-Mills`
4. `site:arxiv.org/abs/ (stiffness OR "good cell" OR contraction) gauge theory arXiv 2026`
5. `site:arxiv.org/abs/2611. "Yang-Mills" after:2026-11-15`
6. `site:arxiv.org/abs/2611. (hep-lat OR "lattice gauge") after:2026-11-15`
7. `site:arxiv.org/abs/2611. (confinement OR "mass gap" OR "area law") after:2026-11-15`
8. `site:arxiv.org/abs/2611. (stiffness OR "helicity modulus" OR "good cell") gauge after:2026-11-15`

The search surfaced only the cited `Bulk Wilson Loops from I` as a plausible new Yang–Mills paper. The date/category new-list checks for hep-th, hep-lat, math-ph, and math.PR (23 November lists) showed no further candidate meeting the question's target. Queries 5–8 returned empty search results. This is a bounded search of results and visible category lists, not a claim that every submission in those categories has been inspected. No bot check, sign-in gate, or paywall was reached for arXiv; the direct API route failed, so no source was downloaded.

## Disposition

The only arXiv candidate found was a perturbative Wilson-loop matching identity, not an inequality. The current `openai/math` catalog had no YM addition. The Sussman–Alpoge post-base outline update was readable and explicitly keeps the physical mass gap separate; its closest cell-history event estimate is in a small-coupling RG-history law and lacks the R1 physical observable and U(1) comparison. It also contains no qualifying order-one stiffness/area-law/good-cell bound. No qualifying selective inequality or U(1)-failing non-Abelian result was found in the bounded arXiv sweep. The remaining uncertainty is search coverage, not a candidate with unresolved technical details.

RESULT: Found one nonqualifying O(g^2) 4D Wilson-loop identity and one updated SU(2) outline with a small-coupling RG-history cell-event estimate but an explicit separation from physical mass gap; found no published/postable order-one selective inequality that fails compact U(1); not read the 505-page Sussman–Alpoge PDF or the full arXiv paper, not exhaustively scanned all 721 `openai/math` manuscript texts or every category submission, and did not verify material beyond the recorded bounded searches.
