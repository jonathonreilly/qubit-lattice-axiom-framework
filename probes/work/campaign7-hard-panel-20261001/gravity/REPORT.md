I couldn't save `c7/hard/gravity/REPORT.md`: the harness blocks subagents from writing report files, so the full report is below for you to save at that path. Nothing was run: no code, numerics or symbolic programs. The repo was read at `origin/main` 0485dc0738.

## 10-line summary
1. **Answer to (i):** a nearest-neighbour rule can carry the vector rank-2 Gauss law ∂_iE_ij = 0 as a support check at link sites, given V/L/P roles (so a frame source is still needed). The scalar law, and Pretko's ∂∂E = 0, reach two sites away and are never a single nearest-neighbour check. [EXACT]
2. **Placement lemma (new):** any rotation-covariant placement puts all three diagonal components E_ii on one site class, the vertex or the body centre. One qubit cannot hold three commuting slots, so that site must be a composite of at least three qubits. [EXACT]
3. **Compactness costs one power of k per side (new):** clocks on both sides give k³ (landed); a rotor on one side gives k² (new); Schrödinger variables on both sides give linear (landed). The reason is that relabellings shift h and re-timings shift E, whereas Maxwell's E is gauge-inert. [EXACT within the regular local class]
4. **Finite qubit composites are (ℤ_N, ℤ_N) Weyl pairs.** So the "large-S" escape works only in the strict infinite limit, or through aliased characters whose exponents grow with N. [EXACT, standard]
5. **One term gives both effects:** the same h·R(h) term produces the k² TT stiffness and the inverse-Laplacian (1/r) pull. The compact-allowed |R(h)|² gives only a contact energy. So a linear graviton and a tensor-sector 1/r are one requirement. [EXACT, from the landed source calculation]
6. **The lattice sea breaks relabelling at k = 0.** Its energy is negative definite under uniform traceless strain (landed 09-26), which would make the uniform TT strain tachyonic. Separately, the sea's inertia read isotropically gives the DeWitt kinetic parameter λ = 1/3, not GR's λ = 1. [landed; the λ reading is ARGUED]
7. **Top route for (ii), a sea-induced Einstein–Hilbert term:** the sea's own bilinear ⟨Θ_a^j⟩ = −θ₀δ_a^j is a soldered frame. Treat the frame as a field with zero bare action. If the induced coefficient c_TT > 0, there are two linear TT modes, with a computed speed and a computed G. [frame identity EXACT; route conditional]
8. **Fierz–Pauli uniqueness, derived here:** under rotation symmetry, the only relabelling-invariant k² form is ∝ the landed member's R₂. Cubic-anisotropic admixtures are not excluded. [EXACT]
9. **Decisive computation (not run):** the O(k²) static frame Hessian of the half-filled sea, at staggered mass μ > 0. It is free-fermion Brillouin-zone sums and fits one numeric slot. The two read-outs are the relabelling (Ward) test and the sign of c_TT.
10. **Minimal clause for (iii), Decision V (recorded, NOT adopted):** "The lowest arrangement of the walk's half-filled sea, at whatever uniform frame it sits in, is the zero of every ledger; only departures from it are sources." Companion Decision R (relabelling) is needed only if the Ward test fails.

---

# REPORT: Lane F (gravity): the graviton and the source

**Labels.** EXACT means proved here or in the cited landed note. ARGUED means reasoned but unverified. LANDED means exact within a landed note's own scope, re-read for this report.

**Sources read on main:**
- `MINIMAL_AXIOMS_2026-06-29`
- `LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_…_2026-09-14` ("tensor parent")
- `TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_…_2026-09-24`
- `DYNAMICS_CLAUSE_…TENSOR_CONSTRAINTS_FREEZE…` and `…SOFT_VECTOR_CONSTRAINT…`, both 2026-09-24
- `TENSOR_HELICITY_RATIONAL_CERTIFICATES_…_2026-09-29`
- `FINITE_RANGE_CANONICAL_TENSOR_MIXED_CONSTRAINT_BOUNDARY_…_2026-09-30`
- `COVARIANT_NN_SUPPORT_RULES_GAUSS_LAW_AS_GLUED_SUPPORT_…_2026-09-14`
- `CANDIDATE_ASSEMBLY_…_2026-09-22`
- `ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_…_2026-09-21` (block 62)
- `…EVERY_CLOCK_PROFILE_A_RELABELLING…_2026-09-25`
- claim scopes only: `…WALKER_SEAS_ENERGY_FALLS_UNDER_EVERY_UNIFORM_SHEAR…_2026-09-26`, `…ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE…_2026-09-24`, `…THE_BLIND_WALK…_2026-09-21`, `…NO_MASTER_CLOCK…_2026-09-21`

