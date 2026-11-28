lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T14:34Z

# uses-pda-um: do library/pda.md and library/um.md cover the uses listed in library/uses-old.md §§3–4?

Queue row 371. Commit 02f31fdc9. Claude Opus 5.5, max effort, Mac mini worker, fresh session. One reading, not an audit. No numeric job was run; every step is by hand. Checked line by line by Claude (Mini worker).

Moves: the two old-input rows of `library/uses-old.md` for CA-I `4.14:prop-prepared-data-admissible` and `4.2:lem-unmarked`. If a use is covered, that input can be cited at the use with no new lane. If it is not covered, the row names the weakest statement still owed.

Kind of result (FINISH item 9): a check of our ports against their consumers in the account. There is one exception: §3 proves a step the account assumes, (A2) at every T-step. That proof is not yet checked by the other model. Sources: CA-I, CA-II, CA-III at `31a47c543775`, fetched by URL into a scratch folder. The CA-I SHA-256 is `4cb5cb5e…6e93`, the same as in `pda.md`.

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
| III 53327–53335 | `9.8:lem-exponent-localisation` | the point count #Y ≤ M⁴C_d(d(Y)+1) for a localisation domain | **not covered**; this is not (A1) content. Weakest statement: every Y ∈ 𝒟_k meets at most C_d(d_k(Y)+1) level-k cubes of side M, each with M⁴ sites, where d_k is Balaban's size from CMP 109 (CA-I 1016–1020, 3739). Given a tree definition of d_k, this is a short hand count. But the definition is cited, not rebuilt, and `pda.md` does not prove the count |

**Inventories.** These are I 45558–45559 and 45598–45618 (the declaration), I 166579 and 166647, II 145579–145580, III 75801, III 111073–111079 and 111104–111106, and III 111311–111312. They list the input and derive nothing. `pda.md` changes the status of its (A1) half for one operation. Still listed: (A2), the T-step half, the point count and the constant conditions.

**N1. (A2) is not touched.** Weakest statement: at every level k of the history, the next domain Ω_t = Ω_{k+1} that T carves satisfies three things. First, Ω_t ⊂ Ω_k. Second, dist_∞(Ω_t, Ω_k^c) ≥ 6M. Third, Ω_t is a union of closed level-k LM-cubes of the compatible family. Here {Ω_j}_{j≤k} is the nest in force; it is the prepared nest if an operation acted at k. §3 (R1) derives this statement from the account's `4.4:lem-collar-avoidance`(b), with gap 8LM.

**N2. The old-label (A1) premise is the T-step half.** `pda.md` takes (A1) before each operation as input. Here is a reduction I did not find written in the account or the library. It rests on one premise: T extends the nest by Ω_{k+1} and leaves Ω₀, …, Ω_k unchanged. The account reads this premise from CMP 119 (2.1) and (3.20) at CA-I 12234–12240; I did not check it against CMP 119. Under that premise, (A1) at level k and (A2) at level k give (A1) for the extended nest at level k+1. Proof:
- The gap ℓ_j^{−1} dist_∞ counts level-j spacings, so a change of reference level does not change it. With ℓ′_j = ℓ_j/L and dist′ = dist/L, the quotient is unchanged.
- At the new junction j = k, (A2) gives a gap ≥ 6M ≥ M.
- A closed level-k LM-cube is a closed level-(k+1) M-cube.
- The Dirichlet hull of Ω₁ does not change.

By induction over the history, (A1) at every nest then follows from three inputs: (A1) at the first nest, `pda.md` at every operation, and (A2) at every T-step. (A2) alone does not give the LM gap of 45630: it gives 6M at the new junction, and LM ≥ 8M. R1 in §3 gives 8LM there, which is enough. No listed use reads the LM gap.

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


## 2. Uses of `4.2:lem-unmarked` against `library/um.md`

