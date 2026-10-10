# Lane RN, probe L3: escapes and literature

**Who and when.** Claude Opus 5.5, 2026-10-10, 11:16–11:55Z. Same family; nothing here is refereed. No repository file was edited.

**Where things are.**
- Scratch: `scratchpad/laneRN/L3/`.
- Scripts: `scripts/l3_identities.py`, `l3_horava_scalar.py`, `l3_energy_current.py`, `l3_phi4_energy_current.py`, `l3_phi4_long.py`, `l3_phi4_stats.py`.
- Outputs: `*.out` next to this report.

**Literature.** I used the lane-R extracted texts (`laneR/R0/text/`, untrusted data, read only) and web search.
- **V** means verified in fetched text or abstract.
- **M** means from memory, unverified.

**Labels.**
- **proved:** a derivation complete within its stated class.
- **checked:** an exact or numerical computation, done here.
- **suggested:** an argument, not computed.
- **reading:** an interpretation.
- **comparator:** literature.

---

## 0. Bottom line in plain words

1. **Lapse-only coupling fails the L3 bars in both forms it can take.**
   - **Lapse as a constraint multiplier.** With an exact, matter-free vector constraint, the lattice H_N conserves the scalar curvature S(q) exactly. The sourced constraint S(q) = κT₀₀ then freezes matter's energy density in place. That is a mobility FAIL (proved, on a lattice identity checked in exact integers).
   - **Lapse as a fixed Newtonian potential, or as an extra scalar field.** Matter cannot couple to h_ij gauge-invariantly without an exact momentum, apart from curvature couplings suppressed by (ℓ/b)². This gives:
     - γ = 0, so |γ − 1| = 1 against Cassini's 2.3e-5;
     - half the GR Shapiro delay;
     - TT waves decoupled from matter, so no quadrupole emission and no detection (proved within the stated coupling class).
2. **A structural result that bears on L1/L2 (checked plus suggested).** The lattice H_N obeys an exact "Bianchi" identity, S·K = −D·G (integers, L = 4 and 5). It forces the shift's matter source to be the matter's **energy current** divided by J, up to a curl. A first-class lapse-and-shift coupling then needs the **total energy current to be conserved**, up to the time derivative of a local sum.
   - By Mazur's bound, that means ballistic heat transport (nonzero thermal Drude weight).
   - Free and integrable lattice matter has it (checked: XX, XXZ, transverse Ising).
   - Generic interacting lattice matter does not:
     - checked: XXZ with next-nearest-neighbour terms, and tilted Ising;
     - checked, classical, L = 8: 3D onsite φ⁴. Its current autocorrelation decays to about 0, while the free value stays exactly 1.
   - If this holds up, K3a's obstruction is not a defect of the stress search. It is "interacting lattice matter conducts heat diffusively (umklapp)". It would also cover every local or quasi-local stress, not only K3a's tested class.
