# T0 dependency tree

Provenance: Codex; assembly lane T0MAP; checkout 6d9df38c26ddcd12f61d3763fd6dbe6d9374152e; research dependency map, not an audit and grants no status. Sources borrowed from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, are credited below.

## 1. Contract, standing, and how to read the tree

This maps the files at the pinned checkout. It proves and checks no mathematics.
**T0 remains open.** A frozen implication is not an established actual-construction input.

The contract is `GOAL.md:20–37`; the porting rule is `GOAL.md:39–48`.
The target here is the Wilson SU(2) scalar curvature sector, with componentwise OS properties and Wightman reconstruction. NT1 and the current NT2 proposal remain required. The Euclidean test domain is separated tests and diagonal-flat Schwartz functions. A full coincident-point Euclidean extension or a complete gauge-observable theory is not supplied by these texts (`wr1.md:403–429`; `port-map.md:13`; SA:74–82, 4416–4425, 4595–4598). Do not silently strengthen this sector contract to either claim.

The outline and complete account have different Theorem 0 statements. Here **A0–AV** mean the complete account's clauses, CA-I `3.1:thm-main`, lines 2512–3016. The outline's main page is SA:66–130. In particular CA does not assert clustering, unique vacuum, Wightman functions, the forward cone, or O(4) in (ii): CA-I:2705–2711. Its (iv) does not assert non-Gaussianity: CA-I:2815. Half B is essential.

Standing used throughout:

