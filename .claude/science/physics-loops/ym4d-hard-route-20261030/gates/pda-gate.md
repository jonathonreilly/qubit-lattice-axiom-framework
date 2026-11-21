# PDA gate: referee check of library/pda.md (prepared-data admissibility, geometric (A1))

First failing step: none

Text checked: `library/pda.md` (237 lines). Source: local `ca_I.tex`, SHA-256 `4cb5cb5e…6e93`, and `ym4.tex` (SA), SHA-256 `d7f77d4d…4b6f`. Both match the hashes in pda.md L9–10. CMP 122a was not available. I worked from the account's quotations and definitions. Also read: `port/p4-operator.md` L561–575 (P4-H-prepared) and `gates/p4-operator-gate.md` L155–168.

## (1) Statement against the source

- CA-I 45593–45595, the last sentence: "For the nest of the prepared large-field data … condition (A1) holds." (A1) at 45582–45588 has four parts: the nesting; the gap ℓ_j^{-1} dist_∞(Ω_j^c, Ω_{j+1}) ≥ M for 1 ≤ j ≤ k−1; closed level-j M-cubes from compatible L-adic partitions; and Ω_0 equal to the Dirichlet hull of Ω_1. PDA's display (PDA), L12–17, states the same: M ℓ_j = m_j, with the same index range. Right.
- (A2), 45589–45591 (Ω_t ⊂ Ω_k, 6M margin, LM-cubes), is not in the last sentence. 45622–45624 says so, and the operator theorem assumes (A1) and (A2) at 46044–46046. PDA L18 and L202 keep (A2) and `4.14:rem-supply-scope` (label at 49495) separate. Right.
- What of the sentence remains: nothing of its geometric content. Not supplied by PDA: (A2) for Ω_t, and the analytic supply conditions.
- Input made explicit: PDA L55 uses (A1) for the old label in force as an inductive premise (§4, first case). The proposition's sentence leaves this implicit. The account supplies it only through Balaban's representation as a sum over admissible sequences (4224–4226) and through an unlabelled "admissibility lemma for the produced nests" (45626–45628). PDA proves one operation step: (A1) in gives (A1) out. This is the honest form of the claim. It is not a new hypothesis about the prepared nest.

## (2) Rule (C)

- The account leaves the intermediate members to be chosen. The Balaban quotation at 45608–45611 reads "complete these two sets … in such a way that the complements … form an admissible sequence … based on partitions into M-cubes". The account's restatements give the constraints: members are unions of level-i M-cubes, nested, and adjacent members are "separated by one layer" (51713–51716, 53779–53782, 121772–121777). (C) satisfies each constraint. Within X, Ω''_i = X \ Z''_i (48780). Right.
- Endpoints: D_k = X \ Ω_s^{(+5M)}. This is 48783, and 53782 with Ω^{∼5}_s = Ω_s^{(+5σ_s)} and σ_s = M (48164–48165, 48192). D_s = X \ Ω_s^{(+7M)} is the quoted (1.10) at 92015. PDA L39 notes correctly that 51712 says "Z''_k and Z''_{k−1}", against 45600 and the quotation at 92015. PDA follows the quoted formula. The two readings agree when N_0 = 2.
- "At least one layer" (PDA L51) is the only reading that can hold. Steps of exactly one layer m_i from level s+1 to level k add up to less than ML/(L−1) ≤ 8M/7. That is less than the prescribed 7M − 5M = 2M between the endpoints, so "exactly one layer" fails in general. (C) gives exactly m_{i+1} for s < i < k. At the junction (s, s+1) it gives ≥ m_{s+1}: 2M when s = k−1. The consumers of (A1) need only lower bounds. So (C) is a choice the account allows, not a new hypothesis.

## (3) Steps

