**Title:** Bare-density normalization in 4.33(h4)(a), and a conditional completion of the Chapter 6 last-scale lemma

Ethan and Levent,

Your Chapter 1 bare density is incompatible with the vacuum-energy substitution in 4.33(h4)(a). Definition 1.1 starts with $e^{-x_0A}$ ([CA-I 477–481](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L477-L481)); Definition 1.5 retains it ([924–933](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L924-L933)). But [(h4)(a), 157039–157041](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L157039-L157041) uses the vacuum energy initialized at [159153–159160](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L159153-L159160). The bare identity needs the extra term: $-E_k^{\rm bare}=E_{\rm vac}+\mathfrak l_k-\mathfrak r_k$.

[This note](@LINK@) repairs the application using your existing convention $\widehat Z=e^{-E_{\rm vac}}Z_{\rm bare}$, explicit at [CA-II 140916–140926](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L140916-L140926). The bare floor retains $e^{E_{\rm vac}}$. The lower-bound argument itself remains valid in the corrected convention.

The note then reconstructs `6.3:lem-last-scale-constants`, whose statement is unwritten at [CA-II 63365–63367](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L63365-L63367). At fixed $g$ and $m_J(g)$, it gives the bounded stopping-index offset, matched lattices, separately uniform normalized upper and lower exponents, finite rescaling maximum, local small-cutoff bound, and fixed-offset subsequence.

Your printed proofs already give (b)–(e) and the floor mechanism. The additions are the offset argument, explicit common-window constants, normalization reconciliation, and completion under the original torus floor. The claimed application covers the checked Chapter 6 consumers and clause (iii-b)'s original floor, at their retained inputs' standing. Balaban's real-background, representation and majorant inputs remain explicit assumptions.

**Not covered.** The upstream construction or preparatory window-data statement. Cross-torus vacuum-density comparisons or every later use. An unconditional stability or main-theorem result, factorial growth, clustering, or rotation invariance.

Codex wrote the working proof and the separate normalization check; its exact model variant was not recorded. A fresh Claude session rejected the first bare-mass application. A fresh Claude session checked the repaired changes line by line, retaining the accepted first-round parts: “First failing step: none.” Codex wrote this outward version; it has no separate independent check. These are conditional model checks, not human review or an audit, and grant no scientific status.

This is a proposed correction and proof for your review.
