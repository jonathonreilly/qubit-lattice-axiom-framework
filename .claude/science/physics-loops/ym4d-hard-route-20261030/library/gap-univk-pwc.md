lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T05:39Z

# Row 1406, gap-univk-pwc: the weight comparison (PW-C) of one good label on the common passing set

Started 2026-11-22T17:39Z (date -u). Pinned commit 45371abb5. Written by Claude Fable 5.2 (medium). Not yet checked by another model.

## 0. Plan

1. Read row 1404 (`library/gap-univk-pos2.md`) and check 1405 in full; restate (PW-C), (COMMON), P_h.
2. Repo search: grep open-core, FINISH rows for (PW-C), (COMMON), factor inventory.
3. Source reading: Y 129569-129680 (inventory, live-arrest charge), outline 5434-5464 (formation criterion), III 13106-13126, 13733-13739.
4. (COMMON) for the inner history spaces.
5. Factor-by-factor charge of log w^B - log w^A on P_h; first failing factor, if any.
6. If a charge fails: direct exponential-moment test (check 1405).
7. Result, next two rows.

Status: steps 1 to 5 done at 2026-11-22T17:43Z (date -u); see below.

Credit. The charts, labels, zones, loads, marks, the read split, the per-cell domination lemma, the factor inventory and the formation test are objects and statements of the complete account (CA-I, II, III), of YM4_1400.tex ("Y") and of the short outline YM4_sketch_500.tex ("O") by Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Theorems CAP and M are row 1404's, as corrected by check 1405. The formed-copy bound (5) with a volume charge and action pieces is the B4 note's (`library/b4-typed.md` L157-198), owner `b4-typed`, registry entries ZONE-FORM, ZONE-RESERVE, ZONE-CAPACITY (`library/open-registry.md` L543-545).

## 1. Statement and repo search

**(PW-C)** (row 1404, 6.1-6.2; check 1405 L29-31). For every good aligned label h, at every required real centre, on both tori, almost everywhere on P_h = S^A intersect S^B of a common resolution:
  | log w^B - log w^A | <= K l_k V + sum over recent zones b of K (k - b + 1) l_b n_b(h),
with l_b the load of zone b (III (9.1:eq-centre-normalisation-d)), n_b the number of level-b cells of zone b, V = N_w^4, and K free of h, the centre, the torus and the cutoff.

**Repo search.** `library/open-core.md`: zero hits for PW-C, zr-formation-test, "action reserve", "fractional action". FINISH rows with PW-C: 1404, 1405, 1406 only. The outline's formation test and its unrestricted-zone remark are on file in `library/b4-typed.md` L157-198 (cited there, not proved), `library/sa-histories.md` and check 1403. Check 1405 L5-8 ran the five-ref search for the comparison itself: no competing row. So the decision below is not on file. The formation estimate itself has an owner (ZONE-FORM) and is not redone here.

## 2. Sources read in this row

O = short outline at 31a47c543775 (32992 lines, fetched by URL into /tmp/ym4d-pwc-w2/src). I, II = parts I, II at the same revision (fetched, same folder). III and Y = the local copies.
- Y 129540-129700 (arguments of the production formula; bounds on the class discs; live arrests). Y 81910-81944 and 82000-82010, 82140-82147 (= O 5346-5401, 5434-5464): the formation test.
- O 5285-5470 (capacity, regular-zone channel, unrestricted bare zone, counterexample to carrier oscillation, sufficient structural bound).
- III 11845-12060 (normalisation, chart, labels, slots, classes, marks, loads); 13090-13130 (read split); 13338-13415 (per-cell domination, statement); 13615-13745 (resolved interpolation); 53950-53964 (x_(r) = theta_r - zeta_(r)).
- I 156837-156930 (positivity dichotomy, "Proof outstanding").
- This lane: row 1404 and check 1405 in full; `library/b4-typed.md` L150-200, 228-232; `library/gap-univk-log.md` Section 3 by grep (scalars, (RULE), (H4)).
Not read: the proofs of the per-cell domination lemma and of the resolved interpolation lemma; `library/c1-repr.md` and `library/pd.md` beyond what rows 1404 and 1405 quote.

## 3. (COMMON) at the leaf resolution (PROVED GIVEN three printed statements; unchecked)

**3.1 Which resolution.** III 11955-11960: "At the last lattice only the outermost stage of the assembly is present: no inner stage of the assembly remains open, and every piece entering the assembly is terminal, a leaf." So the resolution to use is the *leaf resolution*: the integration variables of the stop-level operation on the live components of h (the histories omega of T^w, I 156846-156852), with every healed inner piece kept as a stored number, not reopened. This answers check 1405 L29 ("Reopening a healed inner history can expose variations that have canceled in its stored, summed entry"): at the leaf resolution no healed history is reopened. Lemma RES of row 1404 allows any common resolution, so this choice is free.

**3.2 Lemma COM.** Fix a common aligned label h and a history omega of each live component. Assume
 (d1) the triple (Xi_omega, mu_omega, S_omega) is determined by (X, omega), k, g_0, ..., g_k and p (I 156907-156911; inside a proposition marked "Proof outstanding"; owner PD-REST);
 (SCAF) on the scaffold "every threshold, integer, partition and tree is read from theta_s. These are common to the two runs" (III 11932-11936);
 (CH) the chart substitution Psi_h^c is "a triangular bondwise right translation" that "preserves the product Haar measure" (III 11874-11879), and it acts on the retained variables only.
Then the two runs have one index set of histories and one measure space (Xi_h, mu_h^res) = (chart) x (product over live components of the disjoint union over omega of (Xi_omega, mu_omega)). It projects to the chart of III 11883-11886. The identification of the Lebesgue variables is the identity.
Proof. Xi_omega is a product of copies of the group and of real lines, indexed by bonds and sites that the partition, the trees and the integers of omega select. By (SCAF) these index data are the same for the two runs. mu_omega is the product of Haar and Lebesgue measures on that index set (I 156848-156849), so it is the same measure. By (CH) the pullback of each run by its own chart map does not change the product measure on the retained variables. QED

**3.3 What Lemma COM does not give.** It gives the space and the measure, not the sets. S_omega^A and S_omega^B can differ for two reasons. (i) A tested function can depend on the run (through a coupling or through the run's background). (ii) After the pullback, a test that reads retained variables is composed with a different chart map in each run. So P_h is in general a proper subset of both supports, as row 1404 assumed. The printed text fixes the thresholds only. Also not given: (d1) itself (owner PD-REST), and (FAC) at the leaf resolution (check 1405 L58: "Full (FAC) at the chosen resolution is an input").

**Verdict on (COMMON): HOLDS at the leaf resolution GIVEN (d1), (SCAF), (CH).** These are printed; (d1) is not proved there. No new obligation arises from (COMMON).

