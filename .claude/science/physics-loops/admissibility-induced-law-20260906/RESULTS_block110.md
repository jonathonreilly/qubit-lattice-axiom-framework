# Block 110 — results (2026-09-24)

- **Runner.** `scripts/admissibility_rule_around_a_body_the_walks_rays_and_the_two_charges_of_the_curvature_member_2026_09_24.py`: `TOTAL: PASS=24 FAIL=0` (~30 s). Six mutations, each failing in its own family.
- **T1.** Exterior χ = 1 + a/r, N = 1 − p/r; index n = χ³/N = (r + a)³/(r²(r − p)). At p = a = M/2 it is the comparator's index identically.
- **T2.** Site equations (Δχ) = −e/(8Kwχ), (ΔN) = (e + 2τ)/(8Kχ). Charges Q = Σe/(8Kwχ), P = Σ(e + 2τ)/(8Kχ), and P − Q = (1/8K)Σ[2τ − e(1−w)/w]/χ.
  - At rest, P < Q.
  - Balance: 2Στ/χ = Σe(1−w)/(wχ). A balanced exact example has P = Q = 7/4.
  - With 0 ≤ τ ≤ e, balance is impossible if every content clock is below 1/3.
  - At weak field, P/Q = 1 + 2Στ/Σe ∈ [1, 3].
  - Globally, the ledger 8KQ = H + F and 4K(P + Q) = H_rest + 2H_hop; so P = Q exactly when F = H_hop (the lattice counterparts of the comparator's two masses).
- **T3.** b_c = min r n(r) at r* = a + p + √(a² + ap + p²). At a fixed first-order turn 4M/b, b_c/M rises with ρ = P/Q: 9/2, then 3√3 at ρ = 1, then 6.065 at ρ = 3, tending to 8.
- **T4.** χ = 2ν₁/b + π(ν₂ + ν₁²/2)/b² + (4/3)(ν₁³ + 6ν₁ν₂ + 3ν₃)/b³ + …. For the member at a fixed first-order turn, the second-order term is 6π(5 + 4ρ + ρ²)/(3 + ρ)², which is 15π/4 at ρ = 1.
- **T5.** For the index e^{kA/r}: capture at ekA and the tree-function series. With lengths, the second-order term is 4π, not 15π/4.
- **Control.** 3D ray integration agrees with the quadrature to 1e-8. Capture brackets hold at b_c(1 ± 1e-3).
