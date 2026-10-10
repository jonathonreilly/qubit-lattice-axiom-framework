# C3 lane K-ana: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. Codex sol referee: pending if the verdict is a FAIL or no-go.

**Verdict (worker):** INCONCLUSIVE against the fixed reading. The analytic lane cannot supply the converged numbers that decide PASS-by-"systematically to 0" against FAIL.

The PASS-by-exact-identity branch is closed under hypotheses H1-H5. This is a conditional no-go and must be refereed before it is recorded:
- No identity built from W(B4), the gauge invariance of K7a's kinetic term or the U(1) Ward identity forces the 5 anisotropic O(e^2) forms to vanish.
- The only identity that would do it is an exact Ward identity of the coupled stress through O(s^3).
- That identity needs a charge that adds up exactly on the lattice-scale resonance set. Its on-shell defect is nonzero in the K3a class and at every K3a' range up to R=18.

Expected outcome:
- Natural couplings: FAIL by orders of magnitude.
- K3a'-optimized stress at R=18: marginal, about C x 3e-4 relative, with C = O(1) unknown.
- The fixed-basis numbers depend on the convention at O(1) until the two shear masses are tuned.

**Plain summary:** Keeping the fixed grid needs one more protection for gravity beyond the two tuned shear numbers: the grid must not make gravitational waves travel at different speeds in different directions. Exact algebra shows that the five direction-dependent terms are set, one to one, by how far the matter's momentum flow fails to be exactly conserved, and that three of the five change the speed or polarisation of a gravitational wave. Nothing else on offer forces those terms to zero: not the grid's 384 symmetries, not the gauge symmetry of the graviton's own kinetic term, and not the photon's gauge rule. Only an exactly conserved momentum flow would, and interacting matter on a fixed grid has none in any class tested so far, because lattice-scale "umklapp" collisions spoil momentum conservation. Their size is therefore a number this lane cannot pin down. For natural couplings it is expected to be of order one, far above the 1e-4 bar. For the best stress available it is roughly proportional to that stress's leftover defect, about 3e-4 at range 18, which sits right at the bar. Physically, the speed tuning needed would be mild (about 1e-10 to 1e-13 against the GW170817 neutron-star merger) next to the 1e-98 shear-mass tuning, but it is still a tuning.

# Lane K, analytic worker (campaign C3): can an exact identity remove the 5 anisotropic W(B4) graviton forms at O(e²)?

**Worker and provenance.**
- Claude Opus 5.5, maximum effort, analytic lane K.
- Same model family as the lane-K numeric worker. I worked independently and did not open its folder.
- **Clock:** started 00:51Z; `PREREG.md` stamped Sat Oct 10 01:04:13 UTC 2026, before any computation; report at about 01:35Z.
- No papers were downloaded. Literature named here is cited from memory and labelled COMPARATOR (not re-read in this run).
- **Labels:** EXACT (rational sympy algebra), CHECKED (numerics run here), ARGUED, COMPARATOR.

## Plain summary

Keeping the fixed grid needs one more protection for gravity beyond the two tuned shear numbers: gravitational waves must not travel at different speeds in different directions.
- Exact algebra (§3.2) shows that the five direction-dependent terms are fixed one to one by how far the coupled matter stress fails to be exactly conserved.
- Three of the five change the speed or polarisation of a gravitational wave (§3.3).
- Nothing else on offer forces them to zero (§3.5): not the grid's 384 symmetries, not the gauge symmetry of the graviton's own kinetic term, not the photon's gauge rule. Only an exactly conserved stress would.
- Interacting lattice matter has no such stress in any class tested so far, because lattice-scale umklapp resonances spoil momentum conservation (K3a, §3.8).

So there is no free identity, and the outcome is a number:
- For natural couplings it is expected to be of order one.
- For the K3a′-optimized stress it is roughly proportional to that stress's leftover defect (3e-4 at R = 18), which straddles the 1e-4 bar.

## 1. What I read

