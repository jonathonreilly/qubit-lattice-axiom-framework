# bb3 criteria (BFT lane B session 3; written 2026-10-28 ≈06:40 UTC, after BFT_B.md §9 (stat 06:37:48) and before checks/bb3_walk.py exists)

Target: the algebra of BFT_B.md §9.4 Theorem RW^∇_k and §9.5 Construction BB-bond_k, on a model local operator. It tests
identities, supports and the class splitting; it tests **no** k-uniformity, no lane-A norm and no Hölder component.

Model: d = 2 periodic lattice, N_s = 48 sites per side (sites = "coarse positions"), real scalar site fields, ℓ^∞ torus
distance. 𝓛 := -Δ + μ² (5-point Laplacian), μ² = 2 for the verdicts. Boxes of side R = 4 (12 × 12), cubes of side M_c = 2R
= 8 (6 × 6), *-adjacency (8 neighbours). Cutoffs, as in §9.0 but discrete: χ_□ = normalised products of 1D weights
supported within distance 1 of the box (Σχ = 1); ψ_□ = Π_μ clamp((R - dist_μ)/(R/2), 0, 1) (1 on □^{(R/2)}, 0 off
□^{(R)}); η_Q = normalised products of 1D weights supported within distance 2 of the cube (Ση = 1). Local tori of side
T_W = 3R + 8 = 20, box placed by a lattice translation; 𝓖_□ := the local torus inverse; P_□y := ψ_□·(transported
𝓖_□(χ_□y)); C_ψ(u) := 𝓛_loc(ψu) - ψ𝓛_locu on the local torus (the commutator covector; 𝓛 symmetric); R_□y := -(transported
C_{ψ_□}(𝓖_□χ_□y)). 𝓛 itself is applied on the 48 × 48 torus. Weighted cube operators 𝐈(s), 𝐑(s), 𝐏(s), 𝐊(s) and views
S_Q𝐀 exactly as §9.0 (s_{QQ} = 1, s = 0 for non-adjacent pairs).

Nonlinear model: 𝔑(x) := c·x³ sitewise (c = 1), data source g uniform in [-0.05, 0.05] (seed 0);
E(x) := ½⟨x, 𝓛x⟩ + ⟨g, x⟩ + (c/4)Σx⁴, site densities D_i(x) := ½x_i(𝓛x)_i + g_ix_i + (c/4)x_i⁴, owner cube = cube of i,
trapezoid defect 𝔇_{D_i}(u) = -(c/4)u_i⁴ (computed from the definition D(u) - D(0) - ½⟨∇D(0) + ∇D(u), u⟩ in the script, not
from this closed form); 𝔈_Q(s) := ½⟨η_Qg, S_Q𝐀⟩ + Σ_{i∈Q}𝔇_{D_i}(S_Q𝐀).

Verdicts (complex128; random inputs from numpy default_rng(1)):
- **B3-1 (parametrix identity 𝓛P = 1 - R).** max|𝓛P - (I - R)| (dense 2304 × 2304) ≤ 1e-12.
- **B3-2 (the expansion reproduces the inverse).** max|P(I - R)^{-1} - 𝓛^{-1}| / max|𝓛^{-1}| ≤ 1e-10. Also report
  ||R||_∞ (max absolute row sum); B3-2 additionally requires ||R||_∞ < 1 (so the Neumann series converges at s ≡ 1).
- **B3-3 (s ≡ 1 identity of (d)).** For a random cube-supported 𝐲 (y_Q complex normal on Q^{(2)}, 0 elsewhere):
  Σ_{Q'}(𝐊(1)𝐲)_{Q'} versus 𝓛^{-1}Σ_Qy_Q, relative sup error ≤ 1e-10, (1 - 𝐑)^{-1} by Neumann iteration to increment
  ≤ 1e-15·|||first term|||.
- **B3-4 (class splitting of (d)).** Classes A = cubes with first cube index in {0, 1, 2}, B = the rest (two class
  boundaries on the torus). s random complex with |s_b| ≤ s_sp := min(1.5, 0.5/||R||_∞) on intra-class bonds, 0 on
  inter-class bonds. PASS iff (𝐊(s)𝐲)_{Q'} for every Q' ∈ A changes by ≤ 1e-12 × max_{Q'∈A}|(𝐊(s)𝐲)_{Q'}| when (i) y_Q
  (Q ∈ B) are replaced by fresh random fields, and (ii) s on B-internal bonds is replaced by fresh random values; and
  (control) the class-B components change by ≥ 1e-6 (relative) under (i).
- **B3-5 (enlarged nonlinear fixed point at s ≡ 1).** The fixed point of 𝐀 = -𝐊(1)𝐲(𝐀), y_Q(𝐀) := η_Q(g + 𝔑(S_Q𝐀)),
  versus the global fixed point x = -𝓛^{-1}(g + 𝔑(x)) (both by iteration from 0 to increment ≤ 1e-15): relative sup error of
  Σ_{Q'}A_{Q'} - x ≤ 1e-10.
- **B3-6 (energy identity).** |Σ_Q𝔈_Q(1) - (E(x) - E(0))| ≤ 1e-10·|E(x) - E(0)|.
- **B3-7 (energy splitting).** At the split s of B3-4 (nonlinear fixed point, iteration as B3-5): Σ_{Q∈A}𝔈_Q(s) changes by
  ≤ 1e-12 (relative) when (i) the class-B cubes' data copies are replaced (y_Q for Q ∈ B uses g' := fresh random data) and
  (ii) s on B-internal bonds is replaced; control: Σ_{Q∈B}𝔈_Q(s) changes by ≥ 1e-8 (relative) under (i).
- **Informational (no verdict).** ||R||_∞ and R·||R||_∞ for μ² ∈ {1, 2} and R ∈ {4, 6, 8} (M_c = 2R, T_W = 3R + 8,
  N_s = 48), real arithmetic.

Runner: numeric lock (`until mkdir …/locks/numeric 2>/dev/null; do sleep 20; done`), load1 < 8, nice 10, thread variables
1, PYTHONDONTWRITEBYTECODE=1, /usr/bin/time -l, python3 without -I, no `timeout`, `rmdir` exactly once, no trap. Budget
< 20 min, < 1 GB.
