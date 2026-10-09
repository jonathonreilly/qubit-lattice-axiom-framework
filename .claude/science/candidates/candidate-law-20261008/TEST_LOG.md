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

## G0b: fermions inside a constrained sector? (2026-10-08)

**Verdict: FAIL** for G0's architecture, extended:
- corner occupation qubits, with edge link qubits;
- one occupation-transfer monomial per direction;
- sign-type product dressings, Pauli/Z₄, plus a Z₈ census.

The worker is Sonnet 5.5. The referee (codex sol) is running.

**What the worker found (CHECKED unless marked).**
- **The holonomy on the occupation domain is c × a Pauli string.**
  - Corner junctions are +1 as an operator identity, or zero, in every candidate. No sector can make them −1.
  - T-junctions are +1, zero, or ±Z_{l_a}Z_{l_{−a}}: the parity of the two collinear edges at the corner. The last case is exactly G0's non-scalar set.
- **The constraint family (194 templates).** It covered vertex Gauss laws, polarizations and coarse-square fluxes.
  - Only G_v = (−1)^{n_v}∏₆Z commutes with the hops, for 512 tables. In that sector the T-junctions stay non-scalar.
  - No flux generator commutes with any non-scalar candidate.
- **Every Pauli stabilizer sector, searched exhaustively.** No scalar −1 is feasible: 0 of 3072 × 12 × 16.
- **Non-Pauli sectors (ARGUED, with the loop's existence CHECKED).** A closed two-particle hopping loop flips exactly one collinear edge. So no hop-invariant sector that contains dilute two-particle states can have H = −1.
- **Z₈ dressings.** The 196,608-candidate census is exhaustive and finds no −1 anywhere.

**Plain reading.** With the occupation on the corner and the links on the edges, the exchange sign is either +1 or tied to the edge parity along a line. Moving particles around a loop can flip that parity, so no local constraint can pin it to −1.

**Not excluded.**
- **Sums and non-product hops.**
- **Face/cube-qubit architectures.** An example is Chen–Kapustin exact 3D bosonization, with qubits on faces and fermions as fluxes on cubes. It needs a spin-structure or branching choice, which is likely the same ordering obstruction (READING).
- **A52's corner records.** Under exact turns, a record at every corner holds the direction ordering in the *state*. This is the one known escape, and it is consistent with G0's obstruction: the ordering cannot be in the law, but it can be in the state.

**Effect on priors.** K2(L,P) goes from 0.04 to 0.03 and K2(E,P) stays at 0.04, because the A52 route works under exact turns.

**Referee: codex gpt-5.6-sol xhigh, CONFIRMED WITH CORRECTIONS (2026-10-08).** This is a bounded no-go.

Confirmed:
- The holonomy signatures, over all 27,168 class entries. There are 1,536 distinct non-scalar tables (C1 sits inside C2).
- The 194-template scan.
- Pauli constraints that commute with every individual hop.
- The loop lemma, for termwise hop-invariant sectors containing dilute two-particle states.
- The Z₈ census, for its finite ansatz on the unconstrained domain.

Not covered:
- dense sectors;
- subspaces invariant only under the summed Hamiltonian;
- non-Pauli sectors without dilute states;
- face-qubit exact bosonization. **Chen–Kapustin (arXiv:1807.07081) is genuinely outside the architecture, and G0's turn obstruction does not transfer without a separate calculation.**

**Follow-up.** G0c was pre-registered in `KILL_SHEET.md` and launched. Its question is whether the 24 turns act locally on the Chen–Kapustin face-qubit model.

## K3a: graviton mass from the interacting sea (2026-10-08)

**Verdict, read against the pre-registered line: INCONCLUSIVE.** The worker labels it "FAIL, qualified". The pre-registered FAIL needs two things:
1. **No exact local stress.** CHECKED for the interacting theory, so this half is met.
2. **Induced terms that are O(1) in lattice units.** NOT met: the interacting remainder is about 1e-5 to 1e-4 per cell (ARGUED).

The line is not changed after the fact.

**What the worker found (Sonnet 5.5).**
- **The criterion.** The gauge condition Dᵀ F = i[H, 𝒫] holds iff P = Σ𝒫 and L = Σc×𝒫 are both conserved local charges. "Only if" is EXACT; "if" is ARGUED by module duality.
- **Free fields: an exact local stress exists (CHECKED).**
  - Staggered fermions, in 1D, 2D and 3D, massive or massless: residual ≤ 4e-14. In 2D the symmetric T is rebuilt explicitly.
  - Yee Maxwell, with Gauss and Bianchi multipliers: residual 1.6e-11 in 3D.
- **Interacting lattice QED: no exact finite-range stress (CHECKED, perturbative at O(e)).**
  - Lattice-scale resonant emission and absorption (|p| ≥ 1.5) exist, with nonzero amplitudes.
  - Once 400–800 resonances are imposed, no free-conserved momentum survives at ranges 2, 3 or 4.
  - The best finite-range defect is 13% at R ≤ 3 and 3.5% at R ≤ 4.
  - A 1D gauge comparator has only the identity and H as local charges.
- **Size of the mass term.**
  - At the free level it is about +0.27 / +0.22 per cell (axis / face), which is cutoff-sized, but a coupling can be designed to remove it.
  - The interacting remainder, about e²·defect², is 1e-5 to 1e-4 per cell (ARGUED). That is about 1e95 above the gravitational-wave bound.
- **Diagnosis.** It blames the fixed grid plus any local interaction, not the room setting. The listed escapes:
  - free or integrable matter;
  - non-explicit (emergent) gravity;
  - a stress of very long range.
- **No symmetry forbids the term.** Gauge, translation and cubic symmetry allow two TT numbers.

**Effect on priors** (moderated after the referee, below).
- X loses 0.6× on every room.
- G loses 0.85×.

**Follow-up.** K3a′, pre-registered above before running, asks whether the defect falls fast enough with range: a quasi-local stress about 1e11 sites wide (about 1e-23 m) would be invisible.

**Referee: codex gpt-5.6-sol xhigh, NOT CONFIRMED as a theorem (2026-10-08).** The bounded obstruction is confirmed; K3a stays INCONCLUSIVE.

Confirmed:
- **The criterion.** On infinite Z³, for compact support, conservation of [H,P] and [H,L] is necessary and sufficient. L is coordinate-weighted.
- **Free fields.** 3D Maxwell has an *exact* radius-½ stress, 207 coefficients that are multiples of 1/16 (`checks/referee_K3a/referee_maxwell3d_exact.py`).
- **The lattice-scale umklapp resonances**, with |p|min ≈ 1.49, are genuine.

Not supported or overclaimed:
- **"No finite-range charge" holds only for the tested class.** That class is a one-body fermion symbol plus a scalar photon weight, at electron range ≤ 4 and photon range 3, not 4. It omits:
  - polarization-matrix photon charges;
  - higher-body and mixed charges;
  - larger and quasi-local ranges.
- **The defect percentages are optimizer diagnostics, not bounds.** The drop from 13% to 3.5% blocks extrapolating any floor.
- **The mass estimate is unsupported.**
  - The 1e-5–1e-4 figure was α·δ², not e²·δ².
  - No interacting remainder or graviton pole was computed.
  - For the strictly linear coupling, the free-level shape coefficients are +0.118/+0.071.
- **Lattice EMT literature** (Caracciolo et al., Suzuki): EMTs are defined through Ward identities and renormalization. That is not a theorem excluding an exact stress for this Hamiltonian.

Strongest correct statement (referee): genuine lattice-scale resonances obstruct every conserved momentum in the tested bounded class at O(e). The evidence strongly supports generic lattice-scale gauge breaking, but it does not exclude larger-range, quasi-local, polarization-matrix, higher-body or engineered stresses. It does not establish a graviton-mass size either.

**K3a′.** The referee's corrections were passed to the worker before its fit was used.

## G0c: face-qubit bosonization under the 24 turns (2026-10-08)

**Verdict: PASS on the pre-registered line.** The worker is Sonnet 5.5. The referee (codex sol) is running, so priors do not move until it reports.

**What the worker found.** The source is the arXiv:1807.07081v2 PDF, read directly.

**The construction (EXACT, from the paper):**
- Fermions sit on cubes, and the qubits sit on faces.
- Hop: U_f = X_f ∏_{f′ before f} Z_f′, using a within-cube ordering.
- Parity: W_t = ∏_{f⊂t} Z_f.
- One Gauss constraint per lattice edge.

**The algebra (CHECKED).**
- It matches the paper's eq. 30 bit-for-bit.
- The code space is 2^(L³−1), exactly the even Fock sector.
- A dense 2×2×2 block reproduces fermion traces and an interacting spectrum to about 1e-14.
- **The Levin–Wen holonomy is −1 on all 12 T-junctions and all 8 corner junctions.** These are fermions.

**The 24 turns (CHECKED).**
- **Construction.** V_g = C_g ρ_g, where ρ_g permutes the faces and C_g is a diagonal Clifford: CZ gates between faces of the same cube, at depth ≤ 13, plus Z signs.
- **Hops.** V_g U_f V_g† equals the rotated hop modulo the stabilizers. This holds for all 24 turns, about cube centres and vertices, at L = 3, 4, 5, under all 64 within-cube orderings.
- **Parity.** V_g W_t V_g† = W_{gt} exactly.
- **Group law.** V_gV_h = V_{gh} on the code space for all 576 pairs. Support was sampled on the torus; the dense block is exact.
- **Controls.** Without C_g, 46 of 48 cases fail. Corrupting one CZ fails.
- **Why site-local frames cannot do it** (EXACT): the required images put Z on other faces. G0's ordering obstruction is real for relabelling alone, and the CZ network is what removes it.

**Plain reading.** One qubit per site *can* carry fermions, symmetrically under every turn.
- **Where.** The qubits sit on the face sites of the 2×2×2 cell, and a fermion is a twist of those qubits around a cube.
- **The price.** A turn acts as a relabelling followed by a shallow, fixed network of two-qubit phase gates. That network changes only phases, never which possibility a record would lock.

**Caveats.**
1. **This is covariance up to a diagonal dressing.** Whether that reads as "covariant under proper cubic rotations" (Admissibility) is a reading.
2. **Turns about edge-role or face-role sites** preserve the face pattern for only 8 of 24 turns. The pattern's cost to "rotations about each site" stays (K0, P).
3. **Spin structure.** Only the PPP and AAA sectors are fully rotation-invariant (ARGUED, not run).
4. **The Hamiltonian is supplied**, and the Gauss law is imposed as a constraint.
5. **No double-cover sign appears in the group law.** Whether the emergent fermions carry spin-½ under turns (2π → −1) is put to the referee.

**Referee: codex gpt-5.6-sol xhigh, CONFIRMED WITH CORRECTIONS (2026-10-08).**

Confirmed:
- **The Pauli and Majorana conventions.**
- **All 24 turns,** about both cube centres and vertices, at L = 3 and 4, on the genuine CK A10 framing:
  - the hop, flux, stabilizer and Hamiltonian covariance all hold;
  - the dense block reproduces;
  - **the exchange sign is −1 on all 20 junctions.**
- **The group law V_gV_h = V_{gh}** for all 576 products, now **exact** over the full affine support. The worker's original 40-sample check was inadequate.

Corrections:
1. **"Eq. 30 bit-for-bit" was false for the worker's frames,** which had a −G_e sign. It is repaired on the actual CK A10 frame, which gives +G_e on all 81 edges.
2. **The CZ depth is 12** (DSATUR), not 13. The greedy colouring gave 14. Every gate joins faces of one cube, so locality is secure.
3. **These are one-component spinless lattice fermions,** with no spin-½ double-group action. On the even sector a 2π spinor sign could not be detected anyway. This is the same kind of fermion the staggered route uses: spin emerges from the taste structure. So it is not a defect for this programme.
4. **Spin structures.** Only PPP and AAA are fixed by all 24 turns. Only PPP was tested.
5. **ρ_g is a geometric relabelling,** so the result is crystalline covariance, not a full finite-depth circuit.

**Strongest correct statement (referee).** On the CK A10 framing, each of the 24 proper turns is a face permutation followed by a cube-local diagonal Clifford. That preserves the Gauss-law code, the parity and hop generators, and the fermionic exchange sign, with an exact non-projective group law.

**Effect.** **One qubit per site can carry covariant lattice fermions.** The qubits sit on the face sites, and the fermions are cube fluxes. G0 and G0b are now a statement about one architecture only, corner occupation.

**Open cost.** In a 2×2×2 cell, the U(1) photon link between neighbouring cubes would cross the same face site that holds the CK qubit. Coupling light to these fermions therefore needs a larger cell or a second role (to be designed).

**Reading.** The turns act up to a cube-local CZ dressing. That is broader than "site-local U(1) frame" (L), so L is read here as "up to a locality-preserving local dressing".

**Priors.** K2(L,P) goes from 0.03 to 0.08. K2(E,P) stays at 0.04, because the dressing is not an exact turn.

## K3a′: how fast does the stress defect fall with range? (2026-10-08)

**Verdict against the fixed line: FAIL.** The worker is Sonnet 5.5, and the K3a referee's corrections were applied. The referee (codex sol) is running, and nothing goes into `RESULTS` until it reports.

**Protocol.**
- **Charge class.** Taste-scalar charges with an exact IR constraint.
- **Solve.** Exact least squares (Cholesky, with no penalty), on 300–400k training resonances.
- **Test set.** A fixed 150k set, shared by every R.
- **Convergence.** Seed spread is ≤ 1%. Changing the ridge, doubling the training set, or changing the photon radius barely moves the result (≤ 1.5%).
- **Not done.** Polarization-matrix photon weights.

**Mean |defect| on the test set.**

| R | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 |
|---|---|---|---|---|---|---|---|---|---|
| defect | 0.114 | 0.0224 | 0.00735 | 0.00316 | 0.00162 | 0.00095 | 0.00061 | 0.00044 | 0.00030 |

**Fits.**
- **Power law:** p = 2.87 ± 0.02, χ²/dof 0.66. Every window of three or more consecutive R gives p between 2.80 and 2.97.
- **Exponential:** rejected, χ²/dof 122. Its local rate falls like p/R, which is the signature of a power law.

**Extrapolation.** The defect reaches 1e-51 at R ≈ 2e17 to 1e19 sites, above the fixed 1e15 bar. Reaching 1e15 would need p ≥ 3.4. The extrapolation spans 16 decades.

**Physical reading (supervisor).**
- **At Planck spacing,** 1e17–1e19 sites is about 1e-18 to 1e-16 m, still below the proton radius.
- **If the induced mass² is quadratic in the defect,** the miss is a miss of the conservative pre-registered bar, not obviously of any experiment.
- **If it is linear,** the target defect is about 1e-103, so R ≈ 1e35 sites ≈ 1 m. Gravity is tested down to about 50 μm, so that is excluded. The worker argues "linear" from the Ward identity, but no prefactor was computed.

**Referee: codex gpt-5.6-sol xhigh, NOT CONFIRMED. K3a′ is INCONCLUSIVE (2026-10-08).**

Confirmed:
- **The data reproduce.**
- **The test set is valid.**
- **A power law beats a constant-rate exponential.**

Not confirmed:
1. **"Exact Cholesky" is ridge-regularized normal equations.** The solver minimizes mean square but reports mean |defect|, so the number is not the optimum and not a bound. Only one seed exists at R = 16 and 18.
2. **The scalar class is not shown to be adequate.** The referee's cheap polarization-matrix test at R = 2 changes little, but large R is uncovered.
3. **The quoted precision on p is not physical.** A defensible range is p ≈ 2.7–3.0.
4. **Decisively, the extrapolation is not identified.** Other forms fit the observed points equally well:
   - stretched exponentials with β = 0.01–0.02 give R(1e-51) = 1e13–1e15, which is a PASS;
   - a power law times exp(−R/1e13), invisible in the data, also gives a PASS.
5. **The defect-to-mass law is not derived.** Linear dependence is generically allowed, but no self-energy was computed.
6. **The scale.** The 1e15-site bar (1.6e-20 m) is a naturalness benchmark, far stricter than any direct gravity test, which reaches about 50 μm.

**Lesson.** A 16-decade extrapolation cannot decide this. The next test is a direct calculation: **K3a″, pre-registered in the kill sheet.**

## K3a″: the interacting vacuum's shear response, computed directly (2026-10-08)

**Verdict against the fixed line: FAIL, a naturalness kill.** The worker is Sonnet 5.5. The referee (codex sol) is running, and nothing goes into `RESULTS` until it reports.

**What was computed (CHECKED).**
- **The model.** A continuous-time Hamiltonian with constant spatial h. The photon is in a generalized Coulomb gauge, ∇·(M⁻¹A) = 0. The O(e²) energy is the sum of pair-plus-photon exchange, the diamagnetic term and the Coulomb term.
- **The coupling rules.**
  - The fermion hop along j carries Σ_a e_aj σ_a, and the photon energy carries G = g/√g.
  - Three versions were run: the exponential vielbein (volume-preserving), "vlin" and "lin". vlin and lin differ from exp only by trace responses, so the clean TT value is the exp one.
  - The face channel was run with nearest-neighbour ("natural") hops and with universal range-2 hops.

**c₂ per e² per cell (L → ∞, converged over L = 8 … 48).**

| Channel | c₂ |
|---|---|
| axis | −0.01303 |
| face, natural | +0.01247 |
| face, universal | +0.01337 |

- **Size.** At α = 1/137, |c₂| ≈ 1.2e-3 per cell, about 1e101 above the gravitational-wave bar. The opposite signs make it a strongly cubic-anisotropic term.
- **The axis pieces.** Exchange +0.0016, diamagnetic −0.0086, Coulomb −0.0060.

**No protected zero.**
- **The family.** c₂ = A x_f² + B x_f x_γ + C x_γ². The axis channel vanishes only at x_γ/x_f = 0.127 or 2.78, meaning light coupled to the metric 0.13 times as strongly as matter. That breaks universality, and nothing protects it. The face channel has no real root.
- **Counterterms.** Contact terms can cancel c₂, but they are tuned bare counterterms.
- **Symmetry.** Gauge, translation, cubic and C/P/T symmetry all allow the term.
- **The free part was already tuned.** Before its counterterm it is +0.267 (axis) and +0.592 (face): an O(1) bare TT-mass term. A structural axis cancellation exists at x_γ = x_f/2, but it is non-universal.

**Controls.**
- The trace response sums to E2(0) to 7e-9, and isotropic scaling is exact.
- The continuum pure-gauge control gives about 1e-12, so the effect comes from the grid.
- Cubic covariance holds to 1e-14 and the vertex Ward identity to 2e-16.
- An exact-diagonalization check at L = 2 agrees to about 0.1%.
- The genuine KS staggered result equals the walker result ×½ to 6 digits.

**Plain reading.** On a fixed grid, the interacting vacuum resists being sheared, at about one part in a thousand per cell. A metric field coupled to it therefore picks up a mass at nearly the Planck scale, unless a bare counterterm is tuned to about 1e-100. This is the cosmological-constant problem's twin for the graviton mass. It is a naturalness failure, not a contradiction.

**Referee: codex gpt-5.6-sol xhigh, CONFIRMED WITH CORRECTIONS (2026-10-08).**

Confirmed:
- **The numbers.** Re-run with symmetric five-point differences: at L = 48, axis −0.0130346 and face +0.0124652, with the universal rule +0.0133654.
- **The generalized Coulomb-gauge reduction,** confirmed to 1e-14.
- **The face-channel photon averaging** is valid but not unique. Every alternative tried stays positive, from +0.01245 to +0.01375.
- **The universal rule** is a three-link path. Every path choice gives a nonzero response.
- **Not the source:** the photon zero mode and the fermion boundary conditions.

Corrections:
1. **The Coulomb convention should be named.** Using Candidate 1's alternating background charge adds −1/288 (axis) and +1/288 (face). That strengthens the result. With the whole Coulomb term removed, about ∓0.007 remains.
2. **The free-level counterterm is a c-number.** It cannot create the O(e²) result. An O(e²h²) counterterm can cancel it, and that is the tuning. Cubic symmetry allows separate E_g and T_2g contact terms, so "every local rule fails" is **not proved**.
3. **The mass interpretation is conditional.**
   - U(1) gauge invariance does not forbid h_TT², but gravitational diffeomorphism invariance would.
   - For an independent dynamical metric with this coupling, the term is a graviton mass term.
   - **A genuine coordinate relabelling that moves the lattice embedding, the reciprocal cutoff and the measure together can protect c₂ = 0.** The no-grid (proper-momentum) control demonstrates this, and Wetterich's "lattice diffeomorphism invariance" (arXiv:1110.1539) is the known framework.
4. **The 1e-100 tuning number is not derived.** It needs the lattice-to-Planck normalization and the graviton's kinetic term.
5. **For an emergent graviton, this is a naturalness diagnostic only.** The collective metric operator and its zero-momentum 1PI inverse propagator must still be computed.

**Recorded in `RESULTS`.** ("K3 gravity", gravity X) = 0. An explicit metric on the rigid grid is a naturalness kill on every room, so **Candidate 1 (Q L O B X) is dead.**

**Added to the matrix.** Gravity option **W**: dynamical geometry on fixed adjacency, with matter coupled only through relations, as in lattice diffeomorphism invariance (Regge/Wetterich). It is the escape the referee identified.

## Prior-art sweep for gravity option W (2026-10-08, Sonnet; literature from abstracts)

**The repo's Regge programme.** Everything in it is unaudited.
- **Flat-space results.**
  - Vertex displacements are exact zero modes.
  - The Regge action matches linearized Einstein–Hilbert, Q_h = −½ Q_EH + O(k⁴).
  - In 4D there are 15 edge classes against 10 metric components. One spurious direction is flat at quadratic order (Roček–Williams type).
- **Where it stands.**
  - The 09-03 4D note was downgraded. It has 7 small singular directions on shell against 5 off shell, which is unexplained, and no physical graviton.
  - Matter coupling, the physical graviton and nonlinear closure are all open.
- **The repo's own version of W.** "Embedding-inert" edge-length actions, read as a framework reading of the Lattice axiom being adjacency-only, are stated as a hypothesis (`CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_..._2026-06-10.md`).

**Literature.**
- **Wetterich (arXiv:1110.1539).** The invariance means the action does not depend on where the points are placed, and the metric is a collective field. The examples are sigma models and spinor gravity, with no gauge fields shown.
- **Bahr–Dittrich.** Discretization breaks diffeomorphism symmetry except around flat space. Perfect actions are known only in limited cases.
- **Hamber.** Regge simulations show smooth and rough phases.
- **Missing.** No result has a massless spin-2 with interacting matter and untuned couplings on fixed combinatorics.

**Two strains on W.**
1. Regge needs diagonal edges, which is more than nearest-neighbour adjacency. The Coxeter complex also has only S₄ × inversion symmetry, not all 24 proper turns.
2. Lengths are not readable unless derived from records.

**Next.** W1 and W2 were pre-registered in `KILL_SHEET.md` and launched.

## W2: vacuum Regge graviton count (2026-10-08)

**Verdict: PASS.** The worker is Sonnet 5.5. A PASS needs no referee under the recording rule.

- **Off the pole: nullity 5 at every real k (EXACT).**
  - 4 gauge vertex displacements, G_A ξ = 2(z_A−1)Σξ_a.
  - 1 spurious hyperdiagonal direction e_h.
  - The 4 body variables are auxiliary and massive at the cutoff.
  - The conformal mode has the usual wrong sign.
- **On the shell: nullity 7 = 5 + 2 TT (the plus and cross polarizations).**
  - The source propagator on conserved sources is −(4/Δ)(T·T′ − ½trT trT′). It has a simple pole whose residue has rank 2 (CHECKED).
  - **So the repo's "7 vs 5" is a counting convention**: 5 off the pole, 7 on it. It is not an artefact or an extra mode.
  - Prior art the sweep missed: `docs/REGGE_EXACT_REDUCTION_..._2026-09-13.md:193-231` already proves it, and the worker re-derived it independently.
- **The spurious direction has a cubic term.** The per-cell action is S = q³/8 + q⁴/32 + … along it. The provenance note's −4√2 t³ + (4023/256) t⁴ is reproduced.
- **Caveat.** "Has a cubic term" is not "massive": u has no propagator or gradient term, and its stability is untested. Scope: linearized, matter-free, flat background, with S₄ × inversion symmetry only.

**Effect.** The vacuum graviton on the fixed-adjacency Regge complex is healthy. Whether W survives now depends on W1, i.e. interacting matter.

## W1: interacting vacuum on a dynamical-length Regge complex (2026-10-08)

**Verdict against the fixed line: FAIL.** The worker is Sonnet 5.5. The referee (codex sol) is running, and nothing goes into `RESULTS` until it reports.

**The model.**
- **The complex.** 3D Kuhn/Coxeter, with 7 edge classes. Each tetrahedron's metric comes from its six edge lengths.
- **The weights.** Whitney/Galerkin Hodge stars, with no free parameter: Nédélec mass for the electric term, Raviart–Thomas mass for the magnetic term. Circumcentric DEC is degenerate on this complex, so it could not be used.
- **The fields.** The photon lives on all 7 edge classes: 2 physical modes plus 4 gapped lattice modes. The fermion is P1-Galerkin Weyl with Peierls links. It is not staggered and has 2 extra nodes.
- **The coupling.** Universal by construction, since both sectors follow one geometry.

**The TT Hessian (volume-preserving), at L = 24 (converged to about 1e-4).**
- At O(e⁰), the E-block eigenvalues are −0.931 and +0.403. They are dominated by the gapped photon modes.
- At O(e²)/e², they are −0.01395 and +0.00552, which is about 1.3e-3 per cell at physical α.
- The Kuhn complex has only S₃ symmetry, so A1 tadpoles exist.

**The mechanism (CHECKED).**
- **The local weights are covariant.** Uniform scaling gives E(λ) = E/λ to 2e-16.
- **The breaking comes from the fixed index-space Brillouin zone.** In a free-fermion diagnostic, a momentum window fixed in index space gives a nonzero TT response, while a window that follows the strain gives about zero.
- So under strain the lattice's cutoff is not a proper-momentum ball. **A strained fixed-adjacency lattice is a different crystal, and it carries elastic (TT) stiffness at the cutoff scale.**

**Controls.**
- The exact-diagonalization check at L = 2 agrees to 0.05%.
- The Ward identity holds to 2e-16.
- S₃ covariance holds to 1e-16.

**Supervisor reading.** If the referee confirms, this is the TT twin of the cosmological-constant problem. On a lattice whose adjacency, and therefore whose Brillouin zone, is fixed, the vacuum has a cutoff-scale shear stiffness whether the lengths are rigid (K3a″) or dynamical (W1). A graviton coupled to that vacuum is massive unless tuned. Two escapes would remain:
- an emergent graviton with an exact emergent constraint (no construction exists);
- an action that does not depend on where the points are placed, Wetterich-type, a new candidate with different content.

Otherwise the casualty is the **fixed adjacency itself**, which is the Lattice axiom, and that is an owner decision.

**W1 referee: codex gpt-5.6-sol xhigh, CONFIRMED WITH CORRECTIONS (2026-10-09).**

Confirmed:
- **The construction.** The Whitney/Galerkin construction is the legitimate lowest-order FEEC Hodge. Note that "parameter-free" does not mean unique.
- **The photon.** Two IR modes, ω²/q² = 1 ± 4e-6.
- **The geodesic Hessian formula.** A direct five-point check at L = 12 gives (−0.013915, +0.005659)e². The L = 24 values and the O(e⁰) values both reproduce.
- **The controls.** Uniform scaling, S₃ covariance and the Ward identity all hold to about 1e-16.
- **The BZ mechanism, for the free IR cone.** A momentum window fixed in index space gives E″/K₀⁴ = −1/(60π²) = −0.00169, and one that follows the strain gives exactly 0.

Corrections:
1. **Convergence.** "1e-4 relative" is too strong: the positive E eigenvalue moves by about 1% between L = 16 and 24. It is still converging to a nonzero value.
2. **The fermion has at least 18 nodes, not 2**, so it is not a single-Weyl regulator. Its normalization is half a Weyl determinant; the physical normalization doubles the O(e²) values and strengthens the FAIL.
3. **The O(e⁰) stiffness is photon-dominated.** Keeping only the two lowest photon bands still gives nonzero O(e²) E eigenvalues.
4. **A physical graviton mass needs more.** It needs tadpole cancellation or a stationary background, plus kinetic normalization. The linear-path Hessian is also nonzero, so this does not rescue W1.
5. **Untested:** a second Hodge or fermion discretization on the same complex. The ED script is not reproducible from the packet.

**What it is not.** It is not a universal no-go. These escapes remain open:
- exact emergent diffeomorphism constraints;
- position-blind (Wetterich) actions;
- embedding-and-reciprocal-cutoff covariance;
- protected field-content cancellations;
- suitably dynamical adjacency, which alone is not sufficient.

"TT twin of the cosmological-constant problem" is a naturalness analogy, not a theorem.

**Recorded in `RESULTS`.** ("K3 gravity", gravity W) = 0. **Explicit dynamical-length geometry on fixed adjacency fails.**

## Where gravity stands after wave 1 (2026-10-09, supervisor)

| Option | Status |
|---|---|
| Explicit metric, rigid grid (X) | **Dead** (K3a″, refereed) |
| Explicit dynamical lengths, fixed adjacency (W) | **Dead** (W1, refereed). Vacuum Regge graviton healthy (W2) |
| Emergent graviton (G) | No construction. Finite-slot harmonic no-gos (probes 10/20/21: light-like TT forces a light-like ±1 partner; exact slides give ω ~ q²). Needs an exact emergent constraint that also protects zero TT stiffness |
| Induced or entanglement gravity (I) | Jacobson dead on the grid; no propagating spin-2 |
| Record-carried gravity (R) | Falls short (campaign 8) |

**Escapes outside the tested settings.**
- Wetterich position-blind actions, a new candidate with different content.
- Exact field-content cancellation. Lattice SUSY is the obvious kind, but SUSY broken at the TeV scale would leave about (TeV/M_P)⁴ ≈ 1e-60, far above the about 1e-102 needed. This is suggested, not computed.
- Dynamical adjacency, which changes the Lattice axiom.
- Accepting tuning, which means inheriting a second cosmological-constant-sized fine-tuning.
