lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T15:06Z

# cov-frames: the eight read statements of cov-global in the weak form (FINISH row 638)

Status: DONE 2026-11-10 (one session, Claude Fable 5.2, medium; not checked by
another model; no numeric job was run; nothing here rests on a computation).

Queue row: FINISH 638. Pinned at commit ff474586e. Source: Sussman and Alpoge, `YM4_1400.tex` at commit
2bc0658f91d2 of the Yang--Mills-LLM-experiment repository; `Y n` is line n of that file.

Credit. The operation and all its moves (step, stages, collar gauge, extension test, central integration
with its fresh field, frame sum, tree gauge, reference law, last test), the two-slot rule at a refreshed
bond, the assignment of suppliers and the sentence "A gauge draw, a frame change or a tree gauge conjugates
the holonomy" are Sussman and Alpoge's (their text names Claude and Codex as authors): Y 4285-4366,
61973-62078, 62104-62180, 63836-63864, 65417-65474, 71488-71497, 72244-72260, 72678-72692, 75677-75704,
76003-76040, 76654-76701, 77741-77825, 78285-78296, 97525-97612. The step, the box minimiser and the trees
are Bałaban's (CMP 119 (1988) 243; CMP 122 (1989) 175, Proposition 1 and pp. 193-196). In this repository:
`library/cov-global.md` (Claude Fable 5.2; the invariant, the statements proved here are its hypotheses),
`library/cov-x.md` and `library/cov-xstar.md` (Claude Fable 5.2; (D1) to (D6), Lemma 5.1, Theorem 6.1, 6.2),
`library/i3-cert.md` (Definition T, Definitions 4.1 to 4.3, (AV2)), `library/rim-scale-check.md` ((I4) and
the constant), `library/prior/cov-frames-read.md` (gpt-6-luna; the map of the Y passages and the line
corrections).

Labels: **proved** (a written argument from the stated clauses), **read** (a clause of the definition of a
move in Y, with its lines; not rebuilt), **gap**.

## 0. Result

**Verdict.** Stop condition (i) for the eight statements, in the weak form, each **proved** from clauses
of the definition of its move that are **read** from Y and listed in section 3 (each with its lines) — with two changes to `cov-global`, and one move that `cov-global` does not list:

