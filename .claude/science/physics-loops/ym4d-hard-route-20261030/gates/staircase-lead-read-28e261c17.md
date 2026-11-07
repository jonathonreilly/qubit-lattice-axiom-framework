Provenance: Claude Opus 5.5, the target lead, reading a proof written by OpenAI GPT-6 Astra at max effort. Different provider from the author. The lead wrote the prompt, so this read isn't independent of the framing. Not an audit, grants no status, no run used.

| Statement in `library/staircase-by-hand.md` | Verdict |
|---|---|
| O1 is still consumed (section 1) | CORRECT-NO-ADVANCE: the lead followed the cited lines only through the note's own trace |
| G1, G2: no pinch at any prefix or seam | ADVANCE |
| (R), (R0), (R1): integer reflection, paths of length at most 7, energy bound | ADVANCE |
| (E-s), (E-cov), (EXT), (E-D0) | CORRECT-NO-ADVANCE: read at the level of steps, and the constant counts were not rechecked |
| (BG) from the class reference and (small) | ADVANCE, as an implication |

Rechecked by hand: the graph description t <= h(y) in (G); that R is an involution with q -> 1 - q; the unit changes of q across a bond, including j = d; the a(q) steps, giving the length bound 7; the use of the down-set property to keep paths in D; and the reorientation at a seam.

Defects: none that break a step. O1 stays conditional on F-D's other estimates, the fine lifting, HS-P, HS-T and the gas bounds, as the note says. (small) has to be added to the mapped order of constants at the choice of a_*.
