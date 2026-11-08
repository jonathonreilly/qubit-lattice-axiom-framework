# T0 dependency tree

Provenance: Codex; assembly lane T0MAP; checkout 6d9df38c26ddcd12f61d3763fd6dbe6d9374152e; research dependency map, not an audit and grants no status. Sources borrowed from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, are credited below.

## 1. Contract, standing, and how to read the tree

Current synchronization: FINISH row 391, checkout `5467e79de`, 2026-11-06.

This maps the files at the pinned checkout. It proves and checks no mathematics.
**T0 remains open.** A frozen implication is not an established actual-construction input.

The contract is `GOAL.md:20–37`; the porting rule is `GOAL.md:39–48`.
The target here is the Wilson SU(2) scalar curvature sector, with componentwise OS properties and Wightman reconstruction. NT1 and the current NT2 proposal remain required. The Euclidean test domain is separated tests and diagonal-flat Schwartz functions. A full coincident-point Euclidean extension or a complete gauge-observable theory is not supplied by these texts (`wr1.md:403–429`; `port-map.md:13`; SA:74–82, 4416–4425, 4595–4598). Do not silently strengthen this sector contract to either claim.

The outline and complete account have different Theorem 0 statements. Here **A0–AV** mean the complete account's clauses, CA-I `3.1:thm-main`, lines 2512–3016. The outline's main page is SA:66–130. In particular CA does not assert clustering, unique vacuum, Wightman functions, the forward cone, or O(4) in (ii): CA-I:2705–2711. Its (iv) does not assert non-Gaussianity: CA-I:2815. Half B is essential.

Standing used throughout:

- **proved**: <a id="node-b99-w"></a>B99-W, a written repository implication; say separately whether refereed. All named hypotheses survive.
- **ported-checked**: one checked port, at its exact stated scope and repairs.
- **ported-unchecked**: a port awaiting its other-model reading.
- **theirs-cited**: a step the Sussman-Alpoge account proves in detail, used here as a cited input, with its check deferred to the final hardening pass (owner rule). This is an unchecked conditional input, not a closure of its hypotheses.
- **OPEN**: no supplier at the required scope. Keep this standing for account statements marked incomplete, outstanding, cited without proof, printed without proof or model, and for missing interfaces. A detailed conditional deduction may be theirs-cited while its actual application remains OPEN.

Latest freeze/change-log entries and the user's explicit standings override older provenance sentences. “Checked” describes the recorded reading, not an independent check by this mapping lane. No run discharges a mathematical step.

Paths below are relative to this `library/`, except `GOAL.md`, `FINISH.md` and `parts/`, which are relative to the lane folder. `file:lines` is a source citation. CA-I and SA refer to the two files fetched once at upstream commit `31a47c543775`. CA-II/III loci below are carried by the cited repository ports/maps; this lane did not fetch or independently read those volumes. Credit for their statements, constructions and routes belongs to **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**; credit for the underlying RG inputs belongs to **Tadeusz Bałaban**. LG1 also credits Osterwalder–Seiler and Fröhlich–Israel–Lieb–Simon (`lg1.md:5`); WR1 credits Osterwalder–Schrader and the authors' YM3 reconstruction (`wr1.md:419–423`).

Indentation lists required inputs; inline right arrows show supplier-to-consumer pipelines, and a left arrow reads “requires the right-hand side”. Repeated node IDs refer to the same subtree, not extra obligations. This is a tree presentation of a shared dependency graph. The (0)/(i) cycle is a **joint induction on earlier levels**, not a proof by mutual assertion (`chain-ca.md:19–27`; `port/p10-stability.md:604–687`). The source choice order is another constraint on every edge.

## 2. T0 tree

```text
T0 — OPEN: GOAL.md:20–37,39–48
├─ E. One continuum Wilson SU(2) curvature hierarchy on R^4
│  ├─ A0 + AI: actual first-passage trajectory and exact Wilson RG
│  │  ├─ P1 flow arithmetic; P5 A12/A13; P7 A14; P10 A15
│  │  ├─ P10 A17/A19/A20: representation, normalized stability, exactness
│  │  ├─ P4 A3/A4/A9 + P5 A5/A6 + P1 gas/logarithm
│  │  ├─ proved repairs: MU, LRB, OC, UI, PDA
│  │  ├─ checked conditional repairs: UM, OL-transfer (round 4 only)
│  │  └─ K1–K8, R1–R7, BP/BC leaves below (not just eight core lemmas)
│  ├─ AIII: P6 B2/B3/B4 + PI + P8 B5/B7 + LSC
│  │  └─ A0/AI + K4/K5 + R8 + retained BP/BC inputs
│  ├─ AII-R: P8b B10–B13, from A0 + AIII-b + finite lattice RP
│  └─ CL1 Theorem 9, using LG1 + SR1 + compatible first passage (I1)
│     └─ J1 (checked reduction, four OPEN premises) + J2 (full rooted UV1)
├─ E0. Regularity and factorial growth
│  └─ SR1 Theorem 1(3)–(4) + PH1 Theorem 1(3)
│     └─ LG1 + J1/J2 + CL1 for realized components
├─ E1. R^4 translations and full O(4), in each component
│  ├─ RO1 Theorem 9: UI → PD → angular kernels → TU → all-order closure
│  │  └─ LG1 + CL1 + SR1 + PH1 + J2 + J3 (component-uniform TU10)
│  └─ restricted shortcut: O4-2, connected n=2 on torus-limit class V
│     └─ A0 + AIII-b + AIV + LG1 + restricted CL1
│        [does not supply all-order/component O(4) or insertion bounds]
├─ E2. Reflection positivity, including diagonal mirrors used in the proof
│  └─ LG1 Theorem 10/13 → CL1 Lemma 3 → SR1 Lemma 10 → PH1(3)
│     └─ J1/J2 for the continuum hierarchy; lattice LG1 has no RG premise
├─ E3. Symmetry and reality
│  └─ P1 lattice invariance + LG1 → CL1 Lemma 3/Theorem 9 → PH1(3)
│     └─ same actual sequence and common centering, supplied via J1/J2
├─ E4. Components, clustering, unique vacuum
│  └─ PH1 Theorem 1(2)–(5), Lemmas 7–10
│     └─ LG1 + SR1 all-state bounds/growth + CL1 realization + proved J6
│        [CA (v) is coupling uniqueness, not this phase theorem]
├─ W. One scalar Wightman theory per component
│  └─ WR1 Theorem 11: H1–H5, all on the same component
│     ├─ SR1 growth/density and RP; CL1 Hilbert space/cube cone
│     ├─ RO1 all-order O(4) AND full degree-uniform insertion density
│     └─ PH1 bounds, clustering and unique vacuum → J1/J2/J3
└─ N. Non-triviality in GOAL's sense
   ├─ NT1: TP1 Lemma 7.2 + PH1(5)
   │  └─ positive reflected connected two-point value per component
   │     └─ J4 (component lower witness), or full conditional TP1 package
   └─ NT2: parts/witness.md Text 8.1 (proposal adopted by GOAL)
      └─ J5: one joint blocked state, admissible M, NT2-V/M/g/R
         └─ eight named witness hypotheses; AIII-d alone is insufficient

Half-A comparison branches, mapped but NOT prerequisites of subsequential T0:
AII-T-b: fixed-torus first-passage subsequence ← AIII-a + P8 B5/B8 + A0
  └─ identification with a tuned member additionally needs AV-c(2)
AII-T-a: whole tuned torus family ← AV-a–e + AIII + R11
AV-a–e: exact pin, family, comparison, renormalized labels, Lipschitz step
  └─ R11 + inherited A0/AI/AIII and BC-v/BP22
AV-f: coupling covariance/injectivity ← AV-a–e + AIII + AIV + R12
```

**Node supplier citations.** E0 uses `sr1.md:107–129`, `ph1.md:62–80`. E1 uses `ro1.md:630–649` and `o4-two-point.md:47–75,186–203`. E2/E3 use `lg1.md:365–435`, `cl1.md:142–199,455–485`, `sr1.md:481–512`, `ph1.md:73`. E4 uses `ph1.md:62–82,400–577`. W uses `wr1.md:17–65,403–448`. N uses `tp1.md:550–566`, `GOAL.md:30–33`, `parts/witness.md:863–1018`. A-node sources and standing follow immediately. These references are to suppliers of implications, not declarations that their leaves hold.

## 3. Half A: clause-by-clause assembly now

| Node | Exact supplier now | Standing and surviving dependency |
|---|---|---|
| A0: CA (0), flow and windows | P5 `4.19:prop-clause-zero`, A12, and `prop-containment`/`cor-windows`, A13 (`port/p5-induction.md:417–497,564–672,828–855`); P1 `4.2:lem-first-passage`, `4.19:lem-flow-bounds` (`port/p1-base.md:55–150,766–768,811–821`); P10 A15 (`port/p10-stability.md:280–443,1640–1642`). | P1/P5 **ported-checked**; P10 **ported-checked**. Needs the actual joint induction, not arithmetic alone. P5's (b)/(g)/(h) suppliers now include checked UM, round-4 OL-transfer, K8-CORR and P7; their other premises survive. |
| AI: CA (i-a), representation | P10 A17 `4.20:thm-representation` (`port/p10-stability.md:444–794,1643–1648`). | **ported-checked**. A10 `4.18:thm-preparatory-boundary` (`:43–160,1636–1639`) retains H-STAGE. Needs K/R/B leaves; representation is not a closed input. |
| AI: CA (i-b),(i-c), stability and mass | P10 A19 `4.33:thm-stability` (`port/p10-stability.md:1010–1261,1649–1652`). | **ported-checked** with all eleven (h1)–(h11), not only the eight in the older CHAIN summary. Normalized floor; real positivity and reference normalizers still required. |
| AI: CA (i-d), exact insertion and sourced identity | P10 A20 `4.34:lem-sourced-exactness` (`port/p10-stability.md:1362–1438,1591–1628,1653–1655`). | **ported-checked**, conditional on actual transformation identities and the complex correlation induction. Exactness is not a theorem about the continuum block laws. |
| AIII-a,c,d: fixed-torus bounds, running shift, cumulative one-loop law | P6 B3 `5.1:thm-correlation-theorem`; B4 `5.3:lem-driven-flow`, `5.14:thm-one-loop-law` (`port/p6-correlation.md:460–728,2647–2670,4630–4662`). | **ported-checked**; reads A0/AI, B2's two weight lemmas, PI, K4/K5 and R8. Running law uses the actual Gaussian finite part plus the unmarked/remnant bounds, not free-field algebra alone. |
| AIII-b: per-ball bound | P8 B7 `6.4:thm-per-ball-bound` (`port/p8-positivity.md:148–208,560–707,854–866`) + LSC B6 (`lsc.md:688–700,720–724`). | P8 **ported-checked**, LSC **proved/refereed**. Retains H-LOC/H-DOM, shared normalized upper/floor, zero-source energy identification, and CMP 116 (1.26). No n=1, factorial bound, decay at large separation, or arbitrary-state result follows from the statement alone. |
| AII-T-b: first-passage torus limits | P8 B8 `5.12:prop-subsequential-limits`, `5.12:lem-limit-positivity` (`port/p8-positivity.md:709–852,856,862`). | **ported-checked** on H-FIRST-PASSAGE, torus floor/bound, distributional H-KERNEL, and finite RP. Its extra tuned-family identification needs AV-c(2) (CA-I:2688–2689). |
| AII-R: growing tori/R4 | P8b B10 transport/symmetries/half-space/modulus/linearity; B11 `7.4:thm-infinite-volume`; B12 limit distributions/invariance/positivity; B13 `7.7:prf-reconstructed-space` (`port/p8b-limits.md:19–67,258–328,329–674,1288–1298`). | **ported-checked**. Gives curvature Hilbert space, H≥0 and W3. H-BLOCK (`:57`) is an extra block-state assertion, not a consequence of curvature bounds and not needed for the scalar-only route. Full OS, components and Wightman theory require B. |
| AIV: finite witness, transfer, continuum consequences | P9 C9 `8.18:thm-torus-witness`, C10 `8.22:thm-volume-transfer`, C11 `8.1:thm-two-point-witness` and reference-volume assembly (`port/p9-witness.md:288–325,1109–1141`); C5 now in P9b `8.2:prop-gaussian-extraction` (`port/p9b-extraction.md:177–229,739–749`). | Both **ported-checked**, with P9 C9(d) restricted to θ≤1/2 by its check. Needs R9/R10, actual A0/AI/AIII, and Balaban inputs. P9's old “C5 not ported” is superseded only at P9b's conditional scope. H-GXa/H-GXb are explicitly still open. CA (iv)'s torus-limit conclusion is weaker than NT2 and than a componentwise lower bound. |
| AV-a–e; AII-T-a | `chain-ca.md:112–127`: D8 `9.8:thm-uniqueness-theorem`, D11–D12 coordinate/comparison deductions; B9 `7.3:thm-tuned-family` (`chain-ca.md:88`). CA-I:2828–2983,2668–2682. | **OPEN as repository assembly**: no corresponding port among the supplied P-files. CA has conditional deductions, with R11 and cited inputs still open. Neither P7 torus independence nor PH1 phase decomposition proves this clause. |
| AV-f | D13 `9.8:thm-two-blockings` and its reconciliation (`chain-ca.md:128`), CA-I:2984–3016. | **OPEN**, R12; requires AV core, AIII and AIV. Do not feed it back into AV-a–e. It is not needed for subsequential T0. |

**Current check receipts (override stale headers in the ports).** P6 is **ported-checked**: `../gates/p6a-check.md:16–18` says “ADVANCE” for both weights and driven flow; `../gates/p6b-check.md:60–61` says “ADVANCE as an implication” for B3 and “ADVANCE” for the one-loop law. Keep W5-rim OPEN, W5 geometry's missing supplier, weights≥1, weighted-amplitude/a_flat/straddling rows and the max{1,10C_M M} repair (`../gates/p6a-check.md:26–32`). Keep the new **C-stability** OPEN, complex sourced bound (7) on D, which CMP 119 (2.50) does not prove (`../gates/p6b-check.md:20–26`); run the frozen step through k=K, carry real-family induction, separate flow quantifiers from torus admission, and cite CMP 119 (3.1) for preservation (`:28–50`). These are not closed by marking P6 checked.

P8/P8b are **ported-checked**: `../gates/p8-check.md:28–36`: “First failing step none.” B5 supplies torus RP on centred sites with N_T even; retain H-LOC/H-DOM/H-STAB/LSC/H-TREE and all B8/B11 kernel, block, analytic, Fourier, spectral and flow inputs. H-BLOCK is optional only for the scalar route, never proved from curvature bounds. Keep the domain of H dense and the stronger LSC cell-side floor (`:14–21`).

P9/P9b are **ported-checked with repairs**: `../gates/p9-check.md:30–32`: “proved implications after the repair ... (theta <= 1/2)” and “closes none of their open inputs”. The first failing step was P9:483's reflected-pair existence; C5 had none. Keep H-depth as a tail floor, H-GXa/H-GXb/H-source-use and every named H-C/B input. H-CK is unnecessary for C9(d) separately, but kernel (h3) survives; extraction support is 3l+6C_W and the tail rate needs its smaller-rate repair (`:14–19`).

