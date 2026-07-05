# The Curved 3+1 Prism Regge Second Variation: Tick-Momentum Channel Dispersion on the Round ∂Δ⁴ × Z_τ — and Why the Symmetric-Representative Route Does Not Supply the Distinguished Connection

**Date:** 2026-06-17
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Actual current-surface status:** bounded-support construction plus a
tested route-insufficiency boundary for the Reynolds-symmetrization
criterion.

**Claim scope:** The cubic-Coxeter Regge **second variation `δ²S_R` on the curved 3+1 prism**
(round `∂Δ⁴` spatial slice × periodic tick `Z_τ`, right-prism product metric) is **built and
independently verified** as a genuine 4D-Regge operator: the global-order Freudenthal–Kuhn staircase
tiles it into a closed 4-manifold (closed-manifold tiling gate G1), the assembled Hessian is
Hermitian (Hermiticity gate G3), satisfies the curved-background Schläfli identity (Schläfli gate G4),
and **matches a finite difference of the actual 4D Regge action
`S_R = Σ_h A_h δ_h − 2Λ Σ V₄` to rel `4e-8` (action finite-difference gate G6, validated against a from-scratch
coordinate-geometry action — not self-referential)**; its `k_τ=0` spatial block **reduces to the
retained round-S³ structure** (deficit `2π−3·arccos(1/3) ≈ 2.5903`, the S₅ channels `1⊕4⊕5`;
round-S³ reduction gate G5).
**The substantive new result (tick-dispersion gate DISP):** the S₅-isotypic channel weights **disperse in tick momentum**
`k_τ` (e.g. `h₁` varies materially across the sweep) — genuine 3+1 structure the static 3D round-S³
slice cannot produce. **The honest negative result:** the canonical / frame-covariant channel
structure on this prism is carried **only by the Reynolds-symmetric representative `H_sym`** (the
S₅-group-average over the 120 triangulation orderings), and that canonicity is **automatic, not
discovered** — a *random* Hermitian matrix group-averaged by the same S₅ passes the same
commutation/Schur/frame-invariance tests (tautology gate TAUT). Therefore these tested
Reynolds-symmetry tests do not by themselves supply the distinguished connection the
polarization-frame-bundle blocker names; **the capstone is not achieved**, and the remaining open
problem is now more sharply localized. This is not a no-go for every possible covariant-transport or
connection-building route.

**Status authority:** independent audit lane only. This note writes no audit verdict and retags no row.
**Loop:** gravity-capstone campaign 2026-06-17 (3+1 curved-prism build).
**Runner:** [`scripts/regge_curved_prism_tick_dispersion_2026_06_17.py`](../scripts/regge_curved_prism_tick_dispersion_2026_06_17.py)
(`TOTAL: PASS=11 FAIL=0`, deterministic; numpy+sympy only; ~18 s).
**Authority role:** source-note proposal. If retained, supplies the verified curved 3+1 prism Regge
second variation plus the tick-momentum channel dispersion, and records the tested route boundary:
the Reynolds-symmetric representative's commutation/Schur/frame-invariance tests are automatic and
therefore do not by themselves discharge the frame-bundle blocker.

## 1. What is built and verified (the genuine achievement)

The single genuinely-unbuilt piece of the gravity-capstone — the **4D-Regge second variation on a
curved 3+1 prism** — is now constructed and machine-verified end-to-end. Reusing the verified
4-simplex dihedral kernel (`THETA`/`AREA`, from the flat tick-extension machinery) and the
Cayley-Menger 4-volume, on the round `∂Δ⁴ × Z_τ` right-prism:

- **Closed-manifold tiling gate (G1):** the global-order staircase tiles `(tet × tick) → 4` four-simplices, giving a **closed
  4-manifold** (every tetrahedron shared by exactly two four-simplices; `20·L_τ` four-simplices).
- **Hermiticity and Schläfli gates (G3/G4):** `H(k_τ)` Hermitian (`4e-16`); curved-background Schläfli `Σ_h A_h dθ_h = 0`
  (`9e-16`); **action finite-difference gate (G6):** the Bloch `H(k_τ)` matches a central finite difference of the **actual** action
  `S_R` (rel `4e-8`) — independently re-validated against a from-scratch coordinate-geometry Regge
  action (no kernel reuse), so the operator is correct, not self-consistent-only.
- **Round-S³ reduction gate (G5):** the `k_τ=0`, tick-decoupled **spatial block reduces to the retained round-S³** structure
  (deficit `2.5903` exact; the S₅ multiplicity-free channels `1⊕4⊕5`).

## 2. The new result: tick-momentum channel dispersion (DISP)

On the S₅-symmetric representative the three spatial channel weights `h_λ(k_τ)` are **well-defined
functions of the tick momentum** and **disperse** across `k_τ` (the nearest-neighbour tick coupling
block is nonzero, norm `~1.07`; `h₁` sweeps materially over `k_τ ∈ [0,π]`). This is real 3+1 content
**absent from the static 3D round-S³ slice** (a single rigid finite complex with no tick momentum) —
it is exactly what the curved 3+1 prism build adds beyond the retained spatial result. No GR/PDG
input; the dispersion is fixed by the prism geometry.

