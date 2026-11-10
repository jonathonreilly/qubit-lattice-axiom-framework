lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T15:06Z

# cov-frames: the eight read statements of cov-global in the weak form (FINISH row 638)

Status: IN PROGRESS (started 2026-11-10T03:06Z; one session, Claude Fable 5.2, medium; not checked by
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
- (supp) `u = 1` on `Lay_{q-1}` and outside `Lay_{q-1} cup Lay_q`. [A level-q row can end in `Lay_{q-1}`, where
  the rows of level `q - 1` end too, and these do not move.]

Then: a tested plaquette of level `q` has the loop conjugated by `u` at its base corner; a tested
plaquette of any other level has the same loop.

*Proof.* Under (pin) and (supp) each row of level `!= q` has `u = 1` at both ends, and each row of level `q`
with no end in `supp u` too; so the move is a site-gauge move. Lemma 2.2. A tested plaquette of level
`l != q` has its corners in `Lay_{l-1} cup Lay_l`, at level-l sites; for `l > q` these are level-(q+1) sites
(pin); for `l < q` they are outside `Lay_q`, and those in `Lay_{q-1}` (when `l = q - 1`) have `u = 1` by
(supp). `square`

@@APPEND@@
