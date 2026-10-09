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
1. **The unreduced Euclidean gravity form is indefinite.** The conformal mode gives 255 negative eigenvalues at L = 4. "H = −(1/a) log T" therefore cannot be taken directly. The referee notes that a positive physical transfer matrix after reduction is open, not excluded.
2. **Tick size.** Hypercubic means a_t = 2 fine (Z³) edges. A25's leapfrog at τ = a_s is unstable (max|eig| 9.9); τ = a_s/2 is stable but not hypercubic.
3. **Matter content.** 4D staggered fermions have 4 tastes and a two-step transfer matrix. That differs from the 3D Hamiltonian H_ψ written in `CANDIDATE_1.md`.

**Supervisor check.** Not run independently: the referee re-derived it exactly instead. The fermion and gauge hypercubic invariance is standard.

**Referee: codex gpt-5.6-sol xhigh, CONFIRMED WITH CORRECTIONS (2026-10-08).** It re-ran everything and added an independent exact-arithmetic check.

Confirmed:
- (a) W(B4) covariance: exact via generators, and the symbol is in fact O(4)-covariant.
- (b) K(s)D(s) = 0: exact.
- (c) Spectrum s²{−1, 0×4, ½×5} at every s ≠ 0, so no doublers.
- (d) The ADM reduction: exact.
- The fermion and Wilson-gauge invariance on Z⁴: exact. Finite tori need even extents.
- The 9/4/1 count: exact.

Corrections:
1. Say "no extra zero modes or doublers", not "no extra modes". Physical counting also uses the constraints.
2. The shift row is −s₄s_j(h_ij − δ_ij tr₃h). The runner used √2-scaled coordinates.
3. Photon and graviton share the pole 1/Σ4sin²(k_μ/2). Their numerators differ, and the graviton's is (2/s²)(I − ½tt^T).
4. The 9/4/1 count covers constant-coefficient two-half-step forms. Gauge symmetry therefore protects the unique leading graviton structure and its single TT speed. It does not protect higher-derivative lattice artefacts, which are Planck-suppressed.
5. **"No positive transfer matrix" is NOT proven.** Only the unreduced Euclidean form is indefinite (the conformal-factor problem). A positive physical transfer matrix after constraints, gauge reduction or a contour prescription is open.

Prior literature (referee, from memory): Roček–Williams 1981 linearized Regge calculus, Barrett 1987, Höhn 2015. No published source is known for this exact staggered h_μν stencil, which is not a novelty proof.

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

## G0: can one qubit per site host fermions locally? (2026-10-08)

**Verdict: FAIL for the class searched. Not yet recorded in `RESULTS`: the referee is running.**

**The class searched** (13-qubit corner star, exhaustive):
- **The hops.** One hop per direction: t_δ = σ⁺_{v+2δ} X_{edge δ} σ⁻_v + h.c., times a product of single-qubit dressings, which are:
  - Pauli letters on the other edges, the far corners and the corner;
  - Z₄-monomial gates on the edges.
- **Covariance.** Required under all 24 turns, up to site-local Z₄ phase gates and scalars. This is a superset of the projective tables.
- **The observable.** The Levin–Wen holonomy on all 20 junctions: 12 T-shaped and 8 corner.

**What the worker found (CHECKED).**
- Every covariant candidate whose holonomy does not vanish gives +1 on every junction.
- Class A has 32 covariant patterns of 2048, all +1.
- Classes B and C (2560, 8192 and 20480 candidates): none gives −1 on any junction.
- **Controls.** Non-covariant "tournament" dressings give −1 on all 20 junctions. Turn-invariant tournaments exist only for the trivial group and the four C3 subgroups.
- **Helper face qubits.** They can make the 8 corner junctions −1, but never a T-junction.

**Supervisor's own check (ARGUED, independent of the worker's code).**
1. Commutation signs between hop factors do not change when a hop is multiplied by a scalar. They do not change under conjugation by a common frame either.
2. Take the half-turn about an axis ε ⊥ δ. It swaps δ ↔ −δ and fixes e_{±ε}. It swaps e_η ↔ e_{−η} for the third axis η, and e_δ ↔ e_{−δ}.
3. Covariance gives d_{−δ}(e_{gx}) = d_δ(e_x) for every dressing letter. So:
   - the e_{±ε} contributions are a letter against itself, which is 0;
   - the (e_η, e_{−η}) and (e_δ, e_{−δ}) contributions come in equal pairs, which is even.
4. Only the corner factor is left. It is σ^∓ in both hops, fixed by occupation transfer, and phase frames only rephase it. So the factors commute.
5. The T-junction sign is therefore +1 for any product dressing, at any range.
6. The corner junctions are a separate orbit. This is why helper faces can flip them but never the T-junctions.

This matches the worker's pair-sign argument. The plain version: a local fermion needs an ordering of the six directions at each corner, and a half-turn always reverses some pair.

**Scope.** The FAIL does not exclude:
- sums of several dressed terms per direction;
- continuous non-Clifford dressings;
- non-product composites (A50's CZ composite was not re-tested);
- corner records (A52);
- non-local strings;
- more than one qubit per site.

Bravyi–Kitaev superfast needs a fixed tournament, so it fails. Verstraete–Cirac needs auxiliary modes.

**Referee: codex gpt-5.6-sol xhigh, CONFIRMED WITH CORRECTIONS (2026-10-08).** The verdict and the referee's independent script are in `checks/referee_G0/`.

**Confirmed, for the narrower class.**
- **The class:** one directed occupation-transfer monomial per direction, with sign-type product factors (Pauli or Z₄-monomial).
- **The requirement:** a scalar −1 holonomy on the full unconstrained domain.
- **The result:** no PASS. Every scalar nonzero holonomy is +1.
- **The extension:** the obstruction extends to sign-type product dressings of any finite range, by a corrected orbit-parity argument. My half-turn argument needed a second turn to pair the two non-origin sites on the fixed axis.

**Corrections.**
1. **Non-scalar candidates do reach −1.** "No candidate gives −1 on any junction" is false. The covariant candidate `XS0|S0,S1,S1,S1,S1`, and about 1536 others, give +1 on some link backgrounds and −1 on others. They fail only because the value is not a scalar.
2. **Gauge sectors were never tested.** No Gauss, stabilizer or flux sector was imposed, although the kill sheet asked for a KS-flux check. String-net and bosonization fermions live inside such a sector, so **the constrained-sector route is open.**
3. **The helper-face corner flips** fail the exact frame group law.
4. **"Vanishing" cases** are mostly not proper occupation-transfer hops. They are partial zeros, not statistics.
5. **The BKSF statement** rules out only an order kept invariant under this restricted action, not every symmetry implementation.

**Recorded.** The narrowed FAIL is recorded as a prior change, not a zero, because the class is narrower than the room setting P:
- K2(L,P) goes from 0.06 to 0.04;
- K2(E,P) goes from 0.05 to 0.04.

**Follow-up G0b (launched).** The non-scalar candidates are retested inside local covariant constraint sectors: a Gauss law at corners and the KS π-flux. The question is whether the Chen–Kapustin / Z₂-gauge route gives fermions with one qubit per site.
