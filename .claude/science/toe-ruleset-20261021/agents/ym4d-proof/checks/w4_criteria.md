# w4 criteria (lane H, session 4), written 2026-10-28 before checks/w4_footprint.py exists

Purpose: informational check of the influence-column geometry used by HW.md session 4 (U2 (b)). Never a proof.

Model (pure combinatorics, no measure). Multi-level tori, side L = 3 per level; a level-m cube is a level-(m+1) site
(x ↦ ⌊x/L⌋); π maps a level-m cube to the level-(m+1) cube containing it. Kernel data-reading (HIST l.964: "S4' contours of
c stay in c's two endpoint blocks"): a level-(m+1) link c = (X, X + e_μ) reads a level-m link ℓ iff both endpoints of ℓ lie
in the blocks X ∪ (X + e_μ). Footprint F_{k} := A (a set of level-k links), F_{m+1} := {c : c reads some ℓ ∈ F_m}. A level-m
link is read by the level-m constraint iff its two endpoints lie in one level-m cube Z with Z ∈ S^{(m)} (bad-only clause:
interior plaquettes of Z), and by a spectator iff both endpoint cubes project to one Q'' ∈ 𝒰_{m+1}. Histories: random
𝒰_j obeying (A2) (𝒰_j ∩ Σ(Ω^c_{j-1}) = ∅); (A1) (component size > n_♯) is not imposed (irrelevant to the geometry; disclosed).
Ω^c_m = Σ(Ω^c_{m-1}) ∪ 𝒰_m, Σ(B) = N_1(π(B)), A_m := Σ(Ω^c_{m-1}) ∪ N_1(𝒰_m), S^{(m)} := all level-m cubes ∖ A_m (= R(𝔥)).
Runs: d = 2 (K = 5, top side 4) and d = 4 (K = 3, top side 4); fixed seeds.

Pass criteria (all must hold for OVERALL PASS):
- A (containment): for every tested single level-k link ℓ with endpoint cubes x_1, x_2, every level-m cube that contains
  both endpoints of a footprint link (m = k+1 … K-1) lies in π^{m-k}({x_1, x_2}); every footprint link at level m ≥ k+1
  has an endpoint site in π^{m-k-1}({x_1, x_2}). Zero exceptions.
- B (relaxed column is never read): for every random history and every tested level-k link ℓ with π(x_1), π(x_2) ∈ A_{k+1},
  zero constraint reads and zero spectator reads at every level m = k+1 … K-1.
- C (control, constrained column is read): for every tested ℓ inside one level-k cube x with π(x) ∈ S^{(k+1)}, at least one
  constraint read at level k+1. Zero exceptions (C must find reads, else the reading rule is vacuous).
- D (negative control): with a widened kernel (c reads ℓ iff both endpoint cubes of ℓ lie in N_1({X, X + e_μ})), the
  statement B must FAIL for at least one tested (history, ℓ) in each dimension.
Resource limits: < 20 min, < 1 GB; one run under the numeric lock; nice 10; BLAS threads 1.
