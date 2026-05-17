# Route Portfolio

## Target 1: F1-vs-F3 canonical weighting selection (BAE residual)

| Route | Probability | Closure type | Cycle priority |
|---|--:|---|---|
| (c) NCG spectral triple / KO-dimension with explicit J | **18%** | Positive closure via real-structure isotype collapse | **CYCLE 1 (parallel A)** |
| (b) Cl(3) bivector irrep on dim-2 spinors | **14%** | Positive closure via bivector Hodge collapse | **CYCLE 1 (parallel B)** |
| (d) Alternative Plancherel on SU(2) | 9% | Requires lifting C_3 → SU(2) — likely import | Cycle 2 if (b)+(c) fail |
| (a) SUSY oscillator decomposition (Z3-graded) | 8% | Bargmann-Fock measure, but C-linear risk | Cycle 2 if (b)+(c) fail |
| (e) Literature canonical principle import | 4% | Forbidden as PDG import | Skip |
| **(f) Honest bounded no-go via N1-N8 battery** | **47%** | Negative result with full discipline | **CYCLE 2** (if positives fail) |

## Target 2: Numerical u_0(SU(2)) (g_2(v) chain residual)

| Route | Probability | Closure type | Cycle priority |
|---|--:|---|---|
| (e) Honest gap — narrow rescope with admitted lit import | **82%** | Bounded interval (Path B) | **CYCLE 1 (parallel C)** |
| (c) Match-to-literature + frame uniqueness | 8% | Bounded with named lit admission | Subsumed by (e) |
| (b) Strong-coupling truncated series | 5% | Bounded at small β only | Cycle 2 if (e) doesn't land |
| (a) Analytic Lüscher tadpole | 3% | No closed form exists | Skip |
| (d) SU(3) template port | 2% | Vacuously applicable, no new content | Skip |

## Cycle 1 dispatch

3 parallel agents, isolated worktrees, science block branches off origin/main:

**Agent A: NCG/KO-dimension route on F1-vs-F3** — `physics-loop/bae-ncg-kodim-block01-20260517`
- Build real spectral triple (A_F, H_F, D, J, Gamma) with A_F = circulants, D = H_circ, J = complex conjugation
- KO-dim conditions force J to swap omega and omega^* characters
- Spectral action heat-kernel weights pick J-fixed real bimodule
- Test whether this enforces F1 isotype counting
- Open imports allowed: KO-dim formalism (Connes-Chamseddine) with explicit ADMITTED CONVENTION label
- Sympy: explicit J on C^3, verify isotype collapse under J-projection

**Agent B: Cl(3) bivector irrep on dim-2 spinors for F1-vs-F3** — `physics-loop/bae-cl3-bivector-block01-20260517`
- Use retained `cl3_pauli_irrep_uniqueness_narrow_theorem` + `cl3_complexification_split_narrow_theorem` + `cl3_faithful_irrep_dim_two_narrow_theorem`
- Map B_1 = C + C^2, B_2 = i(C - C^2) into Cl(3) bivector subspace
- Check if bivector Hodge star collapses doublet to single mode
- Sympy: build Cl(3) explicit basis, verify pi_perp embedding, check Hodge-collapse

**Agent C: Bounded g_2(v) interval given u_0 admission** — `physics-loop/g2-bounded-interval-block01-20260517`
- Accept literature import for u_0(SU(2)) ∈ [0.96, 0.98] as NAMED EXTERNAL ADMISSION (with reference: Trottier et al hep-lat/9803024, Münster strong-coupling series)
- Build g_2(v) bounded interval at the framework lattice scale (β=16 from native_gauge_closure)
- Apply retained b_2 = 19/6 for running coefficient
- Result: Pattern A narrow bounded theorem of "given u_0 ∈ [0.96, 0.98], g_2(v=246 GeV) ∈ [X, Y]"
- Sympy: explicit interval arithmetic, verify endpoints match
