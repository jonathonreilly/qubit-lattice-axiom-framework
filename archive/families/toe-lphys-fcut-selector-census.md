# Sub-campaign roll-up: the f_cut coverage/selector censuses (toe-lphys-20260812, ~#6476–#6567)

The band that IS the true census family (44/44 template-content). Full-diff
read of every member (densify 2026-08-31). No (reverse,face) verdicts — these
are f_cut coverage/selector censuses on the 32 cube-covariant cut maps.

## The cross-cutting result no single PR states
**Seed-size-indexed exact selector table** (with #6531/#6539/#6548):
k=1 wt1∧adj2 · k=2 wt1∧(adj2∨v3∨m3) · k=3 NO member of the menu ·
k=4 wt1∨adj2 · k=6 wt1∨adj2∨v3 · k=7 adj2∨v3 · k=8 wt1∨opp2∨adj2∨v3.
**The k=7 selector DROPS wt1** (present at both k=6 and k=8): four Q6-true
wt1-only maps have cov7=0 but cov8>0 — the positivity selector is
NON-MONOTONE in seed size. Per-map coverage is also non-monotone
(#6493: cov1..6 of (1,0,0,0,0) = 0,0,0,7,0,4; #6519/#6524).

## Exact identities established
#6516: cov1>0 ⇔ wt1∧adj2 (unique). #6494: cov2>0 ⇔ wt1∧(adj2∨v3∨m3).
#6518: cov4>0 ⇔ wt1∨adj2 (fp=fn=0). #6567: cov7>0 ⇔ adj2∨v3 (unique of 18 —
its TITLE reports only the negatives; the positive match is in the body).
#6522: inside Q_*, cov1=12 ⇔ vertex3 (levels {0,8,12}). #6476/#6487:
complement duality only at middle sizes; K_unique={4..8} with one maximizer.
#6561: UNREMARKED by its own note — its data gives cov3=220 ⇔ v3∧m3 inside
Q_* (opp2 free); the note's candidate failed only because opp2 was bundled.

## Exhaustive negatives
#6514+#6524: all 32 single-bit/AND/OR menu candidates fail cov3 (k=3 selector
is outside the menu). #6503/#6509: P is necessary-not-sufficient at k=1 and
sufficient-not-necessary at k=4. #6564: positivity-freedom from mixed3 does
not extend to the integer (14 of 15 pairs differ).

## Promotion candidates
The selector table as a set (#6516/#6494/#6518/#6567/#6522), the
non-monotonicity pair (#6493 + the k=7 drop), #6524's completed refutation.

## Notes
#6567 ships 3 files (no manifest bump); ~7 members use the V1–V5 gate layout;
#6486 uses alternate bit labels for the same partition.

## Second census half (~#6568–#6622, fread_03) — the complete selector law

Read together, the 44 "X is not Y" censuses CONTAIN a complete exact selector
law for every seed size on the two-cube, stated by no member:
k=1 iff Q_* (wt1∧adj2) · k=2 iff wt1∧Q10 · k=3 ⟹Q4/Q6/Q8, ⇏Q10 (menu has no
k=3 member) · k=4 iff Q4 · k=5 adj2∨(wt1∧v3)∨(wt1∧opp2∧m3) · k=7 iff adj2∨v3
· k=8 iff Q8 · k=9 iff adj2∨v3∨(opp2∧m3) · k=10 iff Q10 · k=11 iff adj2∨v3 ·
k=12 degenerate (the seed is the patch, #6596).
Consequences no note draws: (1) k=7 and k=11 are EXACTLY the 2-bit OR the
band's own summaries say was not found; (2) every datum fits the closed form
**cov11(f) = 4·adj2 + 8·vertex3** on all 32 maps (from #6582/#6616/#6602/
#6613) — making the k=11 census a corollary; (3) positivity is non-monotone
in k (vertex3-only maps: cov5=0 but cov7,cov11>0), and the only work opp2∧m3
does anywhere is the lone exceptional positives at k=5 and k=9.
Parity pattern (via #6570/72/81/92/93/94/95, #6604): odd k → the two Q maps
are TOTAL; even k → f1=(1,1,1,1,1) is the unique maximizer.

## Defect cluster requiring repair (#6611–#6613, #6614)
Copy-paste cluster from the cov3 sibling: wrong seed-size prose throughout,
N8 triples contradicting Theorem 2, No-Go text asserting the opposite of
Theorem 1 — and in #6612/#6613 the `thm1-pos-implies-q4` check contains
literal `and True` placeholder stubs (lines 907/909) that still report
PASS/FAIL=0. **PR bodies are correct; only the diffs reveal it** — a
body-level triage marks exactly these three clean. Fourth independent
false-green finding for the methodology dossier.