**What `um.md` supplies.** It assumes the lemma's four hypotheses (CA-I 4046–4058) and keeps the analytic inputs listed below. Then, for every l ≥ 1, |β^𝔄_l − β⁰_l| ≤ C_rem ε₁^I and |β^𝔄_l| ≤ C_β. The constants are C_rem = C_ext A_R and C_β = C_ext E₀ (`um.md` (25)), with C_ext = 4C_N C_* S_ρ T_ρ (23) and C_* = 16C_H²a^{−2}K₀e^{4c_dMρ} (20). Both are uniform in l. This uniformity is what the account's own later proof lacks: it allows C_𝗁(j) (58786–58847).

**Inputs `um.md` keeps** (its §2), beyond the four hypotheses:
- (R-a) CMP 109 (3.11)–(3.14) and (4.2)–(4.5), with the free-boundary replacement (4.35)–(4.37). These give the four-norm response bound (5), with constants C_H and σ.
- (R-b) the flat local-current bound (7), with constant C_F (CA-I 14083–14132).
- (R-c) the `ui.md` continuation, with its retained inputs and the tower rules of CA-I 32950–33080.
- (R-d) CMP 99b (3.132), through (R-a); the account cites it as printed without proof (CA-I 13142–13173).
- (R-e) the rooted count (17), CA-I 58877–58879.

**Where its constants sit, read against the account's order.** The order is in `2.3:not-stages-last` (CA-I 1584–1700), `2.4:lem-no-cycle` (2116–2160) and (H3) (1146–1149).
- *The account's slot for C_β.* C_β is one of "the determined constants". It comes after the radii α′₁, α′₀, α₁, α₀, α₂, after E₀ and after α₄ (1626–1634, 2123–2126). It comes before ε₀^I and ε₁^I. The account says it "reads δ₀, κ and M" (2124).
- *`um.md`'s C_β = C_ext E₀ fits that slot.* It reads C_H, σ and C_F, which are CMP 109 constants fixed early, like B₃ (1596–1598). It reads K₀ (from κ, Stage 3), M (Stage 6), c_d, C_N, and E₀. It also reads a, through `um.md` (8): a < min{1, α₂, α₁/8, α₀/(2C_IV)} and 2a + C_F a² < α₀/2. So a reads the radii and C_IV(d, L). Each of these letters comes before the slot.
- *`um.md`'s C_rem = C_ext A_R comes before ε₁^I.* A_R is the (2.41) coefficient C₃ = 4(L+2)⁴O(1)E₀C₁α₄^{−1}α₆^{−1}M^{q̄}e^{C₂κ₁} (CA-II 3302), with perhaps one more factor α₆^{−1} (CA-II 3440–3446). Here α₆ = α₆(d) is a Stage-0 number (CA-I 1378), α₄ comes before the determined constants, and κ₁ is Stage 4. So C_rem is fixed before ε₀^I and ε₁^I. This is what the lemma requires: C_rem "depends only on L, N and the parameters of (H3) chosen … before ε₁^I" (4034–4038).
- *No cycle.* In the account, every condition that reads C_β or C_β+1 is of one of two kinds:
  - a ceiling on γ: Stage 8, (C_β+1)γ² ≤ 1; 4.7 (Γ4)(b) and (f), 31792–31825 and 31930–31942; the 4.22 convention, 92964–92969 and 93330–93340;
  - the definition of a later quantity: 4.33's C (157195–157202), and 4.36's B̄⁺ = max{C_β+1, c₅} (158118–158122, 163307–163310).
  
  None of these caps a letter that `um.md`'s C_β or C_rem reads. This agrees with `1.2:def-flow-constants`: constants fixed before γ read the flow constants only through (c₀/4, c₅, B̄) (656–657).
- *The ceiling ε₁^I ≤ c₀/(2C_rem) is the account's own* (4017–4021; Stage 7, last item; 163163–163166). It is one-sided. It is imposed when ε₁^I is chosen downward, after C_rem.