- **proved**: a written repository implication; say separately whether refereed. All named hypotheses survive.
- **ported-checked**: one checked port, at its exact stated scope and repairs.
- **ported-unchecked**: a port awaiting its other-model reading.
- **OPEN**: no supplier at the required scope. This includes cited or printed analytic inputs not rebuilt here, missing interface identifications, and unported CA deductions. Their source may nevertheless contain a proof.

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
│  │  ├─ unchecked repairs: UM, OL-transfer
│  │  └─ K1–K8, R1–R7, BP/BC leaves below (not just eight core lemmas)
│  ├─ AIII: P6 B2/B3/B4 + PI + P8 B5/B7 + LSC
│  │  └─ A0/AI + K4/K5 + R8 + retained BP/BC inputs
│  ├─ AII-R: P8b B10–B13, from A0 + AIII-b + finite lattice RP
│  └─ CL1 Theorem 9, using LG1 + SR1 + compatible first passage (I1)
│     └─ J1 (construction/constant dictionary) + J2 (full rooted UV1)
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
│     └─ LG1 + SR1 all-state bounds/growth + CL1 realization + J6
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
| A0: CA (0), flow and windows | P5 `4.19:prop-clause-zero`, A12, and `prop-containment`/`cor-windows`, A13 (`port/p5-induction.md:417–497,564–672,828–855`); P1 `4.2:lem-first-passage`, `4.19:lem-flow-bounds` (`port/p1-base.md:55–150,766–768,811–821`); P10 A15 (`port/p10-stability.md:280–443,1640–1642`). | P1/P5 **ported-checked**; P10 **ported-unchecked**. Needs the actual joint induction, not arithmetic alone. P5's old (b) and (h) statuses are updated by UM/OL and checked P7 below. |
| AI: CA (i-a), representation | P10 A17 `4.20:thm-representation` (`port/p10-stability.md:444–794,1643–1648`). | **ported-unchecked**. A10 `4.18:thm-preparatory-boundary` (`:43–160,1636–1639`) retains H-STAGE. Needs K/R/B leaves; representation is not a closed input. |
| AI: CA (i-b),(i-c), stability and mass | P10 A19 `4.33:thm-stability` (`port/p10-stability.md:1010–1261,1649–1652`). | **ported-unchecked** with all eleven (h1)–(h11), not only the eight in the older CHAIN summary. Normalized floor; real positivity and reference normalizers still required. |
| AI: CA (i-d), exact insertion and sourced identity | P10 A20 `4.34:lem-sourced-exactness` (`port/p10-stability.md:1362–1438,1591–1628,1653–1655`). | **ported-unchecked**, conditional on actual transformation identities and the complex correlation induction. Exactness is not a theorem about the continuum block laws. |
| AIII-a,c,d: fixed-torus bounds, running shift, cumulative one-loop law | P6 B3 `5.1:thm-correlation-theorem`; B4 `5.3:lem-driven-flow`, `5.14:thm-one-loop-law` (`port/p6-correlation.md:460–728,2647–2670,4630–4662`). | **ported-unchecked**; reads A0/AI, B2's two weight lemmas, PI, K4/K5 and R8. Running law uses the actual Gaussian finite part plus the unmarked/remnant bounds, not free-field algebra alone. |
| AIII-b: per-ball bound | P8 B7 `6.4:thm-per-ball-bound` (`port/p8-positivity.md:148–208,560–707,854–866`) + LSC B6 (`lsc.md:688–700,720–724`). | P8 **ported-unchecked**, LSC **proved/refereed**. Retains H-LOC/H-DOM, shared normalized upper/floor, zero-source energy identification, and CMP 116 (1.26). No n=1, factorial bound, decay at large separation, or arbitrary-state result follows from the statement alone. |
| AII-T-b: first-passage torus limits | P8 B8 `5.12:prop-subsequential-limits`, `5.12:lem-limit-positivity` (`port/p8-positivity.md:709–852,856,862`). | **ported-unchecked** on H-FIRST-PASSAGE, torus floor/bound, distributional H-KERNEL, and finite RP. Its extra tuned-family identification needs AV-c(2) (CA-I:2688–2689). |
| AII-R: growing tori/R4 | P8b B10 transport/symmetries/half-space/modulus/linearity; B11 `7.4:thm-infinite-volume`; B12 limit distributions/invariance/positivity; B13 `7.7:prf-reconstructed-space` (`port/p8b-limits.md:19–67,258–328,329–674,1288–1298`). | **ported-unchecked**. Gives curvature Hilbert space, H≥0 and W3. H-BLOCK (`:57`) is an extra block-state assertion, not a consequence of curvature bounds and not needed for the scalar-only route. Full OS, components and Wightman theory require B. |
| AIV: finite witness, transfer, continuum consequences | P9 C9 `8.18:thm-torus-witness`, C10 `8.22:thm-volume-transfer`, C11 `8.1:thm-two-point-witness` and reference-volume assembly (`port/p9-witness.md:288–325,1109–1141`); C5 now in P9b `8.2:prop-gaussian-extraction` (`port/p9b-extraction.md:177–229,739–749`). | Both **ported-unchecked**. Needs R9/R10, actual A0/AI/AIII, and Balaban inputs. P9's old “C5 not ported” is superseded only at P9b's conditional scope. H-GXa/H-GXb are explicitly still open. CA (iv)'s torus-limit conclusion is weaker than NT2 and than a componentwise lower bound. |
| AV-a–e; AII-T-a | `chain-ca.md:112–127`: D8 `9.8:thm-uniqueness-theorem`, D11–D12 coordinate/comparison deductions; B9 `7.3:thm-tuned-family` (`chain-ca.md:88`). CA-I:2828–2983,2668–2682. | **OPEN as repository assembly**: no corresponding port among the supplied P-files. CA has conditional deductions, with R11 and cited inputs still open. Neither P7 torus independence nor PH1 phase decomposition proves this clause. |
| AV-f | D13 `9.8:thm-two-blockings` and its reconciliation (`chain-ca.md:128`), CA-I:2984–3016. | **OPEN**, R12; requires AV core, AIII and AIV. Do not feed it back into AV-a–e. It is not needed for subsequential T0. |

### A's reusable suppliers and repairs