## (1) The problem in framework terms

Under the four axioms (LATTICE, QUBIT, ADMISSIBILITY, RECORD), find a supplied but local construction with three properties:
- **Modes:** at every small nonzero momentum there are exactly two propagating modes. They are transverse-traceless (TT) with ω = c|k| + O(k²).
- **Redundancies:** two families remove everything else.
  - Relabellings (linearised diffeomorphisms) act on h: h → h + sym∇ξ.
  - Re-timings (lapse) act on E: E → E + (Δ − ∇∇)β.
- **Source:** the half-filled sea's normal-ordered energy density ε_v, with the inverse-Laplacian pull as its static limit.

All of this must come from M₂(ℂ) sites, one nearest-neighbour rule and finite composites. A supplied noncompact comparator alone does not count.

## (2) Obstructions, with exact scope

Items marked *new* are proved below or in §4; the rest are landed.

**O1. Placement (new, EXACT).**
- Setting: a fine lattice with any cell size m. Each component sits on one site class mod m, each divergence row on one class, and ∂_i is a two-point difference.
- **Step 1, centred differences.** A C₂ rotation that fixes row j's class but reverses e_i maps the stencil offsets {a, a−m}e_i to {−a, m−a}e_i. A covariant rule needs these to coincide, so a = m/2.
- **Step 2, one class for the diagonal.**
  - Symmetry E_ij = E_ji then gives r_i − (m/2)e_i ≡ r_j − (m/2)e_j =: σ.
  - So o_ij ≡ σ + (m/2)(e_i + e_j) and o_ii ≡ σ.
  - The C₂ rotations force 2σ ≡ 0.
  - The 3-fold rotation forces σ ∈ {0, (m/2)(1,1,1)}. ∎
- **The two covariant placements:**
  - diagonal at the vertex V, off-diagonal at the face P, rows at the link L (the landed one);
  - diagonal at the body centre C, off-diagonal at L, rows at P.
- **Consequence (EXACT).**
  - M₂(ℂ)'s maximal commutative *-subalgebras are 2-dimensional, so one qubit cannot hold three commuting diagonal slots.
  - Either V (or C) is a composite of at least three qubits.
  - Or E_xx, E_yy, E_zz are the three non-commuting Paulis under soldering. Then rows on two links through one vertex fail to commute and the abelian Gauss structure is lost.
  - Edge and face roles carry only off-diagonal components.

**O2. Range (new, EXACT from the landed stencils).**
- The row ∂_iE_ij at L_j reads exactly its six nearest neighbours: two V and four P. Given roles, it is a nearest-neighbour glued-support check.
- The scalar row S = Δtr h − ∂∂h at V reads sites at doubled-lattice distance 2 and √2. The same holds for Pretko's law, because any mixed ∂_i∂_j needs a diagonal neighbour.
- So the scalar law must be either a two-layer glued support or the clock (lapse) constraint.

**O3. Compactness, per side (landed bound plus new table).** The tensor parent proves O(k³) for lifted regular compact characters. The new result is that each compact side costs one power of k (§4 Step 3). Both canonical sides are gauge-shifted; Maxwell's E is not.

**O4. Finite composites (EXACT, standard).** The irreducible Weyl pairs are (ℝ,ℝ), (ℤ,U(1)), (U(1),ℤ) and (ℤ_N,ℤ_N). Finite-dimensional means ℤ_N. The only loophole at finite N is aliased characters with |r| ≳ N/36.

**O5. Partners (landed 09-29).** For local linear tensor moments, ⟨H1⟩ ≥ ⟨TT⟩/4. So linear TT weight from compact local data comes with helicity-1 partners (Pretko-type). The full vector constraint kills every linear moment, including the TT one.

