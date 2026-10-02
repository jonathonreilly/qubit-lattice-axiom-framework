The harness refused to let this subagent write `c7/hard/gauge/REPORT.md` ("Subagents should return findings as text"), so the whole report is below for you to save. The work was derivation by hand: no code was run and the repo was not touched. Sources are origin/main `0485dc0738`.

---

# REPORT: Lane E, the gauge group and the gauge action

Labels:
- **EXACT**: proof.
- **CHECKED**: finite exact test, done by hand.
- **ARGUED**: reasoning, not verified.
- **LIT**: a source whose title or abstract I fetched; I did not read its proof.

No numerics were run.

## 1. Problem (framework terms)

Supplied throughout: the carrier encoding, the Gauss law, the gauge group of any carrier, and all dynamics.

**(i) Gauge group.** A *local redundancy structure* has three parts:
- carrier sites C;
- a compact group G;
- unitaries Γ_v(g) supported near each vertex v.

It must satisfy two conditions:
- (a) the fixed NN rule commutes with every Γ_v (a Gauss law);
- (b) no record's readout value changes. This is what makes it a redundancy rather than a symmetry that moves readable content.

Question: which G can arise from M_2(C) per site, NN covariance and Record? Can G be (SU(3)×SU(2)×U(1))/Z_6?

**(ii) Gauge action.** Given a G-carrier, write the link or plaquette weight as w = Σ_λ d_λ τ(λ) χ_λ. Is it forced to be the heat kernel (HK), τ(λ) = e^{−tC₂(λ)}? Or is it free, as landed in `BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06`?

## 2. Obstructions (exact scope)

**O1. Site-frame redundancies contain no SU(3). EXACT.**
- Let α be a *-automorphism of ⊗_{x∈C} A_x (A_x ≅ M_2(C)) that maps every site factor onto a site factor.
  - α is injective, and distinct factors meet in C·1, so the induced site map π is injective.
  - The factors generate the algebra, so α = (⊗β_x)∘π.
- Skolem–Noether gives Aut(M_2) = PU(2) ≅ SO(3), so the identity component is ∏_x PU(2)_x. On modules it is ∏_x U(2)_x.
- A simple Lie algebra mapping into ⊕su(2)⊕u(1) maps to zero or injectively in each factor. Injective needs dimension ≤ 3.
- So every connected site-frame group is locally SU(2)^a × U(1)^b.
- Consequences:
  - SU(3) acts on no qubit composite as a frame change. This includes M_2⊗M_2 = M_4: U(3), the commutant of the swap, entangles the two sites. It also includes the cube's M_2^{⊗8}.
  - The one-site module frame U(2) = (SU(2)×U(1))/Z_2 has the electroweak shape.

**O2. Fixed-basis records allow abelian redundancies alone. EXACT.**
- If every carrier site is recorded in a fixed product basis, readout invariance puts Γ(G) in a maximal abelian algebra. That algebra is its own commutant, so Γ(G) is abelian.
- With unrecorded sites, Γ(G) ⊂ D_rec ⊗ B(H_unrec). Non-abelian action is then possible on the unrecorded factor, block-diagonal in the record labels.
- Two landed results are consistent with this:
  - the U(1) ice-rule rung, whose gauge phases are diagonal in the s·n record basis;
  - `RECORDS_REGISTER_COLOUR_ONLY_THROUGH_TRIALITY_AND_SINGLETS_…_2026-09-04`.

**O3. Graph-first SU(3) is a commutant, not a redundancy. EXACT under the reading below.**
- `GRAPH_FIRST_SU3_INTEGRATION_NOTE` takes the commutant of {weak su(2), swap} on C^8, the functions on the 8 corners of a 2³ cell.
- Its generators, starting with the corner shift X_μ, move content between corners. If corners are sites, they change readable records:
  - in the one-particle reading, they change which site is occupied;
  - in the three-qubit reading, they entangle sites (O1).
