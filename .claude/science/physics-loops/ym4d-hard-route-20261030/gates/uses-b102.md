lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T15:04Z

# uses-b102: coverage of the CMP 102 uses by `library/b102.md` round 3

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout `ee70ee2e6`, started 2026-11-06T03:04Z.
One reading by one model; not an audit; grants no status.

Status: in progress. Sections are written as the check proceeds.

Scope: every row of `library/uses-old.md` §5 (I: 108 rows, II: 54 rows, III: 30 rows, plus the 20 rows of "ambiguous mentions"), checked against `library/b102.md` round 3 (§8, H15–H25, and the Result), with H1–H14 as its inputs. For each row I read the cited lines of CA-I/II/III at `31a47c543775` (fetched by URL into a scratch folder; CA-I SHA-256 `4cb5cb5e…` matches b102 §1). I read the b102 statements H19–H25 in full and the two gate reports `gates/b102-gate-a.md`, `gates/b102-gate-b.md` (both: first failing step none). No numerical run was used.

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
- **G2, nest floors.** The account reads CMP 102 (1) as: each Ω_j a union of blocks of side 𝔐ℓ_j, gap (ℓ_j)^{−1}dist(Ω_j^c, Ω_{j+1}) > R𝔐 with R ≥ R₁, torus domains admitted (CA-I 12676–12722; CA-III 34660–34668). It leaves 𝔐 and R₁ as "sufficiently large, depending on (d, L) only, such that the theorems hold". b102's floors (R3-T1) read only L and the group. **Ceiling (a floor here):** take 𝔐 and R₁ above b102's floors. No cycle.
- **G3, order of a₀, a₁.** b102 chooses R₁M₁ before its chart radii and before a₀, a₁ (H21 last paragraph; §5 step 5: a₅ ≤ [8C(R₁M₁)²]^{−1}, C R₁M₁ B₃ a₁ ≤ 1/4). The account lists "the determined letters B₁, B₃, B₅, a₁" before "R₁, chosen upward" (CA-I 1509–1511, 2062–2064). **Repair:** place b_*, a₀, a₁ after the last floor on R₁𝔐. I found no floor on R₁ that reads a₁ (all floors on R₁: CA-I 2064, 12691, 12717, 13415–13416; CA-III 21144), so there is no cycle. R₁M₁a₁ ≤ 1/(4CB₃) stays a fixed positive number, so the account's ceiling (2.3:eq-stages-middle-1) stays a ceiling on ε^run.
- **G4, the (172) radius.** The account reads (172) as: |V′ − 1| < C₁ε₁ gives logarithms in |B′| < 2C₁ε₁, and uses the margin sup|B| ≤ ½C₁ε̄₁ (CA-I 13128–13134, 16567–16569). b102 has no constant C₁ of (172); its ball has the fixed radius b_*. **Ceiling:** fix C₁ (any number fixed before a₁, e.g. L³) and require 2C₁a₁ ≤ b_*. This is a ceiling on a₁, which b102 chooses last; no cycle. Then every account polydisc of radius ≤ 2C₁ε₁ with ε₁ ≤ a₁ lies in the R3-P9 ball.
- **G5, named constants.** a₀, a₁, B₁ (H19), B₃, B₄(β₀), M(ε₁), R₁M₁, δ₀ and c_* (= b102's C in H24.12) are b102 constants. B₅ is not in the b102 text (needs gate-b S2). C₁ is defined by G4. The account's Hölder exponent β_H ∈ (0, 1) (CA-I 1377) is inside b102's range β ≤ β₀ < 1.

"Covered" below means: the statement the row reads is an R3 statement, or its immediate specialisation, at the radius, domain and constants the row reads, given G1–G5. It does not check the row's own argument.
- **G6, the datum condition.** R3-T1 reads (7) in the mixed-level form (b102 §1: same-level plaquettes alone are insufficient). Where a row states (7) for block data of one real field, the mixed-level plaquettes follow from CMP 98 Proposition 2 (the account's own step, e.g. CA-I 16494–16498); that step is the row's, not b102's.
- **G7, constants named B₃ or c_*.** Where a row uses "B₃" as the constant of a P9 or (190) bound (not the regularity constant), b102's constant C of H23.3 and H24.12 is built from operator constants fixed before B₃ (H21 order), so B₃ may be taken ≥ C. No cycle.

## 3. Verdicts per row

Codes: **C** covered (given G1–G7); **C+** covered after the stated ceiling or change; **N** not covered (reason; weakest statement needed). b_* is the R3-P9 ball radius.

### 3.1 Clear uses in CA-I (108 rows)

| Row (I:) | Statement | Verdict | Reason, ceiling, or weakest statement |
|---|---|---|---|
| 1031–1035 | 1.5:def-domains | C | (R4) tower minimisers: R3-T1 at real data, R3-P9 at complex data within b_* of the real factor's data; both tower rules are admissible (CA-I 32834–32894), so G2 applies. |
| 1340;1510,1559;1670 | 2.3:not-stages-* | C+ | G3 (a₀, a₁ after R₁); B₅ needs gate-b S2 written into b102. |
| 2063,2094 | 2.4:lem-no-cycle | C+ | G3. With it the no-cycle claim stands; R₁M₁a₁ stays a fixed number. |
| 3136 | 3.1:thm-main (pointer) | C | Pointer to the Ch. 8 uses (II:71256 row). |
| 3791 | 4.2:def-increment | C | The torus linearisation at V = 1 is R3-P9 at B = 0 (h = H₀w). The ℤ⁴ limit 𝔥_∞ in the same definition reads CMP 99b Thms 3.10, 3.12, not CMP 102; b102 gives only volume-uniform torus kernels. |
| 10163–10202 | 4.4:not-response-bound | C | Second case: five members at real bases, complex data in (172) ⊂ b_*-ball (G4). The account's "P₁ member" is covered: P₁ = D_UPD_U*, and P₁h = DD*h when RD*h = 0 (H24 3366–3368, H17.5). The free-current first case is the account's own (G8 below). |
| 10516–10522 | 4.4:lem-twist-stability (hyp.) | C | As the previous row; B₃ plaquette bound is R3-T1 (8). |
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
| 160924–160969,161262 | 4.36:rem-normalisation-inputs | C | |
| 161303,161324–161330,161465,161672 | 4.36:lem-one-link-curvature | C | |
| 161723–161724,161789–161843 | 4.36:rem-curvature-readings | C | (190) is in the operator norm \|·\|. |
| 161964–161975 | 4.36:rem-frozen-background | C | |
| 163160,163174 | 4.36:rem-order-of-choice | C | B₃(L) before A₀/A₁. The SU(N) reading is G1. |
| 163377,163438 | 4.36:not-sun-conventions | C | For N = 2. For N ≥ 3: N (G1). |
| 163795–163834,163932 | 4.36:not-probing-direction | C | |

**G8, free current.** b102 proves its operator, Hessian and response bounds only at the physical current (H18 "at the **physical** current"; H24 "physical-current versions"). The account's chart bounds at an independent current (CA-I 4.5 (K8), (F2), the chart constants) are the account's own lemmas, proved there from its free-current operator inputs; b102 supplies them only on the diagonal J = J(U).