- **In full:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md`.
  - `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, with its generated primitive baselines. The kinetic-isotropy primitive is what makes K7a's hypercubic Z⁴ the relevant setting. I did not open `axiom_premise_nodes.json` separately.
  - Packet `TESTS.md`: the rules and every section, including Campaign C3 and lane K's fixed readings.
  - Packet `SUMMARY.md`, `agents/kill_F2.md` and `agents/kill_F2_referee.md`.
- **The named parts:**
  - `agents/B1_report.md` §2.1–2.3 and §5 (Test 2).
  - `agents/B_referee.md` item 18 and ranked test 2.
  - Candidate pack `TEST_LOG.md`: K7a, K3a, K3a′, K3a″, W1 and the wave-1 summary.
- **Code skimmed:**
  - `scratchpad/test_K7a/k7a_symbol.py`, its G7 form count.
  - `scratchpad/test_K3a/k3a_prime/scalar_defect2.py`. K3a′'s defect is the mean |relative vertex defect| on a fixed set of on-shell resonances.

## 2. Setting, my reading of "the 5", hypotheses

**Setting.**
- K7a's staggered h on Z⁴, with symbols s_μ = 2 sin(q_μ/2).
- Gauge symmetry δh = sξ + ξs.
- Induced action Γ₂ = ½ h(−q)Π(q)h(q) at O(e²).

**"The 5"** (fixed in PREREG; this is not a change of the reading).
- K7a has 9 W(B4) two-derivative forms: 4 are O(4)-invariant and 1 is gauge invariant.
- "The 5" are the O(4)-breaking directions, i.e. the image of Π⁽²⁾ in (9 forms)/(4 O(4) forms).
- **Basis-free criterion:** they vanish iff Π⁽²⁾ is O(4)-invariant.

**Hypotheses.**
- **H1:** the whole coupled theory (lattice QED + stress + seagull + h) is W(B4)-covariant and translation invariant, with a symmetric vacuum.
- **H2:** Π has a Taylor expansion through O(q²). This holds for massless QED with a stress whose couplings have finite second moments. It can fail for slow power-law tails.
- **H3:** no tadpole. The cosmological-constant tuning is assumed done, as the "two shear tunings" price already assumes.
- **H4:** K7a's staggered basis and gauge transformation, exactly as in K7a.
- **H5 (the obstruction input):** at O(e), the coupled stress's charge is not exactly additive on the lattice-scale resonance set. This is K3a (refereed, tested class) and K3a′ (every R ≤ 18).

## 3. Results

### 3.1 The form space (EXACT; `k_forms_exact.py`)

There are 9 W(B4)-invariant forms (Reynolds orbit sums over all 384 elements, in rational arithmetic), of which 4 are O(4)-invariant. The gauge map has rank 8, and its kernel is exactly K7a's Q = ¼(F1 − 2F2 + 2F3 − F4). This reproduces the K7a referee's 9/4/1 independently.

| Label | Form | Type |
|---|---|---|
| F1 | s² h:h | O(4) |
| F2 | \|hs\|² | O(4) |
| F3 | (s·h·s) tr h | O(4) |
| F4 | s² (tr h)² | O(4) |
| A1 | Σ_μ s_μ² h_μμ² | anisotropic |
| A2 | Σ_μ s_μ² Σ_ν h_μν² | anisotropic |
| A3 | (Σ_μ s_μ² h_μμ) tr h | anisotropic |
| A4 | Σ_μ s_μ h_μμ (hs)_μ | anisotropic |
| A6 | Σ_{μ≠ν} s_μ² h_νν² | anisotropic |

- Odd orders in s vanish by the W(B4) reflections: every axis index must appear an even number of times. So Π = Π⁽⁰⁾ + Π⁽²⁾ + O(s⁴).
- **Exact O(4) Haar averages** (`k_forms_tools.py` (a); rank-6 tensor projected onto the 15 isotropic pairings):
  - ⟨A1⟩ = F1/24 + F2/6 + F3/12 + F4/48
  - ⟨A2⟩ = F1/6 + F2/3
  - ⟨A3⟩ = F3/3 + F4/6
  - ⟨A4⟩ = F2/3 + F3/6
  - ⟨A6⟩ = 7F1/24 − F2/6 − F3/12 + 7F4/48