| ID | File and label | Current standing; retained premises |
|---|---|---|
| P1 | `port/p1-base.md:762–789,811–821`: invariance; flow arithmetic; `4.6:lem-polymer-gas`, tree/cluster lemmas, `prop-logarithm-convergence`. | **ported-checked**. Actual activity bound and printed locality remain inputs (`:819`). |
| P3 | `port/p3-free.md:576–596`: `8.1:lem-gaussian-squares`, `lem-free-curvature-covariance`, `lem-kernel-positivity`, `lem-background-tower`, `lem-kernel-bounds`. | **ported-checked**, repaired domain C1. H-BG, H-TOWER, H1-MIN, H2-FLUX, H3-CONT remain (`:586`). Not the unwritten interacting continuum-kernel supplier. |
| P4 | `port/p4-operator.md:192–215,354–374,557–597,891–915`: A4 `4.5:thm-operator-bounds`, A3 `4.4:cor-localised-independence`, A9 `4.14:thm-operator-theorem`. | **ported-checked**, with recorded repairs. MU/LRB/UI/PDA supply specified clauses; P4-H-assembly and P4-H-core remain named missing suppliers (`:913`). |
| P5 | `port/p5-induction.md:17–416,828–855`: A5 `4.6:prop-large-field-bound`, A6 `4.7:prop-beta-extraction`/`prop-coupling-increment`, A12/A13. | **ported-checked**. Membership, activity, positive history law, rooted moment convention and prefix representation remain. |
| P7 | `port/p7-torus.md:257–304,1268–1283,1331–1340`: A14 `4.38:thm-torus-independence`. | **ported-checked**. Seven theorem hypotheses, level hypothesis, joined-domain extension and family propagation survive. It is not the AV uniqueness theorem. |
| PI | `port-pi.md:15–34,542–551`: `5.2:lem-pointed-irrelevance`. | **ported-unchecked** on admitted E-families and the one-layer box hypothesis. Does not supply cp12's full H-ct or CI's OSF-loc/(13). |
| MU | `mu.md:245–280`: `4.13:lem-minimizer-unique`, both tower rules and arbitrary-subdomain nesting. | **proved/refereed** in the regular class and its stated analytic continuation. CMP 102b minimal orbit and CMP 98 averaging remain inputs; other consumer radii are not checked (`:274–278`). |
| LRB | `lrb.md:833–862`: `4.4:prop-local-real-base`, clauses (1)–(4). | **proved/refereed** under (a)–(d), W′, cell-resolvent/coercivity, symmetry and CMP 116 (2.14). Does not construct those primitive walks. |
| OC | `oc.md:243–265`: `4.13:lem-own-constant`. | **proved/refereed** for widened smaller-cube gauges, own constants and one-step reproduction, under (3)–(7) and the cited background/gauge results. Not blanket complex admission. |
| UI | `ui.md:549–572`: `4.5:lem-uniform-increment`. | **proved/checked** completion of the source continuation; retains (189)–(190)/C_H, gauge-map scale count and hierarchy-distance input. This UI is not RO1's small-ball insertion lemma. |
| PDA | `pda.md:231–247`: geometric (A1) of `4.14:prop-prepared-data-admissible`. | **proved/refereed**, one operation and stopped prefixes given old (A1), with rule (C). (A2), other nests/T-steps, analytic gauge supply and separately cited geometry remain. |
| LSC | `lsc.md:688–700,702–724`: `6.3:lem-last-scale-constants`. | **proved/refereed**, round 2. Keep e^{-E_vac} on both sides before cancellation. Frozen smaller-scope round 1 is superseded by the round-2 normalized result, not by a bare floor. |
| UM | `um.md:89–205,563–584`: `4.2:lem-unmarked`, including its missing uniform-domain step. | **proved, unrefereed** implication under its four hypotheses and Balaban analytic/remainder inputs. Updates older “unmarked open” entries, but does not prove its small-field-step premise. |
| OL | `ol.md:2669–2768,2813–2845`: OL-transfer for Gaussian consumers of `4.2:lem-one-loop`. | **proved, unrefereed** replacement. Retains §11's flat/model inputs, actual coefficient/pivot estimates, physical Gaussian and response identification, and §§2–3 bulk calculation. Original OL-W0-CA stays open; Gaussian-only replacement does not establish arbitrary-history/non-Gaussian machinery. |

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
| B21 O4-2: A | Qualitative (iii-b), n=2 (`o4-two-point.md:69`). | P8 B7 + frozen LSC, **ported-unchecked / proved conditional** respectively (`port/p8-positivity.md:560–707`; `lsc.md:720–724`). |
| B22 O4-2: B | (iv)'s nonnegative vanishing upper bound and s(d)→∞ (`o4-two-point.md:70`). | AIV, P9 C9–C11 plus P9b, **ported-unchecked**, with R9/R10 and inherited leaves. Pass volume first at fixed cutoff, then K→∞ for fixed d, then d→0 (`o4-two-point.md:198`). |
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
| K1 = CM | **OPEN** prescribed-word continuation with the original Stage-5 rate, coefficients, complete reads and companion identification (`open-core.md:49–67`; current `mf.md:1528–1572`). | `2.4:prop-m-freeness` and correlation companion machinery; the parameter order underlying A0/AI/AIII and hence all T0 branches. A replacement root kernel with weaker rate is not its supplier. |
| K2 = CR | **OPEN** actual outside-consumer minimizer existence and both curvature/current estimates (`open-core.md:69–97`; `rb.md:796–802`; CA-I:45085–45100). | Outside re-blocking, actual stage/domain admission, then representation/correlation. RB's inside implication is not outside admission. MU proves nesting on admitted data, not this admission. |
| K3 = CA | **OPEN** completion-collar membership at fixed birth domains, whole-cube gauges and all intermediate complex layers (`open-core.md:99–136`; `arr.md:955–978`). | The raw collar rider in arrest/completion and later analytic composition. Does not by itself close every arrest hypothesis. |
| K4 = CW | **OPEN** analytic window admission and both normalized screened inherited-data bounds (`open-core.md:138–172`; `wd.md:365–384`). | Preparatory-window input of P6 B3, two weight machines, AIII and every continuum bound. Real outside estimates alone do not give complex paired-window screening. |
| K5 = CH | **OPEN** actual three reached CMP 122b links on the full independent-switch polydisc (`open-core.md:174–193`; `ph.md:468–474`). | `5.6:prop-polydisc-holomorphy`, hence P6 B2/B3. A term bounded on its own domain does not prove that the links land there. |
| K6 = CO | **OPEN original statement** OL-W0-CA, prescribed actual precision words (`open-core.md:195–225`). **Bypass proved but unrefereed** for the Gaussian coefficient consumers: OL-transfer (`ol.md:2744–2768,2817–2845`). | Literal original-family use, if retained; not a compulsory new proof on the proposed Gaussian-only route after OL-transfer is checked and its inputs supplied. It supplies neither CM's original-word rate nor arbitrary-history/non-Gaussian continuation. Do not record the original CO as proved. |
| K7 = CV | **OPEN** reality of the actual prescribed scalar sum at independent real current, with its masks/subtractions/branches (`open-core.md:227–238`; `pd.md:1442–1470`). | The missing reflection/reality step below `4.32:prop-positivity-dichotomy`, P10 stability and P9's positive history law. CV gives positivity of its own scalar exponential, not all of A18 (`open-core.md:553–560`). |
| K8 = L17 | **OPEN** complex curvature-controlled admission for both actual tower rules, with early B3 and independent input radii (`b109.md:3186–3248,3670–3687`). | CMP 109 (1.17), hereditary small-field admission, P5 class reproduction and the Balaban family step. The weaker quadratic-radius estimate is not L17. P18/LQ is proved only with its premises and remains unchecked (`b109.md:3714–3730`). |

