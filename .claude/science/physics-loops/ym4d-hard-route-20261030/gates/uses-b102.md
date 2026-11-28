lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T15:04Z

# uses-b102: coverage of the CMP 102 uses by `library/b102.md` round 3

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout `ee70ee2e6`, started 2026-11-06T03:04Z.
One reading by one model; not an audit; grants no status.

Status: complete (2026-11-06). Verdicts in §3, summary in §4.

Scope: every row of `library/uses-old.md` §5 (I: 108 rows, II: 54 rows, III: 26 rows, plus the 20 rows of "ambiguous mentions"), checked against `library/b102.md` round 3 (§8, H15–H25, and the Result), with H1–H14 as its inputs. For each row I read the cited lines of CA-I/II/III at `31a47c543775` (fetched by URL into a scratch folder; CA-I SHA-256 `4cb5cb5e…` matches b102 §1). I read the b102 statements H19–H25 in full and the two gate reports `gates/b102-gate-a.md`, `gates/b102-gate-b.md` (both: first failing step none). No numerical run was used.

Credit: T. Balaban (CMP 102 and its prerequisites); Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account whose uses are mapped here; Codex for b102.

## 1. What round 3 supplies, with its parameters

All of it is for d = 4 and G = SU(2), uniform in depth, fine spacing, volume and admissible nest. Status: proved by Codex; H1–H14 checked line by line by Claude (gate-a), H15–H25 checked line by line by Claude (gate-b), first failing step none in both, with two text repairs still pending in b102 (gate-b W1: two lines in H18; gate-b S2: one clause, below).

- **R3-T1** (H21–H22). Nest admissible as in CMP 102 (1), above b102's own floors (H9: block 𝔐 a multiple of M_P and at least c(L)M_P; H21: R₁M₁ at least the localisation length with B₃e^{−aR₁M₁/2} ≤ 1/2 and more than twice the protected-collar width). Dirichlet outer boundary or torus (H9). Datum (7) in mixed-level form with ε₁ ≤ a₁. Conclusions: a minimal orbit in 𝔘_k(B₃ε₁) ∩ 𝔅_k(V); the unique critical orbit in the class B₃ε₁ ≤ ε₀ ≤ a₀; the unique minimum over the regular class (H22.4, stronger than printed); the cube gauge (T5) on the special cube class for M′ a multiple of R₁M₁ with M′ ≤ R₁M₁a₁/ε₁; the second-order members (T6); the Hölder member with B₄(β₀) for β ≤ β₀ < 1 only (no β = 1, gate-b S1).
- **R3-P9** (H23). Base: a real admitted datum V₀ of R3-T1 and its axial minimiser. For complex B in one fixed ball |B| < b_* (b_* is fixed in H20/H23 before a₀, a₁ and is independent of ε₁; the text gives it no name), U_k(e^{iB}V₀) is holomorphic; its normalised Landau form is e^{iηℋ(B)} with ℋ(0) = 0, N(ℋ(B)) ≤ C|B|, the expansion (176)–(177), and agreement with the real minimiser by uniqueness. Charts about nearby real data glue on a uniform neighbourhood of the admitted real data. Raw data enter through the reduced map 𝔟 (H19.6). The clause "ℋ(B) satisfies (19)–(21) with ε₂ = B₅ε₁" is **not stated** in b102; gate-b S2 gives its one-line proof (H23.3 plus the last two lines of H24.12 integrated along tB). Holomorphy in external background coefficients is a sketch, and away from critical backgrounds it is a chart extension, not a minimiser (H23 last paragraph; gate-b S3).
- **R3-(181)** (H25). The complex orbit extension on the saturation G^c𝒟, written for SL(2,ℂ). No bound is asserted after a large complex gauge.
- **R3-(189)** (H24.2). |(V''(A′)v)(y)| ≤ C r ℓ_y^{−3} e^{−δ₀d(y,y′)/4} N(v) for N(A′) ≤ r and supp v ⊂ Δ̃(y′), with N = max{|·|₍₋₁₎, |∇_U·|₍₋₂₎}; the same for the physical-current remainder Ṽ. Here r plays the role of ε₃ and N(A′) ≤ r plays (77).
- **R3-(190)** (H24.12). At every B of the R3-P9 ball, at rate δ₀/8 and with the physical coarse measure ℓ_{y′}^{−4}: K, ∇_U K (covariant at the reference), the ζ-localised Hölder member for β ≤ β₀ < 1, d_U*d_U K and Δ_U^comp K. gate-b matched these to printed (190), p. 308.
- **Not supplied:** independent (free) current versions; complex or non-critical bases (except the chart-extension sketch); CMP 109 (1.16)–(1.17) and CMP 116 (b102 §8.12: "not used, not resolved"); SU(N) for N ≥ 3; any dimension other than 4.

## 2. Global conditions (they apply to every row in §3)

