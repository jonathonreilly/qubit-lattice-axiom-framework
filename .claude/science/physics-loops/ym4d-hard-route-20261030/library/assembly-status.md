Node status is kept in t0-tree.md (row 391); this file is history for status.

# T0 assembly status, 2026-11-05

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05. Bookkeeping and reading only. No new mathematics. Not checked by another model. It grants no status. It does not edit `ym4-assembly.md` or any other file.

Read for this note: `library/ym4-assembly.md` (the skeleton, 568 lines); `FINISH.md` rows 263–277; the status line, Outstanding paragraphs, imports and Result of the frozen texts `p82.md`, `tp1.md`, `in1.md` (with Amendment 1), `pr-lay.md`, `nl1-L.md`, `st1-r4.md`, `ag1.md`, `hm.md`, `descent.md`; their gates `gates/p82-gate.md`, `tp1-gate.md`, `in1-gate.md`, `pr-lay-gate.md`, `nl1-L-gate.md`, `st1-gate.md`, `st1-r4-gate.md`, `ag1-gate.md`, `hm-gate.md`, `descent-gate.md` (first line and Verdict); the distilled texts `ci-form.md`, `td.md`, `td2.md`, `drlocp.md`, `cls.md`, `f-meas.md` (Outstanding paragraphs, imports and Result). I did not read the proofs. A line number "L" below is a line of the named file at this clone.

**Words.** *Frozen*: a fresh-session referee found no failing step (or one repairable step), the fixes were applied, and the text carries "Status: frozen". A frozen text is still an implication from its named imports. *Distilled*: Codex pass 2 exists; no referee yet. *Drafted*: pass 1 only. *Not started*: no part text in the draft → distil → referee → freeze process (FINISH row 263). Older library notes may still carry the skeleton's [C], [P], [SP] or [SS]; I repeat those marks as the skeleton gives them and do not upgrade them.

**Where the skeleton's names went.** No frozen or distilled text uses the skeleton's open-input names ST-cov, ST-map, ST-phase, ST-wit, ST-drop, BG-lay, PR-H, LF-mass, LF-2.8, LF-2.10, LF-2.13, IN-C4, OL-incr, OL-nl, NL-ER7, TP-F2, TP-F3, TP-7.6, AG-rarity, WT-NT2 or WT-X1 (grep count zero in all fifteen texts; IN-order and IN-C4 occur only in `tp1.md` and `cls.md`). Every map from a skeleton name to a later name below is my reading of the two texts. Where I could not match them, I say so.

## 1. The 21 skeleton parts

### 1.1 Summary table