| CA lines | Use | What the use reads | Verdict |
|---|---|---|---|
| I 3601–3605 | `4.1:thm-clause-zero`, explanation | the lemma as a per-step bound at level k+1; it may use only clause (i), the flow bounds up to k, and x₀, …, x_k ≥ γ^{−2} | **covered**: by `um.md` §6, every input uses g_{l−1} and earlier couplings only |
| I 4017–4028 | the application after `4.2:lem-one-loop` (unlabelled) | ε₁^I ≤ c₀/(2C_rem); \|β^𝔄_l − β⁰_l\| ≤ C_rem ε₁^I for all l ≤ n with one C_rem; then Σ_{l=i+1}^n β^𝔄_l ≥ (n−i)c₀/2 − 2c₂ | **covered**: `um.md` (24) and (26); the constant is uniform in l |
| I 56345–56390 | `4.19:lem-flow-bounds`, at n = k+1 | (4.19:eq-flow-bounds-2): \|β^𝔄_l − β⁰_l\| ≤ c₀/2 and \|β^𝔄_l\| ≤ C_β for l ≤ k+1, with the C_β of Definition 1.2 | **covered**: C_rem ε₁^I ≤ c₀/2 by the ceiling, and (25) is the "choice made in Chapter 4" that Definition 1.2 names (644–646) |
| I 56428–56478 | `4.19:prop-clause-zero`, hypothesis (b) | the lemma at every level n with x_i ≥ γ^{−2} for i < n, together with Theorem 4.20 below n | **covered**. The use supplies the four hypotheses: g_i ≤ γ; Theorem 4.20 at earlier levels; (a) for the one-step bounds; and hypothesis 4 by the proposition at 4171–4180, under its two γ ceilings. Its list (a)–(h) must also carry `um.md`'s inputs (R-a)–(R-e). (R-a) and (R-d) are cited Balaban estimates of the kind (a) and (e) already assume; (R-c) goes with (g) |
| I 163165 | `4.36:rem-order-of-choice` | ε₁^I ≤ c₀(N)/(2C_rem), with the SU(N) values of the constants | **covered**. `um.md` is written for SU(N): §4 uses 𝔰𝔩_N, and C_N in (23) is the colour contraction. N enters C_rem only through values. See D2 |

**Mediated reuse of C_β** (I 144, 162; 644–652; 1148; 1631–1687; 2124–2157; 2648; 31794–31942; 56481; 92964–93336; 157195–157202; 158112–158315; 163095–163169; 163307–163423): **covered**. Each reads C_β, or C_β+1, as a constant fixed after M and before γ. In 2.3 and 2.4 it is also fixed before ε₀^I. Each uses it only in ceilings on γ or in later quantities. `um.md`'s C_β meets this.

**Exclusions confirmed.**
- `4.31:prf-tube-analyticity` (156347, 156392, 156478–156482) is not a use. Its C_β is a new constant, introduced by "there are constants" in `4.31:def-standing-inputs` (a) (153937–153960), and it bounds the complete increment. Clause (0) supplies it as max{C_β+1, c₅}, as 4.36 does at 158310–158316, not through this lemma.
- The pile constant of 4.25, and the letters C_β in II and III, are other constants.
- The inventories at I 166617 and III 111368–111369 derive nothing.

**D2. A reading of the SU(N) order remark.** `4.36:rem-order-of-choice` (163095–163100) lists E₀(N, L, 𝔭) among the constants that c₀(N) and B̄ = max{C_β+1, c₅} fix "hence". At 163143 it says that C_β+1 is fixed after 𝔭. Under `um.md`, C_β = C_ext E₀ and C_rem ∝ E₀. So E₀ must be read as one of the (a2) values of Balaban's constants: fixed before C_β and before ε₁^I, as the SU(2) order has it (1630, 2123). If the remark is read literally, with E₀ after B̄, then C_β = C_ext E₀ is circular. Nothing in the account makes E₀ depend on C_β: 4.7 lists E₀ among the step constants, and (Γ0) is a ceiling on γ. Weakest statement needed: E₀ is fixed before C_β. This is a reading, not a defect.

