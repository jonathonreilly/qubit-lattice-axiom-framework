lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T14:34Z

# uses-pda-um: do library/pda.md and library/um.md cover the uses listed in library/uses-old.md §§3–4?

Queue row 371. Commit 02f31fdc9. Claude Opus 5.5, max effort, Mac mini worker, fresh session. One reading, not an audit. Checked line by line by Claude (Mini worker).

Moves: the two old-input rows of `library/uses-old.md` for CA-I `4.14:prop-prepared-data-admissible` and `4.2:lem-unmarked`. If a use is covered, that input can be cited at the use with no new lane. If it is not covered, the row names the weakest statement still owed.

Kind of result (FINISH item 9): a check of our ports against their consumers in the account. No new proof. Sources: CA-I, CA-II, CA-III at `31a47c543775`, fetched by URL into a scratch folder. The CA-I SHA-256 is `4cb5cb5e…6e93`, the same as in `pda.md`.

Credit: the lemmas, their uses and the proof mechanisms are from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The constructions are Tadeusz Balaban's. `pda.md` and `um.md` are Codex's. `pda.md` was checked once by Claude (`gates/pda-gate.md`, first failing step none). `um.md` has not yet been checked by another model; its check is queue row 338 (`um-gate`).

## Method

For each row of `uses-old.md` §3 and §4, I read the cited lines in the source. I wrote down what the use reads: which clause, at which nest or level, at which radius and domain, and which constants in which place of the order of choice. I compared that with the Result of `pda.md` or `um.md`. Verdicts: **covered**, **covered after a stated ceiling**, or **not covered** (with the reason and the weakest statement the use needs). I did not re-check the internal proof of `pda.md`; its gate did that. For `um.md`, which is not yet checked, I read the parts of its proof that fix the constants and their order, because the uses read those. Its full line-by-line check stays with row 338.

## 1. Uses of `4.14:prop-prepared-data-admissible` against `library/pda.md`

**What `pda.md` supplies.** This is one large-field operation at level k. Its input is (A1) for the nest before the operation (the old label), with the account's one-step geometry (T8, T10, cell alignment) and the endpoints (E). The intermediate sets are chosen by rule (C). Then the prepared nest Ω''₁, …, Ω''_k with its Dirichlet hull satisfies (A1) with gap Mℓ_i. An inherited gap LMℓ_i is kept. (A1) also holds for every componentwise stopped prefix: the stage nests and the global componentwise nest (§5). The proof also gives these facts, which some uses read:
- Ω_i ⊂ Ω''_i (G1).
- Ω''_i = Ω_i for i ≤ h and off the operated components.
- D_i ⊂ D_{i+1}, and Z_h ∩ X ⊂ D_{h+1}.
- For every i > h, D_i is a union of level-i M-cubes.
- Γ''_i = D_{i+1} ∖ D_i has width exactly m_{i+1} for s < i < k (U1), and width at least (L−2)/(L−1)·M ≥ m_{s+1} at i = s (U2).

**What it does not supply.** It does not supply (A2). It does not supply (A1) at a nest that is not the output of a large-field operation; this includes its own old-label premise. It supplies no analytic statement.

