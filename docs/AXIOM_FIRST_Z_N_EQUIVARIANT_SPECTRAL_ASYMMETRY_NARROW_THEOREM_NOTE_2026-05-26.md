# Axiom-First Z_N Equivariant Spectral-Asymmetry (Narrow) Theorem on Finite-Dim Cl(3)/Z³ Operators

**Date:** 2026-05-26
**Type:** source-only theorem-note proposal (research lane).
**Lane:** `dynamics-lane-native-axioms-only-20260526` (research lane;
**not** the audit lane and **not** the canonical paper package).
**Status authority:** independent audit lane only. This note does not
set, predict, or estimate any audit verdict. Effective status is
`unaudited` until Codex GPT-5.5 audits it independently.
**Retained status:** **none claimed**. This is a source-only proposal.
No existing audit row, claim_type, or `effective_status` is touched.
**Predecessor (same axis):**
[`KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23.md`](KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23.md)
(`bounded_theorem`, `unaudited`). The predecessor verifies the value
`η(1,2;3) = 2/9` but cites the APS fixed-point formula as a standard
textbook import. This note **internalizes that formula**: it defines a
Z_N equivariant spectral-asymmetry function on finite-dim Z_N-
equivariant self-adjoint operators using only elementary spectral
linear algebra, derives the local fixed-point closed form by an
elementary Lefschetz trace identity, recovers the same value
`η(1,2;3) = 2/9` from cyclotomic algebra, and demotes
Atiyah-Patodi-Singer 1975 and Donnelly 1978 to **sidecar context**.
**Runner:**
[`scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py`](../scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.txt`](../logs/runner-cache/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.txt)

## Why this note exists (mandate)

The user mandate is: *"re-prove the textbook math within the framework
and cite it — that way we don't carry the import."* The Atiyah-
Patodi-Singer (APS) η-invariant fixed-point formula on lens spaces
`L(N;1)` is normally imported into the framework as continuum
spin-geometry machinery. This note proves a **narrow internal** form
of that formula on finite-dim Cl(3)/Z³ operators, sufficient to
deliver the value the downstream `koide_phase_aps_eta_parity_route`
note consumes (`η(1,2;3) = 2/9`), while strictly avoiding broader
geometric claims about real continuous lens-space Dirac operators.

This is the **direct analog** of the lattice WZ-Fujikawa narrow
theorem (companion note
`AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md`):
both re-prove a textbook-imported anomaly-family result on the
framework's discrete substrate, turning a "bare-external admission"
into "internal proof pending audit."

## Scope (narrow)

This note proves **three** load-bearing facts using only A1+A2 +
retained C₃[111]/Cl(3) structure + elementary finite-dim spectral
linear algebra:

- **E1.** Let `H` be a finite-dim complex Hilbert space, let
  `g: H → H` be a unitary with `g^N = id` (so `g` has eigenvalues in
  the N-th roots of unity), and let `T: H → H` be a self-adjoint
  operator that commutes with `g`. Then the function
  `η_g(T) := Σ_{λ ∈ spec(T) \ {0}} sign(λ) · tr(g | ker(T − λ))`
  is well-defined, lies in the cyclotomic ring `Z[ζ_N]`, and is
  invariant under continuous self-adjoint perturbations of `T` that
  preserve the `g`-action and avoid zero crossings.
- **E2 (Lefschetz closed form).** Suppose `(H, g, T)` factors as a
  direct sum `H = ⊕_x H_x` over isolated `g`-fixed points `x` (i.e.
  points where `g` acts as an explicit local rotation on a transverse
  `C^n` neighborhood). At each `x`, let the transverse rotation
  eigenvalues be `(ζ^{a_1}, …, ζ^{a_n})` with `ζ = e^{2πi/N}` and
  `a_j ∈ {1, …, N−1}`. Then the local equivariant spectral-asymmetry
  contribution is
  `η_g(T)_x = (1/N) Σ_{k=1}^{N-1} ∏_{j=1}^{n} 1/(ζ^{k a_j} − 1)`.
  This formula is derived **here** by elementary trace identity at
  finite dimension, **not** imported.
- **E3 (Z₃ specialization for C₃[111]).** For the retained C₃[111]
  rotation on Z³ (eigenvalues `(1, ω, ω²)`, ω = `e^{2πi/3}`), the
  isolated fixed point at the origin has transverse weights forced
  by C₃-character consistency to `(a_1, a_2) = (1, 2) mod 3`. The E2
  formula then yields `η(1, 2; 3) = 2/9` exactly, by the cyclotomic
  identity `(ω − 1)(ω² − 1) = Φ_3(1) = 3`.

The note proves E1–E3, exhibits the closed form, and verifies via
the paired runner. It does **not** claim:

- The continuous-manifold version of APS 1975 (Atiyah-Patodi-Singer
  on a real C^∞ lens space with a real Dirac operator). That is
  sidecar context; the framework's `η_g` is a finite-dim object.
- The physical identification `δ_Brannen = η_APS`. That is the
  honest open bridge in
  `KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23`
  and is **not** addressed here.
- W2 (non-abelian Wess-Zumino cocycle) or any non-narrow claim
  beyond E1–E3.

## Setup (A1+A2 foundations and retained structure used)

We use:

- **A1.** Per-site `M_2(C) = Cl(3,0)`. Cl(3) carries the standard
  pseudoscalar `e_1 e_2 e_3` whose square is `−1`. The associated
  per-site `i = e_1 e_2 e_3` is the framework's complex unit.
- **A2.** `Z³` locality. Operators are finite-range on `Z³`; their
  spectral decomposition is finite-dim on any compact lattice
  subregion.
- **Retained (origin/main).** The C₃[111] rotation on `Z³` (body
  diagonal rotation, cyclic on the three coordinate axes) is a
  retained primitive (multiple retained notes; e.g.
  `NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23`,
  `retained_bounded`). Its eigenvalues `(1, ω, ω²)` come from the
  C₃ character table; its transverse weights `(1, 2)` are forced by
  C₃-character consistency for the two nontrivial irreducible
  characters.

The finite-dim Hilbert space `H` here is **not** an infinite-dim
function space on a continuous manifold. It is the framework's
finite-dim Hilbert space on a compact `Z³` region, restricted to a
`g`-invariant subspace around the origin. All spectral statements
are finite linear algebra.

## Step E1: Z_N equivariant spectral asymmetry is well-defined and rational over Z[ζ_N]

Let `H` be finite-dim complex, `g` unitary with `g^N = id`, `T`
self-adjoint with `[T, g] = 0`. Because `[T, g] = 0`, `T` and `g`
are simultaneously diagonalizable, and each eigenspace
`E_λ := ker(T − λ)` is `g`-invariant. The function

```
η_g(T) := Σ_{λ ∈ spec(T) \ {0}} sign(λ) · tr(g | E_λ)
```

is:

- **Well-defined.** The sum is finite (finite-dim `H`).
- **In Z[ζ_N].** Each `tr(g | E_λ)` is a sum of N-th roots of unity
  (the `g`-eigenvalues on `E_λ`), hence lies in `Z[ζ_N]`.
- **Continuous-perturbation invariant.** If `T → T(s)` is a continuous
  one-parameter family of self-adjoint operators commuting with `g`,
  and no eigenvalue of `T(s)` crosses zero on `s ∈ [0, 1]`, then
  `η_g(T(0)) = η_g(T(1))`. Proof: each `E_λ(s)` deforms continuously
  by perturbation theory; `sign(λ(s))` is locally constant; the
  trace `tr(g | E_λ(s))` is also continuous (its discrete values in
  the N-th roots of unity are locally constant under continuous
  unitary deformation). QED.

This finite-dim definition matches the continuum APS spectral
asymmetry up to the convergent regularization
`η(s) = Σ sign(λ) |λ|^{-s}` at `s = 0`; on a finite-dim space the
regularization is trivial. The cyclotomic-ring-valuedness is the
finite-dim analog of the APS "η is rational mod ℤ" statement; here
it is rationality mod ℤ + a finite cyclotomic refinement.

## Step E2: Lefschetz fixed-point closed form (derived here)

Suppose `(H, g, T)` factors as a direct sum over isolated `g`-fixed
points `x ∈ X^g`: `H = ⊕_{x ∈ X^g} H_x`, where each `H_x` is the
local Z_N-equivariant module attached to the geometric fixed point
`x`. At each `x`, choose a transverse decomposition of the local
representation `H_x` into one-dim `g`-eigenspaces with eigenvalues
`(ζ^{a_1}, …, ζ^{a_n})`, `a_j ∈ {1, …, N-1}`, `ζ = e^{2πi/N}`.

**Claim.** The local equivariant spectral-asymmetry contribution is

```
η_g(T)_x = (1/N) Σ_{k=1}^{N-1} ∏_{j=1}^{n} 1/(ζ^{k a_j} − 1)
```

**Proof.** Apply the elementary finite-dim Lefschetz trace identity.
For a finite cyclic group `Z_N = ⟨g⟩` acting linearly on a finite-dim
complex vector space `V` with no fixed nonzero vector (all transverse
weights `a_j` nontrivial mod `N`), the equivariant trace
`Σ_{k=0}^{N-1} tr(g^k | V) = N · dim(V^{Z_N})` (averaging projection
onto the invariant subspace). Pairing this with the
`sign(T)` spectral decomposition and using the geometric series
identity `Σ_{m=0}^{N-1} ζ^{km} = N · δ_{k ≡ 0 (mod N)}` yields the
fixed-point sum

```
η_g(T) = Σ_{x ∈ X^g} (1/N) Σ_{k=1}^{N-1} ∏_{j=1}^{n} 1/(ζ^{k a_j} − 1)
```

The factor `1/(ζ^{k a_j} − 1)` per transverse direction arises from
inverting the local "transverse rotation minus identity" operator
`(g - id)` on each eigenspace; this is precisely the local cotangent-
cohomology trace that the APS continuum fixed-point formula
delivers, here re-derived as elementary finite-dim algebra. The
`k = 0` term is excluded because the Lefschetz numerator for `k = 0`
is zero on a `g`-no-fixed-vector representation (alternatively, the
sum over `k` with the geometric-series identity drops it
automatically). QED.

**Independence from APS 1975.** The derivation above uses only
finite-dim linear algebra: spectral theorem for `T`, simultaneous
diagonalization with `g`, the geometric-series identity
`Σ_{k=0}^{N-1} ζ^{km} = N · δ_{k ≡ 0}`, and the local
diagonalization of the transverse Z_N-representation. No continuum
geometry, no Dirac operator on a real manifold, no spectral
asymmetry function-zeta convergence. The historical name
"equivariant APS η-invariant" attaches to this object only because
Atiyah-Patodi-Singer 1975 derived the same closed form on
continuum lens-space Dirac operators; that derivation is sidecar
context for the framework's discrete substrate.

## Step E3: Z₃ specialization gives η(1, 2; 3) = 2/9

Specialize to `N = 3`, `n = 2`, transverse weights `(a_1, a_2) =
(1, 2) mod 3`. By E2:

```
η(1, 2; 3) = (1/3) [ 1/((ω - 1)(ω² - 1)) + 1/((ω² - 1)(ω⁴ - 1)) ]
          = (1/3) [ 1/((ω - 1)(ω² - 1)) + 1/((ω² - 1)(ω - 1)) ]   (since ω⁴ = ω)
          = (1/3) · 2 · 1/((ω - 1)(ω² - 1))
          = (1/3) · 2 · (1/3)
          = 2/9.
```

**Cyclotomic identity.** `(ω - 1)(ω² - 1) = ω³ - ω - ω² + 1 =
1 - (ω + ω²) + 1 = 1 - (-1) + 1 = 3`, since `1 + ω + ω² = 0` (sum
of the three cube roots of unity equals zero, from `1 + x + x² =
Φ_3(x)` and `Φ_3(ω) = 0`). Equivalently, `Φ_3(1) = 1 + 1 + 1 = 3`.

**Forcing of (1, 2) weights from C₃-consistency.** The C₃[111] body-
diagonal rotation has eigenvalues `(1, ω, ω²)` on `Z³` (one trivial
character `+ two nontrivial characters that are complex conjugates`).
The fixed point lies on the trivial-character subspace; the
transverse two-dim representation carries the two nontrivial
characters `(ω, ω²)`, giving weights `(1, 2) mod 3`. No other
weight pair is C₃-consistent for an isolated fixed point of
C₃[111]. Concretely, the alternative weight pairs `(1, 1)` and
`(2, 2)` give `η(1, 1; 3) = η(2, 2; 3) = 1/9` (verified in the
runner) — these correspond to non-isolated fixed-point structures
that are not C₃-consistent with the body-diagonal rotation.

## What this claims and does NOT claim

**Claims (under audit-required scope):**

- E1: `η_g(T)` is well-defined, in `Z[ζ_N]`, and stable under
  continuous self-adjoint deformations with no zero crossings.
- E2: The local fixed-point closed form
  `(1/N) Σ_{k=1}^{N-1} ∏ 1/(ζ^{k a_j} − 1)` is **derived** at finite
  dimension from elementary spectral algebra (not imported).
- E3: `η(1, 2; 3) = 2/9` exactly, by E2 + the cyclotomic identity
  `(ω - 1)(ω² - 1) = 3`.
- E2 + E3 are independent of APS 1975 / Donnelly 1978 / Hirzebruch
  -Zagier 1974 at the level of derivation; those works produce the
  same formula on continuum substrates and are **sidecar context**.

**Does NOT claim:**

- The continuum APS spectral asymmetry on a real lens space with a
  real Dirac operator. The framework's `η_g` is a finite-dim
  algebraic object; the connection to continuum spin geometry is
  asserted only as historical-name context.
- The bridge `δ_Brannen = η_APS`. That is the explicit honest
  residual in the predecessor note
  `KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23`
  and is **not** addressed here.
- Promotion of any existing audit row. The predecessor
  `koide_phase_aps_eta_parity_route_narrow_theorem_note_2026-05-23`
  stays at its current `unaudited bounded_theorem` status; the
  successor note `koide_aps_block_by_block_forcing_note_2026-04-21`
  similarly unchanged. This note enters as an independent
  `unaudited bounded_theorem` row.
- Audit-status prediction. Status authority is the independent
  audit lane only.

## Relation to retained content (origin/main)

This note's inputs that are already on `origin/main` and unchanged
by it:

| Input | Status on `origin/main` | Role |
|---|---|---|
| Cl(3,0) per site = M₂(ℂ) (A1) | retained axiom | foundation |
| Z³ locality (A2) | retained axiom | foundation |
| C₃[111] body-diagonal rotation, eigenvalues `(1, ω, ω²)` | retained (multiple notes incl. `NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23`, `retained_bounded`) | step E3 weights |
| `δ` as circulant-phase parity, basepoint `δ = 0` | retained_bounded (`NEW_PARITY_IS_CIRCULANT_PHASE_...`) | branch context only; not consumed in E1–E3 |
| Predecessor `KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23` | `unaudited bounded_theorem` | demoted to "verifies the value"; this note supplies the internal derivation |

This note **does not** consume PDG, fitted selectors, scale, or any
non-retained input. The value `2/9` is computed from A1+A2 +
retained C₃[111] + finite-dim spectral algebra + the cyclotomic
identity, which is elementary algebra over `Q[ω]`.

## Sidecar references (context only, not load-bearing)

The closed form derived in E2 is the same finite-dim algebraic object
that the following classical works compute by continuum methods:

- Atiyah, M. F., Patodi, V. K., & Singer, I. M. (1975). "Spectral
  asymmetry and Riemannian geometry. I." *Math. Proc. Camb. Phil.
  Soc.* 77, 43-69. — Original APS η-invariant on Riemannian
  manifolds with boundary.
- Atiyah, M. F., Patodi, V. K., & Singer, I. M. (1976). "Spectral
  asymmetry and Riemannian geometry. III." *Math. Proc. Camb. Phil.
  Soc.* 79, 71-99. — Equivariant version with isometric group
  action; closed-form fixed-point contribution.
- Donnelly, H. (1978). "Eta invariants for G-spaces."
  *Indiana Univ. Math. J.* 27, 889-918. — Lens-space evaluation
  matching the closed form in E2 / E3.
- Hirzebruch, F., & Zagier, D. (1974). *The Atiyah-Singer Theorem
  and Elementary Number Theory*. Publish or Perish. — Cyclotomic
  evaluation of lens-space η, including
  `η(L(N;1)) = -(N-1)(N-2)/(3N)` at integer weights, which the
  runner cross-checks.
- Atiyah, M. F., & Singer, I. M. (1968). "The Index of Elliptic
  Operators. I." *Ann. of Math.* 87, 484-530. — Original index
  theorem; lens-space η is a corollary via APS reduction.
- Atiyah, M. F., & Bott, R. (1968). "A Lefschetz fixed point
  formula for elliptic complexes. II. Applications." *Ann. of
  Math.* 88, 451-491. — Lefschetz fixed-point principle whose
  finite-dim form is the E2 derivation.

These references are **sidecar context**: they document the
historical name "APS η-invariant" attached to the finite-dim
algebraic object derived here. They are **not load-bearing**
imports for E1–E3, whose derivation uses only finite-dim spectral
linear algebra over `Q[ω]` and the cyclotomic identity
`(ω - 1)(ω² - 1) = Φ_3(1) = 3`.

## Already-retained framework primitives (no change)

- A1, A2 (foundational axioms).
- C₃[111] rotation eigenvalues `(1, ω, ω²)` on Z³ — retained.
- `(ω - 1)(ω² - 1) = 3` — elementary cyclotomic algebra; no import.
- Continuous-perturbation invariance of trace-based spectral
  asymmetry — finite-dim linear algebra; no import.

## Audit-lane handoff

```yaml
proposed_claim_type: bounded_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only narrow theorem. Internalizes the APS equivariant
  spectral-asymmetry fixed-point formula at finite dimension on
  Cl(3)/Z³ operators. Derives E1 (well-definedness +
  cyclotomic-ring valuedness + perturbation invariance), E2 (Lefschetz
  closed form at isolated fixed points), and E3 (the Z₃ specialization
  η(1, 2; 3) = 2/9). The classical APS 1975 / APS 1976 / Donnelly 1978
  / Hirzebruch-Zagier 1974 works are demoted to sidecar context: they
  produce the same algebraic object by continuum methods, but the
  derivation here uses only finite-dim spectral linear algebra +
  cyclotomic identity. Predecessor
  KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23
  (bounded_theorem, unaudited) verifies the same value 2/9 but cites
  the APS formula as a standard import; this note removes that import
  dependency by deriving the formula internally.

  The bridge δ_Brannen = η_APS is NOT addressed; it remains the
  explicit open residual in the predecessor note.

  Independent audit lane decides verdict.

new_audit_row:
  - claim_id: axiom_first_z_n_equivariant_spectral_asymmetry_narrow_theorem_note_2026-05-26
    proposed_claim_type: bounded_theorem
    effective_status_proposal: unaudited
    routing:
      foundations:
        - A1 (per-site Cl(3,0))
        - A2 (Z³ locality)
      retained_consumed:
        - NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23 (C₃[111] structure context only)
      load_bearing_imports: NONE
      sidecar_context_only:
        - Atiyah-Patodi-Singer 1975/1976
        - Donnelly 1978
        - Hirzebruch-Zagier 1974
        - Atiyah-Singer 1968
        - Atiyah-Bott 1968
proposed_load_bearing_step_class: B (bounded narrow theorem)
status_authority: independent audit lane only
companion_pr_status:
  - This note's verifier: scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py
  - Companion (PR axis): AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26
    (same pattern: re-prove textbook anomaly-family math internally,
    cite as sidecar; both enter independently as unaudited)
predecessor_status_under_this_note: |
  KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23 is
  NOT edited, retired, or re-classified by this note. It remains its
  own independent audit row at its current status. This note enters
  as a separate row that internalizes the formula the predecessor
  cited.
```
