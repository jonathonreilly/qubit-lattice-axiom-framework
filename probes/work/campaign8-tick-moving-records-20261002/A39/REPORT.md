*(Saved by the coordinator from the agent's final message; the agent's harness forbade writing REPORT.md.)*

# A39 report: can quiet empty space carry light-like ripples?

**Housekeeping.** No git, no repo edits, no review or audit lanes. Every run went through `run.sh`: `nice -n 10`, all four thread caps at 1, a 55 s alarm and a load gate below 6. Loads at run time were 2.8–4.2. Every model is a supplied toy, and every rule is a named conditional.

**Grades.** EXACT = proof or exact arithmetic. CHECKED = numerics in a stated toy. ARGUED = reasoning without proof. SUPPLIED = a premise put in by hand. COMPARATOR = literature recalled from memory, never adopted.

## 1. Question

**Setup.** Let Ω be a translation-invariant vacuum (one qubit per site) that is stationary under a homogeneous, finite-range change H. Call Ω quiet if every star-local formation weight F_x ≥ 0 annihilates it, F_xΩ = 0, at each star where formation can happen. That means every star, or under gating (A28) only stars next to records.

**What I set out to settle:**
1. Exactly what frustration-free structure does "quiet + stationary" imply?
2. When does "gapless ⇒ z ≥ 2" follow, and from which hypotheses?
3. Which loopholes escape it, and at what cost?

## 2. Answer (short, graded)