- Inputs, L34–43, L82–90 (S): s = ∗ = k − N_0 + 1. Then σ_s = M (48192), σ_j ≤ M for j ≤ s (48194), σ is non-decreasing (48196), h < s − 1 (48201), s ≤ k − 1 (48195), and σ_k = MR_k ≥ LM (48191). R_j ≥ 1 is a non-negative power of L (45845). h ≥ 1 follows from k > N_k (45848). L ≥ 3, odd, ≥ 8 (45681). Right.
- X is a connected component of Z_k (45987). Right.
- T8, L57–62: in `4.4:lem-collar-avoidance`(b), 12215–12225 gives Ω_{j+1}^c ⊃ Z'^{∼8}_j ⊃ Z_j in LMR_{j+1}-cubes of the level-j scale, whose side is σ_{j+1}. Only the (3.5) chain is used. Part (a), which needs the coupling ceiling, is not used. 91991–91997 gives the same 8 at j = h, counted as 4+1+1+2. Right.
- T10, L63–67: 53823 with t = k. 50342 (Z[R] = (Ω_t^c)^{∼2} ∪ R^∼) supports "8 + 2 = 10". The proof that distinct components are at least σ_k apart is right (index gap ≥ 2 in some coordinate). It agrees with 48169–48172 and 48848.
- §1 (B): for i < k, Ω_i^c ⊂ Λ_{k−1}^c = Z_{k−1}. The open 10σ_k-ball about a point of the closure lies in Z_k, is connected and contains the point, so it lies in X. Right. T8 then extends to all of Ω_{i+1}, because 10σ_k ≥ 8σ_{i+1}. Right.
- §1, erosion identity: let x ∈ E_i and r < 10σ_k. Every point within r of x is in X. So dist(x, E_i^c) ≤ r if and only if dist(x, Ω_i) ≤ r, which gives X \ Ω_i^{(+r)} = the r-erosion of E_i. E_i^c (regularised) is a union of σ_i-cubes, since X is σ_k-aligned and σ_k/σ_i is a power of L. By 48162, the enlargement and complement stay in the grid. Right.
- §2, grid: a_i is a multiple of m_{i+1} for s < i < k, because m_r/m_{i+1} = L^{r−i−1} and 5M = L^{k−i−1} m_{i+1}. Also 5M and 7M are multiples of every m_i. So D_i is a union of m_i-cubes, and D_{i−1} is a union of m_i-cubes (this matches 121772–121777). Right.
- U1/U2: a_i − a_{i+1} = m_{i+1}. For s = k−1 the gap is 2M ≥ m_k. Otherwise it is 2M − Σ_{r=s+2}^{k} m_r ≥ 2M − LM/(L−1) = M(L−2)/(L−1) ≥ M/2 ≥ m_{s+1}, since s+1 ≤ k−1. I checked this arithmetic. Right.
- U3: the 1-Lipschitz bound on distance to Ω_s gives |x−y| ≥ a_i − a_{i+1}. Nesting D_i ⊂ D_{i+1} follows. The empty-set cases are handled. Right. D_i ⊂ Ω_s^c ∩ X ⊂ Ω_i^c ∩ X for i ≥ s. Right.
- §3, L1: x ∈ Z_i ∩ X (D_i ⊂ Ω_i^c ⊂ Λ_i^c = Z_i). y is within 5σ_{i+1} of some z ∈ Ω_{i+1}, and z may lie outside X. The full-Ω_{i+1} form of T8 from §1 covers that case. The gap is 3σ_{i+1} ≥ m_{i+1}. Right. At i = h, x ∈ Ω_h^c ∩ X ⊂ Z_h, with no alignment used. Right.
- §3, L2: 8M − 7M = M ≥ m_s ≥ m_{s−1}. This is tight but valid. It uses only the prescribed 7M endpoint. Right. Z_h ∩ X ⊂ D_{h+1} agrees with 53795.
- §4, gluing: the three cases are exhaustive. (i) y ∈ Ω_{i+1}: old (A1). (ii) y new in X and x ∈ X: L1, L2 or U3. (iii) x ∉ X: x ∈ Ω_i^c ⊂ Z_i ⊂ Z_k, in another component of Z_k, at distance σ_k ≥ M ≥ m_i. G1 holds globally. The m_i-grid compatibility follows from old (A1) and σ_k/m_i = R_k L^{k−i}. Nesting follows from the positive gap. Right.
- §4, hull: h ≥ 1 gives Ω''_1 = Ω_1. Ω_0 is, by the proposition's own definition, the Dirichlet hull of Ω''_1. Right.
- §5, prefixes: at i = p(X), y ∈ Ω_{p+1} falls under case (i). G1 holds for every prefix assignment. This matches the "every assignment of states" use at 48843–48846 and the stage nest at 48510–48523 and 48766. Right.

## (4) Quotations and citations