- The canonical anisotropic part is Âi = Ai − ⟨Ai⟩.

### 3.2 The five are fixed one to one by the Ward-identity violation (EXACT)

- Let W^ν(s) = s_μ Π^{μν,ρσ}(s), the gauge variation of Γ₂.
- In K7a's variables the gauge transformation is exactly linear in s, so the orders separate: W⁽¹⁾ = s·Π⁽⁰⁾ and W⁽³⁾ = s·Π⁽²⁾.
- The map G: Π⁽²⁾ → W⁽³⁾ (124 monomials × 9) has rank 8 and kernel span(EH).
- The images of the O(4) block (rank 3) and of the anisotropic block (rank 5) are linearly independent.
- **Consequence:** the 5 anisotropic coefficients are a fixed rational linear function (a left inverse) of W⁽³⁾. G is stored in `k_forms_tools_data.json`. They vanish iff the anisotropic projection of the O(s³) Ward violation vanishes.
- **The mass does not feed it.** In s-variables the mass Π⁽⁰⁾ does not enter W⁽³⁾. In q-variables it enters through s = q − q³/24, which is bookkeeping, not physics.
- **Cross-check available to the numeric lane:** compute W⁽³⁾ directly from Π, apply the left inverse, and compare with the fitted coefficients.

### 3.3 Three of the five move gravitational waves (EXACT; pattern CHECKED)

- **Count.** A3 and A4 vanish on every TT mode (s·h = 0, tr h = 0). A1, A2 and A6 act on TT modes and are independent there. On TT the 9 forms span 4 dimensions: 1 isotropic and 3 anisotropic. **The graviton speed and birefringence cost is 3 numbers.**
- **Pattern** (`k_forms_tools.py` (b)): eigenvalues of each canonical part on the 5 Euclidean TT polarisations, relative to s² e:e.

| Direction | Â1 | Â2 | Â6 |
|---|---|---|---|
| axis (1,0,0,0) | −1/24 (×5) | −1/6 (×5) | −7/24 (×3), +17/24 (×2) |
| face (1,1,0,0) | −1/24 (×4), +1/8 | −1/6 (×2), +1/12 (×2), +1/6 | −7/24 (×3), +5/24, +17/24 |
| body (1,1,1,1) | −1/24 (×2), +1/12 (×3) | +1/12 (×5) | −7/24 (×2), +1/12 (×3) |

- **Reading:** Â2 changes the speed with direction; Â6 splits the polarisations along an axis (birefringence).

### 3.4 One component of the Ward identity is enough, and on Z⁴ it is all or nothing (EXACT)

- **One component suffices.** W⁴ ≡ 0 at O(s³) alone forces Π⁽²⁾ ∝ EH (sympy solve: c1 = −c4, c2 = 2c4, c3 = −2c4, all A-coefficients 0).
- **All or nothing for operator identities.** A W(B4) element maps axis 4 to axis 1. So a W(B4)-covariant stress whose energy current is exactly conserved also has exactly conserved momentum currents.
- **Consequence:** K3a's continuous-time asymmetry (H exact, P broken) has no W(B4)-covariant counterpart on Z⁴. Either all four translation currents are conserved or none is.

### 3.5 What each candidate mechanism can do (EXACT; short proofs)

- **W(B4):** allows all 9 forms (§3.1).
- **Gauge invariance of the K7a kinetic term:**
  - This is a property of the tree action. Π is a separate functional, induced by the matter.
  - Adding any of A1…A6 to Γ keeps W(B4), K7a's tree gauge invariance and the U(1) Ward identity intact. So none of these, alone or together, can force the 5 to vanish.
