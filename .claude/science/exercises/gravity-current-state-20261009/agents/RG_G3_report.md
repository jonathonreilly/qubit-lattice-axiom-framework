# Lane RG, probe G3 (sourcing and consequence): report

Worker: Claude Opus 5.5 (same family as the supervisor), 00:54Z to 01:40Z, 2026-10-11. No repository files were edited. Scratch folder: `.../scratchpad/laneRG/G3/` (scripts `g3_*.py`, outputs `g3_*.out`). Nothing here has been refereed.

## Reading against the FIXED lines

G3 bears on the third PASS item only: "that momentum sources the VS shift constraint consistently at linear order". G3 cannot give the lane a FAIL; that comes from G1's identity theorem.

- **The third PASS item is conditionally achievable.** Linear-order closure forces the shift source to be the matter's energy current (proved below). So a sawtooth momentum can source the constraint only if the matter's own dispersion is exactly E² = m² + c²|k|² on the whole Brillouin zone. That is the SLAC form, with 1/r² hopping.
  - With that dispersion, the identities hold exactly and the algebra is first class at linear order (checked).
  - With any analytic matter dispersion (nearest-neighbour Klein–Gordon, tight-binding, or anything finite-range or exponentially local), it fails, even when non-local densities are allowed (proved).
  - **New necessary condition for a PASS candidate from G1/G2:** the network must make the matter dispersion exactly SLAC, kink at the zone face included. Making the interactions umklapp-free is not enough.
- **Readout Q: no finite n\* in the designs computed.**
  - The part of μ that depends on ε_U scales as ε_U² × natural, with no linear term. On that part alone, n\* ≈ 113/c.
  - But a zone-face contribution does not depend on ε_U. In the RN L2 design it is a floor of natural size. In the fuller design it becomes an O(ε_U·|h|) cusp. And in the E channel no unitary strain completion exists at all.
  - So n\* ≈ 113/c holds only if the face term is removed separately, by tuning or by a construction not found here.

## 1. Sourcing

### 1a. The shift source must be the energy current (PROVED, short)

At linear order (RN L1 algebra, 09-14 stencils), the time derivative of the scalar constraint is

d/dt(S/κ_s + T00) = −(J/κ_s) div G + Ṫ00 ≈ div(P_shift) + Ṫ00 on C_v = 0.

A matter-only expression vanishes weakly only if it vanishes identically. So the requirement is (E): Ṫ00 + div P_shift = 0, with the same P_shift that enters C_v. Momentum continuity (M), Ṗ = −G[T] with symmetric T, is the second condition.

**One-body symbol of the total.**
- From (E), ΣP = i[H, D] with D = Σ x T00.
- On one-particle states with exact dispersion E(k), and with T00's form factor continuous on the diagonal with t(k,k) = E(k), the symbol of ΣP is **E(k)∇E(k)**.
- This holds for any choice of T00, local or not. Only continuity of t on the diagonal is needed: a cusp |k−k′| in t contributes O(q²) and drops out.

**Consequences.**
- **Nearest-neighbour Klein–Gordon:** E∇E = sin k. A sawtooth P_shift (symbol k) leaves d/dt C_s ≈ div(J_E − P_saw) ≠ 0. That is a matter-only secondary constraint, so the system is not first class. Table: `g3_sourcing.out` (a).
- **Option (i) with analytic matter fails** for every T00 whose total is H (and for any other conserved charge q, because q∇E = k needs ∇E ∥ k).
- **An exactly conserved momentum** with nonzero normal scattering in d ≥ 2 has f = b·k on normal processes (Lemma L2-A logic). Then f = E∇E forces **E² = m² + c²|k|² exactly on the zone (SLAC)**. Its kernel has 2(−1)^r/r² tails along the axes.

### 1b. General exact stress for separable free matter (PROVED algebraically; CHECKED to ≤ 4e-14)

**Setting.** W(k) = m² + Σ_i w(k_i), with T00 = ½π² + ½φ·Kφ symmetrized, i.e. C(a,b) = ½(W(a) + W(b)).

**Kernels**, written with centred 09-14 placements (q̂ = 2 sin(q/2), q = a + b):

- P_j (π_a φ_b): i(w(a_j) − w(b_j)) / (2q̂_j), on edges;
- T_ij (φ_a φ_b): (w(a_i) − w(b_i))(w(a_j) − w(b_j)) / (4q̂_i q̂_j). This is symmetric, with T_jj on sites and T_ij on faces, exactly the 09-14 G slots.

(E) and (M) hold identically. The real-space check on random classical fields on 2D odd tori (L = 9, 11) gives relative residuals of 2e-15 to 4e-14, for both nearest-neighbour Klein–Gordon and SLAC (`g3_sourcing.out` (b)).

