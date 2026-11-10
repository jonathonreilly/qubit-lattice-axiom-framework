lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T17:04Z

# Check of `library/cov-global.md` (row 636)

Provenance: Claude Opus 5.5, high effort, Mini Claude worker 2, commit 45cae89b2. One line-by-line reading by a model that did not write the note (cov-global is by Claude Fable 5.2). Not an audit. Source: YM4_1400.tex (Sussman and Alpoge, with Claude and Codex as authors of their text), pin 2bc0658f91d2; 'Y n' is line n.

`library/cov-frames.md` (row 638) exists at the start of this lane. It is named only and not checked here.

(sections follow as they are written)

## 1. Items (1) to (5): the rules and the window lemma

**(1) R1 to R5 against Y.**

- (R1) HOLDS. Y 1158-1160 gives the label and the nesting. Y 62081 (Proposition "geometry") gives cells of their own level, stage sequences and nests, and `dist(Z_j, Omega_{j+1}) >= LM` in level-j units, that is `M L^{j+1}` bare. Citation repair: "every level-(l+1) cell is a union of level-l cells" needs `R_k <= L R_{k+1}` and nested partitions. Y 62001 states both ("Because it is a power of L, all partitions are nested"; "`R_k <= L R_{k+1}`"). Non-increasing alone does not give it.
- (R2) HOLDS as a weakening. Y 61985: `Omega_t^c = Q'^{~2} cup P'^{~4} cup hat Y^{~8}` for `t >= 2`, with `Y = Z_{t-1}` the live region and "Hulls (', ^) and layers are taken in level-t cells". Y 78445-78447 says the same in words. For a component, Y 63700-63705 uses the box hull `H_i`, with `G_{i-1} subset H_i`. Both hulls contain every level-t cell that contains a level-(t-1) cell of `Z_{t-1}`. So the note's `hat Z_{t-1}` is contained in Y's hull, and `N_8(hat Z) subset Omega_t^c` follows. Y gives no one-line definition of `hat`; the inclusion holds for each candidate reading (cover by cells, box hull).
- (R3) HOLDS. Y 63684 is quoted correctly. (Q) is weaker than Y's quarantine: a standing mark of level `s in [h, t)` inside X means that an operation of that level acted on part of X. A weaker hypothesis gives a stronger result. (Q) is also what Y's own proof of (R5) uses ("This contradicts the exclusion of marks at levels h, ..., k-1", Y 63727-63728). Y's literal rule also excludes healed components of level `s in [h, t)` inside X. The note does not need that exclusion, and it does not use it.
- (R4) HOLDS. Y 62104-62121 and 62174-62178: healed, island and drop-out change the entries that the note lists, and "Outside the class no entries change". The note omits the entries `S_l`. No step of the note reads `S_l`.
- (R5) HOLDS, and Y's proof at Y 63712-63738 is sound. I redid it. Let q be a cell of `G_i` and `i <= s < t`. Then q is in `Z_i(S'_s) subset Z_s(S'_s)`. If an operation acts on the component through q: healing, or an island with `i < s`, puts q into `Lambda_i` for good, against `q subset Z_i(S'_t)`. Every other fate makes a mark of level `s in [h, t)`. If the mark is later swallowed, q enters `Lambda_i`. If it stands, it lies in X by nesting and connectedness, against (Q). So no operation acts on q, and steps copy the lower entries. This gives (a). For (b), the component K of `Z_i(S'_i)` through q stays in the same component of `Z_s` as q at each later operation, which therefore leaves K alone; at the end K is connected, contains q and lies in `Z_t(S'_t)`, so `K subset X`.

**(2) Lemma 3.0.** HOLDS. Creation: an island leaves `Lambda_m` unchanged and a drop-out has `Lambda_m cap C` empty (Y 62112-62118). Step: entries of index `m` copied. Operation of level `s > m` on X': `C subset Z_m subset Z_s`, so `C subset X'` or disjoint. Healed or island X' swallows C. Drop-out X': (Q) for X' gives `m notin [s_flat, s)`, so `m < s_flat`, and the changed indices `l > s_flat` miss `m`. Operations of the same level `m` on other components: the note does not name this case. It is covered by the same argument with `s = m`: the other class components are other components of `Z_m(S'_m)`, so disjoint from C, and nothing changes on C. Repair of wording only: "an operation of level `s >= m` other than the one on C".

