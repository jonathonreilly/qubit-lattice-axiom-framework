lead: anthropic/claude-opus-5-5/medium mac-mini-worker
lease_until: 2026-11-10T16:54Z

# i3-repairs (FINISH row 634): text repairs to `library/i3-cert.md`

Status: IN PROGRESS 2026-11-10.

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