| CA lines | Use | What the use reads | Verdict |
|---|---|---|---|
| I 45628–45634 | unlabelled, after the proposition | "the admissibility lemma for the produced nests": (A1) and (A2) at every nest made by T-steps and operations, with gap LMℓ_j | **covered** for the operation step, (A1) only, with the LM gap kept when the old nest has it (`pda.md` §4, last paragraph). **Not covered**: (A2), the T-step half, and the LM gap at the new T junction (N1, N2). CA-I has no labelled lemma of this name; only 45628 and 48522 refer to it |
| I 46045–46046 | `4.14:thm-operator-theorem`, hypothesis | (A1) and (A2) for the nest {Ω_j}_{j≤k} and Ω_t | (A1) **covered** at a prepared or stage nest, given old (A1). (A2) **not covered** (N1) |
| I 46244–46260 | `4.14:lem-reading-hulls` | nesting, and the gap Mℓ_i with the floor M ≥ 13L²M₁♯. (A2) is listed, but the proof reads only (A1) | **covered**, same scope as 46045 |
| I 46478–46481 | remark "No reading hull in the unit frame" | (A2): □̂ ⊂ Ω_k | **not covered** (N1) |
| I 46841–46850 | `4.14:lem-local-balls` | a layer crossing costs weighted length ≥ M > M/2L; level-n M-cubes with faces on compatible grids | **covered**, same scope |
| I 47253–47260 | `4.14:prf-form-walk-expansion`, hypotheses | (A1) and (A2), as the operator theorem's hypotheses | (A1) **covered**; (A2) **not covered** |
| I 47616–47623, 47637–47648 | same, step (vii) and "Hypotheses used" | (A1) read as CMP 96 (2.1)–(2.2) at (M/LM₁, M₁) and (M/LM₁♯, M₁♯), as CMP 96 Lemma 2.1 with M/L, and as (Sc) with (fl-M)′(i); (A1) and (A2) at Λ = Ω_t^(k) in the coercivity proposition | (A1) parts **covered**: each reads M-cube unions and the gap at size M/L or M. The step from (A1) to the CMP 96 form is the account's, not `pda.md`'s. (A2) at Ω_t^(k): **not covered** |
| I 47745–47751, 47869–47875 | `4.14:prf-positivity-inversion` | (A2): the 6M margin puts b^{+ℓ} and a side-M cube Q inside Ω_k, property (b4); then (b1)–(b4) again in the inversion | **not covered** (N1) |
| I 47998–48001 | `4.14:prf-block-identities`, (E)–(G) | (A2): collar cubes within 3M of a core are level-k M-cubes of one aligned partition | **not covered** (N1) |
| I 48042–48050 | same, (H) | crossing cost ≥ M and aligned grids, through local balls | **covered**, same scope |
| I 48132–48138 | same, conclusion | (A1) and (A2) "at every nest of Ba{\l}aban's history" | **not covered** as stated. Covered part: (A1) at every prepared and stage nest, given (A1) before each operation. Missing: (A2) at every step, and (A1) at the nests that T-steps make (N1, N2) |
| I 48337–48344, 48373 | `4.14:lem-hull-cube` | (A1) for the hatted nest: nesting, closed level-i M-cube unions from one compatible family, gap Mℓ_i | **covered** for stage and componentwise nests (`pda.md` §5). For "the old structure, made by T or by earlier fills" (48861) it reads old (A1) (N2) |
| I 48520–48525 | `4.14:lem-gauge-family` (b) | (A1) for the stage nest N^(n) (Ω''_i for i ≤ p, Ω_i above), for every assignment of states | **covered** (`pda.md` §5; the stage nest is the assignment with every p(X′) = p), given old (A1) |
| I 48764–48770, 48843–48847, 48862 | `4.14:rem-tiling-later-steps` (4) | (A1) for the global componentwise nest (Ω''_i on X′ for h < i ≤ p(X′), Ω_i elsewhere); part (a) on the old structure | the componentwise nest is **covered** (`pda.md` §5). Part (a) off 𝖹 reads old (A1) (N2). The component gap MR_k ≥ 3M it uses is the account's own, the same fact as `pda.md`'s T10 |
| I 52560–52566 | `4.16:def-cube-class` (c) | Ω₁ is a closed finite union of level-1 M-cubes | **covered**. The operation leaves Ω₁ unchanged (h ≥ 1), so this is the old premise at level 1 |
| I 52676–52679 | `4.16:prop-lowest-level-regularity`, hypothesis | (A1) for the operator theorem's nest | **covered**, same scope as 46045 |
| I 52806–52813 | same, Fact (i) | each shell X_j (j ≥ 1) is a union of level-j M-cubes; X₀ is a union of level-0 LM-cubes | **covered**: Ω''_{j+1} is a union of level-(j+1) M-cubes, each a union of level-j M-cubes of the compatible family (`pda.md` §4) |
| I 53059–53066 | `4.16:prf-boundary-factors` | X_n ∩ Ω_j = ∅ for n ≤ j−2, from the positive gaps | **covered** |
| I 53111–53118 | same | faces of Ω₁ on the LMη grid | **covered**: Ω''₁ = Ω₁ (old premise) |
| I 97621–97630 | `4.23:def-copies-reading` (a) | says only that "the admissibility of the prepared large-field data is used" to define the copies (whole group for far y ∈ Z, tail for far y ∈ Z^c); the item takes the new determining set of the prepared sequence | **covered** on the only reading I find: the item needs {Ω''_j} admissible in the (A1) sense, so that the generating set 𝔹''_k of CMP 122a is defined. The copy rule is a definition of CMP 122b and needs no proof. The account names no clause. If it reads more than (A1), the rest is not covered |
| I 143833–143835 | `4.28:lem-cutting-strata` | Z''_h = Z_h, and Z''_i increasing in i | **covered**: Ω''_i = Ω_i for i ≤ h; Z_h ∩ X ⊂ D_{h+1} (`pda.md` §3, from (L1)); nesting from (G2) |
| I 143888–143895 | same, (iv) | the definition of N₀ (L^{−N₀+1}MR_{κ₀+1} = M), and "an MR_{κ₀+1}-cube of scale κ₀+1 is an M-cube of scale κ" | **covered by the account's own proof**, not by `pda.md`: this is `4.14:not-operation-conventions` (b), CA-I 48141–48261. `pda.md` reads it as (S), and `pda-gate.md` §3 checked it |
| I 143913–143920 | same, (iv) | for κ₀+1 < m < J, Γ''_m is one layer of scale-(m+1) M-cubes; at m = κ₀+1, width ≥ (L−2)/(L−1)·M; a band of five M-layers | **covered** by rule (C): (U1) gives width exactly m_{m+1} for s < m < k, and (U2) gives the width at m = s. See D1 on the endpoint forms |
| II 14830–14843 | `5.2:prf-arrested-regions` | the band B_n = (Z_{j+1} ∖ Z''_{j+1}) ∩ X_𝔞 is a union of level-(j+1) M-cubes, j = j_n | **covered**: `pda.md` §§2–3 make D_{j+1} a union of m_{j+1}-cubes for j+1 > h; Z_{j+1} is a union of MR_{j+1}-cubes (CMP 119 p. 256, old structure); X_𝔞 is a component at step k_a. At j+1 = h the band is empty |
| II 17129–17132 | `5.2:lem-current-label-anchors` (i) | the preparation remakes Ω''_j and Z''_j only inside its own component; the unprimed Λ_j do not change | **covered**: rule (G) changes nothing off the operated components, and by (B) each D_i reads Ω_s and Ω_i only inside its own X |
| III 21301–21309 | `9.1:not-integer-floors` | β ≤ 1/4, ℓ_∘² ≤ L/3 and L ≥ 3, "read through" the admissibility | **not covered**, and this is not (A1) content. Nothing is owed except to impose the three one-sided conditions in the order of choice. Odd L ≥ 8 (CA-I 45681) gives L ≥ 3, and CA-III 570 imposes L ≥ 3ℓ_∘². `pda.md` reads neither β nor ℓ_∘, so (A1) does not depend on them |
| III 53327–53335 | `9.8:lem-exponent-localisation` | the point count #Y ≤ M⁴C_d(d(Y)+1) for a localisation domain | **not covered**; this is not (A1) content. Weakest statement: a domain Y of level ℓ is a union of at most C_d(d_ℓ(Y)+1) cubes of π_ℓ, each with M⁴ sites, where d_ℓ is the tree length in units of M (CA-I 946–980, 3739). It is a hand count. `pda.md` does not prove it |

