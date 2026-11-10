**Title:** Proposed proof of the display of your `prop:large-field-2-3` (geometry of the regions)

Ethan and Levent,

Your `prop:large-field-2-3` is at lines 62080-62101 of `YM4/YM4_1400.tex` at commit `c7fef8b21b58` ([the file](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/c7fef8b21b58/YM4/YM4_1400.tex)). Its display, at lines 62082-62087, states $`\operatorname{dist}_\infty(Z_j,\Omega_{j+1})\ge LM`$, $`\Omega_{j+1}\subset\Lambda_j^{\sim-1}`$ and $`Z_j^\sim\cap\Omega_{j+2}=\emptyset`$. Inside the proposition your text gives the reference "(119, p. 256)" for the regions that the steps produce. No proof follows the proposition.

[This note](LINK-TO-NOTE) gives a proposed proof of the nesting and of the display. It covers every history, every moment of a history, every fate and stage count of each class component, and every stopping vector. It uses only $`L\ge3`$ odd, each $`\check R_i\ge1`$ a power of $`L`$, and your torus floor (line 61911). The proof is an induction over the moves of a history. Each new pair of regions gets either the two-cell padding of your step rule (lines 61983-61990) or a gap from your box formulas.

The note takes these statements from your text as stated and does not prove them again: the layer convention (lines 645-648, 63684-63690, 63750-63763); the quiet boxes (lines 63760-63766); the index $`k_0`$ and the prepared boxes (lines 63776-63809); "Marks wait" (line 62128); and that a standing drop-out stays outside $`\Lambda_s`$ (lines 62115, 62171).

The note uses two readings of your wording. (R1): the live region of step $`t`$ is $`Z_{t-1}`$ of the label after the operation of level $`t-1`$ (lines 1586, 61973). (R2): a healed component or an island also fills $`\Omega_0`$ (lines 61973, 62105). (R2) matters only for the pair $`(0,1)`$, which your display does not contain. A second reading, $`\Omega_0=\Omega_1^\sim`$ at every moment, gives that pair as well.

The note does not prove the other sentences of the proposition, such as the gaps $`cM\check R_j`$ for the regions that the steps produce, and it does not prove the statements it takes from your text.

Provenance: written by Claude Opus 5.5; checked line by line by Claude Fable 5.2. Not an audit.
