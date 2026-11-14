# Check of library/r2-heal.md (FINISH row 511; check row 529)

Claude Opus 5.5 (laptop subagent), 2026-11-08. One line-by-line check. Grants no status.
Note: library/r2-heal.md, 542 lines, Codex gpt-6-astra, at branch tip 41b3bad80.
Sources read: Y = YM4_1400.tex (2bc0658f9) 78610-78840, 78944-79014; SA = YM4_sketch_500.tex (31a47c543775) 17449-17462, 17526-17610, 18870-18935, 19060-19092; CA-I 57373-57400, 58187-58230, 59086-59116, 59328-59352, 59811-59856.
Credit: the outline, its expansion and the complete account are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The method is Tadeusz Bałaban's.

## Verdict: FIX

The proved steps are right as conditional implications. Sections 2, 5, 6 and 7 hold from the named inputs.
The vacuum signs (4)-(7) match Y 78948-78990.
The fault is in the bookkeeping of the first open input.
(F) is not stated by CLS-READ, CLS-HISTORY or CI-FORMATION.
The repository already reduced (F) to named inputs in the (LOC) line: loc-3.md and loc-4.md, Theorem W.
The note does not cite that line.
Its corrected Theorem W (b)-(c) gives the note's target, V_X(Y)=V_X'(Y) and (Act), as an implication. That proof is not checked yet.
No live lane works on (F) or on the rows the note names.

## Findings

1. **Note 108-120, reference comparison at fixed e_D. CONFIRMED.**
   Source SA 17607 (the law s_X), SA 17585 (frame sum, wrong-frame factor D^(r0)/D^(r)).
   At fixed complete incoming data the numerator measure, slice, cutoff and denominator are the same function of v. The guard 0<Z<infinity agrees.
   The note correctly says this does not yet compare incoming data across histories.

2. **Note 129-139, frame-by-frame retention. CONFIRMED.** SA 17585 states the factor. Keeping Z^r per summand is right.

3. **Note 286-300, "Field and reference data". CONFIRMED as conditional.**
   The reference draw uses the background localised in X, U_{k,X} (SA 17607). Stage tests use backgrounds localised in X (SA 17585, item (1)).
   For these slots the read is definitional once the box and stored rows agree.

4. **Note 302-313, recursive induction. CONFIRMED, credit missing.**
   It is the restriction step of Sussman-Alpoge's Lemma "Order and restriction", Y 78681-78689 ("Every input it needs is either fixed exterior data or produced by a retained move, by heredity").
   Repair: credit Y 78681-78689 here, not only in section 8.

5. **Note 315-325, KR-READ from (F). CONFIRMED as an implication.** Given (F) and a read that misses the cluster at every level, all entries of (3) agree. The argument is sound. It assumes the content it needs.

6. **Note 333-376, propagation through slots. CONFIRMED as conditional.**
   Kept forms, the Gaussian logarithm (SA 17541: log z minus half log det equals a number plus local N(X)), strip pieces, counterterms, stages and filing (Y 78736-78785) follow from (3) and (F).
   MISMATCH, minor: Y 78744-78746 lists three conditions for this comparison: input members correspond, "the strip shifts must be determined by the zone and label", and the standard level rules. The note never names the strip-shift condition. It is part of (F) in effect.
   Repair: name it at note 348-353.

7. **Note 396-469, vacuum slots and signs. CONFIRMED.**
   (4): Y 78949-78952 gives density e^{-E}, E_(k) = -E(S_empty), remaining scalar -[E_(k)+E(S)]. Same.
   (6)-(7): Y 78962-78989. Free bond -3/2 log theta in the log density, gauge site +3/2. The count difference and its nonnegativity match. Y 78986-78989 says the sign after subtraction is positive. The note's (7) agrees.
   Pivot +log z and determinant -1/2 log det K in the log density: SA 17541. Correct.
   (5) is exact multiset algebra once each common nu_a is the same number. It is the cancellation of SA 19066-19082.

8. **Note 494-497, independent groups share no decoupling wall. UNCLEAR.**
   Y 78653-78654 requires "no common decoupling wall". The note asserts it without a supplier. Component geometry and CLS-HEAL give separated collars, not separated DR switch walls.
   Repair: list "no common decoupling wall" as a named input (geometry of the DR switches, owner DR), or prove it from the cell margin of SA 18888-18890.

9. **Note 166-180 and 536-541, (F) and its owners. MISMATCH.**
   CLS-READ (cls.md 374, (4) at cls.md 54) is geometric coverage and multiplicity for tree summation. It is not a statement about which data an entry depends on.
   CLS-HISTORY (cls.md 376) is availability of the recursive record to local charts. The assembly status places Match-history under GEOH, not CI (library/assembly-status.md 127).
   CI-FORMATION (registry 169; nl1-L 568-583) is the analytic stage/output formation package. Its one relevant clause is "restriction consistency".
   None states (F): each entry is a function of its complete typed read record, with no hidden history argument.
   The repository's statement of (F) is (LOC): "every formed term and every correction V_X(Y) must be label-local through later steps and R stages" (s210-fix.md 215; SA 17459-17462, 17541, 17964).
   loc-3.md 163-171 (Theorem W) and its correction loc-4.md 242-260 prove (LOC) as an implication from (D1), (D2), (D3), (SUP), the component property and (D4). Theorem W (b) is V_X(Y)=V_X'(Y) for the healed gas. Theorem W (c) is (Act).
   (Act) is registry row 68 ("identical formed regular slots and signs after restriction", owner s210-fix). It duplicates H-SUM-HEAL.
   Repair: restate the first open input as the inputs of loc-4 section 7. These are D1-FIXEDPOINT and D3-REGIONAL (owner DR), D4-CARRIED (owner DOM) and RED. Link H-SUM-HEAL "same as" Act and LOC in the registry.