**Count for §2.** All 5 clear uses are covered, and so are the mediated rows. Every verdict is conditional on `um.md` passing its check (row 338) and on its inputs (R-a)–(R-e).

## 3. Repair R1: (A2) at every T-step, from the account's collar lemma

Proved here by Claude; not yet checked by the other model. It is an implication from the premises below. It closes N1, and with N2 it closes the old-label premise.

**Statement.** Fix a level k of the history. Let {Ω_j}_{j≤k} be the nest in force before the T-step from level k to k+1. This is the old nest, or the prepared nest if an operation acted at level k. Let Ω_t := Ω_{k+1} be the domain that this T-step produces. Assume:
- (P1) Ω_k ⊃ Λ_k. This is the nesting of CMP 119 (2.1), quoted at CA-I 12234–12236. At a prepared level, also Ω''_k ⊃ Ω_k by `pda.md` (G1), and Λ_k does not change (CA-II 17131).
- (P2) Λ_k ⊃ Ω_{k+1}. This is the one-level extension, CMP 119 (3.20), quoted at CA-I 12238–12240.
- (P3) Ω_{k+1}^c ⊃ (Z′*)^{∼8}. Here Z* is the large-field region from which the T-step runs CMP 119 (3.5). Z′* is the union of the LMR_{k+1}-cubes of the level-k scale that meet Z*, and ∼ adds one layer of these cubes. If no operation intervened, Z* = Z_k = Λ_k^c. Otherwise Z* = Z_k ∪ ⋃_i Y_i, under the hypothesis stated in `4.4:lem-collar-avoidance`(c) (CA-I 12131–12137). With Z* = Z_k, the inclusion is `4.4:lem-collar-avoidance`(b). Its proof reads only (3.5) (CA-I 12205–12225, read in `pda-gate.md` §3), so the same chain holds with Z* in place of Z_k.
- (P4) Ω_{k+1} is a closed union of LMR_{k+1}-cubes of the level-k scale, from the compatible family (CA-I 48151–48155). This is the cell structure of the (3.5) output. It is the same inherited input as `pda.md` item 2 (inherited inputs (a) and (b) in `pda-gate.md`).

Then (A2) holds at level k: Ω_t ⊂ Ω_k; dist_∞(Ω_t, Ω_k^c) ≥ 8LMR_{k+1} ≥ 8LM > 6M; and Ω_t is a union of closed level-k LM-cubes of the compatible family. The same holds with Ω''_k in place of Ω_k. The gap 8LM also exceeds the LM gap of CA-I 45630.

**Proof.**
1. *Inclusion.* By (P2) and (P1), Ω_t ⊂ Λ_k ⊂ Ω_k ⊂ Ω''_k.
2. *Margin.* By (P1), Ω_k^c ⊂ Λ_k^c = Z_k ⊂ Z* ⊂ Z′*, and (Ω''_k)^c ⊂ Ω_k^c. Put s = LMR_{k+1}. Take x ∈ Z′* and y ∈ Ω_t, and suppose |x − y|_∞ < 8s.
   - Then y lies in the open set {z : dist_∞(z, Z′*) < 8s}.
   - For a union of aligned closed cubes of side s, the n-layer enlargement equals the closed metric enlargement by ns (CA-I 48157–48162). So this open set lies inside (Z′*)^{∼8}.
   - By (P4), y is a limit of interior points of Ω_t. So the interior of Ω_t meets (Z′*)^{∼8}.
   - This contradicts (P3), read in the regularised sense of CA-I 45279–45281: the interior of Ω_{k+1} misses (Z′*)^{∼8}.
   
   Hence dist_∞(Ω_t, Ω_k^c) ≥ dist_∞(Ω_t, Z′*) ≥ 8s ≥ 8LM, because R_{k+1} ≥ 1. Also 8LM > 6M.
3. *Cubes.* R_{k+1} is a power of L. So by (P4), each LMR_{k+1}-cube of the level-k scale is a union of level-k LM-cubes of the same compatible family. ∎