## 3. Route boundary: the tested symmetric-representative criterion is automatic

The capstone hoped the prism would supply the blocker's **distinguished connection** (a canonical,
frame-covariant channel split across the family). The tested Reynolds-symmetrization criterion does
not do that by itself, and the runner makes the reason exact:

- **The staircase breaks S₅.** Any single global-order triangulation of the prism has a simplex set
  fixed by **only the identity** (raw spatial-block S₅ deviation `~4.3`). No single triangulation is
  S₅-canonical. The canonical content lives on the **Reynolds-symmetric representative** `H_sym` =
  the group-average over the 120 orderings — which is an **orbit mean no triangulation realizes**
  (it discards `~59%` of the raw block's Frobenius norm; its spectrum lies inside the raw spectrum).
- **Commutation/Schur/frame-invariance tests are automatic, not discovered (TAUT).** Because `H_sym`
  is the S₅-group-average, it commutes with S₅ by the Reynolds identity and is Schur-scalar on the
  multiplicity-free `1⊕4⊕5` channels **by construction**; conjugating it by any S₅ frame returns it
  identically. The runner
  proves this carries no geometry: a **random** Hermitian matrix group-averaged by the same S₅ passes
  the identical commutation/Schur tests to `1.7e-15`. Therefore these tests measure the averaging
  operation, not prism geometry, and are **not by themselves** a distinguished connection.
- **The background is non-critical.** The static round `∂Δ⁴ × Z_τ` right-prism is **not** a Λ-Regge
  critical point (no `(Λ, a_τ²)` makes the EOM vanish; max residual `~3.55`, tick-dominated — as
  expected, static `S³ × R` is not Einstein). So `H(k_τ)` is the second-variation form at a Λ-tuned
  symmetric *reference*, not at a solution; the `k_τ=0` channel **sign** pattern matching the retained
  3D round-S³ holds only for the least-squares `Λ*` (robust for `Λ ∈ [4.3, 15]`), not as a Λ-free
  invariant.

**Verdict:** the curved 3+1 prism build **modestly advances** the program (a verified curved 3+1
Regge Hessian plus the new tick-momentum channel dispersion), but it **does not discharge** the
polarization-frame-bundle blocker. The tested Reynolds-symmetrization criterion is insufficient by
itself (TAUT); a discharge would still need a triangulation-independent covariant transport at a true
Regge-critical background or another comparably strong route. That is the sharpened open problem.

## 4. Inputs (one hop, fresh statuses on origin/main)

| Input | Role | Status |
|---|---|---|
| round `∂Δ⁴` Λ-Regge structure + S₅ channels `1⊕4⊕5` (the reduction target) | round-S³ reduction gate G5 | [`UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md`](UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md) — **retained_bounded** |
| 4-simplex dihedral kernel `THETA`/`AREA` (flat tick-extension machinery) | construction checks G1-G6 (reused verbatim) | [`CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md`](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) — unaudited construction template, not cited as a retained result |
| `Z³`/`∂Δ⁴` adjacency, Cayley-Menger 4-volume | the prism geometry | [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) for the Lattice axiom; the finite `∂Δ⁴` prism geometry is built directly by the runner |
| the frame-ambiguity / distinguished-connection need | §3 context target, not discharged | [`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md) — audited_conditional |

No fitted parameters, no observed values, **no curved-EH / Lichnerowicz / M_EH comparator** (the named
import-risk — the runner is comparator-free; the flat `c=−½` comparator does not appear), no new
axioms, no flavor dial.

## 5. Boundary / honest-auditor read

The correctness backbone (closed-manifold tiling gate G1, Hermiticity gate G3,
Schläfli gate G4, and action finite-difference gate G6) and the round-S³
reduction gate G5 are machine-exact and independently re-validated (G6 against a from-scratch action).
The one new positive result is the tick-momentum
channel dispersion (DISP). Everything labelled "canonical"/"frame-covariant" on `H_sym` is
explicitly **automatic** (definitional on the group-average; TAUT proves it), **not** a discovered
connection. The off-round degeneracy-lift check is a consistency check **replicating** the landed PL-S³
off-round result in the 3+1 prism, not a new connection. The capstone — the distinguished connection
that would discharge the frame-bundle blocker — is **not achieved**; the honest contribution is the
verified curved 3+1 prism build, the new tick dispersion, and the precise route-boundary
characterization (single-triangulation S₅-breaking + symmetrization-is-automatic + non-criticality) of
why the tested symmetric-representative criterion is insufficient. The continuum limit, the dimensionful GR
calibration (import-bounded), and `S₅/∂Δ⁴`-vs-cubic-`O_h` all remain out of scope.
