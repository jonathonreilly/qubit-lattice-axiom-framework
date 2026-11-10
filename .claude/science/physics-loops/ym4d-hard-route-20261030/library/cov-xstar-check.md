lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T17:18Z

# Check of `library/cov-xstar.md` (row 639)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, commit 0cd1bd5ea. This is one line-by-line
read by a model that did not write the file (it was written by Claude Fable 5.2 medium). It is not an audit.
Source: Sussman and Alpoge, `YM4_1400.tex` at 2bc0658f91d2 (their text names Claude and Codex as authors),
fetched into my own scratch folder; `Y n` is line n. No numeric job was run.

## Verdict

**(COV-X\*) HOLDS, with repairs to the wording only, given the read inputs (D1) to (D6), (D3\*) and (AV2).**
First failing step: none. No item FAILS. Lemma 3.1, Lemmas 4.0, 4.1, 4.2, 5.1, Theorems 6.1, 6.2 and the
table (X6) are correct as implications. Findings 1 to 5 of the file are confirmed. Five repairs (R1 to R5)
are given as text below; none changes a statement, a constant or a moment.

| Item | Verdict |
|---|---|
| (1) Lemma 3.1, edge cases | HOLDS |
| (2) Finding 1 | HOLDS WITH REPAIR (R1, wording: "astride", not "meet") |
| (3) Lemma 4.0 | HOLDS |
| (4) Lemma 4.1 at `l = t` | HOLDS |
| (5) Lemma 4.2, thresholds, factor 3 | HOLDS |
| (6) Lemma 5.1 | HOLDS WITH REPAIR (R2: the source of 2.1). The factor `L^2` at `i = t - 1` is needed in the worst case |
| (7) Theorem 6.1 | HOLDS WITH REPAIR (R3: name (LF), or the 5.3 constant). (Q3) is outside (5.1), as the file says |
| (8) Theorem 6.2, table (X6) | HOLDS |
| (9) The last stage against Y | HOLDS. Y states the one-step average on the new rows at the last stage |
| (10) Quoted Y passages | HOLDS (thirteen compared; all are faithful; line offsets of at most 1) |
| (11) Carrying after `nu_t` | HOLDS WITH REPAIR (R4, R5): the weak form is enough; the main-step clause should follow row 638 |

## Repo search

`grep -n -i "cov-xstar\|COV-X\*"` in `library/open-core.md` and `library/open-registry.md`: only registry
row COV. FINISH rows 633, 635, 636, 638 are near this check. None of them checks `cov-xstar.md`. This
checkout has only `origin/claude/ym4d-hard-route`. Present at this commit: `cov-x-check.md` (row 633;
RESULT: (D1) to (D6) are fair readings of Y), `cov-global-check.md` (row 636) and `cov-frames.md` (row 638).
I do not check those files; I name them where they touch an item.

## Items

### (1) Lemma 3.1: HOLDS

What I checked, for general `i` and at each edge case.

- `F(p) subset O_{i+1}`: `O_{i+1} = H_{i+1}^{[8 a_{i+1}]}` is a union of level-(i+1) cells, so it is a union of
  aligned level-(i+1) blocks. Lemma G (b) of `cov-x` applies.
- (Q1): the block of the corner in `Z''_{i+1}` lies in `F(p)` and in `Z''_{i+1}`. The corner in `K_i` lies
  outside it. Lemma G (c) applies.
- Otherwise `F(p) cap Z''_{i+1}` is empty: `Z''_{i+1}` is a union of aligned level-(i+1) blocks (`H_{i+1}` grid
  for `i + 1 <= k_0`; `M`-cubes of level `i + 1` for `i + 1 > k_0`, Y 63806-63809). So `F(p) subset K_i`.
- `i <= k_0`: `O_i subset G_i subset H_{i+1} subset Z''_{i+1}`. For `i = k_0`: `G_{k_0} subset H subset H^{[u_t]} = Z''_{k_0+1}`.
  So `K_i subset O_{i+1} minus O_i`, the region of (D4) for `i = h` and the second region for `h < i <= k_0`.
- `i >= k_0 + 1`: `O_{k_0+1} minus Z''_{i+1}`, `E^i_{k_0+1}`, ..., `E^i_i` partition `K_i`. The nesting
  `O_{k_0+1} subset ... subset O_{i+1}` is (B3) for `l' <= i <= t - 1`. A footprint in no single piece meets
  two pieces, and so it is astride some `dO_{l'}`, `k_0 < l' <= i`.