P10 is **ported-checked**: `../gates/p10-check.md:99–103`: “faithful” for A10/A15/A17/A19/A20. A10's filing must inherit the companion so C∩Ω≠∅; support containment suffices; skeleton counting retains whole strips. The integrand-linear move is a clarification, not a correction of a claim that log is linear (`:16–19`). Keep H-STAGE, profile class, all REP/PRINT/O suppliers, (h1)–(h11), normalized E_vac, positive reference normalizers, and sourced induction. A17 is an assembly with no proof at its account theorem, not a theirs-cited detailed proof.

UM is **proved, checked**: `../gates/um-gate.md:57`: “ADVANCE”, under its four hypotheses and retained inputs `:65–71`. Carry citation repairs F1–F3 (`:47–51`): unpointed common lifts/pointing, CMP 99b walks for the free-boundary P1 passage, and the fixed-level rather than early constant. `../gates/uses-pda-um.md:178` covers its five clear uses and mediated C_β with the original order. OL-transfer is **proved, round 4 checked**: `../gates/ol-gate.md:121`: “ADVANCE, as an implication ... after repair D1”. Put κ at Stage 3, κ₁ at Stage 4, operator floors/radii at Stage 5, M at Stage 6 (`:24–44`). The normalization c₀=(11N²/(12π²))log L is confirmed (`:50–63`). Rounds 1–3 and their bulk/physical-identification inputs were not rechecked (`:124–130`); Q9 below records that remainder.

Canonical clause IDs for the tally: AI-REP = (i-a), AI-STAB = (i-b,c), AI-EXACT = (i-d); AIII-FLOW = (iii-a,c,d), AIII-B = (iii-b); AII-T-B = first-passage torus limits, AII-R = growing-torus limits; AV-CORE = AV-a–e/AII-T-a, AV-F = AV-f. These rename table entries for unique backlinks; they add no statements.

### A's reusable suppliers and repairs

| ID | File and label | Current standing; retained premises |
|---|---|---|
| P1 | `port/p1-base.md:762–789,811–821`: invariance; flow arithmetic; `4.6:lem-polymer-gas`, tree/cluster lemmas, `prop-logarithm-convergence`. | **ported-checked**. Actual activity bound and printed locality remain inputs (`:819`). |
| P3 | `port/p3-free.md:576–596`: `8.1:lem-gaussian-squares`, `lem-free-curvature-covariance`, `lem-kernel-positivity`, `lem-background-tower`, `lem-kernel-bounds`. | **ported-checked**, repaired domain C1. H-BG, H-TOWER, H1-MIN, H2-FLUX, H3-CONT remain (`:586`). Not the unwritten interacting continuum-kernel supplier. |
| P4 | `port/p4-operator.md:192–215,354–374,557–597,891–915`: A4 `4.5:thm-operator-bounds`, A3 `4.4:cor-localised-independence`, A9 `4.14:thm-operator-theorem`. | **ported-checked**, with recorded repairs. MU/LRB/UI/PDA supply specified clauses; P4-H-assembly and P4-H-core remain named missing suppliers (`:913`). |
| P5 | `port/p5-induction.md:17–416,828–855`: A5 `4.6:prop-large-field-bound`, A6 `4.7:prop-beta-extraction`/`prop-coupling-increment`, A12/A13. | **ported-checked**. Membership, activity, positive history law, rooted moment convention and prefix representation remain. |
| P7 | `port/p7-torus.md:257–304,1268–1283,1331–1340`: A14 `4.38:thm-torus-independence`. | **ported-checked**. Seven theorem hypotheses, level hypothesis, joined-domain extension and family propagation survive. It is not the AV uniqueness theorem. |
| PI | `port-pi.md:15–34,542–551`: `5.2:lem-pointed-irrelevance`. | **ported-unchecked** on admitted E-families and the one-layer box hypothesis. Does not supply cp12's full H-ct or CI's OSF-loc/(13). |
| MU | `mu.md:245–280`: `4.13:lem-minimizer-unique`, both tower rules and arbitrary-subdomain nesting. | **proved/refereed** in the regular class and its stated analytic continuation. CMP 102b minimal orbit and CMP 98 averaging remain inputs; extended use coverage and its exceptions are recorded at MU-USES below; no blanket admission follows. |
| LRB | `lrb.md:833–862`: `4.4:prop-local-real-base`, clauses (1)–(4). | **proved/refereed** under (a)–(d), W′, cell-resolvent/coercivity, symmetry and CMP 116 (2.14). Does not construct those primitive walks. |
| OC | `oc.md:243–265`: `4.13:lem-own-constant`. | **proved/refereed** for widened smaller-cube gauges, own constants and one-step reproduction, under (3)–(7) and the cited background/gauge results. Not blanket complex admission. Value check (`../gates/bundle-value.md`, OC section): their account already proves this result elsewhere (§4.9); their "Proof outstanding" label is stale; not offered outward. |
| UI | `ui.md:549–572`: `4.5:lem-uniform-increment`. | **proved/checked** completion of the source continuation; retains (189)–(190)/C_H, gauge-map scale count and hierarchy-distance input. This UI is not RO1's small-ball insertion lemma. |
| PDA | `pda.md:231–247`: geometric (A1) of `4.14:prop-prepared-data-admissible`. | **proved/refereed**, one operation and stopped prefixes given old (A1), with rule (C). PDA-T below gives an unchecked R1/N2 extension; (A2) and the all-history use are not promoted to checked. Analytic and separately cited geometry remain. |
| LSC | `lsc.md:688–700,702–724`: `6.3:lem-last-scale-constants`. | **proved/refereed**, round 2. Keep e^{-E_vac} on both sides before cancellation. Frozen smaller-scope round 1 is superseded by the round-2 normalized result, not by a bare floor. |
| UM | `um.md:89–205,563–584`: `4.2:lem-unmarked`, including its missing uniform-domain step. | **proved, checked by Claude** implication under its four hypotheses and Balaban analytic/remainder inputs. Updates older “unmarked open” entries, but does not prove its small-field-step premise. |
| OL | `ol.md:2669–2768,2813–2845`: OL-transfer for Gaussian consumers of `4.2:lem-one-loop`. | **proved, round-4 transfer checked by Claude** replacement; rounds 1–3 retained, not rechecked by that gate. Retains §11's flat/model inputs, actual coefficient/pivot estimates, physical Gaussian and response identification, and §§2–3 bulk calculation. Original OL-W0-CA stays open; Gaussian-only replacement does not establish arbitrary-history/non-Gaussian machinery. |

## 4. Half B: every declared import and its supplier now

The seven texts are **proved/refereed conditional texts**, not seven closed T0 clauses. Freeze records: `lg1.md:477–485`, `sr1.md:562–568`, `cl1.md:530–536`, `ph1.md:598–606`, `ro1.md:695–702`, `o4-two-point.md:192–203`, `wr1.md:442–448`. The following inventory extends the RO1 comparison at `ro1-vs-ca.md:24–73` to all seven.

| Import slot | Required scope and source | Supplier NOW |
|---|---|---|
| B01 LG1 | Scientific/RG imports: none (`lg1.md:49,460–475`). | **proved** lattice argument, Theorems 10/13 (`lg1.md:365–435`). IN1's L is only notation/order; any odd L≥3 works (`:51`). No continuum input is consumed. |
| B02 SR1: LG1 | Coordinate-link torus RP; all-state isometry invariance and RP (`sr1.md:36`). | **proved** LG1 Lemma 3 and Theorem 10 (`lg1.md:89–119,365–384`). SR1 proves its own chessboard consequence in Lemma 2 (`sr1.md:131–162`). |
| B03 SR1: first-passage data/order | Actual x_j, supplied datum, ten-row order, common constants (`sr1.md:15–19,88–105`). | **proved conditional** IN1 Theorem 12 (`in1.md:583–633,677–681`). Half A offers A0 and P7/P10 at the standings above; identification with all of IN1's consumed data and constant constraints is **OPEN J1**, not supplied by naming both “first passage”. |
| B04 SR1: UV1 | Entire (4)–(6), local/list-independent source energies, point terms, mirror-copied profiles, all scales, rooted entropy margin (`sr1.md:38–65`). | **OPEN J2**. P6 B3, P8 H-LOC/H-DOM, LSC and P10 provide conditional ingredients (`port/p6-correlation.md:2647–2670`; `port/p8-positivity.md:152–208`; `lsc.md:720–724`). No current file proves their conjunction in this exact SR1 consumer form. |
| B05 SR1: an existing limit and compact RP | (7) on all separated tuples; positivity for finite sequences; component realization not constructed (`sr1.md:67–86,121–129`). | **proved conditional** CL1 Lemmas 1–3/Theorem 9 (`cl1.md:99–199,455–485`) constructs limits using SR1's *finite-cutoff* estimates. LG1 supplies compact RP; PH1(3) supplies components (`ph1.md:73`). No circular use of SR1's limit-extension conclusion to prove its finite-cutoff bound. |
| B06 CL1: I1 | IN1(4), compatible unbounded first-passage sequence (`cl1.md:59`). | IN1 Theorem 12, **proved conditional** (`in1.md:583–633`); A0 is the port-route candidate. **J1 remains OPEN**. IN1's nine import families remain in `in1.md:681`: H-M, H-OL, H-SF, H-LF, H-G, H-C, H-E, H-O, H-SUM. |
| B07 CL1: I2 | All periodic-state translations/W4 and coordinate-site/bond/diagonal RP (`cl1.md:61`). | **proved** LG1 Theorem 10/13 (`lg1.md:365–435`). P8 B5 alone supplies only its finite-torus geometry. |
| B08 CL1: I3 | One-point comparison; all-state moments/cumulants; factorial diagonal-flat extension and density (`cl1.md:63–74`). | **proved conditional** SR1 Theorem 1 (`sr1.md:107–129`), hence J2. AIII-b supplies fixed-order position-uniform connected bounds on torus-limit states only; O4-2 checks a restricted substitution, not this full I3 (`ro1-vs-ca.md:58–62`; `o4-two-point.md:173–188`). |
| B09 PH1: LG1 | All-state mirrors/invariance (`ph1.md:43`). | **proved** LG1 Theorem 10 (`lg1.md:365–384`). |
| B10 PH1: S3 | All evaluating states, common centering state, one-point differences and separated cumulants (`ph1.md:44–50`). | **proved conditional** SR1 Theorem 1(1)–(2), Lemmas 3–4 (`sr1.md:109–114,164–216`), hence J2. AIII-b has no n=1 statement. |
| B11 PH1: SR1 growth | All-state graded bound and extension/density (`ph1.md:51`). | **proved conditional** SR1 Theorem 1(3)–(4) (`sr1.md:115–127`), hence J2. Per-order constants do not replace the factorial accounting. |
| B12 PH1: CL1 | Common admissible sequence; centered moments; off-diagonal regularity; agreement of compact and flat Hilbert completions (`ph1.md:52`). | **proved conditional** CL1 Lemmas 2–6/Theorem 9 (`cl1.md:115–360,455–485`). Its cone is not a premise of PH1. |
| B13 RO1: H-U | Rooted D1, ordinary/mirror source classes, independent even/odd lists (`ro1.md:54–62`). | **OPEN J2**, exactly as for B04, with RO1's independent-list clause retained. Not replaced by AIII or by O4-2 at n≥3 (`ro1-vs-ca.md:42–48`; `o4-two-point.md:176–188`). |
| B14 RO1: H-L | All-state and finite-torus mirror properties (`ro1.md:64`). | **proved** LG1 Lemma 3 and Theorem 10 (`lg1.md:89–119,365–384`). |
| B15 RO1: H-C | Same realized hierarchy; local C1 bounds, coordinate/diagonal RP, coordinate Hilbert spaces, translations, cube cone (`ro1.md:66`). | **proved conditional** CL1 Lemmas 3,5,7,8 and Theorem 9 (`cl1.md:142–199,275–324,362–485`), with SR1 bounds. CA AII-R supplies neither diagonal RP nor the cube cone. |
| B16 RO1: H-T | TU10 for the full shape class θ*=1/12000, positions and all component-realizing periodic states (`ro1.md:68–76`). | **OPEN J3**. Frozen TP1 Theorem 3.1/Lemma 7.1 is a conditional supplier (`tp1.md:191–207,524–548`). AIV through P9 gives the torus-limit case only (`ro1-vs-ca.md:64–69`); no all-state/component extension is currently proved. |
| B17 RO1: H-S | Continuous diagonal-flat extension and constrained density (`ro1.md:78`). | **proved conditional** SR1 Theorem 1(4), Lemmas 7–10 (`sr1.md:121–127,333–512`), hence J2. |
| B18 RO1: H-P | Component realization, inherited interfaces and convergent one-point differences (`ro1.md:80`). | **proved conditional** PH1 Theorem 1(3), Lemmas 8/10 (`ph1.md:73,400–487,542–577`). H-U and H-T must still hold uniformly on these states. Mixture covariance does not prove component covariance. |
| B19 RO1: IN-order | Entire order, floors and shapes before final coupling (`ro1.md:84–90`). | IN1's conditional order and **OPEN J1**. No later choice of M or decay rate may repair an earlier floor. |
| B20 O4-2: data/class V | CA first passage, standing (iii)/(iv) hypotheses, θ* ceiling; fixed-cutoff torus-limit DLR states (`o4-two-point.md:49–56`). | A0 (P5/P7/P10, conditional); **proved** LG1 Lemma 2 (`lg1.md:73–87`); restricted CL1 compactness is rebuilt in O4-2 (`o4-two-point.md:77–95,201`). This route does not import original IN1. |
| B21 O4-2: A | Qualitative (iii-b), n=2 (`o4-two-point.md:69`). | P8 B7 + frozen LSC, **ported-checked / proved conditional** respectively (`port/p8-positivity.md:560–707`; `lsc.md:720–724`). |
| B22 O4-2: B | (iv)'s nonnegative vanishing upper bound and s(d)→∞ (`o4-two-point.md:70`). | AIV, P9 C9–C11 plus P9b, **ported-checked**, with R9/R10 and inherited leaves. Pass volume first at fixed cutoff, then K→∞ for fixed d, then d→0 (`o4-two-point.md:198`). |
| B23 O4-2: C | Diagonal RP at each fixed-cutoff DLR state (`o4-two-point.md:71,169`). | **proved** LG1 Theorem 10 (`lg1.md:365–384`). No assertion of diagonal RP for a straight torus. |
| B24 O4-2: D/E, restricted CL1 and RO1 machinery | CL1 Lemmas 1–3,5,7,8 at degree≤1; rebuilt one-field density; selected RO1 angular arguments (`o4-two-point.md:72–75,188`). | **proved/refereed conditional** restricted reading and Lemma A in this note (`o4-two-point.md:77–164,194–203`). Does not import SR1, PH1, D1 or the all-order RO1 conclusion. |
| B25 WR1: H1 | Factorial growth and constrained density, same component (`wr1.md:19–24`). | **proved conditional** SR1 Theorem 1(4) and PH1 Theorem 1(3) (`sr1.md:121–127`; `ph1.md:73`). |
| B26 WR1: H2 | Componentwise full Euclidean invariance, reality/symmetry and full flat-sequence RP (`wr1.md:26–31`). | **proved conditional** RO1 Theorem 9 (`ro1.md:630–649`), SR1 Lemma 10 (`sr1.md:481–512`), CL1 Lemma 3 (`cl1.md:142–199`), realized by PH1(3) (`ph1.md:73`). Needs J2/J3, not O4-2 alone. |
| B27 WR1: H3 | Separable common Hilbert space, dense compact tuples, commuting continuous translations, cube cone (`wr1.md:33–40`). | **proved conditional** CL1 Lemmas 5–8/Theorem 9 (`cl1.md:275–485`), for the PH1 component realization (`ph1.md:73`). |
| B28 WR1: H4 | Full four-variable insertion density, exponent five, uniform over outside degrees and coefficients (`wr1.md:42–49`). | **proved conditional** RO1 Lemmas 2–3 and Theorem 9(2) (`ro1.md:121–289,630–649`). Needs H-U/J2. Neither per-degree moments nor the O4-2 one-field density supplies this. |
| B29 WR1: H5 | Local C1 continuity/bounds, clustering, common centering, component mean and unique vacuum (`wr1.md:51–65`). | **proved conditional** PH1 Theorem 1(3)–(5), Lemmas 8–10 (`ph1.md:73–80,400–577`), with SR1's all-state bounds. This replaces the older cluster-port supplier at the frozen interface; no new cluster claim is inferred from CA. |

