lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T12:49Z

# cov-global: the assignment (COV) outside X as an invariant of the moves (FINISH row 632)

Status: DONE 2026-11-10 (one session, Claude Fable 5.2, medium; not checked by another model; no numeric
job was run; nothing here rests on a computation).

Queue row: FINISH 632. Pinned at commit e8fb5cf0f. Source: Sussman and Alpoge, `YM4_1400.tex` at commit
2bc0658f91d2 of the Yang--Mills-LLM-experiment repository; `Y n` is line n of that file.

Credit. The operation, the three fates, the marks, the two region sequences, the class with its
quarantine, the tracing of an eligible component, the assignment of suppliers and the window statement
are Sussman and Alpoge's (their text names Claude and Codex as authors): Y 1157-1206, 62081-62178,
63684-63876, 65409-65487, 76654-76701, 76826-76840, 77741-77815, 78062-78075, 97547-97557. The step, the
class of small quiet components and the operation R are Bałaban's (CMP 119 p. 256; CMP 122 (1989) 175,
pp. 176-177, 183, 195). In this repository: `library/geoh.md` Lemma 4 and `library/geoh-draft.md` Theorem M
(GEO-mark; Codex and Claude lanes) give the first clause of the window lemma; `library/cov-x.md` (Claude
Fable 5.2) gives the definitions D1 to D6, its Lemma 5.1 and the suppliers in X; `library/i3-cert.md`
(Claude Fable 5.2) gives the statement (COV), Definitions 4.1 to 4.3 and Lemma 2; `library/prior/cov-read.md`
(Codex) is the reading map.

Labels: **proved** (a written argument from the stated hypotheses), **read** (a definition or statement of
Y used as a hypothesis, with its lines; not rebuilt here), **ported** (Y proves it at the lines given; not
redone), **gap**.

## 0. Result

**Verdict: stop condition (i), with the hypotheses named.** (COV-G) is proved as an invariant of the
trajectory (Theorem 5.1), from

- the rules of the history read from Y (R1 to R5, section 2) and the frame statements of the moves read
  from Y (F-step, F-stage, F-stop, F-main, F-refresh, section 4.1);
- (COV-X*), the supplier inside X for the plaquettes that a stage of X makes new (section 4.3). This is
  (COV-X) of row 628 asked at the exit of **each** stage, not only at the final entrance `N`;
- two read statements on the tests: (R-ord) for the ordinary density tests and (R-last), (R-core) for the
  healed component and the island (section 4.2).

The window lemma (G1) is **proved** in full from R1 to R5 (Lemma 3.1, Lemma 3.2). No history breaks the
invariant. No new estimate is made.

| Step of the row | Result | Status |
|---|---|---|
| (G0) definitions | section 2.2, each with its lines | **read** |
| (G1) window lemma, clause `m < h`, `C subset G_h` | Lemma 3.1; it is Y 62128 "Marks wait" and `library/geoh.md` Lemma 4, from the quarantine with closed lower end | **proved** from R1, R3, R4 |
| (G1) the witness lies in the floor less the cells in contact with `Omega_h` | Lemma 3.2: the eight-cell neighbourhood of every level-h cell of the mark lies in `O_h`; the witness is at least six cells inside the cells in contact with `Omega_h` | **proved** from R1, R2, R5. Y states it at Y 76830-76840, 78062-78070 with a two-case sketch; one case suffices |
| (G1) a mark of level `m >= h` meeting X | cannot occur for a class component: it is the quarantine. Remark 3.4 says what the open-window reading (`m = h`) would change | **proved** |
| (G2) frame lemma | Lemma 4.1: the fresh plaquettes of each move, all with footprint in X and level `>= h + 1` | **proved** from the read statements F |
| (G3) base | Lemma 4.2, from (R-ord) | **proved** given (R-ord) |
| (G4) step | Theorem 5.1, by cases in section 5 | **proved** given (COV-X*), (R-last), (R-core) |
| (G5) (c3) | Lemma 5.3: one determining sequence at a point; no loop has links of two data | **proved** from Lemma 3.1 and (E1) |

Five findings for the lead.

1. **The invariant needs no statement about removal of tests.** In the form of `library/i3-cert.md` 5.4 a
   supplier is a test carried at a moment `mu <= nu` of the admitted trajectory, with the loop at `nu`
   equal (up to conjugation) to the loop the supplier bounds. A test removed after `mu` is still a
   supplier. So the step "show by the removal rule that this test is still in the term" is not needed,
   and it cannot be done from Y, which does not list the removed indicators (Y 77751-77757 gives only the
   condition for a removal). Y does keep the two tests that the row asks about: "The removal uses the
   retained averaging deltas and the density tests at the top and the old core" (Y 77747-77749).
2. **Only new plaquettes need a supplier.** Call a tested plaquette *fresh* at a move if it was not tested
   before the move or its loop changed other than by conjugation. Every other plaquette keeps its supplier
   (Lemma 5.2). The fresh plaquettes are: the top level of an ordinary step; at stage `i` of X the
   level-(i+1) plaquettes with all corners in `O_{i+1}` and a corner in the collar `K_i`; at the main step
   the level-t plaquettes with an edge in the box `Lambda^pr`. A stop (stage failure or sharp collar
   split) makes no plaquette fresh, because "the retained determining list still has index `n`"
   (Y 77790-77791). So the supplier (S-col) is not needed for (COV-G): at a collar departure every tested
   plaquette keeps the supplier it had at the entrance of the stage. (S-col) gives a second supplier with
   the test `chi_i^{(n+1)}`; if a consumer wants that one, it is a statement inside X.
3. **(COV-X) is needed at every stage, and after the last one.** `library/cov-x.md` Theorem 6.1 is stated
   at the entrance `N` of the final stage. A drop-out after `n < N_t` stages, and the healed and island
   outcomes, need the supplier for the plaquettes made new by the stage of level `i` for every `i`,
   including the last stage `i = t - 1` (level-t plaquettes in `O_t` with a corner in `K_{t-1}`; their
   supplier would be the guard of the last stage, which `cov-x` does not treat). Section 4.3 lists which
   instances `cov-x` proves (the plaquettes with a corner in `Z''_{i+1}`, every `i <= t - 2`; all of them
   for `i = t - 2`) and which are not written (the exterior position for `i < t - 2`; the last stage).
4. **The floor clause of the window lemma is not what (COV-G) uses.** (COV-G) uses only `m < h` and
   `C subset G_h`: then every tested plaquette that meets the mark has level `<= m < h` and footprint in
   `O_h`, and the stages change no row and no region of level below `h` (Lemma 4.1). The floor clause is
   what the payment (Y 78055-78075) and the "still carried now" form use: the reads of the mark's tests
   are not written by the operation on X.
