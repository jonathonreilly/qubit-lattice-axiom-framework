Provenance: Claude Opus 5.5, the target lead, reading a proof written by OpenAI GPT-6 Astra at max effort. Different provider from the author. The lead wrote the prompt, so this read isn't independent of the framing. Not an audit, grants no status, no run used. This report is about the independent attempt: the mapped side does not read it.

| Statement in `library/shelling-by-hand.md` | Verdict |
|---|---|
| Product rule | ADVANCE |
| Theorem: a union of parts of a distinct-coordinate guillotine partition is an initial segment of a shelling of the whole cube (four blocks) | ADVANCE |
| Subcube restriction | ADVANCE |
| Counterexample to the part's vertex-only reading, which is not library-good | ADVANCE |
| Lemma 7G, Lemma 8G | CORRECT-NO-ADVANCE: only the combinatorial step is new, and the analytic steps weren't read |
| Consumer table, with (AB) named as a gap at Lemma 4.5h | CORRECT-NO-ADVANCE: read, not traced into the consumers |

Rechecked by hand: all four rows of the i-direction table; that A and B stay initial under flips, which is where disjoint X and Y and the extension to a full-cube order are used; that facet orders are the full product orders despite interleaving; the first-vertex case of facet one; and the corner argument in the counterexample.

Defects:
1. The original claim, that every library-good pattern has a shelling, has no hand proof and no counterexample. Lemma 7's scope has to narrow to generated patterns, or that claim has to be proved.
2. (AB) is a real new obligation: the adapted domains 2B of Lemma 4.5h are not shown to be generated. The machine exhaustion had hidden this.
3. Text 3.2's (T3), (T4) and the tiling's existence are hypotheses here, not checked.