- **The U(1) Ward identity:** protects the photon (one Maxwell form, K7a). It says nothing about h.
- **An exact Ward identity of the coupled stress:** this is sufficient.
  - Suppose S[φ,h] is invariant under δh = sξ + ξs together with a local matter transformation. Then T is the Noether current of a translation-like symmetry, and the seagull is its completion.
  - With H2 and H3, W ≡ 0 up to local Jacobian or contact terms. These are fixed by the symmetry, not tuned.
  - Then Π⁽⁰⁾ = 0 and Π⁽²⁾ ∝ EH: all 8 non-EH coefficients vanish, the 5 included.
  - By §3.2 this is also the only lever, since c_an = L_an·W⁽³⁾.

### 3.6 W(B4) is a precondition (EXACT; `k_forms_tools.py` (d), `k_speed_form.py`)

- Take the symmetry of a continuous-time stress such as K3a's: cubic O_h on space times time reflection (order 96).
- Under it there are 26 two-derivative forms, and **2** gauge-invariant ones.
- The second is the time-rescaled EH, Q(DhD; Ds) with D = diag(1,1,1,λ). It is gauge invariant for every λ, and on TT modes it gives (a² + λ²b²)/2: a free graviton speed 1/λ.
- **Consequence:** if the coupled stress is not W(B4)-covariant, the 9-form test is the wrong space. Even a conserved stress then leaves c_g/c_γ free: the T1/Collins problem again.

### 3.7 While the shear masses are untuned, the five depend on the field basis (EXACT; `k_basis_mixing.py`)

- Write Π⁽⁰⁾ = m1 Σh_μμ² + m2 Σ_{μ≠ν} h_μν² + m3 (tr h)².

| Local redefinition | Change in Π⁽²⁾ |
|---|---|
| h → (1 + αs²)h (O(4)-covariant) | δc_A1 = δc_A6 = 2α(m1 − m2); δc_F1 = 2α·m2; δc_F4 = 2α·m3 |
| R = s sᵀ tr h | A3 shifted by 2α(m1 − m2) |
| R = s(hs)ᵀ + (hs)sᵀ | A4 shifted by 4α(m1 − m2) |

- An O(4)-invariant mass (m1 = m2) shifts no anisotropic coefficient.
- K3a″'s E-type and T-type masses have opposite signs, so the anisotropic mass is not small.
- **Consequence:** the reading is well defined in K7a's fixed staggered basis. The physical speed cost is basis independent only after the shear masses are tuned, or once the form of the mass counterterm is specified.

### 3.8 The missing conservation property (inputs CHECKED and bounded, refereed; the rest ARGUED)

**What is needed.**
- A continuous, translation-like symmetry of the interacting lattice matter.
- Equivalently, a quasi-local stress conserved in the vacuum two-point function through O(s³).

**What fails at O(e) (K3a, refereed).**
- An IR-normalised charge (f(p), f_γ(k)) must be additive on the on-shell resonance set. That set lies at lattice scale (|p| ≥ 1.49) and includes umklapp processes.
- No such charge exists in the tested class.
- At q = 0, the divergence's on-shell matrix elements equal this additivity defect, independent of the O(e) correction P¹ to the stress. Reason: ⟨f|[H₀, P¹]|i⟩ = (E_f − E_i)⟨f|P¹|i⟩ = 0 on shell (EXACT).

**Best stress** (K3a′, refereed; its extrapolation is INCONCLUSIVE):

| R | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 |
|---|---|---|---|---|---|---|---|---|---|
| δ(R) | 0.114 | 0.0224 | 0.00735 | 0.00316 | 0.00162 | 0.00095 | 0.00061 | 0.00044 | 0.00030 |

**Natural vielbein coupling** (K3a″, refereed).
- The q⁰ violation at O(e²) is c₂ = −0.0130 e² (axis) and +0.0125 e² (face) per cell, with no small factor.

