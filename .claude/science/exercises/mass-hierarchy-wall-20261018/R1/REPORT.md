**R1 report: flavour model-builder (Froggatt–Nielsen charges, discrete groups, modular symmetry, textures)**

**Refresher read before concluding:** `MINIMAL_AXIOMS_2026-06-29.md` in full, `PRIMITIVE_REGISTRY_CHECK.md`, `SCALE_REFERENCE_PRIMITIVE_NOTE.md`, and `derivation_obligations.json`. That file has three entries: two charged-lepton readout gates and one theta gate. None is a hierarchy entry. I also read WALL.md, the HIER-2 report and its referee, the GEN-1 and GEN-2 reports, and these notes on main:
- `HIERARCHY_VALUE_FRONTIER_PROBE` (FN with ε = α_bare: loose);
- `PRIMITIVE_P_HEAVYQ` (P-Heavy-B FN fit: WEAK);
- `GENERATION_DEGENERACY_MINIMAL_SYMMETRY_BREAKING`;
- `THE_SMALL_MIXING_ANGLES..._C3_BREAKING` (a shared C3 gives V_CKM = 1).

I only grep-scanned the Koide notes, `CKM_FROM_MASS_HIERARCHY` and `YT_GENERATION`.

### Plain words

1. **The grid can fix the integer powers.** Give the generations a cube-symmetry label and let one field break the symmetry. The power of ε in each generation's mass is then the number of times the field must act before it reaches that generation. For generations labelled by the three axes and one strain field, the powers are 0, 1, 2.
2. **It can fix the alignment.** The breaking field can only sit along a short list of symmetric directions, and one sign in its energy picks which.
3. **It does not fix ε.** Fits want ε ≈ 0.03–0.09, and nothing native supplies that number.
4. **Two findings stop this from explaining the masses.**
   - Particle speeds stay the same in every direction only for a few breakings, those that keep the full cube group or its tetrahedral subgroup. Every such breaking gives at most two mass levels. A third level needs a breaking direction off the symmetric list, and that makes space anisotropic at order ε or ε².
   - If every particle type shares the label, as a lattice-native label would, the best fit is off by ×66. If only left-handed fields carry it, ×3.7. If each particle type may pick its own label, the fit passes at ×2.4. But the same menu fits 48% of random fake spectra, so the pass is not evidence.
5. **Δ(27) and modular symmetry.** The groups are present: A4 and Δ(27) sit inside the lattice symmetries, and the cube group is the modular group Γ4. The parts that make them predictive are missing. Δ(27) needs fermions at momentum 2π/3 or a 2π/3 flux. Modular forms need a modulus field, and the lattice is rigid.

### Route 1: integer charges fixed by representation chains ("Krylov charges")

**Object.** A generation representation V of the proper cube group O (or of Z2³⋊O, which adds lattice translations), and one real symmetry-breaking field σ along a direction n̂. The Yukawa matrix is Y(εn̂) = Σ_k ε^k × (degree-k symmetry-respecting maps evaluated at n̂). When the right-handed partners carry no label, the exponents are the degrees at which F_k, the span of these images up to degree k, gains a dimension.

**Lemma (proved; checked numerically).** Take V = the axis-permutation representation (A1 + E) and σ = an Eg strain at angle θ from a tetragonal line.
- F_0 is the A1 direction, F_1 adds n̂, and F_2 adds (n̂²)_E with weight exactly |sin 3θ| (checked to 1e-4).
- The exponents are therefore (0, 1, 2).
- At θ = 0, the symmetric direction, the lightest generation stays massless to all orders.
- Comparator: this is the lattice version of a modular "near fixed point" hierarchy, with θ playing the role of the deviation.

**Number fixed.** The integer exponents. The checked menu (`native_menu.out`) gives the steps (0,1,2), (0,2,4), (1,2,3), (1,3,4), (1,3,5), (2,3,4) and (3,4,5). They are not supplied: each is the first degree at which a power of σ reaches the target representation along a new direction.

**Still supplied.** ε, the off-symmetric angle θ, and which label each particle type carries.

**Strongest objection: Lorentz violation.** Every case with three levels is a uniform anisotropy of space. It appears at first order for E and T2 fields, and at second order for T1 and the corner star. With ε ≈ 0.05, speed anisotropies are about 1e-3 to 1e-1 times the coupling, against bounds of about 1e-15 or tighter.

**Kill condition.** No native placement fits the 9 masses and 3 CKM elements within ×3 with evidence beyond the random-spectrum control.

**Test (run).** Complex random O(1) coefficients with 3 draws, a free scale per sector, and data recalled rather than fetched.

