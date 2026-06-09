# Plaquette Bootstrap — Framework-Integration Theorem Note

**Date:** 2026-05-03
**Type:** bounded/exact support theorem + named-obstruction stretch
**Claim scope:** map the lattice-bootstrap approach (Anderson-Kruczenski 2017,
Kazakov-Zheng 2022/2024, JHEP 12(2025) 033) onto the framework's retained
primitives, establish that the framework's existing reflection-positivity
theorem (A11, `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`)
is sufficient as the load-bearing positivity input for Wilson-loop Gram
matrix PSD **only for Wilson-loop observables proven to lie in A11's
2-step blocked/factorized `A_+^(2)` surface**, and derive the smallest
non-trivial PSD consequence there: reflected connected-plaquette
non-negativity. The retained mixed-cumulant onset theorem
(`P_full(β) = P_1plaq(β) + β^5/472392 + O(β^6)` at small `β`) is cited
as an exact source authority for the first nonlocal coefficient, not as
a full `β = 6` theorem.
The result is a framework-integration scaffold + sharper named obstruction,
NOT closure of the famous open lattice problem.
**Audit repair:** 2026-06-09 A11-surface narrowing + mixed-cumulant source
repair. This revision addresses the prior `scope_too_broad` blocker by
restricting BB1 to the `A_+^(2)` Wilson-loop surface covered by the
retained-bounded A11 reroute and by naming the retained mixed-cumulant
authority explicitly. The `β = 6` arithmetic is demoted to a formal
diagnostic/comparator, not an audited theorem scope.
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/frontier_plaquette_bootstrap_framework_integration.py`

## 0. Question

`PLAQUETTE_SELF_CONSISTENCY_NOTE.md` (status amended 2026-05-01 to
`bounded`) records the verdict:

> "the explicit analytic `beta = 6` insertion remains open."

The user's net-call assessment proposed three routes for closing
`⟨P⟩(β=6)` analytically:
- H1 Route 1: minimal-block self-consistent saddle (attempted in PR
  [#410](https://github.com/jonathonreilly/cl3-lattice-framework/pull/410),
  named-obstruction stretch).
- H1 Route 2: Cl(3)+Klein-four counting forcing β=6 (skipped per V1 —
  `G_BARE_RIGIDITY_THEOREM_NOTE.md` already addresses it).
- H1 Route 3: modern lattice bootstrap with reflection positivity +
  Migdal-Makeenko + SDP.

This note sets up H1 Route 3 inside the framework, identifies what is
already retained vs newly admitted, and derives the smallest non-trivial
PSD consequence that follows from the framework's existing reflection
positivity (A11), while citing the bridge-support stack's exact
mixed-cumulant onset theorem as source context. It does not claim a
retained `β = 6` plaquette value.

## 1. Setup

Retained framework primitives:

| # | Primitive |
|---|---|
| A1-A4 | local algebra `Cl(3)`, substrate `Z³`, finite Grassmann/staggered-Dirac, canonical Wilson normalization `g_bare = 1` (β = 6) |
| A7 | closed-form determinant on minimal `L_s = 2` APBC block |
| **A11** | **retained-bounded 2-step blocked/factorized reflection positivity on `A_+^(2)`** |
| **Gauge OS Step 1 companion** | retained-bounded Wilson plaquette decomposition and reflection-Hermiticity for Wilson-loop observables localized in `t >= 0` |
| **Mixed-cumulant onset theorem** | retained exact first-nonlinear coefficient on the accepted Wilson `3 spatial + 1 derived-time` surface |

Newly proved/narrowed support in this note:

| # | Bridge | Class |
|---|---|---|
| BB1 | Wilson-loop Gram matrix `G_AB = ⟨Θ(W_A) W_B⟩ ⪰ 0` for `{W_A}` already proven to be in the factorized `A_+^(2)` Wilson-loop observable surface | Direct corollary of A11 (R2) restricted to a verified subalgebra |
| BB1' | Connected reflected-plaquette correlator non-negativity for the same verified `A_+^(2)` plaquette pair | Mean-subtracted A11 (R1/R2) application |
| BB2-context | Mixed-cumulant first nonlocal coefficient `β^5/472392` | Cited retained theorem; used as onset/source context, not a `β = 6` closure |

Not newly admitted here:

| # | Bridge | Status |
|---|---|---|
| Migdal-Makeenko / one-link Schwinger-Dyson equations | named future route; not used as a load-bearing theorem in this row |
| Full `β = 6` bootstrap/SDP plaquette bound | open |

Comparators (admitted-context only):

- Canonical lattice MC: `⟨P⟩(β=6) ≈ 0.5934` (`PLAQUETTE_SELF_CONSISTENCY_NOTE`)
- Bridge-support analytic upper-bound candidate: `P(6) ≈ 0.59353`
- Kazakov-Zheng 2022 SU(∞) bracket near λ≈1.35: `⟨P⟩ ∈ [0.59, 0.61]` at L_max=16 ([arXiv:2203.11360](https://arxiv.org/abs/2203.11360))
- Kazakov-Zheng 2024 SU(2) finite-N: 0.1% precision in physical range ([arXiv:2404.16925](https://arxiv.org/abs/2404.16925))
- Mixed-cumulant onset theorem:
  `P_full(β) = P_1plaq(β) + β^5/472392 + O(β^6)` at small `β`
  (`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE`)

## 2. Lemma BB1 — A11 implies scoped Wilson-loop Gram-matrix PSD

**Lemma.** Let `{W_A}` be any finite set of Wilson-loop observables already
proved to belong to the factorized 2-step blocked A11 observable algebra
`A_+^(2)` on the positive-time side. In particular, this includes
Wilson-loop observables whose temporal-gauge plaquette decomposition and
reflection-Hermiticity are supplied by
`GAUGE_OS_STEP1_WILSON_PLAQUETTE_DECOMPOSITION_THETA_INVARIANCE_REFLECTION_HERMITICITY_NARROW_THEOREM_NOTE_2026-06-02.md`.
Then the Gram matrix

```text
G_{AB}  =  ⟨ Θ(W_A) · W_B ⟩
```

is Hermitian positive semidefinite (PSD), where `Θ` is the temporal-link
reflection of A11.

**Proof.** The current retained-bounded A11 route states the PSD
sesquilinear form on the factorized 2-step blocked observable surface
`A_+^(2)`. Therefore, for Wilson-loop observables whose membership in
that surface is supplied by the Wilson plaquette decomposition /
reflection-Hermiticity companion, restricting the bilinear form to the
finite span of `{W_A}` gives `G_{AB}`. Restriction of a PSD Hermitian
sesquilinear form to a finite-dimensional subspace gives a PSD
Hermitian matrix. ∎

**Consequence.** All leading principal minors of `G_{AB}` are non-negative.
For any `α ∈ ℂ^{|A|}`, `∑_{AB} α_A^* α_B G_{AB} ≥ 0`.

## 3. Smallest non-trivial Gram matrix on the minimal block

Let `1` denote the identity (constant observable). Let `P` denote the
Wilson plaquette `(1/N_c) Re tr U_p` for one specific spatial plaquette
`p` localized entirely on the A11-positive, factorized `A_+^(2)` side.
The Gauge OS Step 1 companion supplies the source-level reason this
plaquette observable is reflection-Hermitian in the Wilson surface:
`Θ(1) = 1`, `Θ(P) = P_-`, where `P_-` is the reflected plaquette in the
negative half.

The 2x2 Gram matrix is:

```text
G_{2x2}  =  | ⟨Θ(1) · 1⟩    ⟨Θ(1) · P⟩  |   =   | 1            ⟨P⟩         |
            | ⟨Θ(P) · 1⟩    ⟨Θ(P) · P⟩  |       | ⟨P⟩          ⟨P_- · P⟩  |
