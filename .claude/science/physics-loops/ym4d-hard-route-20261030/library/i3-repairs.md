lead: anthropic/claude-opus-5-5/medium mac-mini-worker
lease_until: 2026-11-10T16:54Z

# i3-repairs (FINISH row 634): text repairs to `library/i3-cert.md`

Status: DONE 2026-11-10 (repairs listed; i3-cert.md not edited, see section "What is proved").

Provenance: Claude Opus 5.5, medium effort, Mac mini worker 2, one session, at commit 01af230c4. No
numerics, no subagents. Inputs: `library/i3-cert.md` (Claude Fable 5.2, row 624), `library/cov-x.md`
sections 0, 3 and 8 (Claude Fable 5.2, row 628), `library/i3-cert-check.md` (row 630) and
`library/cov-x-check.md` (row 633), both Claude Opus 5.5. The underlying argument is Sussman and
Alpoge's (`YM4_1400.tex` at 2bc0658f91d2, their text names Claude and Codex as authors), paragraph
`hi:prepared-real-endpoint` (Y 65406-65591); the nest and the stage test are Bałaban's (CMP 122).

Repo search: `library/open-core.md` has no entry for i3-cert or i3-repairs. This row attacks no open lemma.

**How the repairs are delivered.** The row says to edit `library/i3-cert.md`. The worker instruction for
this session forbids editing any file other than this one (and new lemma files). That instruction wins,
so `i3-cert.md` is **not edited**. Each repair below is given as section, old sentence (verbatim from
i3-cert at 01af230c4) and new sentence, ready for the lead to apply by exact replacement. "APPLY" means
the repair fits the text and the check accepts it; "NOT APPLIED" gives the reason.

**Inputs present / absent.**
- `library/cov-x-check.md`: present. Accepts edits 1, 2 and 4 of cov-x section 8 as stated, and edit 3
  with (d2): `C_2'` also in (H5). Also states (d1) for Lemma 6.
- `library/i3-cert-check.md`: present. Its repair list is in "What stays open", last paragraph.
- `library/cov-xstar-check.md` (row 639): **absent**. So the `C_2'' = max(C_2, 6 . 4^r L^2)` change of
  `library/cov-xstar.md` is **not applied**; the repairs below use `C_2' = max(C_2, 6 . 4^r)`, the form
  that cov-x-check accepts. If row 639 accepts `C_2''`, replace `C_2'` by `C_2''` in repairs A3-A5 and
  in the head line, and nothing else.

## 0. Summary