- Uniqueness of `l'`. `F(p)` meets `O_{l'}` and `O_{l''}^c`, so its diameter (below `2 L^{i+1}`) is at least
  `dist(O_{l'}, O_{l''}^c) >= 2 a_{l'} + 8 a_{l'+1}` by (B3). This exceeds `2 L^{i+1}` because
  `a_{l'+1} >= L u_t`.
- The second half of (2.1), `a_q >= L u_t` for `q >= k_0 + 2`, is Y's sentence (Y 63776-63778). It follows
  from Y's definition of `k_0 + 1` as the *last* index with `a = u_t`. The values `a_q = M R_q L^q` lie in
  `M L^Z`. The ratio `a_{q+1}/a_q = L R_{q+1}/R_q` is at most `L`, since `R` is non-increasing. Also
  `a_t >= u_t`. If some `a_q < u_t` with `q > k_0 + 1`, then the first later index with `a >= u_t` has
  `a = u_t`, which contradicts "last". So `a_q > u_t`, that is `a_q >= L u_t`.

Edge cases.

- `i = h`: (Q1) gives `N subset O_{h+1} minus O_h` (Lemma 6.3 of `cov-x`, case `l = h + 1 <= k_0`, since `h < k_0`).
  (Q2) gives `R = O_{h+1} minus O_h = Lay^h_h`. (Q3) does not occur.
- `i = k_0`: (Q1) gives `N subset H^{[u_t + 2L^{k_0+1}]} minus H^{[u_t - 2L^{k_0+1}]} subset O_{k_0+1} minus O_{k_0}`.
  (Q2) gives `K_{k_0} subset O_{k_0+1} minus O_{k_0}`. (Q3) does not occur.
- `i = k_0 + 1`: (Q1) gives `N subset H^{[8u_t]} minus H^{[u_t]} = E^{k_0+1}_0`. This needs
  `w_{k_0+1} - w_{k_0+2} >= u_{k_0+2} >= 2L^{k_0+2}`, which is (B2). (Q3) occurs only at `dO_{k_0+1}`, with `d = 1`.
- `i = t - 1`: see item (4). (Q2) has the factor 3 only on `E^{t-1}_{t-1} = O_t minus O_{t-1}`.
- `t - 1 = k_0 + 1`: `w_{t-1} = 2u_t` and `Z''_{t-1} = H^{[u_t]}`. (Q1) gives
  `N subset H^{[3u_t + 2L^t]} minus H^{[3u_t - 2L^t]} subset H^{[8u_t]} minus H^{[u_t]} = E^{t-1}_0`. The only wall is
  `dO_{k_0+1} = dO_{t-1}`, with `d = 1`. The last-stage branch of Step 4 of Lemma 5.1 then gives `L^d = L = R_{k_0+1} <= 2^r L R_t`.

The claim "`F(p)` does not meet `Z''_i`" in (Q1) uses Step 1 of Lemma 4.1. That step is a box computation
that does not use Lemma 3.1, so there is no circularity.

### (2) Finding 1: HOLDS WITH REPAIR (R1)

The definition of `Fr_i(X)` (Lemma 4.1 (b) of `cov-global`) puts all four corners in `O_{i+1}`. The alignment
fact for `O_{i+1}` at level `i + 1` then gives `F(p) subset O_{i+1}`. So no plaquette of `Fr_i(X)` is
*astride* `dO_{i+1}`. The walls of (Q3) are `k_0 < l' <= i`, and `d >= 1`.

A level-(i+1) plaquette astride `dO_{i+1}` has a corner in `X minus O_{i+1}`, which is the old member of
index `i + 1`. The level-(i+1) case of Lemma 4.1 (b) of `cov-global` carries it over with the same loop.
Y treats the same plaquettes with "the original level-`q` density test" (Y 77571-77574, early seam) and
"When `q = l` the bound follows directly from the original positive density test" (Y 77700-77702).

**R1 (text for the file).** Finding 1, second sentence, and the last sentence of Lemma 3.1: replace "it
does not meet `dO_{i+1}`" and "in no case does `F(p)` meet `dO_{i+1}`" with "it is not astride `dO_{i+1}`
(it lies in `O_{i+1}`; it can touch the face from inside, and it is then inside one region of (X1))".
Reason: `F(p)` can contain sites of `O_{i+1}` next to its face. The literal "does not meet" is false if
`dO_{i+1}` is read as the set of boundary sites. Nothing in the proofs uses the literal form.
