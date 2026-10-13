# C5 R19-19 report: extend (S\*) to O(q²). Can one local, number-free source clause remove every graviton-cone row, and what does it cost?

**Author and provenance.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 05:46Z to about 06:40Z. I edited no repository file and downloaded nothing.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `S/` = `scratchpad/C5/R19-19/` (this folder); `vR19-15` = `scratchpad/C5/ref_R19-15/REFEREE_VERDICT.md`; `vR19-12` = `scratchpad/C5/ref_R19-12/REFEREE_VERDICT.md`.

**Machine use.** `OMP_NUM_THREADS=2`; load 3–5 from other jobs; longest run about 2 min.

**What I read.** `AX` in full. `P/TESTS.md`: C5 method (`:2302-2319`), my item (`:8008-8046`), and the entries/verdicts for R9-9 (`:3862-3872`, `:3939-3950`), R16-3 (`:5087-5106`, `:5359-5368`, `:5427-5432`), R17-3 (`:5786-5814`, `:5907-5922`, `:6007-6016`), R17-4 (`:5816-5853`, `:5940-5954`, `:6171-6178`), R18-9 (`:6847-6875`, `:7044-7057`, `:7284-7297`), R18-13 (`:7063-7091`, `:7305-7315`, `:7505-7516`), R19-6 (`:7397-7424`, `:7569-7580`, `:7663-7672`), R19-11 (`:7630-7651`, `:7811-7822`, `:7986-7994`), R19-12 (`:7675-7700`, `:7880-7890`), R19-15 (`:7828-7858`, `:7995-8006`); also R11-1's verdict (`:4394-4409`), RFW F2 (`:2269`), R16-5/R17-5 verdicts (`:5437`, `:6179-6197`). `P/agents/C5_R19-15_report.md` in full; `vR19-15` (appeared during my run: CONFIRMED WITH CORRECTIONS, STRUCTURAL-ZERO by construction); `P/agents/C4_V3_referee.md` in full; `vR19-12`; `C5_R9-9_report.md:100-131,180-186`; `C5_R16-3_report.md` (summary, §1); `C5_R17-4_report.md:15-20,54,100-112`; `C5_R19-12_report.md:52-55,263-310`.

**Runners rechecked before use (checked).**
- R17-4 `basis.py` (copied to `S/arch17_4/`): output byte-identical to the archive (`basis_recheck.out`; rank 4, body relation).
- R17-4's NN/U off-axis numbers, by an independent direct-grid evaluator I wrote (`r1919_taylor.py`): face1 = −1.245452929e-4, face2 = −2.289166108e-4 at m = 1, against R17-4's −1.245452931e-4 and −2.289166113e-4 (`C5_R17-4_report.md:110`).
- R19-15 `r1915_d_loops.py` at N = 20 (copied to `S/arch19_15/`): output identical to the archive except the runtime line (μ_T2⁽²⁾ = +4.027058e-9 λ² at m = 1; vR19-15 item 3 reproduced 4.027043e-9 at N = 48).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics run here) / suggested (argued, not proved) / reading (interpretation) / comparator (outside reference) / RECALLED (from memory).

---

## 0. In plain words

1. **The clause, made precise (reading + proved).** (S\*\*) must act on the whole response tensor, not only its TT block: at q → 0 the static response A^{ijkl}h_kl has no "TT" (there is no q), and a TT-only subtraction leaves the non-TT Ward violations in place. Stated properly:
   > **(S\*\*₀):** the law's lowest state contributes nothing to the gravitating source through second order in derivatives of the metric (at linear order in h).
   Equivalently: subtract the Taylor polynomial through total degree 2 in (ω, q) of the exact lowest-state linear response, plus its one-point part. A variant keeps a Lorentz-invariant piece Z·(linearized Einstein operator). The rows are the same for every Z, so Z := 0 is the canonical, rule-free choice.
2. **What it does (proved; checked).**
   - All six rows (Ξ_Eg, Ξ_T2g, face1, face2, μ_E, μ_T2) are functions of that Taylor polynomial alone, so the clause zeroes them identically, for every species and mass, at every loop order (it refers to the exact vacuum).
   - In the NN scalar with the U vertex, the vacuum response is analytic through O(p²), and the remainder after subtraction is pure O(p⁴): ratio 15.97–15.996 against 16, at m = 1, 0.5, 0.3.
3. **New structural fact (checked): five of the six rows are violations of the graviton's own Ward identity; one is genuine Lorentz violation (Lemma G).** Consider local, cubic-covariant, P- and T-even response kernels through two derivatives (32-dimensional).
   - Those that satisfy the linearized-diffeomorphism Ward identity (Bianchi-exact) form a 2-dimensional family. Its image in the six rows is the single line (1, 1, 1, 1, 0, 0): a common isotropic speed shift, no shear.
   - With only spatial gauge invariance (ξ₀ = 0), the image is 2-dimensional: μ = 0, face2 = Ξ_T2g, face1 = (3Ξ_Eg + Ξ_T2g)/4.
   - So R17-4's K₆ term, UD's face2 ≠ T₂g, the shear rows and (under full diffeos) Ξ_Eg − Ξ_T2g all measure how far the lattice vacuum's response fails the Ward identity. Only the isotropic speed is a gauge-invariant Lorentz-violating coefficient.
