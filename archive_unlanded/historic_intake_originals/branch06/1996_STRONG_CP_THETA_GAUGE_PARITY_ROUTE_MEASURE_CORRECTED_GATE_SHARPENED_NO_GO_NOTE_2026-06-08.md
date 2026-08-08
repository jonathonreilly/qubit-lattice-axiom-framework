# Strong-CP θ_gauge: the O_h/Parity Route — Measure-Cancellation Corrected, Gate Sharpened to the Color↔Orientation-Z₂ Coupling (No-Go) Note

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** named-obstruction no-go (with a verified correction + reframing rider)
**Claim type:** no_go
**Status:** no-go proposal. Reframes the strong-CP `θ_gauge = 0` residual from the
diffuse "minimality" admission to a sharp **parity (O_h)** question, **corrects** a
measure-cancellation error, places the framework in the **parity-solution class**,
and pins the precise gate: `θ_gauge = 0 ⟺` the color action couples zero to the
lattice-orientation `Z₂` — an EFT-naturalness assumption, not derived. Adds no
axiom, no fitted value. Audit verdict set by the independent audit lane.
**Authority role:** no-go source proposal (the `θ_gauge` residual, parity-framed).
**Primary runner:**
[`scripts/strong_cp_theta_gauge_parity_route_2026_06_08.py`](../scripts/strong_cp_theta_gauge_parity_route_2026_06_08.py)
(exact numpy, PASS=7).

## The route

`θ̄ = θ_gauge + arg det(M_quark)`. `θ_gauge` is the coefficient of the topological
`F̃F = ε_{μνρσ}F^{μν}F^{ρσ}` slot. This note attacks `θ_gauge = 0` via parity
(O_h-invariance of the color action), the most framework-native template
(Nelson-Barr / parity-Hermiticity), since the substrate is the cubic `Z³` lattice
whose point group `O_h` includes reflections.

## A correction (verified)

The recent exercise claimed O_h-invariance does **not** forbid `F̃F` because "the
`det(R)` in the ε-pseudotensor and the `det(R)` in the measure cancel." **That is
wrong.** The global `θ`-term `S_θ = Σ_x Q[F_x]` (lattice topological charge,
`Q[F] = ε^{ijk}F_{0i}F_{jk}`) is **P-odd** (`Q[R·F] = det(R) Q[F]`, verified on all
48 O_h signed permutations), while the lattice sum `Σ_x` is a **relabeling** of a
fixed discrete set (no Jacobian) and the continuum volume measure is **det-even**
(`|det R| = +1`). So there is **no measure `det(R)`** to cancel the `F̃F` sign:
`S_θ → det(R) S_θ`, and an **O_h/parity-invariant action forbids `F̃F`** (the
P-even `Σ Tr F²` survives). The landed `STRONG_CP_EPSILON_PSEUDOTENSOR_OH_SIGN_BRIDGE`
(B6) is right; the exercise's cancellation claim is refuted.

## The framework is in the parity-solution class

- **Color is vectorlike / P-even:** the color `su(3)` commutes with the chirality
  grading (`[Γ5, color] = 0`); only the weak `su(2)_L` is chiral
  (`[Γ5, T^a P_L] ≠ 0`). The Wilson color action `Re Tr U_P` is parity/orientation
  invariant (`Re Tr U = Re Tr U†`).
- **The matter determinant is K-real:** the Hermitian C₃ mass circulant has a real
  determinant, so `arg det(M_quark) ∈ {0, π}` (orientable to 0) — no continuous CP
  from the matter side.

So both halves of `θ̄` are parity/reality-controlled — the framework sits squarely
in the parity-solution class, with the K-real determinant as its specific strength
(the usual regeneration of `θ̄` through a continuous `arg det M_q` is absent).

## The gate (no-go): `θ_gauge = 0` is not forced

`θ_gauge = 0` requires **parity**-invariance of the color action — proper rotations
(det = +1, 24 of O_h) leave `Q[F]` invariant; only the **improper/reflection**
(parity) elements forbid it. A 6-lens forcing red-team (vectorlike/Vafa-Witten,
no-P-source, orientation-coupling, regeneration, the lattice-QCD objection,
emergent-Lorentz-forces-parity) **unanimously failed to force `θ_gauge = 0`**, for
one recurring reason:

> **The lattice orientation is a framework-native P-source for `F̃F`.** The Cl(3)
> volume element `ω = σ₁σ₂σ₃ = i·I` (the i-identity gate's native pseudoscalar =
> `sign(Vandermonde)` orientation `Z₂`) transforms by `det(R)` under all 48 O_h
> actions — the **same** det-odd character as `F̃F`. So `F̃F` is **sourced** by the
> native lattice orientation, not "unsourced."

Therefore "color has no P-source, so its action is P-even" is the EFT-naturalness
assumption *"respect substrate symmetry absent a source"* — **not derived** from
`{Lattice, Quantum, Record}`. `θ_gauge` is exactly the **un-derived color coupling
to the lattice-orientation `Z₂`** — the same un-derived-couplings wall as `β = 6`,
now parity-framed and tied to the i-gate's orientation `Z₂` (the same `Z₂` that
sets the `δ`-sign and the `arg det` sign). Emergent Lorentz forces only the proper
rotation group; the regeneration-block (`d arg det M/dt = 0`) is an ordinary SM
fact, not framework-native.

## Verdict

`θ_gauge = 0` is **not forced**. It reduces — cleanly and for the first time in
**parity** terms — to: the color gauge action couples zero to the framework-native
lattice-orientation `Z₂`. That coupling is an un-derived action coefficient (the
`β = 6`-class wall); requiring it to vanish is the EFT assumption "the color action
respects substrate parity absent a source," which the lattice orientation (a
genuine native P-source) blocks from being a derivation. The durable gains are the
**correction** (O_h-invariance genuinely forbids `F̃F`), the **reframing**
(minimality → parity), the **parity-solution-class placement** (vectorlike color +
K-real determinant), and the **sharpened gate** (the color↔orientation-`Z₂`
coupling, unifying `θ_gauge` with the i-gate orientation structure).

## What is and is not claimed

- **Is:** O_h/parity-invariant action forbids `F̃F` (no measure cancellation —
  exercise corrected); color is vectorlike/P-even and the matter determinant is
  K-real (parity-solution class); `θ_gauge = 0 ⟺` zero color coupling to the native
  orientation `Z₂`; that coupling is un-derived and "color parity" is an EFT
  assumption (the orientation sources `F̃F`); so `θ_gauge = 0` is **not** forced.
- **Is not:** does **not** derive `θ_gauge = 0` or solve strong-CP; does **not**
  claim `θ_gauge ≠ 0`; does **not** prove no future gauge-action derivation can
  force color parity (a derived O_h-invariant minimal action would retire it); adds
  no axiom, no fitted value. The `θ = 0` empirical target is not consumed.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the cubic `Z³`
  lattice (O_h point group), the qubit `Cl(3,0)` (the volume element `ω = i·I`), and
  the Record K-reality of the C₃ mass circulant; the `F̃F` P-oddness, the lattice-sum
  invariance / det-even measure, the Wilson P-evenness, `[Γ5, color] = 0`, the real
  determinant, and `ω → det(R) ω` are all reproven in the runner.

Companion + context (plain references, not load-bearing deps):
`STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07`,
`STRONG_CP_EPSILON_PSEUDOTENSOR_OH_SIGN_BRIDGE_BOUNDED_NOTE_2026-05-26`,
`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07`,
`I_IDENTITY_AUTOMORPHISM_GATE_SCALAR_I_ONE_OBJECT_REAL_STRUCTURE_INDEPENDENT_NARROW_THEOREM_NOTE_2026-06-08`,
`NO_AXIOM_NATIVE_CP_SOURCE_RDELTA_THETA_UNFORCED_COEFFICIENTS_OF_RECORD_FORCED_ACTION_NO_GO_NOTE_2026-06-08`,
`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23`.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The `F̃F` P-oddness, the lattice-sum
det-invariance and det-even volume measure, the Wilson parity-evenness, the
color/chirality commutator, the K-real circulant determinant, and the `ω → det(R) ω`
pseudoscalar law are reproven in the runner from the cubic `Z³` lattice and the
qubit primitives. Nelson-Barr/parity and Vafa-Witten are named as comparators only.