**Foundational imports, kept distinct from scientific leaves.** LG1 explicitly lists normalized Haar measure, compact product/probability compactness, Riesz, Stone–Weierstrass, spectral decomposition/positive square roots, Fubini/Tonelli, conditional-expectation L2 convergence, Cauchy–Schwarz and Jensen (`lg1.md:49`). CL1 lists Riesz, spectral and joint spectral theorems, measurable calculus, Tonelli/Fubini, dominated convergence and Fatou (`cl1.md:76`). PH1 lists joint spectral calculus, Hilbert projection, Riesz, Stone–Weierstrass and monotone class (`ph1.md:54`). RO1 lists bounded-form representation, joint spectral calculus, unitary spectral theory, Cauchy/identity theorems and integration/distribution calculus (`ro1.md:82`). These are retained classical mathematics with hypotheses checked in those texts, not fresh Yang–Mills estimates or newly proved results of this map. SR1 and WR1 have no further separately declared scientific imports beyond the slots above. Their choice-order passages (`sr1.md:88–105`; `wr1.md:67–71`) retain J1.

**State and domain restrictions are load-bearing.** The volume-first route constructs only a subclass of CA's joint-growing-torus limits (`cl1.md:459–485`). PH1 components are limits of pure periodic states; they need not be torus-selected (`ph1.md:400–487`; `ro1-vs-ca.md:66`). O4-2 gives only the connected two-point function on that subclass, not all-order moments or components (`o4-two-point.md:173–188`). These are three different domains, not interchangeable names for the same state.

## 5. OPEN leaves and what they block

A leaf here is a **named supplier contract**. Some source contracts contain several assertions. The tables retain that fact rather than claiming a count of independent missing lemmas. K, R and BP/BC rows overlap where one consumer exposes another's input. They must not be added as distinct mathematical obstacles.

### 5.1 The eight core statements

| Leaf | Exact source and present endpoint | What it blocks |
|---|---|---|
| K1 = CM | **OPEN** O3 family/domain identification at the old-terms consumer; the literal prescribed-word endpoint also remains open. CM-PART below is checked on its two stated classes. Earlier endpoint: prescribed-word continuation with the original Stage-5 rate, coefficients, complete reads and companion identification (`open-core.md:49–67`; current `mf.md:1528–1572`). | `2.4:prop-m-freeness` and correlation companion machinery; the parameter order underlying A0/AI/AIII and hence all T0 branches. A replacement root kernel with weaker rate is not its supplier. |
| K2 = CR | **OPEN** (conditional SU(2) implication checked; exact statement BLOCKED): `../gates/cr-r2-gate.md:180-199` (row 398) ADVANCE, after its written repairs, (a) and both cases of (b) with the account's K_b, uniform in depth and read domain; n_P=16 under (EC); ROW and SEP no longer separate assumptions. Open premises: (EC), (R-form), (BP), (S), (G-c), (G-t), P6, COMP incl. COMP(=); clause (c) and the real-factor corollary open. Premise round (row 408, `cr-prem.md`, unchecked): P6, native COMP/COMP(=), (G-t) and collared (S) proved; (EC), (R-form), (G-c) fail as stated; stopping lemma: a native representation of the section 4.12 constraint system to which R applies, for every outside read pair and level. `cr-claude.md` (row 348), `cr-r2.md` (row 398). | Outside re-blocking, actual stage/domain admission, then representation/correlation. RB's inside implication is not outside admission. MU proves nesting on admitted data, not this admission. |
| K3 = CA | **OPEN**, despite the checked CA-PART implication below; (B-in), (S-B), full layer/datum/bracket inputs and construction matching survive. Required: completion-collar membership at fixed birth domains, whole-cube gauges and all intermediate complex layers (`open-core.md:99–136`; `arr.md:955–978`). | The raw collar rider in arrest/completion and later analytic composition. Does not by itself close every arrest hypothesis. |
| K4 = CW | **OPEN** analytic window admission and both normalized screened inherited-data bounds (`open-core.md:138–172`; `wd.md:365–384`). | Preparatory-window input of P6 B3, two weight machines, AIII and every continuum bound. Real outside estimates alone do not give complex paired-window screening. |
| K5 = CH | **OPEN** actual three reached CMP 122b links on the full independent-switch polydisc (`open-core.md:174–193`; `ph.md:468–474`). | `5.6:prop-polydisc-holomorphy`, hence P6 B2/B3. A term bounded on its own domain does not prove that the links land there. |
| K6 = CO | **OPEN original statement** OL-W0-CA, prescribed actual precision words (`open-core.md:195–225`). **Bypass proved and checked for round 4** for the Gaussian coefficient consumers: OL-transfer (`ol.md:2744–2768,2817–2845`). | Literal original-family use, if retained; not a compulsory new proof on the proposed Gaussian-only route with OL-transfer repair D1 and its retained inputs supplied. It supplies neither CM's original-word rate nor arbitrary-history/non-Gaussian continuation. Do not record the original CO as proved. |
| K7 = CV | **OPEN** reality of the actual prescribed scalar sum at independent real current, with its masks/subtractions/branches (`open-core.md:227–238`; `pd.md:1442–1470`). | The missing reflection/reality step below `4.32:prop-positivity-dichotomy`, P10 stability and P9's positive history law. CV gives positivity of its own scalar exponential, not all of A18 (`open-core.md:553–560`). |
| K8 = L17 | **OPEN original ε₀-only statement**; the checked replacement K8-CORR suffices at its active consumers. Original: complex curvature-controlled admission for both actual tower rules, with early B3 and independent input radii (`b109.md:3186–3248,3670–3687`). | CMP 109 (1.17), hereditary small-field admission, P5 class reproduction and the Balaban family step. The weaker quadratic-radius estimate is not L17. P18/LQ remains unchecked; K8-CORR/P20 below supply the corrected consumer route, not the original ε₀-only statement. |

These retain the original literal endpoints; K8 has a checked corrected consumer route, not a proof that eight results suffice for T0. The Gaussian route bypasses K6 at its coefficient consumers; K8-CORR replaces K8 at the checked active consumers. `open-core.md:7–16,545–560` expressly proves no minimality or independence theorem. Its old CO endpoint is superseded **at the Gaussian consumers**, not everywhere.

The LOC/L16 obstruction remains a route constraint, not a ninth desired positive lemma: `open-core.md:404–430,541,558`. Do not demand both the universal path and its conditional counterexample. None of the map's K2/K3/K4 requirements assumes that path exists.

### 5.2 Residual Half-A contracts, beyond the core

All R rows are **OPEN at their actual use scope**. Conditional ports named inside them are available at the standings in §3. A source list's attribution is not a new proof that every item enters every clause; exact use-site identifications remain part of the indicated row.

| Leaf bundle | Missing contract, with all named subitems retained | Blocks |
|---|---|---|
| R1 small-field family step (owner `b109`) | CMP 109 Theorem 3 plus CMP 116 refinement: S1–S12, beyond K8. Actual background/primitive operators; exact Haar/Jacobian/Gaussian integral; symmetry; admitted far/near response; cubic/quartic Ward reduction; own response/marginal comparison; potential localization; activity budgets and final family closure (`b109.md:158–228,3728–3730`). P1–P21 are pieces, not the full theorem. | A0/AI, UM's premise and all sourced descendants. |
| R2 operator application/admission | P4's actual frames/charts/one-family/restriction/positivity; P4-H-assembly and P4-H-core (`port/p4-operator.md:192–215,354–374,557–597,899,913`); PDA's residual (A2), old-label/T-step/all-nest (A1), cited geometry and analytic supply (`pda.md:245`). CMP 122a stage theorem and full profile-class scope remain inputs (`port/p10-stability.md:50–105,1636–1639`; CA-I:54989–54998). | P4 A3/A4/A9, P10 A10/A17; all descendants. |
| R3 activity, support and extraction supply | Unwritten `4.6:prop-activity-bound` (`port/p1-base.md:819`); `4.6:rem-widened-support` (`port/p5-induction.md:837`); actual kernel-power, (A3), (A4), membership/locality/moment supply (`port/p5-induction.md:835–838,848`). Literal unrooted (A4) diverges on Z4; a correct rooted/restricted use must be supplied, not assumed. PI leaves H-ct/OSF-loc and consumer coverage open (`port-pi.md:549–551`). | P1 gas/logarithm, P5 A5/A6 and P6 correlation. |
| R4 relative machine and live geometry | `4.21:prop-relative-machine`; persistence of near-group weights on one/two runs; stored orbit data; volume counts, two data bounds, kernel difference (`chain-ca.md:68,272–276`); `4.22:not-live-region-geometry`, `prop-stage-totals`; kept-functional, probe-summand, foreign-operation, covariance-decay (`port/p5-induction.md:762–764,790`). K4 supplies a specified window subproblem, not the entire format. | Representation, source induction and bounds. |
| R5 localized boundary pieces | `4.24:prop-norm-conversion`, `prf-field-dependence`, `prop-holonomy-bound`; `4.25:lem-gaussian-pieces`, `lem-piece-oscillation`, `lem-non-deep-pieces`, `prop-dissolution` (`port/p5-induction.md:765–771`). Their full actual-domain hypotheses remain. | P10 representation and its correlation/witness uses. |
| R6 arrest and inherited domains beyond K3 | `4.27:lem-t-step-layer`, `lem-weights-heredity`, `prf-stage-move-cubes`, `prf-density-increase`, `prf-unheld-raw-points`, `prf-index-zero-margin`, `prf-ambient-inclusion`, `lem-real-minimiser`, `thm-arrest-theorem`, `prf-newborn-continuation`, `prop-live-piece-bounds`, `rem-raw-current-radius`, `rem-index-zero-members`; `4.28:lem-near-pair-sums`; one-point-current and core-freezing prose inputs (`port/p5-induction.md:772–785,790`). ARR retains other arrest, stage, averaging and real-point inputs (`arr.md:959,978`). | A17 and actual source-domain continuation; K3 is one missing collar conclusion, not all these statements. |
| R7 stability, counts and exactness | `4.30:lem-no-two-sided-point`, `prop-cell-counting`; full `4.32:prop-positivity-dichotomy` beyond CV; global history majorants/sum, unit fibre mass, positive reference normalizers, exact transformations; vacuum-energy and sourced/source-free zero-source identification (`port/p5-induction.md:786–790`; `port/p10-stability.md:1017–1138,1370–1438,1672–1682`; `lsc.md:722–724`). | AI stability/exactness, LSC, P8 per-ball estimates and P9 transfer. A normalized correction is available; a bare floor is not. |
| R8 correlation induction not covered by CW/CH alone | C-admitted, C-boundary, C-slots, C-frozen with whole-disc Qζ, all eight C-sites hypotheses, C-last's nine inputs, C-compact's distributional extension, C-sixth (`5.11:lem-sixth-family`, unwritten), plus weight-lemma domain and difference hypotheses (`port/p6-correlation.md:19–459,2647–2666,4658`). C-Mfree is K1; C-preparation/C-B1 include K4/K5. The m-uniform last-scale part is now supplied only at LSC's normalized scope (`lsc.md:724`), not by ignoring its premises. | AIII, AII and downstream B. The general-rank C-rank assertion is outside SU(2) T0. |
| R9 witness analytic inputs | P9 H-C3a/b (small piece; shifted frozen representation); H-C4a/b/c (fine-field/profile radius tails, room/zero-block-mean, remainder kind/coupling comparison/profile locality); H-C6a/b/c (prefactor monotonicity, healed islands unread, removal domination); H-C7a/b/c/d (history translation, target independence, age lemma, volume-dependent depth-floor rarity); H-C8a/b (source lemma, unwritten continuum kernel); H-add, H-free-torus, H-VT including vacuum density and normalizer identification (`port/p9-witness.md:296–325`). | AIV and O4-2; any later all-state/component witness extension. Uniform-old-rarity is explicitly not a premise of this CA route (`:1139`; `chain-ca.md:110`). |
| R10 extraction and exact use-site matching | P9b H-OP/H-step (unwritten one-point/one-step statements), H-jet, H-tail-sum at printed rates, H-support/geometry, H-eq, H-flat/H-free/H-tail, H-tr/H-pos and H-cluster instances (`port/p9b-extraction.md:177–229`). Still missing: P9 H-GXa and H-GXb, two-sided irrelevant bound, normalization, top-field/clean-complement control, H-source-use; H-depth tail-floor admission and C-V1 endpoint match (`port/p9b-extraction.md:654–699,747`; `port/p9-witness.md:1135–1139`). C5 alone does not give the averaged covariance or the six-term bound. | AIV and its literal stated parameter range. For existence at a sufficiently small fixed coupling, the strict-interior C-V1 option is available; that does not prove the supremum endpoint. |
| R11 tuning/uniqueness branch | CA D1–D12: radius/rate/shell floors; carry/extension; geometric-forgetting majorant and nesting; propagator stationarity and second variation; zeroth-order shell transfer; kept-factor/remainder-difference and nested interrupted Gaussian comparison; maximum principle/comparison chain/structure; first-passage exhaustion; refiled induction/Lipschitz/kernel; source/load/last-lattice/source-family/geometric-envelope estimates; equal-coupling endpoint and limit-member reconciliation (`chain-ca.md:116–127,280–287`). `7.3:lem-first-passage-offsets` also remains outstanding (`chain-ca.md:88`). These deductions are not ported by P1–P10. | AV-a–e, AII-T-a, and extra identification in AII-T-b. **Not** the subsequential T0 route. |
| R12 added coupling covariance branch | Unwritten `9.8:thm-two-blockings`, incomplete flow-only increment bound and exact source reconciliation (`chain-ca.md:128,288`). Retains AIII/AIV/AV core. | AV-f only in this map. No feedback edge to its own AV core. |

### 5.3 The Balaban leaves requested in CHAIN §6

These are not closed by the account's citations. BP rows reproduce the **22 sentence bundles** in `chain-ca.md:298–323`. The line citation on each row fixes the exact source scope. “OPEN” means not supplied here in its full consumed scope, not that the published statement has been refuted. J = joint (0)/(i), S = correlation, W = witness, U = tuning.

