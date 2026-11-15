lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T13:18Z

# gap-iloc-opus: (I-loc) for Q, Q', a and (ID-a) torus-freeness of z^(k)(c) and measure constants

FINISH row 990, pinned commit cb6378648. Inputs of row 987 named by row 989.
Marks: PROVED, ARGUED, OPEN. Research-stage working state; no status claimed.

## Plan (at most eight steps)

1. Read FINISH rows 987-990, the efficiency rules and "Build on published work"; read `library/gap-det-fable.md` Lemma P and the statement of (I-loc), (ID-a) there or in row 987's output.
2. Grep `library/open-core.md` and FINISH rows for (I-loc) / (ID-a) overlap.
3. Locate the definitions of the averages Q, Q' and weights a in the repository's step form (pr-lay, hma) and in the account (CA-I/II/III index); quote file:line.
4. Prove or refute (I-loc) for Q (finite-range stencil, commutes with lattice translations) and its periodization compatibility with Lemma P.
5. Same for Q' and the weights a; write the combined statement.
6. (ID-a): read CA-I transcription of Balaban CMP 119 (3.33) and outline (1c.1); decide torus-freeness of z^(k)(c) and measure constants at U = 1; mark what needs CMP 119 itself.
7. Final verdict table and RESULT line.

## Step log

(steps appended below as done)

### Steps 1-2. Inputs read, overlap check (01:25Z)

- Read: FINISH rows 985-990, item 2 of the rules ("Build on published work"), `library/gap-det-fable.md` L220-250 (Lemma P) and L380-420 ((S1), (S3)), `library/gap-det-check-opus.md` (row 989) in the parts on (I-loc) and (ID).
- **(I-loc) as needed by row 987 (S1).** Each primitive of pr-lay (6)-(7) at P_0 on the torus T_n is, for every n large against the stencil, the periodization of one rule on the infinite lattice, i.e. it satisfies R_{n'} pi^* = pi^* R_n for n | n' (Lemma P (i)); and the choices (pivots, gauge fixing, tops) on T_n' are the pull-back of those on T_n. Row 989 confirmed pivots (SA L8167-8169), blocks (SA L7946-7954) and the soft gauge (SA L7180-7182); it left Q, Q' and the weights a unread. Those three are this row's item (1).
- **(ID-a) as stated by row 989 (L154, L200):** at U = 1, every z^(k)(c) of CMP 119 (3.33) and every per-cell constant of its measure is one number per cell, the same on every torus for a common coupling sequence.
- **Overlap check.** `grep -n "I-loc\|ID-a"` over `library/open-core.md` and `FINISH.md`: no hit in open-core.md; in FINISH only rows 987, 989 (which name them as open) and this row 990. No other row covers them. Proceeding.
- **Source.** Sussman and Alpoge's repository (with Claude and Codex as authors of their text), https://github.com/ethanwsussman/Yang--Mills-LLM-experiment, shallow-cloned into my scratch `/tmp/gapiloc990/sa`, HEAD c7fef8b (same as rows 986-989), not committed. `YM4/YM4_sketch_500.tex` has SHA-256 d7f77d4d...4b6f, the outline hash of `library/mu.md` L17, so SA line numbers below are those of the outline at 31a47c543775. `~/ym4d-papers` holds cmp96, 98, 99a, 99b, 102, 122a, 122b only (no CMP 109, 116, 119).
