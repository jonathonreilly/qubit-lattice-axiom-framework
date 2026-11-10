**Title:** Your scale comparison over one window (lines 73382-73383), your index $`k_0`$ (lines 63775-63778), and the cells of your action sequence

Ethan and Levent,

This concerns `YM4/YM4_1400.tex` at commit `c7fef8b21b58` ([the file](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/c7fef8b21b58/YM4/YM4_1400.tex)). Three statements of yours are treated. At lines 73382-73383 your text uses "the scale comparison $`\check R_{h_t}\le L\check R_t`$" between levels that are $`\mathsf N_t=\check R_t`$ apart. At lines 63775-63777 it takes an index $`k_0`$ with $`h<k_0\le k-2`$. Lines 1475-1477 provide $`\mathsf s_j=M`$ for a $`\Lambda_j`$ that is not a union of cells. No proof of the first two is given at those lines. The ratios your text states elsewhere (line 1110, lines 73081-73082, and `rt:eq-adjacent-cell` in `YM4/RT/YM4_RT.tex`) are of one step.

[This note](LINK-TO-NOTE) gives these results, in three parts.

- Example F: a frame that meets your definition at lines 1102-1113 and has $`\check R_{h_{14}}=L^2\check R_{14}`$, for $`r=2`$, $`L=13`$, $`0\le\underline\lambda\le12`$, $`c_5\ge0`$, $`e^{-1}\le\gamma<e^{-1/2}`$ and $`\bar B\ge e^{14}`$.
- Corollary S: your comparison holds under one added ceiling (G) on $`\gamma`$. (G) depends only on $`r,L,c_5,\bar B`$, so it fits your order of constants (lines 72930-72931, 72946).
- Lemma K: assume the frame, (G), $`L\ge4`$ and $`h=k-\check R_k\ge0`$. Then your index $`k_0`$ exists, with the range and the two side inequalities stated at lines 63775-63778.
- Lemma C: every region $`\Omega^{\mathsf a}_l`$, $`\Lambda^{\mathsf a}_l`$ of your action sequence is a union of cells of its own level. With the note's reading (K) and with "those cubes" read as level-$`j`$ cells, the first case of lines 1475-1477 always applies to it.

The note takes these from your text as stated: the frame definition (lines 1102-1113, 1121), your rules for steps, fates, marks and the action sequence (lines 61973-61985, 62080, 62105-62128, 62174-62177, 73081-73092), and one reading of "component".

It does not show whether the ceiling behind "$`\gamma`$ is small" at line 62001 is meant to cover one window.

Provenance: Claude Opus 5.5 wrote Lemmas G, W and C with their corollaries, and Claude Fable 5.2 checked them line by line. Claude Fable 5.2 wrote Example F and Lemma K, and Claude Opus 5.5 checked them line by line. Claude Opus 5.5 added the last sentence of Lemma K and its proof during that check; Codex (gpt-6-astra) then checked that addition line by line and found no failing step. Not an audit.