**Locality.**
- Nearest-neighbour Klein–Gordon: P_j → i sin((a_j − b_j)/2), finite range. The tails are at roundoff.
- SLAC: P_j(q→0) → i s(a), the sawtooth.

**SLAC tails** (1D, which is exact for the axis structure; T_xy is the product of two 1D factors). From `g3_sourcing.out` (c):
- The largest |P| coefficient at distance R falls as R^-2.01.
- The largest |T_jj| coefficient falls as about R^-1.73.
- **The coefficient sum beyond R falls by about 1.38 per doubling, i.e. the ℓ¹ norm of P(x) diverges logarithmically with volume.** The energy-current density is ℓ² (a valid quadratic form) but not ℓ¹-summable. This is where the sawtooth density's 1/r tail (checked: |D(r)|·r → 1) reappears.

### 1c. First class at linear order and the far field

**First class.** The RN L1 linear algebra uses only (E), (M), G Sᵀ = 0, S(q̇) = −J div G and G R2 = 0. Matter locality is never used. So **with SLAC matter the constraints are first class at linear order** (CHECKED through (E)/(M); the stencil identities were checked in RN L1 and confirmed by its referee).

**Far field (ARGUED, not computed).**
- T00 = ½π² + ½m²φ² + ½φKφ has alternating (−1)^r/r² tails along axis lines through the source support.
- The monopole is the total energy, so the 1/r law and universality of G survive: the active charge is energy, and the passive coupling is unchanged.
- Corrections are O(a²/R³), up to logarithms. For smooth low-energy packets the tails are exponentially small, because they come only from zone-face content. They are power-law for compact states.

### 1d. Option (ii): carrying the momentum through the network (ARGUED)

If the network's own fields carry the current, the full nearest-neighbour system has a strictly local, exact energy current. Option (ii) is therefore exactly the question "is the network's total energy current conserved?". The charge then has a summable first moment, so the RN L2 / RS exclusions apply wherever the asymptotic sectors fall in their classes.

**Extra necessary condition.** Every asymptotic species that scatters on shell with matter in normal kinematics (Compton-type) must satisfy E_s∇E_s = p on an open set. A mediator whose dressed dispersion is analytic from p = 0 up to the face cannot satisfy this. The mediator would itself have to be SLAC-like, which regresses to the same problem.

## 2. Consequence of approximate conservation

### 2a. The zone-face obstruction to the uniform-strain Ward identity

**E channel: PROVED, same-family.** The RN L1 seagull needs the unitary flow generated by D_jj = Σ x_j P_j.
- For the sawtooth, the flow dk/ds = s(k) reaches the face in finite time ln(π/k₀).
- The deficiency indices on each half-zone are (1, 0): ψ ∝ |k|^{1/2} is L², |k|^{−3/2} is not. So there is **no self-adjoint extension and no unitary group**.
- Every continuous odd periodic f has f(π) = 0, so its flow is complete. That is why RN L1/L2 worked with sin k.

**Free SLAC field, E channel (CHECKED).** The available completion keeps the fixed Brillouin cube and gives μ_E = +1.73, +1.71 and +1.67 per cell at m = 0, 0.5 and 1 (`g3_face.out`). That is the size of the vacuum energy density itself (about 1.5 per cell), the T0 "cutoff fixed by grid labels" effect. Removing it needs a tuned counterterm or a zone-face boundary operator.

**Corroboration (reading).** RN L2's own discarded Fejér rows show G″ growing to 1.01 at R = 16 as f approaches the sawtooth, in the E channel (`scripts/laneRN/L2/l2_sunset_mu_m1.out`).

**T2 channel (CHECKED).** The sawtooth shear flow (s(k_y), s(k_x)) is measure-preserving: the image of a uniform sample is uniform, with relative std 0.0122 against Poisson's 0.0126. So the unitary exists, but the flow carries legs across the faces, so it changes which interaction terms count as normal (momentum-conserving) and which as umklapp.

### 2b. μ versus ε_U at O(λ²), reusing RN L2's basketball

**Setup.** Filtered onsite φ⁴: the vertex is 1 on normal 4-tuples and ε_U on umklapp 4-tuples. The classes are split by zero-padded linear convolution.
- **Control:** the class totals reproduce RN L2's I4 = 1.656164e-4 and its μ_E = −1.0093e-6 and μ_T2 = +1.6108e-8 (f = sin k).

