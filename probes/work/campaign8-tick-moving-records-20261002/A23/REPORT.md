# A23 report: gravity as a field of the shared possibilities. Requirements, tensions and decisive tests

**Scratch directory:** `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A23/`
- `spin2_cubic_check.py`: the one tiny check, parts C1–C8.
- `out_spin2_cubic_check.txt`: its output.
- `time_spin2.txt`: run statistics (3.9 s, 216 MB peak).

**Grades.**
- **EXACT**: proof, or exact algebra or arithmetic.
- **CHECKED**: numeric check with a stated tolerance.
- **ARGUED**: reasoning without proof.
- **COMPARATOR**: literature or experiment, quoted from memory and unverified. Never adopted.

**Status and what I did not do.**
- Everything here is derivation planning on supplied toys. F1–F5 below are named conditionals. I1–I6 and Q-decisions are used only as "if … then …".
- Repo reading was read-only: `git show` / `git ls-tree` on the existing `origin/main` ref `e485eab6b0` (2026-10-02 11:34 UTC). There was no fetch and no edits.

---

## 1. Question

Suppose gravity is a smooth field carried by the shared possibilities. It is sourced by matter (or records), carried wave-like by the fixed change on a shared beat, and it acts on clocks through fixed interactions.
- What must that field sector have?
- Which requirements can a single-number (scalar) field meet, and which need a tensor (spin-2) field?
- How does the route interact with the campaign's open tensions?
- What do the landed (unaudited) repo notes on Regge gravitons and the U(1) photon already offer?
- Which few computations would most quickly confirm or kill it?

## 2. Answer

**Conditional yes, ARGUED overall, with EXACT and CHECKED pieces.** Several things get better automatically on a field route:
- **No signalling.** The pace is an operator inside a fixed change, not a rule that picks the change from the state, so nothing signals [EXACT].
- **No wakes.** A z = 1 wave carrier makes the field of a moving source the boosted static field [EXACT in the continuum].
- **Natural 1/r.** The static 1/r follows from gaplessness alone [EXACT].
- **Noise.** It is suppressed by the gravitational coupling squared, not by an averaging radius [ARGUED; the scaling is EXACT].

**The scalar branch** can give z = 1 waves, 1/r and universal redshift, the last by choice. But:
- With couplings built only from the field and the flat background, light bending has γ = −1 at linear order [EXACT].
- γ = 1 needs a privileged frame, A18's product composition, which is a stratified metric (COMPARATOR: fails preferred-frame tests).
- It has no frame dragging and the wrong waves.

**The tensor branch** can meet every linear-order requirement. The tiny check here found that its free numbers collapse onto one named conditional:
- Cubic covariance plus linearized spatial gauge invariance leaves exactly one O(k²) potential, the linearized Einstein–Hilbert one [CHECKED to 1e-15].
- Requiring the field's change to preserve the linearized "how much time passes here" (Hamiltonian) constraint then forces GR's kinetic weights, (−½, 1, 1) [CHECKED; EXACT by hand]. That gives isotropy, no gravitational-wave birefringence, and no extra scalar ripple.
- Any other kinetic weights give a birefringent tensor wave plus an unstable or ghost scalar [CHECKED].
- With that conditional, a local reversible leapfrog tick preserves both constraints at every layer, is z = 1, and keeps phases below π (no time doubler) [CHECKED at symbol level].
- The static field gives γ = 1 when the lapse also paces the field's own change [CHECKED].
- Universality among interacting species is forced by source conservation [EXACT].

**New costs specific to the tensor branch:**
- The source must be conserved energy-momentum. So forming records must not change energy, or the field keeps a permanent "ghost source" where the record formed. One-site locks of moving matter break this badly [EXACT core].
- One qubit per site must somehow host the field (payload, open).
- β = 1 needs a second-order derivation (open).

## 3. Derivation

### 3.0 Setup and named conditionals

