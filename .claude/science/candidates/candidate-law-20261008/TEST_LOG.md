# Test log for Candidate 1

**Recording rule.** Each verdict is measured against the pre-registered line in `KILL_SHEET.md`. Each entry gives:
- the worker's provenance (Sonnet 5.5, same-family);
- the supervisor's own check;
- the referee status.

A FAIL goes into `RESULTS` in `decision_matrix.py` only after a referee has checked it. PASS and INCONCLUSIVE outcomes move the priors, with the reason logged here.

Worker scripts are in session scratch; the supervisor check scripts named below are copied into `checks/`.

## K7a: one cone by symmetry (2026-10-08)

**Verdict: PASS on the pre-registered line.** Every sector, gravity included, has a hypercubic Euclidean form with exact lattice gauge invariance.

**The new construction (worker, CHECKED).**
- **Placement.** Staggered linearized gravity on the 16 half-shift role classes of Z⁴: h_μν sits at x+(e_μ+e_ν)/2 and ξ_μ at x+e_μ/2, with symbols s_μ = 2 sin(k_μ/2).
- **Action.** Q = ¼[ s²h:h − 2|hs|² + 2(shs)tr h − s²(tr h)² ].
- **Gauge invariance.** K(s)D(s) = 0 symbolically, with zero residual in real space at L = 3, 4, 5.
- **Hypercubic covariance.** All 384 elements of W(B4) are exact.
- **No doublers or extra modes.** The only zero modes are pure gauge, at every momentum including all 15 zone corners.
- **Reduction to A25.** Exact at the symbol level: the spatial block is A23's V_EH, the inverse of the s₄² block is GR's kinetic weights, and the h_44 and h_4i rows are the constraint rows.
- **Photon match.** The photon's and graviton's gauge-fixed propagators are both 1/Σs_μ², so their speeds agree exactly at every momentum at tree level.

**What protects at loop level.**
- **Photon:** hypercubic symmetry plus gauge invariance leave one two-derivative form (ARGUED, with a CHECKED algebraic step).
- **Fermion:** the shift symmetries remove the taste-nonsinglet dimension-4 terms (Golterman–Smit; COMPARATOR).
- **Graviton:** there are 9 hypercubic forms, of which 4 are O(4)-invariant, and exact gauge invariance leaves 1 (CHECKED count). Without exact gauge invariance, 5 anisotropic forms are allowed. **The graviton's protection therefore hangs on K3a,** whether the interacting stress is exactly conserved.

**Conditions found.**
1. **No positive transfer matrix for gravity.** The conformal mode gives 255 negative eigenvalues at L = 4. "H = −(1/a) log T" cannot define gravity.
2. **Tick size.** Hypercubic means a_t = 2 fine (Z³) edges. A25's leapfrog at τ = a_s is unstable (max|eig| 9.9); τ = a_s/2 is stable but not hypercubic.
3. **Matter content.** 4D staggered fermions have 4 tastes and a two-step transfer matrix. That differs from the 3D Hamiltonian H_ψ written in `CANDIDATE_1.md`.

**Supervisor check.** Not yet run independently. The fermion and gauge hypercubic invariance is standard. The gravity symbol identities are to be re-run by the referee.

**Referee.** Owed: codex sol, for the gravity construction.

**Effect on priors.** K7 for Q goes from 0.15 to 0.30, conditional on K3a.

## K2a: a chirality route (2026-10-08)

**Verdict.**
- **Continuous-time (H) form: PASS, but weak.**
- **Hypercubic (Q) form: INCONCLUSIVE.** It needs an ingredient Candidate 1 lacks, such as an extra dimension or a domain wall.

**The selector.**
- In the 3D Hamiltonian form, the body-diagonal shift Z = T₁T₂T₃ (with its staggered sign frames) equals the Weyl chirality on the zero modes.
- That gives a local, covariant projector onto the mirror, P̄_R (a 9-site stencil).
- The Spin(10)-singlet quartic Fidkowski–Kitaev-type term built on P̄_R ψ respects the lattice symmetries.
- The content is one field → 2×16 ⊕ 2×16̄ with Spin(10) on-site.

**Supervisor check (EXACT, `checks/k2a_selector_momentum_space.py`).**
- In the 2³ unit cell at k = 0, the effective Γ_μ are exactly anticommuting with Γ² = 1.
- Their chirality X = Γ₁Γ₂Γ₃ has eigenvalues ±1 (4 and 4).
- e^{iφ}T₁T₂T₃ = −X to 6e-17. **Confirmed.**
- In 4D, T₁T₂T₃ commutes with γ5 but takes both values ±i inside each chirality block. **No selector in the hypercubic form, confirmed.**

**What the PASS does not carry.**
- **The gap is not shown** (K2b). ψ^R is not canonical, so the Spin(10) atomic-gap proof does not transfer.
- **The separation is in crystal momentum.** Gauge links carry momentum: this is the Eichten–Preskill leakage problem.
- **The staggered mass must vanish.** m ε(v)ψ†ψ is Z-odd.
- **The Gauss law must use a Spin(10) Cartan**, and the record count is conserved only mod 4.
- **A vertex holds 16–32 occupation bits.** That strains "one record per site".
- **Generations come in pairs per field** (K6).

**Referee.** Not owed for a PASS. Codex sol is optional, on the 3D selector.

**Effect on priors.**
- K2 (L,O) moves from 0.18 to 0.20.
- The Q multiplier on K2 moves from 1.1 to 0.5, because the selector is lost in the hypercubic form.

## The tension these two results expose

**What they show.** In the forms tested so far, the grid can either tell left from right (continuous time) or keep one speed for every field by symmetry (hypercubic time), but not both. This is a tension, not a theorem:
- another 4D mirror selector, or another protection of one speed in continuous time, is not excluded.

**What resolves it:**
- K2b: does the mirror gap in the continuous-time form?
- K7b for the H form: how large is the one-loop speed split, and does it need tuning to 1e-15?
- K3a: the graviton's protection, in either form.