```

By translation invariance and ⟨P⟩ = ⟨P_-⟩ = ⟨P⟩ (shorthand for the
canonical-volume average), the off-diagonal is just `⟨P⟩`. The diagonal
`⟨Θ(P) · P⟩ = ⟨P_- · P⟩` is the **reflected-plaquette correlator**,
which by definition splits into a connected and disconnected piece:

```text
⟨P_- · P⟩   =   ⟨P⟩²   +   C_{P_-, P}
```

where `C_{P_-, P}` is the connected correlator (positive by scoped RP;
see Lemma BB1' below). No cluster-decomposition theorem is needed for
this algebraic decomposition.

PSD of `G_{2x2}` ⟺ `det G_{2x2} ≥ 0`:

```text
det G_{2x2}  =  ⟨P_- · P⟩ - ⟨P⟩²  =  C_{P_-, P}  ≥  0.
```

The 2x2 PSD constraint is therefore equivalent to the non-negativity of the
reflected-plaquette connected correlator — which is a direct restatement
of A11 (R1).

**Result of the smallest non-trivial Gram matrix:** `C_{P_-, P} ≥ 0`. This
is *consistent with* but does not *bound* `⟨P⟩(β=6)` on its own.

## 4. Lemma BB1' — connected correlator non-negativity

**Lemma.** For any reflected pair `(P_-, P)` of real-Hermitian Wilson loops
on the verified `A_+^(2)` surface, the connected correlator
`C_{P_-, P} = ⟨P_- · P⟩ - ⟨P⟩² ≥ 0`.

**Proof.** Apply A11 (R1) with `F = P - ⟨P⟩` (a real-valued
mean-subtracted observable on the verified `A_+^(2)` surface). Then
`Θ(F) = P_- - ⟨P⟩` (since the reflection of a
constant is itself). Expanding:

```text
0 ≤ ⟨Θ(F) · F⟩  =  ⟨(P_- - ⟨P⟩)(P - ⟨P⟩)⟩
                =  ⟨P_- P⟩ - ⟨P⟩²       (using ⟨P_-⟩ = ⟨P⟩ = ⟨P⟩)
                =  C_{P_-, P}.
