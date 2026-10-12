# Campaign C5, probe O3: vacuum energy and the E_g shear, reverse-engineered (report)

Worker: Claude Opus 5.5 (same family as the supervisor and as P1/I3/V3/RV4). Run 10:58Z to about 11:25Z, 2026-10-12. **Not refereed.** No repository files were edited.
Scratch: `.../scratchpad/C5/O3/`. Every number below is in a `.out` file there:
- `o3_obs_and_necessity.py/.out`: ρ_Λ, F(M) re-check, the tuned non-paired drift;
- `o3_pairing_precision.py/.out`, `o3_inv_omega_check.py/.out`: how exact the pairing must be;
- `o3_qubit_duality_index.py/.out`: Jordan–Wigner (JW) is one spectrum; the CCR trace; Witten indices on 2D and 3D tori;
- `o3_fs_susy.py/.out`, `o3_fs_naive_cusp.py/.out`: the Fendley–Schoutens–de Boer (FS) M1 model on one fermion mode per site, in 1D and 2D;
- `o3_fs_massive_chain*.py/.out`: doublets in a staggered (massive) M1 chain.

## Verdicts against the FIXED readings

**(1) Derivation (DERIVED / SUGGESTED / REFUTED): DERIVED, with amendments.**
- **Free class: DERIVED (Theorem 1, proved).** If the cancellation is to hold without tuning (on an open interval of the mass scale), the signed, mass-rescaled, strained spectral measure of all species must vanish. That means exact pairing, including doublers.
- **Observation then excludes pairing in the observed sector: DERIVED**, given the observational readings.
  - Pairs may be split by at most about 1e-33 eV for Λ, about H₀.
  - They may be split by at most about 4e-23 eV for E_g (P1's number).
  - Observed splittings are at least 100 GeV.
- **What an untuned substrate is left with:**
  - an imposed rule that is vacuum-referenced, not "zero-point energy does not gravitate" (SUGGESTED, from the equivalence principle);
  - or leaving the fixed-grid strain class. Exact continuous translations and a diffeomorphism Ward identity remove E_g but leave Λ.
- **Interactions.** A transported nilpotent supercharge is a proved sufficient structure (Theorem 2). That it is necessary is SUGGESTED only.

**(2) Qubit-pairing test: FAIL (bounded). This needs an explicit outside realization in the headline.**
- **Bound:** a site supplying a bosonic and a fermionic mode, or free (quadratic, CCR + CAR) paired bands. These are the class in which R0–R6 are defined. FAIL is proved there:
  - a 2-dimensional site holds one mode;
  - JW and exact bosonization are one spectrum in two languages;
  - no finite-dimensional site carries a CCR boson.
- **Outside realization.** FS/Nicolai interacting lattice supersymmetry on one fermion mode per site (M₂(C) ≅ Cl₂(C), graded composition) gives exact many-body boson–fermion doublets that survive interactions. With the strain entering through the supercharge, it gives E_vac(ε) ≡ 0 exactly. So μ_E = μ_T2 = 0 and the vacuum energy is 0 to all orders (proved; checked).
- **Expectation refuted in part.** It does refute the expectation's "interactions break pairing" for supercharge-structured rules.
- **Why it is not PASS:**
  - its excitations are Q-doublets of many-body levels, not free bands;
  - it needs a dynamics rule and a coupling rule;
  - unbroken SUSY forces exact degeneracy, which observation excludes.
- **If the referee counts many-body Q-doublets as "paired bands", the reading should be INCONCLUSIVE, not FAIL.** I flag this rather than choose it.

## 1. Observations and what they force

**Numbers (checked):**
- ρ_Λ = 2.52e-47 GeV⁴ = (2.24 meV)⁴;
- ρ_Λ/M_Pl⁴ = 1.13e-123, and ρ_Λ/M̄_Pl⁴ = 7.16e-121;
- the natural size per real bosonic component on Z³ is ½⟨ω⟩ = 1.1938 (M = 0, lattice units). So Λ needs cancellation to about 1e-123 per cell;
- E_g: the refereed bound is μ_E ≤ 5.7e-99 of natural (P0), with free local matter giving natural size (V3).

**Setting (H1–H3).**
- **H1.** The vacuum energy and μ_E are the ε = 0 value and the ε² coefficient of the strained vacuum energy E_vac(ε; t). This is the RN-L1/V3 frame.
- **H2. "No tuning."** The required vanishing holds for the rule's continuous parameters on an open set. In particular it holds on an open interval of the common mass scale t, with m_s = c_s·t. The scale ma ≈ 1e-17 is fixed by no structure. Requiring the cancellation only at the realized t is exactly P1's precision tuning.
- **H3. Free level.** Each species has ω_s² = c_s²t² + Ω_s(k; ε)², with Ω_s bounded on the compact zone (KG, staggered and naive fermions; not Wilson). E_vac = ½ Σ_s σ_s ∫_BZ ω_s, with σ = +1 per real CCR component and −1 per fermionic mode (Dirac sea).

**Theorem 1 (PROVED; necessity of exact pairing).** Under H1–H3, define the signed measure on y ≥ 0:

  μ_ε = Σ_s σ_s c_s (Ω_s(·; ε)/c_s)_* dk.

Then:
- (a) E_vac(ε; t) ≡ 0 on a t-interval implies μ_ε = 0.
- (b) ∂²_ε E_vac(0; t) ≡ 0 on a t-interval implies ∂²_ε μ_ε|₀ = 0.

*Proof.*
- E_vac(ε; t) = ½∫ dμ_ε(y) √(t² + y²) is real-analytic for t > 0, so it vanishes for every t > 0.
- For t > max y, √(t² + y²) = t Σ_j C(½, j)(y²/t²)^j converges. So every even moment ∫y^{2j} dμ_ε vanishes.
- μ_ε has compact support, so its moments determine it (Hausdorff), and μ_ε = 0.
- (b) follows by differentiating under the integral first. ∎

**Comments on Theorem 1.**
- "Pairing" here means exact cancellation of weighted, rescaled spectra. P1's two pairs are instances: a KG component at 2m against 2 staggered fields at m (ω_stag(p; m) = ½ω_KG(2p; 2m)), and a naive boson against a staggered field. So is a negative-energy mirror copy (σ → −σ, same statistics).
- This is the species version of RV4 S1's Theorem B. It sharpens the P1 referee's correction: unique pairing follows once the cancellation is required on a mass interval, not merely at R0–R6.
- **Illustration (checked).** The content KG(0.5t) + KG(1.0208t) against 4 staggered(0.4t) satisfies R0 and is tuned to μ_E = 0 at t = 0.3. It drifts to −2.5e-7 at t = 0.2 and +5.2e-5 at t = 1. The exactly paired content, 2 KG(0.8t) against 4 staggered(0.4t), is 0 at every t.

**How exact must the pairing be (checked).** Take pairs with identical lattice dispersion split by Δ(M²). The leading residual is (dE/dM²)·Δ(M²)·a⁻², with dE/dM²|₀ = ¼⟨1/ω₀⟩ = 0.11384 (⟨1/ω₀⟩ = 0.455344, converged).

| Target | Allowed \|Σ Δm²\| | Allowed splitting | Observed (≥ 100 GeV) |
|---|---|---|---|
| Λ, a⁻¹ = M_Pl | 1.5e-84 GeV² | 1.2e-33 eV (≈ H₀ = 1.4e-33 eV) | 6.7e87 times too large |
| Λ, a⁻¹ = M̄_Pl | 3.7e-83 GeV² | 6.1e-33 eV | 2.7e86 times |
| E_g (P1, R2) | 1.6e-63 GeV² | about 4e-23 eV (≈ the m_g bound) | about 1e68 (P1: 6e68 × P0 for a 1 TeV splitting) |

- Suppose a structural supertrace rule removed the quadratic term. The quartic residual Δ⁴/(64π²) at Δ = 100 GeV is still 6.3e51 ρ_Λ (comparator scaling). Matching needs Δ of order meV.
- **DERIVED (conditional on the observational reading: no degenerate or near-degenerate partners of e, μ, the quarks, W, Z or H at the sub-eV level).** Pairing cannot be the untuned mechanism for the observed sector. A paired hidden sector cancels only its own vacuum energy, because E_vac is additive over decoupled sectors at the free level (proved).

**Interactions.**
- **Theorem 2 (PROVED, finite volume).** Take any nilpotent odd Q(ε) preserving a graded finite-dimensional space V. Set H(ε) = {Q(ε), Q(ε)†}. Then E_0(ε) = 0 for every ε whenever sdim V ≠ 0.
  - Reason: E > 0 eigenspaces have zero superdimension, so W = Tr_V(−1)^F = sdim V, which is independent of Q.
  - So the vacuum energy, μ_E and μ_T2 vanish exactly, at all orders and non-perturbatively, for any local deformation entering through Q.
- **Necessity is SUGGESTED, not proved.** The other ways to make E_vac(ε) constant are:
  - an isospectral (unitary) strain, which is excluded for bulk-local couplings on Z³ (V3; RV4 S1 Theorem A; RFW bounded);
  - the definitional R₀.
- **The equivalence-principle constraint on an imposed rule.** SUGGESTED; comparator Polchinski hep-th/0603249, from memory. Zero-point and vacuum-polarization contributions to nuclear binding energies gravitate normally to the precision of equivalence-principle tests (1e-13 to 1e-15). So a "vacuum does not gravitate" rule must subtract only the state-independent vacuum c-number. That is the vacuum-referenced form P13/R₀, not "zero-point energy does not gravitate". The reading of "a law privileges no states" stays an interpretive tension (RV4 S1 referee), not a contradiction.

### Mechanism list and classification

| # | Mechanism | Λ | μ_E | Untuned? | Survives interactions? | Observation | Class / price |
|---|---|---|---|---|---|---|---|
| 1 | Counterterms (P0 + bare Λ) | 0 | 0 | no: 1e-123 and 5.7e-99 (+ P0's count) | by retuning | consistent | tuning; no axiom |
| 2 | Exact free pairing (Thm 1) | 0 | 0 | yes, if a symmetry locks the masses | no protection | **excluded** (table above) | mechanism; needs CCR bosons (Prop. 3: not on finite sites) |
| 3 | Unbroken nilpotent SUSY, strain via Q (Thm 2) | 0 exactly | 0 exactly | yes | **yes, exactly** | **excluded**: exact Q-doublets (Prop. 5) | structural rule: H = {Q,Q†}; gravity couples through Q; graded sites for d ≥ 2 |
| 4 | Broken SUSY | ≥ Δ⁴ (and Δ²M_Pl² unless a supertrace rule holds) | about 1e68 × P0 at 1 TeV (P1) | no | — | excluded as untuned | — |
| 5 | Vacuum-referenced subtraction R₀ / S2's DOS-preserving seagull | 0 | 0 | by definition | R₀: by definition | consistent if vacuum-only | definition; P13 |
| 6 | Unimodular Λ (integration constant) | radiatively stable, value free | **no** (√g Λ does not touch E_g; V3) | Λ only | yes | consistent | imposed rule (fixed volume form) |
| 7 | Count-fluctuation Λ (Sorkin, "everpresent Λ") | ~ H₀²M̄² = 0.49 ρ_Λ (arithmetic checked) | no | Λ magnitude without tuning, needs #6 | — | data tension in published fits (comparator, from memory) | SUGGESTED; Lattice → countable random events (RL lanes) |
| 8 | Exact continuous translations + diffeomorphism Ward identity | no | forbidden (μ_E = μ_T2 = tadpole value) | E_g yes | yes | consistent | **excluded on fixed Z³** (RV4 S1, V3, RFW bounded); the O1/O2 direction |
| 9 | Frustration-free, number-conserving empty vacuum | 0 | 0 | yes | yes | **excluded**: gapless frustration-free systems have z ≥ 2 (comparator: Gosset–Mozgunov 2016; ROUTES F3 reading), against matter Lorentz invariance (O1) | — |
| 10 | Negative-energy mirror copy ('t Hooft–Nobbenhuis, Kaplan–Sundrum, Linde) | 0 | 0 | if the Z₂ is exact | instability (ghost-like decay) | not directly excluded | is Thm 1 pairing with σ → −σ; doubles the site; comparator |
| 11 | Self-tuning scalar | — | — | — | — | Weinberg no-go (comparator); F3: "leaves (k_F a)²" | dead |
| 12 | Records-only sourcing ("the vacuum is not a record") | 0 | 0 | by rule | — | must be vacuum-only (EP) | the substrate form of #5; a source/action bridge (axiom open gate); reading |

## 2. The qubit-pairing test

**Proposition 3 (PROVED): no free bosonic band on a finite site.**
- Exact CCR [b, b†] = 1 has no finite-dimensional representation: Tr[b, b†] = 0 ≠ d. Checked for d = 2, 4, 16.
- So the +½ω zero point that cancels the fermion sea needs an infinite-dimensional site (compare P10).
- On qubits a "boson" is hard-core. Its free-level zero point is 0 (ω σ⁺σ⁻), not ½ω.
- Bosons that emerge in a large-N limit (quantum central limit, spin waves) are only asymptotic. R0 and R2 are zone-wide, lattice-scale integrals (P1), so IR-emergent CCR or IR-emergent SUSY (tricritical Ising) cannot meet them (SUGGESTED).

**Proposition 4 (PROVED; checked): duality is one spectrum, not a pair.**
- JW, Bravyi–Kitaev and the Chen–Kapustin–Radičević exact bosonizations are algebra isomorphisms, unitary on the constrained space. They map H to H′ with the same spectrum, so E_vac and every strain derivative are identical in both languages.
- Checked on the XX ring, L = 10: qubit ED equals the JW free-fermion spectrum (with the parity-dependent twist) to 2.9e-14, with E_0 = −6.472 in both.
- Two copies ("boson chain" plus "fermion chain") give 2E_0, so they do not cancel. A CCR boson with ω = |ε_k| would cancel exactly (+6.155 − 6.155), but Proposition 3 forbids it.
- **Site count.** One M₂(C) site is 2-dimensional. A bosonic mode plus a fermionic mode, even hard-core, needs ≥ 4 states.
- **Locality cost** (comparator, from memory). In d ≥ 2, local qubit encodings of fermion hopping use extra edge or face qubits: Bravyi–Kitaev d/2 per site (3 on Z³); Chen–Kapustin 3 per site in 3D. Alternatively, the sites must be composed as graded (fermionic) tensor factors.
- **Majoranas.** A qubit is 2 Majoranas.
  - Kitaev chains are all-fermion.
  - The Kitaev honeycomb gives a Majorana Dirac band plus a static flux sector (Carroll-flat, as in I3), with no matched boson band.
  - N = 1 Majorana-chain SUSY (H = Q²) exists in 1D, but is generically spontaneously broken (Sannomiya–Katsura–Nakayama 2016; comparator, from memory).

**Outside the bound: FS M1 lattice SUSY on one fermion mode per site (PROVED via Thm 2; CHECKED).**
- **Construction.** Q(ε) = Σ_i c_i† B_i, with:
  - B_i = Π_{j∈N₁(i)}(1 − n_j)·exp[ε(Σ_{j∈N₂ˣ(i)} n_j − Σ_{j∈N₂ʸ(i)} n_j)];
  - nilpotency holds for any symmetric dressing (proved: the i ≠ j cross terms cancel iff the dressing is symmetric);
  - ε is an E_g-odd (x↔y antisymmetric) local deformation standing in for any strain entering through Q.
- **The site.** M₂(C) ≅ Cl₂(C) is exactly one complex fermion mode, the site content of one staggered field. Its free version has μ_E = −½F(2m) ≠ 0 (P1). The FS rule replaces it by an interacting hard-core fermion whose H is a supercharge square.

**1D ring, checked:**

| L | W | gap·L |
|---|---|---|
| 9 | −2 | 13.33 |
| 12 | 2 | 14.06 |
| 15 | −2 | 14.51 |
| 18 | 2 | 14.82 |
| 21 | −2 | 15.04 |
| 24 | 2 | 15.20 |

- E_0 = 0 at every L.
- The gap falls as 1/L, so z = 1. Lattice SUSY therefore evades the frustration-free z ≥ 2 bound (#9), because H = {Q, Q†} is not locally frustration-free.

**2D tori, checked:**

| Torus | Hard-core states | W | Zero modes |
|---|---|---|---|
| 4×4 | 743 | 7 | 7 at every ε |
| 4×5 | 3561 | 1 | 3 |
| 5×5 | 25531 | −9 | — |
| 4×6 | 18995 | 3 | — |

- ‖Q²‖ ≤ 2e-16.
- |E_0(ε)| ≤ 3e-14 for ε = 0 to 0.4.
- Every E > 0 level is reproduced by the squared singular values of Q between the F and F + 1 sectors, to ≤ 2e-13. So the **E_g responses of excited levels are paired level by level**.

**Strain applied to H instead of Q, checked.** Scale x-hops by e^ε and y-hops by e^{−ε}; the result is not of {Q, Q†} form.
- The degenerate E = 0 manifold splits at **first order**: E_0/(N|ε|) = −0.265 (4×4), −0.231/−0.028 (4×6, ±ε), −0.026 (5×5) at ε = 1e-3.
- So μ_E is not merely nonzero: the response is a cusp. The protection is all-or-nothing and sits entirely in the coupling rule.
- Whether the V3/RN-L1 bulk-local transport of H coincides with {Q(ε), Q(ε)†} for Q transported the same way is **not computed**.

**Witten index of the hard-core space, checked by transfer matrix.**
- 2D, n × L_z, n = 3–8, L_z = 3–12: never 0. It is periodic for n = 3, 4 and 7 (e.g. 1, 7, 1, 3 for n = 4); the values reach 43.
- 3D, 3×3×L_z, L_z = 2–10: 1, −38, 37, 1, 214, −251, −251, −1118, 2341. It grows like 2.03^{L_z} (the leading |λ| of the signed transfer matrix), so there are extensively many E = 0 vacua along z.
- 3D, 4×4×L_z: 11, 121, 143, 1, 275, 1, 399, 121, 91.
- So E_vac(ε) ≡ 0 holds on every 2D and 3D torus computed.
- The 3D low-energy theory, and whether it is relativistic, is unknown and not computed.
- **Reading, SUGGESTED.** The hard-core rule ("an occupied site forces its neighbours empty") is a nearest-neighbour support constraint, the kind Admissibility names. The index that protects E_vac is a property of the admissible configuration space alone (the independence polynomial at −1). The axioms still do not supply Q, the grading or the coupling.

**Proposition 5 (PROVED, structural): unbroken SUSY forces doublets; observational exclusion is reading and comparator.**
- If E_0 = 0 with H = {Q, Q†} and Q translation-invariant, every E > 0 level is a doublet between F and F ± 1 at the same lattice momentum.
- **Checked in the massive period-3 staggered chain** (λ = 0.4 on i ≡ 0 mod 3):
  - the lowest F₀ − 1 level, 1.2898 → 1.1499 → 1.0832 at L = 12/18/24, is exactly degenerate with an F₀-sector level;
  - the lowest F₀ + 1 level (1.1112 at L = 24) likewise;
  - the gap tends to a constant;
  - λ = 2.0 gives the same structure.
- **SUGGESTED (finite-volume tracking).** The partner of an isolated one-particle level, whose energy is L-independent up to exponentially small corrections, must be an isolated degenerate level. The alternatives are a threshold state with exact mass relations Σm_i = m, or an exact zero mode. All three are observable degeneracies.
- Observation (comparator, from memory): no degenerate partners of e, μ or the quarks; LEP slepton bounds are about 100 GeV and LHC bounds are at the TeV scale. That excludes unbroken SUSY in the observed sector. Breaking it returns to #4.

## 3. Mapping to the fixed readings

- **O3 derivation: DERIVED.** This holds for the free class (Theorem 1) plus the observational exclusion of pairing.
  - The registered "pairing or an imposed spectral-invariance rule" is correct as far as it goes, but incomplete. Tuning stays available. So does leaving the fixed-grid strain class, which leaves Λ alone (#8).
  - The imposed rule must be vacuum-referenced (#5/#12). Unimodular Λ (#6) and count fluctuation (#7) address Λ only.
  - For interactions, sufficiency is proved (Theorem 2) and necessity is SUGGESTED.
- **Qubit pairing: FAIL (bounded).** It is bounded to free or site-level boson-plus-fermion pairing, the R0–R6 class (Propositions 3 and 4).
  - Outside realization: FS/Nicolai lattice SUSY on graded M₂(C) sites gives exact, interaction-proof pairing and E_vac(ε) ≡ 0 when the strain enters through Q.
  - Its costs:
    - (i) a dynamics rule, H = {Q, Q†} (the axioms supply no H);
    - (ii) a coupling rule: gravity couples through Q;
    - (iii) graded composition of sites in d ≥ 2, or extra edge/face qubits;
    - (iv) unbroken SUSY, which forces observed-excluded degeneracy.
- **Against the expectation.** "Duality is one excitation viewed two ways": **confirmed** (proved). "Interactions break pairing": **refuted** for supercharge-structured rules (Theorem 2, checked). It is **confirmed** for couplings not of the {Q, Q†} form, where the failure is first order (the cusp). The expected FAIL holds only as bounded.

## Labels

- **PROVED** (same family, unrefereed):
  - Theorem 1;
  - Theorem 2 (W = sdim V is independent of Q);
  - nilpotency of the symmetric-dressed Q;
  - Propositions 3 and 4;
  - Proposition 5's doublet structure;
  - additivity over decoupled sectors.
- **CHECKED:** every number in §§1–2, including the FS spectra, the doublets, the cusp, the Witten indices, F(1) = 1.970388641879e-3 (matching V3's referee), ⟨1/ω₀⟩ and ρ_Λ.
- **SUGGESTED:**
  - that a protecting structure is necessary;
  - the equivalence-principle restriction to vacuum-referenced rules;
  - finite-volume tracking implying degenerate partners;
  - that IR-emergent SUSY cannot meet R0 and R2;
  - the Admissibility reading of the index.
- **COMPARATOR (from memory):** Kato–Sakamoto–So; FS–de Boer (2003); Nicolai (1977); Bravyi–Kitaev; Chen–Kapustin–Radičević; Gosset–Mozgunov; Sorkin (everpresent Λ); Weinberg; Polchinski; Kaplan–Sundrum; Sannomiya–Katsura–Nakayama; LEP/LHC bounds.
- **READING:**
  - that observation excludes degenerate partners;
  - "graded composition" as a choice the axioms leave open (the Qubit axiom fixes only the one-site algebra);
  - the tension with "privileges no states".

**Not done:**
- V3's bulk transport applied to Q versus H for FS;
- FS exact diagonalization in 3D, and its low-energy content and Lorentz behaviour;
- momentum-resolved doublets;
- turning finite-volume tracking into a theorem;
- the m⁶ ln m term under structural supertrace rules.
