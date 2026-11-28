lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T13:07Z

# b98-gate: line-by-line check of library/b98.md (FINISH row 374)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, commit 392550b85. One reading by one other model; not an audit, not human review. Kind of result: check of our own rebuild (Codex gpt-6-astra) of cited statements of the complete account of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), which credits Tadeusz Balaban (CMP 98, CMP 99a, CMP 109).

Sources read: CA-I and CA-II fetched at `31a47c543775` into a scratch folder (SHA-256 equal to b98 §5), CA-III fetched for uses; Balaban CMP 98 and CMP 99a OCR, and CMP 98 journal pages 23-26, 30-31, 34, 36-37 rendered from the PDF in `~/ym4d-papers` (b98 had no PDF; "p." below means journal page); CMP 109 OCR 170-280; frozen `library/cp12.md` §4 (Lemma 5 (9)-(10), Lemma 6, Theorem 7) as an input. No numerical step was used.

**First failing step: b98.md L300 (Lemma 5, application paragraph).** It says that (8) with n = η^{-1} "is (B3), including the account's symmetric map". In the account, the average in (B3) is the k_o-fold iterate of the one-step map, not one step with block side n. Every other step was redone and holds.

## Verdicts

| Lemma | Verdict | Note |
|---|---|---|
| 1 matrix calculus | ADVANCE | (1)-(4) redone; multinomial majorant, Duhamel coefficients, g^{-1}(-z)e^z = g^{-1}(z) |
| 2 plain average | ADVANCE | (5) equals CMP 98 (42) on the PDF (p. 23); covariance and B^q support redone |
| 3 axial gauge | ADVANCE | swap count (d-1)D/h, unitary telescoping |
| 4 first-order averaging | ADVANCE | one step, block side n; CMP 109 (0.11)-(0.12) read on OCR 190-206, 248-262: G(y,x) is the family of all coordinate-permutation contours, so the connector is direction-free |
| 5 signed plaquette average | **REVISE** | (8), (9), (10), (B1)-(B2) hold for one step. Coverage of target B fails (finding 1). Repair proved in `library/b98-iterate.md` |
| 6 normalized relative gauge | ADVANCE | matches CMP 98 (60)-(63) and CA-I (a) |
| 7 tower recursion | ADVANCE | (12) equals CMP 98 (85) on the PDF (p. 31), with the anchored mean (78); (13)-(15) redone |
| 8 five-term derivative | ADVANCE | (16)-(18) redone from (5) with left perturbations; all five coefficients and signs equal CMP 98 (124) (PDF p. 36) and CA-I 24356-24378; (19) by the chain rule; C_1 = C_1(d), c_3(d,L) as in CMP 98 Proposition 3 |
| 9 bounded-curl primitive | ADVANCE | Hodge identity and (21) redone; uses cp12 (9) at mu = 1, h ≤ 1 |
| 10 massive gauge | ADVANCE | (23)-(28) redone, including r(q;0,w) = 0, the curl product rule (27) and the h-cancellation in dE |
| 11 current and bootstrap | ADVANCE | (31) checked against CMP 99a (1.1)-(1.2): D* carries 1/eta and acts on U(dp) itself; (32)-(34) and the absorption redone |
| 12 one gauge for all cubes | ADVANCE | (36)-(43) redone; collar (39), scaling by sigma, cutoff, composition; U_0' is a gauge transform of U_0 (CMP 99a OCR 1306-1312) |

Target A (CA-I 4.6:lem-averaging-locality): proved, all clauses (a)-(d). Target B (CA-II 8.11:lem-signed-averaging): (B1)-(B2) proved; (B3) proved for one averaging step only, and with the repair for the iterate the account uses. Target C (CA-I 4.9:prop-cube-gauge-regular): proved for k ≥ 1; the consumer also needs k = 0 (finding 2, elementary).

## Findings

**1. Target B, as the account uses it, needs the iterated average (breaks the coverage claim; repaired).** The only consumer is CA-II 8.11:lem-weighted-flux (about L123076-123216), feeding 8.11:thm-deep-curvature-blocks (c). It puts "V := \bar U^{k_o}(U), the top block average of U", takes the block side n and blocks of the signed lemma, and applies (B3) with "\bar U(∂P) = V(∂P)". So \bar U is M^{k_o}, the composition of k_o one-step maps of CA-I Definition 1.5 (block side L each), with n = L^{k_o} = η^{-1}. The threshold c_2 named in (B3) is CMP 98 Proposition 2's (p. 26), which is the iterated estimate. CMP 98 (45)-(49) are one-step relations with block side L (pp. 24-25); the account rewrites them with n in place of L. b98 Lemmas 4-5 treat one step with block side n. For k_o ≥ 2 the iterate is a different map, and a one-step bound does not give it: the nonlinear errors of the k_o steps must be summed. Iterating the one-step lemma level by level with sup-norm bounds on links does not give it either, because that gains a factor (d+1) per level. **Repair (proved here, not yet checked by the other model):** `library/b98-iterate.md`, Lemma I. It works in one fine axial gauge on Δ(P), proves the exact structure of the composed linear map (composite connectors of length at most dL^m/2), and sums the one-step errors of Lemma 4 through it. Result: ‖(M^kU^loc)(∂P) − 1 − i n^{-d}ΣΣΦ^loc(p)‖ ≤ C(d)α² for α = n²f ≤ c(d,L,N), uniformly in k. This gives (B3) for M^{k_o} with C_0'' depending on d only. A change-of-gauge clause transfers it to Balaban's (45)-(46) axial gauge, which the consumer uses.