These are seven literal endpoint obligations plus L17, not a proof that eight results suffice for T0. The current shortest Gaussian route attempts to bypass K6 only. `open-core.md:7–16,545–560` expressly proves no minimality or independence theorem. Its old CO endpoint is superseded **at the Gaussian consumers**, not everywhere.

The LOC/L16 obstruction remains a route constraint, not a ninth desired positive lemma: `open-core.md:404–430,541,558`. Do not demand both the universal path and its conditional counterexample. None of the map's K2/K3/K4 requirements assumes that path exists.

### 5.2 Residual Half-A contracts, beyond the core

All R rows are **OPEN at their actual use scope**. Conditional ports named inside them are available at the standings in §3. A source list's attribution is not a new proof that every item enters every clause; exact use-site identifications remain part of the indicated row.

| Leaf bundle | Missing contract, with all named subitems retained | Blocks |
|---|---|---|
| R1 small-field family step | CMP 109 Theorem 3 plus CMP 116 refinement: S1–S12, beyond K8. Actual background/primitive operators; exact Haar/Jacobian/Gaussian integral; symmetry; admitted far/near response; cubic/quartic Ward reduction; own response/marginal comparison; potential localization; activity budgets and final family closure (`b109.md:158–228,3728–3730`). P1–P21 are pieces, not the full theorem. | A0/AI, UM's premise and all sourced descendants. |
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
| BP13 | **OPEN** layerwise gauge clauses, 122a (1.64)–(1.69). | J; `chain-ca.md:314`; R2/R6. |
| BP14 | **OPEN** layerwise ceiling as a uniform small-coupling condition, 122a p.192. | J; `chain-ca.md:315`. |
| BP15 | **OPEN** old-term bounds beside a new region, 122b p.375. | J/S and constant order; `chain-ca.md:316`. |
| BP16 | **OPEN** joined-domain convergence/analytic extension, 122a (1.70), 122b (1.68)–(1.69). P7/P10 retain it. | J/W/U; `chain-ca.md:317`; `port/p5-induction.md:486`. |
| BP17 | **OPEN** absolute boundary bound and gauge invariance, 122b (1.11),(1.23)–(1.48). | J; `chain-ca.md:318`. |
| BP18 | **OPEN** analytic solution of the large-field equation, 122b (1.40)–(1.41). | J; `chain-ca.md:319`. |
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
| J1 actual construction and constants | **OPEN interface identification.** Supply the one Wilson trajectory, observable normalization, cofinal boards/tori, coupling/source ceilings and compatible order consumed by B03/B06/B19 and the other inherited IN-order passages. CA A0/P7/P10 and frozen IN1 are candidate implications, not an already proved equality of all their hypotheses (`cl1.md:59,78–95`; `in1.md:677–681`; `port-map.md:29–42,53–62`). In particular, do not silently mix an outline independent-current/relative-gauge construction with a different CA datum. | Nonemptiness and simultaneous applicability of the full frozen B chain. The restricted O4-2 route uses CA data directly and avoids original IN1. |
| J2 rooted ordinary source package | **OPEN** SR1 (4)–(6)/RO1 H-U in their exact ordinary repeated-source, mirror-list and actual rooted-geometry scope (`sr1.md:38–65`; `ro1.md:54–62`). Candidate ingredients are P6's sourced format, P8 H-LOC/H-DOM/H-TREE, LSC's normalized constants and P10 exactness/stability. The aggregate raw-source estimate, rooted counting/multiplicity margin and all-state transfer have to be connected in writing at these domains. | All-state n=1 comparison, graded factorial moments, full insertion density, all-order O(4), component construction and WR1. AIII-b alone does not supply it. |
| J3 all-state/component upper witness | **OPEN** TU10 uniformly over PH1's realizing states and full shape class (`ro1.md:68–80`). AIV provides torus and torus-limit states only. Either prove the extension from the CA source/normalizer package, or supply frozen TP1's entire FLOW/FREE/PRES/REG/AMP/AG/STATE/LIMIT package (`tp1.md:50–184,191–207,638–645`). Merely porting P9 does neither. | RO1 endpoint elimination on every component and therefore componentwise WR1 covariance. O4-2 already supplies the restricted connected two-point conclusion. |
| J4 component lower witness / NT1 | **OPEN actual input**, followed by a **proved/refereed** implication: a strictly positive reflected connected two-point value on the chosen component plus PH1's unique vacuum gives NT1 by TP1 Lemma 7.2 (`tp1.md:550–566`; `ph1.md:80`). TP1's full package is one conditional supplier of that lower value. AIV's positive mixture covariance alone is not a component covariance: conditional means can contribute. A chosen nontrivial component must be identified; if all components are claimed nontrivial, the lower bound must be uniform over their realizations. | NT1 in the reconstructed theory. Dimension ≥2 before phase decomposition is not enough. No mass gap is requested or inferred. |
| J5 NT2 | **OPEN** the adopted proposal on one joint blocked state, at all L-adic ultraviolet scales, with the same admissible blocking map, prescribed coefficients, observable coupling, NT2-V, NT2-M and NT2-R (`GOAL.md:31–33`; `parts/witness.md:863–1018`). Its eight supplier hypotheses are expanded below. | Interaction/non-triviality in GOAL's sense. CA (iv) and its bounded-relative-error scalar two-point law do not supply this. CA (iii-d) is a construction-coupling law, not automatically the observable-coupling law. |
| J6 final test-domain and same-theory assembly | **OPEN written assembly**, not a new interacting estimate. PH1 states clustering with an inverse-square rate on compact separated tuples (`ph1.md:74–79,581–587`). The full positive-time diagonal-flat qualitative cluster statement on SA:118–129 still needs its explicit supplier/density passage in the final T0 assembly. Candidate premises: compact clustering, spatial translation unitaries and the isometric density/completion (`cl1.md:463`; `ph1.md:567`). The norm estimate must be uniform in the separating translation; plain Schwartz continuity alone is insufficient. Also identify all imported bounds, reconstruction and the selected nontriviality witnesses on the same hierarchy (`wr1.md:17,65,403–429`). | Literal full-OS T0 assembly. No quantitative inverse-square rate is asserted for arbitrary completed vectors, and WR1 does not claim a Wightman cluster theorem (`wr1.md:446`). |