| ID | Cited sentence; repository coverage now | Reach and source |
|---|---|---|
| BP01 | Prepared large-field geometry, 122a pp.178–179: **proved/refereed at PDA's one-step (A1) scope**. Residual analytic/all-nest/A2 supply is R2, not closed by that proof. | J; `chain-ca.md:302`; `pda.md:241–245`. |
| BP02 | **OPEN** transfer of 109 §3, Lemmas 5–6, to 119's cover. | J; `chain-ca.md:303`. |
| BP03 | **OPEN actual supply** of two lowest tower regularity classes, 99b (3.35),(3.37); CA has a conditional deduction, not unconditional admission. | J; `chain-ca.md:304`; `b109.md:3674–3685`. |
| BP04 | **OPEN** locality of interaction terms, 122b p.379. | J; `chain-ca.md:305`. |
| BP05 | **OPEN** complex-pair inclusion 109 (1.17), precisely K8 at its current frontier. | J; `chain-ca.md:306`; `b109.md:3674–3687`. |
| BP06 | **OPEN** near-data extension of averaged-curvature bounds, 109 (3.26)–(3.28). | J; `chain-ca.md:307`. |
| BP07 | **OPEN full cited scope** inverse constrained-covariance bounds/walks, 99b before (3.132). B109 P18 supplies an unchecked uniform-layer LQ result with its premises, not the whole cited frontier. | J; `chain-ca.md:308`; `b109.md:3714–3730`. |
| BP08 | **OPEN** further operator walks, 99b after Theorem 3.9. | J; `chain-ca.md:309`. |
| BP09 | **OPEN** analytic averaging derivative extension, 98 §E p.43; MU still retains averaging. | J; `chain-ca.md:310`; `mu.md:274–278`. |
| BP10 | **OPEN** second far-family current inequality, 99b (3.49),(3.69). | J; `chain-ca.md:311`. |
| BP11 | **OPEN actual representation premise** for the bracket gas, 122b (1.90); P1 proves its conditional gas/log deduction. | J; `chain-ca.md:312`; `port/p1-base.md:239–288,819`. |
| BP12 | **OPEN** large-field bounds under remaining modifications, 122b p.386. | J; `chain-ca.md:313`. |
| BP13 (owner `stage-claude`) | **OPEN** layerwise gauge clauses, 122a (1.64)–(1.69). | J; `chain-ca.md:314`; R2/R6. |
| BP14 (owner `stage-claude`) | **OPEN** layerwise ceiling as a uniform small-coupling condition, 122a p.192. | J; `chain-ca.md:315`. |
| BP15 | **OPEN** old-term bounds beside a new region, 122b p.375. | J/S and constant order; `chain-ca.md:316`. |
| BP16 (owner `stage-claude`) | **OPEN** joined-domain convergence/analytic extension, 122a (1.70), 122b (1.68)–(1.69). P7/P10 retain it. | J/W/U; `chain-ca.md:317`; `port/p5-induction.md:486`. |
| BP17 | **OPEN** absolute boundary bound and gauge invariance, 122b (1.11),(1.23)–(1.48). | J; `chain-ca.md:318`. |
| BP18 (owner `stage-claude`) | **OPEN** analytic solution of the large-field equation, 122b (1.40)–(1.41). | J; `chain-ca.md:319`. |
| BP19 | **OPEN** small sum of localized remainders, 122b after (1.46)–(1.48). | S; `chain-ca.md:320`. |
| BP20 | **OPEN actual identification** of flat step form with free field, 95 §1; P3 and P9b retain it. | W; `chain-ca.md:321`; `port/p3-free.md:586`; `port/p9b-extraction.md:200–201`. |
| BP21 | **OPEN** positivity/bound of normalized island operations, 122b §1. CV does not automatically provide all these assertions. | W; `chain-ca.md:322`; `open-core.md:557–560`. |
| BP22 | **OPEN cited response passage** between 102b (189),(190). UI uses rather than rebuilds that analytic input. | U, with UI's own use retained; `chain-ca.md:323`; `ui.md:553–570`. |

Of the six **published-theorem frontier bundles** below, five retain OPEN analytic supply; BC4 has supplied finite Wilson content and inherits earlier open bounds. They overlap the BP list and one another. Exact individual clauses remain attached; no theorem is replaced by the name of its paper.

| ID | Required published inputs | Blocks/source |
|---|---|---|
| BC1 | 95 (1.118); 96 (2.36), Lemmas 2.1/2.4, Props 2.6/2.7; 98 Props 1–7; 99a Lemma 1, Thms 2/4, Prop 6, (1.19); 99b Thms 3.1–3.4,3.7,3.9–3.15 and Cors 3.5/3.6/3.8; 102b Thm 1, Props 3/9; 109 Thms 1/3, Lemmas 4–6, (3.37)–(3.50); 116 Lemmas 1–3; 119 Thms 1/2, Cor 3; 122a Prop 1; 122b Thm 1/Prop 1. | A0/AI and descendants; `chain-ca.md:331`; expanded `port/p10-stability.md:695–711`. MU/OC/UI/LRB/PDA and B109 supply only their specified pieces. |
| BC2 | 98 Prop 2 and averaging identities; 99a (1.3)–(1.6); 99b Thms 3.1–3.11,3.15/propagator formulas; 102b Thm 1, Prop 9, §§F–G; 109 Lemma 4, §§2–5; 116 Lemmas 1–3/localized and cluster formulas; 119 Thm 1, Lemma 4, Cor 3/induction; 122a cube/stage conditions; 122b localization/large-field bounds/Thm 1. | AIII-a,c,d; `chain-ca.md:332`; exact local register `port/p6-correlation.md:4331–4524`. |
| BC3 | 109 (0.24)–(0.26); 116 (1.26); 119 (2.49),(2.50); 122b p.355,(0.1). The last-scale deduction is now LSC, with its retained representation/background/normalization hypotheses. | AIII-b; `chain-ca.md:333`; `port/p8-positivity.md:166–198`; `lsc.md:722–724`. |
| BC4 | 109 (0.1),(0.2), the finite Wilson model/positivity conventions. Their finite-measure content is supplied by P1 and LG1/P8 at their scopes; no further Balaban theorem is added for the limit itself. | AII; `chain-ca.md:334`; `lg1.md:57–119`; `port/p8-positivity.md:26–145`. Remaining OPEN supply lies in inherited A0/AIII and distributional hypotheses, not in a new RG theorem invented here. |
| BC5 | 95 free propagators; 96 Props 2.3/2.6/2.7; 98 (19),(20); 99b decay; 102b Thm 1/Prop 9/response; 109 step/action/coupling; 116 Lemmas 2–3/cluster; 119 Thm 2/Cor 3/regularity/flow; 122a history/creation; 122b localization/region estimates. | AIV; `chain-ca.md:335`; individual B01–B24 and subitems in `port/p9-witness.md:325–357`. |
| BC6 | 102b Thm 1, Props 3/5/6/9; 116 Lemma 3; 99b Thms 3.1/3.4/3.12/3.13 and propagator formulas; 109 Lemma 4,(3.15); 98 Props 1/2/4/5; 99a Lemma 1, Props 3/5; 96 Lemma 2.1,(2.60)–(2.61); 122a/122b stage/remainder/localization; 119 induction. | AV/AII-T-a, off the shortest T0 path; `chain-ca.md:336`. |

Non-Balaban imports also survive: Combes–Thomas in the covariance-root use, Osterwalder–Seiler positivity, and the analysis/kernel/spectral results retained by the limit ports (`chain-ca.md:338`; `port/p8b-limits.md:59–67`). LG1 and P8 supply the specified finite positivity; WR1 supplies the stated reconstruction implication. Those facts do not prove a mismatched covariance-root or block-state premise.

### 5.4 Joins into the full T0 contract

| Leaf | Exact obligation and candidate supplier | What it blocks |
|---|---|---|
| J1 actual construction and constants | **OPEN interface identification**, reduced by the checked `t0-joins.md` implication to J1-CA, J1-IN, J1-ID and J1-ORDER. `gates/j16-check.md:62`: “correct conditional on J1-CA, J1-IN, J1-ID and J1-ORDER.” Supply the one Wilson trajectory, observable normalization, cofinal boards/tori, coupling/source ceilings and compatible order consumed by B03/B06/B19 and the other inherited IN-order passages. CA A0/P7/P10 and frozen IN1 are candidate implications, not an already proved equality of all their hypotheses (`cl1.md:59,78–95`; `in1.md:677–681`; `port-map.md:29–42,53–62`). In particular, do not silently mix an outline independent-current/relative-gauge construction with a different CA datum. | Nonemptiness and simultaneous applicability of the full frozen B chain. The restricted O4-2 route uses CA data directly and avoids original IN1. |
| J2 rooted ordinary source package | **OPEN** SR1 (4)–(6)/RO1 H-U in their exact ordinary repeated-source, mirror-list and actual rooted-geometry scope (`sr1.md:38–65`; `ro1.md:54–62`). Candidate ingredients are P6's sourced format, P8 H-LOC/H-DOM/H-TREE, LSC's normalized constants and P10 exactness/stability. The aggregate raw-source estimate, rooted counting/multiplicity margin and all-state transfer have to be connected in writing at these domains. | All-state n=1 comparison, graded factorial moments, full insertion density, all-order O(4), component construction and WR1. AIII-b alone does not supply it. |
| J3 all-state/component upper witness | **OPEN** TU10 uniformly over PH1's realizing states and full shape class (`ro1.md:68–80`). AIV provides torus and torus-limit states only. Either prove the extension from the CA source/normalizer package, or supply frozen TP1's entire FLOW/FREE/PRES/REG/AMP/AG/STATE/LIMIT package (`tp1.md:50–184,191–207,638–645`). Merely porting P9 does neither. | RO1 endpoint elimination on every component and therefore componentwise WR1 covariance. O4-2 already supplies the restricted connected two-point conclusion. |
| J4 component lower witness / NT1 | **OPEN actual input**, followed by a **proved/refereed** implication: a strictly positive reflected connected two-point value on the chosen component plus PH1's unique vacuum gives NT1 by TP1 Lemma 7.2 (`tp1.md:550–566`; `ph1.md:80`). TP1's full package is one conditional supplier of that lower value. AIV's positive mixture covariance alone is not a component covariance: conditional means can contribute. A chosen nontrivial component must be identified; if all components are claimed nontrivial, the lower bound must be uniform over their realizations. | NT1 in the reconstructed theory. Dimension ≥2 before phase decomposition is not enough. No mass gap is requested or inferred. |
| J5 NT2 | **OPEN** the adopted proposal on one joint blocked state, at all L-adic ultraviolet scales, with the same admissible blocking map, prescribed coefficients, observable coupling, NT2-V, NT2-M and NT2-R (`GOAL.md:31–33`; `parts/witness.md:863–1018`). Its eight supplier hypotheses are expanded below. | Interaction/non-triviality in GOAL's sense. CA (iv) and its bounded-relative-error scalar two-point law do not supply this. CA (iii-d) is a construction-coupling law, not automatically the observable-coupling law. |
| J6 final test-domain and same-theory assembly | **proved, checked by Claude**, for PH1's component functionals: full positive-time diagonal-flat qualitative clustering, uniform in the spatial translation. `t0-joins.md:175–252`; `gates/j16-check.md:61`: “(J6.4) is uniform in v. No full-domain rate is claimed.” Inputs remain PH1 Theorem 1(3)–(4), Lemma 10/change-log item 2, CL1 Lemmas 4–6 and the SR1 extension bound. | The domain passage is supplied as an implication. Simultaneous realization of the actual upstream estimates, reconstruction and nontriviality witnesses is still required by T0/J1–J5. |

J6 is now a checked implication. This sync supplies no proof; it records the uniform Hilbert-space approximation of `t0-joins.md` and its check, not a uniform Schwartz-translation bound.

**TP1's alternative witness route: current suppliers of all eight imports.** These are subcontracts of J3/J4, not eight additional independent leaves. TP1 is frozen/refereed (`tp1.md:621–634,654`); its older AG-draft status is updated by AG1's current conditional theorem, not by assuming AG's premises.

| TP1 import | Supplier NOW and retained gap |
|---|---|
| FLOW (`tp1.md:54–69`) | A0/AI, UM, OL-transfer and P6 B4 are candidates at their recorded standings (`port/p6-correlation.md:460–728`; `um.md:563–584`; `ol.md:2744–2768`). **OPEN exact match** to telescoping, constant-source derivatives, fixed auxiliary choices and common datum; J1 applies. |
| FREE (`tp1.md:71–87`) | P3's Gaussian squares, covariance and background tower are **ported-checked conditional** (`port/p3-free.md:576–596`). **OPEN** full TP1 residual covariance bound and volume-uniform continuum comparison at (2.3)–(2.4); slice bounds alone do not supply the terminal bound. |
| PRES (`tp1.md:103–113`) | P10 A20 is **ported-checked conditional** (`port/p10-stability.md:1362–1438,1591–1628`). **OPEN** identification with this four-part formed exponent, positive history law and differentiable expectation, using the same law as AG. |
| REG (`tp1.md:115–130`) | **OPEN** strengthened source discs, deterministic common family, all-level comparison including healed regions, and exact G-ID. The P9/P9b extraction suppliers are weaker conditional ingredients (`port/p9b-extraction.md:654–699`); no exact supplier is established here. |
| AMP (`tp1.md:132–146`) | **OPEN** the stated first-derivative oscillation and live/far bounds with inverse-coupling powers and only logarithmic prefactors. The weaker displayed age-amplitude estimate is expressly insufficient (`tp1.md:146`). |
| AG (`tp1.md:148–154`) | **proved/refereed conditional** AG1 Theorem 12 (`ag1.md:1173–1198,1283–1297`), with the 81-neighbour event conversion. Its current open inputs include ANC, whole-live-attached OS, NL1's full-source distance, QL′ domain/threshold, and fixed-history density identification. Retain FLOW/K/MI/COV/SM/ROOM/R0–R3/LT/CB, QL′ with RS/BGL, and CL0/CL for the same stopped law; AG1 does not establish the imported LT/R2/Q/L (`ag1.md:1309–1320`). Thus the actual AG input is still **OPEN**. |
| STATE (`tp1.md:156–163`) | **proved conditional ingredients** LG1's fixed-cutoff states/invariance/chessboard and SR1's source comparison (`lg1.md:73–87,365–414`; `sr1.md:38–65,131–216`). **OPEN J2/use-site match** for the common state-independent holomorphic normalizer on signed, translated and overlapping tests; separate per-state normalization is insufficient. |
| LIMIT (`tp1.md:165–166`) | **proved conditional** CL1 Theorem 9 and PH1 Theorem 1(3)–(5)/Lemma 8 (`cl1.md:455–485`; `ph1.md:73–80,400–487`), including centered first and second moments and unique vacuum. Retain each component's actual realization; a mixture identity does not substitute for it. |

The full order of choices in `tp1.md:168–184` still applies. IN1, TP1 and AG1 are auxiliary conditional suppliers; they are not counted among the seven downstream texts specifically requested in half B. This alternative is recorded to preserve a current supplier, not to prescribe re-deriving CA by the older outline route.

**NT2's eight imports, individually.** Their exact requirements are `parts/witness.md:1002–1018`. Each is OPEN for the actual common state in the scope required there.