3. **Defect matter is the one escape that removes the exact-momentum problem by construction,** because the stress is the tensor field's own rate of change Ė. Its kinematics is not the decisive failure:
   - vector charges are lineons (Pretko, V), and scalar "mass" defects are fractons (checked);
   - a composite of the two moves along its vector charge at v = Jq/σ (exact identity).

   Read with vector charge = momentum, this is just conservation of momentum and angular momentum (Pretko's own reading, V). In a continuum toy with one speed (c_matter = c_TT), light-like composites even come out with γ = 1 (suggested).

   Where it fails or stays open:
   - **Universality.** The gravitational charge is a conserved topological scalar charge of either sign, not energy (Gu–Wen, V). Field and binding energy carry none.
   - **Stability.** Dynamical defects need finite gaps, and finite gaps on H_N leave an indefinite scalar sector unbounded below (the landed 09-14 note, proved for the Gaussian comparator).
   - **Compactness.** Point defects need compact variables, while linear dispersion needs non-compact H_N.
4. **Smaller gauge groups do not escape.** TDiff, unimodular and Hořava (projectable and healthy non-projectable) all keep local spatial diffeomorphisms, so they still need [H,P] = [H,L] = 0 (proved; this is the K3a criterion). They add a scalar graviton:
   - in TDiff, it brings scalar–tensor bounds (V);
   - in projectable Hořava, it is a ghost for c > ½, tachyonic for c < ½, and has no kinetic term at c = ½, i.e. it is strongly coupled (checked on the lattice symbol; matches Blas–Pujolas–Sibiryakov and Koyama–Arroja, V).
5. **Literature.** Exact lattice Ward identities for translations are not available for interacting theories:
   - lattice energy–momentum tensors are defined by imposing continuum Ward identities up to O(a) (Caracciolo et al., Giusti–Pepe, V);
   - the Kato–Sakamoto–So no-go (V) says no lattice difference operator and product are translation-invariant, local and Leibniz at once, which is the algebraic root of Noether's failure;
   - the SLAC derivative restores exactness at the price of non-locality.

**Against the L3 bars:**

| Escape | Bars it fails |
|---|---|
| Lapse-only | fails γ and Shapiro (fixed-potential form), or mobility (multiplier form) |
| TDiff, unimodular, Hořava | escape nothing on momentum; Hořava adds a pathological scalar |
| Defect matter | does **not** fail γ, Shapiro or mobility at the level computed; fails universality (gravitational charge ≠ energy) and stability (finite gaps) on the Gaussian comparator. That is not an L3 observational bar, so this escape is **INCONCLUSIVE**, leaning FAIL |

---

## 1. Task 1: lapse-only coupling

### 1a. The lattice identity (checked)

Use the 09-14 integer stencils on an L³ torus:
- G from the note, lines 95-97;
- S from lines 98-100;
- canonical slots q, p;
- the DeWitt kinetic map at c = ½: q̇_ii = J(p_ii − ½ tr p), q̇_ij = 2J p_ij for i ≠ j;
- D, the backward divergence from edges to sites.

`l3_identities.py`, in exact integers at L = 4 and 5:
- G Sᵀ = 0;
- **S K + D G = 0 exactly**, so the evolution gives Ṡ(q) = −J D G(p), for any lapse and shift. The lapse term moves only p, and S Gᵀ = 0;
- for c = 0, ⅓ or 1, the rows of S K leave the row space of G (rank excess 63 at L = 4). Only c = ½ is weakly invariant, as R1's referee said.

I derived the same identity by hand: S K p = −J[Σ_j Δ_j p_jj + 2Σ_{i<j} ∂_i⁻∂_j⁻ p_ij] = −J Σ_j ∂_j⁻(Gp)_j.

### 1b. Lapse as a multiplier, with the vector constraint matter-free (proved, given 1a)

Take H = H_N + H_m + ∫n(S q − κT₀₀) + ∫n_j (G p)_j, with matter that does not depend on p.
- Then S(q̇) = −J D G p ≈ 0, so S(q) is exactly constant in time.
- The constraint then forces T₀₀(x, t) = S(q)/κ, constant in time, at every site. This holds for any lapse.
- Matter whose coupling does involve p (an "E-coupled" matter current K) gives ∂_t T₀₀ = S(K)/κ. Sᵀ annihilates exactly the affine functions (checked, polynomial degree ≤ 3), so the energy dipole is conserved and the centre of energy is frozen.
- Either way, the total energy current is zero and matter cannot carry momentum.
- Adding ½h_ij T_ij with G matter-free is no better: preserving G then forces div T ≈ 0.

**Mobility bar: FAIL.**

### 1c. Lapse as a fixed potential (Poisson n, or a new scalar field)

**Gauge-invariant h-couplings.** Under h → h + Gᵀξ, the coupling ∫h:X is invariant for all states only if X is identically divergence-free. Locally that means X = R(Y), with R the linearized incompatibility. This is the Beltrami stress-function representation of divergence-free symmetric tensors: comparator, M; on the lattice G R2 = 0 is landed, but exactness of the complex was not checked here.
- So the only allowed h-coupling is ∫R(h):Y, with two extra derivatives.
- Outside a static mass R_ij ∝ GM/r³, so the effect on light is suppressed by (ℓ/b)². With ℓ at the lattice scale and b = R_sun, that is about 1e-87 (suggested).

**PPN (proved within the class).**
- Matter feels only n. A massless field has ω = (1 + n)|p|, so the deflection is 2GM/b (Soldner's value) and γ = 0.
- Cassini (Bertotti–Iess–Tortora 2003, M) measures γ − 1 = (2.1 ± 2.3)e-5. The miss is a factor of about 4e4.
- The Shapiro delay is (1 + γ)/2 = ½ of GR's.
- For comparison: a scalar coupled to the trace T (Nordström) gives γ = −1, since light decouples.

**TT waves.**
- The scalar constraint involves only the trace and longitudinal parts of h, so the TT modes see matter only through R(h):Y. The amplitude is suppressed by (ωℓ)² and the power by (ωℓ)⁴.
- Hence:
  - no quadrupole emission, while Hulse–Taylor gives 0.9983 ± 0.0016 of GR (M), and the double pulsar agrees with GR to 1.3e-4 (M);
  - no LIGO detection.
- A dynamical scalar n would add a gapless scalar coupled at gravitational strength, which the wall target forbids.

**γ and Shapiro bars: FAIL. The quadrupole requirement fails too.**

---

## 2. The identity's consequence for every lapse+shift coupling (checked plus suggested)

### 2a. The derivation (suggested; it uses only 1a)

Add the shift coupling G p ≈ κ′π, with the matter momentum π on G's edges. Preserving C_s = S q − κε at first order gives

  Ċ_s ≈ −Jκ′ D π + κ D j_E ≈ 0  ⇒  π = (κ/(Jκ′)) j_E + w,  with D w = 0.

- Here j_E is the local energy current, ε̇ = −D j_E. A local current exists for any local H (Kapustin–Sopenko local Noether, M).
- **Cohomology step (suggested, not proved here).** A translation-covariant local edge field with D w = 0 is a curl plus a c-number, so Σw is a c-number.
- Preserving G − κ′π gives π̇ = −(1/2κ′) G T, so Σπ is conserved, and therefore Σ j_E is conserved.
- Changing the energy density by ε → ε + D v shifts J_tot by −V̇. The exact condition is therefore:

  **∃ local V such that P := J_tot − V̇ is conserved and is the momentum.**

### 2b. Mazur's bound (suggested)

- ⟨P J_tot⟩ = ⟨P²⟩, because ⟨P V̇⟩ = 0 in a stationary ensemble.
- So the thermal Drude weight satisfies D_th ≥ ⟨P²⟩/Vol, which is positive for a physical momentum.
- **First-class lapse and shift coupling to the lattice H_N therefore implies ballistic energy transport.**
- In continuum relativistic QFT this is automatic: T⁰ⁱ = Tⁱ⁰ and momentum is conserved. On a lattice it is the integrability-type property that umklapp destroys (Peierls).

### 2c. Checks

**1D quantum, L = 10, periodic** (`l3_energy_current.out`). The table gives ‖[H, J_E]‖ in normalized units.

| Model | ‖[H, J_E]‖ |
|---|---|
| XX (free) | 0 |
| XXZ, Δ = 0.6 (integrable) | 5e-17 |
| transverse Ising (free fermions) | 3e-17 |
| XXZ + NNN | 0.40 |
| tilted Ising | 0.33 |

This agrees with Zotos–Naef–Prelovšek (V: in integrable chains the energy current is tied to the first conservation law).

**3D classical onsite φ⁴, L = 8, m² = 0.5, T = 1** (`l3_phi4_energy_current.out`). The quantity is C(t) = ⟨J(t)·J(0)⟩/⟨J²⟩.

| λ | Result |
|---|---|
| 0 | exactly 1 (conserved) |
| 0.5 | 1 → 0.30 (t = 150) → −0.05 ± noise (t = 300–400) |
| 2 | tail mean over [75, 150] = 0.12 ± 0.11 |
| 4 | tail mean over [75, 150] = −0.16 ± 0.08 |

The energy drift is ≤ 6e-5. The interacting tails are consistent with D_th ≈ 0, within weak statistics (24 trajectories) and one small box. This is classical, not quantum; L2 has the quantum models.

### 2d. Reading

- If the cohomology step and D_th = 0 both hold, then:
  - onsite φ⁴ in 3D admits **no** first-class linear lapse+shift coupling to H_N with **any** local or quasi-local stress or energy density;
  - the same goes for any non-integrable lattice matter.
- That is stronger than K3a's bounded class. Two things stay open:
  - the zero Drude weight is numerical and finite-size;
  - the Mazur step needs P to have extensive thermal fluctuations.
- L1 should check that its free-field stress coincides with j_E/J. L2 can use [H, J_tot] ≠ 0 (projected per Mazur) as a stress-independent screen.

---

## 3. Task 2: matter as defects of the tensor field

### 3a. Mobility

**Vector (electric) charges ρ_j = ∂_iE_ij (comparator, V).** These are Pretko 1604.05329 §III. ∫ρ and ∫x×ρ are conserved because E is symmetric (eq. 9), and Pretko reads them as "linear and angular momentum".
- The charges are "one-dimensional particles … restricted to motion only along their charge vector". A bound x+y pair hops along (1,1,0).
- The traceless vector theory adds ∫x·ρ = 0 (eq. 11) and makes the charges "fully fractonic".
- Rank-2 magnetic vector defects are lineons too.

My check (`l3_identities.py`, polynomials up to degree 3): ker Gᵀ = rigid motions (dimension 6), so lineons.

**Scalar (magnetic) defects σ = S(h).** These are Gu–Wen's "point mass" (V: 0907.1203, "violation of this constraint at one point corresponds to a scalar charge which can be interpreted as a point mass").
- ker Sᵀ = affine functions (dimension 4): charge and dipole are conserved under any compact move. They are **fractons** (checked).
- **Under H_N** (checked through 1a): ∂_tσ = −J D ρ + S(K), and d/dt ∫xσ = J∫ρ exactly. The centre of σ moves at J Q/M_σ.
- So a composite of σ plus vector charge q moves along q at v = Jq/σ. This is the lattice centre-of-energy theorem.
- Comparators:
  - Pretko 1702.07613 (Mach reading, V);
  - fracton ↔ Carroll dictionary, Figueroa-O'Farrill–Pérez–Prohazka JHEP 06 (2023) 207 (V);
  - dislocation glide along the Burgers vector, Pretko–Radzihovsky PRL 120, 195301 (V).

**Reading.** If q is momentum and σ is energy, the restrictions are Newton's first law plus momentum and angular-momentum conservation. They are not an extra observational problem. The price is an **inertia law**: the vector charge must travel at Jq/σ to stay with its σ. The gauge structure does not supply it; it is matter dynamics (suggested).

### 3b. Energy coupling and γ (suggested; continuum toy, not a lattice computation)

**No lapse coupling.** For defect matter S(h) = σ is an identity, so no lapse term exists. Gravity couples to σ: two scalar defects have cross energy −g m M/(8πr), and like signs attract (09-14 note at lines 290-292; Gu–Wen V: "two masses with the same sign attract and two masses with opposite signs repel").

**The toy's potential.**
- A vector charge q moving at v couples through its current at unit strength, ∫h:T with T_ij = v_i q_j. The Gauss law fixes that coefficient, and the gauge part of h drops out as a total time derivative.
- The static field is h = fδ + (gauge), with f = −M/(8πr). So the toy potential is U = f(gσ + q·v) = Φσ(1 + v²/(gJ)), using q = σv/J and Φ = g f.
- GR's test-particle form is EΦ(1 + γv²).
- With c_TT² = Jg, this gives **γ = c_TT²/c_matter²**, so γ = 1 when the speeds match. GW170817 (M) bounds that mismatch at about 1e-15.

**Assumptions.**
1. The inertia law q = σv/J.
2. Light is itself a σ+q composite.
3. Linear order.

**Within the toy, the γ and Shapiro bars are not failed.**

### 3c. Where defect matter fails or stays open

**(i) Universality (suggested).** σ is a conserved topological charge of either sign, created in neutral sets by local operators.
- Smooth field energy has S(h) = 0, so binding and field energy carry no σ unless every energy carrier is itself a defect.
- The inertial mass is M_σ/J (from 3a), whatever the internal energy. Internal kinetic energy enters the passive mass through h:T.
- So the expected WEP violation is of order the internal-energy fraction differences between materials, about 1e-4 to 1e-3. MICROSCOPE bounds it below 1e-15 (M).
- Negative-σ excitations exist. ALPHA-g (M) finds antihydrogen falls down, though anti-defects need not be antimatter.

**(ii) Stability (proved in the landed note, Gaussian comparator only).** Dynamical defects need finite Gauss-law gaps, like the gapped spinons that keep the spin-ice photon protected (Hermele–Fisher–Balents, V via R0).
- Finite penalties U|G|² + V S² on H_N give det K = −J²/2 < 0 and a nilpotent Jordan chain, for **every** finite U (09-14 note, lines 260-278).
- So a gapped-defect Gaussian H_N is unbounded below in the scalar sector. The note limits this to the Gaussian, not the full compact phase.

**(iii) Compactness tension (suggested).**
- Quantized point defects of S(h) need compact h, as in Gu–Wen's lattice model.
- The landed note shows regular compact characters give O(k³) (lines 186-216), and H_N "is not a periodic function of each local compact coordinate" (lines 79-83).
- In a non-compact theory, σ must be supplied as matter, S(h) = κT₀₀. That puts the route back into §1–2.

**(iv) The Standard Model as defects** is not shown, and no paper found does it (comparator search, not a theorem).

**Mobility bar: not failed** (lineon and fracton are consistent with the conservation laws, given the inertia law). **γ bar: not failed** in the toy. **Lane reading for this escape: INCONCLUSIVE, leaning FAIL** on universality and stability.

---

## 4. Task 3: smaller gauge groups

### 4a. TDiff (∂_μξ^μ = 0) and unimodular (WTDiff)

**The condition (proved, one line).** Invariance of h_μν T^μν needs ∂_μT^μν = ∂^νΦ.
- Spatially, ∫∂_jΦ = 0 and ∫x×∇Φ = 0, so total P and L must still be exactly conserved. That is the same K3a criterion ([H,P] = [H,L] = 0).
- Equivalently, T′ = T − ηΦ is exactly conserved.
- Umklapp breaks total P, so TDiff does not help.

**Comparators.**
- Unimodular gravity tolerates only exact-form violations J = dΦ, which accumulate into an effective Λ (Josset–Perez–Sudarsky PRL 118, 021102, V). That relaxes energy, but our lattice H already conserves energy. The missing piece is momentum.
- Non-Weyl TDiff carries "an additional scalar degree of freedom" with scalar–tensor and equivalence-principle bounds (Álvarez–Faedo–López-Villarejo JCAP 0907:002, V).

### 4b. Hořava, projectable: lapse N(t) only

- Spatial diffeomorphisms stay local, so the momentum constraint still needs an exact local matter momentum. This is K3a, and §2 applies to its shift part.
- With no local scalar constraint, the transverse trace scalar becomes physical.
- **Checked on the symbol** (`l3_horava_scalar.out`; vector constraint and gauge kept, kinetic E:E − c(trE)²): ω²_scalar = −(1 − 2c) Jg k², while the TT pair stays at +Jg k².
  - c < ½ (Hořava λ > 1): tachyonic.
  - c > ½ (⅓ < λ < 1): a ghost, with kinetic and potential terms both negative.
  - c = ½ (λ = 1): no kinetic term. This is the 09-14 Jordan chain, i.e. strong coupling.
  - The map is c = λ/(3λ − 1).
- **Literature agrees (V):**
  - ghost-like for ⅓ < λ < 1, tachyonic for λ > 1 (1007.1006);
  - strong coupling as λ → 1 (Koyama–Arroja JHEP 2010; 1104.2087);
  - caustics and a very low strong-coupling scale (Blas–Pujolas–Sibiryakov JHEP 0910:029).
- PPN is then not perturbatively computable near λ = 1.

### 4c. Hořava, healthy non-projectable (Blas–Pujolas–Sibiryakov 2010, M)

- γ = β = 1, but α₁ and α₂ are constrained.
- It still has local spatial diffeomorphisms, so it still needs the exact local momentum.

### 4d. Summary for Task 3

- Every group that keeps local spatial diffeomorphisms needs the exact momentum.
- Dropping them makes the helicity-±1 and 0 parts of h physical. That is the Stückelberg or Lorentz-violating massive-gravity sector (Dubovsky 2004, M), which is R2's μ_E and μ_T2 territory.
- None of these is an escape.

---

## 5. Task 4: literature

**Lattice energy–momentum tensors.**
- Caracciolo–Curci–Menotti–Pelissetto, Ann. Phys. 197 (1990) 119 (V, abstract) build T_μν by imposing the Ward identities "perturbatively and non-perturbatively".
- Giusti–Pepe, PRD 91, 114504 (2015) (V): the lattice breaks translations "down to discrete subgroups". T_μν is a combination of operators up to dimension 4, tuned so continuum Ward identities hold "up to cutoff effects". The singlet, 3 and 6 parts renormalize separately. Shifted boundary conditions are used.
- Dalla Brida–Giusti–Pepe, JHEP 04 (2020) 043, extend this to QCD (V).
- Suzuki, PTEP 2013 083B03 (gradient flow) gives a universal formula valid as a → 0 (M).
- Del Debbio–Patella–Rago 1306.1173 give translation Ward identities along the flow (V).
- **None gives an exactly conserved interacting lattice T_μν at finite a.** This is consistent with the K3a referee's reading (an absence, not a theorem).

**The algebraic root.** Kato–Sakamoto–So 0803.3121 (V, abstract): no lattice difference operator and product can be translation-invariant, local and Leibniz at once, with or without associativity. A local product forces a non-local difference.
- Noether's translation current needs Leibniz, so this explains generically why interacting lattice momentum is not exactly conserved (reading).
- Escapes named there: infinite flavours, or matrix formulations.

**The SLAC derivative** (Drell–Weinstein–Yankielowicz 1976, M) is exact k in the zone but decays as 1/r. Karsten–Smit (1979, M) found non-covariant, non-local counterterms with gauge interactions. **Perfect actions** (Hasenfratz–Niedermayer 1994, M) are quasi-local and classically perfect only. I know of no exactly conserved interacting momentum for them (M).

**Integrable lattice models.** These are the known exact cases (Zotos–Naef–Prelovšek, V): the energy current is conserved, giving ballistic heat. I know of no interacting integrable lattice model in 3D with this property (M; search not done).

**Gu–Wen's matter coupling** (0907.1203, V):
- "In Einstein gravity, the mass of matter is coupled to gravity via a modification of constraint." Their matter is violations of R_ii = 0, i.e. defects.
- The N-type model gives an m₁m₂/r² force: same signs attract, opposite signs repel.
- They give no separate matter field and no stress coupling.
- R0 notes Gu–Wen themselves call N-type "not reliable" (V).

---

## 6. Against the fixed readings (L3 bars: γ, Shapiro, mobility)

| Escape | γ | Shapiro | Mobility | Other | Reading |
|---|---|---|---|---|---|
| Lapse multiplier, vector constraint matter-free | n/a (matter frozen) | n/a | **FAIL**: T₀₀ frozen, or energy centre frozen (proved) | — | FAIL |
| Lapse as fixed or Poisson potential | **FAIL**: γ = 0 vs 2.3e-5 (proved in class) | **FAIL** (½ GR) | ok | no TT emission or detection; a dynamical n is an extra gapless scalar | FAIL |
| Defect matter (VS/H_N) | ok in the toy if c_matter = c_TT (suggested) | ok (same factor) | ok given an inertia law (checked identities, V Pretko) | universality (σ ≠ energy) and finite-gap instability (09-14, Gaussian) | INCONCLUSIVE, leaning FAIL |
| TDiff / unimodular | GR-like if WTDiff; scalar–tensor bounds otherwise (V) | same | n/a | still needs [H,P] = [H,L] = 0 (proved) | no escape |
| Hořava projectable | not perturbative near λ = 1 | — | n/a | ghost, tachyon or strong coupling (checked, V); still needs exact momentum | no escape |

**L3 contribution to the lane's FAIL clause.** "The escapes tested in L3 fail an observational bar" holds for **lapse-only** (γ and Shapiro, or mobility). It does **not** hold for defect matter, which fails on universality and stability instead. Smaller gauge groups are not escapes from the momentum requirement.

**Against the supervisor expectation.**
- "Lapse-only fails Cassini": confirmed (γ = 0). The multiplier form fails on mobility instead.
- "Defect matter is restricted in mobility": **not confirmed** as a failure. The restriction equals the momentum and angular-momentum conservation laws. The real problems are universality and stability.

## 7. Strong-word check

- **"Proved"** is used only for:
  - §1b (from the identity);
  - §1c (within the stated coupling class);
  - §4a (one-line integration).
  The 09-14 finite-penalty result is that note's, within the Gaussian.
- **"Checked"**:
  - exact integer identities at L = 4 and 5, plus the hand derivation for general L;
  - polynomial kernels up to degree 3;
  - the Hořava symbol;
  - the 1D commutators;
  - the 3D classical φ⁴ autocorrelation, which is noisy, finite-size and classical.
- **§2 is "suggested".** The cohomology step and the Mazur step are argued, not proved. D_th = 0 for non-integrable 3D matter is numerical evidence and the standard belief, not a theorem.
- **The §3b result γ = 1 is a continuum toy** that rests on an assumed inertia law.
- **"No paper found" and "I know of none"** are search or memory statements, not theorems.

Sources: [Kato–Sakamoto–So 0803.3121](https://arxiv.org/abs/0803.3121), [Giusti–Pepe 1503.07042](https://arxiv.org/abs/1503.07042), [Caracciolo et al. (INSPIRE)](https://inspirehep.net/literature/26646), [Dalla Brida–Giusti–Pepe JHEP04(2020)043](https://link.springer.com/article/10.1007/JHEP04%282020%29043), [Del Debbio–Patella–Rago 1306.1173](https://arxiv.org/abs/1306.1173), [Zotos–Naef–Prelovšek cond-mat/9611007](https://arxiv.org/abs/cond-mat/9611007), [Álvarez–Faedo–López-Villarejo 0904.3298](https://arxiv.org/abs/0904.3298), [Blas–Pujolas–Sibiryakov 0906.3046](https://arxiv.org/abs/0906.3046), [Koyama–Arroja 0910.1998](https://arxiv.org/abs/0910.1998), [projectable HL perturbations 1007.1006](https://arxiv.org/abs/1007.1006), [HL λ→∞ 1104.2087](https://arxiv.org/abs/1104.2087), [Josset–Perez–Sudarsky 1604.04183](https://arxiv.org/abs/1604.04183), [Pretko–Radzihovsky 1711.11044](https://arxiv.org/abs/1711.11044), [Figueroa-O'Farrill–Pérez–Prohazka 2305.06730](https://arxiv.org/abs/2305.06730), [Bidussi et al. SciPost 12, 205](https://scipost.org/SciPostPhys.12.6.205); Pretko 1604.05329, 1702.07613 and Gu–Wen 0907.1203 read from `laneR/R0/text/`.