**(3) Lemma 3.1.** (a) HOLDS: `m < t`; `C subset Z_m(S'_t) subset Z_t(S'_t)` and connected; (Q) gives `m < h`; nesting gives `C subset Z_{h-1} subset Z_h`. (b) HOLDS: two components of `Z_t(S'_t)` share no point; two closed cells of one grid of side `a_t` with no common point are at sup distance at least `a_t`. (c) HOLDS: C stood at `S'_{m'}` (a swallowed mark does not stand again), and C' is a class component of level `m'` there, so (a) gives `C subset C'` and `m < m'_flat`; the affected levels `(s_flat, s_flat + n]` lie in the window `(s_flat, s]`. This is Y 62128 "Marks wait".

**(4) Lemma 3.2.** HOLDS.

- Input of step h. The mark stands in `S_{h-1}` (made at level `m <= h - 1`, stands in `S'_t`). Lemma 3.0 and nesting give `c subset C subset Z_m subset Z_{h-1}` there. The level-(h-1) cell `c'` that contains c is a cell of `Z_{h-1}` (c has interior points, and `Z_{h-1}` is a union of closed level-(h-1) cells), and `c' subset q` because the partitions are nested. So `q` is in the note's `hat Z_{h-1}`, and (R2) gives `N_8(q) subset Omega_h^c(S'_h)`. This use of (R2) is correct.
- (R5)(b) at `i = h`: `N_8(q)` is connected, contains q and lies in `Omega_h^c(S'_h) subset Z_h(S'_h)`, so it lies in `G_h`. (R5)(a) at `i = h` moves the non-membership in `Omega_h` from `S'_h` to `S'_t`. Both uses are correct. Note that q is in `G_h` because `c subset G_h` (Lemma 3.1 (a)) and `G_h` is a union of level-h cells (X is a union of level-t cells, which are unions of level-h cells).
- (ii) is correct: a cell touching a cell of `N_7(Q)` is in `N_8(Q) subset O_h`.
- `2 L^m < a_h`: `a_h = M R_h L^h >= M L^{m+1}` needs `R_h >= 1` (Y 62001: the smallest power of L not less than `(log min x_i)^r`; this is at least 1 when `min x_i >= e`, as for the large `x_i` of Y; the note should state it) and `M >= 2`. Correct.
- (iii): a point within `2 L^m < a_h` of a cell `c subset q` is in q or in a cell touching q. Correct. The last sentence: a cell meeting `N_1(Q)` is in `N_2(Q)`, and every cell within index distance 6 of `N_2(Q)` is in `N_8(Q) subset O_h`. Correct.
- Against Y 76830-76840 and Y 78062-78070. Y 78064-78067: "an older standing mark of level m<h is in the retained Z_{h-1} and in the innermost box G_h ... The hull and eight-layer enlargement at step h still contain the witness after removing the cells in contact with Omega_h". The note's proof is this sentence written out. Y 76832-76837 splits `h = m + 1` and `h > m + 1`; the note's single case (the mark is already in `Z_{h-1}` at the input of step h) covers both. Agreed.

**(5) Corollary 3.5 and Remark 3.4.**

- Corollary 3.5 HOLDS. (R1) holds for the determining sequence (Y 62081 names the stage sequences and drop-out nests; Y 62128: "each `Omega^nu` is the geometric label obtained by stopping the operations after nu stages"). During a stage of a component X' that contains C, the entries of index `<= m + 1 <= h'` on C do not change, so `C subset Z_m` holds in the determining sequence too. The step `l = m + 1` excluded by `2 L^m + L^{m+1} < M L^{m+1}` is correct. Simplification: once `x in N_1(Q(C))` and every point of `F(p)` is within `2 L^l < a_h` of x, `F(p) subset N_2(Q(C)) subset O_h` follows from Lemma 3.2 (i) directly; the detour through Lemma G (b) is not needed.
- Remark 3.4 HOLDS as a remark. Under (Q) a mark of level `m >= h` in X does not occur, and Y 62145-62151 uses the same exclusion. The sentence on the open window is not part of the theorem; I did not check it.
