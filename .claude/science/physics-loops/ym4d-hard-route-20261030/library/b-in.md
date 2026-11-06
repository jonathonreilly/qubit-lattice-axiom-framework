lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T02:47Z

# (B-in): the sealing construction on D_2 beside S

Queue row 389 (`b-in`). Started 2026-11-06T14:47Z at commit cf6677779. Proved by Claude, not yet checked by the other model. Work in progress; sections are added as they are written.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account CA-I, CA-II, CA-III and outline at upstream `31a47c543775`), for every statement, construction and bound cited with a line number; Tadeusz Balaban for the multiscale construction (CMP 89-122). Earlier lanes here: `library/ca-claude.md` (Lemmas A, B), `gates/ca-gate.md` sections 4-5, `library/prior/b-in.md`.

## 1. Scope, duplicate check, sources

- **Item.** FINISH row 389. Moves: (B-in), named input 1 of CA (`library/ca-claude.md` Result), the first place CA can fail. CA is open-core item CA (`library/open-core.md`, owner `ca-claude`); (B-in) is its input, not CA itself.
- **Duplicate check (rule 0a).** `grep` of `library/open-core.md`, `library/l17c.md` and `library/open-registry.md` for "B-in", "sealing", "own-level": no row attacks (B-in) or the sealing construction. FINISH rows naming it: 382 (check, found no supplier), 383 and 387 (digests), 386 (ca-f, lists it as open), 389 (this row). No other lane attacks it.
- **Account label and status.** (B-in) is clause (b) of `4.27:prf-room-dissolving` (CA-I 138348, index PROVED), whose proof (I:138438-138450) cites "the own-level bound for the configuration U_2 of the sealing construction". The account states no such construction. The second consumer is the core step of `4.27:prf-ambient-inclusion` (I:136490, index INCOMPLETE), I:136718-136760.
- **Sources.** CA-I, CA-II, CA-III fetched by URL into a scratch folder of this lane; SHA-256 agree with `library/arr.md` section 1. Line numbers are of those raw files. CMP 122a/b are not in `~/ym4d-papers`; they are used only as the account quotes them. CMP 98, 99b, 102, 109, 119 are local.
- **Rules.** No numerical run. No computer-assisted step.