4. **What the clause really assumes (proved, elementary; Lemma E).** (S\*\*) holds exactly when the vacuum's local gravitating response through two derivatives is the Lorentz-invariant form. On the graviton cone, that is the six rows set to zero, plus 25 off-shell (gauge-sector and normalization) conditions.
   - Splitting it: five conditions are what any local, Bianchi-consistent gravitating source must satisfy anyway, and the lattice matter cannot supply them through a Ward completion (refereed W15-type walls).
   - One condition, the isotropic graviton speed, is pure stipulation: "assume c_g = c".
5. **O(q⁴) remainder (checked for one species; size envelope suggested).**
   - ω² = q²[1 + α(qa)²], with α = 16π c₄ and c₄ ≈ 1.6–3.5e-5 per NN scalar.
   - At a = ℓ_P and 100 Hz: |δc/c| ≈ 1e-84 per scalar, and ≤ 3e-81 in a generous SM envelope. The GW170817 band is ~1e-15 (RECALLED).
   - The quadratic scale is E_QG,2 ≥ 5e18 GeV, against Fermi-LAT-type photon bounds of ~1e11 GeV (RECALLED).
6. **Cost.**
   - Zero numbers, one clause (it contains (S) and (S\*) and replaces both).
   - Local; linearly non-signalling; Bianchi-exact through the subtracted order.
   - Radiatively exact by construction.
   - No conflict found with W1, weight-1 (Lemma L) or the linear Bianchi identity.
   - The R19-12 bill drops from 11 equalities + window + CC (per class) to **4 charge equalities + CC (paid by (S) ⊂ (S\*\*))**: 10 per species, 2 in the q²-correlated basis.
   - Matter's own cone rows are untouched.
7. **A risk the clause inherits, sharpened here (suggested; counted once with R19-15 §3.4).** The subtraction is fixed to the true lowest state.
   - Before the electroweak crossover the actual vacuum differs: fermions are nearly massless. The unsubtracted shear is then Δμ ~ 5e-19 per cell (Wilson-Dirac) or ~4e-36 (twisted mass), from R19-11's numbers.
   - In R9-9's normalization that is |m_g| ~ 6e10 GeV or ~170 GeV, against H(T_EW) ~ 1e-14 GeV.
   - If the dynamical-metric reading holds, tensor modes have |m_g| ≫ H throughout the symmetric phase.
   - The sign is law-dependent. On R19-11's 0⁺ root edges it is **tachyonic in both channels**: Δμ = −4.70e-19 and −1.20e-19, the negatives of the refereed SM residuals. That is an instability growing at ~1e10 GeV, which is observationally catastrophic if the shear acts as a canonically normalized graviton mass (vR19-11 item 4).
   - Avoiding |m_g| > H needs |Δμ| ≲ 2e-67, i.e. rows that are mass-independent to that level (a tuning again), unless the symmetric-phase response is not a canonically normalized graviton mass.
   - This is a definite prediction of the fixed-state clause, and a possible conflict. It cuts against "non-predictive" and should be tested.
8. **Reading.**
   - **CONE-PRINCIPLE on the letter, by construction** (as vR19-15 item 4 ruled for (S\*)).
   - **TAUTOLOGY:** the equivalence half is demonstrated (Lemma E) and offered to the referee. My assessment is that it does not cleanly meet "non-predictive": five of the six conditions are Ward conditions, and item 7 is a prediction.
   - **CONFLICT:** none found with W1, weight-1 or linear Bianchi.

---

## 1. Class, hypotheses, exclusions (stated before any title)

- **Rows (R9-9/R16-3/R17-4 definitions).**
  - The TT self-energy is Π(ω, q) = S₂ − ¼⟨|V|²/(ε₊ε₋)·E/(E² − ω²)⟩, with dispersion (M²/2)(ω² − q²) = Π (`C5_R9-9_report.md:118-120`).
  - μ = Π(0, 0) (shear rows, seagull included).
  - Ξ(n, e) = ∂_{q²}Π + ∂_{ω²}Π at 0, for (n, e) = (z, E_g), (z, T₂g), (110, face1 = aa − bb), (110, face2 = ab + ba), with a = (1, −1, 0)/√2, b = ẑ (`C5_R17-4_report.md:54`).
  - Physical size: c² − 1 = (2/M²)Ξ = 16πΞ at a = ℓ_P (`C5_R16-3_report.md:276`; `C5_R9-9_report.md:186`).