J6 is a visible assembly obligation, not a claim that the frozen PH1 or WR1 implication is wrong. No new proof is supplied by this map. The qualitative Hilbert-space approximation is a short candidate route; it should not be replaced by an unproved uniform Schwartz-translation bound.

**TP1's alternative witness route: current suppliers of all eight imports.** These are subcontracts of J3/J4, not eight additional independent leaves. TP1 is frozen/refereed (`tp1.md:621–634,654`); its older AG-draft status is updated by AG1's current conditional theorem, not by assuming AG's premises.

| TP1 import | Supplier NOW and retained gap |
|---|---|
| FLOW (`tp1.md:54–69`) | A0/AI, UM, OL-transfer and P6 B4 are candidates at their recorded standings (`port/p6-correlation.md:460–728`; `um.md:563–584`; `ol.md:2744–2768`). **OPEN exact match** to telescoping, constant-source derivatives, fixed auxiliary choices and common datum; J1 applies. |
| FREE (`tp1.md:71–87`) | P3's Gaussian squares, covariance and background tower are **ported-checked conditional** (`port/p3-free.md:576–596`). **OPEN** full TP1 residual covariance bound and volume-uniform continuum comparison at (2.3)–(2.4); slice bounds alone do not supply the terminal bound. |
| PRES (`tp1.md:103–113`) | P10 A20 is **ported-unchecked conditional** (`port/p10-stability.md:1362–1438,1591–1628`). **OPEN** identification with this four-part formed exponent, positive history law and differentiable expectation, using the same law as AG. |
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
| H-FLOW (`:1018`) | The specified corrected-coordinate error law, plus identification of the hard-core coupling with the observable coupling (`:965–973`). OL-transfer and P6 B4 are **proved-unrefereed / ported-unchecked** candidate coefficient/running suppliers; the stronger stated flow and scheme match are **OPEN**. |

