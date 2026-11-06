lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T14:14Z

# uses-ui-oc: do library/ui.md and library/oc.md cover the uses listed in library/uses-old.md §§1–2?

Queue row 370. Commit 61ff5f275. Claude Opus 5.5, max effort, Mac mini worker, fresh session. One reading, not an audit. Checked line by line by Claude (Mini worker).

Moves: the two old-input rows of `library/uses-old.md` (CA-I `4.5:lem-uniform-increment`, `4.13:lem-own-constant`). If every use is covered, both inputs can be cited at their use sites with no new lane. A use that is not covered names the weakest statement still owed.

Kind of result (FINISH item 9): a check of our ports against their consumers in the account. No new proof. The source is CA-I at `31a47c543775`, fetched by URL into a scratch folder; SHA-256 `4cb5cb5e…6e93`, the same as in `oc.md`.

Credit: the lemmas, their uses and the proof mechanisms are from Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; the underlying constructions are Tadeusz Balaban's. `ui.md` and `oc.md` are Codex's ports, each checked once by Claude (`gates/ui-gate.md`, `gates/oc-gate.md`).

## Method

For each row of `uses-old.md` §1 and §2, I read the CA-I lines it cites. I wrote down what the use reads: the radius, the domain and tower, the cube letter, and the constants with their place in the order of choice. Then I compared that with the Result of `ui.md` or `oc.md`. Verdicts: **covered**, **covered after a stated ceiling**, or **not covered** (with the reason and the weakest statement the use needs). I did not re-check the internal proofs of `ui.md` and `oc.md`; the gates did that. Where a use reads a part of the lemma that our note cites rather than proves, I say so and read that part here.


## 1. Uses of `4.5:lem-uniform-increment` against `library/ui.md`

**What `ui.md` supplies.** The marked step (∗), that is the increment bound (4.5:eq-uniform-increment-a), `ui.md` (2):
|Φ_i(e^{iξA}𝐔) − Φ_i(𝐔)| ≤ ½C_IV α₂ λ², for i = 1, 2, every n ≤ j and every x ∈ X^{∼2}.
It holds on every tower that is admissible in the sense of CMP 102b (1) and has collar at most ½M. It uses the floors δ₀M ≥ 32, 2R₁M₁ ≤ M, c₁₂L ≥ 2, L ≥ 4d, the lemma's ceilings, and no other condition. The constant is C_IV = max{4C₁₄, 2(N+F)}, from (d, L) constants only. It sits in stage 2 of `4.5:rem-constants-order` (CA-I 19411), after C_H, ε̄₁ and 𝔯_g, and before M₁, M, the CMP 119 radius constants C₀, C₁′ and every amplitude. The proof is uniform in the cube letter: at M/L with LB and μ-scaled radii, the floors become δ₀M ≥ 32L and 2LR₁M₁ ≤ M (`ui.md` §7). For the maximal tower, `ui.md` (5) proves the collar bound.

**What `ui.md` does not rebuild.** Clauses (i), (ii), (iii)₁ and the U-half of (iv) are the account's own written proof, CA-I 16158–16231. `ui.md` cites them. I read them here. They hold with room. One factor is loose: ξ⁻¹‖Ad U − Ad 𝐔‖ |A| is bounded by 2|A′||A| at 16179. The exact bound is (e^{2ξ|A′|} − 1)ξ⁻¹|A| ≤ 2.6|A′||A|, since ξ|A′| < ½α₁ ≤ ¼ by the third ceiling. The same ceiling gives α₁ ≤ ½, so the sum stays below ½α₁ + 3α₂ before the higher BCH terms, and the stated ½α₁ + 4α₂ still holds.

**Rate correction.** `ui.md` uses rate δ₀/8, the rate (190) gives. The source continuation uses δ₀/4. This changes no use. The account's licence paragraph for the substitution M ↦ M/L (CA-I 33916–33946) quotes (1+M)e^{−δ₀M/32} ≤ 1 + 32/(eδ₀). Under `ui.md` the matching quantity is (1+M)e^{−δ₀M/64} ≤ 1 + 64/(eδ₀), by `ui.md` (21). It is still free of M. The licence holds as stated.

