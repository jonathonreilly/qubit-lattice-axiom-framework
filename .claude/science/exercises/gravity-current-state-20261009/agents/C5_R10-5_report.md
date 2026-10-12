# C5 R10-5 report: an edge supertrace — can boson–fermion pairing on the box edge cancel every one-loop Lorentz-violating coefficient (photon, electron, graviton), and what does it do to the vacuum energy?

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 18:13Z to 18:45Z. No repository file edited.

**Scratch.** `S/` = `.../scratchpad/C5/R10-5/`. Scripts and outputs are in `S/scripts/`. Each runs in under 15 s with `OMP_NUM_THREADS=2`.
- `r105_free_susy.{py,out}`: the free supercharge (Theorem Q), the vacuum energy, the static TT cancellation, and β for the through-Q coupling.
- `r105_tt_paired.{py,out}`: the graviton TT speed coefficient Ξ for the paired multiplet, under two couplings (Theorem PT).
- `r105_photino_chern.{py,out}`: a numerical illustration of Lemma PD (Chern numbers).
- `r105_partner_loop.{py,out}`, `r105_partner_conv.{py,out}`: the electron's speed shift from the selectron–photino loop.
- `r105_aloop.{py,out}`: the N = 2 neutral-scalar (a) loop.
- `*_nobeta.out`: the first, wrong-vertex run (§3.6). It is kept as a control.
- `r101_pairing.py`, `r85_box_qed_copy.py`: unmodified copies of the R10-1 helpers.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`:
  - the C5 method (`:2302-2320`);
  - rounds 7–10 with every referee entry (`:3240-4076`);
  - R10-5 (`:4062-4076`).
- R10-1: the worker report, the scripts, and `ref_R10-1/REFEREE_VERDICT.md` (CONFIRMED WITH CORRECTIONS).
- R8-5: the report, the verdict and `scripts/C5/R8-5`.
- R9-9: the report, Theorem T, and `scripts/C5/R9-9`.
- O3: the report, `C5_O3_referee.md` and `C5_O3_referee_full.md`.
- Prior-art hits:
  - `C4_F2_report.md:93` and `C4_F2_referee.md:46`;
  - `C4_P1_report.md:181` and `C4_P1_referee.md:11`;
  - `C5_R2-1_report.md:76-78`;
  - `SUMMARY.md:540`;
  - `docs/YT_CLASS_3_SUSY_2HDM_ANALYSIS_NOTE_2026-04-18.md:470-535`, which says no SUSY is retained and that Cl(3)'s Z₂ is parity, not SUSY.

**Labels.**
- **proved**: complete under the stated hypotheses.
- **checked**: numerics here.
- **suggested**: argued, not proved.
- **reading**: an interpretation.
- **comparator**: literature. V = verified this session (abstract level); R = recalled, not verified.

---

## 0. In plain words

1. **A lattice supercharge exists for the free paired matter, and it is exactly R10-1's content.** Take R10-1's paired unit: an 8-component Clifford-flat fermion plus 4 complex scalars on the same edge curve.
   - It is the free multiplet of an exact lattice supercharge Q = Σψ†(p − iMφ), with Q² = 0 and {Q, Q†} = 2H.
   - M is a real symmetric, quasi-local 8×8 Clifford operator.
   - Its vacuum energy is exactly 0 for every edge shape and every deformation that enters through Q. With split masses the residual is 2⟨1/E⟩Δm² per site.
   - Proved; checked to 1e-15.
2. **The gauge field cannot join this supersymmetry with a box photon.** In this class the photon's energy must be the squared gradient of a gauge-invariant "superpotential", and the photino's Hamiltonian is its curl.
   - A topological (Chern-number) argument shows that such a lattice curl must have extra zero modes: photon and photino doublers.
   - This is the Hamiltonian form of the known lattice Chern–Simons doubling problem.
   - So no supercharge of this class is compatible with R8-5's box photon (Lemma PD).
   - Charged matter also needs twice R10-1's content (Lemma J).
   - Proved.
3. **Gravity: the pairing works, but only with "minimal" coupling, not with coupling through Q.**
   - **Minimal coupling.** The graviton couples minimally to the fermion, and the scalars get the pairing-fixed partner vertex. Then the paired multiplet's one-loop TT speed shift is exactly the zone average of g·(|c′|² − 1)/E³. That is the velocity-norm anomaly, which is zero for Clifford-flat curves. So the TT speed shift and the TT mass both vanish for every edge shape. Proved; checked to 1e-8; a non-unit-speed control gives −1.93e-2, exactly as predicted. This is a new positive result.
   - **Coupling through Q (O3's rule).** Here the static response is protected exactly, but the speed is not: Ξ = −⟨g/E³⟩ ≠ 0. This is a whole-zone, sign-definite Lorentz violation, not an edge effect. Proved; checked.
4. **The electron is not rescued.**
   - With the photon paired (R10-1), the electron's photon loop leaves −17.96 (Wilson curve) or −10.66 (box curve), in units of e²/16π² (R10-1 referee).
   - The partner loops built here have the same sign:
     - selectron plus photino, with a chiral Lorentz-scalar Yukawa: −1.49 and −2.85 per y²/16π²;
     - N = 2's neutral scalar (pseudoscalar coupling): −2.66 and −2.52.
   - So they enlarge the split. With y² = 2e² (the SUSY value): Δ ≈ −21 (Wilson) and about −15 to −16 (box). That is c_e − c_γ ≈ −9e-3 to −1.2e-2.
   - Checked for the cheapest constructions. This is not a class-wide proof.
5. **Against the FIXED readings: FAIL (bounded), clause 1, in class 𝒮** (worker reading; referee required).
   - Lemma PD with Lemma J: no supercharge of SUSY-QM form is compatible with a box photon.
   - PASS is not met.
   - Clause 2 ("the pairing provably cannot cancel the electron self-energy") is **not** proved. It is only computed, for the constructions here.

---

## 1. Hypotheses and classes (stated before any title)

- **H-lat.** Z³ × ℝ, continuous time. Free or one-loop. q is along a cubic axis. The curves c(k) = (S(k), W(k)) are smooth and periodic:
  - S odd, W even;
  - R10-1's Wilson circle (sin k, 1 − cos k);
  - the box curves b₁ = 0.5 and 0.8 (exactly (k, 0) on |k| ≤ b₁, unit speed);
  - a non-unit-speed control (sin k, ½(1 − cos k)).
- **Class 𝒮 (lattice SUSY of SUSY-QM / Nicolai form).**
  - Real bosonic coordinates x_a (link fields A_ℓ, site fields φ_a), with one canonical complex fermion ψ_a per real coordinate.
  - Q = Σ_a ψ_a†(p_a − i∂_aW), with W real and gauge invariant.
  - Then Q² = 0 and H = ½{Q, Q†} = ½[p² + |∂W|²] + ψ†(Hess W)ψ − ½ tr Hess W (standard; `r105_free_susy.py` docstring).
  - The quadratic A-part of W has a translation-invariant Hermitian symbol C(q), C¹ on T³, with no A–scalar mixing at quadratic order.
  - The gauge-shift symbol D̂(q) vanishes only at q = 0, as in R8-5 and R9-9: D̂ = d e^{iq/2}.
- **Box photon.** Near q = 0 the transverse photon is the continuum one (C² = q²P_T + o(q²)), with no extra zero modes. This is R8-5's photon (`C5_R8-5_report.md:126-131`).
- **Minimal-pairing laws (not exact SUSY).** The fermion vertex is given; the paired scalars get the q-independent part of the vertex the supercharge would induce. Used in §3.5 and §3.6.
- **Excluded, not addressed:**
  - supercharges outside 𝒮:
    - light-cone supercharges with {Q, Q†} = 2(H + P̃);
    - Q not involving all momenta;
    - nonzero central charges;
    - equivariant structures with Q² = H + gauge transformation;
    - A–scalar mixing in W (as in extended-SUSY orbifold lattices);
  - Euclidean Q-exact lattices (Kaplan–Ünsal, Catterall);
  - compact or finite link variables;
  - non-axis q;
  - two loops;
  - the matter-side shift from graviton loops;
  - Ward completion of the pair-creating stress (R9-9's open item);
  - interacting vacuum energy beyond O3 Theorem 2.

## 2. Prior art (each counted once)

- **R10-1** (CWC, SUGGESTED; `ref_R10-1/REFEREE_VERDICT.md` items 2, 3, 5):
  - Theorem P: the Clifford-flat fermion plus matched scalars cancel the photon coefficient pointwise. The 8-component realization needs 4 complex scalars, and masses must be matched.
  - The electron residual is δc_e·16π² = −17.96 (Wilson) and −10.66 (box) at N = 224.
  - The pairing is "untuned narrowly but not symmetry-protected". §3.1 below supplies the protecting supercharge for the free part.
- **R8-5** (CWC FAIL, bounded): Lemma C and Theorem B, the soft photon couples to every charged mode; BQ split −11 to −71 (`TESTS.md:3807-3813`).
- **R9-9** (CWC INCONCLUSIVE): Theorem T, Ξ = (1/32)⟨|V|²A_zz/ε⁵⟩ per real scalar; the narrow mass FAIL (`TESTS.md:3939-3951`).
- **O3** (CWC with corrections, `C5_O3_referee.md`):
  - Theorem 1(a): untuned vacuum cancellation needs equal aggregate spectral measures.
  - Theorem 2: a nilpotent Q gives E₀ = 0 under every Q-preserving deformation.
  - No exact on-site CCR on a finite site.
  - FS M1 is an interacting escape, but it does not establish the gravitational E_g bridge.
  - The precision table: Λ needs |ΣΔm²| ≲ 1.5e-84 GeV².
- **F2 / F2 referee** (`C4_F2_report.md:93`; `C4_F2_referee.md:46`). The worker said a lattice H = {Q, Q†} has no P, so it cannot relate speeds. The referee corrected this to "standard super-Poincaré protection not established", and found no proof that every lattice supercharge fails. §3.7 sharpens what Q² = H can and cannot do.
- **P1 referee** (`C4_P1_referee.md:11`): explicit nilpotent lattice models exist (FSdB); Kato–Sakamoto–So does not exclude all lattice SUSY.
- **R2-1** (`C5_R2-1_report.md:76-78`): the Kato–Sakamoto–So Leibniz no-go (infinite-flavour escape) and the cyclic Leibniz rule keeping one nilpotent Q.
- **Repo docs:** `YT_CLASS_3_SUSY_2HDM_ANALYSIS_NOTE_2026-04-18.md:470-535`. No retained SUSY. Cl(3)'s Z₂ is parity.
- **Comparators:**
  - **Groot Nibbelink–Pospelov, hep-ph/0404271 (V, abstract).** In the supersymmetric SM, LV operators have dimension ≥ 5. The soft-breaking suppression is R.
  - **Berruto–Diamantini–Sodano, hep-th/0004203 (V, abstract via search).** Any local, gauge-invariant, parity-odd Abelian lattice quadratic form has extra zero modes in the zone (Nielsen–Ninomiya-like). A Maxwell term lifts them (hep-lat/0011052, V).
  - **Kaplan–Katz–Ünsal, hep-lat/0206019 (V, abstract).** Spatial lattices keeping some SUSY exact, for example N = 4 SYM in 3+1. That 4D N = 1 or 2 theories with charged matter have no exact-Q lattice is R.
  - **Witten (1994) and Kronheimer–Mrowka** (R): the twisted N = 2 SQED on ℝ × Y is SUSY-QM with the Chern–Simons–Dirac functional.
  - Elitzur–Rabinovici–Schwimmer 1982 (R).
  - LEP and LHC slepton bounds (R).

## 3. Results

### 3.1 Theorem Q: the free edge-SUSY multiplet is an exact lattice supercharge. Proved; checked

- **The operator.** M(k) = Σ_j[S(k_j)A_j + W(k_j)B_j] + mB₀, where:
  - A_j is imaginary antisymmetric and B_j, B₀ are real symmetric;
  - all 7 mutually anticommute and square to 1, i.e. a real 8-dimensional module of Cl(4,3) ≅ M₈(ℝ) ⊕ M₈(ℝ).
- **Why M is real and symmetric.** S odd makes S(−i∇) i×(real antisymmetric) in real space. So M is a **real symmetric, quasi-local** operator on 8 real components per site, and W = −½⟨φ, Mφ⟩ is a valid real superpotential.
- **The Hamiltonian.** Q = Σψ†(p − iMφ) gives Q² = 0 and

  H = ½p² + ½φM²φ + ψ†Mψ − ½tr M.
- **Content.** Bosons: 8 real fields with ω = E, because M² = E² for Clifford-flat curves. Fermions: one-particle operator M, with eigenvalues ±E, four times each.
- **This is R10-1's Theorem-P content.** The R10-1 referee's corrected count is 8 complex fermion modes plus 4 complex scalars, matching the bosons here. So **R10-1's "edge supertrace" is the free part of an exact lattice supersymmetry.**
- **Checked** (`r105_free_susy.out:1-5`):
  - explicit generators (Pauli strings IIY, IYX, XYZ | YYZ, ZIZ, ZXX | ZZX), with anticommutator error 0;
  - |M² − E²| ≤ 3.6e-15 and M(−k) = M(k)* to 2e-15, on all three curves.
- **Prices.**
  - 8 CAR modes plus 8 real CCR modes per site, against the Qubit fibre M₂(ℂ) (`AX:47`). Graded composition and infinite-dimensional bosons (O3 Prop. 3).
  - The dynamics rule H = {Q, Q†}, which is not supplied (`AX:116-130`).
  - Clifford-flat curves (taste doubling).

### 3.2 Vacuum energy. Proved; checked

- **Exact zero.** E_vac = ½Σ|λ(M)| (bosons) − ½Σ|λ(M)| (Dirac sea) = 0 exactly, for every edge shape, every k, and every deformation M → M(ε) entering through Q.
  - Checked: 0.0 on N³ grids; 5e-15 per k by direct eigenvalues (`r105_free_susy.out:6-14`).
- **Mass split.** E_vac = 2⟨1/E⟩Δm² per site. Checked: e.g. 6.655e-4 against a predicted 6.656e-4 (box b₁ = 0.8, m = 0.3, Δm = 1e-3).
  - So O3's precision table applies unchanged: Λ needs |ΣΔm²| ≲ 1.5e-84 GeV² (comparator: O3, refereed).
  - Reading: unbroken pairing means a charged scalar degenerate with the electron (R comparator: excluded). Breaking it reinstates the tuning.
- **Interactions.** Within 𝒮, O3 Theorem 2 gives E₀ = 0 (finite volume, index ≠ 0). But see §3.3: 𝒮 forces photon doublers.

### 3.3 Lemma J (charge) and Lemma PD (photon/photino doubling). Proved

- **Lemma J.**
  - **Claim.** A global U(1) commuting with Q must act on φ by a complex structure J with [J, M] = 0. The fermions are tangent vectors, so they rotate the same way.
  - **Proof.** All 7 generators appear in M with independent coefficient functions, so J lies in the commutant of the real irreducible M₈(ℝ)-module, which is ℝ (Schur). No J with J² = −1 exists. ∎
  - **Consequence.** Charged matter in 𝒮 needs the complexification: 16 complex fermion modes plus 8 complex scalars per site, i.e. 2× R10-1's unit (4 Dirac tastes).
- **Lemma PD (photon/photino doubling in 𝒮).**
  - **Claim.** Under the 𝒮 and box-photon hypotheses of §1, the transverse part of C(q) has a zero eigenvalue at some q ≠ 0. There the photon has ω = 0 and the photino has a zero mode.
  - **Proof.**
    1. **Why C sets the spectrum.** The photon energy is ½(Π² + |∂_AW|²), so ω² = eig C². The photino's one-particle operator is C.
    2. **Gauge invariance.** It gives C(q)D̂(q) = 0. Since D̂ = q + O(q²), the linear part obeys C₁(q)q ≡ 0.
    3. **The linear part is the curl.** Write C₁(q) = Σ_j q_jΓ_j, with T_ijk := (Γ_j)_ik. Then C₁(q)q ≡ 0 forces T to be antisymmetric in (j, k): T_ijk = ε_jkl U_il. Hermiticity then forces U = iaδ with a real. So C₁ = ia ε·q, with a ≠ 0 by the box photon.
    4. **A positive band would be well defined.** Suppose the transverse eigenvalues never vanish on T³∖{0}. Their product is continuous, nonzero, and negative near 0 (±|a||q|). So there is a simple band λ₊ > 0 > λ₋ on all of T³∖{0}, and its eigenline L₊ is a line bundle there.
    5. **Its Chern number near 0 is ±2.** On a small sphere around 0, c₁(L₊) equals that of ia ε·q's upper band, which is ±2: the photon-helicity monopole.
    6. **Contradiction.** That sphere bounds T³ minus a ball, so ⟨c₁, [S]⟩ = 0. ∎
- **Checked** (`r105_photino_chern.out`):
  - the upper band of iε·q has Chern number +2.0000;
  - for the lattice curl iε·sin q, the charges at the 8 zeros are ±2 and sum to 0;
  - generic smooth Hermitian deformations keeping the kernel still have transverse zeros (min |λ| ≈ 1.5e-5 to 2.9e-5 on a 40³ grid, now off the π points), and the Chern number at 0 stays +2.
- **Meaning.**
  - This is the Hamiltonian version of Berruto–Diamantini–Sodano (V).
  - Their cure, a Maxwell term, is not available in 𝒮: the bosonic potential must be exactly ½|∂W|². An added B² term breaks Q, because it is not of gradient form.
  - So **in 𝒮 no supercharge is compatible with the box photon**, whatever the matter content and its Ward-forced Peierls coupling (the matter Hessian M_A is Peierls-dressed, so its coupling is exactly R8-5's class).
- **Scope.** Lemma PD concerns the pure gauge sector. It is evaded only by leaving 𝒮: A–scalar mixing in W, an equivariant Q² = H + gauge-transformation structure (twisted N = 2 with its scalar a), or non-C¹ (power-law) symbols. All are open.

### 3.4 What Q² = H can and cannot protect (proved where stated)

- **No N = 1 supercharge squares to H alone.** In 4D N = 1, every nilpotent complex supercharge is Q = u^αQ_α (nilpotency kills the mixed u σ^μ v̄ terms). Then {Q, Q†} = 2|u|²(H + n̂·P) with |n̂| = 1. Proved, elementary.
- **"Q² = H" needs N = 2.** The twisted Q with central charge Z = 0 does it (comparator R). The hypermultiplet (1 Dirac + 2 complex scalars) matches R10-1's count. Its flat-space SUSY-QM form uses W = Chern–Simons–Dirac (R), which is where Lemma PD bites.
- **What Q does relate.** A translation-, rotation- and charge-commuting Q relates partners only:
  - E_e(k) = E_ẽ(k) and E_γ(k) = E_γ̃(k), to all orders;
  - but not c_e and c_γ, which sit in different charge sectors.
- **A family proving it.** In 𝒮 the gauge superpotential can be rescaled (C → λC) with Q staying exact for every λ, so the tree-level c_γ/c_e is a free parameter of supersymmetric laws. That proves Q² = H imposes no relation between them. Whether a one-loop non-renormalization exists: none is known; suggested no.
- **The super-Poincaré route.** Groot Nibbelink–Pospelov needs P (or a deformed P̃) in {Q, Q†}, exactly conserved and additive. On the lattice the gauge vertex reaches the whole zone (R8-5 Lemma C). By RC C1 Lemma R (`TESTS.md:1172-1177`), the C¹ invariants of normal collisions are λE + b·k + c, so no momentum-like P̃ = k on the box survives edge scattering. Suggested; not a theorem here.

### 3.5 Theorem PT (graviton TT with superpartners). Proved; checked

- **Setting.**
  - The paired multiplet (Theorem Q content), T_2g = h_xy, q along z.
  - Fermion vertex: the Clifford-index vielbein Γ = ½(S_xA_y + S_yA_x). Γ² = g·1 with g = (s_x + s_y)/4, s = S²; {M_⊥, Γ} = f·1 with f = 2S_xS_y; {M_z, Γ} = 0.
  - Two boson couplings:
    - **(M), minimal pairing:** V = f·1. This is R9-9's class 𝒱 (k_z- and q-independent), with |V|² = 4s_xs_y.
    - **(Q), through Q:** V = {M(k+q), Γ} = f + [M_z(k_z+q) − M_z(k_z)]Γ, i.e. an extra O(q) spin term.
- **Claim.** With ⟨·⟩ the zone mean and Ξ = (∂_{q²} + ∂_{ω²})Π:
  - **(M):** Ξ_B + Ξ_F = ⟨g·(|c′(k_z)|² − 1)/E³⟩. This is a moment of the velocity-norm anomaly a = |c′|² − 1 (R10-1 Theorem D's a-term). **For Clifford-flat (unit-speed) curves it is identically 0, for every edge shape and any common mass.**
  - **(Q):** Π(0, q) ≡ const (an exact SUSY static zero), so α = 0 and Ξ_Q = β = −⟨g/E³⟩ < 0.
  - **Both:** the TT mass Π(0, 0) = 0 pointwise in k, with the seagull included.
- **Proof.**
  1. **The fermion pair weight.** t(k, k′) = tr[P₊(k′)ΓP₋(k)Γ] = 2g − f²/(EE′) + 2g(E_⊥² + c_z·c_z′)/(EE′). Equivalently 2g(E + E′)²/(2EE′) − g|Δc_z|²/(EE′) − f²/(EE′).
  2. **The static susceptibilities.** χ_F(0, q) = ⟨2t/(E + E′)⟩. The (E + E′)/(EE′) piece is q-independent after the shift k_z → k_z + q. So χ_F + χ_B^(M) = const − 2⟨g|Δc_z|²/(EE′(E + E′))⟩, while χ_B^(Q) adds exactly +2⟨g|Δc_z|²/…⟩, which proves (Q)'s static zero.
  3. **α for (M).** |Δc_z|² = q²|c′|² + O(q⁴) gives α_M = ⟨g|c′|²/E³⟩.
  4. **β, the same for both.** All pair energies at q = 0 are 2E, and ∂_{ω²}χ sums to ⟨f²/(4E⁵)⟩ + ⟨g/E³ − f²/(4E⁵)⟩ = ⟨g/E³⟩. So β = −⟨g/E³⟩.
  5. **Sum.** Ξ_M = ⟨g(|c′|² − 1)/E³⟩. ∎

  The same algebra applies to E_g with Γ = ½(S_xA_x − S_yA_y) (same g). Proved, not run.
- **Checked** (`r105_tt_paired.out:3-14`; α by exact grid shifts and Richardson; N = 96 and 160; m = 0.3 and 0.1):

| curve | Ξ_B (direct = Theorem T) | Ξ_F | Ξ_B + Ξ_F (M) | prediction | Ξ_Q (through Q) |
|---|---|---|---|---|---|
| Wilson circle, m = 0.3 | −0.002843 | +0.002843 | −2e-10 | 0 | −0.02645 |
| box b₁ = 0.5, m = 0.3 | −0.007316 | +0.007316 | −3e-9 | 0 | −0.03965 |
| box b₁ = 0.8, m = 0.1 | −0.012345 | +0.012345 | −2e-8 | 0 | −0.05740 |
| control (sin k, ½(1 − cos k)), m = 0.3 | −0.015061 | −0.004195 | −1.93e-2 | −1.93e-2 | −0.06029 |

- **Further checks.**
  - R9-9's Theorem T reproduces Ξ_B directly to 1e-6.
  - α_Q = 1e-14: the static zero.
  - The static T_2g second-order energy cancels pointwise to 7e-16 (`r105_free_susy.out:15-16`).
- **Physical size.** Take R9-9's normalization, c_T² − 1 = 2κ_lat Ξ with κ_lat = 8π(ℓ_P/a)², which uses the same |V|² = 4u_xu_y.
  - (M) gives 0 at one loop, untuned, with matched masses.
  - (Q) gives c_T² − 1 ≈ −1.3 to −2.9 per multiplet at a = ℓ_P. GW170817 then needs a ≳ 4e7 ℓ_P (reading).
- **Reading.**
  - Coupling gravity through Q (O3's rule, which protects μ_E) is itself Lorentz-violating: a twisted coupling, with the Källén–Lehmann-positive β left unbalanced.
  - The minimal pairing rule removes the one-loop graviton-sector LV that R9-9 found for scalars.
- **Scope:**
  - one loop, free paired matter;
  - matched masses (the mass-split residual is not computed; O(Δm²) is suggested);
  - q along an axis;
  - the pair-creating stress is not Ward-completed (R9-9's open item);
  - the matter speed from graviton loops is not computed.

### 3.6 The electron: what the partners do. Checked for the stated constructions

- **Method.** Rayleigh–Schrödinger second order on the one-electron state, with Dirac seas filled. It has a normal term plus the Pauli-blocked vacuum (Z) term, averaged over the 4 positive-energy states. Then δc = ½∂_{p²}(2E_pδE), with Richardson in p.
- **The vertex had to be fixed first.** A Lorentz-scalar Yukawa needs λ̄ = λ†B₀:
  - With λ†Pψ (the first run, `*_nobeta.out`), the speed grows like ln(1/m): −7.6, −9.0, −10.2 at m = 0.1, 0.05, 0.025. That is an IR, in-box Lorentz violation, i.e. an error.
  - With B₀P_{L,R} it is m-independent to 2e-3. This validates the normal/Z-term structure (`r105_partner_conv.out`).

| loop (per y²/16π²) | Wilson e / Wilson partner | box b₁ = 0.8 e / box partner | box e / Wilson partner |
|---|---|---|---|
| selectron + photino, chiral B₀P_L + B₀P_R (2 selectrons) | −1.494 (N = 128–192, m = 0.1, 0.05) | −2.847 to −2.850 | −2.42 (N = 64) |
| selectron + photino, scalar B₀ (1 selectron) | +0.01 to +0.11 (not converged) | −2.84 (N = 64) | −2.42 (N = 64) |
| N = 2 neutral a, pseudoscalar B₀g₅ | −2.661 | −2.517 | −1.137 |
| N = 2 neutral a, scalar B₀ | −1.8 to −3.6 (not converged; massless-boson threshold) | −4.6 to −6.5 (not converged) | −3.2 to −5.1 (not converged) |

- **Matching.** The photino is Clifford-flat and massless. In the Wilson column its dispersion equals the naive photon's (2|sin(q/2)| per axis), matching R10-1's "Wilson circle, no photon box" electron row.
- **Result.** Every converged partner entry is ≤ 0, the same sign as the photon loop (−17.96, −10.66).
  - With the N = 1 SUSY value y² = 2e² (R): Δ = δc_e − δc_γ ≈ −17.96 − 2.99 = −20.95 (Wilson) and −10.66 − 4.8 to −5.7 = −15.5 to −16.4 (box). The pseudoscalar a-loop makes it more negative still.
  - In physical units, c_e − c_γ ≈ −9e-3 to −1.2e-2. That is 3e16 to 5e16 times R8-5's 2.66e-19 photon-decay bound.
  - The only near-zero entry (the scalar Wilson case) would need y²/e² ≳ 170 to cancel.
- **Scope.** These are the cheapest constructions: on-site Yukawa; partner curves equal to the photon's or the electron's; one loop. They are not an exact SUSY (Lemma PD) and not a class. "The pairing provably cannot cancel the electron self-energy" is **not** proved.

## 4. Against the FIXED readings (`TESTS.md:4073-4076`)

**Worker reading: FAIL (bounded), clause 1, in class 𝒮.** Referee required before recording.

- **Clause 1** ("no lattice supercharge compatible with box symbols and Ward-forced gauge coupling exists in a stated class"):
  - Lemma PD: every 𝒮 supercharge forces transverse photon and photino zero modes at q ≠ 0, so it cannot carry R8-5's doubler-free box photon. Its matter coupling is Ward-forced Peierls, since M_A is the Hessian.
  - Lemma J adds that charged matter needs twice R10-1's content.
  - Theorem Q shows that the obstruction is in the gauge sector only.
- **Clause 2** (the pairing provably cannot cancel the electron self-energy): **not met**. Only §3.6's computations exist: the same sign in every converged construction.
- **PASS is not met.**
  - No law with a stated lattice supersymmetry and a box photon exists in 𝒮.
  - The non-SUSY minimal-pairing law cancels the photon (R10-1) and graviton TT (§3.5) coefficients, but leaves Δ ≈ −15 to −21.
- **If the referee judges 𝒮 too narrow:** INCONCLUSIVE. Then the open routes are:
  - equivariant or extended structures (twisted N = 2 with its scalar a; KKU-type orbifolds with A–scalar mixing);
  - light-cone supercharges with an exactly additive P̃;
  - non-C¹ symbols.
- **The record, if confirmed.** "The edge supertrace is the free part of an exact lattice supercharge (Theorem Q; vacuum energy exactly 0, residual 2⟨1/E⟩Δm²). In SUSY-QM form the gauge multiplet cannot join it with a doubler-free photon (Lemma PD, a lattice Chern–Simons doubling). The minimal pairing rule cancels the one-loop photon and graviton-TT speed and TT mass for every edge shape. Coupling gravity through Q does not. The electron's split survives, and the partner loops built enlarge it."

## 5. Prices (named, not adopted)

- **P-site.** 8 CAR modes plus 8 real CCR modes per site (neutral), or 16 plus 16 (charged, Lemma J). This requires graded composition and infinite-dimensional bosons, against `AX:43-53`.
- **P-dyn.** H = {Q, Q†} as the dynamics rule (`AX:116-130`).
- **P-flat.** Clifford-flat, unit-speed edge curves (taste doubling).
- **P-match.** Exactly matched masses, which means unbroken pairing:
  - a charged scalar degenerate with the electron (reading; comparator R excludes it);
  - or a soft split, with residuals 2⟨1/E⟩Δm² (vacuum), 0.335m_s² (photon, R10-1), and an uncomputed TT residual.
- **P-gauge.** Photon/photino doublers (Lemma PD), or leaving 𝒮 (open).
- **P-grav.** The minimal pairing coupling rule, not "through Q".
- **For the electron.** Nothing built cancels it. A tuned relative-speed counterterm remains (R8-5's price).

## 6. Strong-word check

- **"Exact"/"identically":**
  - the operator identities of Theorem Q (free);
  - E_vac = 0 (free, Gaussian);
  - the static zero for coupling (Q);
  - Theorem PT's algebraic identity, at one loop, q along an axis, with matched masses.
- **"Proved":**
  - Theorem Q;
  - Lemma J (Schur);
  - Lemma PD (topological; C¹ symbols and the 𝒮 hypotheses);
  - §3.4's N = 1 statement;
  - Theorem PT (hand algebra above, with the general Γ case).

  Lemma PD's step 3 (the tensor argument) is written out in my working, not reproduced at full length.
- **"Checked":** every table number, with convergence in the `.out` files. The partner-loop code was validated only internally (the IR/LI test and agreement between the two code paths, −1.4937). There is no independent code.
- **"Not converged":** the scalar a-loop and the scalar selectron Wilson rows.
- **Not claimed:**
  - any statement outside 𝒮 about supercharges;
  - two loops;
  - mass-split TT residuals;
  - the Ward completion of the graviton coupling;
  - observational exclusion of partners beyond comparator R.

## 7. For the referee

1. **Lemma PD:**
   - the C₁ uniqueness (Hermitian, linear, C₁(q)q = 0 ⇒ iaε·q);
   - the sign-of-product step;
   - the Chern ±2;
   - whether 𝒮 (canonical SUSY-QM, C¹, no A–scalar mixing) is a fair "stated class";
   - whether equivariant twisted N = 2 escapes it.
2. **Theorem PT:**
   - t(k, k′) and the |Δc|² rearrangement;
   - that the (M) boson vertex is a legitimate "minimal" coupling;
   - rerun `r105_tt_paired.py`, including the non-unit-speed control.
3. **The partner loop:**
   - the Z-term structure and the B₀ requirement;
   - whether the sign is convention-safe against R8-5's B − A. Both measure the physical speed, and δc < 0 means slower.
4. **Theorem Q's generators** and Lemma J's commutant.

No downloads were saved: web lookups were abstract-level only (arXiv hep-ph/0404271, hep-lat/0206019, and a search for hep-th/0004203 and hep-lat/0011052).