- The selector V_sel = 32Σφ_i²φ_j² ≥ 0 vanishes on the axes. Axis selection therefore needs the supplied sign "minimise"; maximising gives the S₃ point.
- The fibre-frame notes (`MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_…_2026-06-08` and the bridge `…_2026-06-09`):
  - place C^8 at each *site*, which predates the 2026-06-29 axioms (M_2(C) per site);
  - count as registered just the weak central-sector projectors.
  Under one-record-per-site readability, their local U(3) fails condition (b).

**O4. Landed.** SU(N) links need at least 2N states, so SU(3) needs 3 qubits (`DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_…_2026-09-24`).

**O5. EXACT (Lemma 1, §4).** Gauss invariance fixes centrality but not τ. Wilson, HK and Manton all qualify.

**O6. ARGUED.** "A site never carries more than one record." So the landed i.i.d. emergent-time link walk is record-compatible just when the link value depends on many *distinct* sites' records. Limit theorems must compose distinct carriers.

## 3. Escape routes (ranked)

**R1 (ii), top: a Lévy–Khintchine reduction of the action form.**
- Supplied:
  - S1: a carrier L²(G) with the Gauss law at both ends.
  - S2: a configuration-independent electric factor that conserves Gauss.
  - S3: closure of the weight family under composition (emergent-time powers or planar gluing), continuous in the composition parameter. This is zoom-out covariance.
  - S4: the half-turn acts on G by at most an inner automorphism.
- Shows:
  - w = HK ⊗ (central, symmetric Poisson jumps).
  - One rate per simple factor, plus a positive semidefinite form on the abelian centre, which allows U(1) kinetic mixing.
  - HK holds exactly when the jump measure Π = 0.
  - U(1) Wilson is the pure-jump member.
- ADM-2 becomes Gauss conservation, and "choose HK" becomes "no finite holonomy kicks".
- Cheapest decisive test: §5.

**R2 (i): unidentified frames force a transport.**
- Supplied:
  - no inter-site identification of possibility domains;
  - records lock pure possibilities;
  - a link carrier for the transport.
- Shows (EXACT lemma, §4 D9):
  - Directional NN dependence needs a bond transport valued in SO(3) (or U(2)).
  - A flat transport reproduces the landed global possibility covariance (Heisenberg).
  - A non-flat transport is an SO(3)/U(2) lattice gauge field whose plaquette holonomy is frame-invariant content.
- Test: exact nullspace classification of NN generators on vertex+link carriers invariant under independent site frames, in the style of the landed two-qubit classification.

**R3 (i): colour on unrecorded composite carriers, with the global form from the cell.**
- Supplied:
  - link carriers of at least 3 qubits that are never recorded;
  - an SU(3) constraint energy UΣ_v C₂(G_v), the analogue of the ice energy;
  - the structure C²⊗(Sym²C²⊕Λ²C²).
- Shows (EXACT, §4 D10): the identity component of the unimodular structure group is (SU(3)×SU(2)×U(1))/Z_6, with B−L = +1/3 on 6 states and −1 on 2. This is the SM global form, but it is taste structure, not a redundancy (O3).
- Test: can the 3 interior sites of a blocking-4 coarse link carry a (3,1)⊕(1,3̄) link (6 of 8 states) with NN-local Gauss generators?

**R4: Pati–Salam and hypercharge. Owner-gated, so analysis only.**
- C^8 = C²⊗C⁴ has commutant u(4). The swap breaks it to su(3)⊕u(1)_{B−L}, giving SU(4)×SU(2)_L on one block.
- Y becomes derivable if two things are supplied:
  - a second (opposite-chirality) block in which the selected-axis su(2) is broken to its Cartan Z_μ/2;
  - a rule fixing the mixing between the two abelian generators (anomaly cancellation).
- Given those, Y = Z_μ/2 + (B−L)/2 reproduces 2/3, −1/3, 0, −1 (EXACT arithmetic).
- The undelivered pieces are that breaking and the second block.

## 4. Derivation for R1 (with D9–D10 for (i))

