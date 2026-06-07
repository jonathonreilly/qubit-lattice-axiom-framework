# Strong-CP: the Multi-Plaquette F̃F (Clover) Is Admissible — the Open Action-Class Boundary Is Not Clean-Closeable (Action-Side Complement)

**Date:** 2026-06-07
**Scope:** bounded obstruction note (action-side; presses the single-plaquette note's open boundary; NOT a closure)
**Claim type:** no_go
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_strong_cp_multiplaquette_ftf_admissible_not_clean_closeable_exact.py`](../scripts/audit_companion_strong_cp_multiplaquette_ftf_admissible_not_clean_closeable_exact.py) (sympy, 5/5)
**Runner cache:** [`logs/runner-cache/audit_companion_strong_cp_multiplaquette_ftf_admissible_not_clean_closeable_exact.txt`](../logs/runner-cache/audit_companion_strong_cp_multiplaquette_ftf_admissible_not_clean_closeable_exact.txt)

## Result

The single-plaquette gauge action class is `F̃F`-free (a real class function `f` gives `O(a^6)`, no leading `F̃F`;
[`NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md`](./NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md)), with **multi-plaquette (two-field-strength)
operators** named as the open boundary. This note presses that boundary to a definite answer: **the boundary does
not close `θ_gauge = 0`** — the `F̃F` slot is realizable by an operator that no clean framework principle excludes.

**Computed (exact, runner (1)–(3))** — the `F̃F` algebra, plus the leading-order reduction under the *standard
clover model* `Q_{μν} ~ i a² F_{μν} + O(a^4)`:

- `F̃F = ε_{μνρσ} F_{μν} F_{ρσ} = 8(F_{01}F_{23} − F_{02}F_{13} + F_{03}F_{12})` — the `E·B` topological density,
  generically nonzero. **[fully computed]**
- Under the leading-order clover model `Q_{μν} ~ i a² F_{μν}`, the contraction `ε_{μνρσ} tr(Q_{μν} Q_{ρσ})`
  reduces to `−a⁴ F̃F` — i.e. the lattice `F̃F` slot is populated at leading order. **[computed under the standard
  clover-model substitution, not a from-scratch lattice expansion]**
- A **single** plaquette cannot build `F̃F` (`tr F = 0`; `ε·F` carries free indices, needing a second field strength
  in the complementary plane) — `F̃F` is intrinsically a **two-field-strength** object, consistent with the
  single-plaquette `O(a^6)` theorem.

**Admissibility** (standard facts, bookkept — *not* derived here; runner (4)): the clover topological density is
**gauge-invariant** (a trace of Wilson loops), **local** (a finite cluster), a **real-valued density** entering the
action as the **imaginary** `iθ q(x)` term, **not excluded by the retained reflection-positivity half-square no-go**
([`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](./STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md); note: the complex Euclidean
`θ`-weight is *not* claimed to be full OS reflection-positive — only that the retained RP no-go does not forbid it),
and **CPT-even** (`Q` is CPT-even;
[`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](./STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md)).
So **no** reality / RP-no-go / CPT / locality / gauge-invariance principle excludes the clover `F̃F`.

**Conclusion** (runner (5)): only a **single-plaquette / minimality admission** removes the `F̃F` slot. The
multi-plaquette boundary is therefore **not clean-closeable**: `θ_gauge = 0` requires that admission; it is not
derived by restricting the action class to forbid `F̃F`.

## Two-sided picture for θ_gauge

Together with the measure-side companion
([`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](./STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md)), `θ_gauge` is
admitted from **both** sides:

| side | statement |
|---|---|
| **measure** | reality, positivity, and CPT of the measure do **not force** `θ_gauge = 0` (extends the RP no-go) |
| **action** | the `F̃F` operator (clover) is **admissibly realizable**; no clean principle excludes it (this note) |

The action *can* carry `F̃F`, and the **listed measure-side principles (reality, positivity, CPT) do not force or
forbid it** — because the topological term is `Θ`-anti-invariant. So `θ_gauge` is a **minimality admission**,
structurally parallel to the matter-side Koide
`r = 1/2` (`BAE`) admission: both ride on un-derived **dynamics** (the gauge action here; the matter realization
there) while the kinematic axioms `{Lattice, Quantum, Record}` fix only the structure.