NT2's map admissibility is part of the contract: free blocked flux variances must remain bounded and converge; simple straight decimation fails that test (`parts/witness.md:880–890`). Matching is o(g_m^2), o(g_m^{2k}), o(g_m^4) on every fixed finite template family (`:975–987`); the running test is the leading logarithm, not a per-step derivative (`:989–1000`). A result on a mixture must not be silently asserted on each component. No continuous-r interpolation follows from the L-adic proposal (`:870–878`). These qualifications remain attached to J5; they are not new physical axioms.

## 6. Checks still owed

These are readings of written arguments, distinct from proving OPEN leaves. Checks of a conditional proof do not establish its premises. Do not repeat the completed checks solely because this map cites them.

| Check unit | Text and scope requiring the other-model reading |
|---|---|
| Q1 | P6, both weight lemmas, correlation assembly, driven flow and one-loop law (`port/p6-correlation.md:4630–4662`). Retain C-sixth, domain and uniformity limitations. |
| Q2 | P8, B5/B7/B8 including vacuum-normalized LSC use and source-domain distinctions (`port/p8-positivity.md:854–866`). |
| Q3 | P8b, B10–B13 and its restricted curvature reconstruction (`port/p8b-limits.md:1288–1298`). |
| Q4 | P9, C9/C10/C11 and reference transfer, with H-depth/H-source-use/H-GXa/H-GXb and endpoint qualification (`port/p9-witness.md:1109–1141`). |
| Q5 | P9b, C5's conditional covariance proof and the limits of its P9 supply (`port/p9b-extraction.md:654–749`). Checking it is not closing H-jet/H-tail-sum. |
| Q6 | P10, A10/A15/A17/A19/A20 and normalization/exactness corrections (`port/p10-stability.md:1630–1686`). |
| Q7 | PI, pointed irrelevance on its admitted E-family domain (`port-pi.md:542–551`). |
| Q8 | UM, uniform-domain/current/Cauchy/second-moment extraction implication (`um.md:563–584`). |
| Q9 | OL's complete current Gaussian replacement, including §§2–3, actual §11 input use and §§16–19 transfer; not merely its newest Result (`ol.md:2744–2768,2813–2845`). Retain the original-family exception. |
| Q10 | B109's used P1–P21 implications, especially the new P15–P18/LQ and the weaker P20 domain result, before using them to discharge a cited leaf (`b109.md:3689–3730`). The user grants no referee status to this rebuild. The full Theorem 3 remains open. |