1. **The direction fails at one point: the set `B` of the main step.** The lead's row and `cov-global`
   take `B` = the level-t bonds with *both* ends in `Lambda^pr`. Y integrates and redraws `V_t` on the
   level-t bonds with *an* end in `Lambda^pr` (Y 71488: "a function of `V_k` on the level-k bonds having
   an end point in `Lambda^pr`"; Y 75680-75684: "Central integration has consumed the old box field,
   including the bonds crossing its boundary. The resulting term has unrestricted fresh Haar coordinates
   on the bonds with an end in the box"). So `B_main` is that larger set, and the fresh set (d) of
   Lemma 4.1 of `cov-global` grows from "an edge in the box" to **`B*(X)`: the level-t plaquettes with a
   corner in `Lambda^pr`**. The added plaquettes are those with exactly one corner in `Lambda^pr` (at the
   faces of codimension two). Each has its certificate: the last test (healed), the cutoff and the
   reference (island) (Lemma 5.2, Lemma 5.4). Every statement below is monotone in `B`, so it also holds
   under the "both ends" reading.
2. **(R-core) with the exterior bound that the invariant gives.** The exterior plaquettes that the
   proposition 'minimiser in a box' needs are in `Fr_{t-1}(X)`, position (Q2) of `cov-xstar`, in the
   region `E^{t-1}_0`; the invariant bounds them by `C_2'' e_t`, not by `C eps_t`. So the restored box
   has defect at most `(4 M_0 + 2 C(M) C_2'') e_t`, `e_t = R_t^2 eps_t`, under the ceiling
   `(4 M_0 + 2 C(M) C_2'') ebar(gamma) < a_Lambda`. Y states `C(M) eps_t` (Y 72692, 76684), from "the exterior
   bounds of the passed extendibility test"; I could not derive an exterior bound of order `eps_t` from
   the invariant (Remark 5.5). The consumers use `C e_l` only (`cov-xstar` finding 3).
3. **A sixth move: the late stop.** A component can leave *after* the central integration and the tree
   gauge, at the shell-field test or the last-shell test (Y 63836 (0), 75677-75686, 78285-78296). It is a
   drop-out with `n = N_t`. `cov-global` lists the stop only before the main step. At a late stop `B` is
   empty by the two-slot rule (the datum reads the old slot), and the weak frame statement is **reduced
   to one named statement on this move**, stop condition (iii):

   **(TG)** the tree gauge of the main step acts on the retained prepared datum as `u . V''` for one
   function `u` on the sites of the shells of `Lambda^pr` (level-q sites in the shell of level `q`), on
   every determining row with an end at such a site, the rows across the outer face of `Lambda^pr` and
   across the core face included (old slot).

   Given (TG), Lemma 2.2 conjugates every tested loop. Y asserts the conclusion (Y 76675-76677) and gives
   the structure (Y 63849, 4366); it does not state the action on the rows across the two faces. Without
   (TG) the plaquettes at stake are the tested plaquettes of levels `h, ..., t` with a corner in
   `Lambda^pr minus G_h`. For the outcomes healed and island (TG) is **not** needed (Lemma 4.4).

| Statement of `cov-global` | Weak form proved here | `B` | Place |
|---|---|---|---|
| (F-step) | tested plaquettes of level `< l - 1`: same loop; level `l - 1`: conjugate loop | empty | Lemma 4.1 |
| (F-stage), with (D3\*) | carried plaquettes: same loop; new rows get `M(V_i)`; no move of another component writes in X | empty | Lemma 4.2 |
| (F-stop), early | same loop | empty | Lemma 4.3 (a) |
| (F-stop), sharp collar split | level `j`: conjugate (or same) loop; other levels: same loop | empty | Lemma 4.3 (b) |
| late stop (not in `cov-global`) | conjugate loop, **given (TG)** | empty | Lemma 4.3 (c) |
| (F-refresh) | the datum reads the old slot; no tested plaquette and no test of a supplier reads the fresh slot while the mark stands | empty | Lemma 4.5 |
| (F-main) | level-t plaquettes with no corner in `Lambda^pr`: same loop | level-t bonds with an end in `Lambda^pr` | Lemma 4.4 |
| (R-ord) | each tested level-l plaquette at the output of step `l` has a corner in a carried test cube in `Omega_l`; defect `<= (2 pi / 3) eps_l < 2.1 eps_l` | | Lemma 5.1 |
| (R-last) | each plaquette of `B*(X)` has a corner in a test cube of `X^{~-6}`; defect `<= 2.1 eps_t` | | Lemma 5.2 |
| (R-core) | each plaquette of `B*(X)`: defect `<= (4 M_0 + 2 C(M) C_2'') e_t` | | Lemmas 5.3, 5.4 |

The fresh sets after (F2): (a), (b), (c) of Lemma 4.1 of `cov-global` are unchanged; (d) becomes `B*(X)`.
With these, Theorem 5.1 of `cov-global` holds with `B*(X)` in the place of `B(X)` and the constant of
item 2 in its last line (section 6).

What stays open: (TG) for the late stop; the clauses of section 3 are Y's definitions of the
moves, read and not rebuilt (among them (M-cut): the cutoff of the reference law holds on every bond of
`B_main`); the proposition 'minimiser in a box' is cited, not proved; a check by another model.

## 1. Repo search

- `grep -n -i "cov-frames\|frame statement\|F-main\|Haar refresh\|fresh slot\|old slot" library/open-core.md`:
  no entry. FINISH rows near this one: 632 (`cov-global`, states the eight statements as read), 635
  (`cov-xstar`, uses (D3\*), (F-stop), (F-main) as read), 636, 639 (checks), 637 (`cov-frames-read`, the
  reading map). Registry row COV names this row for the frame statements. No other row proves them.
- `grep -l -i "Haar refresh\|fresh slot\|box coins\|late stop\|central integration" library/*.md library/prior/*.md parts/*.md`:
  `library/prior/cov-read.md` line 74 (a reading of the refresh), `library/inset-chart.md` items 6, 8 (the
  final guard as preceding guard of the central integration; not the frame statements), `library/i3-cert.md`
  Definition 4.3 (the moves (m1) to (m5), where "every datum loop is conjugated" is part of the
  definition of a trajectory). No proof of a frame statement from the definitions of the moves, and no
  statement on the late stop or on the bonds across the face of the box.
- This checkout has the ref `origin/claude/ym4d-hard-route` only (`git branch -r`); `origin/main` and the
  other YM4D PR branches are not present, so I did not search them. `library/cov-global-check.md`,
  `library/cov-x-check.md`, `library/cov-xstar-check.md` are not present at this commit.

## 2. Setting, and the two algebra lemmas

Notation of `cov-global` section 2 and `cov-x` 2.1: X a class component of level `t`, window from `h`;
`a_q = M R_q L^q`, `u_q = M L^q`, `M >= 2` a power of `L` (Y 55275), `L >= 3`; boxes `H_q, O_q, G_q, Z''_q`,
`H = H_{k_0+1}`, `K_i = O_{i+1} minus Z''_{i+1}`; `Lambda^pr = Z''_t^{[u_t]} = H^{[4 u_t]}` (Y 63836 (1): "`Z''_k(X)`
enlarged by one more layer of `M`-cubes"); `C_h := G_h`, the core. The determining sequence, tested
plaquettes, row and completed edges, the datum loop `W(p)`: Definition T and Definition 4.1 of `i3-cert`,
as in `cov-global` 2.2. In particular (Definition T; Y 72270-72276, 65419-65424, 65455-65457):

- **(DB)** a completed edge `e` of level `l` has both ends in `Lay_{l-1}`; its two order-l blocks lie in
  `Lay_{l-1}`, all level-(l-1) bonds of these blocks are rows, and its value is `M(V_{l-1})(e)`.

Read from Y, on the averaging map:

- **(MC)** `M` is gauge covariant: if `V^u(b) = u(b_-) V(b) u(b_+)^{-1}` on the fine bonds of the double
  block of a coarse bond `c`, for a function `u` on the fine sites of that double block, then
  `M(V^u)(c) = u(c_-) M(V)(c) u(c_+)^{-1}` (Y 3573: "the two requirements ..., namely gauge covariance and
  agreement with the linear block average"; Y 5139: "The group mean and (QC3) are gauge covariant"; Y 4083).

`Sigma` is the set of points of the determining region with their finest level: a point `x in Lay_q` that
is a level-q site. A site of level `q + 1` in `Lay_q` is a level-q site, so both ends of every row and of
every completed edge are in `Sigma`.

**Definition 2.0 (the set `B` of a move; weak frame statement).** For a move between consecutive moments,
`B` is a set of bonds (each with its level). The *weak frame statement with `B`* is: every plaquette that
is tested before and after the move, with the same kind (row, completed) of each edge, and with no edge
in `B` and no completed edge whose double block contains a bond of `B`, has after the move a loop that is
a conjugate of its loop before. Then the fresh plaquettes of the move (Definition 4.0 of `cov-global`)
are among: the plaquettes that become tested or change the kind of an edge, and the tested plaquettes
with an edge in `B` (or a completed edge reading `B`).

**Lemma 2.1 (conjugation).** Let `p` be a plaquette with corners `x_1, ..., x_4` and edge values `V(e)`,
`V'(e)`. If there is a function `g` on the four corners with `V'(e) = g(e_-) V(e) g(e_+)^{-1}` for each
edge, then `W'(p) = g(x_1) W(p) g(x_1)^{-1}`, where `x_1` is the base corner of the loop.

*Proof.* In the ordered product of the four values (an edge traversed backwards enters with its inverse,
which transforms as `g(e_+) V(e)^{-1} g(e_-)^{-1}`) the inner factors `g(x_i)^{-1} g(x_i)` cancel. `square`

**Definition (site-gauge move).** A move is a *site-gauge move with `u : Sigma -> SU(2)`* if the
determining sequence does not change and every row `b`, of every level, changes from `V(b)` to
`u(b_-) V(b) u(b_+)^{-1}` (so a row with `u = 1` at both ends keeps its value).

**Lemma 2.2 (a site-gauge move conjugates every datum loop; proved from (DB), (MC)).** After a
site-gauge move with `u`, every tested plaquette `p` has `W'(p) = u(x_1) W(p) u(x_1)^{-1}`. If `u = 1` at the
corners of `p`, the loop is the same.

*Proof.* A row edge transforms with `u` at its ends, by definition. A completed edge `e` of level `l`: by
(DB) the level-(l-1) bonds of its double block are rows, with both ends in `Lay_{l-1}`, so each changes to
`u(b_-) V(b) u(b_+)^{-1}` with `u` on level-(l-1) sites of `Sigma`; (MC) gives
`M(V')(e) = u(e_-) M(V)(e) u(e_+)^{-1}`, and `e_+-` are in `Lay_{l-1}`, the same points of `Sigma`. Lemma 2.1
with `g = u`. `square`

**Corollary 2.3 (a block gauge at one level; where the pin is used).** Let `u` be a function on the
level-q sites, and let a move change every level-q bond `b` with an end in `supp u` to
`u(b_-) V(b) u(b_+)^{-1}` and no other row. It is a site-gauge move (with `u` extended by one) if

- (pin) `u = 1` at the level-(q+1) sites. [The rows of level `> q` end at such sites, and they do not move.]
- (supp) `u = 1` on `Lay_{q'}` for every `q' < q`. [A level-q row can end in `Lay_{q-1}`, where the rows of
  level `q - 1` end too, and these do not move.]

Then: a tested plaquette of level `q` has the loop conjugated by `u` at its base corner; a tested
plaquette of any other level has the same loop.

*Proof.* A row of level `> q` ends at level-(q+1) sites (pin). A row of level `q' < q` has its ends in
`Lay_{q'} cup Lay_{q'-1}` (supp). So each row of level `!= q` has `u = 1` at both ends, and each row of level
`q` with no end in `supp u` too: the move is a site-gauge move. Lemma 2.2. A tested plaquette of level
`l != q` has its corners in `Lay_{l-1} cup Lay_l`, at level-l sites; for `l > q` these are level-(q+1) sites
(pin); for `l < q` they are in layers of index below `q` (supp). `square`

## 3. The moves as Y defines them (read)

Each clause is a part of the definition of a move, with its lines. The proofs of sections 4 and 5 use
nothing else about the operation. A *write* of a move is a variable of the point whose value changes, or
that enters or leaves the point.

**Step `l`** (Y: step `t = k + 1`).

- (S-ent) The step adds the entries of index `l`; "the earlier entries and standing marks are copied"
  (Y 62174).
- (S-avg) It creates `V_l` with the delta `V_l = M(V_{l-1})` (Y 3653, 4288). The delta on a level-l bond is
  carried as long as the level-(l-1) variables of its double block are carried ((E1) of `i3-cert`; Y 62050
  (a): "the tests and averaging constraints that the term still carries"; Y 65419-65424).
- (S-gauge) The gauge draw is a function `u` on the level-(l-1) sites with `u = 1` at the level-l sites
  ("If `u = 1` on the coarse sites", Y 4358) and outside the blocks of the gauge region
  `(P_l'^{~1} cup hat Z_{l-1}^{~5})^c`, where `hat Z_{l-1}` is the hull of `Z_{l-1}` in level-l cells (Y 4285: "on
  the blocks `P''` that lie away from failures and from `Z_k`"; Y 97397-97399; Y 75602-75605: "The
  block-gauge draw is outside its five-layer enlargement"; for `l = 1`, Y 61979-61980). Every level-(l-1)
  bond `b` becomes `u(b_-) V_{l-1}(b) u(b_+)^{-1}` (Y 97401-97403).
- (S-int) The level-(l-1) bonds with an endpoint in `Omega_l` are integrated and leave the point (Y 4285).
- (S-else) The step writes no variable of level below `l - 1`, and no level-(l-1) variable other than by
  (S-gauge), (S-int) (Y 4288: the step is an integral over `V_{l-1}` of `rho_{l-1}(V_{l-1})` with the delta,
  the tests and the gauge factor; Y 62174).

**Stage of level `i` of X, `h <= i <= t - 1`.**

- (D1), (D2) of `library/cov-x.md` 2.2, with (m1), (m2), (m3) (Y 72244-72260, 64035-64036, 77767-77778).
- (G-collar) The collar gauge is a function `u` on the level-i sites, `u = 1` at the level-(i+1) sites ("the
  group is pinned at the next coarse sites", Y 77767) and outside the complete level-(i+1) blocks with
  centres in `K_i^- := O_{i+1}^{[-3 a_{i+1}]} minus Z''_{i+1}` (Y 97525-97528: "complete blocks with centres in
  `((Omega_{iota+1}^{~3})^c minus Z''_{iota+1}) cap X`"; Y 64119-64120). Every level-i bond with an end in
  these blocks becomes `u(b_-) V_i(b) u(b_+)^{-1}` ("The resulting incident links agree and the coarse
  centres are fixed", Y 97533-97534).
- (O-order) The operation of level `t` is performed after step `t` and before step `t + 1`. Each of its
  moves is a move of one class component; for one component the stages run in the order
  `i = h, ..., t - 1`, then the main step (Y 1169-1176; Y 63836 (1): "for `j = k_flat, ..., k - 1`, one value
  after another"). "Outside the class no entries change" (Y 62177); a component changes entries only
  inside itself ((R4) of `cov-global`).

**Tests and stops.**

- (P-test) A test is an indicator function of the variables that the point carries (Y 1146-1149).
  Making, completing, retaining or removing a test writes no variable (Y 77756-77758: "Remove an old
  indicator only when it equals one on the complete chart used for its removal"; Y 77778: "The later
  tests are weights on the resulting variables").
- (P-collar) Stage `n + 1`, `j = h + n`, has the order: regularity test, collar gauge, approximate test,
  completions, removals, sharp test (Y 77741-77763). If the sharp test fails, "the retained determining
  list still has index `n`" (Y 77793-77794). The retained variables are the gauged ones, or the
  untransformed ones (Y 97586-97587: "On a failure of the local sharp test, the stored prefix uses the
  untransformed real variables"); I prove the statement for both.
- (P-late) After the central integration and the tree gauge, the test on `B` and the last-shell test are
  made; "If one of the tests of (1)-(3) fails in a component, that component drops out" (Y 63857); "If a
  component leaves after the tree gauge, its frame sum stays with it" (Y 63836 (0)); Y 75677-75686,
  78285-78296. It is the drop-out of (R4) with `n = N_t`.

**Main step of X** (after `N_t` stages; `B_main` := the level-t bonds with an end in `Lambda^pr`).

- (M-int) Central integration: "`V_k` is integrated over `Lambda^pr`"; "Integrals against any bounded `F`
  that is independent of `V_k` on the box are left unchanged by it" (Y 63836 (3)). Its bonds are `B_main`
  (Y 71488, 75680-75684, quoted in section 0). The move writes a fresh Haar variable on each bond of
  `B_main` (Y 97596-97600: "the Haar refresh uses the box coins and keeps the old variables for the
  prepared datum"; Y 75063-75067).
- (M-slot) Two slots. After (M-int) a bond of `B_main` carries the old variable and the fresh one. A
  determining row at that bond reads the old slot: "A late Haar refresh leaves the old determining datum
  in the inner slot. The fresh field is used by the outgoing rows" (Y 76677-76679); "On a fresh slot used
  only by the next graph, a same-bond datum retained in the old determining set is a separate variable"
  (Y 76011-76013); "A retained row at a bond address shared by the fresh field still reads its old slot"
  (Y 76038-76039); Y 73172-73173.
- (M-tree) The frame sum selects a frame `r in W_4` for the component and writes no variable (Y 63836 (0):
  the objects of X "are formed in the frame `r`"). The tree gauge writes only old-slot variables `V''` on
  bonds of levels `h, ..., t` with an end in `Lambda^pr minus C_h` (Y 63838-63846: "the fluctuation bonds
  `B_0 = B'' cap (shells)`"; Y 63849; Y 75684: "Its frame tree acts on the old shell variables"). "The core
  operation ..., which contains the failed tests, is at no point unfolded" (Y 63849).
- (M-ref) Restoration (outcomes healed, island). The fresh variable on `B_main` is drawn from the
  reference law: `V_t(b) = V'(b) V_Lambda(b)`, with `V'` on the slice of the tree gauge `delta_ax` of the
  level-t sites of `Lambda^pr` (Y 63856, 72678-72686). **(M-cut)** `abs(log V'(b)) < M_0 eps_t` on every bond
  of `B_main` ("on the bonds of the box", Y 63856; "The cutoff in the subsequent draw restricts
  `V'_m = V_m V_Lambda^{-1}` to its reference ball. Its complement carries zero mass", Y 72682-72685).
  `V_Lambda` is the element of the critical orbit of the proposition 'minimiser in a box' (Y 71488) for
  the exterior values of the point; on a bond with no end in `Lambda^pr` put `V_Lambda(b) := V_t(b)`,
  `V'(b) := 1`. After the draw the datum of X reads the restored variable on `B_main`: "A reference-law
  draw changes the datum itself" (Y 76679-76680); "Where restoration replaces the field, the tests of the
  restored datum provide the new bound" (Y 65472-65474).
- (M-last) "The test of `chi_j(X^{~-6})` is made on the newly drawn field in the inset test cubes. Its full
  local test neighbourhoods stay in X" (Y 97609-97611). Healed: it passes; island: "only the last test
  fails, namely `chi_t` of the new field on X less a margin" (Y 62105-62106). Entries: (R4).
- (M-rev) The reverse tree gauge is a function `u` on the level-t sites of `Lambda^pr`; every level-t bond
  with an end there becomes `u(b_-) V_t(b) u(b_+)^{-1}` (Y 63856: a tree "that contains all the sites of this
  set"; Y 4366: "a unique `u` satisfies `(u . V)|_T = V_0`"; Y 76698-76699).
- (M-else) The main step writes no other variable.

**The density tests.**

- (T-cube) In bare units the level-l test cubes have side `L w_l`, `w_l := M_2 R_l L^l`, and their
  enlargement layers have width `w_l` (Y 62410-62411, 63165-63166; Y 62001 says "side of order `M_2 R_t`").
  `M_2` is a power of `L` with `L^2 M_2 <= M` (Y 62001); I assume the floor `M_2 >= L`. They are the cubes of
  the partition of that side on the grid of the cells ("Because it is a power of `L`, all partitions are
  nested", Y 62001; Y 643-648; "The density cube and the footprint are taken in the prescribed
  partitions of the test", Y 77812-77813).
- (T-dens) `chi_l(square) = 1` at a point if and only if the local background `U = U_{l,square}(V_l)` exists
  and `norm(dU(q) - 1) < eps_l L^{-2l}` for every bare plaquette `q subset square^~` (Y 1149-1151,
  61976-61978, 134115-134116). `U` is a bare configuration with `M^l U = V_l` on the level-l bonds with
  both ends in `square^{~4}`, and it depends on no other variable (Y 62405-62407; Y 134117-134119: "since
  the localized orbit has the prescribed `V_k` there").
- (T-carried) "After the step, the tests that stand outside the integral operations are exactly
  `chi_{t,S} = prod_{square subset Omega_t} chi_t(square)`" (Y 62050 (c)).

## 4. The frame statements (F1)

**Lemma 4.1 (F-step; proved from (S-ent), (S-gauge), (S-int), (S-else), (DB), (MC)).** At step `l`, `B` is
empty. A tested plaquette of level `q < l - 1` after the step was tested before, with the same loop. A
tested plaquette of level `l - 1` after the step was tested before, with the same kind of each edge, and
its loop is conjugated by `u` at its base corner. So the fresh plaquettes are the tested plaquettes of
level `l`: (a) of Lemma 4.1 of `cov-global`.

*Proof.* The members of index `< l` do not change (S-ent), and before the step there is no member of
index `l`. Level `q < l - 1`: the status and the edge kinds read the members `q - 1, q, q + 1`, and the
values read rows of level `q` and `q - 1 < l - 1`, which are not written (S-else). Level `l - 1`: after the
step `p` has a corner in `Omega^det_{l-1}` and none in `Omega_l`; so it was tested before. An edge of `p`
that touches `Omega^det_{l-1}` has no end in `Omega_l`, so it is a row before and after; an edge with both
ends in `Lay_{l-2}` is completed before and after. The rows of level `l - 1` that remain are moved by
(S-gauge) only ((S-int) removes rows, (S-else)). I check Corollary 2.3 with `q = l - 1` for the sequence
after the step. (pin): (S-gauge). (supp): `supp u` lies outside `hat Z_{l-1}^{~5} supset Z_{l-1}`. Now
`Lay^det_{q'} subset Z_{l-1}` for `q' <= l - 2`: outside the standing drop-outs the sequence is the label and
`Omega_{q'} minus Omega_{q'+1} subset Omega_{l-1}^c subset Z_{l-1}` (`Lambda_{l-1} subset Omega_{l-1}`); a
standing drop-out `C` of level `s <= l - 1` lies in `Z_s subset Z_{l-1}` (Lemma 3.0 of `cov-global`, (R1)).
Every level-(l-1) row with an end in `supp u` is moved by `u` (S-gauge). Corollary 2.3. `square`

**Lemma 4.2 (F-stage and (D3\*); proved from (D1), (D2), (G-collar), (O-order), (MC), and the write sets of
this section).** Let `h <= i <= t - 1`.

- (a) Every bond that the collar gauge of the stage moves is integrated by (m3) of the same stage. So at
  the exit `nu_{i+1}` the variables with support in X that changed since `nu_i` are the new rows, with
  `V_{i+1}(c) = M(V_i)(c)`, the average being the same before and after the collar gauge. `B` is empty, and
  Lemma 5.1 of `cov-x` (Lemma 2.1 of `cov-xstar`) holds for every `i`: a plaquette of level `<= i` tested
  after the stage was tested before with the same four edge values. With Lemma 4.1 (b) of `cov-global`:
  the fresh plaquettes are in `Fr_i(X)`.
- (b) **(D3\*).** Between `nu_h` and `nu_t`, and until the end of the main step of X, no move of another
  structure writes a variable on a bond with an endpoint in X or changes an entry inside X.

*Proof.* (a) `K_i` is a union of aligned level-(i+1) blocks (`cov-x` 2.1), so a block with centre in
`K_i^-` lies in `K_i`, and a moved bond has an endpoint in `K_i`. Its other end is within `L^i` of that
block, which is at distance at least `3 a_{i+1} - L^{i+1}/2 > L^i` from `X minus O_{i+1} = A^i_{i+1}`. So the bond
has an endpoint in `K_i` and none in `A^i_{i+1}`: it is in the set of (m3). The average `M(V_i)(c)` on a new
row: by (MC) the collar gauge changes it to `u(c_-) M(V_i)(c) u(c_+)^{-1}`, and `u = 1` at the level-(i+1)
sites `c_+-` (Y 77767-77768: "so the coarse row remains fixed"). The rest is the proof of Lemma 5.1 of
`cov-x`, which uses (D1), (D2) and (b).

(b) By (O-order) every move between `nu_h` and the end of the main step of X is a move of a class
component of the operation of level `t`. Let `X' != X` be one. Its writes: a stage writes bonds with an
endpoint in `K_i(X')` (collar gauge, (m3)) and new rows with both ends in `O_{i+1}(X')` ((D1), (D2)); a stop
writes nothing more ((P-test), (P-collar), (P-late)); the main step writes bonds with an end in
`Lambda^pr(X')` and variables of the core operation ((M-int) to (M-else)). `K_i subset O_{i+1} subset O_t`
and `Lambda^pr subset O_{k_0+1} subset O_t` ((B1), (B3) of `cov-x`, and `O_i subset G_i subset H_{i+1} subset O_{i+1}`
for `i <= k_0`). So every written bond has an end in `O_t(X') = X'^{[-2 a_t]}`, and both ends within
`L^t < 2 a_t` of it, in `X'`. `X cap X'` is empty. Entries: (O-order). `square`

**Lemma 4.3 (F-stop; (a), (b) proved from (P-test), (P-collar), (G-collar), (R4); (c) given (TG)).** At a
stop of X the determining sequence does not change ((R4): the sequence of a component with `n` completed
stages is the sequence (R21) with `nu = n`), and `B` is empty.

- (a) *Early stop* (the regularity test of stage `n + 1` fails, or the extension test (2) fails after
  `N_t` stages). No variable is written. Every tested plaquette has the same loop.
- (b) *Sharp collar split*, `j = h + n`. A tested plaquette of level `j` has its loop conjugated by the
  collar gauge `u` at its base corner (the same loop if no corner is in `supp u`, or if the untransformed
  variables are retained). A tested plaquette of any other level has the same loop. The tests that the
  retained list gains write no variable.
- (c) *Late stop.* The central integration changes no determining row (M-slot); the frame selection
  writes nothing; given (TG) the tree gauge conjugates every tested loop; the tests write nothing.

*Proof.* (a) (P-test): "At this stop the central integration is still pending. The old top values and the
bare averaging chain in the core keep their original places" (Y 78249-78253).

(b) Before the stop the unfinished stage has made tests and the collar gauge (P-collar). The sequence is
`A^j` of (D1). I check Corollary 2.3 with `q = j`. (pin): (G-collar). (supp): `supp u subset K_j subset X`, which does
not meet `Z''_{j+1}`; and inside X the layers of index below `j` lie in `Z''_j subset Z''_{j+1}` for `j > h`, in
`O_h subset Z''_{h+1}` for `j = h` ((D1), (B1)); `K_j subset Lay^j_j`. A level-j bond with an end in `supp u` touches `A^j_j` (which contains
`X minus Z''_{j+1}`) and has no end in `A^j_{j+1} = X minus O_{j+1}` (proof of Lemma 4.2 (a)), so it is a row, and
it is moved by `u` (G-collar). Corollary 2.3. For a tested plaquette of level `j + 1` this can be seen
without the pin: its completed edges have their ends within `L^{j+1}` of a corner in `X minus O_{j+1}`, their
double blocks within `3 L^{j+1}/2` of it, and `supp u` is at distance at least `3 a_{j+1} - L^{j+1}/2 > 3 L^{j+1}/2 + L^j`
from it. The gained tests: (P-test).

(c) (M-slot), (M-tree), (P-test); (TG) says that the tree gauge is a site-gauge move; Lemma 2.2. `square`

**Lemma 4.4 (F-main, outcomes healed and island; proved from (M-int) to (M-else), (R4); (TG) is not
used).** `B = B_main`.

- (a) After the move no plaquette of level below `t` with a corner in X is tested, and no tested
  plaquette of level below `t` has a footprint that meets X; the other tested plaquettes of level below
  `t` have the same loop.
- (b) A level-t plaquette that is tested after the move and has no corner in `Lambda^pr` was tested
  before, all its edges are rows before and after, and its loop is the same.
- (c) The level-t plaquettes with a corner in `Lambda^pr` are the set `B*(X)`; they are the fresh
  plaquettes of the move. For `p in B*(X)` the loop after the move is a conjugate of the loop at the
  point after the draw (M-ref), where the last test (M-last) is made.

*Proof.* (a) Lemma 4.1 (d) of `cov-global`, first part, as written there. (b) No edge of `p` has an end in
`Lambda^pr`. Each corner is in `X minus Lambda^pr subset X minus Z''_t = A^t_t`, or outside X, and then in
`Omega_t` (proof of Lemma 4.1 (d) of `cov-global`); so the edges are rows before, and after (X is in the top
member). Every write of the main step is on a bond with an end in `Lambda^pr` or in the core operation
((M-int), (M-tree), (M-ref), (M-rev), (M-else)). So the four values are the same. (c) A plaquette with a
corner in `Lambda^pr` has two edges in `B_main`. After (M-ref) all four edges of a level-t plaquette with a
corner in X are rows; (M-rev) changes each by `u` at its ends (`u = 1` at sites outside `Lambda^pr`);
Lemma 2.1. `square`

**Lemma 4.5 (F-refresh; proved from (M-slot), (R1), Lemma 3.0 of `cov-global`).**

- (a) The central integration changes no determining row and no entry: `B` is empty, and every tested
  plaquette has the same loop.
- (b) Let X stand as a late drop-out of level `t` (or let the moment be between (M-int) and (M-ref)). A
  tested plaquette of level `l <= t` reads, on a bond of `B_main`, the old slot. A tested plaquette `p` of
  level `l > t` has `dist(F(p), X) >= L^l / 2 > L^t`, so neither its loop nor a density test whose cube
  contains a corner of it reads through a double block that contains a bond of `B_main`.
- (c) The fresh slot is read by the level-(t+1) variables that step `t + 1` writes (Y 75698-75704); by (b)
  none of them is an edge value of a tested plaquette while X stands.

*Proof.* (a) (M-slot). (b) Level `l <= t`: (M-slot), and by (DB) a completed edge reads rows. Level `l > t`:
`p` has a corner `y in Omega^det_l`. `X subset Z_t subset Z_{l-1}` (Lemma 3.0 of `cov-global`, (R1)), and
`dist(Z_{l-1}, Omega^det_l) >= M L^l` ((R1) for the determining sequence, as in Corollary 3.5 of `cov-global`).
Every point of `F(p)` is within `3 L^l / 2` of `y` (Lemma G of `cov-x`). So
`dist(F(p), X) >= (M - 3/2) L^l >= L^l / 2 >= L^{t+1} / 2 > L^t`. The bonds of `B_main` have both ends within `L^t`
of `Lambda^pr subset X`. The edges of `p` and their double blocks lie in `F(p)`. (c) follows. `square`

## 5. The tests (F3), (F4), (F5)

**Lemma 5.1 ((R-ord), (F3); proved from (T-cube), (T-dens), (T-carried), (AV2), (E1)).** Let `p` be a tested
plaquette of level `l` at the output of step `l`, on an admitted trajectory, and let
`(pi / 3) eps_l <= alpha_L`. Then:

- (i) `p` has a corner `x in Omega_l`, and `x` lies in exactly one level-l test cube `square`; `square subset Omega_l`.
- (ii) `chi_l(square)` is carried at the output of the step, so it equals one.
- (iii) `F(p) subset square^~`, and the four edges of `p` have both ends in `square^~`. The test reads: the level-l
  variables on the bonds with both ends in `square^{~4}`, through `U_{l,square}`; and it bounds the bare
  plaquettes of `square^~`. So the test of `square` reads every edge of every level-l plaquette with a corner
  in `square`, and bounds the bare plaquettes of its whole footprint.
- (iv) `(U_{l,square}, chi_l(square))` at the output of the step is a bare supplier of `p` (Definition 3.1 of
  `cov-x`) with allowance `(pi / 3) eps_l`, and `norm(W(p) - 1) <= (2 pi / 3) eps_l < 2.1 eps_l`.

*Proof.* (i) At the level `l` the determining member is the label member (the affected levels of a
standing drop-out of level `s < l` are at most `s`). `Omega_l` is a union of level-l cells (R1). The cell
side `M R_l L^l` is a multiple of the cube side `L M_2 R_l L^l` (`M` and `M_2` are powers of `L` and
`L^2 M_2 <= M`), so by (T-cube) each cell is partitioned into test cubes. (ii) (T-carried). (iii) Every
point of `F(p)` is within `3 L^l / 2` of `x` (Lemma G), and `w_l >= L . L^l >= 3 L^l` by the floor `M_2 >= L`.
(T-dens). (iv) By (T-dens), `norm(dU(q) - 1) < eps_l L^{-2l}` on the bare plaquettes of `F(p)`; for a unitary
matrix with `norm(e^{iF} - 1) <= 1` one has `abs(F) <= (pi / 3) norm(e^{iF} - 1)`, so
`eps(U; F(p)) <= (pi / 3) eps_l L^{-2l}`: (c1). (AV2) gives `abs(F_p(M^l U)) <= 2 (pi / 3) eps_l`. By (T-dens),
`(M^l U)(e) = V_l(e)` on the four edges. On a row edge `V_l(e)` is the datum value. On a completed edge the
datum value is `M(V_{l-1})(e)`, and `V_l(e) = M(V_{l-1})(e)` by the delta of (S-avg), which is carried because
the level-(l-1) rows of its double block are carried (Lemma 5.3 (b) of `cov-global`): (c2'), (c3'). `square`

Remark 5.1' (answers to (F3)). *The constant in place of 2.1* is `2 pi / 3`; the factor 2 is (AV2), the
factor `pi / 3` converts the chord norm of the test to the angle of (AV2). Y states `2 eps_k` (Y 134117).
`library/rim-scale-check.md` line 61 has the same account. *Part (a) of the lemma at Y 62050* is not
needed: every tested plaquette of level `l`, with all corners in `Omega_l` or not, has a corner in a cube
inside `Omega_l` by the partition. What (a) gives is another statement: at the output of step `l + 1` the
level-l tests on `Omega_{l+1}^~` equal one, so they are implied and may be removed there; a supplier does
not need the test to remain (finding 1 of `cov-global`). *The partition* is the one clause of (R-ord) that
Y does not state in one sentence; (T-cube) gives its three sources. The weak form that the proof uses is:
every level-l site of `Omega_l` lies in a test cube contained in `Omega_l`.

**Lemma 5.2 ((R-last), (F4); proved from (M-last), (T-cube), (T-dens), (AV2), Lemma 4.4).** Let X be healed
and `p in B*(X)`. Then a corner of `p` lies in a level-t test cube `square subset X^{~-6} = X^{[-6 a_t]}`, the
last test of `square` equals one on the newly drawn field, and after the main step
`norm(W(p) - 1) <= (2 pi / 3) eps_t`.

*Proof.* The inclusion, in the notation of `cov-x` 2.1 (`G_{i-1} subset H_i`, `G_i = H_i^{[10 a_i]}`,
`a_{k_0+1} = u_t`, `k_0 + 2 <= t`, `X = G_t`):

`Lambda^pr = H^{[4 u_t]} subset H^{[10 u_t]} = G_{k_0+1} subset H_{k_0+2} subset ... subset H_t subset H_t^{[4 a_t]} = G_t^{[-6 a_t]} = X^{[-6 a_t]}`.

X is a union of level-t cells, so `X^{[-6 a_t]}` is one, and by (T-cube) the corner `x in Lambda^pr` of `p`
lies in a test cube `square subset X^{[-6 a_t]}`. (M-last): the test of `square` is made on the newly drawn field and
passes. After (M-ref) all four edges of `p` are rows with the values `V_t` that the test reads. Parts
(iii), (iv) of Lemma 5.1 give the bound at the point after the draw; Lemma 4.4 (c) carries it through the
reverse tree gauge. `square`

So the last test on the six-cell inset reads every plaquette of `B*(X)`, the added ones included. The
other level-t plaquettes with a corner in X are carried (Lemma 4.4 (b)), as in Theorem 5.1 of `cov-global`.

**Lemma 5.3 (the exterior of the box; proved from Theorems 6.1, 6.2 of `cov-xstar`, Lemma 4.2, Lemma 4.3
(a), (M-int), (M-slot), (M-tree)).** Let `Ext(X)` be the set of level-t plaquettes with no corner in
`Lambda^pr` and all corners within `L^t` of `Lambda^pr` (within distance 1 in level-t units). At the point
before the draw (M-ref):

- (a) every `p in Ext(X)` is in `Fr_{t-1}(X)`, in position (Q2) of `cov-xstar` with the region
  `E^{t-1}_0 = O_{k_0+1} minus Z''_{t-1}`, all its edges are rows with no end in `Lambda^pr`, and
  `norm(W(p) - 1) <= C_2'' e_t`;
- (b) every level-t plaquette with a corner in X and no corner in `Lambda^pr` has
  `norm(W(p) - 1) <= max(2.1 eps_t, C_2'' e_t) = C_2'' e_t`.

*Proof.* (a) The corners are in `H^{[4 u_t + L^t]} minus H^{[4 u_t]}`, inside `O_{k_0+1} = H^{[8 u_t]} subset O_t` and
outside `Z''_t = H^{[3 u_t]}`: all corners in `O_t`, all in `K_{t-1} = O_t minus Z''_t`. So `p in Fr_{t-1}(X)` with no
corner in `Z''_t`. `F(p)` is within `3 L^t / 2` of a corner, so `F(p) subset H^{[4 u_t + 5 L^t / 2]} subset O_{k_0+1}`
(`5/2 <= 4 M`), and `F(p)` does not meet `Z''_t supset Z''_{t-1}` (Lemma G (b)): `F(p) subset E^{t-1}_0`, position (Q2).
Theorem 6.1 of `cov-xstar` gives the bound at `x_{nu_t}`. Between `nu_t` and the draw the moves are the
extension test (no write), the central integration (writes fresh slots on `B_main`; no edge of `p` is in
`B_main`), the frame selection and the tree gauge (writes on bonds with an end in `Lambda^pr`). So the
loop of `p` is the same. (b) Such a plaquette is tested at `nu_t` (a corner in `X minus Z''_t = A^t_t`).
Theorem 6.2 of `cov-xstar` at the exit `nu_t`: all corners in `O_t`, case (a), the bound `C_2'' e_t`; a
corner in `Omega_t cap X` (or outside X), (S-ord), Lemma 5.1. Then as in (a). `square`

**Lemma 5.4 ((R-core), (F5); proved from (M-ref), (M-cut), Lemma 5.3 and the proposition 'minimiser in a
box', which is cited and not proved).** Let the main step of X have the outcome island (or healed), and
let `(4 M_0 + 2 C(M) C_2'') ebar(gamma) < a_Lambda`. Then after the main step every `p in B*(X)` has

`norm(W(p) - 1) <= (4 M_0 + 2 C(M) C_2'') e_t`.

*Proof.* The proposition (Y 71488-71491), in the form used: *if the exterior data satisfy
`norm(dV_t(q) - 1) < eps` on the plaquettes `q in Ext(X)` and `C(M) eps <= a_Lambda`, then the critical
orbit `V_Lambda` satisfies `norm(dV_Lambda(p) - 1) <= C(M) eps` on every level-t plaquette `p` all of whose
corners lie within `L^t` of `Lambda^pr`.* A plaquette with a corner in `Lambda^pr` has all corners within
`L^t` of it, so the bound holds on `B*(X)`. Take `eps := 2 C_2'' e_t`; Lemma 5.3 (a) gives the hypothesis.
Let `p in B*(X)`, with edges `b_1, ..., b_4`. After (M-ref) all are rows with `V_t(b_i) = V'(b_i) V_Lambda(b_i)`,
where `V'(b_i) = 1` if `b_i` has no end in `Lambda^pr`, and `norm(V'(b_i) - 1) <= abs(log V'(b_i)) < M_0 eps_t`
otherwise (M-cut). Replace `V'(b_1), ..., V'(b_4)` by 1 one at a time; the other factors are unitary, so
`norm(W(p) - V_Lambda(dp)) < 4 M_0 eps_t`. So `norm(W(p) - 1) < 4 M_0 eps_t + 2 C(M) C_2'' e_t`, and `eps_t <= e_t`.
In particular the drawn field is in the class of continuations of the proposition. Lemma 4.4 (c) carries
the bound through the reverse tree gauge. `square`

Remark 5.5 (what the hypothesis of the proposition needs, and Y's constant). (i) *Which exterior
plaquettes.* The proposition says "the exterior data satisfy `abs(dV_k - 1) < eps`" and fixes the class by
the plaquettes "whose corners all lie within distance 1 of `Lambda^pr`". In the narrow reading the
exterior plaquettes are `Ext(X)`; their certificate is the guard `chi_t^{(t-1-h)}` at `nu_{t-1}`, the supplier
(Q2) of the last stage ("the newly made layer uses its own regularity guard", Y 76685-76687). In the wide
reading they are all level-t plaquettes with a corner in X and no corner in `Lambda^pr`; Lemma 5.3 (b)
gives each the same bound: (Q1) to (Q3) of the last stage for corners in `O_t`, the top density test of
step `t` for a corner in `Omega_t` ("the surrounding density cubes", Y 76682-76683). The existence of the
localized background `U_{t,X}` is part of the proposition and is not examined here. (ii) *The constant.* Y
has `C(M) eps_i` (Y 76684) and "the plaquette bound at `V_Lambda` is `C eps_m`" (Y 72692). That needs
exterior data of order `eps_t` on `Ext(X)`. The invariant gives `C_2'' e_t`: in (Q2) the threshold of the
guard has the factor `L_flat^{2(t-k_0-2)}` and the supplier lemma the factor `L^2`. The passed extension test
(2) gives an extension with curvature below `2 eps_t` on the plaquettes that contain a bond of the
extension; it is not a bound on the exterior plaquettes. I found no statement in Y that bounds `Ext(X)`
by `C eps_t`. The bound `C e_t` is what the consumers use (Y 65481-65484: "each test gives a bound `C e_l`
directly"); only Y's remark that `psi_l` is `O(1)` at a restored core (Y 65477-65478) is not recovered.
(iii) (M-cut) is the one reading on which the added plaquettes of `B*(X)` depend: if the cutoff held
only on the bonds with both ends in `Lambda^pr` while the draw wrote the crossing bonds too, a plaquette
with one corner in `Lambda^pr` would have no bound. Y 72682-72686 excludes that ("There is no failure
event for that cutoff on the free Haar argument").

## 6. Comparison with Lemma 4.1 of cov-global (F2), and the carrying of cov-xstar

| Move | `B` | Fresh set of `cov-global` 4.1 | After this row |
|---|---|---|---|
| step `l` | empty | (a) the tested plaquettes of level `l` | the same |
| stage of level `i` | empty | (b) `Fr_i(X)` | the same |
| stop, early or collar | empty | (c) none | the same |
| late stop | empty | not listed | none, given (TG) |
| central integration (refresh) | empty (old slot) | (c) none | the same |
| restoration, healed or island | `B_main`: level-t bonds with an end in `Lambda^pr` | (d) `B(X)`: an edge with both ends in `Lambda^pr` | `B*(X)`: a corner in `Lambda^pr` |

`B*(X) minus B(X)` is the set of level-t plaquettes with exactly one corner in `Lambda^pr` (if two corners
are in the box, either they span an edge, or they are diagonal and then all four are in the box).
Certificates of the added plaquettes: healed, the last test (Lemma 5.2); island, the cutoff and the
reference (Lemma 5.4); this is Y 65472-65474. In Theorem 5.1 of `cov-global` read `B*(X)` for `B(X)`,
"a corner in `Lambda^pr`" for "an edge in the box" in its table and in "How the cases come out", and
`(4 M_0 + 2 C(M) C_2'') e_t` for `(4 M_0 + C(M)) eps_t`. Its proof of the healed case already uses only a
corner in `Lambda^pr`. Lemma 5.3 (c) there (the rim of a mark) is not affected: `B*(X)` is deep in X.

**The carrying of `cov-xstar` section 6 (X5).** The weak forms are enough, with one change of wording and
one condition.

- At the extension stop: Lemma 4.3 (a), the same loop.
- At the main step: a plaquette of `Fr_{t-1}(X)` with **no corner in `Lambda^pr`** is tested before and
  after with the same loop (Lemma 4.4 (b)); `cov-xstar` says "no edge in the box". A plaquette of
  `Fr_{t-1}(X)` with a corner in `Lambda^pr` is in `B*(X)` and has (R-last) or (R-core).
- At a late stop (not treated in `cov-xstar`): the plaquettes of `Fr_i(X)`, `h <= i <= t - 1`, with no corner
  in `Lambda^pr` keep the same loop (the tree gauge writes only bonds with an end in `Lambda^pr`, (M-tree));
  those with a corner in `Lambda^pr minus C_h` need (TG).
- (D3\*): Lemma 4.2 (b). It holds up to the end of the main step.

## 7. Table (F6), corrections, what stays open

| Statement | Weak form | Proof place | Y lines of the clauses |
|---|---|---|---|
| (F-step) | level `< l - 1` same loop, level `l - 1` conjugate; fresh: level `l` | Lemma 4.1 | 62174; 4285, 4288, 4358-4363; 97397-97403; 75602-75605; 61979-61980 |
| (F-stage), (D3\*) | carried plaquettes same loop; collar gauge moves only removed bonds; no write from another component | Lemma 4.2 | 72244-72260; 77767-77778; 97525-97534; 64119-64120; 63836 (1); 62177 |
| (F-stop) early | same loop | Lemma 4.3 (a) | 1146-1149; 63857; 78249-78253 |
| (F-stop) collar split | level `j` conjugate by the collar gauge, others same; gained tests write nothing | Lemma 4.3 (b) | 77741-77763; 77793-77808; 97586-97587 |
| late stop | conjugate, given (TG) | Lemma 4.3 (c) | 63836 (0); 63849; 75677-75686; 78285-78296; 4366 |
| (F-refresh) | old slot is the datum; fresh slot read by no tested plaquette | Lemma 4.5 | 97596-97600; 76677-76679; 76011-76013; 76038-76039; 73172-73173; 75698-75704 |
| (F-main) | no corner in `Lambda^pr`: same loop; `B*(X)` fresh | Lemma 4.4 | 63836 (3); 71488; 75680-75684; 63856; 72678-72686; 76698-76699 |
| (R-ord) | corner in a carried cube of `Omega_l`; `(2 pi / 3) eps_l` | Lemma 5.1 | 62001; 62410-62411; 63165-63166; 62050 (c); 1149-1151; 62405-62407; 134113-134120 |
| (R-last) | `B*(X)` read by the last test on `X^{~-6}` | Lemma 5.2 | 97609-97611; 62105-62106; 76692-76697 |
| (R-core) | `B*(X)`: `(4 M_0 + 2 C(M) C_2'') e_t` | Lemmas 5.3, 5.4 | 71488-71491; 63856; 72682-72692; 76680-76687 |

Line corrections to `cov-global` (those of `library/prior/cov-frames-read.md` section 6 hold; I add):
(F-main) "the level-t bonds with both ends in `Lambda^pr`" should be "with an end in `Lambda^pr`"
(Y 71488, 75680-75684); (R-last) is Y 97609-97611, which has the quantifier that the reading did not find
("the inset test cubes"); (R-ord) the cube side is Y 62410-62411 and 63165-63166; (F-refresh) the two
slots are Y 76011-76013, 76038-76039.

**Open.**

1. **(TG)**, for the late stop only (section 0, item 3). Exact statement missing: the tree gauge of
   Y 63849 moves every determining row with an end at a shell site by the site factors, the rows across
   the outer face of `Lambda^pr` and the core face included. Nearest lines: Y 63849 ("the tree of a shell
   uses up the gauge freedom at every site of the shell except one ... one external bond crossing its
   boundary is added"), Y 4366, Y 76675-76677, Y 78318-78322. Not in `library/open-core.md`.
2. The clauses of section 3 are definitions of Y in prose, read and not rebuilt. The ones a checker
   should look at first: (M-int) with `B_main` (an end, not both ends), (M-slot), (M-cut), (S-gauge)
   (the support of the step's gauge draw), (T-cube) with the floor `M_2 >= L`.
3. The proposition 'minimiser in a box' is cited; its hypothesis is used with `eps = 2 C_2'' e_t`, and
   the ceiling `(4 M_0 + 2 C(M) C_2'') ebar(gamma) < a_Lambda` is added to the ceilings on `gamma`.
4. (MC), (DB), (AV2), (E1): read, with the lines given; Theorems 6.1, 6.2 of `cov-xstar` are used in
   Lemma 5.3 and are not checked (row 639).
5. Not checked by another model.

For the lead (I edited no other file):

1. `library/cov-global.md`: 4.1 (F-main) and Lemma 4.1 (d): `B*(X)` (a corner in `Lambda^pr`); Theorem 5.1,
   fourth line of the table: `(4 M_0 + 2 C(M) C_2'') e_t`; (F-stop): the wording "no row changes" is false
   at a collar split with the gauged variables retained (the level-j rows in the collar move by the
   gauge), the weak form holds; add the late stop as a move.
2. `library/cov-xstar.md` section 6 (X5), "Carrying": "no edge in the box" should be "no corner in
   `Lambda^pr`"; the late stop needs (TG).
3. Registry row COV: the uncovered case that it cites at Y 78316-78319 (a lower footprint at a seam of an
   earlier shell) stands in Y's paragraph "The tests retained at a late stop" (Y 78285-78322), the move
   of (TG). I did not examine that case.

RESULT: the eight read statements of cov-global are proved in the weak form from the clauses that define each move in Y (section 3): B is empty at a step, a stage, a stop and the refresh, and at the restoration B is the set of level-t bonds with an end in Lambda^pr (not both ends, so the direction fails there and the fresh set (d) grows to the level-t plaquettes with a corner in Lambda^pr, each with its certificate from the last test or from the cutoff and the reference); (D3*) is proved up to the end of the main step; (R-ord) holds with the constant 2 pi / 3, (R-last) from Y 97609-97611, (R-core) with the bound (4 M_0 + 2 C(M) C_2'') e_t instead of Y's C(M) eps_t. Open: (TG), the action of the tree gauge on the rows across the faces of the shells, needed only at a late stop (a drop-out after the central integration, a move cov-global does not list); the clauses of section 3 and the proposition 'minimiser in a box' are read or cited, not rebuilt; no check by another model.
