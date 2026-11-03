lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T15:20Z

# h-walk: the walk expansion of chi_Y A chi_Y (outline statement 5, (1c.8)-(1c.9))

Queue row 115. Pinned at branch claude/ym4d-hard-route, commit c90e340cc. Same-model, ungated, research-stage working state. Written section by section.

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max as configured for this worker (Mac mini); repository commit c90e340cc; Sussman–Alpoge outline `YM4_sketch_500.tex` at commit `31a47c543775`, fetched by URL into a scratch folder (SHA-256 d7f77d4d…b6f, as recorded in `sa-2.8.md`) and not committed; SA nnnn below are its line numbers. Balaban CMP 95, 96, 99 (389-434) read from `~/ym4d-papers/` (OCR, outside git). Research text by one model, not an audit and not a gate; it grants no status. No step rests on a computation. No numerical job was run, so the numeric lock was not needed. No subagent.

**Credit.** The statement (statement 5, SA 10302-10340), the operators (SA 10142-10208), the walk vocabulary (SA 10210), the unfolding with auxiliary unknowns (mechanism (f), SA 10540), the tree treatment of H^T J (mechanism (g), SA 10548), the multiplier (mechanism (h), SA 10550) and the consumer (SA 14108-14196) are Ethan Sussman and Levent Alpoge's outline, with Claude and Codex as authors of their text. Tadeusz Balaban supplies the method: generalized random-walk expansions from local inverses built on **cut-down sequences** around each cube (CMP 99b pp. 408-410, (3.87)-(3.94), Theorem 3.7, Corollary 3.8), the summation lemma (CMP 96 Lemma 2.1, (2.50)-(2.66)) and the walk-relative distance (CMP 99b (3.93)); CMP 95 Proposition 1.2 is the one-region prototype. The global operator bounds used as inputs are Claude's `a2-layers.md` §7 with Codex's repairs in `gates/a2-layers-gate.md`, resting on Codex's `a2-curved.md` §8 as gated in `gates/a2-curved-gate.md`. The parametrix lemma template is `path_expansion_locality.md` Lemma 1 (Claude, after Dimock arXiv:1108.1335 §2.4). The local saddle system and its commutator estimates are Codex's `flat-port.md` §§8-11, gated in `gates/flat-port-gate.md`.

## 0. Disposition (provisional; final in §10)

In progress.
