lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T14:14Z

# uses-ui-oc: do library/ui.md and library/oc.md cover the uses listed in library/uses-old.md §§1–2?

Queue row 370. Commit 61ff5f275. Claude Opus 5.5, max effort, Mac mini worker, fresh session. One reading, not an audit. Checked line by line by Claude (Mini worker).

Moves: the two old-input rows of `library/uses-old.md` (CA-I `4.5:lem-uniform-increment`, `4.13:lem-own-constant`). If every use is covered, both inputs can be cited at their use sites with no new lane. A use that is not covered names the weakest statement still owed.

Kind of result (FINISH item 9): a check of our ports against their consumers in the account. No new proof. The source is CA-I at `31a47c543775`, fetched by URL into a scratch folder; SHA-256 `4cb5cb5e…6e93`, the same as in `oc.md`.

Credit: the lemmas, their uses and the proof mechanisms are from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; the underlying constructions are Tadeusz Balaban's. `ui.md` and `oc.md` are Codex's ports, each checked once by Claude (`gates/ui-gate.md`, `gates/oc-gate.md`).

## Method

For each row of `uses-old.md` §1 and §2, I read the CA-I lines it cites. I wrote down what the use reads: the radius, the domain and tower, the cube letter, and the constants with their place in the order of choice. Then I compared that with the Result of `ui.md` or `oc.md`. Verdicts: **covered**, **covered after a stated ceiling**, or **not covered** (with the reason and the weakest statement the use needs). I did not re-check the internal proofs of `ui.md` and `oc.md`; the gates did that. Where a use reads a part of the lemma that our note cites rather than proves, I say so and read that part here.

(Sections 1 and 2 follow as they are finished.)
