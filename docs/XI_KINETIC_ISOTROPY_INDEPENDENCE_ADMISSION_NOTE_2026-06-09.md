# The Matter Kinetic Isotropy `c_t = c_s` (ξ = 1) Is Independent of `{Lattice, Quantum, Record}` + Emergent-Time + Reflection Positivity — a Two-Model Witness That It Is an Irreducible Euclidean-Kinetic-Normalization (OS0) Admission — Independence Note

**Date:** 2026-06-09
**Claim type:** no_go / independence (a positive theorem that a sentence is independent of the axiom theory; it names — does not derive — the missing premise)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/frontier_xi_kinetic_isotropy_independence_2026_06_09.py`](../scripts/frontier_xi_kinetic_isotropy_independence_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_xi_kinetic_isotropy_independence_2026_06_09.txt`](../logs/runner-cache/frontier_xi_kinetic_isotropy_independence_2026_06_09.txt)

---

## What this settles

Emergent Lorentz invariance on the marginal sector requires the time-vs-space kinetic coefficients
of the matter action to be equal, `c_t = c_s` (equivalently `ξ := c_t/c_s = 1`, equivalently the
4D-hypercubic B₄ symmetry of the kinetic measure, equivalently `a_τ = a_s` with `c = 1`). The
retained
[`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
**names** this as the missing premise ("an explicit Euclidean kinetic-normalization / 4D-hypercubic
premise") but leaves open whether it is derivable. **This note proves it is not:** `ξ = 1` is
**independent** of the axiom theory plus emergent time plus reflection positivity — neither derivable
nor refutable from them — so it is an **irreducible admission**, an OS0-type Euclidean kinetic
normalization parallel to but not a consequence of OS1 (reflection positivity).

This sharpens the anisotropy-gate from *"names the premise"* to *"the premise is axiom-independent."*

## The witness (exact scope of the runner, 17/17)

Let `Σ = {Lattice (Z³, 6-NN, no diagonals), Quantum (M₂(ℂ) per site), Record (durable timeless
scalar)}` + emergent time via a positive self-adjoint transfer `T` (Stone). The free Euclidean
lattice scalar is the minimal carrier (the marginal anisotropy lives at quadratic order; the
staggered fermion is identical there): `S = Σ_n [K_t(∂_τφ)² + K_s|∂_xφ|² + m²φ²]`, with
`ξ = c_t/c_s = K_t/K_s` (at `a_τ = a_s`).

- **(A) RP does not force `ξ = 1`.** The transfer single-mode energy `cosh E(p) = 1 + ω²(p)/(2K_t)`
  is real and positive, with `e^{−E} ∈ (0,1)` and `H = E/a_τ ≥ 0`, for **every** `c_t/c_s ∈
  {½, 1, 2, 5}`. OS1 (reflection positivity) and the spectrum condition pin the **form** (positive
  self-adjoint transfer, bounded-below `H`), not the dimensionless ratio. `c_t = c_s` is OS0 (full
  Euclidean SO(4)/B₄ invariance) = the Lorentz output being sought, so invoking it is circular.
- **(B) `ξ` is a different object from the clock-rate `a_τ`.** A clock rescale `a_τ → 2a_τ` gives a
  **constant** `E(p)`-ratio across all modes (spread `0`, a pure conformal factor), whereas a
  `c_t → 2c_t` change gives a **p-dependent** reshape (spread `0.04`). So the single-clock no-go
  (`single_clock_uniqueness_scope_boundary`: only the product `a_τ·H` is fixed) is structurally blind
  to `ξ` — it removes a constant scale, while `ξ` is a p-dependent shape.
- **(C) The causal order fixes the cone shape, not the aperture.** The 6-NN no-diagonal reachability
  order is the L1 **taxicab** order; its front speed differs by direction (axis `1.0`, face-diagonal
  `0.707`, body-diagonal `0.577`), so **no round L2 cone matches it** — a round cone through the
  diamond-boundary points would need `c_t = 1.0, 1.414, 1.732` at once. The combinatorial
  1-tick-1-edge tie fixes the reachability-cone shape but admits a 1-parameter `ξ` embedding family;
  this is why
  [`MIN_TIME_STEP…`](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md)
  is `audited_renaming` (it fixes the combinatorial ratio, not the dynamical aperture).
- **(D) The independence witness.** Two realizations — `M1 (c_t = c_s, ξ = 1)` and `M2 (c_t = 2.5c_s,
  ξ ≠ 1)` — both satisfy every shared retained structure (positive transfer/RP, spectrum `H ≥ 0`,
  the single-clock product `a_τ·H`, the 1-tick-1-edge reachability cone) and differ **only** on the
  sentence `ξ = 1`, which `M2` violates **only** in the matter-Lorentz *output* (cone speed² `= 0.4 ≠
  1`), not in any axiom. Robinson/Vaught: neither `Σ ⊢ ξ=1` nor `Σ ⊢ ¬(ξ=1)`. The only premise that
  excludes `M2` is `c_t = c_s` itself — circular. Hence `ξ = 1` is independent of `Σ`.

## Why no axiom supplies it

- **Lattice** (`Z³`, 6-NN) supplies no metric scale, lattice spacing, causal cone, unit conversion,
  or temporal axis at all — let alone its kinetic weight relative to space.
- **Quantum** (`M₂(ℂ)` per site) and **Record** (durable timeless scalar) supply no dynamics and no
  time metric/normalization/weighting.
- The `scale_reference_primitive` (`a⁻¹ = M_Pl`) carries **zero dimensionless content**, so it cannot
  supply the dimensionless `ξ = c_t/c_s`.
- **RP/OS1** is invariant under `ξ` (Part A); `c_t = c_s` is the separate OS0 Euclidean-invariance
  premise of constructive QFT, not a consequence of OS1.
- **Single-clock / Stone / modular** fix only the product `a_τ·H` (a constant rescale), provably a
  different object from the p-dependent `ξ` (Part B).
- The discrete causal order fixes only the conformal class up to the L1 diamond (Part C).

The missing primitive, named precisely: **an explicit Euclidean kinetic-normalization (OS0)** — the
temporal kinetic coefficient on the same footing as the three spatial ones — equivalently a retained
bridge that derives the record/update tick as the physical time coordinate (a finite temporal lattice
with a temporal Brillouin zone), not merely a continuous Stone parameter sampled by `Tⁿ`. The
independence witness shows this primitive is not a consequence of the current axioms.

## Ground-up sharpening: spatial isotropy is *also* an admission, but ξ=1 is strictly stronger (the Cl(3) root)

A natural objection is that the matter spatial isotropy `z_x = z_y = z_z` is "axiom-derived for
free," making `c_t = c_s` look like the same kind of structural fact extended to a 4th axis. A
ground-up re-examination (runner Parts E–F) shows the picture is subtler, and the difference is
load-bearing:

- **(E) Spatial isotropy is *also* an admission at the bare-axiom level.** The witness **M3** — a
  spatially anisotropic action (`K_x ≠ K_y`) on the *same* `Z³` / Quantum / Record — is axiom-faithful
  (positive transfer, spectrum, RP all hold) and breaks O_h. So "the matter action respects O_h" is
  *not* a theorem of the three bare axioms either; it is a covariance premise, exactly parallel to the
  ξ=1 admission.
- **(F) But the two premises differ in *kind*, not just degree.** O_h is the *genuine* automorphism
  group of the `Z³` 6-NN edge set (all 48 signed permutations preserve `{±e_i}`; a shear does not) — a
  symmetry the Lattice axiom *asserts* by fixing a **cubic** (not rectangular) lattice. So spatial
  isotropy follows from "respect the symmetry you already asserted." The ξ=1 generator (the space↔time
  swap, the B₄ leg beyond O_h) is **not** an automorphism of any axiom object: under axiom-resident
  O_h × time-parity the four axes split into **two** orbits `{t}` and `{x,y,z}`, and only B₄ merges
  them — which *is* the ξ=1 premise.
- **The root (decisive test).** No 4th anticommuting time-like Clifford generator exists in
  `M₂(ℂ) = Cl(3,0)`: solving `{T, σ_i} = 0` for all three Paulis gives only `T = 0` (the coefficient
  system is full rank), and the pseudoscalar `σ_x σ_y σ_z = i·I` is **central**, not a generator. The
  **"3" of Cl(3)** — three anticommuting Paulis = three commensurable spatial axes, one O_h orbit — is
  exactly why time is structurally the odd-one-out. **ξ=1 is rooted in the same place as the framework's
  d = 3.**

So `ξ = 1` is **strictly stronger** than spatial isotropy: spatial isotropy *respects* a generator the
axioms assert (O_h ⊂ Aut(Z³)); ξ=1 *adds* a generator the axioms disclaim (the temporal B₄ leg, absent
because Cl(3) has no 4th anticommuting generator). Cubic→hypercubic is therefore **not a relabel** — it
posits a metrically-commensurable temporal axis the substrate does not host. Dimension count: the
bare-Σ kinetic form has 3 dimensionless ratios; granting axiom-resident O_h covariance removes 2
(leaving ξ); the temporal B₄ generator removes the last (→ full SO(4)). The lone residual after
axiom-resident covariance is **exactly one number, ξ**, needing the one generator the axioms lack.

## Honest scope

- This is a **positive independence theorem** (`ξ = 1` is not derivable), not a closure and not a
  framework inconsistency. The framework is self-consistent; the axioms simply do not fix the matter
  action's temporal-vs-spatial kinetic ratio.
- It **does not demote** any row. It sharpens the retained anisotropy-gate, which already names the
  premise; it adds the independence atom.
- The realistic landing for emergent Lorentz is therefore **positive·retained CONDITIONAL** on this
  named OS0 admission — **not** unbounded derivation. On the canonical symmetric `Z⁴` (`η₀ = 1`)
  surface where the premise holds, the precomputed `|δv| < 6×10⁻¹⁸` is rep-blind and all-orders (the
  B₄ boundary note), so the conditional positive result is strong; only this one units-bridge
  admission remains, and it is provably irreducible to the current axioms.
- The continuous-time horn is separately closed by `γ < γ_crit` (the AF-trap,
  [`GAMMA_FULL_VS_GAMMA_CRIT`](GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md)); no
  internal/taste/CPT/O_h/Ward symmetry repairs `δv` there (the obstruction is the loop-measure
  asymmetry, common to `c_t` and `c_s`).

## Reprove-and-cite ledger

- **Reproven here** (runner, from primitives; every check an independent numeric/symbolic test): the
  positive transfer / spectrum condition for the whole `ξ`-family; the constant-vs-p-dependent
  E-ratio distinguishing the clock-rate from `ξ`; the L1-taxicab no-round-cone-match; the two-model
  independence witness.
- **Cited** (comparator / scope only, never a derivation input): the field-wide Lorentz-naturalness
  / fine-tuning literature (Collins-Perez-Sudarsky-Urrutia-Vučetič gr-qc/0403053; Iengo-Russo-Serone
  0906.3477) as the external confirmation that marginal `c_t ≠ c_s` is a fine-tuning, not a theorem;
  Groot Nibbelink-Pospelov hep-ph/0404271 (SUSY+CPT custodial cure, which the framework lacks) as the
  scope marker; Robinson/Vaught as the independence-method reference.

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. The cited ledger
statuses are recorded verbatim as of 2026-06-09 (authorities below are on main).

- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md) (`retained_no_go`; the row that names the missing `c_t = c_s` premise — this note proves that premise axiom-independent)
- [SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md) (`retained_no_go`; only `a_τ·H` fixed — shown blind to `ξ`)
- [MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md) (`audited_renaming`; combinatorial ratio, not the aperture)
- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md) (`retained`; reachability-only, retired as physical cone)
- [GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md](GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md) (the continuous-horn flow no-go)
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md) · [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + scale primitive; (2) emergent time via a positive
self-adjoint transfer (Stone); (3) reflection positivity / the spectrum condition; (4) the free
scalar as the minimal marginal carrier. The result is a model-theoretic independence: two realizations
faithful to all of (1)–(3) differ only on `ξ = 1`, so `ξ = 1` is not derivable from them.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag; the
fine-tuning / SUSY-cure literature and Robinson/Vaught are comparators / method references only,
never derivation inputs; the transfer, dispersion, and independence witness are reproven from
primitives in the runner.

**No-promotion statement:** this note does **not** promote, demote, or set the audit status of the
anisotropy-gate, the single-clock no-go, the `MIN_TIME_STEP` renaming, the B₄ boundary note, or any
other row. It adds an independence atom: `ξ = 1` is an irreducible Euclidean-kinetic-normalization
(OS0) admission. The independent audit lane is the only status authority.
