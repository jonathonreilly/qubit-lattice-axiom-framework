---
claim_id: tensor_linear_dispersion_needs_oscillator_slots_both_canonical_variables_must_be_non_compact_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: the landed finite-clock tensor note's slots and integer stencils in doubled coordinates (diagonal slots at vertex sites, face slots at plaquette sites, vector rows (G E)_j on link sites, the scalar-gauge pattern S^T delta_c as the sum of three planar pieces) and its noncompact linear comparator H_N = (J/2) sum [E:E - (tr E)^2/2] + (g/2) sum h:R(h). Finite certificates. (i) On the 4^3 torus G S^T = 0 exactly, ker G has dimension 195 of 384, the scalar-gauge shift s = S^T beta is a null direction of the momentum form (s.M0 s = 0 for every delta_c and for a random beta), and the form changes under E -> E + s by 6e-14 for E in ker G and by 44.864 for a generic E: the momentum term is invariant on the constraint surface only. (ii) The periodic version of the momentum term changes under the continuous scalar-gauge orbit E -> E + theta s for E in ker G (by 694.3, 656.4, 647.8 at theta = 0.7 for three random E), and a nonzero quadratic potential in h changes under h -> h + 2 pi e_slot (by 640.9, -1232.5, -908.9 for three slots); so neither canonical variable can be compact, and no assignment of roles realizes H_N on rotor slots with exactly preserved constraints. (iii) A Hermitian lattice potential X(k) with G(k) X(k) = 0 is fixed uniquely by the landed pieces (486 unknowns, rank 486, residual 1e-13); on the doubly constrained surface (ker G modulo the scalar gauge for E, ker S modulo the vector gauge for h) there are exactly two modes with omega^2 = J g lambda(k), lambda/|k|^2 = 1.000 at small k in every direction, lambda/|k|^2 at least 0.420 over 4000 random k with no negative mode, while off the constraint surface the potential has an eigenvalue of -0.963 |k|^2: linear isotropic dispersion under exact constraints, indefiniteness under penalties. (iv) An oscillator slot truncated to N Fock levels has [x_N, p_N] = i (1 - N |N-1><N-1|) exactly for N = 8, 16, 32, 64, and a unit coherent state has top-level weight e^{-1}/(N-1)! = 7.3e-5, 2.8e-13, 4.5e-35, 1.9e-88 at 3, 4, 5, 6 qubits per slot. No gravitational phase, graviton, finite model, or physical identification is claimed; the oscillator slot type is recorded as a decision point, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/tensor_linear_dispersion_needs_oscillator_slots_in_both_canonical_variables_2026_09_24.py
---

# A linear tensor dispersion needs oscillator slots: both canonical variables must be non-compact

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates under supplied decision points; unaudited.

## Result

The landed
`LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`
proves that compact character dynamics keeping both tensor constraints
exactly has every frequency `O(k³)`, and that its noncompact linear
comparator `H_N` escapes that class with `ω² = J g k²`. Open PR 9095 found
that a one-neighbourhood soft constraint generates the tensor field's moves
with `ω ∝ k²`. This note asks what `H_N` needs from the slots themselves.
- **Both terms of `H_N` are only weakly invariant.** The momentum term
  `E:E − (tr E)²/2` is invariant under the scalar gauge on the constraint
  surface only; the potential `h:R(h)` is a quadratic form. Certified with
  the landed integer stencils on a torus.
- **So neither canonical variable can be compact.** A compact `E` forces a
  periodic momentum term, which moves under the continuous scalar-gauge
  orbit even on the constraint surface. A compact `h` forces a periodic
  potential, and no quadratic form is periodic. A rotor slot has one compact
  variable, so no assignment of roles realizes `H_N` on rotors with exactly
  preserved constraints. The compact alternative is the landed cubic bound.
- **On oscillator slots the lattice symbol is linear and isotropic.** With
  the landed stencils, the doubly constrained surface carries exactly two
  modes with `ω² = J g λ(k)` and `λ/|k|² = 1.000` at small `k` in every
  direction, positive over the whole zone. Off the surface the potential is
  indefinite, so exact constraints, not penalties, are needed.
