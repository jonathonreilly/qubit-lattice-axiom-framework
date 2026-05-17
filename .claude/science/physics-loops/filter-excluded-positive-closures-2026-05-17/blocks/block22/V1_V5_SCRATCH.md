# Block 22 V1-V5 Scratch

Row: `observable_principle_from_axiom_note`
State: `audited_conditional` (bounded_theorem), desc=713, lbs=26.70, critical.
Lane: observable_principle (TOTALLY FRESH — no prior block under this
campaign on this row).

## Setup

Target is the parent `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` which
conditionally derives `W = log|det(D+J)|` as the unique additive CPT-even
continuous scalar generator on the exact minimal hierarchy block, given
four admitted premises P1-P4. As of 2026-05-09, the runner-local
derivations retire P2/P3/P4 to runner-local algebraic consequences plus
zero-source baseline convention. The remaining admitted premise is
**P1 (scalar additivity on independent subsystems)**.

The audit `notes_for_re_audit_if_any` repair target:

> Re-audit if scalar additivity and CPT-even phase-blindness are
> accepted as retained-grade upstream theorems, **or if the source is
> narrowed to a conditional exact-algebra statement**.

The note already implements branch (b) (narrowed conditional). Path (a)
(close P1) has been heavily attacked in 5 prior sibling notes (PRs
#1368, #1373, #1402, #1406, plus the Route D consolidated sharpened
no-go). All five routes converge on the same obstruction: the
counterexample family `F_p[J] = r(J)^p` for `p ≠ 1` is compatible with
every standard mathematical scaffold considered (operator-algebraic,
information-theoretic, framework-internal, cross-disciplinary
categorical/topological/tropical), so P1 is **not derivable** from the
current retained authority chain combined with those four scaffold
families. Documenting a sixth route on P1 derivation would be churn.

## Distinct angles from prior observable_principle siblings

Existing siblings around this parent:

- `OBSERVABLE_PRINCIPLE_REAL_D_BLOCK_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10` —
  block-local uniqueness of `W` on the real anti-Hermitian Dirac block
  given admissibility class (X2). Currently `audited_failed` on the
  live ledger; its X2 embeds P1 as criterion (A).
- `OBSERVABLE_PRINCIPLE_SCALE_INVARIANT_SOURCE_RESPONSE_NARROW_THEOREM_NOTE_2026-05-16` —
  the residual scale `c` cancels in every normalized ratio observable
  on the (X2) class. Already lands; covers the `c = 1` normalization
  side of P4.
- `OBSERVABLE_PRINCIPLE_P1_BRIDGE_OPERATOR_ALGEBRAIC_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17`
  (Route A). Records the operator-algebraic obstruction.
- `OBSERVABLE_PRINCIPLE_P1_BRIDGE_SHANNON_KHINCHIN_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17`
  (Route B). Records the information-theoretic obstruction.
- `OBSERVABLE_PRINCIPLE_P1_BRIDGE_FRAMEWORK_INTERNAL_NARROW_BOUNDED_NOTE_2026-05-17`
  (Route C). Records the framework-internal obstruction.
- `OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_D_SHARPENED_NO_GO_NOTE_2026-05-17`
  (Route D). Sharpened consolidated no-go.
- `OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_E_TAO_CROSS_DISCIPLINARY_NARROW_BOUNDED_NOTE_2026-05-17`
  (Route E). Records the cross-disciplinary obstruction.

A sixth P1-derivation route would be churn (per
`feedback_physics_loop_corollary_churn.md`).

Distinct in-scope theorems closing **different** load-bearing steps of the
parent are needed.

## V1 — A 6th P1-derivation route (e.g., model-theoretic categorical
       semantics, type-theoretic propositions-as-types, ergodic theory,
       Galois conjugation forcing)

VERDICT: SKIP. Route D explicitly enumerates the structural obstruction
(`F_p` counterexample compatible with every standard mathematical
scaffold; Pattern L circularity + Pattern D inapplicability). Any new
route either invokes `log` (Pattern L = P1) or operates on non-scalar
direct-sum structure (Pattern D = inapplicable to scalar `Z ∈ R`).
Documenting another negative is churn; six negatives across one
load-bearing step is already comprehensive. SKIP.