- Every CA-I range that PDA cites was opened and checked against what PDA says it shows. These are: 45557–45634, 45228–45234 (the Route belongs to `4.13:lem-own-constant`, label 45204), 45236–45294, 45669–45687, 45803–45863 (order (O) is the same as 45809–45810; 45853 says no operation where the regime fails), 45962–46034, 48141–48261, 48774–48800, 51707–51728, 53737–53839, 91991–92022, 12103–12257, 50316–50350 and 121760–121790. No misquotation found.
- The CA-I and SA hashes match. SA 17398 and 17575 are the outline's geometry and its "where it acts" rule, as PDA says. No premise is drawn from them.
- The use ledger, L210–225, is complete for CA-I. All 24 occurrence lines of the label and of `eq-prepared-data-admissible-a` outside 45557–45634 lie in the listed ranges: 46046, 46245–46246, 46480, 46846–46847, 47256–47257, 47617–47618, 47639, 47746–47747, 48001, 48046, 48133, 48339, 48523, 48766, 48844, 52560, 52677, 52807, 53061. I spot-read 46242–46263, 46476–46482, 47636–47648, 47742–47750, 47997–48003, 48043–48048, 48128–48134, 48336–48345, 48505–48523, 48757–48770, 48838–48863, 52556–52564 and 53058–53062. Each reads only what PDA's table says.
- The ledger is incomplete outside CA-I. It is true that the exact label has no occurrence in CA-II or CA-III (grep confirmed). But the phrase "admissibility of the prepared large-field data, pp. 178–179" is cited by name at CA-II 145579 and at CA-III 21303, 53328, 111073 and 111311. CA-III 21303 reads constant conditions of 122a through it (β ≤ 1/4, ℓ_∘² ≤ L/3, L ≥ 3; display 9.1:eq-integer-floors-1). CA-III 53328 reads a point-count bound, #Y ≤ M⁴C_d(d(Y)+1). Neither is (A1) content. PDA does not prove either, and it does not claim to. Its sentence "Exact-label searches … returned no occurrences" is accurate but is not a survey of uses.
- Minor: L62 counts the eight layers as 5+3, as 12215–12225 does. 91992 counts them as 4+1+1+2. The total is the same, so this is not an error.

## Inherited inputs (account statements, not PDA hypotheses)

PDA's proof is complete relative to these account statements. Several of them the account itself takes from Balaban rather than proves:
(a) for i > h, Z_i inside X is produced by T-steps and is cell-made, with the margin T10 (53816–53831). This rests on the account's reading of class condition (ii).
(b) the Ω_j^{∼n} inside X are σ_j-aligned (48164–48168, 92012).
(c) the endpoint Z''_s = (Ω_s^{∼7})^c ∩ Z, from the 92015 quotation of (1.10). 51712 says otherwise.
(d) old (A1) for the label in force (4224–4226, 45626–45628).
T8 is proved in the account (12215–12225), from (3.5) as quoted.

## Verdict

**Proved as stated.** PDA proves the geometric content (A1) of the last sentence of `4.14:prop-prepared-data-admissible`, with intermediate sets chosen by rule (C). This includes the componentwise stopped prefixes used at 48507–48523, 48766 and 48843. It is proved as one operation step: (A1) for the old label gives (A1) for Ω''. (C) is a choice the account allows, and the "at least one layer" reading is forced. No fabricated step was found.

**What P4-H-prepared still needs:**
1. (A2): Ω_t ⊂ Ω''_k, dist_∞(Ω_t, (Ω''_k)^c) ≥ 6M, and Ω_t a union of level-k LM-cubes. PDA does not touch it.
2. (A1) at every other nest of the history (48133: "at every nest of Ba{\l}aban's history"). This needs the T-step half of the produced-nests induction and the old-label premise above. PDA supplies only the large-field-operation half.
3. The inherited account inputs (a)–(c) above, if a check against CMP 119/122a themselves is wanted.
4. The analytic supply conditions of `4.14:rem-supply-scope` (49495–49546). These stay separate.

The CA-III by-name readings of pp. 178–179 (constant conditions, point-count bound) are outside (A1) and stay printed inputs. P4-H-prepared can now be narrowed: its (A1) half for the prepared nest is supplied by PDA, given old (A1). Its (A2) half is unchanged.

Checked line by line by Claude (fresh session).