**Design A (RN L2's: flow the free part only). PROVED exact at this order:** μ(ε_U) = μ_N + ε_U² μ_U, with no linear term, because each 4-tuple lies in exactly one class.

Values in units of λ² per cell, m = 1 (`g3_epsU_mu.out`, `g3_epsU_slac.out`):

| Flow, dispersion, channel | μ_N | μ_U |
|---|---|---|
| sin, KG, T2 | +3.20e-7 | −3.04e-7 (total 1.61e-8) |
| sin, KG, E | −9.30e-7 | −7.9e-8 |
| sawtooth, KG, T2 | +2.81e-6 | +3.41e-6 |
| sawtooth, SLAC, T2 | +2.4e-6 to 2.5e-6 | +4.3e-6 to 4.7e-6 |

- The ε² scaling is analytic, with no |ε| cusp (`g3_epsU_epsdep.out`).
- **With f = sin k, filtering out umklapp raises μ_T2 twentyfold**, from 1.6e-8 to 3.2e-7, because normal and umklapp nearly cancel.
- **With the sawtooth, μ_N is an ε_U-independent floor of about 1.5–1.7 × the "natural three-loop" 1.67e-6.** It comes from face crossing.

**Design B (flow the free part and the normal interaction; possible only because P_saw is exactly conserved by the normal part). CHECKED by Monte Carlo** (`g3_cross_mc.out`; the control I_N = 6.17e-5 matches the convolution).
- The floor cancels.
- But the flowed-normal and lab-umklapp vertices overlap on the face-crossing set, giving E^(2) ⊃ −(λ²/12)·ε_U·I_X with I_X = 5.8e-5·|h|.
- This is **linear in ε_U and a cusp in the strain** (I_X/|ε| is constant to 3% for ε = 0.01–0.08). For ε_U > 0 the unstrained vacuum is a local maximum.

**All orders (ARGUED).** At h = 0 with ε_U = 0, H conserves P_saw, and umklapp vertices carry charge. So E₀ is even in ε_U whenever the strained theory also conserves a charge that the umklapp term breaks (design A). The face is what spoils this in design B.

**Design-dependence (RN L2 referee).** The vacuum 0 → 4 sector is off shell, so an analytic O(λ) dressing may still cancel these vacuum pieces. Nothing here is "forced". The face terms are unprotected by any Ward identity, and are of natural size in every design computed.

## 3. Readout Q

**Formula.** n\*(ε_target) = ln(1/ε_target)/c, for ε_U = e^{−cn}.

**If μ ∝ ε_U² × natural** (design A, after the floor is removed):
- ε_U ≤ √B, so n\* = ½ln(1/B)/c.
- B = 5.7e-99 (refereed, reduced-Planck cell): ε_U ≤ 7.6e-50, n\* = 113.1/c.
- B = 9.0e-102 (framework convention): ε_U ≤ 3.0e-51, n\* = 116.3/c.
- B ≈ 1e-99: ε_U ≤ 3.2e-50, n\* = 114/c.

**Using the computed μ_U ≈ 3.4e-6λ²** against the absolute bound 1.08e-104 M_Pl⁴: ε_U ≤ 5.6e-50/λ, so n\* = (113.4 + ln λ)/c.

**If μ ∝ ε_U** (design B's cusp is worse than this, since it is not a μ): n\* ≈ 226/c to 233/c.

**The face floor alone** (design A, 2.8e-6λ²) is about 4e95 to 3e98 times the bound, independent of n. So no finite n\* exists unless it is removed separately.

**Against the expectation:**
- **Sourcing.** Expected: only non-local sourcing works. Confirmed, and sharpened: it needs SLAC matter, and nearest-neighbour matter fails even non-locally.
- **Size of μ.** Expected: about ε_U² × natural. Confirmed only for the ε_U-dependent part in design A. Not foreseen: the zone-face floor or cusp, and the missing E-channel unitary.
- **n\*.** Expected: 10² to 10³. Recovered (113/c) only conditionally.

## Labels and strong words

- **Proved (same-family, unrefereed):**
  - (E) forces the shift source to be the energy current, with symbol E∇E;
  - the sawtooth therefore needs SLAC matter;
  - the separable stress formulas;
  - the E-channel deficiency;
  - the O(λ²) class split with no linear term in design A.
- **Checked:** the identity residuals; the tail exponents; the ℓ¹ log-divergence; the μ_N and μ_U table; the ε² scaling; the T2 measure preservation; the |h|·ε_U cross term; the free SLAC μ_E.
- **Argued:**
  - the far-field corrections;
  - option (ii)'s Compton condition;
  - all-orders evenness in ε_U.
- **Suggested:** that no other determined local completion removes the face terms.
- **"Exact"** means identities with the stated residuals.
- **"No unitary"** applies to the E-channel sawtooth dilation in infinite volume.
- **"Floor" and "cusp"** describe designs A and B. They are not forced, because of the dressing caveat.