**D1. Setup (S1, S2).**
- Actions: (L_gψ)(U) = ψ(g⁻¹U) and (R_hψ)(U) = ψ(Uh).
- The Gauss operator at v contains L on outgoing links and R on incoming links.
- The step is T = T_E^{1/2} M_f T_E^{1/2}, where M_f multiplies by a gauge-invariant positive f.
- S2 requires the electric factor T_E to conserve Gauss by itself (for example at f ≡ 1).

**D2. Lemma 1 (EXACT).**
- Claim: T commutes with L(G) and R(G) exactly when T = ⊕_λ τ(λ)·1_{V_λ⊗V_λ*}.
  - Proof: Peter–Weyl, plus Schur on the inequivalent G×G blocks.
- For a convolution step T_ν ψ(U) = ∫ψ(Uξ)ν(dξ):
  - T_ν always commutes with L;
  - R_h T_ν R_h⁻¹ = T_{Ad_h ν}, so T_ν commutes with R exactly when ν is Ad-invariant;
  - then τ(λ) = ∫χ_λ dν / d_λ.
- Establishes: ADM-2 for the electric factor is equivalent to Gauss conservation at the right end.
- The landed drifted step (Part 6 of `EMERGENT_GAUGE_HEAT_KERNEL_CLT_…`) is a frame-*covariant* family. Every fixed member fails [T, G_{x+μ}] = 0, so it is covariant but not invariant.
- The landed quenched-staple caveat (`ADM2_GLOBAL_SU3_…`) concerns staple-dependent update kernels, not T_E.

**D3. Lemma 2 (EXACT under S4).**
- Rotating a half-turn about z at a site, then translating by e_x, maps (x,y,z) ↦ (1−x, −y, z). This reverses bond (0, e_x), and it lies in the axiom group.
- With W = U⁻¹ on the reversed bond, a central right step becomes a left step with law ι_*ν. Covariance then gives ν = ι_*ν.
- So τ(λ) = τ(λ̄) = τ(λ)*.
- This kills U(1) drift (τ(n) = τ(−n)) and the cubic Casimir of SU(3) in log τ.
- If the half-turn acts by an outer twist (charge conjugation), the condition is vacuous, because χ_λ(ξ^T) = χ_λ(ξ).

**D4. Composition (EXACT given S3).**
- In emergent time, T_E^n has coefficients τ^n.
- In a plane, gluing gives ∫w₁(aγ)w₂(γ⁻¹b)dγ = (w₁*w₂)(ab) (substitute η = aγ), and the coefficients multiply.
- So a planar disk of A plaquettes has weight w^{*A}.
- In 3D, plaquettes are coupled through the cubes, so planar composition there is ARGUED to be inexact.
- S3 makes {ν_s} a central, symmetric, weakly continuous convolution semigroup.

**D5. Hunt's theorem (EXACT-standard: Hunt 1956, Trans. AMS 81, 264–293; Liao 2004).**
- τ_s = e^{−sψ}, with ψ(λ) = Σ_i c_i C₂^{(i)}(λ) + q(λ_Z) + ∫_{G∖e}(1 − Re χ_λ/d_λ) dΠ.
- Ad-invariance allows one c_i per simple factor and any positive semidefinite q on the centre. D3 removes drift.
- HK holds exactly when Π = 0, which is exactly when sample paths are continuous, which is exactly when the generator is a differential operator. The positive maximum principle excludes C₂²-type generators.

**D6. Casimir content (EXACT).**
- Claim: c_i = lim_{|λ|→∞} ψ/C₂^{(i)}.
- Proof:
  - 1 − Re χ_λ(e^X)/d_λ ≤ (1/2d_λ)·tr(−ρ(X)²). Since this is a class function, average over Ad, which gives ≤ C₂(λ)|X|²/(2 dim g).
  - So jump/C₂ is dominated by |X|²/(2 dim g) near e (Π-integrable) and by 2/C₂ elsewhere. Dominated convergence sends it to 0.
