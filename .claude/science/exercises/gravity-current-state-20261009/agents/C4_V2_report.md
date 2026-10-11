# Lane RV2, probe V2: can Rule R be made canonical, and does the scattering defect matter? (report)

Worker: Claude Opus 5.5, the same family as the supervisor, V1 and W1. Run 18:15Z to about 18:55Z, 2026-10-11. No repository files were edited. Scratch: `.../scratchpad/C4/V2/`. **Not refereed.**

Setting as in V1: massive onsite normal-ordered φ⁴ on Z³, lattice KG ω(k), free momentum symbol f = sin k, uniform TT strain h, with μ_E and μ_T2 the vacuum Hessians. The interacting vacuum is Ω and its transport is Ω_h := U_h(λ)Ω. H_full(h) = U_h(λ) H U_h(λ)† is exactly isospectral to H but not translation-covariant. The coupling used is H_loc(h) = H_full(h) − D(h), where D is the dropped non-covariant part.

## Reading against the FIXED line

**V2: INCONCLUSIVE, leaning PASS. No FAIL disjunct is met.**

**(a) Canonical R.** R has an exact basis-free form. Two of the four candidate principles select it and give μ ≡ 0. The selecting principle is a coupling rule, though, not a consequence of the four axioms. Whether it counts as "derived" is the one remaining question, and it is a reading.
- The selecting principles:
  - (iii) with the vacuum norm: minimise the vacuum norm of the dropped part;
  - (iv): uniform strain acts as an exact relabelling on the vacuum and one-particle sectors.
- Kato (i) and Gell-Mann–Low (ii) fix the dressing W uniquely. Kato's W is V1's S. Neither fixes the split.
- New, and PROVED:
  - With the Kato dressing, μ = 0 at O(λ²) holds for every split whose difference from R annihilates the free strained vacuum. So **at O(λ²) the referee's objection (i) is answered by the dressing alone.**
  - **From O(λ³) on, the split must be referenced to the interacting vacuum Ω_h.** Otherwise a cloud-scattering term of natural size enters.

**(b) The defect.**
- Relative size on normal shells is 0.037·(ka)², with local slopes between 1.96 and 2.08 (CHECKED). An improved symbol pushes it to 0.006·(ka)⁴.
- Universality defect of a composite: η = 1 − ⟨cos κ_x⟩ ≈ 0.39·(a/r_rms)² for smooth binding (CHECKED). Lattice-scale contact binding is the worst case, η ≈ (2–8)·p_B·a.
- At a = ℓ_P this is 1e-40 (smooth) to 1e-20 (worst case), against MICROSCOPE's ~1e-15.
- **No feedback into μ at O(λ³) under R** (PROVED). There is none at any perturbative order once W is built to the order needed. W truncated at O(λ^n) leaves a removable artifact at O(λ^{2n+2}).

**Why not PASS.** The PASS needs R to be "derived". What I found is a canonical, basis-free and μ-agnostic statement of R, with Kato forced underneath it. By MINIMAL_AXIOMS ("a choice not fixed by the supplied structure remains a named conditional") it is a named conditional coupling principle.

**Why not FAIL.**
- Candidate principles do select R and give μ = 0.
- The defect is far below bounds.
- Under R the defect does not feed back.

**Supervisor's "real risk" (O(λ³) feedback).**
- It is real for every split that is not referenced to Ω_h. There it is natural size: the vacuum cloud lives at lattice momenta, where the defect is O(1).
- It is exactly absent under R. So the decider moves back to (a).

## 1. What R is, basis-free (PROVED)

**Exact identity.** H_full(h) is unitarily equivalent to H, so E_vac(H_full) = E₀ for all h. For any dropped part D:

E_vac(H_loc) − E₀ = −⟨Ω_h|D|Ω_h⟩ − Σ_n |⟨n_h|D|Ω_h⟩|²/(E_n − E₀) − … (perturbation series in D around the exact eigenbasis of H_full(h)).