- **Response kernel.** Π^{μνρσ}(ω, q) is the exact lowest-state linear response of the gravitating (weight-1) source to h. All rows depend only on its Taylor polynomial T₂[Π] through total degree 2 (definitions above). Degree-1 terms are excluded by parity (O_h ∋ inversion); checked in the invariant-space construction.
- **Symmetry class for Lemma G.** Kernels invariant under O_h (spatial signed permutations) × T (time-index sign flip), symmetric in (μν), (ρσ), (μν)↔(ρσ). Gauge action δh_μν = p_μξ_ν + p_νξ_μ. In the IR the N-type box graviton's lattice derivatives equal p exactly (`C5_R9-9_report.md:100`), and the midpoint phase is absorbed.
- **Model for numerics.** NN scalar, ε² = m² + Σ4 sin²(k_i/2); U vertex with R17-4's E1 extension, V_e = Σe_ij f_i f_j, f = sin k (`C5_R16-3_report.md:36`; `C5_R17-4_report.md:15`). m ∈ {1, 0.5, 0.3}; 3D midpoint grids N = 48–128.
- **Excluded.**
  - Nonlinear (O(h²∂²)) completion of the clause.
  - Non-lowest states, except the estimate in §3.6.
  - Box-law (root-edge) O(q⁴) coefficients (not computed; envelope suggested).
  - Two-loop q ≠ 0 diagrams (not computed).
  - Pairing; superluminal edges.

## 2. Prior art (each counted once)

- **R19-15 + vR19-15.**
  - Lemma H: μ is the full uniform-strain Hessian of the vacuum energy, seagull included.
  - No registered bridge clause removes the anisotropy A = μ_E − μ_T2.
  - Two-loop T₂g basketball +4.027e-9 λ².
  - (S\*) "earns STRUCTURAL-ZERO by construction", is "tautological as a cancellation mechanism", and is "a stipulated renormalization/source definition, not a derived Ward mechanism"; a "full nonlinear action/Bianchi completion is not" established (`vR19-15:14,18`).
  - Its §3.3 names an untested (S\*\*) as the entire, non-local linear response (`C5_R19-15_report.md:254-258`). That is not this item's clause; this item truncates at O(q²) and is local.
- **R17-3 verdict.** (S), "C = E₀[H]", is "a genuine, consistent, number-free principle that would have to be added", "not a disguised tuning" (`TESTS:6015-6016`).
- **C4 V3 referee.** R₀ "imposes μ = 0 as a renormalization condition"; extended to the exact interacting strained ground energy it is "explicitly tautological" (`C4_V3_referee.md:29`).
- **R16-3.** IBP identity Ξ = (1/32)⟨|V|²(5v_z² − 1)/ε⁵⟩ (`TESTS:5361`). **R9-9.** Theorem T: Ξ = α + β (`C5_R9-9_report.md:118-131`).
- **R17-4 + verdict.**
  - Off-axis formula; rank 4.
  - U identities: face2 ≡ T₂g and face1 = (3Ξ_Eg + Ξ_T2g)/4 − ⟨K₆/ε⁷⟩/128 (`C5_R17-4_report.md:17-20`; `TESTS:6171-6178`).
- **R18-9 / R18-13.**
  - UD Dirac breaks face2 ≡ T₂g (~7e-5, `TESTS:7055`).
  - Lemma S: "no exactly conserved improvement moves the face rows" (`TESTS:7310`).
  - Bill: 6 + 1 (`TESTS:7505-7516`).
- **R19-11 + verdict.**
  - Rows analytic in m (Wilson-Dirac) or m² (scalar, vector), with finite m → 0⁺ limits.
  - SM shear residuals O(1e-19) per cell, "catastrophic only if … identified with a canonically normalized physical graviton mass" (`TESTS:7986-7994`).
- **R19-12 + vR19-12.**
  - Charge block: 4 per class, 10 per species, 2 q²-correlated.
  - Route A: 11 + window + CC (`vR19-12` item 4, "Strongest correct statement").
- **R11-1 verdict.** Matter's own graviton-loop speed is c_m² − 1 = 4κm²J₂; "for light matter the split tends to −κΞ"; prescription dD-M only (`TESTS:4401-4409`).
- **Ward walls.**
  - RFW F2: "No translation-covariant completion makes the action gauge invariant through O(κ²)" (`TESTS:2269`).
  - R16-5 (`TESTS:5437`) and R17-5 ("standard W2_pf is impossible for nonzero momentum density", `TESTS:6186`).
- **R19-5 / R19-6 verdicts.** Exact W1 ≠ W2; Lemma L confirmed (`TESTS:7747-7752`, `:7663-7672`).

---

## 3. Results

### 3.1 (a) The clause as an equation

**Definition.** Let Π_vac^{μνρσ}(p) be the exact lowest-state linear response of ⟨√−g T^{μν}⟩ to h_ρσ, and T₂ its Taylor polynomial at p = 0 through total degree 2. Let s₀^{μν} = ⟨√−g T^{μν}⟩_vac be the one-point part. Then

  S_grav^{μν}[h] = ⟨√−g T^{μν}⟩_h − s₀^{μν} − ( T₂[Π_vac] − Z·E_EH )^{μνρσ} h_ρσ,