- U(1) Wilson:
  - τ(n) = I_n(β)/I₀(β), and I_n(β) ~ (β/2)^n/n!, so ψ ~ n log n and c = 0 at every fixed β.
  - The von Mises law is infinitely divisible for all κ (LIT: Kent 1977, *Proc. LMS* s3-35, 359–384; Lewis 1975 for small κ).
  - So U(1) Wilson is a pure-jump Lévy law, while HK (Villain on U(1)) is pure diffusion.
- SU(2) Wilson:
  - τ_W(j) = I_{2j+1}(β)/I₁(β). EXACT, via I_{ν−1} − I_{ν+1} = (2ν/β)I_ν.
  - ψ ~ 2j log 2j, so c = 0 if it is a Lévy law.
  - Large β gives e^{−2C₂/β} (ARGUED, standard asymptotics).
- SU(3) Wilson: the coefficients decay factorially (ARGUED).
- Establishes: at finite β, the Wilson/HK difference is the high-flux tail, i.e. jump against diffusion. It is not the low-flux slope, where they agree at t = 2/β.

**D7. CLT window (EXACT).**
- Suppose E_ε|X|² = O(ε) and ν_ε(far) = o(ε). Then τ_ε = 1 − C₂ E_ε|X|²/(2 dim g) + o(ε), so ν_ε^{*s/ε} → HK.
- A fixed kick law at rate r per unit area survives as a compound-Poisson factor.
- Centre kicks Π = ν(δ_ω + δ_ω²) give ψ ⊃ 3ν·[triality ≠ 0]. This is a thin Z₃-vortex area term (EXACT).
- Constituent check (CHECKED by hand at n = 1, 2):
  - Setup: K unbiased spin-½ flux units on SU(2), with n = K/2.
  - Exact coefficients: τ_K(j) = m_j/((2j+1)m₀) = (n+1)/(n+j+1) · ∏_{i=1}^{j} (n−i+1)/(n+i).
  - Expansion (Taylor, EXACT): log τ_K = −C₂/n + C₂/n² − C₂/n³ − C₂²/(6n³) + O(n⁻⁴).
  - So this is HK at t ≈ 2/K, matching Wilson at β ≈ K.
  - The flux is truncated at j ≤ K/2, so a finite carrier is not a Lévy law at all.
- Note on scale: β = 6 corresponds to K ≈ 6, which is outside the CLT regime.

**D8. Result (conditional on S1–S4).**
- w = HK ⊗ (central symmetric Poisson jumps).
- The residual of the action-form question is exactly Π: does any single composed carrier change the holonomy by a finite amount in the zoom-out limit?

**D9. Forced transport (R2, EXACT).**
- Suppose frames are independent per site.
- PU(2)_x-invariance makes μ_x uniform in angle.
- PU(2)_y-invariance makes the dependence on c_y pass through spectral invariants alone, which are trivial for pure possibilities.
- So "varies with NN conditions" needs a supplied R_xy ∈ PU(2).
- If every site's content is frame-relative, no site can carry R_xy without a further identification. This is the exact form of the global→local gate.

**D10. Structure-group kernel (R3, EXACT).**
- Take A⊗(B₀ z ⊕ z⁻³) with A ∈ SU(2), B₀ ∈ SU(3), z ∈ U(1) (6Y charges 1 and −3).
- The identity requires A = z³ and B₀ = z²·1₃, with z⁶ = 1. So the kernel is Z₆.
- The image is 12-dimensional, so it is the identity component of the unimodular structure group.

## 5. Next computation (spec, not run)

**C1: infinite-divisibility test of Wilson weights.** Cheap: single thread, mpmath at 60 digits, minutes.

- **Inputs:**
  - SU(2): τ_W(j) = I_{2j+1}(β)/I₁(β) for j ≤ 2000, β ∈ {1, 2, 4, 6, 8, 12}.
  - SU(3): τ_W(p,q) from torus Weyl integration, p+q ≤ 40, β ∈ {4, 5, 6, 7}.
  - U(1) control: τ = I_n/I₀.