- **The price of finite emulation.** An oscillator slot truncated to `N`
  Fock levels keeps the polynomial energies and breaks the canonical
  commutator only on its top level; a unit coherent state's weight there is
  `e⁻¹/(N−1)!`, below 1e-12 at four qubits per slot. The constraints of
  oscillator slots have continuous spectra, so they are not stabilizers.

So a linear tensor dispersion costs the slot type, not the neighbourhood
size: oscillator (Fock-type) slots in both canonical variables, with exact
constraints of continuous spectrum, emulable by qubits only up to a
top-level defect. This is recorded as a decision point, `D-osc`, and not
adopted.

## Setting and decision points

- **The landed tensor model.** Slots `E_jj` at vertex sites and `E_ij` at
  plaquette sites; vector rows
  `(G E)_j(x) = E_jj(x + e_j) − E_jj(x) + Σ_{i≠j}[E_ij(x) − E_ij(x − e_i)]` on
  link sites; the scalar-gauge pattern `S^T δ_c`, the sum of three planar
  pieces, in the landed integer form as placed by open PR 9077.
- **The linear comparator (supplied).**
  `H_N = (J/2) Σ [E:E − (tr E)²/2] + (g/2) Σ h:R(h)`, with `E:E` counting each
  face slot twice and the canonical pairing `Σ E_slot dq_slot`,
  `q = (h_xx, h_yy, h_zz, 2h_xy, 2h_yz, 2h_xz)`.
- **Slot types (supplied).** Rotor: one integer-valued and one compact
  variable. Clock: `Z_N` in both. Oscillator (`D-osc`): both variables
  non-compact, or truncated to `N` Fock levels.

None is adopted.

## Theorem 1 — the momentum term is invariant on the constraint surface only

On the `4³` torus with the landed rows, `G S^T = 0` exactly and `ker G` has
dimension 195 of 384.
- The scalar-gauge shift `s = S^T β` is a null direction of the momentum
  form: `s·M₀s = 0` for every `β = δ_c` and for a random `β`.
- Under `E → E + s` the form changes by `2 E·M₀ s`, which is 6e-14 for a
  random `E ∈ ker G` and 44.864 for a generic `E`.

So the momentum term is weakly invariant: exactly invariant as a sum on the
constraint surface, not as a density and not off it. This is the lattice
form of the landed note's statement that `H_N`'s momentum term is
scalar-gauge invariant only on `G = 0`. ∎

## Theorem 2 — neither canonical variable can be compact

- **Compact `E`.** The momentum term must then be periodic in `E`. The
  cosine version with the same quadratic expansion changes under the
  continuous scalar-gauge orbit `E → E + θ s` even for `E ∈ ker G`: by
  694.3, 656.4 and 647.8 at `θ = 0.7` for three random `E`. So it does not
  preserve the constraint subspace.
- **Compact `h`.** The `k²` potential is a nonzero quadratic form, and no
  quadratic form is `2π`-periodic: a gauge-invariant quadratic form in `h`
  changes by 640.9, −1232.5 and −908.9 under `h → h + 2π e_slot` for three
  slots. The landed note shows that a periodic potential keeping the
  constraints has zero zeroth and first moments and so is `O(k⁴)`.

A rotor slot has one compact variable. Whichever role it takes, one term
of `H_N` fails. So `H_N` needs oscillator slots. ∎

## Theorem 3 — the lattice Gaussian symbol on oscillator slots

A Hermitian lattice potential `X(k)` whose diagonal rows are the landed
planar pieces and which satisfies `G(k) X(k) = 0` is unique: 486 unknowns,
rank 486, residual 1e-13. It is the Fierz–Pauli form `h:R(h)` in the slot
variables.
- **Two modes.** On the doubly constrained surface, `E ∈ ker G` modulo the
  scalar gauge and `h ∈ ker S` modulo the vector gauge, with dual bases of
  the two quotients, the reduced problem has exactly two modes with
  `ω² = J g λ(k)`.