where E_EH is the linearized Einstein operator (identically transverse; checked in `r1919_gauge.out`: Ward residual 0, rows 0).
- (S\*\*₀) takes Z := 0.
- In position space the subtracted term is Σ_{|α|≤2} c_α ∂^α h(x): a constant-coefficient differential operator of order 2, with coefficients computed from the law.
- At p = 0 it reduces to (S\*)'s linear part, and its s₀ part is (S).

**Proved (elementary).**
- (i) **Local.** It is a finite-order differential operator.
- (ii) **Covariant.** It inherits the law's translation and O_h covariance.
- (iii) **Number-free.** The coefficients are functionals of the law; Z := 0 needs no rule.

**Correction to the item's wording (reading).** The item writes "Π_TT's Taylor coefficients at q⁰ and q²".
- At q⁰ the response is the 4-index tensor A^{ijkl} acting on a uniform strain. "TT" is undefined there because there is no q.
- At O(q²), subtracting only the TT block leaves the non-TT Ward violations (§3.3).
- The consistent version is the full-tensor one above. The six rows are unaffected by this choice; Bianchi is not.

**Z is unobservable on the cone (proved).** Z·E_EH has zero rows, so every Z gives the same six rows. Z ≠ 0 shifts only the induced Newton constant (a Sakharov-type term), which is absorbed into the fitted a/ℓ_P (`AX:189-190`).

### 3.2 (b) Effect on the six rows

**Lemma R (proved).** By the R9-9/R17-4 definitions, every row depends only on T₂[Π]: μ_pol = e·Π(0,0)·e, and Ξ(n, e) = e·(∂_{ω²} + ∂_{q²})Π·e at 0. Under (S\*\*), T₂[Π_grav] = Z·E_EH, whose rows are (0, 0, 0, 0, 0, 0) (checked: `r1919_gauge.out`, "EH rows" and "eps.eps.t (t = η)").

**Hence (proved):** all six rows vanish identically.
- For every species and every mass, provided T₂[Π_vac] exists.
- At every loop order, because Π_vac is the exact lowest-state response.
- No knob is used.

**Existence of T₂ (checked in one model; refereed elsewhere).**
- Massive separable bands: rows analytic in m or m², with finite m → 0⁺ limits (R19-11 Lemmas A/B, confirmed `TESTS:7988-7990`).
- Massless species: IR power counting gives integrands ~ k⁴/k⁵ for the degree-2 coefficients, so they are finite. Non-analyticity starts at p⁴ log p (suggested).
- Checked (`r1919_taylor.out`): T₂ exists for NN/U at m = 1, 0.5, 0.3; the residual Π − T₂ scales as p⁴ along an off-shell ray (ratios 15.869–15.996 → 16) and on shell (R/s⁴ constant to ≤ 0.7% from s = 0.4 to 0.05).

| m (N) | Ξ_Eg | Ξ_T2g | Ξ_face1 | Ξ_face2 | on-shell c₄ range (s = 0.05) |
|---|---|---|---|---|---|
| 1 (48, 64; identical) | −6.8832e-5 | −2.2892e-4 | −1.24545e-4 | −2.28917e-4 | −5.58e-6 … −1.61e-5 |
| 0.5 (96) | −1.0534e-4 | −3.2469e-4 | −1.87088e-4 | −3.24691e-4 | −1.17e-5 … −2.88e-5 |
| 0.3 (128) | −1.1860e-4 | −3.5537e-4 | −2.08626e-4 | −3.55373e-4 | −1.48e-5 … −3.45e-5 |

These are the raw rows that (S\*\*) removes. After the clause the rows are exactly zero, and the remainder is the c₄ column.

**Lemma G (checked; exact linear algebra in `r1919_gauge.py` → `r1919_gauge.out`).** In the stated symmetry class:
- invariant degree-2 kernels: 26-dimensional; degree-0: 6-dimensional; the map to the six rows has rank 6 (all rows independent);
- **FULL linearized-diffeo Ward identity** (p_μΠ^{μνρσ} ≡ 0): allowed degree-2 space 2-dimensional (the ε·ε·t family with t = diag(t₀₀, t, t, t)), degree-0 space 0. Rows image: **the line (1, 1, 1, 1, 0, 0)**;
- **SPATIAL only** (ξ₀ = 0): allowed degree-2 space 8, degree-0 space 1. Rows image 2-dimensional, spanned by (1, 1, 1, 1, 0, 0) and (1, 0, ¾, 0, 0, 0). The second is the cubic kinetic term Σ_a K_aa², which I verified by hand: E_g diagonal weight 2, face1 weight 3/2, T₂g and face2 weight 0.