| Import | Supplier now / missing match |
|---|---|
| H-NET (`:1011`) | A joint bounded-block-observable state with RP, ordered limits and semigroup identification. The witness cites conditional upper-chain 10.2. P8b's H-BLOCK is a separate assumption (`port/p8b-limits.md:57`); scalar WR1 is not this block state (`wr1.md:429`). **OPEN** common block/scalar realization. |
| H-SCALE (`:1012`) | One anchored trajectory and joint subsequence for all fixed blocked scales. A0 supplies first-passage windows and P7 torus independence conditionally; **OPEN** the specified blocking-state and physical-anchor identification. |
| H-MOM (`:1013`) | Uniform all-order finite-window moments for the actual fluctuation and pulled-back chart laws. Conditional FF/locality/reflections are cited; the pullback side is additional. **OPEN**; scalar separated cumulants do not prove it. |
| H-G0 (`:1014,1020–1033`) | Integrated gauge-invariant polynomial one-step Gaussian comparison, degree≤8, uniformly in level and volume, also on the lifted kernel class. **OPEN**; a covariance norm alone is weaker. |
| H-LIFT (`:1015`) | Closed invariant polynomial/kernel norm, strict contraction and exact iterated free covariance identity for the chosen M. **OPEN**; P3/P9b's conditional free tower has not been identified with this normed blocking contract. |
| H-FIRST (`:1016,1035–1039`) | Second-order chart jets, first covariance response, cubic correction and uniform o(gamma) remainders, including o(gamma^4) failures/pullback errors for T. **OPEN**; neither PI nor scalar two-point extraction supplies this vertex-sensitive estimate. |
| H-TREE (`:1017`) | Scale-independent blocked free coefficients and degree≤8 moments; NT2-V for a finite family before choosing the state. **OPEN** at the blocked scale (`:940–960`). An n=1 calculation is not the required admissible-blocking limit. |
| H-FLOW (`:1018`) | The specified corrected-coordinate error law, plus identification of the hard-core coupling with the observable coupling (`:965–973`). OL-transfer and P6 B4 are **proved (round 4 checked) / ported-checked** candidate coefficient/running suppliers; the stronger stated flow and scheme match are **OPEN**. |

NT2's map admissibility is part of the contract: free blocked flux variances must remain bounded and converge; simple straight decimation fails that test (`parts/witness.md:880–890`). Matching is o(g_m^2), o(g_m^{2k}), o(g_m^4) on every fixed finite template family (`:975–987`); the running test is the leading logarithm, not a per-step derivative (`:989–1000`). A result on a mixture must not be silently asserted on each component. No continuous-r interpolation follows from the L-adic proposal (`:870–878`). These qualifications remain attached to J5; they are not new physical axioms.


### 5.5 Results synchronized since 2026-11-05

Each row is a node, or a named refinement of a parent node. **Owner** is a FINISH lane name, not a grant of mathematical authority. Quotes are the recorded evidence for the standing, scope and repairs; this lane did not repeat any proof check. A repair written in a check is retained here as part of the conditional supplier even if its source file still awaits that text edit.

| Node (parent) | Standing; owner | Recorded result, scope, inputs and repairs; file:line quote |
|---|---|---|
| CM-PART (K1/P4) | **proved**, checked; `cm-claude` | Lemma R, Theorems 1–2 and Lemma W pass on (b3), local balls about a global real base, and the specified W′⊂Ω cell class. `cm-claude.md:219–220`; `../gates/cm-gate.md:51,71`: “ADVANCE as an implication retaining (Inv-x) and (Sh3-u)” / “ADVANCE on their stated local class”. Keep W′, base positivity, sheet readings, the new rate floors where used and λLM≥324κ₁. |
| CM-O3 (K1) | **OPEN**; `cm-claude` | `../gates/cm-gate.md:87`: “CM merger: not established as claimed”. Old-term local reads must be placed in the supplier's analytic class and assigned companion family. The cited random-walk leaf is owned by `b99-w`; do not relaunch it as CM. Original MF endpoint and O2/Inv-x/Sh3-u remain distinguished. |
| CA-PART (K3/R6) | **proved**, checked conditional implication; `ca-claude` | Combined `ca-claude.md:208–214` + replacement `ca-f.md:178–190`. `../gates/ca-gate.md:144–146`: “valid implication from its complete displayed inputs”. Replace original F's blocked datum cut by S/R/F′. Retain every input in gate §5, add Lemma E/N9 to R, keep N8-current independent of (d′), and use M≥1's 1/600<1/85 budget. This does not discharge CA. |
| CA-BIN (K3/R6) | **OPEN** (conditional cell bounds checked; full sealing conclusion BLOCKED); `b-in` | `../gates/b-in-gate.md:217-227`: REVISE, BLOCK on the full sealing conclusion. Restricted B1/B2 cell estimates, Lemmas I, C, J, BCH, A_n, E' ADVANCE; Round 2 (row 399, `b-in-r2.md`; check `../gates/b-in-r2-gate.md:176-190`): the three local BLOCKs now have conditional repairs. B2(c) ADVANCE after the equality-case repair; P ADVANCE for geometric placement, REVISE its identification with every use of B_S (interface coverage, units and raw-core matching stay consumer obligations); Sh' ADVANCE from read-complete (K-id), with global 1(e) admission and ca-f's (N1)-(N8) kept as explicit premises. The full sealing conclusion is still BLOCKED from the shortened input list. `b-in.md` (row 389).
| CA-LAYER (K3/R6) | **OPEN**; `layer-thm` (moved from `stage-claude`, 2026-11-07) | Full (N1)/(L), all four entries, arbitrary weights, actual completion kernels and complex range. `../gates/stage-gate.md:157`: “BLOCK its use as a discharge of ca-f's full (N1)”. STAGE-PART is only zero-field/block datum. |
| CA-FIELD (K3/R6) | **OPEN**; none | (N2) actual G″J all-weight derivative datum norm and operator identification. `../gates/ca-gate.md:78`: “Retain both the operator identification and (N2)'s estimate.” |
| CA-BRACKET (K3/B99b-T314) | **OPEN**; none | (N3) decoupling bracket in the full datum norm, including the Laplacian qualification. `../gates/ca-gate.md:131`: “Passing to every datum-norm entry is additional.” A pointwise CMP 99b citation is not this application. |
| CA-MATCH (K3/R6) | **OPEN**; `ca-claude` | Retain G-sep, actual kernels/frames, N7 kernel admission, N8-current, full read sets and every-label geometry. `../gates/ca-gate.md:131–135` lists these separately; `:120`: “no noncircular supplier”, rather than a refutation of B-in. |
| K8-CORR (K8/BP05) | **proved**, checked; `l17c` | `l17c.md:512–538,544`; `../gates/l17c-gate.md:97`: “corrected L17 suffices for every active consumer”; `../gates/p20-gate.md:95`: “now rests on a checked P20”. Keep the Stage-7 ceiling, P20's gap-order repair F1 and default inward-free determining sets. Original ε₀-only L17/Q119 stays OPEN. |
| P20 (K8-CORR/R1) | **proved**, checked; `b109` | Quadratic-radius bound under (104), a1-balaban (8.2),(9.1)–(9.2), flat-port F0 and required gap. `../gates/p20-gate.md:13`: “ADVANCE, as an implication”; `:83`: choose CA-I R₁ after a1's localization length. (105) is unused. P15 bootstrap/P19 are checked; P1–P14/P17–P18 are not checked by this reading (`:14–15`). F0 provenance and a1 (10.2) remain inputs (`:97`). |
| B109-PART (R1/BP07) | **proved**, not wholly checked; `b109` | `b109.md:3689–3730` records P1–P21 with premises. P20 is separately checked; no blanket P1–P21 reading is recorded. `../gates/p20-gate.md:15`: “not read by P20; not checked here”. S1–S12 and the full small-field theorem remain OPEN. |
| B119-PART (R1/BC1) | **proved**, unchecked; `b119` | `b119.md:1354–1419`: B1–B12 implications; Q119 is the original K8 endpoint. `../gates/p20-gate.md:95`: “inherits the same resolution” means the corrected consumer route, not proof of ε₀-only Q119 or of all CMP 119 theorems. |
| B98-A (BP09/BC1) | **proved**, checked; `b98` | CA-I 4.6:lem-averaging-locality, all (a)–(d), not all CMP 98 propositions. `b98.md:655`; `../gates/b98-gate.md:29`: “proved, all clauses (a)-(d)”. |
| B98-B (BC5) | **proved**, checked with repairs; `b98` | CA-II 8.11:lem-signed-averaging in top units, using the actual kₒ-fold iterate. `../gates/b98-gate.md:33`: “needs the iterated average”; `b98-iterate.md:54–102`; `../gates/b98i-gate.md:24–30,161`: “covers the iterated (B3) ... with the written repairs”. Carry repair 1 (group log chart, constants with slack and common threshold). |
| B98-C (BC1/BC5) | **proved**, checked with repairs; `b98` | CA-I 4.9:prop-cube-gauge-regular, enclosing-cube (C4)–(C5), k≥0. `../gates/b98-gate.md:35` identifies the k=0 case; `../gates/b98i-gate.md:31–34,161` supplies it with repair 2 in Balaban's norm. Extra normalized Landau/site-average (1.137)–(1.138) and CMP 98 Prop 6 (164) are excluded (`../gates/b98-gate.md:49`). |
| B102-O (BC1/BP07) | **proved**, checked; `b102` | H1–H14/Lemma O on admitted nests. `../gates/b102-gate-a.md:4`: “First failing step: none”; its `:18–33` retains H6.7, FP1, flat-port, P82 and a1 inputs. This is not intrinsic local independent-current walk supply. |
| B102-T1 (MU/BC1) | **proved**, checked with repairs; `b102` | Real minimal/unique critical regular orbit, d=4, SU(2), uniform depth/mesh/volume; Hölder exponent strictly below 1. `../gates/b102-gate-b.md:47–50`: “ADVANCE (S1)” / “after the two-line addition W1”. Keep all inputs there, the admissible nest and order floors; β=1 is not proved. |
| B102-P9 (MU/BC1) | **proved**, checked with repairs at stated scope; `b102` | Complex datum branch and orbit extension on saturation. `../gates/b102-gate-b.md:20–24,53–56` retains S2 (write the (19)–(21) clause from H24 integration) and S3 (external-background holomorphy only sketched, not redone). No bound after a large complex gauge. |
| B102-RESPONSE (UI/BP22) | **proved**, checked with repairs; `b102` | H24, (189) at δ₀/4 and five members of (190) at δ₀/8, true-current graph. `../gates/b102-gate-b.md:45`: “ADVANCE (W2)”; `../gates/uses-b102.md:298`: “outstanding ... passage ... is supplied by H24”. Keep W1, W2 and actual admitted datum/forcing norms. |
| B102-USES (R2/R8/R9) | **proved**, checked coverage implication; `b102` | `../gates/uses-b102.md:278`: 188 clear rows, 110 C, 60 C+, 18 N, plus 20 ambiguous rows; SU(2) only. Carry G2–G4 chart/localization/radius floors, subunit Hölder scope, rate δ₀/8, S2 clause and admitted nests (`:289–300`). This does not prove the account's arguments or nest admission. |
| B102-RESIDUAL (R2/R8/R9) | **OPEN**; `b102` | `../gates/uses-b102.md:282–287`: (7♭) large-field transfer; 4.12 non-admissible/gapless partitions and weaker uniqueness class; free independent current; ε₀-only (1.17); strict local contraction; external-background holomorphy. B102 does not supply these. The corrected K8-CORR route is separate. |
| B99-PART (BP07/BC1) | **proved**, unchecked; `b99-w` | `b99.md:2528–2565`: “The full B99 targets are not proved”; B1–B20 are conditional pieces, including real gap U and resolvent/root given intrinsic analytic form/accretivity. `prior/b99-w.md` is a retrieval record, not a check. |
| B99-W (K1/BP07/BC1) | **proved** (conditional implication, clauses 1-4; checked by Codex, `../gates/b99w-gate.md:190-194`: REVISE the note, ADVANCE the repaired Lemma W; repairs to apply in `b99-w.md`); `b99-w` | `b99-w.md` Lemma W on the true-current graph from b102 H9-H12, B13, B11, B15 (63), H16 and the account's level-k maps and (HD). Not a complete CM supplier: `../gates/b99w-gate.md:179-186` keeps OPEN B17's local accretivity (for the W to B17 route), the conditioned/root families at independent currents with switches (CA-II 2181-2277 (b3)), identification with the assigned family (owned by CO/`ol`), and CM-O3.
| MU-RADII (MU/R6/R8) | **proved**, checked with repair; `mu-radii` | `mu-radii.md:901–912`; `../gates/mur-gate.md:4`: “No conclusion changes”; `:104` replaces C_Q by max{1,K_loc/(5.6 K_ax M C_M^av)}. Covers needed stage/4.28 and II:35714 uses after (8),(11). Block-constant Landau-gauge readings (a),(c) are refuted, corrected relative-gauge identities/norms suffice for consumers; literal gauge bound 2 and whole-rim/B₃ readings remain unproved. |
| MU-USES (MU/R8/R9) | **proved**, checked coverage implication; `mu-uses-check` | `../gates/mu-uses-check.md:124–142,156`: “ADVANCE for the coverage claims marked ‘covered’”. RR uses regular real restriction, domination and ceiling (C); CN covers bounded complex boxes after c(d)M C_𝔞 sup α<δ. 4.29 and 8.5 need their explicit radius ceilings. CA-III 9.1 is off-chain/unassessed. |
| MU-RESIDUAL (R8) | **OPEN**; `mu-uses-check` | `../gates/mu-uses-check.md:148–149`: “Domination is needed and not stated”; “Complex continuations on unbounded two-layer boxes: not covered”. No on-chain consumer of the latter was found. Keep the former CMP 122b application as a separate interface. |
| UI-USES (UI/R2) | **proved**, checked coverage; `uses-ui-oc` | `../gates/uses-ui-oc.md:93`: eighteen of twenty rows covered; the two layerwise rows have (a),(b) covered and (c) after c₁₂LMB^(109)α₀,j+α₁,j+α₂≤c♯ at p=j. `:95`: “repair in D1 is by Claude and not yet checked by Codex”. UI's original proof remains checked; this extra repair has that separate standing. |
| OC-USES (OC/R2) | **proved**, checked coverage; `uses-ui-oc` | `../gates/uses-ui-oc.md:94`: “seed uses are covered after ... ε₀<c₉₈”; B₁₂ covered. Transport at ⟨8⟩,⟨9⟩,⟨13⟩, general-nest seeds and clause (0)(a′) as a whole are not supplied by OC. TC-THIN is their conditional supplier, not a proved actual interface. |
| PDA-T (PDA/R2) | **proved**, unchecked new implication; `uses-pda-um` | `../gates/uses-pda-um.md:177`: “R1 and N2 (proved here, not yet checked by Codex)” derive T-step (A2) from collar avoidance (b) with gap 8LM, and inductively (A1) with gap LM plus (A2). Keep (P2)–(P4), 4.4(c)'s hypothesis and indexing; no analytic admission is supplied. Existing PDA one-operation proof remains checked. |
| PDA-USES (PDA/R2) | **proved**, checked coverage; `uses-pda-um` | `../gates/uses-pda-um.md:169–178`: 29 uses: 17 covered, four (A1)-only, four (A2)-only not covered, 45628 partial, 48132 not covered as stated; constant-choice and point-count rows separate. UM's five clear uses and mediated C_β uses covered, conditional on UM and (R-a)–(R-e); UM's check now exists. |
| STAGE-PART (R2/AI-REP) | **proved**, checked restricted implications; `stage-claude` | `../gates/stage-gate.md:163–164`: “block-datum L estimate ... with ... summability ... and corrected constants”; “ADVANCE the corresponding conditional scalar admission statement”. BL needs settled determining neighbourhood, identical functionals/units, absolute ball and derivative conversion. L needs M-chart, uniform kernel summability, matched K10 switch family and corrected constants. |
| STAGE-MATCH (R2/AI-REP) | **OPEN**; `stage-claude` | `../gates/stage-gate.md:104,122,157,165`: Theorem S is “BLOCK” for the prescribed actual response; independent-current chart-partner identification, full Σ-space match, branch/admission/common gauges and FC's quantitative condition remain. `../gates/fc-gate.md:167-182` (row 392): the current half is a conditional chart-rule replacement (C1 and Lemma R ADVANCE), not closure of AD-ST(2); the complex frame change stays BLOCK (Lemma G seams and datum conversion, (2.3) membership, reduction to CC). The partial layer is not CA's full N1. H-STAGE integration remains unsupplied. |
| J1-CA / J1-IN / J1-ID / J1-ORDER (J1) | **OPEN**; `t0-joins` | `t0-joins.md:52–62`; `../gates/j16-check.md:62`: “Open: J1-ID, J1-ORDER, J1-CA and J1-IN”. Reduction checked after integer-exponent/label repairs; a CA-only interface is recommended, not supplied. |