**Inventories.** These are I 45558–45559 and 45598–45618 (the declaration), I 166579 and 166647, II 145579–145580, III 75801, III 111073–111079 and 111104–111106, and III 111311–111312. They list the input and derive nothing. `pda.md` changes the status of its (A1) half for one operation. Still listed: (A2), the T-step half, the point count and the constant conditions.

**N1. (A2) is not touched.** Weakest statement: at every level k of the history, the next domain Ω_t = Ω_{k+1} that T carves satisfies three things. First, Ω_t ⊂ Ω_k. Second, dist_∞(Ω_t, Ω_k^c) ≥ 6M. Third, Ω_t is a union of closed level-k LM-cubes of the compatible family. Here {Ω_j}_{j≤k} is the nest in force; it is the prepared nest if an operation acted at k. One help, unproved as a premise: (G1) gives (Ω''_k)^c ⊂ Ω_k^c. So if T carves Ω_t with the 6M margin inside the old Ω_k, then (A2) holds for the prepared nest too.

**N2. The old-label (A1) premise is the T-step half.** `pda.md` takes (A1) before each operation as input. Here is a reduction I did not find written in the account or the library. It is proved below, but it rests on one premise that I did not check: T extends the nest by Ω_{k+1} and leaves Ω₀, …, Ω_k unchanged. Under that premise, (A1) at level k and (A2) at level k give (A1) for the extended nest at level k+1. Proof:
- The gap ℓ_j^{−1} dist_∞ counts level-j spacings, so a change of reference level does not change it. With ℓ′_j = ℓ_j/L and dist′ = dist/L, the quotient is unchanged.
- At the new junction j = k, (A2) gives a gap ≥ 6M ≥ M.
- A closed level-k LM-cube is a closed level-(k+1) M-cube.
- The Dirichlet hull of Ω₁ does not change.