- **F1 (field sector).** Degrees of freedom in the shared possibilities that are linear at long wavelength. Records never lock them. The fixed, local, reversible change carries them on the shared beat (A15).
- **F2 (fixed coupling).** Matter's local change carries field-dependent factors: a lapse on one-site terms and a frame on bond terms. These are operators inside the change, never state-dependent rules.
- **F3 (source).** The field is sourced by an operator density of the possibilities: energy and momentum.
- **F4 (tensor version).** The field's change preserves the linearized momentum and Hamiltonian constraints.
- **F5 (formation).** The formation weight acts on matter, F_x = N̂_x ⊗ F_m or F_m ⊗ 1, never on field excitations alone.

### 3.1 What any field route gets for the four A17/A18 obstacles

- **D1 [EXACT] No signalling.** A fixed coupling layer is part of a fixed finite-depth local circuit, which is linear in the state, so it keeps the strict cone and no-signalling (A5 T1.1, T1.2).
  - What signals (A9 Th.2(d), A15 S11) is choosing the dose as a nonlinear function of the possibilities.
  - So "paces set by unrecorded possibilities" is safe exactly when the pace is an operator inside a fixed change.
- **D2 [EXACT] 1/r from gaplessness.** Take a field obeying (∂_t² + K(k))φ = J, with K analytic, O_h-symmetric, K = c²|k|² + O(k⁴) and K > 0 for k ≠ 0. The cubic-invariant quadratic in k is only |k|².
  - Its static Green function is 1/(4πc²r) + O(r⁻³), by standard Fourier asymptotics as used by A6/A17.
  - So 1/r follows from z = 1 plus gaplessness, with no sink, unlike A6/A8.
  - Gaplessness must be protected. A scalar mass term is cubic-invariant and allowed, which brings screening as in A6. A gauge field's mass term is not gauge invariant.
- **D3 Moving sources.**
  - EXACT in the continuum, ARGUED on the lattice with O((a/r)²) corrections.
  - A wave equation with source ρ(x − vt) gives the boosted (Heaviside-ellipsoid) static field with no upstream screening. That removes A18 D23's wake for scalar and tensor alike.
- **D4 Noise [ARGUED; scaling EXACT for linear response].**
  - The field is sourced by energy with gravitational strength, so its fluctuations from source shot noise scale as G² × (source fluctuations), i.e. per source quantum as (m/m_P)².
  - A17 Theorem 2 does not apply, because the drive is not a record gas.
  - Gravity's weakness becomes "matter is light on the grid" (m_p/m_P = 7.7e-20, EXACT arithmetic), not a tuned capture odds; A8 had q ≈ 1e-18.
- **D5 Momentum [EXACT in the linear theory].**
  - Momentum lives in unrecorded matter possibilities and in field waves.
  - The vector (frame-dragging) sector is sourced through the momentum constraint by matter's momentum density, an operator.
  - Records, which carry no momentum (A7/A13), cannot source it. So F3 must use possibilities, not record counts.

### 3.2 The scalar branch

