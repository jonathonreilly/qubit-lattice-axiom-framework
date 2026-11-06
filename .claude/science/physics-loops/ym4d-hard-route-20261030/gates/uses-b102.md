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