## V2 — Strengthen the X2 admissibility-class generator-uniqueness
       theorem from the (now `audited_failed`) real-D block uniqueness
       note to a positive narrow theorem on a different admissibility
       class

VERDICT: SKIP. The X2 class explicitly bundles P1 as criterion (A) per
Route C's catalog. Any uniqueness theorem on a P1-containing
admissibility class is equivalent to admitting P1; uniqueness is then
just Cauchy's logarithm functional equation closure, which is the same
P1-conditional move the parent already does. No new load-bearing step
closure. SKIP.

## V3 — Klein-four orbit structure on APBC phases for ALL even L_t
       (closed-form proof of parent's Theorem 4)

This is the angle.

**Observation.** Parent note Theorem 4 claims:

> The curvature kernel depends only on `sin² ω`, so it is exactly
> invariant under the Klein-four action on APBC phases: `z → z, -z, z*, -z*`.
> On the APBC temporal circle:
>   - `L_t = 2` gives only the unresolved sign pair
>   - `L_t = 4` gives the unique minimal resolved closed orbit
>   - `L_t > 4` splits immediately into multiple orbit sectors
> So the `L_t = 4` selector is internal to the axiom-plus-source response.

The parent runner (`frontier_hierarchy_observable_principle_from_axiom.py`)
checks this **numerically** only on the finite scan
`L_t ∈ {2, 4, 6, 8, 10, 12}` (`orbit_partition`, `orbit_weights`,
`test_orbit_kernel_and_selector`). The "for all even `L_t`" closure
exists in the natural-language proof but is not verified at runner
scope, and not proved in closed form anywhere.

Sibling `HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md` makes the same
qualitative claim ("L_t > 4 splits immediately into multiple closed
orbit sectors") but without a closed-form derivation or all-even-L_t
witness. Neither note proves it as a number-theoretic statement.

**Narrow theorem opportunity.** The Klein-four orbit structure on APBC
phases is entirely a finite-group action on roots-of-unity. It is
**independent** of P1, **independent** of the Dirac determinant,
**independent** of any physical-principle premise. It is a purely
algebraic / number-theoretic statement.

The closed-form proof: APBC phases of order `L_t = 2m` (even) are
`z_n = e^{i(2n+1)π/(2m)}` for `n = 0, …, 2m-1`. The Klein-four invariant
of `z = e^{iω}` is `sin²(ω)`. The Klein-four orbit count equals the
number of distinct values of `sin²((2n+1)π/(2m))` for `n = 0, …, 2m-1`.

By the identities `sin²(θ + π) = sin²(θ)` and `sin²(π - θ) = sin²(θ)`:

- `n ↔ n + m` mod `2m` collapses (period-π identity).
- `n ↔ m - 1 - n` on `{0, …, m-1}` collapses (reflection identity).

Effective parameter space: `n ∈ {0, …, m-1}` modulo `n ↔ m - 1 - n`,
giving
   - `(m+1)/2` distinct values for odd `m`,
   -  `m/2` distinct values for even `m`.

Equivalently, distinct orbit count = `⌈m/2⌉`.

Single-orbit condition `⌈m/2⌉ = 1 ⟺ m ∈ {1, 2} ⟺ L_t ∈ {2, 4}`.

At `L_t = 2`: one orbit `{i, -i}` of size 2 with `sin²(π/2) = 1`.
   This is the **unresolved sign pair** — orbit size = 2.

At `L_t = 4`: one orbit `{e^{iπ/4}, e^{i3π/4}, e^{i5π/4}, e^{i7π/4}}` of
   size 4 with `sin²(π/4) = 1/2` uniformly across the orbit.
   This is the **unique minimal resolved orbit (size > 2)**.

At `L_t = 6, 8, 10, …`: at least 2 distinct `sin²` values, so at least
   2 orbits — never a single resolved orbit.

So the closed-form claim is:

> **Theorem (Klein-four APBC orbit partition).** For every even
> `L_t = 2m` with `m ≥ 1`, the number of Klein-four orbits on the APBC
> phase set `{e^{i(2n+1)π/(2m)} : n = 0, …, 2m-1}` equals `⌈m/2⌉`.
> Equivalently, the Klein-four orbits are level sets of
> `sin²((2n+1)π/(2m))` and there are exactly `⌈m/2⌉` distinct level
> values.

> **Corollary (unique minimal resolved orbit).** The Klein-four orbit
> partition has a single orbit iff `L_t ∈ {2, 4}`. At `L_t = 2` the
> orbit has size 2 (the unresolved sign pair `{+i, -i}`). At
> `L_t = 4` the orbit has size 4 (the unique minimal resolved orbit)
> and is uniformly weighted with `sin² ω = 1/2`. For every even
> `L_t ≥ 6`, the orbit partition has `⌈L_t/4⌉ ≥ 2` orbits.

This is exactly Theorem 4 of `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`
proved in closed form for **all** even `L_t`, not just the runner's
finite scan up to `L_t = 12`. It does not consume P1, P2, P3, or P4. It
does not promote the parent. It does not change any audit status. It
closes one named load-bearing step (Theorem 4 selector claim) at the
strongest possible scope: closed-form derivation for every even `L_t`.

The runner verifies (a) the closed-form orbit count `⌈m/2⌉` against
direct orbit-partition enumeration for `L_t ∈ {2, 4, 6, …, 64}` (more
than 5× the parent's scan range), (b) the symbolic SymPy verification
of the trigonometric identities `sin²(θ + π) = sin²(θ)` and
`sin²(π - θ) = sin²(θ)` that drive the proof, (c) the uniqueness of
`L_t ∈ {2, 4}` for single-orbit case across `L_t = 2, 4, …, 200`, and
(d) the unique-resolved-orbit characterization at `L_t = 4` (size 4,
weight 1/2).

## V4 — Klein-four orbit weight uniformity → A(L_t) numerator
       structure for selector base

VERDICT: SKIP. The parent's quadratic-coefficient `A(L_t)` is computed
as `(1/(2 L_t u_0^2)) Σ_ω 1/(3 + sin² ω)`. Once V3 proves the orbit
structure, the `A(L_t)` numerator is fixed by counting orbits and
weights, but the parent runner already exhibits this computation
numerically and the (7/8)^(1/4) ratio is a downstream consumption of
hierarchy baseline — promoting it would touch the parent's
out-of-scope numerical `v` readout. SKIP — too close to parent's
out-of-scope content.

## V5 — Klein-four orbit characteristic-polynomial structure
       (cyclotomic-Galois)

This is potentially additional content but at risk of being a stretch
beyond the 90-min budget. The Klein-four orbits at `L_t = 4` are
exactly the roots of `Φ_8(x) = x^4 + 1`. The orbit weights `sin² ω = 1/2`
follow from `x + 1/x = 2 cos(ω) = ±√2`, giving the algebraic
characterization. For `L_t = 2m`, the APBC phases are the `2m`-th roots
of `-1` (i.e., primitive `4m`-th roots of unity not in `(2m)`-th roots
of unity), which factor through cyclotomic polynomials.

VERDICT: Useful supporting algebraic content for V3, but the orbit count
`⌈m/2⌉` already gives the clean closed-form statement. Including the
cyclotomic identification as an `Observation 5` strengthens the
narrative without expanding scope. KEEP AS SUPPORTING.

## Decision

V3 is the angle. Build a positive narrow theorem note + paired runner +
cached output. Source-only PR. A_min only. V5 included as a brief
algebraic observation; not load-bearing on its own.

## Hard rules check

- A_min only: the entire derivation is on APBC roots-of-unity under the
  Klein-four `{1, -1, *, -*}` action; uses no framework primitives
  beyond the APBC phase set definition already in the parent. No new
  framework primitives. No P1 input. No Dirac determinant input.
- Source-only PR: docs/ source note + block artifacts, scripts/ runner,
  logs/runner-cache/ runner output. No CANONICAL_HARNESS_INDEX,
  DERIVATION_ATLAS, DERIVATION_VALIDATION_MAP, audit-data, README, or
  lane-registry touches.
- Status authority: independent audit lane only; note labels itself
  bounded_theorem with claim scope explicit.
- Does NOT close: the P1 admitted premise, the parent's overall
  `audited_conditional` audit verdict, the `v` numerical readout, the
  hierarchy baseline `M_Pl * α_LM^16`, the Grassmann factorization
  step, or any sibling note's audit status. Closes ONLY the closed-form
  algebraic Theorem 4 selector content for all even `L_t`.
