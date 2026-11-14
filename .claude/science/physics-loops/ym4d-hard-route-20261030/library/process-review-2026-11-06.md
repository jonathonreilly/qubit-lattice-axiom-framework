# Process review, 2026-11-06

Owner, 2026-11-06: "we are not even checking our own work for existing solutions? How is this efficient. review everything in our process again and optimize it."

## What went wrong on 2026-11-05

1. **No prior-work search before proof lanes.** Lanes started proving at once. Afterwards: their 4.5 and own-constant "open" labels were already proved in their own text (library/ui.md, oc.md); our ST1 was a different theorem from the stage theorem (library/stage.md); CMP 119 re-attacked the lemma two other lanes held (library/b119.md); the pointed-irrelevance port did not fit our statements (library/port-pi.md).
2. **Consumers checked last.** Use searches and consumer checks ran after the proofs (library/mu-radii.md, uses-*.md, l17c.md). L17 closed only once we asked what its consumers need.
3. **No single registry of open statements.** open-core.md, ours-vs-core.md, t0-tree.md and FINISH each list open items differently; the lead deduplicated from memory.
4. **Expensive models did bulk reading.** Astra proof lanes read 4-10M input tokens each, much of it source reading; both laptop Codex accounts ran out in a day.
5. **Brittle launches.** Wrong output paths, repo2/repo2b confusion, a missing login shell on the Mini, overlapping watchers.

## New method (binding; FINISH rules 0b-0e)

- **0b. Prior work first.** Before any proof, port or rebuild lane, a gpt-6.1-sol lane writes `library/prior/<name>.md`: every place in OUR repository (library/, gates/, port/, FINISH rows) and in THEIR account (CA-I/II/III and outline) that states, proves, partly proves, or uses the target, with file:line and one line each; and whether their own text completes a step marked incomplete. The proof lane reads that digest first and attacks only what is not already covered. Cost: a few hundred thousand cheap tokens instead of a wasted astra or Claude round.
- **0c. Consumers first.** For every open statement, the same sol lane lists its consumers; the proof lane's first task is the weakest statement all consumers accept (the l17c.md pattern), then prove that.
- **0d. One registry.** `library/open-registry.md` lists every open statement on the T0 chain: name, exact location, owner lane (one), status, files. The lead updates it at every dispatch and result; a statement with an owner is not given a second lane.
- **0e. One launcher, cheap reading.** `scratchpad/codex/launch.sh` is the only way to start a Codex lane: it takes machine and slot, model (default gpt-6-astra; gpt-6.1-sol for reading), effort, prompt and output path, sets the login shell and repo correctly, checks the first events, and writes the registry line. Heavy lanes get line ranges and digests, never "read the account". One laptop Codex lane at a time; xhigh default; max only for hard proofs.

## What stays

Codex writes, Claude referees (cross-provider). A claim counts only after its referee. Port, never redo, their proved steps. Nothing goes outward without the owner's approval of the exact text.
