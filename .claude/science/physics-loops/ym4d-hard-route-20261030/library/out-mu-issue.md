**Title:** Proposed proof of your constrained-minimizer lemma (CA-I §4.13)

Ethan and Levent,

Your [constrained-minimizer lemma](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45162-L45201), `4.13:lem-minimizer-unique`, is marked "Proof outstanding." [This note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/877743789c269744f7500a62087d21e545df72b1/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-mu.md) gives a proposed proof of its uniqueness claim and of (3.38).

Scope: $Z\subset X\subset\tilde\square^2$, both tower rules, and $1\le n\le p\le j$, under the amplitude ceilings stated in the note.

The proof uses your real refinement lemma `9.3:lem-refinement`. It also uses Tadeusz Balaban's CMP 98 Propositions 2, 4 and 6, and CMP 102b Theorem 1 and Proposition 9, including (172)–(173) and (181). It does not re-prove these inputs.

Uniqueness is proved in the real regular space. For complex data, the note uses the analytic continuation of the real minimizer. It does not claim that all complex critical points are unique.

The note does not cover the later nesting domains, the later composite radii, boxes without sequence domination, unbounded complex boxes, or the uses in CA-III §9.1.

Codex wrote the working proof, and a separate Claude session checked it line by line. That check found no failing step. Codex wrote this outward version, and Claude read it against the working proof and your cited lines.

We hope its admission and restriction arguments help you complete the lemma. This is a proposed proof for your review. It does not claim that the full account is complete.