**O6. Kinetic sign (landed 09-25).**
- Closure of the clock algebra forces β = −α, i.e. DeWitt λ = 1. That line contains no positive-semidefinite form.
- The sea's adiabatic inertia is positive semidefinite, with zero dilation part at μ = 0.
- *Reading (ARGUED):* read isotropically, that gives λ_sea = 1/3 (the Hořava anisotropic-Weyl value), not 1.

**O7. Lattice preferred frame (landed 09-26).**
- The sea's energy under a uniform frame is −⟨(|Es|² + μ²)^{1/2}⟩. At fixed volume it is negative definite in traceless strain, while the member's R₁ and R₂ vanish on uniform strains.
- So relabelling is broken at k = 0 and the uniform TT strain is tachyonic. This is the lattice analogue of "crystal gravity = the Higgs phase of gravity".

**O8. Nonlinear closure (landed 09-30).** Finite-range canonical tensor carriers fail the next mixed constraint equation at degree two.

**Answer to (i).**
- **Can a nearest-neighbour rule carry a rank-2 Gauss law?** Only the vector law. Given V/L/P roles, ∂_iE_ij = 0 is a nearest-neighbour check, with composite vertex sites (O1, O2). The scalar law and Pretko's ∂∂E = 0 are not.
- **Does compactness doom the linear graviton?** Compactness does not by itself gap the mode in 3+1D. Precedents:
  - the compact U(1) nonconfining phase in 4D (PRD 21, 2291);
  - Xu's compact rank-2 phase, gapless with ω ∝ k² (cond-mat/0602443, cond-mat/0609595);
  - Rasmussen–You–Xu (arXiv:1601.08235).
- **What compactness does do:** with exact constraints and regular local terms, it fixes the power at k³ (or k² with a rotor side).
- **Composite-site escape:** a composite / large-S limit escapes only when the composite is infinite (O4), or through aliases.

## (3) Escape routes, ranked

**R1 (top): composite solder, i.e. a sea-induced Einstein–Hilbert term.**
- **Supplies:**
  - block 62's frame E_a^j(x) as an independent real field with zero bare action, coupled through the landed ⟨H⟩ = ΣE·Θ;
  - Decision V.
- **Would show:** the h·R(h) term and the TT inertia both come from the infinite sea, with no compact slot involved, so O3 and O4 do not apply. That gives two linear TT modes with a computed speed and a computed G.
- **Test:** §5.

**R2: explicit Schrödinger slots.**
- **Supplies:** the landed noncompact comparator, with composite V/C sites (O1) and the scalar law as a two-layer glued support (O2).
- **Shows:** linear dispersion exactly, but it adds a new primitive: an unbounded real local variable, which no finite qubit composite gives (O4).
- **Test:** none needed; this is an owner decision.

**R3: large-N composite clocks via aliases.**
- **Supplies:** blocks of log₂N qubits per slot, the exact landed ℤ_N code, and Villain-periodised DeWitt and Einstein–Hilbert densities projected onto the stabiliser sector.
- **Would show:** linear dispersion on scales up to ℓ*(N), with a k³ tail beyond, if aliases carry the zeroth moment.
- **Test:** the exact character expansion of one projected DeWitt density for N = 3…9. Measure the zeroth-moment weight on characters with S r ≡ 0 mod N but S r ≠ 0.

**R4: compact Pretko-type law.**
- **Shows:** five linear modes, consistent with O5, but no tensor-sector 1/r (Step 5). It is a stable compact gapless phase that contains spin-2, not GR.
- **Test:** the helicity content of the linear branch on the doubled lattice.

## (4) Deepest derivation: R1

**Step 1. The sea's composite frame is the solder (EXACT).**
- Take the walk H = Σ_a σ_a S_a (block 54, soldered).
- In the lower band ⟨σ⟩ = −s/|s| with s_j = sin k_j, so Θ_a^j = −s_a s_j/|s| per state (block 62, T2).
- k_a → −k_a kills the off-diagonal averages, and axis permutation equalises the diagonal ones. So ⟨Θ_a^j⟩ = −θ₀δ_a^j with θ₀ = ⟨sin²k₁/|s|⟩ > 0.
- Check: Σ_a⟨Θ_a^a⟩ = −⟨|s|⟩, which is the sea energy.
- This is the lattice form of spinor gravity's composite tetrad (Hebecker–Wetterich; Diakonov arXiv:1109.0091), used as context only.