**R in basis-free form.**
- R ⟺ D Ω_h = 0 = D† Ω_h. Then Ω_h is an exact eigenvector of H_loc(h) with eigenvalue E₀, so μ_E = μ_T2 ≡ 0.
- No quasiparticle basis enters this statement. The basis is needed only to *construct* such a D.
- This answers the referee's "not basis-free" for the condition. The condition still references a state, but that state is Ω_h, the ground state of the exactly transported H. It is not chosen.

**Existence needs a vacuum-annihilating P_λ (PROVED).**
- The total of the explicit-position part is B ∝ [P_λ, H] (times h).
- If D Ω_h = 0, the first moment of D's density annihilates Ω_h, so B annihilates Ω.
- Conversely, [P′,H]Ω = 0 makes P′Ω an eigenvector with energy E₀. A unique ground state then forces P′Ω ∝ Ω, and parity forces P′Ω = 0.
- So R is available iff the strain-generating momentum annihilates the vacuum. This is a Wightman-type condition. For the bare P it fails: PΩ = λΣf·T|0⟩ ≠ 0.

## 2. The four candidate principles: what each fixes, and μ

Values are in units of λ² per cell at m = 1. The numbers are reused from V1 and W1, not recomputed.

| Principle | Fixes W? | Fixes the split? | μ_E, μ_T2 at O(λ²) | Locality |
|---|---|---|---|---|
| (i) Kato transport of the vacuum projector: minimal-norm translation-invariant quasi-local generator with e^{λS}\|0⟩ ∝ Ω | **Yes, uniquely:** S₁ = −V₄₀/Σω + h.c. (PROVED, below). This is exactly the S in V1's seagull script. | No | 0, 0 for any split whose difference from R annihilates the free strained vacuum (PROVED, §3). Convention-dependent from O(λ³). | Exponential, length ≈ 1/m (V1) |
| (i′) Kato for the vacuum ⊕ one-particle projector | Adds S^{31} = −V₃₁/D₃ + h.c. (forced; gapped by V1's D₃ bound) | No | same | Exponential |
| (ii) Gell-Mann–Low / Møller W₊ | Yes: 40 and 31 blocks as Kato (i′); 22 block V₂₂/(ΔE + i0) | Not needed: P_in = W₊PW₊† is exactly conserved, so H_full is covariant and nothing is dropped | 0, 0 exactly (isospectral) | **Fails.** The 22 kernel is non-summable (principal value plus on-shell δ; L2-A). Also in/out asymmetric: P_in ≠ P_out because [S-matrix, P] ≠ 0, which is the defect in invariant form. |
| (iii) Minimal vacuum-GNS norm of the dropped part, N(D) = ‖DΩ_h‖² + ‖D†Ω_h‖² per cell, over all splits and dressings | **Yes:** N/V grows as L²·S_B(0) unless BΩ = 0, so finiteness forces P_λΩ = 0 (PROVED) | **Yes:** min N = 0, reached exactly on the R class (PROVED) | 0, 0 (all orders) | Exponential (V1 construction) |
| (iii′) The same with a state-free translation-invariant norm, or the free-vacuum norm | — | No | Undetermined (state-free); O(λ³)-different selection (free-vacuum norm) | ARGUED: the cross term between the explicit-position and local parts vanishes by symmetry on a symmetric box; the remainder is boundary-dominated |
| (iv) H_loc exactly isospectral to H on the vacuum and one-particle sectors | Forces (i′) | Constrains D on those sectors only; R ⊂ (iv) | 0, 0 for every member; tautological on the vacuum | Exponential |
| Control: bare P, site convention (L2 design) | none | site | −1.009e-6, +1.61e-8 | local |
| Control: bare P, centroid convention (W1 Monte Carlo) | none | centroid | +2.335e-5 (E) | local |
| Control: Kato W, coupling linearised (no λ²h² seagull) | Kato | — | −1.419e-5, −7.69e-7 | — |

**The Kato claim (PROVED).**
- Constraint: e^{λS}|0⟩ ∝ Ω at O(λ) fixes the column ⟨n|S₁|0⟩ = −⟨n|V|0⟩/E_n.
- In a translation-invariant sector expansion S = Σ_{p,q} S^{(p,q)}:
  - only the (p,0) kernels act on |0⟩, so they are fixed (here p = 4, from :φ⁴:);
  - anti-Hermiticity fixes (0,p);
  - every block with q ≥ 1 annihilates |0⟩ and is unconstrained.
- Any norm that sums kernel norms over sectors is therefore minimised uniquely by S₁ = S^{40} − S^{40†}.
- **Caveat:** the literal Kato direct rotation of the projector alone is a rank-2, non-extensive generator. "Minimal *within quasi-local translation-invariant generators*" is the right statement.
- The same holds order by order (§4).

**Plain-language principle behind (iii) and (iv).** Uniform strain is a pure relabelling. The coupling may fail to be a relabelling only where particles actually collide, never on the empty vacuum or on a single particle. Stated without reference to μ, this gives μ ≡ 0.

## 3. What the split controls, order by order (PROVED, using §1's identity)

Write D = D_R + Δ, where D_R = W·(anomaly of the transported Kato-frame residual, any kernel convention)·W† is R-compliant and Δ is a local, translation-invariant operator of O(λε).

**Kernel conventions inside the Kato frame are all R-compliant.** These are W1's site, centroid, or any fibre connection, applied to the b-ordered transported residual and then conjugated by W. Each leaves a b-ordered operator in the (3,1), (2,2) and (1,3) sectors, which annihilates W|0_h⟩ = Ω_h. So **W1's ×23 convention dependence disappears once the dressing is Kato**: at O(λ²) outright, and at all orders once W is extended as in §4. It was a property of the bare P.

**Δ annihilates the *free* strained vacuum |0_h⟩ but not Ω_h.** Examples: a convention applied in the original frame, or b-ordered there. Take Ω_h = W|0_h⟩ and W = e^{λ(T − T†)} with T = −V₄₀/Σω. The first-order term in §1 has these pieces:
- ⟨0_h|Δ|0_h⟩ = 0;
- λ⟨0_h|[Δ,S]|0_h⟩ = 0;
- the first non-zero piece is **λ²⟨0_h|T†ΔT|0_h⟩ = O(λ³ε)**.

The second-order term is O(λ⁴). **So μ = 0 at O(λ²) for every such split, and a convention-dependent O(λ³) term appears.** This is the cloud-scattering diagram: two legs of the vacuum's virtual 4-particle cloud scatter through Δ.

**Refinement (PROVED).** Write Δ = λ(εX₁ + ε²X₂ + …), with X₁ and X₂ fixed number-conserving kernels in strained modes.
- The ε-linear piece gives no TT Hessian at O(λ³). In ⟨0_h|T†X₁T|0_h⟩, the Bogoliubov term linear in s produces only a 2-particle component, which X₁ cannot connect to the 4-particle component. The c factors are 1 + O(ε²). So the bracket is constant up to O(ε²), and its first derivative vanishes.
- The O(λ³) cloud term is therefore **μ⁽³⁾ = −2λ³⟨T₄|X₂|T₄⟩**, set by the h² part of the split difference.

**Mixed-frame prescriptions (ARGUED, not computed).** An example: transport the residual 22 vertex in the original frame without its W-conjugation. This produces (4,0)_b contraction pieces at O(λε²). Paired with S^{(0,4)}, these leak into μ already at O(λ²).

**Size of the O(λ³) cloud term outside R (CHECKED inputs; size SUGGESTED).** From `v2_cloud.out`:

| m | ⟨1 − cos k_x⟩ on the cloud | Weight with \|k_leg\| < 0.3 | Defect \|ΔP\|/\|P_pair\| on cloud 2→2 sub-scatterings |
|---|---|---|---|
| 1 | 0.86 (uniform BZ: 1.00) | 0.15% | median 0.74 |
| 0.3 | 0.80 | 0.42% | median 0.69 |

- The cloud sits at lattice momenta, where no (ka)² suppression applies.
- The cloud matrix element of the actual 2↔2 vertex is ⟨T₄|V₂₂|T₄⟩ = +8.57e-8 per cell, L-converged from L = 12 to 20 (`v2_cloud_scale.out`, CHECKED). For comparison, ⟨T†T⟩ = 7.11e-7, so the typical 22 element on the cloud is 0.12.
- So μ⁽³⁾ ~ 2λ³·8.6e-8·w, where w is an O(1) weight from X₂ that I have not computed (SUGGESTED). That is about 1e-7·λ³: ~10% of the L2 E-channel value and ~10× the T2 value, per unit λ. That is natural size, not suppressed.
- **R's interacting-vacuum reference is therefore load-bearing from O(λ³).** It is not cosmetic.

## 4. All orders (objection iii): formal construction (PROVED, perturbative)

**Induction.** At order n, take the residual of W†HW and remove its creation blocks.
- **(p,0) blocks (p ≥ 2), and their adjoints:** remove with S_n = −R_n^{(p,0)}/Σ_p ω. The denominator is ≥ p·m ≥ 2m.
- **(2j+1,1) blocks:** remove with S_n = −R/D_{2j+1}. The denominator is ≥ the gap, which V1 proved positive.
- The numerators are polynomials in lower-order analytic kernels.
- So every S_n is analytic, and exponentially quasi-local at every finite order.

**Consequences.**
- The R construction exists to every finite order.
- With W truncated at O(λ^n):
  - the first convention-dependent vacuum term is O(λ^{2n+2}). It comes from the residual creation blocks at O(λ^{n+1}), whose anomaly cannot be made R-compliant.
  - the 2↔2 defect itself first reaches the vacuum at O(λ^{2n+3}): D_R is O(λ) and acts on the O(λ^{n+1}) admixture of W†Ω, twice.
  - For V1 (n = 1): O(λ⁴) and O(λ⁵). This confirms V1's "μ = 0 through O(λ³)".
- Extending W is forced by vacuum annihilation; it adds no choice.

**Non-perturbative W: open.** Hastings–Wen quasi-adiabatic continuation, or Bachmann–Michalakis–Nachtergaele–Sims automorphic equivalence, would give a quasi-local W with stretched-exponential tails for bounded lattice interactions with a uniform gap (SUGGESTED). Unbounded boson fields need a truncation argument.

## 5. (b) The scattering defect and universality

### 5a. On-shell defect vs momentum (`v2_defect.out`, CHECKED)

**Exact identity, verified to 4e-16.** For a normal process with k₁,₂ = Q/2 ± κ and k₃,₄ = Q/2 ± κ′:

ΔP_i = 2 sin(Q_i/2)(cos κ_i − cos κ′_i).

- The defect is set by the *internal* momentum, and it vanishes at Q = 0.
- In umklapp processes the sign flips and the defect is O(1). Those need |Q| ≈ π/a.

Relative defect |ΔP|/|P_in|, with momenta in a ball of radius s = ka (3000 shells per row):

| s | f = sin: median (m = 1) | median/s² | Local slope | f₂ = (4/3)sin k − (1/6)sin 2k: median | median/s⁴ |
|---|---|---|---|---|---|
| 0.01 | 3.71e-6 | 0.0371 | — | 6.15e-11 | 0.0062 |
| 0.03 | 3.28e-5 | 0.0364 | 1.98 | 4.83e-9 | 0.0060 |
| 0.1 | 3.81e-4 | 0.0381 | 2.04 | 6.26e-7 | 0.0063 |
| 0.3 | 3.28e-3 | 0.0364 | 1.96 | 4.78e-5 | 0.0059 |
| 1.0 | 4.01e-2 | 0.0401 | 2.08 | 5.94e-3 | 0.0059 |

- m = 0.3 is the same to within 10%.
- **The relative defect is ≈ 0.037·(ka)².** The improved symbol makes it (ka)⁴. That is a legitimate local choice of the free momentum density.
- **Physical consequence.** In a field of strain ε, outgoing momenta deviate from transport by a relative ε·0.04·(ka)². At a = ℓ_P and the Earth's surface (ε ≈ 7e-10):

| Process | Relative deviation |
|---|---|
| Nuclear Fermi momentum | 3e-49 |
| LHC partons | 2e-40 |
| 1e20 eV cosmic rays | 5e-26 |

### 5b. Universality of a bound composite (`v2_bound_L40.out`, `v2_contact_m*_N128.out`, CHECKED)

**The band symbol.** On an isolated bound band, the canonical coupling (Principle M / Kato for the band) transports the band with its symbol f_B(Q) = ⟨sin k₁ + sin k₂⟩ = 2 sin(Q/2)⟨cos κ⟩ (exact). A moving composite therefore carries T_ij = f_B,i v_B,j.

**Elementary control (PROVED).** For lattice KG, f = sin k = ω·∂ω/∂k *exactly*, so T^{0i} = T^{i0} (p = E·v) at every k. The elementary particle is exactly universal in this sense.

**The parameter.** For the composite, the momentum that gravitates is f_B = Q⟨cos κ_x⟩ (Q → 0), not Q:

η := 1 − f_B/Q → 1 − ⟨cos κ_x⟩ = ½⟨κ_x²⟩_lat.

η is zero in the continuum, so it is a pure lattice effect.

| Binding | Result |
|---|---|
| Smooth (Gaussian wells, r_rms = 1.4 to 4.7, m = 1 and 0.3, L = 40) | η·r_rms² = 0.366, 0.382, 0.391, 0.393 at m = 1, rising to **0.39–0.40** (m = 0.3: 0.389, 0.397). **η ≈ 0.39·(a/r_rms)².** With f₂: η·r⁴ → 0.36, so η ∝ (a/r)⁴. |
| Lattice-scale contact (separable, infinite volume, N = 128) | η ∝ p_B·a, with η/p_B = 2.5 at m = 1 and 7.6 at m = 0.3 at the smallest p_B, not yet converged. UV-dominated, because ψ ∝ 1/κ². f₂ does **not** help: the tail lives where f ≠ k. |

**Physical translation at a = ℓ_P.**

| System | η |
|---|---|
| Nucleus or deuteron, smooth binding, r ≈ 2 fm | ≈ 0.39·(1.6e-35/2e-15)² ≈ 3e-41 |
| Nucleon, r ≈ 0.85 fm | ≈ 1e-40 |
| Worst case, lattice-scale contact binding, deuteron p_B = 46 MeV | (3–8)·p_B·ℓ_P ≈ 1e-20 to 3e-20 |

- MICROSCOPE bounds |Δη| at ~1e-15. The margin is ≥ 5 orders in the worst case and ~25 orders for smooth binding.
- **Implied bound on the lattice spacing:**
  - smooth binding: a ≲ 1e-22 m;
  - contact-like binding: a ≲ 1e-30 m.
  - So the universality PASS needs a near ℓ_P. That is the scale-reference primitive, an open gate.

**Caveats.**
1. η is a strain-sector (h_ij, momentum-flux) effect. The Newtonian lapse coupling that Eötvös experiments test directly was not part of V1/V2. A uniform lapse rescales H, which is universal trivially.
2. The model also prints η_EP = 1 − f_B/(E_B v_B) and η_LI. These are dominated by the static two-body potential's own continuum Lorentz violation (~E_bind/2m) and are not lattice effects. I do not use them.
3. **Von Laue (PROVED):** under Principle M, f_B(0) = 0, so a composite at rest carries ∫T_ij = 0.
   - Under V1's R alone, the bound band is not protected. A 22-sector split convention can give a rest-frame trace stress of O(E_pot·(κa)²).
   - This is ARGUED, not computed. The TT channels vanish anyway by cubic symmetry for s-wave states.

## 6. Against the supervisor's expectation

| Expectation | Finding |
|---|---|
| Kato or GML selects V1's split ("PASS on (a), probable") | **Partly.** Kato and GML select V1's *dressing* uniquely, and that alone secures μ = 0 at O(λ²). They do not select the *split*. The split is selected by the vacuum-norm and sector-isospectrality principles, which are canonical but are coupling rules. |
| Universality defect ~ (E/M_Pl)², negligible | **Confirmed** for normal scattering and smooth binding (0.04·(ka)² and 0.39·(a/r)²). Lattice-scale contact binding gives a linear p_B·a. That is still negligible at ℓ_P. |
| O(λ³) feedback through lattice-scale loops is the real risk | **It is real for any split not referenced to Ω_h.** It is natural size, because the cloud is lattice-scale and the defect there is O(1). **It is exactly absent under R.** So the risk is precisely the content of R's vacuum reference. |

## Labels

**PROVED (same family, unrefereed):**
- the basis-free form of R and μ ≡ 0 under it;
- R exists iff P_λΩ = 0;
- Kato's unique minimal quasi-local generator equals V1's S;
- the vacuum-norm variational principle forces P_λΩ = 0 and selects the R class (finite-volume first moment; the infinite-volume domain question raised by the V1 referee is not addressed);
- the order counting of §3 (O(λ²) safe for splits that annihilate the free vacuum; O(λ³) cloud term, which comes from the h² part of the split difference only);
- the formal all-orders construction, and the truncation orders (2n+2, 2n+3);
- the identity ΔP = 2 sin(Q/2)(cos κ − cos κ′);
- lattice-KG f = ω·v;
- η = ½⟨κ_x²⟩_lat;
- von Laue under M.

**CHECKED:**
- the defect scaling table, with slope 2 for f = sin and 4 for f₂, at two masses;
- the identity, to 4e-16;
- η scaling, smooth (a/r)² and contact p_B·a, at two masses;
- cloud momentum statistics, and the cloud matrix elements ⟨T†T⟩ and ⟨T₄|V₂₂|T₄⟩.

**ARGUED:**
- state-free norms do not select a split;
- mixed-frame splits leak at O(λ²);
- GML non-locality (from L2-A);
- the rest-frame stress under R-only.

**SUGGESTED:**
- the natural size of the O(λ³) cloud term outside R (≈ 1e-7·λ³ per cell; the weight w of X₂ is not computed);
- the physical η numbers (they depend on the binding's UV tail);
- a non-perturbative W via automorphic equivalence.

**READING:**
- whether "the non-covariant remainder must annihilate the vacuum" is derived or chosen. Under MINIMAL_AXIOMS it is a named conditional coupling principle.

**Not done:**
- the O(λ³) Hessian for a specific non-R split (the X₂ weight w; only the cloud scale was computed);
- non-uniform h;
- the C3 constraint algebra for H_loc;
- fermions (lane RV3).

## Files (`.../scratchpad/C4/V2/`)

- `v2_defect.py` / `v2_defect.out`: on-shell defect scaling, identity check, improved symbol, physical translation.
- `v2_bound.py` / `v2_bound_L40.out`: smooth-well composites; η_mom, the f₂ variant, elementary control.
- `v2_contact.py` / `v2_contact_m1_N128.out`, `v2_contact_m0.3_N128.out`: contact composites near threshold, in infinite volume.
- `v2_cloud.py` / `v2_cloud.out`: vacuum-cloud momentum distribution, and the defect on cloud sub-scatterings.
- `v2_cloud_scale.py` / `v2_cloud_scale.out`: ⟨T†T⟩ and ⟨T₄|V₂₂|T₄⟩ per cell (the O(λ³) cloud scale), with L = 12, 16, 20.
- Reused without rerunning: V1's `v1_vacuum_seagull_*.out` and W1's `w1_mu2_m1.out` and `w1_fullflow_mc_m1.out` (control rows in §2).