| CM-RW (K1/R8) | **OPEN**; `b99-w` | Full cited `5.2:lem-random-walk-bounds`, not supplied by an unfinished true-current W-b claim. `../gates/cm-gate.md:26`: “proof is expressly not reproduced”; `:87` retains the cited leaf. Clauses (I)/(III), reference transfer and complex local decouplings remain at their consumed scopes. |
| P4-SHEET (P4/CM-PART) | **OPEN**; `port-p4` | `../gates/cm-gate.md:55`: “O4 is not discharged by this check.” Keep (Inv-x), (Sh3-u), one-box inversion and datum-uniform sheet majorants as named inputs; Theorem 1 is checked conditional on them. |

| CH4-AUX (K5) | **OPEN**; `ch-r1` | `ch-bridge.md:270–277`: first localized auxiliary-stage admission remains open; `cwch.md:372` retains it for the link-3 input. Owner moved from the finished `ch-bridge` lane to `ch-r1` by the lead, 2026-11-07 (row 412). Digest: `prior/ch.md`. |
| B119-THEOREMS (R1/BC1) | **OPEN**; `b119` | `b119.md:1354–1419` supplies B1–B12, not full CMP 119 Theorems 1/2/Corollary 3; corrected K8 is only one ingredient (`../gates/p20-gate.md:95–97`). Existing `b119` ownership remains. |
| MU-LITERAL (MU-RADII) | **OPEN**; `mu-radii` | `mu-radii.md:909–910`, `../gates/mur-gate.md:106–108`: literal gauge bound 2 and unweighted whole-rim/B₃ readings remain unproved and unneeded at the identified consumers. These are distinct from MU-RESIDUAL's domination/unbounded-box interfaces. |
| PDA-A2 (R2) | **OPEN** at actual full-use scope; `pda` | `pda.md:245`: (A2) outside the checked one-operation geometric proof. PDA-T is an unchecked candidate for all-history geometry, with its retained hypotheses (`../gates/uses-pda-um.md:177–182`); no analytic supplier follows. |

### 5.6 Detailed account inputs used by citation

These steps are **theirs-cited**, not OPEN merely because their complete proofs have not been ported. The scope is the account's conditional deduction. Every unsupplied premise or identification stays in K/R/J and §5.5. No incomplete, outstanding, cited-only, unwritten or model step is promoted by an index's generic PROVED flag.

| Node | Account label and proof locus | Parent and retained scope; evidence quote; owner |
|---|---|---|
| TC-BALL | CA-I `4.14:lem-local-balls`, 46800–46950 | P4/CM-PART. Global real base, W-format, compatible admissible geometry, M>2L and M/(2L) cutoff; not arbitrary merely local-real data. CA-I:46928–46931: “So ... analytic on the local ball”; `../gates/cm-gate.md:53`: “written conditional proof”. Owner: `port-p4`. |
| TC-THIN | CA-I `4.9:lem-thin-cube-gradient`, 37902–38144 | R2/OC-USES, including its stated exclusions and (a)–(f), gluing, factorization, real-stage regularity, all floors/ceilings. `../gates/uses-ui-oc.md:94`: “account statements declared PROVED and not ported here”. This supplies their implication, not the missing actual transport/admission. Owner: `uses-ui-oc`. |
| TC-FAMILY | CA-I `4.26:lem-family-consumption`, 117492–117700 | STAGE-PART/R6. Fat regularity space, recorded recursive layer/bump estimates, window, units and matching premises. `../gates/stage-gate.md:25`: “analogous family-consumption implication, with its own hypotheses”. Owner: `stage-claude`. |
| TC-DILATION | CA-II `5.2:cor-response-dilation`, 13933–14131 | STAGE-PART/R2. `../gates/stage-gate.md:25`: “states and proves the all-blocks implication with the listed antecedents”. Uniform scalar specialization is theirs; actual AD-ST current/space matching remains OPEN. CA-II locus is taken from that check; not fetched/read anew here. Owner: `stage-claude`. |
| TC-CANCEL | CA-I `4.22:lem-current-localisation`, cancellation substep 92500–92558 | CA-PART/N4, Euler–Lagrange identity, matched determining sets, Q bounds and actual σ=1 kernel. `../gates/ca-gate.md:140`: “cancellation identity in (N4) is proved”. Not N2/N3's all-weight datum norm. Owner: `ca-claude`. |
| TC-CURRENT | CA-I `4.4:eq-current-remainder-a` real-current formula, 10335–10347 | CA-PART/real-current algebra only. `../gates/ca-gate.md:140`: “real-current formula is worked out”. Its actual-kernel analytic application remains conditional. Owner: `ca-claude`. |

ER8 (SA:6586–6630) is already proved conditional on ER7; mechanism 8 and the quadratic budget (SA:9746–9753,9899–9911) are Sussman–Alpoge's. K8-CORR/P20 provide the recorded repository supplier/consumer implementation, so ER8 is not counted as a new independent open lemma. `wu-l17.md:272,292,296–301` and `out-l17.md:182–189` retain that attribution, default determining sets and SU(2)-only checked derivations. Their write-ups do not supply MU/OC, stage backgrounds, re-minimization or the rest of clause (0).

## 6. Checks still owed

Checks record readings; they do not supply open hypotheses. Completed Q1–Q6 and Q8 must not be relaunched because an older file says “not yet checked”.

| Check unit | Current disposition |
|---|---|
| Q1 P6 | Completed by Claude, `../gates/p6a-check.md:16–18`, `../gates/p6b-check.md:60–61`; conditional, with the source/input repairs recorded in §3 and C-stability/W5-rim still OPEN. |
| Q2 P8 | Completed by Claude, `../gates/p8-check.md:28–30`; even centred torus RP and all original inputs retained. |
| Q3 P8b | Completed by Claude, `../gates/p8-check.md:31–36`; restricted curvature reconstruction, not full T0. |
| Q4 P9 | Completed by Claude with θ≤1/2 repair, `../gates/p9-check.md:6,30–32`. |
| Q5 P9b | Completed by Claude, first failing step none, `../gates/p9-check.md:29`; H-jet, support/tail and use-site hypotheses survive. |
| Q6 P10 | Completed by Claude, `../gates/p10-check.md:99–105`; conditional and repaired. |
| Q7 PI | Still owed; `port-pi.md:542–551`. No later check file found in this pinned checkout. |
| Q8 UM | Completed by Claude, `../gates/um-gate.md:57–73`. Citation repairs remain attached. |
| Q9 OL | Round 4 completed by Claude, `../gates/ol-gate.md:121`, with D1. That gate explicitly did not recheck rounds 1–3 (`:14,124–129`); their used proofs/identifications remain to be read. Do not rerun round 4. |
| Q10 B109 | P19/P20 and the used P15 bootstrap completed by Claude (`../gates/p20-gate.md:12–15`); other used P1–P21 pieces, including P18/LQ, still need their reading. Retain F1 and default determining sets. |

Other outstanding readings: the B99 pieces and unfinished W-b manuscript; PDA-T R1/N2; UI-USES' extra ceiling repair; the new `wu-mu.md` write-up (`:8,213`: “has not been checked by the other model”). CM, CA, MU-radii, B98 iterate, B102 and J1/J6 already have their recorded checks at the precise scopes above. Written gate repairs retained in the skeleton still need folding into their proof files by those owners; this lane edits no proof file. Assembly interfaces J1–J5 and actual T0 realization remain open even where their reductions/implications are checked.

## 7. Shortest remaining route to T0, in order

This is the shortest **presently specified route in this map**, not a theorem of optimality. It avoids adding tuned uniqueness or universal periodic-state recognition where existence needs only a selected volume-first hierarchy. It does not assume that any proposed bridge will succeed.

1. **Use the checked coupling repairs at their recorded scopes, and fix the common construction dictionary.** UM and round-4 OL-transfer have checks; Q9 retains the earlier OL inputs and their readings. Keep OL's original-family leaf open outside those consumers. Write J1's actual current, gauge, source, normalization and constant-order matches. This determines which further proofs are usable together.
2. **Close the hard joint-induction inputs at their exact scopes.** K1 (original words at the fixed rate), K8-CORR with P20 for the corrected admission, and R1 (full small-field step), K2/K3 (outside and completion admission), K7/R7 (scalar reality and the full positive exact history construction), and R2–R6/BP/BC supply must all be available. These branches can be worked independently where their prerequisites permit; there is no asserted implication K1⇒K2⇒K3. Reuse MU/LRB/OC/UI/PDA. Complete Q10 for every B109 piece actually consumed. Do not restart the invalid universal-path route.
3. **Close the sourced induction and normalized estimates.** K4/K5 and R8 supply the missing window/switch inputs. Use checked P1/P4/P5/P7, ported P6/P10 and frozen LSC. Use completed Q1/Q6 with their repairs; finish Q7. Derive J2 explicitly from the resulting source format, including ordinary repeated/mirror sources, rooted geometry and the common vacuum convention. This is the essential join into the frozen downstream chain.
4. **Finish the CA witness and its component extension.** Resolve R9/R10 with the precise P9 use-site bounds, supply the retained free/background inputs, and use completed Q4/Q5 with their repairs. Use the sufficiently small interior coupling when that avoids an unnecessary supremum-endpoint claim. Prove J3 and the needed J4 lower witness on the actual PH1 realizations, or supply the full frozen TP1 package if that route is shorter. CA's torus-uniform bound alone does not settle this choice.
5. **Take volume first, then spacing, and apply the frozen chain.** Use completed Q2/Q3 for the CA branch used. LG1 gives fixed-cutoff states and all mirrors; SR1 gives all-state bounds/growth; CL1 selects the hierarchy; PH1 supplies clustering components and the unique vacuum. RO1 then supplies full componentwise O(4) and insertion density; WR1 reconstructs each scalar theory. Use J6's checked domain passage and retain the common-realization identification. No new derivation of these frozen implications is needed unless an input changes.
6. **Close NT1 and NT2 on the same selected theory.** Apply TP1 Lemma 7.2 once J4 and PH1(5) hold. Supply all eight J5 witness inputs, the admissible joint blocked state and map, and the observable-scheme identification. The coefficient/running work from steps 1–3 can supply only the portions explicitly matched. NT2 is separate interacting work and may proceed earlier; it is written last here because the final assertion needs the constructed state.
7. **Assemble the actual theorem, with no status promotion.** All leaf contracts, their quantifiers and order must hold simultaneously. State the scalar observable/test-domain scope, component choice, and NT1/NT2 precisely. The checklist is not the proof; the cited written implications and supplied leaves must form it.

Do **not** add AV, AII-T-a, AV-f, general SU(N), mass gap, full gauge-sector identification, or arbitrary contact terms to this shortest route. They remain separately mapped or explicitly outside the working contract. Conversely, omitting J2, componentwise J3/J4, or NT2 would give a weaker target, not T0.

## 8. Recovery and verification limits

The original map recorded scratch paths `/tmp/t0map-6d9df38c2/`; those are historical recovery locators. Row 391 fetched SA and CA-I once to `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`. Their identities are:

- SA, 32,992 lines: `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`.
- CA-I, 166,711 lines: `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`.

GOAL and the requested FINISH guidance were read first. The outline index README, relevant chunk rows/neighbors and obligations, and the CA 4.12–4.19 index were used before the corresponding bounded source reads. Main statement checks: SA:66–130; CA-I:2512–3016, in bounded pieces. The source/OS bridge readings include SA:4086–4122,4400–4474,4572–4627. The CA re-blocking/minimizer/prepared/stage scope checks include CA-I:45085–45115,45162–45175,45203–45224,45582–45614,49495–49546,54985–55000. Local import, hypothesis, Result and latest change-log sections govern the supplier map. This is not a fresh line-by-line check of all their proofs.

The workflow file is absent from this sparse checkout; row 391 read it and the worker procedure from origin/main without checking them out. The planning AGENTS was read without changing the working tree. No audit, external post or status promotion was performed. Searches stayed within the allowed checkout and task scratch files. No mathematical claim rests on a tool run. Text/hash/count checks are editorial bookkeeping only.

Current recovery decisions: use checked UM/OL at their scopes and retain OL's earlier unread proofs; supply the actual hard-core/stage interfaces; derive the ordinary-source join; obtain component witnesses; retain NT2 and use the checked J6 implication. Failed path and original-word routes remain explicitly recorded above. Refresh this map against source changes before using a newer endpoint; never inherit a stale “open” or “closed” label without its scope.

Row 391 changes only `t0-tree.md`, `open-registry.md`, and the one-line history headers in `assembly-status.md`, `port-map.md`, `open-core.md`. GOAL/FINISH, proof texts, ledgers and audits are untouched.

## Result

**T0 is open. This reading and bookkeeping sync grants no scientific status.** The full T0 branches and all original K/R/BP/BC/J contracts remain visible. Checked implications retain their named inputs and repairs. The original ε₀-only L17, CM's O3 interface, CA's base/layer interfaces, and the full small-field/source chain are not promoted by the corrected or partial suppliers. J6 is a checked conditional domain passage. NT1/NT2 and componentwise joins remain required.

## 9. Hardening tally

Count convention: **175 named nodes**, listed below exactly once. These are supplier contracts, partial suppliers and explicit interface/aggregate nodes, not independent mathematical lemmas. Repeated uses in the diagram, TP1/NT2 import expansions and Q reading tasks are not extra nodes. K8 and K8-CORR are different statements; B99-W is an unfinished, unchecked implication claim. Composite OPEN nodes retain their proved children. “Proved” includes checked and unchecked written implications; the check and completeness qualifiers in §§3–6 remain binding. This count cannot be read as 56 completed actual-construction inputs.

| Standing | Nodes |
|---|---:|
| proved | 57 |
| ported-checked | 22 |
| ported-unchecked | 1 |
| theirs-cited | 6 |
| OPEN | 89 |
| Total | 175 |

**Exact node inventory, by standing** (anchors are registry backlinks):

