# The tight-sibling lemma, exhaustively on small cones — run 1

Worker `w-jonathonsmac4f50-j0268`, model `claude-opus-5-5`. Blocks 32–33 were written in this campaign by the same model family (Claude). The log is `logs/probes/C:tight-sibling-exhaustive:a1/w-jonathonsmac4f50-j0268__1c9f948f__20260925T060828Z.*`.

## Method

- **Automaton.** The two-level majority automaton in level time (`probes/lib/family.py`) runs on the cone below the root (4,4,4). Sites outside the cone are 0.
- **Rooted value.** `v(z)` is the minimum over the counted family's trees containing z, at levels ≤ level(z), of `E − 3(|S| − 1) − |A|` (c = 1).
  - A site's kind depends only on its predecessors, so `v(z)` depends only on the configuration at levels ≤ level(z).
  - It is computed **exactly** by `family.brute_min` on that restriction (Fractions), and cached on the translated configuration.
- **Cross-check.** 209 processed sites of random depth-3 configurations (3–7 marks) agree with `rooted.py`'s integer program.
- **Enumeration.** Every mark configuration is enumerated. The cone's axis-permutation symmetry reduces them to orbits, and the orbit sizes are weighted back.

## Results

| cone | configurations (orbits) | processed 1-sites | v over processed sites | processed sites with v = 0 | sites with every 1-predecessor processed and tight | largest v allowing tight seeds as predecessors (count) |
|---|---|---|---|---|---|---|
| depth 3 (20 sites), ≤ 6 marks | 60460 (10571) | 164320 | −14 … −1 | **0** | **0** | −2 (71665) |
| depth 4 (35 sites), ≤ 5 marks | 384168 (65470) | 496585 | −11 … −1 | **0** | **0** | −2 (267860) |

The full distributions of v are in the log. At depth 3 the most frequent values are −5 (24982) and −6 (24745); at depth 4 they are −2 (125481) and −5 (94811).

## Reading

- On these cones **no processed site is tight**: every processed site has `v ≤ −1`. So the lemma's hypothesis, a processed site whose 1-predecessors are all processed and tight, never occurs. The lemma holds vacuously here.
- If tight **seeds** (v = 0) may count among the predecessors, the hypothesis occurs often, and the conclusion holds with margin: largest v = −2.
- No counterexample exists within these bounds.
- This agrees with the other worker's derivation unit on the lemma's vacuity (J:derive tight-sibling-vacuity, untriaged at the time of this run). Its reported counterexample uses ten marks, beyond these bounds.

## Verdict

There is no HIT: `v ≤ 0` everywhere the hypothesis applies. The hypothesis never applies with processed predecessors at depth 3 with ≤ 6 marks, or at depth 4 with ≤ 5 marks.
