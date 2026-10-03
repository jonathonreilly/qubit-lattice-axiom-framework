I have all the numbers. One last point to note: the reach computation shows the sea's best single-mode formation weight has a vacuum rate falling about as R⁻³ with its support radius R (1.3e-2 on the star, 2.1e-5 at R=16). The report follows.

# A9 report: what the per-tick formation chance may depend on

Scripts and outputs are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A9/`.

**Grades.** EXACT = proof or exact arithmetic. CHECKED = numeric check with a stated tolerance. ARGUED = reasoning without proof. COMPARATOR = literature, cited and not adopted.

All models here are supplied toys, and every rule is a named conditional, not framework content. I use "formation weight" for the local operator F_x.

## 1. Question

What may the chance that a record forms at site x on a tick depend on, given four requirements?
- **(i) No signalling.** The chance must be linear in the possibilities (lane T, T1.2).
- **(ii) Covariance.** Qubit's "No possibility is privileged"; translations and proper cubic rotations; Q3, under which formation odds are not soldered.
- **(iii) Locality.** Only nearest-neighbour conditions: unrecorded neighbours' possibilities (Q1) and recorded neighbours (Q7).
- **(iv) A quiet vacuum.** The vacuum never forms records.

Is the answer forced into chance = ⟨F_x⟩, with F_x ≥ 0 local, covariant and annihilating the vacuum? A concrete example would be the local excitation energy of a frustration-free change: "records form where energy is".

## 2. Answer

**Conditional yes, with two forced additions and one thing that is not forced.**

**The form is forced (EXACT).** Requirements (i) and (iii) force the per-tick chance to be tr(F_x ρ), for one operator 0 ≤ F_x ≤ 1 on x and its six neighbours, per pattern of recorded neighbours. Dependence on recorded contents is unrestricted. This holds given that a distant record can steer a neighbourhood, which Q1's at-once sharing supplies.

**Two additions are forced by the same argument (EXACT):**
- The lock odds given formation must be computed after the formation update. Pairing a state-dependent chance with the site's raw odds signals.
- A tick with no record must also reshape the possibilities; the minimal form is √(1−F_x).
- The toy confirms both: linear rules stay at round-off (≤ 8e-16), while these two violations signal by up to 0.08 and 0.04 (CHECKED).

**The quiet vacuum has an exact criterion (EXACT):**
- (iv) holds iff F_x annihilates the vacuum.
- That is possible iff the vacuum's marginal on each star is rank-deficient, i.e. iff the vacuum is a zero-energy ground state of the frustration-free sum Σ F_x.
- With Q4's equal single-site odds, neighbours in the vacuum must share possibilities.
- Covariant quiet vacua exist on Z³ qubits: aligned ("ferromagnetic") states, Klein-type singlet coverings, and a stabilizer state if internal covariance is reduced.
- The half-filled staggered sea is not one. No local linear rule leaves it quiet: EXACT for the massless sea; CHECKED with smallest star eigenvalue 5.0e-6.

**Not forced:** that F_x is the change's own energy.
- "Records form where (Σ F_x)-energy is" is a tautology.
- Tying F to the change is a separate named conditional.
- If adopted, the change must itself be frustration-free. By a comparator theorem, its massless ripples then disperse quadratically rather than like light (ARGUED).

## 3. Derivation

### 3.0 Setup and hypotheses

- **Star.** N_x = x plus its 6 neighbours.
- **State.** ρ = the snapshot's possibilities on the unrecorded sites of N_x. R = the recorded neighbours' contents.
- **Recorded neighbours.** By Q1 a recorded site's possibility agrees with its record, so it is a fixed pure state |r⟩. Acting on it reduces to a classical dependence on r.
- **H1, locality (requirement iii).** The chance depends on the snapshot only through (ρ, R). No-signalling also implies this, because every extension of ρ is reachable from a purification by an operation on distant sites.
- **H2, steering.** For any σ1, σ2 on N_x and any p, a snapshot exists in which a record at a distant site b, outside x's reach that tick, leaves N_x in σ1 or σ2 with odds p and 1−p under one distant condition. Under another distant condition it leaves N_x's marginal equal to ρ̄ = pσ1 + (1−p)σ2.
  - Construction: |Ψ⟩ = √p|s1⟩|00⟩_bc + √(1−p)|s2⟩|11⟩_bc, with s_i purifying σ_i on distant sites and c a distant flag.
  - The two conditions are menu {0,1} versus {+,−} at b. "b forms now versus later" also works.
- **H3, no signalling.** x's formation statistics, averaged over b's unread outcome, do not depend on b's condition.

### 3.1 Theorem 1 (EXACT): the chance is tr(F_x ρ), with 0 ≤ F_x ≤ 1

**Proof.**
1. By H2 and H3, f(pσ1 + (1−p)σ2) = p·f(σ1) + (1−p)·f(σ2) for all σ1, σ2, p. So f is affine on the density operators of N_x.
2. An affine f extends uniquely to a linear functional on Hermitian operators. Well-definedness: aρ1 − bρ2 = cρ3 − dρ4 implies a+d = b+c, and affinity gives equal values.
3. Riesz representation gives f(σ) = tr(Fσ) for a Hermitian F.
4. Since 0 ≤ f ≤ 1 on pure states, 0 ≤ F ≤ 1.

**Record dependence.** F_x = Σ_R |R⟩⟨R| ⊗ F_x^(R). Linearity constrains only the possibilities, not the classical record contents R.

### 3.2 Theorem 2 (EXACT): the whole formation step is a local instrument

**(a) Joint statistics.** P(form, lock k) must also be linear. So P(form, k) = tr(E_k ρ), with E_k ≥ 0 and Σ_k E_k = F_x.

**(b) The "product rule" signals.** The product rule pairs a linear chance with the site's raw odds: P(form, k) = tr(Fρ)·tr(P_k ρ_x).
- Proof: a product of two affine functions on the state space is affine only if one of them is constant (restrict to segments; ΔaΔb = 0 on an open dense set). So the product rule needs F ∝ 1 or a trivial menu.
- Consequence: with a state-dependent chance, the lock odds are tr(E_k ρ)/tr(Fρ), the odds after the formation update, for example E_k = √F P_k √F.
- Bell example (CHECKED): x is linked with distant b, and F = |1⟩⟨1|_x. The product rule gives P(form, lock 0/1) = (0.25, 0.25) when b has no record or locks in X, and (0, 0.5) when b locks in Z. The instrument rule gives (0, 0.5) in every case.
- **Flag for Campaign 7, sentence 3** ("odds from the site's own part"): it is compatible with a possibility-dependent formation chance only if "own part" is read after the formation update. Alternatively, F must not act on x and x must be uncorrelated with its neighbours.

**(c) A tick without a record must update the possibilities.**
- If the no-record branch left the possibilities untouched, P(no record on tick 1, record on tick 2) = (1 − tr Fρ)·tr(U†FU ρ). That is quadratic, so it signals unless F ∝ 1.
- So the no-record branch is a linear, completely positive map with weight tr((1−F)ρ). The minimal (Lüders) choice is √(1−F).
- Because F·vac = 0, this update leaves the vacuum untouched. Repeated null updates move excitations toward the zero-weight sector (see 3.7c).

**(d) Menus.**
- A menu chosen as a function of unrecorded neighbours' possibilities signals: by up to 0.47 in the toy (CHECKED).
- Under linearity, menus may depend freely on records (Q7). They can depend on unrecorded possibilities only through one joint linear instrument on the star.

**(e) Converse.** Local instrument families do not signal outside the cone (A5, T1.2).

### 3.3 A state-independent chance (Task 1) (EXACT)

1. "State-independent" means F_x^(R) = p(R)·1.
2. If "No possibility is privileged" is read site by site (covariance under independent automorphisms of each site's M₂(C)), Schur's lemma forces F_x^(R) = p(R)·1. The commutant of ⊗U(2) on (C²)^⊗7 is the scalars.
3. If p(∅) > 0, every empty site with no recorded neighbour forms at rate p. Then h(t) = h0·(1−p)^t exactly (A4, 3.1e): every region freezes. Void formation also screens clock potentials (A6, m² = f0/κ). Not quiet.
4. If p(∅) = 0, the rule is quiet but blind to the possibilities. The empty grid is inert, and p0 = p(all recorded) is a free choice.
5. Q4 governs lock odds, not the formation chance. If it is extended to say an uninfluenced site's chance cannot depend on which possibility it holds, polarization gives F restricted to x = c·1_x.
6. **Conclusion:** a state-independent chance is either noisy and freezing, or energy-blind. Tracking "where things happen" needs the relational (global) reading of covariance.

### 3.4 Covariance classes (EXACT)

**Global internal reading.** F commutes with U^⊗7. By Schur–Weyl duality, F lies in the span of permutations of the 7 star factors, invariant under the 24 cubic rotations that permute the neighbours. Q3: spatial rotations only permute sites.

**With full S₇ symmetry:**
- F = Σ_S f_S·P_S(star), with S ∈ {1/2, 3/2, 5/2, 7/2} and 0 ≤ f_S ≤ 1.
- Ferromagnetic example: F_ferro = Σ_y P_singlet(x,y)/3.5. Its kernel is the symmetric subspace Sym⁷ (dimension 8); the normalization 3.5 is CHECKED.
- Klein example: F_Klein = P_{7/2}(star), which is the projector onto Sym⁷.
- These two choices are complementary.

**Strict menu-relative reading (Q3 + Q4 applied to the chance).** If F must be invariant under rephasing and relabelling the menu at x alone, then F = 1_x ⊗ G_{N(x)}: only the neighbours' possibilities set x's chance.

### 3.5 Quiet-vacuum criterion (Task 2)

**Lemma (EXACT).**
- For F ≥ 0, tr(Fρ) = 0 ⇔ Fρ = 0 ⇔ supp F ⊆ ker ρ_star. The quiet rules form the cone 0 ≤ F ≤ Π_ker.
- So a nonzero quiet rule exists iff the vacuum's star marginal is rank-deficient, iff the vacuum is a zero-energy ground state of a frustration-free local positive H_F = Σ F_x.
- Vacuum rate bound: tr(Fρ) ≥ λ_min(ρ)·tr(F). By Ky Fan, the least vacuum rate of a rank-d projector is the sum of the d smallest eigenvalues of ρ.

**Q4 plus quiet ⇒ sharing (EXACT).** With every single-site marginal equal to 1/2, a product star marginal would be 2⁻⁷·1, which is full rank. So quiet neighbours must be linked, classically or quantum-mechanically.

**Vacua that cannot be quiet:**
- **(n1)** The maximally mixed state (1/2)^⊗: full rank (EXACT).
- **(n2)** A product |0⟩^⊗ with a law singling out |0⟩: a law-level privileged possibility, since the stabilizer of |0⟩ in SU(2) is only U(1). With an SU(2)-covariant law, the whole orbit |n⟩^⊗ is quiet; that is the ferromagnet (EXACT).
- **(n3)** Pair-local, SU(2)-invariant terms (EXACT):
  - A positive invariant two-qubit term is h = a·P_s + b·P_t.
  - If b > 0, every nearest-neighbour pair must be a pure singlet, which monogamy forbids.
  - So b = 0, and the quiet states are symmetric on every pair. On Z³ these are mixtures of |n⟩^⊗ (quantum de Finetti; COMPARATOR: Størmer, Hudson–Moody).
  - So the singlet-type (antiferromagnetic) option is not frustration-free with pair terms.
- **(n4)** Dirac seas, including the half-filled staggered sea.
  - Massless (EXACT): suppose a finitely supported v satisfies Pv = v. Then Hv = −|H|v, so |H|v has finite support. |H| is the translation-invariant operator with symbol |E(k)| = √(Σ sin² k_μ), so |E|·v̂ would be a trigonometric polynomial. At a Dirac point, |E| ≈ |k| is a cone; |k|·(nonzero analytic) is never analytic, because |k| is not rational. The same holds for Pv = 0. So every restricted correlation eigenvalue lies in (0,1), and the Gaussian marginal is full rank on every finite region.
  - Massive: ARGUED by branch points, and CHECKED numerically.
- **(n5)** Frustrated antiferromagnetic ground states: CHECKED full rank on small clusters only.

**Vacua that can be quiet (EXACT):**

| Family | Formation weight | Quiet vacua | Change that fixes them | Costs |
|---|---|---|---|---|
| (e1) Ferromagnetic | any F with kernel ⊇ Sym | \|n⟩^⊗ and mixtures; the SU(2)-twirled mixture has single-site 1/2 | Any product of partial swaps e^{−iθ·SWAP} fixes every \|n⟩^⊗ exactly; per-tick covariance needs cycled partitions (A3, Step 10) | Magnons ω = J(1−cos k), i.e. z = 2 |
| (e2) Klein valence-bond | P_{7/2}(star) | Every nearest-neighbour singlet covering and every superposition of coverings (CHECKED ≤ 4e-19, single-site marginal exactly 1/2); translation- and rotation-invariant mixtures exist | Any ordered product of e^{−iθF_x} fixes all quiet states | 7-body star terms; extensive degeneracy |
| (e3) Stabilizer (3D cluster state) | (1−K_x)/2, K_x = X_x·Π_y Z_y on the star | Unique, pure, translation- and rotation-invariant, single-site 1/2 | e^{−iθΣF} is a covariant, strictly local step | The law privileges the X and Z axes (internal covariance only finite); moving excitations need extra vacuum-annihilating hops |

- Why (e2) is quiet: x's singlet partner is inside its star and the other five neighbours are paired outside, so the star's total spin is at most 5/2.
- Within the S₇ family, F ∝ P_{7/2} is the unique weight quiet on coverings, because covering marginals populate S = 1/2, 3/2 and 5/2.

**Strict menu-relative reading (F = 1_x ⊗ G).** The 6-neighbour marginals of a single covering and of the cluster state are maximally mixed (EXACT), so (e2) and (e3) fail and (e1) passes.

**Comparator (Lieb–Schultz–Mattis–Oshikawa–Hastings).** With one spin-1/2 per site, SU(2) and translations, H_F cannot have a unique gapped symmetric ground state. This fits (e1) and (e2) being degenerate and (e3) not being SU(2)-covariant.

### 3.6 Best approximate form when marginals are full rank (Task 2)

**Least vacuum rate per tick for the massless sea** (Ky Fan; CHECKED, converged in L):

| Formation weight | Vacuum rate per tick |
|---|---|
| Rank-1 projector | 5.0e-6 |
| Rank-8 | 4.0e-5 |
| Rank-32 | 1.6e-4 |
| Rank-96 (everything except the 32 likeliest star patterns) | 2.5e-2 |

For staggered mass m = 0.5 the rank-1 rate is 1.4e-7.

**Energy-based weights.** F = (h − λ_min)/(λ_max − λ_min) has vacuum rate equal to the vacuum's frustration over the range (EXACT). In the massless sea that is 0.012 per tick for the star hopping energy and 0.30 for a single bond (CHECKED).

**Trading reach for quietness.** Use one upper-band local mode, P₊e_x, cut to radius R. Its vacuum rate falls as ε(R) ≈ R⁻³ (CHECKED, local slope −3.0 to −3.2 for R = 6–16):

| R | 1 (star) | 3 | 6 | 12 | 16 |
|---|---|---|---|---|---|
| ε(R) | 1.28e-2 | 2.42e-3 | 3.75e-4 | 4.92e-5 | 2.05e-5 |

**Tiny vacuum rate ε.**
- Freezing e-fold time is about 1/ε ticks (A4, 3.1e).
- Screening length is about √(κ/ε) sites (A6, 3.9). For example, ε = 5e-6 gives about 2·10⁵ ticks and 129 sites; ε = 0.012 gives about 83 ticks and 2.6 sites.
- With Planck-scale ticks, staying unfrozen for the age of the universe needs ε ≲ 10⁻⁶¹, and A6's 1/r profile out to about 1 AU needs ε ≲ 10⁻⁹³ (ARGUED).
- That requires the vacuum to be frustration-free to extreme precision, a fine-tuning similar in kind to the cosmological-constant problem. This is a dimensional observation, not evidence.

### 3.7 Consequences if formation tracks local excitation energy (Task 3)

**(a) Records form where things happen.**
- Σ_x ⟨F_x⟩ = c·⟨H_F⟩ (EXACT).
- In the 1D magnon toy the vacuum never forms, a uniform magnon never forms, and a plane wave's chance per tick equals 2c(1−cos k) to 6 digits (CHECKED).

**(b) Covariance makes records relational (ARGUED; toy CHECKED).**
- An SU(2)-covariant weight compares neighbours, so it cannot single out which end of a bond holds the excitation.
- In the toy, 53–80% of the records triggered by one excitation lock the vacuum value next to it, typically within 1–2 sites.

**(c) Soft excitations can escape being recorded (EXACT).**
- Let D be the set of states with zero formation weight that the change maps into itself. Then P(never recorded) ≥ ‖Π_D ψ0‖², with equality when nothing else stays at zero weight. Proof: the null update and the change both preserve D and its complement.
- In the ferromagnet, D contains the rotated vacuum (the uniform magnon). Deterministic check: P(never recorded) = |⟨uniform|ψ0⟩|² to within 3e-12 (CHECKED).
- Degenerate quiet sectors, as Lieb–Schultz–Mattis forces for SU(2)-covariant vacua, therefore hide soft modes.

**(d) The lone-hole odds p0 (A4, lane M).**
- p0 = tr(F_eff ρ_x), with F_eff = ⟨R|F|R⟩ on the hole. Its floor is λ_min(F_eff) (EXACT).
- **Klein:** p0 ≥ 1/7! = 1.98e-4 always (EXACT, Marcus's permanent inequality); numerically ≥ 8.9e-3. Enclosed holes always freeze.
- **Ferromagnetic:** zero floor iff all six recorded contents agree. That happens in 3.4% of equal-odds Z draws (expected 1/32) and never for Haar-random contents (CHECKED).
- **Cluster:** zero floor iff the records are Z eigenstates (CHECKED).
- **Rule switch:**
  - If recorded neighbours enter F (variant A), the generic outcome is freezing.
  - If they do not (variant B), p0 ≡ 0 and the rule is in A4's thinning class. But the toy shows 19–55% of excitations end up enclosed by records in a zero-weight state and are never recorded (CHECKED).
- Energy tracking realizes A4's N5: formation switches off for a reason the record pattern does not show.

**(e) Moves and clocks (ARGUED).**
- Under A3's R1, moves are re-formations, so they also need ⟨F⟩ > 0 at the destination.
- Under R3, moves follow the possibilities' flow, which vanishes in a stationary quiet vacuum.
- Either way, quiet regions host no events. The move clock ticks only where energetic records travel, and a record whose content agrees with the vacuum is inert.

**(f) Gravity source (EXACT at A6's mean-field level; ARGUED overall).**
- **Majority carriers (u∞ > 1/2):** formation consumes holes at rate c·e(x)·h(x). That gives Δ_lat N = (c/κ)·e(x)·N, A6's transparent absorber with q·n → c·e. The source is then proportional to energy density, closer to T₀₀, with slower clocks near energy (A6 sign table).
- **Minority carriers:** records minted at energy that wander off are exporters, which gives the wrong sign. The GR sign needs capture; one route is a carrier jammed by records formed around it, at a rate ∝ e·u.
- Quietness gives f0 = 0, so the far field is massless.
- Compact sources still saturate at their capacity, which grows with radius rather than content: non-additive, as in A6.

**(g) Breeding.**
- Variant A: each recorded excitation gets a bounded halo of vacuum-content records (0.8–1.6 per excitation in 1D) that do not breed further (CHECKED).
- Excitations also leave 0.6–1.9 vacuum-content records along their path before being recorded.

### 3.8 Comparison with the vacuum ruling (Task 5) (ARGUED; the memory summary only, repo not consulted)

- **The sea is not quiet.** "Vacuum = half-filled staggered sea" has full-rank local marginals (3.5, n4). Every nonzero local linear rule forms records in it at a positive rate, so it is not a quiet vacuum.
- **"Tick = formation rate" needs a noisy vacuum.** Read literally in empty space, the ruling requires a nonzero vacuum formation rate. Lanes M and G show that this freezes every region (A4) and screens clock potentials (A6).
- **Normal-ordering formation above the sea is not available with strictly local weights.** A nonlocal weight would break requirement (iii) and the strict cone (A5, T1.2).
- **What reconciles them:**
  - accept a small, nonzero vacuum rate, bounded below by the table in 3.6;
  - use quasi-local, energy-absorbing weights (3.6, reach R); or
  - change the vacuum to a frustration-free one, which a Dirac sea is not.
- **"Pointer basis".** Under 3.2(d), the pointer basis must be set by records or the law, not by the sea's state.
- **"Source T₀₀ = ε_v".** In the quiet picture empty space sources nothing, and a uniform ε_v is A6's constant mode. With an energy-based weight, the sea's vacuum formation rate equals its frustration energy density, so the ruling's two clauses would then be the same quantity. This is speculative.

## 4. Checks

All runs used `nice -n 10` with OMP, OPENBLAS, VECLIB and MKL thread caps at 1, one job at a time. Load stayed about 3.

| Script | What it does | Key numbers | Time, memory |
|---|---|---|---|
| `sig_toy.py` | 3000 random 4-qubit snapshots; distant menu: none, Z, X or random | Linear rules: max change 7.8e-16 (chance), 4.4e-16 (joint), 7.8e-16 (two-tick); tolerance 1e-14. Nonlinear: squared 0.092; impurity 0.40; product 0.082; two-tick without update 0.042; neighbour-set menu 0.47. Non-vacuity: mean trace distance between Z and X branches 0.53 | 2 s, 60 MB |
| `vacuum_rank.py` | Staggered sea (dense versus k-space, agree ≤ 6.7e-16; L up to 48); antiferromagnet exact diagonalisation; Klein; permanent floor | Massless sea ν = {0.0126, 0.5×5, 0.9874}. Antiferromagnet minimum eigenvalue 7.1e-3 (1D N=16) and 3.4e-4 (2D 4×4). Klein ≤ 4e-19. Product-state symmetric weight ≥ 8.93e-3 | 6.9 s, 168 MB |
| `sea_energy.py` | Energy-based vacuum rates | 0.0122 star, 0.301 bond; m = 0.5: 0.051, 0.317 | 0.3 s |
| `sea_radius.py` | Vacuum rate versus reach R, L = 64 | P₊ idempotent to 3.5e-16; ε(R) table in 3.6 | 0.2 s, 100 MB |
| `lone_hole.py` | Lone-hole floors, 3000 draws per case | As in 3.7(d) | 3.6 s |
| `magnon_toy.py A/B` | 1D ring N = 30, τ = 0.5, c = 1/3, 300 trajectories per case, 3 sublattice passes per tick | As in 3.7; outputs in `magnon_A.out` and `magnon_B.out` | 16 s and 59 s |
| `dark_exact.py` | Deterministic P(never recorded) | Equals \|⟨u\|ψ0⟩\|² within 2.7e-12 | 0.2 s |
| `sampler_check.py`, `dark_check.py` | Monte Carlo against exact | Never-recorded counts within 1.8σ but all on the high side. Sampler shown unbiased: per-pass probabilities identical to the deterministic sequence (difference 0); a 2·10⁵-sample replay agrees within 1.4σ | — |

**Budget breaches:**
- The first `vacuum_rank.py` run peaked at 408 MB. I rewrote it and reran at 168 MB.
- `dark_check.py 700` took 111 s against the 60 s cap (59 MB).
- The inline replay allocated about 0.35 GB. That figure is an estimate; I did not measure it.

## 5. Real-physics match

- **No signalling forces linear event rates.** This matches standard quantum mechanics (COMPARATOR: Gisin 1990, Polchinski 1991 on nonlinear rules signalling). The structure is the same as GRW/CSL flash or collapse theories: linear statistics, and no flashes in the vacuum for mass-density operators (COMPARATOR: Bell 1987, Tumulka 2006, Ghirardi–Pearle–Rimini 1990).
- **Exact quietness is impossible for strictly local detectors in relativistic field theory** (COMPARATOR: Reeh–Schlieder). The lattice analog is EXACT for the Dirac sea.
  - Real detectors are vacuum-quiet only through energy-absorbing, positive-frequency parts, which are quasi-local (COMPARATOR: Glauber photodetection rate ⟨E⁻E⁺⟩).
  - Here the quasi-local version has vacuum rate ∝ R⁻³.
- **If F is the change's own energy, the change is frustration-free.**
  - As I recall the literature, gapless frustration-free systems have dispersion exponent z ≥ 2: Gosset–Mozgunov 2016 in 1D, and Masaoka–Soejima–Watanabe 2024 in general dimension. Verify the exact hypotheses before relying on this.
  - The quantum-dimer Rokhsar–Kivelson point is the canonical example: its emergent photon has quadratic dispersion and zero speed (COMPARATOR).
  - Cross-link, not verified: the memory index records the repo's photon velocity ∝ √(1−V/g), vanishing at RK (#9239).
  - **Falsifier:** photons have z = 1 to high precision. So "exactly quiet vacuum + F = change energy + photons from that change" conflicts with light.
- **Energy-tracking formation decoheres and heats excited matter** in proportion to c·energy, while leaving the vacuum untouched. Collapse-model experiments bound this kind of effect.
- **Gravity.** The source is ∝ energy density only in the dilute regime. Compact bodies saturate at capacity (A6), so mass additivity falsifies it unless sources are transparent.

## 6. Open edges and next steps

1. **Owner choices that need deciding:**
   - which vacuum (frustration-free families versus the sea);
   - whether F is the change's energy;
   - whether recorded neighbours enter F (variant A or B), which decides freezing versus caged excitations;
   - the form of the no-record update (Lüders is the minimal one);
   - the same-tick order for overlapping, non-commuting F's. A5's schedule-independence needs commuting instruments.
2. **Campaign 7, sentence 3,** needs re-reading under a possibility-dependent chance (3.2b), and an explicit no-record update (3.2c).
3. **z = 1 versus quietness.** Does any lattice vacuum with linearly dispersing excitations have rank-deficient star marginals for physical (non-constraint) weights? Gauss-law constraints are quiet but detect only unphysical states. Check the ice/photon lane at and away from RK.
4. **Energy-absorbing multi-tick weights inside the strict cone.** Build them on the 1D sea with ticks and measure the vacuum rate against the window.
5. **Dynamics of the Klein and stabilizer families** with moving excitations, and an LSMOH-type constraint for covariant stepwise changes.
6. **Larger check (not run).** 2D/3D multi-excitation toy with R1 moves to test trail accumulation and the hole-sink source. A6's `g3` with capture odds ∝ e(x) covers the mean-field part.

## 7. Plain-language summary

If the chance that a record forms at a spot depended on that spot's possibilities in any curved, non-proportional way, a menu chosen far away could change how often records appear here. So the chance must be a straight average of one fixed local weighting, and even a tick in which no record forms must nudge the possibilities a little. Empty space then stays perfectly quiet only if its possibilities get zero weight everywhere. That works for some tidy kinds of emptiness, such as all possibilities lined up or every spot paired with one neighbour, but not for the half-filled sea now in the repo, which would keep forming records at a small steady rate. With a quiet emptiness, records form only where something is going on, roughly in proportion to how much. But because the weighting compares neighbours, many of those records lock the plain empty value right beside the disturbance, and some slow, spread-out disturbances are never recorded at all. Calling that weighting "energy" is a further choice, not something the axioms force, and if it is the change's own energy, then the lightest ripples would spread slowly, like waves in a magnet, not like light.