- **proved**: <a id="node-mu"></a>MU, <a id="node-lrb"></a>LRB, <a id="node-oc"></a>OC, <a id="node-ui"></a>UI, <a id="node-pda"></a>PDA, <a id="node-lsc"></a>LSC, <a id="node-um"></a>UM, <a id="node-ol"></a>OL, <a id="node-b01"></a>B01, <a id="node-b02"></a>B02, <a id="node-b03"></a>B03, <a id="node-b05"></a>B05, <a id="node-b06"></a>B06, <a id="node-b07"></a>B07, <a id="node-b08"></a>B08, <a id="node-b09"></a>B09, <a id="node-b10"></a>B10, <a id="node-b11"></a>B11, <a id="node-b12"></a>B12, <a id="node-b14"></a>B14, <a id="node-b15"></a>B15, <a id="node-b17"></a>B17, <a id="node-b18"></a>B18, <a id="node-b20"></a>B20, <a id="node-b23"></a>B23, <a id="node-b24"></a>B24, <a id="node-b25"></a>B25, <a id="node-b26"></a>B26, <a id="node-b27"></a>B27, <a id="node-b28"></a>B28, <a id="node-b29"></a>B29, <a id="node-bp01"></a>BP01, <a id="node-bc4"></a>BC4, <a id="node-j6"></a>J6, <a id="node-cm-part"></a>CM-PART, <a id="node-ca-part"></a>CA-PART, <a id="node-k8-corr"></a>K8-CORR, <a id="node-p20"></a>P20, <a id="node-b109-part"></a>B109-PART, <a id="node-b119-part"></a>B119-PART, <a id="node-b98-a"></a>B98-A, <a id="node-b98-b"></a>B98-B, <a id="node-b98-c"></a>B98-C, <a id="node-b102-o"></a>B102-O, <a id="node-b102-t1"></a>B102-T1, <a id="node-b102-p9"></a>B102-P9, <a id="node-b102-response"></a>B102-RESPONSE, <a id="node-b102-uses"></a>B102-USES, <a id="node-b99-part"></a>B99-PART, <a id="node-mu-radii"></a>MU-RADII, <a id="node-mu-uses"></a>MU-USES, <a id="node-ui-uses"></a>UI-USES, <a id="node-oc-uses"></a>OC-USES, <a id="node-pda-t"></a>PDA-T, <a id="node-pda-uses"></a>PDA-USES, <a id="node-stage-part"></a>STAGE-PART.

- **ported-checked**: <a id="node-a0"></a>A0, <a id="node-ai-rep"></a>AI-REP, <a id="node-ai-stab"></a>AI-STAB, <a id="node-ai-exact"></a>AI-EXACT, <a id="node-aiii-flow"></a>AIII-FLOW, <a id="node-aiii-b"></a>AIII-B, <a id="node-aii-t-b"></a>AII-T-B, <a id="node-aii-r"></a>AII-R, <a id="node-aiv"></a>AIV, <a id="node-p1"></a>P1, <a id="node-p3"></a>P3, <a id="node-p4"></a>P4, <a id="node-p5"></a>P5, <a id="node-p6"></a>P6, <a id="node-p7"></a>P7, <a id="node-p8"></a>P8, <a id="node-p8b"></a>P8b, <a id="node-p9"></a>P9, <a id="node-p9b"></a>P9b, <a id="node-p10"></a>P10, <a id="node-b21"></a>B21, <a id="node-b22"></a>B22.

- **ported-unchecked**: <a id="node-pi"></a>PI.

- **theirs-cited**: <a id="node-tc-ball"></a>TC-BALL, <a id="node-tc-thin"></a>TC-THIN, <a id="node-tc-family"></a>TC-FAMILY, <a id="node-tc-dilation"></a>TC-DILATION, <a id="node-tc-cancel"></a>TC-CANCEL, <a id="node-tc-current"></a>TC-CURRENT.

- **OPEN**: <a id="node-t0"></a>T0, <a id="node-e"></a>E, <a id="node-e0"></a>E0, <a id="node-e1"></a>E1, <a id="node-e2"></a>E2, <a id="node-e3"></a>E3, <a id="node-e4"></a>E4, <a id="node-w"></a>W, <a id="node-n"></a>N, <a id="node-nt1"></a>NT1, <a id="node-nt2"></a>NT2, <a id="node-av-core"></a>AV-CORE, <a id="node-av-f"></a>AV-F, <a id="node-b04"></a>B04, <a id="node-b13"></a>B13, <a id="node-b16"></a>B16, <a id="node-b19"></a>B19, <a id="node-k1"></a>K1, <a id="node-k2"></a>K2, <a id="node-k3"></a>K3, <a id="node-k4"></a>K4, <a id="node-k5"></a>K5, <a id="node-k6"></a>K6, <a id="node-k7"></a>K7, <a id="node-k8"></a>K8, <a id="node-r1"></a>R1, <a id="node-r2"></a>R2, <a id="node-r3"></a>R3, <a id="node-r4"></a>R4, <a id="node-r5"></a>R5, <a id="node-r6"></a>R6, <a id="node-r7"></a>R7, <a id="node-r8"></a>R8, <a id="node-r9"></a>R9, <a id="node-r10"></a>R10, <a id="node-r11"></a>R11, <a id="node-r12"></a>R12, <a id="node-bp02"></a>BP02, <a id="node-bp03"></a>BP03, <a id="node-bp04"></a>BP04, <a id="node-bp05"></a>BP05, <a id="node-bp06"></a>BP06, <a id="node-bp07"></a>BP07, <a id="node-bp08"></a>BP08, <a id="node-bp09"></a>BP09, <a id="node-bp10"></a>BP10, <a id="node-bp11"></a>BP11, <a id="node-bp12"></a>BP12, <a id="node-bp13"></a>BP13, <a id="node-bp14"></a>BP14, <a id="node-bp15"></a>BP15, <a id="node-bp16"></a>BP16, <a id="node-bp17"></a>BP17, <a id="node-bp18"></a>BP18, <a id="node-bp19"></a>BP19, <a id="node-bp20"></a>BP20, <a id="node-bp21"></a>BP21, <a id="node-bp22"></a>BP22, <a id="node-bc1"></a>BC1, <a id="node-bc2"></a>BC2, <a id="node-bc3"></a>BC3, <a id="node-bc5"></a>BC5, <a id="node-bc6"></a>BC6, <a id="node-j1"></a>J1, <a id="node-j2"></a>J2, <a id="node-j3"></a>J3, <a id="node-j4"></a>J4, <a id="node-j5"></a>J5, <a id="node-cm-o3"></a>CM-O3, <a id="node-ca-bin"></a>CA-BIN, <a id="node-ca-layer"></a>CA-LAYER, <a id="node-ca-field"></a>CA-FIELD, <a id="node-ca-bracket"></a>CA-BRACKET, <a id="node-ca-match"></a>CA-MATCH, <a id="node-b102-residual"></a>B102-RESIDUAL, <a id="node-mu-residual"></a>MU-RESIDUAL, <a id="node-stage-match"></a>STAGE-MATCH, <a id="node-j1-ca"></a>J1-CA, <a id="node-j1-in"></a>J1-IN, <a id="node-j1-id"></a>J1-ID, <a id="node-j1-order"></a>J1-ORDER, <a id="node-c-stability"></a>C-stability, <a id="node-w5-rim"></a>W5-rim, <a id="node-cm-rw"></a>CM-RW, <a id="node-p4-sheet"></a>P4-SHEET, <a id="node-ch4-aux"></a>CH4-AUX, <a id="node-b119-theorems"></a>B119-THEOREMS, <a id="node-mu-literal"></a>MU-LITERAL, <a id="node-pda-a2"></a>PDA-A2.

**Theirs-cited verification queue**: TC-BALL — CA-I `4.14:lem-local-balls`; TC-THIN — CA-I `4.9:lem-thin-cube-gradient`; TC-FAMILY — CA-I `4.26:lem-family-consumption`; TC-DILATION — CA-II `5.2:cor-response-dilation`; TC-CANCEL — cancellation substep of CA-I `4.22:lem-current-localisation`; TC-CURRENT — CA-I `4.4:eq-current-remainder-a` real-current derivation. Exact scope, sources and owners are in §5.6. Their detailed proofs are cited now; the final hardening pass still owes their readings. Other classical imports and optional AV branches retain the separate scopes in this tree; this is not a count of every numbered statement in the account.

## 10. Synchronization receipts and change log

The following covers every FINISH row ≥300 with an extant result/check at `5467e79de`, including stale “queued” rows whose files exist. Ranges group a result with its checks; each numbered row listed is accounted for. An inventory, digest or outward draft adds no proof status of its own.

| FINISH row(s) | Tree node(s); result/check evidence and recorded disposition |
|---|---|
| 300,304 | B13/B16/B20–B24, J2/J3; `ro1-vs-ca.md:24–73`, `o4-two-point.md:192–203`: frozen two-point shortcut only, no all-order/component substitution. |
| 301,345,378 | K1, CM-PART/CM-O3; `mf.md:1528–1572`, `cm-claude.md:217–223`, `../gates/cm-gate.md:87`: “not established as claimed”; retain the checked restricted statements and O3. |
| 302 | K7/R7; `pd.md:1442–1470`: original scalar-reality endpoint still open; no cv-claude result exists. |
| 303,307,308,311,315 | P1/P3/P4/P5/P7; existing checked scopes and repairs in §3. `../gates/p1-base-gate.md`, `p3-free-gate.md`, `p4-operator-gate.md`, `p5-induction-gate.md`, `p7-torus-gate.md` are the existing receipts; no duplicate reading. |
| 305,306,309,312 | LRB/UI/OC/PDA; existing frozen implications, refined only by the later use checks below. `lrb.md:833–862`, `ui.md:549–572`, `oc.md:243–265`, `pda.md:241–247`. |
| 310,348 | K2/R2; `rb.md:796–802` stays OPEN; `cr-claude.md:10`: “Sections follow as they are written.” The header is not a result. |
| 313,318 | LSC/AIII-B/R7; `lsc.md:688–724`, `../gates/nrm-check.md:1–21`, `../gates/lsc2-gate.md`: round-1 bare floor superseded by checked round-2 **vacuum-normalized** upper/floor. E_vac cancels only at the stated consumers. |
| 314,321,331 | K4/K5 and CH4-Aux; `wd.md:365–384`, `ph.md:468–474`, `ch-bridge.md:266–277`: analytic admission endpoints remain OPEN. |
| 316,343,344 | P6/AIII-FLOW/R8; checks `../gates/p6a-check.md:16–32`, `../gates/p6b-check.md:20–61`: checked conditional port, W5-rim and C-stability still OPEN, all repairs in §3. |
| 317,338 | UM/Q8; `um.md:563–584`, `../gates/um-gate.md:57–73`: “ADVANCE”, citation repairs F1–F3 and four hypotheses retained. |
| 319,347,382,386 | K3/R6, CA-PART/CA-BIN/CA-LAYER/CA-FIELD/CA-BRACKET/CA-MATCH; `arr.md:955–978`, `ca-claude.md:208–214`, `ca-f.md:178–190`, `../gates/ca-gate.md:128–146`. Combined implication checked; base and full layer/datum/application inputs remain OPEN. |
| 320,339 | OL/K6/Q9; `ol.md:2813–2845`, `../gates/ol-gate.md:121–130`: round-4 “ADVANCE” after D1; earlier proofs not rechecked, original assignment still OPEN. |
| 322,328,333 | K1–K8 and entire tree; `open-core.md`/`ours-vs-core.md:242–265`/the original map are historical inventories. Their older stops yield to explicit later result/check scopes; none is a proof that eight results suffice. |
| 323,327,342 | P8/P8b/AIII-B/AII-R/AII-T-B; `../gates/p8-check.md:28–41`: checked conditional ports, no input closed by the reading. |
| 324,326,341 | P9/P9b/AIV; `../gates/p9-check.md:25–32`: checked with θ≤1/2 and support/tail-floor repairs; full extraction/witness use matching remains OPEN. |
| 325,332,334,336,365,366 | K8/K8-CORR/P20/B109-PART/B119-PART; `l17c.md:512–544`, `../gates/l17c-gate.md:97`, `../gates/p20-gate.md:95–97`: corrected consumer route checked, ε₀-only L17/Q119 neither proved nor refuted; full step remains open. |
| 329,340 | P10/AI/A0/R2/R7; `../gates/p10-check.md:99–105`: faithful conditional port with named repairs; H-STAGE and actual representation/stability inputs survive. |
| 330,354,355,372 | B102-O/T1/P9/RESPONSE/USES/RESIDUAL; `../gates/b102-gate-a.md:18–33`, `../gates/b102-gate-b.md:47–56`, `../gates/uses-b102.md:278–300`: SU(2), subunit Hölder scope, W1/S1/S2/S3 and use-specific gaps retained. Row 337's originally proposed separate gate has no file; use 354/355, not a duplicate check. |
| 346,388 | STAGE-PART/STAGE-MATCH/CA-LAYER/TC-DILATION/TC-FAMILY; `stage-claude.md:266–284` is narrowed by `../gates/stage-gate.md:159–166`: actual response match BLOCK, restricted implications ADVANCE. |
| 350 | MU/MU-RADII/MU-USES; write-up reading still owed; `wu-mu.md:8,203,213`: write-up of checked inputs, itself unchecked; no stronger scope or new check. |
| 353 | K1–K5; `crca.md:307–308`, `cwch.md:370–374`: consumer simplifications alone supply no missing admission; later CM/CA results/checks refine those stops. |
| 356,357,363,364 | MU/MU-RADII/MU-USES/MU-RESIDUAL; `mu-uses-sol.md:75` is a qualified inventory, `../gates/mur-gate.md:4,92`, `../gates/mu-uses-check.md:124–156` record the exact checked coverage, ceiling repair and exceptions. |
| 358,360 | J1/J6; `t0-joins.md:52–62,175–252`, `../gates/j16-check.md:61–62`: J6 checked; J1 remains four OPEN premises after the checked reduction and its repairs. |
| 361,374,379 | B98-A/B/C; `b98.md:655–672`, `b98-iterate.md:54–108`, `../gates/b98-gate.md:29–49`, `../gates/b98i-gate.md:24–34,161`: checked narrow targets, iterate and k=0 repairs carried; no blanket CMP 98/99a theorem closure. |
| 367,369 | LRB/LSC/UI/OC/PDA/UM/B102-USES; `uses-lrb-lsc.md:4–8,137–147`, `uses-old.md:402–408`: reading inventories only. LSC's newly listed use coverage still awaits row 368 (no result file); the four round-2 checked consumers stay frozen. |
| 370,371 | UI-USES/OC-USES/PDA-T/PDA-USES/UM; `../gates/uses-ui-oc.md:93–95`, `../gates/uses-pda-um.md:169–182`: keep uncovered OC transport, PDA analytic/geometric limits, and new unchecked R1/N2 and D1 repair. |
| 373,380,381 | K8-CORR/P20; `wu-l17.md:296–330`: “write-up of results already checked”, with every row-380 repair logged; `../gates/wu-l17-gate.md` records REVISE, no BLOCK. No new supplier beyond those nodes. |
| 375 | Registry synchronized to these node standings/owners/backlinks. Original totals are superseded bookkeeping, not science. |
| 376,387 | K1/K2/K3/K7/J2/B99-W/STAGE-MATCH. `prior/{ca-claude,cr-claude,cv-claude,j2-claude,b99-w}.md`, plus `prior/b-in.md:71`, `prior/cm-o3.md:71`, `prior/fc.md:83`: “partly covered” retrieval records. No proof promoted; row 383's lost digest is superseded by the extant row-387 files. |
| 377 | B99-W/B99-PART; `b99-w.md:101–145,412–415`: W-b claimed from N1–N6, not checked, manuscript ends before the cited walk-construction §5. Preserve the older full-theorem gaps and distinguish true-current from independent-current families. |
| 384,385 | K8-CORR/P20; `out-l17.md:182–189`, `../gates/out-l17-check.md:11` (“faithful, conditional on its named inputs”), `FINISH.md:450`: edits applied and owner **HELD**. The outward draft/issue body confer no mathematical standing or authorization to post. |

