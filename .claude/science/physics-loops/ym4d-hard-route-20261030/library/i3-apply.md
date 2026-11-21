lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T00:44Z

# i3-apply (FINISH row 643): edits applied to `library/i3-cert.md`

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort high, Mac mini worker 2, branch `claude/ym4d-hard-route` at c33161ce2. Not an audit. Started 2026-11-10T12:44Z.

Outputs of this row: `library/i3-cert.md` (edited) and this log.
Inputs: `library/i3-repairs.md` (row 634), `library/cov-x-check.md` (row 633), `library/cov-global-check.md` (row 636, defect (6)), `library/cov-x.md` (row 628, (c2')), `library/cov-xstar-check.md` (row 639, `C_2''`), `library/i3-cert-check.md` (row 630).

## Repo search

- `library/open-core.md`: no entry for i3-cert, i3-apply, (COV) or `C_2''` (grep). This row attacks no open lemma; it edits text.
- FINISH rows near this one: 624 (i3-cert), 630 (its check), 633 (cov-x-check), 634 (i3-repairs), 636 (cov-global-check), 639 (cov-xstar-check), 642 (cov-apply, which edits `cov-global.md` and `cov-xstar.md` and is told not to edit `i3-cert.md`). None of them edits `library/i3-cert.md`; row 643 is the one row allowed to.
- `library/i3-cert.md` is unchanged since 01af230c4 (the commit `i3-repairs.md` quotes), checked with `git diff 01af230c4 HEAD`; so every "Old" fragment of i3-repairs is quoted from the text being edited.
- Credit: the argument of i3-cert is Sussman and Alpoge's (`YM4_1400.tex` at 2bc0658f91d2; their text names Claude and Codex as authors), paragraph `hi:prepared-real-endpoint`; the nest and the stage test are Bałaban's (CMP 122). The repairs are by the checks named above (Claude Opus 5.5) and by `library/cov-x.md`, `library/cov-xstar.md` (Claude Fable 5.2).

## How the edits were made

Each edit is an exact replacement of an old fragment by a new one. A small text script (in my own scratch folder, not a proof step) asserted that each old fragment occurs exactly once before replacing it. No numeric job was run. Memory free at start: 61 percent.

## 1. Edits, one line each

Places are sections of `library/i3-cert.md`. Ids are those of `library/i3-repairs.md`. Wherever i3-repairs writes `C_2' = max(C_2, 6 . 4^r)`, this row writes `C_2'' = max(C_2, 6 . 4^r L^2)`. The row asks for this, and `library/cov-xstar-check.md` (row 639) accepts it: its item (6) shows that the factor `L^2` is needed at the last stage of an operation.

**(a) Repairs of `library/i3-repairs.md` with status APPLY**

| Id | Place | Result | Note |
|---|---|---|---|
| H | head, after line 2 | APPLIED | The head line of i3-repairs H, with `C_2''` in place of `C_2'`, with (d1), (d2) and the (COV) restatement added, and with "not applied: `C_2''`" removed. The lines `lead:` and `lease_until:` of the earlier lane are not changed. |
| A1.1 | 5.1, Definition 5.1, (s1) | APPLIED | Edge form. |
| A1.2 | 5.4, (COV), (c2) | APPLIED, then restated by (c) | See the (COV) entry under (c). |
| A1.3 | 5.4, (COV), (c3) | APPLIED | (c3') verbatim. |
| A1.4 | 5.4, proof of Corollary 5.2 | APPLIED, with two additions | Added "is a conjugate of" and "the defect is invariant under conjugation", for (c). Added the (K-core) sentence, "the bound on the datum loop at `x_nu` is carried to `x_N` by (c2')", because the old proof covered (K-core) through (c2) and A1.4 dropped it. |
| A1.5 | 5.4, after Corollary 5.2 | APPLIED | `C_2''`, (c2'). |
| A1.6 | 9.2, "to the present by (c2')" | APPLIED | |
| A2.1 | 5.4, item 3 | APPLIED | |
| A2.2 | 5.4, item 5 | APPLIED | |
| A2.3 | 0, finding 2 | APPLIED | |
| A2.4 | 10, item 1, two fragments | APPLIED | In the first fragment, "equal to the loop the supplier bounds" became "equal, up to conjugation, to the loop the supplier bounds", for (c). |
| A2.5 | 10, item 2 | APPLIED | |
| A2.6 | 9.2, crux paragraph | APPLIED | With `C_2''`. |
| A3.1 | 5.2, new row (K-wall) | APPLIED, `psi` column changed by A5 | The `psi` column reads `<= 3 . 4^r L^2 R_l^2` at level `l`: `3 . 4^r R_j^2` at the walls inside `X` at the final entrance (cov-x Lemma 6.4), with the factor `L^2` for a plaquette made at the last stage of an operation (cov-xstar (Q3)). This is A5's "the (K-wall) row of A3.1 then needs `psi_t <= 3 . 4^r L^2 R_t^2`". The other columns are verbatim. |
| A3.2 | 5.2, before (5.1) | APPLIED | |
| A3.3 | 5.2, after (5.1) | APPLIED with `L^2` | `psi_l <= 3 . 4^r L^2 R_l^2`, `2 psi_l eps_l <= 6 . 4^r L^2 e_l`. |
| A3.4 | 5.3, Lemma 2b | APPLIED | `C_2'' := max(C_2, 6 . 4^r L^2)`. |
| A3.5 | 5.3, proof of Lemma 2b | APPLIED with `L^2` | (K-wall): `2 psi_l eps_l <= 6 . 4^r L^2 R_l^2 eps_l = 6 . 4^r L^2 e_l <= C_2'' e_l`. Depth 0: `2.1 eps_l <= 2 c_0 eps_l <= C_2 e_l <= C_2'' e_l`, because `2.1 < pi = 2 c_0`, `C_2 >= 2 A_L >= 2 c_0` and `e_l = R_l^2 eps_l >= eps_l`. |
| A3.6 | 5.3, (s2) ceiling | APPLIED with `L^2` | |
| A3.7 | 5.4, (COV), (c1) | APPLIED | Written as `alpha = psi_l eps_l`, with `psi_l` from the (K-wall) row; the value `3 . 4^r e_j` of A3.7 is kept for the walls inside `X` at the final entrance. |
| A3.8 | 5.4, item 4 | APPLIED | |
| A3.9 | 5.4, new item 7 | APPLIED | Verbatim; inside `X` at `N`, `d <= m - k_0 - 2`, so no `L^2` (cov-x-check item 8). |
| A3.10 | 5.4, Corollary 5.2 statement | APPLIED | With `C_2''`. |
| A3.11 | 0 (three places), 5.3 heading, 6.3, Lemma 4 (`C_3`, proof), Remark 7.2 (four fragments), 9.1 proof, 9.2 table (new row `C_2''`, `C_3` row), 9.2 crux (three fragments) | APPLIED, 17 fragments | With `C_2''`; the new table row reads `max(C_2, 6 . 4^r L^2)`, depending on `C_2, r, L`. |
| A4.1 | 7, Lemma 4, hypothesis | APPLIED | With `C_2''`. |
| A4.2 | 7, case A | APPLIED | With `C_2''`. |
| A4.3 | 7, case A display | APPLIED | With `C_2''`. |
| A5 | (`C_2''`) | APPLIED | Through A3 to A4, B7 and H as above. i3-repairs says "A3-A5 and the head line, and nothing else" in one place, and "in (H5) (B7)" in A5. I followed A5 and (d2): (H5) carries `C_2''`. |
| B1.1 | 2.3, status paragraph and Lemma 2.3a | APPLIED | |
| B2.1 | 4, Lemma 1' after the proof of Lemma 1 | APPLIED | The old fragment was not found literally, because the line before reads "At `N = 0`" and not "at `N = 0`". The lemma was inserted after "there is nothing before. `square`", which is the place i3-repairs names (after line 283). |
| B2.2 | 9.1, (H4) | APPLIED | |
| B2.3 | 9.1, Theorem 9.1 | APPLIED | |
| B3.1 | 4, Definition 4.3, (m6) | APPLIED | The full stop of (m5) became a semicolon. |
| B3.2 | 4, Definition 4.3, admitted | APPLIED | |
| B4.1 | 7, proof of Lemma 6 | APPLIED, with one added sentence | The sentence links B4.1 to (d1); see (b). |
| B4.2 | 5.4, item 6 | APPLIED | |
| B4.3 | 7, Remark 7.3 | APPLIED | |
| B5.1 | 2.4, (G1) | APPLIED | |
| B6.1 | 5.2, row (K-x) | APPLIED | |
| B6.2 | 5.2, row (K-col) | APPLIED | `c_f` is labelled **unproved**, as i3-repairs labels it. |
| B7.1 | 9.1, (H5) | APPLIED with `C_2''` | This is also (d2). |
| B7.2 | 9.2, order of constants | APPLIED | |
| B9.1 | 3, Lemma F2 | APPLIED | |

**Repairs that i3-repairs marks NOT APPLIED, left as they are**

- B8, the rename of `c_0`: NOT APPLIED. Reason, from i3-repairs: the rename would break the cross-references to `cov-x.md` and `cov-x-check.md`, which use the same `c_0 = pi/2`.
- B10: NOT APPLIED. (K-ext) for `l < j` is not in the check's repair list. `R_mat` to `r_U` is a change of status, not a repair. The wording of `inset-chart.md` belongs to another file.
- The A2 flag on the word "(crossing)" in (E2) of Definition 4.2: NOT APPLIED, because no repair names it. No step of the proof reads a crossing clause after A2.

**(b) The defects of `library/cov-x-check.md` (row 633)**

- (d1), first form, "a tower holonomy is any tested plaquette that is not interior, at every level": APPLIED through B4.1. The definition puts the top level in explicitly ("at every level, the top level included"), so Theorem 9.1 (i) gets no exclusion. One sentence was added to the proof of Lemma 6: a plaquette with `F(p) subset Int` (cov-x Definition 7.1) is interior in the sense of B4.1, because every point of `Int` lies in every `T_q` (h-geo Lemma 3.1), so for it the conclusion is cov-x Lemma 7.2 (a). The interior of B4.1 is a larger set than `Int`. On that larger set the proof of Lemma 6 is B4.1's own two lines, not Lemma 7.2 (a); see check point K4 in section 3.
- (d2), `C_2''` in (H5): APPLIED (B7.1).

**(c) Defect (6) of `library/cov-global-check.md` (row 636), with its source, item (10)**

- (COV) restated: APPLIED. The (c2') form of cov-x Definition 3.1, with bare and coarse suppliers. (c2') is read up to conjugation, as item (10) of cov-global-check says. The moment `nu` may come before `p` is first tested, and the plaquette need not be tested at `x_nu`. The (K-core) sentence was adapted: (c2') there says that the datum loop at `x_N` is a conjugate of the datum loop at `x_nu`, which is the content of the old (c2) for that kind, and (c3') is void.
- The wider set of moments, in Definition 4.1: APPLIED. A moment is now also the output of a step, the exit of a stage, or the place just after a stop or a main step. These are the moments of item (10). The text says that Definition 4.3 and Lemma 1 are read with this set and that the proof of Lemma 1 does not change.

**Left unchanged, because no repair names them (stale wording for the lead)**

- 5.4, "What Y gives for (COV)", (b): it still says "(c3) at a mixed loop". This is a historical remark about Y; the clause is now (c3').
- 7, after Lemma 6: "Lemma 6 takes the trichotomy as the definition of 'tower holonomy'; the trichotomy itself is (R1)". Since B4.1, the definition is by a set, and (R1) is only Y's bound for the tower holonomies. Section 10, item 3 has the same phrase ("the trichotomy of the joined datum (Lemma 6)").
- 5.1, Lemma 2 and its proof: unchanged. i3-repairs says the first clause of the proof becomes redundant under the edge form.
- Lines 1-2 (`lead:` and `lease_until:` of the row 624 lane) and the Status line 6 ("not checked by another model"): unchanged.

## 2. The steps of the proof of Theorem 9.1 that read (COV)

The proof of Theorem 9.1 is: Lemma 1, then Corollary 5.2, then Lemma 4, then Lemma 6. Of these, only Corollary 5.2 reads (COV) itself. Lemma 4 reads (COV) through the statement of Corollary 5.2, and the crux of 9.2 reads the form of (COV). Lemma 1 and Definition 4.3 are where `T(x_nu) = 1` comes from. For each step below I say what it reads and why the restated form gives it. Constants are those after the edits.

**U1. Corollary 5.2 (the one direct reader).** Fix `x_N in Ent_N` and a tested plaquette `p` of level `l >= 1` of `D(x_N)`. The proof reads five things.

- (i) A moment `nu <= N` and a test `T` carried at `nu` with `T(x_nu) = 1`. The restated (COV) gives `nu` and `T`. The equality `T(x_nu) = 1` holds because the trajectory is admitted (Definition 4.3, B3.2): every pass factor carried at a moment equals one at that moment. Since Definition 4.1 now includes the moments of item (10), this also covers a supplier whose moment is the output of a step, or a stage moment before `p` is tested (cov-xstar: `mu in [nu_h, nu_i]`).
- (ii) A bare bound on `F(p)` from `T = 1`, read on the configuration that `T` reads. This is (c1) together with (c3'). For a bare supplier, `U` is the restriction of what `T` reads, and (c1) gives `eps(U; F(p)) <= alpha L^{-2l}` with `alpha = psi_l eps_l`. For a coarse supplier, `W` is the level-l' datum at `x_nu`, and (c1) gives `abs(F_q(W)) <= alpha L^{-2d}` for each level-l' plaquette `q` with corners in `F(p)`.
- (iii) `alpha <= alpha_L`. Lemma 2b gives `alpha = psi_l eps_l <= (C_2''/2) e_l`. Lemma F4 gives `e_l <= ebar(gamma)`. The first clause of (H5) gives `C_2'' ebar(gamma) <= alpha_L`.
- (iv) The loop at `x_N`. (c2') says that `V(dp)` at `x_N` is `g X g^{-1}`, where `X = (M^l U)(dp)` (or `(M^d W)(dp)`) and `g` is in SU(2). Then `norm(V(dp) - 1) = norm(X - 1)`. This is the only use of the loop, and the conjugation does not change it. The old (c2) asked for more: that `p` is tested at every moment from `nu` on, and that `U` satisfies (s1) for `D(x_nu)`. The proof does not use either.
- (v) The estimate. (AV2) gives `abs(F_p(X)) <= 2 alpha`, and `norm(e^{iF} - 1) <= abs(F)` gives defect `<= 2 alpha = 2 psi_l eps_l`. Lemma 2b gives `<= C_2'' e_l`, for the kinds within (5.1) and for (K-wall). For (K-core), (c2') says the loop at `x_N` is a conjugate of the datum loop at `x_nu`, which has defect `<= 2 psi_l eps_l` by the (K-core) bound. Conjugation carries this to `x_N`.

Verdict for U1: the restated form gives the step, **except at one place where the hypothesis list is short**. For a coarse supplier with `d >= 1`, the step uses (AV2) for a configuration on the level-l' lattice. Hypothesis (H3) of Theorem 9.1 names (AV1), (AV2) "in the local form of 2.3", and 2.3 states (AV2) for a configuration on the bare bonds. I did not change the step or (H3). **Missing statement (AV2'):** let `0 < alpha <= alpha_L`, let `W` be a real configuration on the level-l' bonds of `F(p)`, `p` of level `l = l' + d`, with `abs(F_q(W)) <= alpha L^{-2d}` for every level-l' plaquette `q` with corners in `F(p)`; then `abs(F_p(M^d W)) <= 2 alpha`. (AV2') is (AV2) on the lattice `L^{l'} Z^4`, read as a copy of the bare lattice, if the one-step average from level `t` to level `t + 1` is the same map at every `t`. Lemma 2.3a (B1) is a statement about any lattice box. `library/cov-x.md` section 8, read item 6, lists (AV2') as read and not rebuilt. Repair, unproved: add (AV2') to (H3), with the sentence that `M` is the same map at every level (Y's `M^l` is the `l`-fold iterate of one average).

**U2. 5.4, the paragraph after Corollary 5.2, "The proof passes a value ... by (c2')".** This paragraph reads only that the bound at `x_N` comes from the threshold of `T` at its own moment and not from an earlier estimate. The restated (COV) has this form: (c1) is a threshold of the operation, and (c2') carries a loop, not a bound. HOLDS.

**U3. Lemma 4 (statement (ii)).** Lemma 4 reads the statement of Corollary 5.2 at the same `x`, and nothing of (COV) beyond it.

- Cases `l < j`, `l = j`, case B of `l = q`, and `l = q + 1`: each reduces to an old tested plaquette of `D(x)` with the same loop, then applies Corollary 5.2. The bound is `C_2'' e_l <= C_3 e_l`, since `C_3 >= C_2''` (A3.11, `2 c_0 L^2 C_F(1) >= 1`).
- Case A: Corollary 5.2 for the level-j plaquettes of `D(P)`, all old tested plaquettes. This includes those astride an original wall, item 7 (A4.2). Then 2.3 gives `eps(W; D(P)) <= c_0 C_2'' e_j`. The conversion needs defect `<= 1`, which is the third clause of (H5) (`C_2'' ebar <= 1`). (AV1) needs `c_0 C_2'' e_j <= eps_L`, and the absorption needs `C_L c_0 C_2'' e_j <= L^2`; both come from the hypothesis of Lemma 4 (A4.1) and the second clause of (H5).

Since the statement of Corollary 5.2 is unchanged apart from the constant, the restated form gives Lemma 4. HOLDS.

**U4. Theorem 9.1, proof.**

- Lemma 1: an induction over consecutive moments. It uses no property of a moment other than that the term at `nu + 1` is an integral of the term at `nu` times the factors carried at `nu`. That holds at the added moments, which are places in the same iterated formula. Lemma 1' is the same induction in measure form.
- Corollary 5.2: U1.
- Lemma 4: U3.
- Lemma 6: it reads Lemma 4 and Definition T, and not (COV).

HOLDS, with the (AV2') gap of U1.

**U5. 9.2, the crux paragraph.** It reads that at each entrance every old tested plaquette, including one made new at the entrance before, is supplied by a test with a threshold written in the operation, at the moment the test is carried. It also reads that the constant is `C_2''` again, not `C_3`. The restated (COV) allows exactly the suppliers that do this. One is the stage supplier of cov-xstar Theorem 6.1, whose moment comes before `p` is first tested, which is the reason for the wider moments. The others are the supplier at the output of a step, (S-ord), and the island supplier after the main step, (S-core), of cov-global Theorem 5.1. Their allowances lie within (5.1) or in (K-wall), so Lemma 2b gives `C_2''`. HOLDS. One reading is needed: the (K-core) constant `C(M, M_0)` of table 5.2 must be at least `4 M_0 + C(M)`, the island bound of cov-global Theorem 5.1, so that `A_L` contains it. Table 5.2 does not define `C(M, M_0)`, so I record this as a reading, not as a defect.

**U6. Readers of Corollary 5.2 outside the proof of Theorem 9.1.** Lemma 3 with `B = C_2''` (6.3), Remark 7.2, and Lemma 5 (through `C_3`). They read only the statement of Corollary 5.2, so they are unchanged. Not needed for Theorem 9.1.

**Steps that need more than the restated form gives:** one, U1 for a coarse supplier, at depth `d >= 1`. Missing statement: (AV2') above, in (H3). No step was changed because of it.

## 3. For the one check by another model (the row asks for it)

These are the places where this row chose a wording that the repair texts do not give word for word. Each needs to be checked.

- K1. (c2') read up to conjugation (cov-global-check item (10)), not the edge equality of cov-x Definition 3.1. The edge equality is kept as the sufficient case. This makes (COV) weaker, so it is easier to supply. Corollary 5.2 still holds: U1 (iv).
- K2. The (K-core) form of (c2'): the datum loop at `x_N` is a conjugate of the datum loop at `x_nu`. It carries over what old (c2) said for this kind. A1.4 dropped (K-core), so its proof gained one sentence.
- K3. The (K-wall) `psi` column and A3.3, A3.5, A3.6 with `L^2`. For the walls inside `X` at `N`, the sharper `3 . 4^r R_j^2` is kept (A3.9, item 7).
- K4. B4.1 interior (levels `l - 1, l, l + 1`) used as the "interior" of (d1). It is a larger set than `Int` of cov-x Definition 7.1. Lemma 6 for the extra plaquettes rests on B4.1's two lines, not on cov-x Lemma 7.2 (a). I checked one point that the B4.1 text leaves implicit, and it holds. A corner outside `X` lies outside `J_{l-1}`, so B4.1 makes it lie outside `Omega'_{l-1}`. But every corner of a tested plaquette lies in `Omega'_{l-1}` by the separation. So no corner is outside `X`. The row edges and the double blocks then lie in `J_{l-1} subset X`, and the condition at level 0 (`Omega_0`) is not needed.
- K5. The wider moments in Definition 4.1 (U4): Lemma 1's induction does not read what a moment is.
- K6. The missing (AV2') of U1.

## 4. What is proved, what stays open

No new mathematics. The edits are text. The only arguments written here are those of section 2: each is a named hypothesis, a quoted clause, or a one-line inequality. Examples are `norm(g X g^{-1} - 1) = norm(X - 1)` for unitary `g`, and `2.1 eps_l <= 2 c_0 eps_l <= C_2 e_l <= C_2'' e_l`.

After this row, Theorem 9.1 of i3-cert reads: given (COV) in the restated form ((c1), (c2') up to conjugation, (c3'), seven kinds, wider moments), (H1) to (H5) with `C_2''`, and (AV2'), `I(omega) = 1` with `C_3 = 2 c_0 L^2 C_F(1) C_2''`.

Open, unchanged by this row:

- (COV) for levels below `h` and outside `X`, row 632 (cov-global, given its read statements, and cov-xstar, checked).
- `c_f` (B6, unproved).
- (AV2') as a stated hypothesis (U1).
- The reading `C(M, M_0) >= 4 M_0 + C(M)` (U5).
- The stale wording listed at the end of section 1.
- One check of the uses of the restated (COV) by another model (section 3).

Status: DONE 2026-11-10.

RESULT: library/i3-cert.md edited. APPLIED: every APPLY repair of i3-repairs (A1-A4, B1-B7, B9, head line), with C_2'' = max(C_2, 6.4^r L^2) in place of C_2' throughout, including (H5) and the (K-wall) psi <= 3.4^r L^2 R_l^2; (d1) through B4.1, first form (tower holonomy = every non-interior tested plaquette, top level included); (d2) through (H5); (COV) restated with bare and coarse suppliers, (c2') up to conjugation, (c3'), and the wider set of moments in Definition 4.1. NOT APPLIED: B8 (c_0 rename), B10, the (E2) "(crossing)" flag. Every step of Theorem 9.1 that reads (COV) holds under the restated form (Corollary 5.2, Lemma 4, Lemma 1 with the wider moments, the 9.2 crux), except one hypothesis gap: a coarse supplier needs (AV2') on the level-l' lattice, which (H3) does not list (step not changed; repair: add it to (H3)). Open: (COV) below h and outside X (row 632), c_f, (AV2'), the reading C(M,M_0) >= 4M_0 + C(M), and one check of these uses by another model.
