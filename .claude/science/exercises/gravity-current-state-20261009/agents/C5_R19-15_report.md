# C5 R19-15 report: the shear rows as a graviton mass. Does any part of the bridge remove them, or are they a ~1e-98 tuning?

**Author and provenance.** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. Run on 2026-10-13 from 05:23Z to about 05:46Z. I edited no repository file and downloaded nothing.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`
- `S/` = `scratchpad/C5/R19-15/`. My scripts and `.out` files are in `S/run/`. `S/arch14_3/` holds unmodified copies of `P/scripts/C5/R14-3/*.py`.

**Machine use.** `OMP_NUM_THREADS=2`. Load was 6–7 from other jobs. The longest run took 80 s.

**What I read.**
- `AX`, in full.
- `P/TESTS.md`:
  - the C5 method (`:2302-2319`) and my item (`:7826-7858`);
  - the entries and verdicts for R14-3 (`:4830-4844`, `:4915-4923`), R16-9 (`:5373-5408`, `:5668-5684`), R16-13 (`:5595-5622`, `:6088-6104`, `:6146-6156`), R17-11 (`:6230-6253`, `:6319-6333`, `:6590-6600`), R17-13 (`:6365-6383`, `:6654-6662`, `:6802-6805`), R18-6 (`:6684-6712`, `:6826-6843`, `:6969-6979`), R19-5 (`:7319-7350`, `:7470-7487`, `:7747-7752`), R19-6 (`:7397-7426`, `:7569-7577`, `:7663-7672`), R19-9 (`:7546-7568`, `:7761-7769`) and R19-11 (`:7630-7651`, `:7811-7822`);
  - lanes RV4 (`:2156-2235`) and RFW (`:2237-2300`), and R17-3's verdict line (`:6015`).
- `P/PRICE_NOTE.md`: P0 (`:162`, revised at `:356-361`), the V3 cells (`:286-295`) and P13 (`:367`).
- `P/agents/`:
  - `C5_R19-11_report.md` in full, and its referee verdict, which appeared during my run (`scratchpad/C5/ref_R19-11/REFEREE_VERDICT.md`, CONFIRMED WITH CORRECTIONS, reading OPEN);
  - `C5_R14-3_report.md` and `C5_R14-3_referee_verdict.md`;
  - `C5_R17-11_report.md` (`:75,123,252-253`) and `C5_R17-11_referee_verdict.md`;
  - `C4_V1_referee.md`, `C4_V2_referee.md:9-12` and `C4_V3_referee.md:25-29`.

**Runner rechecked before use (checked).** My copy of R14-3's `prof.py` gives:
- G(1.4): μ_E = +3.525431673e-3 at m = 1 and +4.252012416e-3 at m = 0.3 (IBP form, N = 64). R14-3 had +3.52543170e-3 and +4.25201261e-3 (`C5_R14-3_report.md:105`).
- The NN scalar at m = 1: +1.970388642e-3. V3's comparator is +1.97038864e-3 (`PRICE_NOTE.md:290`).

**Labels.**
- **proved:** a complete argument under the stated hypotheses; unrefereed.
- **checked:** numerics run here.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** an outside reference point.
- **RECALLED:** quoted from memory.

---

## 0. In plain words

1. **What μ is (proved; checked).** The shear rows are the second derivative of the vacuum's zero-point energy density under a uniform traceless strain. In other words, they are the shear stiffness of the lattice vacuum.
   - The archived formula is exactly that second derivative along the SF strain flow (Lemma H). Lemma H is R9-2's Liouville formula; this run checks it by integrating the flow.
   - Two pieces enter: a contact ("seagull") term and a pair-creation ("bubble") term.
   - In the continuum the two pieces cancel. That cancellation is what makes a uniform strain a mere relabelling of coordinates.
   - On the lattice they do not cancel. The lattice vacuum behaves like an elastic **solid** with two cubic shear moduli. A Lorentz-invariant vacuum is a **fluid** (p = −ρ) with zero shear modulus.
2. **No piece of the registered bridge removes μ (proved, each step bounded to its stated class).**
   - (S), (d-i), N_red and the weight-1 clause are all rotation-invariant (O(3)). They can only shift μ_E and μ_T2 by the same amount, so they never touch the cubic anisotropy A = μ_E − μ_T2.
     - (d-i)'s receiver is built with zero traceless stress (E^TL = 0), so it cannot absorb any anisotropic stress.
     - The weight-1 clause acts through ∂·ξ, which vanishes for a traceless strain.
   - Exact W1 leaves the rows unchanged. μ depends only on the band and the strain flow, and R19-5's referee confirmed that the rows are unchanged under the exact completions.
   - A ≠ 0 at every point computed: the natural sizes, the Dirac slopes, and the SM residuals of the m → 0⁺ law.
3. **Without a new clause, μ = 0 is a P0-level tuning that does not survive higher orders (checked in one model).** R19-11's spectrum-tuned law needs its knobs fixed to about 1e-98. Here I add an interaction check.
   - At O(λ), with the unstrained physical mass held fixed, the correction to the shear Hessian vanishes exactly. This is a correction to the naive expectation: at this order the interaction only renormalizes the mass.
   - At O(λ²), the momentum-conserving "basketball" diagram gives a nonzero shear. That includes the scalar T₂g row, which is zero at one loop for every edge and every mass by Liouville's theorem: μ_T2⁽²⁾ = +4.03e-9 λ² (NN scalar, m = 1).
   - So a one-loop zero must be re-tuned at every order.
4. **One new clause does work: (S\*).** It reads: "in every uniform static background, the law's lowest state contributes nothing to the gravitating source."
   - It is (S) extended from the constant e₀ to the whole uniform-deformation energy e₀[H(h)].
   - It fixes no numbers. It acts point by point (ultralocal), so it adds no signal at linear order. It restores the zero-derivative Ward identity. It holds at every loop order and for every species and mass, because it refers to the exact lowest state.
   - It contains (S). It is the lattice stand-in for "the vacuum gravitates as if it were Lorentz invariant".
   - It is a definition-type clause:
     - it has the same logical type as (S), which R17-3's referee ruled "an added source/action principle", number-free, "not a disguised tuning" (`TESTS:6015,6021`);
     - it is also the full-interacting extension of R₀, which C4's V3 referee called "explicitly tautological" as a matter coupling (`C4_V3_referee.md:29`).
5. **Limits of (S\*) (suggested).**
   - It covers the lowest state only.
   - A sea that differs from the true vacuum still has unsubtracted shear. Examples are the plasma before the electroweak crossover (about 5e-19 per cell with Wilson-Dirac, about 4e-36 with twisted mass; these are R19-11's numbers) and R19-10's insertion excitations, if those exist.
   - A matter-side "relabelling" principle does not help. That means a strain coupling that preserves the spectrum: Liouville flows, or RV4 S2's density-of-states seagull. The two-loop check shows it fails once interactions conserve momentum.
6. **Reading: STRUCTURAL-ZERO on the letter, through a new priced clause P-R19-15a = (S\*).**
   - Within the registered bridge, the content of TUNING-ONLY is shown at worker level: no piece forces μ = 0, the zero needs about 1e-98, and it is unstable at O(λ²). That content needs a referee before it can be recorded.
   - The referee must also rule whether a definition-type source clause counts as a "principle" in this reading. The item's own examples suggest that it does (`TESTS:7837`).

---

## 1. Class, hypotheses, exclusions (stated before any title)

- **Rows.** μ_E and μ_T2 as archived: the one-loop static TT response of the supplied zero-point vacuum under the SF strain flow, at q → 0.
  - Scalars: R14-3's closed form (`C5_R14-3_report.md:86-93`; `prof.py:6`).
  - Dirac and vector: the same SF flow applied to each species' vacuum energy per mode, −(N_c/2)E for a Dirac sea (`C5_R16-13_report.md:90-97`; `TESTS:6659`).
  - The rows read as a graviton mass only through R9-9's normalization, m_g²a² = 16πμ. That holds only for a supplied dynamical metric (`PRICE_NOTE.md:22`; `vR19-11` item 4).
- **Bridge class (C-box-E).** (S): λ = −κe₀[H] (`TESTS:6686`); (d-i): Q_ν = ∇^μ(W h_μν) (`TESTS:6319-6331`); N_red, the net gravitating stress (`TESTS:6971`); W1-weight, the weight-1 one-point source (`TESTS:7569-7575`); exact W1 completions (R19-5 and R19-9).
- **Model for probe (d).**
  - The NN lattice scalar, ε² = m² + Σ2(1 − cos k_i), with an on-site (λ/4!)φ⁴ vertex.
  - Strain acts on the one-particle dispersion by the SF pullback ε_t = ε∘Φ_t. The vertex is strain-blind (for TT in the unimodular parametrization √g = 1, so a √g factor would change nothing).
- **Excluded.**
  - Pairing, which needs matched spectra (C4 RP, `PRICE_NOTE.md:404`; O3).
  - Superluminal edges.
  - Changes to the speed rows (Ξ, face).
  - Gauge-field interactions at two loops (not computed).

## 2. Prior art (each counted once)

- **V3 / PRICE_NOTE v6 2a (refereed).**
  - Free local matter has μ_E ≠ 0.
  - μ_T2 = 0 for single-band local coupling, because the T₂g flow is divergence-free (`PRICE_NOTE.md:290-295`; `TESTS:2160-2163`).
  - "√g·Λ enters E_g and T₂g equally" (`C4_V3_referee.md:27`).
- **RV4 (refereed: FAIL, bounded).**
  - No periodic momentum field makes every shear flow divergence-free (the conformal Killing obstruction).
  - Compact Ward covariance would force μ_E = μ_T2, but it is incompatible with the field-independent bulk response (`TESTS:2212-2219`).
  - S2's density-of-states seagull is "definition/R₀-type" (`TESTS:2225`).
- **RFW F2 (refereed: bounded FAIL).** "No translation-covariant completion makes the action gauge invariant through O(κ²)" in the K2 scalar class (`TESTS:2269`).
- **P13 / R₀.** The vacuum-referenced coupling rule gives μ = 0 "by definition"; it is not basis-free or derived (`PRICE_NOTE.md:367`). C4 V3's referee: extended to the exact strained ground energy of the interacting theory, R₀ is "explicitly tautological" (`C4_V3_referee.md:29`). Rule R is "conditional design data, not a principle" (`C4_V1_referee.md:9`).
- **R17-3 / R17-7 on (S).** "The number-free rule C = E₀[H] tracks radiative corrections by definition. It is an added source/action principle … So the result is OPEN, not TUNING" (`TESTS:6015`).
- **R14-3 and its verdict.** The μ_E formula, the IBP form, analyticity in m², and the subluminal shear zero at fixed mass (`TESTS:4915-4923`).
- **R16-9, R16-13 and R17-13.**
  - No subluminal shape zero for μ_E was certified (R16-9 verdict OPEN).
  - The Wilson-Dirac μ_T2 ≠ 0 (R16-13).
  - μ_T2 can be zeroed by one Dirac-edge tuning, and depends only on the band and SF (`TESTS:6659,6802-6805`).
- **R17-11 and its verdict.**
  - (d-i) is consistent in class 𝒟.
  - "anisotropic vacuum responses are not absorbable, because E^TL = 0 is imposed" (`C5_R17-11_report.md:252-253`).
  - "the TT/shear walls are … correctly left unchanged" (`vR17-11` item 4; `TESTS:6326,6597`).
- **R18-6 and its verdict.** N_red is a new completion; the net-source bridge is three clauses with zero numbers (`TESTS:6969-6979`).
- **R19-5 and its verdict.** Exact W1 ≠ W2. Exact completions exist for the massive species. "The scalar and Dirac rows are unchanged" (`TESTS:7747-7750`).
- **R19-6 and its verdict.** Lemma L, ⟨L_ξ𝔜⟩ = (w − 1)⟨(∂·ξ)𝔜⟩, confirmed. Reading OPEN (`TESTS:7571,7663-7672`).
- **R19-9 (worker).** An exact photon completion; the rows re-solve with knob shifts ≤ 2.9e-6 (`TESTS:7761-7769`).
- **R19-11 and its verdict.**
  - Shear residuals of the m → 0⁺ law: μ_E = 4.70e-19 and μ_T2 = 1.204e-19.
  - Bound |μ| ≲ 3.20e-98 at 100 Hz, conditional on the graviton bridge.
  - The IFT law is "conditionally correct" (`REFEREE_VERDICT.md` items 4-5).
- **P0.** Two TT counterterms, each leaving ≤ 5.7e-99 of natural size (`PRICE_NOTE.md:162,356-361`).

---

## 3. Results

### 3.1 (a) μ as a vacuum strain response

**Lemma H (proved; this is a restatement of R9-2's Liouville formula μ = −⟨(div v)(v·∇ε_vac)⟩, quoted at `C5_R16-13_report.md:93-96`, so count it once). What is new here is the flow-integrated check and the seagull/bubble split.**
- **Setting.** A separable one-band law ε² = m² + Σg(k_i), with energy-current momentum f = ∇(ε²/2) (`prof.py:2-6`). The unit E_g strain h = diag(1, −1, 0) acts by the SF flow v = ½h·f. Let Φ_t be its time-t map, and let e(t) = ½⟨ε∘Φ_t⟩ be the zero-point energy density of the strained law.
- **Claim.** e″(0) = −(1/8)⟨(f′_x − f′_y)(f_x² − f_y²)/ε⟩. This is exactly R9-2's closed form for μ_E (`prof.py:6`).
- **Proof.**
  - d²/dt²[ε∘Φ_t] at t = 0 equals v·∇(v·∇ε).
  - Periodic integration by parts gives ⟨v·∇(v·∇ε)⟩ = −⟨(∇·v)(v·∇ε)⟩.
  - With ∂_iε = f_i/ε: v·∇ε = (f_x² − f_y²)/(2ε) and ∇·v = (f′_x − f′_y)/2. ∎
- **T₂g.** For h_xy = 1 the flow v = ½(f(k_y), f(k_x), 0) has ∇·v = 0. So Φ_t preserves the measure, and e(t) = e(0) for **all** t, not only to second order (Liouville). This reproduces V3's μ_T2 = 0.
- **Split.** e″(0) = seagull + bubble.
  - Seagull: ⟨(f_x²f′_x + f_y²f′_y)/(4ε)⟩, the second-order change of the dispersion.
  - Bubble: −⟨(f_x² − f_y²)²/(8ε³)⟩, the q = 0 pair-creation term with denominator 2ε.
  - **Continuum.** For f = k on ℝ³ with a rotation-invariant regulator, the linear traceless flow preserves volume exactly, so the two pieces cancel. That cancellation is the relabelling Ward identity.

**Checked** (`run/r1915_a_hessian.py`; outputs `r1915_a_hessian_N64.out` and `_gw_N256.out`, `_gw_N400.out`):

| law, m | closed form μ_E | e″(0) from the integrated flow (Richardson) | seagull | bubble | T₂g: e(0.2) − e(0) |
|---|---|---|---|---|---|
| NN, m = 1 (N = 64) | +1.970388642e-3 | +1.970388723e-3 (8e-11) | +4.287693e-3 | −2.317304e-3 | 0 |
| G(1.4), m = 1 (N = 64) | +3.525432e-3 (IBP) | +3.523893e-3 (quadrature 1.6e-6) | +1.5598e-2 | −1.2074e-2 | −1.3e-9 |
| G(1.4), m = 0.3 (N = 64) | +4.252012e-3 | +4.250350e-3 | +2.0268e-2 | −1.6018e-2 | −1.4e-9 |
| G_w(1.4, 0.349416), m = 0.3 (N = 400; R14-3's root) | +3.3e-10 (IBP) | −1.7e-8 | +9.795216e-3 | −9.795229e-3 | −4e-13 |
| G_w(1.4, 0.2), m = 0.3 (N = 400) | −2.514e-4 (IBP) | −2.358e-4 (N = 256: −4.02e-4; converging) | +9.0824e-3 | −9.3182e-3 | +1.6e-10 |

- The narrow-step G_w laws converge slowly in N for the flow integration, because their steps are sharp. The closed form and the flow agree as N grows. At R14-3's root, seagull and bubble cancel to 1e-6 relative.
- **Dirac and vector rows.** By SF's definition they are the same Hessian of the sea energy, −(N_c/2)E per mode (`C5_R16-13_report.md:90-97`). So the identification holds by definition; it was not re-checked numerically here.
  - For Dirac, the T₂g flow is not divergence-free: ∇·v_T2 = H_xy = W′_xW′_y ≠ 0, because the Wilson mass couples directions. That is R16-13/R17-13's Wilson-Dirac μ_T2 mechanism, so Liouville protects only separable bands.

**Answer to (a).**
- μ = ∂⟨T_TT⟩/∂h_TT, which by Hellmann–Feynman (∂e/∂h = ⟨∂H/∂h⟩) is the full second derivative of the vacuum energy, seagull included.
- The only contact term to subtract is the Ward-identity (tadpole/CC) one. For TT strain in this unimodular flow parametrization it is zero (`C4_V3_referee.md:27`: √g·Λ "vanishes in an exactly unimodular exponential parametrization").
- So μ is the vacuum's violation of the relabelling Ward identity.
- If "contact term" meant the seagull, the answer is no. The seagull is part of the row, and the bubble alone (−2.32e-3 for NN at m = 1) is not the row.

**Reading.**
- The lattice vacuum is an elastic solid with cubic shear moduli: μ_E is of (c₁₁ − c₁₂)/2 type and μ_T2 of c₄₄ type.
- In GR a medium with shear rigidity gives tensor modes a mass. **Comparator (RECALLED):** solid inflation, Endlich–Nicolis–Wang 2013.
- A Lorentz-invariant vacuum, ⟨T_μν⟩ = −ρg_μν, is a fluid with zero shear modulus, so μ = 0 there by symmetry.
- **Suggested.** In the same function e(h), the first-order trace coefficient is the vacuum pressure. R17-7/R17-11's enthalpy W = e₀ + p₀ is that coefficient's deviation from the fluid value. So W and μ are the first- and second-order Taylor coefficients of one non-fluid vacuum potential. I did not compute W in R17-7's normalization.

### 3.2 (b) Each bridge piece against μ

**Cubic decomposition (proved).**
- Traceless symmetric strain decomposes under O_h as E_g (2 components) ⊕ T₂g (3 components). Under O(3) it is one l = 2 irrep.
- So an O(3)-covariant contribution to the static quadratic response has equal E_g and T₂g coefficients (with equal-norm channels, as in `C4_V3_referee.md:27`).
- It therefore moves only the singlet S = (2μ_E + 3μ_T2)/5, never the anisotropy A = μ_E − μ_T2.
- Zeroing both rows needs A = 0 first.

**A ≠ 0 at every computed point (checked; `run/r1915_b_cubic.out`):**

| point | μ_E | μ_T2 | A | \|A\| / 3.2e-98 |
|---|---|---|---|---|
| NN scalar, m = 1 | +1.97e-3 | 0 | +1.97e-3 | 6e94 |
| Dirac slope c₁ per field at the 0⁺ root | +1.069e-2 | +2.739e-3 | +7.95e-3 | 2.5e95 |
| SM residuals of the 0⁺ law (vR19-11 item 4) | +4.70e-19 | +1.204e-19 | +3.50e-19 | 1.1e79 |
| the same, with twisted mass | +4.38e-36 | −2.3e-39 | +4.38e-36 | 1.4e62 |

Taking each bridge piece in turn:

- **(S): λ = −κe₀[H], a constant.**
  - It enters as −e₀√g. That is zero for TT strain in the unimodular parametrization, and equal in E_g and T₂g otherwise.
  - Effect on A: none (proved).
  - It has no free coefficient, so it cannot be adjusted to cancel S either.
- **(d-i): Q = ∇(W h_μν).**
  - It absorbs only the isotropic stress W h_μν.
  - Its receiver, the E-sector, has E^TL = 0 imposed. So "anisotropic vacuum responses are not absorbable" (`C5_R17-11_report.md:252-253`, confirmed by `vR17-11` item 4, "TT/shear walls … unchanged").
  - Effect on μ: none (proved, by R17-11's confirmed uniqueness lemma inside 𝒟).
- **N_red.** It subtracts (V − e₀)g_μν (`TESTS:6971-6976`), which is isotropic. Effect on A: none (proved).
- **W1-weight (Lemma L, `TESTS:7571`, confirmed `TESTS:7665`).**
  - ⟨L_ξ𝔜⟩ = (w − 1)⟨(∂·ξ)𝔜⟩.
  - A uniform traceless strain is generated by ξ_i = ½h_ijx_j, so ∂·ξ = ½ tr h = 0. The weight term then vanishes for every w.
  - So the weight has no effect on the TT channel (proved).
  - More basically, Lemma L assumes that L_ξ is a symmetry. On the lattice a uniform strain is not a relabelling, and that failure is μ itself.
- **Exact W1 (R19-5 and R19-9).**
  - By Lemma H, μ depends only on (ε, SF) and contains no vertex. The same holds for μ_T2 (`TESTS:6659`).
  - Exact completions differ from U, UD and VW by identically conserved superpotentials (Lemma I, `TESTS:6608,6800`; `TESTS:7325`), which vanish at q = 0. The referee recorded that "the scalar and Dirac rows are unchanged" (`TESTS:7750`).
  - The q = 0 Ward identity that would force μ to the fluid (CC) value is a second-order (O(h²)) diffeomorphism identity. Two refereed results exclude it:
    - RFW F2 excludes it for local translation-covariant completions in the K2 scalar class (`TESTS:2269`);
    - RV4 S1 finds it incompatible with the field-independent bulk response (`TESTS:2219`).
  - Exact W1 conserves the first-order stress. It does not supply the second-order identity.
  - Effect on μ: none (proved for the cited classes).
- **Pairing (count once).** Exact cancellation needs matched boson–fermion spectra (R0, R2, R4, R6; `PRICE_NOTE.md:404`). The SM spectrum is not matched.

**Answer to (b).** No piece of the registered bridge forces μ_E = μ_T2 = 0 (proved, bounded as listed).

### 3.3 (c) The minimal principle that does, and its cost

**(S\*) stated.**
- The rule: "In every uniform static background h, the law's lowest state contributes nothing to the gravitating source." Equivalently, the gravitating source excludes −∂/∂h[√g·e_vac(h)] at every order in uniform h, where e_vac(h) is the ground-state energy density of the strained law H(h).
- For a slowly varying h(x), the subtraction is applied pointwise. It is the zero-derivative term of the vacuum effective action.

**What it does (proved by construction; checked through Lemma H).**
- It removes the whole uniform-deformation potential of the vacuum:
  - the constant e₀, which is (S);
  - the first-order trace, which is the lowest state's W (suggested in §3.1);
  - the second-order TT coefficients μ_E and μ_T2, for every species, at every mass and every loop order, because it refers to the exact interacting lowest state.
- By Lemma H, the subtracted second-order TT coefficients are exactly the archived rows. Nothing at O(q²), meaning the speed and face rows, is touched.

**Cost, item by item.**
- **Numbers: 0.** e_vac(h) is fixed by the law.
- **Signalling: none at linear order (proved, short).**
  - The subtraction is ultralocal in g_μν(x), with no derivatives and no global variable.
  - The linearized TT equation becomes GR's: the generated mass term and the subtracted term cancel identically.
  - No λ(t)-type global channel appears. That channel is the R15-1 mechanism, and here the Lemma-S parameter stays at its GR value.
  - Beyond linear order the subtraction is still ultralocal (suggested).
- **Bianchi (suggested; sketch).**
  - Before (S\*), the vacuum's static response breaks the O(q) Ward identity by q_iμ_ijkl h_kl.
  - After (S\*), the breaking starts at O(q³), i.e. relative size (qa)². That is the speed-row level, the same scale as P13's O(λε) Ward defect (`PRICE_NOTE.md:367`).
  - The total gravitating source is conserved at zero-derivative order.
- **Sentences.** It contains (S), so it can replace (S): the bridge stays at four clauses, (S\*), (d-i), N_red and W1-weight.
  - **Suggested:** for the lowest state (S\*) also removes W, so in C-box-E (d-i) is needed only for W changes across crossovers. That would make three clauses.
- **Bill effect (reading).**
  - The two shear rows are paid at every mass by one clause. R19-11's 6 + 1 knobs become 4 + 1 + (S\*).
  - P0's shear half ("5.7e-99") is replaced by a clause.
  - The speed rows still need tuning, and the R16-2 comparator issue remains (`vR19-11` item 6).
- **Logical type.** Like (S), it subtracts the very c-number under test. So it is a definition-type principle: number-free and radiatively exact by construction, not derived from the axioms.
  - R17-3's referee accepted this type for (S) as "an added source/action principle", "not a disguised tuning" (`TESTS:6015,6021`).
  - Its matter-side twin, R₀, was called "explicitly tautological" (`C4_V3_referee.md:29`).
  - I report this tension rather than resolve it.
- **Comparator.** In continuum QFT with a Lorentz-invariant regulator, μ = 0 by symmetry, with no clause needed. (S\*) imposes on the gravitating source what Lorentz invariance would give, at zero derivatives only. This matches the item's expectation.

**Matter-side alternative: a spectrum-preserving strain coupling. It fails at two loops (checked).**
- This covers Liouville flows, RV4 S2's density-of-states seagull, and P13.
- Such a coupling makes every single-momentum functional of ε_t strain-blind, which is the T₂g mechanism.
- But a momentum-conserving interaction is not a single-momentum functional. A nonlinear flow does not preserve k₁ + k₂ + k₃ + k₄ = 0.
- In the model of §1, the O(λ²) basketball gives a nonzero T₂g row even though the one-loop and Hartree parts are exactly T₂g-blind (§3.4).
- So no one-particle relabelling rule protects an interacting vacuum. Only the exact-vacuum subtraction, (S\*), does (checked in the model; suggested in general).

**Extension, not tested: (S\*\*).**
- The rule: the vacuum's *entire* linear response to the metric does not gravitate, so gravity is sourced only by excitations relative to the vacuum in the actual background.
- It would also pay the four speed and face rows. Those are vacuum-polarization O(q²) terms.
- Its costs: the subtraction is a retarded, non-local functional, which is causal but power-law for massless loops; it is ambiguous above the pair threshold (ω > 2m); and it removes the vacuum's induced-G terms.
- Labelled suggested. It is outside this item's rows.

### 3.4 (d) Radiative stability under each option

Run `run/r1915_d_loops.py` (N = 20, 28 and 36; converged to ≤ 1e-6 relative from N = 28 to 36; Gauss–Legendre in e^{−2mτ}). Per site, NN scalar.

| channel, m | one loop e″ | O(λ), bare-mass convention | O(λ), unstrained physical mass fixed | O(λ²) basketball |
|---|---|---|---|---|
| E_g, m = 1 | +1.970389e-3 | −5.3473e-5 λ | **0** (proved) | +1.9276e-7 λ² |
| T₂g, m = 1 | 0 (Liouville) | 0 | 0 | **+4.0270e-9 λ²** |
| E_g, m = 0.6 | +2.379222e-3 | −8.2916e-5 λ | **0** | +3.7465e-7 λ² |
| T₂g, m = 0.6 | ~1e-12 (grid) | ~2e-13 | 0 | **+1.0284e-8 λ²** |

**Why O(λ) is zero at fixed physical mass (proved).**
- E(h) = E₀(h; m_b) + (λ/8)G(h)², where G(h) = ⟨1/(2ε_h)⟩. With m_b² = m_p² − (λ/2)G(0) and ∂E₀/∂m² = G/2:
  - E(h) = E₀(h; m_p) − (λ/4)G(0)G(h) + (λ/8)G(h)² + O(λ²);
  - its Hessian at h = 0 is (λ/4)G′(0)², and G′(0) = 0 by cubic symmetry.
- So the one-loop zero is not detuned at O(λ). This corrects the naive expectation.
- **Checked** (`run/r1915_d_hartree.py` → `r1915_d_hartree.out`; NN scalar, m_p = 1, N = 28):
  - with m_b² = m_p² − (λ/2)G(0), the shift μ − μ₀ is −3.03e-9, −7.56e-10 and −1.88e-10 at λ = 0.04, 0.02 and 0.01. That scales as λ², with ratio −1.89e-6 (an O(λ²) remainder);
  - at fixed bare mass the shift is linear: −5.3472e-5·λ.

**Why the T₂g basketball is convention-independent (proved).**
- Any quadratic local counterterm (mass, Z, or a pulled-back hopping) has a vacuum expectation that is a single-momentum functional of ε_t. Such functionals are T₂g-invariant by Liouville.
- So none of them can absorb the basketball's T₂g Hessian.
- The E_g O(λ²) value depends on the convention (sunset-type mass and dispersion renormalization) and is quoted in the bare convention only.

**Under each option.**
- **Registered bridge, tuned zero.**
  - It is detuned by any change of the spectrum at O(c₁ΣΔm·a) ≈ 5e-19 (R19-11; arithmetic confirmed in `vR19-11` item 4).
  - It is detuned by two-loop interactions at ~1e-8 λ² per scalar in the shear rows. That includes the T₂g row, which no one-loop shape knob or quadratic counterterm protects beyond one loop.
  - Each order needs re-tuning at the ~3e-98 level. **Radiatively unstable** (checked in the stated model; for gauge interactions, suggested).
- **(S\*).** Stable at all orders for the lowest state, by construction.
  - **Not covered.** States that are not the lowest state:
    - the sea before the electroweak crossover differs by Δμ ≈ 5e-19 (Wilson-Dirac) or ≈ 4e-36 (twisted mass) per cell. These are R19-11's spectrum-change numbers, counted once; their observational consequence (a pre-crossover TT mass) is not computed.
    - R19-10's insertion excitations (worker, unrefereed). They are lattice-scale quanta, so their anisotropic shear should be O(ρ_ins) (suggested). That would give m_g ~ (Gρ_ins)^{1/2} ≳ 1e30·H₀ ~ 1e-3 eV, against the ~1e-21 eV bound (RECALLED from `vR19-11`). This is the same problem as R19-10's Λ̃, counted once.
- **Matter-side relabelling.** Unstable at O(λ²) (checked, above).

### 3.5 (e) Prices (named, not adopted)

- **P-R19-15a (new; reading): (S\*).**
  - Statement: "the law's lowest state, in every uniform static background, contributes nothing to the gravitating source".
  - It extends (S)'s P-vac′ (`TESTS:5004,6332`) from the constant to the uniform-deformation potential. It has 0 numbers and 1 clause, and it can replace (S).
  - Gates: source/action and physical-observable identification (`AX:187`). It also shares (S)'s reference to a privileged state (`AX:94`, "A law privileges no states"); count that once with (S).
  - Buys: μ_E = μ_T2 = 0 at every mass and order for the lowest state, and P0's shear half.
  - Does not buy: the speed rows, or states other than the lowest.
- **P-R19-15b (suggested; not tested): (S\*\*).** The vacuum's whole linear response does not gravitate. It would buy the speed rows too, at the price of a non-local (retarded) subtraction.
- **No new price for the tuning route.** That is P0 together with P-R19-11a (count once).
- No axiom text changes.

---

## 4. Against the FIXED readings (`TESTS:7854-7857`)

| reading | clause | status |
|---|---|---|
| **STRUCTURAL-ZERO** | a stated principle, existing or new | **existing: none** (proved, §3.2). **New: (S\*)** (§3.3) |
| | number-free | **met** (0 numbers) |
| | non-signalling | **met at linear order** (proved; ultralocal). Beyond linear order: suggested |
| | forces μ_E = μ_T2 = 0 for every species at every mass | **met for the lowest state**, at every loop order, by construction. Not for other states (§3.4) |
| | checked | the identification "rows = vacuum uniform-strain Hessian" is **checked** for scalars (Lemma H; NN agrees with V3 to 8e-11), and holds for Dirac and vector rows by SF's definition (`C5_R16-13_report.md:90-97`). The zero is by construction |
| **TUNING-ONLY** | a *refereed* demonstration within the stated bridge class: μ = 0 needs ~1e-98 tuning and is radiatively unstable | **worker content shown:** no bridge piece forces μ = 0 (proved); the zero needs the IFT law at ~1e-98 (R19-11, conditionally confirmed); unstable at O(λ²) (checked). **Not recordable without a referee** |
| **OPEN** | otherwise | not the literal outcome, if (S\*) counts as a principle |

**Worker reading: STRUCTURAL-ZERO on the letter, through the new priced clause P-R19-15a (S\*).** Literal first, `TESTS:7124`.
- **Why the item admits a new clause.** STRUCTURAL-ZERO admits "existing or new" principles, and the item names a rule of this kind ("the vacuum's static strain response does not gravitate") among its candidate principles (`TESTS:7837`).
- **The decisive question for the referee.** Does a definition-type source clause count as a principle? Precedent cuts both ways:
  - (S) itself was ruled a principle (`TESTS:6015,6021`);
  - R₀ was ruled tautological as a matter coupling (`C4_V3_referee.md:29`).
  - If the referee rules no, the reading becomes OPEN, with the TUNING-ONLY content waiting on a referee.
- **Within the registered bridge,** the TUNING-ONLY content holds at worker level.

**Against the expectation (`TESTS:7858`).**
- "TUNING-ONLY within the current bridge" holds in content.
- "A new principle … could give STRUCTURAL-ZERO … likely the lattice analogue of requiring a Lorentz-invariant vacuum" also holds. Two refinements:
  1. (S\*) need not be a *fifth* clause. It contains (S) and can replace it.
  2. The matter-side form of the same idea, a spectrum-preserving strain coupling, fails at two loops. Only the source-side form survives.
- New to the expectation: the O(λ) shift vanishes at fixed physical mass, so detuning starts at O(λ²).

## 5. Strong-word check

- **"Proved"** is used for:
  - Lemma H (two lines; R9-2's formula, restated);
  - the Liouville invariance of T₂g;
  - the cubic decomposition and the isotropy of the bridge pieces;
  - the weight term vanishing for ∂·ξ = 0;
  - the O(λ) cancellation at fixed physical mass;
  - the convention-independence of the T₂g basketball;
  - linear-order non-signalling of an ultralocal subtraction.

  All are short and unrefereed. The (d-i) and exact-W1 steps rest on refereed results (R17-11 and R19-5), each within its own class.
- **"Checked"** is used for:
  - the Lemma H numerics (NN and G(1.4) tightly; narrow G_w converging in N);
  - the A ≠ 0 table, from archived and confirmed numbers;
  - the two-loop table (converged in N and in τ quadrature).
- **"Every species at every mass"** for (S\*) means the lowest state of any law. It does not cover thermal or inserted states.
- **"Non-signalling"** means at linear order, with an ultralocal subtraction. No nonlinear analysis was done.
- **"Radiatively unstable"** was checked in one scalar model with a strain-blind on-site vertex. For gauge interactions and Dirac seas it is suggested.
- **"Graviton mass"** is used in R9-9's normalization, conditional on the supplied metric bridge (`PRICE_NOTE.md:22`; `vR19-11` item 4).
- **Not claimed:**
  - that (S\*) is derived from the axioms;
  - a numerical check of the Dirac and vector identification with Lemma H (it holds by SF's definition, `C5_R16-13_report.md:90-97`);
  - (S\*\*)'s consistency;
  - observational consequences before the crossover.

## 6. For the referee

1. **Lemma H** (R9-2's formula), and the flow-integrated check.
2. **The isotropy argument** for (S), (d-i), N_red and W1-weight, and the exact-W1 step: does a q = 0 coupling difference vanish for all exact completions?
3. **Whether (S\*) is a "principle"** in STRUCTURAL-ZERO's sense. Compare (S) (`TESTS:6015`) with R₀ (`C4_V3_referee.md:29`).
4. **The two-loop check** (`run/r1915_d_loops.py`). The basketball normalization −(λ²/48)∫dτΣ_x G⁴, the T₂g convention-independence argument, and the O(λ) cancellation.
5. **Whether the TUNING-ONLY content** (§3.2 + R19-11 + §3.4) suffices for TUNING-ONLY within the registered bridge.

## 7. Files (`S/run/`)

- `r1915_a_hessian.py` → `r1915_a_hessian_N64.out`, `r1915_a_hessian_gw_N256.out`, `r1915_a_hessian_gw_N400.out`. This is Lemma H: the flow-integrated Hessian against the closed form, the seagull/bubble split, and T₂g Liouville. It imports `S/arch14_3/prof.py`, an unmodified copy of R14-3's.
- `r1915_b_cubic.py` → `r1915_b_cubic.out`. The cubic singlet and anisotropy of the archived rows.
- `r1915_d_loops.py` → `r1915_d_loops_N20.out`, `_N28.out`, `_N36.out`. The O(λ) and O(λ²) shear Hessians for the NN scalar.
- `r1915_d_hartree.py` → `r1915_d_hartree.out`. The O(λ) cancellation at fixed physical mass.