| Id | Source | Where in i3-cert | Verdict |
|---|---|---|---|
| A1 | cov-x edit 1 (accepted, cov-x-check item 11.1; i3-cert-check item 12.1) | Def. 5.1 (s1); 5.4 (c1)-(c3); Cor. 5.2 proof | APPLY (text below) |
| A2 | cov-x edit 2 (accepted, cov-x-check item 11.2; i3-cert-check item 12.2) | 5.4 items 3, 5; section 0 finding 2; 10 items 1-2; 9.2 | APPLY |
| A3 | cov-x edit 3 + cov-x-check (d2) (i3-cert-check item 12.3-12.4) | table 5.2, (5.1), 5.4 item 4 and new item 7, Lemma 2b, Cor. 5.2, (H5), `C_3`, 9.2 | APPLY with `C_2' = max(C_2, 6 . 4^r)` |
| A4 | cov-x edit 4 (accepted, cov-x-check item 11.4) | Lemma 4 case A | APPLY |
| A5 | row 634 addendum (cov-xstar, `C_2''`) | - | NOT APPLIED: `library/cov-xstar-check.md` absent |
| B1 | i3-cert-check item 4 (Lemma 4.1) | 2.3 status paragraph | APPLY |
| B2 | i3-cert-check item 2 (Lemma 1', (H4)) | section 4 after Lemma 1; (H4) | APPLY |
| B3 | i3-cert-check item 1 ((m6), fail factors) | Def. 4.3 | APPLY |
| B4 | i3-cert-check item 8 + cov-x-check (d1) | Lemma 6; remarks in 5.4 item 6 and 7.3 | APPLY (one definition serving both) |
| B5 | i3-cert-check item 6 (`L >= 13`, floors of Y 35270) | (G1) | APPLY |
| B6 | i3-cert-check item 5 ((K-x), (K-col)) | table 5.2 | APPLY ((K-col) labelled unproved, as the check labels it) |
| B7 | i3-cert-check item 10 ((H5) additions 1, 2) | (H5), 9.2 | APPLY |
| B8 | i3-cert-check item 10 addition 3 (rename `c_0`) | throughout | NOT APPLIED (reason in B8) |
| B9 | i3-cert-check item 3 (F2 cite) | Lemma F2 | APPLY |
| B10 | i3-cert-check item 5 ((K-ext) for `l < j`), item 6 (`R_mat` to `r_U` closed), item 11 (inset-chart wording) | - | NOT APPLIED: not in the check's repair list / other file |
| H | row 634 | head of i3-cert | head line given in section H |

Conventions below: "Old" is quoted verbatim from `library/i3-cert.md` at 01af230c4 (line numbers given);
"New" is the replacement. Where only a fragment changes in a long line, the old fragment is quoted
(each is unique in the file; I checked with grep) and replaced in place. Nothing else in i3-cert changes.
`C_2'` is a new symbol; `C_2` keeps its definition `2^{r+1} L L_flat^2 A_L`.

## A1. (c2) to (c2'), and the edge form of (s1) (cov-x section 8 edit 1)

Accepted form: cov-x-check item 11.1 ("Needed ... Enough: Lemma 3.2 gives the bound at `x_N` directly
from (c2') and (AV2)"); i3-cert-check item 12.1. The form is `library/cov-x.md` Definition 3.1 and
Lemma 3.2. (c2') comes with (c3') in that definition, because at the supplier's moment of case P4 the
plaquette is not a tested plaquette of `D(x_nu)` (cov-x-check 11.1), so the old (c3) clause "satisfies
(s1) for the datum `D(x_nu)`" has no meaning there.

**A1.1, section 5.1, Definition 5.1 (lines 299-300).**
Old: "- (s1) `(M^l U)(c) = V_l(c)` on every row edge `c` of `p`, and `M^{l-1} U = V_{l-1}` on every level-(l-1)
  bond of the double block of every completed edge of `p`;"
New: "- (s1) `(M^l U)(c) = V(c)` for each of the four edges `c` of `p`, where `V(c) := V_l(c)` on a row edge
  and `V(c) := M(V_{l-1})(c)` on a completed edge (edge form, `library/cov-x.md` section 3). The bondwise
  form `M^{l-1} U = V_{l-1}` on the double blocks implies it and is not required; it can fail for (K-ord)
  at a mixed loop (`library/cov-x.md` finding 4);"

(The proof of Lemma 2 reads unchanged: its first clause becomes redundant, and its conclusion
`V(dp) = (M^l U)(dp)` is (s1) itself.)

**A1.2, section 5.4, (COV), bullet (c2) (lines 376-377).**
Old: "- (c2) `p` is a tested plaquette of `D(x_nu')` for every `nu <= nu' <= N`, and its datum loop at `x_nu'`
  is a conjugate of its datum loop at `x_nu` (only moves (m1), (m4) touch its edges, or none);"
New: "- (c2') `(M^l U)(c) = V(c)` at `x_N` for each of the four edges `c` of `p` (`V(c)` as in (s1)); for a
  coarse supplier of depth `d = l - l'` (a configuration `W` on the level-l' bonds of `F(p)`),
  `(M^d W)(c) = V(c)` at `x_N` (`library/cov-x.md` Definition 3.1). The plaquette need not be a tested
  plaquette of `D(x_nu)`;"

**A1.3, section 5.4, (COV), bullet (c3) (lines 378-379).**
Old: "- (c3) `U` is the background that `T` reads at `x_nu` (or, for (K-col), the reconstructed field), and it
  satisfies (s1) for the datum `D(x_nu)`."
New: "- (c3') `U` is the restriction to `F(p)` of the configuration that `T` reads at `x_nu` (or, for (K-col),
  the reconstructed field); for a coarse supplier, `W` is the level-l' datum at `x_nu`."

**A1.4, section 5.4, proof of Corollary 5.2 (lines 387-388).**
Old: "*Proof.* Lemma 2 at the moment `nu` with the supplier of (c1), (c3) gives defect `<= 2 psi_l eps_l` at
`x_nu`. By (c2) the defect at `x_N` is the same number. Lemma 2b. `square`"
New: "*Proof.* By (c2') the datum loop of `p` at `x_N` is `(M^l U)(dp)`, or `(M^d W)(dp)` for a coarse
supplier. (AV2) with (c1) gives defect `<= 2 psi_l eps_l` at `x_N`; for a coarse supplier, (AV2) on the
level-l' lattice at depth `d` (`library/cov-x.md` Lemma 3.2). Lemma 2b. `square`"

**A1.5, section 5.4, after Corollary 5.2 (lines 390-391), fragment.**
Old: "The constant in Corollary 5.2 is `C_2` at every entrance. The proof passes a *value* from the moment `nu` to
`N` by (c2);"
New: "The constant in Corollary 5.2 is `C_2'` at every entrance. The proof passes a *value* from the moment `nu` to
`N` by (c2');"

**A1.6, section 9.2 (line 729), fragment.**
Old: "to the present by (c2)."  New: "to the present by (c2')."

Proof-assistant form of the step A1 relies on: for each edge `c`, `V(c)|_{x_N} = (M^l U)(c)` (c2'); the
loop is the ordered product of the four edge values; so `V(dp)|_{x_N} = (M^l U)(dp)`; (AV2) applied to `U`
under `eps(U; F(p)) <= alpha L^{-2l}`, `alpha <= alpha_L` gives `abs(F_p(M^l U)) <= 2 alpha`; and
`norm(e^{iF} - 1) <= abs(F)`. Each is a named hypothesis or a one-line identity.

## A2. One supplier for items 3 and 5: the guard before the promotion (cov-x section 8 edit 2)

Accepted form: cov-x-check item 11.2 ("Needed: in the default operation T9 has no clause astride
`dZ''_j` or the earlier faces (Y 64370-64373, 64384, 64435) ... Enough: Lemma 6.3 works in both
operations"); i3-cert-check items 5 ((K-x) not carried at the entrance) and 12.2. Constant of the
supplier: cov-x table, case P4, `psi_l = sqrt(2) c_0 L^2 L_flat^{2(l-k_0-2)_+}` (defect
`2 sqrt(2) c_0 L^2 L_flat^{2(l-k_0-2)_+} eps_l`), inside (5.1) with `e <= (l - k_0)_+`.

**A2.1, section 5.4, item 3 (lines 427-429).**
Old: "3. A seam loop at the last prepared face `dZ''_j`: footprint in the last shell, astride the face, and in
   the exterior; the shell clause, the crossing clause and the exterior clause of T9, at `nu = N`, with
   Lemma 2a. (c3): `U^-` has the old datum."
New: "3. A loop at the last prepared face `dZ''_j`. Footprint wholly in the last shell: the shell clause of
   T9 at `nu = N`. Wholly in the exterior: item 4 (or item 7 at an original wall). With a corner in `Z''_j` and the footprint astride the face (case P4 of
   `library/cov-x.md`, `l = j`): the exterior clause of the preceding guard `chi_m^{(j-1-h)}` at the
   entrance `nu_{j-1}` of the stage of level `j - 1`, before the promotion (`library/cov-x.md` Lemma 6.3;
   Y 77621-77645), with (c2'), (c3') and `psi_j = sqrt(2) c_0 L^2 L_flat^{2(j-k_0-2)_+}`. No crossing
   clause is used: in the default operation T9 has none (Y 64278, 64371-64373)."

**A2.2, section 5.4, item 5 (lines 432-440).**
Old: "5. A seam loop at an earlier face `dZ''_{i+1}`, `i + 1 < j`. If the operation carries the crossings (T3),
   T9 contains the clause, at `nu = N`. In the default operation T9 has no clause on the bare plaquettes
   astride that face; this is case (c) above. The supplier is then the stage test of the stage of level
   `i`, at the moment `nu` just after that stage: its shell clause (inside), its crossing clause (astride),
   its exterior clause (outside), with Lemma 2a, and `U^{(.)}` of that stage has the datum of that moment.
   (c2): the rows of the loop lie within `L^{i+1}` of the face, inside the shells of levels `i` and `i+1`,
   whose widths are at least `u_{i+1} = M L^{i+1}` (Y 63846-63851); later stages change rows of level
   above `i + 1` only, and "all holonomies below level `j` are unchanged" (Y 65522-65523).
   Lemma 1 is what makes that earlier test available at `x_N`."
New: "5. A seam loop at an earlier face `dZ''_{i+1}`, `h <= i`, `i + 1 < j`, with a corner in `Z''_{i+1}`
   (case P4 of `library/cov-x.md`, `l = i + 1`). In the default operation T9 has no clause on the bare
   plaquettes astride that face; this is case (c) above. The supplier is the same as in item 3: the
   exterior clause of the preceding guard `chi_m^{(i-h)}` at the entrance `nu_i` of the stage of level
   `i`, before the promotion. The whole footprint lies in one exterior region of that guard, inside the
   layer of index `i`, and the loop at `x_N` is the level-(i+1) plaquette of the averages of that guard's
   background ((c2'), (c3'); `library/cov-x.md` Lemma 6.3; Y 77557-77589, 77609-77645), with
   `psi_{i+1} = sqrt(2) c_0 L^2 L_flat^{2(i-k_0-1)_+}`. The stage test just after the stage is not used:
   its clause `kappa_x` astride the face exists only in the split with added crossing tests
   (Y 64384-64386). Lemma 1 is what makes the earlier guard available at `x_N`."

**A2.3, section 0, finding 2 (lines 44-45), fragment.**
Old: "The repair is the stage test of the
   stage that prepared that face, used at its own moment, with the loop unchanged since (5.4, item 5)."
New: "The repair is the exterior clause of the preceding guard at the entrance of the stage of level `i`,
   before the promotion, used at its own moment, with (c2') (5.4, items 3 and 5; `library/cov-x.md`
   Lemma 6.3, checked in `library/cov-x-check.md`). The stage test after the stage has no crossing clause in
   the default operation."

**A2.4, section 10, item 1 (lines 744-749), two fragments.**
Old: "supplier of one of the six kinds, with complete footprint (c1), unchanged loop since the test's moment
   (c2), and the right averages (c3)."
New: "supplier of one of the seven kinds (with (K-wall)), with complete footprint (c1), the loop at `x_N`
   equal to the loop the supplier bounds (c2'), and the right averages (c3')."
Old: "the repair I propose is the earlier stage test plus (c2), unproved."
New: "the repair is the preceding guard at the entrance of the earlier stage, with (c2') (`library/cov-x.md`
   Lemma 6.3; HOLDS in `library/cov-x-check.md`)."

**A2.5, section 10, item 2 (lines 754-755), fragment.**
Old: "for the
   first, the stage test of the stage that prepared the face bounds the same loop."
New: "for the
   first, the preceding guard at the entrance of the stage of level `i` bounds the same loop
   (`library/cov-x.md` Lemma 6.3)."

**A2.6, section 9.2 (line 731), fragment.**
Old: "positive stage test of the stage that made it (items 3, 4, 5 of the list in 5.4), which gives `C_2` again."
New: "retained test of the kind that supplies it (items 3, 4, 5 and 7 of the list in 5.4), which gives `C_2'` again."

**Flag, not applied: (E2) of Definition 4.2 (lines 243-245).** It lists "the deep exterior (crossing)
clause at the last prepared face". cov-x-check 11.2 observes that the crossing clause (E2) cites is the
optional `kappa_x` of the final inset split (Y 64308-64313), and cov-x-check item 2 reads the deep
exterior clause as a containment clause (Y 64223-64228, 64278). Neither check states a repair to (E2),
so the text is not changed. With A2 no step reads a crossing clause, so (E2) is harmless for Theorem
9.1; the lead may drop the word "(crossing)".

## A3. The seventh kind (K-wall), and `C_2'` (cov-x section 8 edit 3, with cov-x-check (d2))

Accepted form: cov-x-check item 11.3 ("Needed ... Not enough as written: see (d2), the ceiling (H5)
with `C_2'`") and (d2); i3-cert-check items 12.3, 12.4 ("`C_2' = max(C_2, 6 . 4^r)`: HOLDS, provided it
is used in (H5) as well (both conditions)"), and its finding that no step uses the spare factor `1/R_l`.
The supplier is `library/cov-x.md` Lemma 6.4 (a coarse supplier, Lemma 3.2): defect `<= 6 . 4^r e_j` for
`d = j - l' >= 1`, `<= 2.1 eps_j` for `d = 0`. Then `psi_j := 3 . 4^r R_j^2` gives `2 psi_j eps_j = 6 . 4^r e_j`.

**A3.1, section 5.2, table: new row after (K-core) (after line 334).**
New: "| (K-wall) | original density tests of level `l'` at the wall `dO_{l'}`, `k_0 < l' <= j`, carried at the entrance `nu_{l'}` of the stage of level `l'` (Y 64697-64716, 77673-77686); coarse supplier of depth `d = j - l'` (`library/cov-x.md` Definition 3.1, Lemma 6.4; Y 77647-77704) | `abs(F_q) <= 2.1 eps_{l'}` on the level-l' plaquettes of `F(p)`, i.e. allowance `alpha = 3 . 4^r e_j` at depth `d >= 1` | `3 . 4^r R_j^2` (level `j` only); not within (5.1) |"

**A3.2, section 5.2, before (5.1) (line 337), fragment.**
Old: "which costs the factor `sqrt(2) L^2`. So in every kind"
New: "which costs the factor `sqrt(2) L^2`. So in every kind except (K-wall)"

**A3.3, section 5.2, after (5.1) (after line 341), new sentence.**
New: "For (K-wall), `psi_j = 3 . 4^r R_j^2` is of order `(log theta_j)^{2r}`, not `<= C R_j`; (5.1) fails there.
It enters only through Lemma 2b below, as `2 psi_j eps_j = 6 . 4^r e_j` (`library/cov-x.md` finding 3)."

**A3.4, section 5.3, Lemma 2b (lines 345-347).**
Old: "**Lemma 2b.** Assume (FR), (T1), (T3), (LF), and (5.1). Then `2 psi_l eps_l <= C_2 e_l / R_l <= C_2 e_l` with

`C_2 := 2^{r+1} L L_flat^2 A_L`."
New: "**Lemma 2b.** Assume (FR), (T1), (T3), (LF), and (5.1) for the kinds other than (K-wall). Then for those
kinds `2 psi_l eps_l <= C_2 e_l / R_l <= C_2 e_l`, and for every kind, (K-wall) included,
`2 psi_l eps_l <= C_2' e_l`, with

`C_2 := 2^{r+1} L L_flat^2 A_L`,  `C_2' := max(C_2, 6 . 4^r)`."

**A3.5, section 5.3, proof of Lemma 2b (lines 352-353).**
Old: "*Proof.* If `l <= k_0` then `e = 0` and `psi_l <= A_L`. If `k_0 < l <= k`, Lemma F3 gives
`L_flat^{2e} eps_l <= 2^r L L_flat^2 e_l / R_l`. `square`"
New: "*Proof.* If `l <= k_0` then `e = 0` and `psi_l <= A_L`. If `k_0 < l <= k`, Lemma F3 gives
`L_flat^{2e} eps_l <= 2^r L L_flat^2 e_l / R_l`. For (K-wall), `2 psi_j eps_j = 6 . 4^r R_j^2 eps_j = 6 . 4^r e_j`;
for `d = 0` its defect is `2.1 eps_j <= 2 c_0 eps_j <= C_2 e_j`. Both bounds are at most `C_2' e_l`. `square`"

(Check of the last inequality: `2.1 < pi = 2 c_0`, `A_L >= c_0`, `R_j >= 1`, so `2 c_0 eps_j <= C_2 e_j`.)

**A3.6, section 5.3 (line 365).**
Old: "For (s2) one needs `alpha = psi_l eps_l <= C_2 ebar(gamma) <= alpha_L`: a ceiling on `gamma`."
New: "For (s2) one needs `alpha = psi_l eps_l <= C_2' ebar(gamma) <= alpha_L`: a ceiling on `gamma`. For
(K-wall) the allowance is `3 . 4^r e_j <= C_2' ebar(gamma)`."

**A3.7, section 5.4, (COV) bullet (c1) (lines 374-375).**
Old: "- (c1) `F(p)` lies in the set where `T` gives its bare bound, so (s2) holds with `alpha = psi_l eps_l`,
  `psi_l` as in (5.1);"
New: "- (c1) `F(p)` lies in the set where `T` gives its bare bound, so (s2) holds with `alpha = psi_l eps_l`,
  `psi_l` as in (5.1); for (K-wall), in the coarse form `abs(F_q(W)) <= alpha L^{-2d}` for every level-l'
  plaquette `q` with corners in `F(p)`, `alpha = 3 . 4^r e_j` (`library/cov-x.md` Definition 3.1);"

**A3.8, section 5.4, item 4 of the list inside `X` (lines 430-431).**
Old: "4. Level `j`, footprint in the exterior `(Omega_m^c minus Z''_j) cap X`: the exterior clauses of T9, at
   `nu = N`. This covers the collar `K`. No use of T6."
New: "4. Level `j`, footprint in one exterior region of T9 inside `(Omega_m^c minus Z''_j) cap X` (case P5a of
   `library/cov-x.md`): the exterior clauses of T9, at `nu = N`. A footprint in `K` astride an original
   wall is item 7. No use of T6."

**A3.9, section 5.4, new item 7 after item 6 (after line 443).**
New: "7. Level `j`, footprint astride an original wall `dO_{l'}`, `k_0 < l' <= j`, inside the exterior (case P5b
   of `library/cov-x.md`; these walls lie in `K` and no clause of T9 reads them, Y 77647-77704): (K-wall),
   the level-l' density tests at `nu_{l'}` and the exact averages of depth `j - l'`
   (`library/cov-x.md` Lemma 6.4). Defect `<= 6 . 4^r e_j`, or `<= 2.1 eps_j` if `l' = j`."

**A3.10, section 5.4, Corollary 5.2 statement (lines 384-385).**
Old: "**Corollary 5.2 (base bound; proved from Lemma 2, 2b, given (COV)).** At every `x_N in Ent_N`, every
tested plaquette of level `l` of the old global datum `D(x_N)` has defect at most `C_2 e_l`."
New: "**Corollary 5.2 (base bound; proved from (AV2) and Lemma 2b, given (COV)).** At every `x_N in Ent_N`, every
tested plaquette of level `l` of the old global datum `D(x_N)` has defect at most `C_2' e_l`."

**A3.11, `C_2` to `C_2'` where the base constant is meant (fragments; each old fragment is unique).**

| Line | Section | Old | New |
|---|---|---|---|
| 28 | 0, table | "Lemma 2b: `2 psi_l eps_l <= C_2 e_l`." | "Lemma 2b: `2 psi_l eps_l <= C_2' e_l`, `C_2' = max(C_2, 6 . 4^r)`." |
| 30 | 0, table | "`C_3 = 2 c_0 L^2 C_F(1) C_2`." | "`C_3 = 2 c_0 L^2 C_F(1) C_2'`." |
| 32 | 0, table | "restarted at `C_2` at every entrance" | "restarted at `C_2'` at every entrance" |
| 343 | 5.3 heading | "### 5.3 The bound `C_2 e_l`, and" | "### 5.3 The bound `C_2' e_l`, and" |
| 530 | 6.3 | "Lemma 3 is used once for the old sequence (`B = C_2`)" | "Lemma 3 is used once for the old sequence (`B = C_2'`)" |
| 539 | 7, Lemma 4 | "`C_3 := 2 c_0 L^2 C_F(1) C_2`," | "`C_3 := 2 c_0 L^2 C_F(1) C_2'`," |
| 541 | 7, proof | "*Proof.* `C_3 >= C_2`." | "*Proof.* `C_3 >= C_2'`." |
| 582 | Remark 7.2 | "(Lemma 3 with `B = C_2`)" | "(Lemma 3 with `B = C_2'`)" |
| 583 | Remark 7.2 | "`c_0 K_w K_F C_2 e_j L^{-2j}`" and "`abs(F_P) <= 2 L^2 c_0 K_w K_F C_2 e_j`" | same with `C_2'` |
| 585 | Remark 7.2 | "`2 c_0 L^2 K_w K_F C_F(1) C_2`." | "`2 c_0 L^2 K_w K_F C_F(1) C_2'`." |
| 688 | 9.1, (H5) | see B7 | see B7 |
| 700 | 9.1, proof | "the base bound `C_2 e_l` for the old datum" | "the base bound `C_2' e_l` for the old datum" |
| 709 | 9.2, table | new row after the `C_2` row | "\| `C_2'` \| `max(C_2, 6 . 4^r)` \| `C_2, r` \| Lemma 2b; (K-wall) \|" |
| 710 | 9.2, table | "\| `C_3` \| `2 c_0 L^2 C_F(1) C_2` \|" | "\| `C_3` \| `2 c_0 L^2 C_F(1) C_2'` \|" |
| 724 | 9.2 | "`tests --(Lemma 2, 2b)--> C_2 --(Lemma 4)-->" | "`tests --(Lemma 2, 2b)--> C_2' --(Lemma 4)-->" |
| 726 | 9.2 | "the chain starts again at `C_2`, because" | "the chain starts again at `C_2'`, because" |
| 735 | 9.2 | "`(2 c_0 L^2 C_F(1))^N C_2`" | "`(2 c_0 L^2 C_F(1))^N C_2'`" |

Lines 345-349 (definition of `C_2` and its dependence) keep `C_2`; line 365 is A3.6; lines 536, 556,
561 are A4.

## A4. Case A of Lemma 4 with `C_2'` (cov-x section 8 edit 4)

Accepted form: cov-x-check item 11.4 ("`D(P)` for `P` in `K` near a wall contains level-j plaquettes of
case P5b ... Enough, together with (d2)"). The P5b plaquettes of the stencil are old tested plaquettes
(corners in `Lay_j`), so the text of case A stands with the constant changed.

**A4.1, section 7, Lemma 4 hypothesis (line 536), fragment.**
Old: "Let `gamma` be so small that `c_0 C_2 ebar(gamma) <= min(eps_L, L^2/C_L)`."
New: "Let `gamma` be so small that `c_0 C_2' ebar(gamma) <= min(eps_L, L^2/C_L)` and `C_2' ebar(gamma) <= 1`."

**A4.2, section 7, case A (line 556), fragment.**
Old: "by Corollary 5.2 and 2.3, `eps(W; D(P)) <= c_0 C_2 e_j`."
New: "by Corollary 5.2 and 2.3, `eps(W; D(P)) <= c_0 C_2' e_j` (this includes the plaquettes of `D(P)` astride
an original wall, item 7 of 5.4)."

**A4.3, section 7, case A (line 561).**
Old: "`abs(F_P) <= L^2 c_0 C_2 e_j + C_L (c_0 C_2 e_j)^2 <= 2 L^2 c_0 C_2 e_j <= 2 L^2 c_0 C_2 C_F(1) e_q`."
New: "`abs(F_P) <= L^2 c_0 C_2' e_j + C_L (c_0 C_2' e_j)^2 <= 2 L^2 c_0 C_2' e_j <= 2 L^2 c_0 C_2' C_F(1) e_q`."

Step check: the second inequality uses `C_L c_0 C_2' e_j <= L^2`, which is the hypothesis A4.1 with
`e_j <= ebar(gamma)` (Lemma F4); the conversion `abs(F) <= c_0 . defect` uses defect `<= C_2' e_j <= 1`
(the added clause, i3-cert-check item 10 addition 2); the third uses Lemma F1 with `n = 1`.

## A5. `C_2''` of `library/cov-xstar.md` (row 634 addendum) — NOT APPLIED

`library/cov-xstar-check.md` (row 639) is not present in this checkout at 01af230c4, so, as the row
says, nothing from cov-xstar is applied. If row 639 accepts it, the change is mechanical: write
`C_2'' = max(C_2, 6 . 4^r L^2)` for `C_2'` in A3.4 (definition), A3.11 and A4, in (H5) (B7), and in the
head line; the (K-wall) row of A3.1 then needs the `psi_t <= 3 . 4^r L^2 R_t^2` that cov-xstar states.

## B1. The local averaging estimate: Lemma 4.1 of i3-cert-check (item 4)

**B1.1, section 2.3, status paragraph (lines 130-133).**
Old: "Status: Y states both for a whole lattice with the global maximum. The local forms hold because `M^l U` on
the four edges of `p` reads `U` only in `F(p)`, and the proof of the corollary (Y 4927-4948) is a
recurrence on the maxima over the nested stencils of `p`. I read the proofs; I did not rebuild them."
New: "Status: Y states both for a whole lattice with the global maximum. Y's proof of the one-step bound reads
curvature on a box `D_C` with an extra layer (Y 4800-4803, 4815-4816), so the fact that `M^l U` on the four
edges of `p` reads `U` only in `F(p)` gives the values, not the estimate. The local form of the estimate
is Lemma 2.3a.

**Lemma 2.3a (the one-step chart fits in the footprint; `library/i3-cert-check.md` Lemma 4.1).** For a
coarse plaquette `C`, the box `F(C)` (the union of the four corner blocks, a lattice box) can serve as
`D_C` in Y 4800-4880.

*Proof.* Each contour path of an edge `c = (y, y + L e_mu)` of `C` is a shortest path from `y` to
`x in B(y)`, the straight segment from `x` to `x + L e_mu in B(y + L e_mu)`, and a shortest path back to
`y + L e_mu`; a shortest lattice path lies in the coordinate box of its ends, so every path lies in
`F(C)`. Root the coordinate comb at the initial vertex of `C`; each comb path is coordinatewise
monotone, so it lies in `F(C)`. In the loop "comb path, edge `b`, comb path back", each interchange of
two consecutive unit steps replaces one vertex by the fourth corner of a unit square whose other three
corners are on the path; that corner has each coordinate equal to a coordinate of those three, so it
stays in the box, and so does the inserted plaquette. Hence the integers `n_{b,p}` of Y 4830-4834 are
supported on plaquettes of `F(C)`, and every quantity in Y 4806-4871 is read in `F(C)`. `square`

So (AV1) holds with `D(p) = F(p)` read on the level-(l-1) lattice. For (AV2), put
`eps_t(p) := max abs(F_q(M^t U))` over the level-t plaquettes `q` with all corners in `F(p)`; the blocks
are aligned and nested (Y 62001), so for such `q` at level `t + 1` the box `F(q)` is a union of order-(t+1)
blocks inside `F(p)`, and Lemma 2.3a gives the one-step bound for it. Y's recurrence
`eps_{t+1} <= L^2 eps_t (1 + C_L eps_t / L^2)` and its induction (Y 4927-4948) then run word for word, with
the constant 2. I read Y's proofs of (AV1), (AV2); apart from the localisation, I did not rebuild them."

## B2. Lemma 1 in measure form, and (H4) (i3-cert-check item 2)

**B2.1, section 4, new lemma after the proof of Lemma 1 (after line 283).**
New: "**Lemma 1' (measure form; `library/i3-cert-check.md` item 2).** Let `mu_nu` be the (complex) measure of
the incoming term at moment `nu`. For every Borel set `B` with `B cap Ent_N` empty, `|mu_N|(B) = 0`.

*Proof.* `mu_N(B) = int (1_B chi_N)(f(x, y)) K(x, dy) mu_{N-1}(dx)`, `f` the move, `K` the kernel, `chi_N` the
product of the indicator factors imposed at `N` (the factors carried at `N - 1` are already in `mu_{N-1}`).
If `x` is the end of an admitted trajectory, then either `chi_N(f(x, y)) = 0` or `f(x, y)` is the end of an
admitted trajectory; in both cases `(1_B chi_N)(f(x, y)) = 0`. By induction `|mu_{N-1}|` is carried by
`Ent_{N-1}`, so the integrand vanishes `|mu_{N-1}|`-almost everywhere, and the same holds for
`|mu_N| <= |chi_N| f_*(|K| |mu_{N-1}|)`. Base: `mu_0` carries its own indicators. `square`

Measurability of `Ent_N` is not needed: only Borel sets disjoint from it are measured. The set
`{I != 1}` is Borel (finitely many continuous functions of finitely many links) and, by Theorem 9.1,
disjoint from `Ent_N`; so `I = 1` holds `|mu_N|`-almost everywhere. Lemma 1 is the pointwise form, valid
when the term is read as the function given at every point by its iterated-integral formula."

**B2.2, section 9.1, (H4) (line 687).**
Old: "- (H4) the incoming term is an iterated integral in the sense of Lemma 1;"
New: "- (H4) the incoming term is a finite sum of iterated integrals in the sense of Lemma 1, each step being
  the insertion of a finite decomposition of unity, a multiplication by an indicator or a delta, an
  integration against a kernel, a reference-law replacement (m5), or the removal of an indicator that
  equals one on the chart of its removal, which is an identity of measures (Y 77757-77758); Lemma 1' is
  applied summand by summand;"

**B2.3, section 9.1, Theorem 9.1 (lines 691-692), fragment.**
Old: "(in particular wherever
the incoming term is not zero)"
New: "(so, by Lemma 1', `|mu_N|`-almost everywhere for the incoming measure, and, in the pointwise reading
of Lemma 1, wherever the incoming term is not zero)"

## B3. Definition 4.3: the move (m6) and the fail factors (i3-cert-check item 1)

**B3.1, section 4, Definition 4.3, after (m5) (after line 267).**
New: "- (m6) a deletion of a determining plaquette: the newly made layer uses its own regularity guard
  (Y 76686-76688), which supplies its loops. A loop crossed by an (m6) move has that guard as supplier,
  which is not in the table of 5.2; this concerns structures outside `X` (rows 628, 632). Lemma 1 does
  not use the list of moves."

**B3.2, section 4, Definition 4.3 (lines 269-270), fragment.**
Old: "The trajectory is *admitted* if at every moment `nu <= N` every test carried by the term at that moment
equals one at `x_nu` and every carried constraint holds."
New: "The term is a finite sum of summands from decompositions of unity: the frame sum, the pass/fail split
`a_r + b_r = m` (Y 63836), drop-outs at a failed test (Y 63856), and failed sharp indicators carried as
separate factors (Y 65449-65450). Trajectories are taken summand by summand. The trajectory is *admitted*
if at every moment `nu <= N` every indicator factor carried by its summand at that moment (pass factors
`chi` and fail factors `1 - chi`) equals one at `x_nu`, and every carried delta constraint holds. (E1)-(E4)
are pass factors at the entrance of a stage that is entered. Points are read in the original
variables: coordinate changes that keep the datum (`V'' = e^{i g_k B} V_0`, Y 63858; `V'' = V' V_0`,
Y 78327-78330) are not moves."

## B4. Lemma 6: the set that defines "not a tower holonomy" (i3-cert-check item 8, cov-x-check (d1))

i3-cert-check item 8 offers two repairs: require `J_t = Omega'_t` on `F(p)` for `t = l - 1, l, l + 1`, or
use Y's interior case. cov-x-check (d1) asks that "tower holonomy" mean every tested plaquette that is
not interior, at every level, as Y 13100-13102 has it, or else that the exclusion be written into
Theorem 9.1 (i). One definition serves both: the first repair of item 8 with the first repair of (d1).
The proof of Lemma 6 stays the two lines it was. Theorem 9.1 (i) is not changed.

**B4.1, section 7, proof of Lemma 6 (lines 612-615), fragment.**
Old: "A tested plaquette is "not a tower holonomy" when its
footprint and the double blocks of its edges lie where `T_l = T_{l-1} =` everything, that is, where
`J_l = Omega'_l` and `J_{l-1} = Omega'_{l-1}`; there Definition T gives the same edges with the same values
for the two sequences."
New: "A tested plaquette of level `l` is *interior* when its footprint and the double blocks of its edges lie
where `T_t =` everything for `t = l - 1, l, l + 1` (`t <= m`), that is, where `J_t = Omega'_t` for these `t`.
Level `l + 1` is needed because it decides which edges of `p` are rows and whether `p` is tested
(Definition T). A *tower holonomy* is a tested plaquette of the joined datum that is not interior, at
every level, the top level included (Y 13100-13102: either `R(p) subset W^{(-2)}`, or `R(p) subset Q_a`
for a part with `q <= j_a`); Y bounds those through (R1) (Y 13117-13126). For an interior plaquette
Definition T gives the same tested status, the same edges and the same values for the two sequences."

**B4.2, section 5.4, item 6 (line 443).**
Old: "Statement (i) excludes these plaquettes anyway."
New: "Theorem 9.1 (i) does not exclude them; they are covered here."

**B4.3, section 7, Remark 7.3 (lines 593-594), fragment.**
Old: "which gives `2.1 eps_m` by (I4)
of `library/rim-scale.md`, and statement (i) excludes it."
New: "which gives `2.1 eps_m <= C_2 e_m` by (I4)
of `library/rim-scale.md`; Theorem 9.1 (i) does not exclude it."

Reason for B4.2-B4.3: with the definition of B4.1, a level-m plaquette near the old seam of `Omega_m`
lies deep in `X` (`O_m = H_m^{[8 a_m]}`, `X = H_m^{[10 a_m]}`, tower within `3 M_1 L^m` of `X^c`), so it is
interior and is in (i). The two remarks said otherwise (cov-x-check (d1), "lines 443 and 594").

## B5. (G1): `L >= 13` and the floors of Y 35270 (i3-cert-check item 6)

**B5.1, section 2.4, (G1) (lines 151-153).**
Old: "- (G1) Both sequences, and the global ones, satisfy the separation with the floors of
  `hi:real-datum-profile` (Y 15317-15322): `sigma >= L^2 rho_c`, `frakM >= frakM_c`, `rho >= L^2 sigma`,
  at least `6 rho` sites in each direction at the top level."
New: "- (G1) Both sequences, and the global ones, satisfy the separation with the floors of
  `hi:real-datum-profile` (Y 15317-15322): `sigma >= L^2 rho_c`, `frakM >= frakM_c`, `rho >= L^2 sigma`,
  at least `6 rho` sites in each direction at the top level; and, for (BG), `L >= 13` with the floors of
  the aligned separated geometry of `mb:datum-descent-critical-ascent` as raised at Y 35270-35275. All are
  fixed before `gamma`; none changes a constant of this note."

## B6. The (K-x) and (K-col) rows of table 5.2 (i3-cert-check item 5)

**B6.1, section 5.2, row (K-x) (line 332).**
Old: "| (K-x) | crossing clause `kappa_x` at the prepared face of the stage of level `j` | `< (1 - 3 beta_s/4) F_j eps_j L^{-2j}`, `F_j = L_flat^{2(j-k_0-1)_+}` (Y 64308-64313) | `c_0 F_j` |"
New: "| (K-x) | crossing clause `kappa_x` astride `dZ''_m` of the final inset test, in the prospective background (Y 64308-64313). It is imposed after the entrance, like T6, and is **not carried at the entrance**; a crossing clause is carried only if the operation has the added crossing tests (T3; Y 64384-64386). No step of 5.4 uses it (A2) | `< (1 - 3 beta_s/4) F_j eps_j L^{-2j}`, `F_j = L_flat^{2(j-k_0-1)_+}` | `c_0 F_j` |"

**B6.2, section 5.2, row (K-col) (line 333), fragment.**
Old: "| `c_f L_flat^{2(l-k_0)_+}` (Y 76669-76670), plus `8 delta'_{j'}/eps_l` |"
New: "| `c_f L_flat^{2(l-k_0)_+}` (Y 76669-76670), plus `8 delta'_{j'}/eps_l`. `c_f` occurs in Y only at Y 76670 and is not defined there; put `c_f := 3 sqrt(2) c_0 L^2` (from the (K-shell)/(K-ext) bound with Lemma 2a; **unproved**, `library/i3-cert-check.md` item 5). Used only for departures outside `X` |"

With this `c_f`, `A_L` of (5.1) is unchanged: `c_f` equals its first entry.

## B7. (H5) and the order of constants (i3-cert-check item 10, additions 1 and 2)

**B7.1, section 9.1, (H5) (line 688).**
Old: "- (H5) `gamma` so small that `C_2 ebar(gamma) <= alpha_L` and `c_0 C_2 ebar(gamma) <= min(eps_L, L^2/C_L)`;"
New: "- (H5) `gamma` so small that `C_2' ebar(gamma) <= alpha_L`, `c_0 C_2' ebar(gamma) <= min(eps_L, L^2/C_L)`
  and `C_2' ebar(gamma) <= 1` (the last for the conversion `abs(F) <= c_0 . defect` of 2.3);"

**B7.2, section 9.2 (line 720), fragment.**
Old: "All are fixed
before `gamma` in Y's order (Y 72931)."
New: "All are fixed
before `gamma` in Y's order (Y 72931). `L_flat` is not in Y's display; it is chosen together with `L`
(Y 63876). `c_f` is not defined in Y; with B6 it is a function of `L`. So the three conditions of (H5) and
the floors (T1)-(T3) are ceilings on `gamma`, satisfiable since `ebar(gamma) -> 0`."

## B8. Rename of `c_0` (i3-cert-check item 10, addition 3) — NOT APPLIED

The check calls it a notation clash, not an error: i3-cert's `c_0 = pi/2` is not Y's `c_0` (Y 1681).
The rename touches 22 lines of i3-cert, and `library/cov-x.md` and `library/cov-x-check.md`, which this
session may not edit, use `c_0` for the same `pi/2`; the formulas quoted in A2 and A4 come from them.
Renaming in i3-cert alone would break those cross-references. Left for the lead, to do in all three
files at once.

## B9. Cite in Lemma F2 (i3-cert-check item 3)

**B9.1, section 3, Lemma F2 (line 195), fragment.**
Old: "(the compression identity, Y 63798-63801: `a_{k_0+1} = u_k`)"
New: "(the compression identity, Y 63749, 63774-63776: `a_i = M R_i L^i`, `u_i = M L^i`, `a_{k_0+1} = u_k`)"

## B10. Not applied (not in the check's repair list, or another file)

- (K-ext) for `l < j` (item 5): `psi` would carry `(1 + Bbar)^{1/2}`. The check says no step uses that
  case and leaves it out of its repair list. Text unchanged.
- `R_mat` to `r_U` (item 6): closed by Y 35290 in the check. That is a status change, not a repair.
  Lines 477-479 and 758-759 ("I did not check the conversion") are unchanged. The lead may cite
  `library/i3-cert-check.md` item 6 there.
- `library/inset-chart.md` 5.1/5.6 wording (item 11): that is another file.

## H. Head line for `library/i3-cert.md`

Insert after line 2 (`lease_until: ...`), before the title, one blank line and:

"Repairs 2026-11-10 (FINISH row 634; old and new sentences in `library/i3-repairs.md`): A1 (c2'), (c3') and
the edge form of (s1); A2 one supplier for 5.4 items 3 and 5, the guard before the promotion; A3 the
seventh kind (K-wall) and `C_2' = max(C_2, 6 . 4^r)` in Lemma 2b, Corollary 5.2, (H5) and `C_3`; A4 Lemma 4
case A with `C_2'`; B1 Lemma 2.3a (local averaging); B2 Lemma 1' and (H4); B3 (m6) and fail factors; B4
the interior set of Lemma 6 (levels `l - 1, l, l + 1`); B5 `L >= 13` in (G1); B6 (K-x), (K-col); B7 (H5) and
the order of constants; B9 cite in F2. Not applied: `C_2''` of cov-xstar (its check is absent), the rename
of `c_0`."

## What is proved, what stays open

No new proof, as the row says. The only mathematical content added is quoted from the two checks:
Lemma 2.3a (i3-cert-check Lemma 4.1, proved there), Lemma 1' (proved there), and the one-line constant
checks under A3.5 and A4 (`2.1 eps_j <= C_2 e_j`, because `2.1 < pi = 2 c_0`, `A_L >= c_0` and `R_j >= 1`;
and the conditions of A4.1 give each inequality of case A). Every step is a named hypothesis, a quoted
Y line or a one-line inequality, as a proof assistant would need.

After these repairs, Theorem 9.1 of i3-cert reads, unchanged in statement: given (COV) in the form
(c1), (c2'), (c3') with seven kinds, `C_3 = 2 c_0 L^2 C_F(1) C_2'`. This is the form both checks accept.

Still open (unchanged by this row): (COV) for levels below `h` and outside `X` (row 632); the constant
`c_f` (B6, unproved); `C_2''` (row 639); and (E2)'s word "(crossing)", flagged in A2 but not changed.

Not done here: `library/i3-cert.md` is **not edited**. The worker instruction for this session forbids
editing it, so the lead must apply A1-A4, B1-B7, B9 and H by exact replacement. Each old fragment above
was checked to occur exactly once in i3-cert at 01af230c4.

Status: DONE 2026-11-10.

RESULT: i3-repairs written as old/new sentence pairs, not applied to i3-cert.md (the session forbids editing it). APPLY: cov-x edits 1-4 in the form cov-x-check accepts ((c2')/(c3') and the edge form of (s1); the guard before the promotion for 5.4 items 3 and 5; (K-wall), with C_2' = max(C_2, 6.4^r) in Lemma 2b, Cor. 5.2, (H5), Lemma 4 case A and C_3), and the i3-cert-check repairs (Lemma 2.3a local averaging, Lemma 1' and (H4), (m6) and fail factors, Lemma 6 interior set over levels l-1, l, l+1, which also settles cov-x-check (d1), L >= 13 in (G1), (K-x) and (K-col) rows, (H5) additions, F2 cite). NOT APPLIED: C_2'' of cov-xstar (cov-xstar-check.md absent), the c_0 rename (would break the cross-references to cov-x), and (K-ext) l<j and R_mat (not repairs). Open: (COV) below h and outside X (row 632), c_f unproved, C_2'' pending row 639.
