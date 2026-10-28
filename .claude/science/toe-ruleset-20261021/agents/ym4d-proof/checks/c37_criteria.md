# c37 criteria (written before any c37 script; session 21, 2026-10-28 UTC; targets RTARGET.md §46 A)

Run discipline: machine-wide numeric lock (`until mkdir …/locks/numeric; do sleep 20; done`, run, `rmdir` exactly once, no
trap), nice 10, OPENBLAS/OMP/MKL/vecLib threads 1, load (1-min) < 8 and memory ≥ 25% free before each job, peak memory
< 1 GB, no `timeout`, python without -I. A FAIL is recorded as a FAIL; no criterion is edited after a run. Parts are
independent: `python3 c37_kcurv.py A|B|C|D|E`.

Objects (abelian, trivial background, d = 4, L = 3, κ ≡ 1 unless stated; the SU(N) linearisation is this ⊗ 1 on su(N), and
the ℓ^∞ → ℓ^∞ norm with HS block norms equals the scalar one, so no separate SU(N) run). Õ_0 = ΠO_0Π + (1 - Π),
O_0 = d*d + κQ^TQ + dP_resd* (c35 AbOp), C^0 := Õ_0^{-1} - (1 - Π). ι: coarse plaquettes → fine plaquettes, the L^{d-2} = 9
block-corner plaquettes (x_μ ≡ x_ν ≡ L - 1) of each coarse plaquette (Lemma U0 (ii)); J: the lift (Lemma U0), coarse link
→ its 27 crossing fine links. Linearised branch at the trivial background: x = -C^0d*ιF_V (BR1's fixing), F_1 = 𝒦F_V,
**𝒦 := ι - dC^0d*ι**, ρ = 𝒦_ρF_V, **𝒦_ρ := -QC^0d*ι**. K_p := max fine-plaquette row ℓ¹ norm of 𝒦 (block norms scalar),
K_ρ := max coarse-link row ℓ¹ norm of 𝒦_ρ, **K_curv := max(K_p, K_ρ)**. Kernels by Bloch fibres on the coarse torus of side
T (unit cell = one block: 324 links, 486 plaquettes), inverse FFT; torus kernels include aliasing.

## A. Validation (coarse torus T = 3, fine side 9, direct real space vs Bloch)
- A1: Q J = 1 and d J = ι d_1 (d_1 the coarse curl) for a random coarse field, max abs error ≤ 1e-12.
- A2: for each of the 6 unit coarse plaquettes δ_P at the origin, (ι - dC^0d*ι)δ_P and -QC^0d*ιδ_P computed directly
  (C^0 by CG on Õ_0, relative residual ≤ 1e-12) agree with the Bloch kernel on the (2π/3)Z⁴ grid to ≤ 1e-8 × (max abs
  entry).
- A3: for 20 random K on the (2π/8)Z⁴ grid, every eigenvalue of the fibre d(K)C^0(K)d(K)^† lies in [-1e-10, 1 + 1e-10]
  (REVIEW_S20's 0 ≤ dCd* ≤ 1).
PASS iff A1-A3.

## B. Main: K_curv at κ = 1 (pre-registered "K_curv < 1")
K_p(T), K_ρ(T) for T ∈ {6, 8, 10}; report the arg-max rows, the max imaginary part of the kernels, and the decay profile
(max entry of 𝒦 by coarse ℓ^∞ distance) at T = 10.
PASS iff K_curv(10) < 1 and |K_curv(10) - K_curv(8)| ≤ 0.02.

## C. Informational: attained ratios and the exact norm on exact inputs
- C1 (T = 10): sup|F_1|/sup|F_V| and sup|ρ|/sup|F_V| for F_V = d_1a with (i) a = one unit coarse link, (ii) Gaussian random
  a (3 seeds), (iii) a smooth a (a_0(X) = sin(2πX_1/T), other components 0). Lower bounds for the norm on exact inputs.
- C2 (T = 6): the exact torus norm of a row on exact inputs, max_a (row of 𝒦d_1)·a subject to |d_1a|_∞ ≤ 1 (HiGHS LP, box
  |a| ≤ B for the gauge recession directions; reported for B = 50 and B = 100), for the 16 fine-plaquette rows of 𝒦 with the
  largest row sums and the 4 coarse-link rows of 𝒦_ρ; reported against the row sums.

## D. Informational: κ-dependence and the displacement / branch-derivative factors
- D1 (T = 8): K_p, K_ρ at κ ∈ {0.25, 4, 16}.
- D2 (T = 8, κ = 1): K_A := row-ℓ¹ norm of F_V ↦ x; for SC1's branch derivative a' := κC^0Q^T (coarse → fine):
  Z_row := max_b Σ_c|a'(b, c)|, Z_col := max_c Σ_b|a'(b, c)|, and the products Z_col·Z_row², (1 + Z_col)·max(1, Z_row)².

## E. Informational: level 1 against level 0 at equal torus size (level-2 torus side 4, c36 D's construction)
Ĥ_1 on the level-1 grid (2π/12)Z⁴ by the Schur formula (as c36 D), Õ_1(K2) fibres on (2π/4)Z⁴, C^1 := Õ_1^{-1} - (1 - Π).
Level-i linearised branch on the a-variables: F = d(J - C^iH_iJ)a, ρ = -QC^iH_iJa (H_0 = d*d, H_1 = Ĥ_1).
- E1 (validation): max_K ||𝒜_i(K)d_0(K)|| ≤ 1e-8 and the same for the ρ map (the coarse gauge mode is annihilated), for
  i = 0, 1; c36 D1's per-mode value 0.030950 reproduced to relative 1e-4.
- E2: the exact torus norm on exact inputs (LP as in C2, B = 50) for every fine-plaquette row and every coarse-link row,
  level 0 on the side-4 coarse torus and level 1 on the side-4 level-2 torus; report max over rows, K_p^{(i)}(4),
  K_ρ^{(i)}(4).
E reports numbers only if E1 holds.