Rows 349/351/352/359/362/368/389/390 have no result file in this pinned checkout; 348 is a header-only placeholder as recorded above. No result is inferred from a queue label. Rule 0f is this row-391 bookkeeping task; no separate proof lane or scientific check is launched.

### Change log

- 2026-11-06, row 391 at `5467e79de`: synchronized result/check standings, named inputs, scopes, written repairs and one owner per synced registry row; all changes are sourced above.
- Added theirs-cited and its six-item verification queue; retained incomplete/outstanding/cited-only/printed-only/model and missing-interface obligations as OPEN.
- Replaced stale port/repair/Q totals and J6 status. Kept the original ε₀-only L17, CM-O3, CA interfaces, unfinished B99 claim and unreviewed repairs explicit.
- Added status-history headers only to assembly-status, port-map and open-core. No proof, FINISH row, mathematical claim, audit or ledger changed. Mechanical file/count/link validation is editorial only.

Synced by Codex (gpt-6.1-sol), reading only.
- 2026-11-06, rule 0f, lead: B99-W moved OPEN to proved after `../gates/b99w-gate.md` (row 393); tally 57 proved, 89 OPEN.

- 2026-11-06, rule 0f, lead: K2 = CR records the written cr-claude proof; standing stays OPEN until its check (row 396).
- 2026-11-06, rule 0f, lead: CA-BIN records the written b-in proof; standing stays OPEN until its check (row 397).
- 2026-11-06, rule 0f, lead: K2 = CR updated after cr-gate (row 396); stays OPEN.
- 2026-11-06, rule 0f, lead: CA-BIN updated after b-in-gate (row 397); stays OPEN.
- 2026-11-06, rule 0f, lead: OC annotated after bundle-value (row 400); standing unchanged.
- 2026-11-06, rule 0f, lead: K2 = CR updated after cr-r2-gate (row 398); stays OPEN.
- 2026-11-06, rule 0f, lead: STAGE-MATCH updated after fc-gate (row 392); stays OPEN.
- 2026-11-06, rule 0f, lead: CA-BIN records the written b-in-r2 proof (row 399); standing stays OPEN until its check.
- 2026-11-06, rule 0f, lead: CA-BIN updated after b-in-r2-gate (row 399); stays OPEN.
- 2026-11-07, rule 0f, lead: K2 = CR records the unchecked cr-prem round (row 408); stays OPEN.
- 2026-11-07, lead: CH and CH4-AUX owner moved to `ch-r1` (rows 411-412); standing unchanged.
- 2026-11-07, rule 0f, lead: K5 = CH records ch-r1 (row 412): CH4-AUX stays the first open input after three failed attacks; standing OPEN.
- 2026-11-07, rule 0f, lead: K7 = CV records cv-claude round 3 (row 413, unchecked): Theorem A and the reduction to (CH-a) and (PT); standing OPEN until row 414.
- 2026-11-07, rule 0f, lead: K7 = CV updated after cv-gate (row 414): Theorem A holds for the whole-lattice small-field step only; reduction and Proposition C not established; standing OPEN.
- 2026-11-07, rule 0f, lead: new registry row LAYER-THM (rows 416-417): the general layer theorem the account assumes but does not state; consumed by K7, STAGE-MATCH and K5; OPEN, owner `layer-thm`.
- 2026-11-07, rule 0f, lead: LAYER-THM records layer-thm (row 417, unchecked): partial proof; U15 covered conditional on CA-LAYER/(N1); first unproved input (G); standing OPEN.
- 2026-11-07, rule 0f, lead: STAGE-MATCH records fc-r2 (row 404, unchecked): frame-change BLOCK answered as implications; open lemma CX; standing OPEN until row 421.
- 2026-11-07, lead: BP07 / PRINT-INVERSE owner set to `print-inverse` (rows 423-424); chosen as the next outward contribution target; standing OPEN.
- 2026-11-07, rule 0f, lead: STAGE-MATCH updated after fc-r2-gate (row 421): frame-change BLOCK stands; standing OPEN.
- 2026-11-07, rule 0f, lead: LAYER-THM updated after layer-thm-gate (row 418): (b) reduces to CA-LAYER/(N1); (G) follows from (3); (3) rests on PRINT-INVERSE (row 424) and analytic CMP 98 Prop. 5; standing OPEN.
- 2026-11-07, rule 0f, lead: BP07 / PRINT-INVERSE records Theorem PI (row 424, unchecked): proved under (S1-loc), (S2); thin-tower counterexample to the remark as printed (Prop. 3.2); standing OPEN until row 427.
- 2026-11-07, rule 0f, lead: BP07 / PRINT-INVERSE updated after pi-gate (row 427): Theorem PI not correct as stated; repaired implication advances; Balaban Theorem 3.3 claim removed; standing OPEN; repair round row 428.
- 2026-11-07, rule 0f, lead: K2 = CR records cr-prem-gate (row 410): premise positives ADVANCE; stopping lemma REVISE; first open premise (S') on general outside reads; native-representation branch impossible (Prop. N, unchecked); standing OPEN.
- 2026-11-07, rule 0f, lead: BP07 / PRINT-INVERSE records round 2 (row 428, unchecked): Theorem PI for the literal CMP 99b rows under (S1-loc), (S2), (S2+); remark's hypothesis refuted on the account's tower class (Props. 3.2, 3.3); standing OPEN until row 430.
- 2026-11-07, rule 0f, lead: BC1 / B98-P5 records round 2 (row 429, unchecked): (D) false on the account's class at levels j >= 1 (Prop. 1), proved on the (PL) subclass and on thick towers; standing OPEN until row 431.
- 2026-11-07, rule 0f, lead: BP07 / PRINT-INVERSE after pi-r2-gate (row 430): Theorem PI checked by Codex, REVISE then ADVANCE at its local scope (S1-loc), (S2), (S2+); written repairs queued (row 432); the full S1-S2 remark and BP07's other inputs (G_0 pointwise bounds, G_1, C1 covariance) stay open; standing OPEN.
- 2026-11-07, rule 0f, lead: BC1 / B98-P5 after b98p5-r2-gate (row 431): carrier bridge proved on S^pl and (TH); (D) false for the fixed-side-12 cube-only class; census incomplete (CA-II uses, minimiser tube, lowest levels); round 3 queued (row 433); standing OPEN.
- 2026-11-07, rule 0f, lead: LAYER-THM chosen as our own end-to-end piece (owner: 'Both, layer first'); CA-LAYER/(N1) owner moved from `stage-claude` to `layer-thm`; package round queued (row 441); standing OPEN.
- 2026-11-07, rule 0f, lead: BP07 / PRINT-INVERSE contribution posted as their issue #13 (out-pi.md at 94df5579a); standing OPEN (local scope only; G_1, G_0 pointwise bounds and C1 remain).
- 2026-11-07, rule 0f, lead: LAYER-THM records layer-pkg (row 441, unchecked): conditional theorem proved; open GW (= PRINT-WALKS at graph level, owner moved to `layer-thm`, row 444), admission certificates, FM/FD, clause (e), RC; standing OPEN.
- 2026-11-07, rule 0f, lead: BC1 / B98-P5 records round 3 (row 433, unchecked): census decided at every explicit use (CA-II 5.8 lemma and CA-III minimiser tube covered; I 52248-52300 not a use); rests on round 1's port (check row 446); standing OPEN.
- 2026-11-07, rule 0f, lead: PRINT-WALKS / LAYER-THM record walks-gw (row 444, unchecked): GW proved on the PI class with common constants; check row 447; remaining layer obligations in round row 448; standing OPEN.
- 2026-11-07, rule 0f, lead: LAYER-THM records layer-r3 (row 448, unchecked): admission A missing at nearly every use; switched-current defect (M3) claimed (check row 449); uniform admission round row 450. BC1 / B98-P5 records b98p5-r3-gate (row 445): REVISE; full consumer coverage not established. Standings OPEN.
- 2026-11-07, rule 0f, lead: LAYER-THM records adm-pl (row 450, unchecked): uniform conditional admission theorem UA; relaxed K109 lacks the plaquette clause; hereditary replacement S1' proved; distil queued (row 451); standing OPEN.
- 2026-11-07, rule 0f, lead: LAYER-THM distilled to library/layer-thm-part.md (row 451): one conditional theorem, 16 named Outstanding premises; referee row 452 (folds the (M3) check, row 449); standing OPEN.
- 2026-11-07, rule 0f, lead: PRINT-WALKS check (row 447) moved from Mini worker 1 to a laptop Claude subagent (owner OK); layer-part-ref (row 452) now follows b98p5-port-check on the Mini; standing OPEN.
- 2026-11-07, rule 0f, lead: B98-P5 records b98p5-port-check (row 446): round-1 local port sections 2.1-2.5 pass as an implication from (11), first failing step none, two repairs (R1 covariance, R2 constant) applied by row 453; (11) on the account class and the r3-gate coverage items stay open; standing OPEN.
- 2026-11-07, rule 0f, lead: B98-P5 port repairs applied (row 453, 212387d8c); standing OPEN.
- 2026-11-07, rule 0f, lead: PRINT-WALKS records walks-gw-check (row 447): REVISE, no BLOCK; two repairs ((P15) cube count, complex-background Wilson vertex) and one wording fix, applied by row 454; standing OPEN.
- 2026-11-07, rule 0f, lead: PRINT-WALKS repairs applied (row 454, b133dfe5f); outward note queued (row 455); standing OPEN.
- 2026-11-07, rule 0f, lead: PRINT-WALKS outward note drafted (row 455) and checked (row 456: FIX, no false step; nine fixes, row 457); rule 0g clean; standing OPEN.
- 2026-11-07, rule 0f, lead: PRINT-WALKS outward note fixed and linked (rows 457, 9a3ad2072); awaiting owner OK; standing OPEN.
- 2026-11-07, rule 0f, lead: PRINT-WALKS outward note posted as issue #14 on owner OK (rule 0h); standing OPEN in our tree (PI class only).
- 2026-11-07, rule 0f, lead: process catch-up (owner): layer-part-ref (row 452), out-lrb-check (439), out-lsc-check (442) moved from Mini worker 1 to laptop Claude subagents; out-pda-check (436, errata class) stays on the Mini; research/ym4d snapshot PR #10141 opened off main (16 frozen parts, posted notes #10-#14); standings unchanged.
- 2026-11-07, rule 0f, lead: LSC outward note checked (row 442: FIX, no false step, defect real as stated); fixes row 458; standing unchanged.
- 2026-11-07, rule 0f, lead: LRB outward note checked (row 439: FIX, no false step, gap as stated, issue text to narrow); fixes row 459; standing unchanged.
- 2026-11-07, rule 0f, lead: LAYER-THM refereed (row 452): FREEZE WITH REPAIRS R1-R11, no BLOCK; (M3) holds as a gap in the account's assumed package; S1' and relaxed-K109 readings hold; repairs and freeze by row 460.
- 2026-11-07, rule 0f, lead: LAYER-THM part library/layer-thm-part.md FROZEN as a conditional theorem (row 460, f5dd57a77); premises PI, GW, AV, R, A0, L0, S, T, P2, ID/EQ/PH/LC, M (M3), RJ, FD, FM, E(e), RC stay OPEN; CA-LAYER standing: conditional on those premises.
- 2026-11-07, rule 0f, lead: LRB outward note posted as issue #15 and LSC outward note as issue #16, on owner OK (rule 0h); standings in our tree unchanged.
- 2026-11-07, rule 0f, lead: errata-check (row 409) and out-pda-check (row 436) moved from Mini worker 1 to laptop Claude subagents (owner OK); errata 1 = the checked A/B entries plus PDA if it is errata-class; later errata findings collect for errata 2.
- 2026-11-07, rule 0f, lead: PDA outward note checked (row 436: FIX, no false step; endpoint defect class A); it is a proof post for a printed-without-proof proposition, so it posts on its own, not in the errata; fixes row 461.
- 2026-11-07, rule 0f, lead: errata 1 checked (row 409): 35 entries (15 A, 20 B); 9 class C held out of the errata; 4 uncertain held for errata 2; awaiting owner OK.
- 2026-11-08, rule 0f, lead: PDA outward note posted as issue #17 on owner OK; engagement check before posting (owner rule 2026-11-08) found no activity on #10-#16.
- 2026-11-08, rule 0f, lead: errata 1 posted as issue #18 (34 entries: 15 A, 19 B), after Claude check and gpt-6.1-sol second reading; 5 held for errata 2; 9 class C held out.
- 2026-11-08, rule 0f, lead: GW1 registered (owner gw1): current-corrected walk bounds completing (K10) on the PI class; prior digest row 463 first.
- 2026-11-08, rule 0f, lead: GW1 narrowed by its prior digest (row 463) to the (J7) port for G_1^J, q_{1,J}, H_1^J on the PI class; proof lane row 464 launched.
- 2026-11-08, rule 0f, lead: GW1 proof claimed (row 464, library/gw1.md, unchecked); Claude check row 465.
- 2026-11-08, rule 0f, lead: GW1 checked (row 465): REVISE, wording only, no failing step; repairs and outward note queued (rows 466-467).
- 2026-11-08, rule 0f, lead: GW1 outward note posted as issue #19 on owner OK.
- 2026-11-08, rule 0f, lead: LAYER-M registered (owner m3) for premise M / (M3) of the frozen layer theorem; prior digest row 470 and proof lane row 471 queued.
- 2026-11-08, rule 0f, lead: critical-path triage done (row 472, library/cp-triage.md). LAYER-M construction claimed (row 471, library/m3.md, unchecked); Claude check row 473.
- 2026-11-08, rule 0f, lead: LAYER-M (premise M of the frozen layer theorem) proved conditionally and checked (row 473: ADVANCE, wording only); repairs and outward note queued (rows 474-475).
- 2026-11-08, rule 0f, lead: M3 outward note posted as issue #20 on owner OK; LAYER-M stays conditional on PI-ADMIT. TPI (FREE join) claimed in library/tpi.md (row 479), Claude check row 481. PI-ADMIT digest launched (row 480).
- 2026-11-08, rule 0f, lead: TPI (coarse covariance bound at YM4_1400 102280) posted as issue #21 on owner OK. PI-ADMIT, GEOH-O6, GEOH-O2, H-C-MARK each stop at one named supplier (C0-SUP, LIFT-ONE, UO2, HCM-R). Mini Codex widened to four slots on owner note "you have full mini codex".
- 2026-11-08, rule 0f, lead: live-strip invariant (geoh-live-ab.md) checked ADVANCE: proves clauses (a)-(e), (h), part of (g) of the account's "Proof outstanding" live-region package CA-I 85598-85644 on its stated rules. Outward note row 521.
- 2026-11-08, rule 0f, lead: SC-NATIVE (leaf-sc.md) checked ADVANCE: A4.1 for the PI/GW/GW1 consumers reduces to PI-ADMIT/C0-SUP. FCO-slot (fco-slot.md) checked, proof holds: GEOH-O2 code count and reserve bound stand. Live-region block: proved under the outlines' no-joining rule (live-nj.md, check row 554), counterexample on the account's class (live-fgi.md, recheck row 555).
