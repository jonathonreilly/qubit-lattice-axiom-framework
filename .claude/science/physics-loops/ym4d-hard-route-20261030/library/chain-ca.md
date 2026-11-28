# CHAIN: Theorem 0 dependency map from the complete account

Provenance: Codex (GPT-6 family; reasoning effort not exposed), 2026-11-05; checkout 4c04bc6b52b71a474f45fd45a04e9b2ef1f3fb17. Research text, not an audit; grants no status. Source: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, complete account and outline at 31a47c543775. No proof is supplied here.

## Scope and reading rule

This maps the account's text. It proves, ports and independently checks no theorem. “Proved” below means **the account supplies a proof**, possibly of an implication. It does not mean its antecedents hold. The account distinguishes those meanings at CA-I:27–76. A cited Balaban theorem remains a porting obligation under GOAL.md:43–45; a printed sentence is a different kind of obligation.

The sources are `theorem_0_complete_account_raw_{I,II,III}.tex` at `31a47c543775`. Here `I:8110` means `/tmp/sa_ca_I.tex`, line 8110; likewise II and III. The fetched outline is `/tmp/sa_ym4.tex`. Its Theorem 0, SA:66–130, differs from the complete account's Theorem 0, I:2512–3022. This map uses the latter. Credit belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and to Tadeusz Balaban for the cited results.