**Step 2. Counting (EXACT, given the redundancies).**
- The frame has 9 canonical pairs.
- Removed: local coin rotations (3), relabellings (3) and re-timing (1). That leaves 2.
- Local rotation is landed at first order (the blind walk). Re-timing closes with walker content through O(q²) (landed 09-25, T5). Relabelling is the open item, tested in §5.

**Step 3. The per-side table (EXACT within the regular local class, H = H_E(E) + V(h)).**

*(a) E side.*
- The landed identities M s_r = G_rᵀK and G_r s_r = 0 give T(E + sβ) = T(E) + Re(β̄ KᵀGE), where T is the DeWitt form, for every β.
- So on ker G, T is invariant under every finite shift, integer ones included.
- For a rotor slot (E ∈ ℤ, h ∈ U(1)), the stabiliser U_x = exp(i(Sq)(x)) shifts E by an integer row and preserves ker G (since GSᵀ = 0). So H_E = J·T preserves the joint sector exactly.
- The obstruction was E's compactness, not its integrality.

*(b) h side.*
- With integer E, the vector gauge parameter α is continuous. Fourier uniqueness then makes every mode of a periodic V(h) strongly invariant (Gm = 0).
- The landed moment bound gives m = O(k²), so H_hh = O(k⁴). With an O(1) E-term this means ω ∝ k².
- Swapping roles (integer h with V = h·R(h); compact E with Sr = 0) gives O(k) E-symbols, so again ω ∝ k².

*(c) Table.*

| E side | h side | TT dispersion | Status |
|---|---|---|---|
| clock | clock | O(k³) | landed |
| rotor | compact | k² | new |
| compact | integer | k² | new |
| ℝ | ℝ | linear | landed |

**Step 4. Why R1 escapes the table (ARGUED).** The frame is not a slot. It enters linearly, and its effective action is the response of the infinite Fock sea, which is a functional of a real, unbounded field.