By induction over the history, (A1) at every nest then follows from three inputs: (A1) at the first nest, `pda.md` at every operation, and (A2) at every T-step. This does not give the LM gap of 45630. (A2) gives 6M at the new junction, and LM ≥ 8M. No listed use reads the LM gap.

**D1. Endpoint forms in 4.28.** This is a difference of reading, not a failure of coverage. `4.28:lem-cutting-strata` (143848–143851, 143897–143912) reads Balaban's (1.10) in the Z′ forms: Z''_{κ₀+1} = (Z′_{κ₀})^∼ and Z''_κ = (Z′_{κ₀})^{∼3}. `pda.md` (E) uses the Ω forms, D_s = X ∖ Ω_s^{(+7M)} and D_k = X ∖ Ω_s^{(+5M)}; at 92015 Balaban writes both forms as equal. The two forms agree when Ω_s^c ∩ X = (Z′_{κ₀})^{∼8} ∩ X. That is the equality case under class clause (ii) (143805–143809). In general 4.28 has only Ω_s^c ⊇ (Z′_{κ₀})^{∼8}, and then the Ω forms are larger. I redid each step of 4.28 (i), (ii) and (iv) that reads the endpoints, using the Ω forms:
- Z''_J ⊂ Z''_κ ⊂ Ω_s^c.
- Γ''_{κ₀} ⊇ (Z′_{κ₀})^∼ ∖ Z′_{κ₀}.
- The band Ω_s^c ∖ Z''_J contains Ω_s^c ∖ D_k, the 5M band about Ω_s in X, which is five layers of M-cubes by `pda.md` §1.
- Γ''_{κ₀+1} has width a_s − a_{s+1} ≥ (L−2)/(L−1)·M, by (U2).

Each conclusion holds. So 4.28 is covered if it is read with the Ω forms, as `pda.md` reads (1.10).

**Count for §1.** There are 29 clear-use rows in `uses-old.md` §3; the table above merges 47616 with 47637 and 47745 with 47869. Of the 29:
- 17 are covered. One of them (143888) is covered by the account's own proof, not by `pda.md`.
- 4 read (A1) and (A2) together (46045, 47253, 47616, 47637). Their (A1) half is covered and their (A2) half is not.
- 4 read only (A2) (46478, 47745, 47869, 47998). They are not covered.
- 45628 is covered in part.
- 48132 is not covered as stated.
- 2 read content that is not (A1) (CA-III 21301 and 53327). They are not covered.

Each (A1) verdict holds at prepared and stage nests and is conditional on old (A1), which is N2.