The checkout is `4c04bc6b52b71a474f45fd45a04e9b2ef1f3fb17`. I read GOAL.md, the requested FINISH instructions, port-map.md, and the SA index before source excerpts. The requested `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent in this checkout. No workflow, audit or status operation was run. Structural scans and counting below are bibliography bookkeeping, not computer-assisted proof.

**Important limitation.** A complete, exact statement-level dependency census is not established by this note. The account's lists disagree with its statements; several named statements are unwritten, and some hypotheses have no identified supplier. Tables distinguish source-confirmed dependencies from list-only dependencies. Counts of displayed consumers are lower bounds, not an invented exact count of all intermediate lemmas. This qualification applies to the Result as well.

## 1. Clause order and subclauses

The account's principal order is at III:110790–110846. The order is:

1. Choose parameters: `2.4:lem-no-cycle` (I:1958), `2.4:prop-m-freeness` (I:2239), `2.4:prop-order-consistent` (I:2271). The last implication uses the first two. Its common dependency reaches every clause (III:110847–110866).
2. Prove (0) and (i) in **one induction**. They are not two independent vertices with an ordinary cyclic proof. Each level reads earlier levels; see I:166702–166709 and III:110790–110794.
3. Deduce (iii-a,c,d) by the correlation theorem and (iii-b) by the per-ball argument (III:110795–110796,110882–110899).
4. Deduce the first-passage torus limits (ii-T-b) and the growing-volume limits (ii-R4). The former reads (iii-a) and lattice reflection positivity. The latter also reads (iii-b) and (0) (III:110797–110806).
5. Deduce the core uniqueness theorem (v-a–e) from the correlation theorem on its prescribed scaffold and chapter 9's additional inputs; deduce the tuned torus family (ii-T-a) from that theorem (III:110798–110800,110821–110824,110966–111005).
6. Deduce the finite-cutoff witness (iv) from (0), (i), (iii), chapter 8, and volume transfer. Its continuum consequences additionally read the appropriate branch of (ii) (III:110807–110820,110908–110965).
7. Keep the **(v-f) addition** separate: it reads (iii), (iv), and the core of (v) (III:111000–111005). The short-distance corollary also reads (iv) (III:75898–75903). Thus the blanket sentence “(iv) is read by no other clause” (III:110842) is not adequate for the full printed (v).

Do not feed (v-f) back into the proof of (v-a–e), or the witness's continuum consequences back into its finite-cutoff theorem. This is the distinction the source's local inputs require, not a new proof of acyclicity.

| Branch | What is asserted | Direct account input statement |
|---|---|---|
| (0) | First passage, two-sided flow bounds, fixed-depth windows | I:2533–2554; III:110790–110794 |
| (i) | Representation, integrated stability, equality of integrals, exact insertion | I:2556–2595; III:110871–110881 |
| (iii) | Torus and per-ball bounds, running shift, cumulative one-loop law | I:2598–2658; III:110882–110899 |
| (ii-T-b) | Subsequence on each fixed torus | I:2683–2689; III:110800–110802 |
| (ii-R4) | One joint diagonal subsequence, hypercubic symmetries, curvature reconstruction | I:2690–2713; III:110803–110806,110903–110907 |
| (v-a–e) | Tuned family and comparison in the two labellings | I:2828–2983; III:110966–110999 |
| (ii-T-a) | Tuned torus limit without subsequences | I:2668–2682; III:75770–75772 |
| (iv) | Finite-cutoff witness, volume transfer, then limit consequences | I:2715–2826; III:110908–110965 |
| (v-f) | Coupling covariance, increments and injectivity | I:2984–3016; III:111000–111005 |

The extra identification sentence of (ii-T-b), I:2688–2689, invokes (v-c)(2). It must not be confused with the existence of the subsequence. The first-passage offsets sentence at I:2682 is another extra assertion, with its own outstanding lemma (II:65470–65489,68351–68353).

The detailed frontier below is for SU(2). The printed theorem also includes (0)/(i) at N≥3. Two additional programme-level inputs are incomplete: the SU(N) stability constants and the passage of every underlying N=2 argument to SU(N), III:111133–111140. They block both (0) and (i) at N≥3, not the N=2 clauses. The near-action stability input is separately listed at I:166690–166692. Their full statement-level expansion is not completed here. No other printed clause is asserted at N≥3 (I:2525–2526). Neither block-law results nor clause (vi) belong to this task (III:110839–110846).

## 2. Ordered main statements and their named inputs

Read each row from inputs to output. These are port **entry points**, not a claim that every proof lemma below them has been enumerated. “Implication” retains every antecedent displayed at the cited statement. Source headings without a status qualification have the convention of I:27–42; explicit missing-proof declarations override that convention.

### 2.1 The joint flow and ultraviolet induction

| Order | Statement and source | Source standing and inputs |
|---|---|---|
| A1 | `4.2:lem-one-loop`, I:3901; `4.3:thm-small-field-step`, I:4136; `4.3:thm-uv-stability`, I:4209 | Cited Balaban inputs: 109 Theorem 3, 116 (2.41), 122b Theorem 1. These are not proofs reproduced in CA. |
| A2 | `4.4:prop-local-real-base`, I:8110–8373 | Outstanding. The local base is an explicit input of the localised-independence corollary, I:9668–9669. It is missing from both summary lists. |
| A3 | `4.4:cor-localised-independence`, I:9615–9670 | Implication. Named inputs include local data classes, uniform agreement, interior sufficiency, the vertex formula, local coercivity, and A2 (I:9624,9639–9641,9668–9669). |
| A4 | `4.5:thm-operator-bounds`, I:19578–19867 | Implication. Named hypotheses at I:19580–19600 include the covariance-inverse walk sentence, averaging analyticity, window minimiser, literal frame and complex block-curvature statement. Its proof explicitly uses `4.5:lem-uniform-increment` at I:19783; that lemma is incomplete at I:16019. |
| A5 | `4.6:prop-logarithm-convergence`, I:22645; `4.6:prop-large-field-bound`, I:22860–22908 | Logarithm convergence has a proof. Large-field representation is an implication from the complex-domain convention, polymer expansion, convergence, activity bound and standing bounds (I:22861–22875). The polymer-gas representation imports 122b (1.90), I:166601–166602. |
| A6 | `4.7:prop-beta-extraction`, I:32226–32410; `4.7:prop-coupling-increment`, I:32412–32496 | Implications from the preceding-level induction, kernel-power bound, smallness conditions, hereditary class and localised independence (I:32228–32231,32413–32430). |
| A7 | `4.12:prop-reblocking-inside`, I:44127; `4.12:cor-real-factor-slots`, I:44803; `4.12:prop-reblocking-outside`, I:45085 | Inside re-blocking is incomplete and outside re-blocking outstanding. The list calls the corollary incomplete (I:166619), but its own proof is an implication from re-blocking and hypothesis (b), I:44804–44844. Do not count that corollary as another missing proof. |
| A8 | `4.13:lem-minimizer-unique`, I:45162–45175; `4.13:lem-own-constant`, I:45203–45224 | Both outstanding at their headings, I:45163,45204. The first covers every field admitted by 109 Lemma 4, including nesting on subdomains; the second concerns the pairs' own curvature constant. |
| A9 | `4.14:prop-prepared-data-admissible`, I:45557; `4.14:thm-operator-theorem`, I:46035–46156 | Prepared-data admission is printed without proof in 122a pp.178–179. The operator theorem assumes it, the real backgrounds and block-size conditions (I:46041–46048). Its application has further supply conditions outside its implication (I:49495–49546). |
| A10 | `4.18:thm-preparatory-boundary`, I:54985 | Implication from Balaban's stage theorem, 122a (1.60)–(1.70), explicitly assumed at I:54989–54998. Do not count the stage theorem as proved by this implication. |
| A11 | `4.19:lem-flow-bounds`, I:56342–56359; `4.2:lem-first-passage`, I:3636 | Arithmetic port leaves, conditional on their displayed numerical hypotheses. Their use in (0) is explicit at I:56472,56498. |
| A12 | `4.19:prop-clause-zero`, I:56419–56524 | Implication from hypotheses (a)–(h), I:56424–56437: the small-field step, widened gauge reproduction, one-loop and unmarked bounds, large-field increment, localised independence, operator bounds, large-field representation, hereditary class and torus independence. It also takes the representation at already reached scales, I:56439–56441. |
| A13 | `4.19:prop-containment`, I:56530–56566; `4.19:cor-windows`, I:56568–56630 | Proved implications from A12 and the stated coupling ceiling. These supply the containment and fixed-depth window clauses. |
| A14 | `4.38:thm-torus-independence`, I:58187–58411 | Implication from its seven hypotheses, I:58188–58216: A3, local walk and single-cell statements, covariance, A4, A6, A5's format and joined-domain extension, and local label rules. The level hypothesis is separate, I:58219 onward. |
| A15 | `4.38:cor-step-count`, I:60810–60878 | Proved implication from A14's hypotheses (I:60812–60813); this is the torus-independent number of steps. |
| A16 | `4.21:prop-relative-machine`, I:61212–61325 | Outstanding at I:61325. Its displayed assumptions include persistence of near-group weights and supply of stored orbit data, both not proved (I:61304–61310). The chapter list additionally attributes volume counts, two data bounds and a kernel-difference bound to this machine (I:166652–166657); that attribution still needs a precise supplier map. |
| A17 | `4.20:thm-representation`, I:61095–61206 | Representation output used by A12 and stability; its full antecedent frontier still needs a complete expansion. Its use is explicit at I:56439–56441 and I:157032. The numbered label must not be treated as a closed leaf. |
| A18 | `4.32:prop-positivity-dichotomy`, I:156837–156951 | Outstanding at I:156837. The assembly calls it incomplete (III:110873–110874); source heading takes priority. |
| A19 | `4.33:thm-stability`, I:157028–157241 | Implication. Hypotheses (h1)–(h8) include representation plus A18, regular bounds, positive flow, the vacuum-energy theorem, history majorants and their sum, unit fibre mass, and positive reference normalisations (I:157032–157075). No independent positivity conclusion is supplied for (h8) by naming it. |
| A20 | `4.34:lem-sourced-exactness`, I:157263 | Sourced equality is the exactness part of (i); the complex-source format still reads the sourced correlation induction, I:2592–2595. |

The four main intermediate steps assigned to (0) by the assembly are A3, A4, A5 and A6 (III:111058–111064,111098). They are not the complete leaf frontier. In particular, A2 and the incomplete uniform-increment lemma remain below them.

### 2.2 Correlations and the three limit regimes

| Order | Statement and source | Source standing and inputs |
|---|---|---|
| B1 | `5.6:prop-polydisc-holomorphy`, II:46131–46165 | **Outstanding at II:46167**, despite the index's PROVED. It supplies hypothesis (H-circle) of `5.6:lem-weight`, not the reverse implication (II:46144–46153). |
| B2 | `5.6:lem-weight`, II:45154–45366; `5.5:lem-weight`, II:35258–35626 | Printed proofs of implications from their displayed hypotheses; the assembly counts the weight lemma as incomplete (III:111080–111088,111103). Do not count both as two independently missing proofs without checking their relationship. B1 is an explicit missing supplier. |
| B3 | `5.1:thm-correlation-theorem`, II:2791–2966 | Implication from (0)/(i), the source induction and its weight machinery; source standing at III:110882–110894. The chapter's open list names B1 (II:60283–60286), but is not the complete inherited frontier. |
| B4 | `5.3:lem-driven-flow`, II:26201; `5.14:thm-one-loop-law`, II:27042 | Running-shift and cumulative-flow ports. One-loop law inherits B3's flow and A1 under the identification of the increment; no further open input is claimed in the assembly (III:110890–110894,111107–111115). |
| B5 | `6.1:lem-reflection-positivity`, II:60440–60624 | Lattice reflection positivity is proved in this chapter (III:110901–110902); it is a separate input, not a consequence of a continuum limit. Its cited finite-cutoff equations are 109 (0.1),(0.2), II:64605–64608. |
| B6 | `6.3:lem-last-scale-constants`, II:63365–63367 | The statement is unwritten and only parts of the proof follow. The assembly calls it incomplete, III:110895–110899, despite “none” at II:64603. |
| B7 | `6.4:thm-per-ball-bound`, II:63964–64068 | Implication from B3, B5, B6, and 116 (1.26), III:110895–110899. Its support-placement, chessboard, periodisation and ultraviolet-bound lemmas are named in the proof, II:64004–64068. |
| B8 | `5.12:prop-subsequential-limits`, II:59926–60087; `5.12:lem-limit-positivity`, II:60089–60178 | Torus first-passage implication from B3 and finite-lattice positivity; no new open input according to II:60291–60296. This is (ii-T-b)'s existence, before its extra (v-c)(2) identification. |
| B9 | `7.3:thm-tuned-family`, II:65424–65465 | Tuned torus output from the uniqueness theorem, III:75770–75772. The offsets assertion separately uses `7.3:lem-first-passage-offsets`, II:65470–65489, outstanding. |
| B10 | `7.4:lem-torus-transport`, II:65661–65767; `7.4:lem-lattice-symmetries`, II:65844–65927; `7.4:lem-half-space`, II:65929–66046; `7.4:lem-translation-modulus`, II:66048–66144; `7.4:lem-linearity`, II:66209–66332 | Proved finite-cutoff/transport deductions on the stated domains. They feed the joint subsequence argument; the finite-cutoff inputs are explicitly catalogued at II:68339–68344. |
| B11 | `7.4:thm-infinite-volume`, II:66412–66675; `7.4:prf-equicontinuity`, II:66677–66843 | Joint diagonal subsequence and equicontinuity, conditional on the per-ball bound and the named finite-cutoff inputs (III:110903–110907; II:68362–68367). |
| B12 | `7.5:prf-limit-distributions`, II:67014–67129; `7.5:prf-exact-invariance`, II:67131–67310; `7.6:prf-centred-positivity`, II:67312–67515 | Proved deductions in the B11 setting. Parent-theorem references in their headings identify the assertion being proved; they are not circular dependency edges. |
| B13 | `7.7:prf-reconstructed-space`, II:67528–67753 | Curvature-space reconstruction from B11–B12. Scope is I:2698–2711: H≥0 and spatial translations, not the Wightman or forward-cone conclusions excluded there. |

### 2.3 Witness and volume transfer

| Order | Statement and source | Source standing and inputs |
|---|---|---|
| C1 | `8.1:lem-gaussian-squares`, II:69457; `8.1:lem-free-curvature-covariance`, II:69516; `8.1:lem-kernel-positivity`, II:69682; `8.1:lem-kernel-bounds`, II:69925; `8.1:lem-running-normalisation`, II:70501 | Free-field port entry points. Do not substitute them for the distinct unwritten `8.21:lem-continuum-kernel` (II:145220–145222). |
| C2 | `8.4:thm-minimiser-analyticity`, II:85845 | Cited 102b Theorem 1, Proposition 9 and (190). It is an external leaf, not a reproduced proof. |
| C3 | `8.4:prop-small-piece`, II:88192; `8.5:def-representation-identity`, II:90196 | Incomplete small-piece bound and outstanding shifted-frozen-run identity (II:145591–145592). These feed localisation/extraction, III:110943–110950. |
| C4 | `8.5:lem-radius-tails`, II:90729; `8.5:thm-room-lemma`, II:93196; `8.5:prop-remainder-covariance`, II:94225 | The list calls all three incomplete (II:145593–145596). At source, radius tails is a proved implication from a missing fine-field bound and profile locality (II:90834–90843); remainder covariance explicitly assumes its missing inputs (II:94242–94261). Room lemma itself is incomplete. |
| C5 | `8.2:prop-gaussian-extraction`, II:77279 | Implication through the correlation theorem, cluster expansion and C2; the second-order input needs the displayed exponent floor q≥21p0+1, III:110944–110950. Keep C4's missing steps. |
| C6 | `8.6:lem-prefactor-monotone`, II:102730; `8.6:lem-healed-islands-unread`, II:103387; `8.6:lem-annealed-removal`, II:104598 | The first two are incomplete at their headings. The list also calls annealed removal incomplete (II:145599), but it prints a conditional proof from its assumptions (II:104599–104626,104628–104761). |
| C7 | `8.7:lem-translation-covariance`, II:107738; `8.8:lem-target-independence`, II:109661; `8.9:lem-age-lemma`, II:112000; `8.12:prop-depth-floor-rarity`, II:126839 | Incomplete, II:145600–145604. The last is a volume-dependent depth-floor statement; it is not uniform-old-rarity. |
| C8 | `8.21:lem-source`, II:145173; `8.21:lem-continuum-kernel`, II:145220 | Source lemma outstanding; continuum-kernel statement and proof unwritten. Both explicitly appear in the assembly, III:110951–110955. |
| C9 | `8.18:thm-torus-witness`, II:144922–145115 | Proved implication from its below-/beyond-horizon statements and depth-floor closure. The assembly's ordered ingredients are at III:110922–110950. |
| C10 | `8.22:thm-volume-transfer`, II:141540–141852 | Proved implication. Normaliser supply reads A14 and the normalising-constant lemma; large volume needs only lattice positivity and lower stability (III:110955–110961). |
| C11 | `8.1:thm-two-point-witness`, II:71279 | Witness statement, with its own inputs marked at II:71370–71384. Assemble C9 and C10, then transfer to each B8/B9/B11 limit using positivity (III:110817–110820). |

Uniform-old-rarity (`8.12:prop-uniform-old-rarity`, II:127294) is **not** a missing input of this route: the assembly expressly excludes it (III:110963–110965). Model exit/inactivity theorems are not a substitute for actual large-field bounds; their model-only status is explicit at III:111498–111507. No verified use outside a model has been identified in this map.

### 2.4 Uniqueness, tuning and the additional coupling statement

| Order | Statement and source | Source standing and inputs |
|---|---|---|
| D1 | `9.1:not-radius-exponent-floors`, III:7; `9.1:not-levelwise-rate`, III:120; `9.1:not-shell-floor-chain`, III:213 | Outstanding assertions embedded in definitions; their unresolved status is explicit at III:108,120,213 and in III:75827–75832. |
| D2 | `9.2:thm-carry`, III:25267 | Incomplete; the extension proposition is itself incomplete (III:24288,75835–75836). |
| D3 | `9.2:thm-geometric-forgetting`, III:34033 | Conditional on the majorant and its nesting clause, outstanding at III:75846–75849. Naming a conditional forgetting theorem does not supply the majorant. |
| D4 | `9.3:prop-second-variation`, III:35577; `9.3:prop-propagator-stationarity`, III:37365 | First is 102b (189)–(190), printed without proof; second outstanding. |
| D5 | `9.4:rem-the-zeroth-order-response-read-on-the-sh`, III:37611–37665 | Outstanding shell transfer at III:37627. Its explicit clause-by-clause scope is III:37636–37648: needed for (v) and (ii-T-a), not (0),(i),(iii),(iv). |
| D6 | `9.5:prop-the-two-cutoff-smallness-of-the-kept-fac`, III:37667; `9.5:prop-remainder-difference`, III:43702 | Outstanding kept-factor bound and remainder-difference input; the former also needs the nested interrupted Gaussian comparison (III:111269–111276,75858–75863). |
| D7 | `9.6:lem-maximum-principle`, III:51821; `9.6:def-comparison-chain`, III:51854; `9.6:lem-chain-structure`, III:51909 | Outstanding at III:51840,51896,51940. These are separate assumptions, even though one is written as a definition. |
| D8 | `9.8:thm-uniqueness-theorem`, III:53784–53951 | Core implication; its additional open inputs are catalogued at III:75825–75894. Its first-passage exhaustion additionally needs `9.8:cor-subsequential-limits`, III:54156–54188, outstanding. |
| D9 | `9.10:thm-refiled-induction`, III:59874–59876; `9.10:thm-refiled-lipschitz`, III:60826; `9.10:thm-lipschitz-kernel`, III:61063 | Induction statement unwritten with partial proof; the latter two incomplete. Their own output theorem does not discharge these antecedents. |
| D10 | `9.10:prop-source-bounds`, III:61923; `9.10:lem-load-envelope`, III:62898; `9.10:thm-last-lattice-comparison`, III:63225; `9.11:prop-source-families`, III:65059; `9.11:thm-geometric-envelope`, III:65827 | All carry incomplete headings. Feed the renormalised-coordinate exponential-rate argument `9.10:thm-exponential-rate`, III:63536–63647. |
| D11 | `9.12:lem-defect-summability`, III:67255–67293; `9.12:lem-bi-lipschitz`, III:67295–67515; `9.12:cor-same-limit`, III:67764–67864 | Proved implications in the tuned-family setting. Endpoint case remains outstanding at III:67866–67879. |
| D12 | `9.13:lem-change-of-units`, III:68448–68509; `9.13:lem-re-rooting`, III:69084–69244; `9.13:lem-depth-convergence`, III:69264–69467; `9.13:thm-limit-member`, III:69553–69918 | The theorem is a proved implication from change of units, earlier uniqueness/flow inputs and the two comparison lemmas (III:69583 onward). This must be distinguished from the earlier outstanding `9.13:lem-limit-member`, III:68855–68889. The summary list still lists the older lemma (III:75894). |
| D13 | `9.8:thm-two-blockings`, III:55354–55356 | Statement unwritten, partial proof follows. This is the additional (v-f) branch; its summary standing is an implication from (iii),(iv),(v), III:111000–111005. Exact source reconciliation remains necessary. |
| D14 | `9.98:thm-short-distance-uniqueness`, III:72033–72196 | Further corollary, outside the bare core of (v). Inputs explicitly include D8, its first-passage exhaustion, (iii), and (iv), III:75898–75903. |

The appearance of the main theorem's name in a lemma's setting, or of a parent theorem in a “Proof of” heading, is not a dependency edge. A raw `\\ref` graph would create false cycles here. It would also mistake B1's reference to the weight lemma it supplies for a dependence on that lemma.

## 3. Open frontier: source declarations and reach

The table records explicit missing-proof declarations at their source. It excludes the conditional deductions separated in §4. It does **not** claim these are all the leaves. The open statements embedded in prose in §5 also matter.

The reach codes count **clause branches**, not all intermediate chain statements. The latter count is unresolved. This is a deliberately labelled lower-resolution count:

| Code | Clauses whose complete stated route reads this group | Branch count | Evidence |
|---|---|---:|---|
| J | (0), (i), (iii), (ii-T-b), (ii-R4), (v), (ii-T-a), (iv) | 8 | Joint induction and inheritance, III:110790–110824,111044–111052; chapter-4 list I:166615–166692 |
| S | (iii), (ii-T-b), (ii-R4), (v), (ii-T-a), (iv) | 6 | Correlation theorem and downstream branches, III:110795–110824 |
| R | (iii-b), (ii-R4) | 2 | III:110895–110907; no claim here that the torus uniqueness proof uses this volume-free input |
| W | (iv), (v-f) | 2 | III:110922–110965,111000–111005 |
| U | (v), (ii-T-a), at the chapter's list resolution | 2 | III:75770–75772,75825–75894; finer attribution within (v) remains to be checked |
| Ta | The first-passage-offset assertion attached to (ii-T-a) | 1 | II:68351–68353 |
| Uf | (v-f) | 1 | III:111000–111005 |

For U, the list does not establish that **every** entry blocks the convergence-only part of (ii-T-a). In particular, derivative/calibration inputs may serve a narrower part of (v). Its branch count is a list attribution, not a certified minimal dependence. Similarly J groups the single induction without counting earlier-level uses as cycles.

| # | Statement | Source | Direct missing-proof declaration | Reach | Additional source evidence |
|---|---|---|---|---|---|
| F01 | `2.4:prop-m-freeness` | I:2239 | incomplete, I:2239 | J | Same statement as `5.10:prop-m-freeness`, II:59574; count once (II:59590–59592). Missing step II:59607–59609. |
| F02 | `4.2:lem-unmarked` | I:4031 | incomplete, I:4031 | J | Source heading or following declaration; chapter attribution as above. |
| F03 | `4.4:prop-local-real-base` | I:8110 | outstanding, I:8110 | J | Omitted from summary lists; explicit consumer I:9668–9669. |
| F04 | `4.5:lem-uniform-increment` | I:16019 | incomplete, I:16019 | J | Omitted from summary lists; explicit consumer I:19783. |
| F05 | `4.12:prop-reblocking-inside` | I:44127 | incomplete, I:44128 | J | Source heading or following declaration; chapter attribution as above. |
| F06 | `4.12:prop-reblocking-outside` | I:45085 | outstanding, I:45085 | J | Source heading or following declaration; chapter attribution as above. |
| F07 | `4.13:lem-minimizer-unique` | I:45162 | outstanding, I:45163 | J | Source heading or following declaration; chapter attribution as above. |
| F08 | `4.13:lem-own-constant` | I:45203 | outstanding, I:45204 | J | Source heading or following declaration; chapter attribution as above. |
| F09 | `4.21:prop-relative-machine` | I:61212 | outstanding, I:61325 | J | Source heading or following declaration; chapter attribution as above. |
| F10 | `4.22:not-live-region-geometry` | I:85575 | outstanding, I:85575 | J | Source heading or following declaration; chapter attribution as above. |
| F11 | `4.22:prop-stage-totals` | I:87328 | incomplete, I:87329 | J | Source heading or following declaration; chapter attribution as above. |
| F12 | `4.24:prop-norm-conversion` | I:106533 | outstanding, I:106533 | J | Source heading or following declaration; chapter attribution as above. |
| F13 | `4.24:prf-field-dependence` | I:106589 | incomplete, I:106589 | J | Source heading or following declaration; chapter attribution as above. |
| F14 | `4.24:prop-holonomy-bound` | I:107073 | outstanding, I:107073 | J | Source heading or following declaration; chapter attribution as above. |
| F15 | `4.25:lem-gaussian-pieces` | I:110806 | incomplete, I:110806 | J | Used by dissolution at I:115120 and piece oscillation at I:111191. |
| F16 | `4.25:lem-piece-oscillation` | I:111188 | incomplete, I:111188 | J | Source heading or following declaration; chapter attribution as above. |
| F17 | `4.25:lem-non-deep-pieces` | I:114658 | incomplete, I:114658 | J | Used by dissolution at I:115128,115167. |
| F18 | `4.25:prop-dissolution` | I:115062 | incomplete, I:115062 | J | Source heading or following declaration; chapter attribution as above. |
| F19 | `4.27:lem-t-step-layer` | I:131633 | incomplete, I:131633 | J | Source heading or following declaration; chapter attribution as above. |
| F20 | `4.27:lem-weights-heredity` | I:132878 | incomplete, I:132878 | J | Source heading or following declaration; chapter attribution as above. |
| F21 | `4.27:prf-stage-move-cubes` | I:134184 | incomplete, I:134184 | J | Source heading or following declaration; chapter attribution as above. |
| F22 | `4.27:prf-density-increase` | I:135143 | incomplete, I:135143 | J | Source heading or following declaration; chapter attribution as above. |
| F23 | `4.27:prf-unheld-raw-points` | I:135466 | incomplete, I:135467 | J | Used by index-zero margin at I:136227. |
| F24 | `4.27:prf-index-zero-margin` | I:136192 | incomplete, I:136192 | J | Source heading or following declaration; chapter attribution as above. |
| F25 | `4.27:prf-ambient-inclusion` | I:136490 | incomplete, I:136490 | J | Source heading or following declaration; chapter attribution as above. |
| F26 | `4.27:lem-real-minimiser` | I:136809 | incomplete, I:136809 | J | Used by index-zero margin at I:136374 and members under maps at I:140750. |
| F27 | `4.27:thm-arrest-theorem` | I:137628 | incomplete, I:137628 | J | Source heading or following declaration; chapter attribution as above. |
| F28 | `4.27:prf-newborn-continuation` | I:138485 | incomplete, I:138486 | J | Source heading or following declaration; chapter attribution as above. |
| F29 | `4.27:prop-live-piece-bounds` | I:138933 | incomplete, I:138933 | J | Source heading or following declaration; chapter attribution as above. |
| F30 | `4.27:rem-raw-current-radius` | I:140297 | incomplete, I:140297 | J | Source heading or following declaration; chapter attribution as above. |
| F31 | `4.27:rem-index-zero-members` | I:140692 | incomplete, I:140692 | J | Source heading or following declaration; chapter attribution as above. |
| F32 | `4.28:lem-near-pair-sums` | I:145837 | incomplete, I:145837 | J | Missing clause (e) imported by core freezing, I:146102–146104. |
| F33 | `4.30:lem-no-two-sided-point` | I:152408 | incomplete, I:152408 | J | Source heading or following declaration; chapter attribution as above. |
| F34 | `4.30:prop-cell-counting` | I:152723 | unwritten / incomplete, I:152724 | J | Imported as hypothesis (h) of frames-instance, I:153221–153223. |
| F35 | `4.32:prop-positivity-dichotomy` | I:156837 | outstanding, I:156837 | J | Source heading or following declaration; chapter attribution as above. |
| F36 | `5.6:prop-polydisc-holomorphy` | II:46131 | outstanding, II:46167 | S | Supplies H-circle, II:46144–46153; index PROVED is wrong. |
| F37 | `6.3:lem-last-scale-constants` | II:63365 | unwritten / incomplete, II:63366 | R | Chapter list says none, II:64603; assembly says incomplete, III:110898–110899. |
| F38 | `7.3:lem-first-passage-offsets` | II:65470 | outstanding, II:65470 | Ta | Only offsets assertion; not required for basic subsequence existence, II:68351–68356. |
| F39 | `8.4:prop-small-piece` | II:88192 | incomplete, II:88192 | W | Source heading or following declaration; chapter attribution as above. |
| F40 | `8.5:def-representation-identity` | II:90196 | outstanding, II:90196 | W | Source heading or following declaration; chapter attribution as above. |
| F41 | `8.5:def-profile-locality` | II:90607 | incomplete, II:90607 | W | Explicit input of remainder covariance, II:94259–94261, and room proof, II:93329. |
| F42 | `8.5:prop-zero-block-mean` | II:91539 | incomplete, II:91539 | W | Explicit room input, II:93214. |
| F43 | `8.5:thm-room-lemma` | II:93196 | incomplete, II:93196 | W | Source heading or following declaration; chapter attribution as above. |
| F44 | `8.5:cor-room-witness-unit` | II:93890 | incomplete, II:93890 | W | Explicit remainder-covariance input, II:94307,94476. |
| F45 | `8.6:lem-prefactor-monotone` | II:102730 | incomplete, II:102730 | W | Source heading or following declaration; chapter attribution as above. |
| F46 | `8.6:lem-healed-islands-unread` | II:103387 | incomplete, II:103387 | W | Source heading or following declaration; chapter attribution as above. |
| F47 | `8.7:lem-translation-covariance` | II:107738 | incomplete, II:107738 | W | Source heading or following declaration; chapter attribution as above. |
| F48 | `8.8:lem-target-independence` | II:109661 | incomplete, II:109661 | W | Source heading or following declaration; chapter attribution as above. |
| F49 | `8.9:lem-age-lemma` | II:112000 | incomplete, II:112000 | W | Source heading or following declaration; chapter attribution as above. |
| F50 | `8.12:prop-depth-floor-rarity` | II:126839 | incomplete, II:126839 | W | Source heading or following declaration; chapter attribution as above. |
| F51 | `8.21:lem-source` | II:145173 | outstanding, II:145173 | W | Source heading or following declaration; chapter attribution as above. |
| F52 | `8.21:lem-continuum-kernel` | II:145220 | unwritten, II:145221 | W | Source heading or following declaration; chapter attribution as above. |
| F53 | `9.1:not-radius-exponent-floors` | III:7 | outstanding, III:108 | U | Source heading or following declaration; chapter attribution as above. |
| F54 | `9.1:not-levelwise-rate` | III:120 | outstanding, III:120 | U | Source heading or following declaration; chapter attribution as above. |
| F55 | `9.1:not-shell-floor-chain` | III:213 | outstanding, III:213 | U | Source heading or following declaration; chapter attribution as above. |
| F56 | `9.1:prop-blind-site-expansions` | III:16559 | outstanding, III:16559 | U | Source heading or following declaration; chapter attribution as above. |
| F57 | `9.2:thm-carry` | III:25267 | incomplete, III:25267 | U | Source heading or following declaration; chapter attribution as above. |
| F58 | `9.2:prop-boundary-term-variation` | III:26156 | incomplete, III:26156 | U | Source heading or following declaration; chapter attribution as above. |
| F59 | `9.2:prop-rest-term-tail` | III:26384 | incomplete, III:26384 | U | Source heading or following declaration; chapter attribution as above. |
| F60 | `9.2:lem-aligned-parts` | III:26424 | incomplete, III:26424 | U | Source heading or following declaration; chapter attribution as above. |
| F61 | `9.2:rem-full-history-index` | III:26575 | incomplete, III:26575 | U | Source heading or following declaration; chapter attribution as above. |
| F62 | `9.2:prop-response-factor` | III:27871 | incomplete, III:27871 | U | Source heading or following declaration; chapter attribution as above. |
| F63 | `9.2:prop-modulus-majorant` | III:32417 | outstanding, III:32417 | U | Source heading or following declaration; chapter attribution as above. |
| F64 | `9.2:lem-linear-size-lower` | III:33089 | incomplete part (2), III:33089–33111 | U | Do not assign part (2)'s missing proof to part (1). |
| F65 | `9.3:prop-propagator-stationarity` | III:37365 | outstanding, III:37365 | U | Source heading or following declaration; chapter attribution as above. |
| F66 | `9.4:rem-the-zeroth-order-response-read-on-the-sh` | III:37611 | outstanding, III:37627 | U | Source heading or following declaration; chapter attribution as above. |
| F67 | `9.5:prop-the-two-cutoff-smallness-of-the-kept-fac` | III:37667 | outstanding, III:37668 | U | Source heading or following declaration; chapter attribution as above. |
| F68 | `9.5:prop-remainder-difference` | III:43702 | outstanding, III:43702 | U | Source heading or following declaration; chapter attribution as above. |
| F69 | `9.6:lem-maximum-principle` | III:51821 | outstanding, III:51840 | U | Source heading or following declaration; chapter attribution as above. |
| F70 | `9.6:def-comparison-chain` | III:51854 | outstanding, III:51896 | U | Source heading or following declaration; chapter attribution as above. |
| F71 | `9.6:lem-chain-structure` | III:51909 | outstanding, III:51940 | U | Source heading or following declaration; chapter attribution as above. |
| F72 | `9.8:cor-subsequential-limits` | III:54156 | outstanding, III:54156 | U | Source heading or following declaration; chapter attribution as above. |
| F73 | `9.8:thm-two-blockings` | III:55354 | unwritten, III:55355 | Uf | Unwritten parent statement of the (v-f) argument; summary says implication, III:111000–111005. |
| F74 | `9.9:prop-remainder-derivative` | III:56333 | outstanding, III:56333 | U | Source heading or following declaration; chapter attribution as above. |
| F75 | `9.10:thm-refiled-induction` | III:59874 | unwritten / incomplete, III:59875,75877–75878 | U | The original statement is unwritten; the chapter list calls it incomplete. |
| F76 | `9.10:thm-refiled-lipschitz` | III:60826 | incomplete, III:60826 | U | Source heading or following declaration; chapter attribution as above. |
| F77 | `9.10:thm-lipschitz-kernel` | III:61063 | incomplete, III:61063 | U | Source heading or following declaration; chapter attribution as above. |
| F78 | `9.10:prop-source-bounds` | III:61923 | incomplete, III:61923 | U | Source heading or following declaration; chapter attribution as above. |
| F79 | `9.10:lem-load-envelope` | III:62898 | incomplete, III:62898 | U | Source heading or following declaration; chapter attribution as above. |
| F80 | `9.10:thm-last-lattice-comparison` | III:63225 | incomplete, III:63225 | U | Source heading or following declaration; chapter attribution as above. |
| F81 | `9.11:prop-source-families` | III:65059 | incomplete, III:65059 | U | Source heading or following declaration; chapter attribution as above. |
| F82 | `9.11:thm-geometric-envelope` | III:65827 | incomplete, III:65827 | U | Additional incomplete output, beyond the list entry naming source families, III:75892. |

## 4. Reconcile the lists before counting missing proofs

These are not stylistic differences. They change the set of open statements and any count of their consumers.

| Statement | List's standing | Source evidence and disposition |
|---|---|---|
| `4.12:cor-real-factor-slots`, I:44803 | Incomplete, I:166619 | I:44804–44844 prints a deduction from re-blocking and a real-factor hypothesis. Count the missing supplier, not another unfinished proof merely because the antecedent is incomplete. |
| `4.22:def-kept-term-reader`, I:85720 | Outstanding, I:166660–166661 | It reads the outstanding live-region geometry, I:85721–85722,85757,85776. The asserted geometric supply is not a pure definition. Resolve those inputs before assigning a separate leaf. |
| `4.22:lem-probe-summand`, I:86220 | Outstanding, I:166662 | Prints proof I:86262–86303, expressly using the outstanding geometry at I:86238. Proved implication, with an open antecedent. |
| `4.22:prop-foreign-operation`, I:87631 | Outstanding, I:166664 | Prints proof I:87689–87760, assuming geometry at I:87671 and earlier kept-term results. Proved implication, with open antecedents. |
| `4.24:rem-covariance-decay`, I:105181 | Included under (i), I:166665 | Explicitly **not used** by (i), I:105193–105194. Exclude from the mandatory (i) frontier. |
| `4.27:lem-current-probe`, I:135723 | Incomplete, I:166675 | I:135726–135728 says only definitions from weights-heredity are used, none of its conclusions. Proof at I:135770–135839. The neighbouring “incomplete” phrase describes another lemma. Source does not justify treating this as another unfinished proof. |
| `4.28:prop-core-freezing`, I:146051 | Incomplete, I:166686 | Prints a conditional proof I:146113–146216. Hypothesis (vii) imports incomplete near-pair-sums clause (e), I:146102–146104. The missing leaf is `4.28:lem-near-pair-sums`, I:145837. |
| `4.30:prop-frames-instance`, I:153174 | Cell counting listed incomplete, I:166688–166689 | Hypothesis (h) explicitly imports `4.30:prop-cell-counting`, I:153221–153223. The actual unwritten proposition is I:152723–152725. Do not attach its status to the complete application proof I:153242–153352. |
| `5.5:lem-weight`, II:35258, and `5.6:lem-weight`, II:45154 | Weight lemma counted incomplete, III:111087,111103 | Both have conditional proofs. The polydisc supplier is explicitly outstanding, II:46167. The remaining named hypotheses must be resolved before deciding whether the two labels denote one or two extra open obligations. |
| `5.11:lem-sixth-family`, II:59618 | Outstanding, III:111239–111240 | Statement and proof absent, II:59619. The adjacent ejected-components question expressly has no dependants, II:59623–59624. Do not infer that its appearance near the correlation proof supplies an on-chain edge. Membership remains unresolved. |
| `8.5:lem-radius-tails`, II:90729 | Incomplete, II:145593 | Source calls it a proved implication from (i)–(iv), II:90841–90843. The missing step is transfer of 109 (0.29) to a different fine-field domain, II:90834–90839, plus profile locality. |
| `8.5:prop-remainder-covariance`, II:94225 | Incomplete, II:145595–145596 | Its proof is conditional on explicitly incomplete hypotheses (b)–(d), II:94252–94261; it also imports room-witness conversion, II:94307. Keep those suppliers open instead of declaring an independent missing proof without reading them. |
| `8.6:lem-annealed-removal`, II:104598 | Incomplete, II:145599 | Printed proof II:104628–104761 assumes healed-islands-unread in (b),(c), II:104604–104610. Proved implication at that standing. |
| `8.21:lem-flat-shell`, II:145224 | Assembly says used, III:110951–110955 | Heading says “input of the alternative bookkeeping only.” It is outstanding, but a mandatory edge for the chosen witness route is not established. Keep an alternative edge. |
| `9.1:lem-glued-minimisers`, III:2166 | Incomplete, III:75864–75866 | A full conditional proof is printed, III:2307–2548, under the hypotheses starting III:2184. The listed stronger-regularity missing supplier needs reconciliation with that exact statement. |
| `9.2:lem-read-set`, III:30514 | Incomplete, III:75842–75843 | Prints proof III:30553–30603. Its distance properties are assumed at III:30518–30524; the “incomplete” phrase at III:30533 names response-factor, not read-set. |
| `9.2:rem-boundary-entry`, III:30961 | Incomplete, III:75844 | Conditional proof III:31113–31247. The missing response bound is explicit at III:31118; the R-born members are expressly outside the supplied weight at III:31030–31031,31134–31135. Do not silently extend its domain. |
| `9.9:rem-gaussian-skeleton`, III:58561 | Outstanding input, III:75876 | The source explicitly says none of its clauses is an input to the statements proved in that section, III:58568–58570. This is a proposed route toward the outstanding derivative bound. Exclude it as a mandatory source-confirmed dependency. |
| `9.13:lem-limit-member`, III:68855 | Outstanding, III:75894 | The later `9.13:thm-limit-member`, III:69553–69918, supplies a conditional theorem. They cannot simply be merged by their English titles. Compare clauses before counting the earlier lemma as a remaining blocker of the later result. |
| `9.5:prop-the-mixed-first-generation-bound`, III:37716 | Outstanding at source; omitted from the final list | Source calls it an input of (v), III:37725–37727. Assembly says mixed-size counting is proved, III:110978–110981. Resolve the replacement statement before treating it as either closed or an extra leaf. |
| `9.8:thm-two-blockings`, III:55354 | Assembly treats (v-f) as implication, III:111000–111005 | Parent statement is unwritten, III:55355. Its partial proof and the other (v-f) pieces require a source-level expansion; the assembly sentence cannot fill the missing statement. |

The account's count “24” at N=2 (III:111092–111096) counts intermediate programme statements. It expressly excludes further inputs (III:111118–111126). It is neither the number of open leaves nor the number of missing mathematical arguments. The index's 1,481 PROVED rows also do not supply either number.

## 5. Named hypotheses and prose entries still needing expansion

This table preserves the remaining entries of the requested lists instead of silently dropping ones without a numbered theorem. “List only” means source attribution has not yet been reconciled at its original statement. It is not a claim that the statement is absent from CA.

| Input | Source for standing/use | Reach | Mapping state |
|---|---|---|---|
| Volume counts in relative small-field machine | I:166652–166653; III:111217–111218: outstanding | J | List only; exact hypothesis/supplier still to locate |
| Two bounds on data entering chapter-5 lemmas | I:166654–166655; III:111219–111220: outstanding | J | One list item containing two bounds; do not pretend it is one atomic statement |
| Kernel-difference bound in the relative machine | I:166656–166657; III:111221–111222: outstanding | J | List only |
| Persistence of near-group weights, for one run and two runs | I:61307–61310: not proved | J | Explicit named hypothesis missing from the short list |
| Orbit data on stored analyticity domains | I:61309–61310: not proved | J | Explicit named hypothesis missing from the short list |
| Fine-field version of 109 (0.29) on the radius-tail domain | II:90834–90839: incomplete domain-transfer step | W | Explicit missing hypothesis (i) of radius tails |
| Source-carrying, unextracted terms have the remainder kind | II:94252–94255: incomplete | W | Explicit hypothesis (b) of remainder covariance |
| Running-coupling comparison in remainder covariance | II:94256–94258: incomplete as cited there | W | Supplier identity still to reconcile with the proved flow deductions |
| Extension proposition used by carry | III:24288,75836: incomplete | U | Original numbered statement not resolved |
| Nesting clause of history-wise modulus majorant | III:75848–75849; III:33549,33616 | U | Clause of `9.2:prop-modulus-majorant`, not automatically another independent theorem |
| One-run expansions on labels | III:75855,111453: incomplete; consumed at III:41361,41459 | U | Original statement still to locate |
| Residual clauses of increment statement | III:75856–75857,111267–111268: outstanding | U | Original statement still to locate |
| Difference of nested interrupted Gaussian integrations | III:75860–75863,111272–111276: outstanding; kept-factor bound depends on it | U | Original statement still to locate |
| Regrouped two-run identity at real centres for re-filed boundary terms | III:75879–75881,111288–111289: outstanding | U | Original statement still to locate |
| Own-history part of R-born boundary terms | III:75882–75885,111290–111292: outstanding; actual missing passage at III:61049 | U | Map the claim to the exact clauses of re-filed Lipschitz |
| Endpoint case of equal-coupling corollary | III:67866–67879,75893: outstanding | U | Separate endpoint assertion; interior bi-Lipschitz proof is not its proof |
| Unwritten two-blockings parent and incomplete flow-only increment bound | III:55355; `9.8:rem-increment-bound`, III:55571–55650 | Uf | (v-f) expansion needed; two facts missing at III:55650 |
| Positive reference normalisations and history-majorant sum | I:157069–157071, hypotheses (h6),(h8) of stability | J | Named hypotheses, not declared open here; precise suppliers not yet traced |
| Application membership for the operator theorem | I:49495–49546 | J | Explicitly outside the operator implication; map to actual stage suppliers |

Other incomplete source statements noticed in the index—`4.11:prop-straddling-clause` (I:40862), `4.11:prop-perturbative-clause` (I:42354), `4.36:prop-transport-every-l` (I:158518)—remain **membership questions**, not automatically new mandatory blockers. The account says the block-law branch has separate inputs and no clause uses it (III:111115–111117). A name match does not settle which branch consumes these statements.

## 6. Balaban input frontier

### 6.1 Printed sentences

Each row is one **sentence bundle as listed by CA**, not necessarily one independent mathematical lemma. “Printed” here reports CA's attribution; the cited Balaban passage was not independently checked in this mapping task. These are porting obligations, not proofs discharged by citation.

| # | Sentence bundle | CA standing/use lines | Reach |
|---|---|---|---|
| P01 | Prepared large-field data admitted; 122a pp.178–179 | I:45557; I:166579–166580; II:145579–145580; III:75801 | J |
| P02 | Transfer 109 §3, Lemmas 5–6, to 119's cube cover; 119 p.276 | I:166581–166583,166638–166640 | J |
| P03 | Two lowest tower regularity classes; 99b p.396, (3.35),(3.37) | I:166584–166585; III:111073–111079 says a conditional proof is supplied | J; replacement/supplier reconciliation needed |
| P04 | Locality of interaction terms; 122b p.379 | I:166586–166587 | J |
| P05 | Complex-pair inclusion; 109 (1.17) | I:166588–166589 | J |
| P06 | Block-averaged curvature estimates extended to near data; 109 p.277, (3.26)–(3.28) | I:166590–166592 | J |
| P07 | Inverse constrained covariance bounds and walks; 99b §3 before (3.132) | I:166593–166594; `4.5:prf-chart-linear-bounds`, I:14711 | J |
| P08 | Further operator walk expansions; 99b after Theorem 3.9 | I:166595–166596 | J |
| P09 | Analytic derivative bounds of averaging maps; 98 §E p.43 | I:166597–166598 | J |
| P10 | Second far-family current inequality; 99b (3.49),(3.69) | I:166599–166600 | J |
| P11 | Polymer-gas representation of bracket; 122b (1.90) | I:166601–166602 | J |
| P12 | Large-field bounds under remaining modifications; 122b p.386 | I:166603–166604 | J |
| P13 | Layerwise gauge clauses; 122a (1.64)–(1.69), pp.190–191 | I:166605–166606 | J |
| P14 | Layerwise ceiling as a small-coupling condition; 122a p.192 | I:166607–166608 | J |
| P15 | Bounds for old terms beside a new region; 122b p.375 | I:166609–166610; II:60275–60276; III:111308–111310 | J/S; also common order of choice, III:110863–110866 |
| P16 | Joined-domain convergence and analytic extension; 122a p.192 (1.70), 122b p.377 (1.68)–(1.69) | I:166611–166613; II:145585–145587; III:111358–111361 | J/W/U |
| P17 | Absolute boundary bound and gauge invariance; 122b (1.11),(1.23)–(1.48), p.369 | I:166641–166642 | J |
| P18 | Analytic solution of large-field equation; 122b p.367 (1.40)–(1.41) | I:166643–166644 | J |
| P19 | Small sum of localised remainders; 122b p.368 after (1.46)–(1.48) | II:60277–60280; III:111351–111353 | S |
| P20 | Flat step quadratic form equals free field's; 95 §1 | II:145581–145582 | W |
| P21 | Normalised island operation positivity and bound; 122b §1 | II:145583–145584 | W |
| P22 | Passage between response bounds (189),(190); 102b p.308 | `9.3:prop-second-variation`, III:35577; III:75781 | U |

### 6.2 Cited theorems and definitions: where bottom-up ports stop

The following are the account's **published-input lists**, with exact loci, not an appeal to the outline's list. A full expansion would split each multi-theorem entry into separate nodes and connect each use. That work is not replaced by assigning one count to each paper.

| Part of chain | Published theorem/definition frontier in CA |
|---|---|
| Joint (0)/(i) | 95 (1.118), 96 p.229 (2.36), Lemmas 2.1,2.4 and Propositions 2.6–2.7; 98 Propositions 1–7; 99a Lemma 1, Theorems 2,4, Proposition 6; 99b Theorems 3.1–3.4,3.7,3.9–3.15 and Corollaries 3.5,3.6,3.8; 102b Theorem 1 and Propositions 3,9; 109 Theorems 1,3 and Lemmas 4–6; 116 Lemmas 1–3; 122a Proposition 1; 122b Theorem 1 and Proposition 1. Exact CA entries I:166565–166578. Additional (i) entries: 99a (1.19), 109 (3.37)–(3.50), 119 Theorems 1,2 and Corollary 3, I:166628–166637. |
| (iii-a,c,d) | 98 Proposition 2 and displayed averaging identities; 99a (1.3)–(1.6); 99b Theorems 3.1–3.11,3.15 and listed propagator formulas; 102b Theorem 1, Proposition 9, §§F–G; 109 Lemma 4 and §§2–5; 116 Lemmas 1–3, localised-term and cluster formulas; 119 Theorem 1, Lemma 4, Corollary 3 and induction bounds; 122a cube and stage conditions; 122b localisation and large-field bounds and Theorem 1. Exact formula lists II:60239–60274. |
| (iii-b) | 109 (0.24)–(0.26); 116 (1.26); 119 (2.49),(2.50); 122b p.355 and (0.1), II:64593–64601. The p.355 dependence is part of the last-scale-constants assumption, not an independent proof of it. |
| (ii) | 109 (0.1),(0.2), II:68339–68344. No further Balaban theorem is cited by statement in either torus branch, II:68346–68347. Lattice positivity and analytic compactness inputs are still present. |
| (iv) | 95 free-propagator formulas; 96 Propositions 2.3,2.6,2.7; 98 (19),(20); 99b decay formulas; 102b Theorem 1, Proposition 9 and analytic-response formulas; 109 small-field step, effective action and coupling theorem; 116 Lemmas 2–3 and cluster bounds; 119 Theorem 2, Corollary 3, regularity, step and running-coupling formulas; 122a history/creation formulas; 122b localisation and region bounds. Exact enumeration II:145537–145578. |
| (v) and (ii-T-a) | 102b Theorem 1 and Propositions 3,5,6,9; 116 Lemma 3; 99b Theorems 3.1,3.4,3.12,3.13 and regularity/propagator formulas; 109 Lemma 4 and (3.15); 98 Propositions 1,2,4,5; 99a Lemma 1 and Propositions 3,5; 96 Lemma 2.1 and (2.60)–(2.61); 122a and 122b stage, remainder and localisation formulas; 119 induction bounds. Exact enumeration III:75776–75823. |

Non-Balaban citations must not disappear: chapter 5 uses Combes–Thomas in `5.2:lem-covariance-root` and Osterwalder–Seiler lattice positivity in `5.12:lem-limit-positivity` (II:60222–60225). Reconstruction names Osterwalder–Schrader (I:2696–2698). This note does not convert those citations into repository proofs.

## 7. Suggested order

### 7.1 Open work: widest established reach first

This is a priority order by the **established clause reach**, not an invented exact centrality ranking. Several entries tie. Source reconciliation precedes any proof attempt where §4 records a conflict.

1. **Common parameter and induction inputs (J, eight branch outputs).** First compare the same M-freeness statement at I:2239 and II:59574–59616. Then the minimiser/own-constant pair, I:45162–45226; the omitted local real base, I:8110–8373; the omitted uniform-increment lemma, I:16019, read by operator bounds at I:19783; and positivity dichotomy, I:156837. These all have actual missing-proof declarations and reach the common induction. The text does not establish an exact ordering among their downstream statement counts.
2. **Remaining J inputs and the printed J sentence bundles.** Follow the inside/outside re-blocking, live-region geometry, arrested-piece, dated-radius, near-pair and cell-counting branches in §3. Resolve the relative machine's named hypotheses at I:61304–61310 before treating “format propagation” as a leaf. This covers the shared obstruction to all the later clauses, III:111044–111052.
3. **Correlation polydisc and weighted inputs (S, six branch outputs).** `5.6:prop-polydisc-holomorphy` at II:46131–46185 is the direct missing supplier. Reconcile the two weight lemmas and their hypotheses; do not re-prove their conditional Cauchy arguments. Preserve P19's printed input, II:60277–60280.
4. **Volume-free constants (R), witness (W), uniqueness (U): separate branches.** Last-scale uniformity directly blocks the per-ball/R4 path (III:110895–110907). Witness inputs block (iv) and the added (v-f) branch (III:111000–111005). Uniqueness's own inputs block its tuned-family route, III:75770–75772. Each has reach two in the coarse accounting; no exact statement-count tie-break is established.
5. **Within W**, resolve the missing fine-field-domain bound of radius tails, II:90834–90843; the frozen-run identity, II:90196; profile locality and zero block mean, II:90607,91539; and the room/source/continuum-kernel chain, II:93196,145173,145220. Avoid spending on uniform-old-rarity, which this route excludes (III:110963–110965), or silently making the alternative flat-shell route mandatory (II:145224).
6. **Within U**, resolve the three floor definitions and the shell-response transfer first (III:7,120,213,37627). Then carry and its four missing members (III:25452–25453), the two-run kept-factor inputs (III:75858–75863), comparison-chain structure (III:51840–51940), and the re-filed induction/Lipschitz/geometric-envelope chain. Reconcile mixed-size counting and limit-member replacement before opening another proof lane (the conflicts are in §4).
7. **Offset-only and (v-f)-only additions** follow their actual consumers. The first-passage offsets lemma is not a prerequisite to mere subsequence existence (II:68351–68356). The unwritten two-blockings statement needs its own complete source map (III:55354–55356).

### 7.2 Proved material: bottom-up port order

This is an order of port entry points. All displayed hypotheses remain attached. A port of a complete implication does not close its open antecedents.

1. **Finite-dimensional definitions and arithmetic.** Wilson action/invariance, `1.1:lem-invariance` (statement I:559–566; proof I:568–604); first-passage arithmetic, `4.2:lem-first-passage` (I:3636–3721); flow arithmetic, `4.19:lem-flow-bounds` (I:56342). These precede applying the construction's flow conclusion.
2. **Geometry and finite polymer combinatorics.** `4.6:lem-tree-cubes` (I:21544–21641) from its definitions; the polymer counting/tree majorants leading to `4.6:prop-logarithm-convergence` (I:22645–22858). Port the conditional polymer-gas representation separately, I:20757–20927, retaining its printed locality hypothesis at I:20767. Do not call that entire cluster chain a definition-only leaf.
3. **Free-field algebra.** `8.1:lem-gaussian-squares` (II:69457–69496), `8.1:lem-free-curvature-covariance` (II:69516–69598), then `8.1:lem-kernel-positivity` (II:69682–69837). Kernel bounds (II:69925–70152) follow with their displayed linear-minimiser hypotheses; running normalisation (II:70501–70584) follows the correlation theorem, not before it.
4. **Published operator and minimiser ports.** Rebuild the cited theorem instances in §6.2 with their stated hypotheses; preserve the separate printed-sentence obligations in §6.1. Then port the account's complete chart/operator implications (A4,A9) and localised-independence implication (A3), retaining the local-real-base and uniform-increment leaves.
5. **Hereditary and level-induction deductions.** Once their precise assumptions are in place, port the account's conditional A5–A6, preparatory-boundary A10, A12–A15 and representation/stability A17–A20. This is a level-by-level order, not a topological ordering of two cyclic-looking whole-theorem labels (I:166702–166709).
6. **Source/weight deductions and correlation assembly.** Port the pointed irrelevance deduction `5.2:lem-pointed-irrelevance` (II:4852–5029) on its own admitted E-family domain (II:4853–4856). Then the complete weight deductions with their missing hypotheses explicit, the sourced step/running-flow deductions, correlation theorem and one-loop law (B2–B4). This does not replace the outstanding polydisc proposition.
7. **Positivity and compactness.** Lattice positivity `6.1:lem-reflection-positivity` (II:60440–60624) can be ported independently. Then the per-ball implication B7 at the standing of B6; the torus subsequence/positivity deductions B8; the finite-cutoff transport lemmas B10; and B11–B13 in order. No step here grants stronger reconstruction than I:2698–2711.
8. **Witness deductions.** Port Gaussian extraction and the proved consequences of its explicit hypotheses, the healed/age deductions, torus witness, and volume transfer; only then assemble the witness and its limit consequences (C5–C11; III:110922–110961). Keep the unwritten continuum-kernel statement visible.
9. **Uniqueness deductions.** Port the complete strip/counting/comparison implications only after their actual inputs are identified; then the core uniqueness deduction and the tuned family. Re-filed exponential convergence needs D9–D10's open inputs. Defect summability and the interior bi-Lipschitz/equal-limit deductions (D11) follow the tuned family. Change of units precedes re-rooting/depth convergence and the later limit-member theorem (D12). The (v-f) and short-distance additions follow both core uniqueness and the witness (D13–D14).

No proof was written or re-derived in this lane. This order says what to port, and what must remain a named input during that port.

## 8. Recovery checkpoint

Only `library/chain-ca.md` is changed. No editable prompt, GOAL, FINISH, skill, audit or platform instruction was modified. The raw source files have these SHA-256 identities:

| Source | Lines | SHA-256 |
|---|---:|---|
| SA outline | 32,992 | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| CA-I | 166,711 | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| CA-II | 145,624 | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| CA-III | 111,583 | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

SA and CA-I were fetched once in this session from the requested pinned URLs. CA-II and CA-III were already present and were reused as instructed; their remote identity was not independently re-fetched. Their line anchors match the repository index and the cited passages. Hashes identify the actual bytes used; they are not a proof of remote provenance.

Scratch evidence and the structural locator are in `/tmp/chain-ca-work/`. `nodes.json` is a **candidate reference index**, not a dependency graph: references in proof headings and statements of an output create false edges. `final-frontier.json` records the §3 row inventory. These scratch files are not repository proofs or committed artifacts.

**Next work to complete CHAIN:** expand the named antecedents of A17/B3/D8 and the remaining prose items in §5; reconcile §4 at the actual use sites; split the cited theorem bundles into individual statements; classify every edge as a hypothesis, a proof input, a definition, a previous-level input, an alternative, or a non-input. Only then compute transitive downstream statement counts and a genuine bottom-up statement order. Do not use the raw reference graph for those counts. Preserve the negative scope statements and alternative routes already identified above.

## Result

**Research dependency map, incomplete as an exhaustive statement-level census. No proof or status is granted.**

- **58 main-chain table rows:** 20 for flow/UV, 13 for correlations/limits, 11 for the witness, 14 for uniqueness. Some rows group several statements; these are not 58 atomic theorem nodes.
- **82 source-declaration rows** in §3: 50 incomplete, 27 outstanding, 3 unwritten/incomplete, and 2 unwritten. M-freeness's two locations count once. These are confirmed missing-proof declarations, not an exhaustive or irredundant leaf count.
- Their coarse attribution is **35 J, 1 S, 1 R, 1 Ta, 14 W, 29 U, 1 Uf**. Branch counts are explicitly defined in §3; they are **not** counts of all downstream intermediate statements.
- **22 printed-sentence bundles** in §6.1; **19 unresolved hypothesis/prose rows** in §5; **21 source/list reconciliation rows** in §4. These sets overlap and must not be added to obtain an open-statement total.
- **Zero verified uses of model theorems outside their models** identified here. The model branch and uniform-old-rarity are not inserted into the mandatory witness chain.
- **Two additional N≥3 programme-level inputs** to (0)/(i) are identified at III:111133–111140 but not expanded into a full frontier; they are not included in the 82 SU(2) rows.
- **Exact open-chain total, exact downstream statement counts, and a complete statement-by-statement port order remain unresolved.** The account's “24” and the index's PROVED total do not provide them. The source-confirmed omissions and conflicts above prevent honestly reporting those numbers from the lists alone.
