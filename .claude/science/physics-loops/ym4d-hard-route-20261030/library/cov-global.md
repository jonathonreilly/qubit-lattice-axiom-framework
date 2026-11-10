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
takes as input. By Lemma 3.0 and (R1) in that label, `c subset C subset Z_m subset Z_{h-1}`. So
`q in hat Z_{h-1}`, and (R2) gives `N_8(q) subset Omega_h^c` at the output of step `h`, which is `S'_h`.
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

*Proof.* By (R1) `dist(C, Omega_{m+1}) >= dist(Z_m, Omega_{m+1}) >= M L^{m+1}`, and the determining members
of index above `m` differ from the label only inside drop-outs of level above `m`, where they are smaller
complements of boxes that contain C's box by Lemma 3.1 (c) (the affected levels of such a drop-out C'
exceed `m'_flat > m`, and `Omega^det_l cap C' = C' minus Z''_l(C')` with `Z''_l(C') supset G_{m'_flat}(C') supset C`;
the distance from `G_{h'}` to the exterior of `Z''_{h'+1}` is at least `3 a_{h'+1}`, Y 63817-63818). So no
point within `2 L^m + L^{m+1} < M L^{m+1}` of C is in `Omega^det_{m+1}`. A tested plaquette of level
`l >= m + 1` has a corner in `Omega^det_l subset Omega^det_{m+1}`, and its corners are within `L^l` of each
other, on the level-l lattice. For `l = m + 1` this contradicts the distance. For `l > m + 1` the corner in
`C^{[2 L^m]}` would be outside `Omega^det_{l-1}`, against `corners subset Lay_{l-1} cup Lay_l`. So `l <= m`.
In X: `l <= m < h`; no corner of `p` is in `Omega^det_{l+1} cap X`, which contains `Omega_h cap X` and is a
union of level-l blocks, so `F(p) subset X minus Omega_h = O_h` (`library/cov-x.md` Lemma P, case P1, and
Lemma G (b)). `square`