5. **(S-core) is a direct bound, and it is the one analytic import.** At an island the last test fails, so
   no density test bounds the level-t loops that touch the restored box. Y's supplier is the cutoff
   `abs(log V') < M_0 eps_t` with the bound on the reference `V_Lambda` from the passed extension test
   (Y 63836 (2), 63876, 76680-76685). I state it as (R-core) and did not rebuild it. The loop algebra from
   (R-core) to the defect is four lines (Lemma 5.4).

What stays open: (COV-X*) in the instances of finding 3; the read statements (R-ord), (R-last), (R-core)
and F as statements about the actual operation (they are Y's prose, not rebuilt); the check of
`library/cov-x.md` (row 633).

## 1. Repo search

- `grep -n "cov-global\|COV\|window" library/open-core.md`: no entry for COV, the window lemma or standing
  marks. FINISH rows: 624 (`i3-cert`), 628 (`cov-x`), 629 (`cov-read`), 630, 633 (checks), 634
  (`i3-repairs`), 632 (this row). No other row owns (COV-G).
- `grep -n "GEO-mark\|standing mark\|Marks wait" library/*.md FINISH.md`: **hit.** `library/geoh.md` Lemma 4
  (frozen; draft `library/geoh-draft.md` section 6, Theorem M) proves, under the quarantine with closed
  lower end: a standing mark `(s, Y)` in a class component at `t` has `s < t - N_t`; windows of standing
  marks that share a point are disjoint; a mark disappears only by a healing or an island. This is the
  first clause of (G1); I use it and do not redo it (Lemma 3.1 repeats the three lines, because the row
  asks for the mark "that meets X enlarged by its collar", which Theorem M does not state). `geoh.md`
  line 34 records an outstanding point: the revised operation of this lane must adopt the closed-end rule.
  For Y it is the definition (Y 63684: "the lower end point included").
- `grep -n -i "floor" library/geoh.md library/geoh-draft.md`: no statement on the floor or on the witness
  of a mark. Lemma 3.2 below is new in this repository. `library/geoh-draft.md` Lemma 7.2 gives
  `Omega_i^c cap X = N_8 H_i` for `h < i <= t`; it does not treat the level `h`.
- `library/prior/cov-read.md` (row 629): a reading; its table of moves is the map I used for section 4.
- This checkout has the ref `origin/claude/ym4d-hard-route` only (`git branch -r`). `origin/main` and the
  other YM4D PR branches are not present, so I did not search them.

## 2. Setting and definitions (G0)

Lengths are in bare units, distances in the sup norm. `a_l = M R_l L^l` is the side of a level-l cell
(Y 63748). `R_l` is a power of `L` and is non-increasing in `l` (Y 62001), so every level-(l+1) cell is a
union of level-l cells. Cells are closed cubes of a grid. For a set `A` of level-l cells, `N_r(A)` is the
set of level-l cells at index distance at most `r` from a cell of `A` (the `r`-cell neighbourhood).

### 2.1 The rules of the history (read)

- **(R1) Label, nesting, grids (Y 1157-1167; Y 62081 Proposition "geometry").** The label is
  `S = (Omega_l, Lambda_l, S_l)_{l <= t}` with `Omega_1 supset Lambda_1 supset Omega_2 supset ...`;
  `Z_l := Lambda_l^c`. Every region of index `l` is a union of level-l cells. `S'_s`, `S_s` are the labels
  just before and just after the operation of level `s` (Y 63713-63714). The nesting holds for the label
  with any stage index on each standing drop-out (Y 62128; `library/geoh.md` Lemma 4, first sentence).
  `dist(Z_l, Omega_{l+1}) >= M L^{l+1}` (Y 62081, first display, in bare units).
- **(R2) Step (Y 62001; Y 63700-63711; Y 75603-75605; Y 78445-78447; `library/geoh-draft.md` (G2)).** Step
  `l` has input `Z_{l-1}` (the label after the operation of level `l - 1`). Its output satisfies
  `Omega_l^c supset N_8(hat Z_{l-1})`, where `hat Z_{l-1}` is the set of level-l cells that contain a
  level-(l-1) cell of `Z_{l-1}` ("the complement of `Omega_t` contains the hull of `Z_{t-1}` and its
  eight-layer enlargement"). A step copies the entries of index below `l` and the standing marks
  (Y 62174).
- **(R3) Class (Y 63684).** `t_flat = t - N_t >= 1`; write `h = t_flat`. A component X of `Z_t(S'_t)` is in
  the class if: (single boxes) `X cap Z_i` is one small component of `Z_i` for `h <= i <= t`; (quiet) step
  `i` creates nothing in it and joins nothing to it, `h < i <= t`; (quarantine) "it has not been acted on
  by any operation whose level lies in `[t_flat, t)`, the lower end point included". I use the quarantine
  in the form in which Y uses it (Y 62128, 63722-63727, 73104-73106, 76856-76857):
  **(Q)** no mark of level `s in [h, t)` that stands in `S'_t` lies in X.
- **(R4) Fates and marks (Y 62104-62121, 62174-62178).** The operation of level `t` acts on the class
  components and changes no entry outside them. *Healed*: `Omega_l, Lambda_l -> Omega_l cup X, Lambda_l cup X`
  for `l <= t`. *Island*: the same for `l < t` and for `Omega_t`; `Lambda_t` unchanged. *Drop-out* after
  `n <= N_t` stages: `Omega_l cap X = Lambda_l cap X = X minus Z''_l(X)` for `h < l <= h + n` (`Lambda` for
  `l < t`), `Lambda_t cap X` empty, every other entry unchanged. Islands and drop-outs are the *marks*. A
  mark of level `t` is made by the operation of level `t`. "A mark persists until a later healed
  component or island swallows it"; a healed component or island "overwrites the older entries on its
  region, and any mark it swallows ceases to stand".
- **(R5) Tracing (ported: Y 63712-63738, with its proof).** Let X be a class component of level `t` and
  `h <= i <= t`. For every level-i cell `q` of `G_i := Z_i(S'_t) cap X`: (a) the memberships of `q` (and of
  its subcells) in the regions of index `i` and `i - 1` are the same in `S'_t` as in `S'_i`; (b) the whole
  component of `Z_i(S'_i)` through `q` lies in `Z_i(S'_t)` and in X.

### 2.2 The terms of the row (read, with lines)

- **Standing mark.** A marked component (island or drop-out) made by an earlier operation and not yet
  swallowed (R4; Y 62121). Its *level* is the level of the operation that made it.
- **Drop-out record (Y 1184-1198, 62121-62126).** For a drop-out C of level `s`: the former regions
  `Omega_l° cap C` (and `Lambda_l°, S_l°`), the stage boxes `Z''_l(C)`, `s_flat < l <= s`, and the stage
  count `n(C)`.
- **Departure.** The pair (stage count `n(C)`, kind). Kind *stage failure*: a test of the stages, or the
  extension test (2), fails after `n` completed stages (Y 62108, 63876 "If one of the tests of (1)-(3)
  fails in a component, that component drops out"). Kind *sharp collar split*: in stage `n + 1`, after the
  regularity test `chi_s^{(n+1)}`, the collar gauge, the approximate test `chi'_j` at `2 delta'_j`
  (`j = s_flat + n`) and the removal, the sharp test at `delta'_j` fails (Y 77741-77763); "the retained
  determining list still has index `n`" (Y 77790-77791). The *least-level departure* of a place
  (Y 65425-65426) is the departure of its owner.
- **Waiting window.** For an operation of level `t`: the levels `(t_flat, t]` (Y 62128: "their windows
  `(s_flat, s]`"); the operation is eligible only if `t_flat >= 0` (Y 1182-1183; `>= 1` at Y 63684). The
  affected levels of a drop-out C are `(s_flat, s_flat + n(C)]`.
- **Determining sequence at a moment (Y 1184-1202, 62122-62128; `library/cov-x.md` (D1)).** The label, with
  (R21) and `nu(C) = n(C)` on each standing drop-out, and on a class component under operation with `n`
  completed stages the same formula with `n`: `Omega^det_l cap X = X minus Z''_l(X)` for `h < l <= h + n`.
  By (R4) it **is** the label at the moments between operations. `Lay_l := Omega^det_l minus Omega^det_{l+1}`.
- **Datum, tested plaquette, footprint, loop.** As in `library/i3-cert.md` Definition 4.1 and Definition T,
  for the determining sequence: a level-l plaquette with a corner in `Omega^det_l` and no corner in
  `Omega^det_{l+1}`; `F(p)` is the union of the order-l blocks of its corners; the value of a row edge is
  the carried link, the value of a completed edge is `M(V_{l-1})` on its double block; `W(p)` is the
  product of the four values. `P_nu` is the set of tested plaquettes at the moment `nu`.
- **Owner (Y 77810-77811).** The standing drop-out of smallest level that contains the place of `p`; none
  if no standing drop-out contains it.
- **Tested inset of a drop-out C with `n` stages (Y 65426-65433, 76661-76668, 77812-77817; the clause
  regions of `library/cov-x.md` (D4)).** The union of the regions on which its last positive stage test
  gives a bare bound: the shells `Z''_{q+1}(C) minus Z''_q(C)`, `s_flat <= q < s_flat + n`, and the exterior
  regions of that test. "Footprint in the tested inset" means `F(p)` inside one of these regions.
- **Witness of a mark C of level `m` (Y 97547-97550, 72146).** `C^+`: C enlarged by two layers of unit
  cubes of level `m`, so `C^+ subset C^{[2 L^m]}`.
- **Floor of a class component X with window from `h` (Y 72655, 78067-78070, 78424-78426).**
  `Fl(X) := O_h = Omega_h^c(S'_t) cap X`, the old core. The *protected floor* `Fl^-(X)` is the union of
  the level-h cells of `O_h` that touch no level-h cell of `Omega_h`.

## 3. The window lemma (G1)

**Lemma 3.0 (a standing mark stays in its top region; proved from R1, R3, R4).** Let `(C, m)` be a mark
that stands in a label `S` later than its creation. Then `C subset Z_m(S)`, and `C` is connected.

*Proof.* C was a component of `Z_m(S'_m)`, a connected union of level-m cells. At its creation
`Lambda_m cap C` is empty (drop-out) or unchanged (island) by (R4), so `C subset Z_m(S_m)`. Induction over
the later moves. A step copies the entries of index `m` (R2). An operation of level `s > m` changes
entries only inside its class components (R4). Let X' be one. By the induction hypothesis and the nesting
(R1), `C subset Z_m subset Z_s` in `S'_s`; C is connected and X' is a component of `Z_s(S'_s)`, so
`C subset X'` or `C cap X'` is empty. In the second case nothing changes on C. In the first case: if X' is
healed or becomes an island, C is swallowed and does not stand afterwards (R4), against the hypothesis.
If X' drops out, the changed entries have index `l` with `s_flat < l <= s` (R4), and (Q) for X' gives
`m < s_flat`, so the entries of index `m` on C are unchanged. `square`

**Lemma 3.1 (marks wait; Y 62128, `library/geoh.md` Lemma 4).** Let X be a class component of level `t`
with `h = t - N_t`, and let `(C, m)` be a mark standing in `S'_t`.

- (a) If C meets X, then `C subset X`, `m < h`, and `C subset Z_{h-1}(S'_t) cap X subset G_h`.
- (b) If C does not meet X, then `dist(C, X) >= a_t`. So C does not meet `X^{[s]}` for any `s < a_t`.
- (c) Standing marks that share a point are nested and their windows are disjoint: if `(C, m)`, `(C', m')`
  stand and meet, `m < m'`, then `C subset C'` and `m < m'_flat`. So at a place and a level at most one
  standing drop-out has that level among its affected levels, and the determining sequence of 2.2 is
  defined without a conflict.

*Proof.* (a), (b). `m < t`, since a mark standing in `S'_t` was made by an operation of level below `t`.
By Lemma 3.0 and (R1), `C subset Z_m(S'_t) subset Z_t(S'_t)`, and C is connected, so C lies in one
component of `Z_t(S'_t)`. If C meets X this component is X, and (Q) gives `m < h`. Then
`Z_m subset Z_{h-1} subset Z_h` in `S'_t` by (R1), so `C subset Z_{h-1}(S'_t) cap X subset Z_h(S'_t) cap X = G_h`.
If C does not meet X, it lies in another component X'. X and X' are unions of closed level-t cells (R1)
with no common point (two cells with a common point are in one component). Two closed cells of one grid
of side `a_t` with no common point have sup distance at least `a_t`. (c) is (a) at the moment `S'_{m'}`
for the class component C' (C stood then, since a swallowed mark does not stand again); the affected
levels of a drop-out lie in its window. `square`

Remark 3.1'. "X enlarged by its collar": every read of the operation on X outside X that Y names lies
within one cell: `X^{+1}` (Y 105657), the two unit layers `X^+` (Y 72146), "complete blocks inside the
component's exterior buffer" (Y 77773-77774). I did not find a single definition of the exterior read of
the operation in Y; (b) holds for every enlargement by less than `a_t`.

**Lemma 3.2 (the witness lies in the protected floor; proved from R1, R2, R5 and Lemma 3.1).** In the
setting of Lemma 3.1 (a), let `Q(C)` be the set of level-h cells that contain a level-m cell of C. Then

- (i) `N_8(Q(C)) subset O_h = Fl(X)`;
- (ii) `N_7(Q(C)) subset Fl^-(X)`;
- (iii) `C^+ subset C^{[2 L^m]} subset N_1(Q(C))`. So the witness lies in `Fl^-(X)`, and every level-h cell
  that meets the witness is at index distance at least 7 from every cell of `Omega_h` (and from `X^c`).

*Proof.* (i) Let `q in Q(C)` and let `c subset q` be a level-m cell of C. The mark C stood at every moment
between its creation (level `m <= h - 1`) and `S'_t`, in particular in `S_{h-1}`, the label that step `h`
takes as input. By Lemma 3.0 and (R1) in that label, `c subset C subset Z_m subset Z_{h-1}`. `Z_{h-1}` is a
union of level-(h-1) cells and `c` has interior points, so the level-(h-1) cell that contains `c` is in
`Z_{h-1}`; it lies in `q`. So `q in hat Z_{h-1}`, and (R2) gives `N_8(q) subset Omega_h^c` at the output of step `h`, which is `S'_h`.
Now `N_8(q)` is a connected union of cells that contains `q` and lies in `Omega_h^c(S'_h) subset Z_h(S'_h)`
(R1: `Lambda_h subset Omega_h`). The cell `q` lies in `G_h`: by Lemma 3.1 (a) the cell `c` is in `G_h`,
which is a union of level-h cells, and `c` has interior points. By (R5)(b) at `i = h` the component of
`Z_h(S'_h)` through `q` lies in `Z_h(S'_t) cap X = G_h`; so `N_8(q) subset G_h`. By (R5)(a) each cell `q'` of
`N_8(q)`, being a cell of `G_h`, has the same membership in `Omega_h` in `S'_t` as in `S'_h`. So
`q' subset Omega_h^c(S'_t) cap X = O_h`.

(ii) A level-h cell that touches a cell `q''` of `N_7(Q(C))` is in `N_8(Q(C))`, hence in `O_h` by (i), hence
not a cell of `Omega_h`, and it is in X.

(iii) `2 L^m < a_h`, because `a_h = M R_h L^h >= M L^{m+1}` and `M >= 2`. A point within `2 L^m` of a cell
`c subset q` lies in `q` or in a cell that touches `q`. `square`

Remark 3.3 (what Y has). Y states the lemma at Y 78062-78070 and argues it at Y 76830-76840 in two cases
(`h = m + 1`: "the eight-cell buffer of the ordinary step therefore puts the full `h`-cell carrier of
`C(v)^+` in the floor"; `h > m + 1`: "the neighborhood has already entered `Z_{h-1}`, whose hull again
receives eight cells before reaching `Omega_h`"), and again at Y 78420-78427. The sentence "the floor
entries on the containing component agree with those of this ordinary step" (Y 76838-76839) is (R5)(a).
The proof above does not need the two cases: the mark itself is in `Z_{h-1}` at the input of step `h`.
Y 1202-1206 ("These geometric facts require verification for the actual operation") is answered by
Lemmas 3.0 to 3.2 for an operation that obeys R1 to R5.

Remark 3.4 (a mark of level `m >= h`). By (Q) no such mark lies in a class component; a component of
`Z_t` that contains one is not in the class and no operation acts on it (Y 62145-62151 uses this:
"that component is ineligible in both labels"). So the case does not occur, and no mark is "swallowed"
other than a mark of level `m < h` inside a component that heals or becomes an island (R4). If the
quarantine had the open window `(h, t)` (the rule of CA-I 45996-46032, see `library/geoh.md` line 32), a
mark of level `m = h` could lie in X. By (single boxes) it would be the whole box `G_h`. Then Lemma 3.2
fails (the witness reaches `2 L^h` beyond `G_h`, outside `O_h`), and the affected levels of the mark
reach `h`, the level whose rows stage `h` of X integrates in `K_h`. I did not examine whether the
invariant survives there; Y's rule excludes it.

Corollary 3.5 (levels at a mark; proved). Let `(C, m)` stand at a moment, and let `p` be a tested
plaquette of level `l` with a corner in `C^{[2 L^m]}`. Then `l <= m`. If moreover C lies in a class
component X with window from `h`, then `l < h` and `F(p) subset O_h`.

*Proof.* The determining sequence is the label, with the stage sequence on a component under operation
(2.2), and (R1) holds for it. `C subset Z_m` by Lemma 3.0, so by (R1) no point at distance less than
`M L^{m+1}` from C is in `Omega^det_{m+1}`. Let `x` be the corner in `C^{[2 L^m]}`. Then `x` is in no member
of index above `m`, so it is in a layer of index at most `m`. The corners of a tested plaquette of level
`l` are in `Lay_{l-1} cup Lay_l` (Definition T), so `l <= m + 1`. If `l = m + 1`, some corner `y` is in
`Omega^det_{m+1}`, and `y` is within `L^{m+1}` of `x`, hence within `2 L^m + L^{m+1} < M L^{m+1}` of C
(`M >= 2`, `L >= 3`): a contradiction. So `l <= m`. In X: `l <= m < h` by Lemma 3.1 (a). No corner of `p` is
in `Omega^det_{l+1}`, which contains `Omega_h cap X` (`l + 1 <= h`) and is a union of aligned level-l
blocks, so `F(p)` does not meet `Omega_h` (`library/cov-x.md` Lemma G (b)). Every point of `F(p)` is within
`3 L^l / 2 < a_h` of `x`, and `x` lies in `N_1(Q(C))`, which is at least seven cells inside X (Lemma 3.2). So
`F(p) subset X minus Omega_h = O_h`. `square`

Remark 3.6. Lemma 3.0 is Y 76018-76019 ("While it stands, it remains a component of its original `Z_i` with
all entries through level `i` unchanged"), which Y states without the induction.

## 4. The moves: what each one changes (G2), and the base (G3)

### 4.0 Moments, fresh plaquettes

A *moment* is a place in the formula between two moves: after a step, at the entrance and the exit of a
stage of a class component, after a stop, after the main step. (`library/i3-cert.md` Definition 4.1 takes
the entrances of stages; the definition of an admitted trajectory, Definition 4.3 there, is used with all
these moments.) Class components of one operation are disjoint and at distance at least `a_t`
(Lemma 3.1 (b) argument), and each move below is a move of one component, so the order among them does
not matter.

**Definition 4.0.** Let `nu`, `nu + 1` be consecutive moments of a trajectory. A plaquette `p in P_{nu+1}`
is *carried over* if `p in P_nu` and `W(p)(x_{nu+1}) = g W(p)(x_nu) g^{-1}` for some `g in SU(2)`. Otherwise
it is *fresh* at the move.

### 4.1 The frame statements (read) and the frame lemma (proved from them)

Each statement gives the variables and the entries that the move writes. X is a class component of level
`t` with window from `h`; boxes `O_i, G_i, Z''_i, K_i = O_{i+1} minus Z''_{i+1}` as in `library/cov-x.md` 2.1
and (D1); `Lambda^pr = Z''_t` enlarged by one layer of level-t `M`-cubes (Y 63836 (1)).

- **(F-step) Step `l` (Y 62174, 62078 (c), 76674-76676).** It adds the entries of index `l` and the level-l
  field; it changes no entry of lower index. For a plaquette of level below `l` that is tested before and
  after the step, the loop after is a conjugate of the loop before (the step moves retained rows only by
  its gauge draws: "A gauge draw, a frame change or a tree gauge conjugates the holonomy").
- **(F-stage) Stage of level `i` of X, `h <= i <= t - 1`.** (D1), (D2), (D3) of `library/cov-x.md` 2.2, read
  there from Y 72244-72260, 64035-64036, 77767-77778, 63836 (1), 63849: the only member of the sequence that
  changes is the one of index `i + 1`, which grows by `K_i`; (m2) each new row `c` of level `i + 1` gets
  `V_{i+1}(c) = M(V_i)(c)`; (m1) the collar gauge acts on level-i bonds with an endpoint in `K_i` and is one
  at the level-(i+1) sites; (m3) the level-i bonds with an endpoint in `K_i` and none in the old member of
  index `i + 1` leave the point; nothing else changes, in X or outside ("the exterior of the component is
  fixed", Y 77775; "The core operation ..., which contains the failed tests, is at no point unfolded",
  Y 63849).
- **(F-stop) A stop of X after `n` completed stages, of either kind (Y 77790-77791; (R4)).** No row and no
  entry of the determining sequence changes: the sequence of a component with `n` completed stages and
  the sequence (R21) with `nu = n` of the drop-out are the same. The moves of the unfinished stage before
  a sharp collar split (regularity test, collar gauge, approximate test, completions, removals,
  Y 77741-77763) write no row other than by the collar gauge, which conjugates the level-j loops and fixes
  the coarse rows (Y 77765-77767).
- **(F-main) Main step of X after `N_t` stages, outcome healed or island (Y 63836 (2), (3), 63876 (4);
  (R4)).** The determining members become `Omega_l cup X` for all `l <= t`. The move writes `V_t` on the
  bonds of the box (the level-t bonds with both ends in `Lambda^pr`): "Integrals against any bounded `F`
  that is independent of `V_k` on the box are left unchanged by it". For a level-t plaquette with no edge
  in the box, tested before and after, the loop after is a conjugate of the loop before (tree gauge and
  its reverse, frame: Y 76674-76676, 76698-76699).
- **(F-refresh) Late Haar refresh (m4) (Y 65470-65472, 76677-76679).** "A late Haar refresh leaves the old
  determining datum in the inner slot." No row and no entry changes.

**Lemma 4.1 (frame lemma; proved from F and Lemma 3.1).** At each move the fresh plaquettes are contained
in the following sets.

- (a) Step `l`: the tested plaquettes of level `l`.
- (b) Stage of level `i` of X: `Fr_i(X)`, the level-(i+1) plaquettes with all four corners in `O_{i+1}` and
  at least one corner in `K_i`. For these `F(p) subset X`, and their level is at least `h + 1`.
- (c) A stop, a refresh: none.
- (d) Main step of X with outcome healed or island: `B(X)`, the level-t plaquettes with an edge in the
  box. After the move no plaquette of level below `t` with a corner in X is tested, and no tested
  plaquette of level below `t` has a footprint that meets X.

In particular a move of the operation on X changes no determining row and no entry outside X, none of
level below `h` in X, and every fresh plaquette has its complete footprint in X.

*Proof.* (a) Let `p in P_{nu+1}` have level `q < l`. Its tested status reads the members of index `q` and
`q + 1`. If `q + 1 < l` these are unchanged, so `p in P_nu`. If `q = l - 1`: `p` has a corner in `Omega_{l-1}`,
and before the step there is no member of index `l`, so `p in P_nu`. (F-step) gives the conjugacy.

(b) Levels `q <= i`: `library/cov-x.md` Lemma 5.1 (b): `p` is tested after the stage only if it was tested
before, and then the four edge values are the same. Levels `q > i + 1`: the members of index `q`, `q + 1`
and the rows of level `q` are unchanged; a completed edge reads the level-(q-1) rows of its double block
in `Lay_{q-1}`; for `q - 1 > i + 1` nothing there changes, and for `q - 1 = i + 1` the old rows of level
`i + 1` keep their values (`Gamma_{i+1} subset Gamma'_{i+1}`, Lemma 5.1 (a) there) and the old layer of index
`i + 1` is contained in the new one. So `p` is carried over with the same loop. Level `q = i + 1`: let `p`
be tested after the stage. Suppose a corner of `p` is in the old member of index `i + 1`. Then `p` was
tested before (the member of index `i + 2` is unchanged). An edge `e` of `p` that was a row keeps its
value. An edge that is a row now and was not: its ends are corners of `p` outside the old member of index
`i + 1`, so in the old `Lay_i`; it was a completed edge with value `M(V_i)(e)`, and by (m2) its value now is
`V_{i+1}(e) = M(V_i)(e)` taken at `x_{nu_i}`: the same. An edge that is completed now has both ends in the
new `Lay_i`, which is contained in the old one; its double block lies in the new `Lay_i`, whose level-i rows
are old rows with unchanged values (`Gamma'_i subset Gamma_i`). So the loop is the same. Suppose no corner
of `p` is in the old member of index `i + 1`. Then some corner is in `K_i subset O_{i+1}`, the other corners
are within `L^{i+1}` of it, and `dist(O_{i+1}, X^c) >= 2 a_{i+1} > L^{i+1}` (`G_{i+1} = O_{i+1}^{[2 a_{i+1}]} subset X`);
so all corners are in X and outside the old member, that is in `O_{i+1}`: `p in Fr_i(X)`. Every point of
`F(p)` is within `3 L^{i+1} / 2 < 2 a_{i+1}` of a corner, so `F(p) subset X`.

(c) is (F-stop), (F-refresh).

(d) After the move X lies in the member of index `t`, the top one. A tested plaquette of level `q < t` has
no corner in the member of index `q + 1 <= t`, so no corner in X; X is a union of aligned level-q blocks,
so `F(p)` does not meet X (Lemma G (b) of `cov-x`), and by (F-main) and (R4) its status and its edge values
do not change. Let `p` have level `t`, tested after the move, with no edge in the box. If no corner of `p`
is in X, nothing it reads changes. Otherwise each edge of `p` has an end outside `Lambda^pr supset Z''_t`. An
end in X outside `Z''_t` is in the member of index `t` before the move (`Omega^det_t cap X = X minus Z''_t`
after `N_t` stages), and an end outside X that is a corner of a tested level-t plaquette with another
corner in X is within `L^t < a_t` of X, hence in `Omega_t` (it is not in another component of `Z_t`, by the
distance `a_t`, and `Omega_t^c subset Z_t`). So `p` was tested before, all four edges were rows, they are
not bonds of the box, and (F-main) gives the conjugacy. `square`

Remark 4.1' (the regions of (m1) to (m5), as the row asks). (m1): reads and writes level-i bonds in
complete blocks with centre in `K_i` (Y 97530-97534: "centres in `((Omega_{iota+1}^{~3})^c minus Z''_{iota+1}) cap X`");
(m2): reads the level-i bonds of the double blocks of the new rows, in `O_{i+1}^{[L^{i+1}]} minus Z''_i`, and
writes the new rows; (m3): removes level-i bonds with an endpoint in `K_i`; (m4): writes a fresh slot that
only outgoing rows read; (m5): writes `V_t` on the bonds of `Lambda^pr`. All of these lie in
`G_t minus G_h` except (m5), which lies in `Lambda^pr` and replaces the core with everything in it. None
meets `G_h` before the main step: `K_i` lies outside `Z''_{i+1}`, the double blocks of its rows are within
`L^{i+1}` of it, and `dist(G_h, X minus Z''_{i+1}) >= M L^{i+1}` (`3 a_{h+1}` for `i = h`, Y 63817-63818; (B2) of
`cov-x` for `i > h`). And `Fl^-(X) subset O_h subset G_h`. With Lemma 3.2: the
operation on X neither reads for writing nor writes any variable in the witness of an older mark, until
a healing or an island replaces the whole of X.

### 4.2 The tests that supply the fresh plaquettes outside (COV-X*) (read)

- **(R-ord) (Y 62078 (c), 1150-1152, 65426-65430, 76654-76660, 76021-76023; (R2); `library/cov-x.md` (D6)).** At
  the output of step `l`, the density test `chi_l(square)` is carried, hence equals one on an admitted
  trajectory, for every level-l test cube `square subset Omega_l`. The test cubes of level `l` partition
  each level-l cell. If `chi_l(square) = 1` at a point, every level-l plaquette `q` with a corner in
  `square` has `norm(W(q) - 1) <= 2.1 eps_l` for the loop of the level-l datum of that point, in which the
  value on a bond that is not a row is the one-step average of the lower rows ((I4_l) of `cov-x`).
- **(R-last) (Y 62104-62105, 76692-76697).** If X is healed, the last test has passed: `chi_t(square) = 1`
  at the point after the main step, for the new level-t datum, for every level-t test cube
  `square subset X^{[-6 a_t]}`; (I4_t) holds for it.
- **(R-core) (Y 63836 (2), 63876 (4) and "The purpose of the stages", 65431-65433, 76680-76685).** After the
  main step with outcome island (or healed), for every level-t bond `b` with an end in X:
  `V_t(b) = V'(b) V_Lambda(b)`, where `V'(b) = 1` unless `b` is a bond of the box, the carried cutoff gives
  `norm(log V'(b)) < M_0 eps_t`, and the reference `V_Lambda` satisfies
  `norm(V_Lambda(dp) - 1) <= C(M) eps_t` for every level-t plaquette `p` with an edge in the box. (Y: "for
  exterior data with `abs(dV_k - 1) < eps` one has `abs(dV_Lambda - 1) <= C(M) eps`"; the exterior bound is
  the passed extension test and the surrounding density cubes.) This is the only analytic statement
  imported; I did not rebuild it, and its form (which plaquettes, which constant) is my reading.

**Lemma 4.2 (base, (G3); proved given (R-ord)).** Every plaquette that is fresh at step `l` has a corner
in a level-l test cube `square subset Omega_l` whose test is carried at the output of the step, and
`norm(W(p) - 1) <= 2.1 eps_l` there. In particular, at every moment before the first stage of any
operation, each tested plaquette of level `l >= 1` has the supplier (S-ord): the density test of step `l`
at the output of step `l`.

*Proof.* By Lemma 4.1 (a) a fresh plaquette has level `l`; it has a corner `x in Omega_l`. `Omega_l` is a
union of level-l cells (R1), each partitioned into test cubes, so `x` is in a test cube `square subset Omega_l`.
(R-ord). The test reads the loop of the level-l datum of that moment, which is `W(p)`. Before the first
stage only steps have occurred, and Lemma 5.2 below carries the supplier. `square`

### 4.3 The hypothesis inside X

**(COV-X*).** For each class component X, each `h <= i <= t - 1`, and each `p in Fr_i(X)` that is tested at
the exit `nu_{i+1}` of the stage of level `i`: `p` has a supplier in the sense of `library/cov-x.md`
Definition 3.1 (bare or coarse, with (c1), (c2'), (c3'), and `nu_{i+1}` in the place of `N`) at a moment
`mu` with `nu_h <= mu <= nu_{i+1}`.

What `library/cov-x.md` gives of it (not checked; row 633 is its check):

| Instance | In `cov-x` | Status |
|---|---|---|
| `i <= t - 2`, a corner of `p` in `Z''_{i+1}` (mixed at the prepared face) | Lemma 6.3 (case P4 with `l = i + 1`): the exterior clause of the guard at the entrance `nu_i`; the footprint is within `2 L^{i+1}` of `dZ''_{i+1}`, so the set of such `p` at `nu_{i+1}` is the set at `N` | proved there |
| `i = t - 2`, no corner in `Z''_{t-1}` | cases P5a, P5b (`l = j = t - 1`), supplier at `N = nu_{t-1}` | proved there |
| `i < t - 2`, no corner in `Z''_{i+1}` | not stated. At `N` the survivors are in case P3, with a supplier at `N`, which is later than `nu_{i+1}`. A drop-out with `h + n = i + 1` needs the guard at `nu_{i+1}`: the proofs of P5a, P5b with `j` replaced by `i + 1`. (D4) of `cov-x` is stated for every `i`, so I expect the same proof; it is not written | **gap** (in row 628's scope) |
| `i = t - 1` (the last stage; level-t plaquettes in `O_t` with a corner in `K_{t-1}`) | not treated: `cov-x` stops at the entrance of the final stage | **gap**; Remark 5.6 removes it for the healed outcome, from (R-last) and the top tests on `Omega_t^{~4}` |

## 5. The invariant (G4), (G5)

**Lemma 5.2 (carrying).** Let `p in P_{nu+1}` be carried over, and let `(mu, T, U)` be a supplier of `p` at
`x_nu` with (c2') up to conjugation: `W(p)(x_nu)` is a conjugate of `(M^l U)(dp)` (bare), or of `(M^d W)(dp)`
(coarse), or `norm(W(p)(x_nu) - 1) <= b` is given directly. Then the same holds at `x_{nu+1}`, with the same
allowance.

*Proof.* A conjugate of a conjugate; the norm of `W - 1` is invariant under conjugation. `square`

**Theorem 5.1 (COV-G).** Assume R1 to R5, the frame statements F, (R-ord), (R-last), (R-core), (COV-X*),
and `gamma` so small that the allowances are at most `alpha_L` (as in `cov-x` section 6). Let `x_0, ..., x_N`
be an admitted trajectory. Then at every moment `nu <= N` every tested plaquette `p` of level `l >= 1` of
the datum `D(x_nu)` has a certificate, namely the certificate it received at the last move `rho(p) <= nu`
at which it was fresh, carried since by Lemma 5.2:

| Last move at which `p` was fresh | Certificate, moment | Defect at `x_nu` | Row's name |
|---|---|---|---|
| step `l` | density test of level `l` on a cube in `Omega_l` that contains a corner of `p`, at the output of step `l` | `<= 2.1 eps_l` | (S-ord) |
| stage of level `l - 1` of a class component X (now under operation, a standing drop-out, or healed or an island with `l = t`) | the supplier of (COV-X*), at a moment in `[nu_h, nu_l]` | `<= C_2' e_l` (`cov-x` Theorem 6.1) | (S-stage), (S-new); the seventh kind of `cov-x` P5b |
| main step of X, healed, `l = t`, an edge in the box | last test on `X^{[-6 a_t]}`, after the main step | `<= 2.1 eps_t` | the top test of the new domain (Y 76697) |
| main step of X, island, `l = t`, an edge in the box | cutoff and reference, (R-core), after the main step | `<= (4 M_0 + C(M)) eps_t` | (S-core) |

In each case (c1) holds by the statement that supplies the certificate, (c2') holds up to conjugation by
Lemma 5.2, and (c3') holds by Lemma 5.3.

*Proof.* Induction on `nu`. At the first moment no plaquette of level `>= 1` is tested. Let the claim hold
at `nu`, and let `p in P_{nu+1}`. If `p` is carried over, Lemma 5.2. If `p` is fresh, the move from `nu` to
`nu + 1` is one of those of Lemma 4.1, and:

*Step `l`.* Lemma 4.2.

*Stage of level `i` of X.* `p in Fr_i(X)` by Lemma 4.1 (b), `l = i + 1`, and (COV-X*) gives the supplier.

*Stop, refresh.* No fresh plaquette (Lemma 4.1 (c)).

*Main step, healed.* `p in B(X)`: level `t`, with an edge whose ends are in `Lambda^pr`. In the notation of
`cov-x` 2.1, `Lambda^pr = H^{[4 u_t]} subset H^{[10 u_t]} = G_{k_0+1} subset H_{k_0+2} subset ... subset H_t`
(`G_{i-1} subset H_i`, `k_0 + 2 <= t`), and `X^{[-6 a_t]} = G_t^{[-6 a_t]} = H_t^{[4 a_t]} supset H_t`. So a corner
of `p` is in a level-t cell of `X^{[-6 a_t]}`, hence in a test cube inside it, and (R-last) gives the bound.

*Main step, island.* `p in B(X)`. Lemma 5.4.

The bound in the second line: `cov-x` Lemma 3.2 with the allowances of its Theorem 6.1. `square`

**Lemma 5.4 (the restored box; proved given (R-core)).** After the main step with outcome island, every
level-t plaquette `p` with an edge in the box has `norm(W(p) - 1) <= (4 M_0 + C(M)) eps_t`.

*Proof.* All four edges are rows after the move (X lies in the top member), with values
`V'(b_i) V_Lambda(b_i)`. `W(p)` is the ordered product of these values or their inverses. Replace
`V'(b_1), ..., V'(b_4)` by `1` one at a time. Each replacement changes the product by a term of norm
`norm(V'(b_i) - 1) <= norm(log V'(b_i)) < M_0 eps_t`, because the other factors are unitary. After four
replacements the product is `V_Lambda(dp)`. So `norm(W(p) - V_Lambda(dp)) < 4 M_0 eps_t`, and (R-core)
bounds `norm(V_Lambda(dp) - 1)`. `square`

**Lemma 5.3 ((c3), (G5); proved from Lemma 3.1 (c) and the carried constraints (E1)).**

- (a) *One datum.* At each moment the determining sequence is one region sequence (Lemma 3.1 (c): at a
  place and a level at most one standing drop-out is active), and the point carries one value on each
  row. So each edge of each tested plaquette has one datum value: a loop never has links from two data.
  The owner of a plaquette selects the supplier, not the values.
- (b) *The test reads the datum loop.* Let `T` be the test of a certificate of `p` at the moment `mu`, and
  let `R(e)` be the value that `T` reads on the edge `e` of `p`. If `e` is a row at `mu`, `R(e)` is the
  carried link, which is the datum value. If `e` is a completed edge at `mu`, the datum value is
  `M(V_{l-1})(e)`. A density test reads this average ((D6) of `cov-x`), or it reads a level-l variable
  `V_l(e)` that the term still carries together with its constraint `V_l(e) = M(V_{l-1})(e)`; the
  constraint holds at every point of an admitted trajectory (Definition 4.3 of `i3-cert`, (E1)), so
  `R(e) = M(V_{l-1})(e)`. This is Y 65419-65424: "These values agree with the fields in the tests by the
  retained averaging constraints." For a guard, the background has the averages of all rows of all
  levels at once ((D5) of `cov-x`), and (c3') is part of (COV-X*).
- (c) *A loop at the rim of a mark.* Let `(C, s)` stand and let `p` be a tested plaquette with a corner in C
  and a corner outside C. Then `p` has level `s`, all its corners are in `Omega_s`, and its certificate is
  the level-s density test of step `s`: the same ordinary datum on both sides of the rim.

*Proof of (c).* Let `x in C` and `y notin C` be corners of `p`, of level `l`. By Corollary 3.5, `l <= s`, so
`dist(x, y) <= L^s < a_s`. The point `y` is not in another component of `Z_s` (these are at distance at
least `a_s` from C, as in Lemma 3.1 (b)), so `y in Lambda_s subset Omega_s`; and `y notin Omega_{s+1}`, which is
at distance at least `M L^{s+1}` from `Z_s supset C` (R1). So `y in Lay_s`. The corners of `p` are in
`Lay_{l-1} cup Lay_l`, so `l >= s`, hence `l = s`. The corner `x` is within `L^s < 2 a_s` of `C^c`, so it is in
`C minus O_s(C)`, where `O_s(C)` is the old `Omega_s^c cap C`, two cells inside C. This set is in the member
of index `s` of the determining sequence: for an island the member contains C; for a drop-out it is the
old `Omega_s cap C = C minus O_s(C)`, or `C minus Z''_s(C)` with `Z''_s(C) subset O_s(C)` when `s` is an affected
level. So all corners are in `Omega_s`. By Theorem 5.1 the certificate of `p` is the one of its last fresh
move. That move is not a stage of C (`Fr_i(C)` has all corners in C), not a stage of a component that
contains C (its fresh plaquettes have level above its `h > s`, Lemma 3.1 (a)), not a main step with
outcome healed or island of a component that contains C (C would not stand), and not a move of a
component that does not contain C (its fresh plaquettes have all corners in it or an edge deep in it,
and it is disjoint from C; at level `s` it is at distance `a_s` from C). So it is step `s`. `square`

**How the cases of the row's (G4) come out.**

- *Footprint outside X with its collar.* Not fresh at any move of X (Lemma 4.1); carried.
- *Complete footprint in X.* Levels `l < h`: never fresh at a move of X before the main step; carried from
  the moment `nu_h` (this is case P1 of `cov-x`, which that note reduced to this row). Levels `l >= h`:
  carried, or fresh at a stage and then (COV-X*).
- *Footprint astride the rim of X.* The plaquette has level `t`, all corners in `Omega_t`, and is not fresh
  at any stage (`Fr_i(X)` has all corners in `O_{i+1}`) nor at the main step (no edge in the box). Its
  certificate is the top density test of step `t` on the complete exterior read, as Y 76666-76668. No
  bound at the bare rim is used (Y 64083-64086). See finding 1 for the removal rule.
- *An older mark in the floor of X.* By Lemma 3.1 (a) and Corollary 3.5 every tested plaquette with a corner
  in `C^{[2 L^m]}` has level below `h` and footprint in `O_h`; it is not fresh at any stage of X or at a
  stop. Its rows and the entries of the mark do not change (Lemma 4.1), and by Remark 4.1' and Lemma 3.2 no
  variable in the witness of the mark is written. "The core operation is at no point unfolded".
- *X healed.* All marks in X cease to stand (R4). After the move the tested plaquettes with a corner in X
  have level `t`: an edge in the box, the last test; no edge in the box, carried (from step `t` if a
  corner is in the old `Omega_t`; from the last stage otherwise, by (COV-X*) at `i = t - 1`, or by
  Remark 5.6).
- *X an island.* The same, with (S-core) in the place of the last test; the plaquettes between the box and
  the old `Omega_t` have the supplier of the last stage ("the newly made layer uses its own regularity
  guard", Y 76685-76687), which is (COV-X*) at `i = t - 1`.
- *X a drop-out after `n` stages.* No mark disappears. Nothing is fresh at the stop. Each tested plaquette
  with a corner in X has the certificate it had at the entrance of the unfinished stage: (S-ord) for the
  levels below `h` and above `h + n`, for level `h`, and for every plaquette with a corner in the old
  `Omega_t` or outside X; the supplier of (COV-X*) for the plaquettes of levels `h + 1, ..., h + n` made
  fresh by the `n` stages.

Remark 5.5 (against the table of the row). The theorem gives each tested plaquette one certificate of
the row's kinds; it does not give the row's rule for *which* kind in two situations. (i) A plaquette of
level `h` with footprint in the first shell `Z''_{h+1} minus O_h` of its owner has, by the invariant, the
density test of step `h`; the row's table gives the last stage test (case P3 of `cov-x` with `l = h`,
proved there at `N`). Both are suppliers. (ii) At a collar departure the invariant gives the supplier
from the entrance of the unfinished stage, not `chi_i^{(n+1)}` with the collar test (finding 2). In every
other situation the last fresh move decides the row of the table: a plaquette with an owner C whose
level is not in the affected levels of C, or that is not in `Fr_i(C)` for a completed stage, was last fresh
at a step and has (S-ord); a plaquette in `Fr_i(C)` has its footprint in the tested inset, or astride an
original wall (the seventh kind, which the row's table files under "the footprint leaves the stage test
region": the ordinary density test at the original cube).

Remark 5.6 (the healed outcome without (COV-X*) at the last stage; read, not part of the theorem). Y
supplies a healed component by two tests (Y 76692-76697): the final test on the six-cell inset, and "the
old top test enlarged by four cells", which "covers the outer six cells of the component". Read: the top
tests `chi_t(square)` are carried at the entrance `nu_{t-1}` of the last stage for the test cubes in
`Omega_t^{~4}` (Y 64096-64097, 76021-76023), and they read level-t loops whose non-row edges are one-step
averages. Then a level-t plaquette `p` with a corner in X after the healing has: a corner in
`X^{[-6 a_t]}`, and the final test bounds it; or a corner in the outer six cells
`X minus X^{[-6 a_t]} = (Omega_t cap X) cup (O_t minus O_t^{[-4 a_t]})`. In the first set, step `t`. In the
second, the top test at `nu_{t-1}` bounds the loop of averages, the promotion (m2) of the last stage gives
the rows these same values, and the plaquette is at distance at least `4 a_t` from the box
(`Lambda^pr subset H_t`, `O_t^{[-4 a_t]} = H_t^{[4 a_t]}`), so it is carried through the main step. This is a
coarse supplier of depth 0 at `nu_{t-1}`. For the island the region `H_t^{[4 a_t]} minus Lambda^pr` has no
such test (the last test fails), and the guard of the last stage is needed.

## 6. What stays open

1. **(COV-X*) at the instances of section 4.3**: the exterior position at a stage of level `i < t - 2`
   (needed for a drop-out that stops with `h + n = i + 1 < t - 1`), and the last stage `i = t - 1` (needed
   for the island, and for a drop-out at the extension test). Exact statement missing: for `p in Fr_i(X)`
   with no corner in `Z''_{i+1}`, the guard `chi_t^{(i+1-h)}` carried at `nu_{i+1}` has a clause region that
   contains `F(p)`, or `F(p)` is astride an original wall `dO_{l'}`, `k_0 < l' <= i + 1`, and the level-l'
   density tests supply it; for `i = t - 1` the guard is the last one, `chi_t^{(N_t)}`. Nearest lines:
   Y 63876 (the clause list), Y 77609-77704, and `library/cov-x.md` Lemmas 6.2, 6.4, 6.5. These are inside X
   and belong to row 628's scope; I did not attack them.
2. **The read statements.** F (five frame statements), (R-ord), (R-last), (R-core) are Y's prose turned into
   hypotheses. (R-core) is an estimate of Y (the extension by least action) with a constant `C(M)`; its
   exact form at the plaquettes astride the face of the box is my reading. (F-step) and (F-main) are
   stated at the level of loops ("conjugate"), because Y states them so (Y 76674-76676); a statement at the
   level of rows needs the support of each gauge draw.
3. **R1 to R5 for the operation of this lane.** For Y they are definitions and one ported proof (R5).
   `library/geoh.md` line 34 keeps "quarantine identification" outstanding for the revised operation; the
   window lemma uses the closed lower end (Remark 3.4).
4. Not checked by another model. Row 633 checks `library/cov-x.md`, on which the second line of the table
   of Theorem 5.1 rests.