There are **7 unrefereed port files and 3 unrefereed proof/rebuild files** in this explicit check list. Of those three proof files, UM and OL are the two new repairs requested in half A; B109 is the additional rebuild used to locate K8 and the partial operator supplier. No check of an unfinished core lane counts as a proof of its endpoint. If its conditional lemma is used, read that argument at the use, with its premises.

Separate assembly checks remain: resolve J1's consumer dictionary, J2/J3/J4's exact scope, J5's joint state and scheme, and J6's domain extension. R11/R12 need porting as well as proofs of their leaves if the full CA comparison branches are pursued. The old LSC round-1 failure is not a new outstanding check: round 2 was refereed (`lsc.md:720–724`). P1/P3/P4/P5/P7 and MU/LRB/OC/UI/PDA/LSC retain their completed readings at the scopes recorded in §3.

## 7. Shortest remaining route to T0, in order

This is the shortest **presently specified route in this map**, not a theorem of optimality. It avoids adding tuned uniqueness or universal periodic-state recognition where existence needs only a selected volume-first hierarchy. It does not assume that any proposed bridge will succeed.

1. **Check the two new coupling repairs once, and fix the common construction dictionary.** Q8/Q9 decide whether UM and OL-transfer can replace the older open extraction/coefficient suppliers. Keep OL's original-family leaf open outside those consumers. Write J1's actual current, gauge, source, normalization and constant-order matches. This determines which further proofs are usable together.
2. **Close the hard joint-induction inputs at their exact scopes.** K1 (original words at the fixed rate), K8/R1 (actual hereditary small-field step), K2/K3 (outside and completion admission), K7/R7 (scalar reality and the full positive exact history construction), and R2–R6/BP/BC supply must all be available. These branches can be worked independently where their prerequisites permit; there is no asserted implication K1⇒K2⇒K3. Reuse MU/LRB/OC/UI/PDA. Complete Q10 for every B109 piece actually consumed. Do not restart the invalid universal-path route.
3. **Close the sourced induction and normalized estimates.** K4/K5 and R8 supply the missing window/switch inputs. Use checked P1/P4/P5/P7, ported P6/P10 and frozen LSC. Finish Q1/Q6/Q7. Derive J2 explicitly from the resulting source format, including ordinary repeated/mirror sources, rooted geometry and the common vacuum convention. This is the essential join into the frozen downstream chain.
4. **Finish the CA witness and its component extension.** Resolve R9/R10 with the precise P9 use-site bounds, supply the retained free/background inputs, and complete Q4/Q5. Use the sufficiently small interior coupling when that avoids an unnecessary supremum-endpoint claim. Prove J3 and the needed J4 lower witness on the actual PH1 realizations, or supply the full frozen TP1 package if that route is shorter. CA's torus-uniform bound alone does not settle this choice.
5. **Take volume first, then spacing, and apply the frozen chain.** Complete Q2/Q3 for the CA branch used. LG1 gives fixed-cutoff states and all mirrors; SR1 gives all-state bounds/growth; CL1 selects the hierarchy; PH1 supplies clustering components and the unique vacuum. RO1 then supplies full componentwise O(4) and insertion density; WR1 reconstructs each scalar theory. Record J6's full test-domain passage and common-realization identification. No new derivation of these frozen implications is needed unless an input changes.
6. **Close NT1 and NT2 on the same selected theory.** Apply TP1 Lemma 7.2 once J4 and PH1(5) hold. Supply all eight J5 witness inputs, the admissible joint blocked state and map, and the observable-scheme identification. The coefficient/running work from steps 1–3 can supply only the portions explicitly matched. NT2 is separate interacting work and may proceed earlier; it is written last here because the final assertion needs the constructed state.
7. **Assemble the actual theorem, with no status promotion.** All leaf contracts, their quantifiers and order must hold simultaneously. State the scalar observable/test-domain scope, component choice, and NT1/NT2 precisely. The checklist is not the proof; the cited written implications and supplied leaves must form it.

