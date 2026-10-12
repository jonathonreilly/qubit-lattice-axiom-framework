# C5 R13-4 report: tails. Are the BF Coulomb-type tail and the off-box gravity-completion tail physical, or constraint-solving?

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 20:18Z to about 21:00Z. No repository file was edited. No downloads; no web lookups (all literature below is RECALLED).

**Scratch.** `S/` = `.../scratchpad/C5/R13-4/`. Scripts and outputs in `S/scripts/` (each under 3 min, `OMP_NUM_THREADS=2`):
- `r134_oneill_fd.{py,out,log}`: high-precision (mpmath, nested central differences) check of Lemma Q, the reduction identity for the BF quotient law, on two gauged toys.
- `r134_green.{py,out}`: the lattice Coulomb kernel G(r), the size of the BF tail, and a mean-field screening estimate.
- `r134_cone.{py,out}`: (iii) maximal group velocity over the whole zone, and commutator leakage outside the c = 1 cone, for the box laws and NN comparators.
- `r134_sublum.{py,out}`: (iii) an explicit box law that is subluminal on the whole zone, and its leakage.
- `r134_cone2d.{py,out}`: (iii) the same leakage in d = 2 (R9-5's dimension) by FFT.
- `r134_nl_fock.{py,out}`: (i) the Fock-space algebra of Theorem NL: commutation of N_x with every ι_s and ι_s†, the double-commutator formula, and the pair norm.
- `r134_susy_compression.{py,out}` (with `r134_oneill_fd_lib.py`, the library part of `r134_oneill_fd.py`): (i) the compression P_hH_flatP_h does not commute with Q.

**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`). `TESTS.md` C5 method (`:2302-2320`), the C5 results from round 6 on, and C5 Round 13 (`:4561-4702`; R13-4 at `:4644-4664`). `agents/C5_S14_synthesis.md`. `SUMMARY.md` §§21–25 (`:534-675`). R12-3 report, referee and verdict (`vR12-3`); R12-1 report and verdict (`vR12-1`); R12-6 report (unrefereed); R11-2 verdict (`vR11-2`); R9-5 report and verdict (`vR9-5`); R7-1 report; R11-6 entry (`TESTS:4326-4331`).

**Labels.** proved (complete under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator (all RECALLED this session).

---

## 0. In plain words

1. **(i) The BF photon multiplet's long-range term is of two kinds, and one of them is physical.**
   - The bosonic part, and a "fermion-charge Coulomb energy", are exactly like Coulomb-gauge QED: they are what you get by solving Gauss's law in a local theory. Harmless.
   - But restricting the fermions to the "horizontal" states (what R12-3 needs for its supercharge) adds one more term to the Hamiltonian. It takes a neutral pair of matter fermions at one site and puts it at another site, with amplitude proportional to e² times the lattice Coulomb kernel, about e²/(4πr). Geometrically, it is the O'Neill curvature of the quotient field space.
   - This term moves particles, so it acts on physical observables at a distance. It is tied to R12-3's exact supercharge: dropping it breaks Q (checked). The rate of change of the commutator between the pair-number at x and the pair-number at y reaches 56e²G(r), about 14e²/(πr) (proved; G(r) checked to 4πrG = 1.00006 at r = 64). A local law gives exactly zero there.
   - So no local "extended" version of the BF law with the same physical content exists in the stated class.
   - R12-6's local equivariant law is not such a version: it adds two massless neutral scalars and a fermion as physical particles. Reading: the BF law looks like the limit of R12-6's law in which that scalar becomes infinitely fast, and exchanging it gives the tail.
   - Size (reading): the matter's own zero-point fluctuations screen the kernel in states near the vacuum, at about 2 lattice spacings in a mean-field estimate. The operator-level power law stays.
2. **(ii) The gravity completion's tail: OPEN.**
   - It is not a choice of basis for the constraints (proved).
   - It makes the gauge transformations themselves reach across space (proved from its form). So no local observable is gauge-invariant, and the registered commutator test cannot be run in R12-1's degree-2 ansatz. That ansatz is also not fully built (`vR12-1:5`).
3. **(iii) Control: the box laws are faster than light at the lattice scale.**
   - The matter box laws actually used have maximal group velocity over the whole zone of 4.1 (R7-1 and R9-5's qubit version, b = 2), 12.4 (R7-1, b = 2.6) and 4.6 (R8-5's Wilson-box Dirac), not 1 (checked).
   - This is forced for any one-band box wider than b*(m): π/2 at m = 0, 1.71 at m = 0.3 (proved, mean-value theorem).
   - A box narrower than π/2 can be subluminal everywhere (checked, v_max = 0.993). It costs the proton almost nothing in boost range: rapidity 45.4 becomes 45.0.
   - R8-5's photon symbol is already subluminal (v_max = 1, reached only in the box).
   - The faster-than-light signal is a Planck-momentum effect. Its weight in any observable Gaussian-smeared over 7 lattice spacings or more is below e^{−98} for b = 2 (reading).

**Against the FIXED readings:** (i) **PHYSICALLY NON-LOCAL** (worker reading; referee required), in the class stated in §3.1. The bosonic sector alone is LOCAL-EQUIVALENT. (ii) **OPEN**. (iii) numbers in §3.3.

---

## 1. Hypotheses and classes (stated before titles)

- **H-BF (object (i)).** R12-3's class 𝒩 law with charged matter (`C5_R12-3_report.md:77-81,132-162`):
  - Real coordinates x^a: A on links, B on plaquettes, τ on cubes, and φ_s ∈ ℝ¹⁶ on sites (16 real CCR per site, onsite charge J with J² = −1, Lemma J).
  - One complex fermion ψ_a per coordinate; Q = Σψ_a†(p_a − i∂_aW), with W = ⟨B, dA⟩ + ⟨τ, dB⟩ + ½⟨φ, M_Aφ⟩ gauge invariant.
  - Abelian gauge action by affine isometries u_s(x) = T_s x + c_s, with c_s = d₀δ_s on A and T_s = eJ on φ_s. The orbit metric is g_st = u_s·u_t = (d₀ᵀd₀)_st + e²|φ_s|²δ_st.
  - Physical space 𝔅 = basic forms: L_s ω = 0 and ι_s ω = 0, with ι_s := u_s·ψ.
  - **Inner product:** the flat L² product restricted to invariant forms (group averaging). R12-3's "quotient metric" Hamiltonian (`:161`) is then H_q := ½(Q Q^♯ + Q^♯ Q), where Q^♯ = P_h Q†|_𝔅 is the adjoint of Q|_𝔅 and P_h is the orthogonal projector onto horizontal forms.
  - A different measure (without the orbit volume) changes Q^♯ by an interior product. That adds only fermion-bilinear terms to H_q and leaves §3.1's four-fermion term unchanged (proved: {Q, ι_κ} contains at most fermion bilinears).
  - Matter curves: Wilson (strictly nearest-neighbour) or box (super-polynomially quasi-local).
- **"Local extended formulation" (registered, `TESTS:4656`).** A Hamiltonian H_ext on an extended space, with local constraints, preserving the constraint subspace, and with H_ext restricted to it unitarily equal to the given law.
  - **Class 𝓔 (for the no-go).** Extensions in which the BF law's own local, gauge-invariant, horizontality-preserving observables (defined in §3.1) are represented by operators supported near their site.
  - The canonical extended space Ω(X) with Gauss law and horizontality is in 𝓔. So is any extension that adds auxiliary fields while keeping matter operators local.
- **H-grav (object (ii)).** R12-1's degree-graded constraints with completions T₀₀^{(1,E)}, T₀₀^{(1,h)}, P^{(1,E)}, P^{(1,h)} (`C5_R12-1_report.md:47-75`). The off-box completion has a symbol homogeneous of degree −1 at zero smearing momentum (`:142-146`). As corrected by `vR12-1:5,15`: a local-germ statement only; the gravity gate, JS/JJ kernels and midpoint phases are not built.
- **H-box (object (iii)).** One-band number-conserving box matter (R7-1, `C5_R7-1_report.md:61-71`; R9-5's qubit realization uses the same ε̃ with b = 2.0, b₂ = 3.1, m = 0.3, `C5_R9-5_report.md:39`). Also R8-5's photon symbol d(q) = ρq + (1 − ρ)2 sin(q/2) and R8-5's Wilson-box Dirac.
- **Excluded, not addressed:** the N = 4 Kähler–Dirac law as an object in its own right (R12-6), except as a comparator for (i); interacting gravity beyond degree 2; non-abelian gauge groups; Euclidean (set B) lattices; interacting box matter in (iii).

## 2. Prior art (each counted once)

- **R12-3** (`vR12-3:5`): "the quotient adjoint requires an inverse orbit Laplacian/Coulomb kernel; the local equivariant completion remains unbuilt." The worker's locality caveat is at `C5_R12-3_report.md:159-162`.
- **R12-6** (worker, unrefereed): the local equivariant (σ, η) law (`C5_R12-6_report.md:27-33,113-152`); σ's potential ½|σ|²|v|² and the σ–pair Yukawa (`:129-134`); content 8 + 8 per momentum (`:150`). I use only these, and recheck the content count in §3.1(f).
- **R12-1** (`vR12-1:5,15`): the 1/r^{d−1} tail is required within the fixed completion ansatz; sufficiency is not established. P12-2 (`C5_R12-1_report.md:272`). The worker said its dressing non-locality is "in the states, not in the law" (`:205`). That statement concerns the box domain, not the off-box completion.
- **R11-2** (`vR11-2:5`): Marolf's theorem allows instantaneous long-range dynamics in its scope.
- **R7-1 / R9-5 tail constants** (`C5_R7-1_report.md:129-131`; `vR9-5:9`): hopping falls super-polynomially, not exponentially (2.0e-5 at r = 32, 1.9e-9 at 128). The R9-5 constants are floating-point estimates, not certificates. **R11-6** large-r fits, β ≈ 0.3–0.45 (`TESTS:4330`).
- **Repo microcausality notes:** `docs/MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md` and `docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`. Both give nested-commutator support growth for supplied finite-range H. I use that standard fact in §3.1(c) and do not use the notes as inputs.
- **Coulomb gauge in this packet:** `agents/C4_V3_report.md:205` (unresolved E_L cloud caveat) and `agents/C5_R9-8_report.md:205` (A_T couplings with Coulomb kernels).
- **Comparators (RECALLED, not verified this session):**
  - Coulomb-gauge QED as the reduction of temporal-gauge QED with Gauss's law;
  - O'Neill's submersion formulas (1966) for the curvature of a Riemannian quotient;
  - Witten's SUSY QM / Weitzenböck four-fermion curvature term;
  - Lieb–Robinson bounds (finite range; Hastings–Koma; polynomial-decay versions by Else et al. and Tran et al.);
  - Hegerfeldt's theorem on positive-energy one-particle non-causality;
  - Donnelly–Giddings and Marolf on gravitational dressing;
  - Dirac's Coulomb dressing (kernel ∂Δ⁻¹).

## 3. Results

### 3.1 Object (i): the BF quotient law

**(a) Lemma Q, the reduction identity. Proved (hand algebra); checked on two toys to 1e-15.**

On 𝔅:

  **H_q = P_h H_flat − ½ P_h Σ_{s,t} X_s† (g⁻¹)_{st} X_t,**

where:
- H_flat = ½{Q, Q†} is the local ambient Hamiltonian;
- X_t := {ι_t, Q†} = i Σ_{ab} T_t^{ab} ψ_aψ_b. For R12-3's matter this is ie ψ_tᵀJψ_t: a field-independent annihilator of a neutral fermion pair at site t, containing no derivatives;
- X_s† = {Q, u_s·ψ†}.

Proof.
1. Q maps 𝔅 to 𝔅 (Cartan: ι_sQω = L_sω − Qι_sω = 0). So Q^♯ = P_hQ†.
2. On 𝔅, P_hQ†ω is basic, so QP_hQ†ω = P_hQP_hQ†ω. Hence H_q − P_hH_flat = −½P_hQVQ†, with V = 1 − P_h.
3. ι_tQ†ω = X_tω and ι_rι_tQ†ω = X_tι_rω = 0. So Q†ω has at most one vertical occupancy, and VQ†ω = Σ(u_s·ψ†)g⁻¹_{st}X_tω. This decomposition is exact: the remainder is annihilated by every ι_r, and (u_s·ψ†)(·) is orthogonal to horizontal forms.
4. P_h(u_s·ψ†) = 0 and {Q, u_s·ψ†} = X_s†. So P_hQVQ†ω = P_hΣX_s†g⁻¹_{st}X_tω. ∎

Checked (`r134_oneill_fd.out`): toys with generic Gaussian×polynomial basic forms, a non-quadratic invariant W, e = 0.7, and generic points.
- T1, one generator on (A, φ ∈ ℝ⁴): |H_q − RHS| = 7.0e-16 (1-forms), 8.6e-16 (2-forms) and 3.5e-16 (3-forms). The controls fail as they should: dropping the four-fermion term misses by 0.059 (2-forms) and 0.56 (3-forms) but not on 1-forms, where X = 0; the unprojected H_flat misses by 0.75–2.2.
- T2, two sites and one link (9 coordinates), so g⁻¹ has an off-diagonal entry, g⁻¹₁₂ = 1.42: |H_q − RHS| = 1.4e-17 on a basic 2-form. The control without the four-fermion term misses by 0.131. The s ≠ t (inter-site) part of the term alone has size 0.058, so the transfer between different sites is present in the exact reduced Hamiltonian.
- The fermion algebra of Theorem NL is checked separately in an explicit Fock space, `r134_nl_fock.out`, with two sites, n = 4 and 6 real matter components per site, and a link fermion:
  - [N_x, ι_s] = [N_x, ι_s†] = 0 to 4e-16;
  - [[S, N_x], N_y] = −4g⁻¹_{xy}(X_x^{W†}X_y^W + h.c.) to 7e-16;
  - ‖X^{W†}|0⟩‖² = 2e²(n − 2) exactly, hence 28e² for n = 16.

Reading (comparator R): the extra term is the O'Neill A-tensor contribution to the Riemann tensor of the quotient metric, entering through the Weitzenböck four-fermion term of SUSY QM on X/G. On the lattice, g⁻¹ couples distant sites.

**(b) Which parts are "Coulomb gauge" and which are not.**
- On physical states, Gauss gives u_s·p = (fermion charge at s). The vertical part of ½p² in H_flat is then ½ρ_ψ g⁻¹ ρ_ψ: a density–density Coulomb energy.
- It sits inside the local H_flat, so it is constraint-solving in the QED sense. The bosonic (zero-fermion) sector is H_q = H_flat restricted to invariant functions (proved: H_flat preserves form degree, and 0-forms are horizontal). The extended formulation is explicit and local, as in QED. Its free photon leakage outside the cone decays super-polynomially (R8-5 symbol, §3.3(c), checked). An interacting Lieb–Robinson bound for the unbounded CCR fields is not proved. So: **LOCAL-EQUIVALENT** for the bosonic sector, with the decay checked at the free level only.
- The one-fermion sector has H_q = P_hH_flat, because X annihilates pairs. There P_h is non-trivial: |H_q − H_flat| = 0.75 on the T1 1-form. Its first-order commutators with 𝔅-preserving local observables are local (§3.1(c)). Higher orders are not examined: second-order nested commutators put P_h between local terms.
- The pair-transfer term −½X†g⁻¹X is not a density–density term. It moves a neutral pair from t to s.

**(c) Theorem NL: the pair-transfer term acts at a distance on gauge-invariant local observables. Proved; constants checked.**
- **Observables.** Let W_x = span(φ_x, Jφ_x)^⊥ ⊂ ℝ¹⁶. It is 14-dimensional and J-invariant, and depends on φ_x. Let N_x = Σ_{a∈W_x}ψ_a†ψ_a.
  - N_x is bounded, Hermitian, gauge invariant and supported at site x.
  - It commutes with every ι_s and ι_s†, because u_s(φ) ⊥ W_x pointwise. Hence it commutes with P_h and preserves 𝔅. It is a local observable of the BF law itself.
- **Locality of the first term.** For an operator O commuting with P_h, [[P_hH_flatP_h, O_x], O_y] = P_h[[H_flat, O_x], O_y]P_h. This vanishes for |x − y| > 1 with cochain symbols and Wilson matter, and is super-polynomially small with box curves.
- **The tail.** With X^W the part of X inside W:

  **[[H_q, N_x], N_y] = 2 P_h g⁻¹_{xy}(φ) (X_x^{W†}X_y^W + X_y^{W†}X_x^W) P_h** for |x − y| > 1.

- **Its size.** g⁻¹_{xy}(φ) ≤ G(r) := (Δ⁻¹)_{xy} entrywise, and approaches G(r) as φ → 0 on all sites. The bound uses resolvent positivity for an M-matrix.
  - On normalized basic states with a gauge-invariant boson wavefunction supported where 0 < |φ_x|, |φ_y| ≤ ε and |φ_s| ≤ ε elsewhere, and with a J-pair in W at y (respectively x), the matrix element is 2‖X^{W†}|0⟩‖² = 56e² times ⟨g⁻¹_{xy}⟩. That lies between 56e²G_{μ²=e²ε²}(r) and 56e²G(r).
  - So the supremum over such states is **56e²G(r)**, with 4πrG(r) = 1.0815, 1.0198, 1.0010 and 1.00006 at r = 1, 4, 16 and 64 (checked, `r134_green.out`). That is ≈ 14e²/(πr), a power law.
- **Consequence.** (d/dt)⟨ω′|[N_x(t), N_y]|ω⟩ at t = 0 equals i⟨ω′|[[H_q, N_x], N_y]|ω⟩ ~ e²/r.
  - If H_ext had finite range ρ, preserved the constraint subspace, restricted to H_q, and kept N_x and N_y local (class 𝓔), every t-derivative of order n < (r − 1)/ρ of that commutator would vanish. That is the nested-commutator support argument.
  - With interactions decaying like F(r), one would need F(r) ≳ e²/r.
  - Hence **no local or super-polynomially quasi-local extended formulation exists in 𝓔**. In the registered words, the gauge-invariant commutator's time derivative decays no faster than a power. ∎
- **Operational form (suggested).** A local unitary at y (creating a J-pair) changes ⟨N_x(t)⟩ at order t² e⁴G(r)², with no light-cone delay.

**(d) Size and screening (reading).**
- The kernel is field-dependent. In states near the matter vacuum, e²|φ_s|² acts like a mass for the orbit Laplacian.
- Mean-field estimate: v² = 16⟨φ_a²⟩ ≈ 3.2 for R8-5's Wilson-box matter, so e·v ≈ 0.54/a with e = 0.303. The screening length is ≈ 1.85a, and G_screened/G ≈ 2e-4 at r = 16 (`r134_green.out`).
- At fixed order e² (g⁻¹ → Δ⁻¹) the vacuum matrix element is the unscreened power law. The mean-field resummation is not proved; ⟨g⁻¹⟩ ≥ ⟨g⟩⁻¹ holds only in operator order, and rare regions with small |φ| keep power-law contributions at exponentially small probability.
- So the operator-level non-locality is exact. Its size in near-vacuum states at a = ℓ_P is plausibly Planckian-range. It also needs two matter fermions at one site in a J-pair, which has amplitude of about (a/L)³ per particle for wavepackets of size L.

**(e) The tail is tied to the exact supercharge. Checked on T1.**
- Dropping the O'Neill term, i.e. using the compression P_hH_flatP_h, breaks R12-3's Q.
- On a basic 1-form, [Q, P_hH_flatP_h]ω = −½ TQω with T = P_hX†g⁻¹X: norm 0.904, matching to 1e-25 (`r134_susy_compression.out`).
- So the law cannot keep exact Q on 𝔅 without the four-fermion term.
- Whether the compression is itself local beyond first order is not examined. It is not proposed as a fix.

**(f) Relation to R12-6 (rechecked what I use).**
- R12-6's equivariant law (`C5_R12-6_report.md:117-140`) is local. But its physical content is 8 bosons + 8 fermions per momentum (`:150`), against BF's 6 + 6 (A_T 2, B 3, τ 1; 7 fermions minus 1 horizontal; `C5_R12-3_report.md:243-245`).
- So it is a different theory: σ (2 massless real scalars with Yukawa √2e, `:260`) and η are physical. It is not a constraint-solving extension of BF in the registered sense, and the item's drop condition ("drop (i) if R12-6 supplies a local completion", `TESTS:4569`) does not apply to BF *without* σ, η.
- **Suggested link (not checked).** R12-6's σ has kinetic coefficient |c|²/2 and potential ½σ̄gσ, and couples to X† through the Yukawa −½σ̄(∂v)ψ†ψ† + h.c. (`:129-134`).
  - In the static limit (|c| → ∞, σ infinitely fast), σ-exchange gives −X†g⁻¹X up to normalization, the same structure as Lemma Q's term.
  - BF would then be the singular limit of the local Cartan family. Its tail would be the exchange of a gauge-invariant scalar with infinite speed, which is physical and not a gauge artefact.
  - Sign and normalization are not checked.

### 3.2 Object (ii): the off-box completion of R12-1

- **(a) Not a basis change. Proved, short.**
  - A completion of the form Σ φ·C₁, with φ a matter bilinear (any kernel), contributes nothing to the degree-2 brackets. Each such term {C₁[N], φ}C₁ + φ{C₁, C₁} vanishes: C₁ is pure gravity and the linear algebra is abelian.
  - So the degree −1 completion that absorbs the off-box Killing jet is not a non-local change of constraint basis. It is a genuine deformation of the gauge generators.
- **(b) The gauge generators reach across space. Proved from the form.**
  - The completion, schematically T₀₀^{(1,E)}[N] = ∫∫N(x)E(x)K(x − y)Ô(y) with K ~ |x − y|^{1−d}, makes a gauge transformation with lapse supported near x act on a matter observable O_y with amplitude ∝ K(x − y)E(x)[Ô(y), O_y].
  - So a strictly local matter observable that fails to commute with the defect density Ô is not gauge invariant. Gauge-invariant observables must be dressed over all space.
  - In GR the gauge generators are local and only the solutions and dressings are non-local (comparator R). Here the non-locality is in the law's generators.
- **(c) Dressing class. Suggested.**
  - The degree −1 kernel has the homogeneity of the Dirac/Coulomb dressing ∂Δ⁻¹.
  - A degree-3 canonical dressing exp(i∫E·K′*O) with a Newtonian kernel K′ = f/s (f smooth, degree −2) trades a singular completion for a change f*O of the matter energy density at degree 2.
  - Absorbing the Killing jet that way requires matter global charges that are Poincaré off the box. No periodic C² band has them: the zone mean of Hess(ε²/2) − I is −1 (C3/R12-1, refereed).
  - So within (dressings + regular matter redefinitions) the non-regularity cannot be removed. It sits either in the completion or in a non-smooth (1/r^{d+1}) energy density.
- **(d) Why (ii) is OPEN.**
  - The registered test needs gauge-invariant local observables. By (b) there are none in the degree-2 constraint system. Dirac observables need a reference frame, which is not built.
  - The object itself is only a local germ (`vR12-1:5`: gravity gate, JS/JJ kernels and midpoint phases unbuilt).
  - Neither the explicit local formulation nor the power-law proof exists.

### 3.3 Object (iii): the box law's own leakage (numbers, no verdict)

**Subtraction (named before any run):** the Klein–Gordon commutator function D(r, t) = (1/2π)∫cos(kr) sin(E(k)t)/E(k) dk of each dispersion. The continuum comparator vanishes identically for r > t, so the subtracted leakage D − D_cont equals D outside the cone. No channel limit is subtracted. The number-conserving one-band propagator has, in addition, the continuum's own Hegerfeldt tail ~e^{−m√(r²−t²)} (comparator R), which is not counted here.

**(a) Maximal group velocity over the whole zone (checked, `r134_cone.out` (A)).**

| law | v_max d = 1 | d = 3 | where |
|---|---|---|---|
| R7-1 / R9-5 matter, b = 2.0, b₂ = 3.1, m = 0.3 | 4.008 | 4.116 | k ≈ 2.68 (transition) |
| R7-1 matter, b = 2.6, b₂ = 3.0, m = 0.3 | 12.24 | 12.42 | k ≈ 2.82 |
| R8-5 Wilson-box Dirac, (2.0, 3.0), r = 1, m = 0.1 | — | 4.569 | k ≈ (2.66, 2.66, 2.66) |
| R8-5 Wilson-box Dirac, (0.8, 2.0), r = 1, m = 0.3 | — | 2.872 | |
| R8-5 photon d, plateau (1, 2) and (2, 3) | 1.0000 | 1.0000 | in the box only |
| NN comparators: sin k / 2 sin(k/2) (m = 0.3); Yee photon | 0.744 / 0.861; 1 | 0.841 / 0.917; 1 | |

**(b) Lemma V (proved, mean-value theorem).**
- Any C¹, odd, 2π-periodic one-band symbol s with s(k) = k on |k| ≤ b has s(π) = 0, so ε̃(πe_x) = m.
- Hence max|∂_xε̃| ≥ (√(m² + b²) − m)/(π − b), which exceeds 1 for every b > b*(m). Values: b*(0) = π/2, b*(0.3) = 1.708, b*(0.5) = 1.786.
- R7-1's b = 2.0 and 2.6 are therefore necessarily superluminal somewhere.
- **The converse is constructive (checked, `r134_sublum.out`).**
  - Take s′ = 1 on [0, b], a symmetric Gevrey step to −1 over [b, π − b], and −1 on [π − b, π]. This gives a C^∞ box law with |s′| ≤ 1.
  - v_max = 0.979 (d = 1) and 0.993 (d = 3) for b = 1.4, m = 0.3. In the massless limit v_max = 1.
- The rapidity budget for a proton at a = ℓ_P falls from 45.4 (b = 2) to 45.0 (b = 1.4).
- Not done: a subluminal Wilson-box Dirac (two-band, with W).

**(c) Leakage outside the c = 1 cone, d = 1, max|D| over 4 sites at x = r − t (checked).**

| law, t = 400 | x = 1 | 5 | 20 | 40 | 80 | 160 | 320 | 640 |
|---|---|---|---|---|---|---|---|---|
| R7-1, b = 2 | 2.2e-2 | 2.0e-2 | 1.3e-2 | 3.6e-3 | 3.6e-3 | 4.9e-3 | 5.3e-3 | 5.9e-3 |
| subluminal box, b = 1.4, m = 0.3 | 1.6e-2 | 1.1e-2 | 6.8e-4 | 1.3e-3 | 7.0e-5 | 2.3e-6 | 7.0e-9 | — |
| R8-5 photon (1, 2) | 7.2e-2 | 1.7e-2 | 1.5e-3 | 1.8e-4 | 2.6e-6 | 5.5e-9 | 1.8e-12 | 5e-17 |
| NN Klein–Gordon, m = 0.3 | 1.2e-11 | 2.0e-12 | 2.0e-16 | floor | | | | |
| Yee photon | 1.2e-1 | 2.9e-2 | 8.1e-6 | 1.1e-12 | floor | | | |

- **R7-1 law.** Inside the superluminal window t < r < v_max·t the leakage is a power law. |D|·t^{1/2} = 0.300, 0.303, 0.296 and 0.298 at t = 100–800 over r ∈ [1.2t, 1.3t] (checked, (E)). It is not super-polynomially small. In d = 2, R9-5's dimension (`r134_cone2d.out`, FFT on a 2048² torus), max|D| over r/t ∈ [1.2, 1.3] gives t·|D| = 0.236, 0.258 and 0.278 at t = 50, 100 and 200. That is the t^{−d/2} stationary-phase law (checked). In d = 3, t^{−3/2} is suggested. Beyond v_max·t it drops to the 1e-16 floor (d = 1, t = 100, x = 640).
- **Subluminal box and R8-5 photon.** The leakage decays faster than any fitted power in x. In d = 2 the subluminal box gives t·|D| = 0.078, 0.039 and 0.017 on the same annuli (t = 50, 100, 200), and 1.7e-10 to 3.2e-10 at x = 320. At t = 1600 the subluminal box gives 9.9e-5, 6.1e-6 and 1.7e-8 at x = 80, 160 and 320. The Gevrey symbol forbids exponential decay (`C5_R7-1_report.md:130`). The numerical s is a 2^16-point interpolation of the C^∞ construction, which is irrelevant at x ≤ 320.
- **NN comparators.** They decay super-exponentially (Bessel fronts) but break the box's exact relativity.

**(d) At a = ℓ_P, a reading on `AX:189-190`.**
- The superluminal modes have |k| > b/a, i.e. Planck momenta. A site-local observable leaks at O((t/a)^{−d/2}) outside the c = 1 cone, out to v_max·t, so the front outruns light by ≈ 3t for R7-1 (v_max − 1 = 3.0 in d = 1, 3.1 in d = 3).
- An observable smeared with a Gaussian of width L carries weight ≲ e^{−(bL/a)²/2} at those momenta: e^{−98} at L = 7a, and about 10^{−3e31} at L = 1e-19 m (6e15 ℓ_P).
- Negligible for every physical observable. The registered expectation "group velocity ≤ 1 achievable on the whole zone" holds only with b < b*(m) ≤ π/2, not for the box laws used so far.

### 3.4 Prices (named, not adopted), against `AX:57` and `AX:116-130`

| price | content | axiom touched |
|---|---|---|
| **P13-4a (BF tail)** | The BF quotient law's O'Neill pair-transfer term: four-fermion, range e²G(r) ~ e²/(4πr), physically non-local in class 𝓔 | Dynamics is downstream (`AX:116-130`), so this is a named price on the supplied dynamics (P-dyn). It is against `AX:57` only if "one fixed nearest-neighbor rule" is read as a range limit on dynamics, which `AX:116-130` do not support |
| | **P47's menu becomes three:** a photon doubler (𝒮; `vR10-5`), a physically non-local O'Neill term (BF), or N = 4 KD content with σ (2 massless real scalars, Yukawa √2e; R12-6, pending referee) | |
| **P13-4b (box superluminality)** | One-band box laws with b > b*(m) have lattice-scale v_max > 1 (4.1 for R7-1/R9-5) | Admissibility's locality (`AX:57`), already priced as quasi-local. The price is avoidable at negligible cost (b < π/2) |
| **P50 (unchanged)** | The off-box completion deforms the gauge generators non-locally (§3.2(b)) | `AX:57` |

## 4. Against the FIXED readings (`TESTS:4659-4663`)

- **(i) BF quotient law: PHYSICALLY NON-LOCAL (worker reading; referee required).**
  - Theorem NL: [[H_q, N_x], N_y] has norm 56e²G(r) ≈ 14e²/(πr) on 𝔅, so the gauge-invariant commutator's first time derivative decays as a power.
  - **Stated class:** the BF Nicolai quotient law of R12-3 with charged matter of ≥ 4 real components per site, the group-averaged inner product, and extensions in 𝓔.
  - The bosonic (zero-fermion) sector alone is LOCAL-EQUIVALENT (exact: H_q = H_flat there). The one-fermion sector passes the first-order test only.
  - Not met: a refereed proof. If the referee rejects class 𝓔, the reading falls to OPEN, not LOCAL-EQUIVALENT: no local extension is known.
  - R12-6's local law does not trigger the item's drop clause (`TESTS:4569`): it changes the physical content (§3.1(f)).
- **(ii) Off-box completion: OPEN.** No local formulation is built and no power-law proof exists. §3.2(a)–(c) are bounded steps.
- **(iii)** Numbers with constants in §3.3. Against the expectation (`TESTS:4664`): "group velocity ≤ 1 on the whole zone" fails for every box law used so far (v_max 4.1–12.4), and is achievable only with b < b*(m) ≤ π/2. "Leakage negligible at a = ℓ_P" holds for smeared observables (reading).
- **Against the expectation for (i)** (LOCAL-EQUIVALENT for the bosonic part; the fermion sector may need the equivariant completion): the bosonic part is confirmed. The fermion sector does not merely "need" a completion. Without σ and η it is physically non-local, and with them the content changes.

## 5. Strong-word check

- **"Exact":**
  - Lemma Q on 𝔅 (algebra; residual ≤ 9e-16 on T1 and 1.4e-17 on T2, with controls failing at 0.06–2.2);
  - the Theorem NL fermion algebra (≤ 7e-16);
  - 4πrG(r) → 1 (checked to 6e-5 at r = 64).
- **"Proved":**
  - Lemma Q;
  - Theorem NL, under the class 𝓔 hypothesis and the operator-norm/state-supremum reading of "decays";
  - §3.2(a) and (b);
  - Lemma V.
- **"Physically non-local":** at the operator level, in class 𝓔. Not claimed for near-vacuum matrix elements after resummation (§3.1(d)).
- **"Suggested":**
  - the σ-exchange link to R12-6;
  - §3.2(c);
  - the d = 3 t^{−3/2} law (d = 1 and d = 2 are checked);
  - operational signalling at O(t²).
- **"Reading":** the screening length, the sizes at a = ℓ_P, and the O'Neill interpretation.
- **Not claimed:**
  - anything about R12-6's law itself;
  - degree-3 gravity;
  - a subluminal Wilson-box Dirac;
  - certified (interval-arithmetic) bounds.

## 6. For the referee

1. **Lemma Q:**
   - the adjoint Q^♯ = P_hQ† for the group-averaged inner product;
   - step 3's single-vertical-occupancy claim;
   - P_h(u·ψ†) = 0 and {Q, u·ψ†} = X†;
   - rerun `r134_oneill_fd.py`.
2. **Theorem NL:**
   - that N_x commutes with every ι_s and ι_s† (u_s ⊥ W_x pointwise), hence with P_h;
   - the commutator formula;
   - g⁻¹_{xy}(φ) ≤ G(r) with the supremum attained as φ → 0;
   - whether class 𝓔 is the right reading of "local extended formulation".
3. Whether the orbit-volume convention or R12-3's "quotient metric" wording could change the four-fermion term.
4. **(iii):** Lemma V, and whether the subtraction (KG commutator, continuum zero outside the cone) is the right observable for the one-band law.

**Files:** `S/scripts/r134_oneill_fd.{py,out}`, `r134_nl_fock.{py,out}`, `r134_susy_compression.{py,out}`, `r134_green.{py,out}`, `r134_cone.{py,out}`, `r134_cone2d.{py,out}`, `r134_sublum.{py,out}`. A superseded slow symbolic version (sympy) was deleted after its only finished output (1-forms, residual 8.9e-16) matched the mpmath run.