- **Linear and isotropic.** `λ/|k|² = 1.000` at `|k| = 0.02` in every
  direction, to 1e-3.
- **Positive over the zone.** Over 4000 random `k`, `λ/|k|² ≥ 0.420` and no
  mode is negative.
- **Indefinite off the surface.** Without the scalar constraint the
  potential restricted to `ker G` has an eigenvalue of `−0.963 |k|²`. This is
  the landed note's indefinite scalar block: penalties leave it, exact
  constraints remove it. ∎

## Theorem 4 — the price of finite emulation

An oscillator slot truncated to `N` Fock levels has
`[x_N, p_N] = i(1 − N |N−1⟩⟨N−1|)` exactly (certified for `N = 8, 16, 32,
64`). Polynomial energies are exact on the truncated space; the canonical
algebra, and with it the gauge algebra, fails only on the top level. A
coherent state of unit amplitude has weight `e⁻¹/(N−1)!` there: 7.3e-5,
2.8e-13, 4.5e-35 and 1.9e-88 at 3, 4, 5 and 6 qubits per slot. ∎

## What this means for the lanes

- **Gravity lane.** The ladder gains a rung that is not about
  neighbourhood size. Compact slots (rotor, clock) with exact constraints:
  `O(k³)` (landed). Compact slots with a soft vector constraint: `ω ∝ k²`
  (open PR 9095). Oscillator slots with exact constraints: `ω ∝ k`, linear
  and isotropic (this note). The framework's qubits can emulate oscillator
  slots only approximately, with a defect exponentially small in the level
  count.
- **The landed escape routes.** Of the landed note's alternatives: exact
  compact constraints keep the cubic bound; the noncompact comparator is
  linear on the lattice too; finite penalties keep the indefinite block;
  truncated oscillators realize the noncompact route up to a top-level
  defect. Finite-N aliases, auxiliary matter, nonlinear gauge actions and
  boundary routes are not addressed here.

## What stays open

- A finite model on truncated-oscillator slots with its constraints handled
  (they have continuous spectra, so no stabilizer projector exists), and its
  low-energy sector. The Gaussian symbol is truncation-blind; the phase is
  not.
- Whether the dynamics clause or the soft-constraint route of open PR 9095
  can generate polynomial rather than periodic energies on such slots.
- Everything the landed note leaves open: sources, a phase, a physical
  identification.

## Prior art

Fierz and Pauli 1939; Gu and Wen 2009 and 2012 (helicity-two modes from
qubit and rotor models, cubic dispersion in the compact class); Xu and
Hořava 2010 (lattice Lifshitz gravity, `z = 2`); Pretko 2017 (higher-rank
U(1) gauge theories). All cited as prior art, not as premises.

## Checks

The runner has 4 checks and all pass in about 4 seconds.

| Check | Result |
|---|---|
| Weak invariance | `G S^T = 0`; `ker G` 195 of 384; `s·M₀s = 0`; change 6e-14 on `ker G`, 44.864 off it. |
| Compactness | Periodic momentum term changes 694.3, 656.4, 647.8 on `ker G`; quadratic potential changes 640.9, −1232.5, −908.9 under `2π` shifts. |
| Lattice symbol | 486 unknowns, rank 486, residual 1e-13; two modes; `λ/|k|²` 1.000 at small `k`; min 0.420 over 4000 `k`, 0 negative; off-surface eigenvalue −0.963. |
| Truncated oscillators | Commutator identity exact for `N = 8..64`; top-level weights 7.3e-5, 2.8e-13, 4.5e-35, 1.9e-88. |

## Independent check

None yet. The runner was rerun from a clean shell; no independent checker has
reviewed this block. One reduction error (a real part taken of a Hermitian
form) was found and fixed by comparing against the continuum comparator's
isotropy before this version.

## What this does not do

- It adopts no slot type, comparator or constraint handling.
- It builds no finite model and claims no gravitational phase, graviton or
  physical identification.
- It does not redo the landed cubic bound; it cites it.
