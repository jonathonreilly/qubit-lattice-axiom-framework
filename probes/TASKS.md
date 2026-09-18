# Task catalog (human view; the machine view is TASKS.json)

Generated (tier 0/1): `R:<runner>` re-execution and `M:<runner>` mutation census for every runner in `scripts/` (about 3300 runners, of which the ones with a mutation gate get an `M:` task), and `F:<refuter>` for every `*refuter*.py` control under `.claude/science/**/specs/`.

Hand-written (see `probes/tasks/*.json` for the exact commands, hit patterns and parsers):

| id | tier | what a HIT means | sweep |
|---|---|---|---|
| `S:tight-sibling-violation` | 1 | a site whose cheapest family tree costs > 0 at `c = 1`: refutes `c* = 1` (block 32) | seeds, boxes `5x5x8`–`8x8x10`, 20–120 min |
| `S:tight-sibling-pairs` | 1 | two tight sibling predecessors: the open case of block 33's lemma | seeds, boxes |
| `S:structural-duplication` | 1 | as above by duplication moves | seeds, boxes |
| `S:family-constant-climb` | 1 | `c* > 1` | seeds, boxes up to `7x7x10` |
| `S:restricted-admissibility` | 1 | a realization where the one-processed-child restriction is not admissible at `c = 2`: kills block 33's `2921` route | seeds, boxes |
| `X:sixaxis-formation-threshold` | 1 | none (a table): the located strength on `(p,1,2)` and other lines | `--extra` p values; sizes |
| `X:sixaxis-static-threshold`, `X:sphere-static-threshold` | 1 | none (tables) | sizes |
| `X:sphere-torus-memory` | 1 | none: `D_1/(σ²/L²)` versus `1/|m|²` as a table in `(β, L)` | `--extra 'beta L T seeds'` |
| `X:sphere-kernel` | 1 | none: `c(β)` by wavevector shell; cross-level ratios | `--extra 'beta L T T0 seed'` |
| `X:sphere-plane-decay` | 1 | a plateau of `|m|` on a large plane would contradict block 26's executed conclusion | `--extra 'beta L T'` |
| `J:falsifier-implementation` | 2 | a falsifier of any note that fires | any note with a Falsifiers section |
| `J:refuting-reimplementation` | 2 | a disagreement with a note's central number | any note |
