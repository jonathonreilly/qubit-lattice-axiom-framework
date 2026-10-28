# h3 criteria (written before h3_shadow.py): Lemma H-geo (i)-(iv), Lemma H-nest (iii) — HIST.md §7

Cube coordinates in Z⁴; π(z) = ⌊z/L⌋ componentwise; N_ρ sup-distance neighbourhood; Σ(A) := N_1(π(A)); sh_m := Σ^m.
L ∈ {3, 5}. Sets 𝒟: (a) 60 random *-connected sets grown by random *-adjacent accretion, n ∈ {1, 2, 5, 10, 30, 100, 300},
fixed seeds; (b) adversarial: axis line, main-diagonal line (step (1,1,1,1)), two-direction diagonal, a sparse
"staircase" alternating e_1 and (1,1,1,1) steps, each with n ∈ {10, 50, 200}, placed at offsets 0 and L^3 - 1 per coordinate
(to straddle block boundaries). m = 1..6 (and M up to 6 for (iv)).
- **G1 (i).** sh_m(𝒟) ⊂ N_3(π^m(𝒟)) for every 𝒟, m. PASS iff no violation.
- **G2 (ii).** |π^m(𝒟)| ≤ min{n, 16 + 32(n - 1)L^{-m}}. PASS iff no violation; print the max ratio.
- **G3 (iii).** |sh_m(𝒟)| ≤ 2401(16 + 32(n - 1)L^{-m}). PASS iff no violation; print max |sh_m| for n = 1 (the persistent
  size) and the max ratio.
- **G4 (iv).** Σ_{m=0}^{M}|sh_m(𝒟)| ≤ 38417n + 38416M for M = 0..6. PASS iff no violation.
- **N1 (H-nest (iii), columns).** 20 random histories (levels 0..4, L = 3, a 3-level torus-free window; each 𝒰_j a union of
  ≤ 3 random *-connected sets placed in the complement of Σ(Ω^c_{j-1})); for every level-0 cube x within the window,
  {m : π^m(x) ∈ Λ_m} is an initial interval. PASS iff no violation.
- **h3 PASS iff G1-G4 and N1 PASS.** Machine: numeric lock, nice 10.