**Consequence, with N2.** N2's premise is (P1) and (P2) with the earlier members unchanged (CA-I 12234–12240). Under it, induction over the history gives (A1) with gap LMℓ_j, and (A2), at every nest:
- *Base.* The nest is (Ω₀, Ω₁). Its only clauses are the cube clause for Ω₁, which is (P4) at k = 0, and the Dirichlet hull, which is a definition.
- *T-step.* Use R1, then N2.
- *Operation.* Use `pda.md`, which keeps the LM gap.

This is the "admissibility lemma for the produced nests" that CA-I 45626–45634 asserts but does not prove. It would cover each geometric use in §1 that is now open or open in part: 45628, 46045, 46478, 47253, 47616, 47637, 47745, 47869, 47998 and 48132. It would also discharge the old-label premise of every (A1) verdict. Its inputs are of the same kind as `pda.md`'s: the account's proved collar lemma, and Balaban's (3.5) and (3.20) as the account reads them.

**What R1 does not show.** It does not check (P2)–(P4) against CMP 119 itself; it uses the account's readings. It does not prove the hypothesis of 4.4(c) after an operation. It proves no analytic statement.

**A further reader, not listed in `uses-old.md` §3.** CA-I 5608–5611 and 5770–5776 read the same 6M margin through an unlabelled "admissibility-margin statement", in the indexing of the walk-expansion theorem. They cite neither the label nor pp. 178–179, so the search for `uses-old.md` did not find them. R1 supplies this margin too, provided that indexing puts Ω_{k*} at the T-step's level. I did not check that indexing.

## Result

**Kind (FINISH item 9).** §§1–2 check our ports against their consumers in the account. §3 proves a step their text assumes; that proof is not yet checked. Nothing here corrects their text.

- **§1, `4.14:prop-prepared-data-admissible` against `pda.md`, 29 uses.**
  - 17 are covered at prepared and stage nests, given old (A1). One of them, 143888, is covered by the account's own proof of the N₀ conventions, not by `pda.md`.
  - 4 are covered for their (A1) half only.
  - 4 read only (A2) and are not covered.
  - 45628 is covered in part. 48132 is not covered as stated.
  - CA-III 21301 lists three constant conditions. Nothing is owed except to impose them. CA-III 53327 needs a point count, an elementary count that is not rebuilt.
  - No use needs a new ceiling.
  - 4.28 must be read with `pda.md`'s Ω-form endpoints (D1), and every step still holds.
- **§3, new.** R1 and N2 (proved here, not yet checked by Codex) derive (A2) at every T-step from the account's proved `4.4:lem-collar-avoidance`(b), with gap 8LM. By induction with `pda.md`, they give (A1) with gap LM, and (A2), at every nest of the history. If they pass a check, every geometric use in §1 is covered.
- **§2, `4.2:lem-unmarked` against `um.md`.** All 5 clear uses and every mediated reuse of C_β are covered. C_rem is fixed before ε₁^I, and C_β sits in the account's slot for determined constants, after the radii and E₀ and before ε₀^I. No condition in the account caps a letter that they read, so there is no cycle. The only ceiling is the account's own, ε₁^I ≤ c₀/(2C_rem). The SU(N) remark must be read with E₀ before C_β (D2). Every §2 verdict is conditional on `um.md` passing its check (row 338) and on its retained inputs (R-a)–(R-e).

**Still open:** the check of `um.md` (row 338); a check of R1 and N2 by Codex; the premises (P2)–(P4) and the 4.4(c) hypothesis, which are Balaban readings; the point count for CA-III 53327; and the clause that `4.23:def-copies-reading` reads, which the account does not name.

**Moves:** the old-input rows of `uses-old.md` §§3–4. If R1 and N2 pass a check, `P4-H-prepared` shrinks to Balaban's (3.5) and (3.20) readings and the 4.4(c) hypothesis; no separate (A2) lane is needed. `4.2:lem-unmarked` can be cited at all its uses once row 338 passes.

Checked line by line by Claude (Mini worker).
