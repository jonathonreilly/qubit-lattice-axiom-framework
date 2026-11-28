# Repo search

**Searches.** In `/Users/jonreilly/Projects/Physics`, I ran `git grep -n -i -E 'Bakry|Emery|Ricci|log-Sobolev|Langevin'` on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141`, restricted to Markdown and TeX and capped with `head`. I also ran targeted searches for `one-link gradient`, `Dynamical approach to area law`, `Lemma NG`, and heat/noise-gradient wording. In this checkout I searched the lane library for the same curvature terms and the `gap-k2-t2` statement. The exact-topic searches found no Lemma NG or equivalent one-link log-heat-gradient bound.

**Relevant repository hits.** The main-branch mass-gap literature notes already record Shen–Zhu–Zhu’s strong-coupling theorem and Chatterjee’s conditional confinement criterion. The closest source, `origin/main:research/mass-gap/library/prior/gap-crux-lit-2.md`, identifies Cao–Nissim–Sheffield’s “Dynamical approach to area law” as a Bakry–Émery route, but that earlier note had only the abstract: it explicitly did not recover the threshold or theorem number. I read the current primary theorem below to fill that specific gap. The related `gap-math-lit.md` says no order-one 4D Wilson SU(2) Poincaré/LSI result was then known; CNS supplies a larger-range area-law statement, but not a global pure-measure Poincaré inequality. The `research/mass-gap/library/prior/gap-lit.md` entry gives SZZ’s abstract range and says it does not reach the continuum limit; the current primary-source read supplies its exact LSI/Poincaré constants and β conversion.

PR `10114`’s `checks/review_massgap_block_literature.md` discusses strong-flow and twisted/untwisted interpolation, not NG. The broad search produced many false-positive “Ricci” and “curvature” hits in unrelated notes; they were not treated as YM curvature results. In this lane, the existing `gap-k2-t2-representation-check-astra62.md` records the prior novelty search: no explicit earlier one-link score estimate was found. `library/open-registry.md` contains no NG/heat-flow row or competing owner. I reuse those findings and the existing SZZ literature digest rather than count them as new work.

For the required repo-first record: exact-topic search across `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141` found the CNS title in the main prior and found no “one-link gradient” statement. The cited main-branch notes are the closest relevant hits: `gap-lit.md` records SZZ’s abstract-level gap/LSI range; `gap-crux-lit-2.md` records CNS’s abstract-level area-law route but says its numeric threshold and theorem number were not available; and `gap-math-lit.md` says no read source establishes an order-one 4D Wilson SU(2) finite-volume seed. The new primary-source reads below supply the missing CNS threshold and SZZ constants. `pr/10114` matches for “Lemma NG” are unrelated lemmas in YM existence snapshots, so they do not state this heat-flow claim.

# Curvature methods for lattice Yang–Mills: literature digest

Provenance: literature-only result for FINISH row 1477, checkout pinned at `0ef70a148`; no proof, audit, or scientific status is claimed. Sources were read at their statements, with coupling conversions explicit. This file is the only output.

## Lemma NG: how much is known

Row 1474’s precise object is the positive heat image `h_t=P_tD` on a finite product of unit round `S^3` link factors, with `Phi_t=-log h_t`. Its assertion is the supremum estimate `||grad_l Phi_t||_infinity <= exp(-2t)||grad_l Phi_0||_infinity`; the Wilson rule has initial bound `6x`. It says U(1) has factor `1` because its circle Ricci curvature is zero.

The curvature mechanism is classical. Bakry–Émery’s `CD(K,infinity)` gradient estimate for `P_t=exp(t Delta)` is `|grad P_t f| <= exp(-Kt) P_t|grad f|`; see Bakry, Gentil, and Ledoux, *Analysis and Geometry of Markov Diffusion Operators*, DOI [10.1007/978-3-319-00227-9](https://doi.org/10.1007/978-3-319-00227-9). On the round unit `S^3`, `Ric=2g`; the product has the same factorwise lower bound, so the linear heat semigroup contracts a one-factor gradient at `exp(-2t)`. This classical theorem is not itself the log-heat estimate: for `Phi=-log P_tD`, one differentiates the logarithmic heat equation and applies the Bochner identity plus the compact maximum principle to `|grad_l Phi|^2`, yielding decay `exp(-4t)` for its square and `exp(-2t)` for its norm. Thus NG is a direct, elementary Bakry–Émery/Bochner consequence specialized to independent link heat. I found no published paper stating this exact lattice-rule/log-density lemma as a Yang–Mills result. Its mechanism and coefficient are established curvature calculus, not a new YM estimate. The `6x` initial score bound uses the six Wilson staples at a link.

For U(1), `Ric=0`, so this argument yields no strict contraction and the factor is `1`. The comparison is geometric; it does not imply that the noise map supplies a mass gap or a useful end-class criterion. Row 1474 itself notes that its one-link score estimate is not an end criterion and does not solve T2.

## Published and arXiv results

### Shen, Zhu, and Zhu: global infinite-volume gap and functional inequalities

Hao Shen, Rongchan Zhu, and Xiangchan Zhu, “A stochastic analysis approach to lattice Yang–Mills at strong coupling,” *Communications in Mathematical Physics* **400** (2023), 805–851, DOI [10.1007/s00220-022-04609-1](https://doi.org/10.1007/s00220-022-04609-1), [arXiv:2204.12737](https://arxiv.org/abs/2204.12737). I read the theorem statements, action convention, and displayed inequalities in the primary PDF (Theorems 1.2 and 1.4, Corollary 1.6; equations (1.2), (1.3), (1.9), (1.10)).

For `G=SU(N)`, `d>1`, the paper uses weight `exp(N beta sum_p Re Tr Q_p)` and assumes `|beta| < 1/[16(d-1)]`. It proves uniqueness of the infinite-volume Langevin invariant measure, convergence of periodic finite-volume measures to it, exponential Wasserstein ergodicity, and infinite-volume log-Sobolev and Poincaré inequalities. It also treats `SO(N)` for `N>=3`, with `|beta|<(N-2)/[32(d-1)N]`; the stated `SU(N)` threshold is the one relevant to the requested SU(2) comparison. Writing `K_S=N/2-8N|beta|(d-1)>0` in the SU case, their inequalities are

- `Ent(F^2) <= (2/K_S) sum_e E(|grad_e F|^2)` for normalized cylinder `F`;
- `Var(F) <= (1/K_S) sum_e E(|grad_e F|^2)`.

For disjoint supports of smooth cylinder observables, Corollary 1.6 gives exponential covariance decay, with constants depending on support sizes and `K_S,N,d`; its exponential rate constant depends on those same parameters. This is an infinite-volume lattice Langevin gap/correlation theorem, not a transfer-matrix or continuum mass-gap theorem.

Conversion: standard Wilson weight `exp[-beta_W sum_p(1-(1/N)Re Tr Q_p)]` has character coefficient `beta_W/N`. Equating with `N beta` gives `beta_W=N^2 beta`. In four dimensions and SU(2), the range is therefore `beta_W<1/12`. Here `K_S=1-12 beta_W`; hence the printed LSI/Poincaré constants become `2/(1-12 beta_W)` and `1/(1-12 beta_W)` in the paper’s gradient convention. This is strong coupling (`beta_W` near zero), far from order one.

### Cao, Nissim, and Sheffield: slab curvature and area-law decay

Sky Cao, Ron Nissim, and Scott Sheffield, “Dynamical approach to area law for lattice Yang–Mills,” [arXiv:2509.04688v2](https://arxiv.org/abs/2509.04688) (revised 28 September 2025). The primary PDF’s Definitions 1.3–1.4, Theorem 1.6, Proposition 3.2, and equations (1.1)–(1.2) were read. I did not verify a journal publication; this is counted as an arXiv result, as requested.

For `d>=2`, `N>=2`, and `G=SU(N)`, the paper’s coupling `b` appears as `exp(N b sum_p Re Tr Q_p)`. Theorem 1.6 proves constants `C,c>0` (depending on `b,d,N`) such that rectangular Wilson loops with side lengths at most `L/2` satisfy `|E W_l| <= C exp(-c Area(l))`, uniformly in torus side `L`, when `b<1/[8(d-1)]`. It obtains this through a uniform-in-boundary covariance-decay estimate for the conditional `(d-1)`-dimensional sigma models on slabs. Proposition 3.2 gives `|Cov(f,g)| <= C1 exp(-C2 dist(supp f,supp g)) (|||f|||_infinity |||g|||_infinity + ||f||_2||g||_2)`, with `C1,C2` depending on `G,d,b`; the proof invokes the SZZ Bakry–Émery calculation. This is a slab mass-gap input yielding area law, not a full 4D global-measure LSI/Poincaré statement or an unconditional transfer gap.

The paper explicitly notes its Bakry–Émery threshold is twice SZZ’s threshold: it applies the criterion to vertex spins on the slab sigma model. Convert to Wilson `beta_W=N^2 b`; at `d=4`, `SU(2)`, this gives `beta_W<4/24=1/6`. This is the largest coupling I found among the published/arXiv curvature-method results that prove a 4D SU(2) gap or decay, counting area-law decay. It is still a small-coupling window and the statement is an area law through slab covariance decay.

### Adhikari and Cao: finite groups, outside the curvature comparison

Arka Adhikari and Sky Cao, “Correlation decay for finite lattice gauge theories at weak coupling,” *Annals of Probability* **53**(1) (2025), 140–174, DOI [10.1214/24-AOP1702](https://doi.org/10.1214/24-AOP1702), [arXiv:2202.10375](https://arxiv.org/abs/2202.10375). Theorem 1.1 was read in the primary PDF.

This is specifically a four-dimensional finite-gauge-group theorem, not a compact Lie-group theorem. For their character action, let `Delta_G=min_{g!=1} Re(chi(1)-chi(g))`. If `beta >= (114+4 log |G|)/Delta_G`, separated rectangular supports `B_1,B_2` and conjugacy-invariant functions of any finite collection of loop holonomies satisfy

`|Cov(f_1,f_2)| <= 4(4*1024|G|^2)^{|B_1|+|B_2|} ||f_1||_infinity ||f_2||_infinity exp[-(beta/2)Delta_G(L-1)]`.

Their `beta` is the coefficient in `exp[-beta sum_p Re(chi(1)-chi(Q_p))]`; the result is at large beta (weak coupling) and uses a two-copy swapping/topological-defect argument, not Bakry–Émery curvature. Since `G` is finite and `Delta_G` depends on the chosen representation/action, there is no SU(2) Wilson-beta conversion. It neither proves a continuous SU(2) result nor sets the curvature-method maximum.

### Chatterjee: conditional route, no curvature supplier

Sourav Chatterjee, “A probabilistic mechanism for quark confinement,” *Communications in Mathematical Physics* **385** (2021), 1007–1039, DOI [10.1007/s00220-021-04086-y](https://doi.org/10.1007/s00220-021-04086-y), [arXiv:2006.16229v5](https://arxiv.org/abs/2006.16229). I read the abstract and stated implications.

The result gives a rigorous center-symmetry/confinement mechanism for connected compact subgroups of `U(n)`: nontrivial center plus exponential correlation decay under arbitrary boundary conditions implies unbroken center symmetry and confinement. The paper’s separate sufficient conditions are assumptions on slab symmetry or boundary-uniform decay; it supplies no coupling interval proving those assumptions for Wilson SU(2) and no Bakry–Émery estimate. Thus it is a conditional implication adjacent to area-law results, not an additional SU(2) beta range.

## Scope and verdict

- **Lemma NG:** the rate and factor are the classical Ricci/Bochner maximum-principle consequence on `SU(2)≅S^3` and are readily specialized to linkwise heat noise. No exact Yang–Mills-specific published statement was found. The bound is local in link-gradient and provides no mass-gap closure by itself.
- **Largest published/arXiv curvature-method 4D SU(2) coupling with gap-or-decay output found:** `beta_W<1/6`, from Cao–Nissim–Sheffield’s slab curvature method for Wilson area-law decay. For a global infinite-volume pure Wilson measure LSI/Poincaré/mass gap, the largest such range located is SZZ’s `beta_W<1/12`.
- **Order-one coupling:** neither range reaches beta of order one. Adhikari–Cao’s result does reach the weak-coupling side but for finite groups and a different action class; Chatterjee’s statement is conditional and supplies no coupling range.
- **Boundary of search:** I searched arXiv and journal records around the named works and the available primary statements. “Largest found” is a scoped literature-search outcome, not a theorem that no unlocated publication exists. The numerical range `sqrt(2/27)` in the public computo ergo sum chapter “One-link integration before Bakry–Émery” is not included in this published/arXiv maximum: I found it as an online research chapter, not a journal or arXiv paper, and its separate mass-gap step is described there as a sketch.

## Sussman–Alpoge outline cross-check

I used `library/sa-index/README.md`, chunk 02, and the obligations list. The relevant neighboring index entries locate the periodic Wilson-state/link-reflection argument at outline lines 2084–2194 and the one-bond convolution at 2195–2245. Those are transfer/reflection statements; the index contains no Bakry–Émery, Langevin, or linkwise heat-log-gradient estimate for the curvature target. I read outline lines 2084–2245: they set the Wilson `SU(2)` convention `a_p=1-(1/2)tr U_p`, prove a periodic-state link-reflection result, and compute positive one-bond convolution eigenvalues. This is useful for normalization and credited transfer context, but it does not prove NG or supply a Langevin gap. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of that outline.