- **G1, group.** The account's Chapter 4 conventions fix G = SU(N), N ≥ 2 (CA-I 35052). b102 proves N = 2 only (H25 is written in SL(2,ℂ); H21 "the fixed compact matrix group of this lane"). Every verdict below is for SU(2). For N ≥ 3 every row is **not covered**; the weakest statement needed is R3-T1, R3-P9, R3-(181), R3-(189), R3-(190) for SU(N). This is off the SU(2) path of T0 and on its SU(N) extension.
- **G2, nest floors.** The account reads CMP 102 (1) as: each Ω_j a union of blocks of side 𝔐ℓ_j, gap (ℓ_j)^{−1}dist(Ω_j^c, Ω_{j+1}) > R𝔐 with R ≥ R₁, torus domains admitted (CA-I 12676–12722; CA-III 34660–34668). It leaves 𝔐 and R₁ as "sufficiently large, depending on (d, L) only, such that the theorems hold". b102's floors (R3-T1, and H14's auxiliary collars) read only L and the group. **Ceiling (a floor here):** take 𝔐 and R₁ above b102's floors, with 𝔐 a power of L (b102 may take M_P a power of L), so that every cube parameter that is a power of L and at least R₁𝔐 is a multiple of R₁𝔐. No cycle.
- **G3, order of a₀, a₁.** b102 chooses R₁M₁ before its chart radii and before a₀, a₁ (H21 last paragraph; §5 step 5: a₅ ≤ [8C(R₁M₁)²]^{−1}, C R₁M₁ B₃ a₁ ≤ 1/4). The account lists "the determined letters B₁, B₃, B₅, a₁" before "R₁, chosen upward" (CA-I 1509–1511, 2062–2064). **Repair:** place b_*, a₀, a₁ after the last floor on R₁𝔐. I found no floor on R₁ that reads a₁ (all floors on R₁: CA-I 2064, 12691, 12717, 13415–13416; CA-III 21144), so there is no cycle. R₁M₁a₁ ≤ 1/(4CB₃) stays a fixed positive number, so the account's ceiling (2.3:eq-stages-middle-1) stays a ceiling on ε^run.
- **G4, the (172) radius.** The account reads (172) as: |V′ − 1| < C₁ε₁ gives logarithms in |B′| < 2C₁ε₁, and uses the margin sup|B| ≤ ½C₁ε̄₁ (CA-I 13128–13134, 16567–16569). b102 has no constant C₁ of (172); its ball has the fixed radius b_*. **Ceiling:** fix C₁ (any number fixed before a₁, e.g. L³) and require 2C₁a₁ ≤ b_*. This is a ceiling on a₁, which b102 chooses last; no cycle. Then every account polydisc of radius ≤ 2C₁ε₁ with ε₁ ≤ a₁ lies in the R3-P9 ball.
- **G5, named constants.** a₀, a₁, B₁ (H19), B₃, B₄(β₀), M(ε₁), R₁M₁, δ₀ and c_* (= b102's C in H24.12) are b102 constants. B₅ is not in the b102 text (needs gate-b S2). C₁ is defined by G4. The account's Hölder exponent β_H ∈ (0, 1) (CA-I 1377) is inside b102's range β ≤ β₀ < 1.
- **G6, the datum condition.** R3-T1 reads (7) in the mixed-level form (b102 §1: same-level plaquettes alone are insufficient). Where a row states (7) for block data of one real field, the mixed-level plaquettes follow from CMP 98 Proposition 2 (the account's own step, e.g. CA-I 16494–16498); that step is the row's, not b102's.
- **G7, constants named B₃ or c_*.** Where a row uses "B₃" as the constant of a P9 or (190) bound (not the regularity constant), b102's constant C of H23.3 and H24.12 is built from operator constants fixed before B₃ (H21 order), so B₃ may be taken ≥ C. No cycle.
- **G8, free current.** b102 proves its operator, Hessian and response bounds only at the physical current (H18 "at the **physical** current"; H24 "physical-current versions"). The account's chart bounds at an independent current (CA-I 4.5 (K8), (F2), the chart constants) are the account's own lemmas, proved there from its free-current operator inputs; b102 supplies them only on the diagonal J = J(U).
- **G9, "minimal".** b102 proves the unique minimum over the regular class (H22.4) and says it does not assert an absolute minimum over unrestricted configurations (§1). Rows that use the critical orbit, its uniqueness in the class, or the regular-class minimum are covered. A row that needs the unrestricted minimum is not.

"Covered" below means: the statement the row reads is an R3 statement, or its immediate specialisation, at the radius, domain and constants the row reads, given G1–G3 and G5–G9 (and G4 where a row is marked C+). It does not check the row's own argument.

## 3. Verdicts per row

Codes: **C** covered (given G1–G3, G5–G9); **C+** covered after the stated ceiling or change, including G4 where the row reads the (172) radius; **N** not covered (reason; weakest statement needed). b_* is the R3-P9 ball radius.

### 3.1 Clear uses in CA-I (108 rows)

| Row (I:) | Statement | Verdict | Reason, ceiling, or weakest statement |
|---|---|---|---|
| 1031–1035 | 1.5:def-domains | C+ | (R4) tower minimisers: R3-T1 at real data, R3-P9 at complex data within b_* of the real factor's data; both tower rules are admissible (CA-I 32834–32894), so G2 applies. |
| 1340;1510,1559;1670 | 2.3:not-stages-* | C+ | G3 (a₀, a₁ after R₁); B₅ needs gate-b S2 written into b102. |
| 2063,2094 | 2.4:lem-no-cycle | C+ | G3. With it the no-cycle claim stands; R₁M₁a₁ stays a fixed number. |
| 3136 | 3.1:thm-main (pointer) | C | Pointer to the Ch. 8 uses (II:71256 row). |
| 3791 | 4.2:def-increment | C | The torus linearisation at V = 1 is R3-P9 at B = 0 (h = H₀w). The ℤ⁴ limit 𝔥_∞ in the same definition reads CMP 99b Thms 3.10, 3.12, not CMP 102; b102 gives only volume-uniform torus kernels. |
| 10163–10202 | 4.4:not-response-bound | C+ | Second case: five members at real bases, complex data in (172) ⊂ b_*-ball (G4). The account's "P₁ member" is covered: P₁ = D_UPD_U*, and P₁h = DD*h when RD*h = 0 (H24 3366–3368, H17.5). The free-current first case is the account's own (G8). |
| 10516,10521–10522 | 4.4:lem-twist-stability (hyp.) | C+ | As the previous row (G4); B₃ plaquette bound is R3-T1 (8). |
| 10725–10738 | same | C+ | Ceiling 2(α_{1,n′} + h_{n′}) ≤ b_* replaces "lies in (172)"; it is a Stage-7 ceiling after b102's constants. |
| 10747–10780 | same | C | First two members integrated from ℋ_p(0) = 0 (H24.12, H23.3); curvature 2B₃α₀ from R3-T1. |
| 12793,12812,12892–12894 | 4.5:not-geometry-conventions | C+ | ε̄₁'s entries read a₁, R₁a₁, C₁: G3, G4. Uniqueness clause B₃ε₁ ≤ ε₀ ≤ a₀ is R3-T1. |
| 13128–13134 | 4.5:not-reading-conventions (ρ5) | C+ | G4. |
| 14847–14865 | 4.5:prf-chart-variation-decay (K8) | N | Free-current analogue (G8). b102 proves it only on the diagonal J = J(U) (H24.1, H24.12). Weakest statement: (K8) for an independent current J with \|J\|₍₋₃₎ small, i.e. H18 and H24 with J a free variable. |
| 15125,15137–15150;15432 | 4.5:prf-chart-constants, prf-chart-walk-localisation | N | Same as (K8): the chart constants are uniform over free J. Covered only at diagonal pairs, where the row says the objects are Balaban's. |
| 15707–15735 | 4.5:prf-diagonal-exactness | C+ | The cubes have side 12𝔐ℓ_j, so M′ = 6𝔐 is **not** a multiple of R₁𝔐 (R₁ ≥ L ≥ 13); R3-T1's cube clause does not apply as stated (nor does printed T1). Route: R3-T1 regularity B₃ε₁ plus H14 (H14.1) gives s\|A\| + s²\|∇A\| ≤ C_L(12𝔐 + 2W_aux)B₃ε₁ on these cubes, with the separation floor of H14. Ceiling: C_L(12𝔐 + 2W_aux)B₃ε̄₁ < a₀(𝔖), one more entry of ε̄₁. |
| 15964–15966 | 4.5:rem-condition-iv | C | Remark on an unused route. |
| 16026,16044–16066 | 4.5:lem-uniform-increment | C+ | G4; the floors δ₀M ≥ 32, 2R₁M₁ ≤ M read b102 constants fixed before M. |
| 16375–16382 | 4.5:prf-increment-geometry | C | Admissibility (block 𝔐, gap ≥ R₁𝔐, one-endpoint bond sets) is exactly b102's hypothesis, given G2. |
| 16492–16532 | 4.5:prf-increment-kernel | C | R3-T1 at ε₁ = ε̄₁ ≤ a₁, ε₀ = B₃ε̄₁ ≤ a₀. (7) at the seams by CMP 98 Prop. 2 (G6). |
| 16565–16579,16595,16667 | same | C+ | G4. Landau-to-axial with node gauge 1 is H23's axial return. |
| 16772–16801 | 4.5:prf-increment-recentring | C+ | G4; a₆ ≤ a₁/(1 + 5C₁) needs C₁ fixed before a₁ (G4). Real (181) is H25 at real gauges. |
| 17555,17592–17594,17617,17769–17771 | 4.5:lem-literal-frame | C+ | Charts at bases 1 and M·U (both real, admitted); margins ½C₁ε̄₁, ¼C₁ε̄₁ (G4). Window tower is admissible (gap LM₁ > R₁𝔐, CA-I 12730–12737). |
| 17882–17905 | 4.5:prf-base-change | C+ | G4. |
| 17940–17964,17976–18000 | same | C | Uniqueness with ε₀ = B₃ε̄₁ ≤ a₀; real-gauge (181) by action invariance and uniqueness, as H25 does. |
| 18492,18499,18633,18671,18690 | 4.5:lem-fine-axial-frame | C+ | G4. |
| 18783–18793 | same (input list) | C | Normalised axial gauge and real agreement: H19, H23. |
| 19023,19069,19079–19089,19126 | 4.5:prf-lattice-stokes | C+ | G4. |
| 19327–19337 | 4.5:lem-window-minimiser | C+ | Ceiling O(1)B₃²ε₁^[15] ≤ a₀ on a later radius. |
| 19806 | 4.5:thm-operator-bounds (F2) | N | Reads (K8) at free current (G8); weakest statement as for 14847–14865. |
| 19876,20110–20123 | 4.5:rem-size-conditions | C+ | Same cube issue as 15707: 12𝔐 cubes are not class cubes when R₁ > 6; use the H14 route with the ceiling stated there. At base one the cap is void, as the row says. |
| 29558–29565 | 4.7:not-true-pairs | N | Reads CMP 109 (1.17) (P9 applied by CMP 109 at complex averages), cited as printed. b102 gives the real-data bound by R3-T1 and the complex continuation by R3-P9, but not (1.17)'s 2B₃α₀′ξ² at complex data; b109 P20 gives only the weaker (110). Weakest statement: (1.17) at the pairs used. |
| 29274–29277 | 4.7:not-step-constants | C+ | C₁^(172) defined by G4. |
| 29325–29333 | 4.7:not-shift-fields | C+ | G4. |
| 30883–30911 | 4.7:prf-lemma-four-gaps | C+ | Sup-Lipschitz bound is H23.3 with B₃ ≥ C (G7); ceiling B₃²O(1)Mα₀ < ½α₁ as in the account; far data through integrated (190). The row then runs the argument on the free-current operator bounds (G8), which b102 does not supply. |
| 32244–32252 | 4.7:prop-beta-extraction (A3) | C+ | N_j's members (value, gradient, Δ, ∂*∂) are in H24.12 (Δ via H20.5 and DD*h = DPD*h). (A3) asks rate δ₀ in dist; b102 gives δ₀/8 in Balaban's d (H13). Read (A3) at rate δ₀/8; I did not check every consumer of (A3) for the rate. |
| 32532,32606–32619,32703–32706 | 4.8:not-regularity-spaces | N | As 29558: CMP 109 (1.17) at complex averages, taken as printed. Real case covered by R3-T1. |
| 32897,32964 | 4.8:def-tower-rules | C | Both rules give admissible towers (G2); complex data by R3-P9. |
| 33245,33269 | 4.8:lem-class-properties | C | Analyticity in the datum (H23). |
| 33620,33679–33682,33792 | 4.8:prf-near-case-labels | C | Uniqueness (R3-T1); continuation (R3-P9); identity datum gives 1. |
| 34064,34149–34159 | 4.8:prop-small-pairs | C | B102 part for both rules, B₃ independent of the cube size. The complex-pair (1.17) is an explicit hypothesis of the proposition, not b102. |
| 34718,34738 | 4.8:lem-layerwise-bound | C | T1 for the re-minimisations; the orbit-form theorem is the account's. |
| 36231–36252 | 4.9:rem-twist-complex-factor | C | R3-T1 (2), (8). |
| 36508,36649–36680 | 4.9:prop-real-backgrounds | C | Trivial (torus) nest admitted (H9); the row builds M′ as a multiple of R₁M₁ with M′ ≤ M(ε₁). |
| 36914–36932 | 4.9:rem-seed-remarks | C | Constant reuse (G3). |
| 37332–37334 | 4.9:prop-ambient-condition | C | Zero-action datum; uniqueness of the minimum (H22). |
| 37907,37956,38043–38045 | 4.9:lem-thin-cube-gradient | C | R3-T1 (8)–(9) on trivial nests. |
| 38511–38529 | 4.10:def-minimiser-continuation | C | R3-T1. |
| 38535–38583,38604–38632 | same (P9.1–P9.4) | C+ | Take 𝓑(V₀) := the retained R3-P9 ball (open, contains 0, \|B(c)\| < π once b_* < π). (b) is H23's gluing on retained balls; (c) H23; (d) H25 on G^c𝒟, so 𝓑(V₀) must also lie in H25's 𝒟: ceiling b_* ≤ r_𝒟 (a ceiling on a radius fixed before a₁). SU(2) only (G1). |
| 38645,38667 | 4.10:def-tower-quantities | C | |
| 39094–39098 | 4.10:prop-continuation-open | C | Open ball. |
| 39176–39177 | 4.10:thm-existence-set | C | |
| 39285 | 4.10:cor-representative-analyticity | C | |
| 39465–39476 | 4.10:rem-representative-assumptions | C | |
| 39499–39500 | 4.10:cor-orbit-extension | C | H25 (SU(2)). |
| 39571–39637 | 4.10:rem-single-valuedness | C | Uniqueness of the fixed point (H20, H23) and real agreement. |
| 39941–39943 | 4.10:prop-tower-clause-open | C | |
| 40109–40112,40159 | 4.10:cor-class-openness | C | |
| 40219–40223 | 4.10:rem-radius-ceilings | C | Threshold ε̄ = b102's final real ceiling (H25). |
| 40422–40428 | 4.11:def-tower-rules | C | |
| 41518–41536,41601,41624 | 4.11:prop-natural-witness | C+ | Ceiling b_H ≤ b_*. |
| 41831 | 4.11:lem-idempotence | C | |
| 41942 | 4.11:rem-no-composition | C | |
| 42094–42097 | 4.11:thm-clause-reproduction | C | |
| 42209–42225,42347 | 4.11:prop-one-layer-clause | C | R3-T1 (8) at ε₁ = 2α′(L^tξ)² ≤ a₁ gives 2B₃α′ξ² and 2B₃α′(L^tξ)². The row states (7) for q-block data; mixed-level plaquettes by G6. |
| 42361–42363,42397–42413 | 4.11:prop-perturbative-clause | C+ | Ceiling b_H ≤ b_*; layered (190) is H24.12 summed (H15.5). |
| 43122–43152 | 4.12:def-constrained-minimisers (b) | N | The 4.12 determining sets are block partitions with neighbouring levels differing by one and no R₁𝔐 gap (CA-I 42991–43000); b102 needs admissible nests above its floors (H9, H21). The uniqueness class (ii) drops the current bound and uses ℓ_𝔅 (smallest nearby block), so it is larger than b102's class. Weakest statement: T1 on the 4.12 partitions in block-scale form, or the 4.12 hypothesis restricted to admissible nests with (ii) taken in b102's class. |
| 43158–43190 | 4.12:def-constrained-minimisers (c) | N | Same class. The block-sum form (b_H, B_H, c_d, δ) would follow from H24.12 by summation on admissible nests; not on the 4.12 partitions. |
| 43380 | 4.12:def-consumer-radii | N | Reads display (b). |
| 43564 | 4.12:def-coupling-thresholds | N | Imports b_H, B_H, c_d, δ of display (c). |
| 44001,44050–44053 | 4.12:lem-minimiser-covariance | N | Uses clause (ii) of display (b). |
| 44168,44248–44255 | 4.12:prop-reblocking-inside | N | Display (b) at reblocked sets 𝔅_E. |
| 44543–44561,44636–44643,44704 | 4.12:prf-below-slot-level | N | Displays (b), (c). |
| 58943 | 4.38:prf-polarisation-limit | C | Uniqueness gives rotation covariance; second derivative at V = 1 by R3-P9. The infinite-volume step is not B102. |
| 60661 | 4.38:rem-locality-induction | C | |
| 88523–88526 | 4.22:rem-gauge-representatives | C | H19 normalised Landau form, H23 axial return. |
| 88639,88655,88781–88784,88865–88869 | 4.22:lem-axialising-map | C | Rate δ₀/8 of (190) converted to the row's δ₁ in d_sc. |
| 120941–120943,121133–121136 | 4.26:prop-near-pairs-outside | C | B₃(L) fixed before the floor on C₁/C₀. |
| 125387–125391 | 4.26:not-arrest-conventions | C | |
| 128914–128925 | 4.26:prf-plaquette-current-entries | C | Current bound B₃ε₁ℓ^{−3} is R3-T1 (class 𝔘_k(B₃ε₁)). CMP 109 (1.16) is CMP 109's. Structures must be admissible nests (G2). |
| 147456–147475 | 4.29:lem-localisation-exact | C+ | Ceiling c_Qℓ_j sup\|𝐇_k\| ≤ b_*. Restriction and uniqueness are the row's hypotheses (1)–(2). The staircase set 𝐁′ must be admissible above G2's floors; the row asserts compatible partitions and I did not check its gap. |
| 147514–147542,147571 | same | C+ | As above; base W₀ = M′(U⁰) real. |
| 147710,147725,147738–147743 | 4.29:lem-collar-staircase (dec) | C | e = 0, 1, 2 with D*D and Δ: H24.12 (Δ via H20.5). Read "∇²" as those two operators; a full second-difference member is not in (190) or b102. |
| 147816,147848–147852,147915 | same | C | P₁ℋ′ = Δℋ′ − D*Dℋ′ + lower order, as the row says. |
| 148819,148828–148832,148894–148902 | 4.29:prop-window-minimiser | C+ | Ceiling B₃·2L²B₃ε₁^g ≤ a₀ (uniqueness class). Truncated set admissible (gap Mℓ_a). |
| 148973–148985 | 4.29:def-path-length-decay (I1) | C+ | Integrated, summed H24.12 gives the layered bound with B₃ ≥ C (G7) and 𝖽_𝐇 ≤ δ₀M/16. |
| 149837–149843,149961–149966 | 4.29:lem-scale-thresholds | N | Clause (b) is covered (H24.12 at b_*). Clause (τ4) reads holomorphy of H_k in the **external** configuration U on 𝔖(Y), with uniform weighted constants. b102 states this only as a sketch (H23 last paragraph; gate-b S3: complex-background H9–H17 not redone). Weakest statement: H9–H18 and H24 at complex backgrounds obeying CMP 99b (3.35)–(3.38). |
| 150100,150119–150124,150180,150282 | 4.29:lem-interpolated-field-bounds | C+ | B(t) in the b_*-ball (ceiling). |
| 150413–150416 | 4.29:prop-near-field-scope | C | Kernel form of H24.12. |
| 151264,151323–151328,151402,151420 | 4.29:rem-transfer-inputs | C | ℋ′ at base W₀ with fixed exterior U⁰ (b102's fixed boundary data). The local problem's reference must be critical (H23.1); the row's restriction hypothesis supplies it. |
| 151767,151773,151917–151918,151938 | 4.29:rem-constants-order | C+ | ε₁^abs := b_*/(2C₁) (G4); B₅ and (19) need gate-b S2. |
| 154052–154066,154134–154140 | 4.31:def-standing-inputs (e) | C | Torus nests; class cubes; translated partitions by H21's arbitrary centre and uniqueness. |
| 154690–154693 | 4.31:prop-fixed-depth-convergence (I5) | C | Aligned class cubes. |
| 155046–155079,155092 | 4.31:lem-window-characteristic | C | w ≤ a₁, B₃w ≤ ε_k; CMP 119 minimal determining sets are r₂ towers (G2). |
| 155104 | 4.31:lem-charts-gluing | C | R3-T1 at ε₁ = w_s; the gluing uses the account's complex-background construction. |
| 155248,155278,155321,155339 | 4.31:lem-background-membership | C | M″ a multiple of R₁M₁, M″ ≤ M(w_s). |
| 155647–155657,155690–155691 | 4.31:prf-marginal-cube-gauge | C | |
| 155866,155956–155989,156040–156067 | 4.31:prf-marginal-minimiser-path | C+ | (W1)–(W2) at base 1 are R3-P9 (ℋ(0) = 0, N(ℋ) ≤ C\|D\|, plaquette and current by H20's expansion, uniqueness of the chart fixed point, real agreement, constant-gauge covariance by H25). Ceiling β_W ≤ b_*. |
| 157470–157481,157521 | 4.35:prop-gauge-fixing (B) | C | |
| 158215–158216,158232–158252 | 4.36:not-flow-thresholds | C+ | C₁^(102) by G4; a₁′ read as b102's final real ceiling. |
| 160157–160174,160187–160201,160288–160303 | 4.36:def-unit-directions | C+ | G4; SU(2) only (G1). |
| 160601,160617–160638,160734–160738 | 4.36:lem-broken-paths | C+ | r₀ ≤ C₁a₁′/4 ≤ b_* by G4. |
| 160800–160825,160840 | same | C | First member and η\|ℋ\| ≤ C_H\|v′\| (H23.3, H24.12); base curvature R3-T1 (8). |
| 160924–160969,161262 | 4.36:rem-normalisation-inputs | C+ | G4 (\|V′ − 1\| < C₁ε₁ in \|·\|). |
| 161303,161324–161330,161465,161672 | 4.36:lem-one-link-curvature | C+ | \|ζ\| < 2r₀ with r₀ ≤ C₁a₁′/4: G4. Plaquette formula from R3-T1 (8) and H20's expansion. |
| 161723–161724,161789–161843 | 4.36:rem-curvature-readings | C | (190) is in the operator norm \|·\|. |
| 161964–161975 | 4.36:rem-frozen-background | C | |
| 163160,163174 | 4.36:rem-order-of-choice | C | B₃(L) before A₀/A₁. The SU(N) reading is G1. |
| 163377,163438 | 4.36:not-sun-conventions | C | For N = 2. For N ≥ 3: N (G1). |
| 163795–163834,163932 | 4.36:not-probing-direction | C+ | r₀ ≤ ¼C₁^(102)a₁′: G4. |

### 3.2 Clear uses in CA-II (54 rows)

| Row (II:) | Statement | Verdict | Reason, ceiling, or weakest statement |
|---|---|---|---|
| 2165–2168 | 5.1:def-admitted-inputs | C | |
| 3996–3998,4044 | 5.2:prop-box-comb-gauge | C | B₃ as the Lipschitz constant: G7. |
| 4149–4150 | 5.2:rem-own-box | C | |
| 4608,4662–4668 | 5.2:lem-extraction-cost | C+ | The row writes ‖𝗁_x‖ ≤ B₃e^{−δ₀dist(x,X)}; b102 gives rate δ₀/8 in Balaban's d (H24.12, H13). Read it at that rate, with B₃ ≥ C (G7) and Cauchy radius r_○ ≤ b_*. |
| 9004 | 5.2:lem-random-walk-bounds | C | |
| 9407–9411 | 5.2:lem-almost-invariance | C | The minimum is over regular U′, as H22 gives. |
| 10231–10237,10322–10323,10344,10365–10369,10434 | 5.2:cor-true-pair-positivity | C+ | Cube parameter M must be a multiple of R₁M₁: true by G2 (𝔐 a power of L), since M and R₁ are powers of L. Ceiling M ≤ M(ε_data) on γ, as in the row. |
| 10608–10610 | 5.2:lem-response-containment | C | |
| 13717 | 5.2:lem-animal-resummation | C | |
| 17530–17533,17551–17553 | 5.2:def-plain-interior-units | C | |
| 34841 | 5.5:def-weight-constants | C | |
| 35582–35587 | 5.5:lem-weight | C | Residual gauges are 1 at determining sites (b102 §1). |
| 35633,35647–35652 | 5.5:prf-box-regularity | C | 𝔅_p(Q) is a maximal (r₁) tower (G2). |
| 35669–35675,35705–35706 | same | C+ | ℓ\|ℋ\|, ℓ²\|∇ℋ\|, ℓ^{2+β}‖∇ℋ‖_β ≤ K_h sup\|B\|: H23.3 and H24.10–H24.11 integrated (β = β_H < 1). Ceiling: the data radius under c_h is ≤ b_*. |
| 43034,43096,43124–43143 | 5.5:def-remainder-constants | C | |
| 43653,43675–43680 | 5.5:prf-box-field-charts | C+ | 𝒪 inside the b_*-ball. |
| 44016–44021 | 5.5:thm-membership-remainder | C+ | The argument's domain bound ≤ b_*. |
| 44402–44405,44415–44420 | 5.5:cor-thin-layers | C+ | 1.2α_{3,j}/L ≤ b_*. |
| 50317–50320 | 5.7:prop-response-zeroth-order | C+ | a_Λ ≤ b_*. |
| 50809–50812 | 5.7:not-canonical-loops | C+ | The ball containing B₀, B₁ lies in the b_*-ball about real V₀₀. |
| 50918–50923 | 5.7:lem-native-loop-closeness | C | Hölder exponent below 1 (gate-b S1). |
| 52177–52181 | 5.7:prop-critical-layer-closeness | C | |
| 58995 | 5.9:def-variation-hypotheses | C | (181): H25. |
| 59247–59250 | 5.9:thm-low-order-variation | C | |
| 69929,70014–70016 | 8.1:lem-kernel-bounds (h1) | C | T1 (9)–(10) carry no kernel; the linear-minimiser kernel bounds are H24.12 at B = 0 (and H13/H15). The free-current operator theorem in (h1) is G8. |
| 71256–71261 | 8.1:rem-extraction-errors | C | |
| 75244–75252,75356 | 8.2:lem-curvature-contraction (I) | N | (5) bounds V_{j,n}'s curvature by B₃L^{−2n} times the max of V over a **fixed finite neighbourhood** 𝒩(p̄_{j+n}). R3-T1 is global: it gives the same with the max over all plaquettes of V (constant 2B₃ after CMP 98 Prop. 2, G6). The local form has no tail term and does not follow from T1; I expect it is false (a datum curved only outside 𝒩 gives a nonzero, exponentially small response), not proved here. (I) also asserts the minimum "over the configurations", which b102 does not prove (G9). Weakest statement b102 supports: (5) with the global sup. |
| 85642,85655–85657 | 8.4:not-step-zones | C | Read "minimal" as G9. |
| 85786,85794–85796 | 8.4:not-box-variation | C+ | B₅ needs gate-b S2; c_* = b102's C. |
| 85913–85956 | 8.4:def-response-hypotheses (a1)–(a7) | C+ | (a1)–(a5), (a7) are H19, H23, H24.12 (functional derivative with ℓ⁴ measure; curl ≤ 2 × covariant difference for (a4)). (a6): a₉ := b_*. |
| 85974–85987 | same (c1) | N | (c1) asks R3-T1/P9/(190) for (𝐁_j, V^base) under (7♭): (7) everywhere **except** deep zone-0 plaquettes, which may be large-field. R3-T1 needs (7) on all plaquettes, and its class 𝔘 includes zone-0 plaquettes, so it fails as stated. The account itself says the transfer is assumed. (7♭) gives regularity only on a zone-0 collar about one step wide, so the nest (Ω₀′ ⊃ Ω₁ ⊃ ⋯) with Ω₀′ = Ω₁ plus that collar violates the gap > R₁𝔐 of G2. Weakest statement that makes b102 apply: (7) on a block-aligned zone-0 collar Ω₀′ \ Ω₁ of fine width > R₁𝔐 around Ω₁. Then R3-T1, R3-P9, R3-(190) hold for (Ω₀′ ⊃ Ω₁ ⊃ ⋯) with V₀ as Dirichlet data outside Ω₀′ (H9's outer boundary), and 8.4:lem-zone-zero-invisible identifies this problem with the row's. |
| 86161 | 8.4:def-far-member-hypotheses | C | Comparison remark. |
| 86291–86300 | 8.4:not-decay-weight | C | b102's d is CMP 96 (2.46) (H13). The comparison with dist_j or ρ_sc is the row's own hypothesis. |
| 86786–86807 | 8.4:lem-far-member (hypotheses) | N | Assumes (c1). |
| 86835,86866 | same | C+ | a₉ ≤ b_*; the gradient member is covariant at the reference (H24.12). |
| 86904–86912 | same | N | The application of T1/P9 to V^base goes through (c1). |
| 86983–87002 | same | C | Given (c1): holomorphic composition on the tube, sup\|B\| < a₉. |
| 87015–87022 | same | C | Given (c1): real agreement, Landau form with fixed base. |
| 87078–87094,87156 | 8.4:prf-far-member-proof | C | Given (c1): both members at every B of the ball, rate δ₀/8. |
| 88384–88389,88428–88435 | 8.4:rem-own-scale-smallness | N | Same (c1) transfer. |
| 95939–95969 | 8.5:def-critical-backgrounds | C | M_Q a multiple of R₁M₁, as in R3-T1. |
| 96003–96034,96061–96122 | 8.5:lem-background-regularity | C+ | Ceiling M_Q ≤ M(ε′) on ε′. |
| 96156–96159,96224–96234 | 8.5:lem-vacuum-subtraction | C+ | α_{3,j} ≤ b_*; the U_j^flat membership is the row's hypothesis. |
| 97407–97412 | 8.5:lem-insertion-sup | C | |
| 97568–97571 | 8.5:thm-averaged-extraction | C | |
| 99758,99774–99778,99804–99806 | 8.5:lem-minimiser-regular | C+ | Hölder with B₄(β), β < 1; cube M a multiple of R₁M₁ (as above) with M ≤ M(ε′). |
| 101126–101128 | 8.5:lem-branch-comparison | C | The (190) decay it rests on is H24.12. The domain-uniform localisation itself (global versus Ω-local minimiser) is the account's derivation, not a b102 statement. |
| 106924–106931 | 8.6:prop-exponential-moment (i) | C | Local problem on □̃: its sup is local, so R3-T1 gives C_B = cB₃, α_B ≤ a₁/c (G6). |
| 109951–109966 | 8.8:lem-stability-exponent | C | Ceiling 4g_k ≤ a₁. |
| 117626 | 8.10:prop-window-lower-bound | C | |
| 119733–119739 | 8.11:not-units-cap-amplitude | C | |
| 138407–138410 | 8.17:not-top-step-notation | C | Continuity from R3-P9 on the crude-regular class (admitted data). |
| 139604–139608 | 8.17:lem-crude-short-move | C | |
| 139967–139974 | 8.17:prop-short-move-construction | C+ | Base is a real regular datum; Cauchy on \|t\| ≤ α_P/4 needs α_P/4 within b_*. |

### 3.3 Clear uses in CA-III (26 rows)

| Row (III:) | Statement | Verdict | Reason, ceiling, or weakest statement |
|---|---|---|---|
| 1065 | 9.1:not-constant-order | C | G3. |
| 2194,2345,2389–2390 | 9.1:lem-glued-minimisers | C | |
| 2919,2939 | 9.1:prop-hull-step | C+ | r_c ≤ b_*. |
| 2999,3025–3030 | 9.1:lem-hull-exactness | C+ | r_c ≤ b_*. |
| 6362 | 9.1:lem-slice-displacement | C | |
| 7265–7269 | 9.1:cor-tolerance-rooms | C | P9 part. The "operator theorem at free current" item is G8. |
| 18821 | 9.1:def-seed-criticality | C | |
| 19103–19106 | 9.1:rem-cellwise-increments | C | |
| 19435 | 9.1:lem-core-gauge | C | (T2) of b102 §1. |
| 19882–19884 | 9.1:cor-seed-rotation | C | |
| 22139,22178 | 9.1:def-natural-vertex | C | (189), (190) at vertices: H24.2, H24.12. The (180) operator bounds "in a strengthened form" in the same list are a separate input; not checked here. |
| 31748 | 9.2:not-parameters-couplings | C | |
| 34767–34840 | 9.3:not-minimiser-bounds | C | Two depths; Hölder exponent θ < 1. Cubes must be class cubes or use the H14 route (as at CA-I 15707). |
| 35173–35176 | 9.3:lem-gauge-fixing | C | |
| 35740–35749 | 9.3:thm-stationarity-minimisers | C | H24.2: rate δ₀/4, r for ε₃, N(A′) ≤ r for (77), N = max{\|·\|₍₋₁₎, \|∇·\|₍₋₂₎}. |
| 35794–35796 | same (torus case) | C | Uses CMP 102 (98) (H4.1/H6), not (189). |
| 35913–35916 | 9.3:cor-stationarity-level-data | C | |
| 36002–36007 | 9.3:not-perfect-action | C+ | Replace "C₁ε₁ ≥ r_c" by r_c ≤ b_*; base at ε = a_A/2 needs a_A ≤ 2a₁. |
| 36252–36256 | 9.3:thm-stationarity-jets | C | \|V′(A′)\|₍₋₃₋θ₎ ≤ Cε₂‖A′‖_θ is the account's integration of (189) along tA′ (V′(0) = 0); with H24.1's exponential weights the level reweighting L^{θ\|j−j′\|} is summable once δ₀R₁𝔐/4 > θ log L (a floor on R₁, placed before a₁ by G3). |
| 36300–36314 | same | C+ | First (190) member: H24.12. "ℋ obeys (19)–(21) with B₅ε₁": needs gate-b S2. |
| 36721–36728 | 9.3:thm-stationarity-covariance | C+ | Response decay (first member) and Cauchy at tube radius r ≤ b_*. |
| 36974–36990 | 9.3:lem-refinement | C+ | Ceilings 2B₃ε ≤ a₁ and 2B₃²ε ≤ a₀; the refined sequence must be admissible above G2's floors. |
| 37006–37015,37026–37030 | 9.3:lem-response-decay | C+ | r_c ≤ b_*; ℋ(0) = 0. |
| 37042–37048 | same | C | First two members along tB; coordinate derivative = ℓ_{y′}⁴ × functional kernel. |
| 37147–37152 | 9.3:prf-local-backgrounds | C | |
| 37324–37330 | 9.3:rem-large-field-regions | C | |

The three source declarations themselves are covered for SU(2): CA-I 35144–35199 (b102 §1 (T4)–(T5) are its cube clauses; gate-b: "covers what CA-I 4.9 quotes"), CA-II 85845–85895 ((a) uniqueness in B₃ε̂₁ ≤ ε̂₀ ≤ a₀; (b) the first two members at δ₀/8 with (L^{n′}η)^{−d}), CA-III 35577–35626 ((189) = H24.2; first (190) entry = H24.12).

### 3.4 Ambiguous mentions, proposed routes, negative uses, inventories (20 rows)

"n/a" means the row applies none of the four results, so nothing is needed from b102.

| Row | Statement | Verdict | Note |
|---|---|---|---|
| I:10065–10072 | 4.4:def-group-factor-bounds | n/a | Rejected route needing 4B₃ ≤ L². b102 chooses B₃ ≥ 72d³L³B₀S_* (H21), with S_* ≥ 1 and B₀ ≥ 1 (an upper-bound constant that may be enlarged), so 4B₃ > L² for every L: b102 does not revive this route. |
| I:15931–15951 | 4.5:rem-condition-iv | n/a | |
| I:16701–16703 | 4.5:prf-increment-kernel | n/a | (19)–(21) not used; b102 does not state it either (gate-b S2). |
| I:20141–20142 | 4.5:rem-not-asserted | n/a | Free-current members not asserted; consistent with G8. |
| I:34928,35007–35018 | 4.8:rem-literal-inclusions | n/a | With b102's B₃, closure would need L^{2g} ≥ 288d³L³B₀S_*(1 + β) at least; not used. |
| I:45179–45190 | 4.13:lem-minimizer-unique | N | Proof outstanding in the account. b102 supplies part: H22 makes the orbit the unique minimum over the regular class, which gives the account's third step and the uniqueness half of its second. Still open: admitted fields satisfy (7) with ε₁ ≤ a₁, and every minimiser of CMP 109 Lemma 4's problem lies in 𝔘_k(a₀) (b102 gives no unrestricted minimum, G9). |
| I:44893,44936–44963 | 4.12:rem-refined-minimiser | n/a | |
| I:131690–131692 | 4.27:lem-t-step-layer | n/a | b102 does not change this: R3-P9 is at admitted real bases, and its external-background chart reads CMP 99b (3.38) and is a sketch. |
| I:155507–155512 | 4.31:rem-non-minimiser-data | n/a | |
| I:154200–154230,154275–154291 | 4.31:def-complex-background (W1)–(W2) | C+ | At base 1 these follow from R3-P9 (bounds from H23.3 and H20's plaquette and current expansions; normalised uniqueness from H20's unique chart point; real agreement; constant-gauge covariance from H25 at real gauges and the identity theorem). Ceiling β_W ≤ b_*. |
| I:164436,164531 | 4.36:prf-regular-absorption | n/a | |
| II:54241–54243 | 5.8:rem-kernel-rates | n/a | |
| II:54659–54660 | 5.8:prop-local-decay | n/a | |
| II:114770 | 8.10:def-window-structure (route) | C | R3-T1 gives the local minimiser's regularity B₃ε₁ from the data's ε₁ on admissible local nests; extracting B_W from it is the row's step. |
| I:166573,166633 | inventories | n/a | |
| II:60248–60253,60315 | 5.13:prop-sun-correlation | N for N ≥ 3 | G1. |
| II:145545–145547 | inventory | n/a | Its inputs are covered as in §3, for SU(2). |
| III:75776–75781 | inventory | n/a | |
| III:110946 | synthesis | n/a | |
| III:111362 | Ch. 13 inventory | C | The account lists "the passage between (189) and (190)" as outstanding. H24 (H24.3)–(H24.12) supplies it; gate-b: ADVANCE. |

## 4. Summary

Counts (rows of §3.1–§3.3, 188 in all): CA-I 108 rows: 57 C, 38 C+, 13 N. CA-II 54 rows: 34 C, 15 C+, 5 N. CA-III 26 rows: 19 C, 7 C+, 0 N. Plus §3.4 (20 rows): 2 C, 1 C+, 1 N, 1 N for N ≥ 3 only, 15 n/a. All verdicts are for SU(2); every row is N for N ≥ 3 (G1).

**Not covered, ranked by what each breaks.**

1. **CA-II 8.4 (c1), the transfer under (7♭)** (II:85974–85987, 86786–86807, 86904–86912, 88384–88435; the far-member rows 86983–87156 are covered only given it). The small-field step's response at base data with level-0 large-field regions needs T1/P9/(190) with (7) and the regular class read only on plaquettes meeting E₁ ∪ C₀. b102 states both globally. The account says the transfer is assumed. Weakest statement: (7) on a block-aligned zone-0 collar of fine width > R₁𝔐 around Ω₁ (then b102 applies with Dirichlet data outside it); (7♭) gives only a collar about one step wide. It sits on the large-field route: base data with level-0 large-field regions.
2. **CA-I 4.12, the block-scale displays (b), (c)** (7 rows, I:43122–44704). The 4.12 determining-set hypothesis admits block partitions without the R₁𝔐 gap, and its uniqueness class drops the current bound. The hypothesis abstracts CMP 122a's large-field determining sets, CMP 119's minimal determining sets and CMP 109's maximal domains (CA-I 43060–43064), so this gap is also on the large-field route. Weakest statement: restrict the hypothesis to admissible nests (if the level function and the boundary tower both come from admissible nests, their minimum is admissible: unions of aligned blocks, gap ≥ the smaller gap) and read clause (ii) in b102's class; the block-sum form (c) then follows from H24.12 by summation. Not done here.
3. **Free current (G8)** (I:14847–14865, 15125–15432, 19806; partly I:30883, II:69929, III:7265). b102 proves (K8)-type bounds only at J = J(U). Weakest statement: H18 and H24 with the current a free variable of small (−3) norm.
4. **CMP 109 (1.17) at complex averages** (I:29558–29565, 32532–32706). Not CMP 102 content. b102 supplies the real-data bound (R3-T1) and the continuation (R3-P9); b109 P20 supplies only the weaker (110).
5. **CA-II 8.2 (I), strictly local curvature contraction** (II:75244–75356). Stronger than T1 and probably false as stated (no tail term). b102 supports the global-sup form with constant 2B₃.
6. **CA-I 4.29 (τ4), holomorphy in the external configuration** (I:149961–149966). b102 has a sketch only (H23, gate-b S3).

**Covered after ceilings that must be written somewhere** (none creates a cycle):

- G3: in CA-I Stage 5, place a₀, a₁ (and b102's chart radius b_*) after R₁; no floor on R₁ reads a₁.
- G2: 𝔐 a power of L and a multiple of M_P; R₁𝔐 above b102's localisation length and H14's auxiliary collars.
- G4: fix C₁ before a₁ and require 2C₁a₁ ≤ b_*; each named radius (b_H, a₉, r_c, β_W, a_Λ, α_{3,j}, α_P, 2(α₁ + h), c_Qℓ_j sup\|𝐇_k\|) at most b_*.
- The 12𝔐 cubes of CMP 99b (3.35) (I:15707–15735, 19876–20123): M′ = 6𝔐 is not a multiple of R₁𝔐, so neither printed T1 nor R3-T1 applies as the account reads it; R3-T1 regularity plus H14.1 covers them after one more entry in ε̄₁.
- Rates: CA-I (A3) and CA-II 5.2:lem-extraction-cost ask decay e^{−δ₀dist}; b102 gives δ₀/8 in Balaban's d. Read them at δ₀/8.
- B₅ and the (19)–(21) clause (I:1340, 151767; II:85786; III:36300): gate-b S2's one-line clause must be written into b102.

**What b102 adds to the account.** The account's outstanding "passage between (189) and (190)" (CA-III 111362) is supplied by H24. The proof-outstanding 4.13:lem-minimizer-unique gets its uniqueness step from H22, leaving two named sub-steps.

Not checked here: the account's own arguments in each row; whether each local, staircase, refined or box determining set the account builds is admissible above b102's floors (I took the account's admissibility claims as given wherever it makes them); every consumer of (A3) for the rate change.

Checked line by line by Claude (Mini worker).