| Part | Status now | Text and gate | Named Outstanding items (names only; quotes in §1.2) | Waits on |
|---|---|---|---|---|
| LG1 | not started (skeleton: [C]) | `am1-port.md` etc.; `gates/o4-check-1.md` §1 | none (ym4-assembly L162: "No open input.") | — |
| FP1 | not started (skeleton: [C]) | `flat-port.md` etc.; `gates/flat-port-gate.md` | none named | — |
| PR1 | **frozen in two pieces**; rest open | `p82.md` + `gates/p82-gate.md`; `pr-lay.md` + `gates/pr-lay-gate.md`. P81+CRIT drafted (`p81-crit-draft.md`), folded into frozen ST1 Lemmas 5–6 | pr-lay: "D for the actual domains", "the actual Gaussian comparison", PR1(5b). p82: none (conditional on I1–I8). Skeleton PR-H: no later text | ST1 (D), H-M, layered-a3 |
| BG1 | not started (skeleton: (2), (3) [C]; (4)–(5) [P]; (6) [P]; (7) [O]) | `a1-balaban.md`, `intrinsic-dom.md`, `oa7.md` | skeleton BG-lay | ST1 domain admission |
| ST1 | **frozen** (round 4, Amendment CV) | `st1-r4.md` (with `f-meas.md` folded) + `gates/st1-r4-gate.md`; round 3 `gates/st1-gate.md` | CI, FM-match, FC-mean-match, FC-test, FC6-history (unused) | NL1/LF1 (CI); DR; P82°–M1 |
| FC1 | not started (skeleton: [SP]) | SA L1379–2084 only | none named; TP1's FREE package is open | rebuild |
| OL1 | not started (skeleton: partly [C], Theorem V [P]) | `b-value.md`, `prefactor-loc.md`, `b2-extract.md` | skeleton OL-incr, OL-nl; IN1's H-OL | — |
| NL1 | **frozen in one piece**; four pieces distilled | `nl1-L.md` (Tq0 branch) + `gates/nl1-L-gate.md`; distilled `ci-form.md`, `td.md`, `td2.md`, `drlocp.md`, `cls.md` | nl1-L: six Outstanding paragraphs; CI (all of Theorem 7's hypotheses) | ST1 (DR, domains), H-M, LF1 |
| LF1 | not started (skeleton: several links [C]) | `c1-repr.md`, `geo*.md`, `floor-screen.md`, `sa-2.8-terms.md`, `s210-fix.md`, `sa-2.13*.md` | via IN1: H-G, H-C, H-E, H-O, H-SUM; via AG1: (ANC) | NL1, ST1 |
| SC1 | not started (skeleton: freezing [SP]; profile induction [P]) | `src-array.md` | via TP1: PRES | NL1, IN1 |
| IN1 | **frozen** (with Amendment 1) | `in1.md` + `gates/in1-gate.md`; Amendment 2 proposed in `cls.md`, not applied | H-M, H-OL, H-SF, H-LF, H-G, H-C, H-E, H-O, H-SUM, each with its Outstanding paragraph | FP1/PR1/NL1/OL1/ST1/SC1/LF1/BG1 |
| UV1 | not started (skeleton: criteria [C]; D1 [O]) | `d1-floor.md`, `p2-floor.md` | D1 for the actual construction (ym4-assembly L347) | IN1, SC1, LF1 |
| AG1 | **frozen** | `ag1.md` + `gates/ag1-gate.md` | (ANC), (OS), NL1's full-source distance bound, QL′ domain/threshold, fixed-history density | LF1, NL1, IN1, BG1 |
| SR1 | not started (skeleton: [C] as implication from D1) | `d2-d4.md`, `growth-qf3.md` | none; open only through UV1 | UV1 |
| CL1 | not started (skeleton: [C] as implication) | `s4-s6.md`, `cone-o6.md` | none | SR1 |
| TP1 | **frozen** | `tp1.md` + `gates/tp1-gate.md` | FREE package, PRES identification, REG with TP1's G-ID, AMP, AG upstream, IN-order | FC1, SC1, LF1, AG1, IN1 |
| RO1 | not started (skeleton: [C] as implication from D1, TU10) | `ui-port.md` … `ac-port.md` | none | UV1, TP1 |
| PH1 | not started (skeleton: [C]) | `cluster-port.md` | none | SR1, CL1 |
| WR1 | not started (skeleton: [C] as implication) | `wightman.md` | none | RO1, PH1 |
| WT1 | not started (skeleton: Lemma W [P]; NT2 [O]) | `t0-skeleton.md`, `parts/witness.md` | skeleton WT-NT2, WT-X1. NT1 is now also proved inside frozen TP1 (Lemma 7.2) | TP1 |
| AS1 | not started | — | all of the above | all |

Counts by part: **frozen as a whole part 4** (ST1, IN1, TP1, AG1); **frozen in pieces 2** (PR1: P82 and PR1(5a); NL1: input (L) and the CI reduction); **distilled only 0** whole parts (six distilled texts sit under NL1, IN1 and ST1); **drafted only 0** whole parts (three pass-1 texts, all folded or dissolved: `p81-crit-draft.md`, `lev-core-draft.md`, `os-draft.md`); **not started 15**. Frozen texts: 9.

### 1.2 Outstanding items, quoted, with what each waits on

Only parts with a frozen or distilled text are listed. For the other fifteen, the skeleton's §5(d) is still the latest status.

**PR1.**

- `p82.md` L642: "**Status: frozen.** Reopens only on a `wrong` signal or when an import it reads changes." No Outstanding paragraph. Result L646: "Theorem P82 at the real critical reference. This is the item denoted **P82°** in a3-derivative; it does not prove the complex-reference extension, the independent-current system, periodisation, P81 or the subsequent nonlinear theorem." Imports I1–I8 (flat-port, a3-balaban, A1 with F0, Balaban CMP 99 Prop 6). The gate (L39) adds: "One claim depends on the reading in F1: that \(\varepsilon_P\) depends on \(L\) alone."
- `pr-lay.md` L372: "D for the actual domains, IN1's H-M and PR1(5b) stay open, as stated."
  - L254: "**Outstanding — D for the actual domains.** SA 6141–6155 defines layer radii on represented domains; it does not verify (19) globally for every input of the domain obligation CI-maps of [nl1-L.md](nl1-L.md) (Theorems 4 and 7)." Waits on: ST1 records and the actual roster (DOM, §2).
  - L328: "**Outstanding — the actual Gaussian comparison.** Theorem 8 supplies the precision hypotheses of frozen IN1 Lemma 2. It does not supply IN1's H-M". Waits on: H-M (§2).
  - PR1(5b) = layered-a3 (1), "still open via Lemma RC" (FINISH row 272). Consumer named there: "the stage response". Frozen `st1-r4.md` names no layered-a3 import (grep count 0). I cannot tell from the texts whether the T0 path still reads PR1(5b).
- Skeleton PR-H (ym4-assembly L188): "(H-ct) (SA L7864) and (H-prof)". No later text mentions it. Status unchanged.

**ST1** (`st1-r4.md` L1696): "**Status: frozen** (round 4, with Amendment CV), as a conditional theorem. Outstanding, all named: CI (NL1/LF1), FM-match, FC-mean-match, FC-test, FC6-history (unused)."

- CI: Theorem 14 hypothesis 4, L1544: "CI supplies the activity \(f\) on the target domain with bound \(b_f\)." Waits on: NL1/LF1 (§2, node CI).
- L1094: "**Outstanding FM-match.** This closes the real measure change for the specified Haar/delta operation, including SA 17531 with its full stored density. It does not prove term-by-term equality with a separately frozen CA-I (1.60) by assigning its symbols new values." Waits on: matching the actual shifted background to CA-I's presentation.
- L1254: "**Outstanding FC6-history and FC-mean-match.** FC6 is not, as stated in pass 1, a proved counterexample for the actual conditional mean of an admitted stored history."
- L1329: "**Outstanding FC-test.** The cited ST1 inputs do not supply FC2's premise for every stored stage."
- L1445: "**Outstanding F-contour.** Full closure for the actual stored stage still requires **FC-mean-match** … and **FC-test** … The positive reference precision, its complex perturbation bound, and the full remainder bound remain the NL1/LF1 inputs."
- Inputs that are hypotheses, not Outstanding (§2, L122ff): GEO, AV/CURV, A1/F0/REG, "P82°, M1 and the derivative theorem", PROF/RCG4, OPS/SLICE/UNQ, "DR, including its specification at one", CH, RUN, GEO-mark, RUN-low, GEO-box, BOX, ST-test, "GEO-slot (new input)", "ST-test\(^{\rm hol}\) (new input)", LOC. L135: "the remaining matching item on this route is M1." Result L1665: "Other imports are A1/F0/REG, AV/CURV, PROF/RCG4, OPS/SLICE/UNQ, CH, the actual DR construction and main-step coordinate/source supply."

**NL1.**

- `nl1-L.md` L698: "**Status: frozen (Tq0 branch).**" Outstanding paragraphs:
  - L154 (H-FL): "**Outstanding:** F8 leaves the stored-threshold comparison explicit; a small completed source alone is not the raw-datum bound (6)."
  - L172 (H-DR): "**Outstanding:** this uniform complex-source estimate, including its current, and this precise row-locality clause strengthen the printed ST1 (16)." Waits on: DR (ST1).
  - L195 (H-ACT): "**Outstanding:** H-ACT on the changed domains is CI plus the actual term identifications."
  - L494: "**Outstanding — the proposed PAN consequence.** Lemma 5 does not prove the draft's replacement of PAN Lemmas 7.4–7.6. … it does not show \(D_f\ge10LM\check R_i-C\) for this full source." This is the "NL1's full-source distance bound" that AG1 needs.
  - L537: "**Outstanding:** the claimed full-interface counterexample under \(r_\iota=\alpha_\iota\epsilon_m\) must be replaced." Nothing on the path needs it (§2).
  - L608: "**Outstanding — what this reduction does not supply.** The draft's CI-form states a pointwise output bound and then infers (18). That inference is invalid". Waits on: "The actual locally normal Mayer estimate, and LF1's external-parameter-independent Borel domination".
  - Theorem 7 (L567ff) hypotheses: CI-base, CI-maps, CI-Gauss (= IN1 H-M), CI-form.
- Distilled, not refereed: `ci-form.md` (Outstanding H-D L38, H-G/H-S L56, H-C L67, H-W L85, regular-gas scope L352, "TD is a bound, not this identity" L368, H-I and LF formation L394); `td.md` (complex island amplitude L63, actual Gaussian identification L235, "draft Theorem 10.2 and `(File♮)`" L375; Result L482: "ordinary-distance TD remains **Outstanding**"); `td2.md` (X° and G-ord L82, external-pair locality L297, draft Prop 8.1 L329, logarithmic-collar repair L331); `drlocp.md` (actual specification L69, full local domains L198, formation and class matching L522); `cls.md` (complete reads L147, actual multiplicities L175, exterior smallness L324, scale/rate transfer L369; Result: "Proposition 12 is a conditional transfer of IN1, **not a proof of (Cls+) from unchanged imports**").

**IN1** (`in1.md` L664: "**Status: frozen.**"). Result L681: "Its imports are H-M (FP1/PR1 and actual UM), H-OL (OL1), H-SF (NL1/ST1/SC1), H-LF, H-G, H-C, H-E, H-O and H-SUM". Outstanding paragraphs:

- L108: "**Outstanding — actual matrix envelope.** Lemma 2 below proves (9) for an auxiliary path-weighted construction under a *global* gap hypothesis. It does not identify that construction with H-M or prove heredity." (H-M.)
- L118: "**Outstanding — coefficient identification.** … OL1 must supply the companion, normalization and localization sum". (H-OL.)
- L143: "**Outstanding — formation and domains.** This is the actual formation theorem, not its numerical output bound alone." (H-SF.)
- L159: "**Outstanding — actual genealogy.** The supplied local geometry and [geo5c-count.md](geo5c-count.md) do not verify (14), the waiting rule and this coding map for all actual histories." (H-G.)
- L173: "**Outstanding — certificates.** Totality alone does not prove the contrapositive certificate for failure of existence." (H-C.)
- L188: "**Outstanding — common domination.** The prepared modulus bound of [gates/sa-2.8-terms-gate.md](../gates/sa-2.8-terms-gate.md) does not prove (16) over evaluation fibres." (H-E.)
- L190: "**Outstanding — full admission.** … It does not construct the gauges, potential bounds or towers in R4–R6. … H-E requires their independent verification at every later read."
- L204: "**Outstanding:** this is SA R25 (6291–6310). Neither the mass estimate nor a bound on \(\operatorname{Re}\Psi\) implies (18)". (H-O.)
- L215: "**Outstanding — sums and stability.** These are separate imports." (H-SUM.)
- L329: "**Outstanding — heredity is stronger than block factorization.**" (three-site chain; feeds H-M.)
- Amendment 1 (L666–675): floors L > L₀♮ and κ ≥ κ₀♮(L); "This amendment remains conditional on td.md surviving its referee".

**AG1** (`ag1.md` L1297): "**Status: frozen**, as a conditional theorem. Outstanding inputs, all named: (ANC), (OS) for the whole live-attached sum, NL1's full-source distance bound, the QL' domain/threshold verification, and the fixed-history density identification."

- L228: "**Outstanding — deriving this interface from (RS) and (BGL).** … The quoted background theorem requires its collars to lie in single layers and does not automatically establish that the new inner boundaries have this property." (QL′; waits on BG1/LF1.)
- L291: "**Outstanding — identification of (11).** Product windows and a Gaussian extraction do not identify the full fixed-history density." (Waits on LF1/NL1.)
- L651: "**Outstanding — old-object summation after capping.** Equations (20)–(22) do **not** give PAN Lemmas 7.5–7.6." This is the content of (OS) (change log L1288, item 3).
- (ANC), change log L1287: "**(ANC)** added as a named LF1(2) input (SA 23328, read by the lead); this repairs the first failing step. Outstanding as an LF1 verification."
- Result L1319: "The imported (LT), (R2), (Q), and (L) are not established by this manuscript." ((L) is frozen nl1-L Theorem 4, conditionally.)

**TP1** (`tp1.md` L634: "**Status: frozen.**"). Imports FLOW, FREE, PRES, REG with G-ID, AMP, AG, STATE, LIMIT (gate Verdict). Outstanding paragraphs:

- L87 (FREE): "**Outstanding:** the full volume-uniform package (2.3)–(2.4) is imported, not proved here." Waits on FC1 and the terminal bound on \(R_j\).
- L113 (PRES): "**Outstanding:** [ref-73.md](ref-73.md) establishes an abstract transport identity; identifying its logarithm with this formed exponent, with the following bounds, remains an input." Waits on SC1.
- L130 (REG): "**Outstanding:** the draft's TP-cx only compares a domain when its background is regular. … Its last equality, called **G-ID**, is also an import". Waits on LF1/BG1.
- L146 (AMP): "**Outstanding:** these bounds, particularly the factors \(x^{-1},x^{-2}\) and only logarithmic prefactors, are not supplied by SA's displayed age-amplitude bound." Waits on LF1/SC1. (`ag1.md` L1211: "TP1's separate amplitude hypothesis remains separate.")
- L154 (AG): "**Outstanding:** (CL)(P) requires derivative and Hessian bounds on the non-Gaussian conditional exponent throughout the small-field region." Now supplied by frozen AG1 Theorem 12 under AG1's own Outstanding list.
- L184: "**Outstanding (IN-order):** [c4-order.md](c4-order.md) flags the need for an early uniform UM cost envelope; [in1-draft.md](in1-draft.md), Part A, is a proposed supplier with its own inputs." Now supplied by frozen IN1 Lemma 3 conditionally on H-M (§4, item 5).

**H-M texts (owned by FP1/PR1/NL1 per `in1.md` L99).**

- `hm.md` L482: "**Status: frozen**, as a conditional theorem on R4 intersect Rep. Outstanding, named: the all-core conclusion (descent; `library/descent-draft.md`), G-ID for the physical clause, F for the completed gauge form."
  - L37: "**Outstanding — all-core representatives.** R4, and the additional R5–R6 conditions defining SA's hereditary core, do not imply Rep."
  - L371: "**Outstanding — actual-family and stage interfaces.** … To consume it as frozen IN1 H-M, the actual construction must use these full-read carriers, and its whole declared local domain must be admitted to the representative class or supplied with a compatible descent theorem."
- `descent.md` L297: "**Status: frozen**, as a conditional theorem. Outstanding, named: local formation and vacuum bounds."
  - L285: "**Outstanding — actual formation and admission.** … Nor does this note put every ST1 chain domain inside this R4 domain."

## 2. The open-input graph

### 2.1 Merged nodes

Each node merges items that state the same obligation, or parts of one obligation, under different names. "Same" is my reading; the evidence column gives the lines.

| Node | Merged names | Evidence for the merge | Status | Feeds |
|---|---|---|---|---|
| **P82M** | P82°–M1 and (15) on the layered class; a3-derivative M1 | st1-r4 L129–135 ("the remaining matching item on this route is M1"); Result L1665 | P82° frozen at a real critical reference; M1 and the layered class open | DR, ST1 Thm 14 hyp 1 |
| **PRH** | skeleton PR-H: (H-ct), (H-prof) | ym4-assembly L188 only | open; no later text | PR1 A2 (consumer as in skeleton) |
| **PR5b** | PR1(5b) = layered-a3 (1) | pr-lay L372; FINISH row 272 | open | stage response; **cannot tell** whether st1-r4 reads it |
| **GEOH** | IN1 H-G actual genealogy; AG1 (ANC); ST1 GEO-mark, GEO-box, GEO-slot; cls Match-history and Lift; skeleton "rest of C2 [O]" (LF1(2)) | in1 L159; ag1 L1287; st1-r4 §2; cls A4 | open (hypotheses on the actual history) | ST1, IN1, AG1, CI filing |
| **DR** | ST1's "actual DR construction"; nl1-L H-DR strengthening; drlocp "actual specification" and "full local domains"; td "Keep ST1's actual DR construction open" | st1-r4 L1665; nl1-L L172; drlocp L69, L198; td L486 | open. DR-locP proved conditionally for the library's DR (drlocp Theorem 1, not refereed) | ST1 Thm 14 hyp 3, CI (TD, filing) |
| **DOM** | pr-lay "D for the actual domains"; nl1-L CI-maps; ci-form H-D; st1-r4 Thm 14 hyp 2 "complex input membership remains this hypothesis"; IN1 "full admission"; descent "put every ST1 chain domain inside this R4 domain"; ST1 inputs BOX, ST-test, ST-test^hol, LOC, RUN-low for the actual history; skeleton BG-lay and ST-cov (reading) | pr-lay L254 names CI-maps; ci-form L36 includes PR-lay D in H-D; descent L285 | open | H-M, CI, IN1 H-E |
| **HM** | IN1 H-M; nl1-L CI-Gauss; ci-form H-G/H-S; td "J" (actual Gaussian identification); hm all-core and actual-family items; descent local formation and vacuum bounds; hm/descent G-ID (physical clause); UM4–UM6, UM14 at all pairs (FINISH row 274) | nl1-L Thm 7 item 3 names "frozen IN1 **H-M**"; ci-form L56; td L235; hm L371 | supplied on R4∩Rep (hm, frozen) and on all R4 for the Y3-form family (descent, frozen); actual-family identification open | CI, IN1 Theorems 11–12 and Lemma 3 (IN-order) |
| **CI** | ST1 CI; nl1-L Theorem 7 (CI-base, CI-form); ci-form H-C, H-W, H-I, H-O, H-F; TD (ordinary TD; TD-natural); complex island amplitude; JC; filing (Cls)/(Cls+) with Match-SF/O, Match-read/file, Match-heal/LD; nl1-L H-FL, H-ACT; IN1 H-SF (the CI part); skeleton (D4) inside NL1 | st1-r4 L1696 "CI (NL1/LF1)"; ci-form Result; td2 L398; cls L9 "through CI's exempt-term filing" | open. Pieces proved conditionally: ci-form Thm 5 (regular gas), td TD-natural, td2 ordinary TD under X°, G-ord, drlocp (JC_τ) and filing bound, cls width and filing bounds | NL1 step, IN1 H-SF, AG1 (CL) |
| **FCON** | ST1 FC-mean-match, FC-test (F-contour) | st1-r4 L1445 | open | CI wherever a stage contour is consumed |
| **FMM** | ST1 FM-match | st1-r4 L1094, Thm 14 hyp 5 | open | only "To identify a separately frozen CA-I \((A_j,B_j)\) presentation" |
| **SF** | IN1 H-SF error bound (11); TP1 FLOW (2.1) \(e_j\); skeleton OL-nl | in1 L120–126; tp1 L54–60; ym4-assembly L262 "(supplied by IN1)" | open (part of the NL1 step) | IN1 E1, TP1 FLOW |
| **OL** | IN1 H-OL (coefficient identification); OL1(1) B2 in full [SS]; OL1(3) Theorem V [P] | in1 L110–118; ym4-assembly L268 | open | IN1 |
| **LFI** | IN1 H-C, H-E, H-O, H-SUM; skeleton LF-2.8 (= H-E common domination), LF-2.10 (= H-SUM healed sum), LF-2.13 (= H-SUM loaded labels) | in1 L188 cites `sa-2.8-terms-gate.md` under H-E; in1 L206 "The actual healed sum is exact"; L215 "loaded-label sum"; FINISH row 266 names "the healed-family Mayer identity (LF-2.10)" | open. Skeleton LF-mass (C3) is now IN1 Theorem 10, conditional on H-LF, H-G, H-C, H-E | IN1 Theorems 10–12 |
| **SRC** | SC1 whole; TP1 PRES; UV1 D1 | tp1 L103–113; ym4-assembly L316, L347 | open | SR1 → CL1, PH1, RO1, TP1 STATE |
| **AGI** | AG1 (OS), QL′, fixed-history density; (LT), (R2), (Q) | ag1 L1297, L1319 | open | AG1 Theorem 12 → TP1 AG |
| **TPI** | TP1 FREE (with FC1 [SP]), REG with TP1's G-ID, AMP | tp1 L87, L130, L146 | open | TP1 Theorem 3.1 |
| **NT2** | WT-NT2, WT-X1 | ym4-assembly L452–453 | open; definition is a working draft (GOAL.md) | AS1 (T0(5)) |
| **PHA** | Phase A freezes: LG1, FP1, SR1, CL1, PH1, RO1, WR1 | ym4-assembly L515 | not open mathematics; distil and referee of checked notes | AS1 |

### 2.2 Edges

"A → B" means B needs A.

- P82M → DR → DOM → HM → CI
- GEOH → DOM, GEOH → CI (filing), GEOH → LFI, GEOH → AGI
- DR → CI (TD, DR-locP, filing)
- FCON → CI (stage contours)
- CI → SF; CI + OL + HM + LFI + GEOH → IN1 (Theorems 10–12)
- IN1 → SRC (SC1, D1) → SR1 → CL1 → PH1; SR1, CL1 → RO1, WR1
- CI → AGI (via (CL), (L), full-source distance) → AG1 → TP1
- IN1 + SRC + TPI + AG1 + SR1/CL1/PH1 → TP1 → RO1 (TU10), WT1 (NT1 is inside TP1 Lemma 7.2)
- TP1 → NT2
- PHA, RO1, WR1, PH1, TP1, NT2, IN1 → AS1
- PRH → PR1 (consumer as in the skeleton); PR5b → stage response (consumer **unclear**)
- FMM → (only a CA-I presentation)

### 2.3 Items that nothing on the path to T0 needs

| Item | Why, with the line |
|---|---|
| OL-incr (OL1(4), the increment law) | in1 L679: the leading logarithm "needs neither monotone increments nor their pointwise convergence"; tp1 L647: "Use telescoping instead of an unproved increment law or monotonicity". |
| FC6-history | st1-r4 L1696: "FC6-history (unused)". |
| CA-III Lemma 7.3, nonconvergence of first-passage offsets (skeleton IN1(c) left this unsettled) | tp1 L593: "Nonconvergence of first-passage offsets is not used." |
| Lemma OS | FINISH row 265: "not needed; its premise is false"; dissolved (Theorem OS′). |
| nl1-L L537, the counterexample under \(r_\iota=\alpha_\iota\epsilon_m\) | nl1-L L540: "Tq is a sufficient design here"; st1-r4 uses (Tq0). |
| The Tq-with-lifts branch of (L) | nl1-L L691: "is withdrawn". |
| (5-sw) | drlocp Result: "Dropping (5-sw) is valid for this route". |
| (File♮) | td L488: "Withdraw `(File♮)`". |
| NL-ER7 for CORE | st1-r4 L1661: "No ER7 or \(b_1^2\le c_\natural b_0\) assumption is needed for CORE." Whether the NL1 step needs (ER7) elsewhere: **cannot tell** from the frozen texts. |
| FM-match | Needed only for a CA-I presentation (st1-r4 Thm 14 hyp 5). **Cannot tell** whether the T0 path uses that presentation. |
| WT1 Lemma W (NT1) | Not needed if TP1's route is used: tp1 Lemma 7.2 proves NT1 "on each realized component" (L550). Both are conditional. |
| TD-natural | td2 L404: "The natural-gas estimates are not used by the ordinary proof; that does not authorize deleting frozen floors." Off the path if the ordinary-TD route closes CI; IN1 Amendment 1's floors stay either way. |
| T1 joint torus extraction | ym4-assembly L528: "serves T1 only". |

## 3. The critical path to T0

Each item lists its owner part and the files with the best current attempt. Each depends only on earlier items. Items that are parallel in the graph are kept in one order for readability.

| # | Open statement | Owner | Best current attempt |
|---|---|---|---|
| 1 | **P82M.** M1 (multiplier normalization) and the derivative bound (15) uniformly on the admitted layered class, on top of frozen P82°. | PR1 | `p82.md`; `a3-derivative.md` §7.5 and L537; `st1-r4.md` §2 L129–135 |
| 2 | **PRH.** (H-ct), (H-prof), as the skeleton states them. No later text; kept because AS1 lists it (ym4-assembly L548). | PR1 | none since the skeleton |
| 3 | **GEOH.** The actual-history geometry: genealogy and coding (14), (ANC), GEO-mark, GEO-box, GEO-slot, Lift. | LF1(2) | `in1.md` H-G; `ag1.md` L1287; `st1-r4.md` §2; `cls.md` §§2–4; `geo5c-count.md` |
| 4 | **DR.** The actual regional response: holomorphic, (16), specification at one, restriction and component splitting, with H-DR's complex-source estimate and row locality, and DR-locP for that specification. Includes the two-current identification of drlocp L69. | ST1 | `drlocp.md`; `st1-r4.md` §2 (DR); `nl1-L.md` L159–174; `td.md` (DR-row); `p81-crit-draft.md` (Specification S1); `o1-decoupled.md`, `dec-field.md` |
| 5 | **DOM.** Full complex-domain admission for the actual roster: PR-lay's D (19), ST1 Theorem 14's complex input membership, BOX, ST-test, ST-test^hol, LOC and RUN-low on the actual history, and every ST1 chain domain inside R4. (PR1(5b) may belong here; cannot tell.) | ST1 (with NL1) | `pr-lay.md` Theorem 8, Lemmas 5–7; `st1-r4.md`; `ci-form.md` H-D; `layered-a3.md` |
| 6 | **HM.** The actual Gaussian family: fix the gauge form (descent Theorem B's Y3 form, or show actual triples are Rep), identify the step's carriers with hm's full-read carriers, prove the local formation and vacuum bounds, and G-ID for the physical clause. | PR1/NL1 (IN1 import) | `hm.md`; `descent.md`; `pr-lay.md`; `in1.md` Lemmas 2–3; `inv-root.md`; `carrier-adopt.md` §6; `um-novelty.md` |
| 7 | **FCON.** FC-mean-match and FC-test, wherever a stage contour is consumed. | ST1 | `st1-r4.md` L1254–1460; `f-meas.md` §§3–5 |
| 8 | **CI.** CI-base and CI-form on the whole domain with normal (Mayer) domination: the regular gas (H-C, H-W, H-I), the exempt terms (ordinary TD with X° and G-ord, complex island amplitude), filing ((Cls+) with Match-SF/O, Match-read/file, Match-heal/LD), and nl1-L's H-FL, H-ACT and full-source distance bound. | NL1/LF1 | `nl1-L.md` Theorem 7; `ci-form.md`; `td.md`; `td2.md`; `drlocp.md`; `cls.md` |
| 9 | **SF + OL.** The NL1 one-step formation theorem (IN1 H-SF, with the error bound (11)), NL1(1) B1 for the actual gas, and H-OL: localized-to-bulk coefficient identification, companion normalization, OL1(1) B2 in full, a check of Theorem V. | NL1, OL1 | `in1.md` H-SF, H-OL; `b4-induction.md`, `b4-step.md`; `b-value.md`; `prefactor-loc.md`; `b2-extract.md` |
| 10 | **LFI.** IN1's LF1 imports: H-C certificates (the 4D nonlinear estimate (15)), H-E common domination and later admission, H-O (SA R25), H-SUM (healed sum, loaded labels, stability floor). With 1–9 this closes IN1 (C4, flow, first passage) by its frozen Theorems 10–12. | LF1 | `in1.md` L161–215; `sa-2.8-terms.md`; `s210-fix.md`; `sa-2.13.md`, `sa-2.13-2.md`; `inn-fix.md`; `c1-repr.md` |
| 11 | **SRC.** SC1 inside the step (freezing [SP] rebuilt, profile induction checked), TP1's PRES identification, and UV1's D1 for the actual construction. | SC1, UV1 | `src-array.md`; `ref-73.md`; `d1-floor.md`; `p2-floor.md` |
| 12 | **AGI.** AG1's (OS) for the whole live-attached sum, QL′ (BGL with single-layer collars), the fixed-history density identification, and (LT), (R2), (Q). | AG1 (LF1, NL1) | `ag1.md`; `ag1-tt-draft.md`; `pan-draft.md`; `nl1-L.md` Lemma 5 |
| 13 | **TPI.** TP1's FREE (FC1 rebuilt, with the terminal bound on \(R_j\)), REG with TP1's G-ID (all-level comparison, common completion), and AMP. | TP1, FC1 | `tp1.md`; `tp1-draft.md`; `tu10.md`; SA L1379–2084 for FC1 |
| 14 | **NT2.** WT-NT2 and WT-X1. The definition is a working draft (GOAL.md). | WT1 | `parts/witness.md`; `witness-running-tests.md`; `nt2-free-value-by-hand.md`; `route-decisions.md` §8 |

Not open mathematics, but required before AS1: **PHA**, the Phase A distil and referee of LG1, FP1, SR1, CL1, PH1, RO1, WR1 (ym4-assembly L515). It depends on nothing above and can run at any time. Then AS1.

What this list does not settle. Items 2 and 5 (PR1(5b)) are kept or flagged because no later text drops or places them. If a referee shows either is unread on the path, it leaves the list.

## 4. Disagreements and stale imports

Each entry gives the texts and lines. "Stale" means a frozen text's import has since been corrected or supplied by a later text. None is a counterexample to a frozen theorem unless I say so.

1. **Comb versus mean-contour (axial) representative.** `st1-r3.md` L41: "The canonical background representative uses combs in order (4,3,2,1)." `st1-r3.md` L345, Lemma 5: "one real regular critical orbit and its canonical comb representative." `f-meas.md` FC6 (L364–388) and the reopening notice `st1-r3.md` L1114 lead to Amendment CV. `st1-r4.md` L41: "**Amendment CV:** the canonical background representative uses the averaged contour variable". CV touches st1-r3 lines 41, 128, 276–277, 339, 345, 581, 1064 (`st1-r4-gate.md` Verdict). **Stale import:** frozen `nl1-L.md` L127 imports "ST1 ([st1-r3.md](st1-r3.md)) Lemmas 5, 8 and 11"; Lemma 5 is a CV-touched line. nl1-L has not been re-read against st1-r4. Whether its Theorem 4 is affected, I cannot tell from the text. Frozen `pr-lay.md` L228 and L366 cite st1-r3 Lemma 10 (59), which is not in CV's list. `pr-lay.md` L60 says only "\(\mathcal M^kU\) block axial on the active blocks"; it does not say which contour. `hm.md` L35 fixes the averaged contour ("not that links on a tree equal \(I\). SA 7178 distinguishes these gauges"), which agrees with CV. `a1-balaban.md` L2501: "The contour variable can be either the comb or the actual mean." Pass-1 `lev-core-draft.md` §6.3 builds LEV with the comb gauge; st1-r4 keeps "Auxiliary comb gauges used to bound curvature" (L41), and its gate fix 4 narrows "LEV's contour claim … to what it proves" (L1693).

2. **Absolute versus relative gauge Hessian; Rep versus all of R4.** `hm.md` L33 imposes **Rep** on the class \(\mathcal K\); L37 keeps "all-core representatives" Outstanding. `pr-lay.md` L60 fixes the axial representative and does not assert full covariance. `descent.md` Theorem A (L151): with the absolute CF2 form a central flip gives an R4 triple where the real gap fails. Theorem B (L196): the Y3 relative form gives the all-R4 envelope. Proposition C (L251): no extension agrees with the absolute precision on R4∩Rep and keeps both the real tie and real-gauge covariance. `descent.md` L311: "Frozen pr-lay and hm are not refuted. … the replacement genuinely changes those matrices." So the frozen pr-lay and hm statements hold only on Rep. A consumer on all of R4 must use descent's family, whose early constants may change (descent L97: "Replacing the form may change the early constants and these final ceilings"). Which form "the actual step" uses is not decided: descent L314 says SA 11243–11247 leaves it to "the model being considered". `h-walk.md` §2.1 also uses the absolute form on non-axial fields (descent L312). **Stale pointer:** `hm.md` L482 names "`library/descent-draft.md`"; the frozen text is `descent.md`.

3. **Two statements named G-ID.** `tp1.md` L130: G-ID is the equality that "these energies have exactly the Gaussian model (2.6)". `hm.md` L45: "**G-ID (physical clause only).** At an admitted complete physical pair the Gaussian part of the actual step has covariance \(\mathsf A(P_W)^{-1}\). … This is not TP1's different, still imported, Gaussian-energy identification." `descent.md` L68 says the same. Same name, two statements. In §2 they sit in different nodes (TPI and HM).

4. **TP1's AG import against frozen AG1.** `tp1.md` change log item 3 (L626): "(2.11) is cited as the R-check form of ag1-draft2 (8.1) plus this text's running-minimum step; ag1-draft2 (8.1) must be repaired." `tp1.md` L632: "The AG hypothesis rests on unrefereed drafts". Frozen `ag1.md` Theorem 12 (L1173) now supplies AG-k1* with three qualifications: the factor 81 between "c belongs to a live component" and TP1's "a live component meets c" (ag1 change log L1286, item 1); validity "above the coupling floor \(x_j\ge X_*\) and on the tori the chessboard input admits" (L1290, item 5, which says "TP1 is unaffected"); and \(c_{\rm AG}=\delta nM/2048\) (L1194), against FINISH row 266's round-2 "w_k = delta n M R_k/512". tp1 L154 still says (P-an) is "drafted in [pan-draft.md](pan-draft.md) … None of this is refereed"; it is now ag1 Theorem 5, frozen, needing (OS).

5. **TP1's IN-order item against frozen IN1.** `tp1.md` L184 names "[in1-draft.md](in1-draft.md), Part A" as "a proposed supplier". Frozen `in1.md` Lemma 3 (L336) gives the order "Under H-M"; the in1 gate Verdict: "The c4-order budget cycle is broken, conditionally on H-M". So TP1's import is now supplied, conditionally on HM (node 6 of §3).

6. **PR1(5) is two statements.** The skeleton has one input ⟦open: PR-lay⟧ (ym4-assembly L187). FINISH row 272 and `pr-lay.md` L353: in1-draft 800 "conflates different statements"; PR1(5) splits into (5a) (frozen pr-lay Theorem 3) and (5b) (layered-a3 (1), open). Frozen `in1.md` does not mention PR-lay by name (grep count 0); the draft did (FINISH row 267: "First open import in proof order: PR-lay").

7. **Which input is "first open" for CI.** The texts name different first items in sequence: FINISH row 267 (IN1 draft) "PR-lay"; FINISH row 273 (ci-form draft) "first open item is TD, not PR-lay"; td.md draft "First open item upstream: DR's construction (ST1)"; td2 draft "First open: (DR-locP) (owner ST1)"; drlocp draft "First open: (Cls), IN1's class induction". These are successive corrections, not contradictions. §3 orders them by dependency instead.

8. **Ordinary-distance TD.** `td.md` L482: "ordinary-distance TD remains **Outstanding**, neither proved nor disproved here." `td2.md` L398: "Theorem 3 proves **ordinary-distance TD** … conditional on TD's R, A, X, G, RUN and complete admission inputs, plus X° and G-ord." The later text proves it with two added premises. Both are unrefereed.

9. **JC and collar decay.** `td2.md` L411: "withdraw the claimed closure even conditional on the displayed JC estimate. Collapsing the logarithmic collar loses the collar-width decay". `drlocp.md` Theorem 2 proves \((\mathrm{JC}_\tau)\) and Lemma 5.1 "preserves collar-width decay" (Result L559); its Result L575: "(31) answers the latter only for the stated labels and family." Partly reconciled; both unrefereed.

10. **cls.md reads the drlocp draft.** `cls.md` L9: "Write IN1, TD, TD2, DRL and AG1 for in1.md, td.md, td2.md, drlocp-draft.md and ag1.md." The distilled `drlocp.md` changed the draft (eleven corrections; Result L559–575). cls's own F4* "replaces, rather than silently retaining, DRL's box-shell F4" (cls L464). Whether other cls steps read draft-only statements, I cannot tell without a line check.

11. **IN1's Amendment 1 rests on an unrefereed distil; Amendment 2 is not applied.** `in1.md` L666: "Source: [td-draft.md](td-draft.md) §11 (pass 1 …)". L674: "This amendment remains conditional on td.md surviving its referee". `td.md` is distilled, not refereed. `cls.md` §8 proposes Amendment 2 and says "**Not applied.**" (L435) and that Theorems 10–12 "transfer only under cls.md Proposition 12's matching hypotheses on the enlarged class, which remain Outstanding" (L472).

12. **Two current continuations.** `drlocp.md` L566: "Distinguish D3L's force-anchored current from ST1's independent-current formula. Specify both via (7); do not infer their equality from physical-locus agreement." L69: "[RED] identifies (5) with that nonlinear map; it does not identify the two current continuations in (7)." This is part of node DR.

13. **IN1 Lemma 2's chain example.** `in1.md` L329 gives a three-site chain where the path-weighted local covariance depends on an exterior edge. The hm draft (FINISH row 275) said "its three-site chain example cannot occur: cut-edge terms have zero tag". Frozen `hm.md` Result item 6 (L497): "IN1 Lemma 2's chain counterexample remains correct for its own family. The full-read replacement excludes its mechanism; it does not disprove the example." Resolved in the frozen text; the FINISH row keeps the draft wording. Similarly drlocp's draft Prop 3.2 (FINISH row 277, "violates (DR-locP) for every collar") is "restricted (not a YM counterexample)" in the distil.

14. **The skeleton against later frozen texts.** These are design changes, not errors in the later texts.
    - ST1: the skeleton's intrinsic seven-bound design with ST-cov … ST-drop (ym4-assembly L218–232) is replaced by the substitution design of FINISH row 265 and st1-r4 Theorem 14. None of the skeleton's ST1 names occurs in st1-r4.
    - TP1: skeleton TP-F2 needs the complete-force term (GCB52) bounded (ym4-assembly L393). FINISH row 266: "Gaussian extraction by Cauchy estimates … so the complete-force term of SA 28219-28221 never appears". tp1 L592 records that SA does not assert the force estimates.
    - IN1: the skeleton marks IN1 [O] with the budget cycle open (ym4-assembly L91, L333). Frozen in1 breaks it conditionally on H-M.
    - OL1: the skeleton's AS1 lists ⟦OL-incr⟧ (L550). IN1 and TP1 do not need it (§2.3).
    - NT1: the skeleton routes NT1 through Lemma W [P] (L451). Frozen TP1 Lemma 7.2 proves it from PH1's unique vacuum (tp1 L550).
    - LF-mass: the skeleton has LF1(3) [O] (L306). Frozen in1 Theorem 10 (L540) gives the component mass for C3, conditional on H-LF, H-G, H-C, H-E.

15. **"Not yet refereed" sentences in frozen texts.** Each frozen text keeps its distil-time closing sentence after its "Status: frozen" line: `p82.md` L659, `tp1.md` L651, `in1.md` L696, `pr-lay.md` L391, `nl1-L.md` L737, `st1-r4.md` L1684, `ag1.md` L1361, `hm.md` L503, `descent.md` L316. The status line is the later statement. Wording only.

16. **Name clashes recorded elsewhere.** `st1-r4.md` uses "M1" for the multiplier matching item (L135) and for "Definition M1 (permanent mark-debt ledger)" (L191), beside the cube size \(M_1\). `td2.md` Result item 2 confirms a clash of \(C_0\) between IN1 (2), row 6 and c4-order row 16. The skeleton already records the two D4s (ym4-assembly L39).

Checked and found consistent: OL1's \(c_0=11N^2\log L/(12\pi^2)\) (ym4-assembly L256) and IN1's \(c_0=\frac{11}{3\pi^2}\log L\) (in1 L114) agree at \(N=2\).
