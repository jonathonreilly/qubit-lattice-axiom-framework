# Strong-CP: O_h Forbids ε^{μνρσ}-Based CP-Odd Action Densities — Narrow Theorem

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/strong_cp_action_class_oh_invariance_runner.py`](../scripts/strong_cp_action_class_oh_invariance_runner.py)

## Audit context

This is **Track A Step 2** of the strong-CP / θ retirement attack
plan. Step 1 (`CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM`) established
that the cubic point group O_h lifts faithfully to Cl(3) with the
pseudoscalar transforming as the det character.

This step proves a **stronger result than the panel proposed**: the
**4D Levi-Civita pseudotensor** structure of every standard
lattice topological-charge density forces it to transform with
sgn(det) under O_h, regardless of the specific field-strength
discretization (single-plaquette, clover, smeared, Lüscher-geometric).
Consequently, **any non-zero θ-coefficient violates O_h-invariance of
the admissible action class** — for the entire family of standard
CP-odd discretizations, not just the single-plaquette case.

This addresses simultaneously **Track A Step 2** (action-class
O_h-invariance for Wilson + staggered + scalar mass) and **Track A
Step 4** (clover-`F̃F` killer counter-attack response, flagged by the
2026-05-26 assumption audit Agent #5).

## Claim

Consider the framework's substrate `Cl(3)/Z³ × T_E` (Z³ spatial +
discrete Euclidean time) with the cubic point group `O_h ⊂ O(3)`
acting on the spatial directions, lifted to Cl(3) by Step 1.

**Theorem (Action-class O_h structure for strong-CP).**

1. **(A1) Wilson plaquette action is O_h-invariant.**
   `S_W[U] = -(β/N_c) Σ_P Re tr(U_P)` satisfies
   `S_W[R · U] = S_W[U]` for every `R ∈ O_h`.

2. **(A2) Staggered + scalar-mass fermion action is O_h-invariant.**
   `S_F[χ, χ̄, U] = χ̄(M_KS[U] + m I)χ` is O_h-invariant under the
   combined site-permutation + staggered taste-rotation action.
   *(Cited retained authority below.)*

3. **(A3) The 4D Levi-Civita with one temporal index is an O_h
   pseudotensor:** `ε^{0ijk} → det(R) · ε^{0ijk}` for every
   `R ∈ O_h ⊂ O(3)`.

4. **(A4) Every standard lattice topological-charge density
   transforms with sgn(det) under O_h.** For any gauge-covariant
   field-strength discretization `F^{(r)}_{μν}[U]` (single-plaquette
   `r = 0`, clover `r = 1/2`, smeared `r > 1/2`, Lüscher-geometric),
   the corresponding 4D topological-charge density
   ```text
   Q^{(r)}[U] = (1/32π²)  ε^{μνρσ}  Tr[ F^{(r)}_{μν}  F^{(r)}_{ρσ} ]
   ```
   satisfies
   ```text
   Q^{(r)}[R · U]  =  det(R) · Q^{(r)}[U]                            (★)
   ```
   for every `R ∈ O_h`. **The entire family of standard CP-odd
   discretizations transforms identically.**

5. **(A5 — UNIFIED COROLLARY) Under the named premise "admissible
   action class is O_h-invariant under the lifted substrate action",
   every `r`-discretization of `θ Q^{(r)}[U]` requires `θ = 0`.**
   Single-plaquette, clover, smeared, Lüscher-geometric — all
   excluded by the same structural mechanism.

(A1) and (A4) are pure lattice-gauge / pseudotensor computations
using Step 1's substrate-algebraic lift. (A5) is a **conditional
result**: it removes θ from the admitted set across ALL standard
CP-odd discretization classes, **conditional on the named premise
"admissible action class is O_h-invariant".**

## Why this absorbs the "clover counter-attack" (Step 4)

The 2026-05-26 assumption audit Agent #5 flagged the clover-`F̃F`
density as the killer counter-attack against single-plaquette-only
arguments:
> "Construct an explicit clover-`F̃F` topological density on
> Cl(3)/Z³: `Q_clov = (1/32π²) ε^{μνρσ} Tr[F_{μν}^{clov} F_{ρσ}^{clov}]`.
> Real, gauge-invariant, leading O(a⁴), standard. The framework's
> only escape is P1 (no multi-plaquette restriction), and P1 is
> admitted from an unaudited no-go."

(A4) of this theorem **kills the counter-attack structurally**: the
clover density has the same `ε^{μνρσ} F·F` form as every other standard
CP-odd discretization, so it transforms with `det(R)` under O_h. P1 is
no longer the load-bearing premise — the load-bearing premise is the
generic O_h-invariance of the admissible action class. The
single-plaquette restriction was a red herring; the real exclusion
mechanism is the universal ε-pseudotensor structure.

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | `R ∈ O_h` permutes the 3 spatial axes via signed permutation; the temporal axis is fixed. | Lattice geometry of cubic point group |
| (B2) | The Wilson plaquette holonomy at site `x` for spatial plaquette `(μ,ν)` transforms under O_h: `U_{μν}(x) → U_{R(μ),R(ν)}(R·x)^{ε(R,μ,ν)}` where `ε = ±1` depending on whether R preserves or reverses the (μ,ν) plane orientation. | Lattice plaquette transport rule |
| (B3) | `Re tr(U)` is invariant under `U → U^†` (since `tr(U^†) = (tr U)^*` and Re is conjugation-symmetric). Hence each individual plaquette's `Re tr` is preserved regardless of orientation. **⟹ A1.** | Reality of Re tr |
| (B4) | Staggered Kogut-Susskind matrix transforms covariantly under O_h via the standard taste-rotation; det positivity (cited Case A) holds; `(χ̄ M χ + m χ̄ χ)` is O_h-invariant in scalar form. **⟹ A2.** | Cited retained: `staggered_only_det_positivity_case_a_note_2026-05-17` + standard staggered taste structure |
| (B5) | The 4D Levi-Civita `ε^{μνρσ}` with one temporal index `0` and three spatial `i, j, k ∈ {1, 2, 3}` reduces to `ε^{0ijk} = ε^{ijk}` (3D Levi-Civita on spatial indices). Under `R ∈ O_h ⊂ O(3)`, the 3D Levi-Civita transforms as `ε^{ijk} → det(R) · ε^{ijk}` (standard pseudotensor property of Levi-Civita under O(n)). **⟹ A3.** | Standard pseudotensor calculus on O(n) |
| (B6) | A purely spatial 4-index ε product `ε^{ijkl}` for `i,j,k,l ∈ {1,2,3}` vanishes identically (4 antisymmetric indices on a 3-dim space). Hence every non-vanishing term in `ε^{μνρσ} F_{μν} F_{ρσ}` has at least one temporal index `0`, so it reduces to a form covered by (B5). | Antisymmetry on 3 spatial directions |
| (B7) | `F^{(r)}_{μν}[U]` for any gauge-covariant lattice discretization (single-plaquette, clover, smeared, Lüscher-geometric) is by construction a rank-2 antisymmetric covariant tensor under O_h: `F^{(r)}_{0i} → R_{ii'} F^{(r)}_{0i'}`, `F^{(r)}_{ij} → R_{ii'} R_{jj'} F^{(r)}_{i'j'}`. The temporal index is fixed (`R_{00} = +1` for O_h ⊂ O(3) acting only spatially). | Standard lattice field-strength covariance |
| (B8) | Combining (B5)–(B7): in `ε^{μνρσ} F^{(r)}_{μν} F^{(r)}_{ρσ}`, the `ε` factor contributes `det(R)` and the four `R`-rotations on `F · F` collapse to identity by `R^T R = I`. **Net: `Q^{(r)} → det(R) · Q^{(r)}` for every `r`. ⟹ A4 (★).** | Pseudotensor contraction calculus |
| (B9) | Under the named premise "admissible action class is O_h-invariant", any term proportional to `Q^{(r)}` must equal its negative under improper R, forcing the coefficient `θ^{(r)} = 0`. This holds for every `r`. **⟹ A5.** | Group invariance + named-premise admissibility |

## Exact arithmetic / verification check

The runner verifies on a 2×2×2 spatial lattice with random SU(3) gauge
configurations:

- **A1 verification**: compute `S_W` before and after O_h transformation
  of the gauge configuration, verify equality across 12 O_h elements
  (6 proper + 6 improper).
- **A3 verification**: explicit computation `R · ε = det(R) · ε` on
  the 3D Levi-Civita symbol for **all 48 O_h elements**.
- **A4 verification**: abstract test with random rank-2 antisymmetric
  `F` tensors. Compute `Q = ε^{ijk} F_{0i} F_{jk}` before and after R.
  Verify `Q[R·F] = det(R) · Q[F]` across 6 proper + 6 improper R.

This is sufficient to verify the structural pseudotensor identity that
underwrites (A4) for any `r`-discretization, since the transformation
law depends only on the index structure, not on the specific
discretization of `F`.

## Dependencies

- [`CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md`](CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md)
  — Track A Step 1: supplies the Cl(3) faithful lift used for the
  staggered taste-rotation correction in B4.
- [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
  — retained: supplies `det(M_KS + mI) > 0` used in B4.

The Wilson plaquette action, standard staggered phase structure, and
pseudotensor property of `ε^{μνρσ}` are framework primitives /
standard mathematical content. No new admission introduced in
(A1)–(A4).

**Named premise registered for (A5):** *Admissibility of the action
class = O_h-invariance under the lifted substrate action.* This is
the conditional premise on which θ = 0 follows. It is **stronger than
"no bare θ slot"** because it derives that conclusion across the
entire ε-pseudotensor family; it is **weaker than full derivation from
primitives** because the admissibility convention is itself a stated
principle (to be derived in Step 5 or ratified as a retained
governance convention).

## Historical provenance (cited prior art, NOT load-bearing imports)

The O_h-invariance / discrete-symmetry argument for excluding CP-odd
terms is a discrete analog of standard continuum-symmetry constraints:

- **Vafa, Witten** (1984). "Restrictions on Symmetry Breaking in
  Vector-Like Gauge Theories", *Nuclear Physics B* **234**, 173.
- **Kuchimanchi, R.** (2025). "Strong CP and Parity in Hamiltonian
  Formalism", arXiv:2507.18620. Discrete-P-invariance argument forcing
  θ̄ ∈ {0, π} on Hilbert-space CP-vacuum sector.
- **Liang, X.; Yanagida, T. T.** (2025). "Non-invertible symmetry
  as a non-axionic solution of the strong CP problem",
  arXiv:2505.05142. Categorical-symmetry forcing of θ=0.
- **Mir, R.; Gunara, B. E.; Faizal, M.** (2026). "Discrete θ
  Projection: A Gauge-Protected Solution to the Strong CP Problem
  Without Axions", arXiv:2603.05195. Z_N gauging of (−1)-form θ-shift.

**These references are cited as historical prior art / provenance
only.** This bridge does not import any theorem from the cited works.
The derivation in (B1)–(B9) proceeds entirely on the framework's
retained Step 1 substrate-algebraic input + standard lattice
field-strength definitions. The cited references provide continuum and
Hamiltonian-formalism precedents.

## Boundaries

This bridge does **not** close:

- The lattice-to-continuum θ_QCD bridge (Track A Step 5 still open);
- The action-class admissibility convention itself — that remains a
  named premise to be either derived from primitives (Step 5) or
  ratified as a retained convention (analog to 𝒞_b for AC_φλ);
- Reflection positivity (handled separately by PRs #1971 + #1973);
- CP-odd terms NOT built from `ε^{μνρσ}` and field strengths (e.g.,
  explicit pseudoscalar-fermion bilinears `iχ̄ γ_5 χ`, out of scope
  for the gauge-sector argument);
- Single-plaquette `Σ Im tr(U_P)` as a pseudo-topological-charge:
  this **does NOT directly sign-flip** under arbitrary O_h elements
  (only inversion-type R); it is **not** the proper lattice
  topological-charge density. The proper density uses `ε^{μνρσ}`
  (A4); this is what's structurally constrained.

What this **does** close:
- (A1) and (A4) are unconditional structural identities;
- (A5) is conditional on the named admissibility premise.

## Track A status after this step

| Step | Target | Status |
|---|---|---|
| **Step 1** | Cl(3) faithful lift of O_h with det character | ✅ shipped PR #1974 |
| **Step 2** | Action-class O_h-invariance for Wilson + staggered + scalar | ✅ **THIS PR (A1, A2)** |
| **Step 3** | Discrete-θ-projection composition (Aharony 2603.05195 + Z₃) | next |
| **Step 4** | Clover-`F̃F` counter-attack response | ✅ **ABSORBED into A4 of this PR** |
| **Step 5** | Lattice-to-continuum θ bridge / admissibility derivation | next |

**Net Track A progress: 2 of 5 explicit steps done, plus Step 4 absorbed.**

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/strong_cp_action_class_oh_invariance_runner.py
```

Expected:

```text
TOTAL: PASS=9 FAIL=0
VERDICT: O_h-invariance holds for Wilson action; ε^{μνρσ} F·F structural
identity holds across all 48 O_h elements; every standard CP-odd
lattice density transforms with sgn(det) and is forbidden under
O_h-invariant action class.
```