| CA-I lines | Use | What the use reads | Verdict |
|---|---|---|---|
| 10534, 10552–10553, 10626 | `4.4:lem-twist-stability` (s3′), (2^int) | C_IV as a (d,L) constant fixed before the CMP 119 constant C₀; the field ceiling min{α₁,j/8, α₀,j/C_IV} | **covered** |
| 11889–11916 | `4.4:prf-interior-sources`, hypothesis (P) | the lemma at the tower of every (p,Z) ∈ 𝔗_j(X), letters (M/L, LB), radii μ(α₀,j, α₁,j, α₂); floors δ₀M ≥ 32L, 2LR₁M₁ ≤ M | **covered** (`ui.md` §7; collar ≤ ½M/L by `ui.md` (5) for the maximal tower, and by the account's (4.8:eq-tower-rules-b) for 𝔯₂) |
| 12037–12057 | same proof | α₂ = L^{−(k−j)}C_H w_k below min{α₁,j/8, α₀,j/C_IV}, by (s3), (s3′); the lemma's ceilings among the ceilings on γ | **covered** |
| 17926–17939 | `4.5:prf-base-change`, real points | only the elementary plaquette expansion, with C₁₄ = 9(2d+2), applied at real A″ of size α₁‴ | **covered**, by the account's written part CA-I 16198–16223 (read here), not by `ui.md`'s new text; the use's own ceiling (c8) gives α₁‴ ≤ 1 |
| 19455, 19466, 19480, 19525 | `4.5:rem-constants-order` | the lemma's floors and ceilings, α₂ ≤ α₀/C_IV, C_IV in stage 2; the fifth entry of ε̄₁ gives sup|𝓗| ≤ 𝔯_g ≤ 1 | **covered**; `ui.md` reads exactly the fifth entry and adds no ceiling |
| 19781–19794 | `4.5:thm-operator-bounds` (F1) | the lemma at A(t_□), |A|, |∇_𝐔A| ≤ ⅔α₂ (covariant, by the (3.14) replacement at 19649), half-radius base, maximal tower; output (i), (ii), (iii)₁, (iv) at (α₀, α₁) | **covered** (`ui.md` (24)–(25) for the 𝐔-half; the rest is CA-I 16158–16231) |
| 19825–19836 | same, (F6) | admissibility and collar ≤ ½M only; maximal tower of X; window tower only where (iv) is established | **covered**, in exactly the scope the use states; no window admission follows |
| 19915–20118 | `4.5:rem-size-conditions` | floors, ceilings, the C_IV ratio, cube letter M/L, the cube cap not read at side M | **covered**. At 20118 the local gauge comes from (1.12), which is how `ui.md` §3 gets it. At 19985 the fluctuation-radius ceiling ε₁ ≤ ⅓α₂ serves (F1)'s hypothesis; the proof of (2) does not read it |
| 29421–29432, 29460 | `4.7:not-shift-fields` | α₂ ≤ min{α₁/8, α₀/C_IV, …}; C_IV ≥ 4(4d+2); the lemma on the maximal tower, uniform in M | **covered**: C_IV ≥ 4C₁₄ = 72(d+1) ≥ 16d + 8 |
| 29533–29535 | `4.7:not-true-pairs` | c_T = min{c_T°, 1/8, 1/C_IV} | **covered** |
| 29621–29682 | `4.7:not-working-radii` | c_α ≤ 1/(3C_IV); α₂,i ≤ min{α₁,i/8, α₀,i/C_IV} | **covered** |
| 33839–33869 | `4.8:prop-far-case`, statement | the lemma's clause for towers: every admissible tower with collar ≤ ½M, uniformly in M = L^{m′}; its ceilings and floors | **covered** |
| 33939–33950, 33988–34004 | same, proof | the substitution (j, X, M, B; α; A; 𝔯₁) ↦ (p, Z, M/L, LB; μα; μA; 𝔯); constants free of M, n, j, k, X | **covered**. For 𝔯₂ towers the collar bound 3dM₁ ≤ R₁M₁ ≤ ½M′ is the account's (4.8:eq-tower-rules-b), not `ui.md` |
| 34037–34054 | same | increment ½C_IV(μα₂)λ′² ≤ ½α₀μλ′², one power of μ | **covered** |
| 34252–34255, 34328–34344, 34391–34392 | `4.8:prop-class-reproduction` | through `prop-far-case`; one C_IV at every point of |A| < α₂, |B′| < α₃ | **covered** |
| 34436–34458, 34504–34506, 34530–34533 | `4.8:lem-top-layer-bound` | C_IV(d,L) fixed before C₀; floor C₀ > 2C_IV C_H(1+β₀)‖C‖C₁^{fl}A₁ | **covered** |
| 34546, 34576–34606 | `4.8:lem-layerwise-bound`, statement | (a), (b): `prop-far-case` at half radii under the account's ceilings. (c): the lemma read **additively** at the source radii F_jα₀,j, F_jα₁,j | (a), (b) **covered**; (c) **covered after a stated ceiling**, see D1 |
| 34660–34686 | same, proof of (b), (c) | as above; the ceilings "read at these source radii" | (b) **covered**; (c) see D1 |
| 34782, 34797–34818 | `4.8:rem-lower-bounds` | floors c₁₂L ≥ 2, L ≥ 4d, δ₀M ≥ 32L, M ≥ 2LR₁M₁; floors on C₀ with C_IV | **covered**; its list of amplitude ceilings must also carry the ceiling of D1 |
| 32419–32424 | `4.7:prop-coupling-increment` | through the membership propositions; "the lemma on admissible towers … at scale M/L" | **covered** (mediated, as `prop-far-case`) |

Mentions (CA-I 15949–15954, 16002–16016) are a route the account does not take and a preview. They need nothing. There is no use in CA-II or CA-III (`uses-old.md` §1, `ui-gate.md` Q3).

**D1. `lem-layerwise-bound` (c) needs one more ceiling at the labels with p = j.** This breaks no proved statement; it is a condition the account does not list.

- What the use reads. At a label (p, Z) with Z meeting Ω_j∖Ω_{j+1}, the source has radii μF_jα₀,j and μF_jα₁,j, μ = L^{−(j−p)}. The use adds ½C_IVα₂ to the first and 4α₂ to the second (CA-I 34675). So it needs the increment bound (2) and the clause-(ii) bound with the base at the radii F_jα, not ½α. Here F_j = 1 − β + β(1+θ)2^{−(k+1−j)} ≥ ¾, since β = ¼ (CA-I 9887, 41300). So the base is never at half radius. And 𝔗_j(X) contains labels with p = j (CA-I 33121), where μ = 1.
- Why the listed ceilings do not give it. In the proof of (2), the base radii enter through the third ceiling: s = c₁₂LMB a₀ + a₁ + α₂ ≤ c_♯ ≤ ¼, where a₀, a₁ are the base radii (`ui.md` (6); CA-I 16432–16434). The same ceiling keeps the twist inside half the radius α₁^{(98)} for the Cauchy estimate on the averages (`ui.md` (3); CA-I 16846–16849). The account imposes the lemma's ceilings at (α₀,j, α₁,j) (CA-I 11907–11909; for (b), 34595–34596). That gives c₁₂LMB·½α₀,j + ½α₁,j + α₂ ≤ c_♯ only. At p = j, F_j ≥ ¾ allows s up to about 2c_♯, above the bound s ≤ c_♯ that the proof uses. Then (14) of `ui.md` and the averaging step lose their margin, and the constant ½C_IV is not proved. The proof of (c) checks only the ceiling α₁ ≤ 1 at the doubled radius (CA-I 34676–34681).
- At p < j it is covered: μ ≤ 1/L gives s ≤ μ·2c_♯ ≤ c_♯.
- **Stated ceiling (repair, not yet checked by Codex):** among the ceilings on γ, impose c₁₂LMB^{(109)}α₀,j + α₁,j + α₂ ≤ c_♯. This is the third ceiling of (4.5:eq-uniform-increment-b) read at (2α₀,j, 2α₁,j). The first and second ceilings need no change: the real-base step has a factor-2 margin (CA-I 16502), and the second ceiling already carries α₁ + α₂ (CA-I 16561). With this ceiling the lemma applies verbatim with (α₀, α₁) := (2α₀,j, 2α₁,j). The base radii F_jα ≤ α = ½·(2α) meet its half-radius hypotheses. It gives the increment ½C_IVα₂λ² with the same C_IV. The written part CA-I 16158–16197 then gives the additive (ii) bound a₁ + 4α₂, since a₁ + α₂ ≤ c_♯ ≤ ¼. The ceiling is a ceiling on amplitudes, chosen after L, M, B^{(109)}, C₀ and C₁′, and uniform in k and j. It bounds nothing chosen earlier, so it makes no cycle. Enlarging C_IV alone would not repair it. The Cauchy estimate on the averages needs the twist inside half the radius α₁^{(98)}. When c_♯ = ½α₁^{(98)}, the listed ceilings keep the twist only inside the full radius, at n = p where λ = 1. Then the margin to the edge of that domain is of the size of an amplitude, and the constant of (3) is not uniform.
- What it does not touch. The account does not claim membership of the straddling producer (CA-I 34720). D1 concerns only the radius arithmetic of (c).

## 2. Uses of `4.13:lem-own-constant` against `library/oc.md`

**What `oc.md` supplies.** It covers the pairs printed in CMP 109 §§3–5 and CMP 116 §§1–2: the unit pair, the small pairs, and the real backgrounds U_k(V) ∈ 𝔘_k(ε₀) on the trivial nest. Each satisfies the widened (1.12), reading (ℓ1) = (L-12). The bound is SB₁₂α₀′ on every closed cube Q ⊂ X of side at most S = c₁₂LM in the units of the level, gradient member included. The radius α₀′ is arbitrary for the unit and small pairs (U = 1). For real backgrounds it is ε₀ at level k and με₀ at level j ≤ k. X is any closed set, thin parts included. There is one B = B₁₂ ≥ 2B₃, an entry of the maximum at CA-I 37914–37918, fixed before M. For reproduction by one step, `oc.md` §5 gives the unitary-factor moves at the loci of the CMP 109/116 analysis: ⟨1⟩–⟨7⟩, ⟨10⟩, ⟨11⟩ in the list at CA-I 35886–36075 (⟨3⟩ in its running form with the account's own floor). It also gives the new seed at level k+1. The conditions are `oc.md` (3)–(7).

**One extra ceiling.** Compared with the account's `4.9:prop-real-backgrounds` (a), `oc.md` adds one condition: ε₀ < c₉₈(d,L). This is the smallness under which CMP 98 Proposition 2 gives averaged defect below 2ε₀. The account's proof uses that proposition at CA-I 36645–36649 but does not state the ceiling. It is a ceiling on the radius ε₀, chosen after the (d,L) constants, so it makes no cycle. The account's consumers already ask for "ε₀ sufficiently small" (CA-I 34087–34090). So each use that reads a real-background seed is **covered after the stated ceiling ε₀ < c₉₈**. Two smaller points. `oc.md`'s strict 2ε₀ < a₁ can be relaxed to ≤, because the minimal-orbit theorem needs only ε₁ ≤ a₁ (CA-I 35170). `oc.md` (7) derives the torus-side floor (T_low)^S from H1 and H5 with the early floor 2L¹⁰ ≥ 3c; the account only assumes it.

**What `oc.md` does not supply.** These are not the content of 4.13, which reads only the CMP 109/116 one-step analysis:
- seeds on general nests, that is, the real stage backgrounds of the large-field operation (`prop-real-backgrounds` (b), (c), through CMP 99a Proposition 6 under (C-2));
- transport at ⟨8⟩, ⟨9⟩, ⟨13⟩, where the source is a CMP 119 (2.38) or CMP 122a (1.65), (1.67), (1.69) space (prolongation, gluing, large-field composites).

The account declares the statements that carry them PROVED: `4.9:prop-real-backgrounds`, `4.9:prop-large-field-cubes`, `4.9:lem-cube-prolongation`, `4.9:cor-gluing-smaller-cubes` (`library/sa-index/ca-full/index.tsv`). None of them is ported here.

| CA-I lines | Use | What the use reads | Verdict |
|---|---|---|---|
| 35388–35415, 35426–35439 | `4.9:rem-reproduction-meaning` | (a) transport at every locus; (b) seeds at α₀′; (c) one B₁₂ before M | (b), (c): **covered after the ceiling ε₀ < c₉₈**. (a): **covered** at the CMP 109/116 loci; **not covered** at ⟨8⟩, ⟨9⟩, ⟨13⟩ (outside 4.13). Weakest statement still needed: clause (i) of `lem-thin-cube-gradient` at those loci |
| 36102–36104, 36190 | `4.9:prop-gauge-transport`, locus ⟨5c⟩ | clause (i) of U_k|_X at α₀′; a seed | **covered after the ceiling ε₀ < c₉₈** (`oc.md` (13)–(16)) |
| 36806–36838 | `4.9:cor-printed-pairs`, statement | (ℓ1) at α₀′ on every cube of side ≤ S; α₀′ = ε₀ at level k, με₀ at level j; the same at k+1 | **covered after the ceiling ε₀ < c₉₈**; `oc.md`'s Result is this statement |
| 36830–36838, 36902–36905 | same, the hypotheses it supplies | the seed hypothesis of one-step closure; hypothesis (i) for minimal U_j, with 2B₃ε₀ ≤ α₀ | **covered after the same ceiling**; `oc.md` keeps 2B₃ε₀ ≤ α₀ as the consumer's own condition |
| 36872–36900 | same, proof | B₁₂ ≥ 2B₃; one factor μ on descent; the same at level k+1 | **covered** (`oc.md` (4), (15)–(16), §5 last paragraph) |
| 38000–38004, 38039–38059, 38083 | `4.9:lem-thin-cube-gradient` (ii), (iii) | (ii): seeds on trivial and general nests; (iii): B, B₁₂ depend on d, L, G only and come before M | (ii) on trivial nests: **covered after the ceiling ε₀ < c₉₈**. (ii) on general nests: **not covered** (outside 4.13); weakest statement still needed: `prop-real-backgrounds` (b), (c) at the stage backgrounds' printed radius, under (C-2) and hypothesis (f). (iii): **covered** |
| 34077–34096 | `4.8:prop-small-pairs` | (i) with (1.12) in the reading (4.8:eq-tower-clause-b) at α₀′, 2B₃α₀′ ≤ α₀; minimal U_j at its own level with "ε₀ sufficiently small" | **covered after the ceiling ε₀ < c₉₈**. The reading at CA-I 33093–33110 is (ℓ1); U_j at its own level has α₀′ = ε₀; `oc.md` (6) makes "sufficiently small" explicit |
| 56425–56427, 56465–56467 | `4.19:prop-clause-zero` (a′) | the widened (1.12) on smaller cubes, reproduced by every step of the construction | **not covered as a whole.** `oc.md` gives the seeds and the CMP 109/116 part only. Weakest statement still needed: clause (i) of `lem-thin-cube-gradient` at ⟨8⟩, ⟨9⟩, ⟨13⟩, and clause (ii) on general nests |

Ambiguous mentions in `uses-old.md` §2:
- CA-I 30206–30218 (`4.7:not-class-restrictions`) and 32417–32424 (`4.7:prop-coupling-increment`) ask for the widened condition on the whole class. They are like (a′): the 4.13 part is covered, and the rest is the thin-cube lemma.
- CA-I 45229–45236, the lemma's own route: **covered after the ceiling ε₀ < c₉₈**. `oc.md` proves 4.13 as stated, in its one-step setting.
- CA-I 166622–166623 and CA-III 111213–111214 are status lists. They make no mathematical use. Given `oc.md`, "proof outstanding" is stale for the stated scope, as `oc-gate.md` found.
- CA-I 53270, CA-II 58892 and CA-III 79880, 79894 are different assertions and need nothing.

## Summary

- **`ui.md`, 20 use rows.** Eighteen are covered. The two rows of `4.8:lem-layerwise-bound` are covered in (a) and (b), and covered after a stated ceiling in (c). One covered row, `4.5:prf-base-change` (CA-I 17926–17939), reads only the elementary plaquette expansion. That expansion is the account's written part, CA-I 16198–16223, not `ui.md`'s new text; I read it here and it holds. The constant C_IV of `ui.md` (23) depends on (d,L) only, sits in stage 2, and meets every reading: ≥ 4C₁₄, ≥ 4(4d+2), and before C₀, c_T, c_α and the amplitudes. No use needs an upper bound on C_IV. The rate correction δ₀/4 → δ₀/8 changes no use. The ceiling for (c) is needed only at labels with p = j (D1). It is c₁₂LMB^{(109)}α₀,j + α₁,j + α₂ ≤ c_♯ among the ceilings on γ.
- **`oc.md`, 8 use rows.** The seed uses are **covered after the stated ceiling ε₀ < c₉₈**. The constant B₁₂ is **covered**. **Not covered:** transport at ⟨8⟩, ⟨9⟩, ⟨13⟩, seeds on general nests, and therefore (a′) of `4.19:prop-clause-zero` as a whole. These lie outside 4.13. They rest on account statements declared PROVED and not ported here.
- **Labels.** Checked line by line by Claude (Mini worker): this covers the coverage check. The repair in D1 is by Claude and not yet checked by Codex. No numeric job was needed, so none was run.