Do **not** add AV, AII-T-a, AV-f, general SU(N), mass gap, full gauge-sector identification, or arbitrary contact terms to this shortest route. They remain separately mapped or explicitly outside the working contract. Conversely, omitting J2, componentwise J3/J4, or NT2 would give a weaker target, not T0.

## 8. Recovery and verification limits

The source identity manifest is `/tmp/t0map-6d9df38c2/sources.json`; the targeted outline-index/neighbor excerpts are `/tmp/t0map-6d9df38c2/index-excerpts.txt`. Both upstream files match the identities recorded by the earlier lanes:

- SA, 32,992 lines: `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`.
- CA-I, 166,711 lines: `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`.

GOAL and the requested FINISH guidance were read first. The outline index README, relevant chunk rows/neighbors and obligations, and the CA 4.12–4.19 index were used before the corresponding bounded source reads. Main statement checks: SA:66–130; CA-I:2512–3016, in bounded pieces. The source/OS bridge readings include SA:4086–4122,4400–4474,4572–4627. The CA re-blocking/minimizer/prepared/stage scope checks include CA-I:45085–45115,45162–45175,45203–45224,45582–45614,49495–49546,54985–55000. Local import, hypothesis, Result and latest change-log sections govern the supplier map. This is not a fresh line-by-line check of all their proofs.

The workflow file named by AGENTS.md is absent in this pinned checkout. No substitute workflow, audit, planning-branch operation, external post or status promotion was performed. Searches stayed within the allowed checkout and task scratch files. No mathematical claim rests on a tool run. Text/hash/count checks are editorial bookkeeping only.

Current recovery decisions: check UM/OL's usable scope; close the actual hard-core contracts without conflating them with stage admission; derive the full ordinary-source join; obtain the all-state/component witness; retain NT2 and the final domain assembly. Failed path and original-word routes remain explicitly recorded above. Refresh this map against source changes before using a newer endpoint; never inherit a stale “open” or “closed” label without its scope.

Only `library/t0-tree.md` was changed in the repository. No editable prompt file, GOAL/FINISH, frozen proof, ledger, audit file, or platform instruction was modified.

## Result

**T0 is open. This assembly grants no scientific status.**

- **8 root contract branches**: existence, regularity/growth, O(4), RP, symmetry/reality, components/clustering, Wightman reconstruction, non-triviality.
- **12 port files inventoried**: **5 ported-checked**, **7 ported-unchecked**, including PI.
- **8 local repairs inventoried**: **6 proved/refereed**, **2 proved/unrefereed** (UM and OL-transfer), all conditional at their stated scopes.
- **7 frozen downstream texts** mapped, with **28 import slots** plus LG1's explicit no-scientific-import entry; foundational imports are separately recorded.
- **8 tracked core statements**: all eight literal endpoints remain OPEN; **one**, CO, has an unrefereed Gaussian-consumer bypass. These are not eight sufficient remaining axioms or a minimal basis.
- **12 residual A-contract bundles** and **6 T0 join/target obligations** remain visible; R11/R12 concern optional CA tuning branches.
- **22 printed Balaban bundles**: one geometric PDA instance is supplied conditionally; **21 retain open full-scope supply**. **6 cited frontier bundles** are retained; five have open analytic supply, while BC4's finite Wilson content is supplied and inherits the earlier open bounds.
- **10 explicit check units owed**: seven ports, UM, OL, and the B109 rebuild pieces used. J6 and the other interface matches also need their written assembly.

The displayed open-register total is **52 rows/contracts**: 8 K + 12 R + 6 J + 21 BP + 5 BC. This is a reproducible bookkeeping count of this map, **not** a count of distinct or independent unproved mathematical lemmas. Shared premises, nested contracts, optional branches and the CO bypass are stated explicitly. **Zero open mathematical statements were proved or refuted by this mapping lane.**
