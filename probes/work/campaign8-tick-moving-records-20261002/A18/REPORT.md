All checks are complete and consistent. The plain (even, odd) word's dispersion formula is confirmed to 10⁻¹⁶, with the band minimum shifted to K = π − μ; the time-symmetric word puts it at K = π with ω = μ exactly.

# A18 report: does the "angle-lapse package" P1–P4 reproduce first-order GR?

All runs used `run.sh`: `nice -n 10`, the four thread caps set to 1, and a 58 s alarm inside each script. Every run finished in 23 s or less with peak memory of 173 MB or less. Scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A18/`. Everything here is a supplied toy, and nothing is adopted. I did no git work, made no repo edits and spawned no subagents.

## 1. Question

The candidate package is a named conditional, not adopted:
- **P1.** One shared beat, rate-locked, with no waiting loops.
- **P2.** The change per beat is set deterministically by records. One-site phases advance by N_x per beat. Two-site steps have angle θ_xy = θ0·N_x·N_y.
- **P3.** Rest energies are one-site; motion is two-site.
- **P4.** N = F(u/u∞), with u the wanderer density, which is harmonic outside clumps (A6). The candidate is F = exp(s − 1), so N = e^{−U}.

Sharp question. Does the package reproduce:
- GR's first post-Newtonian (1PN) light bending, Shapiro delay and perihelion advance (γ = β = 1)?
- universal redshift?
- no reflection at gradients?
- no pacing noise?

And what is supplied rather than derived?

## 2. Answer

**Conditional.**

**What works, at the level of rays (eikonal).**
- P1–P4 give exactly the static metric ds² = −e^{−2U}dt² + e^{2U}dx² (EXACT). That is the exponential (Yilmaz-type) metric, with γ = β = 1.
- So the package gives GR's 1PN light bending, Shapiro delay and perihelion advance. CHECKED by quadrature: perihelion factor 1.000000, light bending 4M/b.
- Free fall and redshift are universal for every species whose rest energy is one-site (EXACT). CHECKED on a 1D lattice:
  - rest frequency is exactly μN;
  - the fall matches the light-calibrated metric to 0.4%;
  - a two-site mass falls about twice as fast.
- Smooth lapse gradients do not reflect (CHECKED: ≤ 5×10⁻⁹).

**What it needs beyond P1–P4.** These are all supplied:
- a small change per beat, θ0 ≲ 6×10⁻³; otherwise γ = 2θ0·cot θ0 − 1 (EXACT);
- the light cone sitting at the vacuum's quasi-energy (EXACT algebra);
- A10's time-symmetric word, so that the one-site mass is a pure mass (EXACT, CHECKED);
- formation odds per beat carrying one factor of N (ARGUED);
- wanderers that are themselves unpaced; if they are paced by the lapse, β = 1/4 or β = 0 (EXACT, mean field);
- a smooth lapse.

**Pacing noise: no for any nearest-neighbour version.**
- A lapse set by the records of an m-site neighbourhood averages to a polynomial of degree ≤ m in u. It cannot be exponential (EXACT, product measure).
- An exponential response to the record count gives β = 1 − 1/(2m) (EXACT). That is 11/12 for the six neighbours, and Mercury then fails.
- The snapshot noise dephases heavy superpositions unless the lapse averages over a radius R ≳ 10⁹/u∞ sites. The pieces are EXACT or CHECKED; the numbers are ARGUED.

**Beyond the static tests, the package departs from GR or fails.**
- Second-order light bending is 4π(M/b)² instead of GR's 15π/4 (CHECKED).
- There is no horizon; N ≥ 1/e for A6 absorbers (EXACT).
- There are no gravitational waves and no frame dragging (g₀ᵢ ≡ 0, EXACT).
- A moving source carries its field only in a narrow wake behind it (ARGUED, from an EXACT mean-field solution).

**γ = 1 and β = 1 are supplied, not derived.** Each comes from one choice:
- the two-site pace exponent b = 2a, since γ = b/a − 1;
- the lapse curvature FF''/F'² = 1, since β = (1 + FF''/F'²)/2.

## 3. Derivation

### 3.1 Task 1: eikonal and metric

**D1. Effective generator (EXACT, small-dose limit).** Under P2, the change per beat is H = Σ_x N_x μ ε_x n_x + Σ_⟨xy⟩ θ0 N_x N_y h_xy. For slowly varying N, its local symbol is ω(x,q) = N·√(μ² + N⁴c²q²/N²), that is:
- **ω² = N²μ² + N⁴c²q².**
- It uses A10's signed time-symmetric cone, H₁ = c·Σq_aA_a with anticommuting A_a, plus a one-site mass ε that anticommutes with every A_a (A10 S11).

**D2. Metric (EXACT).** For ds² = −A²dt² + B²dx², the mass shell gives E² = A²(m² + p²/B²). Matching D1 gives A = N and B = 1/N. So:
- **ds² = −N²dt² + N⁻²dx²**, for massless and massive (P3) ripples alike.
- Massless rays follow Fermat's principle with n = N⁻² (as in A14).
- Massive packets follow geodesics of the same metric.
- The internal clock of a packet at rest runs at ω = μN.
- The product rule enforces **n·N² = 1 exactly**. GR's isotropic Schwarzschild metric has n·N² = 1 − U²/4.

**D3. Universality (EXACT eikonal; CHECKED in 1D).** One-site masses redshift by exactly N, and slow packets fall at ẍ = −c²N³∇N (geodesic). A two-site mass is different (A10's θ_e ≠ θ_o):
- it gives ω = N²√(m² + c²q²);
- it redshifts by N²;
- it falls at ẍ = −2c²N³∇N, an order-one violation of the equivalence principle.

**D4. Finite dose per beat (EXACT).** The cone speed is sin θ, not θ (A10 S4/S9). So:
- n = sin θ0 / sin(θ0N²), which gives **γ_eff = 2θ0·cot θ0 − 1**;
- γ_eff = 0.571 at θ0 = π/4 and −1 at θ0 = π/2 (the full-swap conveyor gives no bending);
- Cassini needs θ0 ≲ 5.9×10⁻³.
- So in this package light travels at only ≲ 1% of the lattice's one-site-per-beat cone.

**D5. Cone offset (EXACT algebra, A14 (d1) adapted).** The swap gate puts the one-excitation cone at E_c ≠ 0 relative to the vacuum. Under P2 this offset scales as N². The rays then obey q̇ = −2N∇N(E_c + c|q|), so:
- the deflection is 4M/b × (1 + E_c/(c|q|)), which is colour-dependent;
- the package needs E_c = 0. For example, the generator SWAP + n_x + n_y centres the cone on the vacuum (checked by hand), at the price of a basis-privileging field term.

**D6. P3 needs A10's time-symmetric word (EXACT; CHECKED to 10⁻¹⁶).** With the plain 1D word (even, odd), the staggered one-site phase gives cos ω = cos μ·cos²θ − sin²θ·cos(K + μ). That is partly a momentum shift: the band minimum sits at K = π − μ, with ω_min < μ. With the block (even θ/2, odd θ, even θ/2), the minimum is at K = π with ω = μ exactly.

**D7. Beyond free Dirac species (ARGUED; dimensional analysis).** Universality needs every term of local physics to be conformally rescaled. A term whose coefficient scales as (lattice spacing)^{−p} needs the weight N^{1+p}. P2's site-count rule gives N^{#sites}. The two coincide only for one-site masses (p=0) and two-site hops (p=1). They differ for:
- **four-site gauge plaquettes**: they need N², site count gives N⁴. Photons would then get n = N⁻³ (γ = 2), and the local light speed would differ from matter's limiting speed by a factor N.
- **one-site contact couplings**: they need N⁴.
- **second-order (bosonic) fields**: A14 found γ = 1/2.

So "all clocks alike" needs a weight rule tied to each term's dimension, which the axioms do not supply.

**D8. Comparator, not adopted (Obukhov 2001, from memory).** GR's Hermitian Dirac Hamiltonian in −V²dt² + W²dx² is βmV + ½{V/W, α·p}. With V = N and W = 1/N this is βmN + ½{N², α·p}. P2–P3 discretize exactly this, to O(a²(∇N)²). So static-field spin effects, such as geodetic precession, would carry over.

### 3.2 Task 2: β

**D9. PPN reading (EXACT; PPN definitions used as comparator).**
- g00 = −e^{−2U} = −(1 − 2U + 2U² − …), so β = 1.
- g_ij = e^{2U}δ_ij = (1 + 2U + 2U²)δ_ij, so γ = 1.
- Perihelion factor: (2 + 2γ − β)/3 = 1.
- With any β = 1 lapse, the product rule forces the second-order spatial coefficient to 2U² (GR: (3/2)U²).

**D10. General β (EXACT).** Write the lapse as N = F(u) with u = u∞(1 − h) and h harmonic. Then **β = (1 + F·F''/F'²)/2**, evaluated at u∞.
- Linear F (A6/A8) gives β = 1/2.
- F = u^p gives β = (2p − 1)/(2p).
- β = 1 at every background density holds if and only if (ln F)'' = 0, i.e. **F = A·e^{λu}**.
- Then G_eff ∝ λu∞. Either G drifts as the far gas depletes (A6 open edge 2), or the law must contain u∞, as P4's F(u/u∞) does.

**D11. What the exponential means (EXACT).** On the package's spatial metric N⁻²δ, the Laplacian of the lapse is D²N = N³·Δ(ln N). So "the lapse obeys GR's static vacuum lapse equation D²N = 0 on the package's own spatial geometry" holds exactly when **N = e^{−U} with U flat-harmonic**.
- A6's wanderers diffuse on the bare flat lattice, which is why u is flat-harmonic and a supplied exponential is needed.
- To make u harmonic on the package geometry instead, wanderer hop rates would have to scale as 1/N (A8's a = −1). That is impossible near absorbers, where u → 0, because a record moves at most one site per beat (I2).

**D12. Finite neighbourhoods cannot give the exponential (EXACT, product measure).** If the per-beat factor f(k) depends on k = the number of wanderers among m sites, the averaged pace is a Bernstein polynomial of degree ≤ m in u.
- An exponential response f = r^k gives F = (1 + u(r−1))^m, so **β = 1 − 1/(2m)** for every r: 11/12 for m = 6 and 13/14 for m = 7.
- A degree-2 rule can be tuned to β = 1 at one background density only: β = 1.06 or 0.96 if the actual density is 10% off.
- Taking P4 literally on 6 neighbours at u∞ = 0.04 gives a mean pace of 724 instead of 1, with relative variance 5.7×10⁶.
- On Z³ the product averages factorize, because adjacent sites share no other neighbour (as A14 noted).

**D13. Shot noise and dephasing (EXACT formula; CHECKED inputs; ARGUED numbers; overlaps A17).**
- A rest phase μ·f(k(t)) accumulates variance T·μ²·Var(f)·2τ_int.
- Measured τ_int ≈ 3.4 ticks for the 6-site star and ≈ 25 ticks for the 124-site cube, at every density tested.
- So the dephasing factor scales as D_f ≈ 2τ/(mu) ≈ 1.2/(R·u) for radius R: enlarging the neighbourhood helps only like 1/R.
- With Planck beats, a Rb-87 superposition kept coherent for 1 s needs D_f ≤ 1.2×10⁻⁹, so R·u∞ ≳ 10⁹.
  - With u∞ ≲ 10⁻⁵, which Cassini needs because wanderers act as walls (A14), R ≳ 10¹⁴ sites.
  - With A14's photon-mass bound u∞ ≲ 10⁻⁴⁷ (if wanderers pin light-like ripples), R ≳ 10⁵⁶ sites, about 50 kpc. The lapse could then not resolve a solar 1/r field at all.

**D14. Wanderers must be unpaced (EXACT, mean field).** If the wanderers' own hops follow the lapse, β changes:

| How wanderer hops are paced | Steady-state field | β |
|---|---|---|
| By the departure site (rate ∝ N_x) | N·u harmonic | 1/4 |
| By the product rule (bond rate ∝ N_xN_y) | N² harmonic | 0 |
| By the mean rule (bond rate ∝ (N_x+N_y)/2) | N harmonic | 1/2 |
| Not paced | u harmonic, N = e^{−U} | 1 |

So the carrier of gravity must run on absolute time, which is exempt from the universality it supplies.

**D15. Lapse floor (EXACT).** In A6/A8, U = h_D ∈ [0,1], so **N ≥ e⁻¹**.
- The largest surface redshift factor is e (z ≤ 1.718).
- A jam's time does not stop through the lapse. It stops only because nothing is left to change.

### 3.3 Task 3: gradients

**D16.**
- In the continuum, a 1D massless Dirac field with any speed profile c(x) has σ_x conserved, so it reflects exactly zero (EXACT).
- On the lattice with the product angle (CHECKED):

| Lapse change | Massless reflection | Massive reflection |
|---|---|---|
| Smooth (Gaussian, 60 cells) | 1.5×10⁻¹⁶ | 4.9×10⁻⁹ |
| 20-cell ramp | 1.8×10⁻⁶ | 1.8×10⁻⁵ |
| One-cell step | 4.6×10⁻⁵ | 1.7×10⁻³ |

- Lattice delays match the exact-dispersion ray prediction to 10⁻⁴.
- Real gradients are smooth on the lattice scale, so their reflection is negligible (ARGUED).

### 3.4 Task 4: is the product angle natural?

**D17 (EXACT).** Give one-site paces N^a and two-site paces N^b. Then g00 = −N^{2a}, g_ij = N^{−2(b−a)}, and **γ = b/a − 1**.
- Product: γ = 1.
- Mean (OR), min and geometric mean (b = a): γ = 0.
- Any symmetric degree-2 combination also gives γ = 1 at first order, so the product is not unique; what matters is "degree 2".

**D18 (ARGUED).**
- The product is the deterministic shadow of A14's AND gating, where each end's participation is independent and multiplies.
- Read literally, "each site's records cap its own change per beat" suggests min(N_x, N_y), which gives γ = 0.
- Locality does not separate the two forms: both use the same two stars.
- Universality does not separate them either: OR is also locally Lorentz-invariant, with γ = 0.
- Q3 glues the change to rotations but says nothing about how paces compose. So the product is chosen to match γ = 1; it is not derived.

### 3.5 Task 5: beyond first order

**D19. Second order (CHECKED; comparator GR).**
- Light bending: 4M/b + **4π(M/b)²**, against GR's 15π/4. At the solar limb the difference is 0.73 μas.
- Circular-orbit periastron: K = 1 + 3x + **(29/2)x²** + (153/2)x³, against GR's 1 + 3x + (27/2)x² + (135/2)x³.
- Redshift at fixed circumferential radius: N = 1 − x − x²/2 − (2/3)x³, against GR's −x³/2.
- The package metric's Einstein tensor is G^t_t : G^r_r : G^θ_θ = +1 : −1 : +1 in units of e^{−2U}(∂U)². That is GR plus a negative-energy scalar sourced by the Newtonian field energy (Yilmaz-type, comparator).

**D20. Strong field (CHECKED/EXACT).**
- No horizon, and N ≥ 1/e (D15).
- Photon sphere at U = 1/2.
- Shadow radius 2e·M = 5.437M, against GR's 3√3·M = 5.196M (+4.6%).
- Innermost stable orbit at R = 6.34M with MΩ = 0.0633 (GR: 6M, 0.0680).

**D21. Waves (EXACT within the toy).**
- U is still set by diffusion (A6/A8), so there are no gravitational waves.
- One scalar N fixes the whole metric, so there are no tensor modes.
- A8's establishment limit is inherited: a 1/r field reaches only about 5×10⁻⁵ m in the age of the universe with Planck steps.

**D22. No frame dragging (EXACT).** P2's paces are scalar, so the effective dispersion is even in q and g₀ᵢ ≡ 0. Rotating sources drag nothing.

**D23. Moving sources (EXACT mean-field solution; ARGUED application).** A sink moving at speed v through the wanderer gas solves D∇²φ + v∂_zφ = 0, with φ ∝ e^{−v(r+z)/(2D)}/r:
- upstream the field is screened beyond D/v;
- the full 1/r survives only in a downstream wake.
- With D ≈ a²/(12τ) at the Planck scale, D/v ~ 10⁻³³ m for v = 370 km/s.
- So a moving Earth would hold no Moon. This applies to the A6/A8 mechanism generally, not just to P4.

**D24. Clocks outside the matter sector (EXACT).**
- A6's accretion clock (a test lump's capture count) runs at 1 − U, against e^{−U} for matter clocks. They differ by U²/2, about 2% at U = 0.2.
- The wanderers' own hops are unredshifted (D14).

### 3.6 Task 6: supplied versus derived

| Choice | Status |
|---|---|
| Shared beat, no waiting loops (P1) | Supplied (A15; A10's N1) |
| Paces set by records rather than possibilities | Forced once paces exist: possibility-set paces signal (A9 Th.2(d), A15 S11) |
| Product composition, b = 2a | Supplied; sets γ (D17) |
| Small dose θ0 ≲ 6×10⁻³ | Supplied (D4) |
| Cone at the vacuum's quasi-energy | Supplied (D5) |
| One-site rest energies (P3), time-symmetric word | Supplied (D3, D6) |
| Dimension-based weights for every other term | Supplied (D7) |
| Formation odds ∝ N_x | Supplied (A15 S14) |
| Exponential F with u∞ inside the law | Supplied; unique for background-independent β = 1 (D10); not reachable by a finite-range rule (D12) |
| Smooth lapse (huge averaging range) | Supplied (D13) |
| Wanderers as source, quiet void, minority density | Supplied (A6/A8) |
| Irreversible capture plus a stopped mark | Supplied (A8) |
| q ≈ 10⁻¹⁸ and q ∝ rest energy (active mass = passive mass) | Supplied |
| Unpaced wanderers | Supplied (D14) |

**Derived, given the above:** the metric, γ = β = 1, the 1PN light bending, Shapiro delay and perihelion, universality for one-site-mass Dirac species, and no reflection at smooth gradients.

**Honest assessment.** If the package worked, it would show that the records-and-beats picture can carry the static weak-field geometry of GR. That would be a proof of possibility. It would not be a derivation: the two numbers GR fixes are dialled in by two choices. It would not explain:
- why gravity is weak;
- gravitational waves;
- frame dragging;
- the fields of moving bodies.

It would also have to keep the gravity carrier on absolute time.

## 4. Checks

| Script | What it checks | Key results |
|---|---|---|
| `pn_rays.py` (mpmath, 30 digits, ≤ 2.1 s) | (a) light-bending fits | A1 = 4.00000000 for AND and 2.00000000 for OR; A2/π = 3.749999 (GR control, prediction 3.75), 3.999999 (package), 4.999996 (linear AND), 1.000000 / 1.500000 (exp/lin OR) |
| | (b) perihelion ratio | 1.000000 (GR and package), 1.166666 (linear AND), 0.333333 (exp OR), 0.500000 (linear OR) |
| | (c) circular-orbit periastron (sympy) | GR series equals (1−6x)^{−1/2}; package series as in D19 |
| | (d) photon sphere and shadow | As in D20 |
| | (e) Einstein tensor | (+1, −1, +1) |
| `invariants.py` | Redshift as a series in M/R_circ; innermost stable orbit | As in D19/D20 |
| `lapse1d.py`, time-symmetric 1D cycle (≤ 6 s) | Bloch facts | Rest quasi-energy/(μN) = 1.000000000000; two-site rest quasi-energy/(0.05N²) = 1.000000000000; γ_eff formula confirmed |
| | Delay through a U = 0.1 bump | θ0 = 0.2: 152.46 (AND) / 73.44 (OR) cycles against ray predictions 152.47 / 73.44. θ0 = 0.6: 48.12 / 23.07, matching. AND/OR = 2.076 and 2.085. Norm conserved to 10⁻¹² |
| | Reflection | As in D16 |
| | Fall, a/a_metric at packet widths σ = 40/100/200 | One-site μ=0.05: 0.966/0.992/0.996. One-site μ=0.02: 0.829/0.967/0.990. Two-site: 1.936/1.970/1.976 (lattice semiclassical value 1.987). The shortfall falls with momentum spread |
| `plainword.py` | Plain-word formula | Holds to 1.1×10⁻¹⁶; band minimum at K − π = −0.05 |
| `estimator.py` (23 s) | β for exponential response | 1 − 1/(2m) to 10 digits for m = 6 to 5000 |
| | Literal P4, tuned rule, coherence time | As in D12–D13; coherence time per unit relative variance: electron 31 s, neutron 9.1 μs, Rb-87 1.2 ns |
| `noise3d.py` (24³ gas, A6 dynamics, ≤ 1.2 s) | Count statistics | Var k matches the binomial to 0.3% (m = 6) and 2–4% (m = 124; includes a ~1% fixed-particle-number correction) |
| | Correlation time and dephasing factor | τ_int 3.4 / 24–25 ticks. Dephasing factor 116 / 11.1 / 1.59 at u = 0.01 / 0.04 / 0.2 |

**First-run error, fixed.** My first fall run used the plain word and was off by about 2×. That is how I found D6.

**Not run (worth running).**
- A 3D lattice test of massive against massless bending under the full package.
- A 3D wanderer gas with a clump plus snapshot paces, measuring β_eff and dephasing directly (overlaps A17).

## 5. Real-physics match

Comparators are from memory and not re-verified.

**Matches**
- Solar-limb deflection of 1.75″.
- Shapiro delay to Cassini precision, if θ0 and u∞ are small.
- Mercury's 42.98″ per century.
- Pound–Rebka and Gravity Probe A redshift.
- Gravity Probe B geodetic precession, which depends on γ.
- Universal free fall for one-site-mass species.

**Falsifiers**
- No gravitational waves: GW170817, and binary-pulsar orbital decay at about 0.1%.
- No frame dragging: Gravity Probe B (~37 mas/yr) and LAGEOS.
- Fields of moving bodies are wakes: lunar and planetary orbits.
- Establishment time of the 1/r field (A8).
- Nearest-neighbour version: β = 11/12, so Mercury would advance 44.2″ instead of 42.98″.
- θ0 > 6×10⁻³ fails Cassini.
- Snapshot noise fails atom-interferometer coherence of about 1 s.
- Two-site-mass species fail MICROSCOPE at order one.
- Weighting gauge plaquettes by site count violates local Lorentz invariance at order U.
- G drift (lunar laser ranging Ġ/G) if λ is fixed.

**Not decisive now**
- The 2PN bending difference of 0.73 μas.
- Shadow +4.6%, against EHT's roughly 10% precision.
- Horizonless absorbers whose surface redshift factor is at most e: comparator horizon tests (e.g. Broderick–Narayan, from memory) argue against observable surfaces.

**What would overturn these results**
- A finite-range record rule whose averaged pace is not polynomial in u. That needs non-product correlations.
- A carrier law with harmonic ln u and bounded hop rates near absorbers.
- A scalar pace rule that produces a g₀ᵢ.

## 6. Open edges and next steps

1. **Owner decisions:**
   - pace composition: product, mean or min;
   - which processes are paced: change, formation, wanderers;
   - whether the lapse may average beyond nearest neighbours.
2. Derive the AND composition from a record-level rule, or show it is a free choice. A14's stochastic AND gating is natural but noisy; the deterministic version is quiet only with a smooth lapse.
3. A carrier that propagates as a wave in the package geometry. That would address waves, wakes and establishment together, and it is missing.
4. If a gauge sector appears, it needs dimension-based weights (D7).
5. Run the 3D tests listed in §4.
6. Second-order and strong-field items (D19–D20) matter only once 3 is solved.

## 7. Plain-language summary

If the records near each place decide how much the shared possibilities change on each shared beat, then change at one place is slowed once near a clump, and passing between two neighbours, which needs both of them, is slowed twice. Light then bends and lags by the full amount seen in nature. If, besides, the slowing grows in one particular smooth way as the wandering records thin out, planet orbits turn the right amount, and everything whose weight sits at single places slows and falls alike. But both of these are choices put in to match nature, not things the rules pick. A place sees only a few neighbours' records, and from so few the slowing comes out jumpy and slightly wrong, so it would need averaging over enormous regions to keep delicate things from blurring. Even then the picture has no ripples of gravity, gives moving or spinning clumps the wrong pull, and the wandering records that carry gravity would themselves have to run on unslowed time.