# Posted notes, GitHub-rendering copies

Each file here is the note exactly as linked from our issue on ethanwsussman/Yang--Mills-LLM-experiment, with the math delimiters rewritten so GitHub renders them: inline math as $`…`$, display math as ```math fences outside lists, and as one in-place $`…`$ inside a list item (\tag{n} written as \qquad(n)); inside table-row math, | is written \vert. Three notes also carry one small repair, disclosed in their issue's edit note:

- out-l17.md: the two internal header lines and the words "Draft, not yet sent." are removed.
- out-lrb.md: one subscript damaged when the note was generated is restored to `{\rm meeting}` (the `\r` had become a line break).
- out-pda.md: one sentence now names the two endpoint indices it compares, k-1 and s.

No other word or formula is changed. The originals stay at the commits the issues first linked:

| File | Issue | Original commit |
|---|---|---|
| out-mu.md | #10 | 877743789 |
| out-um.md | #11 | 0fc778a74 |
| out-l17.md | #12 | 877743789 |
| out-pi.md | #13 | 94df5579a |
| out-gw.md | #14 | 9a3ad2072 |
| out-lrb.md | #15 | 77b182ef7 |
| out-lsc.md | #16 | 470a2a414 |
| out-pda.md | #17 | 39ab806ac |
| out-gw1.md | #19 | 7198d9fa2 |
| out-m3.md | #20 | 43942f5fe |
| out-tpi.md | #21 | 464eed258 |
| out-live.md | #22 | 32de21a18 |

Converted 2026-11-08. Each copy was rendered through GitHub's markdown API: every formula renders, none is raw or in a code block, and every formula sits in the same kind of container (list item, table cell or block) as in GitHub's render of the original. Each copy was diffed against its original: identical apart from the delimiters and the three repairs above. Two independent readers (Codex gpt-6-luna and gpt-6.1-sol) checked every pair.