- **D6 [EXACT] No consistency condition on the source.** A scalar wave equation is solvable for any source, conserved or not, and species-universal or not.
  - So universality is possible, via conformal or uniform-dose coupling (COMPARATOR: Nordström's theory is a metric theory and obeys the weak equivalence principle), but it is never forced.
- **D7 [EXACT at linear order, 1/r terms] Light bending.** A metric built only from φ, its derivatives and η has g = (1 + 2aφ)η + O(∂∂φ). The derivative terms give no 1/r part, so γ = −1: there is no light bending, since light ignores a conformal factor.
  - In A18 D17's language (one-site pace N^a, two-site N^b, γ = b/a − 1):
    - b = 0 is Nordström, γ = −1 (COMPARATOR: Nordström has γ = −1, β = ½, perihelion −1/6 of GR);
    - b = a is lapse-only, γ = 0 (A14);
    - b = 2a gives γ = 1, but the metric −N²dt² + N⁻²dx² is not conformally flat. It needs the lattice rest frame as a preferred vector: a stratified theory, which carries preferred-frame terms (COMPARATOR: stratified theories in Will's catalogue; α-type bounds).
- **D8 [EXACT] Waves and dragging.** A scalar has no vector part, so g₀ᵢ ≡ 0 from mass currents (A18 D22, unchanged by wave transport). It has one scalar polarization, not two tensor ones.
- **Verdict.** A scalar meets R1, R2 and R3 (by choice, D6). It fails R4 without a preferred frame, and fails R5 and the dragging part of R6.

### 3.3 The tensor branch: what cubic covariance plus gauge invariance force

Work in the linear theory: h_ij is symmetric (6 components), π_ij is its conjugate, H = ½π·M·π + ½h·V(k)·h, and gauge directions are δh = kξ + ξk.

| Step | Result | Grade |
|---|---|---|
| D9 | Cubic-invariant kinetic forms on symmetric tensors: 3 (A1 trace, E diagonal-traceless, T2 off-diagonal), under O_h and under O. | EXACT (Schur); CHECKED C1 |
| D10 | Cubic-invariant O(k²) potentials: 9. Spatial gauge invariance leaves exactly 1, the linearized Einstein–Hilbert form. The TT part is +½k² and the transverse-trace (conformal) part is −½k², so the conformal sign is forced. | CHECKED C2 (deviation ≤ 1.4e-15) |
| D11 | Preserving the linearized Hamiltonian constraint R(h) = k²tr h − k·h·k on constraint-satisfying momenta holds iff (m_A1, m_E, m_T2) ∝ (−½, 1, 1). Proof: for transverse π, R(Mπ) = ŝ²trπ(2m_A1 + m_E)/3 − (m_E − m_T2)Σs_i²π_ii, which vanishes for all such π and all s iff m_E = m_T2 and m_A1 = −m_E/2. One condition therefore gives both isotropy and GR's trace weight (λ = 1). | EXACT; CHECKED C3 (1-dim null space) |
| D12 | Otherwise (CHECKED C4, λ²/k² values): m_T2 = 1.1 makes the tensor wave birefringent (1.1 vs 1.0 along an axis) and makes the scalar grow off-axis (+0.024 face, +0.033 body). m_A1 = −0.40 gives a growing (tachyonic) scalar (+0.067). m_A1 = −0.60 gives an oscillating scalar whose kinetic and potential weights are both negative, i.e. a ghost. COMPARATOR: Hořava-type scalar mode. | CHECKED |
| D13 | With GR weights, ∂_t R(h) ∝ s·(πs). So the Hamiltonian constraint propagates whenever the momentum constraint and source continuity hold, with no elliptic solve per beat. The strict cone survives. | EXACT |
| D14 | 4D version: the hypercubic group B4 (384 elements) on the Euclidean Z³×Z_τ regulator gives 9 invariant forms. 4D gauge invariance leaves exactly 1, the 4D linearized Einstein–Hilbert form. Its k_τ² block on spatial h has A1:E:T2 = −2:1:1, which is GR's kinetic metric h:h − (tr h)², and its spatial block equals the 3D potential. So the owner-approved kinetic-isotropy primitive (c_t = c_s), extended to a 4D gauge-invariant field, would supply D11's weights. The Lorentzian step (OS reconstruction) is open. | CHECKED C5 (residual 2e-16) |
| D15 | Leapfrog "Yee for spin-2" at symbol level (s_j = 2 sin(k_j/2), staggered): both constraint rows are preserved by every shear. The tensor-wave dispersion is cos θ = 1 − τ²ŝ²/2. z = 1, with θ/(τ|k|) = 0.99999. For τ < 1/√3, all phases stay below π (max 0.91π at τ√3 = 0.99); at τ√3 = 1.01 it is unstable (|eig| 1.33). There are exactly 2 propagating polarizations, and ŝ = 0 only at k = 0, so no spatial doubler. | CHECKED C6 |
| D16 | Static source in linearized ADM with the lapse multiplying the field's own potential gives n = −U (U = ρ/4k²) and h_ij = 2Uδ_ij modulo gauge, so γ = 1.000000. If the field is unpaced, there is no static solution. This is the opposite of A18 D14, where the record-gas carrier had to be unpaced. | EXACT; CHECKED C7 |
| D17 | Universality forced. The field's source S = Σ_s g_s T_s must be conserved (D13). When species exchange energy-momentum, ∂S = −½Σ(g_s − g_{s'})X_{ss'}, so g_s = g_{s'} for every interacting pair. COMPARATOR: Weinberg 1964 low-energy theorem. | EXACT |
| D18 | Shear needs a frame. The length² of an axis bond is 1 + h_ii, independent of the off-diagonal h. So a field that only rescales nearest-neighbour axis bonds leaves such matter blind to T2/TT shear at first order. Matter must couple through a local frame (soldering) structure. In the axioms' register, Q3's gluing would tilt locally as part of the field, while the law itself stays glued to the grid's rotations. | EXACT (bond algebra); ARGUED reading |
| D19 | Equivalent "harmonic" form: ten same-speed lattice waves h̄_μν sourced by −16πG T_μν. The gauge condition ∂^μh̄_μν = 0 is preserved iff the source is conserved and all components share one operator, which again forces equal speeds. Trace reversal gives h_00 = h_ii, i.e. γ = 1. COMPARATOR: Choquet-Bruhat. | EXACT (standard algebra); ARGUED on the lattice |
| D20 | β = 1 is not fixed at linear order. In GR it follows from second-order self-coupling: the field's own energy gravitates. COMPARATOR: Deser 1970; Hojman–Kuchař–Teitelboim 1976, where closure of the constraint algebra yields GR. | ARGUED |