| Case | Best fit | Random spectra fit as well or better |
|---|---|---|
| Speed-isotropic breakings | ×8.5 | — |
| Label shared by all particle types | ×66 | 0.3% reach ×3 |
| Left-handed fields only | ×3.68 (M_Z), ×3.85 (GUT) | 3.7% |
| Each particle type picks its own label | ×2.44 | 26%; 48% reach ×3 |

The left-handed ×3.68 holds in one of the three coefficient draws; the other two give about ×5.5.

**Reading: KILLED as evidence.** The route fixes the integers. Wherever the native menu passes, either the label choice restores look-elsewhere freedom or the vacuum is Lorentz-violating.

### Route 2: alignment and residual-symmetry accounting (which numbers must be supplied)

**Object.** The residual symmetry group H left by the vacuum.

**Lemma A (proved; checked on all 30 subgroups of O).** A vacuum has no second-rank anisotropy at any order if and only if its long-wavelength point group is T (the tetrahedral group, A4) or O.

**Lemma B (proved; template: Lam's residual-symmetry argument; the C3 case is already on main).** With one shared vacuum, the CKM matrix maps each H-isotypic block of the doublet (Q) generation space into itself. All three CKM angles can be nonzero only if H acts as a multiple of the identity on Q.

**Census (checked: 22 field classes against every native generation representation).** Every single field that keeps speeds isotropic gives at most two finite mass levels. These are the A2 pseudoscalar (breaking O to T), the corner-momentum star along (111), its A2 twist, and the staggered sign field. The abelian part is proved: one character χ with χ² = 1 allows only the levels {0, 1}. Example: the (111) corner star gives levels {0, 3}.

**Alignment.** Native: the symmetric list (100), (110), (111) and tetragonal. Comparator dictionary: O ≅ S4 ≅ Γ4 and T ≅ A4 ≅ Γ3, with residual C4, C3 and C2′ corresponding to the modular fixed points i∞, ω and i.

**Discrete groups.**
- Proved: Δ(3n²), built from the sum-zero translations mod n and C3 about the body diagonal, is a subgroup of the lattice symmetries. Checked for n = 2, 3, 4, giving A4, Δ(27) and Δ(48).
- The A4 triplet is the three hw1 corners. These are genuine nodes and are in the census as S.
- The Δ(27) triplet needs nodes at momentum (2π/3)e_i. The nearest-neighbour Weyl operator Σσ sin k has no nodes there.
- The alternative, a uniform 2π/3 plaquette flux, is forbidden. A C2 rotation reverses the plaquette, so φ = −φ and φ is 0 or π (proved).

**Number fixed.** The alignment, the texture zeros, and a maximum of two levels for isotropy-safe single fields.

**Unavoidable supplied numbers, within this menu.**
1. ε.
2. A second independent amplitude. Isotropy-safe pairs exist: A2 together with the staggered field leaves a residual that acts as a multiple of the identity on character-labelled generations, so CKM is unconstrained. The alternative is an off-symmetric angle with the Lorentz violation tuned away.
3. A label choice for each particle type. This carries the look-elsewhere cost measured in Route 1.

**Strongest objection.** Lemma A assumes the order parameter couples to the speed terms at tree level; GEN-2 c4 says symmetry allows that. If the coupling ran only through Yukawa loops (about y²/16π²), light-fermion anisotropy could be small. The menu also leaves out:
- spinor-valued labels;
- longer-period stars, which I suggest reduce to the same corner costs with ε → ε^{N/2};
- interaction-driven masses.

**Kill condition.** An isotropy-safe single field giving three non-degenerate levels while H acts as a multiple of the identity on Q. None exists in the menu.

**Cheapest next test.** Two isotropy-safe amplitudes (A2 + staggered field, or A2 + the (111) corner star) on a two-dimensional ε grid, with every particle type sharing one label, against the same random control. Suggested outcome: it fails, because the up and down sectors get the same ratios while m_u/m_t and m_d/m_b differ by about ×120.

### Labels and limits

- The Krylov lemma and Lemmas A and B are proved. The ≤ 2-level census and the fits are checked numerically on a finite menu, not proved in general.
- Masses are recalled Xing–Zhang–Zhou-style running values, not fetched. Coefficients are random, not computed from a corner model.
- Free sector scales favour the hypothesis.
- This is same-family work and unrefereed.
- Nothing is left running; peak memory was 208 MB.

### Files

All in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/masswall/R1/`:
- `scripts/native_menu.py` → `native_menu.out` (menu, Lorentz-violation order, residuals, bilinear orders);
- `scripts/native_fit.py` → `native_fit2.out` (free placement plus control);
- `scripts/native_fit_blind.py` → `native_fit_blind.out`;
- `scripts/chiralL_detail.py` → `chiralL_detail.out`;
- `scripts/lemmas_check.py`;
- `scripts/sin3theta_check.py`.

`native_fit.out` is superseded by `native_fit2.out`.