- **Test:** for s = 2^{−k}, k = 1..6, evaluate w_s = Σ d_λ τ^s χ_λ on a class-angle grid that includes the centre, and check w_s ≥ 0.
- **Secondary (SU(2)):** with m = 2j+1, compute the second difference Δ²_m(mψ) = ∫2 sin(mα)(1−cos α)/sin α dΠ. This yields Π directly.
- **Outcomes:**
  - (A) w_s ≥ 0 throughout. Wilson is consistent with a pure-jump law (c = 0), so the framework question becomes diffusion against jumps. Next, locate Π: near e (many small kicks) or at the centre (vortex-like)?
  - (B) w_s < 0 somewhere. Wilson lies in no area-continuous family, so planar zoom-out covariance excludes it and HK ⊗ jumps remains. For SU(3) at β = 6 this sharpens the bridge gap.
  - U(1) must give (A) at every β (Kent). A failure there means a numerical error.

**C2 (control).** Use exact multiplicities in (3⊕3̄)^{⊗K} to check |ψ_K/(t_K C₂) − 1| = O(C₂/K²).

---

## 10-line summary
1. **EXACT:** On any qubit composite, site-frame redundancies are ∏PU(2)_x (U(2)_x on modules), so they are locally SU(2)^a × U(1)^b. SU(3) never arises; U(2) = (SU(2)×U(1))/Z₂ has the electroweak shape.
2. **EXACT:** If every carrier site is recorded in a fixed basis, any redundancy is abelian. Colour can act on unrecorded carriers alone, consistent with the landed triality/singlet note.
3. **EXACT:** Graph-first SU(3) is a commutant on the 2³-cell taste space that moves record-visible corner content. Its selector needs a supplied sign, and the pre-reset fibre-frame bridge puts C^8 at each site.
4. **EXACT:** C²⊗(Sym²⊕Λ²) has unimodular structure group (SU(3)×SU(2)×U(1))/Z₆, with B−L = +1/3 and −1. This is the SM global form, as taste structure rather than redundancy.
5. **EXACT:** With independent site frames, directional NN dependence needs a supplied bond transport. This is the exact form of the global→local gate (R2).
6. **EXACT:** A Gauss-conserving electric factor is central, so ADM-2 is Gauss conservation; the landed drifted step is covariant but not invariant. The bond-midpoint half-turn makes τ real and C-even unless it acts by an outer twist.
7. **EXACT-standard (Hunt 1956):** Under composition closure, the weight is HK ⊗ central Poisson jumps. HK holds exactly when Π = 0, and the Casimir content is c = lim ψ/C₂.
8. **EXACT + LIT (Kent 1977):** U(1) Wilson has c = 0 at every fixed β and is a pure-jump Lévy law, while HK/Villain is pure diffusion. At finite β the action-form question is jump against diffusion.
9. **CHECKED:** K unbiased SU(2) flux units give log τ = −C₂/n + C₂/n² − C₂/n³ − C₂²/(6n³) + …, i.e. HK at t ≈ 2/K, matching Wilson at β ≈ K. β = 6 is outside the CLT regime.
10. **Next (spec §5):** test whether the SU(2)/SU(3) Wilson weights are infinitely divisible (w_s ≥ 0 for s = 2^{−k}). Outcome (A) means Wilson is pure-jump; outcome (B) means it lies in no area-additive family.

Sources:
- [Hunt 1956, Trans. AMS 81](https://www.ams.org/journals/tran/1956-081-02/S0002-9947-1956-0079232-9/)
- [Kent 1977, Proc. LMS s3-35](https://academic.oup.com/plms/article/s3-35/2/359/1579223)
- [Lewis 1975, J. Appl. Prob. 12](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/probability-functions-which-are-proportional-to-characteristic-functions-and-the-infinite-divisibility-of-the-von-mises-distribution/FEEF2DF00CDE25E3B3C9B06D2E7E1B70)