## Scope — what this is and is not

- **Is:** a computed demonstration (`F̃F` algebra + the clover leading-order reduction) that the `F̃F` slot is
  concretely realizable, plus a bookkeeping of its admissibility, concluding the multi-plaquette boundary is not
  closeable by any clean framework principle.
- **Is not:** a claim that `θ_gauge ≠ 0`, or that the framework's action *does* contain `F̃F` (it is an admissible
  *option*, not a forced term); a derivation of the admissibility facts (gauge-invariance, locality, RP, CPT are
  cited/bookkept); a new axiom; a closure. The `θ = 0` selected-surface result is unaffected.
- **Residual:** `θ_gauge = 0` reduces to the **single-plaquette / minimality admission** on the gauge action
  (which the framework hand-adds; the action is not derived).

## No-Go Discipline (N1-N8)

- **N1 — alternative routes.** (1) **ATTEMPTED:** single-plaquette action class excludes leading
  `F̃F`; this is the known minimality route, but it is an action-class admission unless derived.
  (2) **ATTEMPTED:** build `F̃F` from one plaquette; it fails because a scalar `F̃F` needs two
  complementary field strengths. (3) **ATTEMPTED:** two-plaquette/clover construction; it succeeds,
  so the multi-plaquette boundary remains open rather than excluded. (4) **ATTEMPTED:** exclude the
  clover slot by locality/gauge invariance; it fails because the slot is local and gauge-invariant
  as a standard finite Wilson-loop density. (5) **ATTEMPTED:** exclude it by RP/CPT/reality; it
  fails for the same measure-side reasons documented in the companion note. (6) **OPEN:** derive a
  stricter gauge-action principle that forces the single-plaquette/minimal class.
- **N2 — wall independence.** Single-plaquette minimality, clover realizability, locality/gauge
  invariance, and measure-side RP/CPT/reality are independent gates; none follows from another.
- **N3 — hidden-wall scan.** The clover leading-order reduction is computed under the stated standard
  clover model, not claimed as a from-scratch lattice expansion. Standard admissibility facts are
  bookkept rather than smuggled as retained derivations.
- **N4 — residual matching.** The single-plaquette note attacks only the one-plaquette action class.
  This note attacks the named multi-plaquette residual and does not reuse the single-plaquette result
  as a closure.
- **N5 — rhetoric audit.** "Not clean-closeable" means not closed by the listed clean principles
  (single plaquette absent, locality/gauge invariance/RP/CPT/reality). It does not say no future
  gauge-action derivation can exclude `F̃F`.
- **N6 — partial-closure scan.** A derived single-plaquette/minimal gauge action would retire this
  wall without a new axiom. That remains the legitimate import-retirement path.
- **N7 — steelman.** The strongest objection is that the framework might later derive the minimal
  single-plaquette action as the only admissible action. If so, `F̃F` is excluded by that new action
  theorem; this note only says the current multi-plaquette boundary is not excluded by the listed
  principles.
- **N8 — cross-cycle echo.** The result mirrors prior action-class campaigns where a term is absent
  in a minimal ansatz but admissible in a larger local class; the right residual is the action-class
  minimality theorem, not a claim that the term is forced.

## Forbidden-import / reprove-and-cite discipline

- The `F̃F` algebra and the clover leading-order reduction are **reproven** from the Levi-Civita / antisymmetric
  field-strength primitive in the runner (sympy, exact).
- The lattice clover construction, the single-plaquette no-`F̃F` theorem, the RP no-go, and the discrete-symmetry
  parities are **comparators** only — named for provenance and cross-check, never derivation inputs. The
  admissibility facts (gauge-invariance, locality, RP, CPT) are bookkept standard facts, explicitly not derived.
- No PDG values appear; `θ = 0` is the empirical target, not derived.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](./STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md)
- [`NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md`](./NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md)
- [`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](./STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
- [`STRONG_CP_THETA_ZERO_NOTE.md`](./STRONG_CP_THETA_ZERO_NOTE.md)

**Independent audit required.** This note asserts no effective-status change.