**At all orders.** The same holds unless the lattice law has a hidden continuous translation symmetry (ARGUED). COMPARATOR, from memory:
- **Peierls umklapp:** crystal momentum is not conserved in umklapp collisions.
- **Lattice energy-momentum tensor** (Caracciolo–Curci–Menotti–Pelissetto 1988 and 1990; Giusti–Pepe 2015): it is not conserved, and its hypercubic sextet and triplet parts need separate finite renormalisations, fixed only by imposing Ward identities.
- **Shiraishi (2019):** a non-integrable chain has no local conserved quantities.

### 3.9 Expected size (ARGUED; toy CHECKED)

**Structure.** At O(e²), δ_ξΓ₂ = ⟨ξ·D ; h·T⟩ + the seagull mismatch. This is linear in the divergence D, so |c_an| ≤ ‖L_an‖·‖W⁽³⁾‖ ∝ the residual non-conservation.

**Free-field toy (CHECKED, but not the lane-K setting)** (`k_free_demo.py`, `k_free_demo_summary.out`).
- **Setup:** a free massless scalar on Z⁴ with a natural site-placed √g g⁻¹ coupling whose stress is not conserved; one loop.
- **Grid:** N = 12, 16, 24, 32 (1/N² convergence, consistent with the successive differences); ε = 0.025 and 0.05 agree to 1e-3; the 9-form fit residual is ≤ 5e-5.
- **Masses:** m1 = −0.02171, m2 = −0.00612, m3 = −0.02582.
- **O(q²) coefficients, extrapolated in N:**

| F1 | F2 | F3 | F4 | A1 | A2 | A3 | A4 | A6 |
|---|---|---|---|---|---|---|---|---|
| +0.00032 | −0.00064 | +0.00109 | +0.00834 | +0.0050 | +0.0031 | −0.0187 | −0.0031 | +0.0004 |

- **Ratios to c_F1:** A1 +15.6, A2 +9.5, A3 −58, A4 −9.6, A6 +1.3.
- **Basis shift:** 2α(m1 − m2) = +0.0039 for hypercube smearing (α = −1/8), as large as c_A1 itself.

**Natural couplings.** r = |c_an|/|c_EH| = O(1) or larger: there is no small parameter.

**Optimized range-R stress.**
- r ≈ C·δ(R), plus an off-shell residual. That residual depends on how the O(e) part of the stress is built; K3a′ fixes only the on-shell defect.
- At R = 18, r ~ 1e-4 to 1e-3 for C ~ 0.3 to 3. **This straddles the bar.** r should fall with R for as long as δ(R) does.

