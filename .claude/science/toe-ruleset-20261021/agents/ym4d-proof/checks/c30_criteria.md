# c30 criteria (written BEFORE checks/c30_sources.py; session 15, 2026-10-27)

Purpose: instances for the session-15 fixes and targets (REVIEW_S13_S14 fixes 2, 4, 9; RTARGET §33). Not a proof of
anything. Four parts, each its own job (`python3 -I c30_sources.py A|B|C|D`), one job at a time, nice 10, BLAS threads 1.
No float tolerance is added to any inequality below; if a tolerance turns out to be needed, it goes into an addendum to
THIS file, written before the run that uses it (REVIEW_S13_S14 fix 13).

## Part A: the strip constants at the corrected (η, r_0) pairs (mpmath, 30 digits)
Re-implement, from the PROOF text, the conditions defining η_* (Theorem N2-exp: ρ_β ≤ ½, e_Ψ ≤ Ψ_U/2,
br_V ≥ ½/((1 + ρ_β)Γ), λ > 0, AND the f_0 condition (4η²/ψ_0 + 4η/√ψ_0)cosh η ≤ 0.15) and η'_* (Theorem N2-exp': θ_a ≤ π/2,
ρ_R ≤ ½, Ψ_L ≥ 1/10, br'_V ≥ (1 - ρ_R)/(4D_2Γ), 4c_φ ≤ ψ_0/2, λ > 0), L = 3. Pairs (κ, κ̂, η, r_0):
- N2-exp: (1, 1, 0.0111, 0.57), (0.25, 1, 0.0077, 0.37), (4, 1, 0.0117, 0.65), (0.25, 16, 0.0037, 0.25), (4, 16, 0.0082, 0.60);
- N2-exp': (1, 1, 0.0384, 0.70), (0.25, 1, 0.0273, 0.37), (4, 1, 0.0306, 0.90), (0.25, 16, 0.0140, 0.24),
  (1, 16, 0.0226, 0.47), (4, 16, 0.0216, 0.67).
- A1: every condition holds at every pair (exact comparison at 30 digits).
- A2 (informational): the bisection value of η at each stated r_0 (40 halvings), and the margin η_bisect - η_stated.
PASS iff A1.

## Part B: the f_0 half of Lemma SRC-id (iii) at complex points (algebra)
At 200 random complex points z (|Im z_α| ≤ 0.05; 60 at n = 27) for n ∈ {3, 9, 27} (k = 1, 2, 3, κ_i ≡ 1, and κ = (0.5, 2)
at k = 2), with c28's analytic blocks (a, δ, φ, R, β, Ψ), D_n and its conjugate continuation D̄_n(w) := n^{-1}Σ_{j<n}e^{iwj/n},
W_σ := ΠD·D_σ, W̄_σ := ΠD̄·D̄_σ, ν_σ := e^{iz_σ} - 1, ν^{(n)}_σ := n(e^{iz_σ/n} - 1), ν̄^{(n)}_σ := n(e^{-iz_σ/n} - 1), and a random
complex ĵ, S := Σ_νν̄^{(n)}_νR_νĵ_ν/β_ν:
- B1: κ_{k-1}W_σW̄_σ = aδ_σ and W_σν_σ = ΠD·ν^{(n)}_σδ_σ (entire identities): relative error ≤ 1e-10;
- B2 (screening line): with r̂_σ := W̄_σĵ_σ/β_σ + ν_σΠD̄·S/(β_σΨ) (SRC-id's r̂^{(0)} with c = 1),
  ĵ_σ - κ_{k-1}W_σr̂_σ = (φR_σ/β_σ)ĵ_σ - aν^{(n)}_σ(δ_σ/β_σ)S/Ψ: relative error ≤ 1e-10;
- B3 (curl line): for ρ ≠ σ, ν^{(n)}_ρY_σ - ν^{(n)}_σY_ρ, with Y the right side of B2, equals
  φ·[ν^{(n)}_ρR_σĵ_σ/β_σ - ν^{(n)}_σR_ρĵ_ρ/β_ρ - (S/Ψ)ν^{(n)}_ρν^{(n)}_σ(R_ρ/β_ρ - R_σ/β_σ)]: relative error ≤ 1e-10.
PASS iff B1, B2, B3.

## Part C: the chain with sources at every level (identities for §33)
c26's Chain (S4' root maps, d = 2 and 4) on (d, T, k, κ) = (2, 5, 2, (1, 1)), (2, 5, 3, (0.5, 2, 1)), (2, 3, 3, (1, 1, 1)),
(4, 3, 1, (1)), (4, 2, 2, (1, 1)). Random level-l 2-forms G_l (l = 0, …, k-1; fixed seed), j_l := d_l^TG_l, random data
B_k. The critical point of E - Σ_l⟨j_l, B_l⟩ is found by MINRES on M^TMx = M^Tb + (j_0, …, j_{k-1}).
- V1 (validity): the normal-equation residual ≤ 1e-8 relative.
- C1 (generalised source identity): r_{k-1}(j; B_k) = r_{k-1}(0; B_k - g_eff) with
  g_eff := Q^{(0→k)}Δ^{-1}j_tot + Σ_{i=0}^{k-2}κ_i^{-1}Q^{(i+1→k)}Σ_{l=i+1}^{k-1}(Q^{(i+1→l)})^Tj_l, j_tot := j_0 + Σ_{l≥1}(Q^{(0→l)})^Tj_l
  (the chain's own root maps; Δ^{-1} the fine Hodge inverse): relative max error ≤ 1e-6.
- C2 (transport): κ_ir_i = κ_{k-1}(Q^{(i+1→k)})^Tr_{k-1} - Σ_{l=i+1}^{k-1}(Q^{(i+1→l)})^Tj_l for every i, and
  d_0B_0 = d_0Δ^{-1}(j_tot - κ_{k-1}(Q^{(0→k)})^Tr_{k-1}): relative max error ≤ 1e-6.
- C3 (reciprocity): with B_k = 0 and the sources, and with 3 random data B'_k and no sources (chain B'_l),
  κ_{k-1}⟨r_{k-1}, B'_k⟩ = Σ_l⟨G_l, d_lB'_l⟩: relative error ≤ 1e-6.
- C4 (2-form transport bound used in the proof): for 20 random level-l 2-forms H (l < k - 1) and m = 1, 2 (where
  available), sup|(Q^{(l→l+m)})^Td_{l+m}^TH| ≤ 2(d - 1)L^{(2-d)m}sup|H| (Lemma CR (i): column sums L^{2-d}; L^{-2m} in d = 4):
  every ratio ≤ 1.
PASS iff V1, C1, C2, C3, C4.

## Part D (informational): the soft-output constant
For d = 2 (T = 5, k = 1, 2, 3) and d = 4 (T = 2, k = 1, 2), sources G_l with |G^c_l| ≤ 1 at a single level l (l = 0 and
l = k-1), B_k = 0: print sup|r^c_{k-1}| / sup|G^c_l| and L^{k-1-i}sup|r^c_i| / sup|G^c_l|. Informational only (k-stability
of the constant of (G♯_0-soft)); no PASS criterion.
