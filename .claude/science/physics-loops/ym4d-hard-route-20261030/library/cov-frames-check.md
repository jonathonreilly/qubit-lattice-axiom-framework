lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T00:28Z

# cov-frames-check: line-by-line check of `library/cov-frames.md` (FINISH row 646)

Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, branch `claude/ym4d-hard-route` at 3591d5adc, 2026-11-10. A check by a second Claude model of a file written by Claude Fable 5.2 (medium); same provider, so not a cross-provider check. Not an audit. Source Y = `YM4_1400.tex` of the Sussman-Alpoge experiment repository (ethanwsussman/Yang--Mills-LLM-experiment at 2bc0658f91d2), credited to Sussman and Alpoge with Claude and Codex as authors of its text.

Verdict: (in progress; written at the end)

## Repo search

- `grep -n "cov-frames-check\|late-stop-tg\|(TG)" library/open-core.md FINISH.md`: the only rows are 646 (this one) and 647 (`late-stop-tg`, which owns (TG)). I do not attack (TG) here. Rows 633, 636, 637, 638, 639 are the checks and the reading named in the row; I do not redo `cov-global` or `cov-xstar`.
- `library/cov-global-check.md` item (6) already noted the "an end" / "both ends" ambiguity and said the proofs of `cov-global` hold under either reading if (F-main) and (R-core) use the same set; `library/cov-xstar-check.md` R5 is conditional on change (1) of `cov-frames`. Both are used below.
- Sussman-Alpoge text: Y = `/tmp/ym4_1400.tex` (136,637 lines, as the row names it). Every Y quotation below was compared with that file in this session.

## Item (2). The set `B` of the main step: HOLDS

What Y says at each place (read in this session):

| Place | Words | Reading |
|---|---|---|
| Y 71488 (Proposition 'minimiser in a box') | "the map `V_k restricted to Lambda^pr -> A(U_{k,X}(V_k))`, which is a function of `V_k` on the level-`k` bonds having an end point in `Lambda^pr`" | **an end** |
| Y 75680-75683 (first chart of a late stop) | "Central integration has consumed the old box field, including the bonds crossing its boundary. The resulting term has unrestricted fresh Haar coordinates on the bonds with an end in the box." | **an end**; the file quotes it word for word |
| Y 75700-75704 | "A first outgoing row of level `i+1` that reads the box has at least one of its two blocks there, so its middle fine bond has an end in the box. It is one of the free Haar coordinates, even for a row crossing the box face." | **an end** |
| Y 96361 (stage `R` of the other part) | "`b_X` the set of bonds of `T^{(j+1)}` that have an end point in that box. The moves of `R` alter `V_{j+1}` on the bonds of the sets `b_X` and nowhere else ... Each bond of `b_X` has both end points in X." | **an end** (an extra source the file does not cite; it supports change (1)) |
| Y 63836 (3), Y 63856 | "`V_k` is integrated over `Lambda^pr`"; "independent of `V_k` on the box"; "`dV_k restricted to Lambda^pr`"; the cutoff "on the bonds of the box" | **neither**: no rule for the crossing bonds |

I searched Y 63700-63900 for "both end", "an end", "end point", "endpoint": there is no "both ends" there. The registry note "Y 63836 says 'both ends'" (row COV, 2026-11-10, after the three checks) is not supported by the text: Y 63836 is silent, and the only explicit rules in Y (71488, 75680-75683, 75700-75704, 96361) all say "an end". Repair for the registry (for the lead): "Y 63836 does not say which bonds; Y 71488, 75680-75683, 75700-75704, 96361 say 'an end'."

Do the statements of the file hold for each reading?

- *An end* (the file's choice). Lemma 4.4 (b), (c) and the fresh set `B*(X)` are right: a plaquette with a corner `x in Lambda^pr` has its two edges at `x` in `B_main`; a plaquette with no corner in `Lambda^pr` has no edge in `B_main`. `B*(X) minus B(X)` is the set of level-t plaquettes with exactly one corner in `Lambda^pr`: `Lambda^pr` is a product of integer intervals in level-t units, so two adjacent corners in it span an edge with both ends in it, and two diagonal corners `x, x + e_a + e_b` in it force `x + e_a, x + e_b` in it. Checked.
- *Both ends.* Then the move writes fewer bonds, the weak frame statement with `B(X)` holds, and it implies the one with `B*(X)` (a larger `B` gives a weaker statement: Definition 2.0 only asks for conjugacy off `B`). The certificates of Lemmas 5.2, 5.4 are given for every plaquette of `B*(X)`, so Theorem 5.1 holds with either fresh set. Monotone, as the file says.
- One coupling the file states (Remark 5.5 (iii)) and I confirm: the reading of `B_main` and of (M-cut) must be the same set. Y 71450-71453 ("For each non-tree bond, close it by the tree path ... `abs(log(V_k V_Lambda^{-1})(b)) <= C(M) eps_k < M_0 eps_k`") and Y 72682-72686 ("The cutoff in the subsequent draw restricts `V'_m = V_m V_Lambda^{-1}` to its reference ball. Its complement carries zero mass") put the cutoff on every bond of the reference law, which is the integrated set `dV' restricted to Lambda^pr` (Y 63856). With Y 75680-75683 this set contains the crossing bonds.

Verdict on item (2): HOLDS. Change (1) of the file agrees with every explicit statement of Y.