### 3.4 Requirements: scalar against tensor (Task 1)

**Reading of R6.** "No frame-independent drift" is taken as two things: (i) no built-in vacuum drift (A1 D12, A5 T6.1); (ii) no preferred-frame effects, so a moving source's field is the boosted static field.

| Requirement | Scalar field | Tensor (spin-2) field |
|---|---|---|
| R1: z = 1 waves at light speed | Yes, but masslessness is unprotected (D2), and equality with light's speed is a supplied equality | Yes, with gauge-protected masslessness. Equal speeds across components are forced (D11, D19). Equality with light needs a common normalization across sectors, for example the kinetic-isotropy primitive extended (D14) |
| R2: 1/r static | Yes (D2) | Yes (D16) |
| R3: universal clock slowing by a fixed interaction | Possible, not forced (D6) | Forced among interacting species (D17) |
| R4: γ = 1 | γ = −1 (conformal), or γ = 1 only with a preferred frame (D7) | Forced, γ = 1 (D16, D19) |
| R4: β = 1 | Dialled in (A18 D10: exponential F) | Second-order question, open (D20) |
| R5: tensor waves | No (D8) | Exactly 2 polarizations, given F4 (D12, D15) |
| R6(i): no vacuum drift | Yes (covariance) | Yes |
| R6(ii): no preferred frame or wake; dragging | Wakes removed by waves (D3); dragging none; stratified γ = 1 version carries α-type terms | Dragging via the momentum constraint (D5); no preferred frame at linear order given F4 (ARGUED) |

**So the tensor sector is needed for:** γ = 1 without a privileged frame, frame dragging, two-polarization waves, and universality that is forced rather than chosen.

### 3.5 Tensions (Task 2)

| Tension | Field-route verdict | Why | Grade |
|---|---|---|---|
| (a) Quiet vacuum vs z = 1 (A9, A12) | **Better**, conditionally | See below | EXACT pieces; ARGUED overall |
| (b) Per-site memory (A12) vs Q2 snapshot | **Better** for the beat; **neutral** for formation | See below | ARGUED |
| (c) Covariance and sublattice privilege (A16 C7) | **Better** for the field; **neutral** for matter | See below | ARGUED; symbol EXACT |
| (d) Time doublers (A5 T4, A19 R3) | **Better** for the field; **neutral** for matter | See below | EXACT for the field; ARGUED for the coupling |
| (e) Single-particle W3 = 0 (A1, A2) | **Neutral** | See below | ARGUED/COMPARATOR |
| (f) NEW: conserved source vs formation | **Worse**, specific to the tensor branch | See below | EXACT core; ARGUED numbers |
| (g) NEW: payload | **Worse**, open | See below | ARGUED |
| (h) NEW: lattice energy-momentum conservation | **Worse but small** at low energy | See below | ARGUED |
| (i) NEW: shared beat vs Hamiltonian constraint | **Neutral to better** | See below | EXACT linear; ARGUED link |

