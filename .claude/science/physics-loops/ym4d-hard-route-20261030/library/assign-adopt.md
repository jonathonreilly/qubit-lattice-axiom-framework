lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-03T15:00Z

# assign-adopt: the explicit erosion assignment as the localisation, and what its consumers read (queue row 110)

Provenance: Claude Opus 5.5, high effort, Mac mini worker, pinned at 84313ded3. Same-model and not gated. This is research-stage text: no status, no audit. Outline: Sussman-Alpoge `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL to a scratch folder and not copied here. Line numbers below are SA lines in that file.

Credit. The assignment adopted here is the visible repair in `gates/a3-close-meet-gate.md` Section H (Codex, row 106). Its first-rule twin and the joined-sequence lemma are `library/a3-close.md` Lemma J (Claude, row 103). The rules being instantiated are the outline's two erosion assignments (SA 5598-5610), and every consumer named below is theirs: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Balaban (CMP 119 (1988) 243, Sections 1-3) is credited for the localised-background tests that the outline adopts.

Moves: the one premise that row 106 left on real-critical A3 and on 2.8, namely the identification of the erosion assignment (gate D1, Sections B, H, I).

## 0. Result

- **Adoption is admissible.** SA 5608-5609 allow "a particular assignment is supplied". Definition A below supplies both rules. Lemma A proves every requirement SA 5598-5610 places on an assignment, together with the properties the consumers read: cube unions, gaps, actual sets, one translation-compatible rule on all tori, commuting with common lifts of non-wrapping regions, plus an erosion-depth upper bound, monotonicity, locality and independence of the unit (Statement 3.8, SA 22044).
- **The joined sequence is then determined (Lemma JS).** Once Definition A is fixed, SA 9786's qualitative clauses (taken with the cut at depth j_a that its "levels q < j_a" clause forces) single out exactly the cut meet of Lemma J. So the gate's D1, "a compatible construction is not the source's", no longer applies on our chain. What remains is a definitional ruling, recorded as one: the outline's localisations are *defined* by Definition A.
- **Consumers (Section 4): no counterexample.** Every consumer of the localisations or towers that our chain reads uses only properties (A1)-(A9). Those consumers are Theorem 6(a), 6(b), 6(c), the four meets of 2.8 with (SEP) and (SEP-L), the cube-localised backgrounds of the tests (SA 17317-17380) as read by the floor-screening and support notes, the hereditary tower clauses (Lemma T = Theorem 5(a)), and statement 0 of 1c. No consumer reads a property that only a different assignment has. The one candidate, Theorem 5(b)'s requirement that the tower lie inside an ambient sequence, is a hypothesis checked where 5(b) is applied, and Definition A meets it there (4.7(b)). One reading premise remains, for the layered spaces only (4.7(c)): "Z of level p" must mean Z ⊂ Ω_p. It is off the A3/2.8 chain and goes to row 113.
- **Label:** row 106's open identification is **discharged as a definition plus an implication**. The analytic results of rows 103 and 104 (Theorem 6(c) via Lemma 10.1, Theorem M, (SEP) and (SEP-L)) now hold for the outline's localisations as defined here. They still carry their own named premises: F0, the A1 port, P82°, GEO1-GEO6 and EXT (Proposition 2.3).

## 1. Definition A (the adopted assignments)

Conventions are those of SA 5585-5616 and of Lemma T. A level-p cubical subdomain Z is a union of cubes of the level-p localisation partition π_p (centred half-open M-cubes in level-p units). Work in level-p units, with tower scales ξ'_q = L^{q-p} for 0 ≤ q ≤ p. Distances d_∞ are periodic sup-distances between site sets on the torus. An *aligned* cube of side sξ'_q is a cube of the centred grid of that side; all grids are nested because L is odd and all sides are powers of L (SA 6029, 24060-24067). The torus side is a multiple of every grid side used (SA 24063). Fix the powers of L in the outline's order (SA 9916, 19469-19480), with

  𝔐 ≤ M_1' ,   L^2 M_2 ≤ M ,   M_1' < M_2 (so M_2 ≥ L M_1'),   ρ = R_1 𝔐 ≥ L 𝔐 .   (1.0)

**First rule.** T_0 = Z, and T_{q+1} is the union of the aligned cubes Q of side 𝔐ξ'_{q+1} with d_∞(Q, T_q^c) > ρξ'_q.

**Second rule.** T_0 = Z, and T_{q+1} is the union of the aligned cubes Q of side M_1'ξ'_{q+1} with d_∞(Q, T_q^c) ≥ M_1'ξ'_{q+1}.

**Cut at depth n** (0 ≤ n ≤ p): the sequence (T_0, ..., T_n), with T_{n+1} = ∅. Members may be empty.

**Localisation** (SA 9776 (a)): the cube-wise meet Ω'_q = Ω_q ∩ T_q of a separated sequence with the tower of a region. The **joined sequence of a μ-collared region** (SA 9786) is Ω'_q = Ω_q ∩ ⋂_b T^b_{min(q, j_b)}, where T^b is the tower of the part A_b under the rule named by the consumer. This is Lemma J's formula, and Lemma JS shows it is forced. In particular `meet-6c.md` Proposition 7.1's 𝓛_X Ω is the meet with the second-rule tower of X (μ = M_1'), and the cube-localised background U_{k,□} (SA 9789, "one part on one lattice, μ = M_1'") is the background of the second-rule tower of its part.

Units are lattice units throughout. No length in Definition A refers to a physical scale.

**Part of a cube-localised background.** SA 9789 says only "a neighbourhood of a cube □". Fix it as the fourfold enlargement □^{~4}, with layers in the partition of which □ is a cube (test cubes, of side at least M_2 in level-t units). This is Balaban's choice, CMP 119 (1.2), and the one `support-envelope.md` 14.1 reads. The consumers of Section 4 need only □^{~m} with m ≥ 3.

## 2. Lemma A (Definition A meets SA 5598-5610 and has the consumed properties)

Fix a rule, a level-p subdomain Z and a depth n ≤ p. Put c_q = ρξ'_q + 𝔐ξ'_{q+1} (first rule) or c_q = 2M_1'ξ'_{q+1} (second rule), and let e_q = Σ_{i<q} c_i. Then:

- **(A1) Nested cube unions.** T_{q+1} ⊂ T_q, and T_q is a union of aligned cubes of side 𝔐ξ'_q (first rule) or M_1'ξ'_q (second rule).
- **(A2) Gaps.** The first rule gives dist_∞(T_q^c, T_{q+1}) > ρξ'_q, in the outer unit. The second gives dist_∞(T_q^c, T_{q+1}) ≥ M_1'ξ'_{q+1}, in the inner unit.
- **(A3) Erosion depth.** {x ∈ Z : d_∞(x, Z^c) > e_q} ⊂ T_q. Moreover e_q ≤ (ρ + L𝔐)ξ'_q/(L-1) ≤ ρξ'_q under the first rule, and e_q ≤ 3M_1'ξ'_q under the second.
- **(A4) Locality.** Whether x lies in T_q depends only on Z ∩ B_∞(x, e_q).
- **(A5) Monotonicity.** If Z ⊂ Z' (towers indexed by absolute level), then T_q(Z) ⊂ T_q(Z') for every q.
- **(A6) Truncation.** The tower cut at depth n consists of the first n+1 members of one recursion, which does not depend on n.
- **(A7) Translation compatibility.** T_q(τZ) = τT_q(Z) for every torus translation τ preserving π_p. Hence this holds for every translation preserving π_j, j ≥ p, which is the covariance SA 5889 requires of level-j terms. The same holds for every lattice symmetry fixing a common centre of the nested grids.
- **(A8) One rule on all tori; lifts.** Let Z ⊂ T_ℓ and Z̃ ⊂ Z^4 satisfy π(Z̃) = Z, with the covering map π injective on N_r(Z̃) = {y : d_∞(y, Z̃) ≤ r}, where r ≥ max_q c_q. One π_p cube (r = M) suffices. Then T_q(Z) = π T_q(Z̃) for all q ≤ n, with T_q(Z̃) given by the same formula on Z^4.
- **(A9) Unit-free.** The rule reads only the integers 𝔐, ρ, M_1', the relative level q - p and the level-q grids. So a relabelling of levels together with the unit (D_b of Statement 3.8, SA 22044-22053) maps towers to towers.

*Proof.*

(A1) If Q ⊂ T_{q+1} then d_∞(Q, T_q^c) > 0, so Q ⊂ T_q. T_0 = Z is a union of π_p cubes of side M. Since 𝔐ξ'_0 and M_1'ξ'_0 are powers of L not exceeding M, and the centred grids nest, T_0 is a union of aligned cubes of either side. T_{q+1} is a union of aligned cubes by definition.

(A2) Each cube of T_{q+1} satisfies the defining distance bound, and so does their union.

(A3) Let Q(x) be the aligned level-(q+1) cube containing x. Every site of it lies within sup-distance less than its side of x. First rule: if d_∞(x, T_q^c) > c_q, then d_∞(Q(x), T_q^c) > c_q - 𝔐ξ'_{q+1} = ρξ'_q, so x ∈ T_{q+1}. Second rule: if d_∞(x, T_q^c) > 2M_1'ξ'_{q+1}, then d_∞(Q(x), T_q^c) > M_1'ξ'_{q+1}, so again x ∈ T_{q+1}.

Now induct on q. Suppose T_q^c ⊂ {d_∞(·, Z^c) ≤ e_q}. Since d_∞(·, Z^c) is 1-Lipschitz, any x with d_∞(x, Z^c) > e_{q+1} has d_∞(x, z) > e_{q+1} - e_q = c_q for every z ∈ T_q^c. So x ∈ T_{q+1}.

For the sums: ξ'_i = L^{i-q}ξ'_q, so Σ_{i<q} ξ'_i ≤ ξ'_q/(L-1) and Σ_{i<q} ξ'_{i+1} ≤ Lξ'_q/(L-1). The first-rule bound ≤ ρξ'_q is L𝔐 ≤ (L-2)ρ, which holds since ρ ≥ L𝔐 and L ≥ 3. The second-rule bound is 2M_1'L/(L-1) ≤ 3M_1'. (These are Lemma J (a) and gate J(a), Section H, restated.)

(A4) By definition, x ∈ T_{q+1} if and only if every site y with d_∞(y, Q(x)) ≤ ρξ'_q (first rule) or < M_1'ξ'_{q+1} (second rule) lies in T_q. All such y lie in B_∞(x, c_q). Induction gives dependence on Z ∩ B_∞(x, Σ_{i≤q} c_i) only.

(A5) Induct on q. If T_q(Z) ⊂ T_q(Z'), then T_q(Z')^c ⊂ T_q(Z)^c. Distances to the smaller complement are no smaller, so every cube admitted for Z is admitted for Z'.

(A6) This holds by definition.

(A7) All grid sides used are 𝔐ξ'_q, M_1'ξ'_q ≤ M_1' ≤ M. They are powers of L dividing M, the side of π_p. So a translation preserving π_p maps every aligned cube used to an aligned cube, and preserves d_∞. Induction on q then gives T_q(τZ) = τT_q(Z). A translation preserving π_j with j ≥ p preserves π_p, because π_j's cubes are unions of π_p's. For point symmetries: centred cubes of odd side, and d_∞, are invariant under the hypercubic group about a common centre.

(A8) Induct on q. Suppose T_q(Z) = π T_q(Z̃) and T_q(Z̃) ⊂ Z̃. Write N(Q) for the set of sites whose distance to Q is admissible in the definition (A4); it has diameter at most c_q. Aligned grids on Z^4 project to the torus grids, because ℓ is a multiple of every side (SA 24063).

(⊇) If N(Q̃) ⊂ T_q(Z̃), then N(πQ̃) = π N(Q̃) ⊂ T_q(Z). Here π is a sup-isometry on sets of diameter below ℓ/2, which is implied by injectivity on N_r(Z̃).

(⊂) Let Q be admitted on the torus. Pick x ∈ Q, a lift x̃ ∈ Z̃, and the aligned lift cube Q̃ ∋ x̃. Then N(Q̃) ⊂ B(x̃, c_q) ⊂ N_r(Z̃). For ỹ ∈ N(Q̃) we have πỹ ∈ N(Q) ⊂ T_q(Z) = π T_q(Z̃), so πỹ = πz̃ for some z̃ ∈ T_q(Z̃) ⊂ Z̃. Both points lie in N_r(Z̃), so injectivity gives ỹ = z̃. Hence N(Q̃) ⊂ T_q(Z̃) and Q = πQ̃ is the image of an admitted cube.

By (1.0), max c_q ≤ max(2ρ, 2M_1') = 2M_1' < M. Without wrapping, the rule is the same on every torus.

(A9) Definition A is written entirely in level units, with ξ'_q = L^{q-p}. ∎

So Definition A is an assignment in the sense of SA 5598-5610: it gives actual sets (A1), (A2), (A6); it is one translation-compatible rule on all tori (A7); and it commutes with common lifts of non-wrapping regions (A8). SA 5608 then allows it to be supplied.

## 3. Lemma JS (with Definition A fixed, SA 9786 determines the joined sequence)

**Setting.** As in `a3-close.md` §3: parts A_b, collars col_b in single layers j_b, n_c ≥ 5, n_s ≥ n_c + 2, μ ≥ ρ, and towers T^b by Definition A.

**Claim.** Let Ω'' be a nested sequence with Ω''_0 = W, satisfying:

- (i) "with the tower of A_b in the collar", cut at depth j_b (forced by SA 9786's clause that new bonds have levels q < j_b; `a3-close.md` §3 counterexample, accepted in gate Section B): Ω''_q ∩ col_b = T^b_{min(q, j_b)} ∩ Ω_q ∩ col_b ∩ W;
- (ii) "coincides with the given sequence well inside W": Ω''_q = Ω_q on W \ ⋃_b col_b.

Then Ω'' is the cut meet Ω'_q = Ω_q ∩ ⋂_b T^b_{min(q, j_b)} of Lemma J.

**Proof.** Ω'' ⊂ W, and (i) and (ii) prescribe every member pointwise on W. Where two collars overlap, the prescriptions agree. At x ∈ col_b ∩ col_{b'}, Lemma J (c)'s proof gives d_∞(x, A_{b'}^c) ≥ 2ρ max ξ > e_{j_{b'}}, so by (A3) x lies in every T^{b'}_q with q ≤ j_{b'}, and symmetrically for b. Both col_b and col_{b'} are single layers, so j_b = j_{b'}, and both prescriptions give Ω_q at x.

Lemma J's Ω' satisfies (i) and (ii). For (ii): by Lemma J (c), Ω' = Ω off ⋃S_b, and S_b ⊂ col_b. For (i): on col_b ∩ W, Lemma J (c) gives Ω'_q ∩ col_b = T^b_q ∩ col_b ∩ W for q ≤ j_b and ∅ for q > j_b. Since col_b lies in layer j_b, this equals T^b_{min(q, j_b)} ∩ Ω_q ∩ col_b ∩ W. So Ω'' = Ω'. ∎

The result does not depend on the collar count: by (A3) and Lemma J (c), any collar containing S_b and lying in layer j_b gives the same sequence. The joined datum is then fixed by SA 9786 (V on old rows, the lift of V_{j_b} on new rows), with rows classified by Lemma J (d).

**Effect on gate D1 (row 106, Sections B, H).** That gate's non-uniqueness example ("small extra aligned erosion near a face") is a change of *assignment*. Its empty-member example (T_q = ∅ for q ≥ 1) is a different admissible assignment. Definition A excludes both. With Definition A supplied under SA 5608, the outline's localisations (SA 9776 (a)) and joined sequences (SA 9786) are the objects of Lemma J and Proposition 7.1, so the identification premise is gone. The ruling itself, that the outline's localisation means Definition A, is a definition, not a theorem about the outline's text. If the lead or the owner prefers to keep the outline's other option, "the core clauses ... imposed on all admissible assignments", then (SEP-L) fails: gate H's empty-member example breaks it. That option is therefore not available to the 2.8 consumer.

## 4. Consumers: what each reads, and whether Definition A has it

**Counterexample first.** We looked for a consumer that needs a property of a *different* assignment. Any such property would have to be one of three kinds:

1. a smaller tower, i.e. containment in some ambient set;
2. a particular erosion shape, i.e. Balaban's own layer counts;
3. symmetry beyond grid translations.

Every consumer found reads only (A1)-(A9), plus the outline's own geometric premises. The one place where kind 1 could matter is the layered hereditary core, 4.7(c). It is not on the A3/2.8 chain.

| # | Consumer (where it is used on our chain) | What it reads of the assignment | Holds? |
|---|---|---|---|
| 4.1 | Theorem 6(a), SA 9776: towers, localisations and joined sequences are separated (`meet-6c.md` (SEP), Lemma G (G-c); `sa-2.8-terms.md` §3) | (A1), (A2); for meets, Lemma J (b) and Prop. 7.1 | yes |
| 4.2 | Theorem 6(b) restriction (`a1-balaban.md` §9.2, gated), as used in Lemma T and Lemma 10.1 premise (R1) | Ω'_q ⊂ Ω_q, both separated; for a tower, T_q ⊂ Z ⊂ Ω_p ⊂ Ω_q, q ≤ p | yes, (A1) |
| 4.3 | Theorem 6(c), SA 9786-9789: Lemma 10.1 (`a3-derivative.md`, gated), Lemma J, Theorem M (gated row 106) | (A1)-(A3), with e_{j_b} ≤ ρξ_{j_b} ≤ μξ_{j_b}, and the identification (Lemma JS) | yes |
| 4.4 | 2.8, the four meets W1-W4 and (SEP), (SEP-L) (`sa-2.8-terms.md` §3, `meet-6c.md` §§3-7) | second rule (A3): e' ≤ 3μ, mismatch strip ≤ 3μ+3 ≤ 4μ ≤ ¼MŘ (needs M ≥ 16μ, as in meet-6c §3) | yes |
| 4.5 | Cube-localised backgrounds U_{t,□} in the tests, SA 17317-17380 (Lemma 2.2(a), factorisation SA 17336) | (A3), (A4), (A5), (A6), (A7) | yes |
| 4.6 | Floor screening and support: `support-envelope.md` §12 (12.2), §14.1, §15; `support-physical.md` (top member contains D^~); `floor-screen.md` Theorem R (via 6(c)) | collar width c_col M; top member ⊇ D^~ plus adjacent blocks | yes, c_col = 2 |
| 4.7 | Hereditary tower clauses (R5)-(R6), SA 5696-5728, 9654: Lemma T (Theorem 5(a)); Theorem 5(b)-(d); statement 0, SA 10256 | (A1)-(A4), (A6); 5(b)'s ambient containment | (a), (b) yes; (c) reading premise |
| 4.8 | Companions, covariance and naturality: SA 5884-5889, 19418, 20177, 22044 | (A7), (A8), (A9) | yes (2.13 and CT side, not on the A3/2.8 chain) |

**4.3, Theorem 6(c).** Lemma J's proof uses (A1)-(A3) and nothing else about the towers. Its other inputs are geometric hypotheses on the parts (n_c, n_s, single-layer collars). The constant C_μ ~ e^{O(μ)δ_0} of SA 9789 comes from the mismatch lying within e_{j_b} + 3ξ_{j_b} ≤ (ρ + 3)ξ_{j_b} of A_b^c, by Lemma J (e). Theorem M's decay set, from A_i^c, is unchanged (gate row 106, Section G). With Lemma JS, "U°_W is the outline's localised background" holds as a definition-level identity, no longer as a premise.

**4.4, 2.8.** Gate Section H proved (SEP-L) for this exact second-rule assignment. The proof uses e'_k ≤ 3μ, points deeper than 3μ surviving every factor, rows of length ≤ 1, and the double-block carrier within 3μ + 3. The collar check X = H_k^{[10]}, Ω_k^c ∩ X = H_k^{[8]} (SA 17575-17583) is also in Section H. W1 and W2 then read coincidence off a strip of width 3μ + 3 ≤ 4μ, within the ¼MŘ allowance. W3's coincidence of the full and the cut meet is not an assignment property. It is the geometric premise of gate Section B (d(C, Ω_q) ≥ Mξ_q, M > ρ, from GEO3), unchanged. W4's meet is with T \ Λ, a wrapping region. There only the torus formula is used, and (A8) is not needed.

**4.5, cube-localised backgrounds in the tests.** Each property has a specific consumer.

- (A3) gives the top member T_t(□^{~4}) ⊇ {d_∞(·, (□^{~4})^c) > 3M_1'}. One layer has side ≥ M_2 ≥ LM_1' ≥ 3M_1', so this set contains □^{~2} and its adjacent unit blocks: their depth is ≥ 2M_2 ≥ 6M_1' > 3M_1' + 3. So χ'_k's comparison on the non-pivot bonds of □^{~2} (SA 17317) reads averages of U_{t,□} on its top member. This is also the containment that `support-envelope.md` §14.1 and §15 and `support-physical.md` (lines 34, 131) read. Their source was Balaban's tower ("at most two M_1-layers"). Under Definition A the loss is at most 3M_1' and the containment still holds, with a margin of more than 3M_1'.
- (A4) together with (A1) means U_{t,□} depends on V_t only on □^{~4}. This is the locality behind "they depend on V_t, V_k only within O(1) test cubes" (SA 17336).
- (A5) and (A6) supply the restriction premise Ω'_q ⊂ Ω_q of Theorem 6(b) in SA 17374, comparing U_{k,□} with U_{t,□'}. The premise holds whenever □^{~4} ⊂ □'^{~4}, which is the outline's geometric claim, not an assignment property.
- (A7) gives covariance of the tests under translations preserving the test-cube grid.

**4.6, floor screening and support.** The outer collar of a component is X^~, one M-cube (SA 17357), together with the erosion strip of width ≤ 3M_1' + 3 inside X. Since M ≥ L^3 M_1' ≥ 3M_1' + 3, the width is ≤ 2M, so c_col = 2 in (12.2), and (12.2) reads 2M + 3 < MŘ_k, which holds once Ř_k ≥ 3. `floor-screen.md` reads the localisation only through Theorem 6(c), via its Lemma at line 145 and Lemma G. Lemma G is about cells (Proposition 2.3), not about towers.

**4.7, hereditary tower clauses.**

(a) Lemma T (`a3-close.md` §2, the proof of Theorem 5(a)) reads (A1)-(A3). It also needs Z° ⊇ Z minus two π_{p-1} layers, which requires M ≥ L(3M_1' + 2) under the second rule. This holds by (1.0): M ≥ L^2 M_2 ≥ L^3 M_1'. Theorem 5(d)'s "depend only on U|_{□_0}" is (A4) with (A1).

(b) Theorem 5(b)'s hypothesis that the tower lies member by member in an ambient separated sequence is the kind-1 candidate. At statement 0 (SA 10256), X ∈ D_j lies in one level. For Z ⊂ X of level p, n ≤ p, every assignment has T_q ⊂ Z ⊂ Ω_p ⊂ Ω_q for q ≤ n, so the containment holds for Definition A too. Lemma T writes exactly this inclusion. No consumer needs a smaller tower here.

(c) **Reading premise, flagged, not on the A3/2.8 chain.** For the *layered* spaces Ũ^c_j and Ũ^c_σ (SA 6140-6153, 9654), the inclusion in (b) needs every level-p subdomain Z that the quantifier admits to lie in Ω_p. If a level-p Z were allowed to reach a layer r < p, then any assignment with nonempty members of level q > r there would read averages of a large-field layer. The tower clause would then fail (no regular datum), and only an assignment that erodes away from such layers, for example the empty-member one, would avoid it. The outline's text does not say which reading it means. We read "Z of level p" as Z ⊂ Ω_p, the reading under which the restriction to the layered space (Theorem 6(d)) is meaningful, but we do not prove this here. It concerns the pointed-window admission (`sa-ledger.md` rank 4, `wf-room` row 113), not real-critical A3 or 2.8. Under that reading Definition A passes. Under the other, the defect lies in the quantifier, not in the choice of assignment, because Balaban's localised towers also have nonempty upper members.

**4.8, covariance and naturality.** Covariance of level-j terms under the translations preserving π_j (SA 5889), and companions agreeing on common non-wrapping lifts (SA 5884, 19418, 20177), need the assignment to commute with those translations and lifts. These are (A7) and (A8), with a collar of one π_p cube. Statement 3.8 ("rules made for the lattice, not for its unit of length") is (A9). These are consumed by 2.13 and the upper chain, not by A3 or 2.8. They are listed because SA 5606 makes them conditions of admissibility.

**Not found.** No consumer on our chain reads that the outline's assignment equals Balaban's CMP 119 tower. No consumer needs an erosion lower bound beyond the gaps (A2). (The REFUTED construction of `support-envelope.md` §21 reads only that "erosion to the tower's next member has positive width greater than one bare spacing", which is (A2).) No consumer needs symmetry beyond (A7). Of the grep hits for "tower" and "localization" in the outline (60 and 165 lines), the remaining ones are either the tower axial *gauge* (SA 7185, a different notion), the Gaussian localisation of the one-loop analysis (SA 20317, not an erosion), or cell and cluster localisation (SA 14133-14294, 24060-24067), which read only π_j.

## 5. Verdicts, defects, what changes, open

**Verdicts (same-model, to be gated):**

- Lemma A: proved.
- Lemma JS: proved.
- Consumer table: rows 4.1-4.6 and 4.8 pass; 4.7 passes under the stated reading.
- Row 106's open identification premise is **discharged as a definition plus implication**.

**Defects found (ranked by what they break):**

1. **The outline's alternative option cannot serve 2.8.** SA 5608-5609 offer to supply an assignment, or to impose the core clauses on all admissible assignments. For localisations the second option fails: with the admissible empty-member assignment (gate Section H), (SEP-L) is false. So for 2.8 and Theorem 6(c) the assignment *must* be supplied, and Definition A is a valid supply. Nothing else breaks.
2. **The layered quantifier (4.7(c)).** Whether a "level-p" Z ⊂ X must lie in Ω_p is not stated. Under the reading Z ⊂ Ω_p, Definition A passes. Under the other reading, every assignment with nonempty members fails, Balaban's included. This breaks nothing on A3 or 2.8. It goes to row 113 (`wf-room`), to state the quantifier explicitly. **Repair, unproved:** quantify the tower clauses of layered spaces over Z ⊂ X ∩ Ω_p.
3. **The part of U_{t,□} is unspecified (SA 9789, "a neighbourhood of a cube").** Fixed here as □^{~4} (Balaban CMP 119 (1.2)). The consumers need □^{~m} with m ≥ 3. This is a definition, with no failure.

**What changes:**

- `library/a3-close.md` §3 Consequences 1-3 and `library/meet-6c.md` Proposition 7.1 and §8 may be read for *the outline's* localisations, with Definition A as the definition of the localisation, the joined sequence and U_{t,□}. Gate row 106's qualification (D1, Sections B, H, I) is then met. Its D2 (one-sided weight) and D3 (endpoint loss) repairs stay as they are.
- FINISH "Where it stands", second bullet ("with the localisation's erosion assignment to be supplied explicitly (row 110)"): supplied here, pending a gate. This is for the lead to forward; this note does not edit FINISH.
- `support-envelope.md` §14.1's containment now reads the outline's localised background under Definition A (loss ≤ 3M_1'), not Balaban's tower. The conclusion is unchanged.

**Open (none is new):**

- GEO1-GEO6 and EXT (the outline's Proposition 2.3), including the W3 nest-gap premise of gate Section B.
- F0, the A1 port and P82° as already gated implications.
- Reading premise 4.7(c), to row 113.
- A cross-provider gate of Sections 2-4 of this note. Suggested scope: Lemma A (A3), (A8), Lemma JS, and table rows 4.4-4.6.

Computation: none. Every step above is written by hand. No numeric job was run.