```

So `C_{P_-, P} ≥ 0` follows directly from RP applied to mean-subtracted
plaquettes. ∎

## 5. Mixed-cumulant authority and the formal β = 6 diagnostic

The retained `GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE` (also
cited in `PLAQUETTE_SELF_CONSISTENCY_NOTE` "Exact bridge-support stack
on `main`") provides the exact first nonlocal/onset identity:

```text
P_full(β)  =  P_1plaq(β)  +  β^5 / 472392  +  O(β^6).
```

where `P_1plaq(β)` is the single-plaquette baseline value (computable via
SU(3) character expansion). This is an exact small-`β` coefficient
statement on the framework Wilson surface. It is not a nonperturbative
`β = 6` closure and is not used here as a rigorous `β = 6` bound.

Formal diagnostic at `β = 6`:

```text
β^5 / 472392  =  6^5 / 472392  =  7776 / 472392  ≈  0.016460.
```

The single-plaquette `P_1plaq(β)` for SU(3) at the strong-coupling leading
order is `β/(2N²) = 6/18 = 1/3 ≈ 0.333`.

This gives a **single-plaquette + first nonlocal correction** estimate:

```text
P_full(6)  ≈  P_1plaq^LO(6)  +  0.0165  +  (higher orders ignored)
           ≈  0.3498.
```

The actual MC value is 0.5934 — the strong-coupling expansion is NOT
convergent enough at β=6 to give a tight bound from this truncated
onset data. This mismatch is the named obstruction, not a failed
theorem: the exact retained content is the onset coefficient, not the
formal β=6 truncation.

**Honest result:** the smallest non-trivial framework-integration of the
bootstrap approach gives:

(a) Lemma BB1: retained-bounded A11 ⟹ Wilson-loop Gram matrix PSD on
    the verified `A_+^(2)` Wilson-loop surface.

(b) Lemma BB1': connected reflected-plaquette correlator non-negativity
    follows from A11 directly (mean-subtracted variant).

(c) Smallest 2x2 PSD analytically equivalent to (b); does NOT bound
    `⟨P⟩(β=6)` on its own.

(d) Combining with the retained mixed-cumulant onset theorem gives a
    formal truncated diagnostic `P_full(6) ≈ 0.3498`, which is far below
    the MC value 0.5934. This reflects that onset data alone does not
    solve the nonperturbative β=6 problem.

## 6. Sharper named obstruction

Tightening this scaffold into an analytical `β = 6` bound at the
published Kazakov-Zheng precision (~2-3% near λ≈1.35) requires:

```text
[BOOTSTRAP-TIGHTENING OBSTRUCTION]:
  The framework's existing primitives + 2x2 small-truncation bootstrap
  give only weak formal diagnostics for ⟨P⟩(β=6). Tightening requires:
    (a) explicit derivation of lattice Migdal-Makeenko / Schwinger-Dyson
        loop equations on the framework's V-invariant minimal block, OR
    (b) higher-truncation (L_max = 6+) Gram matrices + industrial SDP
        solver, OR
    (c) framework-specific positivity refinements from Cl(3) Hilbert-
        Schmidt structure + Klein-four orbit-closure (block 02 attempt).
