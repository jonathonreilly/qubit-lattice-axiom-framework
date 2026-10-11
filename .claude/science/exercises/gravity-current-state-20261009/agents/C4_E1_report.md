# C4 lane RE, probe E1: emergent Lorentz invariance from strong dynamics (theory and literature)

**Worker:** Claude Opus 5.5 (same family as the supervisor). **Not refereed.** Run 2026-10-11, 16:54Z to about 17:20Z.

**Labels:**
- **proved:** an argument complete under the stated assumptions.
- **checked:** a script or exact algebra in scratch.
- **suggested:** an argument that is not complete.
- **reading:** an interpretation.
- **comparator:** a literature statement. Where it is marked "fetched", it was verified against fetched text (an arXiv abstract or ar5iv full text, read through a summarizing fetch tool). Where it is marked "memory", it was not re-verified.

**Scratch:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/E1/`
- `e1_checks.py/.out`: representation theory, unitarity floors, running exponents, suppression and stiffness arithmetic.
- `e1_ct_weighting.py/.out`: sympy check of Anber–Donoghue's speed beta functions.

No repository file was edited, and nothing was downloaded to disk.

## Plain summary

**Matter.** At a strongly interacting fixed point, differences between the speeds of different matter species can die away as a power of energy.

The overall speed of light of one interacting sector is not a tunable number at all. Deforming by δc·T₀₀ is exactly marginal and **redundant**: it only changes the time unit (proved).

So the question "the stress tensor's dimension is protected; how can speed LV become irrelevant?" has a clean answer:
- A *common* speed couples to the conserved total T. It is protected, but it is unphysical.
- A *relative* speed couples to a non-conserved spin-2 operator, the orthogonal combination of the sector stress tensors. If the sectors interact, unitarity forces its dimension strictly above 4, so it is irrelevant.
- If the sectors are decoupled, or coupled only through an irrelevant coupling, every sector keeps its own conserved T. The relative speed is then exactly marginal and **frozen**.

**What protection forces on elementary fields.** The same protection fixes how fast strong dynamics can drag an elementary field's speed:
- a scalar or fermion mixing with a composite operator: power law, possible;
- a gauge field coupled to a conserved current: only logarithmic, because Δ_J = 3 is protected;
- the graviton coupled to T: not at all, because κ is irrelevant.

**Gravity.** Strong matter dynamics therefore cannot fix:
- the graviton's speed relative to matter;
- the TT stiffness (graviton mass). This is a UV-dominated, relevant, vacuum-energy-like contact term. Emergent Lorentz invariance in the infrared changes it only by a factor 4/(4+γ). Its tuning need, about 1e-101 (P0), is of the same kind as the cosmological-constant problem.

**Matter, quantitatively.** The best mechanism is a single strongly coupled sector, from the lattice scale down to an exit scale Λ_s ≈ 1–100 TeV, with all SM fields composite or dual. It needs a least-irrelevant exponent γ ≳ 1.5 to meet the matter bounds; the 1e20 eV proton bound needs up to 2.8 for one sign.
- Literature exponents range from 0.7 (BPS 2013) to 1–2 (Baggioli–Pujolàs–Wu 2024, holographic).
- No lattice realization is known, and there is no controlled non-SUSY example of a weakly coupled SM gauge sector emerging from such a stage.

**Reading.** E1 = **FAIL (bounded)**, on the TT stiffness and the graviton speed. It is a conditional partial win for matter speeds: in principle, that cuts F2's 1–9 matter speed tunings to 0.

## 1. Literature

| Source | What becomes irrelevant, and how fast | Conditions | Verification |
|---|---|---|---|
| **Bednik–Pujolàs–Sibiryakov 2013**, JHEP 11 (2013) 064, arXiv:1305.0011 | **Sec. 1:** the only exactly marginal two-index operator is T_μν, and it "can be absorbed by the rescaling of the time coordinate". Operators with more than two indices are automatically irrelevant. The dangerous ones are vector operators with d−1 ≤ Δ ≤ d. **Sec. 4:** δc ∝ (Λ/Λ*)^{Δ−d}, with Δ the dimension of the least irrelevant LV operator. **RS model:** suppression (LΛ)^{2(1−ν)}, logarithmic at ν = 1. **Lifshitz flows:** (Λ/Λ*)^{2α} with α ≲ 0.35 in d = 4, so the exponent is ≲ 0.7, "not very strongly suppressed" | Emergence needs the inter-sector coupling to be **relevant**. For an irrelevant coupling the sectors decouple and LV persists. SM fields must be "(partially- or completely-) composite". Elementary gauge fields are suppressed "only logarithmically", which the authors call a "serious obstruction" and leave open. LV in gravity can be sizable; they suggest combining with SUSY or scale separation | comparator, fetched (ar5iv full text) |
| **Baggioli–Pujolàs–Wu 2024**, "Holographic Lifshitz flows", JHEP 09 (2024) 175, arXiv:2407.11552 | δc ∝ (E/Λ)^κ, with κ = Δ − 4 of the least irrelevant LV operator (a Proca operator). Earlier models had κ ≲ 0.35. A quartic Proca self-coupling of order 10–20 pushes κ to 1–2. Larger z_UV recovers Lorentz invariance faster. On the Lifshitz critical line the operator is exactly marginal and κ = 0 | Bottom-up holography; no SM; no gravity completion | comparator, fetched |
| **Anber–Donoghue 2011**, PRD 83, 105027, arXiv:1102.0789 | One-loop speed beta functions for Yukawa and QED (equations extracted, §2d). The equal-speed line is IR-attractive (Jacobian eigenvalue 7g²/24π²). The approach is **logarithmic**: a 10% difference needs about 10^(10¹³) GeV of running. A power law appears only with power-law thresholds of huge numbers of species (N_g ≈ 1e9 hidden U(1)s), or N_f ≈ 120, N_g ≈ 900 for 1e-14. Gravity, the weakest coupling, keeps the largest difference | Weak coupling; species counting | comparator, fetched |
| **Chadha–Nielsen 1983**, Nucl. Phys. B217, 125 | The original "Lorentz invariance as a low-energy phenomenon": logarithmic attraction | Weak coupling | Citation fetched; content from memory, and reproduced as the weak-coupling limit in §2d |
| **Iengo–Russo–Serone 2009**, JHEP 11 (2009) 020, arXiv:0906.3477 | In Lifshitz-type scalar theories, c² and δc² run logarithmically. Lorentz invariance is not recovered unless the UV LV parameters are fine-tuned | Weakly coupled Lifshitz | comparator, abstract fetched |
| **Kostelecký–Lane–Pickering 2002**, PRD 65, 056006, arXiv:hep-th/0111123 | Lorentz-violating QED is one-loop renormalizable. (β_c)_μν = (q²/6π²)(c_μν + c_νμ − (k_F)_μα ν^α). All running goes through Q(μ) = 1 − (q₀²/6π²) ln(μ/μ₀), and the mixed combination falls like Q⁻³. a_μ and b_μ run only through mass-dimension-1 mixing | Weak coupling | comparator, fetched. Q⁻³ reproduced in §2d (checked) |
| **Kharuk–Sibiryakov 2015**, arXiv:1505.04130 | Holographic flows from Lorentz-violating UV to approximately Lorentz-invariant IR, with chiral fermions emerging | Strong coupling | comparator, abstract only; exponents not extracted |
| **Kiritsis 2012**, arXiv:1207.2325 | LV couplings must be fields of the gravitational sector. Cherenkov-type dissipation is generic for LV | Holography | comparator, abstract fetched |
| **Isobe–Nagaosa 2012**, PRB 86, 165127 | 3+1D QED in solids: the electron velocity v and c flow to a common value, with c²v nearly unrenormalized. The coupling is marginal (IR-free), so the approach is logarithmic | Weak coupling, Gaussian fixed point | comparator, search-level summary of the abstract |
| **Roy–Juričić–Herbut 2016**, JHEP 04 (2016) 018, arXiv:1510.07650 | GNY (and GNY + U(1)) with ε = 3 − d spatial. **d = 2:** v_F and v_B flow to the speed of light for any initial values; the velocity difference is an irrelevant perturbation with g*² ∝ ε. **d = 3:** all velocities, including c, flow to a common **non-universal** terminal value | One-loop ε-expansion | comparator, fetched. No explicit exponent is printed. The extractor's linearization of the stated equations gives a rate ∝ g*²(1 + 3N_F)/3 (unverified normalization) |
| **QED₃, large N:** Vafek–Tešanović–Franz 2002 (cond-mat/0203047); Hermele et al. | Dirac velocity anisotropy is irrelevant: dκ/ds = −32/(5π²N_f)(κ − 1), as quoted in the lattice paper hep-lat/0412009, which does not name the source. Concha–Stanev–Tešanović (0906.1103) agree, by a subtler mechanism. **Lattice dissent:** Hands et al. find κ_ren > κ, i.e. anisotropy relevant at accessible N | Large N; O(1/N) exponent | comparator, search-level. Contested |
| **Grozdanov et al.** | Not located. No paper by Grozdanov on emergent Lorentz invariance or Lorentz-violating RG flows was found in two searches. Possibly a misattribution; the nearest are Kiritsis 2012 and Baggioli–Pujolàs–Wu 2024 | — | not found |
| **Unitarity bounds:** Mack 1977; Minwalla 1998 | For a 4D unitary CFT: (j₁,j₂) with j₁j₂ ≠ 0 have Δ ≥ j₁ + j₂ + 2, with equality only if conserved; (j,0) has Δ ≥ j + 1 | — | comparator, memory |
| **3D Ising on a cubic lattice** | Rotation invariance emerges because the leading spin-4 operator has Δ ≈ 5.02, so ω_rot ≈ 2.0 | — | comparator, memory |
| **Weinberg–Witten 1980** | No massless spin-2 particle can carry a Lorentz-covariant, conserved T_μν with nonzero one-particle matrix elements | — | comparator, memory |

**What the literature agrees on (reading).**
- Power-law emergence needs: (i) a strongly coupled, **interacting** fixed point with a single stress tensor; (ii) a **relevant** coupling between the sectors whose speeds must agree; (iii) an empty "vector window", meaning no unforbidden spin-1 operator with 3 ≤ Δ ≤ 4.
- Weak coupling, including every Gaussian 3+1D quantum critical point (Isobe–Nagaosa, GNY at d = 3), gives only logarithms.
- The measured exponents run from O(ε) or O(1/N) in condensed matter, through ≲ 0.7 (BPS), to 1–2 (BPW 2024, with an order-10 bulk quartic).

## 2. Theory: which Lorentz-violating deformations of a Lorentz-invariant IR fixed point can be irrelevant

### 2a. The crux: is δc·T₀₀ exactly marginal? Yes, and it is redundant (proved, standard)

**Setting.** Take a Lorentz-invariant QFT (in particular a CFT) defined covariantly on background metrics, with T^μν = (2/√g) δS/δg_μν.

**Step 1.** The family S_ε = S[g(ε)], with constant g(ε) = η + 2ε e₀e₀, starts as S + ε∫T₀₀ to first order. It is mapped onto S[η] exactly by the linear diffeomorphism x⁰ → (1+2ε)^{1/2} x⁰.

**Step 2.** So every member of the family is the same theory with a different time unit. The beta function of ε vanishes identically: ε is exactly marginal and **redundant** in Wegner's sense. This matches the protected dimension Δ_T = d.

**Consequence.** The speed of light of one interacting sector is a unit, not a coupling. No tuning is ever needed for it. BPS state the same (Sec. 1, fetched).

**Several sectors.** Suppose S = S₁ + S₂ + g∫O₁O₂.

- **g = 0, or g irrelevant in the IR (decoupled).**
  - T₁ and T₂ are separately conserved, each with Δ = d.
  - The relative speed ε₁ − ε₂ is physical and **exactly marginal**: a line of Lorentz-violating fixed points that no dynamics removes.
  - This is the gravity–matter case (§3b) and any irrelevantly coupled hidden sector. BPS: for an irrelevant coupling "the two sectors decouple, so LV persists".
- **g relevant (Δ₁ + Δ₂ < d), or marginally relevant.**
  - The IR fixed point has one stress tensor, T = T₁ + T₂ + O(g).
  - The orthogonal combination T₋ ∝ C_T₂T₁ − C_T₁T₂ (orthogonal in the two-point function) is a spin-2 primary that is **not conserved**.
  - The 4D unitarity bound for (1,1) is Δ ≥ 4, with equality only for conserved operators. So **Δ(T₋) > 4 strictly**, and the relative speed is irrelevant with exponent γ₋ = Δ(T₋) − 4 > 0. **proved**, given unitarity and a unique stress tensor.

**How big γ₋ is (suggested; checked in two weakly coupled cases).**
- By multiplet recombination, ∂·T₋ = (C_T₁ + C_T₂) ∂·T₁ = O(g).
- Hence γ₋ ∝ ⟨∂T₋ ∂T₋⟩/⟨T₋T₋⟩ ∝ g²·(1/C_T₁ + 1/C_T₂), with unit-normalized O_i.
- Two consequences:
  1. Each sector's speed relaxes at a rate ∝ g²/C_T,i.
  2. The C_T-weighted mean speed is invariant: it is the redundant total-T direction. The terminal speed is therefore the C_T-weighted average.
- **Checked** on Anber–Donoghue's one-loop beta functions (`e1_ct_weighting.out`):
  - Yukawa: the rate ratio boson/fermion is exactly 6 = C_T(Dirac)/C_T(real scalar), and 1·β_b + 6·β_f = 0 exactly at first order.
  - QED: the rate ratio fermion/photon is exactly 2 = C_T(Maxwell)/C_T(Dirac), and 12·β_γ + 6·β_f = 0 exactly.
- **Consequence for BPS's power law.** It is this γ₋ (or the vector-operator analogue), made O(1) by strong coupling. At weak coupling γ₋ = O(g²/16π²) per unit of log(scale), which is Chadha–Nielsen.

### 2b. The complete list of non-irrelevant LV channels allowed by the axioms' symmetry (checked)

**Background tensors.** A Z³ lattice with a time direction supplies backgrounds invariant under:
- the chiral cubic group O (axiom Lattice: proper rotations only, no inversion);
- time translations (the unit vector u^μ).

A deformation ∫B·O_(j₁,j₂) needs an O-invariant in the SO(3) content of (j₁,j₂). A_1 multiplicities in spin ℓ: ℓ = 0, 4, 6, 8, 9, 10, 12 (×2) (`e1_checks.out` §1). Combined with the unitarity floors:

| Lorentz rep of the operator | Example | Δ_min | Status at a unitary Lorentz-invariant IR CFT |
|---|---|---|---|
| (½,½) vector, contracted with u | J⁰, J₅⁰ (a₀, b₀, k_AF type; dimension-3 SME) | 3 | **Dangerous window 3 ≤ Δ ≤ 4.** Conserved J: a chemical potential, removable by a phase or gauge redefinition only within fixed-charge sectors. Non-conserved: physical and relevant unless Δ > 4. Every u·V term is CPT-odd |
| (1,1) spin 2, via u^μu^ν | T₀₀: **redundant**. T₋₀₀ (relative speeds, all SME c_μν, k_F, k_φ isotropic parts): **irrelevant**, exponent Δ − 4 > 0 | 4 | §2a |
| (3/2,3/2) spin 3, via uuu | — | 5 | always irrelevant, exponent ≥ 1 |
| (4,0)⊕(0,4) and (2,2) | cubic anisotropy (A₁ in ℓ = 4) | 5–6 | always irrelevant, exponent ≥ 1 (≥ 2 for symmetric spin 4) |
| (1,0), (2,0), (3/2,½), (3,0) | antisymmetric H_μν, Weyl-like | — | **no O-invariant background**: forbidden by the Lattice axiom alone (proved by character count) |

**Result (proved, under unitarity and a unique stress tensor).** At any unitary interacting Lorentz-invariant IR fixed point reached from a Z³ × time law, every Lorentz-violating deformation is one of three kinds:
1. **Redundant:** the common speed.
2. **Irrelevant:** all relative speeds and all anisotropy.
3. **In the spin-1 window.** These are CPT-odd and dimension-3 type. Strong dynamics removes them only if every non-conserved vector has Δ > 4. Conserved-current chemical potentials must vanish by charge conjugation or particle–hole symmetry, or by commensurate filling.

**What the window requires (suggested).** Closing the window needs an antiunitary symmetry that flows to CPT. On Z³ that symmetry must include spatial inversion, which O lacks. It is therefore a property of the chosen admissibility rule, not supplied by the axioms; this agrees with F2's §1a.

### 2c. How fast strong dynamics can drag an *elementary* field (suggested; matches BPS)

| Elementary field | Couples to | Dimension of the coupling | Drag on its speed |
|---|---|---|---|
| Scalar or fermion | composite O of dimension d/2 + ν | 1 − ν | Power law (E/Λ)^{2(1−ν)} if ν < 1. BPS's RS model: e/γ needs ν ≲ 0.38 |
| Gauge field | conserved J, with Δ_J = 3 protected | 0 (marginal) | Rate e²b_CFT/8π² ~ 1/ln(Λ_L/μ): a power of a log at best |
| Graviton | conserved T, with Δ_T = 4 protected | −1 (κ, irrelevant) | Rate ∝ κ²μ² → 0 in the IR: **frozen** |

The protection of conserved operators, which made the common speed harmless, also fixes these drag rates, whatever the strength of the strong dynamics. **Reading:**
- gauge bosons must be *emergent or dual* within the strong stage;
- the graviton cannot be dragged at all.

### 2d. The weak-coupling limit: Chadha–Nielsen running is the DGLAP n = 2 singlet anomalous dimension (checked)

The isotropic c_μν coefficients of quarks and gluons (or of electron and photon) couple to the twist-2 spin-2 operators. Their mixing matrix is the n = 2 moment of DGLAP:
- the zero eigenvalue is the total T (momentum sum rule, i.e. redundancy);
- λ₊ = γ_qq(2) + γ_gg(2) = 64/9 + 4n_f/3, in units of α/4π.

**Checks** (`e1_checks.out` §2; `e1_ct_weighting.out`):
- d_NS(2) = 32/75 at n_f = 4 (Gross–Wilczek).
- Asymptotic quark momentum fraction 3n_f/(16 + 3n_f).
- For QED with one flavour, λ₊ = 8 and |β₀| = 4/3, so the exponent is λ₊/2|β₀| = 3. This equals KLP's Q⁻³ exactly, and equals Anber–Donoghue's relative QED rate e²/2π² = 8·α/4π exactly.

**Numbers (checked arithmetic, one loop):**
- Quark–gluon LV from M_Pl to 1 TeV (n_f = 6, d₊ = 1.08): suppressed by a factor of **0.19**.
- e–γ from M_Pl to m_e: **0.78** (F2 estimated 0.89).

**Cap from the measured SM couplings (checked).**
- If the SM gauge interactions themselves did the dragging, γ ≤ λ₊α_s(TeV)/4π ≈ **0.11**. Fifteen decades then give 0.023. That falls short of 1e-19 by about 17 orders.
- A conformal-window stage with α* = O(1) would give γ₊ ≈ 1.4 (one loop; SU(3), n_f = 12, Banks–Zaks α* = 0.75; illustrative only). But it cannot be the SM's own QCD: once extra flavours decouple, α_s only grows toward the IR, so α_s(TeV) = 0.09 caps α* above the TeV at ≲ 0.09.
- **Reading:** SM couplings cannot do the job. A separate strong sector, with SM fields composite or dual, is required. This is BPS's conclusion, reached here independently from measured couplings.

## 3. The graviton side

### 3a. The TT stiffness (graviton mass) cannot be made irrelevant by matter dynamics (suggested, strong; FAIL item)

**What μ is.**
- μ = ∂²E_vac/∂h_TT² is a c-number contact term in the matter's generating functional W[h]. It is not an operator deformation of the matter fixed point, so the CFT's anomalous dimensions do not act on it.
- In the graviton action, m_g² has RG eigenvalue +2 (μ ~ Λ⁴ in absolute units). The massless point is an **unstable** (relevant) direction. Landing on it is a tuning: P0's two TT tunings are precisely the codimension of that critical surface.

**Why emergent LI in the IR does not help.** Decompose E_vac(h) into RG shells.
- A Lorentz-invariant shell contributes nothing at constant strain, because a constant metric is redundant (§2a).
- A shell at energy E with residual Lorentz violation η(E) contributes ~E³η(E)dE.
- So μ ∝ ∫₀^Λ E³η(E)dE is **UV-dominated**. Even with η = (E/Λ)^γ starting at the lattice scale, μ falls only by **4/(4+γ)**: 0.85 at γ = 0.7, 0.67 at γ = 2 (`e1_checks.out` §4).
- The bound needs ≈ 9e-102 (P0).

**The bound in energy units (checked arithmetic).**
- μ < (m_g M̄_Pl)² = (178 eV)⁴, for m_g < 1.3e-23 eV (comparator, memory).
- This is a vacuum-energy-type fine-tuning, 4·log₁₀(178/2.3e-3) ≈ 20 orders milder than the cosmological constant, and of the same kind. Weinberg's no-go for adjustment mechanisms (comparator, memory) is the relevant prior art.

**Escapes examined:**
- **Exact Q-exact lattice SUSY.** E_vac(h) ≡ 0 for every strain if H(h) = {Q(h), Q(h)†} with unbroken SUSY. But SUSY must be broken by about a TeV, and then μ ~ m_soft⁴/16π² exceeds the bound by **6e36** (checked arithmetic). This is the F3 "dead" route, confirmed in this sense.
- **A composite graviton from the strong sector.** Excluded in a Lorentz-invariant IR by Weinberg–Witten, unless the graviton is the gauge field of an emergent diffeomorphism redundancy. That is lane R's question; matter strong dynamics does not supply it.
- **Holographic, RS-type.** The 4D graviton zero mode lives at the UV brane, where the Lorentz violation sits. BPS: sizable LV in gravity.

### 3b. Graviton speed versus matter speed (suggested; FAIL item)

**Coupling.** Gravity couples through κ, which has dimension −1. By §2a and §2c, c_T − c_matter is frozen at its UV value. Strong dynamics cannot equalize it.

**Induced LV.** Matter loops induce graviton kinetic-term LV, ∝ ∫E·η(E)dE ~ Λ²·2/(2+γ). This is again UV-dominated (0.5 at γ = 2). With a⁻¹ = M_Pl it is O(N_species/16π²), against GW170817's 1e-15.

**Cost.** One more tuning (c_T against the emergent c), on top of P0. This agrees with BPS (Sec. 4) and Anber–Donoghue (gravity keeps the largest difference).

### 3c. Can strong dynamics make C3's algebra anomaly irrelevant? (suggested)

**Operator part: yes, in a sense.** C3's closure defect is Hess(ω²/2) − Hess(0) = O((ka)²). On low-energy states it is already a dimension-6 (irrelevant) effect, and a strong fixed point only suppresses it further, by (E/Λ)^{γ_min}. The hypersurface-deformation algebra closes on low-energy states to that accuracy, never exactly.

**Vacuum and loop part: no.** The zone-averaged anomaly (RI's "order-one zone-averaged anomaly"; the referee's A(π) sequence) enters gravity through loops as the TT stiffness and the induced graviton LV. These are UV-dominated as in §3a and §3b and are not affected by IR fixed points. Whether that part *must* produce a graviton mass is lane RW's question.

## 4. Framework fit, and the best-case estimate

**Requirements for the best mechanism (suggested):**
- **R1.** One interacting, strongly coupled sector runs from about a⁻¹ down to an exit scale Λ_s. All SM fields are composite or dual in it, gauge bosons included (§2c, §2d). There is no light sector coupled only irrelevantly, except gravity.
- **R2.** The least-irrelevant LV exponent is large enough (table below).
- **R3.** The spin-1 window is empty. This needs an antiunitary symmetry including inversion (flowing to CPT), and particle–hole or commensurability for the chemical potentials. That is not supplied by the axioms (§2b).
- **R4.** The fixed point has no unprotected relevant singlet operators, or else tunings return.
- **R5.** A natural exit at Λ_s/M_Pl ≈ 1e-15, by dimensional transmutation (marginally relevant), to a weakly coupled chiral SM. This runs into:
  - the chirality wall, an open gate of the axioms;
  - the absence of any controlled non-SUSY example of weakly coupled gauge fields emerging from a strongly coupled 4D stage. Seiberg's free magnetic phase is the SUSY example; F2 found lattice SUSY with P unavailable on Z³ (comparator, memory).
- **R6.** Gravity is untouched (§3): P0's two TT tunings at ~1e-101, plus one c_T match at 1e-15.

**Exponent needed, with initial LV δ₀ = 1 at the lattice scale and M_Pl = 1.22e19 GeV (`e1_checks.out` §3 and §5).** Bounds are taken from F2 (comparator).

| Bound | Below Λ_s, frozen at (Λ_s/M_Pl)^γ, with Λ_s = 1 / 10 / 100 TeV | Set at energy E > Λ_s, where δc ~ (E/M_Pl)^γ |
|---|---|---|
| e/γ photon decay (2.7e-19) | 1.15 / 1.23 / 1.32 | 1.4 PeV photon: **1.43** |
| ν (1e-20) | 1.24 / 1.33 / 1.42 | — |
| p/γ (4e-23, if c_p > c_γ) | 1.39 / 1.48 / 1.59 | 1e20 eV proton: **2.76** (that sign only); lattice-like sign (9e-13): 1.49 |

**Suppression at Λ_s = 10 TeV for the exponents available:**
- BPS Lifshitz, 2α ≈ 0.7: 3e-11. Fails by 8–12 orders.
- BPW 2024, κ = 1: 8e-16. Fails.
- BPW 2024, κ = 2: 7e-31. Passes every matter bound, including the 2.76 case marginally.
- QED₃-type 1/N exponents (0.16 at N = 4): 4e-3.
- SM-coupling Chadha–Nielsen: 0.02–0.8.

**Best case (suggested).** A holographic-type strong stage with γ ≈ 2 over about 15 decades suppresses matter relative speeds to about 1e-30. That would reduce the matter side from F2's 1–9 speed tunings (Coleman–Glashow count) to 0. Matter would then be as good as F2's hypercubic Z⁴ case, while keeping a preferred frame in the UV. The gravity sector is unchanged: P0 plus a c_T match.

**Axiom compatibility (reading).**
- **Fits.** Qubits on Z³ with a nearest-neighbour rule can in principle host strongly coupled lattice gauge or spin systems: coarse cells of many qubits, quantum-link-type gauge fields. Emergent Lorentz invariance would also *supply* the common c, which suits the axioms' lack of a time metric.
- **Not shown.**
  - No nearest-neighbour qubit Hamiltonian is known to flow to a strongly coupled 4D Lorentz-invariant CFT with γ ≥ 1.5. Hamiltonian, continuous-time versions of conformal-window lattice gauge theories are the natural candidate; that is E2's computation.
  - A large-N holographic-like stage needs O(N²) degrees of freedom per coarse cell.
  - Emergent weakly coupled gauge fields from lattice spin models (spin-ice photons) appear at the lattice scale with their own speed. By §2c they are dragged only logarithmically, so they are the wrong kind: the SM gauge fields would have to appear at Λ_s, not at a.
- **Known physics.** The weakly coupled SM is compatible only as the low-energy (below Λ_s) description of a composite or dual sector. The bound here is Λ_s ≳ 10 TeV from compositeness limits (comparator, memory). At E > Λ_s the highest-energy cosmic rays probe the strong stage directly, which is why the 1e20 eV row bites.

## 5. Verdict against the FIXED readings

- **PASS clause: not met.** No mechanism drives the TT stiffness below bounds. No explicit nearest-neighbour realization with γ ≥ 1.5 and an emergent SM exists.
- **FAIL clause: met for the classes examined.** "For the classes examined, the TT stiffness, or some Lorentz-violating coefficient that bounds require, cannot be made irrelevant":
  1. **The TT stiffness** is a relevant, UV-dominated c-number. IR emergent Lorentz invariance changes it by at most 4/(4+γ), so it stays at ~1e-101 tuning (§3a). The classes are an elementary or induced graviton whose stiffness comes from lattice matter's vacuum response, and a composite graviton in a Lorentz-invariant IR (Weinberg–Witten). Emergent diffeomorphism gauge invariance is excluded from the class, as it is lane R's.
  2. **The graviton–matter speed difference** cannot be equalized, because the coupling is irrelevant (§3b; GW170817 needs 1e-15).
  3. **The CN-type running from SM couplings** is too slow (γ ≤ 0.11; §2d).
- **Matter dimension-4 speeds: a conditional partial win (suggested).** They are irrelevant at any interacting unitary fixed point with one stress tensor (proved). The exponent needed, ≈ 1.5 (2.8 for one sign of the proton bound), lies inside the literature's holographic range (BPW κ = 1–2). This holds only under R1–R5, which are unrealized.
- **E1 = FAIL (bounded)**, pending the other-vendor referee. This matches the supervisor's registered expectation: "E1 FAIL for the graviton mass, with a partial win for matter speeds." A refinement beyond the expectation: the graviton *speed* also fails, for a separate reason (an irrelevant coupling, not a relevant operator).

**What would change this:**
- an emergent diffeomorphism gauge redundancy (lane R) that forbids the TT mass in the IR *and* removes its UV contact term;
- a lattice law with an exact vacuum-energy sum rule that survives SUSY breaking;
- a scale-reference change with a⁻¹ ≪ M_Pl (the Pospelov–Shang-type separation of F2), which is a price.

## 6. Notes for the referee
- **§2a is standard (Wegner redundancy), stated carefully.** The first-order deformation S + ε∫T₀₀ and the covariant family S[g(ε)] differ at O(ε²) by contact terms. Exact marginality is a property of the completed family.
- **The recombination rate formula γ₋ ∝ g²(1/C_T₁ + 1/C_T₂) is suggested.** It is checked only through its two consequences (rate ∝ 1/C_T, C_T-weighted invariance) in the two one-loop models whose equations were extracted. Those equations were transcribed by a summarizing fetch tool; the exact C_T matches make a transcription error unlikely, but the referee should verify them against the paper.
- **The UV-dominance argument (§3a, §3b) is a scaling argument, not a theorem.** A counterexample would need a lattice-scale cancellation (a sum rule) in E_vac(h).
- **The bounds** (2.7e-19, 1e-20, 4.4e-23, 9e-13, 1e-15, m_g < 1.3e-23 eV) are comparators, taken from F2 or from memory.

## Sources (fetched)
- [Bednik, Pujolàs, Sibiryakov, arXiv:1305.0011](https://arxiv.org/abs/1305.0011) ([ar5iv](https://ar5iv.labs.arxiv.org/html/1305.0011))
- [Baggioli, Pujolàs, Wu, arXiv:2407.11552](https://arxiv.org/html/2407.11552v2)
- [Anber, Donoghue, arXiv:1102.0789](https://ar5iv.labs.arxiv.org/html/1102.0789)
- [Kostelecký, Lane, Pickering, hep-th/0111123](https://ar5iv.labs.arxiv.org/html/hep-th/0111123)
- [Roy, Juričić, Herbut, arXiv:1510.07650](https://arxiv.org/abs/1510.07650)
- [Iengo, Russo, Serone, arXiv:0906.3477](https://arxiv.org/pdf/0906.3477)
- [Kharuk, Sibiryakov, arXiv:1505.04130](https://arxiv.org/abs/1505.04130)
- [Kiritsis, arXiv:1207.2325](https://arxiv.org/abs/1207.2325)
- [Isobe, Nagaosa, arXiv:1205.2427](https://ar5iv.labs.arxiv.org/html/1205.2427)
- [Vafek, Tešanović, Franz, cond-mat/0203047](https://arxiv.org/pdf/cond-mat/0203047), [Hands et al., hep-lat/0412009](https://arxiv.org/pdf/hep-lat/0412009), [Concha, Stanev, Tešanović, arXiv:0906.1103](https://arxiv.org/pdf/0906.1103)
- Chadha–Nielsen, Nucl. Phys. B217 (1983) 125 (citation confirmed via [arXiv:1304.5795](https://arxiv.org/pdf/1304.5795) reference list)