**Physical scale** (ARGUED; a = ℓ_P, K7a's Q multiplying M̄²/2 = 1/(16π) ≈ 0.02 in lattice units).
- Δc_g/c ~ 1e-2 for natural couplings, and ~1e-5 for the optimized stress at R = 18, against ~1e-15 from GW170817.
- That means a 3-number tuning to ~1e-10–1e-13. It is mild next to the ~1e-98 shear masses, because the speed terms are marginal (dimension 4) while the masses are relevant (dimension 2).
- Removing it by range alone needs δ ~ 1e-14. The K3a′ power law would put that at R ~ 1e4–1e5 sites. That is a 10-decade extrapolation, quoted as a scale only, **not a verdict**.

## 4. Verdict against the fixed reading: INCONCLUSIVE

**PASS by an exact identity: closed (a conditional no-go; referee required).**
- Under H1–H5, the only identity that forces the 5 coefficients to vanish is an exact Ward identity of the coupled stress through O(s³) (§3.2, §3.5).
- At O(e) that identity needs a charge that adds up exactly on the resonance set. That charge's on-shell defect does not depend on the O(e) correction to the stress, and it is nonzero both in the K3a class and at every K3a′ range.
- W(B4), K7a's tree gauge invariance and the U(1) Ward identity provably cannot replace it.
- At all orders: the same, unless there is a hidden continuous translation symmetry (ARGUED).

**PASS by "systematically to 0", and FAIL: not decided here.** Both need converged numbers.
- **Expectation for natural couplings:** FAIL by orders of magnitude.
- **Expectation for K3a′'s best stress at fixed R = 18:** marginal, about C × 3e-4, and convention-dependent at O(1) unless K7a's basis is fixed or the masses are tuned first.
- **Under the reading's "size" (L) and precision improvement:** at fixed coupling the coefficients converge to nonzero values fixed by W⁽³⁾.
- **Under longer stress range R:** they should fall like δ(R). Counting R as "size" would be a reinterpretation of the reading, and I do not adopt it.

**Not excluded:**
- a stress outside the class whose charge is exactly additive (possibly non-smooth with power-law tails: the R → ∞ limit, if K3a′'s defect really goes to 0; H2 may then fail);
- another lattice law with a hidden continuous symmetry;
- an accidental zero for one particular coupling, which would not be an identity.

## 5. What a referee should re-check

1. **The exact algebra.** Re-run `k_forms_exact.py`, `k_forms_tools.py`, `k_basis_mixing.py` and `k_speed_form.py`. Each takes about 10 s in rational sympy and needs no inputs.
2. **§3.5.** Check that gauge invariance of Π is equivalent to the coupled stress's Ward identity, up to local Jacobian terms. Check whether staggered shift or taste symmetries add anything for a taste-singlet stress; I argue they reduce to translations.
3. **§3.8.** Check that the T¹-independent on-shell defect actually enters the O(e²) vacuum correlator. I argue it does, through intraband matrix elements of D¹ in time orderings with smooth weights. No principled (untuned) off-shell choice of T¹ restores the vacuum Ward identity; tuning local counterterms always can, and that tuning is the reading's "graviton-speed tuning".
4. **For the numeric lane:**
   - Is the coupled theory W(B4)-covariant (§3.6)? A transplanted continuous-time stress is not.
   - Is the decomposition done in K7a's staggered s-basis?
   - Report the basis shift 2α(m1 − m2) next to c_an (§3.7).
   - Cross-check c_an against L_an·W⁽³⁾ (§3.2).
   - If cheap, run two stress ranges R to test linearity in δ.
5. **The reading's normalisation.** "Relative to the gauge-invariant form" is ill-defined when Π is far from gauge invariant (in the toy, c_F1 ≪ c_an). The numeric report should state which EH projection it uses.
6. **The §3.9 estimates.** They have unknown O(1) factors. The tree normalisation of K7a's Q (M̄²/2) should be confirmed.

## 6. Files

All in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/K-ana/`:
- **Pre-registration:** `PREREG.md`
- **Form space, Ward map, TT count, one-component result:** `k_forms_exact.py` / `.out`
- **O(4) averages, TT pattern, rational G, reduced symmetry:** `k_forms_tools.py` / `.out` / `_data.json`
- **Basis mixing:** `k_basis_mixing.py` / `.out`
- **Speed form under reduced symmetry:** `k_speed_form.py` / `.out`
- **Free-field toy:** `k_free_demo.py`, `k_free_demo_eps0.025_N12_16.out`, `k_free_demo_N24_32.out` (plus `.err`, peak memory 1.85 GB), `k_free_demo_N24_32_eps0.05.out` (duplicate), `k_free_demo_eps0.025.json`, `k_free_demo_eps0.05.json`, `k_free_demo_summary.py` / `.out`

No repository file was edited.

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** True

**Corrected verdict:** INCONCLUSIVE against the fixed lane-K reading. This part stands: no converged O(e^2) number exists in the lane-K setting, so FAIL is not reached, and no exact identity was exhibited, so PASS is not reached.

The sub-claim "PASS by an exact identity: closed (a conditional no-go)" must be narrowed to the following:
- **What is established.** In a W(B4)-covariant Z^4 theory, the symmetries in hand (W(B4), tree gauge invariance of the K7a kinetic term, the U(1) Ward identity, discrete staggered shifts) allow all 9 two-derivative forms. So none of them forces the 5 anisotropic coefficients to zero (EXACT). Those 5 coefficients are a fixed rational linear function of the O(s^3) Ward violation W3 (EXACT).
- **What is sufficient.** An exactly conserved, W(B4)-covariant interacting stress is sufficient, given the gauge completion, an invariant measure and no tadpole (ARGUED, standard).
- **What is not established.**
  - Necessity of the full Ward identity: only the anisotropic (oblique) component of W3 has to vanish.
  - Absence of such a stress in the setting the no-go assumes (H1). The obstruction evidence (K3a, K3a', K3a'') comes from a continuous-time Hamiltonian class with O_h x Z2 symmetry, which the worker's own §3.6 shows is not W(B4)-covariant. It was refereed only as a bounded-class obstruction.

So the identity route is not closed. It reduces to the open question whether a conserved interacting W(B4)-covariant stress (or a hidden continuous symmetry) exists, and that question is untested on Z^4.

The 9-form test is also the wrong space for the setting exactly as specified (K3a's continuous-time stress): 26 forms, 2 of them gauge invariant, with a free c_g/c_gamma. This should appear in the verdict, not only in §3.6 and §5.4. The size expectations (FAIL by orders for natural couplings; marginal for the R=18 optimized stress) remain ARGUED and decide nothing.

**Issues:** 1. **The no-go overstates necessity (logic).**
   - §3.2 shows exactly that c_an = 0 iff the component of W3 in im(G_an), taken along im(G_O4), vanishes.
   - §3.5 and §4 then say "only an exactly conserved stress would" and "the only identity ... is an exact Ward identity". Full W = 0 is sufficient, not shown necessary.
   - Under H5 the correct statement is weaker: the known symmetry group allows all 9 forms. The "unless hidden symmetry" escape should then read "hidden continuous translation or rotation symmetry".

2. **H1 and H5 are evidenced in incompatible settings (scope).**
   - H5 is cited as "K3a (refereed, tested class) and K3a' (every R <= 18)". Both are continuous-time Hamiltonian lattice QED: 3D KS staggered fermions, Yee Maxwell, O_h x Z2 symmetry.
   - By the worker's own §3.6 and §3.4, that class violates H1.
   - On Euclidean Z^4 the resonance condition would involve quasi-energy mod 2pi, and no W(B4)-covariant interacting stress has been tested. H5 in the H1 setting is therefore an untested premise.
   - The K3a referee also confirmed only a bounded-class obstruction ("NOT CONFIRMED as a theorem"). The K3a' defect is a ridge least-squares diagnostic, "not the optimum and not a bound".
   - So "closed" sits badly beside the worker's own "Not excluded" list.

3. **The lane setting as specified fails H1.**
   - "K3a's optimized range-R stress" is continuous-time and only a charge (f(p), f_gamma(k)), not a full local stress with a specified O(e) off-shell part. The setting is underdetermined, and the 9-form decomposition does not apply to it.
   - The worker flags this (§3.6, §5.4) but does not carry it into the §4 verdict.

4. **"3 numbers" is a TT-restriction count, not the physical speed-tuning count.**
   - CHECKED by me: A1, A3, A4 and A6 couple TT polarisations to pure-gauge directions on face and body-diagonal propagation. A2 does so for generic directions. Only axis propagation is mixing-free.
   - If the gauge directions are lifted only at O(c s^2), the Schur complement adds an O(c) term -B D^-1 C to the TT dispersion. That happens when the masses are tuned away: Pi0 = 0, or after the shear tunings leave 3 of the 4 gauge directions massless at O(s^0).
   - Then A3, A4 and the O(4) gauge-breaking coefficients also enter at first order (ARGUED, 2x2 example: shift = c(alpha - beta^2/gamma)).
   - Such light Stueckelberg-type modes are themselves extra propagating modes. The EXACT label covers only the count of restricted forms.

5. **The sufficiency proof leaves a hole.** §3.5 says "W = 0 up to local Jacobian or contact terms ... fixed by the symmetry". The q^0 and q^2 coefficients are exactly such local terms. The claim holds cleanly only for an h-independent linear matter transformation with an invariant measure plus H3, and that should be stated.

6. **The size estimate's link to K3a' is weak.**
   - The T1-independence argument (on-shell, E_f = E_i) does not apply to vacuum two-point matrix elements, where E_n != E_0. So the vacuum O(q^2) anisotropy depends on the off-shell O(e) stress, which K3a' does not fix.
   - "r ~ C delta(R)" is ARGUED with an uncontrolled piece, but the plain summary states it as "roughly proportional".
   - The "straddles 1e-4" depends on normalisation:
     - relative to the induced O(e^2) EH it is 1e-4 to 1e-3;
     - relative to the tree M^2/2, the worker's own §3.9 gives about 1e-5, which is below the bar.

7. **Minor points.**
   - The free toy uses site-placed h, not K7a's staggered basis. It has a large anisotropic mass (basis shift 0.0039 vs c_A1 0.005) and a non-conserved free coupling, although conserved free stresses exist (K3a). It is an illustration only, and the worker labels it so.
   - Shiraishi 2019 concerns a specific chain (XYZ in a field) and allows H itself.

**Confirmed.**
- 9/4/1 count; Ward map 124x9 of rank 8 with kernel EH; image ranks 3 (O(4) block) + 5 (anisotropic block) independent.
- TT span 4 = 1 + 3.
- W^4 = 0 alone forces EH.
- All five O(4) Haar averages, re-derived analytically by me from the rank-4 and rank-6 isotropic averages: <A1> = (F4 + 2F1 + 4F3 + 8F2)/48, and so on.
- TT eigenvalue table entries for the axis and body directions.
- Basis-mixing formulas; the reduced-symmetry count 26/2; the speed form (a^2 + lam^2 b^2)/2.
- The free-toy numbers and their 1/N^2 convergence (successive-difference ratio 0.211 to 0.212).

**Re-runs:** All runs used OMP_NUM_THREADS=2, each under 10 s. Files are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/K-ana/verify/.

1. **rerun/: the worker's exact scripts, copied and re-run.** Outputs are byte-identical to the worker's .out files:
   - k_forms_exact.py
   - k_forms_tools.py
   - k_basis_mixing.py
   - k_speed_form.py

2. **indep/check_forms_numeric.py: my independent float code (no sympy, none of the worker's code).**
   - Character-formula dimensions: W(B4) gives 9.0 and O_h x Z2 gives 26.0.
   - Reynolds-projector ranks: 9 and 26.
   - Ward-map ranks: 8 and 24, so the gauge-invariant dimensions are 1 and 2 (null singular values at 5e-16).
   - O(4)-invariant subspace inside the W(B4) forms: dimension 4.
   - Ward ranks: O(4) block 3, anisotropic block 5, total 8 (images independent).
   - TT total rank 4, with the O(4) block at 1.
   - My first version had a pull-back bug in the group action; it was fixed before these results.

3. **indep/mixing_worker_forms.py: TT versus pure-gauge bilinear couplings of the worker's named forms.**
   - All zero for axis propagation.
   - Nonzero for face (A1, A3, A4, A6 each 0.242), body3, body4 (A1 0.148, A4 0.148, A6 0.443) and generic directions (A2 0.093 for generic only).
   - The O(4) forms F1 to F4 never mix.

4. **rerun/k_free_demo.py at eps = 0.05, N = 12 and 16.**
   - It matches the worker's eps = 0.025 values to about 6e-4 relative (A1: 0.003584 vs 0.003582).
   - This confirms the eps-agreement claim, for which no same-N file survived in the worker's folder.

5. **Analytic check by hand.**
   - All five O(4) Haar averages are reproduced from the isotropic tensor averages, for example <A6> = 7F1/24 - F2/6 - F3/12 + 7F4/48. This was cross-checked through A1 + A6 = s^2 sum h_mm^2, whose average is F1/3 + F4/6.
   - The TT eigenvalues for the axis and body directions are reproduced.