```

The (c) route is the natural framework-internal next cycle (block 02 of
this campaign).

## 7. Connection to bridge-support stack

The framework's bridge-support stack
(`PLAQUETTE_SELF_CONSISTENCY_NOTE.md` "Exact bridge-support stack on `main`")
already provides an **analytic upper-bound candidate** `P(6) ≈ 0.59353`
from explicit Perron-state reduction theorems and source-sector matrix-element
factorization at β=6, with the explicit window `0.5934 ≤ ⟨P⟩(β=6) ≤ 0.59353`
(±0.022%).

This bootstrap framework-integration provides:
- A **complementary structural attack** via reflection positivity + Gram-matrix PSD
- A **first-onset diagnostic** (Section 5) — currently far below MC because
  finite-order small-β data do not control the β=6 point
- A **roadmap** (Section 6) for tightening via framework-specific positivity (block 02)

The bridge-support upper-bound route and the bootstrap/PSD diagnostic
route attack the analytic problem from opposite sides; turning the
diagnostic side into an actual lower bound remains part of the famous
open lattice problem.

## 8. What this note closes

- Framework-integration of the lattice bootstrap approach: A11 (RP theorem)
  is the load-bearing positivity input for the verified `A_+^(2)`
  Wilson-loop surface; Wilson-loop Gram matrix PSD follows directly
  there.
- Lemma BB1 + BB1': rigorous PSD on the A11-scoped framework surface for
  any finite Wilson-loop set already proven to lie in `A_+^(2)`.
- Identification of the smallest non-trivial 2x2 case as equivalent to
  reflected connected-correlator non-negativity.
- Sharper named obstruction: explicit roadmap for tightening (block 02 +
  future industrial SDP work).

## 9. What this note does NOT close

- The analytical value of `⟨P⟩(β=6)` (famous open lattice problem).
- A non-trivial lower bound on `⟨P⟩(β=6)` beyond formal small-β onset
  diagnostics.
- PSD for arbitrary Wilson-loop observables not shown to belong to
  A11's `A_+^(2)` surface.
- Industrial-SDP-class precision (~2-3% as Kazakov-Zheng 2022).

## 10. Honest status

```yaml
actual_current_surface_status: bounded/exact support theorem + named-obstruction stretch
target_claim_type: positive_theorem (BB1, BB1') / open_gate (full ⟨P⟩(β=6) bound)
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  Lemma BB1 (Wilson-loop Gram PSD from A11) and Lemma BB1' (connected
  correlator non-negativity) are exact-support theorems on A11's
  verified 2-step blocked/factorized `A_+^(2)` Wilson-loop surface.
  A11 is currently retained_bounded, and the mixed-cumulant source
  theorem is retained for the first nonlinear/onset coefficient.
  The formal β=6 substitution is a diagnostic/comparator only, not a
  rigorous bound; honest output is named-obstruction stretch.
audit_required_before_effective_retained: true
bare_retained_allowed: false
proposal_allowed: false
proposal_allowed_reason: |
  Framework-integration scaffold + lemmas BB1, BB1'. Honest tier:
  bounded/exact support theorem with named obstruction for tightening to
  a non-trivial beta=6 bound. Independent audit decides effective status.
```

## 11. Cross-references

- A11 source: [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
- A11 Wilson-loop membership/source companion:
  [`GAUGE_OS_STEP1_WILSON_PLAQUETTE_DECOMPOSITION_THETA_INVARIANCE_REFLECTION_HERMITICITY_NARROW_THEOREM_NOTE_2026-06-02.md`](GAUGE_OS_STEP1_WILSON_PLAQUETTE_DECOMPOSITION_THETA_INVARIANCE_REFLECTION_HERMITICITY_NARROW_THEOREM_NOTE_2026-06-02.md)
- Verdict-named obstruction: [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
- Mixed-cumulant onset theorem:
  [`GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
- Sister obstruction: [`GAUGE_VACUUM_PLAQUETTE_FRAMEWORK_POINT_UNDERDETERMINATION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_FRAMEWORK_POINT_UNDERDETERMINATION_NOTE.md)
- Prior campaign block 03 (mean-field saddle stretch): PR [#410](https://github.com/jonathonreilly/cl3-lattice-framework/pull/410), `PLAQUETTE_MINIMAL_BLOCK_SADDLE_STRETCH_NOTE_2026-05-02.md`
- Literature: Anderson-Kruczenski 2017; Kazakov-Zheng [arXiv:2203.11360](https://arxiv.org/abs/2203.11360), [arXiv:2404.16925](https://arxiv.org/abs/2404.16925); JHEP 12(2025) 033 SU(3) bootstrap
- Loop pack: `.claude/science/physics-loops/plaquette-bootstrap-closure-20260503/`