**Step 5. One term, two effects (EXACT, using the parent's source calculation).**
- h·R(h) gives the k²|h_TT|² stiffness. With S h = ρ it also gives the static energy −g|ρ|²/(4k²), i.e. the inverse-Laplacian pull.
- |R(h)|² gives a contact energy only.
- The lane's existing inverse-Laplacian results come from the clock sector (log rates), which are already real, law-level fields.

**Step 6. Removing the k = 0 term (EXACT as a definition; ARGUED as a limit).**
- Decision V subtracts the local term Σ_x e₀(g(x)), so χ̃(0) = 0.
- For μ > 0 the sea is gapped, so the response is analytic and its static k → 0 limit equals the uniform Hessian. At μ = 0 the two limits may not commute.

**Step 7. Fierz–Pauli uniqueness (EXACT, derived here).**
- Take F = a k²tr h² + b|hk|² + c(kᵀhk)tr h + d k²(tr h)².
- Impose invariance under δh = k⊗ξ + ξ⊗k. This gives:
  - 4a + 2b = 0;
  - 2b + 2c = 0;
  - 2c + 4d = 0.
- So F ∝ k²tr h² − 2|hk|² + 2(kᵀhk)tr h − k²(tr h)², which is −4 × block 62's R₂.
- F is positive on TT and negative on the transverse trace.
- Cubic-anisotropic admixtures are not excluded.

**Step 8. Conditional graviton and G (EXACT, conditional).**
- If χ̃ = c·F + O(k⁴) with c > 0, and the TT inertia m_TT > 0 (landed 09-25, T4(b)), then ω² = c k²/m_TT: two linear TT modes.
- With the lapse-coupled ε_v source, G ∝ 1/c in lattice units. This bears on the open gate "natural unit = Planck length".
- **Residual (ARGUED):** λ_sea = 1/3 means the induced trace/clock sector is not GR's. The clock sector stays with the lane's own rate field, which matches the lane's existing split.

## (5) Decisive computation (spec; not run)

**Name:** static frame Hessian of the half-filled walk sea at O(k²). One numeric worker, BLAS = 1.

**Inputs:**
- block 62's framed walk ½Σ{E^j·σ, S_j} with E = (1+h)^{−1/2} to second order, including the seagull (second-order) term;
- block 139's staggered mass μ ∈ {0.25, 0.5, 1};
- h_jj on sites, h_ij on faces, endpoint-averaged to bonds;
- filled lower band, L ∈ {32, 48, 64, 96};
- k = 2πn/L along (100), (110), (111), for n = 1…4.

**Compute:**
- the 6×6 matrix χ(k) = ⟨seagull⟩ + Σ_{p,h} |⟨p|V(k)|h⟩|²/(E_h − E_p);
- positive control: χ(0) must equal the landed 09-26 T2 Hessian;
- subtract χ(0) and fit χ̃ = k²C(k̂), Richardson-extrapolated in L and |k|.

**Read-outs:**
- (a) χ̃ applied to sym(k̂⊗ξ): the Ward test;
- (b) the sign and isotropy of c_TT(k̂);
- (c) the sign of the transverse-trace coefficient;
- (d) the cubic residual away from the F form.

**Outcomes:**

| Result | Meaning |
|---|---|
| Ward holds, c_TT > 0, F form | R1 survives. Predicted speed √(c/m_TT) and G. Next, rerun with the two-step-current placement (the examined placement that keeps the divergence condition), then dynamics. |
| Longitudinal part ≠ 0 | The lattice breaks relabelling at O(k²), giving extra vector modes. Rerun with the two-step current, or record Decision R. |
| c_TT < 0 | The free sea gives the wrong-sign Einstein–Hilbert term. Fall back to R2 or R3. |
| Singular as μ → 0 | The Dirac points contribute nonlocally. Report the μ > 0 values only. |

## (iii) The minimal clause (recorded owner decision, NOT adopted)

**Decision V (a vacuum weightless at every frame):** "The lowest arrangement of the walk's half-filled sea, at whatever uniform frame it sits in, is the zero of every ledger; only departures from it are sources."
- It extends the vacuum ruling's normal ordering of T₀₀ to the stress at every frame. It is the lattice counterpart of setting both the cosmological constant and the vacuum's lattice shear modulus to zero.
- It is a named fine-tuning and a source/action identification (outside the axioms), not a statement about records.
- Without it, O7 makes the uniform TT strain tachyonic.

**Companion Decision R (only if the Ward test fails):** "Frame readings that differ by a discrete relabelling gradient are the same state."

**If neither decision is taken:** within the axioms and finite composites, the result is a k³ TT mode (k² with rotor composites) and no tensor-sector 1/r. The pull comes from the clock/rate sector only.

Sources used for planning only, not as premises:
- [Rasmussen–You–Xu, arXiv:1601.08235](https://arxiv.org/pdf/1601.08235)
- [Xu, cond-mat/0602443](https://arxiv.org/pdf/cond-mat/0602443)
- [Xu, cond-mat/0609595](https://arxiv.org/html/cond-mat/0609595)
- [Pretko, arXiv:1604.05329](https://arxiv.org/pdf/1604.05329)
- [Existence of a nonconfining phase in 4D U(1), PRD 21, 2291](https://doi.org/10.1103/PhysRevD.21.2291)
- [Massless phases and symmetry restoration (CMP)](https://link.springer.com/article/10.1007/BF01213610)
- [Phases of Z_N lattice gauge theory](https://link.springer.com/article/10.1007/BF02899851)
- [Zaanen–Balm–Beekman, Crystal gravity, arXiv:2109.11325](https://scipost.org/submissions/2109.11325v2/)
- [Beekman et al., quantum liquid crystals in 3D, arXiv:1703.03157](https://arxiv.org/pdf/1703.03157)
- [Diakonov, arXiv:1109.0091](https://arxiv.org/abs/1109.0091)
- [Wetterich, Lattice spinor gravity, arXiv:1108.1313](https://arxiv.org/pdf/1108.1313)
- [Spinor gravity (OSTI)](https://www.osti.gov/etdeweb/biblio/20387913)
- [Volovik, arXiv:2111.07817](https://arxiv.org/abs/2111.07817)
- Gu–Wen arXiv:0907.1203 is cited through the tensor parent and was not fetched.