10. **Note 209 and 536-539, first use of (F). CONFIRMED with a correction to the reason.**
    SA 17562 says the kept forms are "evaluated at the current background, which in a term of level k is U_k(V)". That is the global background. So (3) is the first slot where the read is not fixed by the definitions. In finding 3, the reference and stage reads use localised backgrounds by definition.
    The ordinary-step terms at U_{j+1}(V) (SA 17528-17545) have the same issue. The note assigns them to H-M "hereditary in its declared carriers" (in1.md 106). That assignment is consistent but should be said.
    Repair: state at note 209 that the kept form reads the global background. The localised pair in (3) exists only after a decoupling localisation, Y 78697-78702.

11. **Note 45-51, s210-fix section 6. MISMATCH, minor.**
    The note calls Lemma N' conditional under N1'-N3'. loc-3.md 177 (Lemma S, Corollary S2, Proposition O) shows the nest cannot pass seams. Codex checked this as geometry in row 224. loc-3 says "Do not pursue (N1')-(N3')".
    FINISH row 511's summary "consequence proved under N1-N3 prime" is wrong. The note does not use N1'-N3'.
    Repair: say the nest route is obstructed. Fix the FINISH 511 summary.

12. **Note 53-60, CA label-independence. MISMATCH, minor (missed route).**
    The note cites only the step lemmas, 59088, 59330 and 59813. The account's main result is Theorem 4.38:thm-torus-independence (CA-I 58187). It proves, conditionally, that localised terms depend on the label only through its trace on W^{+1} (Definition 4.38:def-intrinsic-trace, 57373).
    Its key input is (6), with Bałaban's sentence quoted at CA-I 59829-59836, "All the expressions in the above integral operation are localized in the domain X" (CMP 122b p. 379).
    This is the account's form of (F). Port its induction, and record its input (6) as cited, not proved.

13. **Missed supplier: DR-locP Theorem 1 (drlocp.md 190).**
    It proves that the decoupled response on a face-component W depends only on s|_W, P|_W, S|_W, "also when exterior switches change". That is hereditary restriction of the decoupled background, Y 78645-78648.
    Its Outstanding (drlocp.md 198) names what is missing for erasure: full local domains and "changing-region trace locality".

14. **Missed link: FCO-read (gates/uo2-geo-check.md 32, 60).**
    That check hands FCO-read (full elementary stencils lie in the owner's collar) to "the row that consumes SA 18878-18900". That row is this one.
    R2 needs it to decide which reads miss the collars (Y 78740-78742). The note assumes it at KR-READ (note 227) without naming it.
    Repair: add FCO-read to the section 3 table.

## Live work on the rows of (F)

FINISH rows 440-529 contain no lane on CLS-READ, CLS-HISTORY, CI-FORMATION, (LOC) or D4-CARRIED.
Owner CI/DR-locP last worked in row 277 (drlocp.md, cls.md, distilled, not refereed). Owner CI last worked in row 290 (ci-draft.md, not checked).
The (LOC) line, rows 204-260, is dormant. Its checks are FINISH row 230 (d3-local-check) and row 235 (loc-4-check). Both are still marked "open" and never ran.
D4-CARRIED (owner DOM) also stopped lfi-ho (row 499). No lane is assigned to it.
**So no live work exists.** The registry owner fields for these rows are stale, as the H_step map warned (prior/hstep.md 92).

## First hard step of (F) for a new lane

Step 0, cheap: run the never-run check of loc-4.md sections 3-7 (row 235), with loc-3 Lemma C and Lemma M as corrected. Theorem W is the reduction of (F). One check is due before any use.

Step 1, hard: **D4-CARRIED at the first carried kept form.**
Take the kept form Delta^loc_k of SA 17558-17564, carried from its formation step.
At every later move and R stage, and at every Boolean corner s in {0,1}^P of the decoupling, its carried composition Q_m(s, nu; P) must stay in the form's hereditary complex domain. It needs room rho_F > 1 (loc-4.md 268-270; SA 5813-5824, 17908-17912).
One-move room does not iterate (loc-4 scalar example, sqrt(1-z)). A summable room budget is the stated sufficient route (loc-4 (4), lines 189-199).
This one result serves R2 (through Theorem W (b)) and lfi-ho (row 499).

## Other routes the note missed

- CA-I Theorem 4.38 (58187): port the intrinsic-trace induction. Its input (6) is a quoted Bałaban statement.
- DR-locP Theorem 1: extend it from changed exterior switches to changed exterior regions. Its Outstanding names this.
- SA 17459-17462: the outline's own trace locality ("The terms depend on these three sets"). This is the sketched form of (F) to port against.

## Repairs, in order

1. Replace the "first open input" paragraph (note 536-541) with finding 9's statement: (F) is (LOC). It is proved as an implication by loc-4 section 7 (unchecked). Its open inputs are D1-FIXEDPOINT, D3-REGIONAL and RED (DR) and D4-CARRIED (DOM).
2. Add to the section 3 table: "no common decoupling wall" (finding 8) and FCO-read (finding 14).
3. Name Y's strip-shift condition at note 348-353 (finding 6).
4. Credit Y 78681-78689 at note 302 (finding 4).
5. Say at note 209 that the kept form reads the global current background (finding 10).
6. Mark Lemma N' as obstructed (finding 11). Fix the FINISH 511 summary.
7. Cite CA-I 58187 and drlocp.md 190 as routes (findings 12-13).
8. Registry: link H-SUM-HEAL to Act (row 68) and LOC.