**2. Target C at k = 0 (minor; consumer reads it).** b98 Lemma 12 assumes k ≥ 1. The consumer CA-I 4.9:lem-seed-cube-gauge (L36382) allows j ≥ 0 and applies the proposition with k := j. Balaban also admits k = 0 (CMP 99a OCR 1283-1287). At k = 0 the construction of the enclosing cube differs: □_0 = □ + r is already a union of grid cubes. **Repair (elementary; `library/b98-iterate.md` Lemma C0, not checked by the other model):** for k = 0 use the tree gauge of Lemma 3 on Q = □ + 3r with the level-0 bounds |U_0(∂p) − 1| < α_0 (h = 1). The consumer's Reg_0 on 𝒩(□^a) = □^a + 4r supplies them. Then |A_0| < 9(d−1)M*α_0 < s, and the direct differences of (40) give |∇A_0| ≤ 2s, |ΔA_0| ≤ 4ds, |∂*∂A_0| ≤ 8ds on □_0, with stencils inside Q. Take λ = 0 and u^{-1} = a v^{-1}; B_1 > 8d is already part of B_1 > C_*.

**3. Hypothesis form in (C2) (no defect).** b98 takes \widetilde□ ⊂ Ω_{k−1} as a hypothesis. The account derives it from L^{-1}RM* > 2dR_1M_1 and CMP 99a (1.3)-(1.4), and b98 does not rebuild that step. The consumer builds the nest so that \widetilde□ = Ω_k ⊂ Ω_{k−1} by construction (CA-I 36415-36475), so nothing on the chain needs it.

**4. Constants B_1, c_1 (no defect, bookkeeping).** b98's B_1, c_1 are its own existential constants (B_1 > C_*(d,L)), not Balaban's Theorem 4 values. Every consumer floor that reads B_1 (CA-I 4.9:prop-real-backgrounds: B_12 ≥ 14dL²B_1, B ≥ 14dL^5B_1; 4.9:lem-thin-cube-gradient (φ-B)) is chosen after B_1, so the order of constants has no cycle. The consumer only reads "B_1, c_1 depend on d and L only", which b98 supplies.

## Uses in their account that need clauses b98 does not prove

- Target A. Uses at CA-I 25211, 26792, 26923, 26988, 27264, 27591, 28034 read block-locality, freedom from domains, and the "residual reading" that the operator brackets in (d) are block-local. b98 (c) and Lemmas 2, 6, 7 supply these (Y_x reads V_0 on the double block only). CA-I 47091 and 47207 cite CMP 98 Propositions 3 and 6 at other backgrounds; Proposition 6 (164) is not in b98's scope. No use reads more of target A.
- Target B. 8.11:lem-weighted-flux needs the iterate: finding 1, repaired. (B1)-(B2) (used at CA-II 123129) are proved.
- Target C. Every use goes through 4.9:lem-seed-cube-gauge: CA-I 36401-36500, 36509 (36257 is a remark); 4.9:prop-real-backgrounds (b) and (amb); 4.9:lem-thin-cube-gradient (a) at 37906-38044, "second and third clauses". The lemma reads (C4), "U_0' is a gauge transform of U_0", and the first two bounds of (C5) at j = k on □_k. b98 proves all four bounds on □_0 ⊃ □_k. No use reads Balaban's (1.137)-(1.138) (site average and R∂*A = 0); CA-I 11638-11701 is a remark, not a step. The only gap is k = 0 (finding 2).

## Result

Ten lemmas ADVANCE as written; Lemma 12 ADVANCE for k ≥ 1; Lemma 5 REVISE. Targets A and C (k ≥ 1) are proved as the account states them, by the hand proofs in b98. Target B's (B3) is proved for one averaging step only. The account's use needs the k_o-fold iterate, which `library/b98-iterate.md` Lemma I now proves (Claude, not yet checked by the other model). The k = 0 case of target C is `library/b98-iterate.md` Lemma C0 (elementary, not yet checked by the other model). With these two, all three targets cover every use in the account. Open: one other-provider check of `library/b98-iterate.md` (Lemmas I0, I, C0). CMP 98 Proposition 6 (164) and Balaban's (1.137)-(1.138) stay outside b98's scope, and no consumer of these three targets reads them.

Checked line by line by Claude (Mini worker).