**Consequences (proved from Lemma G).**
- Any local, Bianchi-exact gravitating vacuum response has μ_E = μ_T2 = 0.
- With spatial gauge invariance, it also has face2 = Ξ_T2g and face1 = (3Ξ_Eg + Ξ_T2g)/4. With full linearized diffeos, also Ξ_Eg = Ξ_T2g.
- So the following are Ward-identity violations of the vacuum response:
  - R17-4's K₆ term;
  - UD's face2 − T₂g;
  - μ_E and μ_T2;
  - and, under full diffeos, Ξ_Eg − Ξ_T2g.
- This agrees with R18-13's Lemma S ("no exactly conserved improvement moves the face rows").

**Checked instance (`r1919_bounds.out`), NN/U:**
- face2 − T₂g = +6e-13 to +4e-12 (zero: the U/E1 vertex respects this spatial Ward combination, R17-4's identity);
- face1 − (3Eg + T2g)/4 = −1.57e-5, −2.69e-5, −3.08e-5 at m = 1, 0.5, 0.3 (spatial Ward violation);
- Ξ_Eg − Ξ_T2g = +1.6e-4 to +2.4e-4 (a time-diffeo Ward violation, if the N-type graviton has full linearized diffeos);
- isotropic part (2Ξ_Eg + 3Ξ_T2g)/5 = −1.6e-4 to −2.6e-4 (the gauge-invariant Lorentz violation).

**Lemma E (proved, elementary).** The invariant local kernels through degree 2 form a 32-dimensional space (26 + 6). (S\*\*) with free Z is the statement T₂[Π_grav] ∈ span(E_EH): 31 linear conditions; with Z := 0, 32.
- Six of them are the cone rows, which are independent (rank 6, Lemma G "NONE").
- The other 25 (or 26) are off-shell, gauge-sector and polarization-normalization conditions with no cone observable.
- So (S\*\*) adds nothing on the graviton cone at O(p²) beyond "the six rows vanish for the exact vacuum". It cannot fail a cone observation at that order. This is the "equivalent to assuming the answer" half of TAUTOLOGY.

**Which gauge group applies (reading).** R9-9's N-type graviton has lapse, shift, an exact linear constraint algebra and exactly two TT modes (`TESTS:3940-3944`), which indicates full linearized diffeos. If the lapse is projectable (Hořava-type), the SPATIAL count applies instead: four Ward rows and two gauge-invariant rows.

**Matter's own cone rows (proved, short).**
- (S\*\*) changes only the gravitating source's vacuum-response term. The charge block (O(e²) matter and photon self-energies) contains no source clause, so it is untouched.
- Matter's graviton-loop speed (R11-1(b)) uses the graviton propagator. (S\*\*) changes it only through the internal graviton's dressing, which is O(κ⁴).
- Reading, prescription dD-M only: with Ξ_eff = 0 the R11-1 split reduces to c_m² − 1 = 4κm²J₂, the term that "tends to" zero for light matter (`TESTS:4403-4404`). It is not paid by (S\*\*), and is not shown to need payment at SM masses.

### 3.3 (c) Locality, Bianchi and signalling

- **Locality and covariance:** proved (§3.1).
- **Linear-order signalling: none (proved, short).**
  - After (S\*\*), the graviton equation is (M²/2 − Z)·E_EH h + R₄ h = κ(matter excitations).
  - R₄ = Π_vac − T₂Π_vac is the vacuum's retarded response minus a polynomial. It keeps the retarded support of Π_vac, because subtracting a local operator cannot move support outside the light cone.
  - The principal symbol at low p is the Lorentz-invariant wave operator, strictly hyperbolic with the light cone (for Z := 0, the bare M² > 0).
  - No global variable enters, so there is no R15-1 λ(t)-type channel.
  - Nonlinear orders: not analyzed (the same gap vR19-15 item 4 recorded for (S\*)).
- **Bianchi.**
  - Before (S\*\*), the vacuum response breaks the linear Ward identity at O(p) (μ) and at O(p³) (the rows in Lemma G's complement).
  - After (S\*\*), the local part is Z·E_EH, identically transverse (checked). The remaining defect is p·R₄ = O(p⁵), relative size (pa)⁴. Not computed: suggested, from the analytic structure.
  - So (S\*\*) moves the vacuum's linear Bianchi defect from O(p) to O(p⁵). It does not remove it. Exact removal needs the full linear response (R19-15's non-local P-R19-15b) or an exact W2 completion, which the refereed walls exclude for lattice matter (`TESTS:2269`, `:5437`, `:6186`).
  - **Status:** no conflict with a refereed Bianchi result. No refereed result asserts exact Bianchi for the lattice vacuum; the status quo violates it at O(p).
- **TT-only version (proved).** Subtracting only the TT block at O(q²) leaves the longitudinal and non-TT Ward violations, and is undefined at q⁰. Lemma G shows that Bianchi-exactness constrains the TT rows only through the full tensor, so the full-tensor clause is required.

### 3.4 (d) What remains at O(q⁴) and beyond

**Checked (`r1919_taylor.out`; NN/U).**
- On shell, the remainder is c₄(n, e)s⁴, with c₄ between −5.6e-6 and −3.45e-5 over the four (n, e) at m = 1 to 0.3.
- Its Lorentz-invariant part, ∝ (ω² − q²)², vanishes on shell, so on-shell c₄ is entirely Lorentz-violating.
- With (M²/2)(ω² − q²) = Π: ω² = q²[1 + α(qa)²], α = 16π c₄.

**Bounds (`r1919_bounds.out`; comparators RECALLED).**

| case | α | \|δc/c\| at 100 Hz (qa = 3.4e-41) | E_QG,2 = M_P/√α | \|δc/c\| at 1 TeV |
|---|---|---|---|---|
| one NN scalar, m = 0.3 (checked) | 1.7e-3 | 1e-84 | 2.9e20 GeV | 6e-36 |
| SM envelope: 100 fields × 30 margin for vertex, edge, log(1/ma) (suggested) | 5.2 | 3e-81 | 5.3e18 GeV | 2e-32 |
| comparators (RECALLED) | | GW170817: −3e-15 ≤ δc/c ≤ 7e-16 | Fermi-LAT-type: E_QG,2 ≳ 1e11 GeV (photons) | |

- Margins are ≥ 3e65 against GW170817 and ≥ 5e7 in E_QG,2.
- The Fermi-LAT bound constrains photons. Matter's own O(k⁴) Lorentz violation is outside (S\*\*), so it is quoted only as the item's comparator.
- **Massless species (suggested).**
  - On box laws the IR band is exactly Lorentz-invariant (σ′ = 1 inside the box), so IR non-analytic terms are Lorentz-invariant and vanish on shell. The Lorentz-violating O(p⁴) part comes from the gapped edge and is analytic, with a finite m → 0 limit.
  - On NN-type IR bands, c₄ grows mildly as m falls (×2.1 from m = 1 to 0.3), at most like log(1/ma) ~ 40.
  - Either way it is far below the bounds.

### 3.5 (e) The two-loop check

- **By construction (proved).** (S\*\*) refers to the exact lowest state, so it removes the O(λ²) rows at every order. That includes R19-15's T₂g basketball, +4.027e-9 λ², rechecked here (N = 20, identical to the archive) and confirmed by vR19-15 item 3. It is "by construction" in exactly the sense vR19-15 item 4 used.
- **O(λ), at fixed physical mass, leaves all six rows unchanged (proved, sketch; not checked numerically).**
  - The Hartree energy is (λ/8)∫G(x; h)². After the mass counterterm, the second variation is (λ/4)(δG)².
  - δG(p) is the linear response of the scalar ⟨φ²⟩ to a traceless h. By cubic symmetry it has no p⁰ term. Its first term is Σ_a e_aa p_a² = O(p²); for example it is nonzero for face1, with weight q²/2.
  - So (δG)² = O(p⁴), and none of the six rows moves. This extends R19-15's q⁰ result (G′(0) = 0) to the speed rows.
- **The tunings (S\*\*) replaces are radiatively unstable.**
  - Shear rows: refereed in one model (vR19-15 item 5).
  - Speed rows: suggested, since the O(λ²) basketball is not a single-momentum functional at q ≠ 0.
- **Analyticity at two loops (suggested).** Π_vac − T₂ = p⁴∫ρ_TT(s)ds/[s²(s − p²)] (subtracted dispersion relation). For a stress two-point function the massless spectral weight is ρ_TT(s) ~ s² up to logs, so T₂ exists and the remainder is O(p⁴ log p) at every order.

### 3.6 Non-lowest states: the inherited risk, sharpened (suggested; count once with R19-15 §3.4)

- (S\*\*) subtracts the response of the true lowest state. A state with different vacuum structure, such as the electroweak-symmetric phase where fermion masses ∝ ⟨φ(T)⟩ ≈ 0, keeps an unsubtracted shear Δμ ≈ c₁Σm·a.
- From R19-11/R19-15: Δμ ~ 5e-19 per cell (Wilson-Dirac) or ~4e-36 (twisted mass).
- In R9-9's normalization (m_g²a² = 16π|μ|, conditional on the dynamical-metric reading, vR19-11 item 4): |m_g| ~ 6e10 GeV or ~1.7e2 GeV. Compare H(T ≈ 160 GeV) ~ 1e-14 GeV (RECALLED standard radiation era).
- As energy-density scales, Δμ/a⁴ ~ (3e14 GeV)⁴ or (2e10 GeV)⁴, far above T_EW⁴.
- **Sign (checked from refereed numbers; the reading is suggested).** The gravitating shear in the symmetric phase is Δμ = μ(m ≈ 0) − μ(m_SM) ≈ −(∂μ/∂m)·m·a, so its sign is minus the sign of the row slope.
  - At R19-11's 0⁺ root edges the SM residuals are μ_E = +4.70e-19 and μ_T2 = +1.204e-19 (`C5_R19-15_report.md:180`; A = 3.496e-19 confirmed by vR19-15 item 5). So Δμ = −4.70e-19 and −1.20e-19: **tachyonic in both channels.**
  - With twisted mass (same table, `:181`): Δμ_E = −4.38e-36 (tachyonic) and Δμ_T2 = +2.3e-39.
  - Under (S\*\*) the edges are free, so the slope sign is a law choice. But |Δμ| ≲ (Ha)²/16π ≈ 2e-67, which is what |m_g| < H at T ~ 160 GeV needs, requires the rows to be mass-independent to that level. That is a tuning of the same kind R19-11 priced (a "mass-blind law needs ~14–17 more conditions", `TESTS:7821`).
- **Consequence (suggested, not computed).** Throughout the symmetric phase the tensor modes have |m_g| ≫ H.
  - If tachyonic (as at the root edges): exponential growth at a rate ~1e10 GeV, about 1e24 e-folds per Hubble time. That is observationally catastrophic: a conflict, conditional on the dynamical-metric reading.
  - If massive: super-horizon tensor modes would oscillate and decay, erasing the inflationary tensor background, so the prediction would be r_obs ≈ 0.
- This is a definite, in-principle falsifiable consequence of the fixed-state clause. It argues against reading (S\*\*) as "non-predictive". It is a candidate falsifier or conflict that the supervisor may want pre-registered. Variants that subtract the instantaneous state's vacuum part are R19-14's (S_V)/(S_ad) territory, with their own signalling questions.

### 3.7 (f) The new bill (reading; per (spin, |q|) class unless stated)

| row (R19-12 table, `C5_R19-12_report.md:265-276`; vR19-12 item 4) | before | under (S\*\*) |
|---|---|---|
| Ξ_T2g, Ξ_Eg, μ_E, μ_T2 (b_s, b_f, r, a) | 4 equalities | 0: clause |
| face1, face2 (w_d, w_o signed) | 2 equalities | 0: clause |
| photon window (b_γ) | 1 selection | 0: b_γ freed |
| LV tadpole | 1 (or 0 numbers under (d-i)) | 0: (S\*\*) ⊇ (S\*) removes the lowest state's one-point anisotropy (R19-15 suggested) |
| charged-matter cones e, u, d | 3 (κ_e, κ_u, κ_d) | 3 |
| photon to neutral/graviton cone | 1 (κ_γ, or Σ = 0) | 1 (κ_γ, or Σ = 0 paid by the freed b_γ: R19-12 route B, bracketed) |
| CC | 1 (P51) or 0 numbers under (S) | 0 numbers: (S) ⊂ (S\*\*); growing-lattice caveat inherited (R19-10 OPEN) |

- **Totals.**
  - **4 equalities + CC-by-(S)** per class, against 11 + window + CC (route A, vR19-12).
  - **10** per species (17 before); **2** in the q²-correlated basis (9 before).
- **Bridge clauses.** (S\*\*) (replacing (S) and (S\*)), N_red and W1-weight; (d-i) is needed only for non-lowest states. That is three clauses for the lowest state, with zero numbers.
- **Still outside the bill (listed):**
  - §3.6's non-lowest-state shear;
  - matter's own graviton-loop speeds (R11-1(b), prescription-scoped);
  - mixed O(Ge²) two-loop terms;
  - W± and the non-abelian sectors;
  - exact W1 for the photon (R19-9 OPEN);
  - the E2 extension;
  - the O(h²∂²) completion of the clause.

### 3.8 Prices (named, not adopted)

- **P-R19-19a (new): (S\*\*₀).** "The law's lowest state contributes nothing to the gravitating source through second order in metric derivatives, at linear order in h."
  - Zero numbers; one clause. It contains P-R19-15a (S\*) and P-vac′ (S).
  - Gates: source/action identification (`AX:187`); "A law privileges no states" (`AX:94`), counted once with (S).
  - Buys: all six graviton-cone rows, the tadpole and the CC for the lowest state; frees seven knobs.
- **P-R19-19b (optional):** a Z rule, if the Lorentz-invariant-keeping variant is wanted. It changes no row, only the induced G.
- **P-R19-19c (open):** the nonlinear (O(h²∂²)) extension, and the non-lowest-state prescription (§3.6).
- No axiom text changes.

---

## 4. Against the FIXED readings (`TESTS:8040-8045`)

| reading | clause | status |
|---|---|---|
| **CONE-PRINCIPLE** | stated, local | met (proved, §3.1) |
| | number-free | met (Z := 0) |
| | non-signalling | met at linear order (proved). Nonlinear: not analyzed |
| | zeroes all six rows, every species and mass | met by construction (Lemma R), given that T₂ exists (refereed analyticity; checked NN/U) |
| | O(q⁴) remainders below bounds | checked for NN/U (margin ≥ 3e65 against GW170817; E_QG,2 ≥ 5e18 GeV). The SM envelope is suggested |
| | checked | yes, in the sense above |
| **TAUTOLOGY-OR-CONFLICT** | equivalent to assuming the answer, non-predictively | Lemma E (proved): the whole cone content of (S\*\*) is "the six rows are zero for the exact vacuum" (plus 25 off-shell conditions). **But** five of the six are Ward conditions any local Bianchi-consistent source must meet (Lemma G), and §3.6 is a definite consequence. Needs the referee |
| | conflict with W1, weight-1, Bianchi | none found. W1: the stress operator is untouched. Weight-1: Lemma L concerns the one-point weight, which is unchanged. Bianchi: the linear defect improves from O(p) to O(p⁵) |
| **OPEN** | otherwise | not the literal outcome |

**Worker reading: CONE-PRINCIPLE on the letter, by construction.** This is the same type of verdict vR19-15 item 4 gave (S\*). Literal first (`TESTS:7124`).
- **For the referee.** Lemma E supplies the "equivalent to assuming the answer" half of TAUTOLOGY. Lemma G sharpens what is assumed:
  - **1 row (isotropic speed) is pure stipulation.** Under SPATIAL-only gauge invariance it is 2 rows.
  - **5 rows** are the graviton's Ward identity, imposed by subtraction because lattice matter cannot supply W2.
- **Against the expectation (`TESTS:8046`).**
  - "CONE-PRINCIPLE on the letter … renormalization condition dressed as a principle" holds.
  - "The bill drops to the charge block plus the CC" holds: 4 + CC per class.
  - **New 1:** most of the "dressing" is a Ward identity, not Lorentz invariance.
  - **New 2:** the item's TT-only wording must become full-tensor.
  - **New 3:** the fixed-state clause carries a potentially decisive pre-crossover graviton-mass consequence.

## 5. Strong-word check

- **"Proved"** is used for:
  - the locality, covariance and number-freeness of the clause;
  - Lemma R (the rows depend on T₂ only);
  - Lemma E;
  - the consequences of Lemma G;
  - linear non-signalling;
  - matter rows untouched;
  - the O(λ) sketch.
  
  All are short and unrefereed.
- **"Checked"** is used for:
  - Lemma G's dimensions (exact SVD ranks, with the Einstein-Hilbert kernel and the ε·ε·t family as controls);
  - the NN/U Taylor structure, the O(p⁴) remainder and the R17-4 rows (two N at m = 1 identical);
  - the reruns of the archived runners.
- **"Every species and mass"** means every species whose vacuum response has a degree-2 Taylor polynomial at p = 0. That covers all of R19-11's root content (refereed analyticity). It covers the lowest state only.
- **"Non-signalling"** holds at linear order only.
- **"Bianchi"** means the linear Ward identity of the vacuum response, improved to O(p⁵), not exact. Nonlinear Bianchi is not addressed.
- **"Ward violation"** for the five rows assumes the N-type graviton's gauge group is the full linearized diffeomorphism group. Under projectable lapse it is four rows.
- **§3.6** is an order-of-magnitude, suggested consequence, conditional on the dynamical-metric normalization, and its sign is undetermined.
- **Not claimed:**
  - derivation of (S\*\*) from the axioms;
  - box-law O(q⁴) coefficients;
  - two-loop q ≠ 0 rows;
  - that the charge block can be paid by the freed edges (R16-1/R16-10 suggest not with subluminal edges).

## 6. For the referee

1. Lemma G (`r1919_gauge.py`). Is the invariant space complete? Are the Ward conditions right, with lower p contracting the upper index? Does the N-type graviton carry FULL or SPATIAL gauge symmetry?
2. The full-tensor correction to the item's TT-only wording.
3. Lemma E and the TAUTOLOGY ruling. Does a clause whose five conditions are Ward identities, plus one LI renormalization condition, count as "non-predictive"? Compare vR19-15 item 4, `TESTS:6015-6016` and `C4_V3_referee.md:29`.
4. §3.6: the pre-crossover shear mismatch is tachyonic at R19-11's root edges. Does it count against the clause? It concerns non-lowest states, so it is outside the six rows' letter. It applies equally to (S\*) (vR19-15), so count it once. Avoiding it needs a mass-independence tuning to ~2e-67. This may decide the clause.
5. The O(p⁴) bounds and the SM envelope.

## 7. Files (`S/`)

- `r1919_gauge.py` → `r1919_gauge.out`: Lemma G (invariant kernels; FULL, SPATIAL and NONE Ward classes; row images; Einstein-Hilbert and ε·ε·t controls).
- `r1919_taylor.py` → `r1919_taylor.out`: NN/U direct-grid Π(ω, q); rows; Taylor remainder; on-shell c₄ (m = 1, 0.5, 0.3).
- `r1919_bounds.py` → `r1919_bounds.out`: Lemma G applied to the NN/U rows; O(p⁴) bounds against the comparators.
- `arch17_4/basis.py` → `basis_recheck.out` (identical to the archive).
- `arch19_15/r1915_d_loops.py` → `r1915_d_loops_N20_recheck.out` (identical to the archive except runtime).