**(a) Quiet vacuum vs z = 1.**
- With F5 and a source that annihilates the matter vacuum (T|vac_m⟩ = 0, as for A13's aligned emptiness), the joint vacuum is a stationary product. A9's criterion then needs only the matter marginal to be rank-deficient. The full-rank z = 1 field vacuum is never acted on by formation.
- Formation odds may carry the lapse operator, F = N̂ ⊗ F_m, and stay quiet. That supplies A15 S14's "formation odds ∝ N".
- **Neutral** for a pair-creating Dirac-sea matter vacuum: matter formation still needs A12's windows and memory.
- **Worse** if the field must be a collective mode of the same possibilities. The repo's ring photon shows exactly this: quiet at the RK point, linear only away from it.

**(b) Per-site memory vs Q2 snapshot.**
- The retarded history lives in the field's current possibilities, which Q2 allows. That dissolves A17 L2.
- A12's windows are needed only where formation must stay quiet in a z = 1 matter sea.

**(c) Covariance and sublattice privilege.**
- The field's layers alternate by field role (h-shear, π-shear), and each layer is covariant. There is no law-level pair-cycling.
- Doubler-free exact gauge invariance needs staggered placement: diagonal components at vertex roles, off-diagonal at face roles. On Z³ sites that means role-encoded possibilities, as in the repo's U(1) role compiler (law covariant, 8 state-level translates).
- So the privilege is relocated, not removed. Matter's own A10/A16 C7 problem is unchanged.

**(d) Time doublers.**
- The CFL bound keeps the field's phases below π (D15, C8). The Regge note's proposed dispersion, continued, has band top 2.634 < π.
- A smooth field is an adiabatic coupling, so it adds no sharp-contact umklapp.
- Matter's own doubler and A19 R3's contact umklapp are untouched.

**(e) Single-particle W3 = 0.** The field is bosonic and non-chiral. If net chirality is ever obtained, it adds one condition: gravitational-anomaly cancellation (COMPARATOR).

**(f) NEW: conserved source vs formation.**
- Physical states satisfy C = R(ĥ) − ρ̂ = 0. A formation Kraus operator K preserves this if [K, ρ̂] = [K, Ĵ] = 0.
- Otherwise the violation persists as a static "ghost source" equal to minus the energy change at the formation site (D13). Repairing it at once would shift the far field instantly. That signals whenever the outcome-averaged Lüders energy change −½Σ⟨[P_k,[P_k,H]]⟩ ≠ 0.
- U(1) is fine: occupation locks commute with charge.
- Gravity is not: [n_x, hop_xy] ≠ 0. A one-site lock spreads momentum uniformly over the zone, injecting energy of order the bandwidth, Planck-scale under the identification.
- So the tensor branch requires energy-gentle (coarse/mediated) or energy-commuting locks. That is the same direction A19 reached independently from inertia.

**(g) NEW: payload.** A linear bosonic component needs an unbounded local space. One qubit per site gives either role-encoded truncated components or a collective, emergent field. Whether a qubit lattice gives a gapless spin-2 sector with this constraint structure is open (COMPARATOR: Gu–Wen 2006; Xu 2006; Pretko 2017; Weinberg–Witten as a caution).

**(h) NEW: lattice energy-momentum conservation.**
- Conservation holds only up to umklapp and Floquet heating. At low energy these are kinematically or exponentially suppressed (COMPARATOR: Abanin–De Roeck–Ho–Huveneers).
- Risk: an infrared graviton mass would cut linear light bending to 3/4 of GR (COMPARATOR: vDVZ). So infrared gauge invariance must be protected.

**(i) NEW: shared beat vs Hamiltonian constraint.**
- At linear order the constraint propagates locally (D13, C6). The beat can serve as a harmonic-type slicing (ARGUED).
- F4 is the field-level analogue of A5 T3.1: physics must not depend on how the beat is laid out locally.

### 3.6 Repo cross-reference (Task 3)

All read-only at origin/main e485eab6b0. Every ledger row below has `audit_status: unaudited`.

| Note (short name) | Ledger | What it supplies | Connection (not imported) |
|---|---|---|---|
| `THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_…_2026-09-03.md` (exists; corrected title "Finite spectra and metric projections of a supplied cubic-Coxeter Regge Hessian"; the filename's headline is superseded) | unaudited / effective unaudited; bounded_theorem; criticality medium; deps minimal_axioms, kinetic_isotropy_primitive | Supplied Euclidean Z³×Z_τ Hessian; finite kernel scans (ker Q = 5, ker Q_h = 4 at four momenta); proposed dispersion 4sinh²(ω/2) = Σ4sin²(k_i/2), to 3.3e-13 at 32 points; approximate TT projections (≈1 at k = .05; .957/.891 at k = 3). States explicitly that it gives no physical graviton, OS reconstruction or Record-to-geometry law | Its proposed dispersion is D15's staggered symbol in Euclidean form. D14 shows that hypercubic symmetry plus 4D gauge invariance force the 4D EH form it approximates. Its continued band stays below π (C8). It does not supply what the route needs: a Lorentzian tick, a matter coupling, or formation compatibility |
| `THE_FORMATION_RATE_DEFINES_THE_STATIC_REGGE_EDGE_LENGTHS…_2026-09-03.md` (corrected title "Finite static Regge source response under a supplied endpoint-mean field") | unaudited | Q δl = +2ΔΦ e_τ (lattice Poisson, sign fixed); zero spatial source selects ν = 1 on finite modes; readouts gauge-dependent | The Regge-side analogue of D16 (γ = 1 from the field equations). In the field route, Φ is the field's lapse, not a formation rate; the note itself does not derive a rate meaning |
| `THE_SPATIAL_HALF_OF_THE_METRIC_IS_ONE_DECLARED_WEIGHT_ON_THE_HOP_TERM…_2026-09-03.md` | unaudited (the ledger `claim_type` still reads positive_theorem; the corrected frontmatter says bounded_theorem) | Supplied weights H(α,β) = H0 + {Φ, αM + βmΓ}/2; (2,1) matches γ = 1 at low momentum | (2,1) is A18's product composition. Under F2–F4 it would follow from h_ij = 2Uδ, n = −U (D16) instead of being chosen [ARGUED] |
| `THE_TWO_TT_GRAVITON_POLARISATIONS_ARE_READ_BY_THE_AXIS_BOND_PAIR_RECORD_STATISTICS…_2026-09-04.md` | unaudited | For the KS sea, length-only dressing gives zero shear response; a period-2 T2 intertwiner or a centred curl restores TT rank 2 | Independent instance of D18: shear needs a frame-like coupling |
| `U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_…_2026-09-03.md` | unaudited (in-note "proposed_retained") | 3 local shears; exact Gauss rows per shear; all 48 cubic transformations; conserved local form for h < 1/√3; θ = 2asin(h\|s\|/2) | The template for D15. For spin-2 the Hamiltonian row must also be preserved, and that is what forces GR's weights (D11) |
| `U1_RADIUS_ONE_ONSITE_UNITARY_MINIMAL_MAXWELL_TICK_BOUNDED_NO_GO_…` | unaudited; no_go | A one-layer radius-one gauge-compatible unitary cannot propagate | Same structure as A3 Step 10 and A2 D10. The field route uses role-alternating finite depth |
| `U1_ROLE_ENCODED_DOUBLED_INCIDENCE…_2026-09-03.md` | unaudited | Role labels inside site possibilities; covariant law; 8 translates; payload readability on one qubit open | Template for tension (c); carries the same open payload issue (g) |
| Ring-model photon notes (`…SOFTEN_FROM_THE_PURE_RING_POINT_TO_THE_RK_POINT…`, `ROUND_FOUR_SYNTHESIS…`, `…REGION_BOUNDED_BY_RECORDS…`, `DYNAMICS_CLAUSE_…ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_RK_POINT…`) | all unaudited | At V = 1 (RK), component Hamiltonians are positive graph Laplacians with an exact zero-energy uniform ground state. Energy-only upper bounds soften toward RK; no dispersion is established | The repo's own collective-field instance of A9/A12: quiet at RK, linear only off RK (tension a, collective version) |
| `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS…` | unaudited | Gauss law conserved with occupation-type records | The U(1) case of (f) works; the gravity analogue fails for occupation locks |
| `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | meta (owner-approved primitive per its text) | c_t = c_s; hypercubic Euclidean regulator, for matter | D14: extending it to a gauge-invariant field supplies GR's kinetic weights. That extension would be an owner decision |

## 4. Checks

**Run:** `spin2_cubic_check.py`, numpy only. `nice -n 10`, four thread caps at 1, 58 s alarm. Wall time 3.9 s, peak RSS 216 MB, machine load about 3.3.

| ID | Checks | Result | Tolerance |
|---|---|---|---|
| C1 | Invariant kinetic forms | 3 under O_h(48) and O(24) | projector eigenvalue > 0.5 |
| C2 | Invariant O(k²) potentials; gauge-invariant subset | 9; exactly 1. It equals linearized EH to 4.4e-16 (O_h) and 1.4e-15 (O). TT +0.5k², transverse-trace −0.5k² | SVD 1e-9 |
| C3 | Hamiltonian-row preservation | 1-dim null space ∝ (−0.5, 1, 1) | SVD 1e-9 |
| C4 | Reduced modes in 4 directions | GR: TT speed² = 1, scalar 0. Anisotropic and λ-shifted values as in D12; kinetic weight ±0.1333 against potential weight −0.5 | 1e-6 rounding |
| C5 | B4 4D | 9 invariant forms, 1 gauge-invariant; A1/E = −2.00000, T2/E = 1.00000 (residual 2e-16); spatial block = EH to 1.5e-16 | — |
| C6 | Leapfrog symbol | Constraint rows preserved to 3.2e-15 / 2.3e-15 at 200 random k. m_T2 = 1.1 breaks the Hamiltonian row by 0.138. TT block invariant (leak ≤ 3.2e-15). Power traces j = 1–12 confirm spectrum {1 × 8} ∪ TT (≤ 9.1e-12). cos θ formula holds to 8e-16. Max phase 0.9099π at τ√3 = 0.99; \|eig\| = 1.327 at 1.01 | 13³ zone grid |
| C7 | Static γ | 1.000000 at two momenta (residual ≤ 5e-16); unpaced variant has no solution (residual 0.333) | — |
| C8 | Arithmetic | 2asinh(√3) = 2.633916 < π; Yee band top 2asin(h√3) | exact |

**First-run errors, fixed.**
- The gauge-constraint matrix in C2/C5 was stacked with the wrong orientation, giving a spurious "0 gauge-invariant forms". This contradicted the direct EH gauge check (1e-16), which exposed it.
- C6's unit eigenvalue is defective (gauge and constraint Jordan blocks). Eigensolver splitting of it polluted the first counts; I replaced the count with the invariant-block and power-trace tests above.

**Should be run next (tiny; not run):** the T2 and T3 toys in §6.

## 5. Real-physics match

**If F1–F5 hold, the tensor branch reproduces at linear order:**
- Cassini γ (|γ − 1| ≲ 2e-5, COMPARATOR);
- Shapiro delay and light bending;
- two tensor polarizations;
- frame dragging (GP-B −37.2 ± 7.2 against GR −39.2 mas/yr, COMPARATOR);
- universal free fall among interacting species (MICROSCOPE ~1e-15, COMPARATOR);
- no wakes and no preferred-frame terms;
- quadrupole radiation from conserved sources (Hulse–Taylor ~0.2%, COMPARATOR; ARGUED).

**The scalar branch is falsified by** frame dragging, gravitational-wave polarization tests, and γ (or α-type preferred-frame bounds, |α2| ≲ 1e-7–1e-9, COMPARATOR).

**Falsifiers of the tensor branch:**
- A difference between gravitational-wave and light speeds (GW170817: −3e-15 to +7e-16, COMPARATOR). That would mean no common normalization across sectors.
- Gravitational-wave birefringence or anisotropy. That would mean F4 fails (D12).
- An extra scalar polarization.
- Gravitational-wave decoherence. That would mean field possibilities get locked.
- O(1) equivalence-principle violation for species whose rest energy sits in two-site terms (A18 D3). That is a matter-sector requirement and is unchanged here.
- Gravitating negative "ghost" energy where records form, equal to minus the formation heating. It is tiny if locks are gentle, and testable in principle.

**Not determined here:** β, second post-Newtonian order, horizons. On this route a black hole would be a field configuration with N → 0, not a jam (I5).

## 6. Open edges and next steps

**T0, done here.** Do cubic covariance and gauge invariance leave free anisotropy or scalar-mode numbers? The potential is forced. The kinetic form is forced iff F4 holds. Otherwise the tensor wave is birefringent and the scalar is unstable or a ghost. So the tensor branch reduces to one named conditional, F4.

**Ranked decisive tests:**
1. **Energy-gentle locks.** Derivation plus a tiny 1D toy, hours.
   - *Question:* can a Record-compliant lock (one site, one possibility) commute with the field's source density? Failing that, can a mediated lock (A19 R2), including the sharp lock on its probe, inject energy far below the bandwidth?
   - *Kill:* if every lock registering moving matter injects band-scale energy, every record leaves a Planck-scale ghost source.
2. **Payload.** Counting plus a small exact-diagonalization toy; days, open.
   - *Question:* can role-separated qubit sites host a field sector that is linear (z = 1) with both constraints, never locked?
   - *Kill:* if a spin-2 sector exists only as a collective mode sharing sites with matter, tension (a) returns in full and A12's memory is needed.
3. **Real-space "Yee for spin-2".** Tiny toy, under 1 min, under 100 MB.
   - *Question:* does a first-order (curl-split) role-lattice version keep every layer nearest-neighbour and covariant under the 24 vertex rotations with role relabelling, with constraints preserved to round-off?
   - *Also:* does an unstaggered, exactly covariant, doubler-free, gauge-invariant form exist?
4. **Matter coupling.** Tiny to medium 2D toy.
   - *Question:* coupling A18's time-symmetric one-site-mass Dirac step through a lapse and a frame field (period-2/curl for shear), do packets give γ = 1 with no composition choice, universal fall for one-site masses, and response to h_xy?
   - *Expected:* two-site masses keep their O(1) violation.
5. **Second order.** Derivation, larger.
   - *Question:* is the constraint-preserving second-order self-coupling unique, and does it give β = 1? COMPARATOR: Hojman–Kuchař–Teitelboim, Deser.

**What this would ask the owner to decide (axioms' register):**
- Whether the shared possibilities may carry a never-locked field that the fixed change carries and that multiplies the change's dose locally.
- Scalar or "shape" field.
- Whether the field's bookkeeping is exact (F4, slicing independence).
- Whether Q3's gluing may tilt locally as part of the field.
- Whether the field is fed by the possibilities' energy and momentum rather than record counts.
- Whether forming records must leave energy unchanged.
- Optionally, whether to extend the kinetic-isotropy primitive to the field sector.

**Other edges:**
- Infrared protection against a graviton mass (vDVZ).
- Quiet vacuum for pair-creating matter (A12).
- Gravitational-anomaly cancellation for future chiral matter.
- Common light cone across sectors.

## 7. Plain-language summary

"Gravity as a field of the possibilities" would mean that every place carries, besides its matter, a smooth stretch that records never lock, that the fixed rule passes from neighbour to neighbour at the speed of light, and that is pushed by where energy and motion are. Clocks would slow near a heavy body because the rule multiplies how much changes there per beat by this stretch. The slowing would then be the same on every run, and no faraway choice could leak through it. A stretch that is one number per place gets the slowing and its fall-off with distance right, but it bends light by the wrong amount unless the grid's own resting frame is singled out, and it makes the wrong kind of ripples. A stretch that also says how each direction is squeezed and twisted can do all of this. The small calculation here found that if its bookkeeping is kept exact, the grid's own turns fix every remaining number as in Einstein's gravity. It would ask you to decide whether such a field may live in the shared possibilities, whether the rule's gluing to the grid may tilt from place to place, and whether a forming record must leave energy unchanged, since otherwise the field keeps a phantom weight wherever a record formed.