**Q1. The parent that exists is the formation sum, not the change.**
- Quiet alone makes Ω a zero-energy ground state of H_F = Σ F_x ≥ 0 (EXACT; this is A9's lemma).
- Quiet + stationary does **not** make the change frustration-free, and does not make Ω its ground state (EXACT, by counterexample).
- **The bridge that does it is visibility.** Suppose every local energy term of the change is bounded by nearby formation weights: h_y ≤ C Σ_{x near y} F_x, with h_y ≥ 0. Then quiet forces h_yΩ = 0 for every y. So the change is frustration-free and Ω is its ground state (EXACT).
- A9's "formation tracks the change's energy" is a special case of visibility.

**Q2. A twist lemma, derived here (EXACT).**
- **Hypotheses.** The change is frustration-free with respect to Ω, and gaplessness at k₀ is carried by a local twist: A_{k₀}Ω is a zero-energy state, with S(k) ≥ s₀ > 0 nearby. Then the softest ripple obeys ε(k) ≤ (C/s₀)|k−k₀|².
- **A clustering version (EXACT)** needs no frustration-freeness. Ω must be a ground state with summable second-moment correlations; every product vacuum qualifies.
- **A positivity lemma (EXACT).** With finitely many bands, a linear touching at zero energy forces negative energies.
- **What my derivation does not cover:** frustration-free vacua with a unique ground state and no zero-mode twist.
- The theorems I recall (Gosset–Mozgunov; Masaoka–Soejima–Watanabe) are COMPARATOR only, and their hypotheses are unverified.

**Q3. The loopholes.**
- **(a) Stationary but not the ground state.** It exists, but it is fragile. After a slow on-off cycle of a weak off-axis field, the vacuum is gone with probability 0.28; the ground-state control returns to the vacuum with probability 1.0000 (CHECKED). It is incompatible with formation tracking energy (EXACT), and it needs a painted sign pattern (A31).
- **(b) Gating.** It frees voids (EXACT) but moves the tension to matter's edges. The light-carrying entangled vacuum is full rank next to a record: smallest eigenvalue 1.0e-2 in 1D and 1.5e-4 in 2D (CHECKED).
- **(c) Composites.** There is no linear branch at the bottom (EXACT for one ripple and for isolated pair bound states). On 64², the measured exponents are 1.92–2.00 (CHECKED).
- **(d) Record ticks.** They can set a speed limit but cannot carry light that interferes (ARGUED).
- **Two further escapes:**
  - **(e) Light in the kernel.** Formation weights are blind to the light sector (EXACT construction). The cost: places that never record, a quiet matter vacuum, matter number exactly conserved (no vacuum pair creation), and a law that tells kinds of places apart.
  - **(f) Slow, energy-selective formation (A12).** The vacuum is not exactly quiet, but its rate is exponentially small. It needs Ω to be the ground state, and a per-site memory the axioms do not supply.

**Q4. Verdict: conditional.** Exact quietness and light-like ripples cannot both hold under visibility, a ground state and a local twist. They can coexist only by giving up visibility (e), exactness (f) or the ground state (a). Each has the cost stated in §3.4.

## 3. Derivation

### 3.1 Q1: what quiet + stationary implies

**Lemma Q (EXACT; A9).**
- For F_x ≥ 0: tr(F_xρ) = 0 ⇔ F_xρ = 0 ⇔ supp F_x ⊆ ker ρ_{N_x}.
- Hence H_F = Σ_x F_x ≥ 0 has H_FΩ = 0: a frustration-free Hamiltonian with Ω as a zero-energy ground state.
- There is a canonical maximal parent, H_par = Σ_x Π_ker(ρ_{N_x}). Every quiet weight satisfies F_x ≤ ‖F_x‖Π_ker. The quiet set is G = ker H_par.
- For a mixed vacuum, each component of the vacuum lies in G.

**Not implied (EXACT, by counterexample).**
- **(i) The change need not be frustration-free, and Ω need not be its ground state.** Take Ω = |0⟩^N under π-flux hopping (A31's KS form). Ω is an eigenstate, but 6 of the 12 one-flip states have negative energy on 4×3 (c1). Also, H = −H_par keeps Ω exactly stationary as its top state.
- **(ii) H and H_F need not commute.** Same example.
- **(iii) H_F's ground state need not be unique or gapped.** The aligned vacuum's quiet set contains the whole symmetric sector.
- **(iv) Stationarity is not even necessary for lasting quietness.** What is needed is that the change keep Ω's orbit inside G, i.e. that Ω's cyclic space under H lie inside G. A precessing aligned vacuum stays quiet under the covariant aligned weight.

**Lemma V, the visibility bridge (EXACT).**
- Write H = E₀ + Σ_y h_y with h_y ≥ 0. This is no loss of generality for finite range: shift each term by its minimum.
- If h_y ≤ C Σ_{|x−y|≤r} F_x, then ⟨Ω|h_y|Ω⟩ ≤ C Σ⟨F_x⟩ = 0. So h_y^{1/2}Ω = 0, hence h_yΩ = 0.
- Therefore H − E₀ ≥ 0 and (H − E₀)Ω = 0: the change is frustration-free and Ω is its ground state.
- A9's conditional "Σ⟨F_x⟩ = c⟨H − E_Ω⟩ for all states" gives H − E_Ω = c⁻¹Σ F_x ≥ 0 directly. So **"records form where energy is" excludes loophole (a)**.
- The calm aligned class satisfies visibility: with h_b = 2P_singlet(b) and F_ferro = Σ_y P_singlet(x,y)/3.5, we get h_b ≤ 7F_ferro. A KS-signed bond (2P_triplet) violates it.

**Gated version (EXACT).** Under A28, F^(∅) = 0, so H_F lives only on stars next to records, and visibility forces frustration-freeness only there. Voids are unconstrained.

### 3.2 Q2: frustration-free plus gapless

**Twist lemma, frustration-free version (EXACT; derived here).**
- **Hypotheses:**
  - H − E₀ = Σ_y h_y with h_y ≥ 0, h_yΩ = 0, range r, translation-invariant;
  - a local a₀ (range r_a), with a_x its translates and A_k = Σ_x e^{ik·x}a_x;
  - zero-mode condition: h_y A₀Ω = 0 for all y.
- **Steps:**
  1. Since h_y^{1/2}Ω = 0 and h_y^{1/2}A₀Ω = 0, we get Σ_x[h_y^{1/2}, a_x]Ω = 0.
  2. Hence h_y^{1/2}A_kΩ = Σ_x (e^{ik·x} − e^{ik·y})[h_y^{1/2}, a_x]Ω, with only |x−y| ≤ R = r + r_a contributing.
  3. So ‖h_y^{1/2}A_kΩ‖ ≤ |k|·2‖h₀‖^{1/2}‖a₀‖Σ_{|d|≤R}|d| =: |k|√C.
  4. Summing over y: ⟨A_kΩ|H − E₀|A_kΩ⟩ ≤ |Λ|Ck², while ‖A_kΩ‖² = |Λ|S(k).
- **Conclusion:** the lowest energy at momentum k is ≤ Ck²/S(k). On a torus, this caps the gap at k = 2π/L by C(2π/L)²/s₀, which is z ≥ 2 when S ≥ s₀ > 0.

**Twist lemma, clustering version (EXACT).**
- Here Ω is a translation-invariant ground state, H − E₀ ≥ 0 (not necessarily frustration-free), and A_{k₀}Ω is a zero-energy state.
- Suppose n_d = ⟨a₀†[H, a_d]⟩ and s_d = ⟨a₀†a_d⟩ have summable second moments. This holds for exponential clustering, and trivially for product vacua.
- Then N(k) = Σe^{ikd}n_d ≥ 0 is C² with N(k₀) = 0, so ∇N(k₀) = 0 and N ≤ C′|k−k₀|². Together with S(k₀) > 0, ε(k) ≤ C″|k−k₀|².

**Where frustration-freeness matters.**
- For any H with a conserved density, Feynman's ratio gives ε ≤ f(k)/S(k), with f = O(k²).
- Linear ripples need S(k) ~ |k|. That means power-law correlations and no extensive zero mode (A₀Ω = 0).
- The antiferromagnet does exactly this: S(k)/k ≈ 0.37–0.43 (CHECKED, c2).
- Frustration-freeness supplies the k² numerator without any conservation law.
- **Neither lemma covers** a frustration-free vacuum with a unique ground state, A₀Ω = 0 and power-law correlations. Example: an RK-type quiet state, if some other change has it as ground state. This is the gap in my derivation.

**Positivity lemma (EXACT; uses Rellich's analytic-branch theorem, a standard result I recall).**
- If ripple energies at momentum k are eigenvalues of a finite analytic Hermitian H(k), all ≥ 0 and vanishing at k₀, then along every line the vanishing branch is analytic and ≥ 0. So it is O(t²).
- More directly: any linear touching w·q ± |Vq| changes sign under q → −q.
- **Single band (EXACT; A31 D3).** An analytic band can never give an isotropic cone in d ≥ 2: ε(k₀+q) − ε₀ = v·q + O(q²) cannot equal c|q| in every direction unless c = 0.

**The excited-vacuum loophole and positivity.** If Ω is stationary but not the lowest state:
- visibility fails (Lemma V), so formation cannot track energy (EXACT);
- energy-selective detection (escape f) is unavailable, because a detector can gain energy by creating negative-energy ripples (ARGUED);
- quietness is protected only by an exact symmetry, and Ω is degenerate with a continuum of zero-energy pairs (c1, CHECKED).

**Recalled theorems (COMPARATOR, unverified hypotheses):**
- Gosset–Mozgunov 2016: for frustration-free 1D chains, an open-chain gap above about c/n² at some n implies a gap. So gapless chains have gaps O(1/n²).
- Higher-dimensional thresholds (Lemm–Mozgunov, Anshu, Lemm–Xiang) may be weaker than 1/n² in some geometries. I am not certain.
- Masaoka–Soejima–Watanabe 2024: gapless frustration-free systems disperse quadratically or softer, under assumptions I believe involve locally created excitations and/or finite correlation length. My frustration-free twist lemma is the core I can derive myself.
- All known gapless frustration-free examples have z ≥ 2: the aligned ferromagnet, RK points, and Motzkin/Fredkin chains.

### 3.3 Q3: the loopholes

**(a) Stationary, not ground (|0⟩^N under π-flux hopping).**
- The cone sits at E = 0 with negative states below (A31 D7: the site-sum-0 gauge).
- **What is wrong with it:**
  1. **Energy is not bounded below by the vacuum.** A (+E, −E) pair costs nothing, and a linear touching forces negative energies (EXACT).
  2. **Fragility.** Any field that breaks the protecting symmetry opens a zero-energy pair continuum. In the toy, 139 states lie within 0.05 of E_Ω, against 0 for the ground-state control.
     - A slow on-off cycle of a δΣX field returns the vacuum with probability 0.990 (δ = 0.03) and 0.719 (δ = 0.10). The quiet star weight then fires with chance 6.5e-3 and 0.24.
     - The ground-state control returns with 1.0000, and its weight fires with chance ≤ 1.7e-7 (CHECKED).
     - An off-axis record's field is exactly such a field (A28 Step 6).
  3. **Incompatible with "records where energy is"** (Lemma V) and with energy-selective windows.
  4. **Negative-energy ripples would source gravity with the wrong sign** if the source tracks energy (ARGUED).
  5. **It still needs the law-level sign pattern** (A31).
- **Variant (a′): a cone at finite energy.** Add a field h > W. Ω becomes the ground state, and the cone sits at E = h > 0 with group velocity v. This is not gapless. Every light ripple carries a rest-energy offset, and a softer quadratic band lies below it (EXACT for the bands). Real light has E = c|p| (COMPARATOR).

**(b) Gating.**
- Voids need no quietness, so neither lemma binds the bulk (EXACT; Lemma V gated).
- At edges, A28's floor holds: exactly for free-fermion seas, and checked for the staggered sea (C72).
- c2 (CHECKED): the antiferromagnet, C57's light-carrying comparator, is full rank next to a record.
  - 1D edge star: smallest eigenvalue 1.05e-2 at the plain wall strength. It falls to 1.2e-4, 3.0e-6 and 5.2e-8 at 3×, 10× and 30× wall strength (about λ^{−3 to −4}).
  - The 2D 4×3 edge star gives 1.5e-4. That torus is frustrated along y, so it serves as a rank check only.
  - The aligned vacuum gives 0 (≤ 1e-31).
- ARGUED: in these finite toys det ρ_U(λ) is analytic and nonzero at λ = 1, so exact edge quietness occurs at most at isolated λ.
- **So gating moves the tension to the edges; it does not remove it.**

**(c) Composites over a calm product vacuum** (flip number conserved, Ω the ground state).
- **One ripple:** a single analytic band. Gapless implies quadratic (EXACT).
- **Two ripples:**
  - The continuum bottom is ≤ 2ε(K/2) = O(K²), so a linear branch could only be an embedded resonance, not the bottom (EXACT).
  - An isolated K = 0 bound state is analytic in K (Kato; standard), and ≥ 0, so it is quadratic (EXACT).
  - A cone between composite bands at E = 0 forces negative energies. At E > 0 it is possible in principle (Weyl points are generic in 3D; ARGUED), but then it is case (a′).
- **n ripples:** by cluster induction (ARGUED).
- **CHECKED (c3, 64²):**
  - Model 1 is the frustration-free aligned rule. The lowest pair energy tracks 2ε(K/2) to within 3e-4, with E/K² = 0.4995 → 0.4899 and local exponents 1.997–1.967.
  - Model 2 has gapped flips (m = 0.5) and an attraction tuned so the K = 0 pair sits at E = 0 (1.8e-12; isolated, next state 1.0014).
  - It disperses with E/K² = 0.346 → 0.330 and exponents 1.99–1.92.
  - The same attraction gives a 2×2 four-flip block a diagonal energy of −5.92 (3×3: −31.3). So those sectors drop below the vacuum, and Ω stops being the ground state (EXACT, variational).

**(d) Light carried by the record-tick structure (ARGUED).**
- Records are permanent and at most one per site, so a record-borne pulse leaves a trail. That is incompatible with light that interferes and with transparent voids.
- Steps chosen by odds are diffusive (z = 2) unless directed. A directed conveyor has a built-in index, so it is chiral and anisotropic.
- Ticks can set the strict speed limit (one site per tick), but the light ripple itself must be an unrecorded excitation of the change.

**(e) Light in the kernel (EXACT construction; SUPPLIED toy).**
- **Construction:**
  - Field places carry an entangled light-carrying vacuum Ω_f (for example J > 0, σ·σ).
  - Matter places carry an empty or calm vacuum |0_m⟩.
  - The formation weights are F_x = F_matter ⊗ 1_field.
  - The coupling vanishes on empty matter, for example g n_m(σ_f·σ_f) plus matter hopping.
- Then Ω = |0_m⟩ ⊗ Ω_f is an exact eigenstate, tr(F_xρ) = 0, and field ripples keep their own dispersion.
- Visibility fails, so Lemma V and the twist lemma never bind the field. A28's edge floor applies only to the matter marginal (EXACT).
- **Costs:**
  1. **Field places never record.** This matches A31's D10, which has its own collision with A25's layout (C61).
  2. **The law must treat field and matter places differently.** A single glued pair sign cannot be ferromagnetic on matter and antiferromagnetic on field; star terms (C56) are untested. This is a role pattern, law-level or state-level, and an owner decision.
  3. **Matter number must be exactly conserved.** Any local term that creates matter from the vacuum puts O(g²/Δ²) matter admixture into the true vacuum, which charge weights then record (ARGUED, first order). That conflicts with relativistic pair creation (COMPARATOR: vacuum polarization).
  4. **Matter over a quiet vacuum has one analytic band.** Massive matter (quadratic at rest) is fine; massless relativistic matter with a sea is not (A9 n4).
- **Light is then recorded only through matter.**

**(f) Slow, energy-selective formation (A12).**
- The weight is a time-extended instrument with memory, not a per-tick tr(Fρ). The vacuum rate is nonzero but falls like e^{−2κT} (A12).
- Ω must be the ground state.
- **Cost:** a per-site memory that is not supplied.

### 3.4 Q4: the tension theorem

**Theorem T (EXACT).** Assume:
- **T1.** The change and the weights are homogeneous and finite range.
- **T2.** Quiet: F_xΩ = 0 everywhere.
- **T3.** Visibility: h_y ≤ C Σ_{x near y} F_x.
- **T4.** Gaplessness at k₀ is carried by a local twist, with S(k) ≥ s₀ near k₀.

Then:
- Ω is the ground state;
- the change is frustration-free;
- the softest ripple obeys ε(k) ≤ (C/s₀)|k − k₀|², so no z = 1 ripple is softest at k₀.

**Corollary (EXACT).** For product vacua, T3 can be replaced by "Ω is the ground state" (clustering lemma). Over a uniform product vacuum, a homogeneous law gives no isotropic cone among single ripples at any energy.

**Escapes and costs.**

| Escape | Hypothesis dropped | Cost in the axioms' register |
|---|---|---|
| (e) light in the kernel | T3 | Two kinds of places, field places never record, matter number exactly conserved (no vacuum pairs), light recorded only via matter |
| (f) energy-selective windows | T1 (per-tick locality); exact quietness | Per-site memory; vacuum rate exponentially small, not zero; needs the ground state |
| (b) gating | T2 in voids | Tension moves to edges; at edges it needs (e), (f) or an exactly quiet buffer (not found) |
| (a) excited vacuum | ground state (T3 fails) | Painted sign pattern; energy not bounded below; quietness held only by an exact symmetry; incompatible with (f) |
| (a′) finite-energy cone | gaplessness | Rest-energy offset on light; a softer quadratic band below |
| frustration-free with no zero-mode twist | T4 | Not covered by my derivation; no known example with z < 2 (COMPARATOR) |

## 4. Checks

| Script | Toy | Key numbers | Time, memory |
|---|---|---|---|
| `c1_vacuum_decay.py` | 4×3 torus, 12 qubits; π flux verified on all 12 plaquettes | One-flip energies ±2.83, ±2.24 (×2), ±2, ±1 (×2); 6/12 negative; two-flip block 27/66 negative | 19.2 s, 96 MB |
| | | States within 0.05 (0.2) of E_Ω: 139 (267) versus 0 (0) for the ground-state control | |
| | Slow cycle δ(t) = δ·sin²(πt/400), dt = 0.5 | Not ground: return 0.9904 / 0.7192, flip density 1.7e-3 / 8.6e-2, star weight 6.5e-3 / 0.24 at δ = 0.03 / 0.10 | |
| | | Ground: return 1.0000, flip density ≤ 3.3e-8, star weight ≤ 1.7e-7 | |
| `c2_edge_rank_afm.py` | Antiferromagnet next to a record; ring gaps | Edge-star smallest eigenvalues as in §3.3(b) | 1.6 s, 68 MB |
| | | Ring gaps N = 6–12: antiferromagnet gap·N = 16.43 → 17.08 (z = 1, slow drift); aligned gap·N² = 72.0 → 77.2, matching 4(1−cos 2π/N), limit 8π² | |
| | N = 12 antiferromagnet | S(k)/k = 0.368, 0.393, 0.432 | |
| `c3_two_ripple.py` | 64², relative coordinates (dimension 4095), bosonic sector by penalty, shift-invert below a Gershgorin bound | Numbers in §3.3(c) | 4.1 s, 72 MB |

**Superseded runs, recorded honestly:**
- The first `c1` used an abrupt quench. It showed dressing in both cases: time-averaged survival 0.84 (not ground) against 0.59 (ground) at δ = 0.1, so a quench does not discriminate between them. Its output was overwritten by the slow-cycle version.
- The first `c3` had two bugs. Odd momenta carried a twist offset in the relative momentum, and the shift-invert solver found the eigenvalue nearest the shift rather than the lowest. Both were fixed, and only even momenta are reported.
- The first `c2` had a wrong formula label (factor 2). It was fixed and rerun; the computed gaps were unchanged.

## 5. Real-physics match (comparators flagged)

- **Light has z = 1 to high precision** (photon-mass bound about 1e-18 eV; COMPARATOR). Any setting satisfying T1–T4 contradicts it.
- **The physical vacuum is full rank on every local algebra** (Reeh–Schlieder; COMPARATOR), so it is not quiet in A9's strict sense. Real detectors are quiet because they are energy-selective and the vacuum is the lowest state (Glauber; Unruh–DeWitt; COMPARATOR). That is escape (f), and it needs positivity, which loophole (a) violates.
- **The spectrum condition** (vacuum lowest; COMPARATOR: Wightman) excludes (a).
- **Photons are detected only via charged matter** (COMPARATOR), which fits escape (e). But QED vacuum polarization (COMPARATOR) is the pair creation that (e) must forbid for exact quietness.
- **Massive matter's E ≈ mc² + p²/2m is quadratic at rest.** So z = 2 over a calm vacuum is harmless for massive matter and fatal only for massless ripples.
- **Quantum dimer and ice models (COMPARATOR).** At the RK point the vacuum is exactly quiet and the photon disperses as ω ~ k². Away from it, the speed grows like √(1 − V/t) and exact quietness is lost. This sits right on the tension line. The repo cross-link to #9239 comes from the memory index only and is unverified against main.
- **Falsifiers:**
  - quadratic dispersion in anything meant as light;
  - a photon rest-energy offset (a′);
  - decay of the vacuum near off-axis records (a).

## 6. Open edges

1. **Close or exhibit the T4 gap.** Does a frustration-free vacuum with a unique ground state, no zero-mode twist and power-law correlations (RK-like) admit z = 1 under some change? Verify the recalled theorems' hypotheses.
2. **Realize escape (e) on Z³ with one qubit per site.** Can a homogeneous glued law, possibly with star terms (C56), host calm matter places and a z = 1 field sector together? How does it relate to A25's roles and to A31 D10 (C61)?
3. **Quantify (e)'s vacuum rate under a weak pair-creating coupling,** O(g²/Δ²), against A9 and A28 bounds.
4. **Edge buffers.** Can a record's own field make its neighbours exactly quiet while the bulk carries z = 1? The plain antiferromagnet decays only as about λ^{−3 to −4}.
5. **3D composite Weyl points at finite energy:** do they exist and are they stable (case a′)?
6. **Repo ice/photon lane:** check "quiet ⇔ v = 0" there.
7. **Owner decisions (plain).**
   - Should records be allowed to respond to light directly? Then light is slow.
   - Or should light be invisible to records, which requires two kinds of places and no matter appearing from empty space?
   - Or should records form slowly and energy-selectively, with a memory per spot and a tiny nonzero rate in empty space?
   - Or should empty space be allowed not to be the lowest state, which is fragile and needs a painted pattern?

## 7. Plain-language summary

Can empty space be both quiet and carry light? Not if the thing that triggers records can sense light ripples directly and empty space is the calmest possible state. In that case I proved that the gentlest ripples must spread slowly, like waves in a magnet, never like light. Quiet empty space can carry light in three ways, each with a price. First, light could be invisible to records, so that only matter gets recorded and light is noticed only when matter absorbs it; this needs separate places that never record, and it needs matter never to appear out of empty space, which real physics does allow. Second, records could form slowly and only in response to energy actually delivered; then empty space is not perfectly quiet but almost so, and each spot needs a small memory the axioms do not supply. Third, empty space could be not the calmest state; that needs a painted pattern of signs, and the toy shows that quietness then breaks under a small sideways nudge. Light built from pairs of slow ripples does not help, and quiet only next to matter just moves the problem to matter's edges.