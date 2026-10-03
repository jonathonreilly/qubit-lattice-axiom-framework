# A14 report: can records that get in the way supply the spatial half of light bending?

All runs used `nice -n 10`, the four thread caps set to 1 and a 58 s alarm. Each finished in 21 s or less and peaked at 235 MB or less. Scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A14/`. Everything below is a supplied toy, and none of it is adopted.

## 1. Question

The campaign's gravity analog is a pure clock-rate (lapse) field N = 1 + Φ, with Φ ≤ 0 near a capturing clump (A6, A8). Write U = −Φ. That field bends and delays light-like ripples by half the GR amount (γ_eff = 0), and it has β_eff = 1/2.

Can the owner's ingredients give light-like ripples of the shared possibilities the full weak-field GR index n = 1 − 2Φ, which is γ = 1? The ingredients are:
- records as walls for the flow (A8 B1);
- moving records and wanderers;
- event-paced change (A8);
- ticks (A5, A10);
- condition-set menus.

Can any of them also fix β?

## 2. Answer

**Conditional. Static records in the way do not supply the missing half. A different kind of wall does at first order, but β is not fixed.**

**Static records as walls (ARGUED, from EXACT and CHECKED pieces).** They fail on four counts.
- **Wrong sign.** Around a capturing clump, the wanderers are the population with a 1/r profile, and they are depleted there. Fewer walls make ripples faster near the clump, which opposes the lapse.
- **Too small.** The effect is O(u∞), where u∞ is the far wanderer density per site. The lapse term is O(1) in U.
- **Wrong kind.** Locked records pull their neighbours toward agreement and pin the long-wavelength ripple. The medium then gives a mass, a colour-dependent shift, and loss by scattering of about the same size as the shift.
- **Not universal.** The effect depends on record content and on the ripple's mass.

**Idle sites as walls (EXACT eikonal; CHECKED: bending ratio 1.984 against 2).** Suppose a site whose neighbourhood had no event this tick holds its possibilities still. Then by B1's own algebra it neither relays nor moves. Every two-site step needs its own event at each end within one global tick.
- Transport then runs at N² while one-site clocks run at N.
- The index is n = 1/N² = 1 − 2Φ + 3Φ² with no tuning, because the same activity sets both factors.

This is a named conditional, not a consequence. I call it the AND reading; A8's default, where one event at either end steps the bond, is the OR reading. It needs:
- a global coincidence tick;
- species whose rest energy comes from one-site terms and whose motion comes from two-site terms.

It leaves β = 1/2, which with γ = 1 gives 7/6 of Mercury's perihelion advance. No ingredient here fixes β.

## 3. Derivation

**Conventions.**
- N(x) is the local event rate relative to far away. U = −Φ ≥ 0 is the Newtonian-potential analog.
- GR in isotropic form (comparator): n = 1 + (1+γ)U, so GR's γ = 1 gives n = 1 − 2Φ.
- ρ is the wall density per site. u is the wanderer density, u∞ its far value.

### 3.1 Task 1: event pacing alone gives n = 1/N

**(a) Paced generator (A8 3.9).** Suppose each event delivers a small dose of the change. The evolution then averages to H_eff = Σ_b r_b h_b + Σ_x r_x h_x, where:
- r_x = N_x for one-site terms;
- r_b = (N_x + N_y)/2 for a bond that one event at either end can step (OR).

**(b) Eikonal (EXACT).** For N slowly varying on the wavelength, ω(x,k) = N(x)·ω_loc(k). With ω_loc = c|k|:
- ẋ = Nc k̂ and k̇ = −c|k|∇N;
- rays follow Fermat's principle with n = 1/N.

**(c) Half of GR (EXACT).**
- n = 1 − Φ + Φ² − …
- Bending is ∫|∇⊥n| dl = 2GM/(bc²).
- The delay is ∫U dl.
- Both are half of GR. The matching metric is −N²dt² + δ_ij dx², so γ = 0 at every order.
- A5's seam refraction (k from 0.30 to 0.15 at rate ratio 2) is the discrete version of this.

**(d) Two conditions for (b).**
- **(d1) The cone must sit at zero vacuum-relative quasi-energy (EXACT algebra).** The lapse multiplies the ripple's quasi-energy measured from the paced vacuum. If the cone sits at an offset E_c, then n − 1 = (1 + E_c/(c|k|))U. That is colour-dependent, and it repels when E_c < −c|k|.
  - The conveyor walks (A5 T2 and my 2D toy) have E_c = 0 by construction.
  - A10's Dirac cone sits at −6θ per cycle relative to the all-0 reference, with slope 2 sin θ sites per cycle. So E_c/c → −3 per site, and with that reference, long-wavelength A10 ripples would be pushed away from a clump.
  - With a half-filled sea as the reference the offset vanishes if the sea stays locally half-filled. I did not check that.
- **(d2) Random event timing is noise (CHECKED trend, N4).** The averaged generator is reached only as the dose per event θ → 0 at fixed distance. This applies to A8's lapse as much as to the AND reading.

### 3.2 Task 2: records as walls

**(a) 1D (EXACT).** A wall blocks completely. In N4, the static-wall speed is between −0.01 and +0.003 of free motion.

**(b) Records pin (EXACT).** By A8 B1, a record with content a acts on its neighbour through ⟨a|h|a⟩.
- **Lemma.** ⟨a|h|a⟩ is the same operator for every content a if and only if h has no interaction part.
- **Proof.** Write h = Σ c_μν σ_μ⊗σ_ν. Then ⟨a|h|a⟩ = Σ_ν(c_0ν + Σ_i c_iν n_a^i)σ_ν. Independence of the Bloch direction n_a forces c_iν = 0 for i, ν ≥ 1.
- So any change that moves possibilities between sites gives some record contents a content-dependent pull on their neighbours.
- For A10's SWAP family, ⟨a|SWAP|a⟩ = |a⟩⟨a|. Every record pulls its neighbours toward agreement with itself; this is a dynamical form of Q1. The pull breaks the global re-orientation symmetry that keeps the long-wavelength ripple gapless.

**(c) Effective medium (independent walls, first order in ρ; Foldy–Lax comparator).** ω_eff(k) = ω₀ + ρ·Re t(k), where t is one wall's forward scattering amplitude. Then:
- the phase index is n_ph = 1 − ρ Re t/ω₀;
- the group velocity is v_g = ∂_k ω_eff;
- the extinction rate is Γ = −2ρ Im t.

| Wall type | Long-wavelength form | Effect |
|---|---|---|
| Neutral (does not pin) | Re t = −τω₀ | Achromatic n = 1 + τρ (tortuosity). EMA gives c² ≈ 1 − 2ρ in 3D; measured 1 − 1.52ρ (CHECKED), so τ ≈ 0.76 for a wave |
| Pinning | Re t → constant or ∝ 1/k | Plasma-like: n_ph − 1 ∝ −ρ/ω or −ρ/ω² |

**(d) 3D scalar toy (CHECKED).** This is the SWAP ripple over the all-0 state.
- Content-0 records are Dirichlet sites. The uniform ripple shifts by −Cap₁·ρ, with Cap₁ = 1/G(0) = 3.957.
- That is the crushed-ice term (Cioranescu–Murat, comparator), and it is the same single-site capacity that sets one record's capture charge in A6.
- Content-1 records bind ripple states above the band.

**(e) 2D Dirac toy (CHECKED).** This is a conveyor-product walk with a cone at ω = 0 and speed 1. Walls reflect with phase r.
- **r = ±i** (a record's value in the full-swap brickwork):
  - Re t ≈ −3.05·k·ln(1.12/k): slower, with a log-running speed;
  - Γ ≈ 9kρ;
  - at finite density a mass M ≈ (2.4–3.2)ρ appears.
- **r = ±1:** Re t ≈ +1/k, a first-order gap.
- In both cases the loss is about as large as the shift: Γ/|δω| ≈ 1.2–2.6.

**(f) Which population near a clump.**
- The clump's records have compact support. A ray passing outside sees nothing in ray optics, so they give no 1/r tail.
- The wanderers have u = u∞N = u∞(1 − U) (EXACT, dilute mean field), which is depleted with exactly the lapse profile. They set the long-range obstacle index.

The sign of their effect, ARGUED from the CHECKED medium:
- **Velocity part:** δn = −τu∞U. Ripples are faster near the clump, opposite to the lapse.
- **Mass part:** m² ∝ u is smaller near the clump. Rays bend toward it, but signals arrive early, and both effects go as m∞²/ω². This is a plasma lens with a hole.

### 3.3 Task 3: combined index, and idle sites as walls

**(a) Static walls (EXACT algebra).** n_total = (1/N)·n_obs(u∞N), so n − 1 = (1 − τu∞)U plus colour-dependent mass terms. That is γ_eff = −τu∞.

**(b) No regime among static records (ARGUED).** Equality with the lapse needs a 1/r *excess* of walls with a per-wall effect of order 1/u∞.

**(c) Excess populations exist but carry other problems (EXACT, mean field).**
- **Spectator species.** A species the clump does not capture is crowded in by exclusion. The zero-flux condition gives u₁ ∝ 1 − ρ, so δu₁/u₁∞ = u₀∞U/(1 − u₀∞). That is the right sign but only O(u₀∞).
- **Exported "spent" records.** Records released one-for-one per capture, with equal hop rate and equal far density, have an excess exactly equal to the wanderers' depletion. As static walls they still pin, and they need a spent/fresh mark that content cannot carry, because records are permanent.

**(d) The route that works at first order: idle sites as walls.** Suppose an idle site holds its possibilities for the tick in the strong sense: the bond acts as V_x ⊗ 1_y. Then it neither relays nor moves. Holding is the only change from A8's OR reading.
- On Z³, adjacent sites share no neighbour. A wanderer arriving at x or y occupies it and blocks the bond.
- So the two ends are unlocked by arrivals in disjoint 5-site sets: P_bond ≈ 25·a_x·a_y ∝ N_xN_y, where a is the arrival rate per site. One-site processes run at ∝ N_x. (EXACT, dilute limit.)
- With the eikonal above, n = 1/N², giving bending 4GM/(bc²) and delay 2∫U dl. The metric is −N²dt² + N⁻²dx², so γ = 1. (EXACT; CHECKED in N5.)
- Idle sites blink, so in the small-dose limit the ripple sees their average: no scattering, mass or loss. N4 confirms speed ∝ mean bond activity, and that static walls block.

Conditions (EXACT within the model; each is a named conditional):
- **(i) A global constant tick (I1).** If ticks are local and paced by N, the coincidence window stretches, r_b ∝ N, and γ = 0.
- **(ii) No one-ended steps.** A fraction ε of them gives γ = 1 − ε.
- **(iii) Dilute activity.** γ ≈ 1 − 2.5·a∞.
- **(iv) No triangles in the lattice.** A lattice with triangles would leak OR steps.

**Lean (ARGUED).** Menus are per-site and set by the site's own nearest-neighbour conditions (Q7). If permission to change on a tick is set the same way, AND follows. OR needs a trigger two sites away to change an end.

### 3.4 Task 4: β

**(a) Obstacles cannot shift β (EXACT, mean field).** Obstacles act on transport. β is the U² coefficient of g00 = −N². A8 3.8 shows the event-rate clock is lattice-harmonic for any site-departure hop law, and obstacles enter only through the hop rate. So β = 1/2.

**(b) The pacers cannot be AND-gated themselves (EXACT, mean field).** The condition a = zκa²u has only an unstable nonzero fixed point. So the pacers must hop freely, N stays harmonic, and β = 1/2.

**(c) Consequence.** With γ = 1 and β = 1/2, the perihelion factor is (2 + 2γ − β)/3 = 7/6.

**(d) Target structure (comparator, exact GR fact).** In isotropic Schwarzschild coordinates:
- ψ = 1 + M/2r and χ = Nψ = 1 − M/2r are both harmonic;
- χ + ψ = 2;
- N = χ/ψ = e^(−U)·(1 + O(U³)).

Fresh and spent populations with one-for-one exchange at the clump, equal hop rates and equal far densities give χ + ψ = 2 exactly (EXACT, linear mean field). A clock running at fresh/spent would then give β = 1, and AND transport matches GR's light speed at first order. No ingredient supplies the ratio clock or the spent mark (ARGUED). Other veto forms give β between 1/2 and 1.

### 3.5 Task 5: universality

**(a) Pacing alone is universal (A8).**

**(b) Static walls are not (CHECKED in the toy; ARGUED in general).**
- **Content dependence.** r = ±i and r = ±1 give opposite-sign first-order shifts.
- **Massive versus massless.** For a massive ripple (m = 0.3) the wall shift is 2.2–3.1 times smaller than a common rescaling of the massless shift predicts.
- **Binding.** One wall binds massive ripples.
- **Free-fall violation.** A wall-induced rest-energy shift δE ∝ u(x) gives slow bodies a composition-dependent force at Newtonian order.

**(c) The AND reading is universal for a species if and only if its rest energy is one-site and its propagation two-site (EXACT, averaged generator).** Local physics is then conformally rescaled, and massive and massless Dirac ripples share the same metric. Otherwise:
- second-order waves (one-site inertia × two-site stiffness) give ω² = N²m² + N³k², so γ = 1/2;
- two-site masses (A10's θ_e ≠ θ_o; A5's single-track mass) put the whole species on a pure lapse N².

Kogut–Susskind on-site masses are one-site (comparator). Length standards must be dynamical: a rigid record pattern at fixed sites would show the effect (ARGUED).

### 3.6 Task 6: conclusion

Static records in the way do not give the spatial part. What it needs is a second factor of the same activity that slows every displacement but no clock. In the toy, that is AND gating of two-site steps on a global tick: idle sites as walls. β needs a further, separate ingredient: an exponential or ratio clock.

## 4. Checks

| ID | Script | Result |
|---|---|---|
| N1 | 1D blocking, static control in `g1d_gating.py` | v/(2θP) between −0.010 and +0.003: blocked |
| N2b | `w2d_single.py` (L=256, T=128; slope drift ≤ 0.002 for r=±i) | r=±i: δω/ρ = −0.73, −0.92, −1.05, −1.09, −0.95, −0.48, −0.15 at k = 0.098–0.785. Diagonals agree (isotropic). Γ/ρ = 0.86 to 4.19. r=±1: δω/ρ ≈ +9.3 down to +1.5 (k·δω/ρ ≈ 0.84–1.17); drift up to 40% for k ≤ 0.2 |
| N2d | `w2d_fit.py`, 8 seeds, r=i | v_g at k≈0.23: 0.985±0.003, 0.954±0.009, 0.890±0.018, 0.719±0.027 at ρ = 0.005/0.01/0.02/0.04. At k≈0.29: 0.998, 1.008, 0.957, 0.884. Fit at ρ = 0.02/0.04: v = 0.937/0.886, M²/ρ² = 6.0/6.8. Extrapolating ρ → 0 agrees with N2b to about 10% |
| N2c | `w2d_bound.py`, exact diagonalization, L=24, m=0.3 | In-gap states at ±0.264 (r=i) and ±0.208 (r=1); gap edge 0.300; 235 MB |
| N2m | `w2d_single.py`, m=0.3 | At k = 0.39/0.59/0.79: −0.35/−0.14/−0.05, against the common-rescaling prediction −0.76/−0.44/−0.14 |
| N3 | `s3d_pin.py`, L=24, 3 seeds | Dirichlet top/ρ = −3.66±0.23, −4.09±0.17, −4.05±0.05, −3.97±0.03 against −3.957. Neutral walls: top = 0 and c² = 1 − 1.52ρ. Content-1 walls: bound states above the band |
| N4 | `g1d_gating.py`, θT = 40 fixed | As θ goes 0.1 → 0.0125, v/(2θP) goes 0.35 → 0.82 and fidelity 0.15 → 0.78 (OR, p=0.3); 0.67 → 0.94 and 0.56 → 0.91 (AND, p=0.3) |
| N5 | `d2d_bend.py`, deterministic averaged generator | Drift ratio AND/OR = 1.9836. Against the eikonal prediction: 0.971 / 0.963 at packet width σ=11 (0.935 at σ=7); no pacing gives 0 |

**Should be run (not run).**
- `w3d_single_NOT_RUN.py` at L=128: 3D walls; needs about 1–2 GB. Syntax-checked at L=16.
- A 2D stochastic AND/OR bending test with small doses, combining N4 and N5.

## 5. Real-physics match (comparators, not adopted; values from memory, not re-verified)

**Pacing alone.** γ = 0 gives 0.875″ at the solar limb against 1.75″ observed. It is excluded by VLBI (~10⁻⁴) and Cassini (|γ−1| ≲ 2×10⁻⁵).

**Static walls.**
- They give a colour-dependent, converging, time-advancing lens, plus loss. That is excluded by the agreement of radio and optical deflection and by sharp lensed images.
- If wanderers pin light-like ripples, the photon-mass bound (< 10⁻¹⁸ eV) needs u∞ ≲ 10⁻⁹² (if m² ∝ ρ) or ≲ 3×10⁻⁴⁷ (if m ∝ ρ) per Planck-scale site. This is a new cross-constraint on A6/A8's clock carriers.

**AND reading.**
- It passes Cassini if the one-ended fraction and a∞ are both ≲ 10⁻⁵.
- It fails Mercury: 50.1″ per century against 42.98″.
- It fails lunar ranging if inertia is standard: η = −2.
- Species with γ = 1/2 would be constrained by neutrino–photon and gravitational-wave–photon delay equality.

**AND plus an exponential clock.** This gives the Yilmaz exponential metric: equal to GR at first post-Newtonian order, different beyond, with no horizon.

## 6. Open edges and next steps

1. **Owner decision.** Does an idle site hold (AND) or can it be pulled along (OR)? Is the coincidence window a global tick or a local one?
2. **Mass anatomy.** Are rest energies one-site? A10's masses are two-site.
3. **β.** Is there a ratio clock or a fresh/spent exchange, or a self-sourcing activity?
4. **Coherence under random pacing.** Handshake-ordered schedules avoid the noise, but may turn AND back into OR.
5. **Walls in 3D.** Run the 3D wall script on a bigger machine.
6. **Reference state for the lapse coupling.** All-0 or a half-filled sea; this decides A10's cone offset.

## 7. Plain-language summary

Records sitting in the way of the shared possibilities do not double the bending of light. Near a clump the wandering records thin out, so there are fewer obstacles there, which pushes the wrong way. And because records hold the possibilities next to them still, obstacles treat different colours differently and scatter light, which real bending does not do.

What does double it, in a toy, is a stricter rule: a place where nothing happened on a beat holds its possibilities still. Then possibilities can pass between two neighbours only when both had something happen on the same beat, so near a clump passing is slowed twice over.

The rules leave this as a choice, not a consequence. Even with it, planet orbits would come out wrong unless something else changes how clock slowing builds up close to a clump.